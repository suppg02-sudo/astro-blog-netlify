---
pubDatetime: 2026-04-04T17:24:36Z
title: "Architecture Review — 52 Containers, 8GB RAM, One Server"
postSlug: "architecture-review-52-contain"
description: "Architecture Review — 52 Containers, 8GB RAM, One Server"
tags:
  - others
---

> **TL;DR**: Ambitious AI infrastructure with excellent documentation, but showing growth strain — swap at 92%, principle violations, and 7 idle Astro containers wasting resources. Overall score: 5.7/10.

## Quick Summary

- **52 containers** on 8GB RAM with swap at 92% — OOM risk is imminent
- **Kestra documented as orchestration owner** but not deployed; n8n + cron doing the work
- **6 PostgreSQL instances** with no consolidation strategy
- **7 idle Astro experiment containers** wasting ~50 MiB RAM and 1.2G disk
- **Schema Infrastructure v2.0 design** is excellent — composition/mixin pattern is solid
- **Blog pipeline is functional** — Post 842 live, auto-publishing working

---

## 🔴 Critical — Resource Pressure

### Memory Crisis (Imminent)

| Metric | Value | Risk |
|--------|-------|------|
| Total RAM | 7.7 GiB | — |
| Used | 4.9 GiB (64%) | ⚠️ |
| Swap | 3.7/4.0 GiB (92%) | 🔴 Critical |
| Available | 2.7 GiB | ⚠️ |

Swap at 92% is a ticking bomb. When swap fills, the OOM killer starts terminating containers.

### Heaviest Memory Consumers

| Container | Memory | % of Limit |
|-----------|--------|------------|
| neo4j | 313 MiB | 17% |
| hugo | 301 MiB | 16% |
| astro-blog | 220 MiB | 12% |
| directus | 173 MiB | 9% |
| grafana-otel | 92 MiB | 36% |
| n8n | 75 MiB | 29% |

### Disk at 80% (24G Free)

The biggest space consumers aren't running services — they're dormant projects:

| Directory | Size | Status |
|-----------|------|--------|
| `/media/docker/agent-starter-react/` | 1.5G | Unused |
| `/media/docker/link-in-bio-page-builder/` | 1.4G | Unused |
| `/media/docker/MoneyPrinterTurbo/` | 721M | Running, low value |
| `/media/docker/autogpt/` | 700M | Dormant |
| `/media/docker/livekit-agent/` | 597M | Dormant |
| **7 Astro test containers** | ~1.2G combined | Idle experiments |

---

## 🔴 Principle Violations — Docs vs Reality

### 1. Orchestration Ownership

**Stated** (environment.md, 2026-04-04):
> "Kestra owns ALL automation/orchestration. Directus is purely data + CMS."

**Reality**: Kestra is not running. n8n (port 5678), 47 cron jobs, and Paperclip (port 3100) are doing orchestration.

**Fix**: Either deploy Kestra, or update the principle to reflect n8n + cron as the actual orchestration layer.

### 2. Local-First AI

**Stated** (telos.md):
> "Local LLM inference via Ollama is primary AI compute layer"

**Reality**: No Ollama container. LiteLLM proxies to external providers. OpenRAG uses `text-embedding-3-small` (OpenAI).

**Fix**: Deploy Ollama or update telos.md to reflect "provider-first via LiteLLM."

### 3. Open Source by Default

OpenAI embedding model and z.ai GLM-5 are proprietary. No local embedding model deployed.

---

## 🟠 Data Layer — Fragmentation

Six separate database instances with no unified strategy:

| Database | Port | Purpose | Assessment |
|----------|------|---------|------------|
| pgvector-memory | internal | AI memory | ✅ Active |
| directus-postgres | internal | CMS data | ✅ Active |
| rag-postgres | 5433 | RAG metadata | ⚠️ Unknown usage |
| supermarket-postgres | 5434 | Store data | ⚠️ Low value |
| formbricks-postgres | internal | Surveys | ✅ Active |
| limesurvey-db | internal | Surveys | ⚠️ Duplicate survey tool |
| Neo4j | 7474/7687 | Graph | ⚠️ Unknown usage |
| OpenSearch | 9200 | RAG search | ❌ Not running |

<details>
<summary>📖 Deep Dive: Key Data Layer Issues</summary>

### Two Survey Tools
Formbricks AND LimeSurvey are both running. Pick one.

### rag-postgres Unclear
Port 5433 — unclear if still needed alongside pgvector-memory.

### Neo4j Undocumented
Running at 313 MiB but no documentation of what uses it.

### OpenSearch Missing
Documented in environment.md but NOT in docker ps output.

### No Redis for Semantic Caching
The redis-pgvector-hybrid-architecture.md doc recommends Redis for sub-millisecond semantic caching, but it's not deployed (only Directus and Formbricks have their own Redis instances).

</details>

---

## 🟠 Orchestration Layer — Too Many Cooks

| Layer | Technology | Status | Assessment |
|-------|-----------|--------|------------|
| Cron | 47 jobs | ✅ Running | Reliable but brittle |
| n8n | Port 5678 | ✅ Running | Visual workflows |
| Paperclip | Port 3100 | ✅ Running | Agent orchestration |
| Kestra | — | ❌ Not deployed | Documented as "owner" but missing |
| flows-app | — | ✅ Running | Unknown purpose |
| MeTube watcher | systemd | ✅ Running | Event-driven pipeline |

**Recommendation**: Consolidate to n8n (visual workflows) + cron (scheduled tasks). Drop the Kestra principle until you actually deploy it.

