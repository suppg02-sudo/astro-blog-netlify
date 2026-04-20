---
pubDatetime: 2026-03-02T21:15:00Z
title: "OpenMemory Fine-Tuning for Retrieval: A Complete Guide"
postSlug: "openmemory-fine-tuning-retrieval-guide"
description: "Comprehensive guide to fine-tuning OpenMemory for optimal retrieval performance based on community patterns and official documentation"
tags:
  - openmemory
  - research
  - embeddings
  - retrieval
  - llm
  - fine-tuning
  - ai-memory
---

OpenMemory is a **cognitive memory engine** that goes beyond simple vector databases. With 3.5k GitHub stars and 400 forks, it's become a popular choice for LLM applications needing persistent, explainable memory. This guide covers how to fine-tune OpenMemory for optimal retrieval performance.

## The Retrieval Problem

Most "memory" solutions for LLMs are really just RAG pipelines:

- Text is chunked
- Embedded into a vector store
- Retrieved by similarity

They don't understand whether something is a **fact**, **event**, **preference**, or **feeling**. They don't track how **recent** or **important** information is, or how it links to other memories.

OpenMemory solves this with a **Hierarchical Memory Decomposition** architecture that treats memory as a cognitive system, not a database.

## Retrieval Architecture

### The Pipeline

{{< mermaid >}}
graph LR
    A[Query] --> B[Sector Classifier]
    B --> C[Embedding Engine]
    C --> D[Vector Search]
    D --> E[Waypoint Graph]
    E --> F[Composite Scoring]
    F --> G[Decay Engine]
    G --> H[Top K Results]
{{< /mermaid >}}

### Multi-Sector Memory System

OpenMemory classifies memories into five sectors, each with different retrieval priorities:

| Sector | Purpose | Retrieval Priority |
|--------|---------|-------------------|
| **Episodic** | Events, experiences | High recency weight |
| **Semantic** | Facts, knowledge | High similarity weight |
| **Procedural** | Skills, how-to | Moderate both |
| **Emotional** | Feelings, sentiment | High reinforcement |
| **Reflective** | Insights, patterns | Moderate decay |

## Performance Tiers (Critical for Retrieval Quality)

OpenMemory offers four performance tiers with different tradeoffs:

| Tier | Dimensions | Recall | QPS | RAM/10k | Best For |
|------|-----------|--------|-----|---------|----------|
| **hybrid** | BM25 + synthetic | ~100% | 800-1000 | 0.5GB | Exact searches, code, docs |
| **fast** | 256-dim synthetic | ~70-75% | 700-850 | 0.6GB | Local apps, VS Code, low-end |
| **smart** | 384-dim (256+128) | ~85% | 500-600 | 0.9GB | Production servers, copilots |
| **deep** | 1536-dim OpenAI/Gemini | ~95-100% | 350-400 | 1.6GB | Cloud, high-accuracy |

### Tier Recommendations

```bash
# For production servers (recommended)
OM_TIER=smart

# For documentation/code search
OM_TIER=hybrid

# For cloud deployments needing accuracy
OM_TIER=deep
```

## Configuration Parameters

### Core Retrieval Settings

```bash
# Performance Tier (REQUIRED)
OM_TIER=smart                      # hybrid | fast | smart | deep

# Keyword Matching (HYBRID tier only)
OM_KEYWORD_BOOST=2.5               # Boost multiplier for keyword matches
OM_KEYWORD_MIN_LENGTH=3            # Minimum keyword length

# Similarity Threshold
OM_MIN_SCORE=0.3                   # Minimum similarity threshold
```

### Decay & Reinforcement

```bash
# Smart Decay Settings
OM_DECAY_LAMBDA=0.02               # Decay rate (lower = slower forgetting)
OM_DECAY_INTERVAL_MINUTES=120      # How often decay runs
OM_DECAY_COLD_THRESHOLD=0.25       # When memories become "cold"
OM_DECAY_REINFORCE_ON_QUERY=true   # Boost memories when recalled
OM_REGENERATION_ENABLED=true       # Regenerate cold memories
```

### Embedding Configuration

```bash
# Embedding Backend Selection
OM_EMBEDDINGS=openai               # openai | gemini | aws | ollama | local | synthetic
OM_EMBEDDING_FALLBACK=synthetic    # Comma-separated fallback chain
OM_VEC_DIM=768                     # Must match embedding model

# Local/Ollama (for offline)
OM_EMBEDDINGS=ollama
OM_OLLAMA_MODEL=nomic-embed-text   # Recommended: 768-dim

# OpenAI
OM_OPENAI_MODEL=text-embedding-3-small
```

## How Decay Works

The **composite scoring** system combines multiple factors:

