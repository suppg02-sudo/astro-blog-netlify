---
pubDatetime: 2026-03-21T23:50:00Z
title: "Reminders & Research: Supporting Skills for the Personal Assistant"
postSlug: "reminders-and-research-supporting-skills"
description: "How time-based triggers, deep research capabilities, and execution transparency support the personal assistant ecosystem."
tags:
  - cron
  - automation
  - supporting-skills
  - telegram
  - reminders
  - research
---

## The Supporting Cast

While Memory, Orchestrator, and Meta-Skills form the core, supporting skills make everything practical. This deep dive covers Reminders, Research, and Flow Tracking.

## Reminder System

### Architecture

```mermaid
graph TB
    subgraph "Input"
        CLI[CLI: remind add]
        NAT[Natural Language]
        ORCH[Orchestrator]
    end
    
    subgraph "Processing"
        PARSER[Parse Request]
        SCHED[Schedule]
        STORE[Store in DB]
    end
    
    subgraph "Delivery"
        CRON[Cron Check]
        TELEGRAM[Telegram Bot]
        NOTIFY[Notification]
    end
    
    subgraph "Feedback"
        ACK[Acknowledge]
        SNOOZE[Snooze]
        COMPLETE[Mark Complete]
    end
    
    CLI --> PARSER
    NAT --> PARSER
    ORCH --> PARSER
    PARSER --> SCHED
    SCHED --> STORE
    STORE --> CRON
    CRON --> TELEGRAM
    TELEGRAM --> NOTIFY
    NOTIFY --> ACK
    NOTIFY --> SNOOZE
    NOTIFY --> COMPLETE
    ACK --> STORE
    SNOOZE --> SCHED
    COMPLETE --> STORE
```

### Reminder Types

| Type | Trigger | Example |
|------|---------|---------|
| **one-time** | Specific datetime | "Remind me at 3pm to call John" |
| **recurring** | Interval pattern | "Remind me daily at 9am to take vitamins" |
| **relative** | Duration from now | "Remind me in 30 minutes" |
| **conditional** | Event-based | "Remind me when I'm home" (location) |
| **escalating** | Increasing urgency | Orchestrator harvest phase |

### Natural Language Parsing

```mermaid
flowchart LR
    INPUT["Remind me tomorrow at 3pm to review PR"] --> PARSE[Parse]
    PARSE --> TIME[Time: tomorrow 15:00]
    PARSE --> ACTION[Action: review PR]
    TIME --> SCHEDULE[Schedule]
    ACTION --> SCHEDULE
    SCHEDULE --> CONFIRM["✅ Reminder set for tomorrow at 3:00 PM"]
```

### Cron Integration

```bash
# Check for due reminders (every minute)
* * * * * ~/.config/opencode/skills/reminder/scripts/check-due.sh

# Send Telegram notifications
* * * * * ~/.config/opencode/skills/reminder/scripts/send-telegram.sh

# Daily summary at 8am
0 8 * * * ~/.config/opencode/skills/reminder/scripts/daily-summary.sh
```

### Telegram Bot Commands

| Command | Action |
|---------|--------|
| `/remind <text>` | Create reminder |
| `/list` | List pending reminders |
| `/done <id>` | Mark complete |
| `/snooze <id> <duration>` | Snooze reminder |
| `/cancel <id>` | Cancel reminder |

## Research System

### Architecture

```mermaid
graph TB
    subgraph "Input"
        TOPIC[Research Topic]
        DEPTH[Depth Level]
        SCOPE[Scope: web/local]
    end
    
    subgraph "Sources"
        WEB[Web Search]
        DOCS[Local Documents]
        MEMORY[Memory System]
        RAG[OpenRAG]
    end
    
    subgraph "Processing"
        GATHER[Gather Sources]
        ANALYZE[Analyze Content]
        SYNTHESIZE[Synthesize Findings]
        CITE[Generate Citations]
    end
    
    subgraph "Output"
        SUMMARY[Summary]
        FULL[Full Report]
        BLOG[Blog Post]
    end
    
    TOPIC --> GATHER
    DEPTH --> ANALYZE
    SCOPE --> GATHER
    
    WEB --> GATHER
    DOCS --> GATHER
    MEMORY --> GATHER
    RAG --> GATHER
    
    GATHER --> ANALYZE
    ANALYZE --> SYNTHESIZE
    SYNTHESIZE --> CITE
    
    CITE --> SUMMARY
    CITE --> FULL
    CITE --> BLOG
```

### Research Depths

| Level | Name | Actions | Time |
|-------|------|---------|------|
| **quick** | Quick Overview | 3-5 sources, summary | 2-5 min |
| **standard** | Standard Research | 10-15 sources, analysis | 15-30 min |
| **deep** | Deep Dive | 30+ sources, synthesis | 1-2 hours |
| **comprehensive** | Comprehensive | Exhaustive, citations | 3+ hours |

### Evidence-Based Methodology

```mermaid
flowchart TD
    TOPIC[Research Topic] --> SEARCH[Search Multiple Sources]
    SEARCH --> FILTER[Filter Relevance]
    FILTER --> EXTRACT[Extract Key Points]
    EXTRACT --> CROSS[Cross-Reference]
    CROSS --> VERIFY{Verified?}
    VERIFY -->|Yes| INCLUDE[Include in Report]
    VERIFY -->|No| FLAG[Flag as Unverified]
    INCLUDE --> SYNTHESIZE[Synthesize Findings]
    FLAG --> SYNTHESIZE
    SYNTHESIZE --> CITE[Add Citations]
    CITE --> OUTPUT[Research Output]
```

