---
pubDatetime: 2026-03-04T13:28:25Z
title: "OpenMemory Intelligence Report — 04 Mar 2026"
postSlug: "openmemory-report-2026-03-04"
description: "Automated intelligence report: 922 memories across 5 sectors. Health score: 95/100."
tags:
  - openmemory
  - analytics
  - memory-system
  - report
  - ai-infrastructure
---

## Overview

| Metric | Value |
|--------|-------|
| Total Memories | **922** |
| Database Size | 1.08MB |
| WAL Size | 9.9MB |
| Oldest Memory | 2025-12-23 14:30 UTC |
| Newest Memory | 2026-03-04 06:58 UTC |
| Avg Content Length | 136 chars |
| Version | 2.0-hsg-tiered |
| Tier | fast |
| Health Score | **95/100** 🟢 |

## Sector Breakdown

| Sector | Count | % | Avg Salience | Decay λ |
|--------|------:|--:|-------------:|--------:|
| procedural | 419 | 45.4% | 0.1679 | 0.008 |
| semantic | 397 | 43.1% | 0.2587 | 0.005 |
| emotional | 40 | 4.3% | 0.0897 | 0.02 |
| episodic | 35 | 3.8% | 0.0326 | 0.015 |
| reflective | 31 | 3.4% | 0.4204 | 0.001 |
| **TOTAL** | **922** | | | |

## Salience Distribution

| Range | Count | % |
|-------|------:|--:|
| 0.00-0.01 (nearly forgotten) | 0 | 0.0% |
| 0.01-0.10 (low) | 544 | 59.0% |
| 0.10-0.30 (medium) | 134 | 14.5% |
| 0.30-0.50 (high) | 111 | 12.0% |
| 0.50-0.80 (very high) | 42 | 4.6% |
| 0.80-1.00 (critical) | 91 | 9.9% |

## Context Types

| Type | Count |
|------|------:|
| flow | 226 |
| workflow | 175 |
| skill | 156 |
| conversation | 156 |
| initiative | 65 |
| menu_choice | 31 |
| decision | 23 |
| todo-list | 8 |
| deferred | 4 |
| user-reference | 2 |
| trigger-word-update | 2 |
| research-report | 2 |
| personal-info | 2 |
| improvement | 2 |
| blog-post | 2 |
| *(no metadata)* | 25 |

## Top Tags (5,958 total uses)

| Tag | Count |
|-----|------:|
| `hugo` | 147 |
| `blog-post` | 116 |
| `youtube` | 112 |
| `output` | 95 |
| `workflow` | 88 |
| `documentation` | 87 |
| `transcript` | 78 |
| `mermaid` | 68 |
| `automation` | 67 |
| `opencode` | 59 |
| `research` | 56 |
| `legacy` | 56 |
| `success` | 52 |
| `docker` | 49 |
| `openmemory` | 48 |
| `configuration` | 41 |
| `memos` | 39 |
| `testing` | 35 |
| `troubleshooting` | 34 |
| `complete` | 34 |
| *(untagged)* | 23 |

## Daily Activity (Last 14 Days)

| Date | Memories Added |
|------|---------------:|
| 2026-02-08 | 24 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ |
| 2026-02-09 | 63 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ |
| 2026-02-10 | 27 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ |
| 2026-02-11 | 31 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ |
| 2026-02-12 | 12 ▓▓▓▓▓▓▓▓▓▓▓▓ |
| 2026-02-13 | 22 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ |
| 2026-02-14 | 7 ▓▓▓▓▓▓▓ |
| 2026-02-15 | 5 ▓▓▓▓▓ |
| 2026-02-22 | 1 ▓ |
| 2026-02-23 | 8 ▓▓▓▓▓▓▓▓ |
| 2026-02-24 | 4 ▓▓▓▓ |
| 2026-02-25 | 5 ▓▓▓▓▓ |
| 2026-03-02 | 1 ▓ |
| 2026-03-04 | 87 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ |

## Migration Stats

Total migrated from legacy JSON: **56**

| Source File | Count |
|------------|------:|
| questions.json | 29 |
| actions.json | 25 |
| delegations.json | 2 |

## Improvement Suggestions (1)

### 🟡 1. Upgrade from 'fast' tier
**Category:** Performance | **Severity:** medium

Running synthetic embeddings (256d). Real embeddings (768d+) would significantly improve semantic search quality and query relevance.

**Action:** Set OPENMEMORY_TIER=balanced in docker-compose.yml and configure an embedding provider (OpenAI, local model).

---

*Generated automatically by OpenMemory Intelligence Report on 2026-03-04 13:28 UTC.*
*Dashboard: [http://ubuntu4:13120](http://ubuntu4:13120)*