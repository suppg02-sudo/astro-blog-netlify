---
pubDatetime: 2026-04-07T14:30:00Z
title: "Autoresearch Meets Hermes: Two Approaches to Autonomous AI Research"
postSlug: "autoresearch-meets-hermes-two-approaches-to-autonomous-ai-research"
description: "Autoresearch Meets Hermes: Two Approaches to Autonomous AI Research"
tags:
  - autonomous-agents
  - erag
  - ai
  - autoresearch
  - hermes
  - research
---

> We reviewed Karpathy's autoresearch and Nous Research's Hermes Agent (with Hermes Lab) to understand what autonomous research infrastructure looks like at the bleeding edge — and what our eRAG pipeline can borrow from each.

## The Setup

Our eRAG v2 pipeline already does persistent, topic-based research with PostgreSQL + pgvector + NetworkX. We recently added a Self-Critique Loop (Technique 1 from our AutoGPT exploration) that synthesises research, audits it for gaps, and decides whether another pass is needed.

But we're building on a shoebox compared to what's out there. Two projects caught our attention:

1. **[karpathy/autoresearch](https://github.com/karpathy/autoresearch)** — Andrej Karpathy's overnight experiment loop. An AI agent modifies a training script, runs it for 5 minutes, checks the metric, keeps or discards, and repeats. ~100 experiments while you sleep.
2. **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** + **[amenti-labs/hermes-lab](https://github.com/amenti-labs/hermes-lab)** — A self-improving agent with a closed learning loop, backed by file-first experiment scaffolding with six search strategies.

Here's what we learned from each — and what we're stealing.

## Karpathy's Autoresearch: Brutal Simplicity

The repo has three files that matter:

- `prepare.py` — data prep, never modified
- `train.py` — the file the agent edits every iteration
- `program.md` — the instructions the human edits to steer the agent

The genius is in the constraints:

**Fixed time budget.** Every experiment runs exactly 5 minutes. This makes all experiments directly comparable regardless of what changed (architecture, hyperparameters, batch size). It also means the system automatically finds the optimal model for your hardware in that budget.

**Single metric.** `val_bpb` (validation bits per byte) — lower is better, vocabulary-size-independent. No multi-objective handwringing. One number tells you everything.

**Single file.** The agent only touches `train.py`. Diffs are reviewable. Scope is bounded. When something goes wrong, you know exactly where to look.

**The pattern**: Modify → Run → Measure → Keep/Discard → Repeat. Forever.

Karpathy frames `program.md` as "research org code" — the human's job is to evolve the instructions that govern how the agent researches. The agent's job is to execute within those instructions. This separation of concerns is elegant.

### What We're Borrowing

We already have an `autoresearch` skill in our control plane that generalises this pattern. But reading the source reinforced three things:

1. **Fixed budgets beat flexible ones.** Our eRAG critique loop should have a hard cap on iterations (e.g., max 3 passes before forcing a human review). Open-ended loops drift.
2. **Single metrics beat dashboards.** Our critique confidence score (0.0-1.0) is the right idea. We should trust it more — if confidence < 0.7, stop and surface to the human.
3. **The program file is the product.** Our SKILL.md files are essentially program files. The autoresearch insight is that iterating on the instructions (not the code) is where the real leverage is.

## Hermes Agent: The Agent That Learns

Hermes Agent (19K GitHub stars, 200+ contributors) takes a fundamentally different approach. Where autoresearch is a loop, Hermes is an ecosystem.

**Closed learning loop.** Hermes creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions. This is the "self-improving" part — not just running experiments faster, but actually getting better at running experiments.

**Multi-platform presence.** CLI, Telegram, Discord, Slack, WhatsApp, Signal. One agent, many interfaces. This matters because research doesn't happen only at your desk.

**Subagent spawning.** Hermes can delegate to isolated subagents for parallel workstreams. This is the multi-agent pattern that single-agent systems can't touch.

**The self-evolution repo** (`hermes-agent-self-evolution`) uses DSPy + GEPA to optimise skills, prompts, and code autonomously. This is meta-research — research about how to research better.

### Hermes Lab: The Infrastructure

Hermes Lab is the experiment scaffolding built around the agent:

**File-first state.** All experiment state lives in YAML, JSON, and Markdown. No database. This is the opposite of our PostgreSQL approach — and it's worth understanding why they chose this. Files are portable, version-controllable, and inspectable by both humans and agents without tooling.

**Six search strategies**: random, perturb, bayesian, evolution, tree, and LLM-guided. Each has a clear "when to use" recommendation. Our eRAG pipeline currently has zero search strategies — we just run queries and hope for the best.

**Multi-fidelity tiers.** Run cheap proxy experiments first, promote winners to expensive final validation. This is a research budget optimization we haven't considered.

**Execution modes**: cron (scheduled), burst (back-to-back), guided (human approval), swarm (multi-strategy rotation). Different modes for different research phases.

## The Comparison

| Dimension | autoresearch | Hermes Agent + Lab | Our eRAG v2 |
|-----------|-------------|-------------------|-------------|
| **Core loop** | Modify → Run → Measure → Keep/Discard | Closed learning: experience → skill → improve → persist | Ingest → Synthesise → Critique → Gap-fill → Re-synthesise |
| **State store** | Git (train.py diffs) | Files (YAML/JSON/MD) | PostgreSQL + pgvector |
| **Metric** | Single (val_bpb) | Multi-metric, multi-fidelity | Confidence score (0.0-1.0) |
| **Search strategy** | Agent-driven | 6 strategies (random → LLM) | None yet |
| **Self-improvement** | program.md iteration | Skill creation + DSPy optimisation | Critique loop (v2.3.0) |
| **Parallelism** | Single agent | Subagent spawning | None yet |
| **Platform** | CLI only | CLI + 5 messaging platforms | CLI only |

## What We're Taking Forward

From autoresearch:
- **Hard iteration caps** — no infinite loops, force human review after N passes
- **Single-metric discipline** — trust the confidence score, don't add more dashboards
- **Program file as product** — our SKILL.md files are the real deliverable

From Hermes:
- **Search strategies** — we need at least perturb and bayesian for our query expansion (Technique 3 on our roadmap)
- **Multi-fidelity tiers** — quick proxy queries before deep research (maps to our existing quick/standard/deep query modes)
- **Skill self-improvement** — our critique loop is step one; Hermes shows us the full path

What we're NOT taking:
- **File-first state** — PostgreSQL is the right call for our vector search use case. Files don't give you cosine similarity queries.
- **Multi-platform presence** — our CLI-first approach is correct for a research tool. Chat interfaces are for consumption, not production.
- **Full agent autonomy** — we're deliberately building a semi-autonomous system that keeps humans in the loop at confidence thresholds.

## The Road Ahead

Our 6-technique roadmap from the AutoGPT exploration still stands:

1. ~~Self-Critique Loop~~ (done, v2.3.0)
2. Recursive Research Decomposer
3. Dynamic Adapter Chaining
4. Three-Layer Memory Architecture
5. Research Graph as Control Plane
6. Autonomous Research Agent

But now we have richer inspiration for techniques 4-6. Hermes's skill creation pattern maps directly to our memory architecture. Hermes Lab's search strategies give us a blueprint for technique 3. And Karpathy's brutal simplicity is the design philosophy we should carry through all of them.

The best research systems aren't the most complex ones. They're the ones where the human can understand what happened while they were sleeping.

---

*This post is part of our ongoing exploration of autonomous research systems. The previous post in this series is [Borrowing AutoGPT's Brain: Six Techniques to Supercharge Your Research Pipeline](/posts/borrowing-autogpt-s-brain-six/). Our eRAG pipeline is open-source and documented in our skills repository.*


## Related Posts

- [Borrowing AutoGPT's Brain: Six Techniques to Supercharge Your Research Pipeline](/posts/borrowing-autogpt-s-brain-six/) — The 6-technique roadmap referenced in this post
- [I Turned Andrej Karpathy's Autoresearch Into a Universal Skill](/posts/andrej-karpathy-autoresearch-universal-skill-2026/) — Generalising Karpathy's pattern to our  skill
- [Andrej Karpathy on Code Agents, AutoResearch and the Self Improvement Loopy Era of AI](/posts/andrej-karpathy-on-code-agents/) — The broader 'Self Improvement Loopy Era' framing
- [Self-Improving Architecture #6: The Experiment Controller Is Live](/posts/self-improving-architecture-experiment-controller-live/) — Our own experiment controller implementation
- [OmniMemory Meets Reality: Upgrading Your AI Stack with Autonomous Research Findings](/posts/omnimemory-meets-reality-upgra/) — Memory systems that close the learning loop
- [The AI Agent Control Plane: Schemas, Signals, Controllers, and Factories](/posts/ai-agent-control-plane-schemas-signals-controllers-factories/) — The infrastructure powering these research loops
