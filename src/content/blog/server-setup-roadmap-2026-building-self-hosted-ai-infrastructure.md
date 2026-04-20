---
pubDatetime: 2026-03-04T10:49:28Z
title: "Server Setup Roadmap 2026: Building a Self-Hosted AI Infrastructure"
postSlug: "server-setup-roadmap-2026-building-self-hosted-ai-infrastructure"
description: "A comprehensive 19-phase roadmap for building a production-ready, self-hosted AI infrastructure with OpenCode, Docker, monitoring, databases, and RAG capabilities."
tags:
  - server-setup
  - opencode
  - self-hosted
  - rag
  - opentelemetry
  - ai-infrastructure
  - docker
  - roadmap
---

## Overview

Building a self-hosted AI infrastructure from scratch is no small feat. This roadmap documents a systematic 19-phase journey to create a production-ready, observable, and extensible AI development environment. With 32% completion and three major phases finished, we're establishing a solid foundation for advanced AI capabilities.

## Progress at a Glance

{{< mermaid >}}
graph LR
    A[Roadmap Progress] --> B[32% Complete]
    B --> C[3/19 Phases Done]
    B --> D[1 Phase In Progress]
    B --> E[15 Phases Pending]
    
    style A fill:#4A90E2,stroke:#2E5C8A,stroke-width:3px,color:#fff
    style B fill:#7ED321,stroke:#5FA319,stroke-width:2px,color:#fff
    style C fill:#7ED321,stroke:#5FA319,stroke-width:2px,color:#fff
    style D fill:#F5A623,stroke:#D68910,stroke-width:2px,color:#fff
    style E fill:#D8D8D8,stroke:#9B9B9B,stroke-width:2px
{{< /mermaid >}}

**Status Summary:**
- ✅ **3 Phases Completed** (16%)
- ⏳ **1 Phase In Progress** (5%)
- 📋 **15 Phases Pending** (79%)

## Completed Phases

### Phase 1: OpenCode & Foundation ✅

**Completion Date:** 2026-02-22  
**Duration:** 2 days

The foundation layer establishes the core AI assistant environment:

**Completed Tasks:**
- ✅ Install OpenCode CLI
- ✅ Configure AGENTS.md global rules
- ✅ Setup oh-my-opencode plugin
- ✅ Configure 74+ specialized skills

**Key Achievements:**
- Established persistent memory system (OpenMemory MCP)
- Integrated Context7 for documentation retrieval
- Configured trigger-based workflow automation
- Created custom skill ecosystem

**Technical Highlights:**
- **Memory System**: SQLite-backed HSG (Hierarchical Semantic Graph) with 1,083 memories stored
- **Skills Architecture**: Progressive disclosure system with maturity levels (L1-L5)
- **Agent Orchestration**: Multi-agent system with specialized consultants (oracle, metis, momus)

---

### Phase 2: Docker Containers Setup ✅

**Completion Date:** 2026-02-27  
**Duration:** 3 days

Containerization layer provides isolated, reproducible service deployments:

**Completed Tasks:**
- ✅ Install Portainer (container management)
- ✅ Setup Homepage dashboard (port 8765)
- ✅ Configure Nginx Proxy Manager
- ✅ Deploy Memos (notes service, port 5230)
- ✅ Deploy NextExplorer (file explorer, port 8080)
- ✅ Deploy Astro (backup blog, port 4321)
- ✅ Deploy Hugo (primary blog, port 1314)
- ✅ Deploy FileBrowser (file management, port 8082)

**Architecture:**
{{< mermaid >}}
graph TB
    subgraph "Container Layer"
        P[Portainer<br/>Management UI]
        H[Homepage<br/>Dashboard]
        N[Nginx Proxy<br/>Manager]
        M[Memos<br/>Notes]
        NE[NextExplorer<br/>Files]
        A[Astro<br/>Backup Blog]
        H2[Hugo<br/>Primary Blog]
        FB[FileBrowser<br/>Storage]
    end
    
    subgraph "Network"
        D[Docker Network]
    end
    
    P --> D
    H --> D
    N --> D
    M --> D
    NE --> D
    A --> D
    H2 --> D
    FB --> D
    
    style P fill:#9B59B6,stroke:#7D3C98,stroke-width:2px,color:#fff
    style H fill:#3498DB,stroke:#2980B9,stroke-width:2px,color:#fff
    style N fill:#E67E22,stroke:#D35400,stroke-width:2px,color:#fff
    style M fill:#1ABC9C,stroke:#16A085,stroke-width:2px,color:#fff
    style NE fill:#E74C3C,stroke:#C0392B,stroke-width:2px,color:#fff
    style A fill:#F39C12,stroke:#E67E22,stroke-width:2px,color:#fff
    style H2 fill:#2ECC71,stroke:#27AE60,stroke-width:2px,color:#fff
    style FB fill:#95A5A6,stroke:#7F8C8D,stroke-width:2px,color:#fff
{{< /mermaid >}}

