---
pubDatetime: 2026-04-18T17:00:00Z
title: "The Karpathy Loop for MSPs: Where Auto-Improvement Lands in Managed Services"
postSlug: "the-karpathy-loop-for-msps-whe"
description: "The Karpathy Loop for MSPs: Where Auto-Improvement Lands in Managed Services"
tags:
  - msp
series: karpathy-msp
seriesEntry: true
---

You run an MSP. You manage other companies' IT — their servers, their networks, their projects, their helpdesks. You have ticket queues, alert floods, patching schedules, client onboarding checklists, and project timelines that are always wrong.

Karpathy showed that an AI agent can run 700 experiments overnight and find 20 genuine improvements in code that one of the best ML researchers alive had already optimized. The pattern is simple: propose an edit, run an experiment, measure a metric, keep it or revert it.

The question is: where does that pattern actually land in an MSP? What do you optimize first? What does the triplet look like when your "codebase" is a PSA, an RMM, a pile of PowerShell scripts, and 40 client environments?

This is the practical application guide.

## The Short Answer

You start with ticket triage. Not because it is the sexiest problem — because it is the one where you already have the data, the metric is objective, failure is invisible to clients, and improvement pays immediately in technician time saved.

## Why MSPs Are Perfectly Positioned

Most organizations struggle with the Karpathy Loop prerequisites because they do not have structured data, clear metrics, or sandboxed environments. MSPs have all three by default:

| Prerequisite | What Most Orgs Lack | What MSPs Already Have |
|-------------|---------------------|----------------------|
| Structured data | Ad hoc knowledge in Slack, emails, heads | PSA ticket history with categories, priorities, time logs |
| Objective metrics | Guessing at quality, measuring activity | SLA compliance, first-response time, resolution time, satisfaction scores |
| Sandboxed environments | Production is the only environment | Test tenants in RMM, staging networks, lab environments |
| Eval harnesses | No testing infrastructure | Every ticket resolution is a test case — did the fix work? |
| Version control | Change logs in spreadsheets | RMM config snapshots, script repos, change management records |

The MSP that recognises it is already sitting on the infrastructure for auto-improvement has a 6-month head start on every org still figuring out what "context layer" means.

## The Three Starting Points

You need the Karpathy Triplet: one editable surface, one metric, one time budget. Here are the three that make sense for an MSP in month one.

### 1. Ticket Triage (Start Here)

**Why first**: Your PSA has months or years of ticket data with known correct categorisations. Every ticket that was re-categorised by a technician is a labelled training example. You have thousands of them.

| Component | Detail |
|-----------|--------|
| Edit surface | A classification rules file (JSON/YAML mapping symptoms to categories and priorities) |
| Metric | % of tickets correctly categorised on first pass without human correction |
| Time budget | 5 minutes per batch of 50 historical tickets |

**How the loop runs**:

1. Meta-agent reads the last 90 days of tickets that were re-categorised by technicians
2. It proposes a new rule: "If subject contains 'VPN' AND body contains 'cannot connect', route to Network team, Priority 2"
3. The rule runs against a held-back test set of 500 tickets with known correct categories
4. If accuracy goes up, the rule is committed. If it goes down or creates misroutes, it is reverted
5. Repeat 100 times overnight

**What you get in week one**: A classification engine that catches 70-80% of common ticket patterns correctly, freeing Level 1 technicians from manual triage. The remaining 20-30% (edge cases, ambiguous descriptions) still route to humans.

**Why this is safe**: The agent only touches the classification rules file. It cannot modify the PSA itself, cannot close tickets, cannot contact clients. If a rule is bad, a human sees the misroute and fixes it — exactly what happens today, except now 80% fewer misroutes happen.

### 2. Alert Triage and Noise Reduction

**The pain**: Your RMM generates thousands of alerts per day. Most are noise. Your NOC team spends hours dismissing false positives. Real alerts get lost in the flood. Clients complain about slow response to actual incidents.

| Component | Detail |
|-----------|--------|
| Edit surface | Alert threshold configuration (YAML/JSON with per-device-type, per-client thresholds) |
| Metric | False positive rate must drop while catch rate stays above 98% |
| Time budget | Evaluate against 24 hours of historical alerts with known outcomes |

