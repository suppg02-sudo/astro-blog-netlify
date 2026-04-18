---
pubDatetime: 2026-04-18T19:00:00Z
title: "Taking the Karpathy Loop to Client Environments: The Customer Domain"
postSlug: "taking-the-karpathy-loop-to-cl"
description: "Taking the Karpathy Loop to Client Environments: The Customer Domain"
tags:
  - msp
---

**Part 6 of the [Karpathy Loop for MSPs series](http://ubuntu4:3002/posts/the-karpathy-loop-reference-guide/)**

You've been running Karpathy Loops on your own operations for six months. Ticket triage is sharper. Alert noise is down. Scripts actually work. Your internal dashboards show a measurable improvement curve — not vibes, not feelings, but numbers moving in the right direction.

Now what?

The obvious next step is to extend the same pattern to client environments. The same loop — one editable file, one metric, one fixed time budget — that cleaned up your own operations can clean up theirs.

But here's the thing nobody tells you: **running loops on clients is a fundamentally different problem from running loops on yourself.** Not harder, exactly. Different. The loop mechanics are identical. What changes is everything around the loop — data access, context, trust, and the fact that you don't own the environment.

This post is about that difference. Specifically, it's about the one problem that gates everything else: **getting at the data and building enough context to make the loop work.**

---

## Why Client Loops Are Different

When you run a Karpathy Loop on your own operations, you have three things you take for granted:

1. **Full data access.** Your PSA, RMM, ticketing system, billing platform — it's all yours. You can query anything, any time, without asking permission.
2. **Rich context.** You know why things are the way they are. You remember the decision to use ConnectWise over Autotask. You know that alert threshold was set to 90% because of that one server that always spikes at 3am. The tribal knowledge is *your* tribe.
3. **Permission to fail.** If you tune an alert threshold badly, your own team feels the noise. Nobody sues you. Nobody renegotiates the SLA.

When you run a loop on a client environment, you have none of these. You have partial data access (at best), thin context (usually), and zero tolerance for uncontrolled failure.

The loop itself — edit, measure, learn, repeat — doesn't change. The Karpathy Triplet still applies: one editable file, one metric, one time budget. What changes is the scaffolding you have to build around the loop before it can run at all.

---

## The Data Access Problem: The Gating Factor

Before you can run a single experiment on a client environment, you need data. That sounds obvious. The non-obvious part is how many different ways "need data" can fail:

**You can't experiment without a baseline.** The first question any loop asks is: "What's the current state?" If you can't measure the starting position, you can't measure improvement. You need historical data — ticket volumes, alert counts, response times, categorisation accuracy — before the loop even starts.

**You can't validate without production data.** You can tune a rule in a lab all day. But the test of whether it works is whether it works on real traffic. That means access to real (or realistically anonymised) client data.

**You can't iterate without feedback.** The loop's power is in the rapid cycle. If every data request takes two weeks and a change request form, the loop dies. The time budget collapses from "one hour per cycle" to "one month per cycle," and at that point you're not running a loop — you're running a project.

This is why data access is the gating factor. Not because it's technically hard (it usually isn't), but because it's organisationally hard. It requires contracts, trust, and processes that don't exist yet.

### The Permission Ladder

You don't get full access on day one. Nobody should give you full access on day one. Instead, think of it as a ladder:

1. **Read-only access.** You can see the data but not change anything. This is enough to run baseline analysis and identify opportunities. Most clients will agree to this quickly if you frame it as an "environment assessment."

2. **Historical data analysis.** You get a data dump — last 6-12 months of tickets, alerts, changes. You analyse patterns off-line, in your own time, without touching the client environment. This is where the first real insights come from.

3. **Sandboxed experiments.** You propose a change, it goes into a test environment or a non-production queue, and you measure the effect without client impact. This is where the loop starts to actually run.

4. **Production changes with approval gates.** Changes go live, but a human reviews and approves each one. The loop runs, but slowly — the time budget has to account for the approval delay.

5. **Automated deployment within boundaries.** Changes go live automatically within pre-agreed parameters, with rollback safety nets. The loop runs at full speed, but only in a defined corridor.

6. **Fully autonomous within agreed boundaries.** The loop runs continuously, making and measuring changes without human intervention for each cycle. The client trusts the process because they've seen it work at every previous level.

Most MSP-client relationships will operate at levels 3-4 for a long time. Level 5 is achievable for specific, well-understood domains. Level 6 is rare and should be — it requires deep trust built over many successful cycles.

### Data Sovereignty

