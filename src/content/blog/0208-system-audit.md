---
pubDatetime: 2026-03-02T02:08:41Z
title: "System Audit Report"
postSlug: "0208-system-audit"
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

| relay | Up 9 minutes |
| astro-poo-site | Up 9 minutes |
| astro-tredtt | Up 9 minutes |
| astro-test-portfolio | Up 9 minutes |
| astro-my-landing-page | Up 9 minutes |
| site-creator | Up 9 minutes |
| hugo | Up 9 minutes |
| memos | Up 9 minutes |
| astro-fresh | Up 9 minutes |
|  | Exited (0) 8 hours ago |
| olivetin | Up 9 minutes (healthy) |
| research-task | Up 9 minutes (healthy) |
| production-task | Up 9 minutes (healthy) |
| excalidraw | Up 9 minutes (healthy) |
| nextexplorer | Up 9 minutes (healthy) |
| homepage-nginx | Up 9 minutes |
| homepage | Up 9 minutes (healthy) |
| freshrss | Up 9 minutes |
| prometheus | Up 9 minutes |
| node-exporter | Up 9 minutes |
| cronmaster | Up 9 minutes |
| fossflow | Exited (137) 24 hours ago |
| filebrowser | Up 9 minutes (healthy) |
| dashdot | Up 9 minutes |
| n8n | Up 9 minutes |
| grafana-otel | Up 9 minutes |
| otel-collector | Up 9 minutes |
| nginxproxy | Up 9 minutes |
| portainer | Up 9 minutes |
| jaeger | Up 9 minutes |
| openmemory-openmemory-1 | Up 9 minutes (healthy) |

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

### olivetin
```
level="warning" msg="Failed to read sessions.yaml file" error="open /config/sessions.yaml: no such file or directory"
```

### node-exporter
```
time=2026-03-02T01:59:37.793Z level=ERROR source=diskstats_linux.go:256 msg="Failed to open directory, disabling udev device properties" collector=diskstats path=/run/udev/data
```

### dashdot
```
Error: ENOENT: no such file or directory, lstat '/mnt/host/etc/os-release'
Cannot refresh /etc/os-release (os results may be outdated): Error: ENOENT: no such file or directory, lstat '/mnt/host/etc/os-release'
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
- **Errors Found**: 8

---
*Generated automatically by system-audit.sh*