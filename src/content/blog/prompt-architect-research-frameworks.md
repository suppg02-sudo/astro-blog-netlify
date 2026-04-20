---
pubDatetime: 2026-04-02T12:00:00Z
title: "Prompt Architect - A Research-Backed Framework Collection for Better Prompts"
postSlug: "prompt-architect-research-frameworks"
description: "Discover Prompt Architect, an AI skill that evaluates prompts across 27 quality dimensions and Find the perfect research-backed framework for your use case."
tags:
  - prompting
  - llm
  - claude
  - ai
  - tools
---

## What is Prompt Architect?

[Prompt Architect](https://github.com/ckelsoe/prompt-architect) is an AI skill designed to evaluate and improve prompts using 27 research-backed frameworks. It works with Claude Code, Gemini CLI, Cursor, Copilot, and other AI coding agents.

## Key Features

- **Intelligent Analysis** - Evaluates prompts across 5 quality dimensions (clarity, specificity, context, completeness, structure)
- **Framework Recommendation** - Suggests the best framework(s) for your specific use case
- **Guided Dialogue** - Asks targeted clarifying questions when needed
- **Iterative Refinement** - Continues improving based on feedback

## The 27+ Frameworks

The skill includes frameworks for different prompt types:

| Framework | Best For | Research Backing |
|-----------|---------|-----------------|
| **CO-STAR** | Content creation, writing tasks | Industry standard |
| **RISEN** | Multi-step processes, procedures | Best practices |
| **TIDD-EC** | High-precision tasks with explicit boundaries | Explicit guidance |
| **Tree of Thought** | Decisions requiring exploration | arXiv 2024 |
| **ReAct** | Agentic/tool-use tasks | Yao et al. |
| **Chain of Thought** | Reasoning, problem-solving | Step-by-step reasoning |
| **Skeleton of Thought** | Structured long-form content | ICLR 2024 |
| **Plan-and-Solve PS+** | Zero-shot numerical reasoning | ACL 2023 |
| **Reverse Role Prompting** | Requirements gathering | arXiv 2025 |

## How It Works

1. You provide a prompt for analysis
2. The skill evaluates it across 5 dimensions (1-10 scale)
3. It recommends the best framework(s)
4. If needed, it asks clarifying questions
5. It generates an improved, structured prompt
6. Explains the changes made

## Quick Start

After installing, simply ask:

```
Help me improve this prompt: write a technical blog post
```

The skill will automatically analyze, recommend, and transform your prompt.

## Installation

### Claude Code
```bash
/install-skill https://github.com/ckelsoe/prompt-architect/tree/main/skills/prompt-architect
```

### npm
```bash
npx @ckelsoe/prompt-architect
```

## Why This Matters

Poor prompts lead to:
- Vague outputs requiring multiple iterations
- Missing context causing irrelevant results
- Inconsistent quality across sessions
- Wasted tokens on clarifying exchanges

Prompt Architect solves this by providing structured, research-backed approaches to prompt engineering.

---

*Repository: [ckelsoe/prompt-architect](https://github.com/ckelsoe/prompt-architect)*