---
pubDatetime: 2026-04-11T20:30:00Z
title: "Stop Storing Decisions in YAML: A PostgreSQL Pattern for AI Systems"
postSlug: "stop-storing-decisions-in-yaml"
description: "Stop Storing Decisions in YAML: A PostgreSQL Pattern for AI Systems"
tags:
  - others
---

**Tags**: ai-infrastructure, postgresql, decision-schema, ai-engineering
**Categories**: AI Automation, Tutorials

If you build AI agent systems, you accumulate decisions. Architecture choices, tool selections, migration plans, deprecation notices. At first you scribble them in a notes field. Then a YAML file. Then another YAML file. Six months later you have four different storage locations, three different formats, and zero ability to answer "what did we decide about X?" This post walks through how we consolidated everything into a single PostgreSQL table with a CLI tool, migrated 16 existing decisions, and wired it into our agent's daily workflow.

## The Problem: Four Places, Zero Queries

Our AI agent system (OpenCode) had decisions scattered across four locations with no unified query interface:

**1. YAML strings** -- A `decisions` block in project YAML files containing one-liner summaries. Quick to write, impossible to search. No context, no severity, no entity linkage.

**2. YAML dicts** -- A separate `detailed_decisions` block with more structure but still locked in static files. Any change required a file edit and git commit. No runtime access.

**3. Notes blob** -- Freeform text in a `notes` field mixing decisions with observations, tasks, and random thoughts. Parsing it required regex and hope.

**4. Vector memory** -- Individual decisions embedded into pgvector via a `capture_conversation.py` script. Searchable by similarity but unstructured. No filtering by severity, entity, or date. No way to list "all major decisions for project X."

The result: when our agent needed to recall a decision, it either searched vector memory (fuzzy, no guarantees) or read a YAML file (static, incomplete). Neither was reliable. Format drift was constant. Some decisions had severity tags, others didn't. Some referenced entities, others were orphaned strings.

## The Pattern: Polymorphic + JSONB

The fix was a single PostgreSQL table using the polymorphic + JSONB pattern common in SaaS applications. One table stores all decisions regardless of entity type, with a JSONB column for flexible metadata that varies per domain.

The key design decisions:

- **Entity-agnostic**: `entity_type` + `entity_id` columns allow any domain (project, skill, research topic) to store decisions in the same table
- **Severity enum**: `atomic`, `minor`, `major`, `critical` -- forces classification at write time
- **JSONB metadata**: tags, rationale, evidence, superseded_by -- flexible without schema migrations
- **GIN index on JSONB**: enables fast queries inside the metadata column
- **Auto-embedding**: an `--embed` flag sends the decision to pgvector for similarity search alongside structured storage

## Step 1: Create the Schema

The table lives in an existing PostgreSQL database alongside pgvector extensions:

```sql
CREATE TABLE aimplifi_decisions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_type TEXT NOT NULL,
    entity_id TEXT NOT NULL,
    title TEXT NOT NULL,
    severity TEXT NOT NULL DEFAULT 'minor'
        CHECK (severity IN ('atomic','minor','major','critical')),
    rationale TEXT,
    metadata JSONB NOT NULL DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Fast lookups by entity
CREATE INDEX idx_decisions_entity
    ON aimplifi_decisions (entity_type, entity_id);

-- Fast filtering by severity
CREATE INDEX idx_decisions_severity
    ON aimplifi_decisions (severity);

-- Fast search inside JSONB metadata
CREATE INDEX idx_decisions_metadata
    ON aimplifi_decisions USING GIN (metadata jsonb_path_ops);
```

The `entity_type` uses a TEXT column rather than a PostgreSQL enum for flexibility. New entity types (like `research:karpathy` or `project:evolution`) can be added without DDL changes. The CHECK constraint on `severity` keeps the four-tier classification enforced at the database level.

The JSONB `metadata` column stores anything that doesn't deserve its own column: tags, evidence links, superseded_by references, and custom domain data. The GIN index with `jsonb_path_ops` makes queries like "find all decisions with tag X" fast.

## Step 2: Build the CLI

We wrapped the table in a CLI tool called `pghdecision` for agent-friendly access:

