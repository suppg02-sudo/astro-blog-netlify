---
pubDatetime: 2026-04-04T17:44:11Z
title: "Schema Infrastructure Audit: The Complete State of Our Schema Ecosystem"
postSlug: "schema-infrastructure-audit-the-complete-state-of-"
description: "A comprehensive audit of the OpenCode schema ecosystem — 3 live files, 5 data files, massive duplication, and a 1,042-line design spec waiting for implementation. The schemas that describe themselves,"
tags:
  - meta-programming
  - technical-debt
  - composition
  - audit
  - schemas
  - infrastructure
---

> **The principle of recursiveness demands that our schemas describe themselves.** Right now, they don't. This is that audit.

---

## Executive Summary

The OpenCode schema ecosystem exists in a **pre-composition state**. We have a comprehensive 1,042-line design spec for a 7-layer self-describing schema architecture, but the actual implementation is still at ground zero: **3 live schema files** scattered across skill contexts with **zero composition**, **massive field duplication**, and **no registry, no scanner, no change tracking**.

**Health Score Estimate: 12/100** (baseline — before any improvements)

---

## What Exists Today

### Live Schema Files (3)

| Schema | Location | Lines | Has $-header? | Uses Composition? |
|--------|----------|-------|---------------|-------------------|
| `schema.yaml` (project) | `skills/project-factory/context/` | 177 | ❌ | ❌ |
| `research-schema.yaml` | `skills/research-factory/context/` | 307 | ❌ | ❌ |
| `agent-schema.yaml` | `skills/agents-factory/context/` | 161 | ❌ | ❌ |

### Data Files That Should Be Schemas (2+)

| File | Location | Has Schema Definition? |
|------|----------|----------------------|
| `deferred_options.json` | `data/` | ❌ Implicit structure only |
| `goals.json` (lifeplan) | `skills/lifeplan/context/` | ❌ No schema file exists |

### Referenced But Missing (2)

| Schema | Referenced In | Status |
|--------|--------------|--------|
| `roadmap-schema.yaml` | project-schema, research-schema | Doesn't exist as standalone file |
| `dashboard-schema.yaml` | project-schema, research-schema, agent-schema | Doesn't exist as standalone file |

### The Design Spec (1)

A comprehensive 1,042-line specification exists at [`docs/superpowers/specs/2026-04-04-schema-infrastructure-design.md`](/editor/opencode/docs/superpowers/specs/2026-04-04-schema-infrastructure-design.md). It defines the complete 7-layer architecture. It was written but deferred before implementation planning.

---

## The Duplication Hotspots

This is where the real cost lives. Every duplicate field block is a drift risk — when you update a field in one schema, you must remember to update it in three others.

### `signal_tracking` — Duplicated 3 Times

Identical structure in project-schema, research-schema, and agent-schema:

```yaml
signal_tracking:
  enabled: boolean
  signals:
    - type: selection | co_selection | rejection | frequency | dwell | backtrack
      timestamp: ISO8601
      context: string
      value: string
      metadata: object | null
  aggregates:
    top_selections: object
    co_selection_pairs: object
    rejection_rate: number
```

**Cost**: 3 copies × ~15 lines = 45 lines of duplication. Single source of truth needed.

### `roadmap` — Duplicated 3 Times

The hybrid roadmap structure (phases with embedded checklists) appears in project-schema, research-schema, and agent-schema. Each is a full copy of the phase/checklist/dependencies structure.

**Cost**: 3 copies × ~20 lines = 60 lines of duplication.

### `dashboard` — Duplicated 3 Times

Metrics and visual configuration structure duplicated across all three entity schemas.

**Cost**: 3 copies × ~20 lines = 60 lines of duplication.

### Base Fields — In All 5+ Files

Every single schema and data file repeats these fields:

```
id, title, status, priority, created, updated, description
```

**Cost**: 7 fields × 5 files = 35 implicit duplications. This is what `base-entity` solves.

### `schedule` — In 3 Files

Project schema, research schema, and lifeplan goals all have schedule structures with overlapping but not identical fields (target_date vs target_completion, frequency, cron_id, recurring_tasks, blocking_tasks).

**Cost**: Near-duplicate structures that should share a mixin with configurable variations.

---

## The Design: 7-Layer Architecture

The existing spec proposes a complete overhaul:

```
🔴 Meta-Schema Layer        → schema-schema.yaml: The schema that describes all schemas
🟠 Composition Layer         → base-entity + 4 mixins (schedulable, trackable, traceable, relatable)
🟡 Registry Layer            → Auto-generated schema-registry.yaml via scanner
🟢 Manager Layer             → Menu-driven schema analysis (ss trigger)
🔵 Tracking Layer            → Change history and evolution records
🟣 Publishing Layer          → Auto-generate analysis blog posts
⚪ Integration Layer         → Connect to telos, environment, roadmap
```

### The Composition Model

After composition, each schema only defines its **unique** fields:

```
base-entity (7 fields: id, title, status, priority, created, updated, description, tags)
│
├── mixin-schedulable (schedule object)
├── mixin-trackable (roadmap + dashboard + signal_tracking)
├── mixin-traceable (change_history)
├── mixin-relatable (relations)
│
├── project-schema        = base + schedulable + trackable + traceable + relatable
│   └── adds: phases, context, menu, shopping, actions
│
├── research-schema       = base + schedulable + trackable + traceable + relatable
│   └── adds: category, adapters, sources, quality, findings, history
│
├── agent-schema          = base + trackable + traceable + relatable
│   └── adds: version, identity, tools, parameters, harness_ref, export_targets
│
├── goal-schema (new)     = base + schedulable + traceable
│   └── adds: subtasks, category, reminder_sent
│
├── deferred-schema       = base + traceable
│   └── adds: source, source_id, trigger, origin_date, deferred_date
│
└── task-schema (new)     = base + traceable
    └── adds: action, params, result, started_at, completed_at, error
```

