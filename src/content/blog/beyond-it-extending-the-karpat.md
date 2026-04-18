---
pubDatetime: 2026-04-18T19:00:00Z
title: "Beyond IT: Extending the Karpathy Loop to Every MSP Business Function"
postSlug: "beyond-it-extending-the-karpat"
description: "Beyond IT: Extending the Karpathy Loop to Every MSP Business Function"
tags:
  - msp
series: karpathy-msp
---

You've been running the Karpathy Loop for six months. Ticket routing is tighter. Alert tuning actually works. Your script library evolves itself. The triplet — one editable file, one metric, one fixed time budget — is muscle memory now.

Good. Because the triplet doesn't care what business function it touches.

The same pattern that optimises ticket routing can optimise invoicing accuracy. The same loop that tunes alert thresholds can tune proposal win rates. The mechanism is identical: propose a change, measure the result, keep or revert. What changes is the surface you edit and the number you watch.

This post maps the triplet across six non-IT domains. Each one is a loop waiting to run.

## Why This Works Outside IT

The Karpathy Loop isn't an IT concept. It's an optimisation concept that happens to have been applied to IT first because that's where the data lives in neat, structured piles.

But every business function has:

- A configuration that controls how it behaves (your editable surface)
- A definition of success (your metric)
- Historical data to validate against (your time budget)

If those three things exist, the loop can run. Let's walk through them.

---

## 1. Accounts and Finance

**Edit surface:** Invoice rules configuration (JSON/YAML) — auto-categorisation rules, cost allocation logic, payment term mappings.

**Metric:** Percentage of invoices sent without correction. If your finance team re-issues more than 2% of invoices, your rules are wrong.

**Time budget:** Evaluate against the last 50 invoices per batch.

**What the loop proposes:** The loop examines correction patterns and proposes adjustments — shifting cost allocation logic when recurring misclassifications cluster around specific service categories, adjusting payment terms based on client payment history (clients who consistently pay at 45 days get net-15 with early-payment discounts instead of net-30), and tightening auto-categorisation rules where human overrides keep firing.

**Why it matters:** Every corrected invoice is 15 minutes of someone's time and a hit to credibility. Get this to 99%+ first-pass accuracy and you've bought back an entire FTE's worth of rework.

The loop runs overnight. In the morning you see: "Tried adjusting payment terms for Client X from net-30 to net-15 with 2% discount. Predicted correction rate drop: 0.8% → 0.2%. Actual: 0.3%. Keeping." That's the pattern from [Part 1](http://ubuntu4:3002/posts/the-karpathy-loop-for-msps-whe/), applied to your AR ledger.

---

## 2. Project Management

**Edit surface:** Estimation model — a YAML or JSON file containing phase weights, complexity multipliers, resource rates, and risk buffers.

**Metric:** Estimation accuracy — the percentage of projects delivered within 10% of the original estimate.

**Time budget:** Evaluate against the last 50 completed projects.

**What the loop proposes:** The loop compares estimated vs actuals across project phases and proposes corrections. Maybe your "network refresh" complexity multiplier should be 1.4, not 1.2, based on the last eight projects all running 20% over in the deployment phase. Maybe the discovery phase for cloud migrations needs a 1.6x weight because the scoping consistently underestimates environment complexity.