**How the loop runs**:

1. Meta-agent reads the last 30 days of alerts tagged "false positive" or "dismissed" by NOC
2. It proposes threshold adjustments: "Raise CPU alert threshold for Server-ABC from 80% to 92% — this device consistently spikes to 85% during backup windows with no actual issues"
3. The adjusted config runs against historical alert data with known real incidents
4. If false positives drop and no real incidents are missed, commit. Otherwise revert
5. Run continuously — thresholds adapt as client environments change

**What you get**: Alert fatigue drops 40-60% within two weeks. NOC team focuses on real incidents. SLA response times improve because real alerts are not buried in noise.

**The safety mechanism**: Every threshold change is logged. If a real alert is suppressed, it shows up in the daily review. The agent cannot suppress alerts entirely — it can only adjust numeric thresholds within human-approved bounds.

### 3. Script Library Optimisation

**The pain**: You have hundreds of PowerShell and Bash scripts for routine tasks — new user provisioning, server health checks, backup verification, permission audits. Some are years old. Some have edge case bugs. Some are slow. Nobody has time to review and improve them.

| Component | Detail |
|-----------|--------|
| Edit surface | One script at a time (the agent can only modify the target script) |
| Metric | Script passes existing test suite AND runs faster / handles more edge cases |
| Time budget | 30 seconds per script execution, max 50 variations per script overnight |

**How the loop runs**:

1. Agent reads the script, its test suite, and the last 20 execution logs (successes and failures)
2. It proposes a modification — adding error handling for a known failure case, or optimising a slow loop
3. Modified script runs against the test suite
4. If all tests pass and runtime improves (or new edge cases are handled), commit. Otherwise revert
5. Move to the next script

**What you get**: A self-maintaining script library. Scripts that have been untouched for years get modern error handling, better logging, and faster execution — without a technician spending a single hour on it.

**Why this is the safest starting point**: Scripts run in your lab, not on client machines. Test suites catch breakage. If a script modification fails tests, nobody notices — it just gets reverted silently.

## MSP Auto-Improvement Roadmap

Where each loop lands and when to start it:

| Domain | Loop Target | When to Start | Risk Level |
|--------|-----------|---------------|-----------|
| Ticket triage | Classification rules file | **Month 1** | Low — sandboxed in PSA |
| Alert tuning | Threshold configs | **Month 1** | Low — revertable configs |
| Script library | PowerShell/Bash scripts | **Month 1** | Low — lab environment |
| Patch deployment sequencing | Rollout order rules | **Q3** | Medium — staging first |
| Config drift detection | Golden config comparison | **Q3** | Medium — read-only initially |
| Client onboarding | Checklist automation | **Q4** | Medium — internal first |
| Project scoping | Estimation model tuning | **Q4** | Medium — requires historical data |
| Client stack recommendations | Vendor fit evaluation | **2027** | High — client-facing advice |

## The Readiness Checklist

Before you start any loop, you need these in place:

| Item | What It Looks Like at an MSP | How to Get It |
|------|----------------------------|---------------|
| **Structured ticket history** | PSA export with category, priority, re-categorisation flags | Export from ConnectWise/AutoTask/HaloITSM |
| **Labelled test set** | 500+ tickets where you know the correct category | Use re-categorised tickets as ground truth |
| **Sandbox environment** | Test PSA instance or staging RMM tenant | Your existing lab/dev environment |
| **Version control on configs** | Git repo for classification rules and threshold configs | `git init` in your scripts/rules directory |
| **Baseline measurement** | Current triage accuracy, current false positive rate | Measure for one week before starting |
| **Ownership** | Named person who reviews experiment logs daily | Assign to NOC lead or service delivery manager |
| **Revert protocol** | How to roll back a bad rule in under 5 minutes | Keep previous config version tagged in git |

## What Not to Touch (Yet)

