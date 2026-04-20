---
pubDatetime: 2026-03-26T23:28:22Z
title: "Architecture: Progressive Disclosure & Hierarchical Context"
postSlug: "architecture-progressive-discl"
description: "Architecture: Progressive Disclosure & Hierarchical Context"
tags:
  - hierarchy
  - architecture
  - ai
  - progressive-disclosure
---

> **Series**: Knowledge Crystallization | **Post**: 2/5 | **Complexity**: L2
>
> 📍 Breadcrumb: [Series Home](/posts/knowledge-crystallization-seri) › [1. Problem](/posts/the-problem-why-your-ai-assist) › **2. Architecture**

---

## The Core Insight

**Don't load everything. Load what's needed, when it's needed.**

This is **Progressive Disclosure** - a UX pattern adapted for AI context management.

---

## The 4-Level Model

```
┌─────────────────────────────────────────────────────────────┐
│                  PROGRESSIVE DISCLOSURE                      │
│                                                              │
│  L0: DEFAULTS ──────► Always loaded (basic rules)           │
│         │                                                    │
│         ▼                                                    │
│  L1: CAPABILITY ─────► On first use (what it does)          │
│         │                                                    │
│         ▼                                                    │
│  L2: WORKING ─────────► During tasks (commands, examples)   │
│         │                                                    │
│         ▼                                                    │
│  L3: REFERENCE ───────► When troubleshooting (full docs)    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

| Level | Name | When Loaded | What's Included | Tokens |
|-------|------|-------------|-----------------|--------|
| **L0** | Defaults | Always | Basic rules, mandatory behaviors | ~100 |
| **L1** | Capability | First use | What it does, quick status | ~500 |
| **L2** | Working | During tasks | Commands, scripts, examples | ~2000 |
| **L3** | Reference | Errors | Full docs, API specs | ~10000+ |

---

## The Loading Flow

```
User triggers skill ───► L0 loaded (defaults only)
         │
         ▼
User asks "what can this do?" ───► L1 loaded (capability)
         │
         ▼
User runs a task ───► L2 loaded (working examples)
         │
         ▼
User hits an error ───► L3 loaded (full reference)
```

**Result**: Same functionality, 90% less context usage.

---

<details>
<summary>📖 Deep Dive: Implementation Details (L1)</summary>

### How Progressive Disclosure Works in Practice

**File Structure**:
```
~/.config/opencode/skills/{skill-name}/
├── SKILL.md              # Main file (L0-L1 content)
├── context/
│   ├── config.json       # Configuration (L2)
│   └── environment.md    # Operational reference (L3)
├── scripts/              # Automation (L2)
├── docs/
│   ├── README.md         # Overview (L1)
│   └── references/       # Full docs (L3)
```

**Loading Logic**:
1. **L0**: Always parse YAML frontmatter + first section
2. **L1**: Read Overview section on first use
3. **L2**: Load scripts/ and context/ when executing
4. **L3**: Read docs/references/ only on errors

**Freshness Headers** (prevent stale data):
```markdown
<!-- last_verified: 2026-03-25 | freshness: 30d | check_if: container version changes -->
```

</details>

---

## Hierarchical Context Inheritance

Progressive disclosure is about **depth**. Hierarchy is about **breadth**.

```
┌─────────────────────────────────────────────────────────────┐
│                  HIERARCHICAL INHERITANCE                    │
│                                                              │
│   globalmenu.md (L0)                                        │
│   │   "Question tool is MANDATORY"                          │
│   │   "Max 5 options per menu"                              │
│   │                                                          │
│   └───┬─────────────────┬─────────────────┐                 │
│       │                 │                 │                 │
│       ▼                 ▼                 ▼                 │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐            │
│   │ Skill A  │    │ Skill B  │    │ Skill C  │            │
│   │  Menu    │    │  Menu    │    │  Menu    │            │
│   └────┬─────┘    └────┬─────┘    └────┬─────┘            │
│        │               │               │                   │
│        └───────────────┴───────────────┘                   │
│                        │                                    │
│                        ▼                                    │
│              + 11 Global Options (inherited)                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### The Pattern

| Level | File | Purpose |
|-------|------|---------|
| **Global** | `globalmenu.md` | Rules that apply to ALL skills |
| **Skill** | `SKILL.md` | Domain-specific options |
| **Merged** | Runtime | Skill options + global options |

