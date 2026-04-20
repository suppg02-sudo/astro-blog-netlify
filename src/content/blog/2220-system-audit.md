---
pubDatetime: 2026-03-01T22:20:25Z
title: "System Audit Report"
postSlug: "2220-system-audit"
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

| astro-poo-site | Up 2 hours |
| astro-tredtt | Up 2 hours |
| astro-test-portfolio | Up 2 hours |
| astro-my-landing-page | Up 3 hours |
| site-creator | Up 3 hours |
| hugo | Up 4 minutes |
| memos | Up 3 hours |
| astro-fresh | Up 4 hours |
|  | Exited (0) 4 hours ago |
| olivetin | Up 52 minutes (healthy) |
| relay | Up 4 hours |
| research-task | Up 4 hours (healthy) |
| production-task | Up 4 hours (healthy) |
| excalidraw | Up 4 hours (healthy) |
| nextexplorer | Up 4 hours (healthy) |
| homepage-nginx | Up 2 hours |
| homepage | Up 48 minutes (healthy) |
| freshrss | Up 4 hours |
| prometheus | Up 4 hours |
| node-exporter | Up 4 hours |
| cronmaster | Up 4 hours |
| fossflow | Exited (137) 20 hours ago |
| filebrowser | Up 4 hours (healthy) |
| dashdot | Up 4 hours |
| n8n | Up 4 hours |
| grafana-otel | Up 4 hours |
| otel-collector | Up 4 hours |
| nginxproxy | Up 4 hours |
| portainer | Up 4 hours |
| jaeger | Up 4 hours |
| openmemory-openmemory-1 | Up 3 hours (healthy) |

## Recent Actions


## Errors Detected

### grafana-otel
```
t=2026-03-01T22:13:50.368966821Z level=error caller=logger.go:234 time=2026-03-01T22:13:50.108486418Z msg="cleaning up inactive secure values" error="fetching inactive secure values that need to be cleaned up: acquiring leases for inactive secure values: leasing inactive secure values: context deadline exceeded"
logger=dashboards-k8s-client t=2026-03-01T22:15:25.521272485Z level=error msg="failed to fetch initial list" error="Get \"https://127.0.0.1:3000/apis/dashboard.grafana.app/v0alpha1/namespaces/default/dashboards?labelSelector=grafana.app%2Fget-trash%3Dtrue&limit=10&resourceVersion=0&resourceVersionMatch=NotOlderThan\": context canceled"
logger=dashboard-service t=2026-03-01T22:15:26.015397979Z level=error msg="Failed to cleanup k8s dashboard resources" error="org 1: failed to list resources: Get \"https://127.0.0.1:3000/apis/dashboard.grafana.app/v0alpha1/namespaces/default/dashboards?labelSelector=grafana.app%2Fget-trash%3Dtrue&limit=10&resourceVersion=0&resourceVersionMatch=NotOlderThan\": context canceled"
```


## Summary

- **Running Containers**: 29
- **Exited Containers**: 2
- **Pending Flows**: 0
- **Errors Found**: 1

---
*Generated automatically by system-audit.sh*