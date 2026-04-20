---
pubDatetime: 2026-04-10T10:00:00Z
title: "The IP Problem With AI Architecture Patterns"
postSlug: "the-ip-problem-with-ai-archite"
description: "The IP Problem With AI Architecture Patterns"
tags:
  - others
---

I spent three sessions designing a generative schema hierarchy. Four tiers: seed, factory, domain, instance. An audit loop that flows findings upward and improves the system autonomously. Two factory schemas with generation rules, instance schemas, and escalation thresholds. Over 1,600 lines of JSON Schema. Then I realised something uncomfortable: none of it is protectable.

## The Trap

Here's the pattern I built. A seed schema defines universal types — identity, lifecycle, audit specification, agent interface. Factories inherit those types and add domain-specific generation rules. Domains are schemas produced by factories for specific use cases. Instances are concrete items created from domains. An audit loop at every tier checks quality, escalates recurring findings upward, and refines the factory that produced the failing instance.

Sounds clever, right? It is. It's also an abstract idea. You cannot copyright an idea. You cannot patent a four-tier hierarchy — that's just meta-programming with extra steps. Anyone who reads this paragraph can implement it in an afternoon.

This is the central tension of building AI infrastructure in 2026: the most valuable thing you can design is also the hardest to defend.

## Why I Built It Anyway

I didn't build the schema hierarchy to own a pattern. I built it because I was drowning in complexity. My system has 81 skills, 36 deferred tasks, a PostgreSQL memory store with 2,800+ entries, a menu optimization engine, a prompt library with signal tracking, and a blog pipeline that auto-publishes daily analysis. Without structure, it collapses under its own weight.

The schema hierarchy gave me something I couldn't get from a simpler approach: **self-improvement as a structural property, not a feature I bolt on**. Every instance carries an audit spec. Every audit finding can escalate to the factory that produced it. The factory's `improvement_log` is append-only institutional memory. Over time, the factories get better because the instances report what went wrong.

That's not a patentable invention. It's the principle of feedback loops applied to schema design. Kaizen for JSON.

## Where the Actual Moat Lives

If the pattern isn't the moat, what is?

**The data.** My research factory has been running long enough that its `improvement_log` contains real findings from real research instances. "Source quality scoring was too lenient on Medium articles" — that's a finding. "Cross-reference checks miss oblique connections" — that's another. Each finding refines the factory's generation rules. The rules are specific to my domain, my sources, my quality thresholds.

Nobody cloning the pattern gets that data. They get an empty vessel.

**The running system.** The schema hierarchy is the skeleton. The 81 skills, the memory system, the menu optimizer, the signal tracking — that's the organism. The skeleton is reproducible. The organism took months to grow.

**The audit trail.** Every significant decision is logged: which factory was selected, which generation rules were applied, what the user decided, what the audit found. That decision trail is irreplaceable. It's the difference between a system that knows why it does things and one that just does them.

## The Open-Core Calculus

I've settled on this strategy: the seed schema is open. The concept is out there — I'm writing about it right now. The factories, the generation rules, the specific audit criteria, the improvement logs — those stay private. They're the proprietary layer.

This is the Red Hat model applied to AI infrastructure. The kernel (the pattern) is free. The distribution (the tuned factories, the running service, the accumulated data) is the product.

Open-core works when three conditions are met:

1. **The open layer is genuinely useful on its own.** The seed schema is. You can build your own factories on it. You'll just start with empty improvement logs.
2. **The proprietary layer compounds over time.** The audit loop ensures that. Every day the factories run, they get better. A new entrant starts from zero.
3. **Network effects are possible.** If multiple users run instances through the same factories, the improvement data compounds faster. That's the platform play.

## What I'd Tell Someone Starting From Scratch

Don't design the perfect schema hierarchy first. That's the trap I fell into — three sessions of beautiful JSON Schema that hasn't served a single user yet.

Start with one factory. Pick the thing you do most — for me it's research. Build the instance schema, the generation rules, the audit criteria. Run real instances through it. Let the audit loop find problems. Refine the factory based on real findings. Then extract the common patterns into a seed schema.

The seed is the last thing you generalise, not the first thing you design. I built mine top-down. In retrospect, bottom-up would have been faster and the result would have been grounded in actual usage rather than theoretical elegance.

## The Honest Assessment

My schema hierarchy is well-designed. It's also undeployed. It lives in an Upload folder, not in production. The inference cluster it's supposed to serve doesn't exist yet — I don't have a GPU. The blog posts it's supposed to generate go through a different pipeline (Astro + Directus, not the publishing factory).

The pattern is sound. The implementation is theoretical. The moat is the data I'll accumulate once I actually run instances through it. Until then, the "IP" is worth exactly what anyone would pay for a well-structured idea: nothing.

That's not discouraging. That's clarifying. The value isn't in the design. It's in the running.

**Tags**: ip-strategy, ai-architecture, schema-design, open-core, aimplifi
**Categories**: AI Automation, Opinion, Architecture