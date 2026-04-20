---
pubDatetime: 2026-04-05T14:00:00Z
title: "The Menu Controller: From Theory to Production"
postSlug: "the-menu-controller-from-theory-to-production"
description: "The Menu Controller: From Theory to Production"
tags:
  - control-plane
  - controller
  - reconciliation
  - automation
  - kubernetes
---

# The Menu Controller: From Theory to Production

Last week I wrote about the AI Agent Control Plane — the idea that AI infrastructure needs the same reconciliation pattern that Kubernetes uses for containers. Schema declares desired state. Signals measure observed state. Controllers reconcile the gap. Factories actuate corrections.

This week, the first Controller went live.

## What It Does

The **Menu Controller** (`menu_controller.py`) implements the full Controller Contract against a real resource type: the 59 menus embedded in skill SKILL.md files across the OpenCode system.

It runs a classic three-phase reconciliation loop:

1. **Observe** — Reads each skill's menu JSON, pulls signal data (how many times each option was presented and selected), checks selection counts
2. **Diff** — Runs 8 detection patterns against the observed state: dead options (never selected), underperformers, order fatigue, context mismatch, size violations, template drift, missing options, stale globals
3. **Act** — Auto-corrects LOW/MEDIUM drift (prune dead options, reorder by usage), queues HIGH/CRITICAL drift for human review as proposals

Every mutation is logged to an audit trail. Every resource gets spec + status + conditions + drift stored in PostgreSQL.

## The Numbers

The first full reconciliation pass produced immediate results:

| Metric | Value |
|--------|-------|
| Menu resources registered | 59 |
| Drift detected | 58 (98%) |
| Auto-corrected | 58 |
| Dead options pruned | 123 |
| Change log entries | 59 |
| Fully synced (no drift) | 1 |

The dominant pattern was `dead_option` — menu options that existed in SKILL.md files but had zero selections in the tracking data. These accumulated over months as skills evolved but their embedded menus were never cleaned up.

123 dead options removed. Zero manual intervention.

## Why This Matters

Before the Controller, menu cleanup was manual. I'd notice a stale option, edit the SKILL.md, and move on. The optimize.py script could detect problems, but it was a one-shot tool you had to remember to run.

The Controller changes this in three ways:

**Continuous reconciliation.** A cron runs the loop every Sunday at 09:00. It doesn't forget. It doesn't skip weeks. Drift gets caught and corrected automatically.

**Structured state.** Every menu resource now has a proper spec (what the menu should look like), status (what it actually looks like), conditions (Synced, Ready, Healthy), and a drift classification (NONE/LOW/MEDIUM/HIGH/CRITICAL). This isn't ad-hoc — it's the same pattern Kubernetes uses for Pods.

**Audit trail.** Every change is logged: what was before, what changed, why, and whether it was automatic. The `controlplane.change_log` table is the system of record for all menu mutations.

## The Architecture

The controller wraps the existing `optimize.py` (752 lines, 28 functions) rather than replacing it. The pipeline mapping is:

```
optimize.py Ingest → Controller Observe
optimize.py Detect → Controller Diff
optimize.py Decide + Apply → Controller Act
```

New capabilities added on top:

- Schema Registry integration (PostgreSQL `controlplane` schema)
- Conditions array management (Synced, Ready, Healthy)
- Drift severity classification (NONE → CRITICAL)
- Change log audit trail
- Resource upsert with spec/status separation

## What's Next

The Menu Controller proves the pattern works. The next controllers to build:

1. **Skill Controller** — wraps skill-improver to continuously reconcile skill health (stale triggers, missing dependencies, maturity drift)
2. **Agent Controller** — monitors agent configurations for model changes, tool availability, context budget drift
3. **Research Controller** — tracks eRAG projects for source freshness, chunk quality, embedding coverage

Each one follows the same contract: observe → diff → act, with spec/status/conditions/drift stored in the registry and every mutation logged.

The goal isn't more controllers for the sake of it. The goal is a system that **maintains itself** — where drift is detected automatically, low-risk corrections are applied without human involvement, and humans only review the changes that actually need judgement.

That's what the Kubernetes control plane does for infrastructure. That's what this control plane does for AI agent configuration.

## Try It

```bash
# Check drift for a single skill
python3 menu_controller.py --drift skill-factory

# Full reconciliation (dry run)
python3 menu_controller.py --reconcile-all --dry-run

# Live reconciliation
python3 menu_controller.py --reconcile-all

# Check registry status
python3 menu_controller.py --status skill-factory
```

The control plane is running. The first controller is live. The reconciliation loop is turning.
