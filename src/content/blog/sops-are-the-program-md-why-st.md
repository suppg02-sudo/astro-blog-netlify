---
pubDatetime: 2026-04-18T18:00:00Z
title: "SOPs Are the Program.md: Why Standard Operating Instructions Are the Missing Link in MSP Auto-Improvement"
postSlug: "sops-are-the-program-md-why-st"
description: "SOPs Are the Program.md: Why Standard Operating Instructions Are the Missing Link in MSP Auto-Improvement"
tags:
  - msp
---

When Karpathy ran 700 experiments overnight, the agent was not free to do whatever it wanted. It operated within a plain English instruction file — the program.md — that defined what to explore, what constraints to respect, and what constituted improvement. The agent's intelligence was in execution. The human's intelligence was in the instructions.

Most MSPs already have a version of program.md sitting on a SharePoint drive somewhere. They call them Standard Operating Instructions. They are written in plain English. They define what to do, in what order, with what constraints, and what constitutes success.

The problem is not that MSPs lack program.md files. The problem is that nobody has treated SOPs like what they actually are: the directive layer for auto-improvement loops.

## The Direct Mapping

Every component of the Karpathy Loop has a direct SOP equivalent in MSP operations:

| Karpathy Loop Component | MSP SOP Equivalent |
|------------------------|-------------------|
| program.md (directive file) | The SOP itself — written in plain English |
| The single editable file | The SOP document + its associated config/script |
| The constraint boundaries | "Do not contact the client", "Do not modify production", "Escalate if uncertain" |
| The success metric | "Ticket resolved within SLA", "Alert correctly triaged", "Backup verified" |
| The experiment log | Change management record in PSA |
| The revert mechanism | Previous SOP version in version control |

An MSP that has well-maintained SOPs for ticket triage, alert response, patch deployment, and client onboarding already has the directive layer. The gap is not the instructions — it is the loop infrastructure around them.

## Why Poor SOPs Kill Auto-Improvement

The Karpathy Loop is only as good as its directive. Feed an agent a vague instruction file and it optimises in random directions. Feed it a precise, constrained directive and it finds genuine improvements.

The same applies to SOPs:

| SOP Quality | What Happens When You Run a Loop Against It |
|------------|---------------------------------------------|
| Detailed, specific, with clear success criteria | Agent proposes targeted improvements, measurable results |
| Vague, generic ("handle the alert professionally") | Agent proposes changes that are technically valid but operationally useless |
| Missing edge cases documented | Agent discovers edge cases the hard way — by breaking things |
| No constraints defined ("do not escalate to client without approval") | Agent optimises the metric by taking shortcuts humans would never take |
| No version history | No way to tell whether a change improved things or made them worse |
| Written for humans, not machines | Ambiguity that humans resolve with judgement causes agents to fail silently |

Most MSP SOPs fall into the bottom three categories. They are written for human technicians who can read between the lines, apply judgement, and know that "escalate if needed" means "escalate if the client is a hospital, not if it is a 5-person accounting firm." An agent cannot read between lines. It reads the lines.

## The Three Levels of SOP Maturity for Auto-Improvement

### Level 1: Human-Only SOPs (Where Most MSPs Are)

Written in prose. Designed for technician onboarding. Contain implicit knowledge that exists in the writer's head but not on the page.

Example:

> **Alert Response — High CPU**
> Check the server. If it is a backup window, dismiss. If not, check top processes. Restart the service if it is the usual one. Escalate if you are not sure.

This is fine for a human who has been on the team for six months and knows which server has the "usual" problem. It is useless for an agent. What server? What service? What does "not sure" mean in measurable terms?

### Level 2: Machine-Readable SOPs (What You Need for Loops)

Written in structured format. Every step is explicit. Every decision point has defined criteria. Every metric is measurable.

Example:

