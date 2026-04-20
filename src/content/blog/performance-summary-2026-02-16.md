---
pubDatetime: 2026-02-16T23:55:37Z
title: "Performance Summary - February 16, 2026"
postSlug: "performance-summary-2026-02-16"
description: "Performance Summary - February 16, 2026"
tags:
  - performance
  - system
  - monitoring
---

System performance analysis and health summary for February 16, 2026.

## System Metrics

**Uptime:**  23:55:01 up  2:03,  0 user,  

### Memory
- Total: 7749MB | Used: 5008MB (64%) | Available: 2740MB
- Swap Total: 6143MB | Used: 3629MB (59%) | Free: 2514MB

**Memory Pressure (PSI):** avg10=0.00%, avg60=0.00%, full avg10=0.00%

**zswap:** Enabled | Compressor: lz4 | Pool: 20% of RAM

### Disk
- Root: 164G | Used: 155G | Available: 9.2G (95%)

### Docker & Swarm
- Running containers: 73 | Stopped: 75
- Swarm services: 2 | Node availability: Active

### Top Memory Consumers

## Issues & Events

### Memory Management
- **earlyOOM actions:** 1207 SIGTERM sent in last 24h
- **CPU limiter:** 281 processes limited at 50% cap

### Service Health
⚠️ **Unhealthy services detected:**
```
homarr	Up 2 hours (unhealthy)
blog-ratings-api	Up 2 hours (unhealthy)
directus-test	Up 2 hours (unhealthy)
kuse-cowork	Up 2 hours (unhealthy)
teeshirts-website	Up 2 hours (unhealthy)
joplin-app-1	Up 2 hours (unhealthy)
kavita	Up 2 hours (unhealthy)
```

⚠️ **High kernel error rate:** 9 errors in last 1000 dmesg entries

## Trends & Analysis
- Average available memory: 0MB (last 24h)
- Average free swap: 0MB (last 24h)
- Load averages: 1min=1.03, 5min=0.48, 15min=0.40

### Key Observations
ℹ️ **Moderate memory usage** (64%) - monitor trends
ℹ️ **Swap moderately used** (59%)