---
pubDatetime: 2026-04-06T01:00:00Z
title: "Self-Improving Architecture #3: Progressive Disclosure as an Attention Budget"
postSlug: "self-improving-architecture-progressive-disclosure-attention-budget"
description: "Why progressive disclosure is not just an API pattern but an evolutionary mechanism. Machine-readable L0→L4 structures and how to compile schemas into templates."
tags:
  - self-improving-architecture
  - context-optimization
  - schema-templates
  - attention-budget
  - recursive-loading
  - progressive-disclosure
---

# Self-Improving Architecture #3: Progressive Disclosure as an Attention Budget

In Parts 1 and 2, I covered the six-layer architecture, the data flow, and the feedback loop. This installment gets into the most overlooked layer: progressive disclosure — and why it's the engine of recursion, not just a content loading strategy.

## Progressive Disclosure is Not Just an API Pattern

Most documentation systems treat progressive disclosure as a convenience. "Don't overwhelm the user. Show the important stuff first, hide the rest." That's true but incomplete.

In a self-improving architecture, progressive disclosure serves three functions simultaneously:

1. **Attention budget** — agents have limited context windows. Loading only what's needed preserves that budget for the actual work
2. **Evolutionary pressure** — if L0 is wrong, nobody reaches L4. Bad schemas get punished by abandonment before they waste resources
3. **Recursive mechanism** — the disclosure rules are themselves disclosed progressively. You learn the rules for loading L2 only when you reach L1

This third point is the key. **Progressive disclosure is recursion in practice.**

The system that loads content uses loading rules. Those loading rules are content. They are loaded using the same loading rules. This is not a circular dependency — it's a bootstrapping sequence.

## The Five Levels, Machine-Readable

Currently, progressive disclosure is a human convention. Skills put their identity in the header (L0), their intent in context/intent.md (L1), their commands in SKILL.md (L2), troubleshooting in references (L3), and everything in L4. An agent learns this through training.

What it should look like: **the schema declares the disclosure structure.**

```yaml
# Example: skill-schema.yaml
disclosure_levels:
  L0:
    name: "identity"
    fields: [name, version, maturity, description]
    loaded_by: "default — always"
    purpose: "Answer: what is this?"

  L1:
    name: "intent"
    source: "context/intent.md"
    loaded_when: "user asks about purpose or scope"
    purpose: "Answer: what does it do?"

  L2:
    name: "usage"
    fields: [triggers, menu, services, cron]
    source: "SKILL.md"
    loaded_when: "user asks how to execute"
    purpose: "Answer: how do I use it?"

  L3:
    name: "reference"
    source: "context/references/"
    loaded_when: "user encounters an error or edge case"
    purpose: "Answer: what goes wrong?"

  L4:
    name: "complete"
    source: "entire skill directory"
    loaded_when: "user explicitly requests full context"
    purpose: "Answer: everything"

  load_rules:
    - "Agent requests L0 automatically for every skill"
    - "Agent loads L1 when user asks what a skill does"
    - "Agent loads L2 when user invokes a trigger or menu"
    - "Agent loads L3 when error context matches skill domain"
    - "Agent loads L4 only on explicit user request"
    - "Total loaded content must not exceed 4000 tokens for L0-L2"
```

This turns progressive disclosure from a human convention into a **machine-contract**. The agent asks the schema "what should I load?" and gets a structured answer instead of guessing based on file paths and conventions.

## The Context Budget Problem

Here's the problem this solves: the current system loads files based on file inventory in skill.yaml. The inventory lists SKILL.md, intent.md, environment.md, and references. But it doesn't say which to load when. So an agent loading a complex skill might pull everything at once — consuming 15,000+ tokens for a skill the user only mentioned in passing.

Progressive disclosure with machine-readable rules means the agent loads 200 tokens (L0) for a passing mention, 1,000 tokens (L0+L1) for a purpose inquiry, and 5,000 tokens (L0-L2) for actual execution. That's a 75% context window saving on non-critical interactions.

In a system with 60+ skills, that saving compounds. Every interaction uses less of the context budget. More of the budget is available for the actual work — reasoning, implementing, debugging.

## The Recursive Loading Sequence

Here's what self-disclosure looks like in practice:

1. Agent encounters skill X for the first time
2. Agent loads L0 (identity): name, version, maturity — 50 tokens
3. L0 contains a pointer to L1: "Read intent.md for purpose"
4. Agent loads L1 (intent): purpose, scope, success criteria — 300 tokens
5. L1 contains the loading rules: "For menu operations, load L2"
6. Agent loads L2 (usage): triggers, commands, workflows — 2,000 tokens
7. L2 contains advanced loading rules: "For debugging, load L3"
8. L3 is loaded only if needed

