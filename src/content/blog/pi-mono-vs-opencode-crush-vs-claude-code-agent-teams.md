---
pubDatetime: 2026-03-30T18:00:00Z
title: "Pi Mono vs OpenCode/Crush vs Claude Code: Building Advanced Custom Agent Team Harnesses"
postSlug: "pi-mono-vs-opencode-crush-vs-claude-code-agent-teams"
description: "Three powerful approaches to AI coding agents with team orchestration. Compare Pi Mono's extensibility, Claude Code's enterprise infrastructure, and Crush's polished terminal UX."
tags:
  - pi-mono
  - ai-agents
  - llm
  - coding-assistants
  - claude-code
  - crush
---

# Pi Mono vs OpenCode/Crush vs Claude Code: Building Advanced Custom Agent Team Harnesses

> **TL;DR**: Three powerful approaches to AI coding agents with team orchestration. Pi Mono offers maximum extensibility via TypeScript, Claude Code provides enterprise-grade infrastructure with Agent SDK, and Crush (formerly OpenCode) delivers polished terminal UX with MCP integration. Choose based on your customization needs and infrastructure requirements.

## Quick Summary

| Framework | Best For | Extension Model | Multi-Agent |
|-----------|----------|-----------------|-------------|
| **Pi Mono** | Maximum customization, TypeScript-first | Extensions, Skills, Packages | Via extensions |
| **Claude Code** | Enterprise workflows, production systems | Agent SDK, Skills, Hooks | Built-in subagents |
| **Crush** | Polished terminal experience, MCP ecosystem | MCP servers, Skills, Themes | Not built-in |

---

## The Landscape: Why Custom Agent Teams Matter

As AI coding assistants mature, the one-size-fits-all approach is giving way to specialized agent teams. Instead of a single AI handling everything, modern workflows orchestrate multiple agents—each with specific capabilities, context, and tools.

This comparison examines three leading frameworks for building these advanced agent harnesses:

1. **Pi Mono** - A TypeScript-first toolkit with aggressive extensibility
2. **Claude Code** - Anthropic's official CLI with enterprise-grade infrastructure
3. **Crush** (formerly OpenCode) - Charmbracelet's polished terminal agent

---

## Pi Mono: Maximum Extensibility

### Philosophy: "Adapt pi to your workflows, not the other way around"

Pi Mono (29.3k GitHub stars) takes an opinionated stance: the core should be minimal, and everything else should be an extension. This philosophy enables unprecedented customization without forking.

### Core Architecture

```
@mariozechner/pi-ai           → Unified LLM API (OpenAI, Anthropic, Google, etc.)
@mariozechner/pi-agent-core   → Agent runtime with tool execution
@mariozechner/pi-coding-agent → Interactive CLI
@mariozechner/pi-tui          → Terminal UI components
@mariozechner/pi-web-ui       → Web chat interfaces
@mariozechner/pi-pods         → vLLM deployment management
```

### Extension System

Pi's extension API is remarkably powerful:

```typescript
export default function (pi: ExtensionAPI) {
  // Register custom tools
  pi.registerTool({
    name: "deploy",
    description: "Deploy to staging",
    parameters: Type.Object({ env: Type.String() }),
    execute: async (id, params, signal, onUpdate) => {
      // Custom deployment logic
    }
  });

  // Register commands
  pi.registerCommand("stats", { ... });

  // Hook into events
  pi.on("tool_call", async (event, ctx) => { ... });

  // Replace UI components
  pi.replaceEditor(customEditorComponent);
}
```

### What's Possible with Extensions

- **Sub-agents and plan mode** - Build your own orchestration
- **Custom compaction strategies** - Control context management
- **Permission gates** - Implement security policies
- **Custom UI components** - Status lines, headers, footers
- **MCP server integration** - Add Model Context Protocol support
- **Games while waiting** - Yes, Doom runs in the terminal

### Pi Packages: Shareable Customization

Bundle extensions, skills, prompts, and themes as npm packages:

```bash
pi install npm:@foo/pi-tools
pi install git:github.com/user/repo@v1
```

### Agent Team Harness Pattern

Since Pi doesn't include built-in subagents, you build them:

```typescript
// extension.ts - Multi-agent orchestration
export default function (pi: ExtensionAPI) {
  pi.registerTool({
    name: "spawn_agent",
    description: "Spawn a specialized sub-agent",
    execute: async (id, params) => {
      // Create new agent with specific tools/context
      const specialist = new Agent({
        initialState: {
          systemPrompt: params.rolePrompt,
          tools: getToolsForRole(params.role),
          model: getModel("anthropic", "claude-sonnet-4")
        }
      });
      
      const result = await specialist.prompt(params.task);
      return { content: [{ type: "text", text: result }] };
    }
  });
}
```

### SDK for Embedding

```typescript
import { createAgentSession } from "@mariozechner/pi-coding-agent";

const { session } = await createAgentSession({
  sessionManager: SessionManager.inMemory(),
  authStorage: AuthStorage.create(),
  modelRegistry: ModelRegistry.create()
});

await session.prompt("Analyze this codebase");
```

