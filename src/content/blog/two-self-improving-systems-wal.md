---
pubDatetime: 2026-04-09T14:00:00Z
title: "Two Self-Improving Systems Walked Into a Server"
postSlug: "two-self-improving-systems-wal"
description: "Two Self-Improving Systems Walked Into a Server"
tags:
  - feedback-loops
  - menu-factory
  - self-improving-systems
  - prompt-library
  - agent-infrastructure
---

I built two feedback-loop systems: one for menus, one for prompts. The menu system actually learns. The prompt system has a more impressive design doc. Here's what the gap taught me.

## The Menu System That Works

My `menu-factory` skill has a simple self-improvement loop:

1. **Present** a menu — record every option shown
2. **Select** — record which option the user picked and how fast
3. **Score** — weighted formula across frequency, recency, co-selection, time-to-select
4. **Reorder** — next time, highest-scored options surface first

The scoring weights live in a YAML file: frequency 35%, recency 20%, co-selection 15%, time-to-select 10%, new-option boost 10%, device fit 10%. Six dimensions, one number per option, one rule: show the best options first.

It works because it's small. Signal tracking is two function calls (`signal.py present`, `signal.py select`). The scoring is deterministic. The feedback loop closes every single time a menu is shown.

## The Prompt System That Doesn't (Yet)

My `prompt-library` skill has an ambitious five-phase loop:

```
Capture → Analyse → Improve → Reuse → Monitor
```

It has background cron jobs for auto-mining sessions, auto-analysing quality, auto-improving weak prompts, auto-deduplicating, and auto-reporting. It has pgvector embeddings for semantic search. It has a PostgreSQL-backed CLI (`promptlib`) with capture, search, rate, and export commands.

It also has **2 prompts** captured and **0 embeddings** generated.

The analysis in `improve.py` is a static checklist: does the prompt have examples? Constraints? Context? Output format? It generates suggestions like "consider adding examples" — useful heuristics, but they never change. The system doesn't learn which suggestions actually improved prompt quality. There's no feedback loop.

## The Three Gaps

Comparing the two revealed three specific deficits in the prompt system:

**Gap 1: No real signal data.** The menu system tracks every presentation and selection. The prompt system only has a 1-5 rating scale that nobody uses. Without signal data, there's nothing to score.

**Gap 2: Static heuristics vs adaptive scoring.** The menu system's scoring weights adapt over time. The prompt system's analysis is the same checklist whether it's run once or a thousand times. It should be tracking which improvements led to higher-rated prompts and weighting those patterns more heavily.

**Gap 3: The loop never closes.** The menu loop closes on every interaction: present → select → score → reorder. The prompt loop has a gap between "improve" and "reuse" — when a user reuses an improved prompt, the system doesn't track whether the improvement helped. Without that closure, the loop is decorative.

## Why the Simple One Won

The menu system works because it optimises a single, measurable thing: option ordering. Every signal directly informs that optimisation. There's no ambiguity about what "better" means — it means the user finds what they want faster.

The prompt system tries to optimise prompt quality, which is inherently harder to measure. A 1-5 rating doesn't capture whether a prompt produced better output, faster iteration, or fewer retries. The system would need to track prompt → output → revision count → final satisfaction to close the loop properly.

That's the real lesson: **self-improvement systems need a clear definition of "better" before any loop can close.** For menus, better is obvious. For prompts, I built the machinery before defining the metric.

## What I'm Doing About It

The fix isn't to simplify the prompt system — it's to add what the menu system has:

1. **Track reuse signals**: when a prompt is reused, log it (like `signal.py select`)
2. **Track improvement outcomes**: when an improved prompt gets a higher rating than its predecessor, feed that back into `improve.py`'s heuristics (like `scoring.yaml` weights)
3. **Close the loop**: reuse → outcome → score → adjust improvement patterns

The prompt system's architecture is sound. It just needs the feedback wires connected.

---

## SEO Tags
`#self-improving-systems` `#feedback-loops` `#menu-factory` `#prompt-library` `#agent-infrastructure`