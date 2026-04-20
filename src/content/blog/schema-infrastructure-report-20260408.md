---
pubDatetime: 2026-04-08T03:15:25Z
title: "Schema Infrastructure Report — 2026-04-08"
postSlug: "schema-infrastructure-report-20260408"
description: "Automated analysis of the OpenCode schema ecosystem. Health score: 83.5/100, 19 schemas, 18 issues."
tags:
  - schema-report
  - automated
  - health-83.5
  - infrastructure
---

# Schema Infrastructure Report — 2026-04-08

## Executive Summary

Health Score: **83.5/100**
Schemas: 19 | Issues: 18

## Health Breakdown


| Area | Score | Detail |

|------|-------|--------|

| composition | 90% | base-entity: missing $extends |

| dedup | 100% | No issues |

| coverage | 100% | No issues |

| freshness | 10% | base-entity: no changelog entries; dashboard-schema: no changelog entries |

| integration | 100% | No issues |


## Schema Inventory (19)


| Schema | Type | Fields | Lifecycle |

|--------|------|--------|-----------|

| base-entity | entity | 2 | stable |

| dashboard-schema | sub | 2 | stable |

| experiment-schema | entity | 2 | draft |

| file-index-schema | validation | 1 | stable |

| mixin-deferrable | mixin | 2 | stable |

| mixin-relatable | mixin | 2 | stable |

| mixin-schedulable | mixin | 2 | stable |

| mixin-traceable | mixin | 2 | stable |

| mixin-trackable | mixin | 2 | stable |

| research-task-schema | entity | 2 | draft |

| roadmap-schema | sub | 2 | stable |

| schema-schema | meta | 8 | stable |

| signal-tracking-schema | sub | 1 | stable |

| task-schema | entity | 2 | draft |

| agent-schema | entity | 3 | draft |

| harness-schema | sub | 2 | draft |

| attention-schema | sub | 1 | stable |

| project-schema | entity | 3 | stable |

| research-schema | entity | 3 | stable |


## Issues (18)


- **[INFO]** ISS-001: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry

- **[INFO]** ISS-002: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry

- **[INFO]** ISS-003: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry

- **[INFO]** ISS-004: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry

- **[INFO]** ISS-005: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry

- **[INFO]** ISS-006: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry

- **[INFO]** ISS-007: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry

- **[INFO]** ISS-008: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry

- **[INFO]** ISS-009: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry

- **[INFO]** ISS-010: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry

- **[INFO]** ISS-011: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry

- **[INFO]** ISS-012: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry

- **[INFO]** ISS-013: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry

- **[INFO]** ISS-014: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry

- **[INFO]** ISS-015: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry

- **[INFO]** ISS-016: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry

- **[INFO]** ISS-017: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry

- **[INFO]** ISS-018: No changelog entries. Version history unknown.

  - Fix: Add $changelog header with creation entry


## Recommendations


- **[HIGH]** Adopt base-entity inheritance for entity schemas — +90 composition score points

- **[MEDIUM]** Add changelog entries to all schemas — +10 freshness score points


## Overlap Matrix (Top 5)


| Pair | Overlap | Status |

|------|---------|--------|

| base-entity ↔ experiment-schema | 100.0% | warning — high overlap without shared base/mixin |

| base-entity ↔ mixin-deferrable | 100.0% | warning — high overlap without shared base/mixin |

| base-entity ↔ mixin-relatable | 100.0% | warning — high overlap without shared base/mixin |

| base-entity ↔ mixin-schedulable | 100.0% | warning — high overlap without shared base/mixin |

| base-entity ↔ mixin-traceable | 100.0% | warning — high overlap without shared base/mixin |

---

*Generated automatically by schema-scanner.py v1.0.0*
