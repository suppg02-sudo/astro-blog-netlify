---
pubDatetime: 2026-03-01T21:25:25Z
title: "System Audit Report"
postSlug: "2125-system-audit"
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

| astro-poo-site | Up 55 minutes |
| astro-tredtt | Up About an hour |
| astro-test-portfolio | Up About an hour |
| astro-my-landing-page | Up 2 hours |
| site-creator | Up 2 hours |
| hugo | Up 2 hours |
| memos | Up 3 hours |
| astro-fresh | Up 3 hours |
|  | Exited (0) 3 hours ago |
| olivetin | Up 46 minutes (healthy) |
| relay | Up 3 hours |
| research-task | Up 3 hours (healthy) |
| production-task | Up 3 hours (healthy) |
| excalidraw | Up 3 hours (healthy) |
| nextexplorer | Up 3 hours (healthy) |
| homepage-nginx | Up 2 hours |
| homepage | Up 2 hours (healthy) |
| freshrss | Up 3 hours |
| prometheus | Up 3 hours |
| node-exporter | Up 3 hours |
| cronmaster | Up 3 hours |
| fossflow | Exited (137) 19 hours ago |
| filebrowser | Up 3 hours (healthy) |
| dashdot | Up 3 hours |
| n8n | Up 3 hours |
| grafana-otel | Up 3 hours |
| otel-collector | Up 3 hours |
| nginxproxy | Up 3 hours |
| portainer | Up 3 hours |
| jaeger | Up 3 hours |
| openmemory-openmemory-1 | Up 2 hours (healthy) |

## Recent Actions


## Errors Detected

### grafana-otel
```
logger=plugins.update.checker t=2026-03-01T21:20:19.412651529Z level=info msg="flag evaluation succeeded" flag="{Value:false EvaluationDetails:{FlagKey:pluginsAutoUpdate FlagType:bool ResolutionDetail:{Variant:default Reason:STATIC ErrorCode: ErrorMessage: FlagMetadata:map[]}}}" details="{Value:false EvaluationDetails:{FlagKey:pluginsAutoUpdate FlagType:bool ResolutionDetail:{Variant:default Reason:STATIC ErrorCode: ErrorMessage: FlagMetadata:map[]}}}"
```


## Summary

- **Running Containers**: 29
- **Exited Containers**: 2
- **Pending Flows**: 0
- **Errors Found**: 1

---
*Generated automatically by system-audit.sh*