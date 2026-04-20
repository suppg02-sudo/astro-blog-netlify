---
pubDatetime: 2026-01-24T21:52:45Z
title: "Fixing Workflow: Standardizing on Hugo Agent Over MCP Tools"
postSlug: "fixing-workflow-standardizing-on-hugo-agent-over-mcp-tools"
description: "Fixing Workflow: Standardizing on Hugo Agent Over MCP Tools"
tags:
  - Hugo
  - Documentation
  - Workflow
  - Agents
  - TELOS
---

## Executive Summary

Updated global agent configuration to standardize Hugo operations through delegation to Hugo Specialist Agent instead of direct MCP tool access. This change eliminates ambiguity, creates a consistent workflow, and aligns with TELOS principles of explicit tool usage and deterministic processes.

## The Problem

When the Oracle agent was tasked with creating a blog post, it attempted to load a non-existent Hugo skill:

```
Error: Skill "hugo" not found. Available skills: playwright, frontend-ui-ux, git-master
```

This happened because the system has **two ways** to interact with Hugo:
1. **Hugo MCP tools** (`hugo-mcp_*`) - Direct tool access
2. **Hugo Specialist Agent** (`hugo-specialist`) - Delegation-based agent

The documentation didn't explicitly state which method to use, leading to **ambiguous tool selection**.

## What Changed

### Updated `/root/.config/opencode/agents.md`

**1. Specialist Agent Table Enhancement**
Added "How to Invoke" column with explicit instructions:

| Agent | Description | How to Invoke |
|-------|-------------|---------------|
| **Hugo Specialist** | Hugo static site management, theme expertise, Mermaid diagrams, blog posts | `delegate_task(subagent_type="hugo-specialist", ...)` - **DO NOT use Hugo MCP tools directly** |

**2. Trigger Word Protocol Update**
Changed "blog post" trigger from:
```
OLD: Automatically load Hugo skill via `skill load hugo` for site and content management
NEW: Delegate to Hugo specialist agent via `delegate_task(subagent_type="hugo-specialist", ...)`
      DO NOT use Hugo MCP tools directly
```

## Why This Change

### User Preference
**Primary reason**: User prefers using agents (delegation model) over direct MCP tool access.

### Operational Consistency
- **Single source of truth**: All Hugo operations go through Hugo Specialist Agent
- **Context preservation**: Agent maintains session state across operations
- **Simplified workflow**: No need to choose between agent vs. MCP tools

### Reduced Complexity
- Removes decision point from agent reasoning: "Should I delegate or use MCP tools?"
- Makes operations deterministic - always delegate
- Reduces cognitive load on AI models

## Benefits

### 1. Consistency ✅
All Hugo site operations follow the same path:
- Blog post creation → Delegate to hugo-specialist
- Site building → Delegate to hugo-specialist
- Theme management → Delegate to hugo-specialist

No mix of agent delegation and direct MCP tool calls.

### 2. Context-Awareness ✅
Hugo Specialist Agent:
- Maintains session state across operations
- Knows project-specific configurations (site path, base URL)
- Carries context between related tasks

Example workflow:
```
1. "Create blog post" → hugo-specialist creates post
2. "Add Mermaid diagram" → hugo-specialist knows where post is
3. "Build site" → hugo-specialist uses correct configuration
```

### 3. Deterministic Workflows ✅
Clear protocol eliminates ambiguity:

| Situation | Action (Before) | Action (After) |
|-----------|-------------------|-----------------|
| Create blog post | Try `skill load hugo` → fail | Delegate to hugo-specialist → success |
| Manage content | Maybe use MCP tools | Always use hugo-specialist |
| Hugo operations | Unclear path | Clear: delegate to agent |

**TELOS Principle (Lines 36-40)**: "Prefer deterministic workflows where outcomes are predictable"

### 4. Maintainability ✅
**Single point of evolution**: All Hugo workflow improvements go to Hugo Specialist Agent

- Skills evolve in one place: `/root/.config/opencode/agent/hugo-specialist.md`
- No need to update multiple protocols (agent + MCP tools)
- Agent can improve its own procedures over time

### 5. Local Model Instruction Design ✅
Clear instructions reduce local model reasoning overhead:

```
Task: "Create Hugo blog post"
Before (implicit): Model must discover hugo-specialist exists, infer it's better than MCP tools
After (explicit): Documented as "delegate_task(subagent_type='hugo-specialist', ...)"
→ Local model can execute without searching/scanning
```

**TELOS Principle (Lines 161-229)**: "Create instructions so clear and deterministic that smaller open-source models can execute tasks correctly"

## Technical Implementation Details

### File Changes
- **Modified**: `/root/.config/opencode/agents.md`
- **Lines Updated**: 27 (Specialist Agent table), 313 ("blog post" trigger)
- **Type**: Documentation-only enhancement

### Protocol Changes
**Before**:
```
User: "Create a blog post"
→ Agent tries: skill load hugo
→ Error: Skill not found
→ Fallback: Use Hugo MCP tools (if available)
```

**After**:
```
User: "Create a blog post"
→ Agent delegates: delegate_task(subagent_type="hugo-specialist", prompt="Create blog post...")
→ Hugo Specialist Agent: Creates post using its internal knowledge
→ Result: Consistent, successful operation
```

### No Breaking Changes
- Existing Hugo MCP tools still available if needed
- Documentation-only update
- Backward compatible with current system

## TELOS Constitution Alignment

### 1. Explicit Tool Usage ✅
**TELOS Design Principle #1** (Lines 167): "Always specify exact tool names, parameters, and expected outputs"

This change provides:
- Exact invocation pattern: `delegate_task(subagent_type="hugo-specialist", ...)`
- Clear prohibition: "DO NOT use Hugo MCP tools directly"
- No ambiguity about which approach to use

### 2. Deterministic Workflows ✅
**TELOS Principle** (Lines 36-40): "Prefer deterministic workflows where outcomes are predictable"

- Hugo operations now have a single, predictable path
- Agent selection is a lookup operation, not reasoning task
- Outcomes are consistent across sessions

### 3. Local Model Support ✅
**TELOS Goal** (Lines 161-163): "Instructions so clear and deterministic that smaller open-source models can execute tasks correctly"

Clear protocols enable:
- GLM-4.7 Flash to execute Hugo tasks via delegation
- Reduced reasoning overhead through explicit instructions
- Reliable task completion without complex tool discovery

## Bottom Line

This small documentation fix eliminates a major source of workflow ambiguity:

**Before**: Agents had to choose between Hugo MCP tools or Hugo Specialist Agent → inconsistent behavior, errors

**After**: Always delegate to Hugo Specialist Agent → consistent, deterministic operations

**TELOS Alignment**:
- ✅ Explicit tool usage
- ✅ Deterministic workflows
- ✅ Support for local models
- ✅ Single point of evolution
- ✅ Context preservation

The system now follows the user's preferred workflow: **delegate to agents, don't use tools directly**.

---

*Published: 2026-01-24*
*Tags: TELOS, Documentation, Hugo, Workflow, Agents*