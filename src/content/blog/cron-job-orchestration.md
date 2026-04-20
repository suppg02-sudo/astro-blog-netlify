---
pubDatetime: 2026-03-07T13:15:00Z
title: "Cron Job Orchestration: 18 Automated Tasks Powering This Server"
postSlug: "cron-job-orchestration"
description: "Cron Job Orchestration: 18 Automated Tasks Powering This Server"
tags:
  - Automation
  - Server Management
  - Cron
  - Self-Hosted
---

## Overview

This server runs **18 automated cron jobs** that handle everything from memory management to blog post generation. This post provides a complete inventory of all scheduled tasks, their outputs, and current status.

## Complete Cron Job Inventory

| # | Schedule | Script | Blog Post? | Output | Status |
|---|----------|--------|------------|--------|--------|
| 1 | Every 5 min | `automation-health-monitor.py` | No | Health metrics JSON | ✅ Running |
| 2 | Every 15 min | `openmemory-wal-monitor.sh` | No | WAL checkpoint triggers | ✅ Running |
| 3 | Every 15 min | `automation-alerts.py` | No | Alert notifications | ✅ Running |
| 4 | Every 8 hours | `memory-report.py` | No | Memory stats + Hugo rebuild | ✅ Running |
| 5 | Hourly | `hourly-issue-monitor.sh` | No | Issue tracking log | ✅ Running |
| 6 | Hourly | `automation-predictive.py` | No | Predictive analytics | ✅ Running |
| 7 | Daily @ 03:00 | `overnight_indexing.py` | No | OpenMemory indexing | ✅ Running |
| 8 | Daily @ 06:00 | `daily_research_analysis.py` | **Yes** | AI ecosystem research post | ✅ Running |
| 9 | Daily @ 06:15 | `daily_memos_analysis.py` | **Yes** | Memos digest post | ✅ Running |
| 10 | Daily @ 06:30 | `analyze_menus.py` | **Yes** | Menu analytics post | ✅ Running |
| 11 | Daily @ 06:45 | `daily_prompt_extraction.py` | **Yes** | Prompt patterns post | ✅ Running |
| 12 | Daily @ 07:00 | `weekly_webserver_report.py` | No | Webserver stats log | ✅ Running |
| 13 | Daily @ 07:30 | `cron-report.sh` | No | Cron summary log | ✅ Running |
| 14 | Daily @ 07:45 | `flow-report.sh` | No | Flow analysis log | ✅ Running |
| 15 | Weekly Mon @ 06:00 | `directus-weekly-report` | No | Directus analytics log | ✅ Running |
| 16 | Weekly Sun @ 08:00 | `blog-weekly-analyzer` | No | Blog stats log | ✅ Running |
| 17 | Weekly Sun @ 08:00 | `weekly_ecosystem_digest.py` | **Yes** | Weekly digest post | ✅ Running |

## Context Type Monitoring

Cron jobs grouped by what context types they monitor/analyze:

### 🔄 Flows (2 Jobs)

| Script | Schedule | What It Monitors |
|--------|----------|------------------|
| `flow-report.sh` | Daily @ 07:45 | Flow activity, delegation patterns, action tracking |
| `weekly_ecosystem_digest.py` | Weekly Sun 08:00 | Aggregates daily research flows into weekly digest |

### 🎯 Question Tool / Menus (2 Jobs)

| Script | Schedule | What It Monitors |
|--------|----------|------------------|
| `analyze_menus.py` | Daily @ 06:30 | Menu conflicts, inheritance issues, central menu compliance |
| `daily_research_analysis.py` | Daily @ 06:00 | Question tool research sessions, menu choices |

### 📝 Prompts / Skills (1 Job)

| Script | Schedule | What It Monitors |
|--------|----------|------------------|
| `daily_prompt_extraction.py` | Daily @ 06:45 | Extracts prompts from sessions, categorizes by type (cron, research, troubleshooting, workflows, quick_actions, architecture) |

### 💾 Memory / Sessions (3 Jobs)

