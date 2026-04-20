---
pubDatetime: 2026-01-21T00:00:00Z
title: "Mermaid Working Test"
postSlug: "mermaid-working"
description: "Mermaid Working Test"
tags:
  - others
---

# Mermaid and Chart Rendering Test

This post verifies that both mermaid diagrams and Chart.js are working correctly in our new Astro theme.

## 1. Mermaid Flowchart

```mermaid
graph TD
    A[Start] --> B{Does it work?}
    B -->|Yes| C[Happy User]
    B -->|No| D[Debug Mode]
    C --> E[Success]
    D --> B
```

## 2. Chart.js Bar Chart

Here is a dynamic chart rendered from a JSON code block:

```chart
{
  "type": "bar",
  "data": {
    "labels": ["January", "February", "March", "April"],
    "datasets": [{
      "label": "Simulated Growth",
      "data": [12, 19, 3, 5],
      "backgroundColor": "rgba(74, 144, 226, 0.5)",
      "borderColor": "rgba(74, 144, 226, 1)",
      "borderWidth": 1
    }]
  },
  "options": {
    "responsive": true,
    "maintainAspectRatio": false,
    "scales": {
      "y": {
        "beginAtZero": true
      }
    }
  }
}
```

## 3. Hugo Shortcode Compatibility

{{< mermaid >}}
graph LR
    X[Astro] --> Y[Directus]
    Y --> Z[Success]
{{< /mermaid >}}

If you see a flowchart, a bar chart, and another flowchart above, then everything is working perfectly!