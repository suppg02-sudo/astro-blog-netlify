---
pubDatetime: 2026-04-08T15:00:00Z
title: "Research Schema v2.1.0: When Your Skills Don't Know What Changed"
postSlug: "research-schema-v210"
description: "Research Schema v2.1.0: When Your Skills Don't Know What Changed"
tags:
  - brainplane
  - opencode
  - erag
  - schema
  - architecture
  - research
---

# Research Schema v2.1.0: When Your Skills Don't Know What Changed

## The Problem

On March 25, 2026, I scaffolded the research skill's input and output schemas. They looked reasonable at the time:

```json
{
  "topic": "string",
  "depth": "standard",
  "snowball": false,
  "gaps": false
}
```

Two weeks later, the system had evolved dramatically. We had eRAG v2 running with PostgreSQL + pgvector persistent knowledge stores, NetworkX graph operations, scratchpad orchestration, self-critique loops, and agent-driven extraction pipelines. We had project-factory creating structured projects. We had a whole brainplane knowledge engine (raw → wiki → sync).

The research skill knew about none of it.

Its schemas were frozen in time. Its output was just learnings and sources — with no way to signal that research might want to become a blog post, a project, a skill, or a monitoring metric. Research results died in markdown files.

This is the story of how we fixed it and why the fix is part of something bigger.

## What Changed (v2.1.0)

### 4 New Input Fields

All **opt-in**. Research defaults to Brave Search + webfetch. Even when eRAG is installed and running, it stays off unless you ask.

| Field | Default | Purpose |
|-------|---------|----------|
| `erag_project` | null | Link to existing eRAG persistent project |
| `erag_create` | false | Create new eRAG project from research |
| `scratchpad` | false | Use iterative research workspace |
| `project_awareness` | true | Scan project-factory for context |

The key insight: **capability should not equal compulsion**. Just because research CAN use eRAG does not mean it SHOULD automatically. Opt-in keeps the pipeline simple, predictable, and fast by default.

### 3 New Output Fields

Research now speaks the language of downstream factories:

Research outputs an `elevate` array with structured signals like:

```json
{
  "type": "blog",
  "title": "eRAG v2 Architecture Deep Dive",
  "confidence": 0.85,
  "reasoning": "12 sources, structured architecture analysis, implementation patterns",
  "priority": "high",
  "payload": { "sources": 12, "depth": "deep", "tags": ["erag", "architecture"] }
}
```

Research does not auto-act on these signals. It **suggests**. The agent decides: publish to blog, create a project, defer it, or ignore it. This is the **Signal + Output pattern** — research produces structured suggestions, downstream systems consume them optionally.

`project_context` outputs existing projects that are relevant to the research topic. `erag_augmented` is a boolean flag indicating whether vector search contributed to results.

### The Elevation Signal Structure

Every elevation signal has the same shape:

- `type`: project, blog, skill, erag, or monitor
- `title`: human readable name
- `confidence`: 0.0 to 1.0, how strongly research supports it
- `reasoning`: why it is suggested
- `priority`: high, medium, or low
- `payload`: type-specific context

Each payload type has a defined structure:
- **project**: `related_deferreds[]`, `skills_affected`
- **blog**: `sources` (int), `depth`, `tags[]`
- **skill**: `skill_name`, `maturity_level`
- **erag**: `project_name`, `chunk_count`
- **monitor**: `metric`, `threshold`

This means factories downstream can consume elevation signals with zero guessing. The payload is a contract, not a blob.

## The Bigger Problem: Schema Decay

The research skill was a symptom, not the disease. Every skill in this system has schemas, and none of them know when the world around them changes.

When eRAG gained NetworkX graph operations, research did not know. When project-factory consolidated its schema structure, research did not know. When the brainplane pipeline started capturing raw → wiki → sync flows, research did not know.

This is **schema decay**: the gap between what a skill thinks the system looks like and what it actually looks like.

### Why Schema Decay Matters

Schema decay is silent. It does not break builds. It does not fail tests. It just makes skills less useful over time. They keep working, but against a stale model of reality. Research that should suggest "this could be a project" does not, because it does not know projects exist. Research that should augment with persistent knowledge cannot, because its schema does not include eRAG fields.

### The Fix: Brainplane Sync Protocol

The tactical fix includes a sync script:

```
python3 scripts/refresh_schema.py --dry-run
```

This reads the brainplane wiki, checks if wiki content is newer than schemas, extracts structured facts, and updates schemas accordingly. It never writes to wiki/. The wiki is source of truth. Schemas are the derived interface.