Some clients will have hard constraints on where data can go. Regulated clients may require data stays within their tenant, their region, or their on-premises infrastructure. The loop must be able to run where the data lives.

This is a technical constraint, not a political one. If the data can't leave the client's Azure tenancy, the analysis engine needs to run inside the tenancy. If the data can't leave the country, the compute needs to be in-region.

Plan for this early. The architecture that works for a small business on M365 (delegated admin, everything in the cloud) will not work for a financial services firm with on-prem Active Directory and a data residency requirement.

---

## The Context Gap

Data access gets you raw material. Context is what turns that raw material into something useful.

When you started running loops on your own operations, you already had context. You knew that the spike in disk alerts every Tuesday was because of the backup window. You knew that the "printer not working" tickets always came from the second floor. You knew, because you'd lived it.

With a client environment, you don't know what you don't know. The alert threshold might be set to 85% because of a specific hardware limitation nobody documented. The ticket routing rule might exclude a whole class of issues because of an incident three years ago that everyone's forgotten.

**The first month with a new client is not for optimising. It's for mapping.**

You're building what I call the **per-client context layer** — a knowledge base that captures:

- Every ticket and its resolution (what happened, what fixed it, what should have happened)
- Every alert and its disposition (real incident vs false positive vs expected behaviour)
- Every change record (what changed, why, what broke, what improved)
- Every SOP and runbook (formal processes, but also the informal ones people actually follow)
- Every incident post-mortem (the honest ones, not the ones written for the audit)

This context layer is what makes the loop effective. Without it, you're optimising blind. With it, you're making informed changes that compound over time.

The good news: the loop itself generates context. Every experiment produces data. Every measurement produces a baseline. Every cycle adds to the knowledge base. The context layer grows organically as a byproduct of running the loop — which is another reason to start small and start early.

---

## Four Client Profiles, Four Starting Points

Not every client should start the same loop. The Karpathy Triplet — one editable file, one metric, one time budget — applies everywhere, but *which* file, *which* metric, and *how much* budget depends entirely on the client type.

Here are four profiles with specific, ready-to-run starting loops.

### Profile 1: Small Business on M365 (10-50 Users, Fully Cloud)

**The client.** Small professional services firm — accountants, solicitors, a design agency. Everyone uses M365. The MSP has delegated admin access to the tenant. There's no on-premises anything. The client has no IT documentation. The MSP *is* the IT documentation.

**Starting loop: Outlook/Mail flow rule optimisation.**

Reduce spam false positives. Auto-categorise support emails so the client's "support@company.com" address routes correctly instead of dumping everything into one inbox.

| Triplet Component | Details |
|---|---|
| **Edit surface** | Exchange transport rules (JSON export/import via PowerShell) |
| **Metric** | Percentage of support emails correctly routed without manual intervention |
| **Time budget** | 30 minutes per cycle, one cycle per week |

**Data access: Easy.** The MSP already has delegated admin access to the M365 tenant. Message trace logs, transport rule hit counts, and quarantine data are all available via PowerShell and the Exchange admin centre.

**Context: Thin.** The client has no IT documentation. You're building it from scratch. Start by collecting: how many emails hit the support address per week, how many are spam vs legitimate, how many legitimate ones get misrouted. That's your baseline.

**Why start here:** Full access, low-impact failure mode, immediate visible value. When the client sees their inbox get cleaner — fewer false positives, automatic categorisation of support requests — they understand what the loop does without needing to understand *how* it does it. This is the "quick win" that builds trust for harder problems later.

---

### Profile 2: Mid-Market with On-Prem Infrastructure (50-500 Users, Hybrid)

**The client.** A manufacturing company, a regional professional services firm, a mid-size charity. Hybrid environment — some M365, some on-prem Active Directory, file servers, maybe a legacy line-of-business application. The MSP has RMM agents deployed across the estate. The client has some documentation, some tribal knowledge, and some runbooks that were accurate three years ago.

**Starting loop: Monitoring alert tuning (per client).**

This is the same alert noise problem you solved internally — now applied to each client individually. Every client has different thresholds, different baseline behaviour, and different alert fatigue patterns.

| Triplet Component | Details |
|---|---|
| **Edit surface** | RMM alert threshold configurations, exported per client |
| **Metric** | False positive rate per client, while maintaining or improving catch rate |
| **Time budget** | 1 hour per cycle, one cycle per week per client |

**Data access: Moderate.** The MSP has RMM agent access, which covers most of the infrastructure. But some clients may require approval for firewall log access, domain controller event logs, or application-specific monitoring data. Expect to negotiate for the deeper data sources.

