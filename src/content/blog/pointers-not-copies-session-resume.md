---
pubDatetime: 2026-04-09T18:30:00Z
title: "Stop Duplicating Data in Your AI Sessions — Use Pointers Instead"
postSlug: "pointers-not-copies-session-resume"
description: "Stop Duplicating Data in Your AI Sessions — Use Pointers Instead"
tags:
  - session-management
  - schema-design
  - ai-infrastructure
  - postgresql
  - research
---

# Stop Duplicating Data in Your AI Sessions — Use Pointers Instead

**Tags**: research, ai-infrastructure, postgresql, schema-design, session-management

A practical pattern for resuming AI research sessions without the copy-paste trap. Real architecture from a production system.

## The Trap Every AI Agent Falls Into

Here's what happens. You build a research skill. It gathers sources, extracts entities, synthesizes findings. Great. Then someone asks "can I resume where I left off?" and you think: easy, I'll save the session state to a file.

So you create a session object. You serialize the sources, the findings, the gaps, the decisions into a JSON blob. Next session, you deserialize it and continue. Problem solved.

Except now you have two copies of every source. Three copies of every entity. Four copies of the synthesis. And they're all slightly different because the eRAG project was updated between sessions but the session file wasn't.

This isn't theoretical. I watched it happen in our stack.

## Our Stack Before the Fix

Three independent knowledge stores, each with a clear job:

- **eRAG** — PostgreSQL + pgvector. Stores raw sources, chunked text, extracted entities, facts, and synthesis per research topic. The ground truth for *what was found*.
- **Brainplane wiki** — Markdown files. Stores domain knowledge, architectural patterns, design decisions. The ground truth for *what was understood*.
- **pghmem** — PostgreSQL memory with semantic search. Stores decisions, preferences, patterns. The ground truth for *why things were decided*.

Plus session narrative files — markdown reports of what happened during each research session.

All three stores already had the data. The question was: how do you resume a session without copying any of it?

## The Answer: Manifests That Point, Never Copy

A session manifest is a JSON file in `history/sessions/` that contains exactly zero bytes of research content. It has three sections:

**Pointers** — addresses, not data. The eRAG project slug, the wiki file path, the pghmem tags to search. When the agent resumes, it follows these pointers to the canonical stores.

**Signals** — state that doesn't live anywhere else. Which research gaps are still open. Which elevation signals (suggestions to create blog posts, projects, skills) are pending disposition. What the agent recommended as next steps. A staleness threshold for sources.

**Stats** — cumulative progress. How many iterations, sources, learnings, facts, entities across all sessions on this topic.

```json
{
  "id": "2026-04-08-paperclip",
  "status": "active",
  "pointers": {
    "erag_slug": "colemedin-analysis",
    "wiki_path": "wiki/paperclip.md",
    "memory_tags": ["research", "paperclip"]
  },
  "signals": {
    "gaps_open": ["heartbeat scheduling integration"],
    "next_steps": ["Compare with OpenCode agent adapters"],
    "stale_after_days": 30
  },
  "stats": {
    "iterations": 2,
    "total_sources": 12
  }
}
```

Every field is either an address or transient state. No content.

## Why This Works

**The canonical copy principle**: every fact lives in exactly one place. eRAG owns sources and entities. Wiki owns domain knowledge. pghmem owns decisions. The manifest owns... nothing. It just knows where everything is.

This means:

- When eRAG gets updated with new sources, the manifest doesn't need updating. The pointer still points to the right project.
- When the wiki evolves, same thing. The path is still valid.
- When you want to know what gaps remain, the manifest tells you directly — that's its job.
- When you want to know what a source said, you ask eRAG — not the manifest.

## The Resume Pipeline

Resuming isn't reloading. It's reconstructing the minimum context needed to make smart decisions about what to research next. Here's the actual flow:

1. **List sessions.** The `list_sessions.py` script scans `history/sessions/` for both `.json` manifests and `.md` narratives. It merges them — the manifest provides structured data, the markdown provides the human-readable title.

2. **Load context at the right depth.** Three modes:
   - *Minimal*: just gaps and stats. Fast. Use when you know the topic well.
   - *Summary*: manifest plus the synthesis section of the narrative. Good default.
   - *Full*: manifest plus eRAG facts plus wiki plus pghmem search. For when you need the complete picture.

3. **Cross-reference before continuing.** Check if eRAG has grown since last session (someone ran another research on the same slug). Check if the wiki has new entries. Check if pghmem has new decisions. Don't assume the manifest is the only thing that changed.

4. **Present options.** Continue with gaps only. Extend with new sub-questions. Refresh stale sources. Or disposition pending elevation signals (that blog post idea from last session — publish it, defer it, or drop it).

5. **Execute and update.** After research, update the manifest: resolved gaps move to `gaps_resolved`, new gaps appear in `gaps_open`, stats increment, elevation signals get their disposition recorded.

## Schema-Driven, Not Code-Driven

The manifest structure isn't defined in `list_sessions.py`. It's defined in the output schema:

```json
{
  "session": {
    "type": "object",
    "properties": {
      "id": {"type": "string"},
      "status": {"enum": ["active", "paused", "completed", "abandoned"]},
      "pointers": {
        "erag_slug": {"type": ["string", "null"]},
        "wiki_path": {"type": ["string", "null"]},
        "memory_tags": {"type": "array", "items": {"type": "string"}}
      },
      "signals": {
        "gaps_open": {"type": "array", "items": {"type": "string"}},
        "next_steps": {"type": "array", "items": {"type": "string"}}
      }
    }
  }
}
```

The input schema gains three fields for resume operations: `resume_session` (which session), `resume_mode` (gaps_only, extend, refresh), and `resume_context_depth` (minimal, summary, full). The agent doesn't need to know how manifests work internally — it reads the schema and produces conformant output.

## Backward Compatibility

We had existing sessions — markdown files with no manifests. The `list_sessions.py` script handles this. When it finds a `.md` without a matching `.json`, it parses the H1 for the title and the filename for the date. The manifest is authoritative when present, but its absence isn't fatal.

Creating a manifest for a legacy session is one command:

```bash
python3 scripts/list_sessions.py create 2026-04-08-paperclip \
  --erag-slug colemedin-analysis \
  --topic-tag paperclip
```

Idempotent. Run it twice, it updates rather than duplicates.

## What We Learned Building This

**Pointers scale; copies don't.** Three stores today, maybe five tomorrow. If each session duplicated data from all stores, you'd have N×S copies to keep in sync. With pointers, you have N references and S canonical copies. Always.

**Signal data is different from content data.** "This gap is still open" has a fundamentally different lifecycle than "Source X claims Y." Signals change every session. Content accumulates. Mixing them in one store means neither access pattern is optimal.

**Resume is a query, not a restore.** You're not restoring a snapshot. You're asking "what was I doing, what's still unresolved, and what should I do next?" The manifest answers this directly. The actual content lives where it always did.

**Schemas are contracts between sessions.** When the output schema says the manifest has `pointers.erag_slug`, every session produces it the same way. Next session reads it the same way. No implicit conventions. No "well, the slug is usually in the second paragraph."

---

*This is production code running on an Ubuntu server with PostgreSQL + pgvector. The research skill is at v2.2.0. Manifests are in `~/.config/opencode/skills/research/history/sessions/`. The schema files are in `context/schemas/`.*