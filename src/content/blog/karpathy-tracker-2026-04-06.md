---
pubDatetime: 2026-04-06T23:18:00Z
title: "Karpathy Tracker — 06 April 2026"
postSlug: "karpathy-tracker-2026-04-06"
description: "Karpathy Tracker — 06 April 2026"
tags:
  - evolution
  - indexing
  - karpathy
  - daily-tracker
---

# Karpathy Tracker — 06 April 2026

## Quick Summary

No significant new activity from Karpathy today. Weekly deep-dive will catch any patterns.

## Repo Activity

### No new commits in last 24 hours

### All Repos Status

| Repo | Description | Stars | Language | Last Push |
|------|-------------|-------|----------|----------|
| [karpathy/autoresearch](https://github.com/autoresearch) | AI agents running research on single-GPU nanochat training a | 67,231 | Python | 2026-03-26 |
| [karpathy/nanoGPT](https://github.com/nanoGPT) | The simplest, fastest repository for training/finetuning med | 56,205 | Python | 2025-11-12 |
| [karpathy/nanochat](https://github.com/nanochat) | The best ChatGPT that $100 can buy. | 51,228 | Python | 2026-03-27 |
| [karpathy/llm.c](https://github.com/llm.c) | LLM training in simple, raw C/CUDA | 29,417 | Cuda | 2025-06-26 |
| [karpathy/llama2.c](https://github.com/llama2.c) | Inference Llama 2 in one file of pure C | 19,360 | C | 2024-08-06 |
| [karpathy/llm-council](https://github.com/llm-council) | LLM Council works together to answer your hardest questions | 16,711 | Python | 2025-11-22 |
| [karpathy/micrograd](https://github.com/micrograd) | A tiny scalar-valued autograd engine and a neural net librar | 15,358 | Jupyter Notebook | 2024-08-08 |
| [karpathy/reader3](https://github.com/reader3) | Quick illustration of how one can easily read books together | 3,457 | Python | 2025-11-18 |
| [karpathy/rendergit](https://github.com/rendergit) | Render any git repo into a single static HTML page for human | 2,151 | Python | 2025-08-21 |
| [karpathy/jobs](https://github.com/jobs) | A research tool for visually exploring Bureau of Labor Stati | 1,355 | HTML | 2026-03-16 |
| [karpathy/karpathy.github.io](https://github.com/karpathy.github.io) | my blog | 1,098 | CSS | 2026-02-13 |
| [karpathy/hn-time-capsule](https://github.com/hn-time-capsule) | Analyzing Hacker News discussions from a decade ago in hinds | 592 | Python | 2025-12-10 |
| [karpathy/rustbpe](https://github.com/rustbpe) | The missing tiktoken training code | 418 | Rust | 2026-01-03 |

## News & Community Discourse

No new articles detected today.

## Indexing Deep Dive

### Karpathy's Indexing Approach (Reference)

Karpathy uses the **raw/ → compile → lint → wiki** pattern:
1. **raw/**: Ingest papers, repos, articles, transcripts
2. **compile**: LLM reads raw data, writes structured wiki with summaries, backlinks
3. **lint**: LLM scans for inconsistencies, missing data, new connections — self-healing
4. **wiki**: Clean vault of verified knowledge, human-readable, auditable

**File-over-app philosophy**: Markdown as source of truth, no vendor lock-in.

## Evolution Project Cross-Reference


**Recent decisions** (12 tracked):
  - 2026-04-05: Knowledge compiler deployed as systemd service (compiler_watcher.py). Polls Directus knowledge_queue. 2 item
  - 2026-04-05: Weekly OpenCode Bible deployed (weekly_bible.py). Cron Sunday 9am UTC. First report generated.
  - 2026-04-06: Deployed Kestra orchestration layer

## Coverage Improvement Suggestions

1. 🔬 **Karpathy/autoresearch updated** — compare his experiment loop (observe→diff→actuate) against your autoresearch skill. Check program.md changes for new agent instruction patterns.
2. ⚡ **Karpathy/llm.c updated** — review C/CUDA training code changes. Relevant for understanding raw/compile efficiency patterns.
3. 📊 **Indexing coverage audit** — check raw/ directory has recent content, wiki/ articles are self-healing, pghmem embedding coverage improving.
4. 🔗 **Backlink check** — review wiki/_backlink-index.md for orphaned articles. Karpathy's system auto-generates backlinks; yours needs manual review.

## Resources

| Type | Link | Description |
|------|------|-------------|
| 📁 **GitHub** | [karpathy](https://github.com/karpathy/) | Karpathy's GitHub profile |
| 🔍 **Autoresearch Repo** | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | Autonomous research loop |
| 📖 **VentureBeat** | [Karpathy LLM Knowledge Base](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an) | Original knowledge base article |
| 📰 **NextBigFuture** | [Karpathy on Code Agents](https://www.nextbigfuture.com/2026/03/andrej-karpathy-on-code-agents-autoresearch-and-the-self-improvement-loopy-era-of-ai.html) | Agentic engineering coverage |
| 🧠 **Your Wiki** | [karpathy-pattern](http://ubuntu4:8080/editor/opencode/wiki/karpathy-pattern-llm-knowledge-base.md) | Your compiled wiki article |
| 📊 **Evolution Project** | [evolution.yaml](http://ubuntu4:8080/editor/opencode/skills/project-factory/projects/evolution.yaml) | Project tracking file |
| (No new sources to add today) |

## Metrics

| Metric | Value |
|--------|-------|
| Karpathy Repos Tracked | 13 |
| New Commits (24h) | 0 |
| News Articles Found | 0 |
| Videos Found | 0 |
| Social Posts Found | 0 |
| Improvement Suggestions | 4 |

---

*Report generated: 2026-04-06 23:18 UTC*
*Sources: GitHub API + Brave Search API + evolution.yaml*
*Pipeline: raw/ → compile → wiki → blog*
