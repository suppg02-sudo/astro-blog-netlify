---
pubDatetime: 2026-02-26T23:55:35Z
title: "Performance Summary - February 26, 2026"
postSlug: "performance-summary-2026-02-26"
description: "Performance Summary - February 26, 2026"
tags:
  - performance
  - system
  - monitoring
---

System performance analysis and health summary for February 26, 2026.

## System Metrics

**Uptime:**  23:55:01 up  4:45,  1 user,  

### Memory
- Total: 7237MB | Used: 3549MB (49%) | Available: 3688MB
- Swap Total: 6143MB | Used: 3900MB (63%) | Free: 2243MB

**Memory Pressure (PSI):** avg10=0.00%, avg60=0.00%, full avg10=0.00%

**zswap:** Enabled | Compressor: lz4 | Pool: 20% of RAM

### Disk
- Root: 164G | Used: 152G | Available: 13G (93%)

### Docker & Swarm
- Running containers: 55 | Stopped: 55
- Swarm services: 0 | Node availability: Active

### Top Memory Consumers

## Issues & Events

### Memory Management
- **earlyOOM actions:** 332 SIGTERM sent in last 24h
- **CPU limiter:** 539 processes limited at 50% cap

### Service Health
⚠️ **Unhealthy services detected:**
```
blog-ratings-api	Up 5 hours (unhealthy)
```

⚠️ **High kernel error rate:** 10 errors in last 1000 dmesg entries

## Trends & Analysis
- Average available memory: 0MB (last 24h)
- Average free swap: 0MB (last 24h)
- Load averages: 1min=0.94, 5min=0.77, 15min=0.82

### Key Observations
✅ **Memory usage healthy** (49%)
ℹ️ **Swap moderately used** (63%)