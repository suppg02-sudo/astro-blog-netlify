---
pubDatetime: 2026-03-04T16:30:00Z
title: "OpenMemory: Production-Ready Long-Term Memory for AI Agents"
postSlug: "openmemory-production-ready"
description: "A deep dive into OpenMemory - the Hierarchical Memory Decomposition (HMD v2) system with 5-sector embeddings, graceful decay curves, and production-grade retrieval. Currently running with 1,083 memori"
tags:
  - agents
  - openmemory
  - cavira
  - memory-system
  - hmd
  - mcp
  - ai
---

OpenMemory is a production-ready long-term memory system for AI agents, implementing the **Hierarchical Memory Decomposition (HMD v2)** specification. Unlike flat vector databases or simple JSON storage, OpenMemory treats every conversation as a living system—capturing emotion, context, and time with graceful decay and automatic reinforcement.

## Current Server Status

| Metric | Value |
|--------|-------|
| **Container** | `openmemory-openmemory-1` |
| **Status** | Up 2 hours (healthy) |
| **Port** | 8081 (external) → 8080 (internal) |
| **Protocol** | MCP 2024-11-05 |
| **Database** | SQLite at `/data/openmemory.sqlite` |
| **Total Memories** | 1,083 |
| **Dashboard** | http://ubuntu4:13120 |

## The Five-Sector Memory Model

OpenMemory encodes conversations into **five synchronized dimensional vectors** that elegantly preserve nuance across sessions:

| Sector | Purpose | Decay Lambda | Use For |
|--------|---------|--------------|---------|
| **Episodic** | Events & experiences | 0.015 | Session logs, interactions |
| **Semantic** | Facts & concepts | 0.005 | Knowledge, documentation |
| **Procedural** | Skills & patterns | 0.008 | How-to, configurations |
| **Emotional** | Sentiment arcs | 0.020 | Preferences, frustrations |
| **Reflective** | Meta-cognition | 0.001 | Insights, patterns learned |

The lower the decay lambda, the longer memories persist. Reflective insights (0.001) outlast emotional reactions (0.020), matching how human memory prioritizes different types of information.

## Memory Sector Distribution

Current breakdown of the 1,083 memories stored:

{{< chart >}}
{
  type: 'doughnut',
  data: {
    labels: ['Procedural', 'Semantic', 'Episodic', 'Emotional', 'Reflective'],
    datasets: [{
      data: [497, 451, 44, 47, 38],
      backgroundColor: ['#6366f1', '#22d3ee', '#f59e0b', '#ef4444', '#10b981']
    }]
  },
  options: {
    plugins: {
      title: { display: true, text: 'Memory Distribution by Sector (1,083 total)', color: '#e2e8f0' },
      legend: { labels: { color: '#e2e8f0' } }
    }
  }
}
{{< /chart >}}

## Graceful Decay & Automatic Reinforcement

Memories fade following curved trajectories, while reinforcement pulses lift critical context back above the retention threshold:

1. **Sector-aware decay** — Each dimension carries its own slope and minimum floor
2. **Automatic reinforcement** — High-signal events fire a pulse that restores strength
3. **Attribution trails** — Every reinforcement links back to its trigger

This means frequently accessed context stays sharp without manual tuning, while stale information gracefully fades.

## Performance Comparison

OpenMemory delivers superior contextual recall at a fraction of the cost of hosted memory APIs:

{{< chart >}}
{
  type: 'bar',
  data: {
    labels: ['OpenMemory', 'Supermemory', 'Mem0', 'Vector DBs'],
    datasets: [{
      label: 'Query Latency (ms)',
      data: [110, 350, 250, 160],
      backgroundColor: ['#6366f1', '#94a3b8', '#94a3b8', '#94a3b8']
    }]
  },
  options: {
    indexAxis: 'y',
    plugins: {
      title: { display: true, text: 'Query Latency Comparison (lower is better)', color: '#e2e8f0' },
      legend: { display: false }
    },
    scales: {
      x: { grid: { color: '#334155' }, ticks: { color: '#e2e8f0' } },
      y: { grid: { color: '#334155' }, ticks: { color: '#e2e8f0' } }
    }
  }
}
{{< /chart >}}

