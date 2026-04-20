---
pubDatetime: 2026-04-04T22:11:02Z
title: "Paperclip multi-agent orchestration deep dive"
postSlug: "paperclip-validates-the-market-skills-are-the-supply-chain"
description: "Paperclip multi-agent orchestration deep dive"
tags:
  - others
---

# Paperclip Validates the Market — But Skills Are the Supply Chain

> **TL;DR**: Paperclip got 40,000 GitHub stars in 3 weeks for multi-agent orchestration. But orchestration without content is an empty shell. The real opportunity is being the **npm packages** that run inside the **Paperclip runtime** — typed, tested, factory-generated agent skills.

## Quick Summary

- Paperclip (40K GitHub stars) proves multi-agent orchestration has massive demand
- But Paperclip is the runtime, not the content — agents need workflows to run
- OpenCode's 71 skills, 5 factories, and research engine are the supply chain
- This reframes the relationship: not competitor, but **runtime + packages**
- Same pattern as Node.js (runtime) + npm (packages), Docker (runtime) + Docker Hub (images)

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHZpZXdCb3g9JzAgMCA3MjAgMzgwJyBzdHlsZT0nYmFja2dyb3VuZDojMGEwMDIwO2JvcmRlci1yYWRpdXM6MTJweDsnPgo8ZGVmcz4KICA8ZmlsdGVyIGlkPSdnJz48ZmVHYXVzc2lhbkJsdXIgc3RkRGV2aWF0aW9uPSczJyByZXN1bHQ9J2InLz48ZmVNZXJnZT48ZmVNZXJnZU5vZGUgaW49J2InLz48ZmVNZXJnZU5vZGUgaW49J1NvdXJjZUdyYXBoaWMnLz48L2ZlTWVyZ2U+PC9maWx0ZXI+CiAgPG1hcmtlciBpZD0nYScgbWFya2VyV2lkdGg9JzEwJyBtYXJrZXJIZWlnaHQ9JzcnIHJlZlg9JzknIHJlZlk9JzMuNScgb3JpZW50PSdhdXRvJz48cG9seWdvbiBwb2ludHM9JzAgMCwxMCAzLjUsMCA3JyBmaWxsPScjMDBmZmZmJy8+PC9tYXJrZXI+CjwvZGVmcz4KPHN0eWxlPnRleHR7Zm9udC1mYW1pbHk6c3lzdGVtLXVpLHNhbnMtc2VyaWY7ZmlsbDp3aGl0ZTtmb250LXNpemU6MTNweDt9LnR7ZmlsbDojMDBmZmZmO2ZvbnQtc2l6ZToxOHB4O2ZvbnQtd2VpZ2h0OmJvbGQ7fS5ze2ZpbGw6I2IzODhmZjtmb250LXNpemU6MTFweDt9PC9zdHlsZT4KCjx0ZXh0IHg9JzM2MCcgeT0nMzAnIHRleHQtYW5jaG9yPSdtaWRkbGUnIGNsYXNzPSd0Jz5UaGUgQUkgQWdlbnQgU3VwcGx5IENoYWluPC90ZXh0PgoKPHJlY3QgeD0nNDAnIHk9JzYwJyB3aWR0aD0nMjAwJyBoZWlnaHQ9JzcwJyByeD0nMTAnIGZpbGw9J25vbmUnIHN0cm9rZT0nI2ZmMDBmZicgc3Ryb2tlLXdpZHRoPScyJyBmaWx0ZXI9J3VybCgjZyknLz4KPHRleHQgeD0nMTQwJyB5PSc4NScgdGV4dC1hbmNob3I9J21pZGRsZScgZmlsbD0nI2ZmMDBmZicgZm9udC13ZWlnaHQ9J2JvbGQnPlBhcGVyY2xpcDwvdGV4dD4KPHRleHQgeD0nMTQwJyB5PScxMDUnIHRleHQtYW5jaG9yPSdtaWRkbGUnIGNsYXNzPSdzJz40MEsgc3RhcnMgwrcgRGFzaGJvYXJkIMK3IE9yY2hlc3RyYXRpb248L3RleHQ+Cgo8cmVjdCB4PSc0ODAnIHk9JzYwJyB3aWR0aD0nMjAwJyBoZWlnaHQ9JzcwJyByeD0nMTAnIGZpbGw9J25vbmUnIHN0cm9rZT0nIzAwZmY0MScgc3Ryb2tlLXdpZHRoPScyJyBmaWx0ZXI9J3VybCgjZyknLz4KPHRleHQgeD0nNTgwJyB5PSc4NScgdGV4dC1hbmNob3I9J21pZGRsZScgZmlsbD0nIzAwZmY0MScgZm9udC13ZWlnaHQ9J2JvbGQnPk9wZW5Db2RlPC90ZXh0Pgo8dGV4dCB4PSc1ODAnIHk9JzEwNScgdGV4dC1hbmNob3I9J21pZGRsZScgY2xhc3M9J3MnPjcxIFNraWxscyDCtyBTY2hlbWFzIMK3IEZhY3RvcmllcyDCtyBlUkFHPC90ZXh0PgoKPHJlY3QgeD0nMjAwJyB5PScyMDAnIHdpZHRoPSczMjAnIGhlaWdodD0nNjAnIHJ4PScxMCcgZmlsbD0nbm9uZScgc3Ryb2tlPScjZmZhYjAwJyBzdHJva2Utd2lkdGg9JzInIGZpbHRlcj0ndXJsKCNnKScvPgo8dGV4dCB4PSczNjAnIHk9JzIyNScgdGV4dC1hbmNob3I9J21pZGRsZScgZmlsbD0nI2ZmYWIwMCcgZm9udC13ZWlnaHQ9J2JvbGQnPlR5cGVkIFNraWxscyBhcyBQYWNrYWdlczwvdGV4dD4KPHRleHQgeD0nMzYwJyB5PScyNDUnIHRleHQtYW5jaG9yPSdtaWRkbGUnIGNsYXNzPSdzJz5TY2hlbWEtdmFsaWRhdGVkIMK3IEZhY3RvcnktZ2VuZXJhdGVkIMK3IFJlc2VhcmNoLWJhY2tlZDwvdGV4dD4KCjxyZWN0IHg9JzE2MCcgeT0nMzEwJyB3aWR0aD0nNDAwJyBoZWlnaHQ9JzUwJyByeD0nMTAnIGZpbGw9J25vbmUnIHN0cm9rZT0nIzAwYmZhNScgc3Ryb2tlLXdpZHRoPScxLjUnIGZpbHRlcj0ndXJsKCNnKScvPgo8dGV4dCB4PSczNjAnIHk9JzM0MCcgdGV4dC1hbmNob3I9J21pZGRsZScgZmlsbD0nIzAwYmZhNScgZm9udC1zaXplPScxNCcgZm9udC13ZWlnaHQ9J2JvbGQnPlNlbGYtSW1wcm92aW5nIEFnZW50IENvbXBhbnk8L3RleHQ+Cgo8bGluZSB4MT0nMjQwJyB5MT0nMTMwJyB4Mj0nMjgwJyB5Mj0nMjAwJyBzdHJva2U9JyNmZjAwZmYnIHN0cm9rZS13aWR0aD0nMS41JyBtYXJrZXItZW5kPSd1cmwoI2EpJy8+CjxsaW5lIHgxPSc0ODAnIHkxPScxMzAnIHgyPSc0NDAnIHkyPScyMDAnIHN0cm9rZT0nIzAwZmY0MScgc3Ryb2tlLXdpZHRoPScxLjUnIG1hcmtlci1lbmQ9J3VybCgjYSknLz4KPGxpbmUgeDE9JzM2MCcgeTE9JzI2MCcgeDI9JzM2MCcgeTI9JzMxMCcgc3Ryb2tlPScjZmZhYjAwJyBzdHJva2Utd2lkdGg9JzEuNScgbWFya2VyLWVuZD0ndXJsKCNhKScvPgoKPHRleHQgeD0nMTQwJyB5PSc1NScgdGV4dC1hbmNob3I9J21pZGRsZScgZmlsbD0nI2ZmMDBmZicgZm9udC1zaXplPScxMCc+UlVOVElNRTwvdGV4dD4KPHRleHQgeD0nNTgwJyB5PSc1NScgdGV4dC1hbmNob3I9J21pZGRsZScgZmlsbD0nIzAwZmY0MScgZm9udC1zaXplPScxMCc+UEFDS0FHRVM8L3RleHQ+Cjwvc3ZnPg==" alt="AI Agent Supply Chain" style="display:block;width:100%;max-width:680px;height:auto;margin:1.5rem auto;">

