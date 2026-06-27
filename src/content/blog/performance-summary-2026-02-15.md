---
draft: true
pubDatetime: 2026-02-15T23:56:24Z
title: "Performance Summary - February 15, 2026"
postSlug: "performance-summary-2026-02-15"
description: "Performance Summary - February 15, 2026"
tags:
  - performance
  - system
  - monitoring
---

System performance analysis and health summary for February 15, 2026.

## System Metrics

**Uptime:**  23:55:01 up  1:30,  3 users,  

### Memory
- Total: 7749MB | Used: 7254MB (93%) | Available: 497MB
- Swap Total: 6143MB | Used: 6143MB (100%) | Free: 0MB

**Memory Pressure (PSI):** avg10=3.71%, avg60=1.92%, full avg10=3.22%

**zswap:** Enabled | Compressor: lz4 | Pool: 20% of RAM

### Disk
- Root: 164G | Used: 154G | Available: 10G (94%)

### Docker & Swarm
- Running containers: 73 | Stopped: 73
- Swarm services: 2 | Node availability: Active

### Top Memory Consumers

## Issues & Events

### Memory Management
- **earlyOOM actions:** 8298 SIGTERM sent in last 24h
- **CPU limiter:** 463 processes limited at 50% cap

### Service Health
⚠️ **Unhealthy services detected:**
```
blog-ratings-api	Up 2 hours (unhealthy)
directus-test	Up 48 minutes (unhealthy)
kuse-cowork	Up 2 hours (unhealthy)
teeshirts-website	Up 2 hours (unhealthy)
joplin-app-1	Up 2 hours (unhealthy)
kavita	Up 2 hours (unhealthy)
```

## Trends & Analysis
- Average available memory: 0MB (last 24h)
- Average free swap: 0MB (last 24h)
- Load averages: 1min=7.60, 5min=5.16, 15min=4.44

### Key Observations
⚠️ **High memory usage** (93%) - consider identifying memory leaks or adding more RAM
⚠️ **Swap nearly full** (100%) - swap reclaim should activate when memory allows
⚠️ **Low available memory** (497MB) - close to OOM threshold