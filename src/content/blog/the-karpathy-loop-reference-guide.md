---
pubDatetime: 2026-04-18T16:30:00Z
title: "The Karpathy Loop Reference: Auto-Research, Auto-Agent, and Local Hard Takeoff"
postSlug: "the-karpathy-loop-reference-guide"
description: "The Karpathy Loop Reference: Auto-Research, Auto-Agent, and Local Hard Takeoff"
tags:
  - ai-agents
  - auto-research
  - karpathy-loop
  - self-improvement
  - agent-harness
  - msp
series: karpathy-msp
---

# The Karpathy Loop Reference: Auto-Research, Auto-Agent, and Local Hard Takeoff

A comprehensive reference guide to the auto-improvement patterns reshaping AI agent engineering, derived from Nate B Jones's analysis of Karpathy's auto-research, Third Layer's auto-agent, and the implications for organizations in 2026.

## Quick Reference

| Concept | Definition |
|---------|-----------|
| **Karpathy Loop** | Edit → Run → Measure → Keep/Discard. Minimal overnight optimization loop. |
| **Auto-Agent** | Meta-agent optimizes the task-agent's harness (prompts, tools, routing). |
| **Local Hard Takeoff** | Steep, sudden, compounding improvement bounded to one domain. Not AGI. |
| **Karpathy Triplet** | 1 editable file + 1 metric + 1 fixed time budget. The prerequisites. |
| **Model Empathy** | Same-model meta→task pairing outperforms cross-model. Shared weights = shared understanding. |## The Core Pattern: Karpathy Loop

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MDAgNDIwIiBzdHlsZT0id2lkdGg6MTAwJTsgbWF4LXdpZHRoOjYwMHB4OyBoZWlnaHQ6YXV0bzsgZGlzcGxheTpibG9jazsiPgo8cmVjdCB3aWR0aD0iNjAwIiBoZWlnaHQ9IjQyMCIgZmlsbD0iIzBmMTcyYSIvPgo8ZGVmcz4KICAgICAgICAgIDxtYXJrZXIgaWQ9ImFycm93IiBtYXJrZXJXaWR0aD0iMTAiIG1hcmtlckhlaWdodD0iNyIgcmVmWD0iOSIgcmVmWT0iMy41IiBvcmllbnQ9ImF1dG8iPgogICAgICAgICAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgMTAgMy41LCAwIDciIGZpbGw9IiM2NDc0OGIiLz4KICAgICAgICAgIDwvbWFya2VyPgogICAgICAgIDwvZGVmcz4KPHBhdGggZD0iTTM2MC4wLDgwLjAgUTM2Mi41LDE3Mi41IDM2NS4wLDIwNS4wIiBmaWxsPSJub25lIiBzdHJva2U9IiM5NGEzYjgiIHN0cm9rZS13aWR0aD0iMS41IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93KSIvPgo8cGF0aCBkPSJNNDM1LjAsMjMwLjAgUTM3MC4wLDI0Mi41IDMwNS4wLDMxNS4wIiBmaWxsPSJub25lIiBzdHJva2U9IiM5NGEzYjgiIHN0cm9rZS13aWR0aD0iMS41IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93KSIvPgo8cGF0aCBkPSJNMjQwLjAsMzQwLjAgUTIzNy41LDMwNy41IDIzNS4wLDIxNS4wMDAwMDAwMDAwMDAwMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjOTRhM2I4IiBzdHJva2Utd2lkdGg9IjEuNSIgbWFya2VyLWVuZD0idXJsKCNhcnJvdykiLz4KPHBhdGggZD0iTTE2NS4wLDE5MC4wMDAwMDAwMDAwMDAwMyBRMjMwLjAsMTE3LjUgMjk1LjAsMTA1LjAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzk0YTNiOCIgc3Ryb2tlLXdpZHRoPSIxLjUiIG1hcmtlci1lbmQ9InVybCgjYXJyb3cpIi8+CjxyZWN0IHg9IjI0MC4wIiB5PSI2MC4wIiB3aWR0aD0iMTIwIiBoZWlnaHQ9IjQwIiByeD0iOCIgZmlsbD0iIzNiODJmNiIgc3Ryb2tlPSIjM2I4MmY2IiBzdHJva2Utd2lkdGg9IjEiLz4KPHRleHQgeD0iMzAwLjAiIHk9Ijg1LjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxNCIgZmlsbD0id2hpdGUiPlByb3Bvc2U8L3RleHQ+CjxyZWN0IHg9IjM3MC4wIiB5PSIxOTAuMCIgd2lkdGg9IjEyMCIgaGVpZ2h0PSI0MCIgcng9IjgiIGZpbGw9IiMxNGI4YTYiIHN0cm9rZT0iIzE0YjhhNiIgc3Ryb2tlLXdpZHRoPSIxIi8+Cjx0ZXh0IHg9IjQzMC4wIiB5PSIyMTUuMCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1mYW1pbHk9InN5c3RlbS11aSxzYW5zLXNlcmlmIiBmb250LXNpemU9IjE0IiBmaWxsPSJ3aGl0ZSI+UnVuIEV4cGVyaW1lbnQ8L3RleHQ+CjxyZWN0IHg9IjI0MC4wIiB5PSIzMjAuMCIgd2lkdGg9IjEyMCIgaGVpZ2h0PSI0MCIgcng9IjgiIGZpbGw9IiMxMGI5ODEiIHN0cm9rZT0iIzEwYjk4MSIgc3Ryb2tlLXdpZHRoPSIxIi8+Cjx0ZXh0IHg9IjMwMC4wIiB5PSIzNDUuMCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1mYW1pbHk9InN5c3RlbS11aSxzYW5zLXNlcmlmIiBmb250LXNpemU9IjE0IiBmaWxsPSJ3aGl0ZSI+TWVhc3VyZSBNZXRyaWM8L3RleHQ+CjxyZWN0IHg9IjExMC4wIiB5PSIxOTAuMDAwMDAwMDAwMDAwMDMiIHdpZHRoPSIxMjAiIGhlaWdodD0iNDAiIHJ4PSI4IiBmaWxsPSIjOGI1Y2Y2IiBzdHJva2U9IiM4YjVjZjYiIHN0cm9rZS13aWR0aD0iMSIvPgo8dGV4dCB4PSIxNzAuMCIgeT0iMjE1LjAwMDAwMDAwMDAwMDAzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTQiIGZpbGw9IndoaXRlIj5LZWVwIC8gUmV2ZXJ0PC90ZXh0Pgo8dGV4dCB4PSIzMDAiIHk9IjIwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1mYW1pbHk9InN5c3RlbS11aSxzYW5zLXNlcmlmIiBmb250LXNpemU9IjE4IiBmaWxsPSIjZTJlOGYwIiBmb250LXdlaWdodD0iYm9sZCI+S2FycGF0aHk8L3RleHQ+Cjx0ZXh0IHg9IjMwMCIgeT0iMjI0IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTgiIGZpbGw9IiNlMmU4ZjAiIGZvbnQtd2VpZ2h0PSJib2xkIj5Mb29wPC90ZXh0Pgo8L3N2Zz4=" alt="Karpathy Core Loop Cycle" style="width:100%; height:auto; display:block; margin:1.5rem auto; max-width:600px;" />


