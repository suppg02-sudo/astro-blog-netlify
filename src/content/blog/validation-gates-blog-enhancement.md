---
pubDatetime: 2026-03-04T07:48:25Z
title: "From Mandatory to Intelligent: Building Validation Gates for Blog Post Enhancement"
postSlug: "validation-gates-blog-enhancement"
description: "How we replaced rigid mandatory requirements with a 4-gate validation system that ensures visuals are added when appropriate—not forced."
tags:
  - automation
  - mermaid
  - triggers
  - hugo
  - quality-assurance
  - charts
  - validation
  - blog
---

The `bp` (Blog Post) trigger needed to solve a quality problem: blog posts were missing diagrams. The first fix worked, but it was too rigid. Here's how we evolved from "mandatory" to "intelligent."

## The Problem: Invisible Diagrams

A recent audit showed that blog posts with clear data patterns (flows, metrics, comparisons) were publishing without any visual enhancement. The `bp` trigger had a Visual Enhancement phase, but it was phrased as a suggestion:

> "Add visuals where they genuinely help."

The result: visuals were often skipped because "helpful" is subjective.

## First Fix: Mandatory Requirements

The initial solution was to make visual enhancement **mandatory** with hard requirements:

- **MUST** add Mermaid if flow exists
- **MUST** add Chart.js if data exists
- Checkboxes to force compliance

This worked—visuals started appearing—but it felt wrong. Some posts don't need diagrams. Forcing them creates visual slop.

## Second Fix: Validation Gates

{{< mermaid >}}
flowchart TD
    A[Missing Diagrams] --> B[Mandatory Requirements]
    B --> C{Too Rigid?}
    C -->|Yes| D[Validation Gates]
    D --> E[Gate 1: Flow Check]
    E --> F[Gate 2: Data Check]
    F --> G[Gate 3: Appropriateness]
    G --> H[Gate 4: Quality]
    H --> I[Documented Decision]
    I --> J[Smart Visual Enhancement]
{{< /mermaid >}}

The better solution: replace "mandatory" with **explicit decision gates** that force consideration without forcing compliance.

### The 4-Gate System

**Gate 1: Flow/Architecture Check**

Question: Does this post describe a process, system, or relationships that would be clearer as a diagram?

Answer explicitly:
- [ ] YES → Add Mermaid (select type)
- [ ] NO → Skip diagrams, move to Gate 2
- [ ] PARTIAL → Consider simplified diagram or skip

**Gate 2: Data Visualization Check**

Question: Does this post contain numeric data that would be clearer as a chart?

Answer explicitly:
- [ ] YES → Add Chart.js (select type)
- [ ] NO → Skip charts, move to Gate 3
- [ ] PARTIAL → Consider if table is clearer

**Gate 3: Appropriateness Check**

Even if visuals could be added, should they be?

Skip visuals if:
- Post is short (<100 lines) and visual would feel forced
- Data is already clear in a small table (2-3 rows)
- Flow is trivially simple (2 steps)
- Adding visual would just repeat what text explains

**Gate 4: Quality Check**

If adding visuals:
- Placed immediately after relevant section
- Not redundant with existing content
- Maximum 3 per post (unless data-heavy)
- Frontmatter flags added: `mermaid: true` / `charts: true`

### Decision Documentation

Before proceeding, state the decision:

```
Visual Enhancement Decision:
- Mermaid diagrams: [YES - type / NO - reason]
- Chart.js charts: [YES - type / NO - reason]
- Frontmatter flags: [mermaid: true/false, charts: true/false]
- Rationale: [1-2 sentences]
```

This creates accountability without rigidity.

## Work Completed This Session

{{< chart >}}
{
  type: 'bar',
  data: {
    labels: ['Posts Fixed', 'Instruction Files Updated', 'Validation Gates Designed', 'Test Posts Created'],
    datasets: [{
      label: 'Items',
      data: [4, 2, 4, 1],
      backgroundColor: ['#6366f1', '#22d3ee', '#a855f7', '#10b981'],
      borderWidth: 0
    }]
  },
  options: {
    plugins: {
      title: { display: true, text: 'Session Work Summary', color: '#e2e8f0' },
      legend: { display: false }
    },
    scales: {
      y: { grid: { color: '#334155' }, ticks: { color: '#e2e8f0' } },
      x: { grid: { display: false }, ticks: { color: '#e2e8f0' } }
    }
  }
}
{{< /chart >}}

| Item | Count | Details |
|------|-------|---------|
| Posts Fixed | 4 | Added missing diagrams, removed redundant titles |
| Instruction Files | 2 | bp.md, AGENTS.md updated |
| Validation Gates | 4 | Flow, Data, Appropriateness, Quality |
| Test Posts | 1 | Verified new system works |

## Why This Works Better

**Mandatory approach:**
- ✅ Ensures visuals are considered
- ❌ Forces visuals even when inappropriate
- ❌ No accountability for bad decisions

**Validation gate approach:**
- ✅ Ensures visuals are considered
- ✅ Allows skipping when appropriate
- ✅ Requires explicit reasoning
- ✅ Documents decision for review

The key insight: **forcing consideration** is different from **forcing compliance**. The gates ensure every post goes through a thoughtful evaluation, but the final decision respects context.

## YouTube Flow Comparison

The YouTube-to-blog flow has a similar issue at Phase 4:

> "Adds Mermaid diagram if themes suggest visual representation"

This is the same vague instruction we just fixed. The YouTube flow could benefit from the same validation gates—especially since video summaries often contain:
- Timelines (good for Mermaid)
- Topic distributions (good for charts)
- Process explanations (good for flowcharts)

But that's a future improvement. The bp trigger now has intelligent visual enhancement.

---

**Files Updated:**
- `~/.config/opencode/docs/instructions/triggers/bp.md` - Added 4-gate validation system
- `~/.config/opencode/AGENTS.md` - Updated bp trigger description

📁 File: http://ubuntu4:8080/editor/opencode/docs/instructions/triggers/bp.md