---
pubDatetime: 2026-04-06T19:00:00Z
title: "Deep Analysis: Research & eRAG Skills — Overlap, Integration & Future Work"
postSlug: "deep-analysis-research-erag-skills-overlap-integration-future-work"
description: "Deep Analysis: Research & eRAG Skills — Overlap, Integration & Future Work"
tags:
  - skills
  - rag
  - integration
  - erag
  - architecture
  - analysis
  - research
---

# Deep Analysis: Research & eRAG Skills — Overlap, Integration & Future Work

A deep architectural analysis of two complementary OpenCode skills: the **research** skill (methodology and discovery) and **eRAG** (persistent knowledge infrastructure). They overlap in 5 critical areas but operate as isolated silos. Here's what to fix, what to merge, and what to build next.

---

## The Two Skills at a Glance

**Research Skill** — Enterprise-grade research methodology. Provides depth levels (glance → comprehensive), GRADE evidence ratings, bias detection, quality gates, web search providers (Tavily, Firecrawl, Serper), and blog/memory output pipelines. Ships its own ephemeral RAG scratchpad using ChromaDB.

**eRAG v2** — Persistent research knowledge store. PostgreSQL + pgvector for hybrid search (vector cosine + PostgreSQL FTS + RRF fusion), NetworkX for graph operations, Jina AI embeddings, entity/fact extraction (regex + optional LLM), living documents, and agent-driven scratchpad orchestration. 103/103 tests passing.

## The Problem: Isolated Silos With 5 Critical Overlaps

### 1. Competing Vector Databases

Research ships its own embedded ChromaDB (~200MB in `.venv/`) with SQLite FTS5 fallback. Data goes to `/tmp/` and dies on reboot. Meanwhile, eRAG already runs on the same PostgreSQL instance with pgvector and IVFFlat indexing.

**Verdict**: Research's `EphemeralRAG` class is the v1 prototype that eRAG was designed to replace. It should be deprecated.

### 2. Same Graph Library, Different Quality

Both use NetworkX with GML persistence. But Research's entity extraction is literally `words[0]` and `words[10]` — splitting text on whitespace. eRAG has typed regex patterns for TECHNOLOGY, PERSON_ORG, URL, EMAIL, COMMAND, PORT, LICENSE plus relational fact extraction (uses, provides, built_with, connects_to, requires).

### 3. Complementary Search Strengths, Not Connected

- **Research**: Discovery-oriented — can find new sources via web search providers
- **eRAG**: Retrieval-oriented — hybrid search across already-ingested data

These are **complementary, not competing**. Neither leverages the other.

### 4. Duplicate Synthesis/Output

Research has templates (`research-plan.md`, `research-summary.md`). eRAG has living documents with LLM synthesis, entity knowledge graphs, and confidence tables. Different formats, overlapping purpose.

### 5. Quality Systems That Don't Talk

eRAG has confidence tiers (raw → verified → promoted). Research has GRADE ratings (A/B/C/D). They should map directly:

| eRAG Tier | Research GRADE | Meaning |
|---|---|---|
| raw | D | Unverified, single source |
| verified | B | Cross-referenced |
| promoted | A | Multiple high-quality sources agree |

Neither system implements this mapping. Research defines GRADE in config but has no implementation code.

---

## The Capability Matrix

| Capability | Research | eRAG | Winner |
|---|---|---|---|
| Vector Search | ChromaDB (deprecated) | pgvector + FTS + RRF | **eRAG** |
| Web Discovery | Tavily/Firecrawl/Serper | None | **Research** |
| Entity Extraction | Mock (whitespace split) | Regex + optional LLM | **eRAG** |
| Graph Operations | Mock only | Louvain, centrality, paths | **eRAG** |
| Persistence | Ephemeral (/tmp) | PostgreSQL (permanent) | **eRAG** |
| Methodology | Depth levels, GRADE, bias | Query expansion, gaps | **Research** |
| Test Coverage | Zero tests | 103/103 passing | **eRAG** |
| Embeddings | ChromaDB default | Jina AI v3 (768d) | **eRAG** |

