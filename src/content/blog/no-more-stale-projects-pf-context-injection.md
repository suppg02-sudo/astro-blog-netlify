---
pubDatetime: 2026-04-06T19:00:00Z
title: "No More Stale Projects — The Project Factory Context Injection Pipeline"
postSlug: "no-more-stale-projects-pf-context-injection"
description: "15 gate checks, auto-populated history, and structured context summaries ensure no project ever resumes blind."
tags:
  - agent-workflow
  - automation
  - open-code
  - project-management
---

# No More Stale Projects — The Project Factory Context Injection Pipeline

Every time you resume a project, you lose context. Decisions fade. Intent blurs. The roadmap you drafted last week? Forgotten. The gate checks that would catch missing scope? Non-existent.

This is the **Project Factory context injection pipeline** — a structured approach to ensuring no project ever resumes blind.

## The Problem

You trigger `pf`, the project factory loads. It shows a dashboard, maybe a recommendation. But you pick a project and you're left asking: *What was I doing? What did I decide? Is anything broken? Where's the roadmap?*

The agent doesn't show you. It just offers a menu.

## The Solution: 15 Gate Checks

Every time a project is loaded or resumed, a gate check runs before the menu is presented. It validates 15 aspects of the project's health:

| Gate | Checks | Fail Level |
|------|--------|-----------|
| G1 | Identity fields populated | FAIL |
| G2 | Intent and scope defined | WARN |
| G3 | Current phase has exit criteria | WARN |
| G4 | Actions list populated | WARN |
| G5 | Roadmap phases defined | WARN |
| G6 | Context sources available | WARN |
| G7 | Schedule dates set | WARN |
| G8 | Decisions tracked | WARN |
| G9 | Relations configured | INFO |
| G10 | History entries exist | WARN |
| G11 | Shopping items tracked | INFO |
| G12 | Dashboard metrics set | INFO |
| G13 | Next action defined | WARN |
| G14 | Project stale or fresh | WARN |
| G15 | Memory searchable (pghmem) | WARN |

The result: you see a structured summary before you ever interact with the menu.

## Auto-Populated History

Every project tracks an append-only `history.entries` log. Entries are auto-created for:

- **Session** — every time you load or resume
- **Decision** — via `pf update --decision`
- **Phase change** — via `pf advance`
- **Action** — via `pf action-done`
- **Context add** — via `pf add`
- **Milestone** — when a roadmap phase completes
- **Capture** — via `pf capture`

This means the last three entries in any project's history show you exactly what happened last session — no guessing.

## Load Pipeline

The full pipeline when you load a project:

```
🔴 Load Project YAML
→ 🟠 Run 15 Gate Checks
→ 🟡 Search pghmem for related memories
→ 🟢 Present Context Summary
→ 🔵 Append Session History Entry
→ 🟣 Present Phase-Aware Project Menu
```

If any gate returns FAIL, the pipeline stops — you must fix before proceeding. WARN gates show warnings but allow you to proceed.

## Real Output

Here's what you see when loading the *lockdown* project:

```
╔════════════════════════════════════════════════════════╗
║  PROJECT CONTEXT — lockdown                            ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║  📋 IDENTITY                                           ║
║  ID: lockdown | Priority: 🔴 high | Phase: idea       ║
║  Created: 2026-04-01 | Updated: 2026-04-06            ║
║  Orchestrator: personal domain                         ║
║                                                        ║
║  🎯 INTENT                                             ║
║  Achieve 6 months of self-sufficiency for 4 adults...  ║
║                                                        ║
║  🔄 CURRENT PHASE: idea                                ║
║  Exit: Intent and scope defined, 3-month targets...    ║
║                                                        ║
║  ➡️ NEXT ACTION                                         ║
║  Take stock of what's already on hand, top up gaps     ║
║                                                        ║
║  ✅ PROGRESS                                           ║
║  Actions: 0 done | 4 pending | 1 active                ║
║                                                        ║
║  📜 HISTORY (last 3)                                   ║
║  • 2026-04-06 [session] Session loaded — 12 PASS       ║
║  • 2026-04-06 [session] History section initialised    ║
║                                                        ║
║  ⚠️ 3 WARN: Roadmap, Context Sources, Tracking         ║
╚════════════════════════════════════════════════════════╝
```

## Dashboard Integration

The dashboard now shows **last session loaded** for each project:

```
🔴 HIGH  lockdown
   Phase: idea · Updated: 2026-04-06 (0d)
   Last session: loaded: 0d ago
   🔴 HIGH PRIORITY
   ➡️ NEXT: Take stock of what's already on hand
```

No more forgetting when you last touched a project. This data comes from `history.entries` with `type: session`.

## How It Works

1. **Schema** (`schema.yaml` v2.1) — `history` section defines the append-only event log structure
2. **Script** (`load_project_context.py`) — runs gates, renders context summary, records history
3. **Protocol** (`context/load.md`) — defines gate thresholds, fix suggestions, menu integration
4. **Template** — new projects start with an initial history entry
5. **Migration** — all 8 existing projects now have history sections

## Gates by Level

**FAIL** — must fix before menu appears:
- Identity (G1): id, title, status, priority all required

**WARN** — should address but can proceed:
- Description, phase state, actions, roadmap, context, schedule, tracking, history, next action, staleness, memory

**INFO** — nice to have:
- Relations, shopping, dashboard

## The Key Insight

The dashboard tells you *what* to work on. The context injection tells you *where* each project stands and *why* you made the decisions you did. You're never resuming from scratch again.

All existing projects are migrated. New projects start with history tracking enabled. The gate checks run automatically when you select a project. The agent shows you warnings and offers to fix them.

No more stale projects. No more forgotten context.
