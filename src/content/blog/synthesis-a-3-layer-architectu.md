---
pubDatetime: 2026-04-09T14:25:41Z
title: "Synthesis: A 3-Layer Architecture for Verified Knowledge"
postSlug: "synthesis-a-3-layer-architectu"
description: "Synthesis: A 3-Layer Architecture for Verified Knowledge"
tags:
  - others
---

We are evolving our infrastructure. After a comprehensive research analysis of MemPalace (ChromaDB/SQLite) against our existing PostgreSQL-based memory stack (pghmem), we are **not** replacing our foundation. We are **synthesizing** the best ideas to build a more robust, stable, and evolutionary "Verified Knowledge" stack.

## The 3-Layer Architectural Framework

| Layer | Function | Component | Strategy |
| :--- | :--- | :--- | :--- |
| **Layer 1: Foundation** | Storage & State | **PostgreSQL** (`controlplane`) | Stable, ACID, battle-tested. |
| **Layer 2: Structure** | Context & Taxonomy | **MemPalace Metadata** | Adopt taxonomies (Wings/Rooms/Halls) as JSONB tags in `controlplane` events. |
| **Layer 3: Evolution** | Knowledge Curation | **Karpathy Pattern** | Pipeline `raw/` → `compile` → `lint` → `wiki/`. |

## Key Findings

### MemPalace's Strengths (To Adopt)
- **Structural Taxonomy:** Organizing data into Wings, Rooms, and Halls delivers a documented 34% recall boost.
- **MCP Integration:** A 19-tool interface is excellent for LLM clients.
- **Auto-Save Hooks:** Context capture upon session termination is vital.

### MemPalace's Weaknesses (To Avoid)
- **Stability:** 380+ open issues, fragmented PyPI versions (3.0.0 vs 3.0.14), and Windows breakage make it unsuitable for production.
- **Design Gaps:** The knowledge graph is currently disconnected from semantic search, forcing users to build manual "bridge" layers.
- **Scaling OOM:** Single-process ChromaDB fetches OOM on large collections. PostgreSQL handles this effortlessly.

## The Synthesis Roadmap

We are bypassing the instability of MemPalace's codebase while gaining its architectural benefits.

1. **Adopt Taxonomy Tags:** We are integrating the MemPalace taxonomy (Wings/Rooms/Halls) into our existing PostgreSQL schema as standard JSONB metadata. This gives us the retrieval boost without the technical debt of a secondary database.
2. **Implement Karpathy Pipeline:** We are automating knowledge maturation. The `raw/` → `compile` → `lint` → `wiki/` pipeline transforms raw data into a curated, human-readable knowledge base.
3. **Build MCP Interface:** We will wrap our stable PostgreSQL `controlplane` in an MCP server, implementing the MemPalace tool patterns natively.

## Why This Wins

This "Verified Knowledge" stack gives us the structural, search, and evolutionary benefits of MemPalace, while keeping the stability, concurrency, and existing integration depth of our PostgreSQL foundation.

**The result**: A system that doesn't just "remember" — it evolves.

**Tags**: architecture, memory, postgresql, mempalace, karpathy, rag, directus, astro
**Categories**: AI Architecture, Systems Design