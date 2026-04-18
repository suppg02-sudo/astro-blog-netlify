---
pubDatetime: 2026-04-18T18:30:00Z
title: "The Microsoft MSP Dilemma: Build the Loop in Open Source, Run It on What You Know"
postSlug: "the-microsoft-msp-dilemma-buil"
description: "The Microsoft MSP Dilemma: Build the Loop in Open Source, Run It on What You Know"
tags:
  - msp
series: karpathy-msp
---

Both MSPs run on Microsoft. Intune for device management. Entra ID for identity. Defender for endpoint protection. M365 for everything else. Their technicians live in PowerShell, Azure portals, and Teams. Their developers use GitHub Copilot. Their clients pay for Microsoft licences and expect Microsoft-compatible everything.

The Karpathy Loop — the auto-improvement pattern that runs 700 experiments overnight — was built in 630 lines of Python by one person using open-source tooling. No Azure. No Copilot Studio. No Microsoft anything.

So which stack should the MSPs use for auto-improvement? The honest answer is both — but not in the way most people think.

## The Wrong Question

"Do we go all-in on Microsoft AI or build everything in open source?" is the wrong framing. It assumes the loop and the environment it operates on must be the same stack.

They do not. The Karpathy Loop has three layers, and they have different stack requirements:

| Layer | What It Does | Right Stack |
|-------|-------------|------------|
| **Loop infrastructure** | Propose → test → measure → keep/revert. The engine. | Open source — Python, bash, git |
| **Agent intelligence** | The model that proposes changes. Reads traces, writes modifications. | Either — GitHub Copilot API, Claude, GPT, local models all work |
| **Editable surfaces** | The thing being optimised — SOPs, configs, scripts, rules. | Whatever the MSP already uses — PowerShell, YAML, JSON, Azure configs |

The loop engine is 12 lines of logic. The agent can be any LLM. The surfaces are whatever your MSP runs on. Conflating these three layers into one stack decision is where most teams go wrong.

## Why Open Source for the Loop Infrastructure

The loop itself — propose, test, measure, commit or revert — should be built on open-source tooling. Not because open source is ideologically superior, but because the Karpathy Loop pattern has specific requirements that Microsoft's AI tooling does not currently optimise for.

| Requirement | Open Source Tools | Microsoft Equivalent | Gap |
|-------------|-----------------|---------------------|-----|
| Overnight experiment batching | Python scripts, cron, simple loops | Azure ML pipelines | Azure ML is designed for model training, not config optimisation loops |
| Single-file constraint enforcement | Git + file-level permissions | Azure DevOps branch policies | Close, but heavier than needed |
| Per-experiment metric comparison | Python + JSON logs + simple comparison | Azure Monitor + Log Analytics | Massive overkill for "did metric X improve?" |
| Revert on failure | Git revert | Azure DevOps rollback | Both work, git is simpler |
| Experiment logging | Plain text files, JSON, SQLite | Azure Cosmos DB, Application Insights | Enterprise logging for what is essentially "tried X, score went from 72 to 68, reverted" |
| Cost for 100 experiments/night | $0-2 in compute | $5-20 in Azure services for equivalent | 10x cost difference at scale |
| Portability | Runs anywhere Python runs | Locked to Azure | If you change clouds, you rewrite |

The loop infrastructure is simple on purpose. Karpathy's entire setup was three files. Wrapping that in Azure ML pipelines, Azure Monitor dashboards, and Copilot Studio workflows adds complexity without adding capability. The point of the loop is minimalism. Azure is built for enterprise complexity.

## Why Microsoft for the Editable Surfaces

The thing being optimised should stay on whatever the MSP already uses. If your technicians write PowerShell, the agent proposes PowerShell modifications. If your alert configs live in Azure Monitor, the agent modifies Azure Monitor rules. If your SOPs are in SharePoint, the loop reads and writes SharePoint documents.

| Surface | Stay on Microsoft Because |
|---------|-------------------------|
| PowerShell scripts | Your team knows them. Your RMM runs them. Rewriting in Python helps nobody. |
| Intune configuration profiles | These ARE Microsoft. No alternative exists. |
| Azure Monitor alert rules | The data source is Azure. The rules should live next to the data. |
| Entra ID conditional access policies | Microsoft-only. Agent proposes JSON modifications to existing policies. |
| Defender detection rules | Microsoft-only. Agent tunes sensitivity and exclusion lists. |
| M365 admin configs | Microsoft-only. |
| SOPs in SharePoint | Your team already searches SharePoint. Keep them there. Add version control via SharePoint versioning or git sync. |
| PSA ticket data (ConnectWise, etc.) | Whatever PSA you use, the agent reads its API. No migration needed. |

