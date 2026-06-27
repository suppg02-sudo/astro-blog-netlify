---
draft: true
pubDatetime: 2026-02-22T23:57:35Z
title: "Performance Summary - February 22, 2026"
postSlug: "performance-summary-2026-02-22"
description: "Performance Summary - February 22, 2026"
tags:
  - performance
  - system
  - monitoring
---

System performance analysis and health summary for February 22, 2026.

## System Metrics

**Uptime:**  23:55:01 up 9 min,  1 user,  

### Memory
- Total: 7749MB | Used: 5275MB (68%) | Available: 2474MB
- Swap Total: 6143MB | Used: 4159MB (67%) | Free: 1984MB

**Memory Pressure (PSI):** avg10=0.00%, avg60=0.00%, full avg10=0.00%

**zswap:** Enabled | Compressor: lz4 | Pool: 20% of RAM

### Disk
- Root: 164G | Used: 145G | Available: 19G (89%)

### Docker & Swarm
- Running containers: 67 | Stopped: 70
- Swarm services: 2 | Node availability: Active

### Top Memory Consumers

## Issues & Events

### Memory Management
- **earlyOOM actions:** 1851 SIGTERM sent in last 24h
- **CPU limiter:** 355 processes limited at 50% cap

### Service Health
⚠️ **Unhealthy services detected:**
```
blog-ratings-api	Up 10 minutes (unhealthy)
kuse-cowork	Up 10 minutes (unhealthy)
teeshirts-website	Up 10 minutes (unhealthy)
joplin-app-1	Up 10 minutes (unhealthy)
kavita	Up 10 minutes (unhealthy)
```

⚠️ **High kernel error rate:** 10 errors in last 1000 dmesg entries

## Trends & Analysis
- Average available memory: 0MB (last 24h)
- Average free swap: 0MB (last 24h)
- Load averages: 1min=2.02, 5min=2.19, 15min=1.86

### Key Observations
ℹ️ **Moderate memory usage** (68%) - monitor trends
ℹ️ **Swap moderately used** (67%)