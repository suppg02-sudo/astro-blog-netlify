---
pubDatetime: 2026-01-25T00:57:00Z
title: "Flow Documentation Protocol - Complete Transparency for Task Execution"
postSlug: "flow-documentation-protocol-complete-transparency-for-task-execution"
description: "Flow Documentation Protocol - Complete Transparency for Task Execution"
tags:
  - skills
  - task-management
  - protocol
  - documentation
  - delegation
---

## Overview

I've updated global instructions with a comprehensive **"flow" trigger** mechanism. This provides complete transparency into the entire request execution chain whenever you say "flow".

## What's New

### Trigger Word: "flow"

When you say **"flow"**, you'll now receive:

1. **Decision-Making Process**: How requests are classified and routed
2. **Agent Selection**: Which subagents are chosen and why
3. **Skill Discovery**: How available skills are evaluated and selected
4. **Execution Flow**: How tasks are delegated and completed
5. **Issues Encountered**: What problems occurred and how they were resolved
6. **Session Management**: How background tasks are managed and canceled

### Flow Output Format

```
FLOW DIAGRAM:

[Step 1] User Request: "<original request text>"
  ├─ Classification: <task type>
  ├─ Complexity: <simple/medium/complex>
  └─ Decision: <direct tools vs delegation>

[Step 2] Approach Selection:
  ├─ Chosen Path: <direct execution | delegate_task | parallel agents>
  └─ Rationale: <why this approach was selected>

[Step 3] <if delegation> Agent Selection:
  ├─ Category: <visual-engineering|ultrabrain|quick|artistry|unspecified-low|unspecified-high|writing>
  └─ Subagent Type: <explore|librarian|oracle|frontend-ui-ux|hugo-specialist|etc.>

[Step 4] <if delegation> Skill Selection:
  ├─ Skills Evaluated: <list of ALL available skills checked>
  ├─ Skills Selected: <final list with reasons>
  └─ Skills Omitted: <if any, with justification per MANDATORY protocol>

[Step 5] <if delegation> Delegation Execution:
  ├─ Session ID: <ses_XXXXXXXXXXXXXXXX>
  ├─ Run Mode: <background|foreground>
  └─ Final Outcome: <success|failure|partial>

[Step 6] <if applicable> Follow-up Actions:
  ├─ Verification Steps: <what was done to verify results>
  └─ Additional Work: <any extra tasks completed>
```

## Why This Matters

Subagents are **stateless** - they only know what you tell them. This new protocol forces:

- ✅ **Reading skill descriptions** before choosing
- ✅ **Evaluating ALL available skills** systematically
- ✅ **Documenting decisions** with clear justifications
- ✅ **Preventing lazy omissions** of potentially useful skills

This improves:

- **Debugging**: Complete visibility into decision-making
- **Decision Quality**: Systematic skill selection process
- **Future Improvement**: Learning from documented issues and patterns

## Skill Discovery & Selection Protocol

This is now **MANDATORY** for every `delegate_task` call.

### Available Skills

| Skill | Domain | Best For |
|--------|---------|-----------|
| `playwright` | Browser-related tasks (testing, scraping, screenshots) | Any browser interaction, web verification |
| `frontend-ui-ux` | Designer-turned-developer UI/UX | Frontend, design, styling, animation |
| `git-master` | Git operations (commit, rebase, squash, search) | ANY git commands or operations |

### Mandatory Evaluation Format

For EACH skill available, I must answer:

```
SKILL EVALUATION for "[skill-name]":
- Skill domain: [what the skill description says]
- Task domain: [what the task is about]
- Decision: INCLUDE or OMIT
- Reason: [if INCLUDING - why matches; if OMITTING - specific explanation of why domains don't overlap]
```

### Mandatory Justification for Omissions

If I choose NOT to include a skill that MIGHT be relevant, I MUST provide justification:

