---
pubDatetime: 2026-04-09T18:00:00Z
title: "Zero-Duplication Session Resume: How We Fixed Research Continuity"
postSlug: "zero-duplication-session-resume"
description: "Zero-Duplication Session Resume: How We Fixed Research Continuity"
tags:
  - ai-agents
  - schemas
  - session-resume
  - architecture
  - research
---

# Zero-Duplication Session Resume: How We Fixed Research Continuity

**Tags**: research, architecture, ai-agents, schemas, session-resume

Building an AI research skill that remembers where it left off — without copying a single byte of data.

## The Problem

Research sessions are ephemeral. You start investigating a topic, gather sources, extract entities, synthesize findings — and then the session ends. Next time you want to continue, you're starting from scratch or manually digging through markdown files.

The naive solution is to create a "session file" that stores everything. But that creates a worse problem: **data duplication across three existing stores**.

Our research skill already had:

- **eRAG projects** (PostgreSQL + pgvector) — sources, chunks, entities, facts, synthesis
- **Brainplane wiki** — domain knowledge, architectural decisions
- **pghmem** (PostgreSQL memory) — decisions, patterns, preferences
- **Session narratives** — full markdown reports in `history/sessions/`

Adding a rich session file would duplicate content across all four. That's not just wasteful — it's dangerous. Stale copies diverge from the truth. Which copy is authoritative when they disagree?

## The Design: Thin Manifests

We went with a **pointer + signals** pattern. The session manifest is a JSON file that contains zero content — only addresses and state.

```
history/sessions/
├── 2026-04-08-paperclip.json   ← manifest (pointers + signals)
└── 2026-04-08-paperclip.md     ← narrative (full report)
```

A manifest contains three sections — **pointers** (addresses: eRAG slug, wiki path, memory tags, history file), **signals** (state: open gaps, resolved gaps, pending elevation dispositions, recommended next steps, staleness threshold), and **stats** (progress: iteration count, source count, learning count, fact count, entity count). No content. No synthesis. No sources. Just addresses and state.

## The Resume Flow

When a user selects "Resume Research", the agent follows a structured pipeline:

```
🔴 List sessions → present as menu
🟠 User selects → load manifest
🟡 Context loading (configurable depth)
    minimal: gaps + stats only
    summary: manifest + narrative synthesis
    full: manifest + eRAG facts + wiki + pghmem
🟢 Intelligent analysis
    → Check open gaps
    → Check pending elevation signals
    → Check source staleness (stale_after_days)
    → Cross-reference eRAG (has knowledge grown?)
    → Cross-reference wiki (has understanding evolved?)
    → Cross-reference pghmem (new decisions?)
🔵 Present resume options:
    • Continue (gaps only)
    • Extend (new sub-questions)
    • Refresh (re-research stale sources)
    • Disposition pending elevation signals
🟣 Execute → update manifest
✅ Done
```

## Schema Integration

We extended the research skill's input and output JSON schemas (v2.1.0 → v2.2.0) to make this first-class:

**Input** — 3 new fields:

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| `resume_session` | string or null | null | Session ID to resume |
| `resume_mode` | enum | gaps_only | gaps_only, extend, or refresh |
| `resume_context_depth` | enum | summary | minimal, summary, or full |

**Output** — 1 new block:

The `session` object with `pointers`, `signals`, and `stats` — matching the manifest structure exactly. The agent writes this block on session completion, creating or updating the manifest.

## Why Not Just Use eRAG?

eRAG stores **what you know** — sources, entities, facts. But it doesn't store:

- **What you don't know** (open gaps)
- **What you decided to do about it** (elevation dispositions — act/defer/ignore)
- **Where you left off** (next steps)
- **How many times you've iterated** (cumulative stats)

That's signal data, not content data. It belongs in the manifest, not in the vector database.

Conversely, the manifest doesn't store facts or sources — that's eRAG's job. The manifest just points to the eRAG project slug.

## The One Canonical Copy Principle

Every piece of data has exactly one home:

| Data | Home | Referenced by |
|------|------|---------------|
| Sources, chunks, entities, facts | eRAG project | `manifest.pointers.erag_slug` |
| Domain knowledge, decisions | Brainplane wiki | `manifest.pointers.wiki_path` |
| Decision history, preferences | pghmem | `manifest.pointers.memory_tags` |
| Full narrative report | Session markdown | `manifest.pointers.history_file` |
| Gap state, elevation signals, stats | Session manifest | Direct (this IS the manifest) |

No overlaps. No stale copies. No ambiguity about which source is authoritative.

## Implementation Details

The `list_sessions.py` script handles three operations:

```bash
# List sessions (merges manifest + markdown)
python3 scripts/list_sessions.py list -n 10

# Show session detail (manifest enriched with markdown title)
python3 scripts/list_sessions.py show 2026-04-08-paperclip

# Create or update manifest (idempotent)
python3 scripts/list_sessions.py create 2026-04-08-topic \
  --erag-slug topic-slug \
  --wiki-path wiki/topic.md \
  --topic-tag topic
```

Legacy sessions (markdown-only, no manifest) still work — the script falls back to parsing the markdown header for title and date. When a manifest exists alongside the markdown, the manifest is authoritative.

## Lessons Learned

1. **Duplication is a design smell.** If you're copying data between stores, you're missing an abstraction. Pointers are cheaper than copies.

2. **Separate signal from content.** "What gaps are open?" is signal data. "What did source X say?" is content data. They have different lifecycles and should live in different stores.

3. **Make schemas the contract.** Input/output schemas define what the agent expects and produces. The manifest structure is defined in the output schema, not in ad-hoc code.

4. **Resume is not reload.** Resuming a session isn't about reloading everything — it's about loading the minimum context needed to make intelligent decisions about what to research next.

5. **Idempotent operations.** Creating a manifest should be safe to run multiple times. It updates if it exists, creates if it doesn't. This makes the agent's job simpler.

---

*This post describes the v2.2.0 update to the research skill in the OpenCode ecosystem. The skill is part of an AI infrastructure stack running on Ubuntu Server with PostgreSQL + pgvector for knowledge persistence.*