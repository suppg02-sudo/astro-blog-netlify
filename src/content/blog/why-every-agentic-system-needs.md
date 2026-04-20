---
pubDatetime: 2026-04-09T16:36:14Z
title: "Why Every Agentic System Needs a Model Router"
postSlug: "why-every-agentic-system-needs"
description: "Why Every Agentic System Needs a Model Router"
tags:
  - others
---

When building production AI applications, most teams hardcode a direct connection to a single model provider. Santiago Valdarrama (Underfitted) demonstrates why that approach is fragile and introduces a far better architecture: the model gateway.

## The Problem with Direct Model Connections

The typical setup is deceptively simple: your application talks directly to GPT, Claude, or an open-source model. This works for demos, but breaks down in production. What happens when your provider goes down? When you need different models for different complexity levels? When you want to track spending across five different models without managing five separate API keys?

## The Model Gateway Architecture

The solution is a router — an intermediate layer between your application and model providers. Instead of connecting directly to OpenAI or Anthropic, your application connects to a single gateway that handles:

- **Model routing** — Send requests to different models based on availability, cost, or complexity
- **Cost management** — Centralise billing instead of distributing credit cards across providers
- **Observability** — Log every request, view traces, monitor performance
- **Caching** — Avoid redundant inference calls
- **Security** — Single point of control for API key management
- **Failover** — Automatically route to backup providers when one goes down

## Open Router in Practice

Valdarrama uses [Open Router](https://openrouter.plug.dev/0RKxzak) as his gateway of choice. In a multi-agent tic-tac-toe game built with Google ADK, he routes five different agents through a single Open Router connection:

| Agent | Model | Role |
|-------|-------|------|
| Player 1 | GPT 5.2 | Strategic player |
| Player 2 | Cohere 3.5 (9B) | Opposing player |
| Tournament Agent | DeepSeek R1 | Game orchestration |
| Commentator | DeepSeek | Live play-by-play narration |
| Random/Minimax | Algorithm-based | Benchmark strategies |

## One Line to Swap Models

The key insight is abstraction. Using LiteLLM with Open Router, swapping models requires changing a single string:

```python
# Instead of connecting to each provider directly:
# openai.Client(api_key="...")

# Connect once to Open Router, specify model per agent:
model = "openrouter/gpt-5.2"
model = "openrouter/cohere-3.5-9b"
model = "openrouter/deepseek-r1"
```

Each agent specifies `openrouter/` followed by the model name. LiteLLM handles the rest — no separate API keys, no provider-specific SDKs, no code refactoring when you switch models.

## Open Router Features

Beyond routing, Open Router provides:

- **Centralised spending** — See total costs across all models in one dashboard
- **Request logs** — Every API call tracked with full details
- **Provider selection** — Choose specific inference endpoints or let Open Router auto-select the best one
- **Pricing transparency** — See per-token costs for each provider variant
- **Uptime monitoring** — Check availability before committing to a provider
- **Precision info** — Know the quantisation level of each endpoint

## The Multi-Agent Demo

The tic-tac-toe game demonstrates the architecture beautifully. Five agents collaborate in real-time, each powered by a different model, all routed through Open Router. A commentator agent narrates plays like a baseball announcer. A tournament agent orchestrates matches. Players using different strategies (random vs minimax) compete while different models handle the thinking.

The entire system runs on a single Open Router API key. No OpenAI key. No Cohere key. No DeepSeek key. Just one.

## Why This Matters for Agentic Systems

Agentic systems are inherently multi-model. Different tasks have different requirements:

- **Complex reasoning** needs frontier models (expensive, slow)
- **Simple formatting** can use smaller models (cheap, fast)
- **Fallback paths** need alternative providers when primaries fail

A model router makes this practical. You define routing logic once, and every agent in your system benefits from cost optimisation, observability, and resilience.

## Key Takeaways

1. **Never connect directly to a model provider in production** — Use a gateway
2. **Centralise your API management** — One key, one billing dashboard, one place to rotate credentials
3. **Design for model swapability** — Your code shouldn't care which model it's talking to
4. **Use LiteLLM + Open Router** — The simplest way to get started with model routing
5. **Match model complexity to task complexity** — Don't use a frontier model for formatting tasks

> The best time to add a model router was before you wrote your first API call. The second best time is now.

**Tags**: ai-agents, model-routing, open-router, litellm, multi-agent, google-adk, llm
**Categories**: AI Automation, Tutorials