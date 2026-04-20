---
pubDatetime: 2026-04-09T20:30:00Z
title: "Build a Self-Improving Prompt Library in 5 Phases"
postSlug: "build-a-self-improving-prompt"
description: "Build a Self-Improving Prompt Library in 5 Phases"
tags:
  - others
---

## What You'll Build

A prompt library that learns from every use — tracking which prompts work, improving the ones that don't, predicting what you'll need next, and automatically mining new prompts from your conversation history. The system follows the Triad principle: Schema defines structure, Signal captures evidence, Auto-Improvement closes the loop.

## Prerequisites

- PostgreSQL with pgvector extension
- Python 3 with psycopg2
- A conversation memory store (we use `pghmem` — any PostgreSQL-backed memory works)

## Mental Model

Think of it as a 5-layer pyramid. Each phase builds on the one below: signals feed scoring, scoring feeds co-occurrence, co-occurrence feeds improvement, and improvement feeds intelligence. You can stop after any phase and still have something useful.

## Step 1: Capture Usage Signals

Create a `prompt_usage` table to log every prompt reuse:

```sql
CREATE TABLE prompt_usage (
    id SERIAL PRIMARY KEY,
    prompt_id UUID REFERENCES captured_prompts(prompt_id),
    used_at TIMESTAMPTZ DEFAULT NOW(),
    session_id TEXT,
    outcome TEXT CHECK (outcome IN ('success','partial','fail')),
    revisions INTEGER DEFAULT 0,
    metadata JSONB DEFAULT '{}'
);
```

Every time you use a prompt, log it:

```bash
promptlib use <uuid> --outcome success --revisions 0 --session abc123
```

Build a composite score from 5 dimensions: shot score (did it work first try?), use frequency, recency, category fit, and manual rating. Store weights in `config/scoring.yaml`:

```yaml
shot_score: 0.35
use_frequency: 0.25
recency: 0.20
category_fit: 0.10
rating: 0.10
```

The shot score is the key innovation — `1/(1+revisions)`. A first-try prompt scores 1.0; one needing 3 revisions scores 0.25.

## Step 2: Track Co-Occurrence Patterns

Prompts don't exist in isolation. Create a materialised view that detects which prompts appear together in 30-minute session windows:

```sql
CREATE MATERIALIZED VIEW prompt_co_affinity AS
SELECT u1.prompt_id AS prompt_a, u2.prompt_id AS prompt_b,
       COUNT(*) AS co_count,
       COUNT(*)::float / NULLIF(COUNT(DISTINCT u1.session_id), 0) AS affinity
FROM prompt_usage u1 JOIN prompt_usage u2
  ON u1.session_id = u2.session_id
  AND u1.prompt_id < u2.prompt_id
  AND u2.used_at BETWEEN u1.used_at AND u1.used_at + INTERVAL '30 minutes'
GROUP BY u1.prompt_id, u2.prompt_id;
```

Boost search results by session context: `promptlib search "debug" --boost-co-occur SESSION_ID`.

## Step 3: Build Adaptive Improvement Weights

Create an improvement engine that learns which suggestion types work. Start with 6 types, each at weight 1.0:

```yaml
# config/improvement_weights.yaml
learning_rate: 0.1
clamp_range: [0.3, 3.0]
suggestions:
  add_examples:    { weight: 1.0, acceptances: 0, rejections: 0 }
  add_constraints: { weight: 1.0, acceptances: 0, rejections: 0 }
  add_context:     { weight: 1.0, acceptances: 0, rejections: 0 }
  add_output_format: { weight: 1.0, acceptances: 0, rejections: 0 }
  add_role:        { weight: 1.0, acceptances: 0, rejections: 0 }
  shorten_prompt:  { weight: 1.0, acceptances: 0, rejections: 0 }
```

When users accept or reject suggestions, update weights with `learning_rate`:

```bash
promptlib improve-feedback <id> --suggestion add_examples --accepted true
# Weight: 1.0 → 1.1 → 1.21 → 1.33 (after 3 accepts)
```

Clamp weights to [0.3, 3.0] so nothing dies completely or dominates.

## Step 4: Build the Dashboard

Create a `promptlib dashboard` command showing everything at a glance: top prompts by composite score, improvement weight evolution with acceptance/rejection counts, 14-day usage trends, and category distribution. Output both a formatted terminal view and JSON for programmatic access.

```
╔════════════════════════════════════════════════════════════╗
║                  PROMPT LIBRARY DASHBOARD                  ║
║   Prompts:   28   Uses:   29   Sessions:   19             ║
║   Success: ██████████░░░░░░░░░░ 52% (15/29)               ║
║                                                            ║
║ IMPROVEMENT WEIGHTS (adaptive)                             ║
║   add_examples       ██████░░░░░░░░░ 1.32  (✓4 ✗1)        ║
║   shorten_prompt     ██░░░░░░░░░░░░░ 0.50  (✓0 ✗0)        ║
╚════════════════════════════════════════════════════════════╝
```

## Step 5: Add the Intelligence Layer

Link prompts to your skill system. Add columns for `linked_skills`, `linked_actions`, and `next_moves`. Build a `suggest` command that uses keyword relevance scoring:

```bash
promptlib suggest "debug this error" --limit 3
# → debugging prompt (relevance: 23), linked to systematic-debugging skill
```

Build a `predict` command using co-occurrence patterns to guess what comes next in a session. If you just used a research prompt, predict a blog-writing prompt.

Finally, wire an auto-mine cron that scans your conversation memory nightly, extracts candidate prompts, scores them for complexity, deduplicates, and captures the best ones automatically. Our first run found 264 candidates and added 10 new prompts.

## Validate It Works

```bash
# Full pipeline test
promptlib stats          # 28 prompts, 29 uses
promptlib dashboard      # Visual health check
promptlib suggest "research AI trends"  # Returns ranked suggestions
```

## Mistakes I Made

**Scoring too strict initially**: I set the auto-mine threshold at score >= 6. Most real user prompts score 0-3 because they're short queries. Lowered to >= 4 and added minimum length filtering (30 chars) instead.

**psycopg2 INTERVAL parameter**: `INTERVAL '%s hours'` with parameterized queries doesn't work in psycopg2. Use f-string formatting with `int()` casting for safety: `f"INTERVAL '{int(hours)} hours'"`.

**Embedding server dependency**: Designed semantic search assuming pgvector embeddings would always be available. The embedding server went down for days. Built keyword-based fallback (`ILIKE`) for the `suggest` command so it works without embeddings.

**Taking content at face value**: pghmem stores multi-line conversations. My first pass only grabbed the first line after "USER:" — missing multi-line prompts. Fixed by accumulating lines until hitting "ASSISTANT:".

## Taking It Further

The shot score is a novel quality metric that could power a prompt marketplace. The adaptive improvement engine could become a SaaS. The co-occurrence engine is collaborative filtering for prompts. Every component in this system has commercial potential — that's the power of closing the loop.

---

**Tags**: prompt-library, feedback-loop, postgresql, adaptive-learning, triad, auto-improvement, tutorial