---
pubDatetime: 2026-04-08T09:00:04Z
title: "Deferred Schema Consolidation: One Problem, Not Fifteen"
postSlug: "deferred-schema-consolidation"
description: "Deferred Schema Consolidation: One Problem, Not Fifteen"
tags:
  - others
---

# Deferred Schema Consolidation: One Problem, Not Fifteen

When analyzing deferred items, duplication is easy to miss. A recent audit of open deferred tasks revealed something interesting: what appeared to be fifteen separate schema inheritance issues was actually seven unique problems—each detected twice.

## The Duplicate Pattern

The deferred list included warnings like:
- "High overlap without shared base: base-entity ↔ experiment-schema"
- "High overlap without shared base: base-entity ↔ task-schema"
- "High overlap without shared base: base-entity ↔ mixin-deferrable"
- And five more variations...

Each relationship appeared twice, creating the illusion of fifteen distinct issues.

## Root Cause

**Diamond inheritance**: Mixins extended base-entity, while entities also extended base-entity AND mixed in those same mixins. This created the same field duplication detected twice by different code paths.

Example:
```
base-entity (id, title, status, priority, created, updated, description, tags)
    ↑
    ├── task-schema extends base-entity, mixes in mixin-deferrable
    │       ↑ 
    │       └── mixin-deferrable extends base-entity  ← DUPLICATE
    │
    └── research-task-schema extends base-entity, mixes in mixin-deferrable
            ↑
            └── mixin-deferrable extends base-entity  ← DUPLICATE AGAIN
```

## The Fix Applied

Removed `$extends: base-entity` from all 5 mixins:
- mixin-deferrable
- mixin-relatable  
- mixin-schedulable
- mixin-traceable
- mixin-trackable

Mixins are composed into entities that already extend base-entity — they don't need to extend it themselves.

## Results

| Before | After |
|--------|-------|
| 15+ high overlap warnings | 3 (expected: project↔base, dashboard↔trackable, trackable↔roadmap) |

The 3 remaining are correct — project-schema legitimately extends base-entity, and trackable imports dashboard/roadmap schemas.

## Lessons

1. **Diamond inheritance is a smell** — when entities AND their mixins both extend the same base
2. **Mixins compose, they don't extend** — a mixin adds capability to an entity that already has the base
3. **Detect patterns first** — the duplicate detection flagged the same issue twice
4. **Fix is surgical** — remove redundant extends, not schema fields
