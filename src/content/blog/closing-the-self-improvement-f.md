---
pubDatetime: 2026-04-11T22:00:00Z
title: "Closing the Self-Improvement Feedback Loops: From Data Lake to Data Loop"
postSlug: "closing-the-self-improvement-f"
description: "Closing the Self-Improvement Feedback Loops: From Data Lake to Data Loop"
tags:
  - others
---

An AI system designed to improve itself had captured 703 artefacts — menu selections, trigger firings, evolution proposals — and approved exactly 3. The self-improvement loop was broken at the one step that mattered: activation. Everything flowed in. Nothing flowed out.

## The Diagnosis: A Data Lake, Not a Data Loop

The system had three feedback loops running in production. All three stalled at the same point — the approval gate.

**Menu intelligence** tracked which options users selected and which they ignored. 412 signals captured. Zero menu restructures applied.

**Evolution engine** monitored skill maturity, detected stagnation, and proposed improvements. 189 proposals generated. Two auto-approved (both typo fixes).

**Skill improvement** scanned for dead references, orphaned files, and stale cross-links. 102 issues detected. One cleanup applied — manually.

The pattern was clear: data was flowing in, being stored, being analysed, but never acting on its own conclusions. The system was a data lake with aspirations of being a data loop. It had observational capacity without operational capacity.

The root cause wasn't a bug. It was an architectural gap. There was no tiered approval engine, no risk classification, no automated activation path. Every improvement proposal — regardless of risk — required human approval. A typo fix in a skill description sat in the same queue as a schema migration. Nothing moved because everything required the same level of scrutiny.

## The Architecture: Triple-Loop Design

The fix required three connected loops sharing a central nervous system: a PostgreSQL `usage_signals` table with a `record_signal()` stored function and three aggregation views (`v_daily_signals`, `v_weekly_signals`, `v_skill_summary`).

Every signal — menu selection, trigger firing, subagent dispatch, evolution proposal — writes to the same table. The structure is deliberately simple:

```
CREATE TABLE usage_signals (
    id SERIAL PRIMARY KEY,
    skill TEXT NOT NULL,
    event_type TEXT NOT NULL,
    event_data JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

The three aggregation views roll up daily, weekly, and per-skill statistics. The skill summary view is the one that feeds the auto-approve engine — it knows which skills have low engagement, which menus have high defer rates, and which triggers fire without downstream action.

### The Auto-Approve Engine

The heart of the fix is `auto_approve.py` — a domain-based risk classifier that routes proposals to three tiers:

| Risk Level | Domains | Auto-Approve? | Example |
|------------|---------|---------------|---------|
| **LOW** | Prompts, descriptions, labels | Yes, immediately | Fix typo in skill summary |
| **MEDIUM** | Menus, signals, tracking | Yes, with rate limit (10/day) | Restructure menu option order |
| **HIGH** | Schemas, database, API | No — queue for human | Add new column to usage_signals |

The rate limiting isn't theoretical. LOW-risk changes execute without limit. MEDIUM-risk changes are capped at 10 per day to prevent cascading menu restructures. HIGH-risk changes sit in a queue with full diff output, waiting for explicit approval.

This was the missing piece. Not better data collection — the system was already collecting everything. Not better analysis — the aggregation views were already surfacing the right signals. The gap was the activation path between "the system knows what to do" and "the system does it."

### Safety Layer

Every auto-approved action has three safety nets:

1. **Rate limits** — per-domain caps prevent runaway changes
2. **Rollback** — every change is logged with a full before-state, and `rollback.py` can revert the last N changes for any domain
3. **Audit trail** — every auto-approved action writes to an `auto_approve_log` table with the proposal, the risk classification, the rationale, and the outcome

## The Implementation: P1 Through P4

The deployment happened in four phases over a weekend.

**P1 — Signal infrastructure.** Deployed the `usage_signals` table, the `record_signal()` function, and the three aggregation views. Connected the existing menu signal tracking (`record_signal.py`) to write directly to the table instead of JSON files. This was the easiest phase — pure infrastructure, no behavioural changes.

**P2 — Auto-approve engine.** Wrote `auto_approve.py` with the domain-based risk classifier. Deployed the rate limiter and the audit log. Ran it in dry-run mode for two days to validate the risk classifications. Found three misclassifications — a schema migration tagged as MEDIUM (should be HIGH), a prompt update tagged as HIGH (should be LOW), and a menu reorder tagged as LOW (should be MEDIUM). Fixed the classification rules.

**P3 — Cross-reference linting.** Built `crossref_lint.py` — a 225-line Python script that scans four directories (skills, schemas, docs, context files) for broken links, orphaned files, and stale references. First run found 43 issues. All 43 were errors, not warnings — broken links that would fail silently at runtime. Fixed all of them. The script now runs as part of the weekly pipeline.

**P4 — Subagent tracking.** Implemented `track_subagent.py` with a dual-track pattern: the orchestrator logs dispatch events (which subagent was called, when, with what task), and the subagent logs its own completion event (success/failure, duration, tokens used). Both tracks write to the same `usage_signals` table. This gives a complete picture: the system knows not just what was requested, but what actually happened.

### Continuation Work

After the core four phases, three more pieces completed the loop:

**Research-factory signal wiring.** Connected the research pipeline to the signal table so every research session — queries fired, sources found, summaries generated — feeds back into the skill improvement loop. High-query-count topics surface as skill improvement candidates.

**Experience compounding.** Added an `experience_compound.py` script that reads the past week's signals, identifies patterns (skills that are improving, skills that are stagnating), and generates a weekly digest. This is the compound interest of self-improvement — each week's analysis builds on the previous week's, creating an accelerating improvement curve rather than independent snapshots.

**Hugo-era path cleanup.** Found and removed Hugo-era paths across 9 files — the telegram SKILL, documentation files, trigger definitions. The system had migrated from Hugo to Astro months ago, but ghost references lingered. The crossref lint caught them.

## The Sunday Pipeline

The payoff of all this infrastructure is the Sunday Pipeline — a fully automated weekly chain that runs five Kestra workflows in sequence:

```
08:00  Knowledge Compiler  →  Reads raw session notes, proposes wiki updates
09:00  Crossref Lint        →  Scans all directories, flags broken references
10:00  Skill Improver       →  Analyzes signal data, proposes skill improvements
11:00  Experience Compound  →  Rolls up weekly patterns, generates digest
```

The first workflow kicks off at 08:00. Each subsequent workflow starts only if the previous one completed successfully. If the crossref lint finds critical errors, the skill improver doesn't run — you don't want to propose improvements to a codebase with broken references.

The Kestra integration required one non-obvious fix: Directus API calls from Kestra Docker task runners need `networkMode: host` to reach the Directus container. Without it, Kestra's task runners run in their own Docker network and can't resolve `localhost:8055`. This took an embarrassingly long time to debug.

In addition to the five Sunday workflows, two daily workflows keep the system warm:

- **07:00 Evolution Report** — Generates the daily self-improvement status report
- **08:00 Auto-Approve** — Processes the LOW and MEDIUM risk queue

Seven Kestra workflows total. Zero manual intervention required for routine improvements.

## The Result: From Broken to 93%

The evolution roadmap tracks 15 items. 14 are complete. The one remaining item — automated schema migration testing — is a HIGH-risk domain that deliberately requires human approval.

The numbers tell the story:

| Metric | Before | After |
|--------|--------|-------|
| Signals captured | 703 | 703 (unchanged — collection was working) |
| Signals acted on | 3 | ~180/week (auto-approved LOW + MEDIUM) |
| Cross-reference errors | 43 | 0 |
| Active Kestra workflows | 0 | 7 |
| Manual intervention per week | ~20 actions | ~2 actions (HIGH-risk queue only) |

The system didn't need more data. It didn't need better algorithms. It needed an activation path — a way to close the loop between knowing and doing.

## What's Left

The one remaining item on the evolution roadmap — automated schema migration testing — is instructive. It's the boundary case that proves the safety model works. Schema changes are HIGH-risk. They should require human approval. The system correctly classifies them and correctly refuses to auto-approve them.

The goal was never full autonomy. The goal was appropriate autonomy — low-risk changes flow automatically, medium-risk changes flow with rate limits, and high-risk changes wait for human judgment. The feedback loops are closed at every tier where closure is safe, and deliberately open at the tier where human oversight adds value.

That's the design. A data loop, not a data lake. Seventy-three percent of captured signals now produce downstream action within 24 hours. The system improves itself every Sunday at 08:00, and I review the HIGH-risk queue with my Monday coffee.

**Tags**: ai-infrastructure, self-improvement, feedback-loops, kestra, postgresql, automation
**Categories**: Engineering, AI Infrastructure