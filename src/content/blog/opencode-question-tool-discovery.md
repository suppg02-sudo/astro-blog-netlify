---
pubDatetime: 2026-02-08T22:00:00Z
title: "The Missing Question Tool: How We Found OpenCode's Built-in Interactive UI"
postSlug: "opencode-question-tool-discovery"
description: "The Missing Question Tool: How We Found OpenCode's Built-in Interactive UI"
tags:
  - configuration
  - opencode
  - interactive-ui
  - question-tool
  - context7
  - debugging
---

## The Problem

When typing `skill` in OpenCode, the system was supposed to present interactive clickable options — a proper menu where you click your choice instead of typing a number. Instead, every session fell back to plain text numbered lists. The documentation referenced a `question` tool (sometimes called `mcp_question`), audit reports claimed it was "tested and working", but it simply wasn't there.

What followed was a detective story through documentation versions, blog posts, source code, and configuration files.

---

## The Investigation

### Following the Paper Trail

The first clue was in the documentation itself. Three different files referenced the tool with three different names:

| File | Reference | What it said |
|------|-----------|--------------|
| `skillmenu.md` | `question` tool (`mcp_question`) | "Present interactive options" |
| `global-instructions.md` (pre-cleanup) | `mcp_question` (9 mentions) | "Interactive question tool" |
| `skill-trigger-audit-complete.md` | `mcp_question` | "Tested and working ✅" |
| `global-instructions.md` (current) | `question` tool (4 mentions) | "Present options using question tool" |

The audit report from earlier today (February 8, 2026 at 18:31) confidently stated:

> ✅ `mcp_question` tool creates interactive clickable options
> ✅ Interactive mcp_question tool integration
> ✅ Status: Properly documented and functional

But the tool wasn't in the available toolset. Not as `mcp_question`, not as `question`, not as anything.

### The MCP Server Theory

The natural assumption was that `mcp_question` was an MCP server that needed to be installed. We checked:

- `/root/.config/opencode/opencode.json` — no question-related MCP servers
- `npm search mcp-question` — nothing found
- OpenMemory — no records of installation or removal
- All MCP server directories — nothing question-related

Dead end. It wasn't an MCP server.

### Context7 Reveals the Truth

The breakthrough came from querying the OpenCode source code directly via Context7. Searching the `/anomalyco/opencode` repository revealed something unexpected:

```
packages/opencode/src/tool/question.ts    ← The tool implementation
packages/opencode/src/tool/question.txt   ← The tool description
packages/opencode/src/question/index.ts   ← The Question type definitions
packages/opencode/test/tool/question.test.ts ← Tests proving it works
```

**The `question` tool was built into OpenCode all along.** It was never an MCP server. It's a native tool, compiled into the OpenCode binary, sitting at `packages/opencode/src/tool/question.ts`.

---

## What the Source Code Shows

### The Tool Implementation

```typescript
// packages/opencode/src/tool/question.ts
import z from "zod"
import { Tool } from "./tool"
import { Question } from "../question"
import DESCRIPTION from "./question.txt"

export const QuestionTool = Tool.define("question", {
  description: DESCRIPTION,
  parameters: z.object({
    questions: z.array(Question.Info.omit({ custom: true }))
      .describe("Questions to ask"),
  }),
  async execute(params, ctx) {
    const answers = await Question.ask({
      sessionID: ctx.sessionID,
      questions: params.questions,
      tool: ctx.callID 
        ? { messageID: ctx.messageID, callID: ctx.callID } 
        : undefined,
    })
    // Format and return answers...
  },
})
```

### The Schema

```typescript
// packages/opencode/src/question/index.ts
export const Option = z.object({
  label: z.string().describe("Display text (1-5 words, concise)"),
  description: z.string().describe("Explanation of choice"),
})

export const Info = z.object({
  question: z.string().describe("Complete question"),
  header: z.string().describe("Very short label (max 30 chars)"),
  options: z.array(Option).describe("Available choices"),
  multiple: z.boolean().optional()
    .describe("Allow selecting multiple choices"),
  custom: z.boolean().optional()
    .describe("Allow typing a custom answer (default: true)"),
})
```

### The Test

```typescript
// packages/opencode/test/tool/question.test.ts
test("should successfully execute with valid question parameters", async () => {
  const questions = [
    {
      question: "What is your favorite color?",
      header: "Color",
      options: [
        { label: "Red", description: "The color of passion" },
        { label: "Blue", description: "The color of sky" },
      ],
      multiple: false,
    },
  ]
  askSpy.mockResolvedValueOnce([["Red"]])
  const result = await tool.execute({ questions }, ctx)
  expect(result.title).toBe("Asked 1 question")
})
```

The tool exists. It's tested. It works. So why wasn't it available?

---

## The Root Cause

The answer was embarrassingly simple. In OpenCode, tools must be **explicitly enabled** in each agent's configuration. Looking at `opencode.json`:

```json
"openagent": {
  "tools": {
    "write": true,
    "edit": true,
    "bash": true,
    "task": true,
    "skill": true,
    "read": true
    // ← "question" was MISSING
  }
}
```

Every single agent — all 12 of them (3 primary + 9 subagents) — was missing `"question": true` in their tool permissions. The tool existed in the binary but was never enabled in the configuration.

---