| Script | Schedule | What It Monitors |
|--------|----------|------------------|
| `daily_memos_analysis.py` | Daily @ 06:15 | Memos tags, todos, pinned items, OpenMemory sync |
| `overnight_indexing.py` | Daily @ 03:00 | OpenMemory semantic indexing |
| `memory-report.py` | Every 8 hours | Memory statistics, session counts |

### 🌐 Webserver / Infrastructure (3 Jobs)

| Script | Schedule | What It Monitors |
|--------|----------|------------------|
| `weekly_webserver_report.py` | Daily @ 07:00 | Webserver access logs, traffic patterns |
| `directus-weekly-report` | Weekly Mon 06:00 | Directus CMS usage, collections, API calls |
| `blog-weekly-analyzer` | Weekly Sun 08:00 | Blog post stats, popular content |

### 🤖 System Health (5 Jobs)

| Script | Schedule | What It Monitors |
|--------|----------|------------------|
| `automation-health-monitor.py` | Every 5 min | Docker containers, service health |
| `automation-alerts.py` | Every 15 min | Failure detection, error alerts |
| `automation-predictive.py` | Hourly | Predictive failure analysis |
| `openmemory-wal-monitor.sh` | Every 15 min | SQLite WAL checkpoint status |
| `cron-report.sh` | Daily @ 07:30 | Cron job health, log sizes |

## Blog Post Generators (5 Jobs)

These cron jobs automatically create Hugo blog posts:

| Script | Schedule | Blog Post Type |
|--------|----------|----------------|
| `daily_research_analysis.py` | Daily 06:00 | AI ecosystem research with GitHub stats |
| `daily_memos_analysis.py` | Daily 06:15 | Memos notes digest and analysis |
| `analyze_menus.py` | Daily 06:30 | Question tool menu analytics |
| `daily_prompt_extraction.py` | Daily 06:45 | Extracted prompt patterns |
| `weekly_ecosystem_digest.py` | Weekly Sun 08:00 | Aggregated weekly research |

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    CRON ORCHESTRATION                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │  MONITORING  │  │   CONTENT    │  │   MEMORY     │       │
│  │  (5 jobs)    │  │  (5 jobs)    │  │  (3 jobs)    │       │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘       │
│         │                 │                 │                │
│         v                 v                 v                │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │ Alert System │  │ Hugo Blog    │  │ OpenMemory   │       │
│  │              │  │ /posts/      │  │ SQLite DB    │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │    FLOWS     │  │    MENUS     │  │   PROMPTS    │       │
│  │  (2 jobs)    │  │  (2 jobs)    │  │  (1 job)     │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Log File Sizes

Current log storage usage:

| Log File | Size |
|----------|------|
| `youtube-channel-processor.log` | 22 MB |
| `opencode-web.log` | 2.7 MB |
| `automation-health.log` | 808 KB |
| `automation-predictive.log` | 68 KB |

## How to View Logs

```bash
# View all cron logs
ls -la /root/cron-logs/

# Check specific job log
tail -50 /root/cron-logs/automation-health.log

# Run cron reporter manually
/root/scripts/cron-reporter/cron-report.sh

# Run flow reporter manually
/root/scripts/flow-reporter/flow-report.sh
```

## Key Insights

- **5 automated blog posts** generated daily/weekly
- **All 18 jobs currently running** without errors
- **Total log storage**: ~26 MB
- **Most frequent**: Health monitor (every 5 min)
- **Most valuable**: Daily research posts with AI ecosystem tracking

### Context Type Coverage

| Context Type | Jobs | Primary Output |
|--------------|------|----------------|
| **Flows** | 2 | Flow reports, weekly digests |
| **Question Tool / Menus** | 2 | Menu analytics, research posts |
| **Prompts / Skills** | 1 | Prompt pattern extraction |
| **Memory / Sessions** | 3 | Indexing, memos sync, stats |
| **Infrastructure** | 3 | Webserver, Directus, blog stats |
| **System Health** | 5 | Monitoring, alerts, predictions |

---

*This post was generated from the cron job inventory. Last updated: 2026-03-07*