## What Paperclip Got Right

David Andre's video lays it out clearly. Paperclip solves the "dozens of terminals" problem:

- **Multi-agent dashboard** — see every task, decision, and dollar spent
- **24/7 VPS deployment** — agents work while you sleep
- **Any agent support** — Claude Code, Cline, OpenClaw, Codex — no vendor lock-in
- **Company structure** — board → CEO → departments, or flat like Nvidia
- **Completely free and open source**

40,000 stars in 3 weeks. That's not just hype — that's **validated market demand** for multi-agent systems.

## What Paperclip Is Missing

Here's the gap nobody in the video comments is talking about: **Paperclip runs agents, but what do those agents DO?**

An orchestrated team of agents without typed workflows is like a company where every employee reinvents their own processes from scratch every morning. The CEO agent says "build me a blog pipeline" and... what? Each agent interprets that differently. There are no schemas. No type system. No quality gates.

Paperclip gives you the org chart. It does not give you the **institutional knowledge**.

## Where OpenCode Fits

This is where the positioning shifts from "competitor" to "supply chain":

| Layer | Paperclip | OpenCode |
|-------|-----------|----------|
| **Runtime** | Dashboard, orchestration, VPS | — |
| **Type System** | — | Schemas (JSON Schema, Pydantic, Zod) |
| **Packages** | — | 71 tested skills |
| **Meta-Compiler** | — | 5 recursive factories |
| **Knowledge Store** | — | eRAG (pgvector + NetworkX) |
| **Quality Assurance** | — | Progressive disclosure, confidence tiers |

