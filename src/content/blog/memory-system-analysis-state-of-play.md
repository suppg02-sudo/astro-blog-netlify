---
pubDatetime: 2026-03-22T20:27:21Z
title: "Memory System Analysis: The State of Play"
postSlug: "memory-system-analysis-state-of-play"
description: "A comprehensive audit of the PostgreSQL pgvector memory system — what works, what's broken, what's missing, and where to go next."
tags:
  - architecture
  - analysis
  - memory
  - pgvector
  - postgresql
  - infrastructure
---

A full audit of the memory system that underpins everything — agent conversations, decisions, skill usage, flow tracking, and infrastructure knowledge. Built on PostgreSQL with pgvector, it was designed to be the single source of truth. This analysis examines whether it's living up to that promise.

<!--more-->

## The Vision

The goal was simple and ambitious: **one place** for all infrastructure and conversation memory that's fast, searchable via metadata and vectors, supports graph relationships, and provides full CRUD access to original memories. Telemetry data goes elsewhere — this system is for remembering and analysing flows, skill usage, tool usage, conversations, decisions, menu choices, and deferred items.

## Current Architecture

```
┌─────────────────────────────────────────────────────┐
│                   pghmem CLI                         │
│         /usr/local/bin/pghmem                       │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│              PostgreSQL + pgvector                   │
│         - Full-text search (GIN index)              │
│         - Vector similarity (HNSW index)            │
│         - JSONB metadata (GIN index)                │
│         - 3,217 memories / 32MB                     │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│                 Jina AI API                          │
│         1024-dim embeddings (86% coverage)           │
└─────────────────────────────────────────────────────┘
```

### Database Schema

The `memories` table carries the full weight:

| Column | Type | Purpose |
|--------|------|---------|
| `id` | bigint | Auto-increment primary key |
| `memory_id` | varchar(255) | UUID for external reference |
| `user_id` | varchar(255) | Always "sisyphus" |
| `content` | text | The actual memory content |
| `memory_type` | varchar(50) | conversation, decision, action, exchange |
| `scope` | varchar(20) | user or project |
| `priority` | integer | 0-10 importance scale |
| `created_at` | timestamptz | When stored |
| `updated_at` | timestamptz | Last modification |
| `last_accessed_at` | timestamptz | Last read time |
| `access_count` | integer | Read frequency |
| `metadata` | jsonb | Flexible key-value data |
| `tags` | text[] | Array of tags |
| `embedding` | vector(1024) | Jina AI embedding |

### Indexes (10 total)

The indexing strategy is comprehensive — perhaps the strongest part of the design:

- **HNSW** on embeddings for vector similarity
- **GIN** on content for full-text search
- **GIN** on metadata for JSONB queries
- **B-tree** on created_at, priority, scope, memory_type, user_id

## What's Working

### ✅ Storage & Retrieval

PostgreSQL is rock-solid. The `pghmem` CLI provides fast full-text search and the capture script stores memories reliably. The database is healthy at 32MB with proper indexing.

### ✅ Memory Types

The four-type taxonomy works well:

| Type | Count | % | Purpose |
|------|-------|---|---------|
| conversation | 1,404 | 44% | Session summaries, research |
| action | 709 | 22% | Things done — files created, commands run |
| decision | 685 | 21% | Architecture choices, preferences |
| exchange | 418 | 13% | Quick checkpoints |

### ✅ Backup System

Every 3 hours with tiered retention (7 daily, 4 weekly, 6 monthly). Both primary SMB and local fallback. Disaster recovery documented and tested.

### ✅ Cron Integration

8-hour reports and daily indexing run on schedule. Memory capture integrated into session workflows.

## What's Broken

### 🔴 Hybrid Search Doesn't Actually Hybrid Search

The `hybrid_search()` PostgreSQL function exists but only does FTS. The vector search path is commented out with a note: *"If we have embeddings, use RRF to combine vector + FTS. For now, just use FTS since no embeddings."*

But we **do** have embeddings — 2,766 of them (86% coverage). The function was never updated after the embedding generation completed. This means semantic search — the entire point of pgvector — is effectively disabled.

### 🔴 58% Duplicate Content

The migration from Hybrid Memory + OpenMemory created massive duplication:

| Metric | Count |
|--------|-------|
| Total memories | 3,217 |
| Unique content | 1,349 |
| **Duplicates** | **1,868 (58%)** |

The worst offenders:
- 360 "Session checkpoint" entries (cron spam)
- 240 completely empty entries
- Hundreds of content duplicated across both source databases

### 🔴 Access Tracking is Dead

The schema has `access_count` and `last_accessed_at` columns — a great design for understanding which memories matter. But **every single row shows 0 accesses and NULL last_accessed_at**. The pghmem CLI never updates these columns when searching or reading.

### 🔴 CLI is Read-Only (No CRUD)

`pghmem` supports: `search`, `list`, `stats`, `recent`. That's it. No:
- `update` — can't modify content or metadata
- `delete` — can't remove duplicates or noise
- `tag` — can't add/remove tags
- `get` — can't retrieve by ID
- `metadata` — can't query by metadata keys

### 🔴 Tag Data Corruption

1,378 memories (from OpenMemory migration) have tags stored as JSON strings inside the PostgreSQL array:

```
tags = {"[\"output\"", "\"memory-architecture\"", "\"openmemory\"]"}
```

Instead of proper arrays:

```
tags = {output, memory-architecture, openmemory}
```

This means tag-based queries return garbage for 43% of tagged memories.

### 🔴 8-Hour Report Queries Wrong Database

`mem-h8-report.py` still copies from the OpenMemory SQLite container for analysis. It should be querying PostgreSQL directly.

## What's Missing

### Graph Relationships

