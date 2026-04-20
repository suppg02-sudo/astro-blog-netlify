---
pubDatetime: 2026-04-04T00:04:34Z
title: "Running an AI Agent Company with Paperclip"
postSlug: "running-an-ai-agent-company-wi"
description: "Running an AI Agent Company with Paperclip"
tags:
  - others
---

Self-hosted AI agent orchestration is now possible with Paperclip - an open-source platform for running autonomous AI companies with org charts, budgets, heartbeats, and governance.

## What is Paperclip?

Paperclip is an open-source Node.js server and React UI that orchestrates a team of AI agents to run a business. Think of it this way: if OpenClaw is an employee, Paperclip is the company.

It brings your agents together under one roof with:
- **Org charts** - hierarchical agent structures with roles and reporting lines
- **Budgets** - monthly spending limits per agent
- **Heartbeats** - scheduled agent wake-ups for recurring tasks
- **Governance** - approval gates, pause/terminate any agent
- **Ticket system** - full conversation tracing and audit logs

## Why Self-Hosted Agent Orchestration Matters

If you are running multiple AI agents (Claude Code, Codex, Cursor, OpenClaw) across different projects, you likely face:
- Losing track of what each agent is doing
- No single view of all agent activity
- Manual context management between agents
- No budget enforcement (hello, runaway token spend)
- No governance or approval workflows

Paperclip solves this by treating AI agents like employees in a company.

## Quick Setup on My Ubuntu Server

Here is how I deployed Paperclip on my home server (ubuntu4):

```bash
# Clone the repo
git clone https://github.com/paperclipai/paperclip.git /media/docker/paperclip

# Build and run (quickstart mode with embedded PostgreSQL)
cd /media/docker/paperclip
docker run -d --name paperclip-local \
  -p 3100:3100 \
  -e HOST=0.0.0.0 \
  -e PAPERCLIP_HOME=/paperclip \
  -e PAPERCLIP_DEPLOYMENT_MODE=authenticated \
  -e PAPERCLIP_DEPLOYMENT_EXPOSURE=private \
  -e PAPERCLIP_PUBLIC_URL=http://ubuntu4:3100 \
  -e BETTER_AUTH_SECRET=your-secret-here \
  -v /media/docker/paperclip/data:/paperclip \
  paperclip-paperclip:latest
```

The container bundles everything - Node.js, embedded PostgreSQL, and even installs Claude Code and Codex globally inside the container.

## Integration Possibilities

My setup already includes:
- **LiteLLM** (port 4000) - unified LLM gateway for cost routing
- **PostgreSQL + pgvector** - memory and embeddings
- **Directus CMS** - content management
- **Tailscale** - remote access

Paperclip fits nicely:
- Route agent LLM calls through LiteLLM for unified billing
- Use existing PostgreSQL for data if needed
- Access via Tailscale for mobile management
- Agents can use the OpenCode adapter to work alongside me

## First Impressions

The UI looks like a task manager but with company management features:
- Create companies with org charts
- Hire agents (OpenCode, Claude Code, Codex, Cursor, etc.)
- Assign goals that cascade down the hierarchy
- Set budgets per agent
- Approve or reject agent actions
- Full audit trail of everything

## What is Next

Now that Paperclip is running, I will experiment with:
1. Adding my OpenCode agent as an employee
2. Setting up a research team with scheduled heartbeats
3. Testing budget enforcement on agent spend
4. Exploring multi-company isolation for different projects

The upcoming **Clipmart** marketplace for pre-built company templates could be interesting - think download a marketing team with prompts, skills, and workflows in one click.

## Resources

- [Paperclip GitHub](https://github.com/paperclipai/paperclip)
- [Documentation](https://paperclip.ing/docs)
- [Discord Community](https://discord.gg/m4HZY7xNG3)

**Tags**: ai-agents, orchestration, self-hosted, open-source, autonomous
**Categories**: AI Automation, Infrastructure