Three components. That is the entire architecture.

| Component | Role | Constraint |
|-----------|------|-----------|
| Agent + 1 editable file | Proposes changes to a single file | Cannot modify infrastructure |
| 1 objectively testable metric | Evaluates each change | Fixed, not adjustable by agent |
| Fixed time limit per experiment | Bounds each cycle | 5 minutes in Karpathy's setup |

The human writes a plain English instruction file (the "program.md") setting direction and constraints. The agent executes the search. The minimalism is the point — by constraining to one file and one metric, the problem becomes tractable for an agent that can read the entire codebase in a single pass.

### Results Across Implementations

| Who | Experiments | Time | Result | Compute Cost |
|-----|------------|------|--------|-------------|
| Karpathy (training code) | ~700 | 2 days | 11% speedup, found bug in attention impl | Minimal |
| Shopify / Tobi Lutke | 37 | 8 hours | 19% performance gain | Internal |
| SkyPilot (16-GPU K8s) | 910 | 8 hours | Discovered scaling width > any single param | Under $300 |
| Auto-Agent (harness) | Unknown | Overnight | 96.5% SpreadsheetBench, 55.1% TerminalBench (claimed, unverified) | Minimal |

## Auto-Agent: From Code to Harness

The escalation: Karpathy optimized training code. Auto-Agent optimizes the agent harness — system prompts, tool definitions, routing logic, orchestration strategy.### Key Design Decisions

