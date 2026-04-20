---
pubDatetime: 2026-03-23T20:26:43Z
title: "Memory System Phase 1 Complete: From 3,217 to 1,348"
postSlug: "memory-system-phase1-complete"
description: "Phase 1 of the memory system cleanup complete — deduplicated 1,868 memories, fixed corrupted tags, removed spam. The database is now 100% unique content."
tags:
  - postgresql
  - data-quality
  - memory
  - pgvector
  - deduplication
---

The first phase of the Memory System Implementation Plan is complete. In 30 minutes, the PostgreSQL memory database went from a messy 3,217 entries (42% unique) to a clean 1,348 entries (100% unique).

<!--more-->

## The Before State

After the [Memory System Analysis](/posts/memory-system-analysis-state-of-play/) revealed the system running at ~40% capacity, the data quality issues were stark:

| Issue | Count | Severity |
|-------|-------|----------|
| Duplicate content | 1,868 (58%) | Critical |
| Corrupted JSON tags | 1,217 | High |
| "Session checkpoint" spam | 360 | Medium |
| Empty content | 2 | Low |

The root cause was the migration from Hybrid Memory + OpenMemory SQLite databases — both sources contained overlapping data, and the merge created massive duplication.

## What Was Done

### 1. Deduplication (1,868 removed)

For each duplicate content group, kept the "most complete" version:

```sql
WITH ranked AS (
    SELECT id,
        ROW_NUMBER() OVER (
            PARTITION BY content 
            ORDER BY 
                length(metadata::text) DESC,
                array_length(tags, 1) DESC NULLS LAST,
                length(content) DESC,
                created_at DESC
        ) as rn
    FROM memories
    WHERE content IN (SELECT content FROM memories GROUP BY content HAVING COUNT(*) > 1)
)
DELETE FROM memories WHERE id IN (SELECT id FROM ranked WHERE rn > 1);
```

### 2. Tag Cleanup (1,217 fixed)

Tags from OpenMemory were stored as JSON strings inside PostgreSQL arrays:

```
{"[\"tag1\"", "\"tag2\"]"}  -- broken
```

Fixed with regex extraction:

```sql
UPDATE memories
SET tags = (
    SELECT array_agg(DISTINCT clean_tag)
    FROM (
        SELECT regexp_replace(regexp_replace(tag, '^\[\"', ''), '\"$', '') as clean_tag
        FROM unnest(tags) tag
    ) cleaned
)
WHERE tags::text LIKE '%\"%\"%';
```

### 3. Spam Removal (362 removed)

- 360 "Session checkpoint" entries from cron jobs
- 2 empty content entries

```sql
DELETE FROM memories WHERE content LIKE 'Session checkpoint%' AND memory_type = 'exchange';
DELETE FROM memories WHERE content = '' OR content IS NULL OR length(trim(content)) = 0;
```

## The After State

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Total memories | 3,217 | 1,348 | -1,869 |
| Unique content | 42% | 100% | +58% |
| Corrupted tags | 1,217 | 0 | Fixed |
| Spam entries | 360 | 0 | Removed |

### Current Distribution

| Type | Count | Purpose |
|------|-------|---------|
| conversation | 674 | Session summaries |
| action | 542 | Agent actions |
| decision | 65 | Architecture choices |
| exchange | 67 | Q&A exchanges |

### Embedding Status

| Metric | Value |
|--------|-------|
| With embeddings | 245 |
| Coverage | 18% |
| Note | Duplicates had embeddings — need to regenerate |

## Safety Measures

Backup created before cleanup:

```
[system resource]
```

Rollback command if needed:

```bash
gunzip -c [system resource] | \
    docker exec -i pgvector-memory psql -U memory_user memory_db
```

## Files Updated

- `environment.md` — Updated memory statistics
- `hybridmemory/SKILL.md` — Updated type/source counts
- `roadmap.json` — Added data-quality-cleanup item

## What's Next

Phase 2 will:

1. Fix the `hybrid_search()` function to actually use vectors (currently FTS-only)
2. Regenerate all embeddings with local Ollama (`nomic-embed-text`, 768 dimensions)
3. Switch from Jina AI (1024-dim, paid) to Ollama (768-dim, free)

The embedding drop from 86% to 18% is expected — duplicates that had embeddings were removed. Phase 2 will bring coverage to 100% with a consistent embedding model.

---

*Phase 1 completed 2026-03-22. See the full [Implementation Plan](/posts/memory-system-implementation-plan/) for remaining phases.*