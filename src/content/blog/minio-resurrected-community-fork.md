---
pubDatetime: 2026-02-27T22:30:00Z
title: "MinIO Is Dead, Long Live MinIO: The Community Fork Rises"
postSlug: "minio-resurrected-community-fork"
description: "MinIO Is Dead, Long Live MinIO: The Community Fork Rises"
tags:
  - supply-chain
  - minio
  - fork
  - open-source
  - s3
---

On February 12, 2026, MinIO officially archived its GitHub repository—marking the end of an era for one of the most popular open-source S3-compatible object storage solutions. With over 60,000 GitHub stars and more than a billion Docker pulls, MinIO's demise sent shockwaves through the infrastructure community.

But open source doesn't die that easily.

## The Death Certificate

MinIO's decline wasn't sudden—it was a slow, deliberate wind-down over 18 months:

| Date | Event | Nature |
|------|-------|--------|
| 2021-05 | Apache 2.0 → AGPL v3 | License change |
| 2022-07 | Legal action against Nutanix | License enforcement |
| 2023-03 | Legal action against Weka | License enforcement |
| 2025-05 | Admin console removed from CE | Feature restriction |
| 2025-10 | Binary/Docker distribution stopped | Supply chain cut |
| 2025-12 | Maintenance mode announced | End-of-life signal |
| 2026-02 | Repo archived, no longer maintained | End of project |

A company that raised $126M at a billion-dollar valuation spent five years methodically dismantling the open-source ecosystem it built.

## The Resurrection

**Ruohang Feng** (Pigsty Founder) forked MinIO and restored it to life. The community fork at [`pgsty/minio`](https://github.com/pgsty/minio) addresses three critical issues:

### 1. Restored the Admin Console

In May 2025, MinIO stripped the full admin console from the community edition, leaving only a bare-bones object browser. User management, bucket policies, access control, lifecycle management—all gone. The fork brought it back.

### 2. Rebuilt Binary Distribution

MinIO stopped distributing pre-built binaries and Docker images in October 2025. The fork restored:

- **Docker Images**: `pgsty/minio` on Docker Hub
- **RPM/DEB Packages**: For major Linux distributions
- **CI/CD Pipeline**: Fully automated build workflows

### 3. Restored Documentation

MinIO's official docs started redirecting to their commercial product (AIStor). The fork preserved the community documentation at `silo.pigsty.io`.

## Migration Path

**Drop-in replacement**: Just swap `minio/minio` → `pgsty/minio`

```bash
# Docker
docker pull pgsty/minio

# Linux (via pig package manager)
curl https://repo.pigsty.io/pig | bash
pig repo add infra -u
pig install minio
```

## Key Lessons

### AGPL Cuts Both Ways

MinIO switched from Apache 2.0 to AGPL to use it as leverage in legal disputes. But open-source licenses are irrevocable—once code is released under AGPL, the community's right to fork is guaranteed.

> A company can abandon a project, but it can't take the code with it.

### Supply Chain Stability Matters

For most users, the value of open-source software isn't just the source code—it's having stable artifacts for Dockerfiles, Ansible playbooks, and CI/CD pipelines.

### AI Changed the Game

With AI coding tools, the cost of maintaining a complex infrastructure fork has dropped by an order of magnitude. What once required a dedicated team can now be handled by one experienced engineer with an AI copilot.

## Fork It

`git clone` is the most powerful spell in open source. When a company decides to shut the door, the community only needs two words:

**Fork it.**

---

*Source: [MinIO Is Dead, Long Live MinIO](https://blog.vonng.com/en/db/minio-resurrect/) by Ruohang Feng*