Version 2.1.0 knows it was reviewed today. The `freshness_check` concept tracks when schemas were last validated against system reality. When wiki files are modified after the last review, the script can warn: "schemas may be stale."

This is Phase 1 — manual refresh. Phase 2 will add automatic freshness checks on skill invoke. Phase 3 (the strategic vision) is a full schema sync engine with dependency graphs across all skills.

## Architecture: Signal + Output

```
Research Input (v2.1.0)
├── topic, depth, breadth, concurrency
├── snowball, grade, gaps, tree, gates
├── blog, notify, save_memory (opt-in)
├── erag_project, erag_create (opt-in, OFF)
├── scratchpad (opt-in, OFF)
└── project_awareness (ON by default)

Pipeline: Brave Search + Webfetch (always)
  └── + eRAG vector (if opted in + available)
  └── + project scan (if awareness=true)

Research Output (v2.1.0)
├── success, learnings, sources, gaps
├── tree, statistics
├── elevate: [signals]    ← NEW
├── project_context: []   ← NEW
└── erag_augmented: bool  ← NEW
```

The elevation signals flow downstream. The agent receives them and decides disposition: **act** (feed to factory), **defer** (capture for later), or **ignore** (not relevant now).

## What This Enables

### For Research
Research results do not just become markdown files. They become structured opportunities: blog posts waiting to be published, projects waiting to be created, skills waiting to be built, metrics waiting to be monitored.

### For Factories
Project-factory receives elevation signals with pre-filled context: which deferred items are related, which skills are affected, how confident the signal is. No guessing.

### For TeLOS
**Every research session produces revenue signals.** Elevation flags "this could be a blog post", "this skill should exist", "this project makes money". Research becomes an income-generation pipeline, not just knowledge collection.

### For the Brainplane
Wiki entries tagged with `research`, `erag`, `schema` flow directly into skill schemas. Knowledge is not trapped in markdown files — it propagates to the interfaces that actually use it.

## The Design Process

This fix went through the full brainstorming → design → spec → review loop:

1. **Brainstorm**: Explored research skill gap, brainplane knowledge not reaching skills
2. **Scoping**: Tactical fix with project awareness and elevation signals (strategic sync engine deferred)
3. **Design**: 3 sections validated iteratively — problem framing, input schema, output schema, elevation pattern, brainplane sync
4. **Spec review**: Self-review caught 12 issues including `schema_version` in wrong place (moved to metadata), `defer` as wrong type (moved to disposition), missing payload structures
5. **Implementation**: 7 files changed, all schemas validated, refresh script dry-run tested, wiki entry created
6. **Blog**: You are reading it

The spec lives at [2026-04-08-research-schema-refinement-design.md](http://ubuntu4:8080/editor/opencode/docs/superpowers/specs/2026-04-08-research-schema-refinement-design.md). 186 lines, zero TBDs, 8 verified success criteria.

## The Strategic Vision

This tactical fix is a blueprint for the full **Schema Infrastructure v2.0** (DO-017):

```
Schema Registry (truth of all schemas, versions, deps)
        │
        ▼
Sync Engine (detects changes → maps deps → propagates)
        │
        ▼
Factory Triggers (skill-factory, project-factory, etc.)
        │
        ▼
Brainplane (wiki = source of truth for all knowledge)
```

Every skill gets auto-awareness of system changes. Every schema gets a freshness score. Every factory gets triggered when its dependencies evolve.

The tactical fix proved the pattern works. The next build scales it.

## Files Changed

| File | Change |
|------|--------|
| `skills/research/context/schemas/input.json` | 4 opt-in fields, eRAG defaults OFF |
| `skills/research/context/schemas/output.json` | elevation signals, project_context, erag_augmented |
| `skills/research/context/metadata.json` | v2.1.0, new features, optional_dependencies |
| `skills/research/SKILL.md` | Full v2.1.0 overview, pipeline behavior, sync docs |
| `skills/research/scripts/refresh_schema.py` | New wiki→schema sync (dry-run, no-op, validation) |
| `wiki/research-skill.md` | Brainplane entry, capability matrix |
| `docs/superpowers/specs/2026-04-08-*.md` | 186-line design spec, self-reviewed, approved |

Success criteria: all 8 verified. No breaking changes to existing CLI usage. All JSON schemas validate. Wiki entry created and brainplane-cleaned.

*Schema decay is a silent killer. Now we have a way to fight it.*