```
SKILL EVALUATION for "[skill-name]":
- Skill domain: [what the skill description says]
- Task domain: [what the task is about]
- Decision: OMIT
- Reason: [specific explanation of why domains don't overlap]
```

### Example: Correct Skill Selection

**Task**: "Build a React component with beautiful UI"

```
Skill Evaluation:

SKILL EVALUATION for "playwright":
- Skill domain: MUST USE for any browser-related tasks
- Task domain: Frontend development, UI components
- Decision: OMIT
- Reason: Task is about building React components, not browser automation/testing. No browser interactions required.

SKILL EVALUATION for "frontend-ui-ux":
- Skill domain: Designer-turned-developer who crafts stunning UI/UX even without design mockups
- Task domain: Frontend, UI/UX design, styling
- Decision: INCLUDE
- Reason: Task requires UI/UX design and styling work - this is exactly what the skill specializes in.

SKILL EVALUATION for "git-master":
- Skill domain: MUST USE for ANY git operations
- Task domain: Frontend development
- Decision: OMIT
- Reason: Task is about building a React component, not git operations. No git commands needed.

Final Selection: load_skills=["frontend-ui-ux"]
```

## Category Selection Protocol

### Step 1: Select Category

Choose ONE category whose domain BEST fits your task.

| Category | Domain / Best For |
|----------|-------------------|
| `visual-engineering` | Frontend, UI/UX, design, styling, animation |
| `ultrabrain` | Deep logical reasoning, complex architecture decisions |
| `artistry` | Highly creative/artistic tasks, novel ideas |
| `quick` | Trivial tasks - single file changes, typo fixes |
| `unspecified-low` | Tasks that don't fit other categories, low effort |
| `unspecified-high` | Tasks that don't fit other categories, high effort |
| `writing` | Documentation, prose, technical writing |

**Note**: Focus on domain expertise, not effort level.

### Step 2: Evaluate ALL Skills

For EVERY skill available, apply the mandatory evaluation format.

### Step 3: Final Selection

Provide the category, selected skills, and complete 6-section prompt structure.

## Common Issues & Solutions

### Skill-Related Issues

| Issue | Solution |
|--------|-------------|
| Empty skills without justification | Always evaluate and document ALL skills per mandatory protocol |
| Missing domain overlap | Read skill descriptions more carefully - if overlap exists, explain why omitted |
| Category mismatch | Focus on domain expertise, not effort level when choosing category |

### Delegation-Related Issues

| Issue | Solution |
|--------|-------------|
| Background tasks not collected | Always use `background_output()` before final answer |
| Session not resumed | Store session_id and always resume for follow-ups |
| Orphaned background tasks | Always call `background_cancel(all=true)` at end of task |

### Interruption & Trigger Issues

| Issue | Solution |
|--------|-------------|
| User interrupts with new request | Use background_cancel, acknowledge interruption, note state |
| Tool timeout | Check timeout, adjust strategy, inform user |
| Background task failure | Check `background_output()` for errors, retry if needed |
| Rate limiting | Wait and retry, or use alternative approach |

## Documentation Reference

The complete flow documentation protocol has been added to:

- **File**: `/media/docs/instructions/global-instructions.md`
- **Section**: `PART 4: Flow Documentation & Skill Discovery Protocol`

### Quick Reference: Say "flow" to See

Whenever you want complete transparency into how a request was handled, just say:

```
flow
```

And you'll get complete execution breakdown including:

- Skill discovery and selection
- Agent delegation decisions
- Issues encountered and solutions
- Session management details

This makes complex multi-agent workflows completely transparent and debuggable.

## Summary

The **"flow"** trigger now provides:

✅ **Complete Transparency**: Every decision documented
✅ **Skill Discovery**: Systematic evaluation of all skills
✅ **Issue Tracking**: Problems and solutions documented
✅ **Session Management**: Clear tracking of delegations
✅ **Reference Links**: URL access to all generated documents

This improves debugging, decision-making quality, and future task delegation effectiveness.