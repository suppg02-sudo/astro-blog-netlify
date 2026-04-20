---
pubDatetime: 2026-04-03T17:24:21Z
title: "OpenCode Evolution: Building Meta-Factories and Shared Schemas"
postSlug: "opencode-evolution-building-me"
description: "OpenCode Evolution: Building Meta-Factories and Shared Schemas"
tags:
  - others
---

> **TL;DR**: We've redesigned the OpenCode ecosystem around hub-and-spoke meta-factories — most notably the Research Factory (L4) — and extracted shared Roadmap and Dashboard sub-schemas that enforce consistency across every project and research instance. This post covers the full architecture, the six adapter categories, eight quality gates, the Progressive Disclosure strategy, signal tracking, cron scheduling, and the technical decisions behind each.

---

## The Problem: Ecosystem Drift

Over months of iterative development, the OpenCode ecosystem accumulated a powerful but fragmented toolkit: `erag` for persistent knowledge graphs (pgvector + NetworkX), `attention` for multi-source news scanning, `research` for enterprise-grade methodology, `news` for aggregation, and `project-factory` for structured project management.

The problem wasn't capability — it was **orchestration**. Each skill started inventing its own way to track progress, validate quality, and manage state. Scheduling meant writing ad-hoc bash scripts. Quality assurance was manual and inconsistent. A research task that combined `erag` for ingestion, `attention` for scanning, and `research` for methodology required an agent to load and coordinate all three independently, with no shared contract between them.

This was ecosystem drift: every tool growing in a slightly different direction, with no connective tissue.

---

## The Architecture: Hub-and-Spoke Meta-Factories

The solution was to introduce **meta-factories** — control planes that sit above existing skills and orchestrate them without modification. The Research Factory is the primary example.

```
┌──────────────────────────────────────────────────────────┐
│                   RESEARCH FACTORY (Hub)                  │
│                                                          │
│  instances/*.yaml    ← research instances (YAML files)   │
│  context/globals.yaml ← defaults + instructions          │
│  context/adapter-registry.yaml ← category→adapter map    │
│  context/quality-gates.md ← gate definitions             │
└──────────┬──────────┬──────────┬──────────┬──────────────┘
           │          │          │          │
      ┌────▼───┐ ┌────▼───┐ ┌───▼────┐ ┌──▼───┐
      │research│ │  erag  │ │attention│ │ news │
      │(L2)    │ │ (L3)   │ │ (L2)   │ │ (L1) │
      └────────┘ └────────┘ └────────┘ └──────┘
           Adapters (untouched, loaded on demand)
```

The key insight: **adapters remain completely untouched**. They receive a scope, execute their core function, and return findings to the factory. The factory handles lifecycle management, scheduling, quality validation, and publishing — concerns that don't belong inside any single adapter.

This pattern mirrors the existing `project-factory` and `skill-factory`, making it the third meta-factory in the ecosystem. Each factory is a hub; each downstream skill is a spoke.

---

## The Six Adapter Categories

Research isn't a single activity — it spans real-time monitoring, deep investigation, persistent knowledge building, and custom workflows. The Research Factory defines six categories, each mapping to a specific combination of primary and secondary adapters with tailored quality gates:

| Category | Primary Adapter | Secondary | Quality Gates |
|----------|----------------|-----------|---------------|
| **News Monitoring** | `attention` | `news` | source_diversity, recency, search_quality |
| **GitHub Research** | `research` | `erag` | source_diversity, verification, search_quality |
| **One-Off Research** | `research` | `pghmem` | multi_source, recency, search_quality |
| **Ephemeral Research** | `erag` | `research` | confidence_tier, coverage |
| **Infinite Ephemeral** | `erag` | `research`, `attention` | confidence_tier, coverage, source_diversity, search_quality |
| **Custom** | User-chosen | User-chosen | User-defined |

When an agent creates a research instance, the factory prompts for the category, resolves the adapter combo from the registry, and applies the appropriate gates. This eliminates the need for the agent to understand which tool does what — the factory handles the mapping.

---

## Eight Quality Gates

Every research execution runs quality gates before storing results. These aren't optional — they're enforced at the data layer:

1. **source_diversity** — Unique source domains must meet a minimum threshold (default: 3). Prevents findings based on a single source.

2. **recency** — Majority of sources must be within a configurable window (default: 90 days). Catches stale intelligence.

3. **multi_source** — Claims must be corroborated by 2+ independent sources. Eliminates single-source assertions.

4. **verification** — Key claims traced back to primary sources (not aggregators). Critical for GitHub research where secondary references are common.

5. **confidence_tier** — Every finding tagged as `raw`, `verified`, or `promoted`. Provides an explicit confidence gradient.