**The rules for loading L3 are inside L2. The rules for loading L2 are inside L1. The rules for loading L1 are... well, L1 is the first one beyond the default, so the meta-rules are in L0.**

This is recursion with a base case: L0 is always loaded, and L0 contains the seed rules for everything else. No infinite loop. No bootstrap problem.

## Schema-to-Template Compilation

The missing link in the current architecture is the connection between schemas and templates. Here's how it should work:

### The Compilation Step

```
Schema (abstract definition)
    ↓
  Schema Scanner reads disclosure_levels
    ↓
  For each level, extract the corresponding content
    ↓
  Combine into template with level markers
    ↓
  Template (concrete manifestation with L0-L4 sections)
```

The schema scanner (Phase 2 implementation) reads a schema's disclosure_levels, finds the corresponding files and fields, and generates a template that has explicit level markers:

```yaml
# Generated template for project-schema
L0:
  fields: [id, title, status, priority]
  source: base-entity.yaml

L1:
  fields: [description.intent, description.scope]
  source: base-entity.yaml + mixin-schedulable.yaml (schedule section)

L2:
  fields: [phases, context, menu]
  source: project-schema.yaml (own fields)

L3:
  fields: [change_history]
  source: mixin-traceable.yaml

L4:
  fields: [all resolved fields]
  source: base-entity + all mixins + own fields
```

This is the **fossilization step** — the abstract schema becomes a concrete template that can be loaded, modified, and tracked independently of the schema itself.

### Why This Matters

When a schema evolves (field added, structure changed, validation rule modified), the template should be regenerated. But not instantly — only when the signal data shows that the old template is producing poor results (high rejection rates on template instantiation, or frequent backtracks during template use).

The schema defines what is valid. The template defines what is proven. When what is valid changes, what is proven eventually follows — but only after the new schema has proven itself through signal data.

This lag between schema change and template update is **by design**. It prevents the system from adopting unproven changes too quickly. Templates are the conservative force in the evolutionary equation — schemas introduce variation, templates select what persists.

## The Three Laws of Progressive Disclosure

Derived from how the system actually works in practice:

1. **L0 must be sufficient for identity** — if you can't tell what something is from L0 alone, it has an L0 problem
2. **Each level must describe the next level** — if L1 doesn't tell you about L2, the chain breaks
3. **No level may require a level above it** — L0 cannot depend on L4. Loading must be strictly unidirectional from low to high

These laws sound obvious. They're violated constantly in practice. Skills that put their name and version (L0) in three different places. Skills that assume you've read the references (L4) to understand the basic commands (L2). Skills that describe their loading strategy in a reference document (L3) — which you won't find unless you already know the loading strategy.

Self-improvement starts with fixing these violations. When the schema scanner detects them (L0 incomplete, missing level pointers, circular references), it flags them as issues. The agent can then fix them. Each fix improves the efficiency of every subsequent interaction with that skill.

## Measuring the Budget

A real progressive disclosure system tracks context usage:

| Metric | Target | Why |
|---|---|---|
| L0 tokens | < 100 | Identity should be instant |
| L0+L1 tokens | < 500 | Purpose should be cheap |
| L0-L2 tokens | < 3,000 | Execution should be reasonable |
| L0-L4 tokens | < 15,000 | Full reference should be reserved |
| Average load level | < L2 | Most interactions shouldn't need deep context |
| Context window utilization | < 60% | Never use the full window on loading alone |

The last metric is the constraint that makes progressive disclosure necessary. In a 200K context window system, spending 150K on loading leaves 50K for thinking. In an 8K context window system, spending 5K on loading leaves 3K for thinking. The ratios change but the tension remains: **every token spent on loading is a token not spent on reasoning**.

## Conclusion

Progressive disclosure is not a documentation convenience. It's an optimization strategy for limited compute. It's a quality control mechanism for content. And it's the practical expression of recursion in a self-improving system — because the rules for loading are loaded progressively, the system bootstraps its own understanding of itself.

The schema-to-template compilation step connects the abstract (what is valid) to the concrete (what is proven). The lag between them provides evolutionary stability. The budget metrics provide measurable evidence that the system is working.

In the next installment, I'll cover the schema evolution loop — how the system audits its own schemas, proposes improvements, and applies them autonomously.

---

*This is the third installment in the Self-Improving Architecture series. Part 1: The Architecture. Part 2: Data Flow and the Feedback Loop.*