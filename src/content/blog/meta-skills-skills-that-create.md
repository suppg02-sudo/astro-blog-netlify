---
pubDatetime: 2026-03-26T23:28:24Z
title: "Meta-Skills: Skills That Create Skills"
postSlug: "meta-skills-skills-that-create"
description: "Meta-Skills: Skills That Create Skills"
tags:
  - automation
  - meta-skills
  - skill-factory
  - ai
---

> **Series**: Knowledge Crystallization | **Post**: 3/5 | **Complexity**: L3
>
> 📍 Breadcrumb: [Series Home](/posts/knowledge-crystallization-seri) › [1. Problem](/posts/the-problem-why-your-ai-assist) › [2. Architecture](/posts/architecture-progressive-discl) › **3. Meta-Skills**

---

## The Factory Pattern

In software, a **factory** creates other objects. In AI systems, a **meta-skill** creates other skills.

```
┌─────────────────────────────────────────────────────────────┐
│                    META-SKILL PATTERN                        │
│                                                              │
│   skill-factory ───► Creates L1-L5 skills                   │
│   menu-factory ────► Creates compliant menus                │
│   bot-factory ─────► Creates L5 MCP servers (coming)        │
│                                                              │
│   Input: Requirements, patterns, intent                     │
│   Output: Complete, structured skill                        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## The Knowledge Crystallization Pipeline

Meta-skills sit at the heart of a transformation pipeline:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    KNOWLEDGE CRYSTALLIZATION PIPELINE                    │
│                                                                          │
│   Ad-hoc ───► Skills ───► Protocols ───► Scripts ───► APIs ───► MCP     │
│     │          │           │            │          │         │          │
│     L1         L2          L2           L3         L4        L5         │
│     │          │           │            │          │         │          │
│     ▼          ▼           ▼            ▼          ▼         ▼          │
│   Raw      Structured   Sections    Automation  API    Deterministic   │
│                                                                          │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │                     META-SKILLS (Factories)                     │   │
│   │                                                                 │   │
│   │   skill-factory ──► Analyzes sessions, extracts patterns       │   │
│   │   menu-factory ───► Validates menus, applies global options    │   │
│   │   bot-factory ────► Generates MCP servers (future)             │   │
│   └────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Skill Maturity Model (Aligned with CMM)

Your skill levels align with the industry-standard **Capability Maturity Model**:

| CMM Level | Skill Level | Name | Characteristics |
|-----------|-------------|------|-----------------|
| 1: Initial | **L1: Raw** | Chaotic | Single SKILL.md, no automation |
| 2: Repeatable | **L2: Structured** | Documented | YAML metadata, sections, commands |
| 3: Defined | **L3: Script-Attached** | Standard | Shell/Python automation |
| 4: Managed | **L4: API-Integrated** | Quantified | REST endpoints, metrics |
| 5: Optimizing | **L5: MCP/Deterministic** | Optimized | Full MCP server, typed tools |

**Key insight**: Not all skills should reach L5. Methodology skills (research, telos) stay at L2. Only service management needs L5.

---

<details>
<summary>📖 Deep Dive: skill-factory Internals (L1)</summary>

### What skill-factory Does

1. **Session Analysis** - Extracts patterns from recent work
2. **Intent Capture** - Defines WHY before WHAT
3. **Filing Structure** - Creates standardized directories
4. **Progressive Disclosure** - Implements L0-L4 content
5. **Documentation** - Downloads and organizes references
6. **Menu Configuration** - Generates compliant menus
7. **Trigger Registration** - Updates AGENTS.md
8. **History Tracking** - Logs all changes

### The Workflow

```
User: "Create a skill for X
         │
         ▼
┌─────────────────────┐
│  Phase 1: Analyze   │ ───► What type? What domain?
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  Phase 2: Intent    │ ───► Why does this exist? Goals? Scope?
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  Phase 3: Structure │ ───► Create directories, files
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  Phase 4: Content   │ ───► Write SKILL.md with sections
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  Phase 5: Validate  │ ───► Check against schema
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  Phase 6: Register  │ ───► Add trigger to AGENTS.md
└─────────────────────┘
```

### Intent Capture

Every skill captures **intent** before building:

```markdown
# {Skill Name} Intent

