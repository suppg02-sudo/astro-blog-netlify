---
pubDatetime: 2026-04-03T13:29:47Z
title: "System Roundup — April 2026"
postSlug: "system-roundup-april-2026"
description: "System Roundup — April 2026"
tags:
  - others
---

A comprehensive health check of the AImplifi personal AI platform — a self-hosted server running 52 Docker containers, 69 AI skills, and serving 842 blog posts. Here's what the numbers look like and what they mean.

> **TL;DR**: Platform is healthy. 81% roadmap complete, disk at 80%, zero OOM events in 24h, daily content pipeline auto-publishing.

## Quick Summary

- **52 containers** running (9 stopped — OpenRAG, Langflow, OpenSearch, Clipable intentionally offline)
- **69 AI skills** across 62 domain clusters
- **842 blog posts** published via Directus CMS
- **1,520 memories** in PostgreSQL + pgvector knowledge base
- **Roadmap**: 9/11 items complete (81%)
- **Daily evolve report** auto-publishes every morning at 06:00 UTC

## System Performance

| Metric | Value | Status |
|--------|-------|--------|
| Uptime | 3h 18m (recent reboot) | ✅ |
| CPU Load | 0.87 | ✅ |
| Memory | 5.5/7.7 GiB (71%) | ⚠️ Moderate |
| Swap | 2.2/4.0 GiB (55%) | ⚠️ High |
| Disk | 80% (24G free of 116G) | ✅ |
| OOM Events (24h) | 0 | ✅ |

### Top Memory Consumers

| Container | Memory | Notes |
|-----------|--------|-------|
| Neo4j | 1.0 GiB | Graph database for research |
| Hugo | 414 MiB | Legacy blog (Astro is primary) |
| Astro Blog | 306 MiB | Primary blog (Directus-backed) |
| n8n | 226 MiB | Workflow automation |
| Directus | 213 MiB | Headless CMS |

## The Pipeline

The server runs a daily content pipeline that runs automatically:

🔴 `Daily Report` → 🟠 `Directus Publish` → 🟡 `Astro Restart` → 🟢 `Live on Blog` → ✅ `Done`

### Active Cron Jobs

| Schedule | Job | Purpose |
|----------|-----|---------|
| 06:00 daily | Daily Work Analysis | Generates evolve report, publishes to blog |
| 06:30 daily | Menu Analysis | Analyzes menu patterns across skills |
| 07:30 daily | Cron Reporter | Reports on cron job health |
| 07:45 daily | Flow Reporter | Reports on flow tracking |
| 08:00 daily | AI News Research | Fetches and processes AI news |
| Every 5 min | Automation Health | Monitors system health |
| Every 15 min | Automation Alerts | Checks for failures |
| Monday 06:00 | Directus Weekly | CMS analytics report |

## Roadmap Progress

**Overall: 9/11 items complete (81%)**

| Status | Count | Items |
|--------|-------|-------|
| ✅ Completed | 9 | Memory cleanup, Hub & Spoke (x2), Agentsys skills, Core principles, KC blog series, Roadmap cron, Flow tracking (wontfix), MoneyPrinter2 |
| 📋 Planned | 2 | Skill Metadata Schema (low priority), Interactive Content (medium priority) |

### Recent Completions

- **Daily Evolve Report → Blog**: Auto-publishes daily analysis as blog posts
- **MoneyPrinter2**: Content generation pipeline with 8 research runs completed
- **Flow Tracking**: Closed as wontfix — intent achieved via cron + skills + AGENTS.md orchestration
- **AGENTS.md Hub & Spoke**: Reduced from 1,637 to 293 lines (5.6x reduction)

## Known Issues

Three minor issues found in this roundup:

| Issue | Severity | Status |
|-------|----------|--------|
| `system-coherence` script references missing `memories` table | Low | Needs schema fix |
| `market-news-cron` has stale Hugo service references | Low | Blog uses Astro now |
| `automation-health.log` counting 91 non-critical errors | Low | Mostly session.yaml warnings |

None are blocking. All are cosmetic or legacy reference issues.

## Architecture

The platform follows three core patterns:

1. **Factory Pattern** — skill-factory, project-factory, and menu-factory each operate as independent control planes with their own validation, lifecycle, and governance
2. **Progressive Disclosure** — documentation in layers (L0 minimal → L4 full reference), loading only what's needed
3. **Schema-First Design** — structured, typed, validated data over freeform text

### The TELOS

Every decision is filtered through one question: **does this make money?** Revenue-generating work and monetisable assets are prioritised. The platform isn't just technically elegant — it's commercially focused.

**Tags**: roundup, system-health, platform, docker, self-hosting, automation