### The Schema Scanner

A Python script (`scripts/schema-scanner.py`) that:

1. Parses `$`-metadata headers from all schema files
2. Resolves inheritance and mixin composition
3. Calculates overlap percentages between all schema pairs
4. Detects issues: orphans, duplicates, stale references, broken imports
5. Generates health scores across 5 dimensions
6. Outputs `schema-registry.yaml` — the cached index

**Health Scoring Formula:**

```
health_score = (
    composition_score * 0.30   # Are schemas using base-entity + mixins?
  + dedup_score * 0.25         # How much field duplication remains?
  + coverage_score * 0.20      # Are all schemas registered and self-describing?
  + freshness_score * 0.15     # Are schemas recently validated/updated?
  + integration_score * 0.10   # Do schemas declare their consumers correctly?
)
```

### The Schema Manager Menu

Trigger: `ss`

```
📊 Schema System Menu

1. 📋 Full Analysis Report (Recommended)
2. 🌳 Inheritance Map
3. 🔍 Overlap Matrix
4. 📝 Change Log
5. ✅ Validate All Schemas
6. 📤 Publish Analysis to Blog
7. 🔄 Sync Registry
8. 🏗️ Schema Builder
9. 📊 Health Dashboard
```

---

## What's Missing (Implementation Gap)

| Component | Status | Effort |
|-----------|--------|--------|
| `/schemas/` directory | ❌ Doesn't exist | 5 min |
| `schema-schema.yaml` (meta-schema) | ❌ Not created | 30 min |
| `base-entity.yaml` | ❌ Not created | 20 min |
| `mixin-schedulable.yaml` | ❌ Not created | 30 min |
| `mixin-trackable.yaml` | ❌ Not created | 30 min |
| `mixin-traceable.yaml` | ❌ Not created | 20 min |
| `mixin-relatable.yaml` | ❌ Not created | 20 min |
| `signal-tracking-schema.yaml` | ❌ Not created | 20 min |
| `schema-scanner.py` | ❌ Not created | 2-3 hours |
| `schema-registry.yaml` | ❌ Auto-generated | — |
| `schema-history.yaml` | ❌ Not created | 15 min |
| `$`-headers on existing schemas | ❌ Not added | 1 hour |
| Refactor project-schema | ❌ Not done | 1 hour |
| Refactor research-schema | ❌ Not done | 1 hour |
| Refactor agent-schema | ❌ Not done | 45 min |
| `ss` trigger registration | ❌ Not done | 15 min |
| Schema manager menu | ❌ Not created | 1 hour |
| Blog auto-publish pipeline | ❌ Not created | 2 hours |

**Total estimated effort: 10-12 hours** for full implementation across 4 phases.

---

## Phased Delivery Plan

### Phase 1: Foundation (3-4 hours)
- Create `/schemas/` directory
- Write meta-schema, base-entity, all 4 mixins
- Extract signal-tracking from 3 locations into standalone sub-schema
- Refactor project-schema, research-schema, agent-schema to use composition
- Add `$`-metadata headers to all existing schemas

### Phase 2: Registry + Scanner (3-4 hours)
- Build `schema-scanner.py`
- Generate initial `schema-registry.yaml`
- Wire up health scoring, overlap detection, issue reporting
- Create `schema-history.yaml` with initial entry

### Phase 3: Schema Manager Menu (2-3 hours)
- Create `global-schema-menu.json` in menu-factory/rules/
- Register `ss` trigger
- Implement analysis report, inheritance map, validation views
- Wire up schema builder for guided creation

### Phase 4: Blog Pipeline + Change Tracking (2-3 hours)
- Schema-to-blog post template
- Auto-publish via existing Astro/Directus pipeline
- Telegram notifications on publish
- Cron job for weekly automated reports

---

## Success Criteria

1. **Zero duplicate field blocks** — all shared fields flow through base-entity or mixins
2. **100% schema coverage** — every schema file has a `$`-metadata header
3. **Health score > 90** — within one month of implementation
4. **Automated reporting** — blog post published weekly with zero manual intervention
5. **Change traceability** — every schema modification recorded with author, timestamp, and reason
6. **7B model compatible** — a small model can read a schema header and understand what it extends, what it mixes, and what it adds

---

## The Path Forward

The design is done. The spec is written. The deferred item is captured (DO-017). What's needed now is **execution** — breaking this into the implementation plan and working through the 4 phases.

The schema infrastructure is the backbone of the entire OpenCode ecosystem. Every skill, every project, every research instance, every agent, every goal, every deferred option — they all speak the language of schemas. Making that language consistent, composable, and self-describing is not just technical debt repayment. It's **infrastructure multiplication** — every improvement compounds across every system that uses schemas.

> **Schemas that describe themselves. Mixins that compose. A registry that scans. A scanner that reports. A report that publishes itself.** That's the recursion. That's the telos.

---

*This audit was generated during a schema infrastructure brainstorming session on 2026-04-04. The full design spec is at `docs/superpowers/specs/2026-04-04-schema-infrastructure-design.md`. Implementation is deferred as DO-017.*