---
pubDatetime: 2026-03-04T05:15:00Z
title: "Building an OpenMemory Intelligence System — From CRUD Discovery to Automated Reporting"
postSlug: "openmemory-system-build"
description: "How we built a complete memory management system for OpenMemory (CaviraOSS) — interactive menus, CRUD pattern discovery, legacy data migration, intelligence reporting, and automated blog publishing."
tags:
  - openmemory
  - cron
  - automation
  - memory-system
  - migration
  - telos
  - ai-infrastructure
  - hugo
---

> A complete build log of turning a basic memory store into a full intelligence platform with diagnostics, migration, reporting, and self-improvement suggestions.

## The Starting Point

OpenMemory (CaviraOSS) was running — an MCP server with SQLite backend, HSG (Hierarchical Semantic Graph), and 5 memory sectors. But it was a black box. No visibility into what was stored, no structured storage pattern, no reporting, and 307 legacy entries trapped in JSON files from an old context-registry system.

**Goal**: Make it observable, structured, self-reporting, and useful.

---

## Phase 1: The CRUD Pattern Discovery

The single most important discovery of this entire build: **the `content` field gets mangled by HSG, but the `metadata` field preserves JSON exactly as-is.**

This means:
- `content` → short searchable description (for semantic search)
- `metadata` → exact structured JSON (for precise data retrieval)
- `tags` → array of strings (for filtering)

```
openmemory_store(
  content: "decision: chose PostgreSQL for auth service",
  metadata: {
    "type": "decision",
    "topic": "database",
    "choice": "PostgreSQL",
    "rationale": "ACID compliance, team familiarity",
    "timestamp": "2026-03-04T05:00:00Z"
  },
  tags: ["decision", "database", "auth"]
)
```

This CRUD pattern unlocked everything that followed. Without it, OpenMemory was just a fuzzy text store. With it, it became a structured context database.

### 8 Context Types Defined

{{< chart >}}
{
  type: 'doughnut',
  data: {
    labels: ['conversation', 'roadmap', 'initiative', 'skill', 'decision', 'menu_choice', 'flow', 'workflow'],
    datasets: [{
      data: [1, 1, 1, 1, 1, 1, 1, 1],
      backgroundColor: ['#6366f1', '#22d3ee', '#f59e0b', '#ef4444', '#10b981', '#94a3b8', '#a855f7', '#ec4899']
    }]
  },
  options: {
    plugins: {
      title: { display: true, text: 'Supported Context Types', color: '#e2e8f0' },
      legend: { position: 'right', labels: { color: '#e2e8f0' } }
    }
  }
}
{{< /chart >}}

| Type | Purpose | When to Store |
|------|---------|---------------|
| `conversation` | Session summaries | End of significant sessions |
| `roadmap` | Project phases, milestones | Roadmap changes |
| `initiative` | Active projects, goals | New initiatives or status changes |
| `skill` | Skill configurations | Skill creation or modification |
| `decision` | Architecture decisions | After making design choices |
| `menu_choice` | User menu selections | After question tool interactions |
| `flow` | Action flows, delegations | After delegations or automated actions |
| `workflow` | Multi-step processes | Complex task completion |

---

## Phase 2: Interactive Memory Menu

{{< mermaid >}}
flowchart TD
    A[memory-menu.sh] --> B[Static Options 1-10]
    A --> C[Reports 11-13]
    A --> D[Memory Operations 14-16]
    A --> E[Other 17-18]
    
    B --> B1[Status & Health]
    B --> B2[Memory Analysis]
    C --> C1[Intelligence Report]
    C --> C2[Blog Generation]
    D --> D1[Add/Search]
    D --> D2[Backup]
{{< /mermaid >}}

Built `memory-menu.sh` — an interactive terminal menu with 18 options across 4 categories:

### Static Options (1-10)
| # | Option | What It Does |
|---|--------|-------------|
| 1 | Is OpenCode running | Container status, uptime, health check |
| 2 | MCP running | MCP endpoint test, protocol version, tool count |
| 3 | Last 5 memories | Fetches via MCP openmemory_list |
| 4 | How many memories | SQLite count + sector breakdown |
| 5 | Backup status | Latest backup age, size, 24hr check |
| 6 | Analyse + Check logs | Full diagnostics (DB analysis, container logs, API logs, MCP status) |
| 7 | Check memory config | Version, tier, dimensions, embedding provider, sector config with decay lambdas |
| 8 | Suggest improvements | Analyses config and gives actionable suggestions |
| 9 | Performance details | Health metrics, sector stats, temporal graph, storage sizes |
| 10 | Open dashboard | Running status + URLs for all 6 dashboard pages |

