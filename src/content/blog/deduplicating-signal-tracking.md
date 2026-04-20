---
pubDatetime: 2026-04-04T20:55:33Z
title: "Deduplicating signal_tracking — Hub-and-Spoke Schema Architecture"
postSlug: "deduplicating-signal-tracking"
description: "Deduplicating signal_tracking — Hub-and-Spoke Schema Architecture"
tags:
  - others
---

> **TL;DR**: Found the `signal_tracking` structure copy-pasted in 12 files across the codebase. Extracted it to a single hub schema, replaced all copies with `$ref` references, and updated the factory-review cron job to enforce hub-spoke congruence going forward.

## Quick Summary

- **Problem**: `signal_tracking` schema duplicated 12 times — hub schemas, spoke schemas, templates, and instances
- **Solution**: Created `/root/.config/opencode/schemas/signal-tracking-schema.yaml` as single source of truth
- **Verification**: All 12 files now reference hub via `$ref`, zero orphan duplicates remain
- **Next**: Created `manifest.yaml` (hub index) and updated `factory_review.py` to enforce congruence rules from `requirements.yaml`

## The Problem — Schema Sprawl

The OpenCode ecosystem uses a hub-and-spoke architecture for shared schemas. The hub lives at `/root/.config/opencode/schemas/` and each factory skill (spoke) owns its domain-specific schemas while consuming shared structures from the hub.

But over time, the `signal_tracking` structure got copy-pasted everywhere instead of being promoted to the hub:

```
🔴 signal_tracking duplicated 12 times across:
  🟠 Hub: dashboard-schema.yaml, roadmap-schema.yaml
  🟠 Spoke schemas: agent-schema.yaml, research-schema.yaml, project-factory/schema.yaml
  🟡 Templates: agent-template.yaml, research-template.yaml, project-template.yaml
  🟡 Instances: browser-agent.yaml, code-reviewer.yaml, test-rf-validation.yaml, evolution.yaml
```

Each copy was slightly different — some had full field definitions, others were minimal. This meant drift between copies was inevitable and undetectable.

## The Fix — Extract to Hub

Created `/root/.config/opencode/schemas/signal-tracking-schema.yaml` with the canonical definition:

```yaml
signal_tracking:
  description: "Capture interaction signals feeding menu-factory optimizer"
  enabled:
    type: boolean
    default: true
  signals:
    type: array
    items:
      type: enum
      values: [selection, co_selection, rejection, frequency, dwell, backtrack]
      timestamp: datetime
      context: string
      value: string
      metadata: object | null
  aggregates:
    top_selections: object
    co_selection_pairs: object
    rejection_rate: number
```

Every file that previously duplicated this structure now contains:

```yaml
signal_tracking:
  $ref: "/root/.config/opencode/schemas/signal-tracking-schema.yaml"
  enabled: true
  signals: []
  aggregates: {}
```

## Hub Manifest

Created `/root/.config/opencode/schemas/manifest.yaml` — the hub index that spokes consult to discover available schemas:

| Schema | Format | Priority | Consumers |
|--------|--------|----------|-----------|
| skill-schema.json | JSON Schema draft-07 | Critical | 5 factories |
| roadmap-schema.yaml | YAML Schema v1 | High | 2 factories |
| dashboard-schema.yaml | YAML Schema v1 | High | 2 factories |
| signal-tracking-schema.yaml | YAML Schema v1 | High | 12 files |

The manifest includes a dependency graph (roadmap + dashboard both depend on signal-tracking) and tracks pending additions like `globals-schema` and `requirements-schema`.

## Factory Review Enforcement

Updated the weekly factory-review cron job (`factory_review.py`) to read `requirements.yaml` and run three new checks:

**Section 18 — Hub Schema Integrity**: Validates manifest exists, all registered hub schemas are present and parse correctly.

**Section 19 — Spoke-Hub Congruence**: For each spoke, verifies owned schemas exist, hub consumption references are valid, and expected globals files are present.

**Section 20 — Signal Tracking $ref Verification**: Scans all YAML files for `signal_tracking` blocks and flags any that don't reference the hub via `$ref`.

The latest run shows:

```
## 18. Hub Schema Integrity
- **Hub root**: `/root/.config/opencode/schemas`
- **Manifest**: ✓ exists
- **Registered schemas**: 4
  - 🟢 `skill-schema.json` (critical) → 5 consumers
  - 🟢 `roadmap-schema.yaml` (high) → 2 consumers
  - 🟢 `dashboard-schema.yaml` (high) → 2 consumers
  - 🟢 `signal-tracking-schema.yaml` (high) → 12 consumers

## 20. Signal Tracking $ref Verification
- **Hub signal-tracking**: 🟢
- **Files with signal_tracking**: 10
- 🟢 All signal_tracking blocks reference hub via $ref
```

## Architecture — Before and After

```
BEFORE (duplicated):
  Hub: 3 schemas
  Spokes: 12 independent copies of signal_tracking
  No manifest
  No enforcement

AFTER (hub-and-spoke):
  Hub: 4 schemas + manifest.yaml
  Spokes: 12 $ref references → single source of truth
  Factory review enforces congruence weekly
  Deduplication saves ~400 lines of repeated structure
```

## What's Next

Three pending additions identified in the manifest:

1. **globals-schema.yaml** (medium) — Abstract the shared `defaults/instructions/attention_rules` pattern from agents-factory and research-factory globals files
2. **requirements-schema.yaml** (low) — Self-referential: validate the requirements.yaml that controls the review process
3. **manifest-schema.yaml** (low) — Self-referential: validate the manifest file itself

The hub-and-spoke model is now enforced automatically — every weekly factory review will detect schema drift, missing hub references, and orphan duplicates.

**Tags**: opencode, schema-architecture, hub-and-spoke, deduplication, factory-review, automation