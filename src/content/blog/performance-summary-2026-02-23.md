---
pubDatetime: 2026-02-23T23:56:10Z
title: "Performance Summary - February 23, 2026"
postSlug: "performance-summary-2026-02-23"
description: "Performance Summary - February 23, 2026"
tags:
  - performance
  - system
  - monitoring
---

System performance analysis and health summary for February 23, 2026.

## System Metrics

**Uptime:**  23:55:01 up 3 min,  2 users,  

### Memory
- Total: 7237MB | Used: 5614MB (77%) | Available: 1623MB
- Swap Total: 6143MB | Used: 4348MB (70%) | Free: 1795MB

**Memory Pressure (PSI):** avg10=0.03%, avg60=1.49%, full avg10=0.03%

**zswap:** Enabled | Compressor: lz4 | Pool: 20% of RAM

### Disk
- Root: 164G | Used: 149G | Available: 16G (91%)

### Docker & Swarm
- Running containers: 54 | Stopped: 54
- Swarm services: 0 | Node availability: Active

### Top Memory Consumers

## Issues & Events

### Memory Management
- **earlyOOM actions:** 3985 SIGTERM sent in last 24h
- **CPU limiter:** 706 processes limited at 50% cap

### Service Health
⚠️ **Unhealthy services detected:**
```
blog-ratings-api	Up 4 minutes (unhealthy)
```

⚠️ **High kernel error rate:** 10 errors in last 1000 dmesg entries

## Trends & Analysis
- Average available memory: 0MB (last 24h)
- Average free swap: 0MB (last 24h)
- Load averages: 1min=2.86, 5min=3.67, 15min=1.90

### Key Observations
ℹ️ **Moderate memory usage** (77%) - monitor trends
ℹ️ **Swap moderately used** (70%)