**Key Achievements:**
- Centralized service management via Portainer
- Single dashboard for all services (Homepage)
- Reverse proxy with SSL termination
- Persistent file access across services
- Dual blog system (primary + backup)

---

### Phase 3: OpenMemory Integration ✅

**Completion Date:** 2026-02-28  
**Duration:** 2 days

Memory persistence layer enables context retention across sessions:

**Completed Tasks:**
- ✅ Install OpenMemory MCP server
- ✅ Configure memory decay system
- ✅ Test memory persistence

**Technical Details:**

**Storage Architecture:**
- **Database**: SQLite with HSG indexing
- **Location**: `/data/openmemory.sqlite`
- **Port**: 8081 (external) → 8080 (internal)
- **Protocol**: MCP 2024-11-05

**Memory Decay Sectors:**
| Sector | Decay λ | Use Case | Retention |
|--------|---------|----------|-----------|
| **Semantic** | 0.005 | Facts, knowledge | Long-term |
| **Procedural** | 0.008 | Processes, configs | Medium-term |
| **Episodic** | 0.015 | Events, sessions | Short-term |
| **Emotional** | 0.020 | Preferences | Dynamic |
| **Reflective** | 0.001 | Meta-knowledge | Permanent |

**Current Metrics:**
- **Total Memories**: 1,083 entries
- **Context Types**: 8 (conversation, roadmap, decision, menu_choice, flow, workflow, skill, initiative)
- **CRUD Pattern**: Content (searchable) + Metadata (exact JSON preservation)

---

## Current Phase: Telemetry & Monitoring ⏳

**Status:** In Progress (33% complete)  
**Estimated Duration:** 2 days  
**Started:** 2026-03-01

**Tasks:**
- ✅ Setup OpenTelemetry collector
- ⏳ Configure centralized logging
- ⏳ Add health checks for all services

**Goal:** Establish comprehensive observability stack for monitoring service health, performance metrics, and distributed tracing.

---

## Future Phases

### Phase 5: Database Setup

**Duration:** 2 days

Deploy production-grade database infrastructure:
- PostgreSQL with pgvector extension
- Redis for caching and queuing
- Automated backup procedures

### Phase 6: Personal Cron Job Automation

**Duration:** 2 days

Automate routine tasks with 12 scheduled jobs:
- Daily AI research at 8 AM
- Daily news briefing at 9 AM
- Roadmap progress reminders
- Weekly ecosystem research
- Monthly agent tools landscape
- Cron failure notifications

### Phase 10: Job Dashboard & Monitoring UI

**Duration:** 3 days

Build comprehensive job monitoring interface:
- Jobs overview (running, failed, completed)
- Cron execution history
- Content aggregation tracking
- Performance trends visualization
- Integration with Homepage dashboard

### Phase 13-16: App Stack Installation

**Duration:** 10 days total

Deploy full-stack application infrastructure:

**Phase 13 - Infrastructure:**
- Supabase (PostgreSQL + Auth + Storage)
- pgvector extension
- pgBouncer connection pooling
- RabbitMQ message queue

**Phase 14 - AI/ML Layer:**
- LiteLLM unified gateway
- Model routing and provider configuration
- Request logging to database

**Phase 15 - Orchestration:**
- Kestra workflow engine
- PostgreSQL backend
- Plugin ecosystem (OpenAI, PostgreSQL, Python, RabbitMQ)

**Phase 16 - Observability:**
- OpenTelemetry Collector
- Prometheus metrics
- Grafana dashboards
- Jaeger distributed tracing
- Loki log aggregation

