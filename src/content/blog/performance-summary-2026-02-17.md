---
draft: true
pubDatetime: 2026-02-17T23:55:25Z
title: "Performance Summary - February 17, 2026"
postSlug: "performance-summary-2026-02-17"
description: "Performance Summary - February 17, 2026"
tags:
  - performance
  - system
  - monitoring
---

System performance analysis and health summary for February 17, 2026.

## System Metrics

**Uptime:**  23:55:01 up 22:28,  0 user,  

### Memory
- Total: 7749MB | Used: 3852MB (49%) | Available: 3897MB
- Swap Total: 6143MB | Used: 4858MB (79%) | Free: 1285MB

**Memory Pressure (PSI):** avg10=0.00%, avg60=0.00%, full avg10=0.00%

**zswap:** Enabled | Compressor: lz4 | Pool: 20% of RAM

### Disk
- Root: 164G | Used: 155G | Available: 9.0G (95%)

### Docker & Swarm
- Running containers: 73 | Stopped: 73
- Swarm services: 2 | Node availability: Active

### Top Memory Consumers

## Issues & Events
- **CPU limiter:** 174 processes limited at 50% cap

### Service Health
⚠️ **Unhealthy services detected:**
```
homarr	Up 26 hours (unhealthy)
blog-ratings-api	Up 26 hours (unhealthy)
directus-test	Up 26 hours (unhealthy)
kuse-cowork	Up 26 hours (unhealthy)
teeshirts-website	Up 26 hours (unhealthy)
joplin-app-1	Up 26 hours (unhealthy)
kavita	Up 26 hours (unhealthy)
```

⚠️ **High kernel error rate:** 9 errors in last 1000 dmesg entries

## Trends & Analysis
- Average available memory: 0MB (last 24h)
- Average free swap: 0MB (last 24h)
- Load averages: 1min=0.50, 5min=0.49, 15min=0.55

### Key Observations
✅ **Memory usage healthy** (49%)
ℹ️ **Swap moderately used** (79%)