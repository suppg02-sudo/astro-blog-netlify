---
pubDatetime: 2026-02-26T20:50:00Z
title: "Hardening a Low-Memory Server: Complete Resource Exhaustion Protection Guide"
postSlug: "resource-exhaustion-protection-low-memory-server"
description: "Hardening a Low-Memory Server: Complete Resource Exhaustion Protection Guide"
tags:
  - memory-management
  - sysadmin
  - oom
  - linux
  - zram
  - docker
  - devops
  - psi
  - telemetry
---

## The Problem: Running 24 Containers on 1.8GB RAM

When you're running a homelab or small VPS with limited resources, memory exhaustion isn't a question of *if*—it's a question of *when*. This server was running 24 Docker containers on just 1.8GB of RAM with **zero resource limits**. The result:

- **402MB available memory** (22% free)
- **60% swap usage** (2.4GB of 4GB used)
- **2.5x memory overcommit** (12.5GB committed vs 5GB limit)
- **No OOM protection** for critical services

This is a recipe for disaster. One runaway container could lock up the entire system.

## The Solution: Multi-Layer Resource Protection

I implemented a comprehensive protection system with **10 layers of defense** that adds multiple safety nets without sacrificing functionality.

## Phase 1: System-Level Memory Protection

### Sysctl Tuning

Created `/etc/sysctl.d/99-memory-protection.conf`:

```bash
# Increase reserved memory for system operations
vm.min_free_kbytes = 65536

# Reduce swap aggressiveness (was 10, now 5)
vm.swappiness = 5

# Aggressively reclaim inode/dentry cache under memory pressure
vm.vfs_cache_pressure = 150

# Reserve memory for admin/root operations
vm.admin_reserve_kbytes = 8192
```

This ensures the kernel keeps 64MB free for critical operations and reduces swap thrashing.

## Phase 2: Tiered Container Memory Limits

The key insight: **not all containers are equal**. I created a 4-tier priority system:

| Tier | Services | Memory Limit | OOM Score | Kill Order |
|------|----------|--------------|-----------|------------|
| **Critical** | portainer, nginxproxy, authentik-postgres, authentik-redis | 256-512MB | -500 | Last |
| **Important** | authentik-server, authentik-worker, openmemory, n8n | 256MB | -100 | 3rd |
| **Standard** | grafana, prometheus, homepage, hugo, memos | 64-256MB | 0 | 2nd |
| **Disposable** | fossflow, litegraph, cronmaster, nextexplorer, astro-fresh | 64-128MB | +500 | 1st |

### Docker Compose Resource Limits

Each `docker-compose.yml` now includes:

```yaml
services:
  myservice:
    # ... existing config ...
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 256M
        reservations:
          cpus: '0.1'
          memory: 32M
```

### Iterative Limit Tuning

After initial deployment, I discovered `astro-fresh` was hitting 91% of its 64MB limit. I increased it to 128MB:

```bash
docker update --memory=128m --memory-swap=128m astro-fresh
```

This brought usage down to 49% - a much safer margin.

## Phase 3: OOM Score Prioritization

The Linux OOM killer uses `oom_score_adj` to decide which process to kill when memory runs out:

- **-500 to -1000**: Protected (almost never killed)
- **0**: Default
- **+500 to +1000**: First to kill

I created a script that sets these scores via `/proc`:

```bash
#!/bin/bash
# Critical services (protected, -500)
for c in portainer nginxproxy authentik-postgres authentik-redis; do
    pid=$(docker inspect -f '{{.State.Pid}}' "$c")
    echo -500 > /proc/$pid/oom_score_adj
done

# Disposable services (first to kill, +500)
for c in fossflow litegraph cronmaster nextexplorer astro-fresh; do
    pid=$(docker inspect -f '{{.State.Pid}}' "$c")
    echo 500 > /proc/$pid/oom_score_adj
done
```

**Important**: OOM scores reset when containers restart. I created a systemd service (`docker-oom-scores.service`) that reapplies scores after Docker starts.

## Phase 4: Memory Watchdog Service

The most critical component—an automated watchdog that prevents system lockup:

```bash
#!/bin/bash
# Memory Watchdog - Prevents system lockup

THRESHOLD_CRITICAL=30    # MB available - emergency
THRESHOLD_WARNING=100    # MB available - warning

# Container kill order (disposable tier first)
KILL_ORDER=("fossflow" "litegraph-mcp" "cronmaster" "nextexplorer")

while true; do
    AVAILABLE=$(awk '/MemAvailable/ {printf "%.0f", $2/1024}' /proc/meminfo)
    
    if [ "$AVAILABLE" -lt "$THRESHOLD_CRITICAL" ]; then
        for container in "${KILL_ORDER[@]}"; do
            docker stop "$container"
            # Check if we recovered
            NEW_AVAILABLE=$(awk '/MemAvailable/ {printf "%.0f", $2/1024}' /proc/meminfo)
            if [ "$NEW_AVAILABLE" -gt "$THRESHOLD_WARNING" ]; then
                break
            fi
        done
    fi
    
    sleep 10
done
```

