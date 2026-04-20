---
pubDatetime: 2026-04-04T00:18:04Z
title: "Andrej Karpathy on Code Agents, AutoResearch and the Self Improvement Loopy Era of AI"
postSlug: "andrej-karpathy-on-code-agents"
description: "Andrej Karpathy on Code Agents, AutoResearch and the Self Improvement Loopy Era of AI"
tags:
  - others
---

Andrej Karpathy is pioneering autonomous loop AI systems—especially coding agents and self-improving research agents—while advancing AI-native education through Eureka Labs and ultra-minimal open-source LLM implementations.

## Coding Agents and the Loopy Era

Coding agents can now reliably edit code, run experiments, and iterate for days.

He created [AutoResearch](https://github.com/karpathy/autoresearch), AI agents that fully close the research loop—design experiments, edit training code, collect data, optimize hyperparameters/architectures, and improve a small LLM autonomously, with no human in the loop.

The loopy era is where agents running continuous self-improvement loops on code and research, which he believes will become standard at frontier labs.

## AutoResearch: 700 Experiments in 2 Days

Autoresearch (github.com/karpathy/autoresearch) using one markdown prompt and ~630 lines of training code on a single GPU) ran 700 experiments in 2 days. It discovered 20 optimizations that improved training. Agents edit train.py, try ideas (including novel architecture tweaks like reordering QK Norm and RoPE), learn from failures, and keep going. He calls this the seed for emulating a research community of agents collaborating asynchronously.

## MicroGPT: Demystifying the Algorithm

He made MicroGPT (Feb 2026 release) a GPT trained from scratch in 243 lines of pure Python + basic math—no PyTorch. Successor to nanoGPT and llm.c. It is meant to demystify the algorithm so both humans and future agents can understand and extend it.

## The Agent Command Center

He's actively running tmux grids of agents. Building watcher scripts to keep them looping, and prototyping an agent command center IDE (because the old single-file IDE is dead. The new unit is teams of agents)

## Broader Vision and New Terms

In 2025, he created and popularized the term **Vibe coding**. Anyone can describe what they want and get working software.

In 2026, he says we are **Agentic engineering**. Humans no longer write most code. We direct, supervise, and orchestrate agents. Technical expertise is still a multiplier, but the bits humans contribute are sparse and rare. Karpathy feels behind and that his manual coding skills are atrophying because agents (Claude Code, OpenAI Codex, etc.) crossed a coherence threshold around Dec 2025.

Programming workflow has fundamentally changed. You are not typing computer code. You are now spinning up AI agents.

There are macro actions that you can take over your code base.

It is the persons skill issue to get the productivity out of the agents.

There is a personality that matter to the agent tools (Claude Code vs OpenClaw).

He use a Claw to automate his home. It scanned all his wireless network and it found his Sonos and lights. He was able to use to control all of this systems and his security. It was 6 apps and now it is merged into one app and dashboard.

## Cursor and the LLM App Layer

LLM apps like Cursor bundle and orchestrate LLM calls for specific verticals:

1. They do the "context engineering"
2. They orchestrate multiple LLM calls under the hood strung into increasingly more complex DAGs, carefully balancing performance and cost tradeoffs.
3. They provide an application-specific GUI for the human in the loop
4. They offer an "autonomy slider"

A lot of chatter has been spent in 2025 on how "thick" this new app layer is. Will the LLM labs capture all applications or are there green pastures for LLM apps? Personally I suspect that LLM labs will trend to graduate the generally capable college student, but LLM apps will organize, finetune and actually animate teams of them into deployed professionals in specific verticals by supplying private data, sensors and actuators and feedback loops.

---

*Source: [NextBigFuture](https://www.nextbigfuture.com/2026/03/andrej-karpathy-on-code-agents-autoresearch-and-the-self-improvement-loopy-era-of-ai.html) by Brian Wang, March 20, 2026*

**Tags**: ai-agents, karpathy, auto-research, vibe-coding, agentic-engineering, self-improvement
**Categories**: AI, Technology