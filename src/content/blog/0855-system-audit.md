---
pubDatetime: 2026-03-05T08:55:33Z
title: "System Audit Report"
postSlug: "0855-system-audit"
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

| rag-postgres | Up 19 minutes (healthy) |
| olivetin | Up 19 minutes (healthy) |
| hugo | Up 19 minutes |
| research-task | Up 19 minutes (healthy) |
| landing-page | Up 19 minutes |
| directus | Up 19 minutes (healthy) |
| fossflow | Up 19 minutes |
| astro-tshirt-sales | Up 19 minutes |
| openmemory-dashboard | Up 19 minutes |
| astro-vector | Up 19 minutes |
| directus-postgres | Up 19 minutes (healthy) |
| directus-redis | Up 19 minutes (healthy) |
| flows-app | Up 19 minutes (healthy) |
| nextexplorer | Up 19 minutes (healthy) |
| omni-web | Up 19 minutes |
| omni-caddy | Up 19 minutes |
| omni-sandbox | Up 19 minutes (healthy) |
| omni-web-connector | Up 19 minutes |
| omni-slack-connector | Up 19 minutes |
| omni-indexer | Restarting (1) 57 seconds ago |
| omni-ai | Up 19 minutes |
| omni-connector-manager | Restarting (1) 56 seconds ago |
| omni-searcher | Restarting (1) 59 seconds ago |
| omni-migrator | Exited (0) 2 days ago |
| omni-postgres | Exited (0) 2 days ago |
| omni-redis | Exited (0) 2 days ago |
| homepage-nginx | Up 19 minutes |
| homepage | Up 19 minutes (healthy) |
| relay | Up 19 minutes |
| astro-poo-site | Up 19 minutes |
| astro-tredtt | Up 19 minutes |
| astro-test-portfolio | Up 19 minutes |
| astro-my-landing-page | Up 19 minutes |
| site-creator | Up 19 minutes |
| memos | Up 19 minutes |
| astro-fresh | Up 19 minutes |
|  | Exited (0) 3 days ago |
| production-task | Up 19 minutes (healthy) |
| excalidraw | Up 19 minutes (healthy) |
| freshrss | Up 19 minutes |
| prometheus | Up 19 minutes |
| node-exporter | Up 19 minutes |
| cronmaster | Up 19 minutes |
| filebrowser | Up 19 minutes (healthy) |
| dashdot | Up 19 minutes |
| n8n | Up 19 minutes |
| grafana-otel | Up 19 minutes |
| otel-collector | Up 19 minutes |
| nginxproxy | Up 19 minutes |
| portainer | Up 19 minutes |
| jaeger | Up 19 minutes |
| openmemory-openmemory-1 | Up 19 minutes (healthy) |

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
[2026-03-05 08:45:42,755] [ERROR] [main:startup_event] Failed to initialize services: [Errno -3] Temporary failure in name resolution
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
[relay] Failed to record action: Extra data: line 15 column 1 (char 542)
```


## Summary

- **Running Containers**: 48
- **Exited Containers**: 4
- **Pending Flows**: 0
- **Errors Found**: 5

---
*Generated automatically by system-audit.sh*