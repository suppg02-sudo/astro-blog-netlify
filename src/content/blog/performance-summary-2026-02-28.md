---
pubDatetime: 2026-02-28T23:55:37Z
title: "Performance Summary - February 28, 2026"
postSlug: "performance-summary-2026-02-28"
description: "Performance Summary - February 28, 2026"
tags:
  - performance
  - system
  - monitoring
---

System performance analysis and health summary for February 28, 2026.

## System Metrics

**Uptime:**  23:55:01 up 10:41,  0 user,  

### Memory
- Total: 7237MB | Used: 3915MB (54%) | Available: 3323MB
- Swap Total: 6143MB | Used: 3747MB (60%) | Free: 2396MB

**Memory Pressure (PSI):** avg10=0.00%, avg60=0.00%, full avg10=0.00%

**zswap:** Enabled | Compressor: lz4 | Pool: 20% of RAM

### Disk
- Root: 164G | Used: 154G | Available: 11G (94%)

### Docker & Swarm
- Running containers: 55 | Stopped: 55
- Swarm services: 0 | Node availability: Active

### Top Memory Consumers

## Issues & Events

### Memory Management
- **earlyOOM actions:** 966 SIGTERM sent in last 24h
- **CPU limiter:** 448 processes limited at 50% cap

### Service Health
⚠️ **Unhealthy services detected:**
```
blog-ratings-api	Up 11 hours (unhealthy)
```

⚠️ **High kernel error rate:** 13 errors in last 1000 dmesg entries

## Trends & Analysis
- Average available memory: 0MB (last 24h)
- Average free swap: 0MB (last 24h)
- Load averages: 1min=1.19, 5min=1.30, 15min=1.34

### Key Observations
✅ **Memory usage healthy** (54%)
ℹ️ **Swap moderately used** (60%)