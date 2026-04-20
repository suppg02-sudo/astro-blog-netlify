---
pubDatetime: 2026-03-21T23:45:00Z
title: "Meta-Skills: The Factory Pattern for Self-Evolving AI Systems"
postSlug: "meta-skills-factory-pattern"
description: "How Skill Factory and Menu Factory enable the personal assistant to create, validate, and improve its own skills."
tags:
  - menu-factory
  - automation
  - meta-skills
  - skill-factory
  - factory-pattern
---

## The Meta-Concept

What if an AI system could create and improve itself? Meta-skills are skills that operate on other skills — creating, validating, and optimizing them. This is the Factory Pattern applied to AI capabilities.

## The Two Factories

```mermaid
graph TB
    subgraph "Skill Factory"
        SF_ANALYZE[Session Analysis]
        SF_CAPTURE[Pattern Capture]
        SF_CREATE[Skill Creation]
        SF_VALIDATE[Quality Gates]
    end
    
    subgraph "Menu Factory"
        MF_VALIDATE[Menu Validation]
        MF_LEARN[Menu Learning]
        MF_APPLY[Apply Learning]
        MF_AUDIT[Audit All Skills]
    end
    
    USER[User Request] --> SF_ANALYZE
    SF_ANALYZE --> SF_CAPTURE
    SF_CAPTURE --> SF_CREATE
    SF_CREATE --> SF_VALIDATE
    SF_VALIDATE --> SKILL[New/Updated Skill]
    
    SKILL --> MF_VALIDATE
    MF_VALIDATE --> MF_LEARN
    MF_LEARN --> MF_APPLY
    MF_APPLY --> OPTIMIZED[Optimized Menu]
    
    MF_LEARN --> MENU_DATA[Usage Data]
    MENU_DATA --> MF_APPLY
```

## Skill Factory

### Purpose

Standardize skill creation with:
- Consistent 13-section structure
- Quality gates per maturity level
- Progressive disclosure templates
- Automatic validation

### The 13-Section Structure

```mermaid
graph LR
    subgraph "Metadata"
        M1[YAML Frontmatter]
    end
    
    subgraph "Core Sections"
        S1[Overview]
        S2[Trigger Commands]
        S3[Section 1-N]
    end
    
    subgraph "Integration"
        I1[Menu Configuration]
        I2[Related Skills]
        I3[History]
        I4[Quick Reference]
    end
    
    M1 --> S1 --> S2 --> S3 --> I1 --> I2 --> I3 --> I4
```

### Maturity Levels

| Level | Name | Characteristics | Target For |
|-------|------|-----------------|------------|
| **L1** | Raw | SKILL.md only | Physical processes |
| **L2** | Structured | Metadata, sections, commands | Methodologies |
| **L3** | Script-Attached | Shell/Python automation | Automation tasks |
| **L4** | API-Integrated | REST/GraphQL endpoints | Data processing |
| **L5** | MCP/Deterministic | Full MCP server, typed tools | Service management |

### Creation Workflow

```mermaid
sequenceDiagram
    participant User
    participant Agent
    participant SkillFactory
    participant MenuFactory
    
    User->>Agent: Create skill for X
    Agent->>SkillFactory: Load skill-factory
    SkillFactory->>Agent: Present workflow
    
    Agent->>User: Confirm creation
    User->>Agent: Approve
    
    SkillFactory->>SkillFactory: Analyze session
    SkillFactory->>SkillFactory: Capture patterns
    SkillFactory->>SkillFactory: Generate structure
    
    SkillFactory->>MenuFactory: Validate menu
    MenuFactory->>MenuFactory: Check rules
    MenuFactory->>SkillFactory: Validation result
    
    SkillFactory->>Agent: Skill created
    Agent->>User: Confirmation
```

### File Structure

```
skill-name/
├── SKILL.md              # Main skill file
├── context/
│   ├── config.json       # User preferences
│   ├── templates.json    # L1-L4 templates
│   └── examples.md       # Usage examples
├── scripts/
│   ├── main.sh           # Main automation
│   └── helpers.py        # Helper functions
├── history/
│   └── changes.log       # Change history
└── docs/
    └── advanced.md       # Deep documentation
```

## Menu Factory

### Purpose

Ensure all skill menus follow rules and adapt to user behavior.

### Validation Rules

| Rule | Value | Why |
|------|-------|-----|
| Label max length | 40 chars | Readability |
| Description max length | 60 chars | Conciseness |
| Max options per menu | 10 | Cognitive load |
| Required suffix | Skill Discovery + Exit | Navigation |

