---
pubDatetime: 2026-03-15T20:24:59Z
title: "Server Database Inventory: Active Databases and Recent Activity"
postSlug: "server-database-inventory-active-databases"
description: "Server Database Inventory: Active Databases and Recent Activity"
tags:
  - postgresql
  - sqlite
  - redis
  - database
  - docker
  - server-management
---

## Overview

A comprehensive inventory of all databases on the server that have been accessed or modified in the last 2 days. This inventory covers PostgreSQL containers, SQLite databases, Redis instances, and system-level databases.

---

## Running Database Containers

The following database containers are currently active:

| Container | Image | Purpose |
|-----------|-------|---------|
| `supermarket-scraper-postgres` | postgres:15-alpine | UK Supermarket Store Scraper data |
| `litellm-postgres` | postgres:15-alpine | LiteLLM usage tracking |
| `directus-postgres` | pgvector/pgvector:pg15 | Directus CMS with vector support |
| `directus-redis` | redis:7-alpine | Directus caching layer |
| `rag-postgres` | pgvector/pgvector:pg15 | RAG document retrieval with embeddings |

---

## PostgreSQL Databases

### Port Configuration
- **PostgreSQL**: `5432` (standard port, listening on all interfaces)
- **MinIO Console**: `9000` (S3-compatible storage)

### Container Details

**supermarket-scraper-postgres**
- Stores UK supermarket location data (Tesco, Morrisons, Sainsburys, Coop, Iceland)
- 11,398+ store records

**litellm-postgres**
- Tracks LLM API usage and costs
- Request/response logging

**directus-postgres**
- CMS backend with pgvector extension
- Supports vector similarity search

**rag-postgres**
- Document embeddings storage
- Vector search for RAG applications

---

## SQLite Databases (Modified in Last 48 Hours)

### Docker Volumes (`/var/lib/docker/volumes/`)

| Database | Purpose |
|----------|---------|
| `npm_data/database.sqlite` | Nginx Proxy Manager configuration |
| `opentelemetry-stack_grafana-data/grafana.db` | Grafana dashboards and settings |
| `portainer_data/portainer.db` | Portainer container management |
| `filebrowser_db/filebrowser.db` | FileBrowser user/file tracking |
| `containerd/metadata.db` | Container runtime metadata |
| `docker/buildkit/cache.db` | Docker build cache |
| `docker/network/files/local-kv.db` | Docker network state |
| `docker/volumes/metadata.db` | Docker volume tracking |

### Application Data (`/media/docker/`)

| Database | Purpose |
|----------|---------|
| `adguard/work/data/stats.db` | AdGuard DNS filtering statistics |
| `freshrss/data/users/admin/db.sqlite` | FreshRSS feed reader data |

### User/Application Databases (`/root/`)

| Database | Purpose |
|----------|---------|
| `.local/share/opencode/opencode.db` | OpenCode session and configuration data |
| `uk-supermarket-scraper/stores.db` | Supermarket store records |
| `uk-supermarket-scraper/data/supermarket_stores.db` | Processed store data |
| `research/crustal-displacement/evidence.db` | Crustal displacement research database |

---

## Redis Instances

**directus-redis**
- Image: redis:7-alpine
- Purpose: Caching layer for Directus CMS
- Improves response times for frequently accessed content

---

## System Databases

### Container Runtime
- `containerd` metadata databases for container state
- Docker BuildKit cache database
- Docker network and volume metadata

### Package Management
- `/var/lib/command-not-found/commands.db` - Command suggestions for uninstalled packages

---

## Database Access Patterns

### High-Activity Databases (Based on Recent Modifications)

1. **OpenCode Database** - Session tracking, configuration changes
2. **Portainer Database** - Container management operations
3. **Grafana Database** - Dashboard updates, metric queries
4. **Supermarket Scraper Databases** - Active data collection
5. **AdGuard Stats Database** - DNS query logging

### Vector-Enabled Databases

Two PostgreSQL containers have pgvector extension:
- **directus-postgres**: Vector search for CMS content
- **rag-postgres**: Document embeddings for RAG applications

---

## Network Configuration

| Port | Service | Status |
|------|---------|--------|
| 5432 | PostgreSQL | Listening (IPv4 + IPv6) |
| 9000 | MinIO Console | Listening (IPv4 + IPv6) |
| 6379 | Redis | Container-internal |
| 27017 | MongoDB | Not in use |
| 3306 | MySQL | Not in use |
| 9200 | OpenSearch | Not in use |

---

## Recommendations

### Backup Priorities

1. **Critical**: PostgreSQL containers (supermarket-scraper, directus, rag)
2. **Important**: SQLite databases in Docker volumes (portainer, grafana)
3. **Configuration**: Nginx Proxy Manager database

### Maintenance Notes

- SQLite databases should be vacuumed periodically
- PostgreSQL containers should have WAL archiving configured
- Redis persistence should be verified for Directus cache

---

## Quick Reference Commands

```bash
# List running database containers
docker ps | grep -iE 'postgres|mysql|mongo|redis'

# Check PostgreSQL databases (from container)
docker exec -it <container> psql -U postgres -c "\l"

# Find recently modified SQLite files
find / -name "*.db" -mtime -2 2>/dev/null

# Check listening database ports
ss -tuln | grep -E '5432|3306|6379|27017'
```

---

*Inventory generated on 2026-03-15*