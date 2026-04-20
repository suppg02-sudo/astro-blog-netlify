---
pubDatetime: 2026-03-04T00:55:03Z
title: "System Audit Report"
postSlug: "0055-system-audit"
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

| directus | Up About an hour (unhealthy) |
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
| omni-indexer | Restarting (1) 44 seconds ago |
| omni-ai | Up About an hour |
| omni-connector-manager | Restarting (1) 44 seconds ago |
| omni-searcher | Restarting (1) 45 seconds ago |
| omni-migrator | Exited (0) 39 hours ago |
| omni-postgres | Exited (0) 26 hours ago |
| omni-redis | Exited (0) 26 hours ago |
| homepage-nginx | Up 21 minutes |
| homepage | Up 21 minutes (healthy) |
| relay | Up About an hour |
| astro-poo-site | Up About an hour |
| astro-tredtt | Up About an hour |
| astro-test-portfolio | Up About an hour |
| astro-my-landing-page | Up About an hour |
| site-creator | Up About an hour |
| hugo | Up About an hour |
| memos | Up About an hour |
| astro-fresh | Up About an hour |
|  | Exited (0) 2 days ago |
| olivetin | Up 8 minutes (healthy) |
| research-task | Up About an hour (healthy) |
| production-task | Up About an hour (healthy) |
| excalidraw | Up About an hour (healthy) |
| freshrss | Up About an hour |
| prometheus | Up About an hour |
| node-exporter | Up About an hour |
| cronmaster | Up About an hour |
| fossflow | Exited (137) 2 days ago |
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
[2026-03-04 00:45:11,651] [ERROR] [main:startup_event] Failed to initialize services: [Errno -3] Temporary failure in name resolution
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

### olivetin
```
level="warning" msg="Failed to read sessions.yaml file" error="open /config/sessions.yaml: no such file or directory"
level="warning" msg="Failed to extract webhook arguments" actionTitle="🔄 Restart AI Stack" error="invalid character 'a' looking for beginning of value"
level="warning" msg="Failed to extract webhook arguments" actionTitle="🧹 Safe Docker Cleanup" error="invalid character 'a' looking for beginning of value"
```


## Summary

- **Running Containers**: 43
- **Exited Containers**: 5
- **Pending Flows**: 0
- **Errors Found**: 5

---
*Generated automatically by system-audit.sh*