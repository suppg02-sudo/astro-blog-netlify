---
pubDatetime: 2026-03-13T00:05:11Z
title: "PostgreSQL + pgvector Migration Plan: Consolidating Memory Systems"
postSlug: "postgresql-pgvector-migration-plan-consolidating-m"
description: "PostgreSQL + pgvector Migration Plan: Consolidating Memory Systems"
tags:
  - postgresql
  - memory-system
  - migration
  - pgvector
  - docker
---

## Overview

This post documents the planning process for migrating from two SQLite memory databases to a unified PostgreSQL + pgvector system. The goal is to consolidate 2,800+ memories into a single scalable database with semantic search capabilities.

## Current State

Two separate memory systems exist:

| System | Records | Purpose |
|--------|---------|---------|
| **Hybrid Memory** (SQLite) | 1,413 | Fast local retrieval, CLI access |
| **OpenMemory** (SQLite + MCP) | 1,419 | Semantic search with embeddings |

Both systems work but have different schemas, access patterns, and limitations. Consolidating them simplifies maintenance and enables unified hybrid search.

## Target Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    POSTGRESQL + PGVECTOR                     │
│                                                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  memories   │  │   HNSW      │  │   GIN (FTS)         │  │
│  │  table      │  │   index     │  │   index             │  │
│  │  2,800+     │  │   vector    │  │   full-text         │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
│                                                              │
│  Features:                                                   │
│  - Vector search (Google text-embedding-004, 768 dims)      │
│  - Full-text search (PostgreSQL FTS)                        │
│  - Hybrid search (Reciprocal Rank Fusion)                   │
│  - JSONB metadata queries                                   │
└─────────────────────────────────────────────────────────────┘
```

## Key Decisions

### Deployment
**Docker with host network** - Minimal latency (~0.1ms overhead vs bridge network's 1-2ms). For memory retrieval where embedding generation takes 50-200ms, Docker overhead is negligible.

### Embeddings
**Google text-embedding-004** (768 dimensions) - Free tier available, good quality, consistent across all memories. Regenerating all embeddings ensures uniformity.

### Index Strategy
**HNSW index** for 10K-100K scale:
- 40.5 QPS vs 2.6 for IVFFlat
- No rebuild needed for updates
- `m=16, ef_construction=64` for initial scale

### Transition
**Parallel run** - Keep both SQLite systems active during migration, switch after validation.

## Schema Design

Hybrid approach combining columns and JSONB:

```sql
CREATE TABLE memories (
    id BIGSERIAL PRIMARY KEY,
    memory_id VARCHAR(255) UNIQUE NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    embedding VECTOR(768),  -- Google text-embedding-004
    
    -- Stable fields as columns
    memory_type VARCHAR(50),
    scope VARCHAR(20),
    priority INT DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    
    -- Flexible metadata in JSONB
    metadata JSONB DEFAULT '{}',
    tags TEXT[] DEFAULT '{}',
    
    -- Full-text search column
    textsearch TSVECTOR GENERATED ALWAYS AS 
        (to_tsvector('english', content)) STORED
);
```
```sql
-- Vector index
CREATE INDEX idx_memories_embedding ON memories 
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);
```
-- FTS index
CREATE INDEX idx_memories_textsearch ON memories USING gin(textsearch);
-- JSONB index
CREATE INDEX idx_memories_metadata ON memories USING gin(metadata);
```
```

## Implementation Phases

### Phase 1: Setup
1. Deploy pgvector Docker container with host network
2. Create schema with indexes
3. Configure PostgreSQL parameters (shared_buffers, work_mem)
4. Add PgBouncer for connection pooling

### Phase 2: Migration
1. Create Python migration script with batch inserts
2. Generate Google embeddings for all 2,800+ memories
3. Migrate both SQLite databases
4. Build HNSW index after full data load

### Phase 3: Integration
1. Update hmem CLI to use PostgreSQL
2. Update capture_conversation.py
3. Add hybrid search with Reciprocal Rank Fusion
4. Configure iterative scan for filtered queries

### Phase 4: Validation
1. Run search quality tests (20 queries, >80% recall)
2. Benchmark performance vs SQLite
3. Parallel run for 1 week
4. Decommission SQLite (preserve backups)

## Hybrid Search Implementation

Combining vector and keyword search with Reciprocal Rank Fusion:

```sql
WITH text_search AS (
    SELECT id, 
           ROW_NUMBER() OVER (
               ORDER BY ts_rank_cd(textsearch, query) DESC
           ) AS rank
    FROM memories, plainto_tsquery('search term') query
    WHERE textsearch @@ query
    LIMIT 20
),
vector_search AS (
    SELECT id, 
           ROW_NUMBER() OVER (
               ORDER BY embedding <=> '[0.1,0.2,...]'::vector
           ) AS rank
    FROM memories
    LIMIT 20
)
SELECT COALESCE(t.id, v.id) AS id,
       m.content,
       1.0 / (60 + COALESCE(t.rank, 1000)) + 
       1.0 / (60 + COALESCE(v.rank, 1000)) AS score
FROM text_search t
FULL OUTER JOIN vector_search v ON t.id = v.id
JOIN memories m ON m.id = COALESCE(t.id, v.id)
ORDER BY score DESC
LIMIT 10;
```

## Scale Considerations

| Scale | RAM | Storage | Index Strategy |
|-------|-----|---------|----------------|
| 10K-100K | 8 GB | 50 GB | HNSW (m=16) |
| 100K-1M | 32 GB | 500 GB | HNSW (m=24) |
| 1M+ | 64+ GB | 1+ TB | pgvectorscale |

## Files Created

| File | Purpose |
|------|---------|
| `.sisyphus/plans/pgvector-migration.md` | Full implementation plan with TODOs |
| `.sisyphus/drafts/postgresql-pgvector-migration-research.md` | Research notes and code snippets |

## Next Steps

1. Run `/start-work pgvector-migration` to begin execution
2. Or manually work through Phase 1 tasks
3. Estimated timeline: 1-2 weeks for full migration

## Lessons from Planning

- **Docker host network** eliminates latency concerns
- **Regenerating embeddings** ensures consistency across merged datasets
- **HNSW index** is the right choice for current scale (10K-100K)
- **Parallel transition** reduces risk during migration
- **JSONB + columns hybrid** balances flexibility and performance