---
pubDatetime: 2026-04-06T23:45:00Z
title: "Schema Unification Pipeline: Unifying 10 Signal Types with Pydantic and PostgreSQL"
postSlug: "schema-unification-pipeline-pydantic-postgresql"
description: "Built a unified Pydantic-based schema registry for all signal types with PostgreSQL + Directus mappings. 269 signals migrated from 7 ad-hoc formats into a single queryable table."
tags:
  - pydantic
  - opencode
  - postgresql
  - signal-capture
  - schemas
  - infrastructure
---

# Schema Unification Pipeline: Unifying 10 Signal Types with Pydantic and PostgreSQL

> **269 signals unified. 7 ad-hoc formats consolidated. One queryable table.**

## The Problem

The opencode ecosystem captured signals through **seven different formats**:

| Signal Type | Storage | Format |
|-------------|---------|--------|
| Menu Present/Select | signals.json | Custom JSON |
| Trigger Usage | trigger_usage.json | Custom JSON |
| Co-Selection | co_selections.json | Custom JSON |
| Menu Violations | menu_violations.jsonl | JSONL |
| Deferred Options | deferred_options.json | Custom JSON |
| Flow Tracking | PostgreSQL | PG |
| Memory Ops | pghmem | PG + pgvector |

No unified schema. No validation. No type safety. Drift risk everywhere.

## The Architecture

10 Pydantic models as source of truth, unified PostgreSQL table with JSONB payload, Directus collection for analytics mirror, CLI query tool for optimizer and dashboard queries.

Signal types: MENU_PRESENT, MENU_SELECT, TRIGGER_USAGE, CO_SELECTION, MENU_VIOLATION, DEFERRED_OPTION, FLOW_EVENT, MEMORY_OP, SCHEMA_CHANGE, RESOURCE_MUTATION.

## The Results

269 signals migrated from 4 types into the unified controlplane.signal_events table:
- Menu present: 96 signals
- Trigger usage: 73 signals  
- Menu select: 70 signals
- Menu violation: 30 signals
- 34 unique skills tracked

## Integration

record_signal.py and record_trigger.py now write to both legacy JSON files (backward compatible) and the unified PG table. Zero downtime during transition.

## Query API

CLI provides: recent signals, per-skill stats, full export for optimizer feeding.

## What is Next

Journey kit publishing is agent-registered and kit-bundle-built but needs email verification. Evolution engine has an 83-step implementation plan ready to execute. This unified signal pipeline is the foundation for the evolution engine - every domain needs signal data to drive improvements: menu optimization, trigger usage tracking, deferred option patterns, and schema change history.