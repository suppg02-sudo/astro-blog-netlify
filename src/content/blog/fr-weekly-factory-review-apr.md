---
pubDatetime: 2026-04-04T15:34:36Z
title: "Weekly Factory Review — April 04, 2026"
postSlug: "fr-weekly-factory-review-apr"
description: "Automated analysis of all 5 OpenCode meta-skills (factories): skill-factory, agents-factory, menu-factory, project-factory, and research-factory. This report checks schemas, directory structures, SKIL"
tags:
  - factory-review
  - weekly-report
  - opencode
  - automation
---

# Weekly Factory Review — April 04, 2026

Automated analysis of all 5 OpenCode meta-skills (factories): skill-factory, agents-factory, menu-factory, project-factory, and research-factory. This report checks schemas, directory structures, SKILL.md completeness, cross-factory consistency, and generates actionable improvement suggestions.

**Tags**: opencode, factory-review, automation, skills, meta-skills

## Executive Summary

This week's scan produced **13 findings** across **6** factories:

- 🟠 **8 warnings
- 🟡 **5 informational** notes

**Overall Health Score: 🟢 86/100**

## Health Scores by Factory

| Factory | Score | Critical | Warnings |
|---------|-------|----------|----------|
| 🟢 skill-factory | 90/100 | 0 | 1 |
| 🟢 agents-factory | 90/100 | 0 | 1 |
| 🟢 menu-factory | 90/100 | 0 | 1 |
| 🟢 project-factory | 80/100 | 0 | 2 |
| 🟢 research-factory | 80/100 | 0 | 2 |

## Maturity & Version Status

| Factory | Maturity | Version |
|---------|----------|---------|
| skill-factory | L4 | 2.0.0 |
| agents-factory | L2 | 1.0.0 |
| menu-factory | N/A | N/A |
| project-factory | L2 | 1.2.0 |
| research-factory | L4 | 1.1.0 |

## Warnings

- **menu-factory** [skill.yaml]: No skill.yaml found
- **agents-factory** [SKILL.md]: SKILL.md incomplete (1/5 standard sections)
- **project-factory** [SKILL.md]: SKILL.md incomplete (0/5 standard sections)
- **research-factory** [SKILL.md]: SKILL.md incomplete (1/5 standard sections)
- **ALL** [consistency]: Low feature overlap across factories: 1/18 features common
- **skill-factory** [menu]: Menu config incomplete (compliance: 1/2)
- **project-factory** [menu]: Menu config incomplete (compliance: 1/2)
- **research-factory** [menu]: Menu config incomplete (compliance: 1/2)

## Top Recommendations

1. **menu-factory** needs a skill.yaml — it's the only factory without one, breaking parity
2. **agents-factory** is at L2 — evolve to L3 with scripts and automation
3. **menu-factory** is at L0 — evolve to L3 with scripts and automation
4. **project-factory** is at L2 — evolve to L3 with scripts and automation
5. **agents-factory** SKILL.md incomplete (1/5 standard sections) — add missing sections
6. **project-factory** SKILL.md incomplete (0/5 standard sections) — add missing sections
7. **research-factory** SKILL.md incomplete (1/5 standard sections) — add missing sections

## Pipeline

🔴 `Collect` → 🟠 `Validate` → 🟡 `Compare` → 🟢 `Report` → 🔵 `Blog Publish`

---
*Automated by the weekly factory-review cron job — Week 14, 2026-04-04*