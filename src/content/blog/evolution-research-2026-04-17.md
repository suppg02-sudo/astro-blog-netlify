---
pubDatetime: 2026-04-17T09:00:11Z
title: "Evolution Research Report — 17 April 2026"
postSlug: "evolution-research-2026-04-17"
description: "Evolution Research Report — 17 April 2026"
tags:
  - evolution
  - research
  - daily-report
---

# Evolution Research Report — 17 April 2026

## Project State

| Metric | Value |
|--------|-------|
| **Status** | active |
| **Priority** | high |
| **Phase** | complete |
| **Roadmap Progress** | 11/15 (73%) |
| **Context Files** | 27 |
| **Tracked Webpages** | 5 |
| **Related Blog Posts** | 10 |

### Roadmap Progress

`██████████████████████████████████████████████████` 73%

**Next Action**: Document chat architecture, then evaluate OpenRAG vs file-based knowledge

### Key Decisions

- 2026-04-06: Deployed Karpathy Tracker — daily cron (7AM), 13 repos, blog auto-publish, evolution cross-ref, coverage suggestions — Track Karpathy work, map to evolution project, identify coverage gaps, automate blog + memory + Telegram
- 2026-04-08: Domain name brainplane.ai identified as available — .com taken — Fits ecosystem brand for AI/agent platform. Deferred item DO-053 created.
- 2026-04-10: Schema alignment session — 9/9 factories aligned to full DNA (identity, factory, audit, agentInterface). 5/5 DNA score for all. — Aspirational schema design (Seed→Factory→Instance with $defs) merged into live PostgreSQL. auto_audit.py, factory_bubbler.py, agent_prompt_builder.py created.
- 2026-04-10: Evolution Engine audited and reconnected — 7 critical bugs fixed, LLM switched to GLM-5.1/Zhipu API, cron registered, CLI built — Engine was a data lake (captured but never improved). Now a data loop with cross-domain bridges. Prompts 2→46, Menu proposals 0→20.
- 2026-04-10: agentInterface vs agentInterfaces vs agent_interface key mismatch fixed across all 9 factories — 5 factories used snake_case, 4 used camelCase, adapter only checked one variant. Added 3-key fallback chain. DB normalized. DO-064 resolved.
- 2026-04-11: Factory prompt wiring deployed — wire_factory_prompts.py maps 9 factory schemas to 4 agent configs — agent_prompt_builder generated prompts nobody read. Solution: inject factory DNA context directly into agent config files via managed sections. Cron keeps them synced. Cross-domain bridges now have data to work with (decisions, attention, intent seeded).
- 2026-04-11: Triple-loop self-improvement architecture deployed — usage_signals hub + tiered auto-approve + Kestra crons — All 3 feedback loops were broken at the approval stage (703 captured, 3 approved). Root cause: no auto-approve mechanism. Fix: usage_signals PostgreSQL table as central hub, auto_approve.py with LOW/MEDIUM/HIGH risk tiers, Kestra daily + weekly crons. Domain-based classification used since quality_scores are NULL across all improved artefacts.
- 2026-04-11: Knowledge closing + experience wiring completed — cross-ref lint, research-factory signals, subagent tracking, experience compounding — Closed the two remaining roadmap workstreams. crossref_lint.py found 43 issues (4 broken links, 12 NextExplorer, 27 orphans). research-factory now records to usage_signals (tested). Subagent tracking uses dual-track pattern (orchestrator + self-report). Weekly experience compounding Kestra workflow aggregates trends.

### Context Notes

This project tracks the evolution of:
- Factories: skill-factory (L4), project-factory (L2), menu-factory (L3), research-factory (new) - Schemas: skill-schema.json, project-schema.yaml, research-schema.yaml - Services: Directus, Reflex, NextExplorer, eRAG, OpenRAG - Control plane: adapter registry, globals, quality gates - Agentic frameworks: hub & spoke, progressive disclosure, recursiveness - Core principles: schemas, progressive disclosure, recursiveness, creativity, advice, context persisten...

## Comparable Ecosystem Projects

### Tracked Projects

