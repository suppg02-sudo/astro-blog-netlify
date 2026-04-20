---
pubDatetime: 2026-02-23T22:00:00Z
title: "Telemetry Streamlining: Removing Redundancy from OpenTelemetry Infrastructure"
postSlug: "telemetry-streamlining-completed"
description: "Telemetry Streamlining: Removing Redundancy from OpenTelemetry Infrastructure"
tags:
  - optimization
  - opentelemetry
  - docker
  - infrastructure
  - telemetry
---

I recently completed a telemetry infrastructure audit on my homelab server and discovered significant redundancy in the OpenTelemetry stack. This post details the cleanup process, the problems found, and the resulting improvements.

## The Problem: Redundant telemetry-oom Stack

My monitoring infrastructure was running 10 telemetry containers, but analysis revealed that the `telemetry-oom` Docker Swarm stack was entirely redundant:

| Component | Status | Network | Issue |
|-----------|--------|----------|--------|
| telemetry-oom_otel-collector | Isolated | telemetry-oom_telemetry | Exports to debug only, no Prometheus/Jaeger |
| telemetry-oom_node-exporter | Isolated | telemetry-oom_telemetry | Not being scraped, port not exposed |

### Why It Was Redundant

1. **Isolated Network**: The `telemetry-oom_telemetry` network was a Docker Swarm overlay network not connected to the main `monitor_monitoring` network where Prometheus runs.

2. **No External Exporters**: The OTel collector configuration only exported to `debug`:
   ```yaml
   exporters:
     debug:
       verbosity: detailed
   ```
   No Prometheus exporter, no Jaeger exporter—just logs going to nowhere.

3. **Not Being Scraped**: Prometheus couldn't reach containers on the isolated network, so no metrics were being collected.

4. **Unstable Services**: Both services crashed repeatedly (exit code 255) and restarted in a loop, consuming resources without providing value.

5. **Duplicate Functionality**: I already had working `otel-collector-main` and `node-exporter` on the monitoring network.

## The Cleanup Process

### Phase 1: Remove telemetry-oom Stack

```bash
# Remove Docker Swarm stack
docker stack rm telemetry-oom

# Clean up exited containers
docker container prune -f
```

**Results**:
- 8 containers removed (2 running + 6 exited)
- 212.9MB disk space freed
- ~640MB RAM saved (512MB collector + 128MB node-exporter)

### Phase 2: Update Prometheus Configuration

The monitor stack's Prometheus config was using an ambiguous target:

```yaml
# Before
- job_name: 'node'
  static_configs:
    - targets: ['host.docker.internal:9100']
```

I updated it to be explicit:

```yaml
# After
- job_name: 'node'
  static_configs:
    - targets: ['node-exporter:9100']
```

This makes it clear which node-exporter Prometheus is scraping (the monitor stack's one, not the redundant telemetry-oom one).

### Phase 3: Reload Prometheus

```bash
curl -X POST http://localhost:9090/-/reload
```

All targets remained healthy after the reload.

## Current Architecture

### Single Monitoring Network

After cleanup, all telemetry components now live on the `monitor_monitoring` bridge network:

| Container | Purpose | Status |
|-----------|---------|--------|
| otel-collector-main | OTLP receiver, metrics/traces export | ✅ Up |
| prometheus | Metrics storage, scraping | ✅ Up |
| grafana | Visualization, dashboards | ✅ Up |
| otel-jaeger | Distributed tracing UI | ✅ Up |
| telemetry-collector | Python service health checks | ✅ Up |
| cadvisor | Container metrics | ✅ Up |
| node-exporter | Host metrics | ✅ Up |

**Total**: 7 containers (all healthy, no redundancy)

### Metrics Flow

The simplified metrics flow:

```
Applications (OpenCode, Demo Apps)
    ↓ OTLP (4317)
otel-collector-main
    ↓
    ├→ Prometheus (metrics) → Grafana (visualization)
    └→ Jaeger (traces)

Host Metrics
    ↓
node-exporter
    ↓
Prometheus
    ↓
Grafana
```

## Benefits Achieved

### Resource Savings
- **Memory**: ~640MB RAM saved
- **Disk**: 212.9MB freed from exited containers
- **CPU**: Reduced overhead from crash loops

### Operational Improvements
- **Simplified architecture**: Single monitoring network, single stack
- **No false alerts**: Eliminated crash loops from unstable services
- **Clear configuration**: Explicit Prometheus targets
- **Easier troubleshooting**: Fewer components to debug

### Data Quality
- **No duplicate metrics**: Single source of truth for each metric type
- **Better performance**: Fewer collectors = lower latency
- **More reliable**: Stable services vs unstable telemetry-oom stack

## Access URLs

All telemetry services are accessible via Tailscale hostname:

| Service | URL | Purpose |
|---------|-----|---------|
| Prometheus | http://ubuntu58-1:9090 | Metrics storage, query, targets |
| Grafana | http://ubuntu58-1:3003 | Dashboards, visualization |
| Jaeger | http://ubuntu58-1:16686 | Distributed tracing UI |
| OTel Collector | http://ubuntu58-1:4317 | OTLP receiver endpoint |
| OTel Metrics | http://ubuntu58-1:8889/metrics | Prometheus metrics endpoint |
| cAdvisor | http://ubuntu58-1:8083 | Container metrics |

## Lessons Learned

1. **Audit Regularly**: Container sprawl happens quickly, especially with Docker Swarm stacks that can create isolated networks.

2. **Check Network Isolation**: If a service isn't being scraped, verify it's on the same network as your monitoring infrastructure.

3. **Review Exporter Configuration**: A collector without exporters is useless—verify your data is actually going somewhere.

4. **Monitor Crash Loops**: Services that crash repeatedly are a symptom of misconfiguration, not normal operation.

5. **Clean Up Exited Containers**: `docker container prune -f` is your friend for reclaiming disk space.

## Next Steps

With the redundancy removed, I can now focus on:

1. **Enabling Tracing**: Update OTel collector config to export traces to Jaeger (currently only metrics export).

2. **Integrating with OpenCode**: Apply the telemetry middleware to capture real skill and LLM usage data.

3. **Adding Grafana Alerts**: Configure alerting rules for LLM costs, skill failures, and system resources.

## Summary

Streamlining telemetry infrastructure from 10 containers (with 2 redundant) to 7 containers (all essential) resulted in:

- ✅ 212.9MB disk space freed
- ✅ 640MB RAM saved
- ✅ Crash loops eliminated
- ✅ Single monitoring network
- ✅ All targets healthy

The cleanup took about 5 minutes and immediately improved system reliability and simplified troubleshooting.