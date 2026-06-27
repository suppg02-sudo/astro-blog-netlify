---
draft: true
pubDatetime: 2026-03-27T14:00:00Z
title: "Test Blog Post with Diagrams"
postSlug: "test-diagrams"
description: "A demonstration of Mermaid diagrams, flowcharts, and Chart.js visualizations in Astro"
tags:
  - diagrams
  - visualization
  - chartjs
  - mermaid
  - test
---

This is a test blog post demonstrating various diagram types supported in Astro.

## System Architecture

Here is a flowchart showing the blog publishing pipeline:

```mermaid
flowchart TD
    A[Write Markdown] --> B[Quality Gates]
    B --> C{Pass?}
    C -->|Yes| D[Publish to Directus]
    C -->|No| E[Fix Issues]
    E --> B
    D --> F[Live on Blog]
```

## Data Flow Diagram

How content moves through the system:

```mermaid
graph LR
    A[Author] --> B[Astro Project]
    B --> C[Directus CMS]
    C --> D[(Database)]
    D --> E[Public Blog]
    E --> F[Readers]
```

## Chart.js Example

Interactive doughnut chart:

```chart
{
  "type": "doughnut",
  "data": {
    "labels": ["Development", "Writing", "Review", "Publishing"],
    "datasets": [{"data": [40, 25, 20, 15]}]
  }
}
```

## Sequence Diagram

The publishing workflow over time:

```mermaid
sequenceDiagram
    participant Author
    participant Astro
    participant Directus
    participant Blog

    Author->>Astro: Write post
    Astro->>Astro: Quality check
    Astro->>Directus: POST /items/posts
    Directus->>Blog: Webhook trigger
    Blog->>Author: Notification
```

## State Diagram

Blog post lifecycle:

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Review
    Review --> Published
    Review --> Draft
    Published --> Archived
    Archived --> [*]
```

## Summary

This test demonstrates:
- Flowcharts for processes
- Graphs for relationships
- Sequence diagrams for workflows
- State diagrams for lifecycles
- Chart.js for data visualization