6. **coverage** — Ratio of answered questions to total questions must meet a threshold (default: 0.7). Ensures research scope is actually addressed.

7. **search_quality** — Search queries must return sufficient actionable results (default: 70% hit rate). Validates engine selection (Brave, GitHub, Context7, pgvector), query structure, and result relevance. Applied to all research categories.

8. **bias_check** — Contentious topics must present multiple perspectives. Enabled per-instance.

Gates run after every execution, before status promotion, and on demand. When any gate fails, gaps are recorded in the instance and the status stays at `active`. Only when **all** gates pass does the instance promote to `mature`.

---

## Shared Sub-Schemas: The Connective Tissue

The biggest architectural breakthrough wasn't the factory itself — it was extracting **shared sub-schemas** that both `project-factory` and `research-factory` use identically.

### Roadmap Schema (`roadmap-schema.yaml`)

A hybrid structure combining high-level phases with granular checklists. Each phase has:

- **id** (kebab-case), **title**, **status** (pending/in_progress/complete/skipped/blocked)
- **exit_criteria** — what must be true to consider the phase done
- **checklist** — array of `{item, done, assignee, notes}` for granular tracking
- **dependencies** — phase IDs that must complete first
- **target_date** and **completed_date** for temporal tracking

Progress is auto-calculated: `(completed checklist items / total checklist items) * 100%`. This formula is consistent across every project and research instance in the ecosystem.

The roadmap phases for research follow a standard pattern:
```
discovery → deep-research → synthesis
├── Define questions       ├── Execute primary        ├── Run quality gates
├── Identify sources       ├── Execute secondary      ├── Address gaps
└── Set scope              └── Cross-reference         └── Write summary
```

### Dashboard Schema (`dashboard-schema.yaml`)

This schema moves **UI contracts into the data layer**. It defines:

- **metrics** — arrays of `{name, value, target, unit, status}` for health tracking (e.g., "Source Diversity: 4/3 domains, healthy")
- **visuals** — arrays of `{type, label, data_source, options}` that tell any frontend how to render the data

Supported visual types include `progress_bar`, `dependency_map`, `radar_chart`, `status_traffic_light`, and `list`. The `data_source` field uses JSONPath references (e.g., `roadmap`, `relations.child_projects`), meaning any frontend — Astro, Reflex, or a future dashboard — can render these widgets without complex integration logic. The logic lives in the data, not the view.

Both schemas include embedded **signal tracking** arrays for capturing selection, co-selection, rejection, frequency, dwell, and backtrack events — feeding directly into the menu-factory optimizer.

---

## Progressive Disclosure Strategy

The Research Factory consists of 18+ files. Loading all of them would exhaust context windows and confuse smaller models. The solution is strict Progressive Disclosure:

- **SKILL.md** (the hub) is ~400 lines — it contains the architecture diagram, the disclosure map, and the main menu
- **Context files** are loaded on demand based on the current task

| Task | File Loaded | Lines |
|------|------------|-------|
| Create instance | `context/create.md` | ~100 |
| Execute research | `context/orchestrate.md` | ~85 |
| Check quality | `context/quality-gates.md` | ~75 |
| Schedule cron | `context/cron.md` | ~55 |
| Search history | `context/history.md` | ~75 |
| Improve methodology | `context/improve.md` | ~65 |
| Publish findings | `context/publish.md` | ~70 |
| Understand scope | `context/intent.md` | ~45 |

When a cron job triggers at 8 AM to run news monitoring, the agent loads only `cron.md` and `orchestrate.md` — saving thousands of tokens while maintaining execution discipline. This pattern is critical for making the system viable on smaller open-source models (7B-14B parameters), which is an explicit design goal.

---

## Instance Lifecycle and Status Promotion

Research instances follow a defined lifecycle with strict status promotion rules:

```
🔴 idea → 🟠 active → 🟡 mature → 🟢 complete → 🔵 archived
              │              │
              └── paused ←───┘  (user can pause at any point)
```

Status transitions are gate-guarded:
- `idea → active`: First execution begins
- `active → mature`: **All quality gates pass**
- `mature → complete`: User explicitly approves
- `active → active`: Any gate fails, gaps recorded
- Any → `paused`: User intervention

This prevents "false complete" scenarios where research looks done but has unaddressed gaps.

---

## Cron Scheduling and Automation

The factory includes native cron integration via `cron-runner.sh`:

```bash
bash scripts/cron-runner.sh --schedule <instance-id>  # Set up cron
bash scripts/cron-runner.sh --list                     # View scheduled
bash scripts/cron-runner.sh --run <instance-id>        # Manual trigger
bash scripts/cron-runner.sh --remove <instance-id>     # Remove schedule
```

