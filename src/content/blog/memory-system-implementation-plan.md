---
pubDatetime: 2026-03-22T21:59:45Z
title: "Memory System Implementation Plan: From 40% to 95%"
postSlug: "memory-system-implementation-plan"
description: "A comprehensive 7-phase plan to fix the PostgreSQL pgvector memory system — addressing duplicates, broken hybrid search, missing CRUD, and fragmented tracking."
tags:
  - implementation-plan
  - architecture
  - memory
  - pgvector
  - postgresql
---

After the [Memory System Analysis](/posts/memory-system-analysis-state-of-play/) revealed the system running at ~40% capacity, this implementation plan addresses every identified gap. The goal: bring PostgreSQL + pgvector memory from broken-but-promising to fully operational.

<!--more-->

## Executive Summary

| Current State | Target State |
|---------------|--------------|
| 3,217 memories (42% unique) | ~1,400 memories (100% unique) |
| 86% embedding coverage | 99%+ coverage |
| Hybrid search broken | Working RRF search |
| Read-only CLI | Full CRUD |
| 3 separate stores | 1 PostgreSQL database |

**Total Effort**: 8-12 hours over 2-3 weeks

---

## Phase 1: Data Quality (Critical)

**Effort**: 2-3 hours

### The Problem

| Issue | Count | Severity |
|-------|-------|----------|
| Duplicate content | 1,868 (58%) | Critical |
| Corrupted JSON tags | 1,378 | Medium |
| Empty content | 240 | Medium |
| "Session checkpoint" spam | 360 | Low |

### The Solution

```sql
-- Deduplicate: keep most complete version
CREATE TEMP TABLE dup_groups AS
SELECT 
    array_agg(id ORDER BY 
        jsonb_array_length(metadata) DESC,
        array_length(tags, 1) DESC NULLS LAST,
        length(content) DESC
    ) as ids,
    content,
    COUNT(*) as dup_count
FROM memories
GROUP BY content
HAVING COUNT(*) > 1;

-- Delete all but the best version
DELETE FROM memories
WHERE id IN (SELECT unnest(ids[2:]) FROM dup_groups);

-- Fix JSON string tags
UPDATE memories
SET tags = (
    SELECT array_agg(elem::text)
    FROM jsonb_array_elements_text(tags::text::jsonb) elem
)
WHERE tags::text LIKE '["%';

-- Remove spam and empty
DELETE FROM memories 
WHERE content LIKE 'Session checkpoint%' AND memory_type = 'exchange';

DELETE FROM memories 
WHERE content = '' OR content IS NULL OR length(trim(content)) = 0;
```

**Result**: ~1,400 clean, unique memories

---

## Phase 2: Fix Core Functionality (Critical)

**Effort**: 2-3 hours

### 2.1 Enable Hybrid Search

The `hybrid_search()` function exists but only does FTS. The vector path was commented out with a note: *"For now, just use FTS since no embeddings."* But we have 2,766 embeddings.

**Solution**: Implement Reciprocal Rank Fusion (RRF)

```sql
CREATE OR REPLACE FUNCTION hybrid_search(
    search_query text,
    query_embedding vector(768),  -- nomic-embed-text dimensions
    search_limit integer DEFAULT 10,
    rrf_k integer DEFAULT 60
)
RETURNS TABLE(
    id bigint,
    memory_id varchar,
    content text,
    memory_type varchar,
    metadata jsonb,
    score double precision,
    match_type text
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    WITH fts_results AS (
        SELECT m.id, m.memory_id, m.content, m.memory_type, m.metadata,
            ts_rank(to_tsvector('english', m.content), plainto_tsquery(search_query)) as score,
            ROW_NUMBER() OVER (ORDER BY ts_rank(to_tsvector('english', m.content), plainto_tsquery(search_query)) DESC) as rank
        FROM memories m
        WHERE to_tsvector('english', m.content) @@ plainto_tsquery(search_query)
        LIMIT search_limit * 2
    ),
    vector_results AS (
        SELECT m.id, m.memory_id, m.content, m.memory_type, m.metadata,
            1 - (m.embedding <=> query_embedding) as score,
            ROW_NUMBER() OVER (ORDER BY m.embedding <=> query_embedding) as rank
        FROM memories m
        WHERE m.embedding IS NOT NULL
        ORDER BY m.embedding <=> query_embedding
        LIMIT search_limit * 2
    ),
    rrf AS (
        SELECT id, memory_id, content, memory_type, metadata,
            SUM(COALESCE(1.0 / (rrf_k + rank), 0)) as rrf_score
        FROM (
            SELECT *, rank FROM fts_results
            UNION ALL
            SELECT *, rank FROM vector_results
        ) combined
        GROUP BY id, memory_id, content, memory_type, metadata
    )
    SELECT r.id, r.memory_id, r.content, r.memory_type, r.metadata,
        r.rrf_score::double precision,
        CASE 
            WHEN f.id IS NOT NULL AND v.id IS NOT NULL THEN 'hybrid'
            WHEN f.id IS NOT NULL THEN 'fts'
            ELSE 'vector'
        END as match_type
    FROM rrf r
    LEFT JOIN fts_results f ON r.id = f.id
    LEFT JOIN vector_results v ON r.id = v.id
    ORDER BY rrf_score DESC
    LIMIT search_limit;
END;
$$;
```

