---
pubDatetime: 2026-04-10T14:37:48Z
title: "I Am Switching to Hermes Agent"
postSlug: "i-am-switching-to-hermes-agent"
description: "I Am Switching to Hermes Agent"
tags:
  - others
---

The moment you realize your AI assistant forgot everything you taught it last week.

That's the trap. You spend three hours crafting the perfect context, uploading documents, explaining your codebase, your preferences, your workflow. You close the session. You come back the next day. "Hey, what were we working on again?" — and you are back to zero.

Most agent frameworks treat every session as a blank slate. Ask a question. Get an answer. Move on. If you ask the same question next week, it starts from scratch, re-deriving everything it already knew. This is not a minor inconvenience. It is a fundamental architectural failure that makes these tools useless for anything that compounds over time.

Hermes Agent does not work that way.

## The Framework

Hermes Agent is an open-source, self-improving AI agent framework built by Nous Research. Version 0.6.0, production-ready, MIT licensed, 19,000 GitHub stars, 200+ contributors. The numbers tell you it has real adoption. But the numbers do not tell you what makes it actually different.

It does three things simultaneously. First: it is a full-featured agent that can use over 40 different tools — web search, terminal, file system, browser automation, code execution, image generation, text-to-speech, and vision. Second: it is a messaging gateway. You can talk to it from your terminal, Telegram, Discord, Slack, WhatsApp, Signal, even email, all from a single process. Third: it has a built-in learning system that is the actual differentiator. It does not just run tasks. It learns from them.

Built on Python — 92.5% of the codebase. Which matters more than it sounds like. Most AI infrastructure lives inside Python. Any LLM API, any transformer, any training framework slots in cleanly. You can debug it. You can extend it. You are not locked into someone else's abstractions.

Installation is one bash command. Handles Python, Node.js, everything.

## The Architecture That Actually Compounds

Here is what changes when your agent has memory that persists.

You have a folder. Every conversation lives inside it. Every task, every question. When you ask something six months from now, Hermes can search its own past using full-text search, find what it already knows about the problem, and pick up from there. It does not just retrieve — it synthesizes. "Haven't we solved something like this before?" Yes. And it can find it.

Then comes the skill system. This is week four thinking applied to your workflow.

You ask it to analyze your monthly revenue — pull data from Stripe, HubSpot, send you a weekly summary with three insights every Tuesday. The first time, it runs twenty steps. Multiple API calls. It does the research. And then it packages that logic as a reusable function. It tests it. It stores it. The next time you ask for something similar, it does not start over. It runs the skill, refines it, and it gets faster.

Then comes the pattern layer. Over weeks and months, Hermes tracks patterns specific to you — your preferences, your working style, what actually matters to you. When you ask something vague, it does not guess. It reaches into your context and fills the gap. It notices patterns across your conversations and can suggest things like: "You probably want a skill that does X instead of Y." You approve or reject. And the system learns.

This is fundamentally different from ChatGPT or Claude or OpenAI's agents. They reset every session. Hermes is designed to get better. It gets smarter the longer it works with you.

## Six Places to Run It

Architecture choices matter as much as capability.

Most agent frameworks run on your laptop or in a notebook. Fine for development. Terrible for production — your laptop sleeps, the agent stops. Hermes runs in six different places.

Local terminal for development. Docker for containerization. SSH on a VPS for production — this is how I run it, because I want it running jobs while I am away without leaving my machine on. Singularity if you have HPC cluster access. Daytona for persistent cloud development environments. Modal for serverless — and this is the interesting one. When your agent is idle and waiting for a message, you pay nothing. Modal hibernates everything automatically. It wakes when a message comes in. You run 24/7 for about five dollars a month.

Different projects need different infrastructure. A personal assistant on your laptop — local. A production system that needs to always be on — SSH. A research project that needs GPU — HPC cluster. A startup trying to keep costs down — serverless. Hermes does not lock you into any of these. You pick the back end that makes sense.

## What This Means in Practice