The adapter registry defines default schedules per category (e.g., News Monitoring defaults to `0 8 * * *` — daily at 8 AM). The scheduler reads the instance YAML, resolves the adapter combo, and executes the pipeline.

---

## Signal Tracking and Menu Optimization

Every menu selection in the factory is tracked via `menu-factory`'s `record_signal.py`:

```bash
python3 ~/.config/opencode/skills/menu-factory/scripts/record_signal.py \
  --skill research-factory \
  --option "Create Research Instance" \
  --source main_menu
```

These signals feed into `smart_menu.py`, which reorders menu options by frequency. Over time, the most-used workflows bubble to the top, reducing cognitive load and execution time. The signal types captured include: selection, co_selection, rejection, frequency, dwell, and backtrack — giving the optimizer rich behavioral data.

---

## File Structure

The complete factory structure:

```
research-factory/
├── SKILL.md                          ← Hub (~400 lines)
├── skill.yaml                        ← Metadata (v1.1.0, L4)
├── context/
│   ├── intent.md                     ← Purpose & scope
│   ├── create.md                     ← Create spoke + roadmap generation
│   ├── orchestrate.md                ← Execution pipeline
│   ├── quality-gates.md              ← 7 gate definitions
│   ├── cron.md                       ← Schedule & import spoke
│   ├── history.md                    ← History search & cross-reference
│   ├── improve.md                    ← Improvement analysis spoke
│   ├── publish.md                    ← Publish findings spoke
│   ├── globals.yaml                  ← Defaults, methodology, instructions
│   ├── adapter-registry.yaml         ← 6 categories → adapter mappings
│   └── research-schema.yaml          ← Instance schema (includes roadmap + dashboard)
├── instances/
│   └── .gitkeep                      ← Research instances live here
├── templates/
│   └── research-template.yaml        ← Blank instance with roadmap + dashboard
├── scripts/
│   ├── validate.sh                   ← Validates instances + roadmap + dashboard
│   └── cron-runner.sh                ← Cron scheduling script
└── history/
    └── sessions/.gitkeep             ← Session archives
```

Validation is enforced via `validate.sh`, which checks: instance fields against the schema, phase IDs match kebab-case patterns, exit_criteria are non-empty, checklist items have descriptions, dependencies reference valid phases, and dashboard metrics/visuals meet their respective type constraints.

---

## Technical Decisions

**Why YAML instances, not new skills?** Creating a skill for every research topic would bloat the ecosystem. Instances are lightweight YAML files in `instances/` — they define scope, category, quality config, and roadmap without the overhead of a full skill structure.

**Why shared sub-schemas?** Both factories needed progress tracking and dashboarding. Without shared schemas, each would implement its own format, and a universal validator or frontend would need to handle N different structures. Shared schemas mean one validator, one renderer, one mental model.

**Why Progressive Disclosure at this granularity?** The target is agentic execution on 7B-14B models. These models have limited context windows and struggle with information overload. By splitting into ~100-line chunks, we ensure each load is digestible and the agent never needs to "find the right section" in a massive file.

**Why signal tracking in schemas?** Without telemetry, menu optimization is guesswork. By embedding signal arrays directly in the roadmap and dashboard schemas, we capture behavioral data at the point of interaction, feeding the menu-factory optimizer with structured, queryable signals.

---

## Lessons Learned

1. **Hub-and-spoke prevents drift.** When orchestration lives in a single hub, adapters stay focused on their core job. Cross-cutting concerns (scheduling, validation, publishing) have one canonical implementation.

2. **Shared schemas are force multipliers.** Extracting `roadmap-schema.yaml` and `dashboard-schema.yaml` into a shared location means any new factory gets progress tracking and dashboarding for free.

3. **UI contracts belong in data, not views.** The `dashboard-schema.yaml` proves that when YAML dictates rendering, frontends become thin mappings. This pattern scales to any UI framework.

4. **Progressive Disclosure is non-negotiable for agentic systems.** At 18+ files, loading everything would break execution. The disclosure map ensures agents load exactly what they need.

5. **Signal tracking closes the optimization loop.** Without data on what workflows are actually used, menus stay static. Signals enable continuous improvement.

---

## What's Next

The Research Factory is at v1.1.0 (L4 maturity). Immediate next steps include:
- Fixing pre-existing LSP type errors in `fetch_news.py`
- Debugging RSS feed and arXiv fetch reliability
- Building a visual dashboard that consumes the `dashboard-schema.yaml` output
- Exploring cross-factory linking (project-factory ↔ research-factory bidirectional references)

---

**Tags**: opencode, agentic-engineering, architecture, schemas, meta-factories, progressive-disclosure, research-automation
**Categories**: Engineering, AI Automation, System Architecture