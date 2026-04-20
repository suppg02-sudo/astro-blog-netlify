---
pubDatetime: 2026-04-04T12:00:00Z
title: "Dual-Model AI Agent Routing With OpenCode"
postSlug: "dual-model-ai-agent-routing-opencode"
description: "Route brainstorming to Anthropic Opus 4.6 while keeping GLM-5 as your default coding model. One config file, two models, automatic routing."
tags:
  - opencode
  - ai-agents
  - model-routing
  - anthropic
---

# Dual-Model AI Agent Routing With OpenCode

Getting different AI models to handle different tasks in the same coding session — fast cheap models for routine work, expensive powerful models for creative thinking. Here's how I set it up with OpenCode's agent system.

> **TL;DR**: Route brainstorming to Anthropic Opus 4.6 while keeping GLM-5 as your default coding model. One config file, two models, automatic routing.

## The Problem

Most AI coding agents use a single model for everything. But different tasks need different capabilities:

| Task | Needs | Best Model |
|------|-------|------------|
| Code editing | Speed, accuracy | GLM-5 (fast, cheap) |
| Architecture planning | Deep reasoning | Opus 4.6 (powerful, expensive) |
| Brainstorming | Creativity, breadth | Opus 4.6 (creative, nuanced) |

Running Opus for everything would cost a fortune. Running GLM for everything sacrifices quality on creative tasks. The answer: **route by agent type**.

## The Architecture

```mermaid
graph LR
    A[User Message] --> B{Agent Router}
    B -->|@build| C[GLM-5]
    B -->|@plan| D[Opus 4.6]
    B -->|@brainstorm| D
    C --> E[Code Changes]
    D --> F[Design Decisions]
```

## Step 1: Create the Brainstorm Agent

Create a markdown file at `~/.config/opencode/agents/brainstorm.md`:

```yaml
---
description: Creative brainstorming using Anthropic Opus 4.6
mode: subagent
model: anthropic/claude-opus-4-6
temperature: 0.7
top_p: 0.9
permission:
  edit: allow
  bash:
    "git *": allow
    "*": deny
  webfetch: allow
---
```

The key line is `model: anthropic/claude-opus-4-6` — this pins the agent to Opus regardless of your default model.

The temperature of 0.7 gives creative divergence without losing coherence. Permissions are read-only for bash (git operations only) but allow edits so the agent can write design docs.

## Step 2: Configure Dual Models

In your `opencode.json` (project root or `.opencode/` directory), add the agent config:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "zai-coding-plan/glm-5",
  "agent": {
    "build": {
      "model": "zai-coding-plan/glm-5"
    },
    "plan": {
      "model": "anthropic/claude-opus-4-6"
    },
    "brainstorm": {
      "model": "anthropic/claude-opus-4-6"
    }
  }
}
```

The top-level `model` sets the default. Each agent overrides it.

## Step 3: Add Trigger Routing

In your `AGENTS.md`, add a routing rule:

```markdown
- **BRAINSTORM ROUTING**: When user types `brainstorm` or `bs`,
  ALWAYS delegate to the `@brainstorm` subagent which uses
  `anthropic/claude-opus-4-6`. Do NOT handle brainstorming yourself.
```

This ensures the primary agent (GLM-5) doesn't try to brainstorm itself — it hands off to Opus.

## How It Works in Practice

**Normal coding** (stays on GLM-5):
```
> refactor the auth module to use JWT
[GLM-5 handles it directly — fast, cheap]
```

**Brainstorming** (routes to Opus 4.6):
```
> @brainstorm give me 5 ideas for monetising AI agents
[Opus 4.6 takes over — creative, expensive, worth it]
```

**Planning** (routes to Opus 4.6):
```
> [Tab to Plan mode]
> design a microservices architecture for the payment system
[Opus 4.6 handles architecture — deep reasoning]
```

## Cost Impact

| Model | Approx Cost/Million Tokens | Best For |
|-------|---------------------------|----------|
| GLM-5 | Low | 80% of daily coding |
| Opus 4.6 | High | 20% creative/strategic work |

By routing only brainstorming and planning to Opus, you get frontier-model quality where it matters without the price tag on routine edits.

## What I Learned

1. **`@mention` is the trigger** — type `@brainstorm` in the TUI to invoke the pinned model
2. **The Task tool doesn't override models** — it inherits from the current session. Only `@` mentions read the agent's `model` field
3. **Temperature matters** — 0.7 for brainstorming (divergent), 0.1 for planning (focused)
4. **Permissions gate behaviour** — the brainstorm agent can write design docs but can't run arbitrary bash
5. **Restart required** — config changes need a fresh OpenCode session to take effect

<details>
<summary>Full Agent Prompt</summary>

```markdown
---
description: Creative brainstorming using Anthropic Opus 4.6
mode: subagent
model: anthropic/claude-opus-4-6
temperature: 0.7
top_p: 0.9
permission:
  edit: allow
  bash:
    "git *": allow
    "*": deny
  webfetch: allow
---

You are a creative brainstorming assistant powered by
Anthropic Claude Opus 4.6.

## Modes

**Quick Think**: Fast ideation. 5+ ideas, evaluate, recommend top 1-2.
**Structured**: Full design process with spec document and review gates.

## Process

1. Reframe the problem in 2-3 ways
2. Generate 5+ ideas without judgment
3. Evaluate by impact, feasibility, originality
4. Recommend top 1-2 with reasoning
5. Suggest concrete next steps
```

</details>

<details>
<summary>Finding Your Model IDs</summary>

Run `opencode models` to see all available models. The format is `provider/model-id`:

```
opencode/claude-opus-4-6        # Zen provider
anthropic/claude-opus-4-6       # Direct Anthropic
openrouter/anthropic/claude-opus-4.6  # Via OpenRouter
```

All three point to the same model. Use whichever provider you have configured.

</details>

**Tags**: opencode, ai-agents, model-routing, anthropic, glm-5, brainstorming
**Categories**: AI Automation, Tutorials
