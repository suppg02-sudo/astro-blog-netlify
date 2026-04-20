---
pubDatetime: 2026-02-27T12:00:00Z
title: "Two Days of OpenCode Evolution: Sessions, Skills, and System Hardening"
postSlug: "opencode-sessions-evolution-feb-25-27"
description: "A comprehensive review of the last 48 hours working with OpenCode AI agent system - from context registry development to resource exhaustion protection."
tags:
  - sessions
  - skills
  - opencode
  - evolution
  - ai-agents
  - observability
  - devops
  - prompt
---

## Session Overview: Feb 25-27, 2026

The last two days represent a significant evolutionary leap for this OpenCode-powered server environment. This review captures the key developments, lessons learned, and the trajectory of the system.

---

## Key Developments

### 1. Context Registry & Progressive Disclosure

The most substantial work was on **context budget management** - a fundamental problem for AI agent systems.

**The Problem:** One skill file contained 8,317 lines. When agents load context for simple tasks, they were loading megabytes of documentation they didn't need.

**The Solution:** A four-level progressive disclosure system:

| Level | Name | When Loaded | Size Target |
|-------|------|-------------|-------------|
| 0 | Capability | Session start | ~2KB total |
| 1 | Metadata | On trigger | ~500B/skill |
| 2 | Working | On execution | 2-10KB |
| 3 | Reference | On demand | Unlimited |

**Result:** Published [42KB blog post](/posts/context-registry-progressive-disclosure-ai-agents) documenting the complete architecture.

### 2. Resource Exhaustion Protection

Running 24 containers on 1.8GB RAM required serious hardening.

**Initial State:**
- 402MB available memory (22% free)
- 60% swap usage
- 2.5x memory overcommit
- No OOM protection

**Solution:** 10-layer defense system including:
- Sysctl tuning (vm.min_free_kbytes, vm.swappiness)
- Tiered container memory limits (Critical/Important/Standard/Disposable)
- PSI (Pressure Stall Information) monitoring
- ZRAM compressed swap
- Early OOM warning system

**Result:** Zero unplanned OOM kills since implementation.

### 3. Server Performance Telemetry

Built automated performance reporting with Prometheus/Grafana stack:

- Real-time memory tracking
- Load average visualization
- Container memory allocation charts
- 30-minute rolling window analysis

### 4. Skill Ecosystem Growth

**13 skills updated** in last 48 hours:

| Skill | Purpose | Update Type |
|-------|---------|-------------|
| roundup | Daily automated reports | New skill |
| context-registry | Progressive disclosure | New skill |
| homepage | Dashboard management | Major update |
| opentelemetry | Observability stack | New skill |
| flow | Workflow orchestration | Enhanced |
| cron | Job management | Enhanced |
| performance | System analysis | Enhanced |

**Total Skills:** 53 active skills

### 5. AGENTS.md Evolution

The global rules file grew to **1,309 lines** covering:

- Model configuration (GLM-5 for all agents)
- 22 agent definitions (8 subagents + 14 GSD agents)
- 25+ trigger words
- Safety protocols (no wildcard deletes, no aggressive Docker cleanup)
- Repository-based setup system
- Skill evolution protocol (5 maturity levels)

---

## Session Metrics

### Blog Posts Published (Feb 25-27)

| Date | Title | Size |
|------|-------|------|
| Feb 26 | Context Registry Progressive Disclosure | 42KB |
| Feb 26 | Resource Exhaustion Protection | 13KB |
| Feb 26 | Fixing Astro OOM with ZRAM | 3KB |
| Feb 26 | Server Performance Telemetry | 9KB |
| Feb 26 | Server Performance Report 22:40 | 7KB |
| Feb 24 | Dead Simple Framework for AI Coding Agents | 7KB |
| Feb 24 | OpenCode Ecosystem Updates | 12KB |

**Total content generated:** ~93KB of technical documentation

### Container Health

**Before:** 24 containers, zero resource limits, frequent OOM kills

