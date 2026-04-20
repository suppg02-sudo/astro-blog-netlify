---
pubDatetime: 2026-04-10T22:03:11Z
title: "Karpathy Tracker — 10 April 2026"
postSlug: "karpathy-tracker-2026-04-10"
description: "Karpathy Tracker — 10 April 2026"
tags:
  - evolution
  - indexing
  - karpathy
  - daily-tracker
---

# Karpathy Tracker — 10 April 2026

## Quick Summary

Activity detected: **8 articles** and **8 videos** / interviews.

## Repo Activity

### No new commits in last 24 hours

### All Repos Status

| Repo | Description | Stars | Language | Last Push |
|------|-------------|-------|----------|----------|

## News & Community Discourse

### Recent Articles

- [Andrej Karpathy Stopped Using AI to Write Code. He’s Using It to Build a Second Brain Instead | by Nikhil | Neural Notions | Apr, 2026 | Medium](https://medium.com/neuralnotions/andrej-karpathy-stopped-using-ai-to-write-code-hes-using-it-to-build-a-second-brain-instead-cddceadc5df5) — *5 days ago*
  - On <strong>April 3, 2026</strong>, Andrej Karpathy co-founder of OpenAI, former AI lead at Tesla, the guy who coined &quot;vibe coding&quot; posted so...
- [r/ClaudeAI on Reddit: Combined Karpathy's LLM Wiki with Milla Jovovich`s MemPalace MCP. Claude Code now remembers everything across sessions](https://www.reddit.com/r/ClaudeAI/comments/1sh48b4/combined_karpathys_llm_wiki_with_milla_jovovichs/) — *1 day ago*
  - But isn&#x27;t Mempalace a scam by a known grifter trying to impersonate the real Milla? Why choose that one to combine with the Karpathy pattern when...
- ['I Call Him Dobby The Elf Claw,' OpenAI Cofounder Andrej Karpathy Says — After Nvidia's Jensen Huang Gift - Benzinga](https://www.benzinga.com/news/topics/26/04/51746743/i-call-him-dobby-the-elf-claw-openai-cofounder-andrej-karpathy-says-after-nvidias-jensen-huang-gifts-him-a-superchip-to-power-his-ai-home) — *1 day ago*
  - Experts say these common ETF pitfalls can catch new investors off guard · Karpathy also said in a post on X that <strong>Huang had gifted him a DGX St...
- [Why Andrej Karpathy Abandoned RAG (Claude Code x Obsidian) - YouTube](https://www.youtube.com/watch?v=WgqqoSkC0bw) — *3 days ago*
  - My IG: https://www.instagram.com/sayed.developerKarpathy’s original tweet:https://x.com/karpathy/status/2039805659525644595Karpathy’s Gist: https://gi...
- [Karpathy's LLM Knowledge Base: Build an AI Second Brain](https://ghost.codersera.com/blog/karpathy-llm-knowledge-base-second-brain/) — *4 days ago*
  - On <strong>April 3, 2026</strong>, Andrej Karpathy posted something on X that resonated well beyond the usual AI news cycle. He wasn&#x27;t announcing...
- [LLM Knowledge Bases | Ivan Walsh](https://ivanwalsh.com/blog/llm-knowledge-bases/) — *6 days ago*
  - No single Slack thread, Notion page, or Google Doc could answer that. The wiki can, because it was built to connect things, not just contain them. Kar...
- [Karpathy's LLM Knowledge Bases Turn Raw Files into ...](https://x.com/i/trending/2042013766036926944) — *2 days ago*
  - JavaScript is not available · We’ve detected that JavaScript is disabled in this browser. Please enable JavaScript or switch to a supported browser to...
- [Andrej Karpathy Says There's a 'Growing Gap' Among AI Users - Business Insider](https://www.businessinsider.com/andrej-karpathy-growing-gap-ai-understanding-2026-4) — *5 hours ago*
  - Andrej Karpathy wrote on X that <strong>AI power users and skeptics were &quot;speaking past each other.&quot;</strong>...

### Videos / Talks

- [Elder Patrick Kearon | ASL | April 2026 General Conference - YouTube](https://www.youtube.com/watch?v=zmdP30j4ebo) — *5 days ago*
  - A talk given by Elder Patrick Kearon during the Saturday morning session of the April 2026 general conference.
- [Elder Patrick Kearon | April 2026 General Conference - YouTube](https://www.youtube.com/watch?v=YH8I1SNli_Q) — *1 week ago*
  - A talk given by Elder Patrick Kearon during the Saturday morning session of the April 2026 general conference.
- [Graphify: 48 Hours After Karpathy's Post, Someone Built the Tool - YouTube](https://www.youtube.com/watch?v=EraQF0GxbOw) — *2 days ago*
  - Andrej Karpathy described his dream workflow — <strong>drop raw files into a folder and have an LLM compile them into a knowledge graph</strong>. 48 h
- [Andrej Karpathy Just 10x’d Everyone’s Claude Code - YouTube](https://www.youtube.com/watch?v=20d5cSkSvcU) — *3 days ago*
  - <strong>Andrej Karpathy&#x27;s latest idea is reshaping how we view artificial intelligence, moving beyond basic prompts to build persistent systems</
- [Karpathy's LLM Wiki: The End of Forgotten Knowledge - YouTube](https://www.youtube.com/watch?v=RQsLXmenr48&vl=en) — *4 days ago*
  - <strong>Andrej Karpathy recently shared a system where &quot;ai agents&quot; remember and organize information, addressing the challenge of knowledge 

## Indexing Deep Dive

### Karpathy's Indexing Approach (Reference)

Karpathy uses the **raw/ → compile → lint → wiki** pattern:
1. **raw/**: Ingest papers, repos, articles, transcripts
2. **compile**: LLM reads raw data, writes structured wiki with summaries, backlinks
3. **lint**: LLM scans for inconsistencies, missing data, new connections — self-healing
4. **wiki**: Clean vault of verified knowledge, human-readable, auditable

**File-over-app philosophy**: Markdown as source of truth, no vendor lock-in.

## Evolution Project Cross-Reference


**Recent decisions** (17 tracked):
  - 2026-04-10: Schema alignment session — 9/9 factories aligned to full DNA (identity, factory, audit, agentInterfa
  - 2026-04-10: Evolution Engine audited and reconnected — 7 critical bugs fixed, LLM switched to GLM-5.1/Zhipu API,
  - 2026-04-10: agentInterface vs agentInterfaces vs agent_interface key mismatch fixed across all 9 factories

## Coverage Improvement Suggestions

1. 📰 **8 new article(s) about Karpathy** — capture to raw/ for knowledge compiler ingestion.
2. 🎬 **8 new video(s)** — YouTube transcripts should be fetched and added to raw/ directory for compilation.
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
| 🔗 **Source** | [medium.com](https://medium.com/neuralnotions/andrej-karpathy-stopped-using-ai-to-write-code-hes-using-it-to-build-a-second-brain-instead-cddceadc5df5) | New content |
| 🔗 **Source** | [www.reddit.com](https://www.reddit.com/r/ClaudeAI/comments/1sh48b4/combined_karpathys_llm_wiki_with_milla_jovovichs/) | New content |
| 🔗 **Source** | [www.benzinga.com](https://www.benzinga.com/news/topics/26/04/51746743/i-call-him-dobby-the-elf-claw-openai-cofounder-andrej-karpathy-says-after-nvidias-jensen-huang-gifts-him-a-superchip-to-power-his-ai-home) | New content |
| 🔗 **Source** | [www.youtube.com](https://www.youtube.com/watch?v=WgqqoSkC0bw) | New content |
| 🔗 **Source** | [ghost.codersera.com](https://ghost.codersera.com/blog/karpathy-llm-knowledge-base-second-brain/) | New content |
| 🔗 **Source** | [www.youtube.com](https://www.youtube.com/watch?v=zmdP30j4ebo) | New content |
| 🔗 **Source** | [www.youtube.com](https://www.youtube.com/watch?v=YH8I1SNli_Q) | New content |
| 🔗 **Source** | [www.youtube.com](https://www.youtube.com/watch?v=EraQF0GxbOw) | New content |

## Metrics

| Metric | Value |
|--------|-------|
| Karpathy Repos Tracked | 13 |
| New Commits (24h) | 0 |
| News Articles Found | 8 |
| Videos Found | 8 |
| Social Posts Found | 0 |
| Improvement Suggestions | 4 |

---

*Report generated: 2026-04-10 22:03 UTC*
*Sources: GitHub API + Brave Search API + evolution.yaml*
*Pipeline: raw/ → compile → wiki → blog*