## The Fix

### Step 1: Enable the Tool

Added `"question": true` to all 12 agents in `/root/.config/opencode/opencode.json`:

```json
"openagent": {
  "tools": {
    "write": true,
    "edit": true,
    "bash": true,
    "task": true,
    "skill": true,
    "read": true,
    "question": true  // ← Added
  }
}
```

### Step 2: Document the Schema

Updated `skillmenu.md` with the complete question tool reference, including schema, field reference, and examples for each menu level:

**Level 1 — Skill Menu:**
```json
{
  "questions": [{
    "question": "What would you like to do?",
    "header": "Skill Menu",
    "options": [
      { "label": "Load a skill (Recommended)", 
        "description": "Browse and load a skill by category" },
      { "label": "Switch model", 
        "description": "Change AI provider and model" },
      { "label": "List active skills", 
        "description": "Show all skills with status" }
    ],
    "multiple": false
  }]
}
```

**Level 2 — Category Drill-Down:**
```json
{
  "questions": [{
    "question": "Which skill category?",
    "header": "Skill Categories",
    "options": [
      { "label": "Content & Publishing", 
        "description": "hugo, astro, memos, presentation, chartjs" },
      { "label": "AI & Research", 
        "description": "research, news, fabric, smart-search" },
      { "label": "Infrastructure & Ops", 
        "description": "maintenance, databases, dokploy, portainer" }
    ]
  }]
}
```

### Step 3: Update Global Instructions

Added a "Question Tool (Built-in OpenCode Interactive UI)" section to `global-instructions.md` with:
- Complete schema reference
- Field reference table
- Usage rules (recommended options, no catch-all, answer format)
- Practical example
- Fallback guidance for sessions where the tool isn't available

---

## Key Takeaways

### 1. Built-in Tools Need Explicit Enablement

OpenCode's tool system requires each tool to be listed in the agent's `tools` configuration. A tool can exist in the binary but remain invisible to agents if not enabled. This is a security feature — it prevents agents from accessing tools they shouldn't use — but it's easy to miss when setting up new tools.

### 2. Documentation Drift is Real

The `question` tool went through at least three naming conventions:
- `mcp_question` (pre-cleanup documentation)
- `question` tool (`mcp_question`) (skillmenu.md — both names)
- `question` (current global-instructions)

None of these were wrong per se, but the inconsistency made debugging harder. The audit report claiming the tool was "tested and working" was technically correct — the tool *does* work — but it wasn't enabled in the configuration being used.

### 3. Context7 is Invaluable for Source Code Investigation

Without Context7's ability to search the OpenCode repository directly, we would have been stuck guessing. The source code at `packages/opencode/src/tool/question.ts` immediately revealed:
- The tool is built-in (not an MCP server)
- The exact schema and parameters
- How it integrates with the TUI
- That it uses an internal `Question.ask()` API

### 4. Check Tool Permissions Before Assuming Tools Don't Exist

The debugging process went:
1. Tool not in available tools → Must not exist
2. Not an MCP server → Must need to be created
3. Source code shows it exists → Must be disabled
4. Check config → Missing from tool permissions
5. Add to config → Fixed

Step 4 should have been step 1.

---

## Verification

After the fix, all 12 agents now have the question tool enabled:

```
Agent Question Tool Status:
--------------------------------------------------
  ✅ openagent: question=True
  ✅ opencoder: question=True
  ✅ researcher: question=True
  ✅ use-glm-fast: question=True
  ✅ use-gemini-pro: question=True
  ✅ use-gpt5-high: question=True
  ✅ use-gpt5-codex: question=True
  ✅ use-gemini-flash: question=True
  ✅ use-opus-4-6: question=True
  ✅ use-opus-4-5: question=True
  ✅ use-sonnet-4-5: question=True
  ✅ use-haiku-4-5: question=True
--------------------------------------------------
Total: 12/12 agents have question tool enabled
```

The change takes effect on the next session. When you type `skill`, the agent should now render interactive clickable options in the TUI instead of plain text numbered lists.

---

## Files Modified

| File | Change |
|------|--------|
| `/root/.config/opencode/opencode.json` | Added `"question": true` to all 12 agents |
| `/media/docs/instructions/skillmenu.md` | Added Question Tool Reference section with schema, examples |
| `/media/docs/instructions/global-instructions.md` | Added "Question Tool (Built-in OpenCode Interactive UI)" section |

## Investigation Flow

```
User types "skill" → text menu appears (wrong) → 
check memory → check docs output → found audit report claiming "tested" → 
check pre-cleanup version → found mcp_question references → 
Context7 search → found source code → discovered built-in tool → 
checked opencode.json → tool NOT in agent permissions → 
added "question": true to all 12 agents → 
updated documentation → stored to OpenMemory → done
```

---

## References

- OpenCode Question Tool Source: `packages/opencode/src/tool/question.ts`
- Question Schema: `packages/opencode/src/question/index.ts`
- Question Tests: `packages/opencode/test/tool/question.test.ts`
- Tool Description: `packages/opencode/src/tool/question.txt`
- Context7 Library: `/anomalyco/opencode`
- OpenCode Version: v1.1.53

---

*Published: February 8, 2026*
*Investigation Duration: ~45 minutes*
*Root Cause: Missing tool permission in agent configuration*