### RPC Mode for Non-Node Integration

```bash
pi --mode rpc  # JSONL over stdin/stdout
```

### Key Trade-offs

| Pro | Con |
|-----|-----|
| Maximum flexibility | Must build orchestration yourself |
| TypeScript-native | Steeper learning curve |
| No MCP lock-in | Smaller ecosystem than Claude Code |
| Pi packages shareable | Requires security review of third-party code |

---

## Claude Code: Enterprise-Grade Infrastructure

### Philosophy: "Production-ready from day one"

Claude Code is Anthropic's official CLI, available across terminal, VS Code, JetBrains, desktop, and web. It emphasizes reliability, multi-surface support, and enterprise integrations.

### Multi-Surface Architecture

| Surface | Use Case |
|---------|----------|
| **Terminal CLI** | Full-featured coding in terminal |
| **VS Code** | Inline diffs, @-mentions, plan review |
| **JetBrains** | IntelliJ, PyCharm, WebStorm integration |
| **Desktop** | Visual diffs, scheduled tasks |
| **Web/iOS** | Remote sessions, long-running tasks |

### Agent SDK: Build Custom Agents

```typescript
import { Agent } from "@anthropic/agent-sdk";

const agent = new Agent({
  model: "claude-sonnet-4",
  tools: [readFile, writeFile, executeBash],
  systemPrompt: "You are a code reviewer..."
});

const result = await agent.run("Review PR #123");
```

### Sub-Agents: Built-In Orchestration

Claude Code includes native subagent support:

```
User: "Implement auth across frontend and backend"

Lead Agent:
├── Spawn frontend-agent → Handle React components
├── Spawn backend-agent → Build API endpoints
├── Spawn test-agent → Write integration tests
└── Merge results → Create cohesive PR
```

### Skills: Reusable Workflows

```markdown
<!-- ~/.claude/skills/code-review/SKILL.md -->
# Code Review Skill
Use this skill when reviewing pull requests.

## Steps
1. Fetch PR diff
2. Analyze changes for bugs, security issues
3. Check test coverage
4. Generate review comments
```

### CLAUDE.md: Persistent Instructions

```markdown
<!-- CLAUDE.md in project root -->
# Project Instructions

## Build Commands
- `npm run build` - Production build
- `npm test` - Run test suite

## Code Style
- Use TypeScript strict mode
- Prefer functional components
- Follow existing patterns
```

### Hooks: Automation Points

```bash
# ~/.claude/hooks/post-edit.sh
#!/bin/bash
# Auto-format after every edit
npx prettier --write "$1"
```

### MCP Integration

```json
{
  "mcpServers": {
    "github": {
      "command": "mcp-server-github",
      "env": { "GITHUB_TOKEN": "..." }
    },
    "jira": {
      "url": "https://company.atlassian.net/mcp"
    }
  }
}
```

### Scheduled Tasks

```bash
# Cloud scheduled tasks (run when computer is off)
/schedule "Review overnight CI failures" --daily 09:00

# Desktop scheduled tasks (local execution)
/schedule "Update dependencies" --weekly monday
```

### Key Trade-offs

| Pro | Con |
|-----|-----|
| Built-in subagents | Less low-level control |
| Enterprise support | Anthropic model lock-in for some features |
| Multi-surface | Heavier infrastructure |
| Native MCP support | Subscription required for full features |

---

## Crush (OpenCode): Polished Terminal Experience

### Philosophy: "Glamourous agentic coding for all"

Crush (22.2k stars) emerged from the OpenCode project when the original author joined Charmbracelet. It emphasizes beautiful terminal UX and industrial-grade reliability.

### Installation

```bash
# Homebrew
brew install charmbracelet/tap/crush

# NPM
npm install -g @charmland/crush

# Go
go install github.com/charmbracelet/crush@latest
```

### Multi-Model Support

```bash
# Switch models mid-session
crush --model claude-sonnet-4
crush --model gpt-4o
crush --model gemini-2.5-pro

# Model cycling
crush --models "claude-*,gpt-4o"
```

### Configuration

```json
{
  "providers": {
    "anthropic": { "api_key": "$ANTHROPIC_API_KEY" },
    "openai": { "api_key": "$OPENAI_API_KEY" }
  },
  "lsp": {
    "go": { "command": "gopls" },
    "typescript": { "command": "typescript-language-server" }
  },
  "mcp": {
    "filesystem": {
      "type": "stdio",
      "command": "node",
      "args": ["/path/to/mcp-server.js"]
    }
  }
}
```

### LSP Integration

Crush uses Language Server Protocol for code intelligence:

- Diagnostics (errors, warnings)
- Multi-language support
- Automatic file watching

### MCP Support

Three transport types:
- `stdio` - Command-line servers
- `http` - HTTP endpoints
- `sse` - Server-Sent Events

### Agent Skills Standard