```
Final Score = (similarity × w1) + (salience × w2) + (recency × w3) + (coactivation × w4)
```

Where:
- **similarity**: Vector cosine distance
- **salience**: Dynamic value with decay
- **recency**: Time-based decay function
- **coactivation**: Waypoint connection strength

### Dynamic Salience Calculation

```json
POST /dynamics/salience/calculate
{
  "initial_salience": 0.8,
  "decay_lambda": 0.01,
  "recall_count": 5,
  "emotional_frequency": 0.2,
  "time_elapsed_days": 7
}
// Returns: calculated_salience_value: 0.782
```

## Waypoint Graph (Explainable Retrieval)

The waypoint system creates **associative links** between memories:

```sql
CREATE TABLE waypoints (
  src_id TEXT PRIMARY KEY,
  dst_id TEXT NOT NULL,
  weight REAL NOT NULL,      -- Connection strength
  created_at INTEGER,
  updated_at INTEGER
)
```

This enables **explainable recall** - you can see exactly which nodes were used in context and why. GitHub issue #141 discusses refactoring waypoint creation to use ANN search for better performance at scale.

## Community Fine-Tuning Patterns

From GitHub discussions and issues:

| Discussion | Insight |
|------------|---------|
| **#90** - LangChain Integration | Best practices for memory conflicts/updates - recommends explicit versioning |
| **#109** - SimHash Deduplication | Cross-user interference issue - deduplication ignores `user_id` |
| **#105** - Temporal Filtering | Request for `startTime/endTime` parameters in query endpoint |

### Common Configurations

**High-Accuracy Production**:
```bash
OM_TIER=deep
OM_EMBEDDINGS=openai
OM_OPENAI_MODEL=text-embedding-3-small
OM_DECAY_LAMBDA=0.01          # Slow decay
OM_MIN_SCORE=0.4              # Higher threshold
```

**Local/Low-Resource**:
```bash
OM_TIER=fast
OM_EMBEDDINGS=ollama
OM_OLLAMA_MODEL=nomic-embed-text
OM_DECAY_LAMBDA=0.03          # Faster decay to save space
```

**Balanced Production (Recommended)**:
```bash
OM_TIER=smart
OM_EMBEDDINGS=openai
OM_EMBEDDING_FALLBACK=synthetic
OM_DECAY_REINFORCE_ON_QUERY=true
```

## Recommendations by Use Case

### For Better Retrieval Quality

1. **Use `smart` tier** for best recall/latency balance (85% recall, 500-600 QPS)
2. **Enable keyword boost** (`OM_KEYWORD_BOOST=2.5`) for exact matching
3. **Set `OM_DECAY_REINFORCE_ON_QUERY=true`** to keep frequently-accessed memories fresh
4. **Use fallback embeddings** (`OM_EMBEDDING_FALLBACK=synthetic`) for resilience

### For Better Performance

1. **Use `hybrid` tier** for documentation/code search (100% recall)
2. **Reduce vector dimensions** with `fast` tier if recall loss acceptable
3. **Increase decay interval** (`OM_DECAY_INTERVAL_MINUTES=240`) to reduce CPU overhead
4. **Enable compression** for long content:
   ```bash
   OM_COMPRESSION_ENABLED=true
   OM_COMPRESSION_MIN_LENGTH=100
   OM_COMPRESSION_ALGORITHM=semantic
   ```

### For Multi-User Systems

1. **Ensure user isolation** - see discussion #109 about simhash issues
2. **Use PostgreSQL backend** for scale:
   ```bash
   OM_METADATA_BACKEND=postgres
   OM_VECTOR_BACKEND=postgres
   ```

## Comparison with Other Memory Systems

| System | Key Differentiator | OpenMemory Advantage |
|--------|-------------------|---------------------|
| **Mem0** | Self-improving, managed | Self-hosted, explainable traces |
| **Supermemory** | Developer API | Local-first, multi-sector |
| **Zep** | Cloud-focused | Temporal KG, waypoint graph |

## Key Takeaways

1. **Choose the right tier** - `smart` is best for most production use cases
2. **Tune decay for your use case** - slower decay for facts, faster for events
3. **Enable reinforcement** - keeps frequently-accessed memories fresh
4. **Use fallback embeddings** - ensures resilience when primary embedding fails
5. **Leverage waypoints** - enables explainable retrieval traces

## Sources

- **Repository**: [github.com/CaviraOSS/OpenMemory](https://github.com/CaviraOSS/OpenMemory)
- **Documentation**: [openmemory.cavira.app](https://openmemory.cavira.app)
- **GitHub Issues**: #105, #109, #141, #90
- **Community**: Medium articles, LinkedIn discussions, research papers