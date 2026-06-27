---
draft: true
pubDatetime: 2026-02-25T23:55:31Z
title: "Performance Summary - February 25, 2026"
postSlug: "performance-summary-2026-02-25"
description: "Performance Summary - February 25, 2026"
tags:
  - performance
  - system
  - monitoring
---

System performance analysis and health summary for February 25, 2026.

## System Metrics

**Uptime:**  23:55:01 up 14:00,  0 user,  

### Memory
- Total: 7237MB | Used: 3850MB (53%) | Available: 3387MB
- Swap Total: 6143MB | Used: 3774MB (61%) | Free: 2369MB

**Memory Pressure (PSI):** avg10=0.00%, avg60=0.00%, full avg10=0.00%

**zswap:** Enabled | Compressor: lz4 | Pool: 20% of RAM

### Disk
- Root: 164G | Used: 150G | Available: 15G (92%)

### Docker & Swarm
- Running containers: 55 | Stopped: 55
- Swarm services: 0 | Node availability: Active

### Top Memory Consumers

## Issues & Events

### Memory Management
- **earlyOOM actions:** 1917 SIGTERM sent in last 24h
- **CPU limiter:** 678 processes limited at 50% cap

### Service Health
⚠️ **Unhealthy services detected:**
```
blog-ratings-api	Up 14 hours (unhealthy)
```

⚠️ **High kernel error rate:** 14 errors in last 1000 dmesg entries

## Trends & Analysis
- Average available memory: 0MB (last 24h)
- Average free swap: 0MB (last 24h)
- Load averages: 1min=1.36, 5min=1.11, 15min=0.90

### Key Observations
✅ **Memory usage healthy** (53%)
ℹ️ **Swap moderately used** (61%)