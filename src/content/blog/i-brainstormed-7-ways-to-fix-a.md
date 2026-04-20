---
pubDatetime: 2026-04-09T15:00:00Z
title: "I Brainstormed 7 Ways to Fix a Broken Feedback Loop"
postSlug: "i-brainstormed-7-ways-to-fix-a"
description: "I Brainstormed 7 Ways to Fix a Broken Feedback Loop"
tags:
  - prompt-engineering
  - feedback-loops
  - self-improving-systems
  - adaptive-learning
  - agent-infrastructure
---

My prompt library has a five-phase self-improvement loop: Capture→Analyse→Improve→Reuse→Monitor. It has cron jobs, pgvector embeddings, a PostgreSQL CLI. It also has exactly 2 prompts captured and 0 embeddings generated. The loop is decorative.

So I sat down and brainstormed every way I could close it, inspired by my menu system that actually works. Here's what I found.

## The Starting Point

My menu factory closes its loop on every single interaction. It tracks which options are shown (`present`), which are picked (`select`), how fast, how often, and which ones appear together. Six weighted dimensions feed into a single score that reorders the next menu. Simple, measurable, closed.

The prompt library has none of that. It has a static checklist in `improve.py` that asks "does this prompt have examples? constraints? context?" — useful heuristics that never change. The system doesn't learn which suggestions actually helped. There's no feedback wire between "improve" and "reuse."

## The Seven Ideas

**Idea 1: Revision Delta Scoring.** Track how many times a user revises their output before accepting it. A prompt that works first-shot scores 1.0. A prompt that needs three revisions scores 0.25. Formula: `1 / (1 + revisions)`. This is the prompt equivalent of "time to select" in the menu system — it measures friction without requiring any human rating.

**Idea 2: Session Co-Occurrence.** When multiple prompts appear in the same session, they have co-affinity. If you always use a debugging prompt alongside a testing prompt, the system should know that and recommend them together. Like co-selection in menus, but across prompts.

**Idea 3: Copy-Paste as Reuse Signal.** The simplest signal: when someone runs `promptlib use <id>`, increment a counter. Most-reused prompts surface first in search. Trivial to implement, immediately closes part of the loop.

**Idea 4: Before/After Diff Weighting.** When `improve.py` suggests adding examples and the user keeps that suggestion, boost the "add examples" weight. When the user rejects "add output format," lower that weight. Over time, the improvement engine learns which suggestions actually help. This is the key to making heuristics adaptive instead of static.

**Idea 5: Outcome Tagging via Session Mining.** My auto-mine script already scans sessions. Add sentiment detection: did the user express satisfaction? Did the task complete without errors? Use that as an automatic quality signal.

**Idea 6: Prompt Lineage Graph.** Track parent→child relationships between original and improved prompts. When a child outperforms its parent on revision delta, the improvement pattern gets validated. Version control for prompts.

**Idea 7: Category-Scoped Scoring.** Different prompt types need different definitions of "better." Bug-fix prompts: speed to resolution. Creative prompts: reuse count. Setup prompts: zero-revision rate. Per-category scoring weights, like the device_fit dimension in the menu system.

## What I Chose

I'm going with a combination of ideas 1, 3, and 4. The minimum viable fix:

1. **`promptlib use <id>`** — log every reuse with revision count (trivial, like `signal.py select`)
2. **Revision delta scoring** — `1 / (1 + revisions)` as the primary quality metric
3. **Adaptive improvement weights** — track which suggestions get accepted, boost the ones that work

The scoring weights mirror the menu system: shot_score 35%, use_frequency 25%, recency 20%, category_fit 10%, manual rating 10%. The first four are automatic. The manual rating is still there for people who want it, but it's the lowest-weighted dimension because nobody uses it.

## The Closed Loop

```
Capture → Use (log revisions) → Score → Improve (adaptive) → Reuse → measure again
```

The key insight from comparing the two systems: the menu system works because "better" is unambiguous — it means the user finds what they want faster. For prompts, "better" means fewer revisions. Once you define that clearly, every other dimension follows.

## What This Enables

The `shot_score` metric (1/(1+revisions)) is novel. No prompt marketplace measures this. Most rate prompts on subjective quality. This measures actual friction in production use. That's a commercial differentiator if this ever becomes a product.

The adaptive improvement engine is also interesting as a pattern. Any system that suggests changes could use acceptance/rejection weighting to learn which suggestions are worth making. It's not specific to prompts — it's a general self-improvement primitive.

## The Spec

Full design spec is at `docs/superpowers/specs/2026-04-09-prompt-library-feedback-loop-design.md` with table schemas, scoring formulas, implementation phases, and measurable success criteria. Next step: implement Phase 1 (signal infrastructure) and start collecting real data.

---

## SEO Tags
`#feedback-loops` `#prompt-engineering` `#self-improving-systems` `#agent-infrastructure` `#adaptive-learning`