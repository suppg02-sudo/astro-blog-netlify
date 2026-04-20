---
pubDatetime: 2026-03-07T00:00:00Z
title: "Cron Job Naming Convention Migration"
postSlug: "cron-job-naming-convention-migration"
description: "Migrated 20 cron jobs to a standardized naming convention with organized directory structure, fixing duplicate entry issue."
tags:
  - naming-convention
  - system-administration
  - cron
  - automation
  - server-management
---

After months of organic growth, our server's cron job collection had become unwieldy—21 jobs scattered across multiple directories with inconsistent naming, Duplicate entries existed. Log files didn't match script names. It was time for a systematic overhaul.

## The Problem

Our original crontab looked like this:

```cron
0 * * * * /root/scripts/hourly-issue-monitor.sh >> /root/cron-logs/hourly-monitor.log 5>&1
*/15 * * * * /root/scripts/openmemory-wal-monitor.sh
0 */8 * * * /usr/bin/python3 /root/.config/opencode/scripts/memory-report.py --quiet >> /root/cron-logs/memory-report.log 2>&1
# ... 18 more lines of similar chaos
```

Issues identified

| Problem | Count |
|--------|-------|
| Inconsistent separators | Mix of `_` and `-` |
| Scattered paths | Scripts in `/root/scripts/`, `/root/.config/opencode/scripts/`, subdirectories |
| Log naming mismatch | `hourly-monitor.log` for `hourly-issue-monitor.sh` |
| Duplicate entries | `overnight_indexing.py` ran twice with different logs |
| No categorization | All jobs in a flat list |

## The Solution: Standardized Naming Convention

### Format

```
{category}-{frequency}-{name}.{ext}
```

### Categories

| Prefix | Category | Purpose |
|--------|----------|---------|
| `mon-` | Monitor | Health checks, status monitoring, alerts |
| `ana-` | Analysis | Reporting, analytics, pattern detection |
| `mem-` | Memory | OpenMemory operations, indexing, cleanup |
| `cnt-` | Content | Blog posts, content generation, publishing |

### Frequency Codes

| Code | Schedule | Example |
|------|----------|---------|
| `m5` | Every 5 minutes | `*/5 * * * *` |
| `m15` | Every 15 minutes | `*/15 * * * *` |
| `h1` | Hourly | `0 * * * *` |
| `h8` | Every 8 hours | `0 */8 * * *` |
| `d` | Daily | `0 X * * *` |
| `w` | Weekly | `0 X * * X` |

## Directory Structure

Before: scattered across multiple locations
After: organized by category

```
/root/scripts/
├── monitor/           # 5 scripts
│   ├── mon-m5-health.py
│   ├── mon-m15-wal.sh
│   ├── mon-m15-alerts.py
│   ├── mon-h1-issue.sh
│   └── mon-h1-predictive.py
│
├── analysis/          # 9 scripts
│   ├── ana-d-research.py
│   ├── ana-d-memos.py
│   ├── ana-d-menus.py
│   ├── ana-d-prompts.py
│   ├── ana-d-coherence.py
│   ├── ana-d-cron-report.sh
│   ├── ana-d-flow-report.sh
│   ├── ana-w-webserver.py
│   └── ana-w-ecosystem.py
│
├── memory/            # 4 scripts
│   ├── mem-h8-report.py
│   ├── mem-d-index.py
│   ├── mem-d-wal-checkpoint.sh
│   └── mem-d-wal-fix.sh
│
└── content/           # 4 scripts
    ├── cnt-d-cron-post.sh
    ├── cnt-d-research-post.py
    ├── cnt-w-blog.sh
    └── cnt-w-directus.sh
```

## The New Crontab

