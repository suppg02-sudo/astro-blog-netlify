---
pubDatetime: 2026-04-08T02:04:08Z
title: "The Night Shift: Karpathy's Autoresearch Pattern for Small LLMs"
postSlug: "the-night-shift-karpathy-s-aut"
description: "The Night Shift: Karpathy's Autoresearch Pattern for Small LLMs"
tags:
  - others
---

> Andrej Karpathy built a system that runs 100 experiments overnight while he sleeps — using fixed budgets, one metric, and a single file. We rebuilt his entire pattern for research tasks: a small LLM (Gemma 4, 100K context) ingests YouTube channels, websites, and local files, and wakes you up with structured findings. Here's how every constraint maps.

## Three Files, One Loop

Karpathy's `autoresearch` repo does one thing overnight: it trains a tiny GPT model by letting an AI agent edit `train.py`, running it for **exactly 5 minutes**, checking whether the model improved, and keeping or discarding the change. Then it tries again. Repeat ~100 times until you wake up.

The repo has three files:

| File | What | Who Edits It |
|------|------|-------------|
| `prepare.py` | Loads data, never changed | Nobody |
| `train.py` | The model training code | The AI agent |
| `program.md` | Instructions for the agent | The human |

The loop is five steps: **Modify → Run → Measure → Keep/Discard → Repeat**. Forever.

The whole thing costs nothing to run and produces real research results. But the real genius isn't in the code. It's in the constraints:

**Fixed budget.** Every experiment gets exactly 5 minutes. This makes them all comparable — a faster change is only better if it beats the slower one at the same time limit.

**Single metric.** `val_bpb` — validation bits per byte. Lower is better. One number tells you everything. No dashboards, no multi-objective confusion.

**Single file.** The agent only touches `train.py`. Diffs are reviewable. Scope is bounded.

**Program.md is the product.** The human's highest-leverage job is to evolve the instructions, not the code. Iterate on `program.md` and the agent gets smarter without changing anything else.

## What We Built: CRIRT

We mapped all five constraints to research tasks run overnight by a small LLM (~100K context window, like Gemma 4). The technique is called **CRIRT** — Constrained Retrievable Iterative Research Technique — and it's now part of our research-task-schema.yaml.

Every Karpathy constraint maps directly:

| Karpathy Concept | CRIRT Schema Field | The Mapping |
|-----------------|-------------------|-------------|
| 5-minute fixed budget | `crirt_config.iteration_budget: 15` | Bounded tokens per iteration, bounded context per question |
| `val_bpb` — one metric | `crirt_config.metric.weighted-confidence` | relevance(40%) + novelty(30%) + evidence(30%) = one number |
| Single file (`train.py`) | `max_context_tokens: 5000` | Each iteration sees ~5K tokens. Replace, never append |
| `program.md` (instructions) | `instructions_template` field | Human refines the instructions between sessions |
| Modify → Run → Measure → Keep/Discard → Repeat | `crirt_config.phase_order` | triage → pattern-extract → hypothesis-test → gap-detect → score-sort |

## The Overnight Research Loop

Here's how the overnight loop actually works. You configure sources before bed, set your technique profile, and let the small LLM work:

```
Sources ingest → eRAG indices built → Phase 1: Triage (binary filter)
    → Phase 2: Pattern Extract (find recurring themes)
    → Phase 3: Hypothesis Test (validate claims)
    → Phase 4: Gap Detect (find what's missing)
    → Phase 5: Score & Sort (one metric, keep or discard)
    → Wake up with structured findings
```

Each phase uses a **thinking type** optimised for small LLMs. Small models fail at open-ended synthesis but excel at structured pattern matching:

| Thinking Type | Budget | What the model does |
|--------------|--------|-------------------|
| **1. Triage Scan** | ~500 tokens | "Is this chunk relevant?" Yes/No + 1 sentence |
| **2. Compare Pair** | ~2K tokens | "Compare A vs B on X. Score 1-5. Pick winner." |
| **3. Pattern Extract** | ~5K tokens | "What 3 patterns repeat? Quote source for each." |
| **4. Hypothesis Test** | ~3K tokens | "Support/Contradict/Inconclusive + reasoning." |
| **5. Gap Detection** | ~2K tokens | "What's unanswered? List 3 with source suggestions." |
| **6. Score & Sort** | ~300 tokens | "Score 1-10: relevance(40%), novelty(30%), evidence(30%)" |

Key insight: the context is **replaced** between iterations, never appended. Each iteration sees system prompt (~200), retrieved chunks (~3K), the question (~200), previous key findings (~500), and generates ~1K tokens. Total: ~5K per iteration. In a 100K window, that's 20 iterations safe, 15 comfortable with 3-hour buffer.

## What Gets Indexed

Not just the findings. **The entire research process.** Every session tracks:

- **Agent advice** — what the model recommended and whether you accepted it
- **Your actions** — file edits with affected files
- **Automatic improvements** — lint fixes, config corrections
- **Decision points** — question, choice, rationale, rejected alternatives

When you resume a research task three weeks later, you don't just see findings. You see how the research *unfolded*.

## Source Configuration

You specify sources before running overnight:

| Source Type | Ingestion | Tags |
|------------|-----------|------|
| YouTube channels | MeTube → transcripts | youtube, channel:name |
| Websites | Fetch → text extraction | web, domain:host |
| GitHub repos | Clone → scan code+docs | github, repo:owner/name |
| Local files (PDF, MD, TXT) | Direct extraction | local |
| ArXiv/API | Search → fetch abstracts | arxiv |

```yaml
sources:
  youtube_channels:
    - 3Blue1Brown
    - Lex Fridman
  websites:
    - arxiv.org/abs/cs.AI
    - anthropic.com/research
  local_files:
    - notes/research-questions.md
techniques:
  - crirt
max_iterations: 15
fidelity: deep
```

## Why This Works

Karpathy's insight: **stop building bigger systems and start building better constraints.** A small LLM doesn't need a bigger context window — it needs a tighter, bounded task it can do well.

The five-step chain is Karpathy's Modify → Run → Measure → Keep/Discard → Repeat, translated to research. Same pattern. Different domain. Same result: you sleep, the system researches, and morning brings structured, scored, retrievable findings.

**Tags**: crirt, research, karpathy, autoresearch, gemma, small-llm, erag, schema