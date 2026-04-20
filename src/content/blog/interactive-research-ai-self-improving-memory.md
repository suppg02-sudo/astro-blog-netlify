---
pubDatetime: 2026-04-05T14:30:00Z
title: "Interactive Research: Building AI's Self-Improving Memory Pipeline"
postSlug: "interactive-research-ai-self-improving-memory"
description: "I built a stage-gated interactive research pipeline for OpenCode — inspired by HERA's self-learning multi-agent RAG framework. Instead of dumping links and getting static analysis back, the system now"
tags:
  - others
---

# Interactive Research: Building AI's Self-Improving Memory Pipeline

> **TL;DR**: I built a stage-gated interactive research pipeline for OpenCode — inspired by HERA's self-learning multi-agent RAG framework. Instead of dumping links and getting static analysis back, the system now asks clarifying questions, recommends approaches based on past experience, and learns from every interaction. The research gets smarter each time you use it.

---

## The Problem

I hit a pattern matching problem. Every time I ran a research task — whether it was analysing Karpathy's LLM knowledge base, OmniMemory's autonomous research patterns, or GLM-5's agentic systems — I'd get the same output: a wiki article indexed in eRAG. Useful, but static. No learning between runs. No steering. No feedback loop.

The existing `>k` pipeline works like this:

🔴 **You paste URL** → 🟠 **LLM processes** → 🔵 **Wiki article output**

Linear. Stateless. Every run starts from zero.

## The Inspiration: HERA's Self-Learning Pattern

I watched a video from Discover AI about **HERA** — a hierarchical framework that jointly evolves multi-agent orchestration and role-specific agent prompts through reward-guided sampling. The core insight: **"words instead of weights"** — instead of optimizing model weights, you optimize prompts, agent topologies, and orchestration patterns through experience accumulation.

HERA maintains an experience library. Every query routes through it. Past successes influence future routing. The system learns from itself.

That's when it clicked: my research pipeline needs the same pattern. Not autonomous auto-research, but **interactive research** — where I steer, the AI asks questions, and every run teaches it what works.

---

## The Architecture: Stage-Gated Interactive Loop

```
🔴 INTAKE → 🟠 CLARIFY → 🟡 PRIORITISE → 🟢 EXECUTE → 🔵 COMPILE
```

Five stages. At each gate, the system asks clarifying questions AND presents recommended options. You choose direction. It executes. Results feed back into the experience layer.

### Stage 1: INTAKE

You provide a URL, file, or reference. The system ingests into `raw/` — same as before. But now it also searches the experience layer for similar past research and shows what worked.

> "✅ Ingested: HERA Video → raw/hera-multi-agent-rag.md. Found 2 similar past research instances."

### Stage 2: CLARIFY

The system reads your content, identifies relevance to your projects, and asks two questions:

1. **Intent** — What's your primary goal? (Understand concept / Find implementation / Evaluate for integration / Just add to knowledge)
2. **Project Link** — Should this tie to an existing project? (Evolution / Bot / Lockdown / Standalone / New)

Then it recommends an approach:

> "Found 2 similar past research instances. Recommended: web-fetch + evolve agent. Past success rate: 90%. Typically produces 2 wiki articles."

### Stage 3: PRIORITISE

Early compiled analysis presented. You steer focus areas, choose techniques (full Karpathy pipeline → quick compile → deep eRAG research → blog output).

### Stage 4: EXECUTE

Deep research with checkpoints. After significant findings:

> "I found [X] — this maps to autonomous-loops. Want to: Dive deeper / Continue / Redirect / Start compiling"

### Stage 5: COMPILE

Wiki article generated, indexed in eRAG, evolution project updated, experience logged. Final question: publish as blog post or just wiki?

---

## The Experience Layer: Where Learning Happens

This is the connective tissue. Every research run logs to `~/.config/opencode/experience/`:

