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
| **Model Empathy** | Same-model meta→task pairing outperforms cross-model. Shared weights = shared understanding. |

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3MjAgMzQwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiPgo8cmVjdCB3aWR0aD0iNzIwIiBoZWlnaHQ9IjM0MCIgZmlsbD0iIzBhMDAyMCIgcng9IjgiLz4KPHRleHQgeD0iMzYwIiB5PSIzMCIgZmlsbD0iIzAwZmZmZiIgZm9udC1zaXplPSIxNiIgZm9udC13ZWlnaHQ9IjcwMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+VGhlIEthcnBhdGh5IExvb3A6IEF1dG8tUmVzZWFyY2ggQXJjaGl0ZWN0dXJlPC90ZXh0Pgo8cmVjdCB4PSI2MCIgeT0iNzAiIHdpZHRoPSIxNjAiIGhlaWdodD0iNTAiIHJ4PSI2IiBmaWxsPSJub25lIiBzdHJva2U9IiMwMGZmZmYiIHN0cm9rZS13aWR0aD0iMiIvPgo8dGV4dCB4PSIxNDAiIHk9IjEwMCIgZmlsbD0iIzAwZmZmZiIgZm9udC1zaXplPSIxMyIgdGV4dC1hbmNob3I9Im1pZGRsZSI+MS4gUHJvcG9zZSBFZGl0PC90ZXh0Pgo8cmVjdCB4PSIyODAiIHk9IjcwIiB3aWR0aD0iMTYwIiBoZWlnaHQ9IjUwIiByeD0iNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjZmZhYjAwIiBzdHJva2Utd2lkdGg9IjIiLz4KPHRleHQgeD0iMzYwIiB5PSIxMDAiIGZpbGw9IiNmZmFiMDAiIGZvbnQtc2l6ZT0iMTMiIHRleHQtYW5jaG9yPSJtaWRkbGUiPjIuIFJ1biBFeHBlcmltZW50PC90ZXh0Pgo8cmVjdCB4PSI1MDAiIHk9IjcwIiB3aWR0aD0iMTYwIiBoZWlnaHQ9IjUwIiByeD0iNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMDBmZjQxIiBzdHJva2Utd2lkdGg9IjIiLz4KPHRleHQgeD0iNTgwIiB5PSIxMDAiIGZpbGw9IiMwMGZmNDEiIGZvbnQtc2l6ZT0iMTMiIHRleHQtYW5jaG9yPSJtaWRkbGUiPjMuIEV2YWx1YXRlIE1ldHJpYzwvdGV4dD4KPHBvbHlnb24gcG9pbnRzPSI1ODAsMTcwIDY0MCwyMTAgNTgwLDI1MCA1MjAsMjEwIiBmaWxsPSJub25lIiBzdHJva2U9IiNmZjAwZmYiIHN0cm9rZS13aWR0aD0iMiIvPgo8dGV4dCB4PSI1ODAiIHk9IjIxNCIgZmlsbD0iI2ZmMDBmZiIgZm9udC1zaXplPSIxMSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+SW1wcm92ZT88L3RleHQ+CjxyZWN0IHg9IjI4MCIgeT0iMTkwIiB3aWR0aD0iMTYwIiBoZWlnaHQ9IjUwIiByeD0iNiIgZmlsbD0iIzAwZmY0MTIwIiBzdHJva2U9IiMwMGZmNDEiIHN0cm9rZS13aWR0aD0iMiIvPgo8dGV4dCB4PSIzNjAiIHk9IjIxNSIgZmlsbD0iIzAwZmY0MSIgZm9udC1zaXplPSIxMyIgdGV4dC1hbmNob3I9Im1pZGRsZSI+Q29tbWl0IENoYW5nZTwvdGV4dD4KPHJlY3QgeD0iNjAiIHk9IjE5MCIgd2lkdGg9IjE2MCIgaGVpZ2h0PSI1MCIgcng9IjYiIGZpbGw9IiNmZjQwODEyMCIgc3Ryb2tlPSIjZmY0MDgxIiBzdHJva2Utd2lkdGg9IjIiLz4KPHRleHQgeD0iMTQwIiB5PSIyMTUiIGZpbGw9IiNmZjQwODEiIGZvbnQtc2l6ZT0iMTMiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlJldmVydDwvdGV4dD4KPGxpbmUgeDE9IjIyMCIgeTE9Ijk1IiB4Mj0iMjgwIiB5Mj0iOTUiIHN0cm9rZT0iIzAwZmZmZiIgc3Ryb2tlLXdpZHRoPSIyIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93KSIvPgo8bGluZSB4MT0iNDQwIiB5MT0iOTUiIHgyPSI1MDAiIHkyPSI5NSIgc3Ryb2tlPSIjZmZhYjAwIiBzdHJva2Utd2lkdGg9IjIiIG1hcmtlci1lbmQ9InVybCgjYXJyb3cpIi8+CjxsaW5lIHgxPSI1ODAiIHkxPSIxMjAiIHgyPSI1ODAiIHkyPSIxNzAiIHN0cm9rZT0iIzAwZmY0MSIgc3Ryb2tlLXdpZHRoPSIyIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93KSIvPgo8bGluZSB4MT0iNTIwIiB5MT0iMjEwIiB4Mj0iNDQwIiB5Mj0iMjE1IiBzdHJva2U9IiMwMGZmNDEiIHN0cm9rZS13aWR0aD0iMiIgbWFya2VyLWVuZD0idXJsKCNhcnJvdykiLz4KPGxpbmUgeDE9IjY0MCIgeTE9IjIxMCIgeDI9IjY4MCIgeTI9IjIxMCIgc3Ryb2tlPSIjZmY0MDgxIiBzdHJva2Utd2lkdGg9IjEuNSIvPgo8bGluZSB4MT0iNjgwIiB5MT0iMjEwIiB4Mj0iNjgwIiB5Mj0iMTU1IiBzdHJva2U9IiNmZjQwODEiIHN0cm9rZS13aWR0aD0iMS41Ii8+CjxsaW5lIHgxPSI2ODAiIHkxPSIxNTUiIHgyPSIxNDAiIHkyPSIxNTUiIHN0cm9rZT0iI2ZmNDA4MSIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KPGxpbmUgeDE9IjE0MCIgeTE9IjE1NSIgeDI9IjE0MCIgeTI9IjE5MCIgc3Ryb2tlPSIjZmY0MDgxIiBzdHJva2Utd2lkdGg9IjEuNSIgbWFya2VyLWVuZD0idXJsKCNhcnJvdykiLz4KPGxpbmUgeDE9IjE0MCIgeTE9IjI0MCIgeDI9IjE0MCIgeTI9IjI3MCIgc3Ryb2tlPSIjMDBmZmZmIiBzdHJva2Utd2lkdGg9IjEuNSIvPgo8bGluZSB4MT0iMTQwIiB5MT0iMjcwIiB4Mj0iMTQwIiB5Mj0iNzAiIHN0cm9rZT0iIzAwZmZmZjQ0IiBzdHJva2Utd2lkdGg9IjEuNSIgbWFya2VyLWVuZD0idXJsKCNhcnJvdykiLz4KPHJlY3QgeD0iNDAiIHk9IjI4MCIgd2lkdGg9IjY0MCIgaGVpZ2h0PSI0NSIgcng9IjQiIGZpbGw9IiNiMzg4ZmYxNSIgc3Ryb2tlPSIjYjM4OGZmIiBzdHJva2Utd2lkdGg9IjEiLz4KPHRleHQgeD0iMzYwIiB5PSIzMDAiIGZpbGw9IiNiMzg4ZmYiIGZvbnQtc2l6ZT0iMTIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtd2VpZ2h0PSI2MDAiPkNvbnN0cmFpbnRzOiAxIEZpbGUgfCAxIE1ldHJpYyB8IEZpeGVkIFRpbWUgQnVkZ2V0IHwgVmVyc2lvbiBDb250cm9sbGVkPC90ZXh0Pgo8dGV4dCB4PSIzNjAiIHk9IjMxNiIgZmlsbD0iI2IzODhmZjk5IiBmb250LXNpemU9IjEwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5LYXJwYXRoeTogNzAwIGV4cGVyaW1lbnRzIC8gMiBkYXlzID0gMTElIHNwZWVkdXAgfCBTaG9waWZ5OiAzNyBleHAgLyA4aHJzID0gMTklIGdhaW48L3RleHQ+CjxkZWZzPjxtYXJrZXIgaWQ9ImFycm93IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI2IiByZWZYPSI4IiByZWZZPSIzIiBvcmllbnQ9ImF1dG8iPjxwYXRoIGQ9Ik0wLDAgTDgsMyBMMCw2IiBmaWxsPSIjMDBmZmZmIi8+PC9tYXJrZXI+PC9kZWZzPgo8L3N2Zz4=" alt="Karpathy Loop Architecture" style="display:block;width:100%;max-width:680px;height:auto;margin:1.5rem auto;">