```bash
# Add a decision
pghdecision add \
    --entity project:evolution \
    --title "Adopt unified decision schema" \
    --severity major \
    --tags schema,postgresql,migration

# Add with rationale and auto-embed to vector memory
pghdecision add \
    --entity research:karpathy \
    --title "Karpathy: simplicity-first coding" \
    --rationale "Fewer lines = fewer bugs. Rewrite if 200 could be 50." \
    --embed

# List decisions for an entity at different detail levels
pghdecision list --entity project:evolution --level L0   # titles only
pghdecision list --entity project:evolution --level L1   # + rationale
pghdecision list --entity project:evolution --level L2   # + evidence

# Cross-entity queries
pghdecision list --severity major,critical               # all high-severity
pghdecision list --entity-type project                   # all project decisions

# View a specific decision
pghdecision show <uuid>

# Supersede an old decision with a new one
pghdecision supersede <old-uuid> --by <new-uuid>

# Usage statistics
pghdecision stats --entity project:evolution
```

The progressive disclosure levels (L0/L1/L2/L3) mirror our documentation system. An agent checking context loads L0 for quick scanning, L1 for reasoning, and L2/L3 when deep context is needed. This keeps token usage proportional to need.

The `supersede` command creates an explicit chain: old decisions are never deleted, but marked as replaced. This gives a full audit trail of how thinking evolved.

## Step 3: Migrate Existing Data

We wrote a migration script that extracted decisions from all four legacy locations and normalized them into the new table:

```bash
# Dry run first
pghdecision migrate --dry-run

# Migrate all sources
pghdecision migrate --source yaml_strings \
                   --source yaml_dicts \
                   --source notes_blob \
                   --source vector_memory
```

Results:

- **16 decisions** migrated from YAML and vector memory
- **4 duplicate detections** merged (same decision stored in multiple locations)
- **3 format normalizations** applied (severity inferred from context tags)
- **0 data loss** -- all original sources preserved, new rows reference their origin in metadata

The migration script used the `--embed` flag on each migrated decision, so all 16 are now searchable via both structured queries and vector similarity.

## Step 4: Wire Into Existing Tools

The `capture_conversation.py` script, which our agent calls after every significant action, now performs a dual write:

```bash
# Still saves to vector memory (backwards compatible)
capture_conversation.py "Decided to use polymorphic table pattern" \
    --type decision \
    --tags "schema,postgresql"

# Now ALSO writes to aimplifi_decisions table
# Same command -- the script detects --type decision and dual-writes
```

The dual-write ensures no regression. Vector memory continues to work for similarity search. The structured table handles exact queries, filtering, and cross-entity analysis. Over time, the structured table becomes the source of truth while vector memory serves as the fuzzy recall layer.

## Step 5: Update Your Agent Instructions

The agent's instruction file (AGENTS.md) was updated with a quick-reference table and decision protocol:

```markdown
### Quick Reference

| Trigger | Command |
|--------|--------|
| Decision made | pghdecision add --entity project:X --title "summary" --severity major |
| List decisions | pghdecision list --entity project:X --level L0 |
| Cross-entity | pghdecision list --severity major,critical |
| Supersede | pghdecision supersede <old-uuid> --by <new-uuid> |
| Search | pghmem search "query" |
```

The key instruction: **always specify severity**. Without it, decisions default to `minor` and get lost in the noise. The agent is prompted to classify every decision as it's made, not retroactively.

## What This Unlocks

With decisions in a queryable table, capabilities that were impossible before become trivial:

**Cross-entity queries**: List all major decisions across every project. Find every critical decision made in the last 30 days. Filter by tag.

**Supersede chains**: When a decision is reversed, the old record links to the new one. You can trace the full evolution of thinking on any topic.

**Progressive disclosure**: Agents load L0 (titles) for quick context, L1 (rationale) for reasoning, L2/L3 (evidence, full detail) when deep context is needed. Token-efficient by default.

**Experience pipeline**: Decisions tagged with `--embed` flow into the vector memory, creating a corpus of past reasoning that informs future decisions. The structured table gives exact recall; the vector layer gives associative recall.

**Statistics and health checks**: `pghdecision stats` shows decision velocity, severity distribution, and entity coverage. You can spot projects that are accumulating unrecorded decisions or domains with too many critical unresolved items.

## When to Use This Pattern

This approach works whenever your AI system meets these conditions:

- Decisions accumulate faster than humans can track them
- Multiple agents or sessions need shared decision context
- You need both exact recall ("what did we decide about X?") and fuzzy recall ("decisions similar to Y")
- Format drift is actively causing problems (inconsistent tags, missing fields, no enforceable schema)

It's overkill for a single-agent, single-session setup. But once you have persistent agents making architectural decisions across multiple projects, the cost of unstructured decision storage compounds fast. A single table with a CLI wrapper is a small investment that pays for itself the first time you answer "why did we do it that way?" in under a second.

The polymorphic + JSONB pattern is transferable beyond decisions. We use the same approach for tracking skill evolution, trigger usage signals, and deferred task management. One table shape, many domains. Start with decisions, then extend to whatever your system accumulates.