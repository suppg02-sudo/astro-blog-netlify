---
pubDatetime: 2026-04-01T16:47:23Z
title: "Your Stack vs Pi: How Your OpenCode Environment Compares"
postSlug: "your-stack-vs-pi-how-your-open"
description: "Your Stack vs Pi: How Your OpenCode Environment Compares"
tags:
  - others
---

> **TL;DR**: Your environment already implements many of Pi's philosophies (minimalism, freedom, extensibility) but goes significantly further with skills, progressive disclosure, memory persistence, and a full self-hosted infrastructure stack. Here's the detailed comparison.

## Quick Summary

- Your OpenCode setup shares Pi's minimalism philosophy but layers on a structured skill system (50+ skills)
- Where Pi gives freedom through no sandboxing, your environment gives freedom through permissive `opencode.json` config (all reads/writes/bash allowed)
- Your stack adds what Pi deliberately omits: memory (pghmem/2,846+ memories), MCP integrations (5 servers), cron automation, and a full self-hosted services layer
- Both agree on one key principle: frontier models benefit more from freedom than rigid guardrails

## The Architecture Comparison

### What You Have That Pi Also Has

| Feature | Pi | Your Stack |
|---------|-----|-----------|
| CLI agent | Yes | OpenCode (GLM-5.1) |
| Multi-model support | 20+ providers | GLM-5.1 + GitHub Models via MCP |
| No sandboxing | Default | `opencode.json` grants full access to `/media/docker/**`, `/root/**`, `/mnt/**`, etc. |
| TypeScript SDK | Yes | OpenCode SDK (TypeScript, event-driven) |
| Event-driven architecture | `agent.subscribe()` | OpenCode MCP protocol + superpowers plugin system |
| Self-hosted model | No (uses APIs) | Self-hosted Directus, Grafana, Neo4j, PostgreSQL |

### What You Have That Pi Doesn't

| Feature | Your Stack | Pi |
|---------|-----------|-----|
| **Skill system** | 50+ skills with progressive disclosure (L0-L4) | None — bare agent |
| **Memory persistence** | pghmem (PostgreSQL + pgvector, 2,846+ memories) | No persistent memory |
| **MCP servers** | 5 (Context7, agent-browser, GitHub, Brave Search, Crawl4AI) | No built-in MCP |
| **Self-hosted CMS** | Directus + Astro blog | None |
| **Infrastructure monitoring** | Grafana + Prometheus + OpenTelemetry + Jaeger | None |
| **Cron automation** | Scheduled tasks linked to skills | No scheduling |
| **Knowledge crystallization** | Skill evolution protocol, cross-pollination merges | None |
| **Progressive disclosure** | L0-L4 layers across skills, menus, blog posts | None |
| **Ad filtering** | AdGuard Home | N/A |
| **Survey management** | Formbricks + Directus integration | N/A |
| **Web scraping** | Crawl4AI + supermarket scraper | None |
| **Graph database** | Neo4j 5.19 | None |
| **Telegram integration** | Full bot with notifications | None |
| **Browser automation** | agent-browser MCP for visual testing | DOOM easter egg |
| **Deterministic systems** | AGENTS.md designed for 7B-14B models | No model portability concern |

### What Pi Has That You Don't

| Feature | Pi | Your Stack |
|---------|-----|-----------|
| **Built-in OAuth for subscriptions** | ChatGPT Plus, Claude Pro, Copilot auth out of the box | Single model (GLM-5.1) |
| **JSON/RPC modes** | One-shot print, JSON event streaming, RPC function calling | OpenCode interactive mode |
| **Self-awareness** | Reads own source from node_modules | Skills loaded via SKILL.md |
| **Auto-compaction** | Handles context window automatically | Session-based, manual context management |

## The Philosophy Overlap

Both your environment and Pi share a core belief that the video highlighted:

> "The more freedom you give these things, the more power you get out of them."

Your `opencode.json` config reflects this exactly:

```json
"permission": {
  "read": "allow",
  "edit": "allow", 
  "write": "allow",
  "bash": "allow"
}
```

No permission checks. No sandboxing. Full access to Docker volumes, root filesystem, and external directories. Like the video presenter says about Pi — you could delete your home directory. But frontier models don't do that. The trust is warranted.

## Where You've Gone Further

### The Skill System
Pi's minimalism means you build everything from scratch. Your 50+ skills provide pre-built workflows for common tasks (transcription, blog publishing, code review, debugging) with progressive disclosure so you load only what you need. This is the "batteries-included" approach that Pi deliberately avoids — but your skills are optional, not forced.

### Memory Persistence
Pi has no memory between sessions. Your pghmem system (PostgreSQL + pgvector with 2,846+ memories) means context survives across conversations. When you start a session, the protocol runs `pghmem search "decision" --recent 7d` to restore recent context.

### Self-Hosted Infrastructure
Pi is a pure client tool. Your environment runs 30+ Docker containers — Directus CMS, Grafana monitoring, Neo4j graph database, PostgreSQL with pgvector, Crawl4AI, AdGuard, Formbricks, and more. The agent has direct access to all of these through filesystem paths.

### The 7B-14B Design Principle
Your AGENTS.md states: *"All instructions, schemas, and workflows should be designed so smaller open-source models (7B-14B) can execute them correctly."* This is a constraint Pi doesn't share — Pi targets frontier models only. Your skill system with progressive disclosure, structured schemas, and deterministic workflows is specifically designed to make smaller models productive.

<details>
<summary>Technical Details: Your MCP Stack vs Pi's Provider System</summary>

**Pi's approach**: Built-in auth for 20+ providers via subscription OAuth + API keys. The `getModel()` function gives type-safe access to all providers.

**Your approach**: 5 MCP servers extending the agent's capabilities:
- **Context7** — Library documentation lookup
- **agent-browser** — Visual testing and browser automation
- **GitHub** — Repository, issue, and PR management
- **Brave Search** — Web search for research
- **Crawl4AI** — Web scraping and content extraction

Plus a plugin system (`superpowers@git+https://github.com/obra/superpowers.git`) that adds brainstorming, TDD, debugging, and other workflow skills.

The key difference: Pi optimizes for model access breadth (many providers). Your stack optimizes for capability depth (many tools for one model).

</details>

## The Verdict

Your environment is what happens when you take Pi's philosophy of freedom and extend it with infrastructure. You're not running a minimal agent — you're running a full agentic platform with:

- **Agent**: OpenCode (GLM-5.1) with full filesystem access
- **Memory**: PostgreSQL + pgvector (2,846+ memories)
- **Knowledge**: 50+ skills with progressive disclosure
- **Infrastructure**: 30+ self-hosted Docker services
- **Automation**: Cron jobs linked to skills
- **Monitoring**: Grafana + Prometheus + OpenTelemetry
- **Communication**: Telegram bot for notifications and Q&A
- **Content**: Directus CMS + Astro blog pipeline

The video asks "which SDK is right for you?" For your use case, the answer is clear — you've already built something more comprehensive than any single SDK provides. The question isn't whether to switch to Pi. It's whether Pi's SDK could enhance specific parts of your stack (like the event-driven agent building for your dashboard or BTCA-like tools).

**Tags**: ai, coding-agents, opencode, pi, comparison, infrastructure, self-hosted