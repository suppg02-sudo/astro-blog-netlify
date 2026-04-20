---
pubDatetime: 2026-04-04T21:14:38Z
title: "The Schema-Driven AI Operating System: Factories, Hubs, and Progressive Disclosure"
postSlug: "schema-driven-ai-operating-system"
description: "How we built a self-improving AI infrastructure where factories create factories, schemas enforce determinism, and progressive disclosure keeps context windows lean."
tags:
  - opencode
  - schema-design
  - meta-skills
  - ai-infrastructure
  - factories
---

# The Schema-Driven AI Operating System: How Factories, Hubs, and Progressive Disclosure Tame Agent Chaos

> Building a deterministic, self-improving AI infrastructure where schemas are law, factories create factories, and every decision survives session compaction.

## The Problem

AI coding agents are powerful but chaotic. Each session starts fresh — no memory, no consistent structure, no enforced patterns. Over months of daily use, patterns emerge: you keep building similar workflows, making similar decisions, creating similar files. But without a schema-driven backbone, every interaction is bespoke, fragile, and impossible for smaller models (7B-14B) to execute reliably.

This is the story of how we turned that chaos into a self-reinforcing operating system — one where **factories create factories**, **schemas enforce determinism**, and **progressive disclosure** keeps the context window lean enough for real work.

## The Architecture: Hub-and-Spoke

Everything is built on a hub-and-spoke pattern. A "factory" is a hub — a meta-skill that creates, validates, and manages other entities. Each factory has:

| Component | Purpose |
|-----------|---------|
| `SKILL.md` | The hub entry point — lightweight, progressive disclosure |
| `context/` | Spoke files loaded on demand (create, validate, export, etc.) |
| `templates/` | Blueprint files for new instances |
| `instances/` | Living instances (agents, research, projects) |
| `scripts/` | Executable automation (validate, export, cron) |
| `models/` | Pydantic validation layers |
| `schemas/` | Shared schemas referenced via `$ref` |

The key insight: **hubs are thin, spokes are deep**. The SKILL.md for each factory is under 400 lines. The real depth lives in context files loaded only when needed. This is progressive disclosure — the principle that saves your context window.

## Progressive Disclosure: The Context Multiplier

Progressive disclosure is the single most important principle in this system. It works in layers:

| Layer | What | When Loaded | Example |
|-------|------|-------------|---------|
| L0 | Trigger + 2-line description | Always | `sf` trigger, `af` trigger |
| L1 | SKILL.md hub (~400 lines) | On skill invocation | Menu, quick reference, workflow overview |
| L2 | Context spoke (~100 lines) | On specific task | `context/create.md`, `context/validate.md` |
| L3 | Template + schema (~200 lines) | During creation | `templates/agent-template.yaml`, `context/agent-schema.yaml` |
| L4 | Full reference docs | Deep research | `docs/references/`, external Context7 |

Without this, a single agent interaction would need to load 6,000+ lines of factory context. With it, most interactions use 400-600 lines — a 10x reduction.

## The Five Factories

### Skill Factory (sf)

The OG. Creates and evolves skills — the atomic units of the operating system. Every other factory is itself a skill created by this factory.

Skills evolve through maturity levels:

| Level | Name | What It Has |
|-------|------|-------------|
| L1 | Raw | Single SKILL.md file |
| L2 | Structured | Metadata, sections, menu |
| L3 | Script-Attached | Shell/Python automation scripts |
| L4 | API-Integrated | REST/GraphQL, templates, intent docs |
| L5 | MCP/Deterministic | Full MCP server, typed tools, integration tests |

The target: **smaller open-source models (7B-14B) should be able to execute L3+ skills correctly.** If a skill needs a frontier model to work, it's not deterministic enough.

### Menu Factory (mf)

Runtime-derived menus. Skills contain **only domain-specific options** — global suffix (Defer, Suggest, Discovery, Reminder), mode toggle (Desktop/Mobile), and mandatory per-skill options are auto-appended at presentation time by `build_menu.py`.

This was one of the hardest-won lessons. Originally, every skill hardcoded its own "Defer", "Suggest", and "Exit" options. When we wanted to add a new global option, we had to edit 50+ skill files. Now `global-config.json` is the single source of truth, and `build_menu.py` enforces it:

```
┌─────────────────────────┐
│  SKILL.md               │
│  (domain options ONLY)  │
└────────────┬────────────┘
             │
     ┌───────▼────────────────────┐
     │  build_menu.py             │
     │  ├─ read session mode      │
     │  ├─ read global-config     │
     │  ├─ inject mandatory opts  │
     │  ├─ truncate to max        │
     │  └─ append suffix + toggle │
     └───────┬────────────────────┘
             │
     ┌───────▼──────────┐
     │  question tool    │
     │  Mobile: ≤4 opts  │
     │  Desktop: ≤8 opts │
     └──────────────────┘
```

Mobile mode is the default — 4 options max. The system assumes you're working in a terminal, not a spreadsheet. Labels max 25 chars, descriptions max 40 chars. Clean, scannable, no emoji soup.

### Project Factory (pf)

Multi-phase projects with schema-driven lifecycle management. Each project follows a deterministic path:

```
🔴 idea → 🟠 plan → 🟢 active → 🔵 harvest → ⚪ rest
```

The schema is the contract. It defines everything a project CAN contain — actions with sub-actions, shopping lists with BOM tracking, supplemental context (webpages, blog articles, eRAG topics, research tasks), roadmaps with phases and checklists, dashboards with metrics and visuals.

The proactive dashboard is the killer feature. On every invocation, it scans all projects, calculates staleness, ranks by priority, and surfaces attention items before the menu even appears. A project that hasn't been updated in 7 days gets a ⚠️ STALE flag. A project in `active` phase with no blog posts gets a 📢 NO OUTPUT nudge. The system prods you to keep things moving.

