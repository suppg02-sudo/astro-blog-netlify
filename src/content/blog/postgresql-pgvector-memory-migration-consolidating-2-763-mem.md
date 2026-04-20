---
pubDatetime: 2026-03-13T03:02:58Z
title: "PostgreSQL + pgvector Memory Migration: Consolidating 2,763 Memories"
postSlug: "postgresql-pgvector-memory-migration-consolidating-2-763-mem"
description: "PostgreSQL + pgvector Memory Migration: Consolidating 2,763 Memories"
tags:
  - memory-system
  - migration
  - pgvector
  - postgresql
  - consolidation
---

## Overview

Migrated two SQLite memory databases into a single PostgreSQL + pgvector database, consolidating 2,763 memories with full-text and vector search capabilities.

## Before: Two Separate Systems

| System | Database | Count |
|--------|----------|-------|
| Hybrid Memory | SQLite | 1,387 |
| OpenMemory | SQLite | 1,375 |
| **Total** | | **2,762** |

Both worked independently but had different schemas, access patterns, and no unified search.

## After: Unified PostgreSQL

| Metric | Value |
|--------|-------|
| Total memories | 2,763 |
| With embeddings | 591 (Jina AI) |
| Search types | FTS + Vector + Hybrid |
| Backup | Every 3 hours |

## Implementation

### 1. Docker Setup

```yaml
# docker-compose.yml
services:
  postgres:
    image: pgvector/pgvector:pg17
    network_mode: host
    environment:
      POSTGRES_USER: memory_user
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: memory_db
```

### 2. Schema Design

```sql
CREATE TABLE memories (
    id BIGSERIAL PRIMARY KEY,
    memory_id VARCHAR(255) UNIQUE,
    content TEXT NOT NULL,
    embedding VECTOR(1024),  -- Jina V3
    memory_type VARCHAR(50),
    metadata JSONB,
    tags TEXT[],
    created_at TIMESTAMPTZ
);

-- FTS index
CREATE INDEX idx_fts ON memories 
    USING gin(to_tsvector('english', content));

-- Vector index (HNSW)
CREATE INDEX idx_emb ON memories 
    USING hnsw (embedding vector_cosine_ops)
    WITH (m = 16, ef_construction = 64);
```

### 3. Migration Script

Python script that:
- Read both SQLite databases
- Mapped schemas (memory_type, tags, metadata)
- Batch inserted into PostgreSQL
- Handled timestamp conversion (milliseconds → ISO)

### 4. CLI Tool

```bash
# New unified CLI
pghmem stats              # 2,763 memories
pghmem search "docker"    # FTS search
pghmem list --type decision
pghmem recent -n 10
```

## Search Capabilities

### Full-Text Search

```sql
SELECT * FROM memories
WHERE to_tsvector('english', content) @@ plainto_tsquery('docker backup')
ORDER BY ts_rank(...) DESC;
```

Results: 2 matches for "docker backup"

### Vector Similarity

```sql
SELECT * FROM memories
WHERE embedding IS NOT NULL
ORDER BY embedding <-> (SELECT embedding FROM memories WHERE memory_id = '...')
LIMIT 5;
```

591 memories have embeddings (Jina AI, 1024 dimensions)

### Hybrid Search (RRF)

```sql
-- Combines FTS + vector with Reciprocal Rank Fusion
SELECT * FROM hybrid_search('memory system', 10);
```

## Automation

| Task | Schedule |
|------|----------|
| Backup | Every 3 hours |
| Embedding generation | Background (paused) |
| Capture script | On-demand |

## Files Created

| File | Purpose |
|------|---------|
| `/media/docker/pgvector/docker-compose.yml` | Container config |
| `/media/docker/pgvector/init.sql` | Schema |
| `/media/docker/pgvector/migrate_to_pgvector.py` | Migration |
| `/media/docker/pgvector/pghmem.py` | CLI tool |
| `[system resource] | Backup automation |

## Lessons Learned

1. **Schema mismatch**: Jina V3 returns 1024 dims, not 768 - had to alter column
2. **Timestamps**: OpenMemory uses milliseconds, Hybrid uses ISO strings
3. **Deduplication**: Used `memory_id` prefix (`om-`) to avoid collisions
4. **Index timing**: Build indexes after data load, not before

## Status

- PostgreSQL container: Running (healthy)
- Memories: 2,763
- Embeddings: 591 (generating more)
- Search: FTS + Vector + Hybrid working
- Backup: Automated

## Next Steps

- Continue embedding generation (2,172 remaining)
- Consider switching capture scripts to PostgreSQL
- Monitor performance at scale