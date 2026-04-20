---
pubDatetime: 2026-04-09T15:46:15Z
title: "The Verified Knowledge Engine: Core Concepts & Stack Summary"
postSlug: "vke-series-pt4-core-concepts"
description: "The Verified Knowledge Engine: Core Concepts & Stack Summary"
tags:
  - vke
  - summary
  - architecture
  - memory-systems
  - research
  - series
---

# The Verified Knowledge Engine: Core Concepts & Stack Summary

> **TL;DR**: The final piece of the puzzle. Here is a high-level, comprehensive summary of the Verified Knowledge Engine (VKE) stack, its core philosophy, and how the entire system snaps together into a single cohesive architecture.

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MDAgNDUwIj4KICA8cmVjdCB3aWR0aD0iODAwIiBoZWlnaHQ9IjQ1MCIgZmlsbD0iIzBhMDAyMCIgcng9IjEwIi8+CiAgPCEtLSBGaWxlIGxheWVyIC0tPgogIDxyZWN0IHg9IjUwIiB5PSI1MCIgd2lkdGg9IjcwMCIgaGVpZ2h0PSIxNTAiIGZpbGw9InJnYmEoMCwgMjU1LCAyNTUsIDAuMDUpIiBzdHJva2U9IiMwMGZmZmYiIHN0cm9rZS13aWR0aD0iMiIgcng9IjEwIiBzdHJva2UtZGFzaGFycmF5PSI1LDUiLz4KICA8dGV4dCB4PSI2MCIgeT0iODAiIGZpbGw9IiMwMGZmZmYiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjE2IiBmb250LXdlaWdodD0iYm9sZCI+RmlsZSBMYXllciAoU291cmNlIG9mIFRydXRoKTwvdGV4dD4KICA8cmVjdCB4PSIxMDAiIHk9IjEwMCIgd2lkdGg9IjE1MCIgaGVpZ2h0PSI2MCIgZmlsbD0iIzBhMDAyMCIgc3Ryb2tlPSIjZmY0MDgxIiBzdHJva2Utd2lkdGg9IjIiIHJ4PSI1Ii8+CiAgPHRleHQgeD0iMTc1IiB5PSIxMzUiIGZpbGw9IiNmZjQwODEiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjE0IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5yYXcvPC90ZXh0PgogIDxwYXRoIGQ9Ik0gMjYwIDEzMCBMIDMzMCAxMzAiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLXdpZHRoPSIyIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93KSIvPgogIDxyZWN0IHg9IjM0MCIgeT0iMTAwIiB3aWR0aD0iMTUwIiBoZWlnaHQ9IjYwIiBmaWxsPSIjMGEwMDIwIiBzdHJva2U9IiNmZmFiMDAiIHN0cm9rZS13aWR0aD0iMiIgcng9IjUiLz4KICA8dGV4dCB4PSI0MTUiIHk9IjEzNSIgZmlsbD0iI2ZmYWIwMCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTQiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkNvbXBpbGVyICsgTGludGVyPC90ZXh0PgogIDxwYXRoIGQ9Ik0gNTAwIDEzMCBMIDU3MCAxMzAiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLXdpZHRoPSIyIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93KSIvPgogIDxyZWN0IHg9IjU4MCIgeT0iMTAwIiB3aWR0aD0iMTUwIiBoZWlnaHQ9IjYwIiBmaWxsPSIjMGEwMDIwIiBzdHJva2U9IiMwMGZmNDEiIHN0cm9rZS13aWR0aD0iMiIgcng9IjUiLz4KICA8dGV4dCB4PSI2NTUiIHk9IjEzNSIgZmlsbD0iIzAwZmY0MSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTQiIHRleHQtYW5jaG9yPSJtaWRkbGUiPndpa2kvIChNYXJrZG93bik8L3RleHQ+CiAgCiAgPCEtLSBEQiBsYXllciAtLT4KICA8cmVjdCB4PSI1MCIgeT0iMjUwIiB3aWR0aD0iNzAwIiBoZWlnaHQ9IjE1MCIgZmlsbD0icmdiYSgxNzksIDEzNiwgMjU1LCAwLjA1KSIgc3Ryb2tlPSIjYjM4OGZmIiBzdHJva2Utd2lkdGg9IjIiIHJ4PSIxMCIgc3Ryb2tlLWRhc2hhcnJheT0iNSw1Ii8+CiAgPHRleHQgeD0iNjAiIHk9IjI4MCIgZmlsbD0iI2IzODhmZiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTYiIGZvbnQtd2VpZ2h0PSJib2xkIj5EYXRhYmFzZSBMYXllciAoQ2FjaGUgJmFtcDsgSW5kZXgpPC90ZXh0PgogIDxyZWN0IHg9IjI1MCIgeT0iMzAwIiB3aWR0aD0iMzAwIiBoZWlnaHQ9IjYwIiBmaWxsPSIjMGEwMDIwIiBzdHJva2U9IiNiMzg4ZmYiIHN0cm9rZS13aWR0aD0iMiIgcng9IjUiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjMzNSIgZmlsbD0iI2IzODhmZiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTQiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlBvc3RncmVTUUwgKENLSUQgJmFtcDsgVGF4b25vbXkpPC90ZXh0PgogIAogIDwhLS0gU3luYyBsaW5lcyAtLT4KICA8cGF0aCBkPSJNIDY1NSAxNzAgTCA2NTUgMzMwIEwgNTYwIDMzMCIgc3Ryb2tlPSIjMDBmZjQxIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1kYXNoYXJyYXk9IjQsNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvdy1ncmVlbikiLz4KICA8dGV4dCB4PSI2NjUiIHk9IjI1MCIgZmlsbD0iIzAwZmY0MSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTIiPnN5bmNfa25vd2xlZGdlX2dyYXBoLnB5PC90ZXh0PgogIAogIDxkZWZzPgogICAgPG1hcmtlciBpZD0iYXJyb3ciIHZpZXdCb3g9IjAgMCAxMCAxMCIgcmVmWD0iOSIgcmVmWT0iNSIgbWFya2VyV2lkdGg9IjYiIG1hcmtlckhlaWdodD0iNiIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgICA8cGF0aCBkPSJNIDAgMCBMIDEwIDUgTCAwIDEwIHoiIGZpbGw9IiNmZmZmZmYiLz4KICAgIDwvbWFya2VyPgogICAgPG1hcmtlciBpZD0iYXJyb3ctZ3JlZW4iIHZpZXdCb3g9IjAgMCAxMCAxMCIgcmVmWD0iOSIgcmVmWT0iNSIgbWFya2VyV2lkdGg9IjYiIG1hcmtlckhlaWdodD0iNiIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgICA8cGF0aCBkPSJNIDAgMCBMIDEwIDUgTCAwIDEwIHoiIGZpbGw9IiMwMGZmNDEiLz4KICAgIDwvbWFya2VyPgogIDwvZGVmcz4KPC9zdmc+" alt="Diagram" style="display:block;width:100%;max-width:680px;height:auto;margin:1.5rem auto;">

