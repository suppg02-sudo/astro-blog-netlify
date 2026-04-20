---
pubDatetime: 2026-04-10T20:30:00Z
title: "When Your Evolution Engine Evolved Wrong"
postSlug: "when-your-evolution-engine-evo"
description: "When Your Evolution Engine Evolved Wrong"
tags:
  - 1
---

We built a self-improving system that was supposed to make our prompts and menus smarter over time. Instead, it spent weeks auditing database schemas that nobody asked it to check. Here's how we found the drift, diagnosed it, and built the bridges back.

## The Trap

The Evolution Engine was designed around a simple loop: capture artefacts from user interactions, analyse their quality, use an LLM to improve the weak ones, and monitor domain health. Eight domains were planned: prompts, menus, skills, triggers, decisions, attention, intent, and roadmap.

What actually happened: we got excited about schema alignment — ensuring every factory in our Seed-Factory-Instance hierarchy had complete DNA (identity, factory rules, audit criteria, agent interface). We built tools, wrote specs, got 9 out of 9 factories aligned. It felt productive.

The numbers told a different story:

| Domain | Artefacts | Avg Quality |
|--------|-----------|-------------|
| schemas (unplanned) | 61 | 0.76 |
| prompts (original goal) | 2 | 7.00 |

The original #1 priority had 2 artefacts. The unplanned addition dominated with 61. The prompts were high quality because we'd captured exactly two of them — not because the system was working.

## The Diagnosis

We ran a full audit using the same GLM-5.1 model that powers the agent. The findings were brutal:

**7 bugs found:**
1. `adapter_schemas.py` crashed with a KeyError on every improve cycle
2. 4 of 9 adapters were never imported — dead code from day one
3. The LLM improve phase used OpenRouter (no API key configured) — it silently returned None for everything
4. Menu adapter's `improve()` was literally `return None`
5. Only 2 prompts captured despite 38 in the prompt library
6. Cron was never registered — nothing ran automatically
7. The `evolved` CLI from the plan was never built

**The core problem**: the Evolution Engine was a data lake, not a data loop. It captured artefacts into PostgreSQL but never fed improvements back to source systems. The self-improvement cycle stopped at "improved artefact stored in DB."

## The Fix

Seven fixes, executed in priority order.

**Quick Win 1: Import the missing adapters.** One line added to `run_phase.py`. Suddenly triggers, decisions, attention, and intent domains came alive — capturing 25 trigger artefacts immediately.

**Quick Win 2: Fix the schemas crash.** The `improve()` method accessed `artefact["source_id"]` directly, but artefacts from the database are `RealDictRow` objects where `source_id` lives inside a `metadata` JSONB column. Fixed with defensive `.get()` chains.

**Quick Win 3: Feed the prompt adapter.** The adapter read from the `captured_prompts` PostgreSQL table which had 38 entries, but the capture function had only been run once. Running it again captured 36 prompts in seconds, scoring them 1-10 based on constraints, examples, and specificity.

**Quick Win 4: Wire the LLM.** Replaced the dead OpenRouter config with the same GLM-5.1 model and Zhipu API that the agent uses. The improve phase went from silent failure to actually rewriting prompts.

**Quick Win 5: Make menu improve real.** Replaced `return None` with a method that analyses selection rates, diagnoses low engagement, and generates structured proposals with specific recommendations.

**Quick Win 6: Build the CLI.** The plan had full source code ready. Created `cli.py` with stats, list, approve, bridges, and dashboard commands. Symlinked to `/usr/local/bin/evolved`. One command now shows the full health picture.

**Quick Win 7: Register cron.** Daily cycles at 7:00 UTC (analyse), 7:30 (improve), 8:00 (monitor), plus weekly deep cycles on Sundays.

## The Bridges

Fixing bugs wasn't enough — the domains needed to talk to each other. We built three cross-domain feedback loops:

**Bridge 1: Schema health triggers prompt rewrites.** When a factory's DNA score drops below 3/5, the bridge generates a prompt artefact specifically asking the LLM to author the missing DNA elements. The prompt enters the normal capture-analyse-improve pipeline and gets refined automatically. First run: 4 prompt artefacts created.

**Bridge 2: Menu signals flag skills for review.** When a skill's menu options have consistently low selection rates (below 20%), the bridge creates a skill review artefact with specific metrics and recommendations. The skill domain picks it up in the next cycle.

**Bridge 3: Intent gaps suggest new prompts.** When users express intents that have no matching prompts (detected via keyword analysis), the bridge suggests prompt templates to fill the gap. Ready for when intent data flows.

## The Result

After the full reconnection:

| Domain | Before | After | Change |
|--------|--------|-------|--------|
| Prompts | 2 artefacts | 46 artefacts | +2300% |
| Menu proposals | 0 | 20 | from NOP to live |
| Adapters running | 5/9 | 9/9 | all active |
| LLM improve | silent fail | GLM-5.1 active | working |
| Cron | not registered | daily + weekly | automated |
| Cross-domain bridges | none | 3 active | feedback loops |

The dashboard tells the story now:

```
  prompts       artefacts=  46  quality= 7.0/10 ███████  active= 36
  menus         artefacts= 209  quality= 2.9/10 ██  active=  5
  skills        artefacts=  75  quality= 1.8/10 █  active=  0
  schemas       artefacts=  99  quality= 0.9/10   active=  0
  triggers      artefacts=  28  quality= 5.5/10 █████  active= 28
```

## Lessons

1. **Beware productive distraction.** Schema alignment felt important because it was measurable (9/9 factories). But the original goal was prompt and menu improvement. Measuring the wrong metric feels like progress.

2. **Verify your loops actually loop.** Every adapter captured data. None fed improvements back. A data lake with no outlet is just expensive storage. The bridges were the real fix — not the bug patches.

3. **Test your LLM integration with actual calls.** The improve phase silently returned None for weeks because the API key was missing. No error, no warning, just... nothing. A single test call would have caught it.

4. **Build the CLI first, not last.** The `evolved dashboard` command showed us the full picture in 10 seconds. Without it, we were debugging blind. Visibility should be phase 1, not phase 3.

5. **Cross-domain bridges are the architecture.** Individual adapters are table stakes. The bridges — schema→prompt, menu→skill, intent→prompt — are what make the system actually self-improving. Each bridge turns observation into action across domain boundaries.

The Evolution Engine now runs daily, improves prompts with GLM-5.1, generates menu restructuring proposals, and cross-pollinates insights across domains. It took finding the drift to build the system we actually needed.

**Tags**: evolution-engine, self-improvement, ai-agents, postgresql, automation