| Project | Stars | Language | Last Push |
|---------|-------|----------|----------|
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | 144,708 | TypeScript | 2026-04-17 |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 133,846 | Python | 2026-04-17 |
| [cline/cline](https://github.com/cline/cline) | 60,373 | TypeScript | 2026-04-17 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 49,078 | Python | 2026-04-16 |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | 43,478 | Python | 2026-04-09 |
| [continuedev/continue](https://github.com/continuedev/continue) | 32,614 | TypeScript | 2026-04-17 |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | 27,722 | C# | 2026-04-17 |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 21,487 | Python | 2026-04-17 |

### Discovered Projects

| Project | Stars | Description |
|---------|-------|-------------|
| [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 11,372 | Turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, |
| [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | 2,437 | World's first open-source, agentic video production system. 12 pipelines, 52 too |
| [wangziqi06/724-office](https://github.com/wangziqi06/724-office) | 1,093 | 7/24 Office — Self-evolving AI Agent system. 36 tools, 10,000 lines pure Python, |
| [pinchbench/skill](https://github.com/pinchbench/skill) | 1,011 | PinchBench is a benchmarking system for evaluating LLM models as OpenClaw coding |
| [coleam00/claude-memory-compiler](https://github.com/coleam00/claude-memory-compiler) | 768 | Give Claude Code a memory that evolves with your codebase. Hooks automatically c |
| [xoai/sage-wiki](https://github.com/xoai/sage-wiki) | 410 | An LLM-compiled personal knowledge base.  Drop in your papers, articles, and not |
| [swarmclawai/swarmvault](https://github.com/swarmclawai/swarmvault) | 220 | Inspired by Karpathy's LLM Wiki. Local-first RAG knowledge base compiler with MC |
| [Agnuxo1/OpenCLAW-Autonomous-Multi-Agent-Scientific-Research-Platform](https://github.com/Agnuxo1/OpenCLAW-Autonomous-Multi-Agent-Scientific-Research-Platform) | 9 | OpenCLAW is an ambitious open-source project that transforms the OpenClaw person |
| [ShackStudios/davidkimai-context-engineering](https://github.com/ShackStudios/davidkimai-context-engineering) | 7 | Meta-recursive context engineering framework for building self-improving AI agen |
| [NoManNayeem/REFLEX](https://github.com/NoManNayeem/REFLEX) | 5 | A functional proof-of-concept demonstrating a self-improving AI agent using **Re |

### Community Discussions

- [What is Agentic AI? | IBM](https://www.ibm.com/think/topics/agentic-ai)
  - <strong>Through reinforcement learning or self-supervised learning, the AI refines its strategies ov
- [GitHub - masamasa59/ai-agent-papers: A collection of AI Agents papers (Updated b](https://github.com/masamasa59/ai-agent-papers)
  - &quot;Strategic Self-Improvement for Competitive Agents in AI Labour Markets&quot; [paper] &quot;Gui
- [LangChain: Observe, Evaluate, and Deploy Reliable AI Agents](https://www.langchain.com/)
  - <strong>Turn any question or task into a recurring agent that improves with feedback and acts autono
- [GitHub - ussumant/llm-wiki-compiler: Claude Code plugin that compiles markdown k](https://github.com/ussumant/llm-wiki-compiler)
  - <strong>A Claude Code plugin that compiles knowledge into a topic-based wiki — from scattered markdo
- [GitHub - atomicmemory/llm-wiki-compiler: The knowledge compiler. Raw sources in,](https://github.com/atomicmemory/llm-wiki-compiler)
  - The knowledge compiler. Raw sources in, interlinked wiki out. Inspired by Karpathy&#x27;s LLM Wiki p
- [GitHub - swarmclawai/swarmvault: Inspired by Karpathy's LLM Wiki. Local-first RA](https://github.com/swarmclawai/swarmvault)
  - Inspired by Karpathy&#x27;s LLM Wiki. Local-first RAG knowledge base compiler with MCP server (Claud

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
| Community Discussions Found | 6 |
| Evolution Decisions Tracked | 20 |
| Roadmap Completion | 73% |

---

*Report generated: 2026-04-17 09:00 UTC*
*Sources: GitHub API + Brave Search API + evolution.yaml*
