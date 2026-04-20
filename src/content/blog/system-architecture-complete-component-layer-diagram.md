---
pubDatetime: 2026-03-07T15:05:00Z
title: "System Architecture: Complete Component Layer Diagram"
postSlug: "system-architecture-complete-component-layer-diagram"
description: "System Architecture: Complete Component Layer Diagram"
tags:
  - documentation
  - architecture
  - mermaid
  - diagram
---

> Generated: 2026-03-07
> Components: 28 containers • 88 skills • 14 agents • 20 cron jobs

---

## 🏗️ Full System Architecture (Top-Down View)

{{< mermaid >}}
graph TB
    subgraph L5["🖥️ Layer 5: Client/User"]
        WEB[Web Browsers]
        TAIL[Tailscale VPN<br/>ubuntu4.tail75e52.ts.net]
        CLI[API/CLI Clients]
        OMNIUI[Omni Search UI]
    end

    subgraph L4["🚪 Layer 4: Gateway/Proxy"]
        CADDY[Omni Caddy<br/>:8443 SSL]
        HOME[Homepage Dashboard<br/>:8765]
        NEXT[NextExplorer<br/>:8080]
        NGINX[Nginx Landing<br/>:8056]
    end

    subgraph L3["⚡ Layer 3: Application Services"]
        OMNI[Omni Search<br/>:3080]
        DIRECT[Directus CMS<br/>:8055]
        HUGO[Hugo Blog<br/>:1313]
        OLIVE[OliveTin<br/>:1337]
        FOSS[FossFlow<br/>:3090]
        OMDB[OpenMemory Dashboard<br/>:13120]
        ASTRO1[Astro Vector<br/>:8092]
        ASTRO2[Astro T-Shirt<br/>:8093]
        RESEARCH[Research Task<br/>Container]
        FLOWS[Flows App<br/>Container]
        RELAY[Relay Service<br/>Container]
    end

    subgraph L2["🤖 Layer 2: AI/Agent Ecosystem"]
        OPENCODE[OpenCode Core<br/>Sisyphus/GLM-5]
        
        subgraph MCP["MCP Servers"]
            OPENMCP[OpenMemory MCP<br/>:8081]
            BRAVE[Brave Search MCP]
            AGENT[Agent-Browser MCP]
            C7[Context7 MCP]
        end
        
        subgraph SKILLS["88 Skills"]
            SK1[openrag]
            SK2[hugo]
            SK3[directus]
            SK4[research]
            SK5[containers]
            SK6[diagnose]
            SK7[flow]
            SK8[cronflow]
        end
        
        subgraph AGENTS["14 GSD Agents"]
            AG1[gsd-executor ✓]
            AG2[13 Disabled]
        end
        
        subgraph CRON["20 Cron Jobs"]
            CR1[Hourly Monitoring]
            CR2[Daily Reports]
            CR3[Weekly Analysis]
            CR4[Overnight Indexing]
        end
    end

    subgraph L1["💾 Layer 1: Data/Infrastructure"]
        subgraph DBS["Databases"]
            PGVEC[PostgreSQL Vector<br/>:5433]
            PGLIT[PostgreSQL LiteLLM<br/>:5432]
            PGDIR[PostgreSQL Directus<br/>:5432]
            REDIS[Redis Cache<br/>:6379]
            SQLITE[SQLite<br/>OpenMemory]
        end
        
        subgraph OBS["Observability"]
            OTEL[OpenTelemetry<br/>:4317/4318]
            JAEGER[Jaeger Tracing<br/>:16686]
            PROM[Prometheus<br/>:9090]
        end
        
        subgraph TOOLS["Admin Tools"]
            PGADMIN[pgAdmin<br/>:5050]
        end
        
        subgraph STORAGE["Storage"]
            MEDIA[/media/docker/]
            CONFIG[~/.config/opencode/]
            BACKUP[/mnt/backup/]
        end
    end

    WEB --> CADDY
    WEB --> HOME
    WEB --> NEXT
    TAIL --> CADDY
    CLI --> OMNI
    OMNIUI --> CADDY
    
    CADDY --> OMNI
    HOME --> OPENCODE
    NEXT --> MEDIA
    NGINX --> ASTRO1
    
    OMNI --> OPENCODE
    DIRECT --> PGDIR
    HUGO --> MEDIA
    OLIVE --> CRON
    FOSS --> OPENCODE
    OMDB --> OPENMCP
    ASTRO1 --> MEDIA
    ASTRO2 --> MEDIA
    RESEARCH --> OPENCODE
    FLOWS --> OPENCODE
    RELAY --> OPENCODE
    
    OPENCODE --> OPENMCP
    OPENCODE --> BRAVE
    OPENCODE --> AGENT
    OPENCODE --> C7
    OPENCODE --> SKILLS
    OPENCODE --> AGENTS
    
    OPENMCP --> SQLITE
    SKILLS --> PGVEC
    SKILLS --> MEDIA
    
    CRON --> OPENCODE
    CRON --> DIRECT
    CRON --> HUGO
    
    OTEL --> JAEGER
    OTEL --> PROM
    PGADMIN --> PGVEC
    PGADMIN --> PGLIT
    PGADMIN --> PGDIR
    
    classDef layer5 fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    classDef layer4 fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef layer3 fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef layer2 fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px
    classDef layer1 fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    classDef storage fill:#fff9c4,stroke:#f57f17,stroke-width:2px
    
    class WEB,TAIL,CLI,OMNIUI layer5
    class CADDY,HOME,NEXT,NGINX layer4
    class OMNI,DIRECT,HUGO,OLIVE,FOSS,OMDB,ASTRO1,ASTRO2,RESEARCH,FLOWS,RELAY layer3
    class OPENCODE,OPENMCP,BRAVE,AGENT,C7,SK1,SK2,SK3,SK4,SK5,SK6,SK7,SK8,AG1,AG2,CR1,CR2,CR3,CR4 layer2
    class PGVEC,PGLIT,PGDIR,REDIS,SQLITE,OTEL,JAEGER,PROM,PGADMIN layer1
    class MEDIA,CONFIG,BACKUP storage
{{< /mermaid >}}

