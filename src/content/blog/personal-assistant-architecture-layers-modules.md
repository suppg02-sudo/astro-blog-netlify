---
pubDatetime: 2026-03-14T16:33:51Z
title: "Personal Assistant Architecture: A Layered Design with OpenCode"
postSlug: "personal-assistant-architecture-layers-modules"
description: "Personal Assistant Architecture: A Layered Design with OpenCode"
tags:
  - opencode
  - ai-agents
  - architecture
  - docker
  - personal-assistant
---

Building a personal assistant system requires careful architectural planning. This post outlines a layered design that separates concerns while enabling seamless communication between components.

## Layer Stack

{{< mermaid >}}
flowchart TB
    subgraph L7[⏰ CRONS]
        direction LR
        C1[Automation]
    end
    subgraph L6[📱 TELEGRAM]
        direction LR
        T1[Chat Interface]
    end
    subgraph L5[🎙️ LIVEKIT]
        direction LR
        V1[Voice Interface]
    end
    subgraph L4[🤖 AGENTS]
        direction LR
        A1[Intelligence]
    end
    subgraph L3[🧠 MEMORY]
        direction LR
        M1[Persistence]
    end
    subgraph L2[⚙️ OPENCODE]
        direction LR
        O1[Orchestration]
    end
    subgraph L1[🖥️ OS]
        direction LR
        S1[Foundation]
    end
    
    L7 --> L6 --> L5 --> L4 --> L3 --> L2 --> L1
    
    classDef layer1 fill:#2d3436,stroke:#636e72,color:#fff
    classDef layer2 fill:#0984e3,stroke:#74b9ff,color:#fff
    classDef layer3 fill:#6c5ce7,stroke:#a29bfe,color:#fff
    classDef layer4 fill:#00b894,stroke:#55efc4,color:#fff
    classDef layer5 fill:#e17055,stroke:#fab1a0,color:#fff
    classDef layer6 fill:#fdcb6e,stroke:#ffeaa7,color:#1a1a2e
    classDef layer7 fill:#e84393,stroke:#fd79a8,color:#fff
    
    class L1 layer1
    class L2 layer2
    class L3 layer3
    class L4 layer4
    class L5 layer5
    class L6 layer6
    class L7 layer7
{{< /mermaid >}}

## Architecture Overview

The system is built on seven distinct layers, each with a specific responsibility. From the foundation up:

