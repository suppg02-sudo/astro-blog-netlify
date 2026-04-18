---
pubDatetime: 2026-04-18T19:00:00Z
title: "The LLM-Wiki Pattern: Write-Time Knowledge Compilation for MSPs"
postSlug: "the-llm-wiki-pattern-write-tim"
description: "The LLM-Wiki Pattern: Write-Time Knowledge Compilation for MSPs"
tags:
  - msp
---

Most MSPs have a knowledge problem masquerading as a tooling problem. You buy a better PSA, a smarter RMM, a fancier documentation platform. None of it fixes the core issue: the gap between what your team collectively knows about a client's environment and what any individual technician can access when they need it.

Karpathy's LLM-wiki concept offers a different approach. Instead of searching through raw data when you need an answer — the query-time synthesis approach that most RAG systems use — you continuously compile raw data into structured wiki entries at write time. Each entry is synthesised, cross-referenced, and maintained by an LLM. The wiki becomes a living knowledge base that compounds over time.

For MSPs managing dozens of client environments, this pattern solves the knowledge problem that kills most managed service engagements: the context gap between what the MSP knows and what the client environment actually needs.

## Per-Client Knowledge Compounding

Every ticket resolution, every incident, every project generates knowledge. But most MSPs store this as ticket comments, email threads, and technician notes that nobody reads. The knowledge exists, but it's entombed.

The LLM-wiki pattern compiles this into structured per-client wiki entries automatically.

Here's what that looks like in practice. A technician resolves a VPN issue at Client A. The ticket closes. Normally, that knowledge is buried in a ticket that nobody will ever search for. With the wiki pattern, the LLM reads the ticket, extracts the resolution, cross-references it with the client's existing wiki entry for VPN configuration, and updates the entry.

Next time a VPN issue occurs at Client A, the context layer already knows: "Client A uses Fortinet. Their VPN drops when the ISP switches routes. The fix is to add a persistent keepalive to the tunnel config. This has happened 4 times in the last year."

The wiki compounds. Each resolution adds a layer. Each layer makes the next resolution faster. After 12 months, the MSP has a deeper understanding of each client's environment than any individual technician could maintain — because no individual technician remembers every interaction across every system. The wiki does.

This is not documentation. Documentation is what you write because someone told you to. This is compiled operational knowledge — extracted from the actual work, not from someone's memory of the work after the fact.

## Cross-Client Pattern Mining

The wiki doesn't just work per-client. It works across clients.

The LLM spots patterns that no human would catch because no human sees the full picture. "This Fortinet VPN keepalive issue at Client A? It also appeared at Client D and Client G. All three use the same ISP. The wiki entry now includes a cross-client note: 'Pattern detected across 3 clients using ISP-X with Fortinet devices. Consider proactive keepalive config for all Fortinet clients on ISP-X.'"

This is intelligence that no individual technician could spot because no individual technician works across all three environments. The wiki becomes a pattern recognition engine across the MSP's entire client base.

The pattern types are broader than you'd think:

| Pattern Type | Example | Value |
|---|---|---|
| Patch-related | Same patch broke same app at 3 clients | Proactive patch blocking for remaining clients |
| Vendor-specific | Same vendor config drift at multiple clients | Standardised remediation SOP |
| Seasonal | Alert spikes at specific times across similar clients | Pre-emptive threshold adjustments |
| Infrastructure | Same hardware failure mode across client base | Bulk warranty/replacement planning |
| Security | Same attack vector attempted at multiple clients | Immediate threat intel distribution |

Each pattern detected is a competitive advantage. The MSP that knows "ISP-X causes VPN drops on Fortinet devices" can proactively fix that for every client before it becomes an incident. The MSP that doesn't know this discovers it one ticket at a time, over months, across multiple technicians, none of whom connect the dots.

Cross-client pattern mining is the single most valuable capability the LLM-wiki provides, because it transforms scattered operational noise into actionable intelligence.

## Client Self-Service Portal

The wiki isn't just for the MSP. Clients get access to their own knowledge base.

Not the raw tickets — that would be overwhelming and largely meaningless to a non-technical audience. The synthesised wiki entries. A client logs in and sees:

- **Your IT Environment Overview** — what you have, how it's connected, what's ageing
- **Recent Resolutions** — what broke, what was fixed, what the root cause was
- **Known Issues and Workarounds** — active problems with temporary mitigations
- **Infrastructure Health Trends** — are things getting better or worse over time
- **Upcoming Maintenance Recommendations** — what should be replaced, upgraded, or reconfigured before it fails

This transforms the MSP relationship from "we fix things when they break" to "we maintain and evolve your IT knowledge continuously." It's a fundamentally different value proposition.

Most MSP quarterly business reviews consist of a technician reading ticket stats from a slide. "You had 47 tickets this quarter, average resolution time 2.3 hours." The client nods. Nobody learns anything. The LLM-wiki turns that review into: "Here's what we learned about your environment this quarter. Here are the patterns we've detected. Here's what we recommend you do before it becomes a problem."

One is a report. The other is intelligence. Clients pay more for intelligence.

## Architecture Overview

The system has three layers — raw data ingestion, compilation, and output:

```
Raw Data Sources          Compilation Engine           Wiki Output
┌──────────────┐     ┌──────────────────────┐     ┌──────────────────┐
│ PSA tickets   │────>│                      │────>│ Per-client wiki   │
│ RMM alerts    │────>│ LLM wiki compiler    │────>│ Cross-client wiki │
│ Incident logs │────>│ (runs nightly)       │────>│ Client portal     │
│ Change records│────>│ Deduplication        │────>│ MSP internal KB   │
│ Project docs  │────>│ Cross-referencing    │────>│ Pattern alerts    │
│ SOPs          │────>│ Pattern detection    │────>│ Improvement feed  │
└──────────────┘     └──────────────────────┘     └──────────────────┘
```

