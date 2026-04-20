---
pubDatetime: 2026-03-06T14:30:00Z
title: "Question Tool Centrality: How Your Global Agent Thinks"
postSlug: "question-tool-centrality-ga"
description: "A deep dive into how the Global Agent loads and applies question tool instructions, including the new Centrality section, brainstorm integration requirements, and complete file inventory."
tags:
  - global-agent
  - brainstorm
  - opencode
  - question-tool
  - ai-infrastructure
---

The question tool is the single most important mechanism in the OpenCode system. This post documents how the Global Agent (GA) is configured to understand and apply question tool instructions.

## The Core Principle

```
User ↔ Question Tool ↔ Agent

NOT:
User → Agent decides → Action
```

Every non-trivial interaction **must** flow through the question tool. This is not optional—it is the foundation of how the system operates.

## Why Centrality Matters

| Without Question Tool | With Question Tool |
|----------------------|-------------------|
| Agent assumes user intent | User explicitly chooses |
| One path forward | Multiple options explored |
| Decisions hidden | Decisions transparent |
| User frustrated | User in control |
| AI slop behavior | Human-centered design |

## Mandatory Behaviors (5 Rules)

From `~/.config/opencode/AGENTS.md` (lines 48-54):

1. **NEVER decide for the user** — Always ask
2. **NEVER proceed without preference** — User must choose
3. **ALWAYS paginate at 5 options** — MAX 5 per page, no exceptions
4. **ALWAYS offer next steps** — End with question menu
5. **ALWAYS use for ambiguity** — Multiple valid approaches = question tool

## The Brainstorm Integration (Critical)

When `brainstorm` or `q-brainstorm` is triggered, the agent **must** load patterns from **both** files:

{{< mermaid >}}
flowchart LR
    A[brainstorm trigger] --> B[Load brainstorm.md]
    A --> C[Load q-brainstorm.md]
    B --> D[Apply Patterns]
    C --> D
    D --> E[multiple: true]
    D --> F[3-state selection]
    D --> G[Conflict detection]
    D --> H[Auto-defer]
    D --> I[MAX 5 pagination]
{{< /mermaid >}}

### Patterns Applied

| Pattern | Source | Description |
|---------|--------|-------------|
| `multiple: true` | q-brainstorm.md | All questions in brainstorm use multiselect |
| 3-state selection | q-brainstorm.md | ✅ Commit / ⏸️ Defer / ❌ Skip |
| Conflict detection | q-brainstorm.md | Warn but allow conflicting selections |
| Auto-defer | q-brainstorm.md | Save "Maybe" items to `deferred.json` |
| Category injection | brainstorm.md | Safe/Wildcard/Cross-Domain/Anti-Pattern/Constrained/Historical |
| MAX 5 pagination | AGENTS.md | 5 options per page with Next → / ← Previous |

### Trigger Relationships

| Trigger | Provides | When to Use |
|---------|----------|-------------|
| `brainstorm` | Thinking methodology (phases, categories, wildcards) | Full brainstorming process |
| `q-brainstorm` | Question tool mechanics (3-state, conflict detection) | Enhanced selection UI |
| **Both together** | Maximum effect | **ALWAYS use together** |

## Complete File Inventory

### Primary Source: AGENTS.md

**File:** `~/.config/opencode/AGENTS.md`

| Section | Lines | Purpose |
|---------|-------|---------|
| Question Tool Centrality | 23-91 | Core principle, mandatory behaviors, anti-patterns |
| Brainstorm Integration | 56-78 | Requires loading both brainstorm.md + q-brainstorm.md |
| Question Tool Anti-Patterns | 80-89 | What NEVER to do |
| Question Tool Enforcement | 1187-1244 | Mandatory user input protocol, pagination rules |
| Question Tool Troubleshooting | 1248-1339 | Debug protocol when tool unavailable |

### Trigger Files (Loaded on Demand)

