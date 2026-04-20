---
pubDatetime: 2026-02-25T17:00:00Z
title: "My OpenCode Integrated System: Complete Overview"
postSlug: "my-opencode-integrated-system-overview"
description: "My OpenCode Integrated System: Complete Overview"
tags:
  - opencode
  - ai-tools
  - system
  - architecture
  - infrastructure
---

A comprehensive look at my integrated AI-assisted development environment built on OpenCode.

---

## System Architecture at a Glance

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         OPENCODE INTEGRATED SYSTEM                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   PLUGINS   │    │   AGENTS    │    │   SKILLS    │    │  TRIGGERS   │  │
│  │     (2)     │    │    (25)     │    │    (71)     │    │    (19)     │  │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘    └──────┬──────┘  │
│         │                  │                  │                  │         │
│         └──────────────────┴──────────────────┴──────────────────┘         │
│                                    │                                        │
│                         ┌──────────┴──────────┐                            │
│                         │    AGENTS.md        │                            │
│                         │  (Global Rules)     │                            │
│                         └──────────┬──────────┘                            │
│                                    │                                        │
│  ┌─────────────────────────────────┴─────────────────────────────────────┐ │
│  │                           MCP SERVERS (3)                              │ │
│  │  • brave-search (web search)  • agent-browser (automation)            │ │
│  │  • crawl4ai (web scraping)                                             │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                    │                                        │
│  ┌─────────────────────────────────┴─────────────────────────────────────┐ │
│  │                        MEMORY SYSTEM                                   │ │
│  │  • Supermemory (persistent semantic memory)                           │ │
│  │  • Session persistence across conversations                           │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Core Platform: OpenCode

| Aspect | Details |
|--------|---------|
| **Primary Model** | Z.ai GLM-5 (all agents) |
| **Config File** | `~/.config/opencode/opencode.json` |
| **Global Rules** | `~/.config/opencode/AGENTS.md` |
| **Philosophy** | TELOS (data sovereignty, local-first, deterministic) |

---

## Component Breakdown

### 1. Plugins (2)

| Plugin | Purpose |
|--------|---------|
| `oh-my-opencode` | Shell integration, aliases, enhancements |
| `opencode-supermemory` | Persistent semantic memory integration |

### 2. Agents (25 Total)

**Core Subagents (11):**

| Agent | Role |
|-------|------|
| Sisyphus | Main agent - complex reasoning, coding |
| librarian | Fast searches, documentation lookup |
| explore | Thorough codebase analysis |
| oracle | Architecture decisions, deep reasoning |
| frontend-ui-ux-engineer | Visual/UI work |
| document-writer | Documentation generation |
| multimodal-looker | Image/PDF analysis |
| sisyphus-junior | Lightweight tasks, quick operations |
| metis | Pre-planning analysis, scope clarification |
| momus | Quality assurance, plan review |
| Hephaestus | Deep research mode |

**GSD Framework Agents (14):**

| Agent | Purpose |
|-------|---------|
| gsd-planner | Phase planning, task breakdown |
| gsd-executor | Plan execution, implementation |
| gsd-verifier | Verification and testing |
| gsd-debugger | Debugging and troubleshooting |
| gsd-roadmapper | Roadmap creation |
| gsd-codebase-mapper | Codebase analysis |
| gsd-phase-researcher | Phase-specific research |
| gsd-project-researcher | Project research |
| gsd-research-synthesizer | Research synthesis |
| gsd-integration-checker | Integration verification |
| gsd-plan-checker | Plan validation |
| gsd-settings | GSD configuration |
| gsd-set-model | Model configuration |
| gsd-set-profile | Profile management |

### 3. Skills (71 Directories)

**Categories:**

| Category | Examples |
|----------|----------|
| **Infrastructure** | containers, databases, nginx, portainer, dokploy |
| **Content Creation** | hugo, astro, glm-slide, presentation, beautiful-mermaid |
| **AI/Research** | research, flow, fabric, openrag, pdf-chunk-advisor |
| **Automation** | cron, activepieces, telegram, news |
| **System** | maintenance, diagnose, performance, space, versions |
| **Integration** | agent-browser, crawl4ai, context-registry |
| **Business** | ceo-board-prep, dashboard, homepage, filebrowser |

**Skill Maturity Levels (Evolution Protocol):**

| Level | Name | Characteristics |
|-------|------|-----------------|
| L1 | Raw | Single SKILL.md, no automation |
| L2 | Structured | Metadata, sections, commands |
| L3 | Script-Attached | Shell/Python automation |
| L4 | API-Integrated | REST/GraphQL endpoints |
| L5 | MCP/Deterministic | Full MCP server, typed tools |

### 4. Triggers (19)

| Trigger | Action |
|---------|--------|
| `a` | Quick browser action |
| `c` | Container status review |
| `check` | System health check |
| `config` | Configuration explorer |
| `docker-dash` | Docker dashboard |
| `ga` | AGENTS.md quick access |
| `git` | Git operations menu |
| `homepage` | Homepage dashboard |
| `mem-check` | Memory system status |
| `openrag` | OpenRAG stack management |
| `performance` | System performance analysis |
| `ragcheck` | PDF chunking analysis |
| `research` / `r` | Deep research mode |
| `rules` | Rules review menu |
| `setup` | Server setup from repository |
| `space` | Disk space analysis |
| `telos` | TELOS constitution menu |
| `why` | Root cause investigation |
| `youtube` | YouTube to blog workflow |