The original vision included graph-based analysis — understanding how memories relate to each other. "This decision led to this action." "This flow used these skills." "This conversation informed this decision."

**Current state**: No relationship tables exist. No graph queries possible. Each memory is an isolated island.

### Flow Tracking in PostgreSQL

Flows live in a separate SQLite database (`[config resource]) with only 2 entries ever created. This defeats the "one place" goal. The flow schema should be a PostgreSQL table alongside memories.

### Skill Usage Tracking

The context-registry's `skills.json` shows 0 invocations and 0 unique skills tracked. Despite using dozens of skills daily, none of this is captured.

### Tool Usage Tracking

No mechanism exists to record which tools (bash, write, edit, search) are used, how often, or in what patterns. The `tool-audit` skill exists but doesn't persist data.

### Menu Choice & Deferral Tracking

`questions.json` captures 25 interactions but isn't connected to PostgreSQL. Deferred items (things you said "later" to) aren't tracked at all.

## Data Quality Deep Dive

### Content Length Distribution

| Category | Count | % |
|----------|-------|---|
| Tiny (<50 chars) | 970 | 30% |
| Short (50-200) | 2,219 | 69% |
| Medium (200-500) | 28 | <1% |
| Long (500-2000) | 4 | <1% |
| Very long (>2000) | 0 | 0% |

**Average content length: 114 characters.** Most memories are one-liners. This is fine for decisions and actions but suggests conversations aren't being captured with enough depth.

### Priority Distribution

| Priority | Count | Meaning |
|----------|-------|---------|
| 0 | 1,398 | Default/unset (migrated data) |
| 3 | 1,337 | Default from capture script |
| 2 | 436 | Low |
| 7 | 41 | High |
| 8 | 3 | Very high |
| 10 | 1 | Critical |

Priority is barely used. 85% of memories are at 0 or 3 (both defaults). This column could be powerful for surfacing important memories but needs intentional use.

### Scope Distribution

| Scope | Count |
|-------|-------|
| user | 3,216 |
| project | 1 |

Scope is effectively unused. Everything is "user" scope. The distinction between cross-project knowledge and codebase-specific knowledge isn't being applied.

### Metadata Key Diversity

The JSONB metadata field contains 30+ different keys across memories, including:

`source`, `original_sector`, `type`, `category`, `backfilled`, `user_id`, `captured_at`, `capture_source`, `date_created`, `components_analyzed`, `file_location`, `document_type`...

But the most common metadata pattern is `{}` (89 entries) or just `{"source": "openmemory"}`. Rich metadata exists in pockets but isn't systematic.

## Assessment: Valid or Over the Top?

**The design is valid. The execution has gaps.**

PostgreSQL + pgvector is the right technology choice. One database with structured queries, full-text search, vector similarity, and JSONB metadata — that's exactly what you need. The schema design is thoughtful (access tracking, priority, scope, tags). The backup system is production-grade.

But the system is running at maybe 40% of its potential:

| Capability | Design | Reality |
|------------|--------|---------|
| Vector search | ✅ Schema ready | 🔴 Function disabled |
| Hybrid search | ✅ Function exists | 🔴 FTS-only |
| CRUD | ✅ PostgreSQL supports it | 🔴 CLI is read-only |
| Graph | ✅ Intended | 🔴 Not built |
| Access tracking | ✅ Columns exist | 🔴 Never written |
| Unified store | ✅ Goal stated | 🔴 3 separate stores |
| Data quality | ✅ Indexes ready | 🔴 58% duplicates |

**It's not over the top — it's under-finished.**

## Recommended Path Forward

### Option A: Clean & Fix (Quick Wins)

Deduplicate the 1,868 duplicates. Fix the `hybrid_search()` function to actually use vectors. Add CRUD commands to pghmem. Fix the corrupted tags. **Effort: 2-3 hours. Impact: Immediate.**

### Option B: Consolidate Into PostgreSQL

Move flows, context-registry, skill tracking, and tool tracking all into PostgreSQL tables. One database, one CLI, one backup system. Matches the original "one place" vision. **Effort: 4-5 hours. Impact: Architectural.**

### Option C: Add Graph Layer

Create a `memory_relationships` table linking memories to each other. Enable queries like "what decisions led to this action?" and "what skills were used in this flow?" **Effort: 2-3 hours on top of Option B. Impact: Analytical.**

### Option D: Full Rebuild

Clean slate with proper schema design incorporating all goals. Risk of over-engineering but cleanest result. **Effort: 6-8 hours. Impact: Complete.**

### Option E: Minimal Viable Fix

Just deduplicate and fix hybrid search. Get the basics working before adding more. **Effort: 1-2 hours. Impact: Foundational.**

**My recommendation: Option B + deduplication from Option A.** This gives you the "one place" you wanted without over-engineering. The PostgreSQL infrastructure is already there — you just need to move the stragglers in and clean the data.

## What Good Looks Like

After fixes, the system should support:

```bash
# Semantic search (actually using vectors)
pghmem search "what did we decide about authentication" --semantic

# Metadata queries
pghmem search --metadata '{"category": "blog_post"}'

# CRUD operations
pghmem update <id> --add-tag "important" --priority 8
pghmem delete <id>
pghmem get <id>

# Graph queries
pghmem related <id>          # What's connected to this memory?
pghmem chain <id>            # Follow the decision chain

# Flow analysis
pghmem flows --active        # Current flows
pghmem flows --skill hugo    # Flows that used Hugo skill

# Analytics
pghmem stats --quality       # Data quality report
pghmem stats --usage         # Most accessed memories
pghmem stats --gaps          # What's not being tracked
```

The foundation is solid. The wiring needs finishing.

---

*Analysis performed 2026-03-22. Memory system: PostgreSQL 16 + pgvector, 3,217 memories, 32MB, running on ubuntu4.*