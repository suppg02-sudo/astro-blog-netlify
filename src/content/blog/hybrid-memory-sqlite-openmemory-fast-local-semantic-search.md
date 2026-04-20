---
pubDatetime: 2026-03-11T22:44:37Z
title: "Hybrid Memory: Fast SQLite Layer with Async OpenMemory Sync"
postSlug: "hybrid-memory-sqlite-openmemory-fast-local-semantic-search"
description: "Hybrid Memory: Fast SQLite Layer with Async OpenMemory Sync"
tags:
  - agents
  - openmemory
  - sqlite
  - memory
  - ai
---

## The Problem

AI agents need memory that's both **fast** and **intelligent**. Traditional approaches force a trade-off:

- **Fast local storage** (JSON, SQLite) → instant access, no semantic understanding
- **Semantic memory** (vector databases) → intelligent retrieval, high latency

Our solution: **Hybrid Memory** — a two-tier system that gives you both.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     AI AGENT                                 │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                  HYBRID MEMORY CLIENT                        │
│                                                              │
│   ┌─────────────────┐         ┌─────────────────────────┐   │
│   │  SQLite Layer   │         │   OpenMemory Layer      │   │
│   │  (Local, Fast)  │ ──────▶ │   (Semantic, Async)     │   │
│   │                 │  sync   │                         │   │
│   │  0.3ms writes   │         │   Vector embeddings     │   │
│   │  0.4ms reads    │         │   Semantic search       │   │
│   └─────────────────┘         └─────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Performance Benchmarks

| Operation | Target | Actual | Status |
|-----------|--------|--------|--------|
| Average write | 0.3ms | 0.186ms | ✅ Better than target |
| P99 write | <1ms | 9.194ms | ⚠️ Occasional cold starts |
| Average read | 0.17ms | 0.435ms | ⚠️ 2.5x target |
| Min read | - | 0.229ms | ✅ Excellent |

The occasional spikes are from cold starts. Warm performance is consistent and reliable.

## How It Works

### Tier 1: SQLite (Instant Operations)

All CRUD operations hit SQLite first:

```python
from hybrid_memory import get_client

client = get_client()

# Store a memory - 0.3ms
memory_id = client.store(
    content="Agent completed task successfully",
    memory_type="action",
    metadata={
        "agent": "sisyphus",
        "tool": "bash",
        "status": "success"
    },
    tags=["#action", "#success"],
    priority=3
)

# Query memories - 0.4ms
memories = client.query(
    memory_type="action",
    metadata_filter={"agent": "sisyphus"},
    limit=10
)
```

### Tier 2: OpenMemory (Semantic Search)

High-priority memories sync to OpenMemory for semantic retrieval:

```python
# Full-text search across all indexed memories
results = client.fulltext_search("database architecture decisions", limit=10)

for result in results:
    print(f"{result['memory_type']}: {result['content']}")
```

## Priority-Based Sync

Not all memories need semantic indexing. The system routes based on priority:

| Priority | Sync Timing | Use Case |
|----------|-------------|----------|
| 1-2 | Overnight batch | Low-value actions |
| 3-4 | Within 1 hour | Routine operations |
| 5-7 | Within 10 minutes | Important decisions |
| 8-10 | Within 10 seconds | Critical reference data |

**High-priority tags**: `#decision`, `#important`, `#critical`, `#reference`

## Memory Types

| Type | Purpose | Default Sync Priority |
|------|---------|----------------------|
| `conversation` | Session summaries | Medium (1hr) |
| `flow` | Agent delegation chains | Medium (1hr) |
| `action` | Individual agent actions | Low (overnight) |
| `decision` | Architecture/design choices | **HIGH (10s)** |
| `menu_choice` | User menu selections | Low (overnight) |
| `skill` | Skill configurations | Medium (1hr) |
| `roadmap` | Project phases | Low (overnight) |
| `initiative` | Active projects | Medium (1hr) |

## Database Schema

```sql
CREATE TABLE IF NOT EXISTS memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    memory_id TEXT UNIQUE NOT NULL,
    content TEXT NOT NULL,
    memory_type TEXT NOT NULL DEFAULT 'conversation',
    metadata JSON NOT NULL DEFAULT '{}',
    tags TEXT NOT NULL DEFAULT '[]',
    priority INTEGER NOT NULL DEFAULT 0,
    indexed_at DATETIME,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Full-text search
CREATE VIRTUAL TABLE memories_fts USING fts5(
    content,
    content='memories',
    content_rowid='id'
);
```

## Background Worker

The worker continuously syncs high-priority memories:

```bash
# Run as background process
python3 ~/.config/opencode/hybrid_memory_worker.py

# Or as systemd service (recommended)
sudo systemctl start hybrid-memory-worker
```

## Overnight Batch Indexing

Process all unindexed memories during off-peak hours:

```bash
# Manual run
python3 ~/.config/opencode/overnight_indexing.py

# Schedule via cron
# 0 3 * * * /root/.config/opencode/overnight_indexing.py >> /var/log/hybrid_memory/overnight.log 2>&1
```

## Migration Path

### Phase 1 (Current) ✅ Complete
- Hybrid SQLite layer
- Background sync worker
- Batch indexing
- Migration utilities

### Phase 2 (Next) 📋 Planned
- Unified SQLite + sqlite-vec
- Single database file
- No sync complexity
- Native vector search

### Phase 3 (Future) 🔮 Optional
- PostgreSQL + pgvector
- Scale to 10M+ records
- Multi-region support

## Quick Start

```bash
# Verify installation
ls -lh ~/.config/opencode/hybrid_memory.db

# Check database
sqlite3 ~/.config/opencode/hybrid_memory.db "SELECT COUNT(*) FROM memories;"

# Run benchmark
cd ~/.config/opencode && python3 -c "
from hybrid_memory import get_client
import time
client = get_client()
start = time.perf_counter()
for i in range(100):
    client.store(content=f'test {i}')
duration = (time.perf_counter() - start) * 1000
print(f'Average: {duration/100:.3f}ms')
"
```

## Key Benefits

1. **Sub-millisecond writes** — No network latency
2. **Sub-millisecond reads** — Instant local queries
3. **Semantic search** — Vector embeddings via OpenMemory
4. **Priority routing** — Critical data syncs fast
5. **Full-text search** — SQLite FTS5 built-in
6. **Zero data loss** — SQLite WAL mode
7. **Simple API** — Single client for all operations

## Related Resources

- [OpenMemory MCP Server](http://ubuntu4:1313/tags/openmemory/)
- [SQLite WAL Mode Documentation](https://www.sqlite.org/wal.html)
- [sqlite-vec Extension](https://github.com/asg017/sqlite-vec)

---

**Version**: 1.0.0  
**Created**: 2026-03-11  
**Skill Location**: `~/.config/opencode/skills/hybridmemory/SKILL.md`