> **Alert Response — High CPU (SRV-ALERT-007)**
> Constraint: Do not restart services on production servers during business hours (08:00-18:00 client local time) without NOC lead approval.
>
> Step 1: Check alert device name against backup schedule in CMDB. If device has backup window within ±30 min of alert timestamp, dismiss alert as false positive. Log dismissal reason.
>
> Step 2: If not backup window, query top 5 processes by CPU usage via RMM API. Compare against known-high-CPU-processes list (maintained in config/high_cpu_exceptions.yaml).
>
> Step 3: If top process matches exception list AND CPU < 95%, log as known behaviour, dismiss.
>
> Step 4: If CPU >= 95% OR process not in exception list, create Priority 2 ticket assigned to Infrastructure team. Include top 5 process list in ticket body.
>
> Success metric: % of high-CPU alerts correctly actioned (dismissed with valid reason OR escalated to Infrastructure) without human correction.

Notice the differences: every decision is binary. Every threshold is a number. Every action is specific. The constraint about business hours is explicit. The success metric is measurable.

This is not better technical writing. This is a different kind of document — one that a loop engineer can translate into agent constraints.

### Level 3: Living SOPs (Where Auto-Improvement Takes Over)

The SOP becomes the editable surface. The loop proposes modifications to the SOP itself. The SOP evolves based on what actually works.

Example of a change the loop might propose:

> **Proposed modification to SRV-ALERT-007, Step 2:**
> Current: "If device has backup window within ±30 min of alert timestamp, dismiss."
> Proposed: "If device has backup window within ±45 min of alert timestamp, dismiss."
> Evidence: Over last 30 days, 23 alerts were dismissed under the 30-min rule but re-opened within 15 min. Extending to 45 min would have correctly dismissed 19 of those 23 without re-opening. The remaining 4 were genuine issues that would still be caught by Step 4.
> Metric impact: False positive dismissal rate drops from 12% to 3%. No genuine incidents missed.

This is the Karpathy Loop operating on SOPs. The agent reads the SOP, reads the outcome data, proposes a change to the SOP, tests it against history, and either commits or reverts.

## What Makes an SOP Auto-Improvable

Not every SOP is ready for a loop. Here is the checklist:

| Requirement | Why It Matters | How to Check |
|-------------|---------------|-------------|
| **Explicit thresholds** | Agents cannot interpret "high" or "unusual" — they need numbers | Search your SOPs for qualitative words: high, low, unusual, slow, many, few |
| **Binary decision points** | Every fork in the process must be answerable with yes/no | Rewrite "if it looks like X" as "if metric Y exceeds threshold Z" |
| **Defined constraints** | What the agent must never do | List every "do not" explicitly — no implicit boundaries |
| **Measurable success metric** | You cannot improve what you cannot measure | Every SOP should have a pass/fail test that runs without human judgement |
| **Version controlled** | You need to know what changed and when | SOPs live in git, not SharePoint |
| **Linked to operational data** | The SOP must connect to systems that produce measurable outcomes | Ticket category, alert severity, resolution time — all linkable to specific SOPs |
| **Ground truth available** | You need labelled examples of correct outcomes | Tickets that were re-categorised, alerts that were manually re-prioritised, tasks that were redone |

### The Qualitative Word Audit

Run this against your SOP library. Every word on the left is a sign the SOP is not ready for auto-improvement:

| Replace This | With This |
|-------------|----------|
| "If CPU is high" | "If CPU exceeds 90% for more than 5 minutes" |
| "Check if it is a known issue" | "Compare against known-issues list in config/known_issues.yaml" |
| "Escalate if uncertain" | "Escalate if confidence score < 0.7 OR process not in exception list" |
| "Respond within a reasonable time" | "Acknowledge within 15 minutes, resolve or escalate within 60 minutes" |
| "Common problem" | "Problem appears in >5 tickets in last 90 days" |
| "As needed" | Delete. Replace with specific trigger condition or remove the step entirely |
| "Professional manner" | Delete. Not measurable. Replace with specific communication template reference |

## SOPs as the Context Layer

There is a deeper reason SOPs matter for auto-improvement that goes beyond the program.md analogy. SOPs are the MSP's **context layer** — the persistent, structured representation of how the business operates.

Karpathy's original insight was about context windows. An agent without persistent memory reinvents "done" every session. It has no idea what it tried before. It cannot distinguish between "this change improved the harness" and "this change happened to work on three tasks before the context window got polluted."

