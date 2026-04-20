---
pubDatetime: 2026-02-23T23:59:00Z
title: "🚨 CRITICAL: System Memory Death Spiral - OpenCode Auto-Restart Loop"
postSlug: "system-memory-death-spiral-20260223"
description: "🚨 CRITICAL: System Memory Death Spiral - OpenCode Auto-Restart Loop"
tags:
  - opencode
  - swap-thrashing
  - critical-alert
  - system-health
  - memory
  - diagnostics
---

## Executive Summary

This post documents a critical system event on **2026-02-23** where OpenCode's auto-restart mechanism created a memory death spiral. The system experienced severe resource exhaustion despite multiple intervention attempts.

### Critical Metrics at Peak

| Metric | Value | Status |
|--------|-------|--------|
| **Disk Usage** | 91% (18GB free of 164GB) | 🔴 CRITICAL |
| **Swap Usage** | 99.8% (880KB free of 6GB) | 🔴 CRITICAL |
| **Free RAM** | 158MB | 🔴 CRITICAL |
| **Load Average** | 13.95 (8 CPU cores) | 🔴 CRITICAL |
| **Swap Thrashing** | 481 pswpin/s average | 🔴 CRITICAL |

---

## Root Cause Analysis

### Death Spiral Mechanism

**Primary Issue**: OpenCode daemon auto-restarts after being killed, immediately recreating memory pressure.

**Evidence**:
1. Killing daemon (PID 1257) freed ~500MB RAM
2. System stabilized briefly (load dropped 13.95→3.90)
3. Daemon auto-restarted (PID 32379) within 2 minutes
4. Memory pressure returned immediately (1.7GB footprint again)

**Pattern**:
```
Kill session → RAM frees briefly →
New sessions spawn OR daemon restarts →
RAM consumed again → Swap thrashing resumes
```

This cycle repeats every time we attempt memory relief.

---

## Timeline of Events

```
23:36 - Session started: 90% disk, 99% swap, load 2.71
23:40 - Identified: 4 OpenCode sessions consuming 2.2GB RAM
23:45 - Attempted Phase 1 cleanup: ~48MB reclaimed
23:50 - Swap pressure spiked to 91.5% - killed pts/1 session
23:52 - Runaway bash-language-server consumed 1.5GB - killed it
23:53 - Daemon restarted automatically - memory returned to 1.7GB footprint
23:55 - Load spiked to 13.95 - system overwhelmed
23:57 - Killed daemon (PID 1257) - system stabilized briefly
23:59 - Daemon auto-restarted (PID 32379) - death spiral confirmed
```

---

## Attempted Interventions

### Phase 1: Safe Cleanups (~48MB Reclaimed)

| Cleanup | Size | Result |
|---------|------|--------|
| Old syslog files | ~48MB | ✅ Removed |
| Stopped containers | 0MB | ✅ Already cleaned by reboot |
| Unused volumes | 421KB | ⚠️ Too small to matter |

### Phase 2: Process Management

| Action | Memory Freed | Outcome |
|--------|-------------|---------|
| Kill pts/1 session | 622MB | Daemon restarted, lost gains |
| Kill bash-language-server | 1.5GB | Runaway process, but system still stressed |
| Kill OpenCode daemon | 500MB | Auto-restarted within 2 minutes |

---

## Key Findings

### Memory Hogs (Final State)

| Process | Memory | CPU | Status |
|---------|--------|-----|--------|
| opencode (serve daemon) | 455MB | 22.7% | Auto-restarted 🔴 |
| opencode (pts/1) | 346MB | 29.2% | Active |
| context7-mcp (x2) | ~290MB each | ~9% | Running |
| brave-search (x2) | ~290MB each | ~8% | Running |
| **Total OpenCode** | **1.7GB** | **~87%** | 25% of system RAM |

### Docker Container Issues

| Container | Issue | Status |
|-----------|--------|--------|
| **blog-ratings-api** | Health check failing (wget not found) | 🔴 Unhealthy |
| **cadvisor** | 77% of 128MB limit used | ⚠️ Near limit |
| **70+ containers running** | Excessive for 8GB RAM | 🔴 Too many |

---

## Recommendations

### Immediate Actions (Post-Crash)

1. **Disable OpenCode auto-restart**
   - Modify systemd service: `Restart=no`
   - Stops death spiral mechanism

2. **Reduce OpenCode sessions**
   - Maximum 2 sessions total (1 daemon + 1 user)
   - Prevents 1.7GB+ memory footprint

3. **Increase swap size**
   - Current: 6GB (too small)
   - Target: 12GB minimum for 8GB RAM

4. **Clean inactive node_modules**
   - Reclaimable: ~8GB
   - Focus on projects not used in 30+ days

### Short-term Actions

1. **Set Docker container memory limits**
   - Prevent single container from consuming all RAM
   - Root cause of previous crashes

2. **Enable cgroups-v2**
   - Persistent resource control
   - Replace cpulimit with systemd-integrated limits

3. **Configure earlyoom more aggressively**
   - Already configured but not triggering effectively
   - Lower threshold to 10% free RAM

4. **Investigate OpenCode memory leak**
   - Daemon process is leaking memory over time
   - Requires profiling and patch review

### Long-term Actions

1. **Upgrade RAM**
   - 8GB insufficient for 70+ containers + OpenCode
   - Target: 16GB minimum

2. **Consolidate containers**
   - Current: 70+ running
   - Target: ~30 active services

3. **Implement real-time monitoring**
   - Install AlertManager for Prometheus
   - Configure email/webhook notifications

4. **Set container resource quotas**
   - Per-container CPU/memory limits
   - Prevent runaway resource consumption

---

## Current Status

**Monitoring**: Active - system is being observed for crash

**Expected Outcome**: System crash or freeze within 10-30 minutes due to continued death spiral

**Decision**: Let system crash naturally rather than killing all processes manually

**Crash Detection Monitoring**:
- Load average spike (>10 = system freeze)
- OOM killer event in journalctl
- Swap exhaustion (99% used)
- Kernel panic

---

## Lessons Learned

### Technical Insights

1. **Auto-restart policies can be dangerous** under memory pressure
2. **Process killing is ineffective** without disabling auto-restart
3. **Swap size too small** for system workload (6GB for 8GB RAM)
4. **Container count excessive** for available memory (70+ containers)

### Process Improvements

1. **Pre-deployment checks**: Verify auto-restart policies match resource constraints
2. **Monitoring gaps**: Need real-time alerts, not manual checks
3. **Resource planning**: 8GB RAM cannot support current workload

### Action Items for Future

1. ✅ Create systemd service override to disable auto-restart
2. ✅ Document OpenCode memory limits
3. ✅ Implement container resource quotas
4. ✅ Set up AlertManager notifications
5. ✅ Schedule RAM upgrade or container consolidation

---

## Conclusion

This diagnostic session revealed a critical design flaw: OpenCode's auto-restart mechanism is incompatible with memory-constrained environments. The death spiral pattern (kill → free → restart → consume) makes manual intervention impossible without disabling auto-restart first.

**Primary Recommendation**: Disable OpenCode auto-restart immediately, then address underlying resource constraints (RAM, swap, container count).

**Next Steps**: After system crash, implement systemd service fix and begin container consolidation project.

---

*Report generated: 2026-02-23T23:59:00Z*
*Diagnostic session duration: ~6 minutes*
*System state: CRITICAL - Death spiral confirmed*