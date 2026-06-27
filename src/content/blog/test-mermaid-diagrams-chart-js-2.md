---
draft: true
pubDatetime: 2026-03-25T12:00:00Z
title: "Test: Mermaid Diagrams & Chart.js"
postSlug: "test-mermaid-diagrams-chart-js-2"
description: "Test post for mermaid and chart rendering"
tags:
  - test
  - charts
  - diagrams
---

# Test: Mermaid Diagrams & Chart.js

This post tests rendering with transparent backgrounds.

## Flowchart

```mermaid
graph LR
    A[Start] --> B[Process]
    B --> C[End]
```

## Chart

```chart
{
  "type": "doughnut",
  "data": {
    "labels": ["A", "B", "C"],
    "datasets": [{"data": [1, 2, 3]}]
  }
}
```

**Tags:** test
**Categories:** technical