---
pubDatetime: 2026-02-24T21:01:00Z
title: "OpenCode AGENTS.md Configuration Reference"
postSlug: "agents-configuration-reference"
description: "OpenCode AGENTS.md Configuration Reference"
tags:
  - configuration
  - reference
  - opencode
---

## Model Configuration

All agents use **z.ai GLM-5** (`zai-coding-plan/glm-5`)

### Active Agents (8)

| Agent | Purpose |
|-------|---------|
| Sisyphus (main) | Complex reasoning, coding tasks |
| librarian | Fast searches, documentation lookup |
| explore | Thorough codebase analysis |
| oracle | Architecture decisions, deep reasoning |
| frontend-ui-ux-engineer | Visual/UI work |
| document-writer | Documentation generation |
| multimodal-looker | Image/PDF analysis |
| sisyphus-junior | Lightweight tasks, quick operations |

### GSD Agents (14)

Located at `~/.config/opencode/agents/`:

- gsd-planner, gsd-executor, gsd-verifier, gsd-debugger
- gsd-roadmapper, gsd-codebase-mapper, gsd-phase-researcher
- gsd-project-researcher, gsd-research-synthesizer
- gsd-integration-checker, gsd-plan-checker
- gsd-settings, gsd-set-model, gsd-set-profile

## Key Trigger Words

| Trigger | Action |
|---------|--------|
| `telos` | TELOS constitution menu (10 options) |
| `setup` | Server setup from GitHub repo |
| `openrag` / `rag` | OpenRAG stack management |
| `ragcheck` | PDF chunking analysis |
| `config` | Configuration Explorer |
| `containers` | Container management menu |
| `checkpoint` | Checkpoint management |
| `research` / `r` | Deep research mode |
| `a` | Quick browser automation |
| `space` | Disk space analysis |
| `url` | Service URL links |
| `cr` | Context registry |
| `mem` | Memory statistics |

## Server Configuration

- **Host**: `ubuntu4`
- **Tailscale FQDN**: `ubuntu4.tail75e52.ts.net`
- **URL Format**: `http://ubuntu4:PORT` (not localhost)

## Documentation Locations

- Instructions: `~/.config/opencode/docs/instructions/`
- Triggers: `~/.config/opencode/docs/instructions/triggers/`
- Skills: `~/.config/opencode/skills/` (53 skills)

## Key Paths

| Path | Purpose |
|------|---------|
| `~/.config/opencode/AGENTS.md` | Global agent instructions |
| `~/.config/opencode/oh-my-opencode.json` | Agent model config |
| `~/.config/opencode/environment.md` | Environment tracking |
| `~/freshstart/` | Setup repository backup |

## Skill Evolution Protocol

Levels: Raw → Structured → Script-Attached → API-Integrated → MCP/Deterministic

## Safety Restrictions

- NEVER execute `rm -rf *` or wildcard deletions
- NEVER use `docker image prune -a` or `docker system prune -a`
- Always ask confirmation before destructive operations

## Setup Repository

**Source**: https://github.com/suppg02-sudo/freshstart

- Code, configuration templates, documentation
- SETUP.md, START_HERE.md, environment.md