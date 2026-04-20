---
pubDatetime: 2026-04-09T15:44:18Z
title: "Researching AI Memory: Methodology & The Stack"
postSlug: "vke-series-pt1-methodology"
description: "Researching AI Memory: Methodology & The Stack"
tags:
  - vke
  - architecture
  - memory-systems
  - research
  - series
---

# Researching AI Memory: Methodology & The Stack

> **TL;DR**: We bypassed standard RAG vector aggregation in favor of empirical code analysis to design our memory architecture. Here is how we researched MemPalace, assessed the Karpathy Pattern, and validated our PostgreSQL foundation.

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MDAgMzAwIj4KICA8cmVjdCB3aWR0aD0iODAwIiBoZWlnaHQ9IjMwMCIgZmlsbD0iIzBhMDAyMCIgcng9IjEwIi8+CiAgPHJlY3QgeD0iNTAiIHk9IjEwMCIgd2lkdGg9IjE1MCIgaGVpZ2h0PSI4MCIgcng9IjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzAwZmZmZiIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgPHRleHQgeD0iMTI1IiB5PSIxNDUiIGZpbGw9IiMwMGZmZmYiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjE2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5FbXBpcmljYWwgQXVkaXQ8L3RleHQ+CiAgPHJlY3QgeD0iMzI1IiB5PSIxMDAiIHdpZHRoPSIxNTAiIGhlaWdodD0iODAiIHJ4PSI1IiBmaWxsPSJub25lIiBzdHJva2U9IiNmZjAwZmYiIHN0cm9rZS13aWR0aD0iMiIvPgogIDx0ZXh0IHg9IjQwMCIgeT0iMTQ1IiBmaWxsPSIjZmYwMGZmIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxNiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+Q3Jvc3MtUmVmZXJlbmNlPC90ZXh0PgogIDxyZWN0IHg9IjYwMCIgeT0iMTAwIiB3aWR0aD0iMTUwIiBoZWlnaHQ9IjgwIiByeD0iNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMDBmZjQxIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8dGV4dCB4PSI2NzUiIHk9IjE0NSIgZmlsbD0iIzAwZmY0MSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlN5bnRoZXNpczwvdGV4dD4KICA8cGF0aCBkPSJNIDIxMCAxNDAgTCAzMTUgMTQwIiBzdHJva2U9IiMwMGJmYTUiIHN0cm9rZS13aWR0aD0iMiIgbWFya2VyLWVuZD0idXJsKCNhcnJvdykiLz4KICA8cGF0aCBkPSJNIDQ4NSAxNDAgTCA1OTAgMTQwIiBzdHJva2U9IiMwMGJmYTUiIHN0cm9rZS13aWR0aD0iMiIgbWFya2VyLWVuZD0idXJsKCNhcnJvdykiLz4KICA8ZGVmcz4KICAgIDxtYXJrZXIgaWQ9ImFycm93IiB2aWV3Qm94PSIwIDAgMTAgMTAiIHJlZlg9IjkiIHJlZlk9IjUiIG1hcmtlcldpZHRoPSI2IiBtYXJrZXJIZWlnaHQ9IjYiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgICAgPHBhdGggZD0iTSAwIDAgTCAxMCA1IEwgMCAxMCB6IiBmaWxsPSIjMDBiZmE1Ii8+CiAgICA8L21hcmtlcj4KICA8L2RlZnM+Cjwvc3ZnPg==" alt="Diagram" style="display:block;width:100%;max-width:680px;height:auto;margin:1.5rem auto;">

## The Research Methodology (L1)

When approaching a major architectural decision for AI memory, reading marketing `README.md` files is insufficient. We utilized a 3-step empirical pipeline:

1. **Empirical Audit**: Deep inspection of GitHub repositories, focusing specifically on open issues and failure modes.
2. **Local Baselining**: Auditing our existing PostgreSQL (`pghmem`) stack to understand our current volume and capabilities.
3. **Cross-Referencing**: Validating concepts against external, proven paradigms (like Andrej Karpathy's `autoresearch` project).

## Why We Bypassed eRAG for This Task (L2)

Our system includes `eRAG` (Ephemeral RAG v2), a tool designed to scrape scattered documents and build NetworkX concept graphs. 

We explicitly **chose not to use eRAG** for this task. Why?
- **Task Nature**: This was a structural engineering task ("How do we merge SQL schemas with JSONB taxonomies?"), not a broad topic exploration.
- **Precision over Recall**: We needed exact lines of code, specific GitHub issue numbers, and concrete architectural constraints. RAG aggregation often blurs exact technical nuances by chunking.

*When would we use eRAG?* If the task was a "Landscape Deep Dive" comparing 15 different memory providers (Mem0, Zep, LangMem, etc.), eRAG would be mandatory to synthesize the scattered documentation.

<details>
<summary>📖 Deep Dive: Memory Techniques Used (L3)</summary>

During this session, we heavily relied on our internal `pghmem` (PostgreSQL) stack. 
- **Session Memory**: Using `capture_conversation.py` to record key decisions mid-research.
- **Context Cross-Referencing**: We executed `pghmem search "Karpathy"` to retrieve prior context on the Karpathy Pattern, linking historical knowledge to active research.

</details>

---

*This is Post 1 of 4 in the **Verified Knowledge Engine** series.*

- **Post 1: Researching AI Memory: Methodology & The Stack** *(you are here)*
- [Post 2: Analysis & Synthesis: Bridging Memory Paradigms](/posts/vke-series-pt2-synthesis/)
- [Post 3: The Verified Knowledge Engine (VKE) Architecture](/posts/vke-series-pt3-architecture/)
- [Post 4: The Verified Knowledge Engine: Core Concepts & Stack Summary](/posts/vke-series-pt4-core-concepts/)
