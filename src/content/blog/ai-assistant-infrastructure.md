---
pubDatetime: 2026-03-27T10:00:00Z
title: "Personal AI Assistant Infrastructure Foundations"
postSlug: "ai-assistant-infrastructure"
description: "A comprehensive visual guide to the infrastructure foundations powering a personal AI assistant setup."
tags:
  - directus
  - architecture
  - ai
  - postgresql
  - infrastructure
---

This post presents a series of diagrams illustrating the infrastructure foundations of a personal AI assistant setup. The architecture is built on two primary pillars: **Content Management** (via Directus) and **Data Intelligence** (via PostgreSQL memory and retrieval systems).

---

## Architecture Overview

The complete infrastructure spans multiple interconnected systems:

```mermaid
graph TB
    subgraph Foundation1["🎯 Foundation 1: Content & Services"]
        D[Directus CMS<br/>Headless CMS]
        D --> DB[Dashboard<br/>+ Chat Assistant]
        D --> BP[Blog Posts<br/>via Astro]
        D --> WS[Websites]
        D --> SV[Surveys<br/>via Formbricks]
        D --> MD[Metadata Store]
        D --> EP[API Endpoints]
    end
    
    subgraph Foundation2["🧠 Foundation 2: Data & Intelligence"]
        PG[(PostgreSQL<br/>Memory & Recall)]
        PG --> MEM[pgvector<br/>Embeddings]
        PG --> RAG[OpenRAG<br/>Document Retrieval]
        PG --> NX[NextExplorer<br/>File Browser]
        PG --> NT[Notes System]
        PG --> GR[Grafana<br/>Dashboards]
    end
    
    Foundation1 <--> Foundation2
    
    style D fill:#4F46E5,color:#fff
    style PG fill:#336791,color:#fff
    style MEM fill:#10B981,color:#fff
    style RAG fill:#F59E0B,color:#fff
```

---

## Foundation 1: Directus CMS Ecosystem

Directus serves as the central content hub, managing all structured data and providing APIs for consumption.

```mermaid
graph LR
    subgraph DirectusCore["📦 Directus Core"]
        API[REST & GraphQL APIs]
        AUTH[Authentication & Roles]
        DB[(Database Layer)]
    end
    
    subgraph ContentTypes["📄 Content Types"]
        PAGES[Pages & Navigation]
        BLOG[Blog Posts]
        FORMS[Forms & Fields]
        MEDIA[Media Library]
    end
    
    subgraph Integrations["🔗 Integrations"]
        ASTRO[Astro Blog<br/>Port 3002]
        DASH[React Dashboard<br/>Port 3000]
        FB[Formbricks Surveys<br/>Port 3001]
    end
    
    API --> ContentTypes
    API --> Integrations
    AUTH --> API
    DB --> API
    
    style API fill:#4F46E5,color:#fff
    style ASTRO fill:#FF5D01,color:#fff
    style DASH fill:#61DAFB,color:#000
    style FB fill:#6366F1,color:#fff
```

---

## Foundation 2: Data Intelligence Layer

The second foundation handles all memory, retrieval, and intelligence capabilities.

```mermaid
graph TB
    subgraph PostgreSQL["🐘 PostgreSQL Core"]
        PGMAIN[(PostgreSQL<br/>Primary Database)]
        PGVEC[pgvector Extension<br/>Embeddings]
        PGJSON[JSON/JSONB Support]
    end
    
    subgraph MemorySystem["🧠 Memory Systems"]
        PGMEM[pghmem CLI<br/>Memory Manager]
        CAPTURE[capture_conversation.py<br/>Memory Storage]
        SEARCH[Semantic Search<br/>Vector Queries]
    end
    
    subgraph Retrieval["📚 Document Retrieval"]
        ORAG[OpenRAG Stack]
        LANG[Langflow<br/>:7860]
        OSEARCH[OpenSearch<br/>:9200]
        DOCLING[Docling Parser<br/>:5001]
    end
    
    subgraph Tools["🛠️ Supporting Tools"]
        NEXPL[NextExplorer<br/>:8080]
        NOTES[Notes System]
        GRAF[Grafana Dashboards<br/>:3003]
    end
    
    PGMAIN --> PGVEC
    PGVEC --> MemorySystem
    PGVEC --> Retrieval
    
    MemorySystem --> Tools
    Retrieval --> Tools
    
    style PGMAIN fill:#336791,color:#fff
    style PGVEC fill:#10B981,color:#fff
    style ORAG fill:#F59E0B,color:#fff
    style LANG fill:#FF4B4B,color:#fff
```

### OpenRAG Stack Architecture

```mermaid
flowchart LR
    subgraph Ingestion["📥 Ingestion"]
        UPLOAD[File Upload]
        PARSE[Docling Parser]
        CHUNK[Chunking Engine]
        EMBED[Embedding Generation<br/>Jina AI]
    end
    
    subgraph Storage["💾 Storage"]
        OPENSEARCH[(OpenSearch<br/>Vector Index)]
        METADB[(Metadata DB)]
    end
    
    subgraph Query["🔍 Query"]
        LANGFLOW[Langflow<br/>Flow Builder]
        RETRIEVE[Retrieval Engine]
        RERANK[Re-ranking]
    end
    
    subgraph Frontend["🖥️ Frontend"]
        RAGUI[OpenRAG UI<br/>:3000]
        APIBACK[Backend API<br/>:8000]
    end
    
    UPLOAD --> PARSE --> CHUNK --> EMBED
    EMBED --> OPENSEARCH
    EMBED --> METADB
    
    RAGUI --> APIBACK --> LANGFLOW
    LANGFLOW --> RETRIEVE --> OPENSEARCH
    RETRIEVE --> RERANK
    
    style OPENSEARCH fill:#005EB8,color:#fff
    style LANGFLOW fill:#FF4B4B,color:#fff
    style EMBED fill:#10B981,color:#fff
```