```yaml
experience:
  id: "exp-20260405-002"
  timestamp: "2026-04-05T14:30:00Z"
  type: "research"
  query: "HERA Multi-Agent RAG — YouTube analysis"
  context:
    project: "evolution"
    adapters: ["youtube", "yt-dlp"]
    agents: ["general"]
  outcome:
    status: "success"
    score: 0.90
    outputs: ["wiki_article", "compiled_analysis", "raw_input"]
  routing_intelligence:
    best_adapters: ["youtube", "yt-dlp"]
    best_agents: ["general"]
    confidence: 0.92
  tags: ["hera", "multi-agent-rag", "youtube", "topology"]
```

Over time, the experience layer aggregates routing intelligence:

```
research:
  Adapter: youtube — 100% success (1 use)
  Adapter: web-fetch — 100% success (2 uses)
  Agent: general — 100% success (2 uses)
  Agent: explore — 100% success (2 uses)
```

A weekly `compound_experience.py` script aggregates all experiences, updates routing patterns, and prepares data for Kestra workflows.

---

## What Was Built

### Core Module: `interactive_research.py`

738 lines of Python orchestrating the 5-stage pipeline:

- `ResearchContext` dataclass holding state across all stages
- `StageResult` dataclass for gate-to-gate handoff
- `InteractiveResearch` class with stage methods that return structured questions for the question tool
- Backward compatible — `--non-interactive` flag preserves existing `>k` behavior
- Experience layer integration — every run reads similar past research, logs outcomes

### Compound Experience: `compound_experience.py`

155 lines aggregating weekly research outcomes:

- Loads all experience YAML files from past 7 days
- Aggregates by query type (research, skills, agents)
- Calculates success rates, average scores, usage counts
- Updates `routing/patterns.yaml` with ranked adapter/agent recommendations
- Collects and deduplicates recommendations from learnings

**Current routing patterns (4 records):**

| Adapter | Success Rate | Usage |
|---------|-------------|-------|
| youtube | 100% | 1 |
| web-fetch | 100% | 2 |
| explore agent | 100% | 2 |
| general agent | 100% | 2 |

As experience accumulates, these patterns will differentiate — some adapters will prove better for certain query types, some agents for certain task types.

---

## The Bigger Picture

This isn't just about research. It's about building a system that **learns from itself**.

The experience layer is the foundation for:

1. **Adaptive routing** — Route queries to agents with proven track records
2. **Auto-evolving skills** — skill-improver uses experience to apply fixes automatically
3. **Smart research suggestions** — "You asked about X last month. Here's what worked."
4. **Agent performance tracking** — "explore succeeds 87% of the time on code tasks, 65% on architecture"

HERA showed that optimizing prompts and topologies instead of weights works. The experience layer applies that philosophy to OpenCode — every research run, every skill invocation, every project decision writes here. Future routing reads here.

This is the difference between a system that **remembers** and a system that **learns**.

---

## What's Next

The pipeline is operational but needs tuning:

1. **Experience enrichment** — Track more granular metrics (time per stage, quality per output type, user satisfaction scores)
2. **Auto-routing** — Use experience layer to suggest adapters before research starts
3. **Kestra workflow** — Weekly compounding runs automatically, updates routing patterns, logs summary
4. **Chat assistant integration** — Chat queries route through experience for smarter agent selection

The foundation is laid. Every interaction makes it smarter.

---

*This post documents the interactive research implementation for OpenCode. Full implementation details: [spec](http://ubuntu4:8080/editor/opencode/docs/superpowers/specs/2026-04-05-interactive-research-design.md), [plan](http://ubuntu4:8080/editor/opencode/docs/superpowers/plans/2026-04-05-interactive-research-plan.md). Source code: [interactive_research.py](http://ubuntu4:8080/editor/opencode/scripts/interactive_research.py), [compound_experience.py](http://ubuntu4:8080/editor/opencode/scripts/compound_experience.py).*