## The Core Pattern: Karpathy Loop

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

The escalation: Karpathy optimized training code. Auto-Agent optimizes the agent harness — system prompts, tool definitions, routing logic, orchestration strategy.

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3MjAgMzgwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiPgo8cmVjdCB3aWR0aD0iNzIwIiBoZWlnaHQ9IjM4MCIgZmlsbD0iIzBhMDAyMCIgcng9IjgiLz4KPHRleHQgeD0iMzYwIiB5PSIyOCIgZmlsbD0iIzAwZmZmZiIgZm9udC1zaXplPSIxNSIgZm9udC13ZWlnaHQ9IjcwMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+QXV0by1BZ2VudDogTWV0YS1BZ2VudCAvIFRhc2stQWdlbnQgU3BsaXQ8L3RleHQ+CjxyZWN0IHg9IjQwIiB5PSI1MCIgd2lkdGg9IjMwMCIgaGVpZ2h0PSIxNTAiIHJ4PSI4IiBmaWxsPSJub25lIiBzdHJva2U9IiNmZjAwZmYiIHN0cm9rZS13aWR0aD0iMiIvPgo8dGV4dCB4PSIxOTAiIHk9Ijc1IiBmaWxsPSIjZmYwMGZmIiBmb250LXNpemU9IjE0IiBmb250LXdlaWdodD0iNzAwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5NZXRhLUFnZW50IChIYXJuZXNzIEVuZ2luZWVyKTwvdGV4dD4KPHRleHQgeD0iMTkwIiB5PSIxMDAiIGZpbGw9IiNiMzg4ZmYiIGZvbnQtc2l6ZT0iMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlJlYWRzIGZhaWx1cmUgdHJhY2VzPC90ZXh0Pgo8dGV4dCB4PSIxOTAiIHk9IjExOCIgZmlsbD0iI2IzODhmZiIgZm9udC1zaXplPSIxMSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+TW9kaWZpZXMgc3lzdGVtIHByb21wdCArIHRvb2xzICsgcm91dGluZzwvdGV4dD4KPHRleHQgeD0iMTkwIiB5PSIxMzYiIGZpbGw9IiNiMzg4ZmYiIGZvbnQtc2l6ZT0iMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlJ1bnMgYmVuY2htYXJrIGFnYWluPC90ZXh0Pgo8dGV4dCB4PSIxOTAiIHk9IjE2MCIgZmlsbD0iIzAwYmZhNSIgZm9udC1zaXplPSIxMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+RW1lcmdlbnQ6IHNwb3QtY2hlY2tpbmcsIHZlcmlmaWNhdGlvbiBsb29wcyw8L3RleHQ+Cjx0ZXh0IHg9IjE5MCIgeT0iMTc1IiBmaWxsPSIjMDBiZmE1IiBmb250LXNpemU9IjEwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5mb3JtYXR0aW5nIHZhbGlkYXRvcnMsIHN1Yi1hZ2VudHM8L3RleHQ+CjxyZWN0IHg9IjM4MCIgeT0iNTAiIHdpZHRoPSIzMDAiIGhlaWdodD0iMTUwIiByeD0iOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMDBmZmZmIiBzdHJva2Utd2lkdGg9IjIiLz4KPHRleHQgeD0iNTMwIiB5PSI3NSIgZmlsbD0iIzAwZmZmZiIgZm9udC1zaXplPSIxNCIgZm9udC13ZWlnaHQ9IjcwMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+VGFzay1BZ2VudCAoRG9tYWluIFNwZWNpYWxpc3QpPC90ZXh0Pgo8dGV4dCB4PSI1MzAiIHk9IjEwMCIgZmlsbD0iIzkzYzVmZCIgZm9udC1zaXplPSIxMSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+RXhlY3V0ZXMgZG9tYWluIHRhc2tzPC90ZXh0Pgo8dGV4dCB4PSI1MzAiIHk9IjExOCIgZmlsbD0iIzkzYzVmZCIgZm9udC1zaXplPSIxMSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+UHJvZHVjZXMgcmVhc29uaW5nIHRyYWNlczwvdGV4dD4KPHRleHQgeD0iNTMwIiB5PSIxMzYiIGZpbGw9IiM5M2M1ZmQiIGZvbnQtc2l6ZT0iMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlJ1bnMgYWdhaW5zdCBiZW5jaG1hcmsgc3VpdGU8L3RleHQ+Cjx0ZXh0IHg9IjUzMCIgeT0iMTYwIiBmaWxsPSIjMDBiZmE1IiBmb250LXNpemU9IjEwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5TYW1lLW1vZGVsIHBhaXJpbmcgd29ya3MgYmVzdDwvdGV4dD4KPHRleHQgeD0iNTMwIiB5PSIxNzUiIGZpbGw9IiMwMGJmYTUiIGZvbnQtc2l6ZT0iMTAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPihDbGF1ZGUgbWV0YSDihpIgQ2xhdWRlIHRhc2spPC90ZXh0Pgo8bGluZSB4MT0iMzgwIiB5MT0iMTM1IiB4Mj0iMzQwIiB5Mj0iMTM1IiBzdHJva2U9IiNmZmFiMDAiIHN0cm9rZS13aWR0aD0iMiIgbWFya2VyLWVuZD0idXJsKCNhcnIyKSIvPgo8dGV4dCB4PSIzNjAiIHk9IjEyOCIgZmlsbD0iI2ZmYWIwMCIgZm9udC1zaXplPSI5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj50cmFjZXM8L3RleHQ+CjxsaW5lIHgxPSIzNDAiIHkxPSIxMTUiIHgyPSIzODAiIHkyPSIxMTUiIHN0cm9rZT0iIzAwZmY0MSIgc3Ryb2tlLXdpZHRoPSIyIiBtYXJrZXItZW5kPSJ1cmwoI2FycjIpIi8+Cjx0ZXh0IHg9IjM2MCIgeT0iMTA4IiBmaWxsPSIjMDBmZjQxIiBmb250LXNpemU9IjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiPmhhcm5lc3M8L3RleHQ+CjxyZWN0IHg9IjQwIiB5PSIyMzAiIHdpZHRoPSI2NDAiIGhlaWdodD0iNjAiIHJ4PSI2IiBmaWxsPSIjMDBmZjQxMTUiIHN0cm9rZT0iIzAwZmY0MSIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KPHRleHQgeD0iMzYwIiB5PSIyNTUiIGZpbGw9IiMwMGZmNDEiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI2MDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkNsYWltZWQgUmVzdWx0czogOTYuNSUgU3ByZWFkc2hlZXRCZW5jaCB8IDU1LjElIFRlcm1pbmFsQmVuY2g8L3RleHQ+Cjx0ZXh0IHg9IjM2MCIgeT0iMjc1IiBmaWxsPSIjMDBmZjQxOTkiIGZvbnQtc2l6ZT0iMTAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkZpcnN0IHBsYWNlIG9uIGJvdGggKHVudmVyaWZpZWQgYXMgb2YgdmlkZW8gZGF0ZSk8L3RleHQ+CjxyZWN0IHg9IjQwIiB5PSIzMTAiIHdpZHRoPSIyMDAiIGhlaWdodD0iNTUiIHJ4PSI0IiBmaWxsPSIjZmY0MDgxMTUiIHN0cm9rZT0iI2ZmNDA4MSIgc3Ryb2tlLXdpZHRoPSIxIi8+Cjx0ZXh0IHg9IjE0MCIgeT0iMzMwIiBmaWxsPSIjZmY0MDgxIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNjAwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5NZXRyaWMgR2FtaW5nPC90ZXh0Pgo8dGV4dCB4PSIxNDAiIHk9IjM0OCIgZmlsbD0iI2ZmNDA4MTk5IiBmb250LXNpemU9IjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkFnZW50IG9wdGltaXplcyBwcm94eSwgbm90IHZhbHVlPC90ZXh0Pgo8cmVjdCB4PSIyNjAiIHk9IjMxMCIgd2lkdGg9IjIwMCIgaGVpZ2h0PSI1NSIgcng9IjQiIGZpbGw9IiNmZmFiMDAxNSIgc3Ryb2tlPSIjZmZhYjAwIiBzdHJva2Utd2lkdGg9IjEiLz4KPHRleHQgeD0iMzYwIiB5PSIzMzAiIGZpbGw9IiNmZmFiMDAiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI2MDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlNpbGVudCBEZWdyYWRhdGlvbjwvdGV4dD4KPHRleHQgeD0iMzYwIiB5PSIzNDgiIGZpbGw9IiNmZmFiMDA5OSIgZm9udC1zaXplPSI5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5Qb2xpY3kgZHJpZnQgdW5kZXRlY3RlZDwvdGV4dD4KPHJlY3QgeD0iNDgwIiB5PSIzMTAiIHdpZHRoPSIyMDAiIGhlaWdodD0iNTUiIHJ4PSI0IiBmaWxsPSIjYjM4OGZmMTUiIHN0cm9rZT0iI2IzODhmZiIgc3Ryb2tlLXdpZHRoPSIxIi8+Cjx0ZXh0IHg9IjU4MCIgeT0iMzMwIiBmaWxsPSIjYjM4OGZmIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNjAwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5Db21wb3VuZGluZyBFcnJvcnM8L3RleHQ+Cjx0ZXh0IHg9IjU4MCIgeT0iMzQ4IiBmaWxsPSIjYjM4OGZmOTkiIGZvbnQtc2l6ZT0iOSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+QmFkIG9wdCBjYXNjYWRlcyB0byBzeXN0ZW1zPC90ZXh0Pgo8ZGVmcz48bWFya2VyIGlkPSJhcnIyIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI2IiByZWZYPSI4IiByZWZZPSIzIiBvcmllbnQ9ImF1dG8iPjxwYXRoIGQ9Ik0wLDAgTDgsMyBMMCw2IiBmaWxsPSIjZmZhYjAwIi8+PC9tYXJrZXI+PC9kZWZzPgo8L3N2Zz4=" alt="Auto-Agent Architecture" style="display:block;width:100%;max-width:680px;height:auto;margin:1.5rem auto;">

