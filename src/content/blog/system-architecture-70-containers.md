---
pubDatetime: 2026-02-03T10:00:00Z
title: "Complete System Architecture: 70+ Container Infrastructure Overview"
postSlug: "system-architecture-70-containers"
description: "Complete System Architecture: 70+ Container Infrastructure Overview"
tags:
  - devops
  - architecture
  - monitoring
---

{{< mermaid >}}
graph TB
    %% ===== STYLING =====
    classDef infrastructure fill:#1e293b,stroke:#334155,color:#f8fafc
    classDef host fill:#0f172a,stroke:#1e293b,color:#38bdf8
    classDef network fill:#0891b2,stroke:#0e7490,color:#fff
    classDef proxy fill:#6366f1,stroke:#4f46e5,color:#fff
    classDef service fill:#3b82f6,stroke:#2563eb,color:#fff
    classDef ai fill:#a855f7,stroke:#7c3aed,color:#fff
    classDef storage fill:#22c55e,stroke:#16a34a,color:#fff
    classDef monitor fill:#ef4444,stroke:#dc2626,color:#fff
    classDef external fill:#f59e0b,stroke:#d97706,color:#fff
    classDef data fill:#06b6d4,stroke:#0891b2,color:#fff

    %% ===== INFRASTRUCTURE LAYER =====
    subgraph Infrastructure["🏗️ Infrastructure Layer"]
        Physical[Physical Server<br/>ubuntu58-1<br/>Linux]:::infrastructure
        DockerEngine[Docker Engine<br/>Container Orchestration<br/>Docker Compose + Swarm]:::infrastructure
        Storage[Local Storage<br/>/media/*<br/>Docker Volumes]:::storage
    end

    %% ===== NETWORK LAYER =====
    subgraph Networks["🌐 Network Layer"]
        Tailscale[Tailscale VPN<br/>Mesh Network<br/>Global Access]:::network
        DockerBridge[Docker Bridge Network<br/>172.17.0.0/16<br/>Internal Communication]:::network
        HostNetwork[Host Network<br/>Direct Host Access<br/>High Performance]:::network
        CustomNetworks[Custom Networks<br/>Service Isolation<br/>Microservices]:::network
    end

    %% ===== REVERSE PROXY LAYER =====
    subgraph Proxy["🔀 Reverse Proxy Layer"]
        NginxPM[Nginx Proxy Manager<br/>:81 (Admin)<br/>:4700 (HTTP)<br/>:4701 (HTTPS)<br/>SSL Termination<br/>Route Management]:::proxy
    end

    %% ===== SERVICE PLATFORMS =====
    subgraph Platforms["🚀 Service Platforms"]
        Dokploy[Dokploy<br/>:3000<br/>Application Deployment<br/>CI/CD Automation]:::service
        Portainer[Portainer<br/>:9443 (HTTPS)<br/>Container Management<br/>Stack Orchestration]:::service
    end

    %% ===== DASHBOARD LAYER =====
    subgraph Dashboard["📊 Dashboard Layer"]
        Homarr[Homarr<br/>:7575<br/>Unified Dashboard<br/>Service Aggregation]:::service
    end

    %% ===== AI & ML PLATFORM =====
    subgraph AIPlatform["🤖 AI & ML Platform"]
        Fabric[Fabric API<br/>:8085<br/>Pattern Management<br/>AI Workflows]:::ai
        Crawl4AI[Crawl4AI<br/>:11235<br/>Web Scraping<br/>Content Extraction]:::ai
        RAG[RAG API<br/>:8000<br/>Retrieval Augmented Gen<br/>Knowledge Base]:::ai
        Meili[Meilisearch<br/>:7700<br/>Semantic Search<br/>Vector Search]:::ai
        VectorDB[Vector Database<br/>:5432<br/>Embedding Storage<br/>Similarity Search]:::storage
        OTEL[OpenTelemetry<br/>:4317-4318<br/>Tracing & Metrics<br/>LLM Observability]:::monitor
    end

    %% ===== CONTENT MANAGEMENT =====
    subgraph CMS["📝 Content Management"]
        Hugo[Hugo Site<br/>:1314<br/>Static Site<br/>Blog Platform]:::service
        Astro[Astro<br/>:8086<br/>Content Framework<br/>Fast Sites]:::service
        WordPress[WordPress<br/>:9999<br/>CMS<br/>Publishing]:::service
        WPDB[WordPress DB<br/>:3306<br/>MySQL Storage]:::storage
        Affine[Affine<br/>:3010<br/>Knowledge Base<br/>Real-time Collab]:::service
        AffineDB[Affine DB<br/>:5432<br/>PostgreSQL<br/>Vector Search]:::storage
        AffineCache[Affine Redis<br/>:6379<br/>Cache Layer]:::storage
        Memos[Memos<br/>:5230<br/>Note-taking<br/>Markdown Notes]:::service
        Convex[Convex Backend<br/>:3170-3171<br/>Real-time Backend<br/>Sync Engine]:::service
    end

    %% ===== WORKFLOW AUTOMATION =====
    subgraph Automation["⚙️ Workflow & Automation"]
        Dagu[Dagu<br/>:40125<br/>Workflow Engine<br/>DAG Orchestration]:::service
        CronMaster[CronMaster<br/>:40123<br/>Cron Management<br/>Job Scheduling]:::service
        CrontabUI[Crontab UI<br/>:40124<br/>Cron Interface<br/>Job Editor]:::service
        CrontabGuru[Crontab Guru<br/>:40126<br/>Cron Generator<br/>Schedule Builder]:::service
        ActivePieces[ActivePieces<br/>Automation<br/>Workflow Builder<br/>Visual Flows]:::service
        APDB[ActivePieces DB<br/>:5432<br/>PostgreSQL<br/>Workflow State]:::storage
        APRedis[ActivePieces Redis<br/>:6379<br/>Job Queue<br/>Cache]:::storage
    end

    %% ===== DATA & STORAGE =====
    subgraph DataStorage["💾 Data & Storage"]
        OpenMemory[OpenMemory<br/>:8080<br/>Memory Database<br/>Knowledge Persistence]:::storage
        Kavita[Kavita<br/>:5000<br/>Digital Library<br/>E-books/Media]:::storage
        FileBrowser[File Browser<br/>:8070<br/>File Management<br/>Web UI]:::storage
        FileBrowserQ[File Browser Quantum<br/>:8071<br/>Quantum Storage<br/>Advanced UI]:::storage
        Copyparty[Copyparty<br/>:3923<br/>File Server<br/>P2P Sharing]:::storage
        Joplin[Joplin<br/>:2230<br/>Note-taking<br/>Markdown Editor]:::storage
        JoplinDB[Joplin DB<br/>:5432<br/>PostgreSQL<br/>Notes Storage]:::storage
    end

    %% ===== APPLICATIONS =====
    subgraph Apps["🎯 Specialized Applications"]
        Medic[Medic API<br/>:8001<br/>Medical Backend<br/>Healthcare]:::service
        MedicFrontend[Medic Frontend<br/>:3007<br/>Medical UI<br/>Patient Portal]:::service
        MedicQdrant[Medic Qdrant<br/>:6333-6334<br/>Vector Database<br/>Medical Records]:::storage
        Formbricks[Formbricks<br/>:8150<br/>Survey Platform<br/>Feedback Collection]:::service
        FormbricksDB[Formbricks DB<br/>:5434<br/>PostgreSQL<br/>Survey Data]:::storage
        FormbricksRedis[Formbricks Redis<br/>:6380<br/>Cache<br/>Real-time]:::storage
        Postiz[Postiz<br/>Automation<br/>Social Media<br/>Content Planning]:::service
        PostizDB[Postiz DB<br/>:5432<br/>PostgreSQL<br/>Campaigns]:::storage
        PostizRedis[Postiz Redis<br/>:6379<br/>Queue<br/>Scheduling]:::storage
        WhatsApp[WhatsApp Gateway<br/>:8091<br/>Messaging<br/>Bot Integration]:::service
        WhatsAppDB[WhatsApp DB<br/>:5432<br/>PostgreSQL<br/>Messages]:::storage
        Openwork[Openwork<br/>:5173<br/>Workspace<br/>Collaboration]:::service
        ConvertX[ConvertX<br/>:4646<br/>Document Conversion<br/>PDF/Word/MD]:::service
        Searxng[SearXNG<br/>:8081<br/>Privacy Search<br/>Meta-Search]:::service
        WebSSH2[WebSSH2<br/>:2222<br/>SSH Terminal<br/>Browser Shell]:::service
        NextAIDraw[Next AI Draw<br/>:6001<br/>AI Drawing<br/>Diagram Generation]:::service
    end

    %% ===== MONITORING & OBSERVABILITY =====
    subgraph Monitoring["📈 Monitoring & Observability Stack"]
        Grafana[Grafana<br/>:3003<br/>Visualization<br/>Dashboards]:::monitor
        Cadvisor[cAdvisor<br/>:8083<br/>Container Metrics<br/>Docker Stats]:::monitor
        NodeExporter[Node Exporter<br/>:9100<br/>System Metrics<br/>Host Stats]:::monitor
        Telemetry[Telemetry Collector<br/>:4567<br/>Metrics Collector<br/>Data Aggregation]:::monitor
        TestMetrics[Test Metrics<br/>:9546<br/>Testing<br/>Dev Metrics]:::monitor
        Jaeger[Jaeger<br/>:16686<br/>Distributed Tracing<br/>Request Tracing]:::monitor
        OTELCollector[OTEL Collector<br/>:4317-4318<br/>Tracing Collector<br/>OpenTelemetry]:::monitor
        OpenLLMetry[OpenLLMetry<br/>LLM Monitoring<br/>Token Tracking<br/>AI Observability]:::monitor
    end

    %% ===== NETWORK SERVICES =====
    subgraph NetworkServices["🌐 Network Services"]
        TechnitiumDNS[Technitium DNS<br/>:53, :5380<br/>DNS Server<br/>Local Resolution]:::network
        Mlocate[mlocate<br/>:8180<br/>File Search<br/>Quick Locate]:::network
    end

    %% ===== EXTERNAL INTEGRATIONS =====
    subgraph External["🔗 External Integrations"]
        TailscaleHost[Tailscale Host<br/>ubhost<br/>Backup Server<br/>/mnt/sda4]:::external
        GitHub[GitHub<br/>Remote Repos<br/>Code Backup<br/>CI/CD]:::external
        Internet[Internet<br/>Public Access<br/>API Services<br/>Updates]:::external
    end

    %% ===== CONNECTIONS =====

    %% Infrastructure to Docker
    Physical --> DockerEngine
    Physical --> Storage
    DockerEngine --> DockerBridge
    DockerEngine --> HostNetwork
    DockerEngine --> CustomNetworks

    %% Network
    Tailscale --> Physical
    Tailscale -.->|VPN Tunnel| Internet

    %% Proxy Layer
    NginxPM --> DockerBridge
    NginxPM -.->|SSL Certs| Storage

    %% Platform Services
    Dokploy --> DockerEngine
    Portainer --> DockerEngine
    Homarr --> DockerBridge

    %% AI Platform Dependencies
    Fabric --> DockerBridge
    Crawl4AI --> DockerBridge
    RAG --> DockerBridge
    RAG -.-> VectorDB
    Meili --> DockerBridge
    Meili -.-> VectorDB
    OTEL --> DockerBridge
    OTEL -.-> OTELCollector
    OTELCollector -.-> Jaeger

    %% CMS Dependencies
    Hugo --> DockerBridge
    Hugo -.-> Storage
    Astro --> DockerBridge
    Astro -.-> Storage
    WordPress --> DockerBridge
    WordPress -.-> WPDB
    Affine --> DockerBridge
    Affine -.-> AffineDB
    Affine -.-> AffineCache
    Memos --> DockerBridge
    Memos -.-> Storage
    Convex --> DockerBridge

    %% Automation Dependencies
    Dagu --> DockerBridge
    CronMaster --> DockerBridge
    CrontabUI --> DockerBridge
    CrontabGuru --> DockerBridge
    ActivePieces --> DockerBridge
    ActivePieces -.-> APDB
    ActivePieces -.-> APRedis

    %% Storage Services
    OpenMemory --> DockerBridge
    OpenMemory -.-> Storage
    Kavita --> DockerBridge
    Kavita -.-> Storage
    FileBrowser --> DockerBridge
    FileBrowser -.-> Storage
    FileBrowserQ --> DockerBridge
    FileBrowserQ -.-> Storage
    Copyparty --> DockerBridge
    Copyparty -.-> Storage
    Joplin --> DockerBridge
    Joplin -.-> JoplinDB

    %% Application Dependencies
    Medic --> DockerBridge
    Medic -.-> MedicQdrant
    MedicFrontend --> DockerBridge
    MedicFrontend -.-> Medic
    Formbricks --> DockerBridge
    Formbricks -.-> FormbricksDB
    Formbricks -.-> FormbricksRedis
    Postiz --> DockerBridge
    Postiz -.-> PostizDB
    Postiz -.-> PostizRedis
    WhatsApp --> DockerBridge
    WhatsApp -.-> WhatsAppDB
    Openwork --> DockerBridge
    ConvertX --> DockerBridge
    Searxng --> DockerBridge
    WebSSH2 --> DockerBridge
    NextAIDraw --> DockerBridge

    %% Monitoring Stack
    Grafana --> DockerBridge
    Cadvisor --> DockerEngine
    NodeExporter --> Physical
    Telemetry --> DockerBridge
    Jaeger --> DockerBridge
    OTELCollector --> DockerBridge
    OpenLLMetry --> DockerBridge

    %% Monitoring Data Flow
    Cadvisor -.->|Container Metrics| Telemetry
    NodeExporter -.->|System Metrics| Telemetry
    Telemetry -.->|Aggregated Data| Grafana
    OTELCollector -.->|Traces| Jaeger
    OTELCollector -.->|Metrics| Grafana

    %% Network Services
    TechnitiumDNS --> HostNetwork
    Mlocate --> DockerBridge

    %% External Integrations
    Physical -.->|SSH Backup| TailscaleHost
    TailscaleHost -.->|Mounts| Storage
    Portainer -.->|Git Push| GitHub
    DockerEngine -.->|Pull Images| Internet
    Services[All Services]:::service
    Services -.-> NginxPM
    NginxPM -.->|Reverse Proxy| Internet
{{< /mermaid >}}

## Overview

This comprehensive system architecture represents the complete infrastructure stack of ubuntu58-1, orchestrating **70+ containers** across multiple layers including infrastructure, networking, AI/ML platforms, content management, workflow automation, data storage, specialized applications, and monitoring.

## Architecture Layers

### Infrastructure Layer

The foundation of the entire system runs on a physical Ubuntu Linux server with Docker Engine providing container orchestration using both Docker Compose and Swarm for different service stacks. All persistent data is stored locally at `/media/*` with Docker volume bindings ensuring data persistence across container restarts.

### Network Layer

The network infrastructure consists of:
- **Tailscale VPN**: Provides secure mesh networking for global access to the server
- **Docker Bridge Network**: Default bridge (172.17.0.0/16) for internal container communication
- **Host Network**: Direct host access for high-performance services that need network-level visibility
- **Custom Networks**: 33 isolated networks for microservices and service grouping

### Reverse Proxy Layer

Nginx Proxy Manager serves as the central ingress controller for all external traffic:
- **Admin UI** on port 81 for configuration
- **HTTP** on port 4700
- **HTTPS** on port 4701 with automatic SSL termination
- Centralized route management for all services

## Service Platforms

Two primary management platforms provide operational control:

- **Dokploy** (port 3000): Application deployment platform with CI/CD automation
- **Portainer** (port 9443): Container management interface and stack orchestration

A unified **Homarr** dashboard (port 7575) aggregates all services into a single control panel.

## AI & ML Platform

The AI and machine learning stack enables advanced capabilities:

- **Fabric API** (port 8085): Pattern management and AI workflow orchestration
- **Crawl4AI** (port 11235): Web scraping and content extraction
- **RAG API** (port 8000): Retrieval Augmented Generation for knowledge base integration
- **Meilisearch** (port 7700): Semantic and vector search engine
- **Vector Database** (port 5432): Embedding storage and similarity search
- **OpenTelemetry** (ports 4317-4318): LLM observability and token tracking

The AI pipeline flows from content scraping (Crawl4AI) through processing (RAG API) to storage (Vector DB) with Meilisearch providing semantic search capabilities.

## Content Management Systems

Multiple content platforms serve different use cases:

- **Hugo** (port 1314): Static site generator for this blog platform
- **Astro** (port 8086): Modern content framework for fast websites
- **WordPress** (port 9999): Classic CMS with MySQL backend
- **Affine** (port 3010): Knowledge base with real-time collaboration and PostgreSQL with vector search
- **Memos** (port 5230): Markdown-based note-taking application
- **Convex** (ports 3170-3171): Real-time backend with sync engine

Each CMS has its own database infrastructure with Affine featuring both PostgreSQL and Redis caching for performance.

## Workflow & Automation

Automation capabilities span multiple tools:

- **Dagu** (port 40125): DAG-based workflow orchestration engine
- **CronMaster** (port 40123): Centralized cron job management
- **Crontab UI** (port 40124): Visual cron job editor
- **Crontab Guru** (port 40126): Schedule builder and generator
- **ActivePieces** with PostgreSQL and Redis: Visual workflow builder for automation

## Data & Storage

Storage and file management services include:

- **OpenMemory** (port 8080): Knowledge persistence and memory database
- **Kavita** (port 5000): Digital library for e-books and media
- **File Browser** (port 8070): Web-based file management
- **File Browser Quantum** (port 8071): Advanced file management UI
- **Copyparty** (port 3923): P2P file sharing server
- **Joplin** (port 2230): Markdown note-taking with PostgreSQL backend

## Specialized Applications

Diverse applications serve specific domains:

### Healthcare
- **MEDIC Stack**: API (port 8001), Frontend (port 3007), Qdrant vector DB (ports 6333-6334) for medical records

### Surveys & Feedback
- **Formbricks** (port 8150): Survey platform with PostgreSQL (port 5434) and Redis (port 6380)

### Social Media
- **Postiz**: Automation platform with PostgreSQL (port 5432) and Redis (port 6379) for campaign management

### Messaging
- **WhatsApp Gateway** (port 8091): Messaging bot with PostgreSQL backend

### Collaboration & Tools
- **Openwork** (port 5173): Workspace collaboration platform
- **ConvertX** (port 4646): Document conversion (PDF/Word/MD)
- **SearXNG** (port 8081): Privacy-focused meta-search
- **WebSSH2** (port 2222): Browser-based SSH terminal
- **Next AI Draw** (port 6001): AI-powered diagram generation

## Monitoring & Observability Stack

A comprehensive monitoring stack provides full visibility:

- **Grafana** (port 3003): Visualization and dashboarding
- **cAdvisor** (port 8083): Container-level metrics collection
- **Node Exporter** (port 9100): Host system metrics
- **Telemetry Collector** (port 4567): Data aggregation
- **Jaeger** (port 16686): Distributed tracing for request tracking
- **OTEL Collector** (ports 4317-4318): OpenTelemetry tracing collection
- **OpenLLMetry**: LLM-specific monitoring and token tracking

### Monitoring Data Flow

The monitoring pipeline collects metrics from multiple sources:

1. **cAdvisor** → Container metrics
2. **Node Exporter** → System metrics
3. **Telemetry Collector** → Aggregates all metrics
4. **Grafana** → Visualizes and displays data
5. **OTEL Collector** → Distributed traces
6. **Jaeger** → Request tracing visualization

## Network Services

Essential network infrastructure:

- **Technitium DNS** (ports 53, 5380): Local DNS server for custom resolution
- **mlocate** (port 8180): Fast file search and indexing

## External Integrations

### Backup System

- **Primary Host**: ubhost (Tailscale hostname)
- **Location**: `/mnt/sda4`
- **Method**: SSH key authentication
- **Scope**: Full system backups including Docker volumes

### Version Control

- **GitHub**: Repository backups and CI/CD integration
- **Portainer**: Stack configuration backup to git

### Internet Access

- Docker image pulls
- Package updates
- API service calls
- Content delivery

## Key Architecture Patterns

### Microservices Architecture

Services are isolated in custom Docker networks with loose coupling via API communication and independent scaling and deployment capabilities. Each service typically has its own database/cache.

### Layered Security

- VPN-only access via Tailscale for remote connections
- Reverse proxy with SSL termination for external traffic
- Network segmentation (bridge/host/custom) for isolation
- Service isolation in dedicated networks

### Observability

Three-tier monitoring spans host, container, and application levels:
- Centralized metrics collection via Telemetry Collector
- Distributed tracing with OpenTelemetry
- Real-time dashboards in Grafana
- LLM observability with OpenLLMetry

### High Availability

- Docker auto-restart policies for resilience
- Health checks for critical services
- Backup to external host (ubhost)
- Git-based configuration management

## Data Flow Patterns

### Service Ingress Flow

1. External request → Nginx Proxy Manager
2. SSL termination → Internal routing
3. Service routing → Docker Bridge/Host Network
4. Service processing → Application logic
5. Response → Reverse through Nginx PM → Client

### AI/ML Pipeline Flow

1. Crawl4AI scrapes web content
2. RAG API processes content
3. Vector DB stores embeddings
4. Meilisearch enables semantic search
5. OpenTelemetry tracks LLM usage

## System Statistics

- **Total Containers**: 70
- **Running Services**: 63
- **Healthy Services**: 18
- **Custom Networks**: 33
- **Exposed Ports**: 60+
- **Storage Volumes**: 50+ volume bindings

## Container Distribution by Category

{{< mermaid >}}
pie
    title Container Distribution by Category (70 Total)
    "Content Management (9)" : 9
    "Specialized Applications (17)" : 17
    "Monitoring & Observability (8)" : 8
    "Data & Storage (7)" : 7
    "Workflow & Automation (6)" : 6
    "AI & ML Platform (6)" : 6
    "Service Platforms (3)" : 3
    "Network Services (2)" : 2
    "Infrastructure (3)" : 3
    "Dashboard (1)" : 1
    "Reverse Proxy (1)" : 1
    "External Integrations (3)" : 3
{{< /mermaid >}}

The largest categories are **Specialized Applications** (24%) and **Content Management** (13%), reflecting the diverse workloads supported by this infrastructure.

## Service Health Status Breakdown

{{< mermaid >}}
pie
    title Container Health Status (70 Total)
    "Running (63)" : 63
    "Unhealthy (4)" : 4
    "Restarting (1)" : 1
    "Stopped (2)" : 2
{{< /mermaid >}}

### Unhealthy Services
- **joplin-app** (:2230) - Note-taking application
- **kuse-cowork** - Coworking platform (host network)
- **teeshirts-website** (:8090) - E-commerce site
- **openllmetry-demo** - OpenLLMetry demo (restarting loop)

## Port Usage Ranges

{{< mermaid >}}
pie
    title Port Usage Distribution by Range
    "2000-2999 (2 services)" : 2
    "3000-3999 (12 services)" : 12
    "4000-4999 (6 services)" : 6
    "5000-5999 (8 services)" : 8
    "6000-6999 (4 services)" : 4
    "7000-7999 (3 services)" : 3
    "8000-8999 (14 services)" : 14
    "9000-9999 (2 services)" : 2
    "10000-19999 (8 services)" : 8
    "20000+ (1 service)" : 1
{{< /mermaid >}}

### Port Distribution Analysis
- **3000-3999 range**: Most heavily used (12 services) - Common for web applications
- **8000-8999 range**: High usage (14 services) - API and internal services
- **Other ranges**: Distributed across various port assignments for specialized services

## Database Technology Distribution

{{< mermaid >}}
pie
    title Database Types (15 Total)
    "PostgreSQL/PGVector (9)" : 9
    "Redis (6)" : 6
    "MySQL (1)" : 1
    "Qdrant (1)" : 1
{{< /mermaid >}}

### Database Stack Summary
- **PostgreSQL/PGVector**: Primary database choice (60%) - Used for applications, surveys, automation, content management
- **Redis**: Caching layer (40%) - Essential for performance across multiple stacks
- **MySQL**: Legacy support (7%) - WordPress
- **Qdrant**: Vector database (7%) - Medical records and AI/ML embeddings

## Infrastructure Resource Allocation

{{< mermaid >}}
pie
    title Services by Resource Demand Level
    "High CPU (8 services)" : 8
    "High Memory (12 services)" : 12
    "High I/O (6 services)" : 6
    "Low Resource (28 services)" : 28
    "Network Intensive (16 services)" : 16
{{< /mermaid >}}

### Resource Demand Analysis
- **Low Resource Services**: 28 containers - Lightweight utilities and simple services
- **Network Intensive**: 16 services - Proxies, gateways, communication services
- **High Memory**: 12 services - Databases, AI/ML, large applications
- **High CPU**: 8 services - Conversion, processing, intensive workloads
- **High I/O**: 6 services - File servers, storage, backup services

## Network Topology Overview

{{< mermaid >}}
graph LR
    Internet[Internet]
    Tailscale[Tailscale VPN]
    Nginx[Nginx Proxy Manager]
    Bridge[Docker Bridge Network]
    Host[Host Network]
    Custom[Custom Networks]
    
    Internet --> Tailscale
    Internet --> Nginx
    Tailscale --> Host
    Nginx --> Bridge
    Nginx --> Custom
    Bridge -->|33 Networks| Custom
    
    style Internet fill:#f59e0b,stroke:#d97706,color:#fff
    style Tailscale fill:#0891b2,stroke:#0e7490,color:#fff
    style Nginx fill:#6366f1,stroke:#4f46e5,color:#fff
    style Bridge fill:#3b82f6,stroke:#2563eb,color:#fff
    style Host fill:#1e293b,stroke:#334155,color:#f8fafc
    style Custom fill:#22c55e,stroke:#16a34a,color:#fff
{{< /mermaid >}}

### Network Architecture Flow
1. **External Traffic** → Internet
2. **Secure Access** → Tailscale VPN (direct to host)
3. **Public Access** → Nginx Proxy Manager (SSL termination)
4. **Internal Routing** → Docker Bridge or Custom Networks
5. **Service Isolation** → 33 custom networks for microservices

## Future Enhancements

Potential improvements for the architecture:

1. **Service Mesh**: Implement Istio or Linkerd for advanced service-to-service communication
2. **Message Queue**: Add RabbitMQ or Kafka for event-driven architecture
3. **CDN Integration**: Content delivery network for static assets
4. **Automated Backups**: Enhanced backup scheduling and verification
5. **Disaster Recovery**: Multi-region backup strategy
6. **API Gateway**: Centralized API management and rate limiting
7. **Secret Management**: Vault or similar for sensitive data
8. **GitOps**: Full GitOps workflow with ArgoCD or Flux

## Conclusion

This architecture represents a robust, scalable, and highly observable infrastructure supporting diverse workloads from content management to AI/ML pipelines. The layered design with comprehensive monitoring, backup, and security practices ensures reliability and ease of management across the entire technology stack.