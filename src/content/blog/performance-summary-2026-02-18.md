---
pubDatetime: 2026-02-18T23:55:31Z
title: "Performance Summary - February 18, 2026"
postSlug: "performance-summary-2026-02-18"
description: "Performance Summary - February 18, 2026"
tags:
  - performance
  - system
  - monitoring
---

System performance analysis and health summary for February 18, 2026.

## System Metrics

**Uptime:**  23:55:01 up 1 day, 22:28,  0 user,  

### Memory
- Total: 7749MB | Used: 3726MB (48%) | Available: 4023MB
- Swap Total: 6143MB | Used: 4926MB (80%) | Free: 1217MB

**Memory Pressure (PSI):** avg10=0.00%, avg60=0.00%, full avg10=0.00%

**zswap:** Enabled | Compressor: lz4 | Pool: 20% of RAM

### Disk
- Root: 164G | Used: 156G | Available: 8.5G (95%)

### Docker & Swarm
- Running containers: 73 | Stopped: 73
- Swarm services: 2 | Node availability: Active

### Top Memory Consumers

## Issues & Events
- **CPU limiter:** 203 processes limited at 50% cap

### Service Health
⚠️ **Unhealthy services detected:**
```
homarr	Up 2 days (unhealthy)
blog-ratings-api	Up 2 days (unhealthy)
directus-test	Up 20 hours (unhealthy)
kuse-cowork	Up 2 days (unhealthy)
teeshirts-website	Up 2 days (unhealthy)
joplin-app-1	Up 2 days (unhealthy)
kavita	Up 2 days (unhealthy)
```

⚠️ **High kernel error rate:** 9 errors in last 1000 dmesg entries

## Trends & Analysis
- Average available memory: 0MB (last 24h)
- Average free swap: 0MB (last 24h)
- Load averages: 1min=0.93, 5min=0.56, 15min=0.58

### Key Observations
✅ **Memory usage healthy** (48%)
ℹ️ **Swap moderately used** (80%)