---
pubDatetime: 2026-04-07T12:00:00Z
title: "Schema Unification Pipeline: A Portable Signal Architecture for AI Development Environments"
postSlug: "schema-unification-pipeline-design"
description: "Schema Unification Pipeline: A Portable Signal Architecture for AI Development Environments"
tags:
  - pydantic
  - opencode
  - design
  - schema
  - architecture
  - signal-capture
---

# Schema Unification Pipeline: A Portable Signal Architecture for AI Development Environments

*Published April 6, 2026*

## Executive Summary

Any serious AI development environment produces a constant stream of interaction data: menu selections, trigger word activations, memory operations, skill invocations, flow state changes, cron job results, and schema health checks. In our OpenCode-based setup, we captured **10 distinct signal types** across a daily cron-driven pipeline.

The problem: each signal type evolved its own ad-hoc schema. YAML design-time schemas, PostgreSQL storage columns, runtime JSON files, and Directus API fields all drifted apart. No shared validation. No portability.

This article presents the design for a **Schema Unification Pipeline** -- a single Pydantic-based schema registry that serves as the source of truth for all 10 signal types, with explicit mappings to PostgreSQL tables and Directus collections. The design prioritises **portability**: when we migrate from OpenCode to pi mono, the schemas travel with us unchanged.

---

## Why This Matters

If you are building any kind of AI agent infrastructure -- whether it is a coding assistant, a research pipeline, or a multi-agent orchestration system -- you will accumulate **observability data**. The question is not whether to capture it, but how to structure it so that:

1. **Every signal validates** -- bad data is caught at ingestion, not discovered weeks later in a dashboard
2. **Schemas are portable** -- switching tools does not mean rewriting your data layer
3. **One definition drives everything** -- PG tables, API fields, and validation rules all derive from a single source

---

## The Problem in Detail

Our signal infrastructure spans four layers with no shared contract:

| Layer | Format | Count | Issue |
|-------|--------|-------|-------|
| Design-time (YAML) | extends/mixins composition | 18 schemas | No runtime validation |
| Storage-time (PostgreSQL) | 11 tables, 38+ columns in daily_signals | 100+ columns total | Naming drift between tables |
| Runtime (JSON files) | Various ad-hoc shapes | 3 file formats | No shared schema |
| API-time (Directus) | Mirrors PG with field renames | 31 fields | No validation at API boundary |

Each layer evolved independently. The YAML composition system uses id, version, extends and mixins. The PG table uses flat column names like menu_presents, trigger_events_total, memory_embedding_coverage. The JSON files use short keys like ts, cnt. Directus uses its own naming. None of them validate against each other.

---

## The Design: JSON Schema as Single Source of Truth

```
Pydantic Models (source of truth)
  |
  +---> PG CREATE TABLE (auto-generated)
  +---> Directus collection fields (auto-generated)
  +---> Runtime validation (Pydantic validates every event)
  +---> YAML schema export (for documentation)
```

Why JSON Schema via Pydantic:

- **Portable**: any Python-based tool can import the models
- **Validated**: Pydantic catches type errors, missing fields, enum violations at runtime
- **Generative**: PG migrations and Directus fields are derived, never hand-written
- **Versioned**: each model carries a version and migration path

---

## The 10 Signal Types

### 1. MenuSignal

Tracks every menu presentation, selection, deferral, and custom answer. Critical for understanding user intent vs. predefined options.

- `event_type`: present / select / defer / custom
- `skill`: which skill presented the menu
- `option_label`: the option shown or selected (max 25 chars)
- `mode`: mobile or desktop
- `position`: option position in the list

### 2. TriggerEvent

Records every trigger word activation (co, sf, bs, etc.) with context.

- `trigger`: the trigger word used
- `context`: what was happening when triggered
- `timestamp`: when it fired

### 3. MemoryEvent

Tracks the PostgreSQL memory system: 2,834+ memories across 6 types with 47.6% embedding coverage.

- `memory_type`: decision / conversation / action / exchange / experience
- `operation`: created / accessed / updated / deleted
- `scope`: project scope if applicable
- `tags`: categorisation tags
- `content_hash`: for deduplication

### 4. ConversationTurn

Full transcript capture from OpenCode sessions -- the richest signal source.

- `session_id`: which session
- `role`: user / assistant / system
- `content_length`: character count (for volume tracking without storing raw content)
- `timestamp`: when the turn occurred

### 5. DeferredItem

Backlogged menu options and suggestions. Currently 22 items across 8 categories.

