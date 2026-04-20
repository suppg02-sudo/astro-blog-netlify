---
pubDatetime: 2026-02-28T14:45:00Z
title: "OpenCode Environment Architecture"
postSlug: "opencode-environment-architecture"
description: "OpenCode Environment Architecture"
tags:
  - opencode
  - automation
  - homelab
  - architecture
---

A visual overview of the OpenCode environment on ubuntu4, showing how components connect: Homepage → Admin Buttons → OliveTin → Microservices → Blog.

## High-Level Architecture

The environment follows a **dashboard-driven automation** pattern where Homepage acts as the central control plane, triggering OliveTin actions that manage Docker containers and services.

```mermaid
flowchart TB
    subgraph USER["👤 User"]
        Browser["Browser"]
    end

    subgraph DASHBOARD["📊 Homepage Dashboard :8765"]
        Apps["Applications<br/>OpenCode, Notes, Files"]
        Content["Content<br/>Hacker News RSS"]
        Backend["Backend<br/>Portainer, n8n, CronMaster"]
        Admin["Admin Buttons<br/>⚡ One-Click Actions"]
    end

    subgraph AUTOMATION["🤖 OliveTin :1337"]
        Scripts["Shell Scripts"]
        Webhooks["Webhook Triggers"]
        Tasks["Scheduled Tasks"]
    end

    subgraph SERVICES["🐳 Docker Containers"]
        Blog["Hugo Blog :1313"]
        Astro["Astro Site :8086"]
        Research["Research Task :8898"]
        N8N["n8n Workflows :5678"]
        Portainer["Portainer :9443"]
        OpenMemory["OpenMemory :8081"]
    end

    Browser --> DASHBOARD
    Admin -->|"?action=restart-ai-stack"| Webhooks
    Admin -->|"?action=docker-cleanup"| Webhooks
    Admin -->|"?action=backup-configs"| Webhooks
    Admin -->|"?action=theme-dark-slate"| Webhooks
    
    Webhooks --> Scripts
    Scripts --> SERVICES
    Tasks --> Scripts
    
    Apps --> SERVICES
    Content --> Blog
```

## Admin Button Flow

The Admin section of Homepage contains one-click action buttons that trigger OliveTin webhooks:

```mermaid
sequenceDiagram
    participant U as User
    participant H as Homepage :8765
    participant O as OliveTin :1337
    participant S as Shell Script
    participant D as Docker

    U->>H: Click "Restart AI Stack"
    H->>O: GET /?action=restart-ai-stack
    O->>S: Execute restart-ai-stack.sh
    S->>D: docker restart container1, container2...
    D-->>S: Containers restarted
    S-->>O: Script completed
    O-->>H: Action success
    H-->>U: Button shows completion
```

## OpenCode Agent Ecosystem

The environment runs 24 agents powered by GLM-5, organized into built-in and GSD (Get Shit Done) categories:

```mermaid
mindmap
  root((OpenCode<br/>Agents))
    Built-in 10
      Sisyphus
        Complex reasoning, coding
      Librarian
        Documentation lookup
      Explore
        Codebase analysis
      Oracle
        Architecture decisions
      Metis
        Pre-planning analysis
      Momus
        Quality assurance
      Sisyphus-Junior
        Quick operations
      Frontend-UI-UX
        Visual design
      Document-Writer
        Documentation
      Multimodal-Looker
        Image/PDF analysis
    GSD Framework 14
      Planning
        gsd-planner
        gsd-roadmapper
      Execution
        gsd-executor
        gsd-debugger
      Verification
        gsd-verifier
        gsd-integration-checker
        gsd-plan-checker
      Research
        gsd-phase-researcher
        gsd-project-researcher
        gsd-research-synthesizer
        gsd-codebase-mapper
      Configuration
        gsd-settings
        gsd-set-model
        gsd-set-profile
```

## Skills Maturity Model

Skills evolve through 5 maturity levels, from raw documentation to deterministic MCP servers:

```mermaid
flowchart LR
    subgraph L1["L1: Raw"]
        S1["SKILL.md only"]
    end
    
    subgraph L2["L2: Structured"]
        S2["YAML metadata<br/>Sections<br/>Commands"]
    end
    
    subgraph L3["L3: Script-Attached"]
        S3["Shell/Python<br/>Automation"]
    end
    
    subgraph L4["L4: API-Integrated"]
        S4["REST endpoints<br/>Health checks"]
    end
    
    subgraph L5["L5: MCP/Deterministic"]
        S5["MCP Server<br/>Typed tools<br/>Deterministic"]
    end
    
    L1 -->|"Add structure"| L2
    L2 -->|"Add scripts"| L3
    L3 -->|"Add API"| L4
    L4 -->|"Add MCP"| L5
    
    style L5 fill:#10b981,color:#fff
    style L4 fill:#3b82f6,color:#fff
    style L3 fill:#f59e0b,color:#fff
```

### Current Skill Distribution

