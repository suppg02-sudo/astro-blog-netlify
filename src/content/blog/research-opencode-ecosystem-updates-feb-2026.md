---
pubDatetime: 2026-02-24T22:00:00Z
title: "Research: OpenCode Ecosystem - Updates, Forks & Alternatives (Feb 2026)"
postSlug: "research-opencode-ecosystem-updates-feb-2026"
description: "Research: OpenCode Ecosystem - Updates, Forks & Alternatives (Feb 2026)"
tags:
  - openmemory
  - opencode
  - ai-agents
  - oh-my-opencode
  - research
---

## Executive Summary

- **OpenCode** (anomalyco) is massive: **109,912 stars** with active daily development
- **oh-my-opencode** plugin ecosystem: **33,883 stars** with 46+ hooks
- **Get Shit Done (GSD)**: **19,373 stars** - spec-driven development system for Claude Code/OpenCode
- **Memory solutions** are the hot category: mem0 (47k stars), claude-mem (30k stars), Letta (21k stars)
- **Google ADK** (17k stars) is a major new competitor for agent orchestration
- **GPT-5.3 Codex** support recently added to OpenCode

---

## 1. OpenCode (anomalyco) - The Core Project

### Current Status

| Metric | Value |
|--------|-------|
| Stars | **109,912** |
| Forks | 10,927 |
| Latest Release | v1.2.10 (Feb 20, 2026) |
| Last Updated | **Today** (actively maintained) |
| Language | TypeScript |

**Key Finding**: OpenCode is one of the largest AI coding agent projects, with 3x more stars than oh-my-opencode.

### Recent Development Activity

| Date | Commit | Author |
|------|--------|--------|
| Feb 24, 2026 | GPT 5.3 Codex support | Frank |
| Feb 24, 2026 | Ignore stale part deltas | adamelmore |
| Feb 24, 2026 | Alpha models restricted to admin | Frank |
| Feb 24, 2026 | Cancel comment unhighlight fix | Filip |

### Top Forks