**Why it matters:** Inaccurate estimates are the silent profit killer. A project that runs 30% over eats margin from three projects that ran on time. As [Part 3](http://ubuntu4:3002/posts/sops-are-the-program-md-why-st/) established, your SOPs are the program — and if your estimation model is a static spreadsheet you updated once in 2023, your program has a bug.

The loop treats estimation as a living model. Every completed project is a training sample. Every overnight run is a model update.

---

## 3. Procurement and Vendor Management

**Edit surface:** Vendor scoring rules — a JSON file with weighted criteria (price, delivery speed, support quality, licence terms, compatibility with existing stack).

**Metric:** Cost savings versus previous vendor arrangement, while maintaining quality scores above a defined floor.

**Time budget:** Evaluate against the last 12 months of procurement data.

**What the loop proposes:** The loop surfaces opportunities you'd miss manually. Adjusted vendor weights based on actual delivery performance (not the SLA on paper — the real SLA from your ticket data). Licence consolidation patterns — three vendors providing overlapping functionality that one contract could cover. Hardware lifecycle timing optimisation — buying workstations in Q3 instead of Q4 when your data shows Q4 lead times are 40% longer.

**Why it matters:** Most MSPs review vendor relationships annually, if that. The market moves quarterly. Pricing changes, support quality drifts, new entrants appear. A loop that continuously evaluates your vendor portfolio against actual performance data catches drift before it becomes a cost problem.

This is the [reference guide](http://ubuntu4:3002/posts/the-karpathy-loop-reference-guide/) pattern applied to spend: fixed criteria, measurable outcome, automated evaluation.

---

## 4. Sales and Proposals

**Edit surface:** Proposal scoring model — a configuration file defining what makes a proposal likely to win (qualification criteria, pricing ranges by client type, service bundle composition, response timing thresholds).

**Metric:** Proposal-to-close conversion rate.

**Time budget:** Evaluate against the last 100 proposals with known outcomes.

**What the loop proposes:** The loop identifies patterns in won vs lost deals. Maybe proposals under £5k have a 60% close rate but proposals between £5k–£10k only close at 30% — suggesting your mid-tier pricing needs restructuring. Maybe clients in the legal sector respond better to response times under 24 hours while retail clients care more about bundled support. Maybe three-person technical proposals outperform single-author proposals by 2x.

**Why it matters:** Sales optimisation in MSPs is usually gut-driven. "We win about one in three" is the typical answer when you ask about conversion rates. But which third? And why? The loop turns proposal performance into data, and data into configuration changes.

As [Part 5](http://ubuntu4:3002/posts/from-riding-microsoft-to-ownin/) discussed, moving beyond platform dependency means owning your commercial model. Your proposal engine is a core asset. The loop makes it self-improving.

---

## 5. Client Success and Retention

**Edit surface:** Client health scoring rules — weighted signals that combine to produce a single health score per client.

**Metric:** Ability to predict churn or expansion 60 days in advance, measured as the accuracy of your health score's directional predictions.

**Time budget:** Evaluate against the last 24 months of client data (churn events, expansion events, and stable clients).

**What the loop proposes:** The loop adjusts signal weights based on what actually predicted churn. The signals it evaluates:

- Ticket volume trend (rising = bad, but dropping fast = also bad)
- SLA breach frequency
- Invoice query rate (sudden increase in billing questions often precedes departure)
- Time since last escalation
- Support contact changes (new IT manager = new relationship to build, or new decision-maker evaluating vendors)
- Frequency of "strategic review" requests
- Responsiveness to quarterly business reviews

Maybe ticket volume trend should be weighted at 0.25, not 0.15. Maybe a support contact change in the last 90 days should be the single strongest churn predictor. The loop figures this out from your data, not from industry benchmarks written for companies that aren't you.

**Why it matters:** MSPs discover churn too late. The cancellation email arrives and the account manager says "I knew they were quiet recently." The loop replaces "I knew" with "the score flagged this 60 days ago and you had a retention playbook ready."

---

## 6. HR and Recruitment

**Edit surface:** Candidate scoring rubric — a YAML file defining weighted evaluation criteria (technical assessment scores, cultural fit indicators, experience relevance, interview performance ratings, reference strength).

**Metric:** Correlation between candidate score and 6-month performance review rating.

**Time budget:** Evaluate against the last 20 hires with completed 6-month reviews.

**What the loop proposes:** The loop tests whether your rubric actually predicts success. Maybe technical assessment scores correlate weakly with 6-month performance (r = 0.2) but cultural fit indicators correlate strongly (r = 0.7). The loop proposes shifting weights accordingly. Maybe candidates who mentioned home lab projects in interviews outperform those who didn't — the loop adds that as a screening criterion. Maybe your onboarding checklist is missing a step that early high-performers all happened to complete organically.

**Why it matters:** Bad hires are expensive. In an MSP, a bad technical hire costs 3–6 months of salary in ramp time, client relationship damage, and team morale impact. The loop treats your hiring process as a predictive model and continuously recalibrates it.

---

## What Makes a Domain Loop-Ready

Not everything is ready for the loop on day one. Before you deploy a triplet to a new domain, check these four prerequisites:

| Prerequisite | What It Means | Red Flag |
|---|---|---|
| **Structured historical data** | You can query past outcomes programmatically | "It's all in people's heads" |
| **Objective success metric** | There's a number that unambiguously defines success | "We'll know it when we see it" |
| **Human-editable configuration** | The control surface is a file, not a meeting | "We'd need to change the process" |
| **Safe experimentation environment** | A bad proposal can be reverted without damage | "If this goes wrong, we lose the client" |

If you're missing the data, start by instrumenting the domain. Collect 3 months of data before running the loop. If the metric is subjective, refine it until it's objective. If the configuration is locked in a vendor platform, export it to a local file you control. If experimentation is risky, reduce the time budget and increase human oversight until you trust the pattern.

[Part 2](http://ubuntu4:3002/posts/when-your-sister-company-alrea/) covered the trap of copying patterns without adaptation. Same principle applies here: don't deploy all six loops simultaneously. Sequence them based on readiness.

---

## The Roadmap: Which Domain First

You've been running IT loops for six months. Here's the recommended sequence for expanding:

| Quarter | Domain | Reasoning |
|---|---|---|
| Q7 | Client Success | Fastest ROI — churn prevention is immediate revenue protection. Your PSA data is already structured. The metric is clear. |
| Q8 | Accounts/Finance | Second easiest — invoice data is structured by definition. Low risk (corrections are caught before sending). Builds finance team confidence in the pattern. |
| Q9 | Project Management | Requires the most historical data (50 completed projects with clean actuals). By Q9 you'll have accumulated enough from the first two loops running. |
| Q10 | Sales/Proposals | Needs volume (100 proposals with outcomes). Takes longest to accumulate data but delivers the highest commercial impact. |
| Q11 | Procurement/Vendor | 12-month evaluation window means this loop's first meaningful cycle completes around the one-year mark. Start the data collection in Q9. |
| Q12 | HR/Recruitment | Lowest data volume (20 hires) but slowest feedback loop (6-month reviews). Start collecting rubric scores now, run the first evaluation when you have 20 completed cycles. |

The sequence isn't arbitrary. It follows a principle: **start where data is richest and risk is lowest.** Client success and finance have clean, structured data and reversible outcomes. Sales and recruitment have high commercial impact but require patience.

---

## The Compound Effect

Here's the meta-point.

By month 12, you're running loops across IT operations, client success, finance, project management, sales, procurement, and recruitment. Seven domains. Seven editable surfaces. Seven metrics. All evolving overnight while your team sleeps.

At this point, the MSP itself becomes the loop.

Every process has a number. Every number has a configuration that controls it. Every configuration is being continuously tested against reality. You've built an organisation where:

- Every process is **measured** (the metric)
- Every measurement is **optimisable** (the editable surface)
- Every optimisation is **automated** (the loop)

This is the compound effect. The first loop teaches you the pattern. The second loop proves it transfers. The third loop makes it routine. By the seventh, it's culture.

Most MSPs optimise by committee. Quarterly review, someone raises a concern, a project is launched, six months later something might have changed. The loop optimises by experiment. Every night. With evidence. Automatically.

The Karpathy Loop isn't an IT tool. It's an operating system for continuous improvement. You just happened to install it in IT first because that's where the data was.

Now it's everywhere.


## The Full Series

- [Part 1: The Karpathy Loop for MSPs](http://ubuntu4:3002/posts/the-karpathy-loop-for-msps-whe/)
- [Part 2: When Your Sister Company Already Does ML](http://ubuntu4:3002/posts/when-your-sister-company-alrea/)
- [Part 3: SOPs Are the Program.md](http://ubuntu4:3002/posts/sops-are-the-program-md-why-st/)
- [Part 4: The Microsoft MSP Dilemma](http://ubuntu4:3002/posts/the-microsoft-msp-dilemma-buil/)
- [Part 5: From Riding Microsoft to Owning Your Stack](http://ubuntu4:3002/posts/from-riding-microsoft-to-ownin/)
- [Reference: The Karpathy Loop Reference Guide](http://ubuntu4:3002/posts/the-karpathy-loop-reference-guide/)
- [Beyond IT: Extending the Loop to Every Business Function](http://ubuntu4:3002/posts/beyond-it-extending-the-karpat/)
- [Taking the Loop to Client Environments](http://ubuntu4:3002/posts/taking-the-karpathy-loop-to-cl/)
- [The LLM-Wiki Pattern for MSP Knowledge Management](http://ubuntu4:3002/posts/the-llm-wiki-pattern-write-tim/)
---

**Tags**: karpathy-loop, msp-operations, continuous-improvement, business-optimisation, ai-agents

**Categories**: MSP Strategy, AI Operations, Business Process