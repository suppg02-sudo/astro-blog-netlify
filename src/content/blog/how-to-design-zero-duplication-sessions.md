---
pubDatetime: 2026-04-09T19:00:00Z
title: "How to Design a Zero-Duplication Session System: A Step-by-Step Guide"
postSlug: "how-to-design-zero-duplication-sessions"
description: "How to Design a Zero-Duplication Session System: A Step-by-Step Guide"
tags:
  - how-to
  - session-management
  - ai-agents
  - architecture
  - postgresql
  - tutorial
---

# How to Design a Zero-Duplication Session System: A Step-by-Step Guide

**Tags**: tutorial, ai-agents, architecture, postgresql, how-to, session-management

A practical walkthrough for applying pointer-first thinking to any multi-store system. Use this when your AI agent needs to remember across sessions without creating a mess.

## Who This Is For

You're building an AI system with multiple knowledge stores. Maybe a vector database for embeddings, a relational database for structured data, a file system for documents. You want sessions that resume cleanly. You don't want five copies of the same fact diverging from each other.

This guide teaches the thinking pattern, then shows every file you need to implement it.

## The Mental Model

Before writing any code, internalise this:

**Every piece of data has one home. Everything else is a pointer.**

A home is where data gets created, updated, and deleted. A pointer is an address — a slug, a path, a tag, an ID — that tells you where to find the home.

If you catch yourself copying data from Store A into Store B "for convenience," stop. You're about to create a sync problem that only gets worse.

Instead: put an address in Store B that points to Store A. When you need the data, follow the pointer.

## Step 1: Map Your Stores

List every place data lives in your system. For each store, write down what it owns and what it's good at.

Our research skill had five:

| Store | Owns | Good at |
|-------|------|---------|
| eRAG (pgvector) | Sources, entities, facts, synthesis | Semantic search, knowledge graphs |
| Wiki (markdown) | Domain knowledge, decisions | Human-readable, git-trackable |
| pghmem (PostgreSQL) | Decisions, patterns, preferences | Relationship traversal, tags |
| Session narratives (markdown) | Research reports | Full human-readable output |
| Session manifests (JSON) | Nothing — just addresses and state | Resume logic |

Notice the last one. The manifest **owns nothing**. That's the key insight.

## Step 2: Identify What Crosses Session Boundaries

Not all data needs to survive between sessions. Ask yourself:

- **What do I need to know to continue?** Not the full content — just what's changed and what's still TODO.
- **What state is transient?** Things like "which gaps are open" or "which blog post ideas are pending." This state doesn't belong in your content stores.
- **What addresses do I need?** The slugs, paths, and tags that point to the canonical data.

For us, the cross-session state was:

- Which research gaps are still open (signal, not content)
- Which elevation signals are pending disposition (signal)
- Recommended next steps (signal)
- Where to find the sources (pointer)
- Where to find the knowledge (pointer)
- Where to find the decisions (pointer)
- Cumulative progress stats (metadata)

None of this is content. It's all addresses and transient state.

## Step 3: Design the Manifest Schema

Create a JSON schema that has exactly three top-level sections:

**pointers** — addresses to your stores. Every pointer is a string (slug, path, tag) or null if not applicable.

**signals** — transient state that changes every session. Gaps, pending actions, recommendations, thresholds.

**stats** — cumulative counters. Iterations, counts, progress.

Here's the template:

```json
{
  "id": "YYYY-MM-DD-slug",
  "status": "active",
  "created": "ISO-8601",
  "updated": "ISO-8601",
  "pointers": {
    "vector_db_slug": null,
    "knowledge_base_path": null,
    "memory_tags": [],
    "narrative_file": null
  },
  "signals": {
    "gaps_open": [],
    "gaps_resolved": [],
    "pending_actions": [],
    "next_steps": [],
    "stale_after_days": 30
  },
  "stats": {
    "iterations": 1,
    "total_items": 0
  }
}
```

Adapt the field names to your domain. The structure stays the same.

**Validation check**: If you find yourself putting content (source text, entity lists, synthesis paragraphs) into the manifest, you're doing it wrong. That data has a home. Put a pointer to that home instead.

## Step 4: Build the Index Script

You need a script that lists sessions and shows their state. It should handle two cases:

1. **Manifest exists** — read it, enrich with title from narrative if available
2. **Legacy session, no manifest** — parse what you can from existing files

The script should support three operations:

**list** — show recent sessions sorted by update time. Include status, title, and open gap count. This is what the agent shows when the user picks "resume."

**show** — display full session detail: all pointers, all signals, all stats. This is what the agent reads before deciding how to continue.

**create** — make a new manifest or update an existing one. Must be idempotent. Running it twice with the same arguments should update, not duplicate.

Key implementation detail: when both a `.json` manifest and a `.md` narrative exist for the same session ID, merge them. The manifest is authoritative for structured data. The narrative provides the human-readable title.

## Step 5: Wire the Input Schema

