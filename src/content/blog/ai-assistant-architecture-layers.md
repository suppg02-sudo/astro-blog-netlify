---
pubDatetime: 2026-03-06T22:15:00Z
title: "AI Assistant Architecture: The 12-Layer Stack"
postSlug: "ai-assistant-architecture-layers"
description: "AI Assistant Architecture: The 12-Layer Stack"
tags:
  - opencode
  - architecture
  - ai
  - roadmap
---

## Overview

This diagram shows the complete architecture of my AI assistant stack, organized into 12 distinct layers. Each layer builds upon the previous one, creating a comprehensive system for AI-assisted development, automation, and knowledge management.

## Quick Reference: Layer Stack

{{< mermaid >}}
graph TD
    L0[🎯 User Interface]
    L1[🧠 Orchestration]
    L2[⚙️ Core Foundation]
    L3[🤖 AI/ML]
    L4[💾 Memory & Knowledge]
    L5[🔍 RAG]
    L6[🗄️ Data]
    L7[🐳 Infrastructure]
    L8[⏰ Automation]
    L9[📦 Services]
    L10[📊 Observability]
    L11[🛡️ TELOS Compliance]

    L0 --> L1 --> L2 --> L3 --> L4 --> L5
    L5 --> L6 --> L7
    L7 --> L8 --> L9
    L10 -.-> L7
    L11 -.-> L2

    classDef complete fill:#10b981,stroke:#047857,color:#fff,stroke-width:2px
    classDef progress fill:#f59e0b,stroke:#d97706,color:#fff,stroke-width:2px
    classDef pending fill:#6b7280,stroke:#4b5563,color:#fff,stroke-width:2px

    class L0,L1,L2,L4,L7,L9 complete
    class L3,L10 progress
    class L5,L6,L8,L11 pending
{{< /mermaid >}}

**Legend**: 🟢 Complete | 🟡 In Progress | ⚪ Pending

## Detailed Architecture Diagram

{{< mermaid >}}
graph TB
    subgraph L0["🎯 User Interface Layer"]
        U1[💬 Chat Interface]
        U2[📊 Homepage Dashboard]
        U3[📝 Blog & Documentation]
        U4[🔍 NextExplorer Files]
    end

    subgraph L1["🧠 Orchestration Layer"]
        O1[Sisyphus Main Agent]
        O2[Explore Agent]
        O3[Oracle Agent]
        O4[Librarian Agent]
        O5[Metis & Momus]
    end

    subgraph L2["⚙️ Core Foundation Layer"]
        C1[OpenCode Engine]
        C2[AGENTS.md Rules]
        C3[oh-my-opencode Plugin]
        C4[Trigger Words System]
    end

    subgraph L3["🤖 AI/ML Layer"]
        A1[LiteLLM Gateway]
        A2[z.ai GLM-5]
        A3[OpenAI API]
        A4[Model Routing]
    end

    subgraph L4["💾 Memory & Knowledge Layer"]
        M1[OpenMemory MCP]
        M2[SQLite + HSG]
        M3[Context Registry]
        M4[Skill Discovery]
    end

    subgraph L5["🔍 RAG Layer"]
        R1[Document Ingestion]
        R2[pgvector Embeddings]
        R3[Retrieval Pipeline]
        R4[Classification]
    end

    subgraph L6["🗄️ Data Layer"]
        D1[Supabase PostgreSQL]
        D2[Redis Cache]
        D3[Vector Storage]
        D4[Backup System]
    end

    subgraph L7["🐳 Infrastructure Layer"]
        I1[Docker Containers]
        I2[Portainer]
        I3[Nginx Proxy]
        I4[Tailscale VPN]
    end

    subgraph L8["⏰ Automation Layer"]
        T1[Cron Jobs]
        T2[Kestra Workflows]
        T3[Daily Research]
        T4[Monitoring Tasks]
    end

    subgraph L9["📦 Services Layer"]
        S1[Hugo Blog]
        S2[Memos Notes]
        S3[FileBrowser]
        S4[Directus CMS]
    end

    subgraph L10["📊 Observability Layer"]
        V1[OpenTelemetry]
        V2[Prometheus]
        V3[Grafana]
        V4[Jaeger Tracing]
    end

    subgraph L11["🛡️ TELOS Layer"]
        E1[Data Sovereignty]
        E2[Open Source]
        E3[Local-First AI]
        E4[Deterministic Workflows]

    end

    %% User flows down through layers
    L0 --> L1
    L1 --> L2
    L2 --> L3
    L3 --> L4
    L4 --> L5
    L5 --> L6
    L6 --> L7

    %% Cross-layer connections
    L1 -.-> L4
    L1 -.-> L8
    L3 -.-> L5
    L4 -.-> L6
    L7 -.-> L9
    L8 -.-> L9
    L10 -.-> L7
    L11 -.-> L2

    %% Styles
    classDef userLayer fill:#e1f5ff,stroke:#01579b,stroke-width:3px
    classDef coreLayer fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef aiLayer fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef dataLayer fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px
    classDef infraLayer fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    classDef telosLayer fill:#fff9c4,stroke:#f57f17,stroke-width:3px

    class L0 userLayer
    class L1,L2 coreLayer
    class L3,L4,L5 aiLayer
    class L6,L7,L9 dataLayer
    class L8,L10 infraLayer
    class L11 telosLayer

