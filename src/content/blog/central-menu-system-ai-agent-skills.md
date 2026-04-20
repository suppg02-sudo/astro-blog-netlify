---
pubDatetime: 2026-02-27T03:20:00Z
title: "Central Menu System for AI Agent Skills"
postSlug: "central-menu-system-ai-agent-skills"
description: "Central Menu System for AI Agent Skills"
tags:
  - skills
  - opencode
  - ai-agents
  - architecture
---

Building a skill system for AI agents is easy. Keeping it consistent as it grows to 70+ skills? That's where architecture matters.

This post covers the design and implementation of a **Central Menu System** that ensures every skill has consistent navigation, discovery features, and progressive context disclosure.

## The Problem

As skill libraries grow, inconsistencies creep in:

- Different menus have different navigation patterns
- Users don't know how to discover related documentation
- No standard way to improve menus based on usage
- Context gets duplicated across skills

## The Solution: Central Menu Configuration

A single source of truth that all skills reference for mandatory options:

```
~/.config/opencode/skills/skill-discovery/
├── SKILL.md                    # Authoritative reference
├── context/
│   ├── central-menu.json       # ⭐ Mandatory options for ALL skills
│   └── index.json
├── scripts/
│   └── analyze-structure.py    # Structure analysis
└── reports/
    └── structure-report-*.md   # Analysis output
```

### Mandatory Menu Suffix

Every skill menu must end with these options:

```json
[
  {"label": "🔍 Skill Discovery", "description": "Discover related docs, improve this menu, learn from your choices"},
  {"label": "Exit", "description": "Return to previous context"}
]
```

## Features

### 1. Document Discovery

Finds related configs, documentation, and references for any skill:

- Local files (configs, templates, examples)
- GitHub repositories (README, docs/)
- Related skills and their contexts
- Environment-specific files

### 2. Skill Structure Analysis

Analyzes all skills and reports maturity levels:

```
L0 (Missing) → L1 (Raw) → L2 (Structured) → L3 (Scripts) → L4 (Templates) → L5 (Complete)
```

| Level | Count | Description |
|-------|-------|-------------|
| L5 | 1 | Complete with MCP |
| L4 | 2 | Has templates/context |
| L3 | 5 | Has automation scripts |
| L2 | 42 | Structured with YAML |
| L1 | 21 | SKILL.md only |
| L0 | 3 | Missing SKILL.md |

Run analysis:

```bash
python3 ~/.config/opencode/skills/skill-discovery/scripts/analyze-structure.py --all
```

### 3. Progressive Disclosure

Four-level context loading to minimize token usage:

| Level | When Loaded | Content |
|-------|-------------|---------|
| 0 | Always | Skill names, descriptions, triggers |
| 1 | On selection | YAML metadata, prerequisites |
| 2 | On execution | Full SKILL.md, scripts |
| 3 | On demand | Deep references, templates |

### 4. Menu Improvement

Analyzes recent choices and suggests improvements:

- Add custom inputs as permanent options
- Remove never-used options
- Reorder by popularity
- Merge similar options

### 5. Custom Input Learning

When users type their own answers:

```json
{
  "question": "You typed: '[user-input]'. Would you like to:",
  "options": [
    {"label": "Add as Permanent Option", "description": "Add this to the menu"},
    {"label": "Add as Shortcut", "description": "Create quick trigger"},
    {"label": "Just Record It", "description": "Store in history only"}
  ]
}
```

## Usage

### Trigger Words

- `skill` - Most intuitive
- `sd` - Short form
- `skill-discovery` - Full name

### From Any Skill Menu

Select "🔍 Skill Discovery" from any skill's menu to access all features.

## Architecture Decisions

### Why Central Configuration?

1. **Consistency** - All skills have the same navigation options
2. **Maintainability** - Update one file, all skills reflect changes
3. **Discoverability** - Users always know how to access discovery features
4. **Progressive Disclosure** - Central point for context loading

### Why Not Inheritance?

Skills are documentation files, not classes. A reference-based approach works better:

- Skills reference the central config file
- No complex inheritance chains
- Easy to audit which skills are compliant

## Integration Example

Before:
```json
{
  "options": [
    {"label": "Install Containers", "description": "..."},
    {"label": "View Status", "description": "..."}
  ]
}
```

After:
```json
{
  "options": [
    {"label": "Install Containers", "description": "..."},
    {"label": "View Status", "description": "..."},
    {"label": "🔍 Skill Discovery", "description": "Discover related docs, improve this menu"},
    {"label": "Exit", "description": "Return to previous context"}
  ]
}
```

## Results

After implementing the Central Menu System:

- **12 skills** updated with Skill Discovery option
- **74 skills** analyzed for structure compliance
- **3 skills** identified as needing SKILL.md creation
- **24 skills** flagged for YAML frontmatter addition

## Next Steps

1. Fix L0 skills (missing SKILL.md)
2. Add YAML to L1 skills
3. Upgrade L2→L3 with automation scripts
4. Identify candidates for L5 MCP integration

## Conclusion

A central menu system provides the scaffolding for skill library growth. As you add more capabilities, the navigation and discovery patterns remain consistent. Users can always find what they need, and the system learns from usage patterns to improve over time.

The key insight: **Consistency at scale requires centralization of common patterns**. Every skill should feel familiar, even if it does something completely different.