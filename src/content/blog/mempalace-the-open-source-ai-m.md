---
pubDatetime: 2026-04-09T12:00:00Z
title: "MemPalace: The Open-Source AI Memory System That Stores Everything"
postSlug: "mempalace-the-open-source-ai-m"
description: "MemPalace: The Open-Source AI Memory System That Stores Everything"
tags:
  - others
---

What if your AI could remember every conversation you've ever had — every debugging session, every architecture decision, every "we tried X and it failed because Y" — without sending a single byte to the cloud? MemPalace, a new open-source project from Milla Jovovich and Ben Sigman, attempts exactly that. And it just scored the highest LongMemEval result ever published: 96.6% recall at zero API cost.

## The Problem MemPalace Solves

Decisions happen in AI conversations now. Not in docs, not in Jira — in Claude, ChatGPT, and Copilot sessions that evaporate the moment you close the window. Six months of daily AI usage generates roughly 19.5 million tokens of context that simply disappears.

The existing approaches are inadequate. Paste everything? Won't fit any context window. LLM summaries? They strip away the reasoning and context that made the original conversation valuable. MemPalace takes a different path: store everything verbatim, then build a navigable structure that makes it findable.

## The Palace Metaphor

The system borrows from the ancient Greek method of loci — the memory palace technique where orators placed ideas in rooms of an imaginary building. In MemPalace, your conversations are organized into:

- **Wings** — dedicated to a person, project, or topic
- **Rooms** — specific subjects within a wing (auth, billing, deploy)
- **Halls** — connections between related rooms in the same wing
- **Tunnels** — cross-wing connections that link the same topic across different domains
- **Closets** — summaries that point back to original content
- **Drawers** — the raw verbatim files, never summarized

This structure delivers a measurable 34% retrieval improvement over flat search. When you search within a specific wing and room, recall jumps from 60.9% to 94.8%. The structure isn't cosmetic — it's the product.

## How It Works Under the Hood

MemPalace runs entirely on your machine using ChromaDB for vector storage and SQLite for its knowledge graph. The core pipeline:

1. **Mine** your data — project files, conversation exports (Claude, ChatGPT, Slack), or general documents
2. **Store** everything verbatim in ChromaDB with wing/room/hall metadata
3. **Search** semantically with structural filters (wing, room, hall)
4. **Retrieve** original exchanges, not summaries

The 96.6% LongMemEval score comes from raw verbatim mode — no LLM summarization, no extraction step, no cloud dependency. The system keeps every word and relies on semantic search to find what matters.

## The Knowledge Graph

Beyond search, MemPalace includes a temporal entity-relationship graph built on SQLite. It tracks facts with validity windows — when something stops being true, you invalidate it, and historical queries still work:

```python
kg.add_triple("Kai", "works_on", "Orion", valid_from="2025-06-01")
kg.add_triple("Maya", "assigned_to", "auth-migration", valid_from="2026-01-15")
kg.invalidate("Kai", "works_on", "Orion", ended="2026-03-01")
```

This gives you a temporal query capability similar to Zep's Graphiti, but local and free instead of requiring Neo4j and a cloud subscription.

## AAAK: An Experimental Compression Layer

MemPalace includes AAAK, a lossy abbreviation dialect that packs repeated entities into fewer tokens. It's designed for scenarios where the same team members and projects appear across thousands of sessions. Here's the honest assessment: AAAK currently regresses LongMemEval performance from 96.6% to 84.2% at small scales. The headline number is raw mode, not AAAK. The compression layer is experimental and being actively iterated on.

## MCP Integration: 19 Tools for Your AI

MemPalace exposes 19 MCP tools that your AI can use directly — palace navigation, semantic search, knowledge graph queries, agent diaries, and auto-save hooks. With Claude Code, installation is a single command:

```bash
claude plugin marketplace add milla-jovovich/mempalace
claude plugin install --scope user mempalace
```

Your AI learns the system automatically from the `mempalace_status` response. No manual configuration needed.

## What Makes This Different

The key insight is philosophical: don't let an AI decide what's worth remembering. Other systems extract "user prefers Postgres" and throw away the conversation where you explained why. MemPalace keeps the entire exchange and relies on semantic search to surface it when needed.

At $0 recurring cost, running entirely on local hardware, with the highest published LongMemEval score — MemPalace is a compelling option for developers who want AI memory without vendor lock-in or data leaving their machine.

## Benchmark Comparison

| System | LongMemEval R@5 | API Required | Cost |
|--------|----------------|--------------|------|
| MemPalace (hybrid) | 100% | Optional | Free |
| MemPalace (raw) | 96.6% | None | Free |
| Mastra | 94.87% | Yes (GPT) | API costs |
| Mem0 | ~85% | Yes | $19–249/mo |
| Zep | ~85% | Yes | $25/mo+ |

The raw mode score is particularly notable: no API key, no cloud, no LLM at any stage of the retrieval pipeline. Just ChromaDB and good structure.

## Getting Started

```bash
pip install mempalace
mempalace init ~/projects/myapp
mempalace mine ~/projects/myapp
mempalace search "why did we switch to GraphQL"
```

Three commands. Local only. MIT licensed. The project is at v3.0.14 with active development and a responsive team that published transparent corrections when the community caught issues in their initial claims.

**Tags**: ai, memory, chromadb, mcp, open-source, local-first, vector-database, longmemeval
**Categories**: AI Tools, Open Source Spotlight