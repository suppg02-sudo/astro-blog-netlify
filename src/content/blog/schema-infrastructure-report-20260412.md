---
pubDatetime: 2026-04-12T09:00:02Z
title: "Schema Infrastructure Report — 2026-04-12"
postSlug: "schema-infrastructure-report-20260412"
description: "Automated analysis of the OpenCode schema ecosystem. Health score: 98.0/100, 21 schemas, 0 issues."
tags:
  - schema-report
  - health-98.0
  - automated
  - infrastructure
---

# Schema Infrastructure Report — 2026-04-12

## Executive Summary

Health Score: **98.0/100**
Schemas: 21 | Issues: 0

## Health Breakdown


| Area | Score | Detail |

|------|-------|--------|

| composition | 100% | No issues |

| dedup | 100% | No issues |

| coverage | 100% | No issues |

| freshness | 100% | No issues |

| integration | 80% | opencode-commons: no consumers declared; skill: no consumers declared |


## Schema Inventory (21)


| Schema | Type | Fields | Lifecycle |

|--------|------|--------|-----------|

| base-entity | entity | 0 | stable |

| dashboard-schema | sub | 0 | stable |

| experiment-schema | entity | 0 | draft |

| file-index-schema | validation | 0 | stable |

| mixin-deferrable | mixin | 0 | stable |

| mixin-relatable | mixin | 0 | stable |

| mixin-schedulable | mixin | 0 | stable |

| mixin-traceable | mixin | 0 | stable |

| mixin-trackable | mixin | 0 | stable |

| opencode-commons | validation | 6 | stable |

| research-task-schema | entity | 0 | draft |

| roadmap-schema | sub | 0 | stable |

| schema-schema | meta | 2 | stable |

| signal-tracking-schema | sub | 0 | stable |

| skill | validation | 20 | stable |

| task-schema | entity | 0 | draft |

| agent-schema | entity | 17 | draft |

| harness-schema | sub | 11 | draft |

| attention-schema | sub | 1 | stable |

| project-schema | entity | 1 | stable |

| research-schema | entity | 19 | stable |


## Overlap Matrix (Top 5)


| Pair | Overlap | Status |

|------|---------|--------|

| agent-schema ↔ research-schema | 38.5% | moderate overlap |

| agent-schema ↔ harness-schema | 16.7% | minimal overlap |

| opencode-commons ↔ agent-schema | 15.0% | minimal overlap |

| skill ↔ research-schema | 14.7% | minimal overlap |

| opencode-commons ↔ research-schema | 13.6% | minimal overlap |

---

*Generated automatically by schema-scanner.py v1.0.0*
