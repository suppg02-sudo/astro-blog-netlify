---
pubDatetime: 2026-03-21T23:40:00Z
title: "Life Orchestrator: Unified Lifecycle Management with Plant→Grow→Harvest→Rest"
postSlug: "life-orchestrator-architecture"
description: "How the Orchestrator skill unifies tracking across all life domains using a natural lifecycle model with phase-appropriate reminders."
tags:
  - lifecycle
  - productivity
  - automation
  - orchestration
  - domains
---

## The Problem

Life has many domains — garden, work, personal goals, blog, energy management. Each has its own rhythm, its own milestones, its own way of tracking progress. How do you unify them without forcing everything into the same mold?

## The Solution: Natural Lifecycle

Every living thing follows the same pattern: **Plant → Grow → Harvest → Rest**. The Orchestrator applies this natural cycle to everything you track.

```mermaid
graph LR
    PLANT[🌱 Plant<br/>Starting/Planning] --> GROW[📈 Grow<br/>Developing/Nurturing]
    GROW --> HARVEST[🎯 Harvest<br/>Completing/Achieving]
    HARVEST --> REST[😴 Rest<br/>Reflecting/Reviewing]
    REST --> PLANT
```

## Phase Characteristics

| Phase | Emoji | Meaning | Reminder Style | Default Frequency |
|-------|-------|---------|----------------|-------------------|
| **plant** | 🌱 | Starting, planning, sowing | Gentle, encouraging | Weekly |
| **grow** | 📈 | Developing, nurturing, working | Regular, informative | Daily |
| **harvest** | 🎯 | Completing, collecting, achieving | Urgent, time-sensitive | Daily (escalating) |
| **rest** | 😴 | Reflecting, pausing, reviewing | Minimal, review-focused | Monthly |

## Architecture

```mermaid
graph TB
    subgraph "Input Layer"
        CLI[CLI Commands]
        TRIGGER[Trigger Words: orch, life]
        TEL[Telegram Commands]
    end
    
    subgraph "Core Engine"
        ORCH[Orchestrator Engine]
        PHASE[Phase Manager]
        REM[Reminder Scheduler]
    end
    
    subgraph "Storage Layer"
        PG[(PostgreSQL)]
        DOMAINS[domains.json]
        CONFIG[config.json]
    end
    
    subgraph "Output Layer"
        NOTIFY[Telegram Notifications]
        REPORT[Reports]
        VIEWS[Views: Today, Week, Overdue]
    end
    
    CLI --> ORCH
    TRIGGER --> ORCH
    TEL --> ORCH
    ORCH --> PHASE
    ORCH --> REM
    PHASE --> PG
    REM --> PG
    ORCH --> DOMAINS
    ORCH --> CONFIG
    REM --> NOTIFY
    ORCH --> REPORT
    ORCH --> VIEWS
```

## Domains

Each domain has phase-specific terminology:

```mermaid
graph LR
    subgraph "Garden 🌱"
        G1[Sowing] --> G2[Growing] --> G3[Picking] --> G4[Winter]
    end
    
    subgraph "Work 💼"
        W1[Planning] --> W2[Execution] --> W3[Delivery] --> W4[Retrospective]
    end
    
    subgraph "Personal 🧑"
        P1[Commitment] --> P2[Building] --> P3[Achievement] --> P4[Reflection]
    end
    
    subgraph "Blog 📝"
        B1[Ideation] --> B2[Writing] --> B3[Publish] --> B4[Analysis]
    end
    
    subgraph "Energy ⚡"
        E1[Install] --> E2[Generate] --> E3[Save] --> E4[Maintain]
    end
```

## Item Data Model

Every tracked item uses the same structure:

```json
{
  "id": "garden_20260321_abc123",
  "title": "Sungold Tomatoes",
  "domain": "garden",
  "phase": "grow",
  "status": "active",
  "priority": "high",
  "created": "2026-03-21T10:00:00Z",
  "updated": "2026-03-21T22:00:00Z",
  "target_date": "2026-07-15",
  "phase_entered": "2026-03-15T08:00:00Z",
  "metadata": {
    "variety": "Sungold",
    "location": "Greenhouse bed 1",
    "quantity": 4
  },
  "history": [],
  "reminders": [],
  "tags": ["tomato", "greenhouse"]
}
```

## Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `orch add` | Create new item | `orch add garden "Tomatoes" --priority high` |
| `orch list` | List all active | `orch list` |
| `orch today` | Today's priorities | `orch today` |
| `orch week` | This week | `orch week` |
| `orch overdue` | Past target date | `orch overdue` |
| `orch phase <id> <phase>` | Transition phase | `orch phase garden_123 grow` |
| `orch complete <id>` | Mark done | `orch complete garden_123` |
| `orch report [type]` | Generate report | `orch report weekly` |

## Views

