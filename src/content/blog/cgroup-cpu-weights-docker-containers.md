---
pubDatetime: 2026-03-18T01:00:00Z
title: "CPU Resource Management with Cgroup v2 Weights for Docker Containers"
postSlug: "cgroup-cpu-weights-docker-containers"
description: "CPU Resource Management with Cgroup v2 Weights for Docker Containers"
tags:
  - performance
  - cgroups
  - linux
  - docker
  - devops
---

## CPU Throttling Review on Hyper-V

Running Ubuntu in a Hyper-V VM means **CPU throttling is controlled at the host/hypervisor level**, not the guest. The guest OS has limited visibility into actual CPU frequency control.

### What You See vs. What's Real

| Guest (Ubuntu) | Host (Hyper-V) |
|----------------|----------------|
| No cpufreq control | Full frequency control |
| No thermal sensors | Host manages thermals |
| Sees "physical" CPU | Virtual processor assignment |
| Can't see throttling | Host throttles if needed |

**Key insight**: All 4 cores running at ~3.1 GHz (above 2.7 GHz base) indicates turbo boost is active and no throttling is occurring.

## The Problem: No Container Limits

All 44 containers had **unlimited CPU access**:
- No cgroup limits applied
- Any container could consume 100% CPU
- Competition during load was unfair

However, **no hard limits** means containers can compete for resources without priority or fairness.

## The Solution: Cgroups v2 CPU Weights

Instead of hard CPU limits (which cause throttling), use **cpu_weight** for priority-based resource allocation.

### Why Weight > Limit

```
Limit (bad):  VM capped at 50% even if host idle
Weight (good): VM gets 50% when contended, burst to 100% when idle
```

### Cgroups v2 CPU Options

| Control | File | Effect |
|---------|------|--------|
| **cpu.weight** | 1-10000 | Relative priority (default 100) |
| **cpu.max** | `$QUOTA $PERIOD` | Hard limit (e.g., `50000 100000` = 50%) |
| **cpuset.cpus** | 0-3 | Pin to specific CPUs |

## Container Classification (5 Tiers)

Based on usage evidence analysis, containers were organized into priority tiers:

### Tier 1: Critical Infrastructure (weight: 500)

**Purpose**: Core databases and infrastructure that must always respond.

- `pgvector-memory` - AI memory storage
- `directus-postgres` - CMS database
- `rag-postgres` - RAG vector database
- `supermarket-scraper-postgres` - Scraper data
- `directus-redis` - CMS cache
- `nginxproxy` - Reverse proxy

### Tier 2: Active Services (weight: 200)

**Purpose**: APIs, frontends, and monitoring that need good performance.

- `directus` - CMS frontend
- `n8n` - Workflow automation
- `litellm` - AI proxy
- `grafana-otel` - Monitoring
- `prometheus` - Metrics
- `nextexplorer` - File browser
- `memos` - Notes
- `portainer` - Container management
- `hugo` - Static site generator

### Tier 3: Standard Services (weight: 100)

**Purpose**: Default for most services.

- `dashdot` - System monitor
- `olivetin` - Command runner
- `cronmaster` - Cron management
- `filebrowser` - File management
- `freshrss` - RSS reader
- `adguardhome` - DNS filtering
- And 15+ more services

### Tier 4: Low Priority (weight: 50)

**Purpose**: Batch jobs, research tasks that can wait.

- `research-task` - Research tasks
- `production-task` - Production tasks
- `site-creator` - Site generation
- `flows-app` - Flow apps
- `relay` - Relay service

### Tier 5: Minimal (weight: 10)

**Purpose**: Static sites, one-off scrapers.

- `landing-page` - Static landing
- All `astro-*` containers (7 sites)

## OpenCode Resource Management

OpenCode runs in `user.slice`, NOT Docker. Requires separate cgroup management.

### Applied Limits

| Control | Value | Effect |
|---------|-------|--------|
| **cpu.weight** | 500 | 5x priority (7% vs 1.5% under contention) |
| **cpu.max** | 75000 100000 | Cap at 75% CPU |
| **memory.high** | 2GB | Soft throttle (slow down) |
| **memory.max** | 2.5GB | Hard limit (OOM) |

### Memory Behavior

| Usage | What Happens |
|-------|--------------|
| < 2 GB | Normal operation |
| 2-2.5 GB | **Throttled** (slows down) |
| > 2.5 GB | **OOM Killed** |

## Implementation

### Docker Compose Integration

Add to any service in `docker-compose.yml`:

```yaml
services:
  myservice:
    image: example/image
    cpu_weight: 200  # Add this line
```

### Runtime Script

A script applies weights to running containers:

```bash
/root/.local/bin/apply-cpu-weights.sh
```

### Systemd Integration

OpenCode limits applied via systemd user service:

```ini
[Service]
ExecStartPost=/bin/sleep 2 && /root/.local/bin/opencode-cgroup-limits.sh
```

## Benefits Summary

1. **No hard limits** - All containers can burst when resources available
2. **Priority-based sharing** - Critical services get 5x standard priority
3. **Databases protected** - PostgreSQL/Redis always get CPU when needed
4. **Static sites deprioritized** - Astro sites use minimal resources
5. **Automatic persistence** - Weights survive container restarts via compose files
6. **Evidence-based** - Tiers based on actual usage patterns
7. **OpenCode runs well** - Higher priority than before, but can't exhaust system
8. **System always responsive** - Resources reserved for critical operations