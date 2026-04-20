---
pubDatetime: 2026-04-08T03:05:27Z
title: "Schema Analysis Report — 2026-04-08"
postSlug: "schema-analysis-2026-04-08"
description: "Schema Analysis Report — 2026-04-08"
tags:
  - automated-report
  - schema-analysis
  - warning
---

<style>
.sev-section { border-radius: 6px; margin: 1.2rem 0; overflow: hidden; border: 1px solid; }
.sev-critical { border-color: #ef4444; background: rgba(239,68,68,0.04); }
.sev-critical > summary { background: rgba(239,68,68,0.12); color: #dc2626; }
.sev-warning { border-color: #f59e0b; background: rgba(245,158,11,0.04); }
.sev-warning > summary { background: rgba(245,158,11,0.12); color: #b45309; }
.sev-action { border-color: #3b82f6; background: rgba(59,130,246,0.04); }
.sev-action > summary { background: rgba(59,130,246,0.12); color: #2563eb; }
.sev-positive { border-color: #22c55e; background: rgba(34,197,94,0.04); }
.sev-positive > summary { background: rgba(34,197,94,0.12); color: #16a34a; }
.sev-neutral { border-color: #6b7280; background: rgba(107,114,128,0.04); }
.sev-neutral > summary { background: rgba(107,114,128,0.08); color: #4b5563; }
.sev-section > summary { padding: 0.6rem 1rem; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 0.5rem; list-style: none; }
.sev-section > summary::-webkit-details-marker { display: none; }
.sev-section > summary::before { content: '▶'; font-size: 0.75rem; transition: transform 0.15s; }
.sev-section[open] > summary::before { transform: rotate(90deg); }
.sev-body { padding: 0.8rem 1rem; }
.summary-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(120px,1fr)); gap: 0.6rem; margin: 0.5rem 0; }
.summary-card { border-radius: 6px; padding: 0.6rem 0.8rem; text-align: center; }
.summary-card .sc-val { font-size: 1.4em; font-weight: 700; }
.summary-card .sc-label { font-size: 0.75em; opacity: 0.7; margin-top: 0.15rem; }
.sc-red { background: rgba(239,68,68,0.1); color: #dc2626; }
.sc-amber { background: rgba(245,158,11,0.1); color: #b45309; }
.sc-green { background: rgba(34,197,94,0.1); color: #16a34a; }
.sc-blue { background: rgba(59,130,246,0.1); color: #2563eb; }
</style>

> **TL;DR**: Automated schema ecosystem analysis. Health score: 95.0/100, 8 issues found, 8 deferred options captured.

## Summary

<div class="summary-grid">
<div class="summary-card sc-green"><div class="sc-val">📊 95.0</div><div class="sc-label">Health Score</div></div>
<div class="summary-card sc-blue"><div class="sc-val">📋 N/A</div><div class="sc-label">Composition Score</div></div>
<div class="summary-card sc-amber"><div class="sc-val">⚠️ 8</div><div class="sc-label">Issues</div></div>
<div class="summary-card sc-blue"><div class="sc-val">⏳ 8</div><div class="sc-label">Deferred</div></div>
</div>

## Issues Found

<details class="sev-section sev-warning">
<summary>🟡 High overlap without shared base: base-entity ↔ experiment-schema                      100.0%  warning</summary>
<div class="sev-body">

Schema pair shows high overlap but no composition via shared base/mixin. Consider composition.

</div>
</details>

<details class="sev-section sev-warning">
<summary>🟡 High overlap without shared base: base-entity ↔ mixin-deferrable                       100.0%  warning</summary>
<div class="sev-body">

Schema pair shows high overlap but no composition via shared base/mixin. Consider composition.

</div>
</details>

<details class="sev-section sev-warning">
<summary>🟡 High overlap without shared base: base-entity ↔ mixin-relatable                        100.0%  warning</summary>
<div class="sev-body">

Schema pair shows high overlap but no composition via shared base/mixin. Consider composition.

</div>
</details>

<details class="sev-section sev-warning">
<summary>🟡 High overlap without shared base: base-entity ↔ mixin-schedulable                      100.0%  warning</summary>
<div class="sev-body">

Schema pair shows high overlap but no composition via shared base/mixin. Consider composition.

</div>
</details>

<details class="sev-section sev-warning">
<summary>🟡 High overlap without shared base: base-entity ↔ mixin-traceable                        100.0%  warning</summary>
<div class="sev-body">

Schema pair shows high overlap but no composition via shared base/mixin. Consider composition.

</div>
</details>

<details class="sev-section sev-warning">
<summary>🟡 High overlap without shared base: base-entity ↔ mixin-trackable                        100.0%  warning</summary>
<div class="sev-body">

Schema pair shows high overlap but no composition via shared base/mixin. Consider composition.

</div>
</details>

<details class="sev-section sev-warning">
<summary>🟡 High overlap without shared base: base-entity ↔ research-task-schema                   100.0%  warning</summary>
<div class="sev-body">

Schema pair shows high overlap but no composition via shared base/mixin. Consider composition.

</div>
</details>

<details class="sev-section sev-warning">
<summary>🟡 High overlap without shared base: base-entity ↔ task-schema                            100.0%  warning</summary>
<div class="sev-body">

Schema pair shows high overlap but no composition via shared base/mixin. Consider composition.

</div>
</details>

## Results Trend

| Date | Health | Composition | Issues | Status |
|------|--------|---------------|--------|--------|
| 2026-04-08 | 95.0 | 0 | 8 | ✅ |

---

*This report was automatically generated by the schema analysis cron job.*