### Menu-Learning Integration

```mermaid
flowchart LR
    USER[User Selects Option] --> LOG[Log Selection]
    LOG --> DATA[Usage Data]
    DATA --> ANALYZE[Analyze Frequency]
    ANALYZE --> REORDER[Reorder Options]
    REORDER --> NEXT[Next Session]
    NEXT --> TOP[Top Options First]
```

### Validation Script

```bash
# Validate a specific skill
python3 scripts/validate.py --skill reminder

# Validate all skills
python3 scripts/validate.py --all

# Auto-fix missing suffix
python3 scripts/validate.py --skill reminder --fix
```

### Apply Learning

```bash
# Reorder a skill's menu by usage
python3 scripts/apply-learning.py --skill reminder
```

## Factory Integration

```mermaid
graph TB
    subgraph "Creation Flow"
        REQ[Create Skill Request] --> SF[Skill Factory]
        SF --> STRUCTURE[Generate Structure]
        STRUCTURE --> MENU[Generate Menu]
        MENU --> MF[Menu Factory]
        MF --> VALIDATE{Valid?}
        VALIDATE -->|Yes| CREATE[Create Files]
        VALIDATE -->|No| FIX[Fix Issues]
        FIX --> VALIDATE
        CREATE --> BACKUP[Backup]
        BACKUP --> DEPLOY[Deploy]
    end
```

## Current Skills Stats

```mermaid
pie title 74 Skills by Maturity Level
    "L5 - MCP/Deterministic" : 1
    "L4 - API-Integrated" : 2
    "L3 - Script-Attached" : 5
    "L2 - Structured" : 42
    "L1 - Raw" : 21
    "L0 - Incomplete" : 3
```

## Quality Gates

### L1 → L2 Transition
- [ ] YAML frontmatter complete
- [ ] All 13 sections present
- [ ] Menu configuration valid
- [ ] Related skills listed

### L2 → L3 Transition
- [ ] Scripts directory created
- [ ] Main automation script
- [ ] Helper functions
- [ ] Error handling

### L3 → L4 Transition
- [ ] API endpoints defined
- [ ] Request/response schemas
- [ ] Authentication
- [ ] Rate limiting

### L4 → L5 Transition
- [ ] MCP server implementation
- [ ] Typed tool definitions
- [ ] Schema validation
- [ ] Policy gates

## Example: Creating a Skill

```bash
# User says: "create a skill for tracking daily habits"

# 1. Skill Factory analyzes request
# 2. Generates structure:
```

```yaml
---
name: habit-tracker
version: 1.0.0
description: Track daily habits with streak counting and reminders
trigger: habit, habits, daily
maturity: L2
created: 2026-03-21
dependencies:
  - reminder
  - telegram
tags: [habits, tracking, daily, streaks]
---
```

```markdown
# Habit Tracker

## Overview
Track daily habits with streak counting, reminders, and progress visualization.

## Trigger Commands
- `habit` - Open habit tracker
- `habits` - List all habits
- `daily` - Today's habits

## Section 1: Habit Model
...

## Menu Configuration
{
  "questions": [{
    "question": "🎯 Habit Tracker - What would you like to do?",
    "header": "Habits",
    "options": [
      {"label": "📋 Today's Habits (Recommended)", "description": "View and complete today's habits"},
      {"label": "➕ Add Habit", "description": "Create a new habit to track"},
      {"label": "🔥 View Streaks", "description": "See your current streaks"},
      {"label": "📊 Weekly Report", "description": "Habit completion statistics"},
      {"label": "🔍 Skill Discovery", "description": "Related docs, improve menu"},
      {"label": "Exit", "description": "Return to previous context"}
    ],
    "multiple": false
  }]
}
```

## The Self-Improvement Loop

```mermaid
graph TB
    CREATE[Skill Created] --> USE[User Uses Skill]
    USE --> TRACK[Track Selections]
    TRACK --> ANALYZE[Analyze Patterns]
    ANALYZE --> IMPROVE[Improve Menu]
    IMPROVE --> USE
    
    USE --> FEEDBACK[User Feedback]
    FEEDBACK --> UPDATE[Update Skill]
    UPDATE --> CREATE
```

## Next Post

In the final deep dive, we'll explore **Reminders & Research** — how time-based triggers and deep research capabilities support the entire ecosystem.

---

*This is part 4 of 5 in the Personal Assistant Ecosystem series.*