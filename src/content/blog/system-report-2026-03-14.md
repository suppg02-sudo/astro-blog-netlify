---
draft: true
pubDatetime: 2026-03-14T08:00:00Z
title: "System Performance Report - March 14, 2026"
postSlug: "system-report-2026-03-14"
description: "System Performance Report - March 14, 2026"
tags:
  - cgroups
  - monitoring
  - performance
  - cpu
---

## Overview

🟡 **System Status:** MODERATE

Daily performance report for `2026-03-14` based on 5 samples collected.

---

## CPU Analysis

| Metric | Value | Assessment |
|--------|-------|------------|
| CPU Cores | 4 | - |
| Avg Load (1m) | 5.83 | 1.46x cores |
| Max Load (1m) | 6.9 | Peak usage |
| Min Load (1m) | 3.82 | Low usage |
| Load Ratio | 1.46x | Overloaded |

### Peak Load Times

| Time | Load |
|------|------|
| 13:51:02 | 6.9 |
| 13:50:57 | 6.63 |
| 13:50:52 | 6.42 |
| 13:50:27 | 5.37 |
| 13:53:22 | 3.82 |


---

## Memory Analysis

| Metric | Value |
|--------|-------|
| Avg Usage | 59.4% |
| Max Usage | 59.7% |
| Min Usage | 59.2% |

---

## Top CPU Consumers

| Process | Avg CPU % |
|---------|----------|
| ps aux --sort=-%cpu | 0.0% |
| ba | 0.0% |
| collect_metrics.py | 0.0% |
| opencode | 0.0% |
| py | 0.0% |
| n8n | 0.0% |
| containerd.sock | 0.0% |
|  | 0.0% |


---

## Container Status

| Metric | Value |
|--------|-------|
| Avg Running Containers | 42 |
| Max Containers | 42 |

---

## CGroup Configuration

Services with cgroup limits configured:
*No services with cgroup limits detected*

---

## Recommendations


#### 🟢 Configuration (LOW)

**Issue:** No services using cgroup limits detected

**Action:** Implement cgroup limits for resource isolation



---

## Summary

The system was **moderate** during this reporting period with an average load ratio of **1.46x** CPU capacity.

Memory usage remained stable at 59.4% average.

---

*Report generated automatically by CPU Monitor System*