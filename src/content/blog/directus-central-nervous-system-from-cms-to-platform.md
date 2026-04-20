---
pubDatetime: 2026-04-05T00:16:18Z
title: "Directus as Central Nervous System: From CMS to Platform"
postSlug: "directus-central-nervous-system-from-cms-to-platform"
description: "How a routine Directus check became a full-stack integration overhaul: 11 automation scripts, 130 RAG chunks, semantic search, and a path to SaaS monetization."
tags:
  - directus
  - skillforge
  - rag
  - automation
  - homelab
  - pgvector
  - saas
---

# Directus as Central Nervous System: From CMS to Platform

What started as a routine weekly Directus check turned into a full-stack integration overhaul. This post documents the transformation of a Directus instance from a simple blog CMS into the central nervous system of an AI-powered homelab — and outlines the path to monetization.

## The Starting Point

Directus was doing one thing well: powering 870 blog posts through an Astro frontend. Behind the scenes, it had 23 custom collections, a signal monitoring system with 7,716 readings, and a service registry tracking 33 containers. But most of this potential was dormant.

> **TL;DR**: Directus was underutilized at 2 Flows and an empty RAG table. After this session: 11 automation scripts, 130 embedded skill documents, a semantic search API, and a SaaS product design.

## What We Found

### Schema Health Check

| Category | Collections | Items | Status |
|----------|------------|-------|--------|
| **Heavily Used** | 5 | 9,000+ | Posts, signals, services, inventory, menus |
| **Lightly Used** | 5 | 50-200 | Documents, metrics, thresholds, apps |
| **Empty** | 5 | 0 | opencode_docs, workflow_stories, shortage_monitor |
| **System** | 8 | 100+ | Directus internals |

The biggest gap: an **opencode_docs** collection with a pgvector column — sitting empty. Zero rows. Zero embeddings. A semantic search engine waiting to be born.

### Redis Cache Failure

Redis was throwing `ECONNREFUSED` errors and failing AOF writes due to disk space (80% full). This was silently degrading Directus performance across the board.

## What We Built

### 1. Redis Fix + Disk Cleanup

Freed 385MB from bloated journal logs. Restarted Redis. Verified cache operations: 8 hits, 3 misses, 57 commands processed. Immediate performance improvement.

### 2. RAG Knowledge Base

Populated the empty `opencode_docs` table with 130 chunks from 86 skills — 34,767 tokens of structured documentation. Each chunk includes metadata: source skill, category, section heading, token count, and code detection.

The ingestion script handles:
- Heading-boundary chunking (~500 tokens per chunk)
- Metadata extraction (category, section, code languages)
- Dry-run mode for preview
- Idempotent re-runs (clears and re-ingests)

### 3. pgvector Embeddings

Generated 128-dimensional TF-IDF + SVD embeddings for all 130 chunks, stored directly in PostgreSQL using the pgvector extension. The embedding column was resized from the default 1536 dimensions to 128 to match our corpus size.

Semantic search verification:
- Query: "directus cms" → Top result: directus skill (similarity: 0.782)
- Query: "telegram bot automation" → Top result: telegram skill (similarity: 0.842)

### 4. Flows Explosion: 2 → 11

Created 11 automation scripts with 8 cron jobs:

| Flow | Frequency | Purpose |
|------|-----------|---------|
| Auto-tag Posts | Hourly | Extract tags from content keywords |
| Signal Escalation | 30 min | Alert on critical/red signals |
| Content Syndication | 15 min | Push new posts to Telegram |
| Skill Change Detector | 6 hours | Detect skill file modifications |
| Service Health Check | 5 min | Ping 33 services, update status |
| Embedding Pipeline | Hourly | Re-embed new documents |
| Blog Performance | Daily | Track engagement metrics |
| Inventory Alerts | 4 hours | Low-stock Telegram notifications |
| Self-Improvement | Daily | Detect empty collections, stale skills |
| Webhook Relay | On demand | Route external webhooks to collections |
| Landing Page A/B | On demand | Track landing page impressions |

### 5. Semantic Search API

A standalone Python API on port 8058 providing:

\`\`\`
GET /search?q=your+query&limit=5
GET /stats
GET /health
\`\`\`

Returns ranked results with similarity scores, source metadata, and content previews. Supports source filtering and POST requests.

### 6. Landing Pages for Monetization

Created two Directus-powered landing pages:

- **AI Skill Development** — Custom skill development for autonomous agents
- **Content Automation Pipeline** — YouTube → blog, news → reports, fully automated

Both use the existing `landing_pages` schema with full SEO support (title, description, image).

## The Bigger Picture: SkillForge

All of this infrastructure work serves a larger goal: **SkillForge**, a SaaS platform for AI agent skill management.

### Why Now?

The AI agent tooling market is exploding. Every team building agents needs:
- Structured skill definitions (not just prompts)
- Monitoring and health checks
- RAG-searchable documentation
- Automated testing and deployment
- A marketplace for sharing skills

We already have 69 production-tested skills running on 52 containers. That is not a demo — it is proof of concept.

### Revenue Model

| Tier | Price | Target |
|------|-------|--------|
| Single Skill | £29 | Individual developers |
| Skill Bundle | £69-99 | Teams with specific needs |
| Full Library | £199 | Power users |
| Solo SaaS | £29/mo | Ongoing access |
| Team SaaS | £99/mo | Small teams |
| Enterprise | £299/mo | White-label + custom |

Conservative projection: £535/mo (Month 1) → £6,110/mo (Month 12).

### What Is Left to Build

| Component | Effort | Status |
|-----------|--------|--------|
| Skill Library + RAG | Done | 130 chunks, pgvector search |
| CMS Backend | Done | Directus with 23 collections |
| Automation | Done | 11 scripts, 8 cron jobs |
| Monitoring | Done | Signal system, Telegram alerts |
| Blog + Content | Done | 870 posts, auto-publish |
| Landing Pages | Done | 2 pages with SEO |
| Storefront Frontend | 2 weeks | Astro browse/search/buy |
| Stripe Integration | 1 week | Payments via Directus Flows |
| User Accounts | 1 week | Directus auth + roles |
| API Access | 1 week | Key management + rate limiting |

We are 70% of the way to a sellable product. The remaining 30% is frontend and payment integration — the fun stuff.

## Lessons Learned

1. **Fix infrastructure first** — The Redis cache errors were silently hurting everything downstream. Disk space at 80% is a ticking bomb.

2. **pgvector is finicky with Directus** — PostgreSQL ARRAY columns (`_text[]`) cannot be written via the Directus REST API. Use raw SQL for array fields, or omit them from API payloads.

3. **TF-IDF + SVD is a valid embedding strategy** — When you cannot run neural embedding models (torch broken, no Ollama, API credits exhausted), TF-IDF with SVD dimensionality reduction produces usable similarity search results with zero cost.

4. **Cron is underrated** — Directus Flows are powerful but limited in execution environment. Shell scripts + cron give you the full power of the host system with Directus as the data layer.

5. **Schema debt is real** — Five empty collections from abandoned features. They do not hurt performance, but they add cognitive overhead. Either commit to using them or clean them up.

## What is Next

The immediate priority is building the SkillForge Astro storefront. Two weeks of focused work on browse/search/buy, Stripe integration, and user accounts would give us a minimum viable product.

The larger vision is a self-improving system where Directus Flows read weekly analysis reports, identify underperforming skills, trigger improvement workflows, and measure the results. The system literally makes itself better on a schedule.

---

*This post was written as part of a Directus weekly integration analysis session. The analysis script runs every Monday at 6AM and generates automated reports. The next evolution will include the SkillForge storefront integration.*