### 2.2 Generate Missing Embeddings

**Decision**: Use local Ollama with `nomic-embed-text` (768 dimensions, free, fast)

```python
# scripts/generate-embeddings.py

import psycopg2
import requests

OLLAMA_URL = "http://localhost:11434/api/embeddings"
MODEL = "nomic-embed-text"

def generate_embedding(text):
    response = requests.post(
        OLLAMA_URL,
        json={"model": MODEL, "prompt": text}
    )
    return response.json()["embedding"]

def main():
    conn = psycopg2.connect(...)
    cur = conn.cursor()
    
    # Get memories without embeddings
    cur.execute("""
        SELECT id, content FROM memories 
        WHERE embedding IS NULL 
        ORDER BY created_at DESC
    """)
    missing = cur.fetchall()
    
    print(f"Generating embeddings for {len(missing)} memories...")
    
    for i, (mem_id, content) in enumerate(missing):
        embedding = generate_embedding(content)
        cur.execute(
            "UPDATE memories SET embedding = %s WHERE id = %s",
            (embedding, mem_id)
        )
        if i % 100 == 0:
            conn.commit()
            print(f"Processed {i}/{len(missing)}...")
    
    conn.commit()
    print("Done!")

if __name__ == "__main__":
    main()
```

**Note**: Switching from Jina AI (1024-dim) to Ollama (768-dim) requires regenerating ALL embeddings for consistency.

---

## Phase 3: Add CRUD to CLI (High)

**Effort**: 1-2 hours

### The Problem

`pghmem` supports: `search`, `list`, `stats`, `recent`

Missing: `get`, `update`, `delete`, `tag`

### The Solution

```python
# Add to /usr/local/bin/pghmem

def cmd_get(args):
    """Get a single memory by ID."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM memories WHERE memory_id = %s", (args.memory_id,))
    result = cur.fetchone()
    conn.close()
    if result:
        print_memory(result, full=True)

def cmd_update(args):
    """Update a memory."""
    conn = get_connection()
    cur = conn.cursor()
    updates = []
    params = []
    
    if args.content:
        updates.append("content = %s")
        params.append(args.content)
    if args.add_tags:
        updates.append("tags = array_cat(tags, %s)")
        params.append(args.add_tags.split(","))
    if args.priority:
        updates.append("priority = %s")
        params.append(int(args.priority))
    
    if updates:
        params.append(args.memory_id)
        cur.execute(f"UPDATE memories SET {', '.join(updates)}, updated_at = NOW() WHERE memory_id = %s", params)
        conn.commit()
    conn.close()

def cmd_delete(args):
    """Delete a memory."""
    if not args.force:
        confirm = input(f"Delete {args.memory_id}? [y/N] ")
        if confirm.lower() != 'y':
            return
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM memories WHERE memory_id = %s", (args.memory_id,))
    conn.commit()
    conn.close()

def cmd_tag(args):
    """Manage tags."""
    conn = get_connection()
    cur = conn.cursor()
    
    if args.list:
        cur.execute("SELECT unnest(tags) as tag, COUNT(*) FROM memories GROUP BY tag ORDER BY COUNT DESC")
        for row in cur.fetchall():
            print(f"{row['tag']}: {row['count']}")
    elif args.search:
        cur.execute("SELECT memory_id, content FROM memories WHERE %s = ANY(tags) LIMIT 20", (args.search,))
        for row in cur.fetchall():
            print(f"{row['memory_id']}: {row['content'][:60]}...")
    conn.close()
```

**New Commands**:

```bash
pghmem get <id>                      # Retrieve by ID
pghmem update <id> --content "..."   # Change content
pghmem update <id> --add-tags "x,y"  # Add tags
pghmem update <id> --priority 8      # Set priority
pghmem delete <id> [--force]         # Remove memory
pghmem tag --list                    # All tags with counts
pghmem tag --search important        # Memories with tag
```

---

## Phase 4: Activate Access Tracking (Medium)

**Effort**: 30 minutes

### The Problem

Schema has `access_count` and `last_accessed_at` columns — but every row shows 0 accesses.

### The Solution

```python
def update_access(memory_ids):
    """Update access tracking for retrieved memories."""
    if not memory_ids:
        return
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE memories 
        SET access_count = access_count + 1,
            last_accessed_at = NOW()
        WHERE memory_id = ANY(%s)
    """, (memory_ids,))
    conn.commit()
    conn.close()

# Call after every search/list/get/recent
def cmd_search(args):
    # ... existing search logic ...
    update_access([m['memory_id'] for m in results])
```