---

## 🟡 Content Pipeline — Proliferation

### 7 Astro Containers Running

| Container | Port | Purpose | Assessment |
|-----------|------|---------|------------|
| astro-blog | 3002 | Main blog | ✅ Keep |
| astro-fresh | 8086 | Experiment | ⚠️ Consolidate |
| astro-my-landing-page | 8087 | Experiment | ⚠️ Consolidate |
| astro-test-portfolio | 8088 | Experiment | ⚠️ Consolidate |
| astro-tredtt | 8089 | Experiment | ⚠️ Consolidate |
| astro-poo-site | 8091 | Experiment | 🔴 Stop |
| astro-tshirt-sales | 8093 | Experiment | ⚠️ Consolidate |
| astro-vector | 8092 | Experiment | ⚠️ Consolidate |

~1.2G disk + ~50 MiB RAM wasted on idle Astro experiments. These should be stopped and rebuilt on-demand.

### Content Flow (Working)

```
🔴 FreshRSS/MeTube/YouTube → 🟠 Transcription → 🟡 Summary → 🟢 Directus → 🔵 Astro Blog → 🟣 Telegram → ✅ Published
```

This pipeline is functional and producing content (Post 842 live).

---

## 🟡 Monitoring — Over-Engineered

| Tool | Port | Assessment |
|------|------|------------|
| Prometheus | 9090 | ✅ Keep |
| Node Exporter | 9100 | ✅ Keep |
| Grafana | 3003 | ✅ Keep |
| Jaeger | 16686 | ⚠️ Overkill for single server |
| OTel Collector | 4317/4318 | ⚠️ Overkill for single server |
| Dashdot | 3001 | ⚠️ Redundant with Grafana |
| Homepage | 8766 | ⚠️ Redundant |
| CronMaster | 40123 | ✅ Useful |

Jaeger + OTel are enterprise-grade distributed tracing tools. On a single-server setup, they add complexity without proportional value (~100 MiB RAM).

---

## 🟢 What's Working Well

- **TELOS constitution** — Excellent philosophical foundation with clear principles
- **Schema Infrastructure v2.0 design** — Composition/mixin pattern is solid, recursiveness applied correctly
- **Hub & Spoke AGENTS.md** — 1,637→293 lines reduction (5.6x), impressive context optimization
- **Skill system** — 69 skills with progressive disclosure and factory patterns
- **Memory system** — PostgreSQL + pgvector with `pghmem` CLI, 1,520 memories
- **Backup system** — Dual-location (SMB + local fallback), pgvector dumps, fast backups
- **Blog auto-publishing** — Daily Evolve Report auto-publishing is a genuine achievement
- **Tailscale networking** — Clean mesh network setup
- **AdGuard Home** — DNS filtering at the edge

---

## Architecture Scorecard

| Dimension | Score | Notes |
|-----------|-------|-------|
| Philosophy/Principles | 8/10 | Excellent TELOS, but docs ≠ reality |
| Documentation | 9/10 | Comprehensive, well-structured |
| Resource Efficiency | 4/10 | 52 containers on 8GB, swap at 92% |
| Data Architecture | 5/10 | 6 DBs, no consolidation strategy |
| Orchestration | 4/10 | 4 competing layers, principle violated |
| Content Pipeline | 7/10 | Working well, but experiment sprawl |
| Monitoring | 5/10 | Over-engineered for single server |
| Security | 7/10 | Tailscale, AdGuard, no secrets in code |
| Monetization | 3/10 | Blog producing content but no revenue streams |
| **Overall** | **5.7/10** | Strong foundation, needs consolidation |

---

## Recommendations — Prioritized

### Immediate (This Week)

| Priority | Action | Savings |
|----------|--------|---------|
| 🔴 | Stop 7 idle Astro containers | ~50 MiB RAM, 1.2G disk |
| 🔴 | Stop Jaeger + OTel Collector | ~100 MiB RAM |
| 🔴 | Pick one survey tool — kill LimeSurvey or Formbricks | ~25 MiB RAM, 200M disk |
| 🟠 | Deploy Ollama or update telos.md to reflect reality | — |
| 🟠 | Update orchestration principle — n8n + cron, not Kestra | — |
| 🟠 | Clear swap — identify and stop memory leaks | 3.7G swap freed |

### Short-Term (This Month)

| Priority | Action | Impact |
|----------|--------|--------|
| 🟠 | Deploy Redis for semantic caching | Query latency 50ms→1ms |
| 🟡 | Consolidate PostgreSQL instances | Reduce container count |
| 🟡 | Document Neo4j usage or remove it | 313 MiB RAM freed |
| 🟡 | Implement Schema Infrastructure v2.0 Phase 1 | Eliminate schema duplication |
| 🟡 | Add memory limits to all containers | System stability |

### Medium-Term (Quarter)

| Priority | Action | Impact |
|----------|--------|--------|
| 🟡 | Upgrade RAM — 8GB→16GB | Headroom for growth |
| 🟢 | Deploy local embedding model | Reduce OpenAI dependency |
| 🟢 | Deploy Kestra or formally adopt n8n | Orchestration clarity |
| 🟢 | Monetize content pipeline | Revenue generation |

---

*This architecture review was generated by automated analysis of the OpenCode ecosystem on 2026-04-04. All metrics are from live container inspection.*

**Tags**: architecture, infrastructure, review, docker, optimization, telos
**Categories**: AI Automation, Infrastructure