### Key Design Decisions

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

You cannot skip steps. Auto-improvement is a graduate-level capability when most orgs are struggling with agents 101.

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3MjAgMzYwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLHNhbnMtc2VyaWYiPgo8cmVjdCB3aWR0aD0iNzIwIiBoZWlnaHQ9IjM2MCIgZmlsbD0iIzBhMDAyMCIgcng9IjgiLz4KPHRleHQgeD0iMzYwIiB5PSIyOCIgZmlsbD0iIzAwZmZmZiIgZm9udC1zaXplPSIxNSIgZm9udC13ZWlnaHQ9IjcwMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+QXV0by1JbXByb3ZlbWVudCBSZWFkaW5lc3MgU3RhaXJjYXNlPC90ZXh0Pgo8IS0tIFN0YWlycyAtLT4KPHJlY3QgeD0iNDAiIHk9IjI4MCIgd2lkdGg9IjEyMCIgaGVpZ2h0PSI1MCIgcng9IjQiIGZpbGw9IiNmZjQwODEyMCIgc3Ryb2tlPSIjZmY0MDgxIiBzdHJva2Utd2lkdGg9IjEuNSIvPgo8dGV4dCB4PSIxMDAiIHk9IjMwMiIgZmlsbD0iI2ZmNDA4MSIgZm9udC1zaXplPSIxMCIgZm9udC13ZWlnaHQ9IjYwMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+Q29udGV4dCBMYXllcjwvdGV4dD4KPHRleHQgeD0iMTAwIiB5PSIzMTgiIGZpbGw9IiNmZjQwODE5OSIgZm9udC1zaXplPSI4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5zdHJ1Y3R1cmVkIG1lbW9yeTwvdGV4dD4KPHJlY3QgeD0iMTgwIiB5PSIyMzAiIHdpZHRoPSIxMjAiIGhlaWdodD0iNTAiIHJ4PSI0IiBmaWxsPSIjZmZhYjAwMjAiIHN0cm9rZT0iI2ZmYWIwMCIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KPHRleHQgeD0iMjQwIiB5PSIyNTIiIGZpbGw9IiNmZmFiMDAiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSI2MDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkV2YWwgSGFybmVzczwvdGV4dD4KPHRleHQgeD0iMjQwIiB5PSIyNjgiIGZpbGw9IiNmZmFiMDA5OSIgZm9udC1zaXplPSI4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5zY29yaW5nIGZ1bmN0aW9uczwvdGV4dD4KPHJlY3QgeD0iMzIwIiB5PSIxODAiIHdpZHRoPSIxMjAiIGhlaWdodD0iNTAiIHJ4PSI0IiBmaWxsPSIjYjM4OGZmMjAiIHN0cm9rZT0iI2IzODhmZiIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KPHRleHQgeD0iMzgwIiB5PSIyMDIiIGZpbGw9IiNiMzg4ZmYiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSI2MDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlNhbmRib3ggRW52PC90ZXh0Pgo8dGV4dCB4PSIzODAiIHk9IjIxOCIgZmlsbD0iI2IzODhmZjk5IiBmb250LXNpemU9IjgiIHRleHQtYW5jaG9yPSJtaWRkbGUiPnNhZmUgZXhwZXJpbWVudGF0aW9uPC90ZXh0Pgo8cmVjdCB4PSI0NjAiIHk9IjEzMCIgd2lkdGg9IjEyMCIgaGVpZ2h0PSI1MCIgcng9IjQiIGZpbGw9IiMwMGZmZmYyMCIgc3Ryb2tlPSIjMDBmZmZmIiBzdHJva2Utd2lkdGg9IjEuNSIvPgo8dGV4dCB4PSI1MjAiIHk9IjE1MiIgZmlsbD0iIzAwZmZmZiIgZm9udC1zaXplPSIxMCIgZm9udC13ZWlnaHQ9IjYwMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+S2FycGF0aHkgVHJpcGxldDwvdGV4dD4KPHRleHQgeD0iNTIwIiB5PSIxNjgiIGZpbGw9IiMwMGZmZmY5OSIgZm9udC1zaXplPSI4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5maWxlICsgbWV0cmljICsgYnVkZ2V0PC90ZXh0Pgo8cmVjdCB4PSI2MDAiIHk9IjgwIiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjUwIiByeD0iNCIgZmlsbD0iIzAwZmY0MTIwIiBzdHJva2U9IiMwMGZmNDEiIHN0cm9rZS13aWR0aD0iMS41Ii8+Cjx0ZXh0IHg9IjY1MCIgeT0iMTAyIiBmaWxsPSIjMDBmZjQxIiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iNjAwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5BdXRvLUltcHJvdmU8L3RleHQ+Cjx0ZXh0IHg9IjY1MCIgeT0iMTE4IiBmaWxsPSIjMDBmZjQxOTkiIGZvbnQtc2l6ZT0iOCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+bG9vcCBydW5uaW5nPC90ZXh0Pgo8IS0tIEFycm93IGFsb25nIHN0YWlycyAtLT4KPHBvbHlsaW5lIHBvaW50cz0iMTYwLDMwNSAxODAsMjU1IDMwMCwyMDUgNDQwLDE1NSA1ODAsMTA1IiBmaWxsPSJub25lIiBzdHJva2U9IiMwMGJmYTUiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWRhc2hhcnJheT0iNiwzIi8+CjwhLS0gTGFiZWxzIC0tPgo8dGV4dCB4PSIzNjAiIHk9IjYwIiBmaWxsPSIjZmY0MDgxIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNjAwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5Nb3N0IG9yZ3MgYXJlIGhlcmU8L3RleHQ+CjxsaW5lIHgxPSIyODAiIHkxPSI2NSIgeDI9IjQ0MCIgeTI9IjY1IiBzdHJva2U9IiNmZjQwODEiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iMywzIi8+Cjx0ZXh0IHg9IjYyMCIgeT0iNjAiIGZpbGw9IiMwMGZmNDEiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI2MDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlRoZSBwcml6ZTwvdGV4dD4KPCEtLSBGYWlsdXJlIHBhdHRlcm5zIC0tPgo8cmVjdCB4PSI0MCIgeT0iMTQwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjExMCIgcng9IjYiIGZpbGw9IiNmZjQwODExMCIgc3Ryb2tlPSIjZmY0MDgxNjYiIHN0cm9rZS13aWR0aD0iMSIvPgo8dGV4dCB4PSIxNDAiIHk9IjE2MCIgZmlsbD0iI2ZmNDA4MSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjYwMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+Q29tbW9uIEZhaWx1cmVzPC90ZXh0Pgo8dGV4dCB4PSIxNDAiIHk9IjE4MCIgZmlsbD0iI2ZmNDA4MTk5IiBmb250LXNpemU9IjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiPk5vIHN0cnVjdHVyZWQgbWVtb3J5PC90ZXh0Pgo8dGV4dCB4PSIxNDAiIHk9IjE5NiIgZmlsbD0iI2ZmNDA4MTk5IiBmb250LXNpemU9IjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiPk1lYXN1cmluZyBhY3Rpdml0eSBub3Qgb3V0Y29tZTwvdGV4dD4KPHRleHQgeD0iMTQwIiB5PSIyMTIiIGZpbGw9IiNmZjQwODE5OSIgZm9udC1zaXplPSI5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5ObyBldmFsIGluZnJhc3RydWN0dXJlPC90ZXh0Pgo8dGV4dCB4PSIxNDAiIHk9IjIyOCIgZmlsbD0iI2ZmNDA4MTk5IiBmb250LXNpemU9IjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkdvdmVybmFuY2UgdmFjdXVtPC90ZXh0Pgo8IS0tIEtleSBpbnNpZ2h0IC0tPgo8cmVjdCB4PSIzMDAiIHk9IjI5MCIgd2lkdGg9IjM4MCIgaGVpZ2h0PSI1NSIgcng9IjYiIGZpbGw9IiMwMGJmYTUxNSIgc3Ryb2tlPSIjMDBiZmE1IiBzdHJva2Utd2lkdGg9IjEiLz4KPHRleHQgeD0iNDkwIiB5PSIzMTIiIGZpbGw9IiMwMGJmYTUiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlNtYWxsIHRlYW1zICgzLTUgcGVvcGxlKSBoYXZlIHN0cnVjdHVyYWwgYWR2YW50YWdlPC90ZXh0Pgo8dGV4dCB4PSI0OTAiIHk9IjMzMCIgZmlsbD0iIzAwYmZhNTk5IiBmb250LXNpemU9IjEwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5LYXJwYXRoeTogMSBwZXJzb24gfCBTa3lQaWxvdDogJDMwMCBjb21wdXRlIHwgQXV0by1BZ2VudDogdGlueSBZQyBzdGFydHVwPC90ZXh0Pgo8L3N2Zz4=" alt="Readiness Staircase" style="display:block;width:100%;max-width:680px;height:auto;margin:1.5rem auto;">

### Prerequisites (In Order)

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