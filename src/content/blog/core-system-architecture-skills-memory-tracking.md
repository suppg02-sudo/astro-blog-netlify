---
pubDatetime: 2026-03-08T17:28:28Z
title: "Core System Architecture: Skills, Memory & Tracking"
postSlug: "core-system-architecture-skills-memory-tracking"
description: "Core System Architecture: Skills, Memory & Tracking"
tags:
  - skills
  - opencode
  - architecture
  - memory
  - tracking
---

This diagram represents the core components of the OpenCode system architecture, showing how skills, memory, automation, and tracking layers interact to create a cohesive AI-powered development environment.

## System Architecture Overview

{{< mermaid >}}
graph TB
    subgraph "Core System Components"
        subgraph "Skills Layer"
            SKILLS[Skills System]
            FLOW[Flow Skill]
            SKILL_FACTORY[Skill Factory]
            SKILL_DISCOVERY[Skill Discovery]
            OTHER_SKILLS[60+ Other Skills]
        end
        
        subgraph "Interaction Layer"
            Q_TOOL[Q Tool<br/>Question System]
            MENU_LEARNING[Menu Learning]
            TRIGGERS[Trigger Words]
        end
        
        subgraph "Memory Layer"
            SUPERMEMORY[Supermemory<br/>Persistent Storage]
            CONTEXT_REGISTRY[Context Registry]
            QUESTIONS_HISTORY[Questions History]
            DEFERRED[Deferred Flows]
        end
        
        subgraph "Automation Layer"
            CRON[Cron Jobs]
            HEARTBEAT[Heartbeat Service]
            DAILY_RESEARCH[Daily Research]
            ROUNDUP[Session Roundup]
        end
        
        subgraph "Tracking Layer"
            TRACKING[Tracking System<br/>Flow Model]
            SESSIONS[Session State]
            ACTIONS[Action Log]
            DELEGATIONS[Delegation Tracking]
        end
    end
    
    SKILLS --> FLOW
    SKILLS --> SKILL_FACTORY
    SKILLS --> SKILL_DISCOVERY
    SKILLS --> OTHER_SKILLS
    
    Q_TOOL --> MENU_LEARNING
    Q_TOOL --> TRIGGERS
    Q_TOOL --> SUPERMEMORY
    Q_TOOL --> QUESTIONS_HISTORY
    
    SUPERMEMORY --> CONTEXT_REGISTRY
    SUPERMEMORY --> QUESTIONS_HISTORY
    SUPERMEMORY --> DEFERRED
    
    CRON --> HEARTBEAT
    CRON --> DAILY_RESEARCH
    CRON --> ROUNDUP
    HEARTBEAT --> TRACKING
    
    TRACKING --> SESSIONS
    TRACKING --> ACTIONS
    TRACKING --> DELEGATIONS
    
    Q_TOOL -.->|Records Choices| MENU_LEARNING
    MENU_LEARNING -.->|Improves| Q_TOOL
    
    TRACKING -.->|Persists| SUPERMEMORY
    CRON -.->|Triggers| SKILLS
    
    SKILL_DISCOVERY -.->|Analyzes| SKILLS
    SKILL_FACTORY -.->|Creates| SKILLS
    
    FLOW -.->|Orchestrates| TRACKING
    FLOW -.->|Uses| Q_TOOL
    
    DEFERRED -.->|Resumes| Q_TOOL
    
    style SKILLS fill:#4A90E2
    style Q_TOOL fill:#7B68EE
    style SUPERMEMORY fill:#50C878
    style CRON fill:#FF6B6B
    style TRACKING fill:#FFD93D
{{< /mermaid >}}

## Component Layers

### Skills Layer

The modular capabilities system with **60+ specialized skills**:

- **Skills System**: Central registry for all available skills
- **Flow Skill**: Orchestrates complex workflows and manages task sequences
- **Skill Factory**: Meta-skill for creating and evolving new skills
- **Skill Discovery**: Analyzes skill structure, maturity levels (L0-L5), and progressive disclosure
- **60+ Other Skills**: Specialized capabilities for documentation, research, automation, and more

### Interaction Layer

User-facing interaction components:

- **Q Tool**: Intelligent questioning system with 5 modes (Explore, Build, Debug, Learn, Plan) and 4 intensity levels
- **Menu Learning**: Adaptive system that learns from user selections to improve future menu options
- **Trigger Words**: Single-word triggers that activate skills and workflows instantly

### Memory Layer

Persistent storage and context management:

- **Supermemory**: Long-term persistent storage for memories across sessions
- **Context Registry**: Tracks question tool interactions and skill usage history
- **Questions History**: Records all Q&A interactions with session state
- **Deferred Flows**: Stores unfinished tasks for later resumption

### Automation Layer

Scheduled tasks and monitoring:

- **Cron Jobs**: Time-based automation for recurring tasks
- **Heartbeat Service**: Monitors system health and triggers maintenance
- **Daily Research**: Automated AI ecosystem research (runs daily at 8:00 AM UTC)
- **Session Roundup**: End-of-session review and cleanup

### Tracking Layer

State and flow management:

- **Tracking System**: Flow model for tracking context, actions, and delegations
- **Session State**: Active session information and context
- **Action Log**: Record of all actions taken during sessions
- **Delegation Tracking**: Monitors delegated tasks to specialized agents

## Layer Interactions

The architecture follows these key interaction patterns:

1. **Skills → Memory**: Skills persist learned patterns to Supermemory
2. **Q Tool → Menu Learning**: Question choices are recorded for continual improvement
3. **Cron → Skills**: Scheduled tasks trigger skill execution
4. **Flow → Tracking**: Flow skill orchestrates and tracks complex workflows
5. **Tracking → Memory**: All tracking data is persisted for future reference
6. **Deferred → Q Tool**: Deferred flows can be resumed through the question system

## Component Summary

| Layer | Components | Purpose |
|-------|------------|---------|
| **Skills** | 60+ skills, Flow, Skill Factory, Discovery | Modular capabilities and automation |
| **Interaction** | Q Tool, Menu Learning, Triggers | User interaction and adaptive questioning |
| **Memory** | Supermemory, Context Registry, History | Persistent storage and context |
| **Automation** | Cron, Heartbeat, Daily Research | Scheduled tasks and monitoring |
| **Tracking** | Sessions, Actions, Delegations | State and flow management |

This architecture enables a deterministic, observable, and memory-augmented AI system that learns from interactions while maintaining clear separation of concerns across functional layers.