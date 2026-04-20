---
pubDatetime: 2026-04-04T12:00:00Z
title: "Journey: A Registry for AI Agent Workflows"
postSlug: "journey-registry-ai-agent-workflows"
description: "Matthew Berman introduces Journey (journeykits.ai) — an npm-like registry for sharing end-to-end AI agent workflows called 'kits' that include skills, tools, memories, tests, and failure examples. Thi"
tags:
  - agents
  - llm
  - openclaw
  - ai
  - workflows
  - journey
---

# Journey: A Registry for AI Agent Workflows

> **TL;DR**: Matthew Berman launches Journey (journeykits.ai) — a registry where you can discover, install, and share complete end-to-end workflows for AI agents. Think npm for agent workflows.

## Quick Summary

- **Journey** is a marketplace/registry for AI agent workflows called "kits"
- A **kit** packages everything an agent needs: skills, tools, memories, learnings, tests, and failure examples
- Teams can share kits internally or publish them publicly
- Built on the premise that replicating useful agent workflows is currently too hard
- Launches alongside an eBook of 25 OpenClaw use cases

## The Problem Journey Solves

If you've built a sophisticated workflow for your AI agent — say a multi-step research pipeline — sharing that workflow with others (or even replicating it yourself on a different agent) is remarkably difficult. You can describe what you did, but the person on the other end has to reconstruct everything from scratch: the prompt engineering, the tool configurations, the edge cases they learned about, the failure modes they debugged.

Matthew experienced this firsthand while making videos about OpenClaw. The most common question wasn't "how does it work?" but "what are you actually using it for?" The use cases were what people found most compelling — and the hardest thing to replicate.

## What's in a Kit?

A Journey kit is a fully packaged workflow, ready to install. Each kit includes:

- **Skills** — The core capabilities the workflow provides
- **Tools** — Regular code that the agent can execute
- **Learnings** — Captured knowledge from previous runs
- **Memories** — Context the agent needs to operate effectively
- **Services** — External integrations the workflow connects to
- **Tests** — Verification that the workflow works as expected
- **Failure examples** — Known edge cases and how to handle them

The goal is that you can point your agent at a kit and it immediately knows how to use it — no reinventing the wheel.

## The Registry Model

Journey follows the npm pattern: there's a central registry where kit creators publish their workflows, and consumers discover and install them. The registry supports:

- **Public kits** — Open workflows anyone can use
- **Team kits** — Shared within an organization for consistent agent behavior
- **Versioning** — Kits evolve over time with updates and improvements
- **Ratings and feedback** — Community-driven quality signals

## How Teams Use It

Journey is designed with team workflows in mind. A team can:

1. Build a workflow once, package it as a kit
2. Share it across all team members' agents
3. Iterate on the kit as they learn more
4. Publish internally for consistency, or publicly for the community

This is particularly powerful for organizations running multiple agents that need to follow the same processes — customer support workflows, research pipelines, content creation chains, and so on.

## Journey in Practice: Knowledge-Base RAG Kit

Matthew demonstrated his own Knowledge-Base RAG kit — a workflow he uses daily. Anytime he encounters an article, tweet, or piece of content he wants to remember, the workflow:

1. Captures and processes the content
2. Stores it in a RAG (Retrieval-Augmented Generation) knowledge base
3. Makes it searchable and available for future agent queries

This is a prime example of the kind of workflow that's valuable to share — once configured, it works seamlessly, but configuring it from scratch requires significant effort.

## Why This Matters

The AI agent ecosystem is maturing past the "build everything from scratch" phase. As agents become more capable, the bottleneck shifts from model capability to workflow design and knowledge transfer. Journey addresses this by:

- **Reducing duplication** — Why rebuild what someone else has already debugged?
- **Accelerating adoption** — New users can start with proven workflows instead of empty agents
- **Enabling collaboration** — Teams and communities build on each other's work
- **Preserving institutional knowledge** — Workflows capture not just what to do, but what went wrong

## Getting Started

Visit [journeykits.ai](https://www.journeykits.ai) to browse available kits and install them for your agent. The platform is actively seeking feedback from early users.

---

*Source: [Matthew Berman — "I built something..."](https://www.youtube.com/watch?v=vn_kU928nww) (YouTube, April 2026)*

**Tags**: ai, agents, workflows, journey, openclaw, llm
