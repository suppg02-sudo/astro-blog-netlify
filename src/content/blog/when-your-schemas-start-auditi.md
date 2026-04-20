---
pubDatetime: 2026-04-10T18:00:00Z
title: "When Your Schemas Start Auditing Themselves"
postSlug: "when-your-schemas-start-auditi"
description: "When Your Schemas Start Auditing Themselves"
tags:
  - others
---

I watched it happen in real time. A cron job fires at 8:30 AM, scans every active instance in the hierarchy, runs verification against its parent factory's audit criteria, and logs the result — pass or fail — into the instance's own improvement log. Then a bubbler script aggregates those logs across all instances, groups them by finding, and proposes a version bump for the factory. Meanwhile, a prompt builder reads the factory's agent interface definition and generates a formatted system context block that any AI agent can use to understand what it's supposed to do.

No human in the loop. No manual checks. The schemas are reading themselves, evaluating themselves, and writing improvement proposals. We didn't set out to build a self-improving system. We set out to align some aspirational design documents with a live database. But that's where the DNA metaphor took us.

## The Problem: Schemas Without Nerve Endings

Here's what happens. You design a beautiful schema hierarchy — seed at the top, factories in the middle, instances at the bottom. Each factory defines generation rules, audit criteria, and an agent interface. Each instance is supposed to follow those rules and pass those criteria. But in practice, the schemas just sat there. Static JSON blobs in PostgreSQL. Pretty architecture, zero feedback.

We had `pghfactory` CLI commands to inspect them, verify them, even log improvements. But someone had to *run* those commands. Someone had to *read* the output. Someone had to *decide* what to do about it. That someone was supposed to be me, and I had better things to do than manually audit schema instances.

The schemas had no nerve endings. No pain signals. No way to say "hey, this instance hasn't been verified in three weeks" or "this factory's audit criteria are failing on 40% of instances." They were beautiful architecture with no operational reality.

## The DNA Metaphor That Started It

The aspirational design documents used a DNA analogy: **Seed → Factory → Instance**. The seed contains the genome — the shared `$defs` like `schemaIdentity`, `auditSpec`, `lifecycle`, `agentInterface`. Factories inherit from the seed and add domain-specific DNA: generation rules, audit criteria, available actions. Instances inherit from factories and carry the full genetic code forward.

Phase 1 was the alignment: merging those aspirational definitions into the live PostgreSQL schemas. The research factory got 8 generation rules, 7 audit criteria, and a structured instance schema with sub-questions, evidence chains, tensions, and synthesis states. The publishing factory got its own 8 rules, 7 criteria, and a hard review gate before publication.

But alignment without automation is just documentation. The schemas were aligned, but they weren't *alive*.

## The Three Scripts That Changed Everything

Phase 2 was three scripts. That's it. Three scripts that turned static schemas into a living system.

### Script 1: auto_audit.py

The first script was supposed to be simple: find active instances, run `pghfactory verify`, log the result. The first version had a bug so obvious it's embarrassing — it only logged improvements on success. When an instance failed verification, the script just printed `[Failed]` and moved on. No log entry. No record. The failure vanished into the void.

The fix was straightforward: log failures with the error detail. But then we hit a more subtle bug. The `verify` command outputs audit criteria text, which includes severity labels like `[ERROR]` and `[WARNING]`. The audit script was scanning stdout for "ERROR" and treating it as a command failure — even though the command exited successfully. So every instance was being logged as a failure because the criteria text happened to contain the word "ERROR" in a severity label.

The real fix: only treat `returncode != 0` or stderr errors as actual failures. The stdout content is criteria text, not error output. This distinction matters because conflating them means your audit system cries wolf on every single check.

```
[FAIL] Logged failure for test-instance: --- Audit Criteria for test-instance ---
[ERROR] Question clarity: Verify that the primary question is specific...
```

That's not a failure. That's the criteria text. The script was auditing the audit output and failing on its own severity labels.

### Script 2: factory_bubbler.py

The second script aggregates improvement log entries from all child instances of a factory, groups them by finding, counts frequency, and proposes a version bump. It's the upward feedback loop — instances talking to their parent factory.

The tricky part was key name resolution. The aspirational schemas used `schemaIdentity` (camelCase). The live database used `identity` (no prefix). The bubbler needed to check both: `data.get('schemaIdentity', data.get('schema_identity', data.get('identity', {})))`. Same for `auditSpec` vs `audit`, `factorySpec` vs `factory`.

This is the reality of schema evolution. The documents said one thing, the database said another, and the code had to speak both dialects fluently. Every lookup became a fallback chain: aspirational key, snake_case key, actual key. Three tries per field, because consistency is a luxury in systems that evolve.

### Script 3: agent_prompt_builder.py

The third script reads a factory's `agentInterface` — entry questions, available actions, context requirements, generation rules, audit criteria — and formats it as a system context block that an AI agent can use as pre-conditioning.

This is where the schema hierarchy becomes *useful*. Not just organized, not just auditable, but *actionable*. An agent loading the research factory's prompt sees:

- 3 entry questions (what are you researching, how deep, what exists already)
- 7 available actions (create_project, add_source, extract_evidence, record_tension, synthesise, audit, resume)
- 8 generation rules with rationale (start with a question, decompose into sub-questions, assess credibility, link evidence, maintain tensions, state confidence, document gaps, check the graph)
- 7 audit criteria with severity levels (question clarity: ERROR, sub-question coverage: WARNING, tension register: INFO)

That's 25 data points extracted from a single factory schema and formatted into a prompt that any LLM can consume. No manual prompt engineering. No copy-pasting from docs. The schema *is* the prompt.

## The Full Cycle

Here's what the pipeline looks like now:

```
auto_audit.py (daily 8:30 UTC)
    → Finds active instances
    → Runs pghfactory verify against parent factory criteria
    → Logs pass/fail to instance improvement_log
    
factory_bubbler.py (on demand)
    → Aggregates improvement_log entries across instances
    → Groups by finding, counts frequency
    → Proposes version bump (e.g., 0.1.0 → 0.1.1)

agent_prompt_builder.py (on demand)
    → Extracts agentInterface from factory
    → Formats entry questions, actions, rules, criteria
    → Outputs system context block for AI agents
```

The data flows in both directions. Downward: factory DNA flows into instances as rules and criteria. Upward: instance experience flows back to factories as improvement proposals and version bumps. The schemas are reading their own output and writing their own evolution.

## Why This Matters

The interesting thing isn't the three scripts. It's what they represent: a system where the *data structure* is also the *operational contract*. The schema doesn't just describe what an instance should look like — it contains the rules for verifying it, the actions available to agents working on it, and the questions those agents should ask before starting.

Most schema systems are passive. They validate shape and move on. This one is active. It defines behavior, audits compliance, logs deviations, and generates prompts. The schema isn't a blueprint — it's a runtime.

We're now at 5 of 9 factories aligned: research, publishing, menu, skill, and project. Each has full aspirational DNA — identity, factory rules, audit criteria, agent interface, lifecycle phases. The remaining 4 (infrastructure, brainstorm, agents, erag) will get the same treatment when their domains mature enough to warrant it.

The cron job runs at 8:30 AM daily. The schemas audit themselves while I'm still on my first coffee. And every morning, there's a fresh improvement log waiting in the database, written by the system, for the system, about the system.

That's the loop. And it's running right now.

**Tags**: schemas, postgresql, ai-agents, self-improving-systems, evolution
**Categories**: AI Automation, Architecture