---
pubDatetime: 2026-04-11T21:59:22Z
title: "How I Made My AI Brainstorming Sessions Compound Over Time"
postSlug: "how-i-made-my-ai-brainstorming"
description: "Every brainstorm session I run with my AI starts from zero. Here's how I applied Karpathy's LLM Wiki pattern to make design sessions compound over time."
tags:
  - compounding-knowledge
  - design-systems
  - karpathy
  - ai
  - llm-wiki
  - brainstorming
---

Every brainstorm session I run with my AI starts from zero. That's the dirty secret of AI-assisted design work. Each time I sit down to think through a new feature, architecture change, or product decision, the AI knows nothing about what came before. It doesn't remember that we already rejected the microservices approach for this project. It doesn't know that we decided on PostgreSQL over MongoDB three sessions ago. It doesn't even know that a spec document exists for the exact topic we're about to brainstorm.

I have 44 design specification documents sitting in a directory. They represent weeks of thinking, debating, and deciding. And every single one of them is write-only. The next brainstorm session on a related topic has zero awareness of them.

This isn't just inefficient. It's fundamentally broken. And the fix comes from an unexpected source: Andrej Karpathy's approach to building personal knowledge bases with LLMs.

## The Problem: Sessions That Forget

Let me make this concrete. Here's what a typical brainstorm session looks like with my AI system:

🔴 **Session starts** → AI reads project files from scratch
🟠 **Clarifying questions** → AI asks things I've already answered in previous sessions
🟡 **Approach proposals** → AI suggests approaches I've already evaluated and rejected
🟢 **Design iteration** → We eventually converge, but slower than necessary
🔵 **Spec written** → Document saved to disk and never looked at again

Multiply this across 44 design sessions and you see the scale of waste. Each spec contains hard-won knowledge — constraints discovered, trade-offs evaluated, decisions made with reasoning. All of it locked in a markdown file that no future session reads.

The core insight from Karpathy's LLM Wiki pattern is simple but powerful: **your LLM agent should never wake up blank**. The pattern uses a structured wiki with an index, append-only log, and periodic health checks to maintain compounding knowledge. But Karpathy's pattern is about general knowledge management. I needed something more targeted — something that made my brainstorming process itself compound.

## Three Approaches to Compounding Brainstorms

I evaluated three approaches, each with a different philosophy about where knowledge should live.

### Approach A: Wiki-First (Rich Articles per Topic)

The most obvious approach: create a rich wiki article for every brainstorm topic. When a spec is written, compile it into a full wiki page with sections, cross-references, and narrative context. Future sessions read these wiki pages before starting.

This sounds right but has a fatal flaw: **duplication**. You now have two sources of truth — the spec and the wiki article — and they will drift apart. When the spec gets updated, the wiki article doesn't automatically follow. When the wiki article gets enhanced with new context, the spec remains frozen.

The maintenance burden scales linearly with the number of brainstorm topics. At 44 topics, you're maintaining 44 wiki articles alongside 44 specs. That's not compounding — that's overhead.

### Approach B: Index-First (Metadata Stubs)

A lighter approach: instead of full articles, create lightweight metadata stubs that contain just the extracted decisions, constraints, and key question-answer pairs. The full reasoning stays in the spec, referenced by path. A PostgreSQL table enables fast lookup.

This avoids duplication but introduces a different problem: **context fragmentation**. When the AI loads a stub, it gets decisions without reasoning. "Use files over database" is a decision, but without the three paragraphs of trade-off analysis that led to it, the AI can't evaluate whether that decision still holds or whether the context has changed.

It also adds a database dependency for something that could work with files alone. At my scale (~100 knowledge articles), Karpathy's insight holds: LLM navigation via summaries is sufficient. Vector databases introduce more complexity than they solve.

### Approach C: Spec-as-Wiki (The Winner)

The approach I chose: **specs ARE the wiki**. Instead of creating new wiki articles or metadata stubs, the specs themselves become the compounding knowledge base. Here's how:

1. **YAML frontmatter** gets appended to each spec with machine-readable metadata: key decisions, constraints, status, and related topics
2. A single **index file** catalogs all specs with their extracted decisions
3. A **cron job** reads specs, extracts frontmatter, and rebuilds the index daily
4. The **brainstorming skill** reads the index at the start of each session and auto-loads prior context when it finds a matching topic