{{< mermaid >}}
graph TB
    subgraph CRONS["⏰ CRONS Layer"]
        direction LR
        CR1[Daily Research<br/>8:00 UTC]
        CR2[Backup Jobs<br/>Scheduled]
        CR3[Health Checks<br/>Periodic]
        CR4[Cleanup Tasks<br/>Maintenance]
    end

    subgraph TELEGRAM["📱 TELEGRAM Layer"]
        direction LR
        TG1[Bot API<br/>Ingress/Egress]
        TG2[Commands<br/>/ask /cmd /run]
        TG3[Notifications<br/>Outbound]
        TG4[Keyboards<br/>Interactive Menus]
    end

    subgraph LIVEKIT["🎙️ LIVEKIT Layer"]
        direction LR
        LK1[Voice Rooms<br/>Real-time Audio]
        LK2[WebRTC<br/>Media Streams]
        LK3[SIP Integration<br/>Phone Bridge]
        LK4[Agents<br/>Voice Assistants]
    end

    subgraph AGENTS["🤖 AGENTS & FLOWS & SKILLS Layer"]
        direction TB
        subgraph AGS["Agents"]
            A1[Sisyphus<br/>Executor]
            A2[Prometheus<br/>Planner]
            A3[Oracle<br/>Consultant]
            A4[Explore<br/>Researcher]
            A5[Librarian<br/>Doc Search]
            A6[Hephaestus<br/>Builder]
        end
        subgraph FLS["Flows"]
            F1[YouTube<br/>→ Blog]
            F2[Research<br/>→ Summary]
            F3[News<br/>→ Digest]
        end
        subgraph SKS["Skills"]
            S1[rag]
            S2[telegram]
            S3[news]
            S4[flow]
            S5[notify]
            S6[50+ more]
        end
    end

    subgraph MEMORY["🧠 MEMORY Layer"]
        direction LR
        M1[(PostgreSQL<br/>+ pgvector<br/>2,846+ memories)]
        M2[Embeddings<br/>Jina AI]
        M3[Hybrid Search<br/>Semantic + Keyword]
        M4[Context Registry<br/>Session Tracking]
    end

    subgraph OPENCODE["⚙️ OPENCODE Layer"]
        direction LR
        OC1[Core Engine<br/>GLM-5 Model]
        OC2[MCP Servers<br/>Playwright, etc.]
        OC3[Tool System<br/>Bash, Read, Write]
        OC4[Session Manager<br/>State & History]
        OC5[Skill Loader<br/>Dynamic Loading]
    end

    subgraph OS["🖥️ OS Layer - Ubuntu + Docker"]
        direction LR
        OS1[Docker Engine<br/>Container Runtime]
        OS2[systemd<br/>Services]
        OS3[Tailscale<br/>VPN Network]
        OS4[Storage<br/>Volumes & Mounts]
        OS5[Network<br/>Ports & Proxies]
    end

    %% Layer connections (top to bottom)
    CRONS -.-> TELEGRAM
    TELEGRAM <--> LIVEKIT
    TELEGRAM --> AGENTS
    LIVEKIT --> AGENTS
    AGENTS <--> MEMORY
    AGENTS --> OPENCODE
    MEMORY --> OPENCODE
    OPENCODE --> OS

    %% Cross-layer connections
    CR1 -.-> A1
    TG1 <--> OC4
    LK4 -.-> A1
    M1 <--> OC4
    S2 <--> TG1

    %% Styling
    classDef osLayer fill:#2d3436,stroke:#636e72,color:#fff
    classDef coreLayer fill:#0984e3,stroke:#74b9ff,color:#fff
    classDef memoryLayer fill:#6c5ce7,stroke:#a29bfe,color:#fff
    classDef agentLayer fill:#00b894,stroke:#55efc4,color:#fff
    classDef commLayer fill:#e17055,stroke:#fab1a0,color:#fff
    classDef autoLayer fill:#fdcb6e,stroke:#ffeaa7,color:#1a1a2e

    class OS osLayer
    class OPENCODE coreLayer
    class MEMORY memoryLayer
    class AGENTS agentLayer
    class TELEGRAM,LIVEKIT commLayer
    class CRONS autoLayer
{{< /mermaid >}}

---

## Layer Breakdown

### 1. OS Layer (Ubuntu + Docker)

The foundation of everything. This layer provides:

| Component | Purpose |
|-----------|---------|
| **Docker Engine** | Container runtime for all services |
| **systemd** | Service management and startup orchestration |
| **Tailscale** | Secure VPN network for remote access |
| **Storage** | Persistent volumes and mount points |
| **Network** | Port bindings, reverse proxies, DNS |

**Key principle**: Keep the OS layer thin and focused on infrastructure concerns only.

---

### 2. OpenCode Layer

The orchestration engine that powers the entire system:

| Component | Purpose |
|-----------|---------|
| **Core Engine** | GLM-5 model for reasoning and execution |
| **MCP Servers** | Model Context Protocol for external integrations (Playwright for browser, etc.) |
| **Tool System** | Native tools: Bash, Read, Write, Edit, etc. |
| **Session Manager** | Maintains conversation state and history |
| **Skill Loader** | Dynamically loads specialized capabilities |

This layer is the "brain" that coordinates all other layers.

---

### 3. Memory Layer

Persistent, semantic memory using modern vector database technology:

| Component | Purpose |
|-----------|---------|
| **PostgreSQL + pgvector** | 2,846+ memories with vector embeddings |
| **Embeddings** | Jina AI for semantic representation |
| **Hybrid Search** | Combines semantic and keyword search |
| **Context Registry** | Tracks session context and decision history |

