---
pubDatetime: 2026-02-10T00:18:33Z
title: "Claude Code's Agent Teams Are Insane - Multiple AI Agents Coding Together in Real Time"
postSlug: "claude-code-agent-teams-multiple-ai-agents-coding-together"
description: "Cole Medin explores Claude Code's new experimental Agent Teams feature, which enables multiple AI agents to collaborate in real-time through shared task lists and peer-to-peer communication."
tags:
  - T-Mux
  - AI agents
  - multi-agent systems
  - sub-agents
  - collaborative AI
  - agentic engineering
  - Cole Medin
  - Agent Teams
  - Anthropic
  - Claude Code
---

## Overview

[Cole Medin](https://www.youtube.com/@ColeMedin) demonstrates Claude Code's new **Agent Teams** feature — an experimental capability that lets multiple AI agents collaborate in real-time on the same codebase through shared task lists and peer-to-peer communication. Unlike traditional sub-agents that work in isolation, Agent Teams enables true coordination where agents can tell each other things like *"let me complete this before you work on that."* While powerful enough for Anthropic to build an entire C compiler with 16 agents ($20K in API costs), the feature is still experimental, token-heavy (2–4x normal usage), and benefits from careful prompting and a "contract-first spawning" approach.

{{< mermaid >}}
graph LR
    subgraph "Sub-Agents (Isolation)"
        A[Lead Agent] -->|Task| B[Sub-Agent 1]
        A -->|Task| C[Sub-Agent 2]
        A -->|Task| D[Sub-Agent 3]
        B -->|Summary| A
        C -->|Summary| A
        D -->|Summary| A
    end

    subgraph "Agent Teams (Collaboration)"
        E[Lead Agent] -->|Shared Tasks| F[Team Agent 1]
        E -->|Shared Tasks| G[Team Agent 2]
        E -->|Shared Tasks| H[Team Agent 3]
        F <-->|Coordinate| G
        G <-->|Coordinate| H
        F <-->|Coordinate| H
    end

    classDef lead fill:#4A90D9,stroke:#2C5F8A,color:#fff
    classDef sub fill:#7B8D8E,stroke:#5A6B6C,color:#fff
    classDef team fill:#27AE60,stroke:#1E8449,color:#fff

    class A,E lead
    class B,C,D sub
    class F,G,H team
{{< /mermaid >}}

## What Are Agent Teams?

Agent Teams is a new **experimental feature** in Claude Code that allows a primary lead agent to spin up multiple AI agents in separate [T-Mux](https://github.com/tmux/tmux) terminals, all working on the same shared task list. What makes this novel:

- **Dynamic team formation** — The lead agent decides the team composition based on your request
- **Shared task list** — All agents work from and update the same task list
- **Real-time communication** — Agents coordinate with each other, not just report back to the lead
- **Automatic terminal management** — Agents spin up in split-pane terminals and spin down when done

## How to Set Up Agent Teams

**[00:03:25]** Getting started requires two steps:

1. **Enable the experimental feature** — Either set the environment variable `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=true` or add it to your `settings.json` (global or per-project in `.claude` directory)
2. **Install a split-pane terminal** — [T-Mux](https://github.com/tmux/tmux) (recommended) or [iTerm 2](https://iterm2.com/) for the visual split-pane experience. Windows users need WSL.

Once enabled, simply tell Claude you want to use the agent team feature — it knows what you mean.

## Agent Teams vs Sub-Agents

**[00:09:52]** This is the critical distinction every Claude Code user needs to understand:

| Aspect | Sub-Agents | Agent Teams |
|--------|-----------|-------------|
| **Communication** | Isolation — returns summary only | Peer-to-peer coordination |
| **Task Management** | Independent, no shared state | Shared task list |
| **Token Efficiency** | Very efficient (focused, minimal comms) | 2–4x higher token usage |
| **Best For** | Research, codebase analysis, web search | Implementation, coding, multi-component work |
| **Visibility** | Black box — only see final output | Can query agents mid-task |
| **Coordination** | None — agents may step on each other | Real-time updates prevent conflicts |

**Rule of thumb**: Use **sub-agents for research**, then feed that into a plan, then send the plan to an **Agent Team for implementation**.

## The C Compiler Example

**[00:02:06]** Anthropic demonstrated the power of Agent Teams by building an entire **C compiler from scratch** using 16 agents:

- Cost: **$20,000 in API costs** (vs. hundreds of thousands for a human dev team)
- Hundreds of thousands of lines of code generated
- Run in an iterative loop forcing agents to write, test, and refine
- Anthropic stated this would be **impossible for a single agent** — even Opus 4.6

## Current Limitations

**[00:14:12]** Despite the power, Agent Teams has notable issues:

1. **Requires very specific prompting** — Vague requests lead to hallucinations, weird team formations, and T-Mux terminal handling issues
2. **Parallel execution race conditions** — Agents with dependencies may race ahead before receiving critical information (e.g., backend agent building on an incorrect database schema)
3. **Limited collaboration visibility** — Hard to see when agents are actually communicating; you have to trust the process
4. **Token-heavy** — 2–4x the cost of regular Claude Code or sub-agents

## Contract-First Spawning: The Solution

**[00:16:38]** Cole Medin built a custom skill to address these limitations with a process called **contract-first spawning**:

{{< mermaid >}}
graph TD
    A[Plan Created] --> B[Lead Agent Analyzes Plan]
    B --> C[Identify Contract Chain]
    C --> D[Spawn Upstream Agent First]
    D --> E[Database Agent Builds Schema]
    E --> F[Contract Sent to Lead Agent]
    F --> G[Spawn Backend Agent]
    F --> H[Database Agent Continues Work]
    G --> I[Backend Builds on Correct Schema]
    I --> J[Contract Sent to Lead Agent]
    J --> K[Spawn Frontend Agent]
    H --> L[All Agents Work in Parallel]
    I --> L
    K --> L

    classDef start fill:#3498DB,stroke:#2980B9,color:#fff
    classDef process fill:#2ECC71,stroke:#27AE60,color:#fff
    classDef contract fill:#E67E22,stroke:#D35400,color:#fff
    classDef parallel fill:#9B59B6,stroke:#8E44AD,color:#fff

    class A start
    class B,C,D,E,G,H,I,K process
    class F,J contract
    class L parallel
{{< /mermaid >}}

Instead of launching all agents in parallel immediately:

1. **Identify the dependency chain** (database → backend → frontend)
2. **Spawn the most upstream agent first** (database)
3. **Wait for the "contract"** — the agent doesn't need to finish, just establish the foundation (e.g., schema)
4. **Then spawn dependent agents** — they build on correct assumptions
5. **Parallel work continues** — but with a smarter, dependency-aware flow

### Using the Skill

The skill provides a `/build` command:

```
/build with agent team <path-to-plan> [number-of-agents]
```

- Point it to a plan you've created (from sub-agent research or manual planning)
- Optionally define the number of agents, or let Claude decide dynamically
- Works for both **new projects** and **features in existing codebases**

## Recommended Workflow

**[00:13:50]** The optimal workflow combines both sub-agents and Agent Teams:

1. **Research phase** — Use sub-agents to analyze the codebase, search the web, gather requirements
2. **Planning phase** — Create a detailed plan from the research
3. **Implementation phase** — Feed the plan into an Agent Team with contract-first spawning
4. **Review phase** — Use Agent Teams for collaborative code review (security, quality, documentation agents)

## Key Takeaways

- **Agent Teams is the future of agentic development** — true multi-agent collaboration, not just parallel isolation
- **It's experimental and imperfect** — expect hallucinations, race conditions, and high token costs
- **Custom skills dramatically improve reliability** — contract-first spawning and specific terminal instructions make a huge difference
- **Sub-agents aren't dead** — they remain the best choice for research and token-efficient focused tasks
- **Context is king** — the choice between isolation (sub-agents) and collaboration (Agent Teams) ultimately comes down to managing your most precious resource: context

---

*Source: [Claude Code's Agent Teams Are Insane - Multiple AI Agents Coding Together in Real Time](https://www.youtube.com/watch?v=-1K_ZWDKpU0) by [Cole Medin](https://www.youtube.com/@ColeMedin)*

*Full transcript available at: `/media/docs/output/youtube_Claude_Codes_Agent_Teams_Are_Insane_-_Multiple_AI__-1K_ZWDKpU0_20260210_001548.txt`*