---
pubDatetime: 2026-04-01T08:21:36Z
title: "When Should You Abstract? The Factory Pattern in Skill Systems"
postSlug: "when-should-you-abstract-the-f"
description: "When Should You Abstract? The Factory Pattern in Skill Systems"
tags:
  - others
---

> **TL;DR**: Three factory-type skills share the same structural DNA — hub-and-spoke, lifecycle phases, schema validation — but it's too early to extract a shared schema. The interesting question isn't *when* to abstract, but *what* the abstraction should look like when you do.

## Quick Summary

- **skill-factory**, **menu-factory**, and **project-factory** share a common architectural pattern
- The pattern includes: hub-and-spoke structure, lifecycle phases, template directories, input/output schemas, and progressive disclosure
- Abstraction becomes valuable at the 4th instance — three is the threshold where you can *see* the pattern, but extracting it now would be premature
- The factory pattern's relationship to agent harness design reveals a deeper layer: factories define *what exists*, harnesses define *how agents interact with it*

## The Three Factories

I've been building a skill system where "factories" are meta-skills that create other things — skills, menus, projects. Three have emerged organically:

| Factory | Creates | Schema Format | Maturity |
|---------|---------|---------------|----------|
| **skill-factory** | New skills | JSON Schema | L4 |
| **menu-factory** | Standardized menus | JSON templates | L3 |
| **project-factory** | Multi-phase projects | YAML schema | L2 |

Each one independently arrived at roughly the same architecture:

1. **Hub file** (SKILL.md) — concise entry point
2. **Context directory** — progressive disclosure, load on demand
3. **Templates directory** — starter shapes for the thing being created
4. **History directory** — append-only tracking
5. **Input/output schemas** — typed, validated interfaces
6. **Lifecycle phases** — with exit criteria and advancement

The `skill.yaml` metadata format is nearly identical between skill-factory and project-factory — same fields, same structure, just different `files` and `features` sections. Project-factory already *composes with* skill-factory (its `plan` phase calls skill-factory as a dependency).

## The Case Against Abstracting Now

Three is the magic number where you can *see* a pattern but shouldn't necessarily *extract* it. Here's why waiting for a fourth factory is the right call:

**Each factory has genuinely different I/O shapes.** Skill-factory validates with JSON Schema. Project-factory uses YAML. Menu-factory uses parameterized templates. Unifying those might constrain domain evolution — the moment you need a factory that produces something with a fundamentally different shape, a shared schema becomes friction rather than acceleration.

**The biggest risk is a schema that's too thin to be useful or too thick to be flexible.** A thin abstraction that only says "factories have names and versions" adds process without value. A thick one that tries to unify JSON Schema, YAML, and template formats becomes a straightjacket.

**Three instances prove the pattern exists but not that it's stable.** A fourth factory — something like a `pipeline-factory` or `dashboard-factory` — would test whether the pattern holds under a genuinely new domain or whether the first three were just similar by coincidence.

## The Factory-Harness Relationship

There's a more interesting question underneath: how should factories relate to **agent harnesses**?

An agent harness (as defined in the `agent-harness-construction` skill) concerns itself with four things:

1. **Action space quality** — well-scoped, schema-first tool definitions
2. **Observation quality** — consistent output shapes with status, summary, next actions
3. **Recovery quality** — error paths with root cause hints and retry instructions
4. **Context budget quality** — minimal prompts, on-demand loading

Factories and harnesses solve different layers of the same problem:

| | Factories | Agent Harnesses |
|---|---|---|
| **Question** | "What should exist?" | "How should an agent use it?" |
| **Output** | Schemas, templates, lifecycles | Action spaces, observation formats |
| **Layer** | Domain model | Execution model |
| **Analogy** | API specification | Client SDK |

The natural relationship is compositional: **a factory defines the schema, the agent harness defines how an agent interacts with that schema.**