## The Core Philosophy (L1)

The VKE is built on three foundational pillars:

1. **File-Over-App (The Truth)**: We reject opaque vector databases as the primary storage mechanism. Markdown files live in the filesystem. They are human-readable, auditable, and inherently portable. If the database drops, the knowledge survives intact.
2. **Database as Cache (The Speed)**: We don't discard databases; we repurpose them. PostgreSQL acts as a high-speed materialized view of the filesystem. It holds the canonical IDs, the semantic vectors, and the structural taxonomy, making retrieval instantaneous without holding the system hostage.
3. **Compound Intelligence (The Loop)**: Knowledge is never static. Autonomous agents operate in a continuous loop: ingesting raw data, compiling it into structured formats, linting it for contradictions against existing knowledge, and promoting it to the verified wiki.

## The Stack Summary (L2)

The stack is aggressively simple, relying on battle-tested technologies rather than trendy, unstable vector stores.

- **Storage & Indexing**: PostgreSQL + JSONB + `pgvector`. (Via our existing `pghmem` implementation).
- **Filesystem Vaults**: 
  - `vault/messy/` (The ingestion playground)
  - `vault/clean/wiki/` (The verified source of truth)
- **Orchestration Scripts**:
  - `compile_knowledge.py`: The LLM agent that transforms raw data into structured Markdown.
  - `lint_knowledge.py`: The Hermes-powered supervisor that checks for contradictions and enforces schema.
  - `sync_knowledge_graph.py`: The cron job that reads Markdown frontmatter and UPSERTs it into PostgreSQL.
- **Client Interface**: An MCP (Model Context Protocol) Server that surfaces this entire architecture as discrete tools to Claude, Cursor, and other LLMs.

<details>
<summary>📖 Deep Dive: The CKID Glue (L3)</summary>

The mechanism that prevents this hybrid system from falling apart is the **Canonical Knowledge ID (CKID)**. 

When raw data is ingested, it is assigned a CKID. When that data is compiled into a Markdown file, the CKID is stamped into its YAML frontmatter. When the sync script reads that Markdown file, it writes the CKID into PostgreSQL. 

Because the CKID is decoupled from the file path or the database row ID, you can rename the Markdown file, move it to a different directory, or completely rebuild the PostgreSQL database from scratch, and the referential integrity of the entire knowledge graph remains 100% intact.

</details>

---

*This is Post 4 of 4 in the **Verified Knowledge Engine** series.*

- [Post 1: Researching AI Memory: Methodology & The Stack](/posts/vke-series-pt1-methodology/)
- [Post 2: Analysis & Synthesis: Bridging Memory Paradigms](/posts/vke-series-pt2-synthesis/)
- [Post 3: The Verified Knowledge Engine (VKE) Architecture](/posts/vke-series-pt3-architecture/)
- **Post 4: The Verified Knowledge Engine: Core Concepts & Stack Summary** *(you are here)*
