---
pubDatetime: 2026-02-13T09:15:00Z
title: "DeepWiki: OpenCode Permission and Question System Architecture"
postSlug: "deepwiki-opencode-permission-question-system"
description: "DeepWiki: OpenCode Permission and Question System Architecture"
tags:
  - opencode
  - technical-deep-dive
  - architecture
  - developer
---

## Overview

DeepWiki provides comprehensive technical documentation for OpenCode's permission and question systems. This is **the definitive reference** for understanding how these systems work internally and integrate with the broader OpenCode platform.

## Architecture Overview

Both systems implement an **asynchronous request/reply pattern** where tool execution pauses until the user responds through HTTP API or UI components.

### Request/Reply Flow

```
Tool Call → System.ask() → State.pending → Event Published
                                            ↓
                                       User Responds
                                            ↓
                                    System.reply() → Promise Resolved
```

## Permission System

The Permission System controls tool execution authorization through an `allow`/`ask`/`deny` model.

### How It Works

`PermissionNext.evaluate()` matches tool requests against configured rules with hierarchical precedence:

1. **Agent rules** (`agent.permission`) - checked first
2. **Session rules** (`session.permission`) - checked second
3. **Default** - if no matches, returns `"ask"`

### Permission Evaluation Logic

Uses `picomatch()` for glob pattern matching:

```
Pattern         Implementation          Matches
*               picomatch("*")          All values
*.ts            picomatch("*.ts")       Files ending in .ts
src/**          picomatch("src/**")     All paths under src/
{a,b}           picomatch("{a,b}")     Either a or b
```

### Three-Level Response Actions

When `PermissionNext.evaluate()` returns `"ask"`:

1. **Once** - Approve single request, don't modify config
2. **Always** - Approve and add allow rule to agent config
3. **Reject** - Deny request, reject promise with error

### Configuration Examples

**Global Configuration** (`opencode.json`):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "bash": "allow",
    "edit": "deny",
    "webfetch": "ask",
    "mcp_*": "ask"
  }
}
```

**Agent-Level Configuration**:

```json
{
  "agents": {
    "my-agent": {
      "permission": {
        "bash": "deny",
        "edit": "allow"
      }
    }
  }
}
```

## Question System

The Question System enables agents to request structured user input via the `question` tool.

### Data Structures

Question system uses Zod schemas for type safety:

```typescript
// Option within a question
Question.Option = z.object({
  label: z.string(),
  description: z.string()
})

// A single question
Question.Info = z.object({
  question: z.string(),
  header: z.string().max(30),
  options: z.array(Question.Option),
  multiple: z.boolean().optional(),
  custom: z.boolean().optional()
})

// User's answer (array of selected labels)
Question.Answer = z.string().array()

// Full request sent to user
Question.Request = z.object({
  id: z.string(),
  sessionID: z.string(),
  questions: z.array(Question.Info),
  tool: z.object({...}).optional()
})
```

### Request/Reply Sequence

When an agent calls the question tool:

```
Question.ask() → Creates Promise in state.pending
                 Publishes "question.asked" event
                 ↓
            User Selects Options
                 ↓
            Question.reply() OR Question.reject()
                 ↓
            Promise Resolved/Rejected
            Publishes "question.replied" or "question.rejected"
            Removes from state.pending