| Level | Count | Examples |
|-------|-------|----------|
| **L5** | 2 | `agent-browser`, `openmemory` |
| **L4** | 3 | `crawl4ai`, `openrag`, `portainer` |
| **L3** | 5 | `containers`, `cronflow`, `diagnose`, `news`, `skill-catalogue` |
| **L2** | 15+ | `research`, `flow`, `roadmap`, `space`, `roundup` |
| **L1** | 50+ | Most documentation skills |

## Memory & MCP Systems

```mermaid
flowchart TB
    subgraph AGENTS["AI Agents"]
        Sisyphus
        Librarian
        Oracle
    end

    subgraph MEMORY["Memory Systems"]
        Supermemory["Supermemory<br/>Persistent memories<br/>Auto-injection"]
        ContextReg["Context Registry<br/>Question tracking<br/>Skill usage"]
        OpenMem["OpenMemory :8081<br/>Semantic search<br/>Reinforcement"]
    end

    subgraph MCP["MCP Servers"]
        Playwright["Playwright<br/>Browser automation"]
        BraveSearch["Brave Search<br/>Web search"]
        Crawl4AI["Crawl4AI<br/>Web scraping"]
        Context7["Context7<br/>Documentation"]
    end

    AGENTS --> MEMORY
    AGENTS --> MCP
    
    Supermemory -->|"stores"| ContextReg
    OpenMem -->|"reinforces"| Supermemory
```

## Service Network Map

All services running on ubuntu4 with their ports:

```mermaid
graph TB
    subgraph PUBLIC["Public Facing"]
        H["Homepage<br/>:8765"]
        B["Hugo Blog<br/>:1313"]
        A["Astro Site<br/>:8086"]
    end

    subgraph APPS["Applications"]
        OC["OpenCode Web<br/>:4096"]
        N["Notes (Memos)<br/>:5230"]
        F["Files (NextExplorer)<br/>:8080"]
        RSS["FreshRSS<br/>:8282"]
    end

    subgraph AUTOMATION["Automation"]
        OT["OliveTin<br/>:1337"]
        N8N["n8n<br/>:5678"]
        CM["CronMaster<br/>:40123"]
        RT["Research Task<br/>:8898"]
    end

    subgraph INFRA["Infrastructure"]
        P["Portainer<br/>:9443"]
        FB["FileBrowser<br/>:2280"]
        DD["Dashdot<br/>:3001"]
        NP["Nginx Proxy<br/>:81"]
    end

    subgraph OBSERVABILITY["Observability"]
        PROM["Prometheus<br/>:9090"]
        GRAF["Grafana OTel<br/>:3003"]
        JAEGER["Jaeger<br/>:16686"]
        OTEL["OTel Collector<br/>:4317"]
    end

    subgraph DATA["Data"]
        OM["OpenMemory<br/>:8081"]
        MEM["Memos<br/>:5230"]
    end

    H --> OT
    H --> OC
    H --> B
    H --> A
```

## Research Skill (Recent Addition)

The **Research skill** provides enterprise-grade research methodology with evidence-based synthesis:

```mermaid
flowchart LR
    subgraph INPUT["Research Input"]
        Topic["Topic/Query"]
        Sources["Source Selection<br/>Web, Docs, GitHub, Academic"]
    end

    subgraph TOOLS["Research Tools"]
        Brave["Brave Search"]
        C7["Context7 Docs"]
        Crawl["Crawl4AI"]
        GH["GitHub Search"]
    end

    subgraph PROCESS["Synthesis"]
        Gather["Parallel Gathering"]
        Verify["Source Verification<br/>CRAAP Evaluation"]
        Conflict["Conflict Resolution"]
        Confidence["Confidence Assessment"]
    end

    subgraph OUTPUT["Output"]
        Report["Research Report"]
        Blog["Hugo Blog Post"]
        Memory["OpenMemory Storage"]
    end

    Topic --> TOOLS
    Sources --> TOOLS
    TOOLS --> Gather
    Gather --> Verify
    Verify --> Conflict
    Conflict --> Confidence
    Confidence --> Report
    Report --> Blog
    Report --> Memory
```

### Research Features

- **Multi-source gathering**: Web, docs, GitHub, academic in parallel
- **Evidence-based synthesis**: CRAAP evaluation for source credibility
- **Conflict resolution**: Priority order (official docs > code > peer-reviewed)
- **Confidence levels**: GRADE framework adapted for technical research
- **Auto-publishing**: Results automatically create Hugo blog posts

## Quick Reference

| Component | URL | Purpose |
|-----------|-----|---------|
| Homepage | http://ubuntu4:8765 | Central dashboard |
| OliveTin | http://ubuntu4:1337 | Admin task automation |
| Hugo Blog | http://ubuntu4:1313 | TELOS Blog |
| OpenCode | http://ubuntu4:4096 | AI coding interface |
| Research | http://ubuntu4:8898 | Research task web form |
| Portainer | https://ubuntu4:9443 | Docker management |

---

*Last updated: February 28, 2026*