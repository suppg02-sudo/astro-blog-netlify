---
pubDatetime: 2026-03-15T17:30:00Z
title: "Why AI Agents Keep Forgetting Context (And How to Fix It)"
postSlug: "context-management-ai-agents"
description: "A technical analysis of why LLM-based agents lose context during long sessions and practical solutions using memory systems, flow tracking, and state management."
tags:
  - LLM
  - opencode
  - AI
  - context-management
  - memory-systems
---

## The Problem

You're working with an AI agent on a complex, multi-hour session. Everything is going well. Then suddenly:

1. **Compaction happens** - Context fills up, the model summarizes and compresses
2. **Nuance is lost** - Important details get flattened into generic summaries
3. **Old topics resurface** - The agent brings up things you explicitly moved on from
4. **State confusion** - "What did we do so far?" becomes a real question

This isn't a bug in the model. It's a fundamental limitation of how LLMs work - and it can be mitigated with the right architecture.

---

## Root Cause Analysis

### 1. The Context Window is Finite

Every LLM has a maximum context window. For this session, it's roughly 128K tokens. Sounds like a lot, but:

| Content Type | Token Estimate |
|--------------|----------------|
| System prompt + AGENTS.md | ~15,000 tokens |
| Skills loaded | ~5,000 tokens |
| Conversation history | Grows with each exchange |
| Tool outputs | Can be massive (file reads, command outputs) |

Once the window fills, **compaction** triggers - older messages get summarized into shorter representations.

### 2. Summarization Loses Information

Compaction is lossy compression. A 50-message thread about crustal displacement becomes:

> "User discussed crustal displacement theories, safe zones in Mongolia/Kazakhstan, and shelter construction."

Gone are:
- Which topics were **resolved** vs **pending**
- User's **preferences** and **decisions**
- What was **explicitly dismissed**
- Nuance about **why** certain paths were rejected

### 3. No Persistent State Between Sessions

Each new session starts "fresh" - the model doesn't automatically know:

- What was completed yesterday
- What's still in progress
- What was explicitly abandoned
- Current priorities

### 4. Memory Systems Exist But Aren't Queried

This system has **3,099 memories** in PostgreSQL with pgvector. But at session start, **none of them are automatically retrieved**.

The memory system is:
- ✅ Available (`pghmem` CLI)
- ✅ Fast (0.2ms operations)
- ✅ Semantic search capable
- ❌ **Not queried at session start**
- ❌ **Not integrated into context loading**

---

## The Architecture Gap

```
┌─────────────────────────────────────────────────────────┐
│                    CURRENT STATE                         │
├─────────────────────────────────────────────────────────┤
│                                                          │
│   Session Start                                          │
│        │                                                 │
│        ▼                                                 │
│   Load AGENTS.md ──────────────────────────────────────►│
│        │                                                 │
│        ▼                                                 │
│   Start with NO context about previous work ◄───────────│
│        │                                                 │
│        ▼                                                 │
│   User asks "what did we do?"                           │
│        │                                                 │
│        ▼                                                 │
│   I search session history retroactively                │
│                                                          │
└─────────────────────────────────────────────────────────┘

                    vs.

┌─────────────────────────────────────────────────────────┐
│                    IDEAL STATE                           │
├─────────────────────────────────────────────────────────┤
│                                                          │
│   Session Start                                          │
│        │                                                 │
│        ├──► Query PostgreSQL: recent decisions          │
│        ├──► Query PostgreSQL: current projects          │
│        ├──► Load current_state.md                       │
│        ├──► Check Flow system for active work           │
│        │                                                 │
│        ▼                                                 │
│   Start with context: "Last session: X, Y pending"      │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## Solutions

### Solution 1: Session Initialization Protocol

At the start of EVERY session, automatically:

```bash
# 1. Query recent memories
pghmem search "decision OR action" --recent 7d

# 2. Check for active flows
python3 scripts/hybrid_tracker.py flow list --active

# 3. Load current state file (if exists)
cat ~/.config/opencode/current_state.md
```

This becomes part of the **Phase 0** protocol - before any user interaction.

### Solution 2: Current State File

Create a persistent state file that tracks:

```markdown
# Current State (Updated: 2026-03-15)

## Active Topics
- Crustal displacement research (skill created, Spain analysis pending)

## Recently Completed
- YouTube → Blog workflow (video processed, published)
- Crustal displacement skill created

## Explicitly Closed
- [None currently]

## Pending Questions
- Spain as safe zone option (user asked, not explored)
```

This file gets updated:
- After completing tasks
- When topics are explicitly closed
- When new questions arise

### Solution 3: Topic Lifecycle Tracking

Track topics through explicit states:

| State | Meaning | Action |
|-------|---------|--------|
| `active` | Currently being worked on | Include in context |
| `pending` | Queued for later | Include in "what's next" |
| `completed` | Done, no more work | Summarize briefly only |
| `dismissed` | User explicitly moved on | DO NOT bring back up |

When user says "let's move on" or "forget about that", mark topic as `dismissed`.

### Solution 4: Memory-Driven Context Loading

Instead of loading everything, load **relevant** memories:

```python
def load_context_for_session():
    # Get recent decisions
    recent = pghmem.search("decision", days=7)
    
    # Get active project context
    active = pghmem.search("active OR pending", days=30)
    
    # Exclude dismissed topics
    dismissed = pghmem.search("dismissed", days=30)
    
    return {
        "recent_decisions": recent,
        "active_work": active,
        "avoid_topics": dismissed
    }
```

### Solution 5: Explicit State Transitions

When transitioning between topics:

```
User: "Let's look at Spain"
Agent: [Marks crustal displacement as 'paused']
       [Creates new topic: Spain analysis]
       [Records transition in memory]
```

This prevents the agent from "forgetting" and bringing back old topics.

---

## Implementation Checklist

### Immediate Fixes

- [ ] Create `current_state.md` file
- [ ] Update it after each major task
- [ ] Query it at session start

### Short-Term

- [ ] Add session initialization protocol to AGENTS.md
- [ ] Query PostgreSQL for recent decisions on session start
- [ ] Implement topic lifecycle states

### Long-Term

- [ ] Build automatic context loading from memory
- [ ] Create topic transition tracking
- [ ] Integrate Flow system with session state

---

## The Meta-Irony

This analysis itself will be lost to compaction eventually. The solution? **Save it to memory:**

```bash
python3 ~/.config/opencode/scripts/capture_conversation.py \
    "Context management analysis: Session initialization protocol, current_state.md, topic lifecycle tracking" \
    --type decision \
    --metadata '{"topic": "ai-engineering", "priority": "high"}'
```

And query it next session:

```bash
pghmem search "context management"
```

---

## Key Takeaways

1. **Context windows are finite** - compaction is inevitable
2. **Summarization is lossy** - nuance gets flattened
3. **Memory systems exist** - but must be actively queried
4. **State must be explicit** - not assumed from conversation
5. **Topics need lifecycle tracking** - active → pending → completed → dismissed

The fix isn't a bigger context window. It's **better architecture** around the context we have.

---

## Files Referenced

| File | Purpose |
|------|---------|
| `~/.config/opencode/skills/tracking/SKILL.md` | Flow model for state tracking |
| `~/.config/opencode/skills/hybridmemory/SKILL.md` | PostgreSQL memory system |
| `~/.config/opencode/AGENTS.md` | Global agent instructions |

---

*Analysis performed: 2026-03-15*  
*Memory count at time of analysis: 3,099*