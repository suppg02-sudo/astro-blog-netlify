---
draft: true
pubDatetime: 2026-02-19T23:55:35Z
title: "Performance Summary - February 19, 2026"
postSlug: "performance-summary-2026-02-19"
description: "Performance Summary - February 19, 2026"
tags:
  - performance
  - system
  - monitoring
---

System performance analysis and health summary for February 19, 2026.

## System Metrics

**Uptime:**  23:55:01 up 29 min,  1 user,  

### Memory
- Total: 7749MB | Used: 5406MB (69%) | Available: 2343MB
- Swap Total: 6143MB | Used: 5033MB (81%) | Free: 1110MB

**Memory Pressure (PSI):** avg10=0.00%, avg60=0.05%, full avg10=0.00%

**zswap:** Enabled | Compressor: lz4 | Pool: 20% of RAM

### Disk
- Root: 164G | Used: 156G | Available: 8.1G (96%)

### Docker & Swarm
- Running containers: 74 | Stopped: 74
- Swarm services: 2 | Node availability: Active

### Top Memory Consumers

## Issues & Events

### Memory Management
- **earlyOOM actions:** 166 SIGTERM sent in last 24h
- **CPU limiter:** 264 processes limited at 50% cap

### Service Health
⚠️ **Unhealthy services detected:**
```
blog-ratings-api	Up 27 minutes (unhealthy)
directus-test	Up 27 minutes (unhealthy)
kuse-cowork	Up 27 minutes (unhealthy)
teeshirts-website	Up 27 minutes (unhealthy)
joplin-app-1	Up 27 minutes (unhealthy)
kavita	Up 27 minutes (unhealthy)
```

⚠️ **High kernel error rate:** 10 errors in last 1000 dmesg entries

## Trends & Analysis
- Average available memory: 0MB (last 24h)
- Average free swap: 0MB (last 24h)
- Load averages: 1min=1.34, 5min=1.10, 15min=1.02

### Key Observations
ℹ️ **Moderate memory usage** (69%) - monitor trends
ℹ️ **Swap moderately used** (81%)