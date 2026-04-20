---
pubDatetime: 2026-03-07T00:00:00Z
title: "Question Tool Documentation Analysis: Consolidation & Progressive Disclosure"
postSlug: "question-tool-documentation-analysis"
description: "Question Tool Documentation Analysis: Consolidation & Progressive Disclosure"
tags:
  - opencode
  - question-tool
  - documentation
  - consolidation
---

## Summary

Analyzed 4 core documentation files (1,484 lines) for the OpenCode question tool system. Found 3 conflicts, 4 gaps, and proposed a single-file consolidation with 4-layer progressive disclosure structure.

## Files Analyzed

| File | Lines | Purpose |
|------|-------|---------|
| AGENTS.md (lines 23-90) | 68 | Core principles, mandatory behaviors |
| q.md | 353 | Context-aware suggestions |
| brainstorm.md | 490 | Divergent thinking methodology |
| q-brainstorm.md | 573 | Question tool UI mechanics |

## Conflicts Found

### 🔴 Critical: Intensity Levels Inconsistency

**AGENTS.md** defines:
- `minimal`: Max 4 options
- `normal`: Max 8 options
- `verbose`: Max 12 options
- `brainstorm`: Max 15 options

**q-brainstorm.md appendix** suggests:
- `brainstorm mode`: 6-9 options

**Resolution**: AGENTS.md is source of truth. Remove conflicting appendix.

### 🔴 Critical: MAX 5 Rule Violation

**AGENTS.md** states:
> **ALWAYS paginate at 5 options** - MAX 5 per page, no exceptions

**q-brainstorm.md appendix** suggests:
> Brainstorm mode: 6-9 options (with scrolling)

**Resolution**: Enforce MAX 5 universally with pagination.

### 🟡 Minor: Storage Location Duplication

Multiple files reference the same paths without a single manifest:
- `~/.config/opencode/questions/session-state.json`
- `~/.config/opencode/questions/deferred.json`
- `~/.config/opencode/context-registry/data/questions.json`

**Resolution**: Create single storage manifest in consolidated file.

## Gaps Identified

1. **No Quick Reference Card** - Agents must read 1,484 lines to understand system
2. **Q + Brainstorm Not Integrated** - Intensity settings don't auto-sync with brainstorm modes
3. **Error Recovery Not Documented** - What happens on timeout, invalid selection, conflicts?
4. **No Progressive Disclosure** - All docs at same depth level

## Proposed Solution: Single Consolidated File

### Structure (4 Layers)

```
QUESTION-SYSTEM.md
├── L0: Quick Reference Card (1 page)
│   ├── Triggers at a glance
│   ├── Intensity levels table
│   ├── MAX 5 rule
│   └── Storage locations
├── L1: Core Principles
│   ├── Question Tool Centrality
│   ├── Mandatory Behaviors
│   └── Anti-Patterns
├── L2: Trigger Implementations
│   ├── Q Trigger
│   ├── Brainstorm Trigger
│   ├── Q-Brainstorm Trigger
│   └── Relationship diagram
└── L3: Full Methodology
    ├── Complete workflows
    ├── All examples
    └── Stress test methodology
```

### Progressive Disclosure Benefits

| Layer | Audience | When to Read |
|-------|----------|--------------|
| L0 | All users | Every interaction |
| L1 | New users | First time setup |
| L2 | Developers | Implementing triggers |
| L3 | Power users | Deep customization |

## Trigger Relationship Diagram

```
Q Trigger (context-aware)
    │
    ├── Intensity Control
    ├── Mode Selection
    └── Settings Access
            │
            ├── Brainstorm (methodology)
            │       └── Thinking process
            │
            └── Q-Brainstorm (UI mechanics)
                    └── Selection mechanics
                    
Both brainstorm + q-brainstorm → Use together for maximum effect
```

## Action Items Completed

1. ✅ Created consolidated `QUESTION-SYSTEM.md` at `~/.config/opencode/docs/instructions/QUESTION-SYSTEM.md`
2. ✅ Resolved intensity levels conflict (AGENTS.md = source of truth)
3. ✅ Enforced MAX 5 rule universally
4. ✅ Created single storage manifest
5. ✅ Added progressive disclosure structure (L0→L3)
6. ✅ Documented error recovery patterns

## Recommendation: OpenMemory vs MD Files

**Question**: Should skills/instructions be stored in OpenMemory instead of MD files?

**Analysis**:

| Aspect | MD Files | OpenMemory |
|-------|---------|------------|
| Version Control | ✅ Git-tracked | ❌ Not tracked |
| Human Readable | ✅ Direct access | ❌ Requires query |
| Agent Query | ❌ Must read file | ✅ Semantic search |
| Updates | ✅ Edit + commit | ⚠️ Delete + re-store |
| Progressive Disclosure | ⚠️ Manual | ✅ Query by depth |
| Context Efficiency | ❌ Full file load | ✅ Targeted retrieval |

**Recommendation**: **Hybrid Approach**
- MD Files = Source of Truth (version controlled)
- OpenMemory = Runtime Cache (semantic queries)
- Sync on creation/update

## Files Changed

| File | Action |
|------|--------|
| `QUESTION-SYSTEM.md` | Created (consolidated docs) |
| AGENTS.md | Updated to reference QUESTION-SYSTEM.md |
| q-brainstorm.md appendix | Marked for removal (conflicts) |

---

**Related**: 
- [QUESTION-SYSTEM.md](http://ubuntu4:8080/editor/opencode/docs/instructions/QUESTION-SYSTEM.md)
- [AGENTS.md](http://ubuntu4:8080/editor/opencode/AGENTS.md)