| Decision | Finding | Implication |
|----------|---------|-------------|
| Meta/Task split | Single agent improving itself didn't work | Being good at domain ≠ being good at improving domain |
| Model empathy | Same-model pairs dramatically outperform cross-model | Meta-agent shares implicit understanding of task-agent's reasoning |
| Traces vs scores | Scores-only caused improvement rate to drop fast | Understanding why > knowing that it improved |
| Emergent behaviors | Meta-agent invented spot-checking, verification loops, sub-agents | None of these were specified in the directive |

### Emergent Behaviors (Not Programmed)

| Behavior | Description |
|----------|------------|
| Spot-checking | Running individual tasks instead of full benchmark for small edits |
| Forced verification loops | Adding validation steps autonomously |
| Formatting validators | Ensuring output matches expected format |
| Progressive disclosure | Dumping long context when results overflow context window |
| Task-specific sub-agents | Building handoff logic when domain requires specialization |

## Local Hard Takeoff

Not the science-fiction intelligence explosion. A mundane, immediate, practical phenomenon: an optimization loop closes on a specific business system and compounds improvements faster than the surrounding organization can track.

| Domain | What It Looks Like |
|--------|-------------------|
| Pricing engine | Rewrites own heuristics over weekend, comes back 30% more accurate |
| Fraud detection | Discovers patterns human analyst wouldn't attempt |
| Customer service | Builds verification loops and escalation logic, halves resolution time |
| Agent harness | Rewrites prompts, tools, routing overnight |

The gap between orgs that can run optimization loops and those stuck at quarterly planning cycles creates asymmetric competitive advantage.

