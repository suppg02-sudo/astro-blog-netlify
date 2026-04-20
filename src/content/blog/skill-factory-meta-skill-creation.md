---
pubDatetime: 2026-03-08T16:15:00Z
title: "Skill-Factory: A Meta-Skill for Creating AI Agent Skills"
postSlug: "skill-factory-meta-skill-creation"
description: "Created skill-factory, a comprehensive meta-skill for creating and updating AI agent skills with consistent structure, progressive disclosure, and optional RAG integration"
tags:
  - skills
  - opencode
  - ai-agents
  - automation
  - meta-skill
---

## Overview

Today I created **skill-factory**, a meta-skill that provides a standardized protocol for creating and updating ANY skill in the OpenCode ecosystem. This fills a significant gap in the existing infrastructure.

## The Problem

While there were scattered resources for skill creation:
- `skill-pattern-creation.md` - Reference guide
- `skillmenu.md` - Basic 7-phase workflow
- AGENTS.md protocol - Post-creation checklist

There was no comprehensive, executable methodology for systematically creating skills with consistent structure.

## The Solution: Skill-Factory

### 13-Section Progressive Disclosure Structure

1. **Session Analysis** - Extract requirements from conversation
2. **Filing Structure** - Standard directory layout
3. **Backup Protocol** - Timestamped backups with retention
4. **Progressive Disclosure** - SKILL.md templates
5. **Documentation Management** - Basic + optional RAG
6. **Scripts & Automation** - Shell script standards
7. **Cron Jobs** - Scheduled task templates
8. **Menu Configuration** - With mandatory Skill Discovery
9. **Trigger Registration** - AGENTS.md updates
10. **History Tracking** - Change logs + session records
11. **Related Skills** - Discovery + categorization
12. **Quality Gates** - Per-maturity validation (L1-L5)
13. **Publishing Workflow** - Blog + Supermemory + backup

### Standard Filing Structure

```
~/.config/opencode/skills/{skill-name}/
├── SKILL.md              # Main skill file (REQUIRED)
├── scripts/              # Automation scripts
├── context/              # Progressive disclosure data
├── templates/            # Reusable templates
├── history/              # Historical data
└── docs/                 # Local documentation
```

### Quality Gates Per Maturity Level

| Level | Requirements |
|-------|--------------|
| L1 | SKILL.md exists |
| L2 | YAML metadata, sections |
| L3 | Scripts attached |
| L4 | API documented |
| L5 | MCP server |

### Optional RAG Module

For skills needing smart document retrieval:
- Metadata strategy with tags structure
- Chunking strategies by document type
- Database choice (SQLite vs PostgreSQL)
- Embedder options (local vs cloud)

## Validation

Research confirmed skill-factory is a **novel contribution**:

- First meta-skill specifically for creating/updating other skills
- Comprehensive 13-section methodology vs scattered documentation
- Operational protocols that didn't exist before
- RAG integration strategy with guidance
- Quality gates per maturity level

## Test Case: Router Skill

Successfully aligned the existing `router` skill with skill-factory standards:

- Added YAML frontmatter with metadata
- Created `context/metadata.json`
- Created `history/changes.log` + session files
- Added Related Skills + History sections
- Updated maturity to L4

## Usage

```
sf              # Launch skill-factory menu
skill-factory   # Full workflow
```

## Related Skills

- **skill-discovery** - Structure analysis
- **menu-learning** - Adaptive menus
- **blog-post-creator** - Publishing
- **openmemory** - RAG embedding

---

**Created**: 2026-03-08  
**Maturity**: L3 (scripts attached)  
**Location**: `~/.config/opencode/skills/skill-factory/SKILL.md`