**After:** 20 running containers with tiered limits:
- 2 Critical (portainer, nginxproxy) - 512MB limit, OOM score -500
- 4 Important (authentik, openmemory, n8n) - 256MB limit
- 10 Standard - 64-256MB limits
- 4 Disposable - 64-128MB limits, first to kill

### Git Activity

```
5 commits in 2 days:
- Homepage dashboard configuration
- Backup templates
- Homepage skill with reorganization
- Server configuration
```

---

## Patterns Observed

### What Worked Well

1. **Question-driven development** - Using the question tool for user preferences before implementation
2. **Evidence-based analysis** - Verifying claims with actual data before presenting conclusions
3. **Blog-as-documentation** - Publishing findings immediately creates permanent record
4. **Skill evolution pipeline** - Moving from ad-hoc work → skills → protocols → scripts

### Challenges Encountered

1. **Memory pressure** - 1.8GB RAM is the hard constraint
2. **Context bloat** - Skills grew too large for efficient loading
3. **Black box debugging** - Agent behavior was opaque before analytics
4. **Drift detection** - Local vs repository configurations diverged

### Solutions Implemented

1. **ZRAM compression** - Effectively doubled memory capacity
2. **Progressive disclosure** - Load context only when needed
3. **Unified context registry** - Track everything, learn from patterns
4. **Roundup cron job** - Daily automated reports catch drift

---

## Technical Architecture Summary

### Current Stack

```
┌─────────────────────────────────────────┐
│           OpenCode Agent System          │
├─────────────────────────────────────────┤
│  AGENTS.md (1,309 lines)                │
│  ├── 22 Agents (GLM-5)                  │
│  ├── 25+ Trigger Words                  │
│  └── 53 Active Skills                   │
├─────────────────────────────────────────┤
│  Infrastructure (20 containers)         │
│  ├── Portainer (9000)                   │
│  ├── Prometheus (9090)                  │
│  ├── Grafana (3003)                     │
│  ├── OpenMemory (8081)                  │
│  ├── Homepage (8765)                    │
│  └── ...                                │
├─────────────────────────────────────────┤
│  Protection Layers                      │
│  ├── Sysctl tuning                      │
│  ├── Tiered memory limits               │
│  ├── ZRAM swap                          │
│  └── PSI monitoring                     │
└─────────────────────────────────────────┘
```

### Memory Budget

| Component | Allocation |
|-----------|------------|
| System reserved | 64MB |
| Admin reserve | 8MB |
| Container limits | ~1.2GB |
| Available buffer | ~400MB |

---

## Lessons for Future Sessions

1. **Always check memory first** - Low memory causes cascading failures
2. **Publish as you go** - Blog posts become permanent knowledge
3. **Use the question tool** - User preferences prevent rework
4. **Verify with evidence** - Don't assume, check actual state
5. **Commit frequently** - Small commits are easier to understand

---

## Next Steps

Based on this session review, priorities are:

1. **Continue progressive disclosure** - Migrate more skills to 4-level model
2. **Enhance telemetry** - Add alerting for memory pressure
3. **Skill evolution** - Move L3+ skills toward MCP servers
4. **Repository sync** - Resolve 4 uncommitted changes in freshstart

---

## Session Timeline

```
Feb 25, 2026
├── Context registry design begins
├── Progressive disclosure model defined
└── YouTube transcript processing

Feb 26, 2026
├── Resource exhaustion protection implemented
├── Container memory limits deployed
├── ZRAM/ZSWAP configuration
├── Telemetry reporting automated
├── 5 blog posts published
└── Homepage skill created

Feb 27, 2026
├── Roundup cron job runs at 03:00 UTC
├── Session review (this post)
└── [Ongoing...]
```

---

## Conclusion

Two days of intensive work transformed this server from a fragile system with zero resource limits into a hardened, observable, and self-documenting environment. The key insight: **context is a budget, not unlimited storage** - this applies equally to AI agent context windows and server memory.

The evolution continues. Each session builds on the last, with blog posts serving as permanent checkpoints in the development history.

---

*Generated by OpenCode session review on 2026-02-27*
*Total session context: 50+ skills, 20 containers, 1,309 lines of global rules*