| File | Path | Lines | When Loaded |
|------|------|-------|-------------|
| q.md | `~/.config/opencode/docs/instructions/triggers/q.md` | 765 | When `q` trigger fired |
| brainstorm.md | `~/.config/opencode/docs/instructions/triggers/brainstorm.md` | 337 | When `brainstorm` trigger fired |
| q-brainstorm.md | `~/.config/opencode/docs/instructions/triggers/q-brainstorm.md` | 573 | When `brainstorm` or `q-brainstorm` trigger fired |

### What Each File Contains

**q.md (765 lines):**
- Phase 0: Session Initialization (load state, context detection)
- Phase 1: Questioning Modes (Explore, Build, Debug, Learn, Plan)
- Phase 2: Intensity Control (Minimal → Normal → Verbose → Brainstorm)
- Phase 3: Recording Verification
- Phase 4: History Review & AI Suggestions
- Phase 5: Deferred Decisions
- Phase 6: Context-Specific Workflows (Docker, Database, Network debug menus)
- Phase 7: Meta Controls
- Phase 8: Memory Management

**brainstorm.md (337 lines):**
- Phase 0: Intent Capture (6 brainstorm types)
- Phase 1: Divergent Explosion (12+ options, 4+ categories, paginated)
- Phase 2: Build & Combine
- Phase 3: Convergent Selection
- Phase 4: Action Commitment
- Implementation Checklist (MUST load q-brainstorm.md)
- Cross-Domain Injection Library

**q-brainstorm.md (573 lines):**
- Always Multiselect Mode (`multiple: true`)
- 3-State Selection Pattern (✅/⏸️/❌)
- Custom Text Input
- Conflict Detection (warn but allow)
- Auto-Defer "Maybe" Items
- Best Practices & Anti-Patterns
- Appendix A: Question Tool Discoveries
- Appendix B: Anti-Patterns

## Data Files Used

| File | Path | Purpose |
|------|------|---------|
| session-state.json | `~/.config/opencode/questions/session-state.json` | Current session config |
| deferred.json | `~/.config/opencode/questions/deferred.json` | Deferred items storage |
| decisions.json | `~/.config/opencode/questions/history/decisions.json` | Decision history |
| questions.json | `~/.config/opencode/context-registry/data/questions.json` | Question/choice tracking |

## Loading Summary

| Trigger | Files Loaded | Key Features Applied |
|---------|--------------|---------------------|
| `q` | q.md only | Session menu, 5 modes, 4 intensity levels, meta controls |
| `brainstorm` | brainstorm.md + q-brainstorm.md | Diverge/Build/Converge phases, `multiple: true`, 3-state, auto-defer |
| `q-brainstorm` | q-brainstorm.md | Enhanced question tool, conflict detection, auto-defer |

## Anti-Patterns (Never Do)

| ❌ Anti-Pattern | ✅ Correct Behavior |
|----------------|---------------------|
| Make decision without asking | Present options, let user choose |
| Show 8+ options on one page | Paginate at 5 per page |
| Skip question tool "to save time" | Always use for non-trivial choices |
| Assume user preference | Ask explicitly |
| Single-select in brainstorm | Always `multiple: true` |
| Block on conflicts | Warn but allow |

## Key Takeaways

1. **The question tool is central** — All decisions flow through it, not around it
2. **Brainstorm requires both files** — Never load just one; they're designed to work together
3. **Pagination is mandatory** — MAX 5 options per page, no exceptions
4. **Conflict detection is permissive** — Warn but allow; user may have valid reasons
5. **Everything is tracked** — Session state, deferred items, decisions, and question history

---

**File Links:**
- [AGENTS.md](http://ubuntu4:8080/editor/opencode/AGENTS.md)
- [q.md](http://ubuntu4:8080/editor/opencode/docs/instructions/triggers/q.md)
- [brainstorm.md](http://ubuntu4:8080/editor/opencode/docs/instructions/triggers/brainstorm.md)
- [q-brainstorm.md](http://ubuntu4:8080/editor/opencode/docs/instructions/triggers/q-brainstorm.md)