```cron
# ============================================
# CRON JOBS - Organized by Category & Frequency
# ============================================

# --- MONITORING (mon-) ---
*/5 * * * * /root/scripts/monitor/mon-m5-health.py >> /root/cron-logs/mon-m5-health.log 2>&1
*/15 * * * * /root/scripts/monitor/mon-m15-wal.sh >> /root/cron-logs/mon-m15-wal.log 2>&1
*/15 * * * * /root/scripts/monitor/mon-m15-alerts.py >> /root/cron-logs/mon-m15-alerts.log 2>&1
0 * * * * /root/scripts/monitor/mon-h1-issue.sh >> /root/cron-logs/mon-h1-issue.log 2>&1
0 * * * * /root/scripts/monitor/mon-h1-predictive.py >> /root/cron-logs/mon-h1-predictive.log 2>&1

# --- MEMORY (mem-) ---
0 */8 * * * /root/scripts/memory/mem-h8-report.py --quiet >> /root/cron-logs/mem-h8-report.log 2>&1
0 3 * * * /usr/bin/python3 /root/scripts/memory/mem-d-index.py >> /root/cron-logs/mem-d-index.log 2>&1

# --- ANALYSIS (ana-) ---
0 6 * * * /usr/bin/python3 /root/scripts/analysis/ana-d-research.py >> /root/cron-logs/ana-d-research.log 2>&1
15 6 * * * /usr/bin/python3 /root/scripts/analysis/ana-d-memos.py >> /root/cron-logs/ana-d-memos.log 2>&1
30 6 * * * /usr/bin/python3 /root/scripts/analysis/ana-d-menus.py >> /root/cron-logs/ana-d-menus.log 2>&1
45 6 * * * /usr/bin/python3 /root/scripts/analysis/ana-d-prompts.py >> /root/cron-logs/ana-d-prompts.log 2>&1
0 5 * * * /usr/bin/python3 /root/scripts/analysis/ana-d-coherence.py >> /root/cron-logs/ana-d-coherence.log 2>&1
30 7 * * * /root/scripts/analysis/ana-d-cron-report.sh >> /root/cron-logs/ana-d-cron-report.log 2>&1
45 7 * * * /root/scripts/analysis/ana-d-flow-report.sh >> /root/cron-logs/ana-d-flow-report.log 2>&1
0 7 * * 1 /usr/bin/python3 /root/scripts/analysis/ana-w-webserver.py >> /root/cron-logs/ana-w-webserver.log 2>&1
0 8 * * 0 /usr/bin/python3 /root/scripts/analysis/ana-w-ecosystem.py >> /root/cron-logs/ana-w-ecosystem.log 2>&1

# --- CONTENT (cnt-) ---
0 8 * * * /root/scripts/content/cnt-d-cron-post.sh >> /root/cron-logs/cnt-d-cron-post.log 2>&1
0 8 * * 0 /root/scripts/content/cnt-w-blog.sh >> /root/cron-logs/cnt-w-blog.log 2>&1
0 6 * * 1 /root/scripts/content/cnt-w-directus.sh >> /root/cron-logs/cnt-w-directus.log 2>&1
```

## Migration Results

| Metric | Before | After |
|--------|--------|-------|
| Total cron jobs | 21 (with 1 duplicate) | 20 (fixed) |
| Directory structure | Flat, scattered | Organized by category |
| Naming convention | Inconsistent | Standardized |
| Log file names | Mixed formats | Match script names |
| Duplicate entries | 1 (`overnight_indexing.py`) | 0 |

## Jobs by Category

| Category | Count | Purpose |
|----------|-------|---------|
| Monitor | 5 | Health checks, WAL monitoring, alerts, predictive analysis |
| Analysis | 9 | Daily reports, menu analysis, flow reports, weekly digests |
| Memory | 2 | OpenMemory reporting and overnight indexing |
| Content | 3 | Blog posts, cron orchestration, Directus reports |

## Key Improvements

### 1. Fixed Duplicate Entry

The `overnight_indexing.py` script was running twice daily at 3 AM with different log files. Now it runs once as `mem-d-index.py`.

### 2. Consistent Log Naming

Before: `hourly-monitor.log` for `hourly-issue-monitor.sh`
After: `mon-h1-issue.log` for `mon-h1-issue.sh`

### 3. Category Organization

Finding related scripts is now trivial

```bash
# All monitoring scripts
ls /root/scripts/monitor/
# mon-m5-health.py  mon-m15-alerts.py  mon-m15-wal.sh  ...

# All analysis scripts
ls /root/scripts/analysis/
# ana-d-research.py  ana-d-menus.py  ...
```

### 4. Self-Documenting Names

The filename tells you everything

- `mon-m5-health.py` → Monitor, every 5 minutes, health check
- `ana-w-ecosystem.py` → Analysis, weekly, ecosystem digest
- `cnt-d-cron-post.sh` → Content, daily, cron post

## Verification

After migration, all scripts were tested

```bash
# Monitor scripts work
bash /root/scripts/monitor/mon-m15-wal.sh
# [2026-03-07T15:40:23+00:00] WAL size: 5MB
# [2026-03-07T15:40:23+00:00] WAL size under 10MB, no action needed

# Memory scripts work
python3 /root/scripts/memory/mem-h8-report.py --quiet
# OpenMemory Report: 1152 memories, score=100/100

# Analysis scripts work
python3 /root/scripts/analysis/ana-d-menus.py
# 🔍 Starting menu analysis...
```

## Backup

The original crontab was preserved

```bash
ls /root/crontab-backup-*.txt
# /root/crontab-backup-20260307-153700.txt
```

## Takeaways

1. **Naming conventions scale** — What works for 5 scripts fails at 20. Standardize early.
2. **Categories reduce cognitive load** — `mon-*` immediately tells you it's monitoring.
3. **Frequency in the name** — `m5`, `h1`, `d`, `w` makes scheduling obvious.
4. **Log files should match scripts** — Debugging is easier when names align.
5. **Organize by purpose, not chronology** — "What does this do?" is more useful than "When was this created?"

---

Migration complete. 20 cron jobs now follow a consistent naming convention with organized directory structure.