Crush implements the [Agent Skills](https://agentskills.io) open standard:

```markdown
<!-- ~/.config/crush/skills/review/SKILL.md -->
# Code Review
Use when reviewing pull requests.
```

### Key Trade-offs

| Pro | Con |
|-----|-----|
| Beautiful TUI | No built-in subagents |
| MCP ecosystem | Less enterprise features |
| Multi-provider | Smaller community than Claude Code |
| LSP integration | No Agent SDK |

---

## Comparison Matrix

### Agent Team Capabilities

| Feature | Pi Mono | Claude Code | Crush |
|---------|---------|-------------|-------|
| **Built-in subagents** | ❌ | ✅ | ❌ |
| **Custom agent SDK** | ✅ | ✅ | ❌ |
| **Extension system** | ✅ (TS) | ✅ (Hooks) | ✅ (MCP) |
| **Skills support** | ✅ | ✅ | ✅ |
| **MCP integration** | Via extension | ✅ Native | ✅ Native |
| **Multi-surface** | CLI, SDK, RPC | CLI, IDE, Web, Desktop | CLI |
| **Session branching** | ✅ | ❌ | ✅ |

### Developer Experience

| Aspect | Pi Mono | Claude Code | Crush |
|--------|---------|-------------|-------|
| **Setup complexity** | Medium | Low | Low |
| **Customization depth** | Maximum | High | Medium |
| **Documentation** | Good | Excellent | Good |
| **Community** | Growing | Large | Active |
| **Enterprise support** | Community | Official | Community |

### Infrastructure

| Requirement | Pi Mono | Claude Code | Crush |
|-------------|---------|-------------|-------|
| **Self-hosted** | ✅ | ❌ | ✅ |
| **Air-gapped** | Via extension | ❌ | ✅ |
| **Subscription** | No | Required | No |
| **Model flexibility** | 20+ providers | Anthropic + others | 15+ providers |

---

## When to Choose Each

### Choose Pi Mono If:

- You need **maximum customization**
- Your team is **TypeScript-proficient**
- You want to **embed agents** in your own applications
- You need **RPC integration** for non-Node systems
- You prefer **building over configuring**

### Choose Claude Code If:

- You need **enterprise support** and reliability
- **Subagents** are core to your workflow
- You work across **multiple surfaces** (terminal, IDE, web)
- **MCP integration** is important
- You want **scheduled tasks** and automation

### Choose Crush If:

- You value **beautiful terminal UX**
- You want **LSP integration** for code intelligence
- You prefer **MCP ecosystem** for extensions
- You need **multi-provider flexibility** without subscriptions
- You like **Charmbracelet tools** (Bubble Tea, etc.)

---

## Building an Agent Team Harness: Patterns

### Pattern 1: Role-Based Specialists (Pi Mono)

```typescript
const roles = {
  architect: {
    systemPrompt: "You design system architecture...",
    tools: [read, grep, find],
    model: "claude-opus-4"
  },
  implementer: {
    systemPrompt: "You write production code...",
    tools: [read, write, edit, bash],
    model: "claude-sonnet-4"
  },
  reviewer: {
    systemPrompt: "You review code for quality...",
    tools: [read, grep, diagnostics],
    model: "claude-sonnet-4"
  }
};

async function orchestrateFeature(spec: string) {
  const design = await architectAgent.prompt(`Design: ${spec}`);
  const code = await implementerAgent.prompt(`Implement: ${design}`);
  const review = await reviewerAgent.prompt(`Review: ${code}`);
  return { design, code, review };
}
```

### Pattern 2: Parallel Execution (Claude Code)

```
User: "Migrate this module to TypeScript"

Lead Agent spawns:
├── types-agent → Generate type definitions
├── convert-agent → Convert JS to TS
├── test-agent → Update tests
└── Merge → Create unified PR
```

### Pattern 3: Pipeline Orchestration (Pi Mono SDK)

```typescript
const pipeline = new AgentPipeline()
  .stage("analyze", analyzerAgent)
  .stage("plan", plannerAgent)
  .stage("implement", coderAgent)
  .stage("test", testerAgent)
  .stage("review", reviewerAgent);

await pipeline.run("Add user authentication");
```

---

## Conclusion

The choice between Pi Mono, Claude Code, and Crush depends on your priorities:

| Priority | Recommendation |
|----------|----------------|
| **Maximum control** | Pi Mono |
| **Enterprise reliability** | Claude Code |
| **Beautiful UX** | Crush |
| **Multi-surface support** | Claude Code |
| **Embeddable agents** | Pi Mono |
| **MCP ecosystem** | Claude Code or Crush |

For **advanced custom agent team harnesses**, Pi Mono offers the most flexibility but requires more investment. Claude Code provides the most complete out-of-the-box experience with native subagent support. Crush delivers the best terminal experience with MCP integration.

The future of AI coding is multi-agent. These three frameworks represent different philosophies for getting there. Choose based on your team's skills, infrastructure requirements, and customization needs.

---

**Tags**: ai-agents, llm, coding-assistants, pi-mono, claude-code, crush, agent-orchestration
**Categories**: AI Automation, Technical Deep-Dives