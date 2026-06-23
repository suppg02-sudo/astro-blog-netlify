---
pubDatetime: 2026-04-11T15:00:00Z
title: "Why Your AI System Needs a Decision Schema (And What Happens Without One)"
postSlug: "why-your-ai-system-needs-a-dec"
description: "Why Your AI System Needs a Decision Schema (And What Happens Without One)"
tags:
  - "7"
---

After running a self-improving AI system for two weeks, I discovered that **decisions** — the most important data in any AI project — were stored in four different places with four different formats. Here's what went wrong, and the schema I designed to fix it.

## The Problem: Decision Entropy

Every AI project accumulates decisions. "We chose PostgreSQL over MongoDB." "The agent routing uses hub-and-spoke." "Knowledge compilation runs as a systemd service." These decisions are the DNA of the system. Lose them, and you lose the ability to understand *why* the system works the way it does.

My system had four places where decisions lived:

1. **`tracking.decisions`** — a YAML list that started as plain strings ("2026-04-03: Hub & Spoke approach selected") and evolved into structured dicts (date + decision + rationale). Mixed format, 15 entries, unsearchable.

2. **`history.entries`** — a different YAML list with richer metadata (date, type, summary, details, agent). Added late, only 4 entries, duplicated some decisions from the first list.

3. **`notes`** — a giant string blob with paragraphs like "Karpathy Pattern Analysis (2026-04-05): 55% alignment..." Grows forever, unstructured, no schema.

4. **`pghmem`** — PostgreSQL with vector embeddings, 2,846+ memories. Requires the exact right search query to surface anything. Decisions get buried under conversation logs.

## Why This Matters

The decay isn't hypothetical. During a recent session, I wanted to answer: "Why did we choose Kestra over Directus Flows for automation?" The answer existed — it was decision #7 in tracking.decisions: "Kestra owns ALL automation/orchestration. Directus is purely data + CMS."

But finding it required:
1. Reading the full project YAML (822 lines)
2. Scanning the `tracking.decisions` array
3. Recognising that entries 1-11 are strings (no `rationale` field) but entries 12-15 have `rationale`
4. Parsing the string manually to extract the reasoning

An AI agent in a new session would need to do the same — read 822 lines of YAML just to find one decision. At current context costs, that's $0.02 per query just for the YAML. Across 100 sessions, that's $2 of API cost for something that should be a single SQL query.

## The Schema

One PostgreSQL table, following the polymorphic + JSONB pattern:

```sql
CREATE TABLE aimplifi_decisions (
  id            UUID PRIMARY KEY,
  entity_type   ENUM('project','research','skill','menu'),
  entity_id     TEXT,              -- "evolution", "karpathy", "skill-factory"
  title         TEXT NOT NULL,
  rationale     TEXT,
  evidence      JSONB,             -- wiki_articles, blog_posts, files, urls
  tags          TEXT[],
  severity      ENUM('info','minor','major','atomic'),
  decided_at    TIMESTAMPTZ,
  decided_by    TEXT DEFAULT 'agent',
  memory_id     UUID,              -- link to vector memory (nullable)
  superseded_by UUID               -- self-reference for reversed decisions
);
```

Key design choices:

**Polymorphic entity** — `entity_type + entity_id` lets me query decisions across all projects ("show me every architecture decision") or filter to one ("decisions about the karpathy research"). Mirrors the existing `aimplifi_schemas` pattern.

**JSONB evidence** — Different decisions have different backing evidence. Some reference wiki articles, some link to blog posts, some point to spec files. JSONB handles this without schema sprawl.

**Severity-gated embedding** — Not every decision needs vector embedding. `info` decisions (routine, like "deployed a cron job") don't need semantic recall. `major` and `atomic` decisions (system-defining, like "Kestra owns all automation") get embedded for fuzzy search.

**Superseded self-reference** — Decisions can be reversed without deletion. "We chose Kestra" can be superseded by "We migrated to Temporal" while preserving the history.

## What the YAML Becomes

Before (4 sources, ~100 lines of mixed content):

```yaml
tracking:
  decisions:
    - '2026-04-03: Hub & Spoke approach selected'
    - date: '2026-04-06'
      decision: 'Deployed Kestra orchestration layer'
      rationale: 'Standalone Docker deploy...'
history:
  entries:
    - date: '2026-04-08T04:50:00Z'
      type: decision
      summary: "Domain name brainplane.ai available"
notes: "This project tracks the evolution of:\n- Factories..."
```

After (1 pointer, 5 lines):

```yaml
decisions:
  source: postgresql
  entity: project:evolution
  count: 15
  latest:
    - "2026-04-11: ShackStudios — 5 portable patterns"
    - "2026-04-08: brainplane.ai domain identified"
    - "2026-04-06: Kestra deployed for orchestration"
```

The `latest` field is the compaction survival mechanism. When AI session context gets trimmed, the 3 one-liners survive. Full detail is one `pghdecision list` call away.

## The CLI

```bash
# Log a decision
pghdecision add --entity project:evolution \
  --title "Kestra owns ALL automation" \
  --rationale "Directus is purely data + CMS" \
  --severity atomic --tags kestra,automation,architecture

# Query it back
pghdecision list --entity project:evolution --severity major,atomic --level L1

# Reverse a decision (no deletion)
pghdecision supersede <old-uuid> --by <new-uuid> --reason "Migrated to Temporal"
```

Progressive disclosure via `--level`:
- **L0**: title + date + severity (quick scan)
- **L1**: + rationale (why?)
- **L2**: + evidence JSONB (what backs this up?)
- **L3**: + raw_context (everything)

## The Lesson

The most important data in an AI system isn't the code, the configs, or the prompts. It's the **decisions** — the accumulated reasoning that explains why the system is the way it is. If those decisions are scattered across four formats in three locations, you don't have a decision system. You have decision entropy.

A decision schema isn't overengineering. It's the minimum viable infrastructure for any AI project that runs longer than a weekend. The cost of the schema (one table, one CLI, one migration) is negligible compared to the cost of not having one (reading 822-line YAML files to answer simple questions, forever).

**Tags**: ai-infrastructure, decision-schema, postgresql, self-improving-systems, context-engineering
**Categories**: AI Automation, Tutorials