**Context: Medium.** There's documentation, but it's incomplete and partially outdated. The tribal knowledge lives in the heads of three people, one of whom is retiring. Your first two cycles should be: (1) baseline the current alert volume and false positive rate, and (2) interview the key people to capture the undocumented context before it walks out the door.

**Why start here:** This directly improves the service the MSP is already paid to deliver. Alert noise isn't an abstract problem — it's a daily frustration for the client's IT team (if they have one) and a direct cost for the MSP (every false positive alert is engineer time wasted). Reducing noise while maintaining or improving catch rate is a measurable, undeniable improvement.

---

### Profile 3: Enterprise with Hybrid Stack (500+ Users, Multi-Vendor)

**The client.** A large professional services firm, a university, a government agency. Multi-vendor environment — Microsoft, ServiceNow, maybe some AWS, three different monitoring tools, ITSM platform, knowledge base, and a wiki that nobody updates. Multiple internal teams with different escalation paths.

**Starting loop: Incident categorisation and routing.**

With multiple teams and multiple escalation paths, the biggest time sink isn't resolving incidents — it's getting them to the right team in the first place. Every misrouted incident adds 15-30 minutes of dead time while the wrong team reads it, realises it's not theirs, and re-assigns it.

| Triplet Component | Details |
|---|---|
| **Edit surface** | ITSM classification rules and escalation policies (structured rule format, version-controlled) |
| **Metric** | Mean time to correct team assignment (from ticket creation to arrival at the team that actually resolves it) |
| **Time budget** | 2 hours per cycle, one cycle per week |

**Data access: Hard.** This is enterprise land. You'll need data sharing agreements. Possibly DPA amendments. Definitely security review. The ITSM data is sensitive — it contains incident details, internal team structures, and sometimes employee information. Budget 4-6 weeks for the legal and compliance process before you see a single ticket.

**Context: Deep but fragmented.** There's a wiki. There's a knowledge base. There are runbooks. There's tribal knowledge spread across five teams on three floors. None of these sources agree with each other. Your first month is mapping: which team owns what, what the escalation paths actually are (vs what the documentation says they are), and where the routing breaks down.

**Why start here:** The problem is expensive at scale. If an enterprise with 2,000 employees generates 500 incidents per month, and 20% of them get misrouted, that's 100 incidents × 20 minutes average dead time = 33 hours of wasted effort per month. Even a modest improvement in routing accuracy saves thousands of hours per year. The ROI is undeniable.

---

### Profile 4: Regulated Client (Healthcare, Finance, Legal)

**The client.** A healthcare provider, a financial services firm, a law firm. Subject to regulatory requirements — HIPAA, FCA, SRA, or equivalent. Compliance isn't optional; it's existential. Documentation is mandatory and usually well-maintained (because the regulator demands it).

**Starting loop: Compliance check automation.**

Currently, someone (probably a human) checks that configurations match policy on a periodic basis — quarterly, maybe monthly. The gap between checks is a compliance risk window. The loop replaces periodic manual checks with continuous automated verification.

| Triplet Component | Details |
|---|---|
| **Edit surface** | Compliance rule definitions in structured format (JSON/YAML policies that can be automatically evaluated against live configurations) |
| **Metric** | Percentage of configurations passing automated compliance check vs manual audit findings |
| **Time budget** | 2 hours per cycle, one cycle per week |

**Data access: Very hard.** Requires regulatory understanding — you need to know what HIPAA, the FCA handbook, or the SRA code of conduct actually requires, not just what the client says it requires. You'll need a Business Associate Agreement (BAA) for healthcare data. Some clients may require all processing happens on-premises, with no data leaving their environment.

**Context: Deep and required.** The compliance documentation exists, it's mandatory, and it's usually well-maintained. This is one area where the context gap is smaller — the client has already documented what "correct" looks like, because the regulator demanded it. Your job is translating "correct" from human-readable policy into machine-checkable rules.

**Why start here:** Compliance is the one domain where "the machine checks it every night" is actually *more* trustworthy than "the human checks it quarterly." Regulators like continuous monitoring. Clients like reducing the manual audit burden. And the MSP can demonstrate value with clear, auditable evidence — every check, every result, every deviation, logged and timestamped.

---

## The Trust Gradient

You cannot skip steps. Trust is earned in order, and each level builds on the last.

**Step 1: Show them YOUR data.**

Before you touch anything in the client's environment, show them what you've done to your own. Pull up your internal dashboards. Show the improvement curve from the last six months of running Karpathy Loops on your own operations. The ticket triage accuracy going from 72% to 94%. The alert false positive rate dropping by 60%. The script success rate climbing.