```mermaid
graph TB
    subgraph "Standard Views"
        TODAY[📅 Today<br/>Morning review]
        WEEK[📋 This Week<br/>Weekly planning]
        PHASE[🔄 By Phase<br/>Phase-based work]
        DOMAIN[🏷️ By Domain<br/>Domain focus]
        OVERDUE[⚠️ Overdue<br/>Problem solving]
    end
    
    QUERY[Query Engine] --> TODAY
    QUERY --> WEEK
    QUERY --> PHASE
    QUERY --> DOMAIN
    QUERY --> OVERDUE
```

## Reminder Escalation

```mermaid
flowchart TD
    CHECK[Daily Check 08:00] --> PHASE{Current Phase?}
    
    PHASE -->|plant| PLANT[Weekly reminder]
    PHASE -->|grow| GROW[Daily reminder]
    PHASE -->|harvest| HARVEST[Daily + escalating]
    PHASE -->|rest| REST[Monthly check-in]
    
    PLANT --> NEAR{Target < 7 days?}
    NEAR -->|Yes| ESCALATE1[Escalate to daily]
    NEAR -->|No| SEND1[Send weekly]
    
    GROW --> NEAR2{Target < 3 days?}
    NEAR2 -->|Yes| ESCALATE2[Escalate to 2x daily]
    NEAR2 -->|No| SEND2[Send daily]
    
    HARVEST --> TODAY{Target = today?}
    TODAY -->|Yes| HOURLY[Hourly reminders]
    TODAY -->|No| SEND3[Send daily]
    
    ESCALATE1 --> TELEGRAM[📱 Telegram]
    SEND1 --> TELEGRAM
    ESCALATE2 --> TELEGRAM
    SEND2 --> TELEGRAM
    HOURLY --> TELEGRAM
    SEND3 --> TELEGRAM
    REST --> TELEGRAM
```

## Integration Flow

```mermaid
sequenceDiagram
    participant User
    participant Orchestrator
    participant Reminder
    participant Telegram
    participant Memory
    
    User->>Orchestrator: orch add garden "Tomatoes"
    Orchestrator->>Memory: Save decision
    Orchestrator->>Reminder: Schedule reminders
    Reminder->>Telegram: Send confirmation
    
    Note over Orchestrator: Time passes...
    
    loop Daily
        Reminder->>Telegram: Send reminder
        Telegram->>User: Notification
        User->>Orchestrator: orch phase garden_123 grow
        Orchestrator->>Memory: Log transition
    end
    
    User->>Orchestrator: orch complete garden_123
    Orchestrator->>Memory: Save completion
    Orchestrator->>Reminder: Cancel future reminders
```

## Cron Jobs

```bash
# Daily reminder check
0 8 * * * ~/.config/opencode/skills/orchestrator/scripts/check-reminders.sh

# Send notifications
5 8 * * * ~/.config/opencode/skills/orchestrator/scripts/send-notifications.sh

# Daily report
0 21 * * * ~/.config/opencode/skills/orchestrator/scripts/report.sh daily

# Weekly report (Mondays)
0 9 * * 1 ~/.config/opencode/skills/orchestrator/scripts/report.sh weekly
```

## Example Workflow

```mermaid
journey
    title Growing Tomatoes
    section Plant
      Add item: 5: User
      Set target: 3: User
      Schedule reminder: 5: System
    section Grow
      Daily check: 3: User
      Phase update: 4: User
      Progress log: 5: System
    section Harvest
      Pick tomatoes: 5: User
      Mark complete: 5: User
      Celebration: 5: System
    section Rest
      Review season: 3: User
      Plan next year: 4: User
```

## PostgreSQL Schema

```sql
CREATE TABLE orchestrator_items (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    domain TEXT NOT NULL,
    phase TEXT NOT NULL,
    status TEXT DEFAULT 'active',
    priority TEXT DEFAULT 'medium',
    created TIMESTAMPTZ DEFAULT NOW(),
    updated TIMESTAMPTZ DEFAULT NOW(),
    target_date DATE,
    phase_entered TIMESTAMPTZ,
    metadata JSONB DEFAULT '{}',
    history JSONB DEFAULT '[]',
    reminders JSONB DEFAULT '[]',
    tags TEXT[] DEFAULT '{}'
);

CREATE INDEX idx_orchestrator_domain ON orchestrator_items(domain);
CREATE INDEX idx_orchestrator_phase ON orchestrator_items(phase);
CREATE INDEX idx_orchestrator_status ON orchestrator_items(status);
CREATE INDEX idx_orchestrator_target ON orchestrator_items(target_date);
```

## Related Skills

| Skill | Relationship |
|-------|--------------|
| **reminder** | Notification delivery |
| **telegram** | Message channel |
| **cron** | Scheduling |
| **tracking** | Progress logging |
| **lifeplan** | Import goals as items |

## Next Post

In the next deep dive, we'll explore the **Meta-Skills** — how Skill Factory and Menu Factory enable the system to evolve and improve itself.

---

*This is part 3 of 5 in the Personal Assistant Ecosystem series.*