This runs as a systemd service and automatically stops low-priority containers before the system becomes unresponsive.

## Phase 5: Prometheus Alerting

Added alert rules for proactive monitoring:

```yaml
groups:
  - name: memory_alerts
    rules:
      - alert: MemoryCritical
        expr: (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100 < 10
        for: 30s
        labels:
          severity: critical
        annotations:
          summary: "Memory critically low"

      - alert: SwapUsageHigh
        expr: (1 - (node_memory_SwapFree_bytes / node_memory_SwapTotal_bytes)) * 100 > 80
        for: 2m
        labels:
          severity: warning
```

## Phase 6: OpenCode Memory Limiter

Created a cgroup for OpenCode sessions:

```ini
[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/bin/bash -c '\
    mkdir -p /sys/fs/cgroup/opencode && \
    echo 2147483648 > /sys/fs/cgroup/opencode/memory.max'
```

This limits OpenCode to 2GB of memory, preventing it from consuming all available RAM during intensive operations.

## Phase 7: PSI (Pressure Stall Information) Monitoring

**New in Linux 4.20+**, PSI provides early warning of resource pressure before the system becomes unresponsive. Check if available:

```bash
cat /proc/pressure/memory
# Output: some avg10=5.45 avg60=6.32 avg300=12.19 total=443759755
#         full avg10=4.31 avg60=4.46 avg300=9.19 total=323650635
```

I created a PSI monitor that logs alerts when pressure exceeds thresholds:

```bash
#!/bin/bash
# PSI Monitor - Early warning system

THRESHOLDS:
  MEMORY_SOME_WARN=20    # Some processes waiting
  MEMORY_SOME_CRIT=40    # Significant contention
  MEMORY_FULL_WARN=10    # All processes stalled
  MEMORY_FULL_CRIT=25    # System unresponsive

# Check every 30 seconds
# Log to /var/log/psi-monitor.log
```

This provides **predictive alerts** 30-60 seconds before OOM would occur.

## Phase 8: Resource Trend Logging

For historical analysis and capacity planning, I added hourly logging:

```bash
# /usr/local/bin/resource-trend-logger.sh
# Logs: timestamp, mem_total, mem_used, mem_available, swap_used, load, containers

# Example output:
2026-02-26 21:03:13 - METRIC,mem_total=1855,mem_used=1496,mem_available=359,swap_used=2843,load=1.06,containers=23
```

Added to crontab:

```
0 * * * * /usr/local/bin/resource-trend-logger.sh >> /var/log/resource-trends.log 2>&1
```

0 * * * * /usr/local/bin/resource-trend-logger.sh >> /var/log/resource-trends.log 2>&1
```

## Phase 9: Zram Compressed Swap

After installing `linux-modules-extra-$(uname -r)`, the zram module became available. Zram compresses swap pages in RAM before writing to disk, reducing I/O and extending effective memory:

### Setup

```bash
# Install extra kernel modules (if needed)
apt-get install -y linux-modules-extra-$(uname -r)

# Load module
modprobe zram

# Configure 2GB compressed swap
echo 1 > /sys/block/zram0/reset
echo lz4 > /sys/block/zram0/comp_algorithm
echo 2G > /sys/block/zram0/disksize
mkswap /dev/zram0
swapon -p 100 /dev/zram0
```

### Systemd Service

Created `/etc/systemd/system/zram-swap.service`:

```ini
[Unit]
Description=Zram Swap Service
After=local-fs.target

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/bin/bash -c 'echo 1 > /sys/block/zram0/reset && echo lz4 > /sys/block/zram0/comp_algorithm && echo 2G > /sys/block/zram0/disksize && mkswap /dev/zram0 && swapon -p 100 /dev/zram0'
ExecStop=/bin/bash -c 'swapoff /dev/zram0 && echo 1 > /sys/block/zram0/reset'

[Install]
WantedBy=multi-user.target
```

### Result

```
NAME       TYPE      SIZE   USED PRIO
/swapfile  file        4G   2.7G   -2
/dev/zram0 partition   2G   186M  100   ← Higher priority = used first
```

With lz4 compression, the 2GB zram provides ~3GB of effective swap space, extending the system's memory capacity by ~50%.

## Phase 10: Disk I/O Telemetry

To identify if disk is the bottleneck, I added `node_exporter` to the OpenTelemetry stack:

### Adding node_exporter

```yaml
# Add to docker-compose.yml
node-exporter:
  image: prom/node-exporter:latest
  container_name: node-exporter
  volumes:
    - /proc:/host/proc:ro
    - /sys:/host/sys:ro
    - /:/rootfs:ro
  command:
    - '--path.procfs=/host/proc'
    - '--path.sysfs=/host/sys'
    - '--path.rootfs=/rootfs'
  ports:
    - "9100:9100"
  networks:
    - otel-net
