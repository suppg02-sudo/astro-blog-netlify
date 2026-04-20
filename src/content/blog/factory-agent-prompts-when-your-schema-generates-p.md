---
pubDatetime: 2026-04-10T20:00:00Z
title: "Factory Agent Prompts: When Your Schema Generates Prompts Nobody Reads"
postSlug: "factory-agent-prompts-when-your-schema-generates-p"
description: "This is the story of how we discovered that our most sophisticated schema feature was producing beautiful, well-organized output that nothing in the system ever loaded. And why that's more dangerous t"
tags:
  - technical-debt
  - schemas
  - dna-hierarchy
  - evolution-engine
  - agent-prompts
---

We built a generative schema hierarchy. Seed, Factory, Instance — like DNA for infrastructure. Each factory carries an `agentInterface` block that tells agents what questions to ask, what actions are available, and what rules to follow. We wrote a builder that renders these blocks into markdown prompts. Nine factories, nine prompts, sitting in a directory. All perfectly structured. All completely disconnected from the agents that should be reading them.

This is the story of how we discovered that our most sophisticated schema feature was producing beautiful, well-organized output that nothing in the system ever loaded. And why that's more dangerous than not having it at all.

## The Stack: Where Prompts Come From

Our schema hierarchy lives in PostgreSQL. The `aimplifi_schemas` table holds the seed (the root genome) and nine factory schemas. Each factory carries five DNA components:

- **schemaIdentity** — what this factory is, its version, lineage
- **auditSpec** — what "good" looks like, with severity-tagged criteria
- **lifecycle** — state machine (draft → active → retired)
- **agentInterface** — entry questions, available actions, context requirements
- **factorySpec** — generation rules with rationale, output targets

The `agent_prompt_builder.py` script reads a factory's JSON from PostgreSQL and renders it into a structured markdown document. It pulls `entry_questions` from `agentInterface`, `generation_rules` from `factorySpec`, and `criteria` from `auditSpec`. The result is a clean, sectioned prompt file.

Nine factories generate nine prompts, stored in `evolve/data/agent_prompts/`. Each has:

- System context header with factory name and version
- Entry questions (3 per factory, each with a stated purpose)
- Available actions (6-8 per factory, each with input/output spec)
- Context requirements (what data the agent needs before acting)
- Generation rules (8 per factory, each with rationale)
- Audit criteria (7-10 per factory, with severity tags)

That's roughly 40-50 lines per prompt, or about 800 tokens per factory. Across all nine, that's 432 lines and approximately 7,200 tokens of carefully structured agent context.

## The Discovery: A Key Mismatch Revealed the Truth

The prompts came to light during a bug fix. We discovered that the adapter checking for `agentInterface` was actually checking for `agentInterfaces` (with an extra 's') — a typo that meant it was also looking at `agent_interface` (snake_case) but never at the canonical camelCase `agentInterface`.

Five factories had the data under `agent_interface`. Four had it under `agentInterface`. The adapter saw neither for the five, and only the correct key for the four. Result: five factories showed `has_interface=false` despite having all the data.

We fixed it with a three-key fallback chain: `agentInterface` → `agentInterfaces` → `agent_interface`. Then normalized the database so all nine factories have the canonical key. DNA score went from mixed to 9/9 at 5/5.

But fixing the key mismatch meant the adapter now correctly reported `has_interface=true` for all nine — and that raised an obvious question: if the interface data is there, what's actually using it?

Answer: nothing. The `agent_prompt_builder.py` reads the data and writes files. No agent config references those files. No skill loads them during invocation. No SKILL.md says "load agent_prompts/{factory}.md for context." The prompts are orphans.

## The Audit: What We Found

Going through all nine prompts systematically revealed a pattern:

**3 out of 9 factories have excellent quality** — menu-factory (v3.0.0), skill-factory (v2.0.0), and project-factory (v1.2.0) all have populated purpose fields, detailed actions, and thorough audit criteria.

**6 out of 9 say "Purpose: N/A"** — brainstorm, agents, research, erag, infrastructure, and publishing factories all have empty purpose fields. An agent loading one of these prompts sees a factory name and version but no explanation of what the factory is for. That's like a README that says "Module X v0.1.0" with no further text.

**All prompts lack freshness tracking** — there's no timestamp, no schema version reference, no content hash. If the schema changes in PostgreSQL, the generated file silently goes stale.

**The builder conflates two concerns** — generation rules (how to produce instances) and behavioral rules (how the agent should act) are different things, but the prompt bundles them together. For factory-tier this works because the factory IS the behavior specification. For instance-tier or domain-tier, it would break.

**Audit criteria include severity labels meant for scripts** — `[ERROR]`, `[WARNING]`, `[INFO]` tags are for `auto_audit.py`, not for an agent reading context. An agent doesn't need to know that a rule is an ERROR-level check. It needs to know what the rule is.

## The Real Problem: False Completeness

Here's the dangerous part. The schema hierarchy is fully aligned. All nine factories score 5/5 on DNA. The `agentInterface` data is present and well-structured. The prompts are generated and stored.

To anyone looking at the metrics, this system appears complete. The Evolution Engine dashboard shows 9/9 aligned factories. The DNA score is perfect. The audit passes.

But the prompts aren't connected to anything. It's like building a beautiful API and never giving anyone the endpoint URL. The data exists, the structure is sound, but the loop is open. Information flows from schema to file, then stops. No agent ever acts on it.

This is worse than not having the feature at all. If the prompts didn't exist, we'd know we had a gap. Instead, we have the illusion of completeness. The metrics say everything is wired. The reality says nothing is.

## The Fix Plan

Three immediate actions, ranked by impact:

**1. Backfill the 6 N/A purpose fields.** Every prompt says what the factory does. This is a data fix, not a code change. Five-minute job per factory.

**2. Wire one factory as proof-of-concept.** Menu-factory (v3.0.0, best purpose, most mature) gets injected into the menu-factory skill's loading flow. When the skill is invoked, it reads the agent prompt from the file and includes it in context. This proves the pipeline works before wiring all nine.

**3. Add freshness headers to the builder.** Every generated prompt gets `Generated: 2026-04-10T12:00:00Z` and `Schema version: 3.0.0` at the top. Stale detection becomes trivial.

Then there's the architectural question: pre-generate or on-demand? Currently, the builder writes static files. If schemas change, files go stale. The alternative is on-demand generation — load from DB when the prompt is needed, not ahead of time. On-demand is more correct but adds latency to every skill invocation.

For now, pre-generation with freshness headers is the pragmatic choice. On-demand becomes necessary at scale.

## The Broader Lesson

Schema-driven systems create a specific trap: the schema can be complete while the system is not. The structure encodes intent, but intent without execution is just documentation.

The `agentInterface` block is the most interesting DNA component because it's the one that bridges structure and behavior. It says not just "what this factory is" but "how an agent should interact with it." That's the control plane. And the control plane is only useful if something reads it.

Every schema hierarchy needs a wiring audit. Not "does the data exist?" but "does anything act on this data?" Our Evolution Engine captures artefacts from 9 domains and had 400+ artefacts, but before this session, zero artefacts had been approved and fed back to source systems. The same pattern: capture without closure.

The fix is always the same: close the loop. Data that doesn't flow is data that decays. Schemas that aren't read are schemas that drift from reality. And perfect metrics on an open loop are the most dangerous kind of technical debt — the invisible kind.