### What Gets Inherited

```
Global Options (11 mandatory):
├── Utility (5): Select Multiple, All, None, Skip, Refresh
├── Navigation (3): Back, Main Menu, Exit
└── Meta (3): 🔧 Improvement, 🩺 Diagnosis, 🔍 Discovery
```

Every skill menu automatically gets these 11 options appended.

---

<details>
<summary>📖 Deep Dive: Single Source of Truth (L1)</summary>

### Why This Matters

**Before hierarchy**:
- 50 skills × 4 options each = 200 lines duplicated
- Update one option? Edit 50 files
- Inconsistencies inevitable

**After hierarchy**:
- 1 global file defines 11 options
- All skills inherit automatically
- Update once, applies everywhere

### Implementation

**globalmenu.md** (excerpt):
```markdown
## L0: Always Loaded

### Question Tool (CRITICAL - ALWAYS USE)

**MANDATORY**: When presenting ANY choices, use the question tool.
**NEVER present options as plain text.**
```

**global-menu-options.json** (machine-readable):
```json
[
  {"position": 90, "label": "Select Multiple", "category": "utility"},
  {"position": 91, "label": "All of the Above", "category": "utility"},
  ...
  {"position": 100, "label": "Exit", "category": "navigation"}
]
```

</details>

---

<details>
<summary>🔧 Implementation: Code Example (L2)</summary>

### Menu Merging in Practice

**Skill menu (SKILL.md)**:
```json
{
  "questions": [{
    "question": "What would you like to do?",
    "header": "OpenRAG",
    "options": [
      {"label": "Search Documents (Recommended)", "description": "Query the RAG index"},
      {"label": "Ingest New Files", "description": "Add documents to index"}
    ]
  }]
}
```

**After merging with global options**:
```json
{
  "questions": [{
    "question": "What would you like to do?",
    "header": "OpenRAG",
    "options": [
      {"label": "Search Documents (Recommended)", "description": "Query the RAG index"},
      {"label": "Ingest New Files", "description": "Add documents to index"},
      {"label": "Select Multiple", "description": "Choose several actions"},
      {"label": "All of the Above", "description": "Execute all actions"},
      {"label": "Back", "description": "Return to previous menu"},
      {"label": "🔧 Skill Improvement", "description": "Analyze usage patterns"},
      {"label": "🩺 Skill Diagnosis", "description": "Run health checks"},
      {"label": "🔍 Skill Discovery", "description": "Find related docs"},
      {"label": "Exit", "description": "Return to previous context"}
    ]
  }]
}
```

**Formula**: `Skill Options (≤8) + Global Options (11) = Total (≤19)`

</details>

---

## The Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                     CONTEXT ARCHITECTURE                             │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                    PROGRESSIVE DISCLOSURE (Depth)             │   │
│  │                                                                │   │
│  │    L0 ──────► L1 ──────► L2 ──────► L3                        │   │
│  │   Always    First     Working   Reference                     │   │
│  │    ~100     ~500      ~2000     ~10000+  tokens               │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                    HIERARCHICAL INHERITANCE (Breadth)         │   │
│  │                                                                │   │
│  │    globalmenu.md                                              │   │
│  │         │                                                      │   │
│  │    ┌────┼────┬────────┬────────┐                              │   │
│  │    ▼    ▼    ▼        ▼        ▼                              │   │
│  │  Skill  Skill  Skill  Skill  Skill                            │   │
│  │    │    │    │        │        │                              │   │
│  │    └────┴────┴────────┴────────┘                              │   │
│  │              │                                                │   │
│  │              ▼                                                │   │
│  │        + 11 Global Options                                    │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                      │
│  Result: Right context, right time, minimal tokens                  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## What's Next?

In [Post 3: Meta-Skills](/posts/meta-skills-skills-that-create), we'll explore:

- skill-factory: Skills that create skills
- menu-factory: Standardizing menus
- bot-factory: The next evolution

---

## Navigation

- ⬅️ [← Previous: The Problem](/posts/the-problem-why-your-ai-assist)
- 🏠 [Series Home](/posts/knowledge-crystallization-seri)
- ➡️ [Next: Meta-Skills →](/posts/meta-skills-skills-that-create)