**Why PostgreSQL?** It's battle-tested, supports vector operations via pgvector, and integrates well with the rest of the stack.

---

### 4. Agents & Flows & Skills Layer

The intelligence layer with specialized capabilities:

#### Agents
| Agent | Role |
|-------|------|
| **Sisyphus** | Primary executor - handles complex tasks |
| **Prometheus** | Planner - breaks down requirements |
| **Oracle** | Consultant - architecture decisions |
| **Explore** | Researcher - codebase analysis |
| **Librarian** | Doc Search - external documentation |
| **Hephaestus** | Builder - deep implementation work |

#### Flows
Predefined workflows that chain multiple operations:
- **YouTube → Blog**: Transcribe, summarize, publish
- **Research → Summary**: Multi-source research synthesis
- **News → Digest**: Daily news aggregation

#### Skills
50+ modular capabilities including:
- `rag` - Retrieval-Augmented Generation
- `telegram` - Bot integration
- `news` - News aggregation
- `flow` - Workflow orchestration
- `notify` - Push notifications

---

### 5. Telegram Layer

The primary user interface for interaction:

| Component | Purpose |
|-----------|---------|
| **Bot API** | Message ingress and egress |
| **Commands** | `/ask`, `/cmd`, `/run`, `/status` |
| **Notifications** | Outbound alerts and digests |
| **Keyboards** | Interactive menu navigation |

This layer makes the assistant accessible from anywhere via mobile.

---

### 6. LiveKit Layer

Voice capabilities for real-time communication:

| Component | Purpose |
|-----------|---------|
| **Voice Rooms** | Real-time audio spaces |
| **WebRTC** | Media streaming protocol |
| **SIP Integration** | Phone system bridge |
| **Voice Agents** | AI-powered voice assistants |

Enables hands-free interaction and voice-first experiences.

---

### 7. Crons Layer

Automated scheduled tasks:

| Task | Schedule |
|------|----------|
| **Daily Research** | 8:00 UTC - AI ecosystem monitoring |
| **Backup Jobs** | Scheduled - data protection |
| **Health Checks** | Periodic - service monitoring |
| **Cleanup Tasks** | Maintenance - log rotation, temp files |

---

## Cross-Layer Communication

The layers aren't isolated silos—they communicate through well-defined interfaces:

```
Crons ──► Telegram ──► Agents ──► Memory
                    │
                    ▼
               LiveKit ──► Agents
                              │
                              ▼
                           OpenCode ──► OS
```

**Key integration points:**
- Crons trigger agents via internal APIs
- Telegram and LiveKit both feed into the agent system
- Memory is accessible from all layers above it
- OpenCode provides the execution environment for everything

---

## Design Principles

1. **Separation of Concerns**: Each layer has a single responsibility
2. **Loose Coupling**: Layers communicate through interfaces, not implementation details
3. **Horizontal Scalability**: Each layer can scale independently
4. **Fault Isolation**: Failure in one layer doesn't cascade to others
5. **Observability**: Clear boundaries make monitoring and debugging easier

---

## Getting Started

To implement this architecture:

1. Start with the **OS Layer** - set up Ubuntu with Docker and Tailscale
2. Install **OpenCode** and configure the core engine
3. Set up **PostgreSQL with pgvector** for memory
4. Deploy **Telegram bot** for user interaction
5. Add **LiveKit** if voice capabilities are needed
6. Configure **cron jobs** for automation
7. Build out **agents and skills** as needed

---

## Conclusion

This layered architecture provides a solid foundation for a personal assistant that's:
- **Modular**: Easy to add, remove, or upgrade components
- **Scalable**: Each layer can grow independently
- **Maintainable**: Clear boundaries simplify debugging
- **Extensible**: New capabilities slot into existing layers

The separation between OS, orchestration (OpenCode), memory, intelligence (agents), and interfaces (Telegram/LiveKit) creates a system that can evolve over time without major rewrites.

---

*What layers would you add or modify for your personal assistant? Let me know your thoughts.*