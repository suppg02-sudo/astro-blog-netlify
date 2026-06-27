---
draft: true
pubDatetime: 2026-03-26T19:02:07Z
title: "Test: Mermaid Diagrams & Chart.js"
postSlug: "test-mermaid-diagrams-chart-js"
description: "{"
tags:
  - "4ade80"
  - fbbf24
  - "3b82f6"
  - f87171
---

# Test: Mermaid Diagrams & Chart.js

This post tests rendering of Mermaid diagrams and Chart.js charts.

## Mermaid Flowchart

```mermaid
graph LR
    A[Input] --> B{Process}
    B -->|Yes| C[Output]
    B -->|No| D[Error]
    C --> E[Success]
    D --> F[Retry]
    F --> B
```

## Mermaid Sequence Diagram

```mermaid
sequenceDiagram
    participant User
    participant API
    participant Database
    User->>API: Request data
    API->>Database: Query
    Database-->>API: Results
    API-->>User: Response
```

## Chart.js Doughnut

```chart
{
  "type": "doughnut",
  "data": {
    "labels": ["Completed", "In Progress", "Pending"],
    "datasets": [{
      "data": [60, 25, 15],
      "backgroundColor": ["#4ade80", "#fbbf24", "#f87171"]
    }]
  },
  "options": {
    "responsive": true,
    "plugins": {
      "title": {
        "display": true,
        "text": "Task Status Distribution"
      }
    }
  }
}
```

## Chart.js Bar Chart

```chart
{
  "type": "bar",
  "data": {
    "labels": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "datasets": [{
      "label": "Tasks Completed",
      "data": [12, 19, 8, 15, 22],
      "backgroundColor": "#3b82f6"
    }]
  },
  "options": {
    "responsive": true,
    "plugins": {
      "title": {
        "display": true,
        "text": "Weekly Progress"
      }
    }
  }
}
```

---

**Tags:** test, diagrams, charts
**Categories:** technical