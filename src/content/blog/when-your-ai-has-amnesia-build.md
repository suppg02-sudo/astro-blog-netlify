---
pubDatetime: 2026-04-18T19:00:00Z
title: "When Your AI Has Amnesia: Building Self-Improving Memory Loops"
postSlug: "when-your-ai-has-amnesia-build"
description: "When Your AI Has Amnesia: Building Self-Improving Memory Loops"
tags:
  - others
---

We discovered something uncomfortable this week. Our AI infrastructure had a signal gap — it was collecting data from 196 trigger events, 380 menu presentations, and 149 user selections, but almost none of that intelligence was feeding back into actual improvement. The system was observing itself without learning. Like a patient hooked up to monitors but with no doctor reading the charts.

## The Diagnosis

The problem surfaced during a routine health check. Our auto-improvement system runs on a simple principle called the Triad: **Schema → Signal → Auto-Improvement**. You define what to track, you track it, and then you adjust based on what you learned. The first two steps were working. The third was broken in two critical places.

First, **subagent tracking was nearly non-existent**. We'd dispatched hundreds of subagents — brainstormers, code explorers, research agents — but only 4 dispatches had been logged. The protocol said "track every dispatch within 2 tool calls" but there was no enforcement mechanism. It was like having a policy that everyone writes timesheets but nobody checks.

Second, **memory quality was catastrophically skewed**. Out of 2,952 memories stored in PostgreSQL, only 17 were categorised as "experience", "lesson", or "pattern" — the types that actually help a system learn from its mistakes. That's 0.6%. The other 99.4% was raw conversation data. It's the difference between a diary and a journal — one records what happened, the other extracts what it means.

## The Fix: Making Compliance Effortless

The old system relied on the AI agent remembering to run tracking commands after every action. That's like hoping someone will floss every night — it works in theory and fails in practice. The fix was to reduce friction to near-zero.

For subagent tracking, we built `subagent_wrapper.py` — a single command that dual-writes to both a local JSON log file and the PostgreSQL database. If the database is down, the file log still captures the event. If the agent forgets the wrapper entirely, the `system-reminder.md` file (loaded every session) now contains a non-negotiable enforcement block that names the exact command to run.

For memory quality, we built `session_quality.py` — a checker that runs at session end and auto-generates the missing memory types from context. Instead of expecting the agent to write a thoughtful "lesson learned" after every session, the script takes a topic and summary and produces structured experience, lesson, and pattern memories automatically. The bar shifted from "write something insightful" to "provide a one-line summary" — a much easier ask.

## The Seven Loops That Make It Work

With the fixes in place, the complete auto-improvement system now has seven operational loops:

**Signal Collection (4 loops):**

1. **Subagent Tracking** — Every dispatched agent gets logged with outcome and context
2. **Memory Quality** — Every session produces at least one experience, one lesson, one pattern
3. **Menu Signals** — Every menu presentation and selection gets recorded for optimization
4. **Trigger Analytics** — Every shortcut command usage gets tracked for discoverability analysis

**Improvement Engine (1 engine, 8 domains):**

5. **Evolve Engine** — Runs daily via cron, analysing and improving agents, prompts, skills, menus, triggers, decisions, attention, and roadmap through LLM-driven improvements

**Auxiliary Scripts (2 systems):**

6. **Prompt Auto-Mine** — Daily scan of conversations for high-quality prompts worth capturing
7. **Skill Improver** — Daily analysis of skill quality, failures, and drift

The key insight: loops 1-4 collect the signals, loop 5 acts on them, and loops 6-7 provide specialised coverage. Each feeds the next.

## The Enforcement Chain

The difference between a system that works and a system that degrades is enforcement. We built three layers:

The first layer is `system-reminder.md`, loaded into every session automatically. It contains the non-negotiable rules in plain language: "After EVERY subagent dispatch, run this exact command." No ambiguity, no interpretation needed.

The second layer is `AGENTS.md`, the persistent context file that defines the protocols. It specifies the wrapper commands, the quality targets (>5% memory quality ratio), and the session wrap-up checklist.

The third layer is the `auto-improvement` skill itself — an operational document that explains the why behind the rules, provides diagnostic procedures for when things break, and includes the health check command that validates the entire system.

If any one layer gets corrupted or outdated, the other two still carry the enforcement signal. Redundancy by design.

## Why This Matters

Most AI agent systems treat memory as a nice-to-have. You chat, the agent responds, the conversation ends. Some systems store transcripts. Very few extract patterns. Almost none close the loop back into their own operating procedures.

The result is an AI that has the same blind spots in session 100 as it had in session 1. It doesn't learn that menu option C is never selected. It doesn't learn that agent X fails 30% of the time. It doesn't learn that the "research" trigger is used once and then abandoned.

Closing these loops turns a chat interface into a compounding intelligence. Every session's mistakes become the next session's guardrails. Every unused menu option becomes a redesign opportunity. Every failed subagent dispatch becomes a routing optimisation.

The system is now generating quality memories at 100% of the target rate for this session. The subagent wrapper is logging dispatches. The health check command validates everything in one pass. It's not perfect — compliance will slip, scripts will break, cron jobs will silently fail. But now there's a dashboard to catch the drift, and a diagnostic to fix it.

**Tags**: ai, self-improvement, memory-systems, auto-improvement, postgresql, agentic-engineering