---
pubDatetime: 2026-03-05T09:39:37Z
title: "System Audit Report"
postSlug: "0939-system-audit"
description: "Automated system audit covering context registry, OliveTin actions, relay logs, and container health."
tags:
  - registry
  - system-health
  - audit
  - monitoring
  - docker
  - relay
  - olivetin
---

## Overview

This report summarizes a comprehensive system audit covering all activity sources from the last 10 minutes.

## Docker Container Status

| rag-postgres | Up About an hour (healthy) |
| olivetin | Up About an hour (healthy) |
| hugo | Up About an hour |
| research-task | Up About an hour (healthy) |
| landing-page | Up About an hour |
| directus | Up About an hour (healthy) |
| fossflow | Up About an hour |
| astro-tshirt-sales | Up About an hour |
| openmemory-dashboard | Up About an hour |
| astro-vector | Up About an hour |
| directus-postgres | Up About an hour (healthy) |
| directus-redis | Up About an hour (healthy) |
| flows-app | Up About an hour (healthy) |
| nextexplorer | Up About an hour (healthy) |
| omni-web | Up About an hour |
| omni-caddy | Up About an hour |
| omni-sandbox | Up About an hour (healthy) |
| omni-web-connector | Up About an hour |
| omni-slack-connector | Up About an hour |
| omni-indexer | Restarting (1) 43 seconds ago |
| omni-ai | Up About an hour |
| omni-connector-manager | Restarting (1) 42 seconds ago |
| omni-searcher | Restarting (1) 45 seconds ago |
| omni-migrator | Exited (0) 2 days ago |
| omni-postgres | Exited (0) 2 days ago |
| omni-redis | Exited (0) 2 days ago |
| homepage-nginx | Up About an hour |
| homepage | Up About an hour (healthy) |
| relay | Up 7 minutes |
| astro-poo-site | Up About an hour |
| astro-tredtt | Up About an hour |
| astro-test-portfolio | Up About an hour |
| astro-my-landing-page | Up About an hour |
| site-creator | Up About an hour |
| memos | Up About an hour |
| astro-fresh | Up About an hour |
|  | Exited (0) 3 days ago |
| production-task | Up About an hour (healthy) |
| excalidraw | Up About an hour (healthy) |
| freshrss | Up About an hour |
| prometheus | Up About an hour |
| node-exporter | Up About an hour |
| cronmaster | Up About an hour |
| filebrowser | Up About an hour (healthy) |
| dashdot | Up About an hour |
| n8n | Up About an hour |
| grafana-otel | Up About an hour |
| otel-collector | Up About an hour |
| nginxproxy | Up About an hour |
| portainer | Up About an hour |
| jaeger | Up About an hour |
| openmemory-openmemory-1 | Up About an hour (healthy) |

## Recent Actions


## Errors Detected

### omni-indexer
```
Error: Failed to create database pool: Connection error: error communicating with database: failed to lookup address information: Temporary failure in name resolution
Error: Failed to create database pool: Connection error: error communicating with database: failed to lookup address information: Temporary failure in name resolution
Error: Failed to create database pool: Connection error: error communicating with database: failed to lookup address information: Temporary failure in name resolution
```

### omni-ai
```
[2026-03-05 09:29:47,853] [ERROR] [main:startup_event] Failed to initialize services: [Errno -3] Temporary failure in name resolution
ERROR:    Traceback (most recent call last):
    raise last_error or exceptions.TargetServerAttributeNotMatched(
```

### omni-connector-manager
```
Error: Failed to create database pool: Connection error: error communicating with database: failed to lookup address information: Temporary failure in name resolution
Error: Failed to create database pool: Connection error: error communicating with database: failed to lookup address information: Temporary failure in name resolution
Error: Failed to create database pool: Connection error: error communicating with database: failed to lookup address information: Temporary failure in name resolution
```

### omni-searcher
```
Error: Failed to create database pool: Connection error: error communicating with database: failed to lookup address information: Temporary failure in name resolution
Error: Failed to create database pool: Connection error: error communicating with database: failed to lookup address information: Temporary failure in name resolution
Error: Failed to create database pool: Connection error: error communicating with database: failed to lookup address information: Temporary failure in name resolution
```

### relay
```
[relay] Failed to record action: 'statistics'
```


## Summary

- **Running Containers**: 48
- **Exited Containers**: 4
- **Pending Flows**: 0
- **Errors Found**: 5

---
*Generated automatically by system-audit.sh*