---
pubDatetime: 2026-04-04T10:49:29Z
title: "Inside Claw Code: The Architectural Map of Claude Code"
postSlug: "inside-claw-code-architectural-map-of-claude-code"
description: "Inside Claw Code: The Architectural Map of Claude Code"
tags:
  - claw-code
  - ai-tools
  - python
  - architecture
  - open-source
  - claude-code
---

# Inside Claw Code: The Architectural Map of Claude Code

> **TL;DR**: The fastest repository to reach 100K GitHub stars — Claw Code — is a Python recreation of Claude Code's architecture. It doesn't run Claude Code, but it maps every module, command, and tool, giving developers a blueprint for building their own AI coding assistants.

## Quick Summary

- **Claw Code** is a Python + Rust architectural recreation of Anthropic's Claude Code
- The original leaked repo was locked, but **claw-code-parity** (5.5K stars) remains active
- It maps **66 Python files, 207 commands, and 184 tools** across the Claude Code ecosystem
- The repo intentionally omits legally sensitive code — it's architecture only
- Six core components form the backbone: Port Manifest, Models, Commands, Tools, Query Engine, and Main

## What is Claw Code?

If you've been anywhere near developer circles recently, you've probably heard of Claw Code. It became the fastest GitHub repository to hit 100K stars — and then got locked. You can't clone it, you can't fork it. But the architecture lives on through **claw-code-parity**, a community-maintained Python port that currently sits at 5.5K stars.

The story starts when Claude Code's entire codebase was leaked. Rather than simply copying it (which would invite legal trouble), a team of smart engineers recreated the **architecture** in Python and Rust. They carefully stripped out anything that could cause legal issues while preserving the structural blueprint — the *how* rather than the *what*.

The result is a map. A detailed, navigable map showing exactly how systems like Claude Code are built.

## The Six Core Components

The Python implementation is organised around six fundamental files in the `src` directory:

| Component | File | Purpose |
|-----------|------|---------|
| **Port Manifest** | `port_manifest.py` | Scans folders, creates summaries, generates project overviews |
| **Models** | `models.py` | Defines data classes, represents entities, pure data transfer objects |
| **Commands** | `commands.py` | Stores metadata, mirrors Claude Code's command structure |
| **Tools** | `tools.py` | Tool definitions and executable actions |
| **Query Engine** | `query_engine.py` | Response generation, session management, multi-step interaction |
| **Main** | `main.py` | Entry point, connects all components, configuration handler, CLI |

Think of it like a robot: `main.py` is the on/off switch and main controller. The query engine is the decision-maker. `models.py` holds the physical components. And `port_manifest` is the body map — telling everything where to go.

## By the Numbers

The scale of the architecture is impressive:

- **66 total files** in the Python source directory
- **207 mirrored command entries** matching the original Claude Code structure
- **184 tools** across built-in agents, file operations, search, execution, and external integrations
- **33 modules** spanning infrastructure, commands, UI, interaction, and monitoring
- **22 unit tests** covering validation, CLI operations, bootstrap, and core features

## The Module Categories

All modules fall into six broader categories:

1. **Infrastructure** — System runtime, CLI runtime, server entry points, bootstrap setup, utils, constants
2. **UI Components** — Screens, component output styles, key bindings
3. **Agents** — Continuation assistant, coordinator, buddy bridge, remote agents
4. **Extensions & Plugins** — Plugin architecture and extensibility
5. **Data & State** — Session management, state persistence
6. **Network & Integration** — External service connections

## The Tools Ecosystem

With 184 tools mapped, the tool ecosystem is vast. It breaks down into several categories:

- **Built-in Agents** — Claude Code guide agent, explore agent, general-purpose agent
- **Agent Management** — Agent tool, run agent, resume agent
- **Agent Utilities** — Supporting functions for agent operations
- **File Operations** — Read, write, edit files, search and navigate
- **Execute & Runtime** — Command execution, runtime integration
- **External Integrations** — Third-party service connections

## CLI Commands

The repository exposes several CLI commands for exploring the architecture:

| Command | Output |
|---------|--------|
| `summary` | High-level project view with file counts, modules, and metrics |
| `manifest` | Files, modules, and layout details |
| `subsystems` | List of all system parts and their roles |
| `test` | Runs the 22 unit tests |
| `parity-audit` | Compares Python port vs original (requires locked repo) |
| `list-actions` | All available commands and tools |

## The Parity Approach

What makes Claw Code clever is the parity approach. The team didn't just build something inspired by Claude Code — they systematically mirrored its structure. The 207 commands and 184 tools aren't random; they're carefully mapped to match the original system's organisation. The parity audit command was designed to compare the two side by side, though since the original repo is now locked, this comparison is no longer possible.

## Why It Matters

Claw Code matters because it demystifies how production-grade AI coding assistants are built. Instead of a black box, you get a labelled schematic. You can see exactly how commands are structured, how tools are organised, how the query engine handles multi-step interactions, and how sessions are managed.

For anyone building AI developer tools, this is an invaluable reference architecture.

<details>
<summary>📖 Deep Dive: Running Claw Code Parity Locally</summary>

To explore the architecture yourself:

```bash
# Clone the parity repo (the original is locked)
git clone https://github.com/anthropics/claw-code-parity
cd claw-code-parity

# Generate architectural summary
python -m src.main summary

# View file manifest
python -m src.main manifest

# List subsystems
python -m src.main subsystems

# Run unit tests
python -m src.main test

# List all commands and tools
python -m src.main list-actions
```

Note: The parity audit command won't work since the original Claw Code repo is locked.

</details>

<details>
<summary>📚 References & Further Reading</summary>

- [Claw Code Parity on GitHub](https://github.com/anthropics/claw-code-parity) — The active fork with 5.5K stars
- Original video: [Data Science in your pocket — Claw Code Setup and Installation](https://www.youtube.com/watch?v=9ALnjKDA55w)
- The repository is written in Python and Rust, covering the full Claude Code architecture

</details>

**Tags**: claude-code, claw-code, ai-tools, architecture, python, open-source
**Categories**: AI Automation, Developer Tools