### Phase 17: RAG & Classification Setup

**Duration:** 3 days

Implement production RAG system:
- Document schema with pgvector
- Multiple chunking strategies
- Dense, sparse, and hybrid retrieval
- Auto-classification taxonomy
- Kestra classification workflows

### Phase 18: TELOS Compliance Review

**Duration:** 2 days

Ensure adherence to TELOS principles:
- Data sovereignty audit
- Open-source license compliance
- Local-first AI migration planning
- Deterministic workflow documentation
- Observability coverage validation

---

## Architecture Vision

{{< mermaid >}}
graph TB
    subgraph "Foundation Layer"
        OC[OpenCode CLI]
        MEM[OpenMemory MCP]
        SK[Skills System]
    end
    
    subgraph "Container Layer"
        DC[Docker Containers]
        PT[Portainer]
        HP[Homepage Dashboard]
    end
    
    subgraph "Data Layer"
        PG[(PostgreSQL<br/>+ pgvector)]
        RD[(Redis Cache)]
        MQ[RabbitMQ]
    end
    
    subgraph "AI Layer"
        LLM[LiteLLM Gateway]
        RAG[RAG Pipeline]
        WF[Kestra Workflows]
    end
    
    subgraph "Observability Layer"
        OTEL[OpenTelemetry]
        PROM[Prometheus]
        GRAF[Grafana]
        JAE[Jaeger]
    end
    
    OC --> MEM
    OC --> SK
    DC --> PT
    DC --> HP
    
    PG --> RAG
    RD --> LLM
    MQ --> WF
    
    OTEL --> PROM
    PROM --> GRAF
    OTEL --> JAE
    
    style OC fill:#4A90E2,stroke:#2E5C8A,stroke-width:3px,color:#fff
    style MEM fill:#7ED321,stroke:#5FA319,stroke-width:2px,color:#fff
    style PG fill:#336791,stroke:#1D4E6B,stroke-width:2px,color:#fff
    style LLM fill:#9B59B6,stroke:#7D3C98,stroke-width:2px,color:#fff
    style GRAF fill:#F46800,stroke:#C85A10,stroke-width:2px,color:#fff
{{< /mermaid >}}

---

## Key Technologies

### Core Infrastructure
- **OpenCode**: AI-powered development assistant
- **Docker**: Container orchestration
- **Tailscale**: VPN networking (ubuntu4.tail75e52.ts.net)

### Data & Storage
- **OpenMemory**: Persistent context storage (SQLite + HSG)
- **PostgreSQL**: Primary database with vector support
- **Redis**: Caching and session storage

### AI & ML
- **LiteLLM**: Unified LLM gateway
- **Context7**: Documentation retrieval
- **pgvector**: Embedding storage and similarity search

### Monitoring & Observability
- **OpenTelemetry**: Distributed tracing
- **Prometheus**: Metrics collection
- **Grafana**: Visualization dashboards
- **Jaeger**: Trace analysis
- **Loki**: Log aggregation

### Automation
- **Kestra**: Workflow orchestration
- **Cron**: Scheduled tasks
- **RabbitMQ**: Message queuing

---

## Progress Metrics

{{< mermaid >}}
pie title Phase Distribution
    "Completed" : 3
    "In Progress" : 1
    "Pending" : 15
{{< /mermaid >}}

**Overall Statistics:**
- **Total Phases**: 19
- **Completed**: 3 (16%)
- **In Progress**: 1 (5%)
- **Pending**: 15 (79%)
- **Overall Progress**: 32%

**Estimated Timeline:**
- **Foundation Complete**: ✅ (6 days total)
- **Full Stack Deployment**: ~25 days remaining
- **TELOS Compliance**: +2 days
- **Total Estimated**: ~33 days from start

---

## Next Steps

### Immediate Priorities (Next 2 Weeks)

1. **Complete Phase 4**: Finish telemetry setup with centralized logging and health checks
2. **Deploy Databases**: PostgreSQL + Redis for application data layer
3. **Automate Cron Jobs**: Implement daily research and monitoring tasks
4. **Build Job Dashboard**: Create monitoring interface for scheduled tasks

### Medium-Term Goals (1-2 Months)

