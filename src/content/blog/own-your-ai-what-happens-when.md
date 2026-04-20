---
pubDatetime: 2026-04-09T21:00:00Z
title: "Own Your AI: What Happens When Your Stack Already Lives This"
postSlug: "own-your-ai-what-happens-when"
description: "Own Your AI: What Happens When Your Stack Already Lives This"
tags:
  - others
---

A LinkedIn post by Mitko Vasilev went viral this week: "My morning routine: Espresso → GLM-5 → Agent Swarm." 231 reactions, 37 comments, one clear message — open source AI running locally isn't a compromise. It's a competitive advantage.

He's right. But the interesting thing isn't the claim. It's how much of this architecture already exists in production for those of us who've been building it.

## The Post

Mitko's setup:
- **GLM-5**: 744B total parameters, 40B active, 28.5T tokens pre-trained, MIT licensed
- **Local**: Runs on his desk, not a datacenter
- **Agentic**: Long-horizon engineering spanning days — research → architecture → implementation → testing → documenting
- **Next step**: Claude Code Agent Swarm for infrastructure tasks

The post resonated because it names something many engineers feel but can't articulate: cloud AI is aligned with the company that owns it, not with you.

## Cross-Referencing the Stack

What caught my attention wasn't the novelty — it was the mirror. Here's what that philosophy looks like when it's been running in production for months.

### Model Sovereignty

Mitko runs GLM-5 locally. This session is running on GLM-5.1 — the same family, same philosophy. No rate limits. No "your conversation is too long." No vendor deciding what you're allowed to build.

### Session Continuity

Mitko describes engineering that "spans days, not chat sessions." That's the Brainplane protocol: session context flows through a raw → wiki pipeline so the next session doesn't start from zero. Knowledge persists. Decisions accumulate. The agent gets smarter about your stack over time, not dumber when the context window fills up.

### Agent Orchestration

"Next up: Agent Swarm" — Mitko's planning it. Meanwhile, an agents-factory already produces validated agent configurations. Subagents dispatch in parallel for independent tasks. The orchestration layer exists: skill-factory, project-factory, menu-factory — each a meta-skill that produces other skills or projects on demand.

### Containment Architecture

Jerry Castille's comment on the post was the sharpest insight:

> "Local models remove vendor alignment risk. But they don't remove the need for enforcement architecture once agents start touching real systems. The next wave won't just be agent capability — it'll be structured containment."

This is exactly right, and it's already solved. The Superpowers Approval Protocol requires explicit approval before agents execute on debugging, TDD, worktree isolation, or any destructive operation. Agents can't just do things — they propose, the human approves, then they execute. Structured containment isn't a future problem. It's a solved one.

### The Signal Pipeline

The full agentic loop that Mitko describes — research → architecture → implementation → testing → course-correcting → documenting — maps directly to an existing pipeline:

- **Research** → research-factory with eRAG (PostgreSQL + pgvector)
- **Architecture** → writing-plans skill with verifiable goals
- **Implementation** → surgical changes, test-driven development
- **Testing** → verification-before-completion (evidence before assertions)
- **Documenting** → automatic brainplane capture at session end
- **Persisting** → wiki architecture + memory system (2,846+ memories indexed)

## What's Actually Novel

The viral post names the philosophy. The philosophy is sound. But naming a thing and living in it are different.

Living in it means:
- 58 Docker containers running services you control
- A blog pipeline that publishes via Directus API, not a cloud CMS
- A prompt library with signal tracking and adaptive improvement
- Trigger words that self-document and validate against a YAML registry
- A menu system that learns from usage patterns and optimises itself

None of this is theoretical. It's been running, producing, and evolving for months.

## The Market Signal

231 reactions on a post that says "own your AI" tells you something about where developer sentiment is heading. The audience for self-sovereign AI infrastructure is real and growing. The content strategy writes itself:

- Schema-driven agent configurations → product
- Trigger registries and menu factories → framework
- Brainplane knowledge persistence → differentiator
- Structured containment protocols → trust

The triad — **Schema + Signal + Self-Improvement** — isn't just an architecture. It's a product category waiting to be named.

## The Takeaway

Mitko's right that we've reached the inflection point. Open source isn't a compromise. Local models aren't a limitation. Agent swarms aren't a future plan.

The question isn't whether to own your AI. It's whether the architecture around your AI is structured enough to let agents do real work without real damage. That's the hard problem. And it's already solvable.

---

*Cross-referenced against the Evolution Project stack. 32 triggers registered. 81 skills active. One aim: AI infrastructure that pays for itself.*

**Tags**: own-your-ai, glm-5, agentic-engineering, local-llm, agent-swarm, self-sovereign, infrastructure