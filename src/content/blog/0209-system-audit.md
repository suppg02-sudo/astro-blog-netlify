---
pubDatetime: 2026-03-02T02:09:48Z
title: "System Audit Report"
postSlug: "0209-system-audit"
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

| relay | Up 10 minutes |
| astro-poo-site | Up 10 minutes |
| astro-tredtt | Up 10 minutes |
| astro-test-portfolio | Up 10 minutes |
| astro-my-landing-page | Up 10 minutes |
| site-creator | Up 10 minutes |
| hugo | Up 10 minutes |
| memos | Up 10 minutes |
| astro-fresh | Up 10 minutes |
|  | Exited (0) 8 hours ago |
| olivetin | Up 10 minutes (healthy) |
| research-task | Up 10 minutes (healthy) |
| production-task | Up 10 minutes (healthy) |
| excalidraw | Up 10 minutes (healthy) |
| nextexplorer | Up 10 minutes (healthy) |
| homepage-nginx | Up 10 minutes |
| homepage | Up 10 minutes (healthy) |
| freshrss | Up 10 minutes |
| prometheus | Up 10 minutes |
| node-exporter | Up 10 minutes |
| cronmaster | Up 10 minutes |
| fossflow | Exited (137) 24 hours ago |
| filebrowser | Up 10 minutes (healthy) |
| dashdot | Up 10 minutes |
| n8n | Up 10 minutes |
| grafana-otel | Up 10 minutes |
| otel-collector | Up 10 minutes |
| nginxproxy | Up 10 minutes |
| portainer | Up 10 minutes |
| jaeger | Up 10 minutes |
| openmemory-openmemory-1 | Up 10 minutes (healthy) |

## Recent Actions


## Errors Detected

### memos
```
2026/03/02 02:07:29 INFO client error method=/memos.api.v1.AuthService/GetCurrentUser error="unauthenticated: authentication required"
```

### astro-fresh
```
02:00:25 [WARN] [router] A collision will result in an hard error in following versions of Astro.
```

### n8n
```
Failed to start Python task runner in internal mode. because Python 3 is missing from this system. Launching a Python runner in internal mode is intended only for debugging and is not recommended for production. Users are encouraged to deploy in external mode. See: https://docs.n8n.io/hosting/configuration/task-runners/#setting-up-external-mode
Task runner connection attempt failed with status code 403
Task runner connection attempt failed with status code 403
```

### grafana-otel
```
logger=plugins.update.checker t=2026-03-02T02:00:16.178541939Z level=info msg="flag evaluation succeeded" flag="{Value:false EvaluationDetails:{FlagKey:pluginsAutoUpdate FlagType:bool ResolutionDetail:{Variant:default Reason:STATIC ErrorCode: ErrorMessage: FlagMetadata:map[]}}}" details="{Value:false EvaluationDetails:{FlagKey:pluginsAutoUpdate FlagType:bool ResolutionDetail:{Variant:default Reason:STATIC ErrorCode: ErrorMessage: FlagMetadata:map[]}}}"
```

### otel-collector
```
2026-03-02T01:59:56.854Z	info	healthcheckextension@v0.146.0/healthcheckextension.go:32	Starting health_check extension	{"resource": {"service.instance.id": "6652bb5c-0e5a-4385-a4b7-4d06670b6477", "service.name": "otelcol-contrib", "service.version": "0.146.1"}, "otelcol.component.id": "health_check", "otelcol.component.kind": "extension", "config": {"NetAddr":{"Endpoint":"0.0.0.0:13133","Transport":"tcp","DialerConfig":{"Timeout":0}},"TLS":{},"CORS":{},"Auth":{},"MaxRequestBodySize":0,"IncludeMetadata":false,"ResponseHeaders":null,"CompressionAlgorithms":null,"ReadTimeout":0,"ReadHeaderTimeout":0,"WriteTimeout":0,"IdleTimeout":0,"Middlewares":null,"KeepAlivesEnabled":false,"Path":"/","ResponseBody":null,"CheckCollectorPipeline":{"Enabled":false,"Interval":"5m","ExporterFailureThreshold":5},"UseV2":false,"GRPCConfig":null,"HTTPConfig":null,"ComponentHealthConfig":null}}
```


## Summary

- **Running Containers**: 29
- **Exited Containers**: 2
- **Pending Flows**: 0
- **Errors Found**: 5

---
*Generated automatically by system-audit.sh*