Paperclip is **Node.js**. OpenCode is **npm + TypeScript + the compiler**.

The analogy works because:
- Node.js without packages is just a runtime nobody uses
- Docker without images is just a container engine
- Paperclip without skills is just an empty dashboard

## The Commercial Play

Instead of competing with Paperclip, **become the content layer that makes Paperclip valuable**.

**Strategy**: Publish skills in a format Paperclip agents can consume. Every Paperclip user needs workflows — we have 71 of them, typed and tested.

The pitch to Paperclip users: "Your agents are orchestrated. Now give them **deterministic, tested workflows** instead of freeform prompts."

This is the same play npm made with Node.js:
1. Node.js created the runtime (free, open source)
2. npm created the package registry (free tier + paid private packages)
3. npm got acquired by GitHub for an undisclosed sum

Paperclip creates the runtime. We create the packages.

## What This Means for the Roadmap

The 6-month patient roadmap still holds, but with a clearer first target:

| Month | Focus | Output |
|-------|-------|--------|
| 1-2 | **Paperclip-compatible skill format** | Skills that install into Paperclip agents |
| 3-4 | **Community signal** | Watch Paperclip community adopt OpenCode skills |
| 5-6 | **Revenue experiment** | Premium skill packs for Paperclip users |

The immediate action: make our 71 skills installable in Paperclip. That's 71 reasons for 40,000 Paperclip users to discover OpenCode.

## The Bigger Picture

The AI agent market is splitting into layers, just like every mature software market:

```
Runtime Layer   → Paperclip, LangGraph, CrewAI (orchestration)
Package Layer   → OpenCode (typed skills, factories, research)
Foundation Layer → Claude, GPT, Gemini (models)
```

The runtime layer will be commoditised (open source, multiple options). The foundation layer already is (multiple model providers). The **package layer** is where value accumulates — because typed, tested, factory-generated workflows are genuinely hard to build, and they compound over time.

npm proved this. The pattern works.

<details>
<summary>Video Details</summary>

**Source**: [YouTube - David Andre](https://www.youtube.com/watch?v=rx4w6zhrhPY)
**Title**: Paperclip multi-agent orchestration deep dive
**Length**: ~59 minutes
**Transcript**: 8,959 words (ingested to eRAG project `journey-kits`)
**Key topics**: Paperclip setup, multi-agent orchestration, company structure, VPS deployment, agent comparison

</details>

<details>
<summary>Competitive Landscape Update (Post-Paperclip)</summary>

| Platform | Stars | Layer | Relationship to OpenCode |
|----------|-------|-------|--------------------------|
| **Paperclip** | 40,000 | Runtime | Complementary (runtime for our packages) |
| Sim Studio AI | 27,500 | Runtime | Competitor to Paperclip, not to us |
| Journey | ~3 | Format | kit.md spec (open, we can adopt) |
| GitHub MCP Registry | Official | Infrastructure | Different layer |
| obra/superpower | 500+ | Packages | Closest competitor, but no schemas/factories |

**Key insight**: Paperclip's explosion means 40,000 developers now need agent workflows. That's our addressable market.

</details>

**Tags**: paperclip, multi-agent, orchestration, supply-chain, npm-model, competitive-analysis
**Categories**: AI Automation, Business Strategy, Market Analysis