### 5. MCP Servers (3)

| Server | Purpose | Port |
|--------|---------|------|
| `brave-search` | Web search API | Local (node) |
| `agent-browser` | Browser automation (Playwright) | Local binary |
| `crawl4ai` | Web scraping/content extraction | Remote API |

---

## Supporting Infrastructure

### Docker Services (20+ Running)

| Service | Port | Purpose |
|---------|------|---------|
| Hugo Blog | 1314 | Static site generator |
| HugoAPI | 8092 | Blog post API |
| Homepage | 8765 | Dashboard |
| Homarr | 7575 | Alternative dashboard |
| Grafana | 3003 | Monitoring dashboards |
| Prometheus | 9090 | Metrics collection |
| Alertmanager | 9093 | Alert handling |
| Jaeger | 16686 | Distributed tracing |
| OpenTelemetry | 4317-4318 | Observability |
| OliveTin | N/A | Web-based scripts |
| Docling | 5001 | Document processing |

### Cron Jobs (15+ Scheduled)

| Frequency | Job |
|-----------|-----|
| Every 5 min | OOM protection, MCP cleanup, memory leak prevention |
| Every 15 min | Swap reclamation |
| Hourly | Idle process cleanup |
| Daily 2am | YouTube cleanup, tagging quality |
| Daily 3am | System review |
| Daily 4am | Agent browser daemon restart |
| Daily 9am | News briefing |
| Daily 11:55pm | Performance summary |
| Weekly | Comprehensive system review, roadmap reports |

---

## Data Flow Architecture

```
┌──────────────────────────────────────────────────────────────────────────┐
│                           USER INPUT                                      │
└─────────────────────────────────┬────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                        TRIGGER DETECTION                                  │
│  Single words: c, check, research, openrag, telos, etc.                  │
└─────────────────────────────────┬────────────────────────────────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    ▼                           ▼
┌──────────────────────────┐    ┌──────────────────────────┐
│     LOAD SKILL           │    │    LOAD AGENT            │
│  (e.g., research.md)     │    │  (e.g., librarian)       │
└────────────┬─────────────┘    └────────────┬─────────────┘
             │                               │
             └───────────────┬───────────────┘
                             ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                         MCP SERVER CALLS                                  │
│  brave-search → web search                                               │
│  agent-browser → browser automation                                      │
│  crawl4ai → web scraping                                                 │
└─────────────────────────────────┬────────────────────────────────────────┘
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                      SUPERMEMORY STORAGE                                  │
│  • Semantic search across all memories                                   │
│  • Project config, architecture, error solutions                         │
│  • Preferences and learned patterns                                      │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Key Files & Locations

| File | Purpose |
|------|---------|
| `~/.config/opencode/AGENTS.md` | Global rules, triggers, agent config |
| `~/.config/opencode/opencode.json` | OpenCode configuration, MCP servers |
| `~/.config/opencode/agents/*.md` | GSD agent definitions (14 files) |
| `~/.config/opencode/skills/*/SKILL.md` | Skill definitions (71 dirs) |
| `/media/docs/instructions/triggers/*.md` | Trigger definitions (19 files) |
| `/media/docker/website/` | Hugo blog site |
| `/media/docker/commands/` | Utility scripts |
| `~/freshstart/` | Setup repository (GitHub sync) |

---

## TELOS Philosophy (Guiding Principles)

| Principle | Meaning |
|-----------|---------|
| **Data Sovereignty** | All data stays local, no external dependencies |
| **Open Source** | Everything built on open source foundations |
| **Local-First AI** | AI processing happens on your hardware |
| **Deterministic Workflows** | Explicit, verifiable, reproducible processes |
| **Observability** | Full visibility into system behavior |

---

## Unique Innovations

### 1. GSD Framework

Goal-Structured Development with 14 specialized agents for systematic project execution. Each agent has a specific role in the planning → execution → verification cycle.

### 2. Skill Evolution Protocol

L1→L5 maturity levels with quality gates for crystallizing ad-hoc work into deterministic components. Skills evolve from raw documentation to full MCP servers.

### 3. Trigger System

19 single-word triggers for instant workflow activation without menu navigation. Type `research` to enter deep research mode, `c` to check containers, `check` for system health.

### 4. Memory Integration

Supermemory provides semantic search across all conversations and learned patterns. Knowledge persists across sessions and can be retrieved contextually.

### 5. Multi-Layer Documentation

AGENTS.md → Instructions → Triggers → Skills hierarchy ensures documentation is always discoverable and up-to-date.

---

## System Stats Summary

| Metric | Count |
|--------|-------|
| Total Agents | 25 |
| Total Skills | 71 |
| Total Triggers | 19 |
| MCP Servers | 3 |
| Plugins | 2 |
| Docker Services | 20+ |
| Cron Jobs | 15+ |
| Documentation Files | 40+ |

---

## What This System Does

This is a comprehensive AI-assisted development environment built for:

- **Infrastructure Management** - Docker containers, databases, nginx, monitoring
- **Content Creation** - Blog posts, presentations, documentation
- **Research** - Deep investigation with evidence-based methodology
- **Systematic Project Execution** - GSD framework for complex projects
- **Automation** - Cron jobs, scripts, workflow automation

All running locally with persistent memory and extensive automation.

---

*A living system that evolves through the skill evolution protocol, guided by TELOS principles.*