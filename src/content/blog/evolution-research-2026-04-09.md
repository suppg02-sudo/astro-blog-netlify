---
pubDatetime: 2026-04-09T09:00:05Z
title: "Evolution Research Report — 09 April 2026"
postSlug: "evolution-research-2026-04-09"
description: "Evolution Research Report — 09 April 2026"
tags:
  - evolution
  - research
  - daily-report
---

# Evolution Research Report — 09 April 2026

## Project State

| Metric | Value |
|--------|-------|
| **Status** | active |
| **Priority** | high |
| **Phase** | complete |
| **Roadmap Progress** | 6/12 (50%) |
| **Context Files** | 21 |
| **Tracked Webpages** | 3 |
| **Related Blog Posts** | 6 |

### Roadmap Progress

`██████████████████████████████████████████████████` 50%

**Next Action**: Acquire brainplane.ai domain and update evolution tracking

### Open Checklist Items

- [interactive-research] Test end-to-end with >k on live URL
- [interactive-research] Document in SKILL.md or trigger-words.md

### Key Decisions

- 2026-04-04: Kestra owns ALL automation/orchestration. Directus is purely data + CMS (no Flows). Two systems, two clear owners.
- 2026-04-05: Karpathy Pattern analysis complete — 55% alignment. 4 gaps identified (raw/ staging, compiler, contamination boundary, backlinks). 7 recom
- 2026-04-05: Karpathy recommendations triaged — P1 (raw/, Bible cron, lint), P2 (compiler, contamination) INTEGRATED. P3 (ephemeral wiki, OpenRAG eval)
- 2026-04-05: Knowledge compiler deployed as systemd service (compiler_watcher.py). Polls Directus knowledge_queue. 2 items processed successfully.
- 2026-04-05: Weekly OpenCode Bible deployed (weekly_bible.py). Cron Sunday 9am UTC. First report generated.
- 2026-04-06: Deployed Kestra orchestration layer — Standalone Docker deploy with dedicated PostgreSQL. Port 8094 (UI), 8095 (internal). Basic auth enabled. Unblocks experience-layer, knowledge-base-evolution, cross-reference lint.
- 2026-04-06: Deployed Karpathy Tracker — daily cron (7AM), 13 repos, blog auto-publish, evolution cross-ref, coverage suggestions — Track Karpathy work, map to evolution project, identify coverage gaps, automate blog + memory + Telegram
- 2026-04-08: Domain name brainplane.ai identified as available — .com taken — Fits ecosystem brand for AI/agent platform. Deferred item DO-053 created.

### Context Notes

This project tracks the evolution of:
- Factories: skill-factory (L4), project-factory (L2), menu-factory (L3), research-factory (new) - Schemas: skill-schema.json, project-schema.yaml, research-schema.yaml - Services: Directus, Reflex, NextExplorer, eRAG, OpenRAG - Control plane: adapter registry, globals, quality gates - Agentic frameworks: hub & spoke, progressive disclosure, recursiveness - Core principles: schemas, progressive disclosure, recursiveness, creativity, advice, context persisten...

## Comparable Ecosystem Projects

### Tracked Projects

| Project | Stars | Language | Last Push |
|---------|-------|----------|----------|
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | 140,120 | TypeScript | 2026-04-09 |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 132,885 | Python | 2026-04-09 |
| [cline/cline](https://github.com/cline/cline) | 60,056 | TypeScript | 2026-04-09 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 48,411 | Python | 2026-04-09 |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | 43,047 | Python | 2026-04-09 |
| [continuedev/continue](https://github.com/continuedev/continue) | 32,388 | TypeScript | 2026-04-09 |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | 27,672 | C# | 2026-04-08 |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 20,663 | Python | 2026-04-09 |

### Discovered Projects

| Project | Stars | Description |
|---------|-------|-------------|
| [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 8,457 | Turn Claude Code into a full game dev studio — 48 AI agents, 36 workflow skills, |
| [neuron-core/neuron-ai](https://github.com/neuron-core/neuron-ai) | 1,827 | The PHP Agentic Framework to build production-ready AI driven applications. Conn |
| [pinchbench/skill](https://github.com/pinchbench/skill) | 964 | PinchBench is a benchmarking system for evaluating LLM models as OpenClaw coding |
| [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | 938 | World's first open-source, agentic video production system. 11 pipelines, 49 too |
| [coleam00/claude-memory-compiler](https://github.com/coleam00/claude-memory-compiler) | 382 | Give Claude Code a memory that evolves with your codebase. Hooks automatically c |
| [xoai/sage-wiki](https://github.com/xoai/sage-wiki) | 301 | An LLM-compiled personal knowledge base.  Drop in your papers, articles, and not |
| [ussumant/llm-wiki-compiler](https://github.com/ussumant/llm-wiki-compiler) | 133 | Claude Code plugin that compiles markdown knowledge files into a topic-based wik |
| [Agnuxo1/OpenCLAW-Autonomous-Multi-Agent-Scientific-Research-Platform](https://github.com/Agnuxo1/OpenCLAW-Autonomous-Multi-Agent-Scientific-Research-Platform) | 9 | OpenCLAW is an ambitious open-source project that transforms the OpenClaw person |
| [ShackStudios/davidkimai-context-engineering](https://github.com/ShackStudios/davidkimai-context-engineering) | 7 | Meta-recursive context engineering framework for building self-improving AI agen |
| [NoManNayeem/REFLEX](https://github.com/NoManNayeem/REFLEX) | 5 | A functional proof-of-concept demonstrating a self-improving AI agent using **Re |

## Evolution Comparison Analysis

### How the OpenCode Evolution Compares

The evolution project encompasses several domains that parallel major open-source efforts:

1. **Skill System** — Comparable to Semantic Kernel plugins and LangChain tools. Our schema-driven approach with progressive disclosure is unique in the ecosystem.

2. **Knowledge Compiler** (raw/compiled/wiki/) — Mirrors Karpathy's LLM knowledge base pattern. The contamination mitigation protocol is novel — most projects don't separate messy/clean knowledge zones.

3. **Factory Pattern** (skill/project/menu/research) — No direct equivalent. Most AI tools use monolithic configs. Our hub-and-spoke with schema validation is distinctive.

4. **Memory System** — pgvector + pghmem is comparable to LangChain's memory modules but with PostgreSQL-native approach. OmniMemory's selective ingestion (+44% retrieval) validates our direction.

5. **Autonomous Research** — The research-factory with adapter patterns is similar to CrewAI/AutoGen multi-agent systems but with YAML-driven configuration and quality gates.

### Competitive Advantages

- Schema-validated, deterministic configuration (7B-14B model compatible)
- Progressive disclosure (L0-L4) for information density management
- Factory meta-pattern enabling self-improvement loops
- Karpathy-pattern knowledge compiler with contamination boundaries

### Gaps vs Ecosystem

- No visual IDE/dashboard for skill management (Zed, Cursor have this)
- Kestra orchestration not yet deployed (blocks compound loops)
- Experience layer not yet tracking agent performance data
- No public API or plugin marketplace (Semantic Kernel, LangChain have these)

---

## Research Metrics

| Metric | Value |
|--------|-------|
| Tracked Repos Analysed | 8 |
| New Projects Discovered | 10 |
| Community Discussions Found | 0 |
| Evolution Decisions Tracked | 14 |
| Roadmap Completion | 50% |

---

*Report generated: 2026-04-09 09:00 UTC*
*Sources: GitHub API + Brave Search API + evolution.yaml*