| Metric | OpenMemory | SaaS Alternatives |
|--------|------------|-------------------|
| **Query Latency** | 110ms | 250-350ms |
| **Cost / 1M Tokens** | $0.35 | $1.20-2.50+ |
| **Monthly Cost (100k)** | $6 | $60-120 |
| **Throughput** | 40 ops/s | 10-15 ops/s |
| **Architecture** | HMD v2 (multi-hop) | Flat embeddings |
| **Data Ownership** | 100% | Vendor |

## System Architecture

The Hierarchical Memory Decomposition pipeline processes memories through five layers:

{{< mermaid >}}
flowchart TD
    subgraph L1["Layer 1: Input & Ingestion"]
        D[Documents]
        C[Conversations]
        E[Events]
        A[Audio]
        W[Web Pages]
    end

    subgraph L2["Layer 2: Processing"]
        PC[Parse & Clean]
        CH[Chunk]
        CL[Classify Sector]
        EM[Generate Embeddings]
    end

    subgraph L3["Layer 3: Storage"]
        EP[Episodic]
        SE[Semantic]
        PR[Procedural]
        EM2[Emotional]
        RE[Reflective]
        VS[(SQLite Vector Store)]
        WG[Waypoint Graph]
    end

    subgraph L4["Layer 4: Retrieval"]
        SF[Sector Fusion]
        AS[Activation Spread]
        CR[Composite Ranking]
    end

    subgraph L5["Layer 5: Output"]
        RR[Ranked Results]
        DS[Decay Scheduler]
        RF[Reinforcement]
    end

    D & C & E & A & W --> PC
    PC --> CH --> CL --> EM
    EM --> EP & SE & PR & EM2 & RE
    EP & SE & PR & EM2 & RE --> VS
    VS --> WG
    WG --> SF --> AS --> CR
    CR --> RR
    DS --> RF --> VS
{{< /mermaid >}}

### Retrieval Pipeline

1. **Sector Fusion** — Query against 2-3 likely sectors simultaneously
2. **Activation Spread** — 1-hop waypoint graph traversal for context
3. **Composite Ranking** — Weighted scoring: `0.6×sim + 0.2×sal + 0.1×rec`

## API Access on This Server

OpenMemory is exposed via MCP (Model Context Protocol) on port 8081:

```bash
# Store a memory
curl -X POST http://localhost:8081/mcp \
  -H "Authorization: Bearer openmemory-secret-key-2025" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "openmemory_store",
      "arguments": {
        "content": "User prefers dark mode and minimal UI design",
        "metadata": {"source": "preferences", "category": "UI"},
        "tags": ["preference", "ui"]
      }
    },
    "id": 1
  }'

# Query memories
curl -X POST http://localhost:8081/mcp \
  -H "Authorization: Bearer openmemory-secret-key-2025" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "openmemory_query",
      "arguments": {
        "query": "What are user interface preferences?",
        "k": 5
      }
    },
    "id": 1
  }'
```

## Key Features

| Feature | Description |
|---------|-------------|
| **Multi-sector embeddings** | 768-dim embeddings per sector with quantization |
| **Cold-start free retrieval** | SQLite vector search with RAM caching, sub-40ms |
| **Multimodal ingestion** | Documents, transcripts, events with adaptive chunking |
| **Modular embedding engines** | OpenAI, Gemini, Voyage, or local models (Ollama) |
| **Deterministic startup** | Seeded sectors for reproducible behavior |
| **Waypoint graph routing** | Bidirectional edges with weight decay |

## Use Cases

| Application | How OpenMemory Helps |
|-------------|----------------------|
| **Conversational AI** | Persistent preferences, tone awareness, session stitching |
| **Personal assistants** | Habit graphs, task recall, adaptive prompts |
| **Knowledge management** | Document sync, waypoint graphs, semantic discovery |
| **Autonomous agents** | Workflow memory, tool outcomes, retrospective learning |

## Resources

- **Official Site**: https://openmemory.cavira.app/
- **GitHub**: https://github.com/caviraoss/openmemory
- **Documentation**: https://openmemory.cavira.app/docs/introduction
- **Local Dashboard**: http://ubuntu4:13120

---

OpenMemory provides the memory stack that autonomous agents deserve—hierarchical, sector-aware, and production-grade with built-in decay orchestration and reinforcement pulses.