```

### State Lifecycle

| State | Location | Condition |
|-------|----------|-----------|
| Created | `Question.state.pending[id]` | `{info, resolve, reject}` |
| Stored | `Question.state.pending` | Promise added to pending map |
| Resolved | `Question.reply()` called | Calls `pending[id].resolve()` |
| Rejected | `Question.reject()` called | Calls `pending[id].reject()` |
| Cleaned | After resolve/reject | `delete state.pending[id]` |

## Event Broadcasting

Both systems publish events via `Bus.publish()` to notify clients about state changes. Events stream over SSE endpoints (`/event`, `/global/event`).

### Permission Events

| Event | Trigger | Payload |
|-------|---------|---------|
| `permission.asked` | `PermissionNext.ask()` | `PermissionRequest` |
| `permission.replied` | `PermissionNext.reply()` | `{sessionID, requestID, reply}` |

### Question Events

| Event | Trigger | Payload |
|-------|---------|---------|
| `question.asked` | `Question.ask()` | `QuestionRequest` |
| `question.replied` | `Question.reply()` | `{sessionID, requestID, answers}` |
| `question.rejected` | `Question.reject()` | `{sessionID, requestID}` |

## HTTP API Routes

Both systems expose REST endpoints for client integration:

### Permission API

```
GET  /permission                      - List pending requests
POST /permission/:requestID/reply     - Approve/deny request
```

**Reply body options**:
```json
{ "reply": "once" }      // Approve single request only
{ "reply": "always" }    // Approve and update config
{ "reply": "reject" }    // Deny request
```

### Question API

```
GET  /question                        - List pending questions
POST /question/:requestID/reply       - Submit answers
POST /question/:requestID/reject      - Dismiss question
```

**Reply body**:
```json
{ "answers": [["Option 1", "Option 2"], ["Option 3"]] }
```

(Array of answer arrays, one array per question)

## UI Components

The TUI provides interactive components for both systems.

### PermissionPrompt

Renders pending permission requests with three action buttons:

**Displayed Information**:
- `permission` - Tool name (e.g., `"edit"`, `"bash"`)
- `patterns` - File paths or glob patterns
- `metadata` - Additional context
- `tool.messageID` - Link to triggering assistant message

**Actions**:
- **Once** - Approve single request
- **Always** - Approve and add rule to config
- **Reject** - Deny request

### QuestionPrompt

Multi-tab interface with:

**Features**:
- Single/multi-select modes
- Tab navigation between questions
- Custom text input (when `custom: true`)
- Confirmation screen before submission
- Keyboard navigation (h/j/k/l arrows)

**Keyboard Bindings**:
```
h, left   → Previous question tab
l, right  → Next question tab
j, down   → Next option
k, up     → Previous option
enter     → Toggle/Select/Submit
escape    → Dismiss or exit custom input
```

## SDK Client Integration

The `@opencode-ai/sdk` provides TypeScript clients for integration:

### Permission Client

```typescript
// List pending permission requests
const requests = await opencode.permission.list();

// Approve request
await opencode.permission.reply({ 
  requestID: "req-123",
  reply: "always"  // "once", "always", or "reject"
});
```

### Question Client

```typescript
// List pending questions
const questions = await opencode.question.list();

// Submit answers
await opencode.question.reply({
  requestID: "q-123",
  answers: [["React"], ["Tailwind"]]  // Array of answers
});

// Reject question
await opencode.question.reject({
  requestID: "q-123"
});
```

## Error Handling

Both systems define error types for request rejections:

### Permission Errors

When a user rejects a permission or permission evaluates to `"deny"`:

```typescript
class PermissionDeniedError extends Error {
  name = "PermissionDeniedError"
  tool: string
  patterns: string[]
}
```

### Question Errors

When a user rejects a question:

```typescript
class RejectedError extends Error {
  name = "RejectedError"
  message = "Question was rejected by user"
}
```

## Key Architectural Insights

### Promise-Based Coordination

Both systems use promises stored in `state.pending` to coordinate between:
- **Server**: Tool execution
- **Client**: User interaction
- **Events**: State synchronization

This enables elegant async coordination without callbacks or polling.

### Event-Driven Architecture

Events published to `Bus` allow multiple clients (TUI, web, IDE) to react to permission/question state changes without tight coupling.

### Hierarchical Precedence

Permission system's three-level precedence (agent > session > global) allows:
- **Global defaults** - Organization-wide policies
- **Session overrides** - Per-session adjustments
- **Agent policies** - Agent-specific rules

This provides flexibility while maintaining security.

### Pattern Matching

Using `picomatch()` for glob patterns enables flexible rules:

```json
{
  "permission": {
    "bash": "deny",
    "edit": "ask",
    "src/**": "allow",
    "node_modules/*": "deny"
  }
}
```

## Conclusion

DeepWiki's documentation reveals OpenCode's permission and question systems as well-architected, promise-based coordination mechanisms that enable:

- **Structured user interaction** (question tool)
- **Tool execution control** (permission system)
- **Event-driven coordination** across clients
- **Flexible policy configuration** with glob patterns
- **Extensible architecture** supporting multiple UIs and clients

Understanding these systems is essential for building custom agents, policies, and integrations with OpenCode.

---

**Source**: [DeepWiki - Permission and Question System](https://deepwiki.com/sst/opencode/2.5-permission-and-question-system)