The difference between a stateless agent and a learning agent is the difference between a tool and a colleague.

A tool you pick up and put down. It does not remember what you built with it yesterday. A colleague you work with over time. They know your preferences, your patterns, your shorthand. They get faster at the things you do repeatedly.

I have been helping companies implement AI for two years, driving over five million dollars in bottom-line revenue across clients. The frameworks that stagnate are the ones that reset. The frameworks that compound are the ones that remember. Hermes Agent is the first open-source framework I have seen that takes the compounding seriously — not as a feature, but as the core architectural assumption.

If you are building anything with AI agents, the question is not just what it can do today. The question is whether it will be more valuable in six months or less. Most agents will not be. Hermes Agent is designed to be.

## What This Means for My Stack

Here is the honest analysis. I run a self-hosted AI infrastructure with around 50 services: Directus, pgvector-memory, MeTube, Crawl4AI, Kestra, n8n, chat-api, Telegram bot, Shlink, Formbricks, multiple Astro blogs, FreshRSS, and a dozen other things. Hermes Agent does not drop into a vacuum.

**Where it overlaps:**

The most obvious overlap is with `chat-api` (port 8057) — my FastAPI chat backend with session memory, tool execution, and MCP integration. Hermes and chat-api both handle messaging to Telegram and both can run LLM-powered agents. The difference is architectural. chat-api is stateless between sessions: each conversation starts fresh, tools are manually defined, and there is no skill system. Hermes would give me persistent memory across sessions, auto-generated skills from repeated patterns, and a learnable context window that compounds over months.

The Telegram bot and Hermes messaging gateway are partially redundant. My current bot (running on chat-api) handles menu triggers and tool execution well. Hermes would take over the persistent memory layer — the bot would become a better listener that remembers what we discussed three months ago. They are complementary, not competing.

`n8n` and `Kestra` overlap with Hermes's automation layer — recurring tasks, API integrations, scheduled jobs. But n8n and Kestra are visual workflow engines. Hermes learns from automation. The first time you ask it to generate a weekly status report, it might take twenty steps. The fifth time, it runs a skill in seconds. That learning loop is not what n8n or Kestra are built for.

**Where it fills gaps:**

My current infrastructure has no agent that improves from interaction. chat-api has sessions, but no cross-session memory. Hermes would be the first service that gets genuinely smarter the longer it runs. Combined with pgvector-memory (which I use for eRAG semantic search), Hermes could query my research knowledge base, synthesize from past conversations, and build skills specific to how I work.

`Crawl4AI` and MeTube handle content acquisition well. Hermes could be the orchestration layer on top — given a research topic, it decides what to crawl, what to search, what to store in eRAG, and what to surface in the blog pipeline.

**Deployment for this environment:**

SSH VPS or Docker on this server is the right move. Modal makes less sense here — I already have 24/7 infrastructure. Docker compose alongside existing services keeps it isolated and restarts cleanly with the rest of the stack. The memory folder on a persistent volume means it survives reboots and keeps compounding.

**Where it would not fit:**

Directus, Astro blogs, Shlink, Formbricks, FreshRSS, LimeSurvey — these are data and presentation layers. Hermes does not replace them. It sits above them as the reasoning, automation, and learning layer.

The honest verdict: Hermes Agent fills the one gap my current stack has — an agent that gets better at working with me over time rather than resetting. It complements Kestra for orchestration, fills the automation gap between chat-api sessions, and could sit above Crawl4AI and MeTube as the decision-making layer. The overlap with chat-api's Telegram integration is the one thing to resolve carefully, likely by keeping chat-api for structured tool execution and routing conversational memory to Hermes.

---

*Video: [I am Switching to Hermes Agent](https://youtu.be/J-kSdzHr9Ek) by Nick Puru | AI Automation*

**Tags**: Hermes Agent, Nous Research, AI Agents, Open Source, LLM Infrastructure, AI Engineering

**Categories**: AI Engineering, Tutorials