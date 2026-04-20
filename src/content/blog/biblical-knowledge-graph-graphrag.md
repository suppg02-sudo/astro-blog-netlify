---
pubDatetime: 2026-03-19T12:00:00Z
title: "Building a Biblical Knowledge Graph with GraphRAG"
postSlug: "biblical-knowledge-graph-graphrag"
description: "Building a Biblical Knowledge Graph with GraphRAG"
tags:
  - knowledge-graph
  - bible
  - graphrag
  - research
---

## Overview

This tutorial walks through building a Biblical Knowledge Graph that combines Neo4j entity relationships with semantic search capabilities.

## The Stack

| Component | Technology | Purpose |
|----------|------------|---------|
| Knowledge Graph | Neo4j | Entity relationships |
| Vector Database | OpenSearch KNN | Semantic search |
| PostgreSQL | pgvector | Chunk storage |
| Embeddings | Nomic (768-dim) | Semantic representation |

## Part 1: Entity Extraction

We extracted entities from 555 biblical chunks using pattern matching:

**Results:**
- 93 unique entities (people, places, concepts, angels, events)
- 8 themes: apocalyptic, creation, fallen_angels, heavenly_ascent, law_covenant, messianic, secret_knowledge, wisdom

## Part 2: Building the Knowledge Graph

Graph Statistics:
- 93 entities
- 545 text nodes
- 7,710 relationships
- 8 theme nodes

## Part 3: Vector Search

We created an OpenSearch KNN index with 768-dimensional embeddings for semantic similarity search.

Search Modes:
- `bm25` - Keyword matching
- `semantic` - Vector similarity
- `hybrid` - Both combined

## Part 4: GraphRAG CLI

```bash
python3 biblerag.py "flood" --mode semantic
```

## Key Findings

### Top Entities

| Entity | Mentions |
|--------|----------|
| Eve | 315 |
| Sin | 245 |
| Heaven | 223 |
| Law | 164 |
| Love | 136 |

### Entity Types

- Places: 27 (Eden, Sinai, Zion)
- People: 25 (Enoch, Noah, Abraham)
- Concepts: 23 (Righteousness, Mercy)
- Angels: 9 (Gabriel, Michael)
- Events: 9 (Fall, Flood)

## Conclusion

This Biblical Knowledge Graph enables entity-aware search, semantic retrieval, and cross-textual analysis across Ethiopian, Gnostic, and Canonical traditions.