---

## Integration Flow

How the two foundations communicate and share data:

```mermaid
sequenceDiagram
    participant User
    participant Dashboard
    participant Directus
    participant PostgreSQL
    participant OpenRAG
    participant Astro
    
    User->>Dashboard: Query Request
    Dashboard->>Directus: Fetch Content
    Directus-->>Dashboard: Return Data
    
    Dashboard->>PostgreSQL: Memory Search
    PostgreSQL->>PostgreSQL: Vector Similarity
    PostgreSQL-->>Dashboard: Relevant Memories
    
    Dashboard->>OpenRAG: Document Query
    OpenRAG->>OpenRAG: Semantic Search
    OpenRAG-->>Dashboard: Retrieved Docs
    
    Dashboard-->>User: Combined Response
    
    User->>Directus: Create Blog Post
    Directus->>PostgreSQL: Store Memory
    Directus->>Astro: Trigger Build
    Astro-->>User: Published Post
```

---

## Service Topology

All services and their port mappings:

```mermaid
graph TB
    subgraph WebLayer["🌐 Web Layer - Tailscale"]
        TS[Tailscale VPN<br/>ubuntu4.tail75e52.ts.net]
    end
    
    subgraph CMSLayer["📦 CMS Layer"]
        DIR[Directus<br/>:8055]
        ASTROB[Astro Blog<br/>:3002]
    end
    
    subgraph AppLayer["📱 Application Layer"]
        DASHB[Dashboard<br/>:3000]
        FORMB[Formbricks<br/>:3001]
        NEXP[NextExplorer<br/>:8080]
    end
    
    subgraph DataLayer["💾 Data Layer"]
        PGDB[(PostgreSQL<br/>:5432)]
        OPENSE[(OpenSearch<br/>:9200)]
        REDIS[(Redis Cache<br/>:6379)]
    end
    
    subgraph AILayer["🤖 AI Layer"]
        LANGF[Langflow<br/>:7860]
        DOC[Docling<br/>:5001]
        RAGB[OpenRAG Backend<br/>:8000]
    end
    
    subgraph MonitorLayer["📊 Monitoring"]
        GRAF[Grafana<br/>:3003]
        KIB[Kibana<br/>:5601]
    end
    
    TS --> CMSLayer
    TS --> AppLayer
    CMSLayer --> DataLayer
    AppLayer --> DataLayer
    AILayer --> DataLayer
    MonitorLayer --> DataLayer
    
    style TS fill:#448AFF,color:#fff
    style PGDB fill:#336791,color:#fff
    style LANGF fill:#FF4B4B,color:#fff
```

---

## Memory Flow Architecture

How memories are captured, stored, and retrieved:

```mermaid
flowchart TD
    subgraph Capture["📸 Capture"]
        AGENT[AI Agent<br/>Conversation]
        SCRIPT[capture_conversation.py]
        TRIGGER[Trigger Words<br/>remember, save this]
    end
    
    subgraph Processing["⚙️ Processing"]
        EMBEDDING[Jina AI Embeddings]
        METADATA[Metadata Extraction]
        SCOPE[Scope Assignment<br/>user/project]
    end
    
    subgraph Storage["💾 Storage"]
        PGVEC[(PostgreSQL<br/>pgvector)]
        TYPES[Memory Types<br/>decision/action/conversation]
    end
    
    subgraph Retrieval["🔍 Retrieval"]
        PGMEM[pghmem search]
        SIMILARITY[Vector Similarity]
        CONTEXT[Context Injection]
    end
    
    subgraph Usage["📈 Usage"]
        SESSION[Session Init]
        DECISIONS[Decision Recovery]
        CONTINUITY[Context Continuity]
    end
    
    AGENT --> SCRIPT
    TRIGGER --> SCRIPT
    SCRIPT --> EMBEDDING
    EMBEDDING --> METADATA
    METADATA --> SCOPE
    SCOPE --> PGVEC
    
    PGVEC --> TYPES
    
    PGMEM --> SIMILARITY
    SIMILARITY --> PGVEC
    SIMILARITY --> CONTEXT
    
    CONTEXT --> SESSION
    CONTEXT --> DECISIONS
    CONTEXT --> CONTINUITY
    
    style PGVEC fill:#336791,color:#fff
    style EMBEDDING fill:#10B981,color:#fff
    style CONTEXT fill:#8B5CF6,color:#fff
```

---

## Key Configuration Files

| Component | Location | Purpose |
|-----------|----------|---------|
| Directus Config | `/media/docker/directus/` | CMS configuration |
| PostgreSQL Data | PostgreSQL container volume | Memory & embeddings |
| Astro Blog | `/media/docker/astro-blog/` | Blog content & builds |
| OpenRAG Stack | `/media/docker/openrag/` | Document retrieval |
| NextExplorer | `/media/docker/nextexplorer/` | File browser |
| AGENTS.md | `~/.config/opencode/AGENTS.md` | Agent instructions |
| Environment | `~/.config/opencode/environment.md` | Environment tracking |

---

## Summary

This infrastructure provides:

1. **Content Management** - Directus as the single source of truth for structured content
2. **AI Memory** - PostgreSQL with pgvector for persistent, searchable memory
3. **Document Intelligence** - OpenRAG for semantic document retrieval
4. **Unified Access** - NextExplorer for file management, Grafana for monitoring
5. **Publishing** - Astro for high-performance blog generation
6. **Feedback** - Formbricks for surveys and user input

The two foundations work together to create a cohesive AI assistant capable of remembering context, retrieving relevant information, and publishing content seamlessly.