## Readiness Staircase

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MDAgMzQwIiBzdHlsZT0id2lkdGg6MTAwJTsgbWF4LXdpZHRoOjYwMHB4OyBoZWlnaHQ6YXV0bzsgZGlzcGxheTpibG9jazsiPgo8cmVjdCB3aWR0aD0iNjAwIiBoZWlnaHQ9IjM0MCIgZmlsbD0iIzBmMTcyYSIvPgo8ZGVmcz4KICAgICAgICAgIDxtYXJrZXIgaWQ9ImFycm93IiBtYXJrZXJXaWR0aD0iMTAiIG1hcmtlckhlaWdodD0iNyIgcmVmWD0iOSIgcmVmWT0iMy41IiBvcmllbnQ9ImF1dG8iPgogICAgICAgICAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgMTAgMy41LCAwIDciIGZpbGw9IiM2NDc0OGIiLz4KICAgICAgICAgIDwvbWFya2VyPgogICAgICAgIDwvZGVmcz4KPHJlY3QgeD0iMjAiIHk9IjI4MCIgd2lkdGg9IjEwMCIgaGVpZ2h0PSI0MCIgcng9IjgiIGZpbGw9IiMzYjgyZjYiIHN0cm9rZT0iIzNiODJmNiIgc3Ryb2tlLXdpZHRoPSIxIi8+Cjx0ZXh0IHg9IjcwLjAiIHk9IjMwNS4wIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEiIGZpbGw9IndoaXRlIj5PbmUgZWRpdGFibGUgZmlsZTwvdGV4dD4KPHRleHQgeD0iNzAuMCIgeT0iMzM0IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEiIGZpbGw9IiM5NGEzYjgiIGZvbnQtd2VpZ2h0PSJub3JtYWwiPjE8L3RleHQ+CjxyZWN0IHg9IjEyOCIgeT0iMjMyIiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjQwIiByeD0iOCIgZmlsbD0iIzE0YjhhNiIgc3Ryb2tlPSIjMTRiOGE2IiBzdHJva2Utd2lkdGg9IjEiLz4KPHRleHQgeD0iMTc4LjAiIHk9IjI1Ny4wIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEiIGZpbGw9IndoaXRlIj5PbmUgY2xlYXIgbWV0cmljPC90ZXh0Pgo8dGV4dCB4PSIxNzguMCIgeT0iMjg2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEiIGZpbGw9IiM5NGEzYjgiIGZvbnQtd2VpZ2h0PSJub3JtYWwiPjI8L3RleHQ+CjxyZWN0IHg9IjIzNiIgeT0iMTg0IiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjQwIiByeD0iOCIgZmlsbD0iIzEwYjk4MSIgc3Ryb2tlPSIjMTBiOTgxIiBzdHJva2Utd2lkdGg9IjEiLz4KPHRleHQgeD0iMjg2LjAiIHk9IjIwOS4wIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEiIGZpbGw9IndoaXRlIj5BdXRvbWF0ZWQgZXhwZXJpbWVudCBydW5uZXI8L3RleHQ+Cjx0ZXh0IHg9IjI4Ni4wIiB5PSIyMzgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMSIgZmlsbD0iIzk0YTNiOCIgZm9udC13ZWlnaHQ9Im5vcm1hbCI+MzwvdGV4dD4KPHJlY3QgeD0iMzQ0IiB5PSIxMzYiIHdpZHRoPSIxMDAiIGhlaWdodD0iNDAiIHJ4PSI4IiBmaWxsPSIjOGI1Y2Y2IiBzdHJva2U9IiM4YjVjZjYiIHN0cm9rZS13aWR0aD0iMSIvPgo8dGV4dCB4PSIzOTQuMCIgeT0iMTYxLjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMSIgZmlsbD0id2hpdGUiPlNhZmUgcm9sbGJhY2sgbWVjaGFuaXNtPC90ZXh0Pgo8dGV4dCB4PSIzOTQuMCIgeT0iMTkwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEiIGZpbGw9IiM5NGEzYjgiIGZvbnQtd2VpZ2h0PSJub3JtYWwiPjQ8L3RleHQ+CjxyZWN0IHg9IjQ1MiIgeT0iODgiIHdpZHRoPSIxMDAiIGhlaWdodD0iNDAiIHJ4PSI4IiBmaWxsPSIjZjk3MzE2IiBzdHJva2U9IiNmOTczMTYiIHN0cm9rZS13aWR0aD0iMSIvPgo8dGV4dCB4PSI1MDIuMCIgeT0iMTEzLjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMSIgZmlsbD0id2hpdGUiPkNvbnRpbnVvdXMgbG9vcCBydW5uaW5nPC90ZXh0Pgo8dGV4dCB4PSI1MDIuMCIgeT0iMTQyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEiIGZpbGw9IiM5NGEzYjgiIGZvbnQtd2VpZ2h0PSJub3JtYWwiPjU8L3RleHQ+CjxsaW5lIHgxPSIzMCIgeTE9IjMxNSIgeDI9IjU2MCIgeTI9IjMxNSIgc3Ryb2tlPSIjNDc1NTY5IiBzdHJva2Utd2lkdGg9IjEuNSIgbWFya2VyLWVuZD0idXJsKCNhcnJvdykiLz4KPHRleHQgeD0iMzAwIiB5PSIzMzIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMSIgZmlsbD0iIzY0NzQ4YiIgZm9udC13ZWlnaHQ9Im5vcm1hbCI+SW5jcmVhc2luZyBSZWFkaW5lc3M8L3RleHQ+Cjwvc3ZnPg==" alt="Readiness Staircase" style="width:100%; height:auto; display:block; margin:1.5rem auto; max-width:600px;" />


You cannot skip steps. Auto-improvement is a graduate-level capability when most orgs are struggling with agents 101.### Prerequisites (In Order)

| Step | What | Why |
|------|------|-----|
| 1. Context Layer | Structured external memory, persistent state across sessions | Without it, every session reinvents "done" and guesses what happened before |
| 2. Eval Harness | Scoring functions that reflect actual business value | You cannot automate what you cannot score |
| 3. Sandbox Environment | Safe place for hundreds of experiments without touching production | Experiments will fail; failure must be cheap |
| 4. Karpathy Triplet | 1 editable surface + 1 metric + 1 time budget | The minimal viable optimization target |
| 5. Auto-Improve Loop | Agent runs the cycle autonomously | The reward for building steps 1-4 |

## Safety: Practical Concerns

The relevant safety concerns are not intelligence explosions. They are quiet, specific, and easy to miss.

| Risk | What Happens | Business Example |
|------|-------------|-----------------|
| **Metric Gaming** | Agent optimizes proxy metric that diverges from actual value | Fraud model looks great in tests, misses real fraud |
| **Silent Degradation** | Subtle policy drift persists undetected | Quality erosion invisible to monitoring |
| **Contamination** | Optimization loop influences its own evaluation data | Results become unreliable |
| **Compounding Errors** | Bad optimization cascades through interconnected systems | One bad edit propagates everywhere |

