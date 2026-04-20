---
pubDatetime: 2026-03-14T14:48:48Z
title: "Docker Containers Currently Running on Server"
postSlug: "docker-containers-running-20260314"
description: "Docker Containers Currently Running on Server"
tags:
  - homelab
  - containers
  - docker
  - infrastructure
---

A snapshot of all Docker containers currently running on the server. This post serves as a reference for the active services and their exposed ports.

## Summary

**Total containers running: 42**

## Container List

| # | Container | Image | Status | Port |
|---|-----------|-------|--------|------|
| 1 | homepage-nginx | nginx:alpine | Up 2h | 8766 |
| 2 | homepage | ghcr.io/gethomepage/homepage:latest | Up 2h (healthy) | 3000 |
| 3 | openmemory-dashboard-1 | openmemory-dashboard | Up 2h (healthy) | 13120 |
| 4 | supermarket-scraper-postgres | postgres:15-alpine | Up 2h (healthy) | 5434 |
| 5 | pgvector-memory | pgvector/pgvector:pg17 | Up 2h (healthy) | - |
| 6 | adguardhome | adguard/adguardhome:latest | Up 2h | 53, 853, 3353, 3443 |
| 7 | hugo | hugomods/hugo:exts | Up 2h | 1313 |
| 8 | relay | python:3.11-alpine | Up 2h | - |
| 9 | olivetin | jamesread/olivetin:latest | Up 2h (healthy) | 1337 |
| 10 | litellm-postgres | postgres:15-alpine | Up 2h (healthy) | - |
| 11 | pgadmin | dpage/pgadmin4:latest | Up 2h | 5050 |
| 12 | directus-postgres | pgvector/pgvector:pg15 | Up 2h (healthy) | - |
| 13 | directus | directus/directus:11.15.4 | Up 2h (healthy) | 8055 |
| 14 | directus-redis | redis:7-alpine | Up 2h (healthy) | - |
| 15 | rag-postgres | pgvector/pgvector:pg15 | Up 2h (healthy) | 5433 |
| 16 | research-task | python:3.11-slim | Up 2h (healthy) | - |
| 17 | landing-page | nginx:alpine | Up 2h | 8056 |
| 18 | fossflow | stnsmith/fossflow:latest | Up 2h | 3090 |
| 19 | astro-tshirt-sales | node:20-alpine | Up 2h | 8093 |
| 20 | astro-vector | node:20-alpine | Up 2h | 8092 |
| 21 | flows-app | python:3.11-slim | Up 2h (healthy) | - |
| 22 | astro-poo-site | node:20-alpine | Up 2h | 8091 |
| 23 | astro-tredtt | node:20-alpine | Up 2h | 8089 |
| 24 | astro-test-portfolio | node:20-alpine | Up 2h | 8088 |
| 25 | astro-my-landing-page | node:20-alpine | Up 2h | 8087 |
| 26 | site-creator | python:3.11-slim | Up 2h | 8090 |
| 27 | memos | neosmemo/memos:stable | Up 2h | 5230 |
| 28 | astro-fresh | node:20-alpine | Up 2h | 8086 |
| 29 | production-task | python:3.11-alpine | Up 2h (healthy) | - |
| 30 | excalidraw | excalidraw/excalidraw:latest | Up 2h (healthy) | 3765 |
| 31 | freshrss | freshrss/freshrss:latest | Up 2h | 8282 |
| 32 | prometheus | prom/prometheus:latest | Up 2h | 9090 |
| 33 | node-exporter | prom/node-exporter:latest | Up 2h | 9100 |
| 34 | cronmaster | ghcr.io/fccview/cronmaster:latest | Up 2h | 40123 |
| 35 | filebrowser | filebrowser/filebrowser:latest | Up 2h (healthy) | 2280 |
| 36 | dashdot | mauricenino/dashdot:latest | Up 2h | 3001 |
| 37 | n8n | docker.n8n.io/n8nio/n8n | Up 2h | 5678 |
| 38 | grafana-otel | grafana/grafana:latest | Up 2h | 3003 |
| 39 | otel-collector | otel/opentelemetry-collector-contrib | Up 2h | 4317-4318, 8889 |
| 40 | nginxproxy | jc21/nginx-proxy-manager:latest | Up 2h | - |
| 41 | portainer | portainer/portainer-ce:latest | Up 2h | 9000, 9443 |
| 42 | jaeger | jaegertracing/all-in-one:latest | Up 2h | 16686, 14268 |

## Service Categories

### Infrastructure & Monitoring
- **prometheus** - Metrics collection (9090)
- **grafana-otel** - Observability dashboard (3003)
- **jaeger** - Distributed tracing (16686)
- **otel-collector** - OpenTelemetry data collection
- **node-exporter** - System metrics exporter (9100)
- **dashdot** - System dashboard (3001)

### Databases
- **pgvector-memory** - PostgreSQL with pgvector (AI memory)
- **rag-postgres** - RAG database (5433)
- **directus-postgres** - Directus backend database
- **litellm-postgres** - LiteLLM database
- **supermarket-scraper-postgres** - Scraper data (5434)

### Web Services
- **homepage** - Dashboard homepage (8766 via nginx)
- **hugo** - Static site generator (1313)
- **directus** - Headless CMS (8055)
- **n8n** - Workflow automation (5678)
- **memos** - Note-taking (5230)
- **freshrss** - RSS reader (8282)
- **excalidraw** - Whiteboard (3765)
- **filebrowser** - File management (2280)

### DNS & Networking
- **adguardhome** - DNS filtering (53, 3353)
- **nginxproxy** - Reverse proxy manager
- **portainer** - Container management (9000, 9443)

### Development Tools
- **pgadmin** - PostgreSQL admin (5050)
- **olivetin** - Web-based command runner (1337)
- **cronmaster** - Cron job management (40123)
- **site-creator** - Site generation tool (8090)

### Astro Sites (Multiple)
- astro-tshirt-sales (8093)
- astro-vector (8092)
- astro-poo-site (8091)
- astro-tredtt (8089)
- astro-test-portfolio (8088)
- astro-my-landing-page (8087)
- astro-fresh (8086)

### Background Workers
- **relay** - Message relay service
- **research-task** - Research automation
- **production-task** - Production task runner
- **flows-app** - Workflow application

---

*Generated on 2026-03-14*