---

## Phase 5: Consolidate Tracking (High)

**Effort**: 2-3 hours

### 5.1 Migrate Flows to PostgreSQL

Currently in `flows.db` (SQLite) — move to main database.

```sql
CREATE TABLE flows (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    trigger TEXT NOT NULL,
    input_data JSONB DEFAULT '{}',
    state JSONB DEFAULT '{}',
    gates JSONB DEFAULT '[]',
    tasks JSONB DEFAULT '[]',
    tracking JSONB DEFAULT '[]',
    output JSONB DEFAULT '{}',
    status TEXT DEFAULT 'pending',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ
);
```

### 5.2 Add Skill Usage Tracking

```sql
CREATE TABLE skill_usage (
    id SERIAL PRIMARY KEY,
    skill_name TEXT NOT NULL,
    trigger_source TEXT,
    session_id TEXT,
    duration_ms INTEGER,
    success BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 5.3 Add Tool Usage Tracking

```sql
CREATE TABLE tool_usage (
    id SERIAL PRIMARY KEY,
    tool_name TEXT NOT NULL,
    agent_type TEXT,
    session_id TEXT,
    duration_ms INTEGER,
    success BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 5.4 Store Deferred Topics in PostgreSQL

Deferred topics become `decision` type memories:

```python
def defer_to_postgresql(topic, time_spec=None):
    metadata = {
        "deferred": True,
        "time_spec": time_spec,
        "status": "pending"
    }
    
    memory_id = capture_to_pg(
        content=f"Deferred: {topic}",
        memory_type="decision",
        tags=["deferred", "reminder"],
        metadata=metadata
    )
    return memory_id
```

Query deferred:
```bash
pghmem search "deferred" --type decision
```

---

## Phase 6: Add Graph Relationships (Medium)

**Effort**: 2-3 hours

### The Problem

Memories are isolated islands. No way to say "this decision led to that action."

### The Solution

```sql
CREATE TABLE memory_relationships (
    id SERIAL PRIMARY KEY,
    source_id TEXT NOT NULL REFERENCES memories(memory_id) ON DELETE CASCADE,
    target_id TEXT NOT NULL REFERENCES memories(memory_id) ON DELETE CASCADE,
    relationship_type TEXT NOT NULL,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(source_id, target_id, relationship_type)
);
```

**Relationship Types**:

| Type | Meaning |
|------|---------|
| `led_to` | Causal: Decision → Action |
| `references` | Mentions: Conversation → Decision |
| `supersedes` | Replaces: New → Old |
| `part_of` | Hierarchy: Action → Flow |
| `uses` | Dependency: Flow → Skill |

**CLI**:
```bash
pghmem relate <source> <target> --type led_to
pghmem related <memory_id>
pghmem chain <memory_id>
```

---

## Phase 7: Update Reports (Low)

**Effort**: 30 minutes

The 8-hour report (`mem-h8-report.py`) still queries the old OpenMemory SQLite container. Update to query PostgreSQL directly.

```python
def get_pg_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        user="memory_user",
        password="...",
        dbname="memory_db"
    )
```

---

## Implementation Timeline

### Week 1: Foundation

| Day | Phase | Task |
|-----|-------|------|
| 1 | 1 | Deduplicate + fix tags |
| 2 | 2 | Hybrid search + embeddings |
| 3 | 3 | CRUD CLI |

### Week 2: Consolidation

| Day | Phase | Task |
|-----|-------|------|
| 4 | 5 | Migrate flows + deferred |
| 5 | 5 | Skill + tool tracking |
| 6 | 4 | Access tracking |

### Week 3: Enhancement

| Day | Phase | Task |
|-----|-------|------|
| 7 | 6 | Graph relationships |
| 8 | 7 | Report fixes + docs |

---

## Success Criteria

| Phase | Deliverable |
|-------|-------------|
| 1 | ~1,400 unique memories, clean tags |
| 2 | Hybrid search working, 99%+ embeddings |
| 3 | Full CRUD in `pghmem` CLI |
| 4 | Access tracking active |
| 5 | All tracking in PostgreSQL |
| 6 | Memory relationships queryable |
| 7 | Reports use PostgreSQL |

---

## Rollback Safety

Before each phase:

```bash
docker exec pgvector-memory pg_dump -U memory_user memory_db > \
    [system resource]
```

---

## Decisions Made

| Question | Decision |
|----------|----------|
| Dedup strategy | Keep most complete version |
| Embedding model | Local Ollama (nomic-embed-text, 768-dim) |
| Implementation | All phases in sequence |

---

*Plan version 1.0 — created 2026-03-22. Full technical details in [implementation-plan.md](http://ubuntu4:8080/editor/opencode/docs/plans/memory-system-implementation-plan.md).*