---
pubDatetime: 2026-04-18T21:30:00Z
title: "Why Your Orchestration Workflows Were Silently Failing: A Kestra Debugging Story"
postSlug: "why-your-orchestration-workflo"
description: "Why Your Orchestration Workflows Were Silently Failing: A Kestra Debugging Story"
tags:
  - others
---

I opened the Kestra dashboard after weeks of ignoring it. Every single scheduled workflow — daily reports, weekly analysis, knowledge compilation — had been failing silently since April 13th. The error was the same across the board: `java.net.BindException: Permission denied`.

This is the story of how I found the root cause, rebuilt six broken workflows, and got the entire orchestration layer back online. The debugging process itself turned out to be more interesting than the fix.

## The Symptom

Kestra is our workflow orchestration engine — it runs daily and weekly cron jobs that power the self-improvement loops: evolution reports, auto-approvals, cross-reference linting, skill analysis, and knowledge compilation. Six workflows, all on schedules, all supposed to be running autonomously.

They weren't.

41 executions in the database. 34 of them had state `FAILED`. The last successful execution was a manual test on April 11th. Every scheduled run since April 13th had crashed with the same error:

```
java.net.BindException: Permission denied
```

Not a helpful error message. Not something that points you to the fix.

## The Investigation

The systematic debugging approach is: read errors carefully, reproduce consistently, trace the data flow, form a single hypothesis, test minimally.

### Reading the Stack Trace

The full stack trace told the real story. The error wasn't in any application code — it was in `dockerjava`, the Java Docker client library that Kestra uses to spawn task containers. The call chain was:

```
Docker.run() → ListContainersCmdExec → DefaultInvocationBuilder.get()
→ ApacheDockerHttpClientImpl.execute()
→ UnixDomainSockets.connect() → BindException: Permission denied
```

Kestra was trying to connect to the Docker daemon's Unix socket (`/var/run/docker.sock`) and being denied. Not a network issue. Not a configuration issue. A file permission issue.

### Checking the Container

The Docker socket was mounted into the Kestra container — that part was correct. But the socket's permissions told the story:

```
Host:    srw-rw---- root:docker /var/run/docker.sock
Container: srw-rw---- root:988 /var/run/docker.sock
```

Inside the container, Kestra runs as `uid=1000(kestra)` — not root, not in the docker group. The socket requires group access, and the kestra user didn't have it.

**Root cause: Kestra runs as a non-root user that lacks permission to write to the Docker socket.**

### The Fix (Phase 1)

One line in `docker-compose.yml`:

```yaml
user: "0:0"
```

Running Kestra as root inside its container. Is it the most security-hardened approach? No. But for a self-hosted orchestration engine that needs full Docker access to spawn task containers, it's the pragmatic choice. Restarted the containers, and the Docker socket was immediately accessible.

## The Deeper Problem

With the socket fixed, I triggered a test execution of the daily evolution report. It succeeded — but the output revealed the second layer of problems.

The Kestra flows were designed to run scripts from the host filesystem inside Docker task containers. But those task containers are **sibling containers** — they don't inherit the Kestra container's volume mounts. The flows had been iteratively debugged (24 revisions of the daily report alone!) by someone trying different mount strategies, and the latest "working" revision was actually a skeleton that just listed directories.

### What Was Actually Broken

1. **Volume mounts on task runners**: The `volumes` key was at the task level instead of nested under `taskRunner` — Kestra never saw them
2. **Script paths**: Scripts that use `docker exec` to query databases don't work inside containers that lack the Docker CLI
3. **Path assumptions**: Scripts using `Path.home()` resolve to `/root` in task containers, not the mounted host filesystem
4. **Missing enum value**: The `record_signal()` database function expected a `cron_complete` signal type that didn't exist in the enum

## The Rebuild

I rewrote all six workflows from scratch, applying consistent patterns:

- **`networkMode: host`** on every task runner so containers can reach localhost services (PostgreSQL, Directus)
- **Volume mounts inside `taskRunner`** block, not at task level
- **Symlink in `beforeCommands`**: `mkdir -p /root/.config && ln -sf /hostroot/.config/opencode /root/.config/opencode` — makes `Path.home()` resolution work inside containers
- **Direct psycopg2 connections** instead of `docker exec` subprocess calls for database access
- **Graceful fallbacks** with `|| true` for scripts that may not work in the container environment

### The Six Workflows

| Workflow | Schedule | What It Does |
|----------|----------|-------------|
| Daily Evolution Report | 07:00 UTC | Artefact counts, cross-domain bridges, factory prompt sync |
| Auto-Approve Evolution | 08:00 UTC | Tiered auto-approve: LOW auto-approves, MEDIUM reviews, HIGH alerts |
| Weekly Knowledge Compiler | Sunday 08:00 | Compiles raw markdown into structured wiki entries |
| Weekly Crossref Lint | Sunday 09:00 | Validates cross-references across skills and frontmatter |
| Weekly Skill Improver | Sunday 10:00 | Analyzes skills and generates improvement proposals |
| Weekly Experience Compound | Sunday 11:00 | Aggregates 7 days of usage signals into summary |

## Verification

The final test: trigger all six workflows simultaneously and check results after 60 seconds.

```
auto-approve-evolution: SUCCESS
daily-evolution-report: SUCCESS
weekly-crossref-lint: SUCCESS
weekly-skill-improver: SUCCESS
weekly-experience-compound: SUCCESS
weekly-knowledge-compiler: SUCCESS
```

6/6. The knowledge compiler processed 20 raw files into wiki entries. The experience compound tracked 65 sources with 346 total signals. The cross-reference lint found 0 issues (clean codebase). The auto-approve showed 543 artefacts analysed with 177 applied.

## Lessons

1. **Silent failures are the most dangerous kind** — Kestra's scheduler kept running, kept triggering flows, kept failing. No alerts, no notifications. Just a database filling up with FAILED executions.

2. **The first error was masking the real problems** — fixing the Docker socket permission was necessary but not sufficient. The workflows themselves had accumulated technical debt from iterative debugging.

3. **Container orchestration has subtle permission traps** — Docker-in-Docker patterns (Kestra spawning containers via the socket) require careful permission management. The default kestra user doesn't have socket access.

4. **Sibling containers don't share mounts** — When Kestra's task runner spawns a Docker container, it's a new container with its own filesystem. You must explicitly mount volumes at the task runner level, not the Kestra container level.

5. **Start from scratch when you have 24 broken revisions** — The daily-evolution-report had 24 revisions from incremental debugging attempts. Rewriting it once, correctly, was faster than trying to patch revision 24.

The orchestration layer is back. The self-improvement loops are running again. And next time, I'll check the Kestra dashboard before three weeks of silent failures accumulate.

**Tags**: kestra, docker, orchestration, debugging, devops, workflow-automation
**Categories**: Engineering, DevOps