This approach has a critical property: **zero duplication**. The spec is the source. The index is derived. If they disagree, the spec wins. There's nothing to drift apart because there's only one source of truth.

## How It Actually Works

Let me walk through the concrete implementation. There are five components, each doing one thing well.

### The Spec Frontmatter Convention

Every spec gets a YAML block at the top that looks like this:

The key design choice: **decisions are one-liners**. They're short enough to scan quickly in the index, specific enough to prevent re-exploration. "Use files over database" is too vague. "File-based wiki preferred over RAG at current scale (~100 articles)" is a decision with reasoning attached.

### The Brainstorm Index

A single file catalogs all spec frontmatter. Every topic gets an entry with the spec path, extracted decisions, constraints, status badge, and cross-references. When the AI starts a new brainstorm, it reads this index and looks for the current topic.

The index is rebuilt by a cron job, not maintained manually. This means it's always in sync with the specs (or at most 24 hours out of sync, which is fine for design knowledge).

### The Skill Modifications

The brainstorming skill gets exactly two changes:

**Step 1**: After exploring project files, read the brainstorm index. If the current topic is found, load prior decisions and present them: "Found prior context on [topic]. Previous decisions: X, Y, Z. Shall I treat these as settled, or revisit any?"

**Step 6**: After writing the spec, generate and prepend YAML frontmatter using the decisions and constraints discovered during the session.

Everything else — clarifying questions, approach proposals, design sections, reviews — stays exactly the same. Two surgical modifications. The compounding happens in the background.

### Confidence Badges and Error Mitigation

The biggest risk with compounding AI knowledge is what Karpathy's commenters call "persistent errors compounding" — the AI reads its own mistakes and treats them as truth. This is a real problem, and the solution is straightforward:

Every piece of brainstorm context gets a confidence badge. Draft (Low trust), Auto-compiled (Medium), Verified (High), Contradicted (Do not trust).

The critical design choice: when the brainstorming skill loads prior context at Step 1, it **presents decisions as "previously decided" not "truth"**. The user gets an explicit override point. They can reject a prior decision without the system fighting them.

A weekly lint pass checks for decision contradictions between specs, orphaned topics, and stale entries. It flags issues for human review — it doesn't auto-fix, because design knowledge shouldn't be silently modified by an automated process.

### Day One Bootstrap

The best part of Spec-as-Wiki: the 44 existing specs are an asset, not a liability. On day one, the cron job runs an LLM extraction pass over all existing specs, generates frontmatter for each one, and builds the initial index. The very next brainstorm session has access to all prior design knowledge.

## The Compounding Effect

Here's what changes with this system:

**Before**: Every brainstorm session is an island. 44 specs, zero compounding.

**After**: Every brainstorm session builds on all prior sessions. The AI starts with context — not just file contents, but design decisions, discovered constraints, and the reasoning behind them.

The practical impact is dramatic. When I brainstorm a new feature related to my knowledge engine, the AI already knows:
- We chose file-based storage over RAG (and why)
- We use a contamination boundary between raw and verified knowledge (and what it looks like)
- We build in four phases, each independently valuable (and what each phase delivers)
- The scale threshold where vector databases become worth the complexity (~100 articles)

These aren't facts I need to rediscover. They're decisions that compound.

## Implications for AI-Assisted Design

This pattern generalizes beyond my specific setup. If you're using AI for design work — whether it's architecture decisions, product planning, or system design — you have the same problem:

1. **Your design documents are write-only**. The AI that helped you write them doesn't read them next time.
2. **Your decisions don't compound**. Each session re-explores ground you've already covered.
3. **Your rejected approaches don't persist**. The AI will propose them again next week.

The Spec-as-Wiki pattern fixes all three with minimal infrastructure:
- A frontmatter convention (5 lines of YAML per spec)
- A single index file (derived, never maintained manually)
- A cron job that keeps the index in sync
- Two small changes to your brainstorming workflow

No database. No vector store. No RAG pipeline. Just files, a convention, and a cron job.

Karpathy was right: the right way to use LLMs for knowledge management is to keep it simple. The complexity isn't in the infrastructure. It's in designing the right convention for your use case.

For brainstorming, the right convention is: **specs are the wiki, decisions are one-liners, and the index is derived**. Everything else follows.