### Agents Factory (af)

Creates, validates, and exports AI agent configurations as OpenCode subagent types with **Pydantic validation**. This is where the schema-first approach gets real teeth.

The key design decision: **agents and harnesses are separate entities**. An agent is identity, tools, and parameters. A harness is the tool contract, observation format, error recovery, and context budget. Multiple agents can share one harness. You can tune the harness without touching agent configs.

Validation is mandatory — a YAML instance must pass through Pydantic models before it can be exported. The lifecycle is enforced:

```
🔴 draft → 🟠 tested → 🟢 production → 🔵 archived
```

### Research Factory (rf)

Unified control plane for research across multiple adapters. The adapter registry maps research categories to adapter combos:

| Category | Primary | Secondary |
|----------|---------|-----------|
| News Monitoring | attention | news |
| GitHub Research | research | erag |
| One-Off Research | research | pghmem |
| Ephemeral Research | erag | research |
| Infinite Ephemeral | erag | research, attention |

Quality gates run after every execution: source diversity (3+ unique domains), recency (within 90 days), multi-source corroboration (2+ sources per claim), confidence tier tagging. Research that doesn't pass gates doesn't get published.

## The Schema Layer: Shared Contracts

Schemas are the connective tissue. The most important pattern is **deduplication via `$ref`**:

```
/root/.config/opencode/schemas/
├── signal-tracking-schema.yaml    ← THE hub schema
├── roadmap-schema.yaml            ← Shared by projects + agents
└── dashboard-schema.yaml          ← Shared by projects + agents
```

Before the schema dedup, `signal_tracking` was copy-pasted in 12 files. When we needed to change it, we had to update all 12 — and inevitably missed one. Now every factory and instance references the hub schema via `$ref: "/root/.config/opencode/schemas/signal-tracking-schema.yaml"`.

This principle applies everywhere:
- Project schema defines the contract for what a project CAN contain
- Agent schema defines the contract for what an agent MUST have
- Menu global-config defines the contract for how menus are rendered
- flows.yaml defines the contract for what ingestion routes exist

## The Ingestion Router: Where It All Connects

The ingestion router (`ingestion-router` skill) is where the user-facing magic happens. Paste a URL, and the system:

1. **Classifies** the input (YouTube, GitHub, web, file)
2. **Loads** the flow registry (`flows.yaml`)
3. **Presents** a multi-select menu (via `build_menu.py` + menu-factory rules)
4. **Executes** selected flows with shared-phase deduplication

The flow registry is pure data — YAML definitions of executable pipelines:

```yaml
- id: blog-post
  label: "Blog Post"
  emoji: "📝"
  description: "Transcript → Summary → Astro Blog → Telegram"
  skills: [transcription, astro, telegram]
  phases:
    - id: extract    → 🟡
    - id: validate   → 🟡
    - id: summarize  → 🟢
    - id: publish    → 🔵
    - id: notify     → 🟣
```

When multiple flows share early phases (e.g., blog-post and eRAG-research both need transcript extraction), the shared phase runs **once** and its output feeds both flows. No wasted work.

## The Memory System: Surviving Session Compaction

All of this is worthless if context dies at session end. The memory stack:

| Layer | Technology | Purpose |
|-------|-----------|---------|
| PostgreSQL + pgvector | `pghmem` CLI | 2,800+ memories, semantic search |
| Project YAML files | `pf` CLI | Structured project state |
| Deferred options | `deferred` CLI | Captured "later" decisions |
| eRAG topics | PostgreSQL + pgvector | Topic-based research knowledge |
| Astro blog | Directus CMS | Published knowledge assets |
| Session state | `current_state.md` | Session initialization anchor |

Every session starts by reading `current_state.md`, searching recent memories, listing active projects, and checking deferred items. Context is never truly lost.

## Self-Improvement: Factories Creating Factories

The deepest recursive pattern: **the skill-factory was created by itself**. The menu-factory is a skill managed by the skill-factory. The project-factory uses the menu-factory for its menus. The agents-factory references both.

```
skill-factory (sf)
  ├── created menu-factory (mf)
  ├── created project-factory (pf)
  ├── created agents-factory (af)
  ├── created research-factory (rf)
  └── created itself (sf)

menu-factory (mf)
  └── validates menus for all factories

project-factory (pf)
  └── references agents from af
  └── references research from rf

research-factory (rf)
  └── uses erag for knowledge storage
  └── uses attention for monitoring

agents-factory (af)
  └── exports to OpenCode subagent types
```

Each factory improves the others. When the menu-factory gets a new global suffix option, all factories benefit. When the skill-factory evolves to a new maturity level, the pattern propagates.

## What Makes This Different

Most AI tooling is prompt engineering — clever instructions that break when context shifts. This system is **schema engineering**:

1. **Schemas are law** — Pydantic validation, YAML schemas, JSON Schema. Structure is enforced, not suggested.
2. **Progressive disclosure is mandatory** — Every factory has a disclosure map. Load only what you need.
3. **Factories are recursive** — The system improves itself by applying its own patterns to itself.
4. **Context survives sessions** — PostgreSQL, YAML files, deferred lists, blog posts. Nothing is truly ephemeral.
5. **Determinism over cleverness** — If a 7B model can't execute it, the schema isn't tight enough.

The ultimate goal isn't to build cool AI tools. It's to build an operating system where AI agents produce consistent, validated, monetisable output — every session, every time.

---

**Tags**: ai-infrastructure, schema-design, meta-skills, factories, progressive-disclosure, opencode, agent-orchestration