- `title`: what was deferred
- `category`: skills / infrastructure / research / etc.
- `priority`: high / medium / low
- `trigger`: what context should resurface it
- `tags`: for search and cross-referencing

### 6. SkillInvocation

Skill usage tracking -- which skills fire, how often, and whether they succeed.

- `skill_name`: which skill was invoked
- `trigger_source`: what triggered it
- `session_id`: which session
- `duration_ms`: execution time
- `success`: whether it completed without error

### 7. FlowEvent

Workflow state changes -- active flows, completions, and failures.

- `flow_id`: unique flow identifier
- `flow_name`: human-readable name
- `status`: created / active / paused / completed / failed
- `trigger`: what started the flow

### 8. SchemaHealthCheck

Schema scanner results -- health scores, issue detection, composition validation.

- `scanner_version`: which scanner version produced this
- `schema_count`: total schemas scanned
- `health_score`: 0-100 composite score
- `issues`: list of detected problems

### 9. CronJobStatus

Infrastructure health -- 41 active cron jobs with failure detection.

- `schedule`: cron expression
- `command`: what runs
- `skill_tag`: associated skill if any
- `last_exit_code`: 0 = success
- `failures_last_24h`: recent failure count

### 10. ProjectActivity

Research decisions and action logs scoped by project domain.

- `scope`: which project/domain
- `action_count`: how many actions recorded
- `related_tags`: cross-reference tags
- `timestamp`: when recorded

---

## Validation Flow

```
Signal Event -> Pydantic Model -> validator.py -> PG Store -> Directus Push
```

Any event that fails validation is logged to a validation_errors table -- no silent data loss. The validator records which schema was expected, the raw input that failed, the specific validation errors, and a timestamp.

---

## Portability: The Migration Path

The entire point of this design is that switching from OpenCode to pi mono (or any other tool) costs **zero schema migration effort**:

1. **Loader** reads existing YAML schemas and generates Pydantic models
2. **Pydantic models** generate CREATE TABLE statements for any database
3. **Pydantic models** generate Directus/Strapi/Supabase field definitions
4. **The new tool** imports the same Pydantic models -- unchanged

The schemas are the contract. The tool is just a consumer.

---

## Implementation Phases

| Phase | Deliverable | Effort |
|-------|------------|--------|
| 1. Registry Core | Base classes + loader + validator | 2-3 hours |
| 2. Signal Schemas | 10 Pydantic models with PG/Directus mappings | 3-4 hours |
| 3. Aggregator Refactor | Replace hardcoded collectors with registry-based | 2-3 hours |
| 4. PG Migration | Align table/column names to schema definitions | 1-2 hours |
| 5. Directus Sync | Auto-generate collection from schema | 1-2 hours |
| 6. Testing | Unit + integration tests | 2-3 hours |

---

## Daily Signal Snapshot (April 6, 2026)

For context, here is what the signal capture recorded today:

| Metric | Value |
|--------|-------|
| Trigger activations | 25 |
| Memory total | 2,834 (47.6% embedded) |
| New memories today | 1,273 |
| Conversations captured | 1,259 sessions |
| Deferred items | 22 (4 new today) |
| Cron jobs | 41 active |
| Schema health | 87.8% |

---

## Architecture Diagram

```
+-------------+     +--------------+     +-------------+
|  10 Signal  |---->|  Pydantic    |---->|  PostgreSQL |
|  Sources    |     |  Registry    |     |  daily_     |
|  (cron/job) |     |  (validator) |     |  signals    |
+-------------+     +------+-------+     +------+------+
                           |                     |
                    +------v-------+      +------v------+
                    |  Directus    |      |  Blog Post  |
                    |  Collection  |      |  Generator  |
                    +------+-------+      +-------------+
                           |
                    +------v-------+
                    |  Dashboard   |
                    |  (Chart.js)  |
                    +--------------+
```

---

## Key Takeaways

1. **Define schemas once, derive everything**: PG tables, API fields, and validation rules should never be hand-written. Generate them from a single source of truth.

2. **Validate at the boundary**: Every signal event should validate before it enters your system. Pydantic makes this trivial.

3. **Design for portability**: If your schemas are coupled to a specific tool, you will rewrite them when you switch tools. JSON Schema is universal.

4. **Version everything**: Schemas evolve. Track versions in the model class, provide migration functions, and maintain backward compatibility.

5. **Capture validation failures**: Silent data loss is worse than no data. Log every validation failure for later analysis.

---

*This post describes a design currently in development. The daily signal aggregator pipeline is live and running at 6:30am UTC daily. The schema unification is the next phase.*
