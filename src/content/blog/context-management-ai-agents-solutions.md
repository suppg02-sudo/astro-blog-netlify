---
pubDatetime: 2026-03-15T20:45:00Z
title: "Context Management Solutions for AI Agents - Implementation Guide"
postSlug: "context-management-ai-agents-solutions"
description: "Practical implementation of context management solutions: Session Initialization Protocol, current_state.md tracking, Memory Save Protocol, and topic lifecycle states."
tags:
  - LLM
  - opencode
  - AI
  - context-management
  - memory-systems
  - implementation
---

## What We Built

Following the analysis of why AI agents lose context, we implemented a complete solution:

| Component | File | Purpose |
|-----------|------|---------|
| **Session Initialization Protocol** | `AGENTS.md` | Load state at session start |
| **Current State File** | `current_state.md` | Track active/completed/dismissed topics |
| **Memory Save Protocol** | `AGENTS.md` | When and how to save to memory |
| **Topic Lifecycle States** | `AGENTS.md` | Explicit state tracking |

---

## 1. Session Initialization Protocol

Added to `~/.config/opencode/AGENTS.md`:

```markdown
## Session Initialization Protocol (CRITICAL)

At the start of EVERY session, the agent MUST:

# 1. Load current state file
cat ~/.config/opencode/current_state.md

# 2. Query recent decisions from PostgreSQL memory
pghmem search "decision"

# 3. Check for active flows
python3 ~/.config/opencode/scripts/hybrid_tracker.py flow list --active
```

### Why This Matters

| Problem | Solution |
|---------|----------|
| Context compaction loses nuance | `current_state.md` preserves topic state |
| Session starts "fresh" | PostgreSQL queries restore recent decisions |
| Old topics resurface | Dismissed topics tracked explicitly |

---

## 2. Current State File

Created `~/.config/opencode/current_state.md`:

```markdown
# Current State

**Last Updated**: 2026-03-15T20:25:00Z
**Session ID**: ses_30d083984ffevzBTdUFS9jEi1C

---

## Active Topics

| Topic | Status | Notes |
|-------|--------|-------|
| (none currently active) | - | - |

---

## Recently Completed

| Topic | Completed | Outcome |
|-------|-----------|---------|
| Context management improvement | 2026-03-15 20:25 | Blog published, AGENTS.md updated |
| YouTube → Blog workflow | 2026-03-15 19:35 | Video processed, published |
| Crustal displacement skill | 2026-03-15 03:57 | SKILL.md created |

---

## Explicitly Closed / Dismissed

| Topic | Closed | Reason |
|-------|--------|--------|
| (none) | - | - |

---

## Pending Questions

| Question | Asked | Status |
|----------|-------|--------|
| Spain as safe zone option | 2026-03-15 04:00 | NOT explored |
```

---

## 3. Memory Save Protocol

Added to `AGENTS.md`:

### When to Save to Memory

| Trigger | Memory Type | Example |
|---------|-------------|---------|
| **Major task completed** | `decision` | Feature implemented, bug fixed |
| **File created/modified** | `action` | New skill, blog post |
| **Decision made** | `decision` | Architecture choice |
| **Research completed** | `conversation` | Deep dive, investigation |
| **User preference expressed** | `decision` | "I prefer X" |
| **Topic explicitly closed** | `decision` | "move on", "done" |

### Command

```bash
python3 ~/.config/opencode/scripts/capture_conversation.py \
    "Brief summary of what was done/decided" \
    --type decision \
    --tags "topic,subtopic"
```

### Memory Types

| Type | When to Use |
|------|-------------|
| `decision` | Choices, preferences, architecture decisions |
| `action` | Files created, commands run, changes made |
| `conversation` | Research, discussions, explorations |
| `exchange` | Quick checkpoints (automatic via cron) |

---

## 4. Topic Lifecycle States

| State | Meaning | Action |
|-------|---------|--------|
| `active` | Currently being worked on | Include in context |
| `pending` | Queued for later | Include in "what's next" |
| `completed` | Done, no more work | Summarize briefly only |
| `dismissed` | User explicitly moved on | **DO NOT bring back up** |

### When User Says "Move On"

1. Add topic to "Explicitly Closed" section in `current_state.md`
2. Save decision to PostgreSQL memory
3. Do NOT bring the topic back up unless user explicitly asks

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    NEW SESSION FLOW                      │
├─────────────────────────────────────────────────────────┤
│                                                          │
│   Session Start                                          │
│        │                                                 │
│        ├──► Read current_state.md                        │
│        │    (active topics, completed, dismissed)        │
│        │                                                 │
│        ├──► Query pghmem search "decision"               │
│        │    (recent decisions from PostgreSQL)           │
│        │                                                 │
│        ├──► Check Flow system for active work            │
│        │                                                 │
│        ▼                                                 │
│   Agent has context: "Last session: X, Y pending"        │
│                                                          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                    DURING SESSION                        │
├─────────────────────────────────────────────────────────┤
│                                                          │
│   Major task completed ──► Save to memory (decision)     │
│   File created ──────────► Save to memory (action)       │
│   Decision made ─────────► Save to memory (decision)     │
│   User says "move on" ───► Mark topic as dismissed       │
│                             + Save to memory             │
│                                                          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                    SESSION END                           │
├─────────────────────────────────────────────────────────┤
│                                                          │
│   Update current_state.md:                               │
│   - Move active → completed                              │
│   - Add new pending questions                            │
│   - Update last updated timestamp                        │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## Files Created/Modified

| File | Action | Purpose |
|------|--------|---------|
| `~/.config/opencode/AGENTS.md` | Modified | Added Session Init + Memory Save protocols |
| `~/.config/opencode/current_state.md` | Created | Tracks topic states |
| `/media/docker/website/content/posts/context-management-ai-agents.md` | Created | Analysis blog post |
| `/media/docker/website/content/posts/context-management-ai-agents-solutions.md` | Created | This implementation guide |

---

## Verification

```bash
# Check protocols are in AGENTS.md
grep -A5 "Session Initialization Protocol" ~/.config/opencode/AGENTS.md
grep -A5 "Memory Save Protocol" ~/.config/opencode/AGENTS.md

# Check state file exists
cat ~/.config/opencode/current_state.md

# Verify memories are searchable
pghmem search "context management"
```

---

## Key Takeaways

1. **Context windows are finite** - compaction is inevitable
2. **State must be explicit** - not assumed from conversation
3. **Memory systems must be queried** - having them isn't enough
4. **Topics need lifecycle tracking** - dismissed topics should stay dismissed
5. **The fix is architecture, not bigger context** - better systems around the context we have

---

*Implemented: 2026-03-15*  
*Memory system: PostgreSQL with pgvector (3,101 memories)*