---

## Proposed Architecture: Unified Research Engine

The fix is a unified pipeline where Research provides **methodology** and **discovery**, while eRAG provides **infrastructure** and **persistence**:

```
DISCOVER (Research) → INGEST (eRAG) → STORE (eRAG pgvector)
    → QUALITY (Research GRADE + eRAG confidence tiers)
    → SYNTHESIZE (eRAG living docs + Research templates)
    → OUTPUT (Blog / Memory / Telegram)
```

This turns two L3 skills into one L4 research engine.

---

## Priority Fixes

### Do Today (Low Effort, High Impact)

1. **Delete `.venv/` in research skill** — saves 200MB, nothing depends on it at runtime
2. **Fix syntax error in `quality_gate_integration.py:18`** — invalid Python: `content_type: str = "news", " research"`
3. **Deprecate `EphemeralRAG`** — route Research through eRAG's Scratchpad instead

### Do This Week (Medium Effort)

4. **Add web search adapters to eRAG** — wrap Tavily/Firecrawl as source adapters so eRAG can discover, not just ingest
5. **Map confidence tiers to GRADE** — add a GRADE field to eRAG's confidence assessment
6. **LLM entity extraction as default** — upgrade from regex to the LLM extraction that already exists but is opt-in
7. **pghmem sync** — auto-push eRAG findings to the main memory system

### Do This Month (Higher Effort)

8. **Re-ranking beyond RRF** — add cross-encoder or Cohere re-ranker for research-grade output
9. **Automated verification pipeline** — promote `raw` → `verified` tier via automated cross-referencing
10. **Temporal facts** — add validity windows (like Graphiti) to the fact table so we know when facts became true or were superseded
11. **Unified CLI** — single `research` command that delegates storage to eRAG

---

## Code-Level Issues Found

**Research Skill:**
- `quality_gate_integration.py:18` — Syntax error, invalid Python
- `ephemeral_rag_research.py:118-126` — Mock entity extraction unusable in production
- Zero test coverage
- 200MB+ `.venv/` embedded in skill directory
- GRADE/bias detection defined in config but no implementation exists

**eRAG Skill:**
- `scratchpad.py:155-178` — `status()` always passes empty `strategies_covered`, making coverage estimates inaccurate
- `llm_client.py` agent mode calls `opencode run` as subprocess — slow (120s+ timeout) and brittle
- No web search capability — can ingest URLs but can't discover new ones
- No cross-project search

---

## Revenue Potential

Per the TELOS directive, the unified research engine has clear monetization paths:

| Path | Description | Revenue Model |
|---|---|---|
| Research-as-a-Service API | Expose unified pipeline as REST API | Per-query pricing |
| Automated Research Reports | Deep research → blog post pipeline | Content marketing, SEO |
| Consulting Reports | White-label research output | One-off sales |
| Knowledge Graph Products | Entity/fact graphs for specific domains | Data licensing |

The highest-ROI path is **closing the loop**: Research discovers sources → eRAG stores and analyzes → Blog post publishes → Traffic → Revenue. This pipeline exists in pieces but isn't connected end-to-end.

---

## Key Takeaways

1. **Research is methodology without infrastructure; eRAG is infrastructure without methodology.** Combined, they're a complete research engine.
2. **Five critical overlaps** mean duplicated effort and inconsistent quality.
3. **The single highest-impact fix** is deprecating Research's `EphemeralRAG` and routing everything through eRAG's Scratchpad.
4. **Both skills are L3 alone; unified they become L4.**
5. **The revenue loop** (discover → store → synthesize → publish) is 80% built but not connected.

---

*Analysis performed on 2026-04-06. Both skills are actively maintained. eRAG v2 has 103/103 tests passing. Research skill metadata reports L4 maturity but lacks test coverage to substantiate that claim.*