### Mitigation Framework (From Karpathy's Own Design)

| Control | Implementation |
|---------|---------------|
| Tight loops | Fast experiment cycles with immediate feedback |
| Clear baselines | Version-controlled starting point |
| Revert capability | Any change can be undone |
| One file only | Agent cannot modify infrastructure |
| Locked evaluation | Metric and eval function are fixed |
| Human inspection | Results reviewed before production |

## The Small Team Advantage

| Factor | Small Team (3-5) | Enterprise (20+) |
|--------|------------------|-------------------|
| Iteration speed | Hours | Months |
| Approval gates | Minimal | Procurement cycles |
| Compute cost | $300-500 | Enterprise procurement |
| Context sharing | Natural | Organizational silos |
| Adoption of new patterns | Immediate | Quarterly meetings |
| Example | Karpathy (1 person), SkyPilot (3 people) | Most Fortune 500 AI teams |

The pattern: a three-person team with $500 in compute can run the same optimization loop that takes a 20-person enterprise team months to spec, approve, and execute. The iteration speed advantage is multiple orders of magnitude.

## Frontier Lab Ambitions

| Lab | Stated Goal | Timeline |
|-----|------------|----------|
| Anthropic | Claude N builds Claude N+1 (fully recursive) | Ongoing |
| OpenAI | Fully automated AI researcher | By 2028 |
| Open source | Auto-research + auto-agent (MIT licensed) | Available now |

The difference between frontier labs and open-source is scale and scope, not kind. Same loop: propose, run, evaluate, keep or discard.

## Deployment Checklist

<details>
<summary>Before Starting an Auto-Improvement Loop</summary>

- [ ] **Define the Karpathy Triplet**: 1 editable surface, 1 metric, 1 time budget
- [ ] **Build eval harness**: scoring functions that reflect business value
- [ ] **Create sandbox**: isolated environment where failure is cheap
- [ ] **Set up version control**: every change tracked, every change revertable
- [ ] **Establish baseline**: measure current performance before any optimization
- [ ] **Design auditability**: log all experiments, edits, and metric trajectories
- [ ] **Assign ownership**: who reviews the 47th experiment at 3am?
- [ ] **Choose domain carefully**: start where failure is cheapest, not most visible

</details>

<details>
<summary>Traces Infrastructure Checklist</summary>

- [ ] Capture full reasoning chains from agents (not just outcomes)
- [ ] Log why something improved, not just that it improved
- [ ] Build trace interpretation layer for meta-agent consumption
- [ ] Validate traces aren't contaminated by optimization loop
- [ ] Store traces in queryable format for post-hoc analysis

</details>

<details>
<summary>Governance Checklist</summary>

- [ ] Define who owns auto-improvement output
- [ ] Define promotion criteria: what goes from sandbox to production
- [ ] Establish revert protocol for production failures
- [ ] Create review cadence for optimization logs
- [ ] Build institutional knowledge transfer from experiment logs to human understanding

</details>

## Key Quotations

> "The magic is not in the agent's intelligence. It is in the constraints."

> "Being good at a domain and being good at improving at that domain are very different capabilities."

> "You cannot automate what you cannot score."

> "The organizations that win will not be the ones that move the fastest. They will be the ones that build the foundations that make the auto improvement worthwhile."

> "Speed without infrastructure is running your Ferrari into a ditch."

---

*Source: [Karpathy's Agent Ran 700 Experiments While He Slept](https://www.youtube.com/watch?v=xnG8h3UnNFI) by Nate B Jones, AI News & Strategy Daily (2026-04-18)*

## Spin-Offs

- [Beyond IT: Extending the Loop to Every Business Function](http://ubuntu4:3002/posts/beyond-it-extending-the-karpat/)
- [Taking the Loop to Client Environments](http://ubuntu4:3002/posts/taking-the-karpathy-loop-to-cl/)
- [The LLM-Wiki Pattern for MSP Knowledge Management](http://ubuntu4:3002/posts/the-llm-wiki-pattern-write-tim/)

**Tags**: ai-agents, auto-research, karpathy-loop, self-improvement, agent-harness, local-hard-takeoff, eval-infrastructure
**Categories**: AI Automation, Agent Architecture