The loop does not replace your Microsoft stack. It optimises it. The agent proposes changes to your existing PowerShell scripts, your existing Azure alert configs, your existing Intune profiles. You do not rip out Microsoft and replace it with Linux. You build a Python loop that makes your Microsoft environment better.

## GitHub Copilot: Where It Fits and Where It Does Not

Both MSPs use GitHub Copilot. This is genuinely useful — but for a different part of the process than most people assume.

### Where Copilot Helps

| Task | How Copilot Helps |
|------|-------------------|
| Writing the loop infrastructure scripts | Copilot is excellent at generating the Python scaffolding for propose/test/measure loops |
| Writing PowerShell modifications | Copilot knows PowerShell deeply. When the agent proposes a script change, Copilot can help validate the syntax. |
| Building eval harnesses | Copilot can generate test cases from historical ticket data |
| Translating SOPs to machine-readable format | Copilot can convert human prose SOPs into structured YAML/JSON |
| Generating API integration code | Copilot knows the Microsoft Graph API, ConnectWise API, RMM APIs |

### Where Copilot Does Not Help

| Task | Why Copilot Falls Short |
|------|------------------------|
| Running the loop itself | Copilot is an assistant, not an autonomous agent. It cannot run 100 experiments overnight without a human clicking "accept" each time. |
| Defining the Karpathy Triplet | Choosing the right metric, the right editable surface, and the right constraints requires domain judgement that Copilot does not have |
| Avoiding metric gaming | Copilot will happily help you optimise a metric that does not reflect business value. It has no opinion on whether the metric is the right metric. |
| Cross-SOP reasoning | Copilot operates within a single file context. It does not see that changing the alert SOP might break the ticket SOP downstream. |
| Governance decisions | Who reviews, who approves, what goes to production — these are organisational decisions, not code generation tasks |

**The right mental model**: Copilot is the technician's power tool. The Karpathy Loop is the overnight shift worker. They do different jobs. Copilot helps you build the loop. The loop then runs autonomously. Copilot is not the loop.

## The Model Empathy Problem

The Nate B Jones video surfaced a finding worth applying here. When Third Layer built the auto-agent, they discovered that same-model pairs dramatically outperform cross-model pairs. A Claude meta-agent writes better harnesses for a Claude task-agent. A GPT meta-agent understands GPT task-agents better.

What does this mean for Microsoft-heavy MSPs?

| Stack Choice | Meta-Agent | Task-Agent | Empathy Score |
|-------------|-----------|------------|--------------|
| All Microsoft | Copilot / Azure AI | Copilot / Azure AI | High — same model, same training data, same tendencies |
| Mixed | Open-source loop + Copilot agent | PowerShell surfaces + Copilot-assisted technicians | Medium — agent knows Microsoft tooling but runs in Python |
| All Open Source | Local model or Claude | Python scripts, bash, open-source tools | High if consistent, but requires rewriting everything |

The pragmatic choice is the mixed stack — open-source loop infrastructure, Copilot as the agent intelligence, Microsoft surfaces. The model empathy works because Copilot has been trained on enormous amounts of Microsoft documentation, PowerShell code, and Azure configurations. It understands the surfaces it is modifying from the inside.

## The Stack Decision Matrix

| Factor | Microsoft-Native | Open-Source Loop + MS Surfaces | All Open Source |
|--------|-----------------|-------------------------------|----------------|
| **Team expertise required** | Low (stay in MS ecosystem) | Medium (Python + MS) | High (rewrite everything) |
| **Time to first loop** | 2-3 months (wait for Copilot Studio maturity) | 3-4 weeks (Python loop + MS APIs) | 3-6 months (full rewrite of operational layer) |
| **Cost** | High (Azure AI, Copilot licensing) | Low (Python free, compute minimal) | Low (everything free) | 
| **Client impact** | None | None | High (clients notice tooling changes) |
| **Lock-in risk** | High | Low on loop, medium on surfaces | None |
| **Flexibility** | Low (Microsoft roadmap) | High (swap any component) | Maximum |
| **Model empathy** | High | High (Copilot knows MS) | Depends on model choice |
| **Maintainability** | Easy for MS-focused team | Moderate | Hard if team is MS-focused |
| **Future-proofing** | Microsoft controls the roadmap | You control the loop, MS controls the surfaces | You control everything |

