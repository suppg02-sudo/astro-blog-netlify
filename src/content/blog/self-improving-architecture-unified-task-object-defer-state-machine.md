---
pubDatetime: 2026-04-06T01:15:00Z
title: "Self-Improving Architecture #4: The Unified Task Object and Defer State Machine"
postSlug: "self-improving-architecture-unified-task-object-defer-state-machine"
description: "Queries, tasks, research, and projects are the same object at different maturity levels. The defer system becomes a contextual state machine, not a flat list."
tags:
  - self-improving-architecture
  - state-machine
  - defer-system
  - schema-design
  - task-promotion
  - recursive-tasks
  - unified-tasks
---

# Self-Improving Architecture #4: The Unified Task Object and Defer State Machine

In Parts 1-3, I covered the six-layer architecture, data flow, and progressive disclosure. There's a missing piece — the most fundamental object type in the system, the one you actually use to get things done.

Tasks. But not as you'd expect them.

## The Problem: Five Separate Task Systems, None Complete

Right now, task-like objects are scattered across the architecture:

- **Queries** — ephemeral. "what is my memory usage?" — answered, gone, never traceable
- **Defer list** — flat JSON array. Chronological. Manual. No intelligence about when to resurface
- **Project phases** — project-specific tasks, tied to a project lifecycle
- **Research tasks** — research-factory items, separate from project tasks
- **Lifeplan goals** — time-based objects with reminders, separate from everything else

Five systems for the same concept: **something needs to be done.** Each has its own structure, its own lifecycle, its own storage. None of them talk to each other. A query that becomes a task gets rebuilt from scratch. A task that needs research spawns a new object. A research task that reveals a project creates another.

**None of them learn from each other.**

## The Fix: One Object, Five Maturity Levels

A query, a task, a research item, a project — these are the same entity at different maturity levels. The same progressive disclosure that governs skill loading (L0 identity → L4 reference) governs task evolution.

```
L0: Query        — "what is my memory usage?" 
                     ~10 tokens, instant, no commitment
L1: Task         — "fix the memory pipeline" 
                     ~200 tokens, scope defined, execution ready
L2: Research Task — "investigate why embeddings aren't generating"
                     ~1,000 tokens, methodology defined, tools allocated
L3: Project Rsrch — "build self-improving schema system"
                     ~5,000 tokens, phases defined, roadmap attached
L4: Project Task  — "implement base-entity mixin with validation"
                     ~15,000 tokens, full spec, plan, tests, implementation
```

This is progressive disclosure applied to *intention*, not just information. Each level is the same object, just with more context loaded and more commitment required.

The promotion path:

```
Query ──────→ Task ──────→ Research Task
   │            │               │
   │            ↓               ↓
   │     Research              Project Research
   │            │               │
   ↓            ↓               ↓
   └────→ Project Task ←────────┘
                │
                ↓
          Execution → Signals → Improvement
```

Some paths are direct (query → task → project task when you already know what to do). Some branch (task → research task when you need investigation first). All of them are promotion decisions, not object rebuilds.

## The Unifying Schema

```yaml
# task-schema.yaml
$extends: base-entity
$mixins: [mixin-schedulable, mixin-traceable, mixin-deferrable]

task_type:
  enum: [query, task, research_task, project_research, project_task]
  default: query

complexity_level:
  enum: [L0_identity, L1_scope, L2_spec, L3_implementation, L4_full]
  default: L0_identity
  description: |
    Progressive disclosure applied to intention. 
    Each level adds context, commitment, and cost.

promotion_path:
  query → task:           "this needs more work than a query"
  task → research_task:   "we don't know enough to build yet"
  research → project_rsrch: "this is a full investigation"
  project_rsrch → p_task: "we know what to build, let's do it"
  task → project_task:    "we know what to do, skip research"

defer_state:
  status: [active, deferred, executing, completed, abandoned]
  resurface_triggers:
    - matching_skill_loaded    # defer "fix nginx" resurfaces when nginx skill loads
    - similar_task_selected    # defer "build blog" resurfaces when a similar task is chosen
    - context_changed          # status change in a dependency
    - time_elapsed             # scheduled resurface (daily, weekly, etc.)
  context_snapshot:
    # What was happening when this was deferred?
    active_skills: []
    deferred_because: ""
    related_tasks: []
    user_intent: ""
  priority_when_resurfaces:
    user_forced: 10
    high_correlation: 8
    time_based: 3
    default: 2
```

This replaces `deferred_options.json`, project phase tracking, research task tracking, goal tracking, and query logging. One schema. Five maturity levels. Promotion, not replacement.

## The Defer System as a State Machine

Right now, defer is a flat list. You say "defer," it gets appended. You forget about it until you run `deferred list` and manually review everything.

The new system is a **contextual state machine**:

```
Task submitted
    ↓
Options presented: [Execute Now] [Defer] [Promote] [Combine with Existing]
    ↓
If Defer:
    1. Record defer_reason, context_snapshot, related_active_tasks
    2. Evaluate resurface_triggers against current context
    3. Compute resurface_priority based on correlation score
    4. Store in defer state machine (not a list)
    5. Emit signal: "task deferred in context X"
    
While deferred:
    1. Monitor context: skill loads, task completions, status changes
    2. When trigger fires: compute relevance score
    3. If relevance > threshold: resurface with "This was deferred because X"
    4. Agent presents: "Still relevant?" [Execute] [Defer Again] [Abandon]
```

The defer system learns from signal data:
- Tasks deferred and never resurfaced → broken trigger rules
- Tasks deferred and later executed successfully → good triggers, strengthen them
- Tasks resurfaced and deferred again → wrong timing, adjust trigger
- Tasks abandoned after deferral → wrong task type? Should have been promoted first?

## What Signals Feed Back

Every task interaction emits signals:

| Signal | What it tells us | How the system responds |
|---|---|---|
| Task promoted from query → task | This query had substance | Future similar queries auto-promote |
| Task deferred and never resurfaced | Defer triggers are wrong | Adjust resurface conditions |
| Task executed immediately | Right type, right time | Strengthen classification for similar tasks |
| Task promoted from task → project | Scope exceeded initial estimate | Future tasks with similar structure start higher |
| Task abandoned after 2 deferrals | Task was never the right action | Flag similar patterns early |
| Task completed from deferred state | Good deferral timing | Strengthen the trigger that resurfaced it |

This is the feedback loop from Part 2, applied to tasks instead of schemas. The same principle: **every action generates data, every data point improves the next action.**

## The Recursive Bit: Tasks About Tasks

Here's where it gets self-referential:

```
User: "Improve the defer resurfacing rules"
System: This is itself a task. Not a query — it has scope and success criteria.
       Type: task (L1), not query (L0).
       It uses the task system to improve the task system.
```

Every improvement to the task system is tracked *as* a task. The task schema evolves based on signals from task outcomes. Tasks that get deferred and never resurfaced signal a broken defer rule. Tasks that get promoted incorrectly signal broken promotion rules.

**Deferring an item about improving deferral rules is still a deferral.** The system processes its own meta-tasks using the same rules it processes the underlying tasks. This is recursiveness in action — the system applies to itself without special handling.

## Relation to Core Principles

### Schemas
One unified task-schema replaces five ad-hoc structures. Every task type validates against the same schema. The schema declares its own promotion path and defer rules.

### Progressive Disclosure
Task promotion *is* progressive disclosure. L0 → L4 applies to tasks identically to skills. Loading rules = promotion rules = commitment rules.

### Recursiveness
Tasks improve the task system. Defer rules improve defer rules. The system applies to itself. No special case for meta-tasks.

### Question Tool
Every decision (execute/defer/promote/combine) goes through the question tool. Every choice emits a signal. The defer engine learns from these signals over time.

### Context Persistence
Tasks survive sessions. Deferred items carry context snapshots. Cross-session continuity. A task deferred today resurfaces next week when the context matches.

### Attention
The defer engine decides what deserves attention *now* based on what deserves attention *given current context*. It doesn't just store — it actively manages attention allocation.

## What This Enables

1. **Every query is traceable** — from the first token, it's a task object
2. **Deferred items resurface when relevant** — not chronologically, contextually
3. **Promotion is cheap** — same object, more context. No rebuild
4. **Classification improves** — signals from outcomes train the classifier
5. **Meta-work is first-class** — "improve the system" is just another task
6. **Context budget is respected** — L0 tasks cost 10 tokens, L4 tasks cost 15,000. You choose.

## Implementation Implications for Phase 2

The schema formalization phase (Phase 2) needs to include:

- **task-schema.yaml** as a new entity schema
- **mixin-deferrable** as a new mixin (resurface rules, context snapshots)  
- **Defer engine** replaces the current `deferred add/done` CLI
- **Classification service** that scores incoming queries against existing tasks to detect duplicates and promotion candidates
- **Promotion UI** — question tool menus that present Execute/Defer/Promote/Combine for every new task

Without this, the schema composition system works beautifully for everything except the object users interact with most: tasks.

## The Bottom Line

Structure = Schemas + Control Plan
Signals = Control
Context = Self-Improvement Feedback Loop

Applied to tasks: the task schema defines the structure. The defer state machine is the control plane. Signals from task outcomes drive the control decisions. The context snapshot at deferral time feeds the feedback loop. And the system applies to itself — tasks about improving tasks are just tasks.

This isn't an add-on. It's the central nervous system of a self-improving agent.

---

*This is the fourth installment in the Self-Improving Architecture series. Part 1: The Architecture. Part 2: Data Flow and the Feedback Loop. Part 3: Progressive Disclosure as an Attention Budget. Part 5 will cover the Schema Evolution Loop — autonomous self-audit and template compilation.*