## Purpose Statement
{One sentence describing why this skill exists}

## Primary Goals
1. {Goal 1}
2. {Goal 2}

## Scope
### In Scope
| Feature | Priority |
### Out of Scope
| Feature | Reason |

## Success Metrics
| Metric | Target |
```

</details>

---

<details>
<summary>📖 Deep Dive: menu-factory Internals (L1)</summary>

### What menu-factory Does

1. **Global Options** - Manages 11 mandatory options
2. **Templates** - Provides service/workflow/analysis patterns
3. **Validation** - Checks compliance with rules
4. **Learning** - Reorders options by usage frequency

### The 11 Global Options

| Category | Options |
|----------|---------|
| **Utility** | Select Multiple, All of the Above, None, Skip, Refresh |
| **Navigation** | Back, Main Menu, Exit |
| **Meta** | 🔧 Skill Improvement, 🩺 Skill Diagnosis, 🔍 Skill Discovery |

### Validation Rules

| Rule | Value |
|------|-------|
| Label max length | 40 characters |
| Description max length | 60 characters |
| Max options per menu | 10 (before global) |
| Mandatory suffix | Skill Improvement, Diagnosis, Discovery, Exit |

</details>

---

<details>
<summary>🔧 Implementation: Creating a Skill (L2)</summary>

### Full skill-factory Workflow

**Trigger**: `sf` or `skill-factory`

**Phase 1: Skill Type Selection**
```json
{
  "questions": [{
    "question": "What type of skill operation?",
    "options": [
      {"label": "Create New Skill (Recommended)", "description": "Full new skill creation"},
      {"label": "Update Existing Skill", "description": "Modify with new features"},
      {"label": "Evolve Skill Level", "description": "L1→L2, L2→L3, etc."},
      {"label": "Merge Skills", "description": "Combine multiple skills"}
    ]
  }]
}
```

**Phase 2: Requirements Gathering**
```json
{
  "questions": [
    {"question": "What should this skill be called?", "custom": true},
    {"question": "What should this skill do?", "custom": true},
    {"question": "What tasks?", "options": ["Single task", "Multi-step workflow", "Complex automation"]}
  ]
}
```

**Phase 3: File Creation**
```
~/.config/opencode/skills/{skill-name}/
├── SKILL.md              # Created with template
├── context/
│   ├── metadata.json     # Initialized
│   ├── intent.md         # From Phase 2
│   └── environment.md    # For operational skills
├── scripts/              # If L3+
├── docs/                 # If L3+
└── history/
    └── changes.log       # Created
```

</details>

---

## The Skill Schema

For L3+ skills, a structured `skill.yaml` provides machine-readable metadata:

```yaml
name: openrag
version: 1.0.0
description: Document retrieval and RAG stack management
maturity: L3
triggers:
  - openrag
  - rag
category: infrastructure

dependencies:
  required:
    - docker
  skills:
    - openmemory

services:
  - name: openrag-backend
    port: 8001
    url: http://ubuntu4:8001

features:
  intent_capture: true
  progressive_disclosure: true
```

This validates against a JSON Schema to ensure consistency.

---

## The Future: Bot Factory

The next meta-skill will generate **MCP servers** (L5 skills):

```
bot-factory
     │
     ├── Input: skill.yaml + scripts/
     │
     ├── Generates:
     │   ├── MCP server code
     │   ├── Tool schemas
     │   ├── Transport config
     │   └── Test mocks
     │
     └── Output: Deterministic L5 skill
```

---

## What's Next?

In [Post 4: Schemas](/posts/schemas-guardrails-quality-gat), we'll explore:

- JSON Schema for skill validation
- Quality gates at each maturity level
- How schemas enable determinism

---

## Navigation

- ⬅️ [← Previous: Architecture](/posts/architecture-progressive-discl)
- 🏠 [Series Home](/posts/knowledge-crystallization-seri)
- ➡️ [Next: Schemas →](/posts/schemas-guardrails-quality-gat)