### Integration with OpenRAG

```bash
# Research with document retrieval
research "crustal displacement theories" --use-rag

# Research with memory context
research "personal assistant architecture" --use-memory

# Research web + local
research "best practices for AI memory" --scope all
```

## Flow Tracking

### Purpose

Execution transparency — understand how tasks flow through the system.

### Architecture

```mermaid
graph LR
    subgraph "Capture"
        ACTION[Action Taken]
        SKILL[Skill Invoked]
        AGENT[Agent Used]
    end
    
    subgraph "Store"
        FLOW_DB[(Flow Database)]
        CONTEXT[Context Stack]
    end
    
    subgraph "Analyze"
        TRACE[Trace Execution]
        OPTIMIZE[Optimize Flow]
        REPORT[Flow Report]
    end
    
    ACTION --> FLOW_DB
    SKILL --> FLOW_DB
    AGENT --> FLOW_DB
    FLOW_DB --> CONTEXT
    CONTEXT --> TRACE
    TRACE --> OPTIMIZE
    OPTIMIZE --> REPORT
```

### Flow Notation

```
User Request → Agent → Global Rules → Skill → Execution
A > B > C > D > E

Example:
"Create reminder" > Sisyphus > Reminder Rules > Reminder Skill > Telegram
```

### Tracked Elements

| Element | What's Tracked |
|---------|----------------|
| **Context** | Current conversation state |
| **Flows** | Execution paths |
| **Actions** | Individual operations |
| **Delegations** | Agent handoffs |
| **Skills** | Skill invocations |
| **Questions** | Question tool usage |

### Flow Analysis

```mermaid
sequenceDiagram
    participant User
    participant Agent
    participant Flow
    participant Skill
    
    User->>Agent: Create reminder
    Agent->>Flow: Log start
    Agent->>Skill: Invoke reminder
    Skill->>Flow: Log skill call
    Skill->>User: Create reminder
    User->>Skill: Confirm
    Skill->>Flow: Log completion
    Flow->>Flow: Analyze path
    Flow->>Agent: Flow report
```

## Integration Map

```mermaid
graph TB
    subgraph "Core"
        MEM[Memory System]
        ORCH[Orchestrator]
    end
    
    subgraph "Meta"
        SF[Skill Factory]
        MF[Menu Factory]
    end
    
    subgraph "Support"
        REM[Reminders]
        RES[Research]
        FLOW[Flow Tracking]
    end
    
    subgraph "Channels"
        TEL[Telegram]
        CRON[Cron]
        RAG[OpenRAG]
    end
    
    ORCH --> REM
    REM --> TEL
    REM --> CRON
    
    RES --> MEM
    RES --> RAG
    
    FLOW --> MEM
    
    SF --> FLOW
    MF --> FLOW
    
    MEM --> RES
    MEM --> ORCH
```

## Complete Ecosystem View

```mermaid
graph TB
    subgraph "User Interface"
        CLI[CLI Triggers]
        TEL_UI[Telegram Bot]
        WEB[Web Dashboard]
    end
    
    subgraph "Intelligence Layer"
        ORCH[Orchestrator]
        RES[Research]
        FLOW[Flow Tracking]
    end
    
    subgraph "Meta Layer"
        SF[Skill Factory]
        MF[Menu Factory]
        ML[Menu Learning]
    end
    
    subgraph "Memory Layer"
        PG[(PostgreSQL)]
        VEC[pgvector]
        STATE[State Tracking]
    end
    
    subgraph "Integration Layer"
        CRON[Cron Jobs]
        TEL[Telegram API]
        RAG[OpenRAG]
    end
    
    subgraph "Skills Library"
        SKILLS[74 Skills]
    end
    
    CLI --> ORCH
    TEL_UI --> ORCH
    WEB --> ORCH
    
    ORCH --> SF
    ORCH --> RES
    ORCH --> FLOW
    
    SF --> SKILLS
    MF --> SKILLS
    ML --> MF
    
    ORCH --> PG
    RES --> PG
    FLOW --> PG
    PG --> VEC
    STATE --> PG
    
    ORCH --> CRON
    ORCH --> TEL
    RES --> RAG
```

## Key Metrics Summary

| Component | Metric | Value |
|-----------|--------|-------|
| **Memory** | Total memories | 2,846+ |
| **Skills** | Total skills | 74 |
| **Skills** | L2+ maturity | 50 (68%) |
| **Triggers** | Active triggers | 30+ |
| **Reminders** | Daily capacity | Unlimited |
| **Research** | Sources per deep dive | 30+ |

## What's Next?

The Personal Assistant Ecosystem is now complete with:
- ✅ **Memory System** — Persistent context
- ✅ **Orchestrator** — Lifecycle management
- ✅ **Meta-Skills** — Self-improvement
- ✅ **Reminders** — Time-based triggers
- ✅ **Research** — Deep analysis
- ✅ **Flow Tracking** — Execution transparency

Future enhancements:
- OpenTelemetry integration
- Voice interface
- Mobile app
- Multi-user support

---

*This is part 5 of 5 in the Personal Assistant Ecosystem series.*