---
draft: true
pubDatetime: 2026-02-21T23:56:10Z
title: "Performance Summary - February 21, 2026"
postSlug: "performance-summary-2026-02-21"
description: "Performance Summary - February 21, 2026"
tags:
  - performance
  - system
  - monitoring
---

System performance analysis and health summary for February 21, 2026.

## System Metrics

**Uptime:**  23:55:01 up 19 min,  1 user,  

### Memory
- Total: 7749MB | Used: 5205MB (67%) | Available: 2544MB
- Swap Total: 6143MB | Used: 6143MB (100%) | Free: 0MB

**Memory Pressure (PSI):** avg10=0.47%, avg60=0.26%, full avg10=0.47%

**zswap:** Enabled | Compressor: lz4 | Pool: 20% of RAM

### Disk
- Root: 164G | Used: 159G | Available: 5.6G (97%)

### Docker & Swarm
- Running containers: 74 | Stopped: 74
- Swarm services: 2 | Node availability: Active

### Top Memory Consumers

## Issues & Events

### Memory Management
- **earlyOOM actions:** 4540 SIGTERM sent in last 24h
- **CPU limiter:** 424 processes limited at 50% cap

### Service Health
⚠️ **Unhealthy services detected:**
```
blog-ratings-api	Up 19 minutes (unhealthy)
directus-test	Up 19 minutes (unhealthy)
kuse-cowork	Up 19 minutes (unhealthy)
teeshirts-website	Up 19 minutes (unhealthy)
joplin-app-1	Up 19 minutes (unhealthy)
kavita	Up 19 minutes (unhealthy)
```

⚠️ **High kernel error rate:** 9 errors in last 1000 dmesg entries

## Trends & Analysis
- Average available memory: 0MB (last 24h)
- Average free swap: 0MB (last 24h)
- Load averages: 1min=2.71, 5min=2.11, 15min=1.86

### Key Observations
ℹ️ **Moderate memory usage** (67%) - monitor trends
⚠️ **Swap nearly full** (100%) - swap reclaim should activate when memory allows