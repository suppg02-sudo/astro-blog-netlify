---
pubDatetime: 2026-02-27T23:55:26Z
title: "Performance Summary - February 27, 2026"
postSlug: "performance-summary-2026-02-27"
description: "Performance Summary - February 27, 2026"
tags:
  - performance
  - system
  - monitoring
---

System performance analysis and health summary for February 27, 2026.

## System Metrics

**Uptime:**  23:55:01 up 1 day,  4:45,  3 users,  

### Memory
- Total: 7237MB | Used: 5403MB (74%) | Available: 1835MB
- Swap Total: 6143MB | Used: 5722MB (93%) | Free: 421MB

**Memory Pressure (PSI):** avg10=0.14%, avg60=0.13%, full avg10=0.14%

**zswap:** Enabled | Compressor: lz4 | Pool: 20% of RAM

### Disk
- Root: 164G | Used: 153G | Available: 12G (94%)

### Docker & Swarm
- Running containers: 55 | Stopped: 55
- Swarm services: 0 | Node availability: Active

### Top Memory Consumers

## Issues & Events

### Memory Management
- **earlyOOM actions:** 839 SIGTERM sent in last 24h
- **CPU limiter:** 467 processes limited at 50% cap

### Service Health
⚠️ **Unhealthy services detected:**
```
blog-ratings-api	Up 29 hours (unhealthy)
medic-api	Up 29 hours (unhealthy)
```

## Trends & Analysis
- Average available memory: 0MB (last 24h)
- Average free swap: 0MB (last 24h)
- Load averages: 1min=1.44, 5min=2.21, 15min=3.17

### Key Observations
ℹ️ **Moderate memory usage** (74%) - monitor trends
⚠️ **Swap nearly full** (93%) - swap reclaim should activate when memory allows