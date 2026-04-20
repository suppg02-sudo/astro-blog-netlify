---
pubDatetime: 2026-02-26T21:58:00Z
title: "Fixing Astro-Fresh OOM Kills with ZRAM and ZSwap on Low-Memory Servers"
postSlug: "fixing-astro-fresh-oom-zswap-zram"
description: "Fixing Astro-Fresh OOM Kills with ZRAM and ZSwap on Low-Memory Servers"
tags:
  - zswap
  - linux
  - memory
  - zram
  - docker
  - devops
---

## The Problem

Running ~20 Docker containers on a 1.8GB RAM server is tight. Very tight. Today, my `astro-fresh` container kept getting OOM killed during startup.

```
[Thu Feb 26 21:48:23 2026] Memory cgroup out of memory: Killed process 45421 (node)
```

The culprit? `npm install` running on every container start, spiking memory usage beyond the 128MB limit.

## Diagnosis

| Metric | Value | Status |
|--------|-------|--------|
| Total RAM | 1.8 GiB | Low |
| Available | 393 MiB | Critical |
| Swap Used | 2.2 / 4.2 GiB | Heavy thrashing |
| zram0 | 256MB | 99.9% full |

The system was thrashing disk swap constantly, making everything slow.

## Part 1: Fix the Astro Container

The original `docker-compose.yml`:

```yaml
command: >
  sh -c "npm install &&
         npm run dev -- --host 0.0.0.0"
environment:
  - NODE_ENV=development
deploy:
  resources:
    limits:
      memory: 128M
```

**Problems:**
1. `npm install` spikes memory during startup
2. No Node heap limit = unbounded memory growth
3. 128MB limit gets hit during install, triggering OOM

**Solution:** Pre-install dependencies and cap the heap.

```yaml
command: >
  sh -c "npm run dev -- --host 0.0.0.0"
environment:
  - NODE_ENV=development
  - NODE_OPTIONS=--max-old-space-size=192
deploy:
  resources:
    limits:
      memory: 128M
```

Run npm install once:

```bash
docker compose run --rm astro-blog npm install
docker compose up -d
```

**Result:** Container now runs at ~110MB (86% of limit) and stays alive.

## Part 2: Optimize System Swap

The system had two swap issues:

1. **zram too small** - 256MB wasn't enough
2. **zswap disabled** - No compressed cache layer before disk swap

### Increase ZRAM to 1GB

Edit `/etc/default/zramswap`:

```bash
# Compression algorithm
ALGO=zstd

# Size in MiB (was 256)
SIZE=1024

# Priority (higher = preferred)
PRIORITY=100
```

### Enable ZSwap

Edit `/etc/default/grub`:

```bash
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash zswap.enabled=1 zswap.compressor=zstd zswap.max_pool_percent=25 zswap.zpool=z3fold"
```

Then update grub:

```bash
update-grub
```

### The Memory Hierarchy After Reboot

```
RAM → zswap (25% cache) → zram (1GB compressed) → swapfile (disk fallback)
```

| Layer | Size | Purpose |
|-------|------|---------|
| zswap | ~450MB | Compressed cache in RAM |
| zram | 1GB | Compressed RAM swap (zstd) |
| swapfile | 4GB | Disk fallback |

## Summary of Changes

| Setting | Before | After |
|---------|--------|-------|
| astro startup | `npm install` every time | Pre-installed deps |
| Node heap | Unlimited | 192MB cap |
| zram size | 256MB | 1GB (4x) |
| zram algo | lzo | zstd (better compression) |
| zswap | Disabled | Enabled (25% pool) |

## Verification

After applying changes:

```bash
# Check memory layout
swapon --show

# Verify zswap enabled
cat /sys/module/zswap/parameters/enabled

# Check container memory
docker stats astro-fresh --no-stream
```

A reboot is required to apply the zswap/zram changes. The container fix is immediate.