| Domain | Why Not Now | When |
|--------|------------|------|
| Client-facing chatbots | Failure is visible to clients | After 3 months of internal loops proving stable |
| Compliance workflows | Regulatory risk from automated changes | After governance framework is built |
| Billing / invoicing | Direct revenue impact | After auto-improve is trusted from 6+ months of results |
| Security policy enforcement | One wrong change = breach | Only with explicit client approval and full audit trail |

## The 90-Day Roadmap

| Week | Action | Outcome |
|------|--------|---------|
| 1-2 | Export ticket history, build test set, measure baseline | You know your current triage accuracy |
| 3-4 | Deploy ticket triage loop in sandbox, run overnight experiments | 70-80% auto-triage on common patterns |
| 5-6 | Deploy alert tuning loop, measure baseline false positive rate | Alert noise starts dropping |
| 7-8 | Begin script library optimisation, write test suites for top 20 scripts | Scripts getting faster and more reliable |
| 9-10 | Promote ticket triage to production with human review layer | Technicians spend less time on triage |
| 11-12 | Review results, document improvements, plan Q3 expansion | First quarterly report showing time saved |

## The Economics

| Metric | Before Auto-Improve | After 90 Days | Annual Savings (50-tech MSP) |
|--------|-------------------|---------------|-------------------------------|
| Ticket triage accuracy | 60% (many re-categorised) | 80%+ | ~2,000 technician-hours/year |
| Alert false positive rate | 40-60% | 15-25% | ~1,500 NOC-hours/year |
| Script failure rate | 5-10% on edge cases | 1-2% | ~500 hours of rework/year |
| **Total** | | | **~4,000 hours = $160K-$200K/year** |

At a fully loaded technician cost of $40-50/hour, the first three loops pay for themselves within the first quarter. The compute cost for running the loops is negligible — under $100/month for an MSP of any size.

## The Competitive Moat

Here is what most MSPs will do: they will read about AI agents, buy a co-pilot licence, let technicians use ChatGPT for ticket responses, and call it "AI-powered service." That is not auto-improvement. That is augmentation — a human still does the work, just slightly faster.

The MSP that builds auto-improvement loops is doing something fundamentally different. Its ticket triage gets better every night. Its alert thresholds adapt to changing environments. Its script library maintains itself. Each loop compounds. Each client benefits from improvements made across all clients.

After 12 months, the gap between an MSP running auto-improve loops and one using ChatGPT for tickets is not marginal. It is structural. One gets slightly faster humans. The other has a system that optimises itself while everyone sleeps.

## What This Requires From Leadership

Not more AI tools. Not bigger budgets. Three things:

1. **Define "better" clearly enough to hand to a machine.** This is the hardest part. "Improve service quality" is not a metric. "Reduce ticket misroutes from 40% to below 15%" is.

2. **Protect experimentation time.** The first month requires someone to build test sets, measure baselines, and review experiment logs. That is 5-10 hours/week from your best technician. Guard that time.

3. **Accept that most experiments fail.** Karpathy's agent ran 700 experiments. 20 worked. That is a 3% hit rate. The value is in the iteration speed, not the success rate. If your culture punishes failed experiments, you will never get auto-improvement off the ground.

The question is not whether auto-improvement is coming to managed services. It is whether your MSP can define what better means clearly enough to let a machine pursue it overnight.

---

*Based on the Karpathy Loop pattern from [The Karpathy Loop Reference](http://ubuntu4:3002/posts/the-karpathy-loop-reference-guide/). Source video: [Nate B Jones — Karpathy's Agent Ran 700 Experiments While He Slept](https://www.youtube.com/watch?v=xnG8h3UnNFI).*
- [Beyond IT: Extending the Loop to Every Business Function](http://ubuntu4:3002/posts/beyond-it-extending-the-karpat/)
- [Taking the Loop to Client Environments](http://ubuntu4:3002/posts/taking-the-karpathy-loop-to-cl/)
- [The LLM-Wiki Pattern for MSP Knowledge Management](http://ubuntu4:3002/posts/the-llm-wiki-pattern-write-tim/)

**Tags**: msp, managed-services, auto-improvement, karpathy-loop, ai-agents, ticket-triage, rmm, psa, it-automation
**Categories**: AI Automation, Business Strategy