---
pubDatetime: 2026-03-05T20:55:01Z
title: "System Audit Report"
postSlug: "2055-system-audit"
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

| olivetin | Up About an hour (healthy) |
| litellm-postgres | Up 2 hours (healthy) |
| pgadmin | Up 2 hours |
| directus-postgres | Up 4 hours (healthy) |
| directus | Up 4 hours (healthy) |
| directus-redis | Up 4 hours (healthy) |
| rag-postgres | Up 4 hours (healthy) |
| hugo | Up 4 hours |
| research-task | Up 4 hours (healthy) |
| landing-page | Up 4 hours |
| fossflow | Up 4 hours |
| astro-tshirt-sales | Up 4 hours |
| openmemory-dashboard | Up 4 hours |
| astro-vector | Up 4 hours |
| flows-app | Up 4 hours (healthy) |
| nextexplorer | Up 4 hours (healthy) |
| omni-web | Up 4 hours |
| omni-caddy | Up 4 hours |
| omni-sandbox | Up 4 hours (healthy) |
| omni-web-connector | Up 4 hours |
| omni-slack-connector | Up 4 hours |
| omni-indexer | Restarting (1) 31 seconds ago |
| omni-ai | Up 4 hours |
| omni-connector-manager | Restarting (1) 36 seconds ago |
| omni-searcher | Restarting (1) 53 seconds ago |
| omni-migrator | Exited (0) 3 days ago |
| omni-postgres | Exited (0) 2 days ago |
| omni-redis | Exited (0) 2 days ago |
| homepage-nginx | Up 4 hours |
| homepage | Up 4 hours (healthy) |
| relay | Up 4 hours |
| astro-poo-site | Up 4 hours |
| astro-tredtt | Up 4 hours |
| astro-test-portfolio | Up 4 hours |
| astro-my-landing-page | Up 4 hours |
| site-creator | Up 4 hours |
| memos | Up 4 hours |
| astro-fresh | Up 4 hours |
|  | Exited (0) 4 days ago |
| production-task | Up 4 hours (healthy) |
| excalidraw | Up 4 hours (healthy) |
| freshrss | Up 4 hours |
| prometheus | Up 4 hours |
| node-exporter | Up 4 hours |
| cronmaster | Up 4 hours |
| filebrowser | Up 4 hours (healthy) |
| dashdot | Up 4 hours |
| n8n | Up 4 hours |
| grafana-otel | Up 4 hours |
| otel-collector | Up 4 hours |
| nginxproxy | Up 4 hours |
| portainer | Up 4 hours |
| jaeger | Up 4 hours |
| openmemory-openmemory-1 | Up 4 hours (healthy) |

## Recent Actions


## Errors Detected

### omni-indexer
```
Error: Failed to create database pool: Connection error: error communicating with database: failed to lookup address information: Temporary failure in name resolution
Error: Failed to create database pool: Connection error: error communicating with database: failed to lookup address information: Temporary failure in name resolution
Error: Failed to create database pool: Connection error: error communicating with database: failed to lookup address information: Temporary failure in name resolution
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


## Summary

- **Running Containers**: 50
- **Exited Containers**: 4
- **Pending Flows**: 0
- **Errors Found**: 3

---
*Generated automatically by system-audit.sh*