## The Recommendation

**Build the loop in open source. Run it on Microsoft. Use Copilot as the agent brain.**

Specifically:

1. **Loop engine**: Python scripts in a git repo. Cron schedules. JSON logs. Zero Microsoft dependencies. This is the 630-line Karpathy pattern. It should be simple, portable, and yours.

2. **Agent intelligence**: GitHub Copilot API or Azure OpenAI. The agent reads traces, proposes changes, and writes modifications. Copilot knows Microsoft tooling deeply. Use that.

3. **Editable surfaces**: Whatever the MSP already uses. PowerShell scripts. Azure Monitor alert rules. Intune profiles. SharePoint SOPs. No migration. No rewrite.

4. **Eval harness**: Python scripts that call the PSA/RMM APIs, pull historical data, and compute metrics. These are integration scripts, not a platform.

5. **Experiment logging**: Git commits + JSON files. Every proposed change is a commit. Every metric measurement is a JSON record. If you want dashboards later, build them. But start with files.

6. **Governance**: Human review in the morning. The loop runs overnight, proposes changes, and flags them for review. Nobody promotes to production without clicking "approve" in the PSA.

This is not a compromise. It is the correct architecture for an MSP that lives in Microsoft but wants to own its improvement infrastructure.

## What to Tell the Microsoft Account Manager

When your Microsoft rep suggests using Copilot Studio for the entire auto-improvement stack, the honest response is:

"We will use Copilot as the intelligence layer. It is excellent at understanding our Microsoft environment and proposing changes. But the loop infrastructure — the propose/test/measure/revert engine — needs to be lightweight, portable, and under our control. Azure ML pipelines are built for model training at enterprise scale. We need a 630-line Python script that runs 100 experiments overnight and costs $2 in compute. We will use Copilot to write that script."

## What to Tell the Open-Source Advocate

When the open-source advocate on the team suggests ripping out Microsoft and running everything on Linux with local models:

"The clients pay for Microsoft. The technicians know PowerShell. The RMM speaks Azure. Rewriting the operational layer to satisfy a stack preference would take 6 months, break client integrations, and produce zero measurable improvement in service delivery. The loop runs in Python. The surfaces stay on Microsoft. The agent uses Copilot. This is pragmatism, not ideology."

## The One Thing Both Sides Agree On

The loop infrastructure — the propose/test/measure/revert engine — should be so simple that it fits in a single directory. Three files. A few hundred lines. If it needs Azure ML, Copilot Studio, Docker containers, or a Kubernetes cluster to run, it is too complicated.

Karpathy's original setup was three files. The MSP version should be five — one extra for the Microsoft API integration layer, one extra for the eval harness.

The sophistication lives in the directive (the SOP) and the metric (the eval harness), not in the infrastructure. Get the stack out of the way. Focus on what to improve and how to measure it.

---

*Part of the Karpathy Loop for MSPs series: [Part 1: Where Auto-Improvement Lands](http://ubuntu4:3002/posts/the-karpathy-loop-for-msps-whe/) | [Part 2: SOC ML Overlap and Gaps](http://ubuntu4:3002/posts/when-your-sister-company-alrea/) | [Part 3: SOPs as Program.md](http://ubuntu4:3002/posts/sops-are-the-program-md-why-st/) | [The Karpathy Loop Reference](http://ubuntu4:3002/posts/the-karpathy-loop-reference-guide/)*
- [Beyond IT: Extending the Loop to Every Business Function](http://ubuntu4:3002/posts/beyond-it-extending-the-karpat/)
- [Taking the Loop to Client Environments](http://ubuntu4:3002/posts/taking-the-karpathy-loop-to-cl/)
- [The LLM-Wiki Pattern for MSP Knowledge Management](http://ubuntu4:3002/posts/the-llm-wiki-pattern-write-tim/)

**Tags**: msp, microsoft, github-copilot, open-source, karpathy-loop, auto-improvement, stack-decisions, azure, managed-services
**Categories**: AI Automation, Business Strategy