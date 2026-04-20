---
pubDatetime: 2026-03-04T07:30:48Z
title: "Enforcing Visual Excellence: Fixing the Blog Publishing Pipeline"
postSlug: "enforcing-visual-excellence-blog-fix"
description: "How we identified a failure in the 'bp' trigger flow, fixed missing diagrams across three posts, and updated the global instructions to make visual enhancement a mandatory checkpoint."
tags:
  - opencode
  - automation
  - mermaid
  - hugo
  - quality-assurance
  - charts
  - blog
---

The `bp` (Blog Post) trigger was designed to be a one-stop-shop for publishing session results. However, a recent audit revealed a gap: the **Visual Enhancement** phase was being skipped or ignored, leading to posts that were heavy on text but light on scannable visuals.

Today, we fixed that.

## The Problem: Invisible Diagrams

Despite having clear instructions in `bp.md` to add Mermaid diagrams and Chart.js visualizations, several recent posts were published without them. This happened because the instruction was phrased as a suggestion ("Add visuals where they genuinely help") rather than a mandatory requirement.

### The Fix Process

{{< mermaid >}}
flowchart TD
    A[Identify Missing Diagrams] --> B[Investigate bp.md Instructions]
    B --> C[Fix Existing Posts]
    C --> D[Update AGENTS.md with MANDATORY Flags]
    D --> E[Add Mandatory Checkpoint to bp.md]
    E --> F[Test Improved Trigger]
{{< /mermaid >}}

## Phase 1: Fixing the Backlog

We identified three major posts from today that were missing their promised visuals. Each was manually updated to include the diagrams and charts that the automated flow should have provided.

{{< chart >}}
{
  type: 'bar',
  data: {
    labels: ['Publishing Flow', 'OpenMemory Build', 'SlopCheck Report'],
    datasets: [{
      label: 'Visuals Added',
      data: [2, 2, 1],
      backgroundColor: ['#6366f1', '#22d3ee', '#a855f7'],
      borderWidth: 0
    }]
  },
  options: {
    plugins: {
      title: { display: true, text: 'Visual Enhancements Applied Today', color: '#e2e8f0' },
      legend: { display: false }
    },
    scales: {
      y: { grid: { color: '#334155' }, ticks: { color: '#e2e8f0' } },
      x: { grid: { display: false }, ticks: { color: '#e2e8f0' } }
    }
  }
}
{{< /chart >}}

| Post Title | Mermaid Added | Chart.js Added |
|------------|---------------|----------------|
| Context-Aware Blog Publishing Flow | ✅ Flowchart | ✅ Bar Chart |
| OpenMemory Intelligence System | ✅ Menu Structure | ✅ Context Doughnut |
| SlopCheck Report | ❌ (N/A) | ✅ Severity Bar |

## Phase 2: Updating the Protocols

To prevent future "visual slop," we updated the core instruction files.

### 1. AGENTS.md Update
The `bp` trigger description was updated to include:
> **Visual Enhancement (Phase 3.5 - MANDATORY)**: Auto-analyses content for mermaid diagrams and Chart.js charts — **MUST** add where data patterns match.

### 2. bp.md Mandatory Checkpoint
We added a hard checkpoint that every agent must pass before moving to the file creation phase:

1. Does this post describe a flow, pipeline, or architecture? → **If YES, add Mermaid.**
2. Does this post contain numeric data, distributions, or comparisons? → **If YES, add Chart.js.**
3. Did I add the corresponding `mermaid: true` or `charts: true` flags? → **MUST be YES.**

## Key Takeaways

- **Probabilistic vs. Deterministic**: Instructions like "add where helpful" are probabilistic. "MUST add when X pattern exists" is deterministic.
- **Visuals Matter**: Diagrams turn a wall of text into a scannable technical resource.
- **Always Verify**: The `bp` flow now includes a visual verification step to ensure the frontmatter flags and shortcodes are correctly applied.

---
*Post generated as a test of the improved `bp` trigger logic.*
📁 File: http://ubuntu4:8080/editor/docker/website/content/posts/2026-03-04-enforcing-visual-excellence-blog-fix.md