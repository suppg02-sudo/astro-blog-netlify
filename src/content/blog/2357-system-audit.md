---
pubDatetime: 2026-03-01T23:57:03Z
title: "System Audit Report"
postSlug: "2357-system-audit"
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

| relay | Up 2 minutes |
| astro-poo-site | Up 3 hours |
| astro-tredtt | Up 4 hours |
| astro-test-portfolio | Up 4 hours |
| astro-my-landing-page | Up 4 hours |
| site-creator | Up 4 hours |
| hugo | Up 2 hours |
| memos | Up 5 hours |
| astro-fresh | Up 5 hours |
|  | Exited (0) 6 hours ago |
| olivetin | Up 19 minutes (healthy) |
| research-task | Up 6 hours (healthy) |
| production-task | Up 6 hours (healthy) |
| excalidraw | Up 6 hours (healthy) |
| nextexplorer | Up 6 hours (healthy) |
| homepage-nginx | Up 16 minutes |
| homepage | Up 4 minutes (healthy) |
| freshrss | Up 6 hours |
| prometheus | Up 6 hours |
| node-exporter | Up 6 hours |
| cronmaster | Up 6 hours |
| fossflow | Exited (137) 22 hours ago |
| filebrowser | Up 6 hours (healthy) |
| dashdot | Up 6 hours |
| n8n | Up 6 hours |
| grafana-otel | Up 6 hours |
| otel-collector | Up 6 hours |
| nginxproxy | Up 6 hours |
| portainer | Up 6 hours |
| jaeger | Up 6 hours |
| openmemory-openmemory-1 | Up 4 hours (healthy) |

## Recent Actions


## Errors Detected

### relay
```
Error response from daemon: can not get logs from container which is dead or marked for removal
```

### homepage-nginx
```
2026/03/01 23:52:31 [error] 22#22: *5 connect() failed (111: Connection refused) while connecting to upstream, client: 100.82.161.63, server: _, request: "GET /api/widgets/resources?type=cpu HTTP/1.1", upstream: "http://172.26.0.2:3000/api/widgets/resources?type=cpu", host: "ubuntu4:8765", referrer: "http://ubuntu4:8765/"
2026/03/01 23:52:31 [error] 22#22: *1837 connect() failed (111: Connection refused) while connecting to upstream, client: 100.66.217.37, server: _, request: "GET /api/services/proxy?group=%F0%9F%93%A6&service=Hacker+News&index=0&query=%7B%22refreshInterval%22%3A10000%7D HTTP/1.1", upstream: "http://172.26.0.2:3000/api/services/proxy?group=%F0%9F%93%A6&service=Hacker+News&index=0&query=%7B%22refreshInterval%22%3A10000%7D", host: "ubuntu4:8765", referrer: "http://ubuntu4:8765/"
2026/03/01 23:52:31 [error] 22#22: *1837 connect() failed (111: Connection refused) while connecting to upstream, client: 100.66.217.37, server: _, request: "GET /api/widgets/resources?type=cpu HTTP/1.1", upstream: "http://172.26.0.2:3000/api/widgets/resources?type=cpu", host: "ubuntu4:8765", referrer: "http://ubuntu4:8765/"
```

### grafana-otel
```
logger=plugins.update.checker t=2026-03-01T23:50:19.57133085Z level=info msg="flag evaluation succeeded" flag="{Value:false EvaluationDetails:{FlagKey:pluginsAutoUpdate FlagType:bool ResolutionDetail:{Variant:default Reason:STATIC ErrorCode: ErrorMessage: FlagMetadata:map[]}}}" details="{Value:false EvaluationDetails:{FlagKey:pluginsAutoUpdate FlagType:bool ResolutionDetail:{Variant:default Reason:STATIC ErrorCode: ErrorMessage: FlagMetadata:map[]}}}"
```


## Summary

- **Running Containers**: 29
- **Exited Containers**: 2
- **Pending Flows**: 0
- **Errors Found**: 3

---
*Generated automatically by system-audit.sh*