{{< /mermaid >}}

## Layer Descriptions

### Layer 0: User Interface
**Status: ✅ Complete**

Entry points for all user interactions. The chat interface connects to the orchestration layer, while dashboards provide system visibility.

### Layer 1: Orchestration
**Status: ✅ Complete**

The intelligent routing layer. Sisyphus (main agent) delegates to specialized agents:
- **Explore**: Codebase pattern discovery
- **Oracle**: Architecture decisions
- **Librarian**: External documentation
- **Metis**: Pre-planning analysis
- **Momus**: Quality assurance

### Layer 2: Core Foundation
**Status: ✅ Complete**

OpenCode engine with AGENTS.md rules defining all behaviors, triggers, and protocols. The oh-my-opencode plugin adds advanced features.

### Layer 3: AI/ML Layer
**Status: 🔄 In Progress (Phase 14)**

LiteLLM gateway provides unified access to multiple LLM providers. Currently using z.ai GLM-5 as primary model.

### Layer 4: Memory & Knowledge
**Status: ✅ Complete**

OpenMemory MCP with SQLite backend and Hierarchical Semantic Graph (HSG). Context Registry tracks all interactions and skill usage.

### Layer 5: RAG Layer
**Status: ⏳ Pending (Phase 17)**

Retrieval-Augmented Generation for document intelligence. Uses pgvector for similarity search with sophisticated chunking strategies.

### Layer 6: Data Layer
**Status: ⏳ Pending (Phase 5, 13)**

Supabase provides PostgreSQL with authentication and storage. Redis handles caching. Vector storage enables semantic search.

### Layer 7: Infrastructure Layer
**Status: ✅ Complete**

Docker-based containerization with Portainer management, Nginx reverse proxy, and Tailscale VPN for secure access.

### Layer 8: Automation Layer
**Status: ⏳ Pending (Phase 6)**

Cron jobs for scheduled tasks. Kestra provides visual workflow orchestration for complex automation pipelines.

### Layer 9: Services Layer
**Status: ✅ Complete**

Self-hosted applications: Hugo blog, Memos note-taking, FileBrowser, Directus CMS, and more.

### Layer 10: Observability Layer
**Status: 🔄 In Progress (Phase 4, 16)**

Full-stack observability with OpenTelemetry traces, Prometheus metrics, Grafana dashboards, and Jaeger distributed tracing.

### Layer 11: TELOS Layer
**Status: ⏳ Pending (Phase 18)**

Compliance with TELOS principles: data sovereignty, open-source commitment, local-first AI, and deterministic workflows.

## Progress Summary

| Layer | Status | Progress |
|-------|--------|----------|
| User Interface | ✅ Complete | 100% |
| Orchestration | ✅ Complete | 100% |
| Core Foundation | ✅ Complete | 100% |
| AI/ML | 🔄 In Progress | 25% |
| Memory & Knowledge | ✅ Complete | 100% |
| RAG | ⏳ Pending | 0% |
| Data | ⏳ Pending | 0% |
| Infrastructure | ✅ Complete | 100% |
| Automation | ⏳ Pending | 0% |
| Services | ✅ Complete | 100% |
| Observability | 🔄 In Progress | 33% |
| TELOS Compliance | ⏳ Pending | 0% |

**Overall Progress: 32%**

## Key Insights

1. **Layered Architecture**: Each layer builds on the previous, allowing incremental deployment
2. **Cross-Layer Communication**: Dashed lines show dependencies between non-adjacent layers
3. **TELOS Foundation**: All layers must eventually comply with TELOS principles
4. **Observability Throughout**: Layer 10 monitors all other layers
5. **Flexibility**: Can swap components within layers without affecting others

## Next Steps

Current priorities from the roadmap:
1. Complete AI/ML Layer with LiteLLM gateway (Phase 14)
2. Finish Observability Layer with Grafana dashboards (Phase 16)
3. Deploy Data Layer with Supabase and Redis (Phase 13)
4. Implement Automation Layer with Kestra workflows (Phase 6)

---

**Related Posts:**
- [Server Setup Roadmap](/posts/server-setup-roadmap/)
- [OpenMemory Integration](/posts/openmemory-integration/)
- [TELOS Principles](/posts/telos-principles/)