SOPs solve this for MSPs in the same way. They encode institutional knowledge that survives technician turnover, shift changes, and context window resets. When a loop engineer writes a program.md that references SOP-007 for alert handling, the agent has access to the accumulated operational wisdom of every technician who contributed to that SOP over years.

| Without SOPs | With SOPs |
|-------------|----------|
| Agent starts from zero each session | Agent starts from accumulated best practice |
| Knowledge lives in technicians' heads | Knowledge lives in version-controlled documents |
| Improvement is reinvented per technician | Improvement compounds across versions |
| No way to measure what "better" looks like | SOP defines the baseline — deviation from it is measurable |
| New technician = knowledge reset | New technician reads the SOP = knowledge transfer |

## The Practical Sequence

If you are an MSP with a SOP library and you want to apply the Karpathy Loop, here is the order of operations:

**Week 1: Audit your SOPs against the auto-improvable checklist.** Count how many have explicit thresholds, binary decisions, and measurable success metrics. Most MSPs find 10-20% of their SOPs meet the standard. That is fine — you only need 3-5 to start.

**Week 2: Upgrade your top 3 SOPs to Level 2.** Pick the ones that cover the most repetitive, most measurable processes. Ticket triage, alert response, and new-user provisioning are typical candidates. Rewrite them with explicit thresholds, binary decisions, and success metrics. Put them in git.

**Week 3: Build the test sets.** For each upgraded SOP, pull historical data from your PSA/RMM. Label correct outcomes. You need 500+ labelled examples per SOP. This is the tedious part. It is also the part that determines whether the loop works at all.

**Week 4: Run the loop.** Point the agent at the SOP, the test set, and the success metric. Let it propose modifications overnight. Review the proposals in the morning. Accept the ones that improve the metric. Reject the ones that game it.

**Week 5-8: Expand.** Upgrade 5 more SOPs. Run loops on all of them. Begin cross-referencing — the alert SOP feeds the ticket SOP, the ticket SOP feeds the escalation SOP. The loops start compounding across processes.

**Week 9-12: Promote to production.** Move the best-performing loop outputs from sandbox to production with human review. Measure the impact on SLAs, resolution times, and technician hours. Report the numbers.

## The Honest Truth About SOPs

Most MSP SOPs are bad. They are outdated, vague, written for compliance rather than operations, and maintained in formats that resist version control. This is not a criticism — it is the natural state of documentation in any organisation that prioritises client delivery over internal process.

But the Karpathy Loop does not work without good instructions. Karpathy himself spent significant time on the program.md file. The agent's success was determined by the quality of the directive, not the sophistication of the search.

The MSP that invests in upgrading its SOPs to machine-readable standard is not just preparing for auto-improvement. It is making its human operations better too. Explicit thresholds help technicians make faster decisions. Binary decision points reduce escalations. Measurable success metrics give managers actual visibility into performance.

The SOP upgrade is the work. The loop is the reward.

---

*Part of the Karpathy Loop for MSPs series: [Part 1: Where Auto-Improvement Lands](http://ubuntu4:3002/posts/the-karpathy-loop-for-msps-whe/) | [Part 2: SOC ML Overlap and Gaps](http://ubuntu4:3002/posts/when-your-sister-company-alrea/) | [The Karpathy Loop Reference](http://ubuntu4:3002/posts/the-karpathy-loop-reference-guide/)*
- [Beyond IT: Extending the Loop to Every Business Function](http://ubuntu4:3002/posts/beyond-it-extending-the-karpat/)
- [Taking the Loop to Client Environments](http://ubuntu4:3002/posts/taking-the-karpathy-loop-to-cl/)
- [The LLM-Wiki Pattern for MSP Knowledge Management](http://ubuntu4:3002/posts/the-llm-wiki-pattern-write-tim/)

**Tags**: msp, standard-operating-procedures, sop, karpathy-loop, auto-improvement, ai-agents, managed-services, documentation
**Categories**: AI Automation, Business Strategy