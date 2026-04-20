---
pubDatetime: 2026-04-05T00:31:40Z
title: "Complete Cron Jobs Inventory — 31 Scheduled Tasks on My AI Infrastructure"
postSlug: "complete-cron-jobs-inventory-3"
description: "Complete Cron Jobs Inventory — 31 Scheduled Tasks on My AI Infrastructure"
tags:
  - others
---

A full audit of every cron job running on my server — 31 active tasks across 10 categories, with health analysis, log bloat warnings, and optimisation opportunities.

## Quick Summary

- **31 active jobs** across 10 functional categories
- **5 deprecated** jobs commented out (replaced by attention pipeline)
- **8 missing log files** — scripts running but not capturing output
- **22MB log bloat** in automation-health.log needs rotation
- **5 high-frequency jobs** running every 5-15 minutes
- **Cron service**: ✅ healthy, running since 2026-04-04

## Full Inventory

### Attention Pipeline (4 jobs)

The attention pipeline consolidates research, news, and blog generation into scheduled workflows.

| Schedule | Script | Log | Status |
|----------|--------|-----|--------|
| Daily 08:00 | `run-scheduled-research.sh daily-ai-news` | attention-daily.log | ✅ Active |
| Sunday 08:00 | `run-scheduled-research.sh weekly-ecosystem` | attention-weekly-ecosystem.log | ✅ Active |
| Tuesday 09:00 | `run-scheduled-research.sh weekly-rag-developments` | attention-weekly-rag.log | ✅ Active |
| 1st of month 08:00 | `run-scheduled-research.sh monthly-agent-tools` | attention-monthly.log | ⚠️ Empty log |

### Market & Research (2 jobs)

| Schedule | Script | Log | Status |
|----------|--------|-----|--------|
| Daily 07:00 | `run-market-news.sh` | market-news-cron.log | ✅ Active |
| Daily 08:00 | `run-scheduled-research.sh daily-oss-releases` | attention-daily-oss.log | ✅ Active |

### Analysis (3 jobs)

| Schedule | Script | Log | Status |
|----------|--------|-----|--------|
| Daily 06:30 | `analyze_menus.py` | daily-menu-analysis.log | ✅ Active |
| Daily 05:00 | `system-coherence-analysis.py` | system-coherence.log | ✅ Active |
| Daily 06:00 | `run-daily-work-analysis.sh` | daily-work-analysis-cron.log | ⚠️ Minimal output |

### Monitoring & Alerts (5 jobs)

These are the highest-frequency jobs, running every 5-30 minutes.

| Schedule | Script | Log | Status |
|----------|--------|-----|--------|
| Every 5 min | `automation-health-monitor.py` | automation-health.log | 🔴 22MB bloat |
| Every 15 min | `automation-alerts.py` | automation-alerts.log | ✅ 385KB |
| Every 15 min | `openmemory-wal-monitor.sh` | wal-monitor.log | ✅ 53KB |
| Every 5 min | `service-health-checker.sh` | health-check.log | ⚠️ Empty |
| Every 30 min | `signal-alert-telegram.sh` | signal-alerts.log | ⚠️ Empty |

### Reports (2 jobs)

| Schedule | Script | Log | Status |
|----------|--------|-----|--------|
| Daily 07:30 | `cron-report.sh` | cron-report.log | ✅ Active |
| Daily 07:45 | `flow-report.sh` | flow-report.log | ✅ Active |

### Directus Flows (8 jobs)

Content management and CMS automation pipelines.

| Schedule | Script | Log | Status |
|----------|--------|-----|--------|
| Hourly :00 | `auto-tag-posts.sh` | auto-tag-posts.log | 🔴 Missing |
| Every 15 min | `content-syndication.sh` | content-syndication.log | ⚠️ Empty |
| Every 6 hours | `skill-change-detector.sh` | skill-changes.log | 🔴 Missing |
| Hourly :30 | `embedding-pipeline.sh` | embedding-pipeline.log | ⚠️ Empty |
| Daily 02:00 | `blog-performance-tracker.sh` | blog-perf.log | 🔴 Missing |
| Every 4 hours | `inventory-low-stock.sh` | inventory-low.log | 🔴 Missing |
| Daily 07:00 | `self-improvement-engine.sh` | self-improve.log | 🔴 Missing |
| Every 5 min | `service-health-checker.sh` | health-check.log | ⚠️ Empty |

### Infrastructure (2 jobs)

| Schedule | Script | Log | Status |
|----------|--------|-----|--------|
| Daily 01:00 | `log_rotation.sh` | log-rotation.log | ✅ Active |
| Monday 06:00 | `run-weekly.sh` (Directus) | directus-weekly.log | 🔴 Missing |

### Weekly Reviews (4 jobs)

| Schedule | Script | Log | Status |
|----------|--------|-----|--------|
| Sunday 08:00 | `run-weekly.sh` (blog analyzer) | blog-weekly.log | 🔴 Missing |
| Sunday 09:00 | `run-review.sh` (factory) | factory-review.log | ✅ Active |
| Sunday 10:00 | `run-audit.sh` (doc audit) | doc-audit.log | ✅ Active |
| Daily 08:00 | `inventory-reorder-check.sh` | inventory-reorder.log | 🔴 Missing |

### Boot (1 job)

| Schedule | Script | Log | Status |
|----------|--------|-----|--------|
| @reboot | `semantic-search-api.py` | semantic-search.log | ✅ 290B |

### Deprecated (3 jobs — commented out)

These were replaced by the attention pipeline consolidation on 2026-04-01.

| Schedule | Script | Replacement |
|----------|--------|-------------|
| Daily 06:00 | `daily_research_analysis.py` | attention-daily |
| Daily 08:00 | `generate-post.sh` | attention pipeline |
| Sunday 08:00 | `weekly_ecosystem_digest.py` | weekly-ecosystem |

## Issues & Recommendations

### Critical

1. **Log bloat**: `automation-health.log` is **22MB** — the log rotation script runs daily at 01:00 but isn't catching this file. Either the rotation config excludes it or the script has a bug.

2. **Missing log files**: 8 jobs reference log files that don't exist on disk. The scripts may be failing silently or the log directory permissions are wrong.

### Warnings

3. **Schedule collision**: Three jobs fire at 08:00 daily (daily-ai-news, daily-oss-releases, inventory-reorder-check). Staggering them by 5-10 minutes would reduce resource contention.

4. **High-frequency overlap**: 5 jobs run every 5-15 minutes. Consider whether all need this frequency — the health checker and signal alerts could potentially run every 10 minutes instead of 5.

5. **Empty logs**: Several jobs produce no output (health-check, content-syndication, embedding-pipeline, signal-alerts). These scripts may need `set -x` or explicit echo statements to confirm execution.

## System Health

```
Cron service: active (running)
Uptime: since 2026-04-04 16:35:01 UTC
Total jobs: 31 active + 3 deprecated
Log directory: /root/cron-logs/ (24MB total)
```

**Tags**: cron, infrastructure, automation, monitoring, devops, system-administration
**Categories**: Infrastructure, Automation