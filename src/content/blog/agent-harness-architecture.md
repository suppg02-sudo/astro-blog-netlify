---
pubDatetime: 2026-04-01T17:00:00Z
title: "The Agent Harness: How AI Agents Are Orchestrated, Equipped, and Remembered"
postSlug: "agent-harness-architecture"
description: "How the agent harness orchestrates AI agents through six layers: LLM, harness, instructions, capabilities, memory, and outputs."
tags:
  - agent-harness
  - opencode
  - ai-agents
  - architecture
  - svg-diagrams
  - mcp
---

# The Agent Harness: How AI Agents Are Orchestrated, Equipped, and Remembered

Every AI coding assistant has the same fundamental challenge: how do you turn a general-purpose language model into a reliable, skilled developer that understands your project, follows your rules, and remembers what it learned yesterday? The answer is the **agent harness** — the orchestration layer that sits between raw LLM capability and productive engineering output.

## Quick Summary

- The agent harness is a layered architecture: LLM → Harness → Instructions → Capabilities → Memory
- Skills provide reusable workflows; MCP tools provide external integrations; Superpowers provide meta-patterns
- Persistent memory (PostgreSQL + pgvector) enables cross-session learning
- Instructions (CLAUDE.md, AGENTS.md) encode project-specific behavioural rules
- The feedback loop between memory and orchestration is what separates a session-aware agent from a stateless chatbot

## The Architecture

The agent harness follows a six-layer architecture, from the LLM core at the top to the outputs at the bottom. Each layer has a distinct responsibility and communicates with adjacent layers through well-defined interfaces.

### Layer 1: The LLM Core

At the centre of everything is the language model. Claude, GPT, Gemini — these are powerful reasoning engines, but they're fundamentally stateless. They don't know your project structure, your coding conventions, or what you decided last Tuesday. The harness changes that.

### Layer 2: The Agent Harness

This is the orchestration layer. Its job is to decompose complex tasks into manageable steps, route each step to the right tool, and manage the context window so the LLM always has the right information at the right time.

Key responsibilities include:
- **Task decomposition** — breaking "add authentication to the API" into concrete steps
- **Tool routing** — deciding which tool to call (file read, bash command, browser interaction)
- **Context management** — loading progressive disclosure layers so only relevant context is consumed
- **Safety enforcement** — preventing destructive operations without explicit user confirmation

### Layer 3: Instructions

The instruction layer is where project-specific knowledge lives. Files like `CLAUDE.md`, `AGENTS.md`, and `GEMINI.md` encode the rules of engagement: coding conventions, architectural decisions, trigger words for skills, and safety restrictions.

This is what makes the difference between a generic chatbot and a team member who understands your codebase. Instructions are loaded progressively — only the relevant sections are injected into context based on the current task.

### Layer 4: Capabilities

Capabilities are the tools the agent can actually use. They fall into three categories:

- **Skills** — Reusable, document-driven workflows like brainstorming, test-driven development, and systematic debugging. Skills are loaded on demand and follow a maturity model from L1 (raw) to L5 (MCP-integrated).

- **MCP Tools** — Model Context Protocol integrations that connect the agent to external systems: browser automation for visual testing, file system access for code manipulation, GitHub API for pull request management.

- **Superpowers** — Meta-skills and patterns that govern how the agent approaches work: planning before coding, verifying before claiming completion, and requesting code review at key milestones.

### Layer 5: Persistent Memory

The feedback loop is what separates a session-aware agent from a stateless chatbot. With PostgreSQL and pgvector, every decision, action, and learning is stored and retrievable across sessions. When you start a new conversation, the agent can recall what it learned yesterday, last week, or last month.

This enables patterns like:
- **Decision continuity** — "We chose PostgreSQL over SQLite because..." remembered across sessions
- **Action tracking** — What files were changed, what was deployed, what failed
- **Context recovery** — Resuming work without re-explaining the entire project

### Layer 6: Outputs

The final layer is what the agent produces: code changes, documentation, diagrams, blog posts, reports, and infrastructure configurations. Every output flows back through memory, creating a virtuous cycle where past work informs future decisions.

## Why This Architecture Matters

The agent harness pattern is significant because it's **composable**. You can swap out the LLM (Claude today, GPT tomorrow) without changing your skills, instructions, or memory. You can add new MCP tools without touching the orchestration layer. You can evolve skills independently of the agent that uses them.

This separation of concerns means the system improves over time — not because the LLM gets smarter, but because the harness, instructions, skills, and memory all get better with each session.