Add resume fields to whatever input structure your agent uses:

```
resume_session: string | null   — the session ID to resume
resume_mode: enum               — how to resume (gaps_only, extend, refresh)
resume_context_depth: enum      — how much to load (minimal, summary, full)
```

These three fields tell the agent everything it needs. No special cases. No flags for "also load the wiki" — the manifest's pointers handle that.

The depth levels control token spend:

- **minimal**: read the manifest only. Gaps + stats. Fastest.
- **summary**: manifest plus the synthesis section of the narrative. Balanced.
- **full**: manifest plus all pointed-to stores. Most expensive. Use when the topic is complex or the user hasn't worked on it recently.

## Step 6: Wire the Output Schema

Add a `session` block to your output structure. It mirrors the manifest exactly:

```
session:
  id: string
  status: enum (active, paused, completed, abandoned)
  pointers: { same structure as manifest }
  signals: { same structure as manifest }
  stats: { same structure as manifest }
```

The agent writes this block at session end. A helper function takes this block and writes/updates the manifest file. The output schema is the contract — whatever shape it defines, that's what gets persisted.

**Critical**: the agent must not write to the manifest mid-session. Write once at the end, atomically. Partial writes create inconsistent state.

## Step 7: Design the Resume Pipeline

The actual resume flow, step by step:

**Phase 1: Discovery.** Run your index script. Present sessions as a menu. Record the signal (which options you showed, which the user picked).

**Phase 2: Loading.** Read the manifest. Based on `resume_context_depth`, load data from the pointed-to stores. Check each pointer — if it's null, skip that store. If the pointed-to resource doesn't exist, note it as a gap.

**Phase 3: Intelligence.** Before asking the user what to do, do your homework:
- Are any open gaps now resolvable because a pointed-to store has new data?
- Have any sources gone stale past `stale_after_days`?
- Are there pending actions that other sessions may have already handled?
- Has any pointed-to store been updated since the last session?

**Phase 4: Options.** Present resume options via a structured menu:
- **Continue** — research only the gaps that are still open
- **Extend** — add new sub-questions to the research scope
- **Refresh** — re-research sources that have gone stale
- **Act on pending** — disposition any pending actions (publish that blog post, create that project)

**Phase 5: Execute.** Run the chosen mode. Update the manifest when done.

## Step 8: Handle Legacy Data

You will have existing sessions without manifests. Don't try to retroactively create manifests for all of them. Instead:

- Make your index script handle both manifest and non-manifest sessions gracefully
- When a user resumes a legacy session, create the manifest on the fly
- The first thing the agent does is figure out which stores have relevant data and populate the pointers

This is why the `create` operation is idempotent. The agent can run it safely at the start of any session, even for legacy data.

## Step 9: Test the No-Duplication Invariant

Here's how to verify your system actually avoids duplication:

1. Run a research session. Note the entities, facts, and synthesis in eRAG.
2. Check the manifest file. It should contain zero entities, zero facts, zero synthesis text. Only pointers and signals.
3. Resume the session. The agent should reconstruct context by following pointers, not by reading content from the manifest.
4. Update a fact in eRAG. Resume the session again. The agent should see the updated fact, not a stale copy.

If any of these fail, you have duplication somewhere. Find it and replace it with a pointer.

## Common Mistakes

**Mistake 1: Storing "just the key findings" in the manifest.** No. Findings are content. They live in eRAG or equivalent. The manifest stores "what gaps remain" — that's signal.

**Mistake 2: Copying the last synthesis into the manifest "for quick access."** You've just created a stale copy. Point to the eRAG project instead. The query takes milliseconds.

**Mistake 3: Making the manifest the source of truth for anything.** It's not a source of truth. It's an index and a signal board. Sources, entities, facts, decisions — these all have homes. The manifest just knows the addresses.

**Mistake 4: Complex pointer resolution.** If following a pointer requires three API calls and a graph traversal, the pointer is too indirect. A slug, a path, or a tag. Keep it simple.

**Mistake 5: Skipping the depth levels.** Always loading everything is wasteful. Always loading nothing is useless. The three-level depth system (minimal, summary, full) lets the agent (or user) control the cost.

## The Generalisation

This pattern isn't specific to research skills. It applies anywhere you have:

- Multiple stores with different data types
- Sessions that need to resume
- A need to avoid sync issues between copies

The invariant is always the same: **one canonical copy, many pointers**. The manifest owns nothing but knows where everything lives.

Think of it like a library card catalog. The catalog doesn't contain the books. It tells you where to find them. And it has a notes section — "pages 45-67 still need reading" — that's transient state the catalog legitimately owns.

---

*This guide is based on the research skill v2.2.0 in the OpenCode ecosystem. The manifest pattern is implemented in `list_sessions.py` with list/show/create subcommands. Schemas are in `context/schemas/input.json` and `output.json`. The system runs on Ubuntu Server with PostgreSQL + pgvector.*