---

## 📊 Layer-by-Layer Breakdown

### Layer 5: Client/User Access

{{< mermaid >}}
graph LR
    subgraph Clients["Client Access Points"]
        BROWSER[🌐 Web Browsers<br/>http://ubuntu4:PORT]
        VPN[🔐 Tailscale VPN<br/>ubuntu4.tail75e52.ts.net]
        API[📡 REST APIs<br/>Programmatic Access]
        SEARCH[🔍 Omni UI<br/>Unified Search]
    end
    
    BROWSER --> |"HTTPS/Web"| GATEWAY
    VPN --> |"Secure Tunnel"| GATEWAY
    API --> |"REST/JSON"| SERVICES
    SEARCH --> |"Search Query"| OMNI
    
    classDef client fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    class BROWSER,VPN,API,SEARCH client
{{< /mermaid >}}

### Layer 4: Gateway & Proxy

{{< mermaid >}}
graph TB
    subgraph Gateways["Gateway Layer"]
        CADDY[🔄 Omni Caddy<br/>:8443 SSL Termination<br/>:8082 HTTP Proxy]
        DASH[📊 Homepage<br/>:8765 Central Dashboard]
        FILES[📁 NextExplorer<br/>:8080 File Browser/Editor]
        NGINX[🌐 Nginx<br/>:8056 Landing Page]
    end
    
    CADDY --> |"Route to"| APPS
    DASH --> |"Links to"| ALL_SERVICES
    FILES --> |"Edit"| CONFIG_FILES
    NGINX --> |"Serve"| STATIC_SITES
    
    classDef gateway fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    class CADDY,DASH,FILES,NGINX gateway
{{< /mermaid >}}

### Layer 3: Application Services

{{< mermaid >}}
graph TB
    subgraph Apps["28 Running Containers"]
        subgraph Core["Core Services"]
            OMNI[🔍 Omni Search<br/>:3080]
            DIRECT[📦 Directus CMS<br/>:8055]
            HUGO[📝 Hugo Blog<br/>:1313]
            OLIVE[⚡ OliveTin Automation<br/>:1337]
        end
        
        subgraph Data["Data Services"]
            OMDB[🧠 OpenMemory Dashboard<br/>:13120]
            FOSS[📊 FossFlow<br/>:3090]
        end
        
        subgraph Web["Web Services"]
            ASTRO1[🚀 Astro Vector<br/>:8092]
            ASTRO2[👕 Astro T-Shirt<br/>:8093]
            LP[🏠 Landing Page<br/>:8056]
        end
        
        subgraph Tasks["Task Containers"]
            RESEARCH[🔬 Research Task]
            FLOWS[🔄 Flows App]
            RELAY[📡 Relay Service]
        end
    end
    
    classDef core fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef data fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px
    classDef web fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    classDef tasks fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    
    class OMNI,DIRECT,HUGO,OLIVE core
    class OMDB,FOSS data
    class ASTRO1,ASTRO2,LP web
    class RESEARCH,FLOWS,RELAY tasks
{{< /mermaid >}}

### Layer 2: AI/Agent Ecosystem

{{< mermaid >}}
graph TB
    OPENCODE[🤖 OpenCode Core<br/>Sisyphus Agent<br/>Model: GLM-5]
    
    subgraph MCP["MCP Servers - 4 Configured"]
        OM[✅ OpenMemory<br/>:8081/MCP]
        BS[✅ Brave Search<br/>Web Search]
        AB[✅ Agent-Browser<br/>Browser Automation]
        PW[❌ Playwright<br/>Disabled]
        C7[✅ Context7<br/>Library Docs]
    end
    
    subgraph Skills["88 Skills - 10 Categories"]
        direction LR
        S1[📦 Infrastructure<br/>containers, space, diagnose]
        S2[🤖 AI/ML<br/>openrag, research, flow]
        S3[📝 Content<br/>hugo, astro, beautiful-mermaid]
        S4[💾 Data<br/>databases, directus, openmemory]
        S5[⚙️ Automation<br/>cronflow, oliveTin, activepieces]
        S6[🔌 Integration<br/>telegram, slack, portainer]
        S7[📊 Monitoring<br/>maintenance, performance, round]
        S8[🎨 UI/UX<br/>chartjs, presentation, dashboard]
        S9[🛠️ Utilities<br/>config, versions, git-master]
        S10[📋 Management<br/>task-management, skill-catalogue]
    end
    
    subgraph Agents["14 GSD Agents"]
        ACTIVE[✅ gsd-executor<br/>Active]
        DISABLED[❌ 13 Agents<br/>Disabled]
    end
    
    subgraph Cron["20 Cron Jobs"]
        direction LR
        H[⏰ Hourly<br/>Monitoring, Alerts]
        D[📅 Daily<br/>Reports, Analysis]
        W[📆 Weekly<br/>Digests, Summaries]
        O[🌙 Overnight<br/>Indexing, Sync]
    end
    
    OPENCODE --> MCP
    OPENCODE --> Skills
    OPENCODE --> Agents
    Cron --> OPENCODE
    
    classDef core fill:#4caf50,stroke:#1b5e20,stroke-width:3px,color:#fff
    classDef mcp fill:#2196f3,stroke:#0d47a1,stroke-width:2px,color:#fff
    classDef skill fill:#ff9800,stroke:#e65100,stroke-width:2px
    classDef agent fill:#9c27b0,stroke:#4a148c,stroke-width:2px,color:#fff
    classDef cron fill:#f44336,stroke:#b71c1c,stroke-width:2px,color:#fff
    
    class OPENCODE core
    class OM,BS,AB,PW,C7 mcp
    class S1,S2,S3,S4,S5,S6,S7,S8,S9,S10 skill
    class ACTIVE,DISABLED agent
    class H,D,W,O cron
{{< /mermaid >}}

### Layer 1: Data & Infrastructure

{{< mermaid >}}
graph TB
    subgraph Databases["Database Layer"]
        PGVEC[🐘 PostgreSQL + pgvector<br/>:5433<br/>Vector Embeddings]
        PGLIT[🐘 PostgreSQL LiteLLM<br/>:5432<br/>LLM Gateway DB]
        PGDIR[🐘 PostgreSQL Directus<br/>:5432<br/>CMS Data]
        REDIS[🔴 Redis Cache<br/>:6379<br/>Session Cache]
        SQLITE[💾 SQLite<br/>OpenMemory<br/>1,083 Entries]
    end
    
    subgraph Observability["Observability Stack"]
        OTEL[📊 OpenTelemetry Collector<br/>:4317 gRPC<br/>:4318 HTTP]
        JAEGER[🔍 Jaeger Tracing<br/>:16686<br/>Distributed Traces]
        PROM[📈 Prometheus<br/>:9090<br/>Metrics & Alerts]
    end
    
    subgraph Admin["Admin Tools"]
        PGA[🛠️ pgAdmin 4<br/>:5050<br/>Database Management]
    end
    
    subgraph Storage["Storage Volumes"]
        DOCKER[/media/docker/<br/>Container Data]
        CONFIG[~/.config/opencode/<br/>Configuration]
        BACKUP[/mnt/backup/<br/>Backups]
    end
    
    OTEL --> JAEGER
    OTEL --> PROM
    PGA --> PGVEC
    PGA --> PGLIT
    PGA --> PGDIR
    
    classDef db fill:#311b92,stroke:#000,stroke-width:2px,color:#fff
    classDef obs fill:#004d40,stroke:#000,stroke-width:2px,color:#fff
    classDef admin fill:#e65100,stroke:#000,stroke-width:2px,color:#fff
    classDef storage fill:#f57f17,stroke:#000,stroke-width:2px
    
    class PGVEC,PGLIT,PGDIR,REDIS,SQLITE db
    class OTEL,JAEGER,PROM obs
    class PGA admin
    class DOCKER,CONFIG,BACKUP storage
{{< /mermaid >}}

---

## 🔄 Data Flow Diagram

{{< mermaid >}}
flowchart LR
    subgraph Input["User Input"]
        U1[Web Request]
        U2[API Call]
        U3[Trigger Word]
        U4[Scheduled Task]
    end
    
    subgraph Processing["Processing"]
        P1[Gateway Routing]
        P2[OpenCode Agent]
        P3[Skill Execution]
        P4[MCP Server]
    end
    
    subgraph Output["Output"]
        O1[Response/Code]
        O2[Blog Post]
        O3[Report]
        O4[Notification]
    end
    
    U1 --> P1
    U2 --> P1
    U3 --> P2
    U4 --> P2
    
    P1 --> P2
    P2 --> P3
    P3 --> P4
    
    P3 --> O1
    P3 --> O2
    P3 --> O3
    P4 --> O4
{{< /mermaid >}}

---

## 📈 System Statistics

| Metric | Count | Details |
|--------|-------|---------|
| **Running Containers** | 28 | Docker API |
| **Listening Ports** | 30+ | `ss -tuln` |
| **Skills** | 88 | 10 categories |
| **GSD Agents** | 14 | 1 active, 13 disabled |
| **MCP Servers** | 4 | 3 enabled, 1 disabled |
| **Cron Jobs** | 20 | Hourly/Daily/Weekly/Overnight |
| **OpenMemory Entries** | 1,083 | Persistent AI memory |
| **Trigger Words** | 40+ | Quick command shortcuts |

---

## 🎯 Architecture Principles

### TELOS Compliance

| Principle | Status | Implementation |
|-----------|--------|----------------|
| **Data Sovereignty** | ⚠️ 90% | Local-first, some external APIs |
| **Open Source** | ✅ 100% | All components open-source |
| **Local-First AI** | ⚠️ 70% | External APIs (GLM-5, Brave) |
| **Deterministic Workflows** | ✅ 95% | Approval gates, explicit flows |
| **Observability** | ✅ 100% | OTel + Prometheus + Jaeger |

---

## 🔗 Quick Access Links

| Service | URL | Purpose |
|---------|-----|---------|
| Homepage | http://ubuntu4:8765 | Central dashboard |
| NextExplorer | http://ubuntu4:8080 | File browser |
| OpenMemory | http://ubuntu4:8081 | AI memory API |
| Directus | http://ubuntu4:8055 | CMS admin |
| Hugo Blog | http://ubuntu4:1313 | Blog frontend |
| Omni Search | http://ubuntu4:3080 | Unified search |
| pgAdmin | http://ubuntu4:5050 | Database admin |
| Jaeger | http://ubuntu4:16686 | Tracing UI |

---

**Diagram generated:** 2026-03-07  
**Data sources:** 4 parallel background agents + 8 direct tool calls  
**Total scan time:** ~4 minutes