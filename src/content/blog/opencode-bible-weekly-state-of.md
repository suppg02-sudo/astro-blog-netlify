---
pubDatetime: 2026-04-05T16:52:20Z
title: "OpenCode Bible — Weekly State of the Ecosystem (Week of 2026-04-05)"
postSlug: "opencode-bible-weekly-state-of"
description: "OpenCode Bible — Weekly State of the Ecosystem (Week of 2026-04-05)"
tags:
  - others
---

Every system that claims to be self-improving needs a mirror. This is the first weekly "Bible" — a comprehensive scan of the entire OpenCode ecosystem: projects, skills, knowledge pipeline, and recommended actions.

---

## Executive Summary

- **Projects**: 8 total, 2 active, 0 stale
- **Skills**: 13 registered
- **Wiki**: 9 articles, 9 new this week
- **Knowledge Pipeline**: 11 raw → 10 compiled → 9 wiki this week
- **High Priority**: 4 projects need attention

This represents the **Karpathy Pattern** in action — the system reading its own state, identifying gaps, and producing a briefing. Without this, the knowledge base gradually goes stale. Every business has a `raw/` directory. Nobody's ever compiled it. This changes that.

---

## Projects Overview

| Project | Status | Phase | Priority | Updated |
|---------|--------|-------|----------|---------|
| Bot (AI/Tech Ecosystem) 🔴 | active | plan | high | 2026-04-01 |
| Consultancy | idea | idea | medium | 2026-04-01 |
| DIY CNC Gantry | rest | idea | medium | 2026-04-04 |
| Evolution 🔴 | active | plan | high | 2026-04-05 |
| Garage Tidy | idea | idea | medium | 2026-04-04 |
| Interactive Research | plan | plan | medium | 2026-04-05 |
| lockdown 🔴 | idea | plan | high | 2026-04-04 |
| Modular Stacked Greenhouse 🔴 | idea | idea | high | 2026-04-02 |

### Key Observations

**4 high-priority projects** are demanding attention. Of these:

- **Bot** — Plan phase, ready to advance to active. Focus: attention pipeline deployment.
- **Evolution** — Plan phase, actively building (Karpathy pattern deployment, Kestra orchestration).
- **lockdown** — Plan phase, preparing for 6-month self-sufficiency.
- **Modular Stacked Greenhouse** — Idea phase complete, awaiting implementation plan.

No stale projects detected — all updated within the last 7 days.

---

## Knowledge Pipeline Activity

The three-stage Karpathy pipeline is now operational:

```
🔴 raw/ → 🟠 compiled/ → 🔵 wiki/
  (dump)    (LLM process)  (review + promote)
```

### This Week's Activity

- **raw/**: 11 total files — everything from Karpathy articles to GLM-5 tutorials
- **compiled/**: 10 analytical summaries with OpenCode mappings
- **wiki/**: 9 verified articles in the clean vault

### Recent Wiki Articles

- Karpathy Pattern — LLM Knowledge Base Architecture
- Contamination Mitigation Protocol
- Directus CMS to Platform
- Fine-Tune Gemma-4 Locally
- GLM-5 Agentic Systems Production Patterns
- HERA Self-Learning Multi-Agent RAG
- OmniMemory Autonomous Memory Architecture
- Pi Agent vs OpenCode Comparison

### Contamination Zones

The pipeline enforces a **contamination mitigation protocol** — raw inputs can't enter the wiki directly. They must pass through compilation and review. This prevents agent experiments from polluting curated knowledge.

> Every business has a raw/ directory. Nobody's ever compiled it. That's the product.

---

## Skills Registry

| Skill | Version | Maturity |
|-------|---------|----------|
| adguard | 2.0.0 | L3 |
| agents-factory | 1.0.0 | L2 |
| astro | 2.12.0 | L3 |
| attention | 1.0.0 | L2 |
| grafana | 1.1.0 | L3 |
| interactive-content | 1.0.0 | — |
| moneyprinter2 | 1.0.0 | L2 |
| openrag | 2.0.0 | L3 |
| project-factory | 1.2.0 | L2 |
| research-factory | 1.1.0 | L3 |
| skill-factory | 2.0.0 | L4 |
| svg | 1.1.0 | L2 |
| transcription | 3.3.0 | 3 |

Most mature: **skill-factory** at L4 — the system that creates and improves other skills.

---

## Infrastructure Deployed This Week

### Knowledge Compiler Watcher

A systemd service (`compiler_watcher.py`) polling a Directus knowledge queue every 30 seconds. Drop a URL into the queue, and the system automatically ingests it, compiles analysis, and promotes it to the wiki. Two items already processed successfully.

### Weekly Bible Script

Runs every Sunday at 9am UTC. Scans all projects, skills, wiki articles, and pipeline stages. Produces this report automatically — no manual curation required.

### Pipeline Coverage

The Karpathy pattern (raw → compiled → wiki) is operating at **55% alignment** with the ideal. Gaps remaining are blocked on Kestra orchestration deployment:

- Cross-reference lint (scanning all files for contradictions)
- Compound loop orchestration (ingest → compile → lint → feedback)
- Ephemeral wiki flow evaluation

---

## Recommended Actions

1. **Advance Bot to active phase** — Plan is written, exit criteria can be validated
2. **Write Greenhouse implementation plan** — All research done, just needs structured plan
3. **Address lockdown next action** — Take stock of existing supplies, identify gaps
4. **Deploy Kestra** — Unblocks 3 deferred pipeline items

---

## The Philosophy Behind This

Karpathy's insight was simple: at ~100 articles / ~400K words, LLM navigation via summaries is sufficient. Vector databases introduce more latency and retrieval noise than they solve. The system should maintain its own knowledge base like a research librarian — reading, compiling, linting, and interlinking.

OpenCode has adopted this pattern. The result is a system that doesn't just remember — it learns. Every raw input gets compiled into structured knowledge. Every week, the system audits itself. Every gap gets flagged.

**Next week's Bible** will track whether the recommended actions moved forward, whether the knowledge backlog was addressed, and whether new wiki material entered the clean vault.

---

*Auto-generated by weekly_bible.py on 2026-04-05. First edition.*