---
pubDatetime: 2026-04-09T15:44:18Z
title: "The Verified Knowledge Engine (VKE) Architecture"
postSlug: "vke-series-pt3-architecture"
description: "The Verified Knowledge Engine (VKE) Architecture"
tags:
  - vke
  - architecture
  - memory-systems
  - research
  - series
---

# The Verified Knowledge Engine (VKE) Architecture

> **TL;DR**: The VKE is our new memory setup. It decouples artifact storage (Markdown) from retrieval caching (PostgreSQL) using Canonical Knowledge IDs (CKIDs) and an autonomous LLM compiler loop.

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MDAgNDAwIj4KICA8cmVjdCB3aWR0aD0iODAwIiBoZWlnaHQ9IjQwMCIgZmlsbD0iIzBhMDAyMCIgcng9IjEwIi8+CiAgPHJlY3QgeD0iNTAiIHk9IjUwIiB3aWR0aD0iMTUwIiBoZWlnaHQ9IjgwIiByeD0iNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjZmY0MDgxIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8dGV4dCB4PSIxMjUiIHk9Ijk1IiBmaWxsPSIjZmY0MDgxIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxNiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+dmF1bHQvbWVzc3kvPC90ZXh0PgogIDxyZWN0IHg9IjI1MCIgeT0iNTAiIHdpZHRoPSIxMjAiIGhlaWdodD0iODAiIHJ4PSI1IiBmaWxsPSJub25lIiBzdHJva2U9IiNmZmFiMDAiIHN0cm9rZS13aWR0aD0iMiIvPgogIDx0ZXh0IHg9IjMxMCIgeT0iOTUiIGZpbGw9IiNmZmFiMDAiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjE0IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5Db21waWxlcjwvdGV4dD4KICA8cmVjdCB4PSI0MjAiIHk9IjUwIiB3aWR0aD0iMTIwIiBoZWlnaHQ9IjgwIiByeD0iNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMDBmZmZmIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8dGV4dCB4PSI0ODAiIHk9Ijk1IiBmaWxsPSIjMDBmZmZmIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxNCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+TGludGVyIChIZXJtZXMpPC90ZXh0PgogIDxyZWN0IHg9IjU5MCIgeT0iNTAiIHdpZHRoPSIxNjAiIGhlaWdodD0iODAiIHJ4PSI1IiBmaWxsPSJub25lIiBzdHJva2U9IiMwMGZmNDEiIHN0cm9rZS13aWR0aD0iMiIvPgogIDx0ZXh0IHg9IjY3MCIgeT0iOTUiIGZpbGw9IiMwMGZmNDEiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjE2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj52YXVsdC9jbGVhbi93aWtpLzwvdGV4dD4KICA8cmVjdCB4PSIyNTAiIHk9IjI1MCIgd2lkdGg9IjMwMCIgaGVpZ2h0PSI4MCIgcng9IjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI2IzODhmZiIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgPHRleHQgeD0iNDAwIiB5PSIyOTUiIGZpbGw9IiNiMzg4ZmYiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjE2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5Qb3N0Z3JlU1FMIChDS0lEIENhY2hlKTwvdGV4dD4KICA8cGF0aCBkPSJNIDIwMCA5MCBMIDI0MCA5MCIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8cGF0aCBkPSJNIDM3MCA5MCBMIDQxMCA5MCIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8cGF0aCBkPSJNIDU0MCA5MCBMIDU4MCA5MCIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8cGF0aCBkPSJNIDY3MCAxMzAgTCA2NzAgMjkwIEwgNTUwIDI5MCIgc3Ryb2tlPSIjYjM4OGZmIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1kYXNoYXJyYXk9IjQsNCIvPgo8L3N2Zz4=" alt="Diagram" style="display:block;width:100%;max-width:680px;height:auto;margin:1.5rem auto;">

## The 3-Layer Architecture (L1)

The Verified Knowledge Engine operates on three distinct layers, completely replacing our previous ad-hoc memory mechanisms.

- **Layer 1: PostgreSQL / JSONB (The Cache)**
- **Layer 2: The Hybrid Registry (CKID)**
- **Layer 3: The Karpathy Pipeline (Evolution)**

## System Definition (L2)

### The Canonical Knowledge ID (CKID)
The core of VKE is the CKID. Domain-specific IDs (SQL integers, file paths) are mapped to a single CKID. This allows a Markdown file in the wiki to maintain perfect referential integrity with the original database event that spawned it, ensuring we never lose the context of a decision.

### The Evolutionary Pipeline
1. **Raw Vault (`vault/messy/`)**: All unstructured data, transcripts, and web fetches enter here.
2. **The Compiler**: An LLM agent sweeps the messy vault, structuring data into Markdown with YAML frontmatter containing the `CKID`.
3. **The Linter (Quality Gate)**: A strict supervisor model checks the compiled Markdown. Does it contradict the database? Are the backlinks valid?
4. **Clean Vault (`vault/clean/wiki/`)**: Only verified, linted knowledge enters here. It is the ultimate "File-Over-App" source of truth.

<details>
<summary>📖 Deep Dive: The PostgreSQL Materialized View (L3)</summary>

While Markdown is the source of truth, `grep` is too slow for global semantic routing. 

We use PostgreSQL as a high-speed materialized view. A sync script parses the YAML frontmatter of the Wiki files and updates `controlplane.knowledge_graph`. When an agent needs context, it queries the DB instantly, retrieves the file path via CKID, and reads the precise Markdown file.

</details>

---

*This is Post 3 of 4 in the **Verified Knowledge Engine** series.*

- [Post 1: Researching AI Memory: Methodology & The Stack](/posts/vke-series-pt1-methodology/)
- [Post 2: Analysis & Synthesis: Bridging Memory Paradigms](/posts/vke-series-pt2-synthesis/)
- **Post 3: The Verified Knowledge Engine (VKE) Architecture** *(you are here)*
- [Post 4: The Verified Knowledge Engine: Core Concepts & Stack Summary](/posts/vke-series-pt4-core-concepts/)
