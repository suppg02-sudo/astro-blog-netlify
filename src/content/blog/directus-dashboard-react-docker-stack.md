---
pubDatetime: 2026-03-24T12:34:41Z
title: "Building a Real-Time Dashboard with Directus, React, and Docker"
postSlug: "directus-dashboard-react-docker-stack"
description: "Building a Real-Time Dashboard with Directus, React, and Docker"
tags:
  - directus
  - tailwind
  - dashboard
  - docker
  - headless-cms
  - react
---

I recently set up a custom dashboard powered by Directus as a headless CMS backend. This post documents the complete stack architecture, the technologies used, and the decisions made along the way.

## Why Directus for a Dashboard?

Directus is an open-source headless CMS that wraps any SQL database with an intuitive API. For dashboards, it offers several advantages:

- **Real-time data sync** - Built-in WebSocket support for live updates
- **REST + GraphQL APIs** - Flexible data querying options
- **Role-based permissions** - Fine-grained access control
- **No vendor lock-in** - Your data stays in PostgreSQL, portable anywhere

## The Complete Stack

{{< mermaid >}}
graph TB
    subgraph "Client Layer"
        A[React Dashboard<br/>Port 8056]
    end
    
    subgraph "API Layer"
        B[Directus CMS<br/>Port 8055]
        C[Redis Cache]
    end
    
    subgraph "Data Layer"
        D[PostgreSQL + pgvector<br/>Port 5432]
    end
    
    A -->|REST/GraphQL| B
    B --> C
    B --> D
    
    style A fill:#61dafb,color:#fff
    style B fill:#64d4ff,color:#fff
    style C fill:#dc382d,color:#fff
    style D fill:#336791,color:#fff
{{< /mermaid >}}

## Container Architecture

The stack runs as **four Docker containers** orchestrated via docker-compose:

| Container | Image | Port | Purpose |
|-----------|-------|------|---------|
| `directus` | `directus/directus:11.15.4` | 8055 | Headless CMS API |
| `directus-postgres` | `pgvector/pgvector:pg15` | 5432 | Database with vector support |
| `directus-redis` | `redis:7-alpine` | 6379 | Caching layer |
| `directus-dashboard` | Custom (nginx) | 8056 | React frontend |

## Frontend: React + Vite + Tailwind

The dashboard frontend is built with modern tooling:

### Tech Stack

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "framer-motion": "^11.0.0",
    "@dnd-kit/core": "^6.3.1",
    "@dnd-kit/sortable": "^10.0.0",
    "lucide-react": "^0.344.0"
  },
  "devDependencies": {
    "typescript": "^5.4.0",
    "vite": "^5.1.0",
    "tailwindcss": "^3.4.1"
  }
}
```

### Key Features

- **Framer Motion** - Smooth animations for widget interactions
- **@dnd-kit** - Drag-and-drop for customizable dashboard layouts
- **Lucide React** - Beautiful, consistent iconography
- **Tailwind CSS** - Utility-first styling with dark mode support

### Build Pipeline

The dashboard uses a multi-stage Docker build:

```dockerfile
# Build stage
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install --legacy-peer-deps
COPY . .
RUN npm run build

# Production stage
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
```

This produces a lean ~25MB production image serving static assets via nginx.

## Backend: Directus Configuration

The Directus CMS is configured via environment variables:

```yaml
environment:
  - DB_CLIENT=pg
  - DB_HOST=postgres
  - DB_PORT=5432
  - DB_DATABASE=directus
  - CACHE_ENABLED=true
  - CACHE_STORE=redis
  - CACHE_AUTO_PURGE=true
  - REDIS=redis://redis:6379
  - PUBLIC_URL=http://ubuntu4:8055
```

### Key Configuration Decisions

1. **pgvector PostgreSQL** - Enables vector similarity search for future AI features
2. **Redis caching** - Auto-purge on content changes keeps dashboard snappy
3. **CORS enabled** - Allows dashboard on port 8056 to communicate with API on 8055

## Networking

Both containers share the `directus_default` Docker network, allowing the dashboard to communicate with the Directus API via internal Docker networking:

```yaml
networks:
  directus_default:
    external: true
```

The dashboard accesses Directus at `http://directus:8055` internally.

## Access Points

| Service | URL | Purpose |
|---------|-----|---------|
| Dashboard | `http://ubuntu4:8056` | User-facing dashboard |
| Directus Admin | `http://ubuntu4:8056/admin` | Content management UI |
| Directus API | `http://ubuntu4:8055` | REST/GraphQL endpoints |

## Health Checks

All containers include health checks for reliability:

```yaml
healthcheck:
  test: ["CMD", "wget", "--spider", "http://127.0.0.1:8055/server/health"]
  interval: 30s
  timeout: 10s
  retries: 3
```

## Data Persistence

Docker volumes ensure data survives container restarts:

| Volume | Purpose |
|--------|---------|
| `directus-uploads` | File uploads and media |
| `directus-extensions` | Custom Directus extensions |
| `postgres-data` | Database persistence |
| `redis-data` | Cache persistence |

## Why This Stack Works

1. **Separation of concerns** - CMS, database, cache, and frontend are independently scalable
2. **Modern frontend tooling** - Vite + TypeScript + Tailwind = excellent DX
3. **Production-ready** - Health checks, logging limits, and proper caching
4. **Future-proof** - pgvector enables AI/ML features, Directus handles schema evolution

The entire stack can be deployed with a single `docker-compose up -d` and provides a solid foundation for building data-driven dashboards with real-time capabilities.

---

*Files referenced: [docker-compose.yml](http://ubuntu4:8080/editor/docker/directus/docker-compose.yml) | [Dockerfile](http://ubuntu4:8080/editor/docker/dashboard/app/Dockerfile) | [package.json](http://ubuntu4:8080/editor/docker/dashboard/app/package.json)*