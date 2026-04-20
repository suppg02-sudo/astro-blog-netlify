---
pubDatetime: 2026-04-10T12:00:00Z
title: "What Claude Code's Creator Taught Me About My Own AI Setup"
postSlug: "claude-code-workflow-lessons"
description: "What Claude Code's Creator Taught Me About My Own AI Setup"
tags:
  - agentic-development
  - nouscoder
  - ai-engineering
  - open-source
  - workflow
  - lessons
  - claude-code
---

I read Boris Cherny's workflow thread last week. You probably did too — it went viral faster than a benchmark tweet. The creator of Claude Code, running five agents in parallel, using only the heaviest model, turning every AI mistake into a permanent rule. Developers called it "Starcraft for coding."

Then a second article landed the same week: Nous Research released NousCoder-14B, a 14-billion parameter open-source coding model trained in four days on 48 B200 GPUs. A Google principal engineer posted that Claude Code replicated a year-long distributed agent project from a three-paragraph prompt.

Together, these two stories define the agentic coding moment of early 2026. And instead of just taking notes, I found myself doing something uncomfortable: comparing Cherny's setup to mine.

## The Trap

Here's what happens. You build an AI-augmented development system. You add memory — PostgreSQL with pgvector, 2,846+ entries and counting. You add skills — 50+ specialized workflows. You add progressive disclosure, menu factories, signal tracking, trigger words, a verified knowledge engine. You add context files and schemas and linting and...

You end up with something that looks more like an enterprise service mesh than a developer workflow.

Cherny has one file. `CLAUDE.md`. Checked into git.

Every time Claude makes a mistake, they add a line. Done. The system compounds. No PostgreSQL, no vector embeddings, no menu optimizer.

Meanwhile, Nous Research trained a competitive coding model by giving it 24,000 problems with binary pass/fail signals. No sophisticated reward shaping. No human preference data. Just: did the code execute correctly within 15 seconds and 4GB of memory? Yes or no.

The pattern repeats: simple feedback loops, tight iteration, compound learning.

## The Stack

Let me be honest about what I'm running:

- **AGENTS.md**: 300+ lines of always-on rules, loaded every session
- **50+ skills**: Each with SKILL.md, scripts, context files
- **Memory system**: PostgreSQL + pgvector with semantic search
- **Trigger system**: 30+ keyboard shortcuts with usage tracking
- **Menu factory**: Runtime-generated menus with signal tracking and optimization
- **Brainplane**: Raw → compile → lint → wiki knowledge pipeline

Cherny has: 5 terminal tabs, a CLAUDE.md file, and system notifications.

Nous Research has: 48 GPUs, a binary reward signal, and four days.

## The Parallel

Here's the thing: Cherny's principles and mine are nearly identical. The divergence is in execution density.

**Parallel agents?** I have `dispatching-parallel-agents` and `subagent-driven-development`. He has 5 numbered iTerm2 tabs. Same concept, different complexity surface area.

**Persistent memory?** I have pghmem with 2,846+ entries. He has a markdown file in git. Both compound over time. His is simpler to query and never suffers from embedding drift.

**Verification loops?** I have `browser-qa`, `validate-delivery`, `verification-before-completion`. He has a Chrome extension that opens the browser, tests the UI, and iterates. Same loop, fewer abstractions.

**Model selection?** He uses Opus 4.5 exclusively — the slowest, smartest model. I route between models based on task type. His approach is simpler and, by his account, faster in total because you steer less.

And here's where NousCoder fits: it achieves 67.87% on LiveCodeBench with a 14B parameter model. Not by being smarter, but by training on verifiable outcomes. The lesson translates: **what you measure and iterate on matters more than how sophisticated your system is.**

## Why Simplicity Wins

The uncomfortable lesson is about cognitive overhead.

Every skill I add, every context file I maintain, every trigger I track — that's a maintenance cost. Every menu signal I record, every progressive disclosure layer I build — that's time not spent shipping.

Cherny's workflow works because it has a tight OODA loop: observe the agent output, orient to the next task, decide what to dispatch, act by sending a prompt. No menus. No factory optimization. No schema validation.

The 2-3x quality improvement he reports from verification loops? That comes from the loop itself, not from the tooling around it.

NousCoder's 7-point improvement over its base model? That came from binary pass/fail rewards and dynamic sampling, not from fancy loss functions.

## The Evidence That Changed My Mind

Four data points that made me reconsider my architecture:

1. **"Since you have to steer it less and it's better at tool use, it is almost always faster than using a smaller model in the end."** This inverts the cost model. The expensive model is cheaper when you factor in human correction time.

2. **"Every mistake becomes a rule."** Compounding knowledge at its purest. Not semantic search, not vector similarity — just a flat list of corrections that grows monotonically.

3. **"Giving the AI a way to verify its own work improves quality by 2-3x."** Not better prompts, not more context, not fancier skills. Just a verification loop.

4. **NousCoder matched models 5-10x its size using only binary execution feedback.** The signal doesn't need to be sophisticated. It needs to be correct and fast.

## What I'm Keeping

I'm not burning down the skill system. Some abstractions genuinely help — the blog pipeline, the ingestion router, the container management skills. These solve real problems that a CLAUDE.md file alone can't.

But I am adopting a simplification principle: **if a system exists to manage complexity that wouldn't exist without the system, remove it.**

The verification loop stays. The parallel dispatch stays. The persistent correction file stays (we call it AGENTS.md, but the principle is identical). Everything else is on notice.

## Lessons

1. **The correction tax beats the compute tax.** Use the best model you can afford, not the cheapest one. Cherny uses Opus 4.5 for everything. NousCoder proves even small models shine with the right feedback.

2. **One file in git beats a database you have to query.** Knowledge that's always loaded beats knowledge that needs a search query. Both compound, but one has zero latency.

3. **Verification loops are the real unlock.** An AI that tests its own work is a workforce. One that doesn't is a fancy autocomplete. This applies at every scale — from a single developer to a 14B parameter training run.

4. **Simplicity is a feature, not a sacrifice.** Cherny's workflow reportedly drives $1B ARR with numbered tabs and a markdown file. NousCoder beat larger models with binary rewards. Complexity is a cost, not a capability.

5. **The mental model matters more than the tooling.** "Workforce, not assistant" isn't a skill you load. It's how you think. And the data ceiling is coming — Nous Research noted they've already consumed "a significant portion of all readily available competitive programming problems." The next frontier isn't more data. It's self-play, synthetic generation, and tighter loops.

---

*Sources: [VentureBeat — Boris Cherny's workflow](https://venturebeat.com/technology/the-creator-of-claude-code-just-revealed-his-workflow-and-developers-are), [VentureBeat — NousCoder-14B](https://venturebeat.com/technology/nous-researchs-nouscoder-14b-is-an-open-source-coding-model-landing-right-in-the), [Boris Cherny on X](https://x.com/bcherny/status/2007179832300581177), [NousCoder-14B on HuggingFace](https://huggingface.co/NousResearch/NousCoder-14B)*

---

*Related: [The Four-Day Coding Model — NousCoder-14B and AI's Data Problem](/posts/the-four-day-coding-model-what-nouscoder-14b-revea/)*