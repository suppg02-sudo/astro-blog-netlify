---
pubDatetime: 2026-03-22T19:12:46Z
title: "Meta-Skills in OpenCode: Understanding Skill Architecture"
postSlug: "meta-skills-opencode-skill-architecture"
description: "Meta-Skills in OpenCode: Understanding Skill Architecture"
tags:
  - skills
  - opencode
  - ai-agents
  - meta-skills
  - architecture
---

Building a robust skill system for AI agents requires understanding the distinction between regular skills and meta-skills. This post explores when to create meta-skills versus regular skills, with detailed analysis of infrastructure skills that *seem* like meta-skills but aren't.

## What Are Meta-Skills?

**Meta-skills operate ON the skill system itself**, not on domain tasks.

| Aspect | Meta-Skill | Regular Skill |
|--------|------------|---------------|
| **Operates ON** | Skills themselves | Domain tasks |
| **Examples** | Create skill, validate menus | Send reminder, manage containers |
| **Scope** | Cross-skill, infrastructure | Single domain |
| **User** | Skill developers | End users of features |

## The Evaluation Criteria

To determine if a skill is meta or regular, apply this test:

> **Does this skill CREATE, MODIFY, VALIDATE, or DELETE skill definitions?**

| Answer | Classification |
|--------|----------------|
| Yes - operates on SKILL.md files, menus, triggers, context folders | **Meta-skill** |
| No - operates on data, tasks, services, logs, schedules | **Regular skill** |

## Current Meta-Skills

In the OpenCode ecosystem, there are **2 meta-skills**:

| Skill | Trigger | Operates ON |
|-------|---------|-------------|
| **skill-factory** | `sf` | Creates/updates SKILL.md files, 13-section structure |
| **menu-factory** | `mf` | Validates menus across all skills, applies learning |

Both explicitly operate ON the skill system:

- **skill-factory**: Writes SKILL.md files, creates skill structure
- **menu-factory**: Reads all SKILL.md files, validates menu JSON, reorders options

## Infrastructure Skills: Not Meta-Skills

These skills *seem* like meta-skills because they're infrastructure, but they fail the test:

### orchestrator

```
Trigger: orch
Purpose: Unified lifecycle management for garden, energy, work, personal, blog domains
Operates ON: Life domains (not skills)
```

**Verdict**: ❌ **Regular skill**

The orchestrator manages *life domains*, not skills. It uses the Plant → Grow → Harvest → Rest model on tasks like "water plants" or "write blog post", not on SKILL.md files.

### hybridmemory

```
Trigger: mem, memory
Purpose: PostgreSQL memory storage with pgvector
Operates ON: Conversation records, memories (not skills)
```

**Verdict**: ❌ **Regular skill**

hybridmemory stores *conversations and decisions*, not skill definitions. If it stored SKILL.md files in PostgreSQL, it would be a meta-skill. But it stores user/agent exchanges.

### tracking

```
Trigger: (automatic)
Purpose: Tracks flows, actions, delegations, skills usage
Operates ON: Flow logs, action records (not skills)
```

**Verdict**: ❌ **Regular skill**

tracking *monitors* skill usage but doesn't CREATE/MODIFY/VALIDATE skills. It's observability, not management. Think of it as a monitoring dashboard, not a factory.

### cron

```
Trigger: cron
Purpose: Manage system cron jobs - list, add, remove, backup
Operates ON: Scheduled tasks (not skills)
```

**Verdict**: ❌ **Regular skill**

cron manages *scheduled tasks*, not skill execution. It could schedule a skill to run, but doesn't define or modify skills.

## Summary Table

| Skill | Meta? | Why |
|-------|-------|-----|
| **skill-factory** | ✅ Yes | Creates SKILL.md files |
| **menu-factory** | ✅ Yes | Validates menus across skills |
| orchestrator | ❌ No | Manages life domains |
| hybridmemory | ❌ No | Stores conversation memory |
| tracking | ❌ No | Monitors usage logs |
| cron | ❌ No | Manages scheduled tasks |

## What Would Make Them Meta-Skills?

| Skill | To Become Meta-Skill |
|-------|----------------------|
| orchestrator | Would need to orchestrate **skill execution order** (like oh-my-opencode's agent system) |
| hybridmemory | Would need to store **skill definitions** (not just conversation memory) |
| tracking | Would need to **validate/fix skills** based on tracking data |
| cron | Would need to schedule **skill validation runs** (not just any task) |

## The Mistake I Made

When analyzing the 84-skill ecosystem for gaps, I initially recommended 5 new meta-skills:

1. state-factory
2. trigger-factory
3. context-factory
4. validation-factory
5. agent-factory

Applying the test rigorously:

| Proposed | Verdict | Reasoning |
|----------|---------|-----------|
| **state-factory** | ❌ Not meta | Manages session state, not skills |
| **trigger-factory** | ✅ Meta-skill | Scans all skills for trigger words, validates conflicts |
| **context-factory** | ✅ Meta-skill | Standardizes context/ folders across skills |
| **validation-factory** | ❌ Not meta | Runs verification patterns on code |
| **agent-factory** | ✅ Meta-skill | Would create agent definitions to replace oh-my-opencode |

## Corrected Recommendations

### True Meta-Skills (3 candidates)

1. **trigger-factory** (`tgf`) - Trigger word validation across 84 skills
2. **context-factory** (`ctf`) - Progressive disclosure standardization
3. **agent-factory** (`af`) - Agent orchestration definitions

### Regular Skills (not meta)

1. **session-state** - Manage current_state.md, topic lifecycle
2. **verification** - Pre-completion validation patterns

## Why This Matters

As AI agent ecosystems grow, the distinction becomes critical:

- **Meta-skills** are infrastructure for skill developers
- **Regular skills** are tools for end users

Mixing them up leads to:
- Confused architecture
- Skills that try to do too much
- Unclear separation of concerns
- "Factory" inflation (everything becomes a factory)

## Conclusion

Before creating any "factory" or "meta" skill, ask:

> **"Does this CREATE, MODIFY, VALIDATE, or DELETE skill definitions?"**

If the answer is "no, it operates on data/tasks/logs/schedules", build a regular skill instead.

---

**Skills mentioned**: 
- [skill-factory](http://ubuntu4:8080/editor/opencode/skills/skill-factory/SKILL.md)
- [menu-factory](http://ubuntu4:8080/editor/opencode/skills/menu-factory/SKILL.md)
- [orchestrator](http://ubuntu4:8080/editor/opencode/skills/orchestrator/SKILL.md)
- [hybridmemory](http://ubuntu4:8080/editor/opencode/skills/hybridmemory/SKILL.md)
- [tracking](http://ubuntu4:8080/editor/opencode/skills/tracking/SKILL.md)
- [cron](http://ubuntu4:8080/editor/opencode/skills/cron/SKILL.md)