```

### Prometheus Scrape Config

```yaml
# Add to prometheus.yml
- job_name: 'node-exporter'
  static_configs:
    - targets: ['node-exporter:9100']
```

### Key Disk Metrics

| Metric | Purpose | Use Case |
|--------|---------|----------|
| `node_disk_read_bytes_total` | Total bytes read | Trend analysis |
| `node_disk_written_bytes_total` | Total bytes written | Trend analysis |
| `node_disk_io_time_seconds_total` | Time spent on I/O | Bottleneck detection |
| `node_disk_io_now` | Current I/O operations | Real-time monitoring |
| `node_filesystem_avail_bytes` | Free disk space | Capacity planning |

### Querying Disk Metrics

```bash
# Check disk I/O time
curl -s 'http://localhost:9090/api/v1/query?query=node_disk_io_time_seconds_total'

# Check filesystem usage
curl -s 'http://localhost:9090/api/v1/query?query=node_filesystem_avail_bytes'
```

## Results: Before vs After

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Containers with limits | 0/24 | 24/24 | ∞ |
| OOM protection | None | 4-tier | Full |
| Automated recovery | None | Watchdog | Full |
| Early warning | None | PSI monitor | Predictive |
| Historical data | None | Hourly trends | Analysis ready |
| Memory reserved for system | 45MB | 64MB | +42% |
| Swap aggressiveness | High (10) | Low (5) | -50% |

### Container Stats After Implementation

```
NAME                      MEM USAGE / LIMIT     MEM %
litegraph-mcp             14.96MiB / 64MiB      23%
astro-fresh               63.34MiB / 128MiB     49%  (was 91% at 64MB)
authentik-server          179.4MiB / 256MiB     70%
authentik-worker          144.0MiB / 256MiB     56%
grafana-otel              91.13MiB / 256MiB     36%
```

Every container now has a hard ceiling it cannot exceed.

## Protection Services Summary

| Service | Purpose | Trigger |
|---------|---------|---------|
| `memory-watchdog` | Kill containers | Available < 30MB |
| `psi-monitor` | Alert on pressure | PSI > thresholds |
| `docker-oom-scores` | Set priorities | Container restart |
| `resource-trend-logger` | Historical data | Hourly cron |

## Key Takeaways

1. **Layer your defenses**: Don't rely on a single mechanism. Use sysctl tuning + container limits + OOM scores + watchdogs + PSI monitoring.

2. **Prioritize ruthlessly**: Not all services are equal. Protect critical infrastructure, sacrifice disposable experiments.

3. **Automate recovery**: The watchdog service is the difference between "system recovered" and "system hung, manual reboot required."

4. **Monitor proactively**: PSI alerts give you 30-60 seconds warning before OOM—enough time to act.

5. **Iterate on limits**: Initial limits may be too tight. Monitor and adjust (like astro-fresh 64MB → 128MB).

6. **Log for trends**: Historical data helps identify memory leaks and capacity needs before they become critical.

## Files Created

| File | Purpose |
|------|---------|
| `/etc/sysctl.d/99-memory-protection.conf` | Kernel memory tuning |
| `/usr/local/bin/memory-watchdog.sh` | Automated OOM protection |
| `/usr/local/bin/set-oom-scores.sh` | OOM priority management |
| `/usr/local/bin/psi-monitor.sh` | Pressure stall monitoring |
| `/usr/local/bin/resource-trend-logger.sh` | Hourly metrics logging |
| `/etc/systemd/system/memory-watchdog.service` | Watchdog daemon |
| `/etc/systemd/system/psi-monitor.service` | PSI monitor daemon |
| `/etc/systemd/system/docker-oom-scores.service` | OOM score applier |
| `/media/docker/*/docker-compose.yml` | Container resource limits |
| `/media/docker/opentelemetry-stack/alerts/memory-alerts.yml` | Prometheus alerts |

## Future Improvements

**Container Consolidation**: Some containers (litegraph, fossflow) have very low usage. Consider stopping when not actively used.

**Grafana Dashboards**: Import the Node Exporter Full dashboard (ID: 1860) for comprehensive disk and system visualization.

## Rollback Plan

If issues arise:

```bash
# Stop monitoring services
systemctl stop memory-watchdog psi-monitor

# Remove resource limits from compose files
# Then recreate containers
docker compose up -d --force-recreate

# Restore sysctl defaults
sysctl vm.swappiness=10 vm.min_free_kbytes=45056
```

---

This multi-layered approach transforms a fragile, crash-prone server into a resilient system that gracefully handles memory pressure. The watchdog ensures automatic recovery, the PSI monitor provides early warning, and the tiered limits ensure critical services survive any memory crunch.