1. **App Stack Deployment**: Complete infrastructure, AI, orchestration, and observability layers
2. **RAG Implementation**: Production-ready retrieval-augmented generation system
3. **TELOS Compliance**: Audit and document adherence to sovereignty principles
4. **Performance Tuning**: Optimize memory usage and container resources

### Long-Term Vision (3+ Months)

1. **Local-First AI**: Migrate from external APIs to local LLM inference
2. **Advanced Analytics**: ML-powered insights from system metrics
3. **Multi-Tenant Support**: Enable multiple users/projects on shared infrastructure
4. **Disaster Recovery**: Comprehensive backup and restoration procedures

---

## Technical Challenges & Solutions

### Challenge 1: Memory Persistence
**Problem**: LLM context lost between sessions  
**Solution**: OpenMemory MCP with SQLite backend and HSG indexing  
**Result**: 1,083 memories stored with semantic search capability

### Challenge 2: Service Discovery
**Problem**: Multiple services difficult to track  
**Solution**: Homepage dashboard with centralized service links  
**Result**: Single pane of glass for 8+ services

### Challenge 3: Skill Evolution
**Problem**: Ad-hoc workflows lack reusability  
**Solution**: Knowledge crystallization pipeline (L1→L5 maturity levels)  
**Result**: 74 skills with structured metadata and automation

### Challenge 4: Observability
**Problem**: Limited visibility into service health  
**Solution**: OpenTelemetry + Prometheus + Grafana stack  
**Result**: Comprehensive monitoring with distributed tracing

---

## Lessons Learned

### What Worked Well

1. **Phased Approach**: Breaking down infrastructure into 19 discrete phases prevents overwhelm
2. **Containerization**: Docker enables reproducible, isolated deployments
3. **Memory System**: OpenMemory provides crucial context persistence
4. **Skills Architecture**: Modular skills enable progressive capability building

### What Could Improve

1. **Earlier Monitoring**: Should have established observability before Phase 4
2. **Documentation**: Real-time documentation could reduce knowledge gaps
3. **Testing**: More automated testing for service health checks
4. **Backup Strategy**: Earlier implementation of backup procedures

---

## Resources & References

### Documentation
- **OpenCode Config**: http://ubuntu4:8080/editor/opencode/AGENTS.md
- **Environment Tracking**: http://ubuntu4:8080/editor/opencode/environment.md
- **Roadmap Data**: http://ubuntu4:8080/editor/opencode/data/roadmap.json

### External Links
- **OpenCode Repository**: https://github.com/anomalyco/opencode
- **oh-my-opencode Plugin**: https://github.com/suppg02-sudo/oh-my-opencode
- **TELOS Principles**: http://ubuntu4:8080/editor/opencode/docs/instructions/telos.md

### Dashboard Access
- **Homepage**: http://ubuntu4:8765
- **Portainer**: http://ubuntu4:9443
- **NextExplorer**: http://ubuntu4:8080
- **Hugo Blog**: http://ubuntu4:1314

---

## Conclusion

The Server Setup Roadmap 2026 represents a methodical approach to building a production-ready, self-hosted AI infrastructure. With 32% completion and solid foundations in place (OpenCode, Docker containers, memory persistence), we're well-positioned to tackle the remaining 15 phases.

The next major milestone is completing the full app stack deployment (Phases 13-16), which will provide database, AI/ML, orchestration, and observability layers. Following that, RAG implementation and TELOS compliance will ensure the system meets both technical and philosophical requirements for sustainable AI infrastructure.

**Key Takeaway**: Building AI infrastructure is not just about deploying services—it's about creating an observable, maintainable, and extensible system that grows with your needs. The phased approach, combined with comprehensive documentation and persistent memory, ensures that knowledge is never lost and progress is always trackable.

---

*Last Updated: 2026-03-04*  
*Progress: 32% (3/19 phases complete)*  
*Next Milestone: Phase 4 - Telemetry & Monitoring*  
*Estimated Completion: ~33 days from project start*

---

## Related Posts

- [OpenCode Question Tool Discovery](/posts/2026-02-08-opencode-question-tool-discovery/)
- [Fixing Ask User Questions MCP Server](/posts/2026-02-20-fixing-ask-user-questions-mcp-server/)
- [TELOS Constitution and Principles](/posts/2026-02-22-telos-constitution-ai-infrastructure/)