| Fork | Stars | Purpose |
|------|-------|---------|
| [evil-opencode](https://github.com/winmin/evil-opencode) | 187 | Unleashed - removes safety guardrails |
| [shuvcode](https://github.com/Latitudes-Dev/shuvcode) | 80 | Unofficial fork |
| [AIGeniusInstitute/opencode](https://github.com/AIGeniusInstitute/opencode) | 35 | AI Genius fork |
| [pi-terminal](https://github.com/AllAboutAI-YT/pi-terminal) | 28 | Prompt Injection Terminal |
| [nanocode](https://github.com/nanogpt-community/nanocode) | 27 | nano-gpt integration |

---

## 2. oh-my-opencode - The Plugin Ecosystem

### Current Status

| Metric | Value |
|--------|-------|
| Stars | 33,883 |
| Forks | 2,550 |
| Latest Release | v3.8.5 (Feb 24, 2026) |
| Last Updated | Today |

### Latest Release (v3.8.5)

- Significantly improved editing accuracy
- Fixed hashline implementation
- 46 hooks now available

### Top Variants

| Variant | Stars | Focus |
|---------|-------|-------|
| [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | 7,253 | Teams-first orchestration |
| [oh-my-opencode-slim](https://github.com/alvinunreal/oh-my-opencode-slim) | 1,605 | Token-efficient version |

---

## 3. OpenMemory - Memory Layer Ecosystem

### Top Memory Solutions

| Project | Stars | Description |
|---------|-------|-------------|
| [mem0](https://github.com/mem0ai/mem0) | 47,939 | Universal memory layer for AI Agents |
| [claude-mem](https://github.com/thedotmack/claude-mem) | 30,688 | Claude Code plugin with AI-compressed memory |
| [Letta](https://github.com/letta-ai/letta) | 21,243 | Stateful agents with advanced memory |
| [Supermemory](https://github.com/supermemoryai/supermemory) | 16,609 | Fast, scalable memory engine |
| [CaviraOSS/OpenMemory](https://github.com/CaviraOSS/OpenMemory) | 3,405 | **Local persistent memory with MCP server** |
| [Cipher](https://github.com/campfirein/cipher) | 3,537 | Memory layer for coding agents |

### CaviraOSS/OpenMemory (Detailed)

| Metric | Value |
|--------|-------|
| Stars | 3,405 |
| Forks | 395 |
| Latest Release | v1.2.3 (Dec 12, 2025) |
| Last Updated | Feb 24, 2026 (active) |
| Language | TypeScript |

**Key Features**:
- Multi-sector memory (episodic, semantic, procedural, emotional, reflective)
- Temporal knowledge graph with `valid_from`/`valid_to`
- Decay engine with adaptive forgetting
- Explainable waypoint traces
- MCP server for Claude/Cursor/Windsurf
- VS Code extension
- Python + Node SDKs
- Self-hosted, local-first (SQLite/Postgres)

**Integrations**: LangChain, CrewAI, AutoGen, Streamlit, MCP, VS Code

**Connectors**: GitHub, Notion, Google Drive, OneDrive, Web Crawler

### OpenCode-Specific Memory Plugins

| Plugin | Stars | Description |
|--------|-------|-------------|
| [opencode-mem](https://github.com/tickernelz/opencode-mem) | 129 | Local vector database memory |
| [opencode-plugin-simple-memory](https://github.com/cnicolov/opencode-plugin-simple-memory) | 44 | Persistent memory across sessions |

---

## 4. Skills Ecosystem

### Cross-Agent Skill Systems

| Project | Stars | Description |
|---------|-------|-------------|
| [Obsidian Skills](https://github.com/kepano/obsidian-skills) | 10,562 | Agent skills for Obsidian |
| [Awesome Agent Skills](https://github.com/libukai/awesome-agent-skills) | 2,107 | Comprehensive skills guide |
| [Awesome LLM Skills](https://github.com/Prat011/awesome-llm-skills) | 929 | Curated skills for AI agents |
| [SkillShare](https://github.com/runkids/skillshare) | 594 | Sync skills across CLI tools |
| [Context Engineering Kit](https://github.com/NeoLabHQ/context-engineering-kit) | 523 | Quality-focused Claude Code skills |
| [AgentSys](https://github.com/agent-sh/agentsys) | 481 | 14 plugins, 43 agents, 30 skills |
| [OpenCode Skills](https://github.com/malhashemi/opencode-skills) | 457 | OpenCode-specific skills |
| [OpenContext](https://github.com/0xranx/OpenContext) | 400 | Personal context store |
| [SkillKit](https://github.com/rohitg00/skillkit) | 396 | Portable skills across 40+ agents |
| [Open Skills](https://github.com/instavm/open-skills) | 375 | Run Claude Skills locally |

---

## 5. Alternatives & Competitors

### Agent Development Kits

| Project | Stars | Description |
|---------|-------|-------------|
| [Google ADK (Python)](https://github.com/google/adk-python) | 17,953 | Code-first toolkit for AI agents |
| [Google ADK (Go)](https://github.com/google/adk-go) | 6,990 | Go version of agent toolkit |
| [Haystack](https://github.com/deepset-ai/haystack) | 24,301 | AI orchestration framework |

### Agent Orchestration

| Project | Stars | Description |
|---------|-------|-------------|
| [Claude Squad](https://github.com/smtg-ai/claude-squad) | 6,133 | Multi-agent terminal manager |
| [Emdash](https://github.com/generalaction/emdash) | 1,600 | Agentic IDE (YC W26) |
| [Agent Deck](https://github.com/asheshgoplani/agent-deck) | 1,050 | Terminal session manager |

---

## 6. Get Shit Done (GSD) - Spec-Driven Development

### Current Status

| Metric | Value |
|--------|-------|
| Stars | **19,373** |
| Forks | 1,716 |
| Latest Release | v1.20.6 (Feb 23, 2026) |
| Last Updated | Feb 23, 2026 (active) |
| Language | JavaScript |

**Description**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code and OpenCode.

### Key Features

- **Context Engineering** - Solves "context rot" (quality degradation as context fills)
- **XML Prompt Formatting** - Structured tasks with built-in verification
- **Multi-Agent Orchestration** - Orchestrator spawns specialized agents
- **Wave Execution** - Parallel plans where possible, sequential when dependent
- **Atomic Git Commits** - Each task gets its own commit
- **Fresh Context Per Plan** - 200k tokens per implementation, zero accumulated garbage

### Workflow Commands

| Command | Purpose |
|---------|---------|
| `/gsd:new-project` | Full initialization: questions → research → requirements → roadmap |
| `/gsd:discuss-phase` | Capture implementation decisions before planning |
| `/gsd:plan-phase` | Research + plan + verify for a phase |
| `/gsd:execute-phase` | Execute all plans in parallel waves |
| `/gsd:verify-work` | Manual user acceptance testing |
| `/gsd:quick` | Ad-hoc tasks with GSD guarantees |

### Supported Runtimes

- Claude Code
- OpenCode
- Gemini CLI
- Codex

### Community Forks

| Fork | Stars | Purpose |
|------|-------|---------|
| gsd (onewithdev) | 16 | Personal adaptation |
| get-shit-done-codex | 14 | Codex-specific version |
| get-stuff-done-for-kilocode | 14 | Kilo Code adaptation |
| get-shit-done-autopilot | 4 | Autonomous "ralph loop" mode |

### Comparison: GSD vs OpenAgentsControl vs oh-my-opencode

| Feature | GSD | OpenAgentsControl | oh-my-opencode |
|---------|-----|-------------------|----------------|
| Philosophy | Spec-driven development | Plan-first + approval gates | Autonomous parallel agents |
| Context | Fresh per plan | Your patterns loaded | Agent-driven |
| Execution | Wave-based parallel | Sequential with approval | Full parallel |
| Best for | Complex features, brownfield | Teams, production code | Speed, power users |
| Stars | 19k | 2k | 34k |

---

## 6. OpenAgentsControl

### Current Status

| Metric | Value |
|--------|-------|
| Stars | 2,200 |
| Forks | 205 |
| Latest Release | v0.7.1 (Jan 30, 2026) |
| Last Updated | Feb 23, 2026 (active) |
| Language | TypeScript |

**Description**: AI agent framework for plan-first development workflows with approval-based execution. Multi-language support (TypeScript, Python, Go, Rust) with automatic testing, code review, and validation built for OpenCode.

### Key Features

- **Pattern Control** - Define your patterns once, AI uses them forever
- **Approval Gates** - Review and approve before execution
- **Context System** - Agents load YOUR coding standards automatically
- **Token Efficient** - MVI principle (80% reduction)
- **Team-Ready** - Shared context files for consistent code

### Included Agents

| Agent | Purpose |
|-------|---------|
| OpenAgent | General tasks, learning |
| OpenCoder | Production development |
| SystemBuilder | Custom AI systems |
| ContextScout | Smart pattern discovery |
| TaskManager | Feature breakdown |
| CoderAgent | Focused implementations |
| TestEngineer | Test authoring |
| CodeReviewer | Security analysis |
| ExternalScout | Live documentation fetching |

### Comparison to oh-my-opencode

| Feature | OpenAgentsControl | oh-my-opencode |
|---------|-------------------|----------------|
| Philosophy | Control & repeatability | Autonomy & speed |
| Execution | Approval gates required | Parallel auto-execution |
| Context | Your patterns loaded | Agent-driven |
| Best for | Teams, production code | Power users, speed |

---

## Confidence Assessment

| Finding | Confidence | Justification |
|---------|------------|---------------|
| OpenCode dominance | **Very High** | 109k stars, active daily commits |
| oh-my-opencode ecosystem | **High** | Direct GitHub API data |
| OpenAgentsControl features | **High** | Found repository, detailed docs |
| Memory ecosystem size | **High** | Multiple verified sources |
| Skills ecosystem | **High** | 10+ cross-platform skill systems |

---

## Key Takeaways

1. **OpenCode is dominant**: 109k stars with daily active development
2. **Plugin ecosystem thriving**: oh-my-opencode adds 46+ hooks, 43 agents
3. **Memory is critical**: 5+ major solutions competing for agent context
4. **Skills are portable**: Multiple systems for sharing across Claude Code, OpenCode, Codex
5. **GPT-5.3 Codex**: Latest model support just added
6. **GSD (19k stars)**: Spec-driven development with wave execution - solves "context rot"
7. **OpenAgentsControl**: Plan-first framework with approval gates - alternative philosophy

---

## References

- [OpenCode](https://github.com/anomalyco/opencode)
- [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)
- [OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)
- [Get Shit Done (GSD)](https://github.com/gsd-build/get-shit-done)
- [CaviraOSS/OpenMemory](https://github.com/CaviraOSS/OpenMemory)
- [mem0](https://github.com/mem0ai/mem0)
- [claude-mem](https://github.com/thedotmack/claude-mem)
- [Google ADK](https://github.com/google/adk-python)
- [Letta](https://github.com/letta-ai/letta)

---

*Research conducted: February 24, 2026*
*Sources: GitHub API, repository statistics*