This is not a sales pitch. It's evidence. You're saying: "Here's what this process looks like when we run it on an environment we control. We're not asking you to trust the theory. We're asking you to trust the evidence."

**Step 2: Run analysis on THEIR data, show insights, no changes.**

Get read-only access. Look at the data. Produce a report: "Here's what we found. Here are the patterns. Here are the likely opportunities." No changes. No actions. Just analysis and insight.

This demonstrates two things: (a) you understand their environment enough to find real patterns, and (b) you have the discipline to look without touching.

**Step 3: Propose changes in a sandbox, show predicted impact.**

Build a sandboxed version of the proposed change. Run historical data through it. Show the client: "If we'd had this rule in place last month, here's what would have happened. Here's what it would have caught. Here's what it would have missed."

This is the moment the loop becomes tangible. The client can see the before and after without risking the after.

**Step 4: Deploy with human approval gate.**

The change goes into production, but a human reviews and approves each cycle's output. The loop runs slowly — the time budget includes the approval delay. But the client sees real results in their real environment.

**Step 5: Automated deployment with rollback safety net.**

Changes deploy automatically within pre-agreed parameters. If something goes wrong, the rollback fires automatically. The loop runs at full speed, but within a defined safety corridor.

**Step 6: Fully autonomous within agreed boundaries.**

Eventually — and only after months of successful operation at previous levels — the loop runs continuously without human intervention for each cycle. The boundaries are clearly defined. The rollback mechanisms are proven. The client trusts the process because they've watched it work, step by step.

Most MSP-client relationships will stabilise at levels 3-4. That's fine. Levels 5-6 require a depth of trust and operational maturity that takes years to build. The point is not to reach level 6 with every client. The point is to have a clear path from "we just met" to "we trust you with our production environment," and to earn each step with evidence.

---

## What You're Actually Selling

The MSP that spends six months running Karpathy Loops on its own operations, then offers to run loops on client environments, is not selling AI.

It is selling **evidence-based continuous improvement.**

The proof is in the MSP's own dashboards. The client can see exactly what happened: the baseline, the experiments, the measurements, the improvement curve. They can see the process, not just the outcome.

That is a fundamentally different offering from "we added AI to our service desk."

"We added AI" is a feature. "We run a continuous improvement loop, here's what it looks like when we run it on ourselves, and here's what it could look like when we run it on you" is a methodology. Features get commoditised. Methodologies build moats.

The Karpathy Loop is not magic. It's discipline applied consistently. The discipline is: one file, one metric, one time budget. The consistency is: every week, without fail, for as long as it takes.

The hardest part is not the loop. The hardest part is everything around the loop — the data access, the context building, the trust gradient, the patience to start with analysis before jumping to automation.

But that's also where the value is. Because every MSP can install an AI plugin. Very few can demonstrate, with their own data, what structured continuous improvement actually looks like when it runs for six months straight.

---

## The Series So Far

- [Part 1: The Karpathy Loop for MSPs — Where It All Starts](http://ubuntu4:3002/posts/the-karpathy-loop-for-msps-whe/)
- [Part 2: When Your Sister Company Already Pays the Bills](http://ubuntu4:3002/posts/when-your-sister-company-alrea/)
- [Part 3: SOPs Are the Program — Why Structured Documentation Unlocks Automation](http://ubuntu4:3002/posts/sops-are-the-program-md-why-st/)
- [Part 4: The Microsoft MSP Dilemma — Building on Someone Else's Road](http://ubuntu4:3002/posts/the-microsoft-msp-dilemma-buil/)
- [Part 5: From Riding Microsoft to Owning the Stack](http://ubuntu4:3002/posts/from-riding-microsoft-to-ownin/)
- [Reference: The Karpathy Loop Reference Guide](http://ubuntu4:3002/posts/the-karpathy-loop-reference-guide/)

- [Beyond IT: Extending the Loop to Every Business Function](http://ubuntu4:3002/posts/beyond-it-extending-the-karpat/)
- [Taking the Loop to Client Environments](http://ubuntu4:3002/posts/taking-the-karpathy-loop-to-cl/)
- [The LLM-Wiki Pattern for MSP Knowledge Management](http://ubuntu4:3002/posts/the-llm-wiki-pattern-write-tim/)

---

**Tags**: Karpathy Loop, MSP Operations, Continuous Improvement, Data Access, Client Management, Evidence-Based Improvement, AI Operations, Monitoring, Compliance, Enterprise IT

**Categories**: MSP Strategy, AI Operations, Karpathy Loop Series