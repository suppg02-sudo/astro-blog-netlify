---
pubDatetime: 2026-04-20T10:54:10Z
title: "Building an Automated Content Scraping Pipeline with Signals"
postSlug: "building-automated-content-scraping-pipeline"
description: "Building an Automated Content Scraping Pipeline with Signals"
tags:
  - scrape
  - automation
  - pipeline
  - signals
  - ai-infrastructure
---

# Building an Automated Content Scraping Pipeline with Signals

> **TL;DR**: We built a self-improving content scraping skill that ingests from YouTube, RSS, Reddit, and Substack daily, generates relevance signals tied to active projects, and publishes contextualised content as blog posts — all running unattended on cron.

## Why We Built This

Our OpenCode AI infrastructure had a gap: every content tool required human initiation. Paste a URL, type a trigger, start a session. Meanwhile, valuable content from AI blogs, Reddit discussions, and YouTube channels flowed past unintercepted.

The scrape skill closes that gap by running **automated, background collection** while we sleep.

## The Architecture

The system follows a clean 8-stage pipeline:

1. **LOAD** — Read active sources from PostgreSQL
2. **FETCH** — Each adapter fetches new items (rate-limited)
3. **DEDUPE** — SHA256 hash prevents duplicates
4. **CLASSIFY** — Weighted relevance scoring
5. **STORE** — Insert into `scrape_items` table
6. **SIGNAL** — Generate signals for the auto-improvement triad
7. **INTEGRATE** — Feed signals to memory, ideas, attention
8. **PUBLISH** — Approved items become blog posts

## The Adapter Pattern

Each source type implements a common Python interface:

```python
class BaseAdapter(ABC):
    async def fetch(self, config, since) -> list[RawItem]: ...
    def parse(self, raw_data) -> RawItem: ...
    @property
    def rate_limit(self) -> tuple[int, int]: ...
```

Adapters self-register via a decorator pattern. Adding a new source type means one new file — no changes to the core pipeline.

We built five adapters:

| Adapter | Method | Key Detail |
|---------|--------|------------|
| RSS | feedparser | Universal fallback |
| YouTube | yt-dlp via MeTube | No API key needed |
| Substack | RSS + curl full-text | Dual-pass extraction |
| Reddit | JSON API | No auth for public subs |
| Web | curl + regex | CSS selector support |

## Signal Generation: The Triad Connection

The core insight: scraped content is worthless without context. We tie every item to our **Schema → Signal → Auto-Improvement** triad through six signal types:

- **project_match** — Keywords overlap with active project scope/intent
- **trending** — Engagement metrics exceed thresholds
- **opportunity** — TELOS income keywords detected
- **blog_candidate** — High relevance + suitable content type
- **source_health** — Auto-pause failing sources
- **content_volume** — Detect anomalies in daily item count

The relevance scorer uses weighted signals: source tags (35%), AI keywords (20%), TELOS income keywords (15%), infrastructure keywords (15%), engagement metrics (5%).

## Blog Publishing Bridge

Approved items flow through the existing Astro/Directus pipeline:

```
scrape_items (approved) → AI contextualisation → Directus API → Astro blog (200 verified)
```

Each published post gets tagged with `scrape` + source type + original tags. The validation gate ensures `date_published` is set (the #1 cause of 404s in our Astro setup).

## Schema Design

Five PostgreSQL tables in our existing `memory_db`:

| Table | Purpose |
|-------|---------|
| `scrape_sources` | Configured sources with type, tags, schedule |
| `scrape_items` | Individual scraped content with relevance scores |
| `scrape_jobs` | Audit trail for every run |
| `scrape_signals` | Feeds the auto-improvement triad |
| `scrape_approvals` | Human/auto approval decisions |

## Live Results

After 24 hours with 4 sources:

- 99 items scraped
- 100 signals generated (project_match, opportunity, blog_candidate)
- 1 blog post published
- 13/13 jobs successful, 0 errors
- 8 active projects matched

## What's Next

- Twitter/X adapter (Nitter bridge — fragile but free)
- FreshRSS integration for RSS dedup
- Prometheus metrics + Grafana dashboard
- Auto-approval rules engine for high-confidence items
- Weekly "Scrape Intelligence Report" auto-published blog post

## The Revenue Angle

This isn't just a hobby project. The scraping pipeline supports multiple income paths:

- **Curated newsletter** — Weekly intelligence report auto-published with `public` tag
- **Premium content gate** — Internal blog has everything, public blog has highlights
- **Consulting authority** — Regular ecosystem analysis establishes expertise
- **Data products** — "State of AI Agents Q2 2026" style reports from aggregated data

The scrape skill embodies a principle: **automated collection + intelligent filtering + strategic publishing = compounding knowledge assets**.

**Tags**: scrape, automation, pipeline, signals, ai-infrastructure, content-ingestion