Right now there's duplication. The `skill-output.json` schema from skill-factory defines what success/failure looks like — status, warnings, artifacts, next steps. The agent harness skill independently says "every tool response should include status, summary, next_actions, artifacts." These are the same idea stated twice in different vocabularies.

The factory schema — when it eventually exists — should be the **single source of truth that the harness references**. The harness becomes "how to interact with factory-shaped outputs" rather than an independent protocol.

## The Practical Design

When the fourth factory arrives and justifies extraction, the factory schema should be:

**A thin interface, not a framework.** Specifically:

1. **Common metadata shape** — the `skill.yaml` fields all factories share (name, version, triggers, dependencies, features)
2. **Common lifecycle protocol** — phases with exit criteria and advancement rules
3. **Common I/O contract** — every factory validates input and produces structured output
4. **Common directory conventions** — `context/`, `templates/`, `history/`

**Not a unified domain schema.** Keep skill-input.json, project schema.yaml, and menu templates separate. The factory schema defines the *interface*, not the *payload*.

**Integrated into skill-factory as a creation template.** When skill-factory creates a new factory-type skill, it uses the factory schema as a base. This is where the real value compounds: new factories get the pattern for free, and the pattern itself is validated every time a new factory is created.

**Explicit about what makes a skill a "factory."** Right now `category: meta` is the only signal. A factory schema would add explicit markers: `type: factory`, required lifecycle phases, required I/O schemas.

## Why This Matters

The practical win isn't consistency between three existing factories — they already work. The win is **acceleration for the next one** and **making the factory pattern explicit enough that a smaller model (7B-14B parameters) could create one correctly.**

That's the real test of any abstraction in a skill system: can it be executed by models that don't have the context to improvise? If the factory pattern requires a 200B-parameter model to interpret correctly, it's not a pattern — it's vibes. If a 7B model can follow a factory schema and produce a working factory, the abstraction has earned its complexity budget.

<details>
<summary>Deep Dive: The Shared Patterns in Detail</summary>

Here's the concrete overlap across all three factories:

**skill-factory (L4):**
- Hub: SKILL.md (314 lines) + 6 context files
- Schemas: skill-input.json, skill-output.json (JSON Schema)
- Lifecycle: L1→L5 maturity levels
- Templates: skill creation templates
- Menu: 10 options with intent capture

**menu-factory (L3):**
- Hub: SKILL.md (519 lines) + context/docs/rules/scripts
- Schemas: 4 template JSONs (service, workflow, analysis, base)
- Lifecycle: implicit (template → apply → validate)
- Templates: menu patterns
- Menu: menu creation workflow

**project-factory (L2):**
- Hub: SKILL.md (221 lines) + context/history/projects
- Schemas: context/schema.yaml (YAML)
- Lifecycle: idea→plan→active→harvest→rest
- Templates: project-template.yaml
- Menu: 8 options

All three share: `skill.yaml` metadata, progressive disclosure, history tracking, template directories, and structured menus.

</details>

<details>
<summary>References & Further Reading</summary>

- **Skill Factory**: The meta-skill that creates other skills — the most mature of the three factories at L4
- **Agent Harness Construction**: Defines action space design, observation formatting, and error recovery for AI agents
- **Progressive Disclosure**: The pattern of structuring information in layers (L0 minimal → L4 full reference) that all three factories implement
- **Hub and Spoke Architecture**: Each factory uses a concise hub file (SKILL.md) that references deeper context files loaded on demand
- **Schema-First Design**: All three factories validate their inputs with typed schemas before proceeding — this is the core determinism principle

The key insight from software engineering applies here: the Rule of Three says you can copy once, but extract the pattern after three instances. But the corollary is equally important — extract too early and you freeze a pattern that hasn't finished evolving.

</details>

**Tags**: ai-agents, skill-systems, design-patterns, abstraction, factory-pattern
**Categories**: AI Automation, Architecture