### Reports (11-13)
| # | Option | Output |
|---|--------|--------|
| 11 | 📊 Full Intelligence Report | Terminal — comprehensive stats with improvement suggestions |
| 12 | 📝 Generate & publish blog | Hugo blog post with tables, charts, suggestions |
| 13 | 📈 JSON report | Machine-readable for dashboards |

### Memory Operations (14-16)
| # | Option | Action |
|---|--------|--------|
| 14 | Add a memory | Interactive store with sector/salience selection |
| 15 | Retrieve/Search | Semantic query with configurable limit |
| 16 | Force backup | Immediate SQLite backup with rotation (keeps last 10) |

### Other (17-18)
Custom menu items and exit.

---

## Phase 3: Legacy Data Migration

307 entries were trapped in JSON files from the old context-registry system:

| Source File | Entries | Context Type |
|------------|---------|-------------|
| `questions.json` | 30 | `menu_choice` |
| `actions.json` | 139 | `flow` (subtype: action) |
| `delegations.json` | 2 | `flow` (subtype: delegation) |
| `flows.json` | 141 | Skipped (duplicate consolidation) |

Built `migrate-legacy-to-openmemory.py` — a migration script that:
1. Reads each JSON file
2. Maps entries to the CRUD pattern (content + metadata + tags)
3. Stores via MCP with rate limiting (0.3s between calls)
4. Reports pre/post migration counts

**Result**: 171 entries migrated, all queryable. HSG deduplicated some into existing semantic clusters — net 56 new unique memories created, rest merged intelligently.

### Migration Data Mapping

**Questions → menu_choice:**
```python
content = f"menu_choice: {category} - {question} → {choice}"
metadata = {
    "type": "menu_choice",
    "source": "legacy_migration",
    "original_id": entry_id,
    "category": category,
    "question": question,
    "choice": choice,
    "migrated_from": "questions.json"
}
```

**Actions → flow:**
```python
content = f"flow: {source}/{action_id} ({trigger}) → {'success' if success else 'failed'}"
metadata = {
    "type": "flow",
    "subtype": "action",
    "source": "legacy_migration",
    "action_id": action_id,
    "trigger": trigger,
    "success": success,
    "duration_ms": duration,
    "migrated_from": "actions.json"
}
```

---

## Phase 4: AGENTS.md Overhaul

The global agent instructions file had 12 references to "Supermemory" (the old memory system) and an entire section pointing to shell scripts for context recording. All replaced:

| Before | After |
|--------|-------|
| `supermemory(mode: "add")` | `openmemory_store(content, metadata, tags)` |
| `supermemory(mode: "search")` | `openmemory_query(query, k)` |
| `record-question-v2.sh` | `openmemory_store` with type `menu_choice` |
| `record-delegation.sh` | `openmemory_store` with type `flow`, subtype `delegation` |
| `record-action.sh` | `openmemory_store` with type `flow`, subtype `action` |
| Memory Scopes section | CRUD Pattern + Context Types + Memory Sectors tables |

Also added full documentation of:
- 6 MCP tools with descriptions
- CRUD pattern with examples
- 8 context types with when-to-store guidance
- 5 memory sectors with decay lambdas

---

## Phase 5: Cleanup

Found and deleted 6 test/debug entries from early experimentation:
- "Testing OpenMemory with valid OpenAI embeddings"
- "Test memory added on 2026-01-12 to verify backup"
- "[DELETED] Task summary memories" (meta-noise)
- "Test memory from OpenCode skill verification"
- "Testing OpenMemory with OpenAI embeddings"
- "Final test: OpenMemory with valid OpenAI API key"

**Post-cleanup**: 1,077 memories across 5 sectors.

---

## Phase 6: Intelligence Report System

Built `memory-report.py` — a comprehensive analytics engine that queries the SQLite database directly and the REST API endpoints.

### What It Reports

**Overview**: Total memories, DB size, WAL size, oldest/newest dates, content length stats, version, tier.

**Sector Breakdown**: Count, percentage, average salience, and decay lambda per sector.

**Salience Distribution**: 6 bands from "nearly forgotten" (< 0.01) to "critical" (0.80-1.00) with visual bar charts.

**Context Types**: Metadata type breakdown showing what structured data exists.

**Top Tags**: Tag frequency analysis across all 6,660+ tag uses.

**Daily Timeline**: Last 14 days of memory creation activity.

**Migration Stats**: How many entries came from legacy JSON files.

**Temporal Graph**: HSG temporal fact statistics.

### 12 Improvement Checks

The report runs 12 automated checks and generates actionable suggestions:

| # | Check | Severity | Threshold |
|---|-------|----------|-----------|
| 1 | Tier upgrade needed | Medium | tier == "fast" |
| 2 | Sector imbalance | Medium | Any sector > 55% |
| 3 | Underused sectors | Low | Any sector < 3% |
| 4 | Low salience dominance | High | > 70% memories low salience |
| 5 | Stale data | High | No new memories in 7+ days |
| 6 | WAL file bloat | High | WAL > 10MB |
| 7 | Database size | Medium | DB > 50MB |
| 8 | Untagged memories | Medium | > 20% untagged |
| 9 | Missing metadata | Medium | > 30% no metadata |
| 10 | Tag dominance | Low | Single tag > 25% of uses |
| 11 | Backup age | High | Last backup > 24 hours |
| 12 | Content quality | Low | Avg content < 30 chars |

Each suggestion includes category, severity, description, and a specific action command.

### Health Score

Calculated as: `100 - (high_severity × 15) - (medium_severity × 5)`

Current score: **75/100** 🟡 Fair — 3 suggestions (WAL checkpoint, tier upgrade, metadata coverage).

### 4 Output Modes

| Mode | Command | Use Case |
|------|---------|----------|
| Terminal | `python3 memory-report.py` | Interactive viewing with colors and bars |
| Blog | `--blog` | Publishes Hugo blog post with markdown tables |
| JSON | `--json` | Machine-readable for dashboard consumption |
| Quiet | `--quiet` | Cron mode — publishes blog + saves log, minimal stdout |

---

## Phase 7: Automated Cron Job

Added to crontab — runs every Sunday at 10:00 AM UTC:

```
0 10 * * 0 /usr/bin/python3 /root/.config/opencode/scripts/memory-report.py --quiet
```

This:
1. Copies the SQLite database from the container
2. Runs all analytics
3. Generates improvement suggestions
4. Publishes a Hugo blog post
5. Saves a terminal report to `/root/cron-logs/memory-report-YYYYMMDD.log`

Sits alongside the existing Sunday jobs:
- 8AM: Weekly todo review
- 9AM: Weekly menu analytics
- **10AM: OpenMemory intelligence report** ← new

---

## Phase 8: Defer System

Built a `defer` / `deferred` trigger system for parking tasks:

- **`defer`** — Captures current context, next steps, and reason → stores to OpenMemory with type `deferred`, status `pending`
- **`deferred`** — Queries OpenMemory for pending deferred items → presents menu to resume, complete, or cancel

Stored in OpenMemory using the same CRUD pattern, so deferred tasks are searchable and persistent across sessions.

---

## Current State

| Metric | Value |
|--------|-------|
| Total memories | 1,077 |
| Sectors | 5 (procedural 497, semantic 451, episodic 44, emotional 47, reflective 38) |
| Context types | 8 defined, all CRUD verified |
| Menu options | 18 |
| Cron jobs | Weekly Sunday 10AM |
| Health score | 75/100 |
| Legacy data migrated | 171 entries |
| Test entries cleaned | 6 |
| AGENTS.md refs fixed | 12 Supermemory → OpenMemory |

### Files Created/Modified

| File | Purpose |
|------|---------|
| `scripts/memory-menu.sh` | Interactive 18-option menu |
| `scripts/memory-operations.sh` | Backup, diagnostics, context queries |
| `scripts/memory-report.py` | Intelligence report with 4 output modes |
| `scripts/migrate-legacy-to-openmemory.py` | Legacy JSON → OpenMemory migration |
| `docs/instructions/triggers/defer.md` | Defer/deferred trigger documentation |
| `AGENTS.md` | Updated with CRUD pattern, context types, OpenMemory tools |
| `memory-menu.json` | Menu configuration |

### Remaining Items (Deferred)

1. **WAL checkpoint** — 36.6MB WAL needs truncating
2. **Backfill metadata** — 418 memories have no metadata
3. **Tier upgrade** — Consider fast → balanced for real embeddings
4. **Auto-tracking** — Automatic flow/workflow recording
5. **Migration status** — Add as menu option

---

## Key Takeaways

1. **The CRUD pattern is everything.** Without discovering that `metadata` preserves JSON exactly, none of the structured storage would work. The `content` field is for search, `metadata` is for data.

2. **SQLite direct access beats MCP for analytics.** The MCP tools are great for CRUD operations, but for aggregate queries (GROUP BY, COUNT, AVG), copying the SQLite file and querying directly is 10x faster and more flexible.

3. **HSG deduplication is real.** Migrating 171 entries only created 56 net new memories — the rest were merged into existing semantic clusters. This is a feature, not a bug.

4. **Self-reporting systems improve themselves.** The improvement suggestions from the report directly drive the next round of work. The system tells you what's wrong with it.

5. **Cron + Hugo = free observability.** A weekly blog post costs nothing and creates a permanent, browsable history of system health over time.

---

*Built on OpenMemory 2.0-hsg-tiered (CaviraOSS) running on Ubuntu with fast tier, 256d synthetic embeddings, and SQLite backend.*

*Dashboard: [http://ubuntu4:13120](http://ubuntu4:13120)*