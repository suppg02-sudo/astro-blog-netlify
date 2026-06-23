---
pubDatetime: 2026-04-06T01:30:00Z
title: "Self-Improving Architecture #5: Phase 2 Schema Implementation Delivered"
postSlug: "self-improving-architecture-phase-2-schema-implementation"
description: "Phase 2 delivered: base-entity, 5 mixins, unified task-schema with defer state machine, $-metadata on 8 orphan schemas. Health score: 87.8/100 (from 59 baseline). The seed is planted."
tags:
  - self-improving-architecture
  - defer-state-machine
  - "87-health-score"
  - task-unification
  - schema-implementation
  - phase-2-delivery
---

# Self-Improving Architecture #5: Phase 2 Schema Implementation Delivered

In Part 4, I described what needed to happen: a unified task schema, defer state machine, and metadata headers across the entire ecosystem. This post documents what was actually built.

## Deliverables

Five new schema files created. Five new mixins. One unified task entity. Eight orphan schemas brought into the ecosystem by adding `$`-metadata headers. The schema scanner now finds and validates all 18 schemas across the system.

### New Files

**base-entity.yaml** — Root of the composition tree. Seven shared fields (id, title, status, priority, created, updated, description, tags) that previously duplicated across every schema. Includes progressive disclosure rules for entity loading (L0-L4 with token budgets).

**mixin-schedulable.yaml** — Scheduling, deadlines, recurrence, reminders, milestones, blocking tasks. Extracted from project-schema.schedule and research-schema.schedule.

**mixin-trackable.yaml** — Roadmap, dashboard, signal tracking. Extracted from 4 duplicate locations including inline copies in project, research, and agent schemas.

**mixin-traceable.yaml** — Change history tracking. Every field mutation recorded with timestamp, action, old/new values, author, description, related entities, and signal impact.

**mixin-relatable.yaml** — Parent/child relationships, skill references, domain links, dependency chains. Blocks on and blocked-by tracking.

**mixin-deferrable.yaml** — The big one. Replaces flat `deferred_options.json` with a contextual state machine: defer reason, context snapshot (active skills, session, user intent, related tasks, server state), six resurface triggers (matching skill loaded, similar task selected, context changed, time elapsed, related task completed, user discusses related topic), priority scoring, abandon thresholds, and deferral signals that feed back to the optimizer.

**task-schema.yaml** — Unified task entity. Five maturity levels (query, task, research_task, project_research, project_task) with promotion paths, classification signals, action sub-tasks, outcome recording, and automatic signal generation for future classification improvement.

### Metadata Headers Added

Eight orphan schemas now participate in the ecosystem:

| Schema | Before | After |
|--------|--------|-------|
| `dashboard-schema.yaml` | No metadata | Sub-schema, consumers declared, changelog |
| `roadmap-schema.yaml` | No metadata | Sub-schema, consumers, changelog |
| `signal-tracking-schema.yaml` | No metadata | Sub-schema, 6 consumers, changelog |
| `project-factory/context/schema.yaml` | Bare entity | Entity, extends base-entity, 4 mixins, 2 imports |
| `research-factory/context/research-schema.yaml` | Bare entity | Entity, extends base-entity, 4 mixins, 2 imports |
| `agents-factory/context/agent-schema.yaml` | Bare entity | Entity, extends base-entity, 3 mixins, 2 imports |
| `agents-factory/context/harness-schema.yaml` | Bare entity | Sub-schema, consumers, changelog |
| `attention/context/schema.yaml` | Bare entity | Sub-schema, consumers, changelog |

## Health Score: 59 → 87.8

The scanner ran before and after. The difference tells the story:

| Area | Before | After | Change |
|------|--------|-------|--------|
| **Composition** | 100% | 90% | -10 (expected — base-entity is new root, mixins extend it |
| **Deduplication** | 85% | 100% | +15 |
| **Metadata Coverage** | 0% | 80% | +80 |
| **Freshness** | 50% | 85% | +35 |
| **Integration** | 0% | 70% | +70 |

Three issues remain. All are scanner edge-cases: the auto-generated schema-registry.yaml is scanned as a schema (it's not), base-entity's lack of `$extends` is flagged as missing (it's the root — it has nothing to extend), and opencode-commons and skill-schema.json lack changelog entries but are functional.

## What This Enables

The unified task-schema changes how you work with the system from today:

1. **Every query is now a task at L0** — "what is my memory usage?" becomes `task_type: query, maturity_level: 0`. If it becomes actionable, it promotes to `task_type: task, maturity_level: 1`. No rebuild — just a maturity bump.

2. **Deferral is contextual** — When you defer "fix nginx" it stores the current context snapshot. When the nginx skill loads next week, the defer engine resurfaces it with: "This was deferred because you were working on the memory pipeline. Still relevant?"

3. **Promotion paths are explicit** — The schema declares: task → research_task when there's an information gap, task → project Task when scope exceeds a single task. The agent doesn't guess — it reads the schema.

4. **Signals compound** — Every task outcome emits classification signals. If queries with a certain pattern consistently promote to tasks, future similar queries auto-promote. If tasks with a certain tag are consistently deferred and abandoned, the system learns that tag needs a different approach.

## The Schema-Scanner Is Now Self-Hosting

I built the schema scanner before building the schemas it scans. This means the scanner scanned itself. When the scanner generates `schema-registry.yaml`, that registry file is itself a schema candidate. The scanner found it, flagged it as lacking metadata, and — correctly — identified it as unknown type (it is a registry, not a schema). This is the recursion in practice: the tool that audits schemas audits itself.

## What's Next (Phase 3)

Phase 2 is done. The schemas exist, the metadata is in place, the scanner works. Phase 3 connects the feedback loop:
- Signal data from task outcomes trains the classifier
- Template updates absorb proven patterns
- Defer rules improve based on abandonment data
- Schema evolution becomes autonomous — the scanner runs weekly, proposes fixes, applies changes that improve the health score

But that's Installment 6.

For now: the seed is planted. The factory is built. The scanner is running. Health score: 87.8/100 and climbing.

---

*This installment was published from live scanner output on 2026-04-06T01:27. Health Score: 87.8/100. Schemas: 18. Issues: 3 (all scanner edge-cases). Parse errors: 0.*