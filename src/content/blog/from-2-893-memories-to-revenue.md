---
pubDatetime: 2026-04-11T12:00:00Z
title: "From 2,893 Memories to Revenue: Building a Productised AI Context Audit"
postSlug: "from-2-893-memories-to-revenue"
description: "From 2,893 Memories to Revenue: Building a Productised AI Context Audit"
tags:
  - others
---

I watched a YouTube video last week that changed how I think about my infrastructure. The argument was simple: only 5 structural moats survive AI commoditization — Trust, Context, Distribution, Taste, and Liability. I looked at my server. 58 containers. 91 skills. 2,893 vector memories. A self-improving AI infrastructure that's been running for months. And I realised: **I've already built the moat. I just wasn't selling it.**

## The Context Wall

Every team building AI agents hits the same wall. Your agents produce generic, context-free outputs because there's no systematic way to capture, structure, store, and surface institutional knowledge.

RAG was supposed to fix this. Just connect a vector database, chunk your documents, embed them, and query. Simple. Except RAG only solves the **retrieval** layer — and retrieval is useless if you haven't solved the two layers beneath it.

**Capture**: Before you can retrieve knowledge, you have to capture it from meetings, Slack, code reviews, documentation, research papers, and the accumulated wisdom of everyone who's ever worked at your company. Most teams skip this.

**Structure**: Raw captured knowledge is useless without types, tags, versioning, and progressive disclosure layers. A decision from last week needs different treatment than one from last year.

**Evolution**: Knowledge degrades. Without a self-improvement loop — tracking what's useful, pruning what's stale, evolving schemas — your context engine is a time bomb.

## What We Built Instead

After months of running a self-improving AI infrastructure, we've built something that works differently:

- **2,893+ vector memories** in PostgreSQL + pgvector — typed, tagged, versioned
- **Progressive disclosure** with 5 detail levels (L0 minimal → L4 full reference)
- **Automated ingestion** from multiple sources on cron schedules
- **Signal tracking** that measures what context is actually useful
- **Self-improvement loop** that evolves schemas based on usage patterns

The key insight: **context is not a feature you add. It's infrastructure you build.**

## The Context Maturity Model

We've distilled this into a 5-dimension model that scores any team's AI context infrastructure:

1. **Capture Breadth** (1-5) — How many knowledge sources are connected?
2. **Structure Depth** (1-5) — Is knowledge typed, tagged, and layered?
3. **Storage Quality** (1-5) — How sophisticated is the vector search setup?
4. **Retrieval Accuracy** (1-5) — Can the system find the right context at the right time?
5. **Evolution Loop** (1-5) — Does it improve without manual intervention?

Total score: 5-25. Most teams score 6-10. They have a vector database and basic RAG, but no capture pipelines, no schemas, and no self-improvement.

| Score | Tier | What It Means |
|-------|------|--------------|
| 5-10 | **Critical** | Your agents are operating blind. Urgent action needed. |
| 11-15 | **Developing** | Foundation exists, but gaps are costing quality. |
| 16-20 | **Mature** | Strong base. Time to optimise. |
| 21-25 | **World-class** | Rare. Focus on governance and maintenance. |

## The Product: ContextIQ Audit

Here's the play. We take everything we've learned from running this system daily and package it as a **productised audit service**:

🔴 **Free Context Score** — 5-minute self-assessment, instant results. The lead magnet.

🟠 **Context Scan (£1,500)** — Gap analysis + priority recommendations. 3-5 days.

🟡 **Context Blueprint (£3,500)** — Full audit + architecture + schema library + Docker Compose starter kit. 1-2 weeks.

🟢 **Context Architecture (£7,500)** — Blueprint + 20hrs implementation support + 30-day Slack. 3-4 weeks.

Every tier delivers something concrete: a score, a report, a blueprint, a working starter system. No vague consulting decks. No "we'll get back to you." Battle-tested schemas from a system that's actually running.

## Why This Works As a Business

Three reasons this isn't just another AI consulting pitch:

**1. The moat is the data, not the code.** Anyone can install pgvector. Nobody else has 2,893+ memories with a working ingestion pipeline, progressive disclosure, and self-improvement all running in production on a single server. The patterns are the product.

**2. It compounds.** Every client engagement makes the context engine better. The schemas, ingestion patterns, and progressive disclosure layers are reusable IP. Each audit generates a case study, which generates more leads, which generates more audits.

**3. The staircase is natural.** Context audit leads to implementation support, which leads to a monthly taste optimisation subscription, which leads to governance add-ons. Each step deepens the relationship and increases ARR.

## The Revenue Staircase

```
🔴 Free Context Score → 🟠 Scan (£1.5K) → 🟡 Blueprint (£3.5K)
    → Implementation Support (£5-10K)
    → Taste Engine Subscription (£500-1.5K/mo)
    → Governance Add-on (£1K/mo)
```

Conservative Year 1 projection: £100-140K from audits + subscriptions. The free Context Score tool drives leads automatically. Blog content (like this post) compounds SEO. Each case study proves the model.

## Lessons From the Build

**Lesson 1: Sell the symptom, not the jargon.** Nobody searches for "context infrastructure." They search for "why does my AI keep forgetting things." Lead with the pain.

**Lesson 2: The audit IS the product.** By scoring teams against a maturity model, you're creating a shared language. Once someone knows they're a 9/25, they want to know what 20/25 looks like. That's the upsell.

**Lesson 3: Open-source your schemas.** We're MIT-licensing our memory, context, ingestion, and signal schemas. It builds trust, attracts technical buyers, and makes competitors who copy look derivative.

**Lesson 4: The starter kit sells the blueprint.** A Docker Compose file that gets a basic context engine running in minutes proves the concept. Teams who try it hit the hard parts and think "I wish someone could help with this." That's the paid tier.

**Lesson 5: Every session is content.** This brainstorm session generated a product spec, an implementation plan, 20+ code files, and this blog post. The TELOS principle — "does this make money?" — forces you to ship, not just plan.

## What's Next

The implementation is underway. Maturity model scoring engine, audit checklists, client deliverable schemas, Docker Compose starter kit — all built. The Astro marketing pages and Directus lead capture come next.

If you're reading this and thinking "my team scored about a 7," you're not alone. Take the free Context Score assessment when it launches, or reach out if you want an early audit.

The moat isn't the AI model. It's the context. And we've been building it for months.

**Tags**: ai-infrastructure, context-engineering, product-design, monetization, rag
**Categories**: AI Automation, Business Strategy