The compilation engine runs nightly. It ingests new tickets, alerts, incidents, and changes from the past 24 hours. It deduplicates (the same issue across three tickets is one entry). It cross-references (does this resolution relate to an existing wiki entry?). It detects patterns (has this issue appeared elsewhere?). It updates the wiki.

The key design decision is that compilation happens on a schedule, not on demand. This is what makes it different from RAG.

## Write-Time Compilation vs Query-Time Synthesis

Most AI knowledge systems in the MSP space are query-time synthesis — you ask a question, the system searches through raw data, and an LLM synthesises an answer on the spot. RAG systems work this way. It's useful for ad-hoc questions. It's terrible for continuous operational improvement.

| Dimension | Write-Time Wiki | Query-Time RAG |
|-----------|----------------|----------------|
| When knowledge is structured | At ingestion, continuously | At query time, on demand |
| Cost per query | Low (pre-compiled) | High (LLM synthesis every time) |
| Quality of cross-references | High (maintained over time) | Variable (depends on retrieval quality) |
| Compound effect | Yes — each entry enriches previous entries | No — each query starts fresh |
| Suitable for MSP context | Yes — scheduled compilation from ticket/alert streams | Partially — good for ad-hoc questions, bad for continuous improvement |
| Editorial control | Human reviews wiki entries before publication | None — output is generated on the fly |

The compound effect is the critical difference. A RAG system answering "why does Client A's VPN keep dropping?" searches tickets, finds a few relevant ones, and synthesises an answer. The next time someone asks the same question, it searches again and synthesises again. Nothing compounds. The LLM-wiki, by contrast, has already compiled that answer into the Client A VPN entry. The query is instant, the cost is near-zero, and the answer has been refined over multiple incidents.

Editorial control matters too. With write-time compilation, a human reviews wiki entries before they're published. With query-time synthesis, the output is generated on the fly and nobody reviews it. For an MSP putting knowledge in front of clients, that distinction is the difference between professionalism and liability.

## The Connection to the Karpathy Loop

The wiki is the context layer that makes the auto-improvement loop work.

Without it, the agent operates blind. It doesn't know what's been tried before, what failed, what worked, or what the client's environment looks like. Every cycle starts from scratch. The loop degrades into a very expensive way to reinvent wheels.

With it, the agent has the accumulated operational wisdom of every technician who has ever worked on that client, synthesised and cross-referenced. The loop becomes genuinely intelligent because it has genuine context.

The relationship is bidirectional:

1. **The wiki feeds the loop.** When the agent starts a cycle — resolving an incident, executing a change, responding to an alert — it reads the relevant wiki entries first. It knows the client's history, their known issues, their infrastructure quirks, their past failures and successes.

2. **The loop feeds the wiki.** Each resolution the loop produces becomes a new wiki entry. Each pattern it detects gets cross-referenced. Each change it makes updates the client's infrastructure documentation. The wiki grows richer with every cycle.

This is the compound effect at its most powerful. The loop makes the wiki better. The wiki makes the loop better. After 6 months of running both together, the MSP has something that no competitor can replicate: deep, structured, continuously-updated knowledge about every client environment, coupled with an automated system that uses that knowledge to resolve issues faster than any human could.

## The Ultimate Lock-In

The MSP that builds an LLM-wiki across its client base is not just running auto-improvement loops. It is building the most valuable asset any managed service provider can have: deep, structured, compounding knowledge about its clients' environments.

That knowledge is not replicable by a competitor. A competitor can match your tooling, your pricing, your SLAs. They cannot match 18 months of compiled operational intelligence about each client's specific environment.

It is not portable if the client leaves. The wiki belongs to the MSP's compilation engine. The client can take their tickets and their documentation — the raw data. But the synthesised, cross-referenced, pattern-enriched knowledge base is a product of your specific compilation process. It doesn't transfer.

This is the ultimate lock-in. But it is lock-in built on genuine value, not contract terms. The client stays not because they're contractually obligated to, but because no other MSP understands their environment as deeply as you do. And that understanding deepens every single day.

---

**This is part of the Karpathy Loop for MSPs series:**

- [Part 1: The Karpathy Loop for MSPs — When Half the Industry Already Has One](http://ubuntu4:3002/posts/the-karpathy-loop-for-msps-whe/)
- [Part 2: When Your Sister Company Already Runs the Loop](http://ubuntu4:3002/posts/when-your-sister-company-alrea/)
- [Part 3: SOPs Are the Program.md — Why Standard Operating Procedures Are the New Source Code](http://ubuntu4:3002/posts/sops-are-the-program-md-why-st/)
- [Part 4: The Microsoft MSP Dilemma — Building on Someone Else's Platform](http://ubuntu4:3002/posts/the-microsoft-msp-dilemma-buil/)
- [Part 5: From Riding Microsoft to Owning the Stack](http://ubuntu4:3002/posts/from-riding-microsoft-to-ownin/)
- [Reference: The Karpathy Loop Reference Guide](http://ubuntu4:3002/posts/the-karpathy-loop-reference-guide/)
- [Beyond IT: Extending the Loop to Every Business Function](http://ubuntu4:3002/posts/beyond-it-extending-the-karpat/)
- [Taking the Loop to Client Environments](http://ubuntu4:3002/posts/taking-the-karpathy-loop-to-cl/)
- [The LLM-Wiki Pattern for MSP Knowledge Management](http://ubuntu4:3002/posts/the-llm-wiki-pattern-write-tim/)

**Tags**: karpathy-loop, msp, llm-wiki, knowledge-management, ai-agents, rag, write-time-compilation, managed-services

**Categories**: AI Strategy, MSP Operations, Knowledge Engineering