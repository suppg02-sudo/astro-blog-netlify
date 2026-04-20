---
pubDatetime: 2026-03-01T22:30:00Z
title: "Tracking Incomplete Processes: A Full Lifecycle Monitoring System"
postSlug: "tracking-incomplete-processes-lifecycle-monitoring"
description: "How to detect and track processes that started but never completed - implementing full lifecycle monitoring with heartbeat detection and automatic stall alerts"
tags:
  - lifecycle
  - opencode
  - process-tracking
  - automation
  - monitoring
---

## The Problem

When managing complex AI agent workflows, a critical question arises: **How do you know if a process didn't complete?**

Current tracking systems record events but lack visibility into process completion:

- **Actions** track `success` and `exit_code` - mostly complete
- **Delegations** have `result.success: null` - never updated
- **No lifecycle tracking** - missing start_time, end_time, status
- **No stall detection** - can't identify hung processes

This gap means processes can silently fail or stall without detection.

---

## Solution: Full Process Lifecycle Tracking

### Enhanced Schema

Every tracked process (delegation, action, flow) needs lifecycle fields:

```json
{
  "id": "proc_20260301_123456_abc",
  "timestamp": "2026-03-01T12:34:56Z",
  "status": "running",
  "lifecycle": {
    "started": "2026-03-01T12:34:56Z",
    "last_heartbeat": "2026-03-01T12:35:00Z",
    "completed": null,
    "duration_ms": null
  },
  "timeout": {
    "expected_duration_ms": 300000,
    "stall_after_ms": 600000,
    "stalled": false
  },
  "result": {
    "success": null,
    "exit_code": null,
    "output_summary": null
  }
}
```

### Status Values

| Status | Description | Auto-transition |
|--------|-------------|-----------------|
| `pending` | Created, not started | → `running` on first update |
| `running` | In progress | → `complete`/`failed` on result |
| `complete` | Finished successfully | Terminal state |
| `failed` | Finished with error | Terminal state |
| `stalled` | No heartbeat for N seconds | → `failed` if timeout exceeded |

---

## Detection Mechanisms

### 1. Heartbeat Updates

Processes actively ping the system every 30-60 seconds:

```bash
# Long-running process
start-process.sh "task-123" --expected-duration 600000
while working; do
  update-heartbeat.sh "task-123"
  sleep 30
done
mark-complete.sh "task-123" --success true
```

**Pros:** Real-time stall detection  
**Cons:** Requires code changes in processes

### 2. Cron-Based Detection

System automatically checks for stalled processes every 5 minutes:

```bash
# Cron job
*/5 * * * * ~/.config/opencode/context-registry/scripts/detect-stalled.sh
```

Detection logic:
- Find: `status == "running"` AND `now - last_heartbeat > 10 minutes`
- Action: Flag as `stalled`
- Escalate: If `now - last_heartbeat > 30 minutes`, mark as `failed`

**Timeout Thresholds:**
- **10 minutes** = stalled (warning)
- **30 minutes** = failed (terminal)

### 3. Session Orphan Detection

Alternative approach using session tracking:
- Track active sessions with process lists
- Orphaned sessions (no activity for X min) = incomplete processes
- Less precise but no code changes required

---

## Implementation Components

### Core Scripts

| Script | Purpose |
|--------|---------|
| `start-process.sh` | Create process with status=pending |
| `update-heartbeat.sh` | Ping that process is alive |
| `mark-complete.sh` | Set status + result + end_time |
| `detect-stalled.sh` | Find processes with no heartbeat |
| `query-incomplete.sh` | Find pending/running/stalled processes |

### Query Commands

```bash
# Find all incomplete processes
query-incomplete.sh

# Find only stalled (no heartbeat for 10+ min)
query-incomplete.sh --stalled

# Filter by type
query-incomplete.sh --type delegation
query-incomplete.sh --type action

# Show statistics
query-incomplete.sh --stats
```

### Integration Points

**For Delegations (Agent Tasks):**
1. `record-delegation.sh` creates with `status=pending`
2. Subagent calls `update-heartbeat.sh` during execution
3. Subagent calls `mark-complete.sh` when done

**For Actions (Automated Tasks):**
1. `record-action.sh` already has success/exit_code
2. Add `start_time`, `last_heartbeat`, `status` fields
3. Update existing entries to include lifecycle

**For Flows (Multi-step Chains):**
1. Add `status` field to flow entries
2. Chain steps tracked as sub-processes
3. Parent flow status = aggregate of children

---

## Migration Strategy

### Phase 1: Schema Enhancement
1. Add lifecycle fields to all tracking files
2. Migrate existing entries with `status=complete` (historical data)
3. Update recording scripts to include new fields

### Phase 2: Heartbeat Integration
1. Add `update-heartbeat.sh` script
2. Integrate into long-running operations (delegations, flows)
3. Test with simulated long process

### Phase 3: Detection & Alerting
1. Add `detect-stalled.sh` script
2. Set up cron job (every 5 min)
3. Create `query-incomplete.sh` for manual checks

### Phase 4: UI Integration
1. Add "Incomplete Processes" to `flows` trigger menu
2. Add stalled count to `mem-check` trigger
3. Add incomplete items to session review

---

## Files to Create/Modify

### New Scripts
```
~/.config/opencode/context-registry/scripts/
├── start-process.sh
├── update-heartbeat.sh
├── mark-complete.sh
├── detect-stalled.sh
└── query-incomplete.sh
```

### Modified Scripts
```
~/.config/opencode/context-registry/scripts/
├── record-delegation.sh  (add lifecycle)
├── record-action.sh      (add lifecycle)
└── query-flows.sh        (add status filter)
```

### Data Files (Schema Updates)
```
~/.config/opencode/context-registry/data/
├── flows.json        (add lifecycle fields)
├── delegations.json  (add lifecycle fields)
└── actions.json      (add lifecycle fields)
```

---

## Trade-offs Analysis

| Approach | Pros | Cons |
|----------|------|------|
| **Heartbeat + Cron** | Real-time detection, best coverage | Requires code changes |
| **Cron-Only** | No code changes, simpler | 5-min detection lag |
| **Session-Based** | No process modification | Less precise timing |
| **Timeout-Only** | Simple implementation | False positives on slow tasks |

**Recommendation:** Full lifecycle with heartbeat + cron detection provides the most reliable monitoring.

---

## Usage Examples

### Starting a Long Process

```bash
# Start tracking
~/.config/opencode/context-registry/scripts/start-process.sh \
  "backup-database" \
  --type action \
  --expected-duration 600000

# Returns: proc_20260301_223000_abc
```

### Sending Heartbeats

```bash
# In long-running script
while backup_in_progress; do
  ~/.config/opencode/context-registry/scripts/update-heartbeat.sh \
    "proc_20260301_223000_abc"
  sleep 30
done
```

### Marking Complete

```bash
# Success
~/.config/opencode/context-registry/scripts/mark-complete.sh \
  "proc_20260301_223000_abc" \
  --success true \
  --output "Backup completed: 2.3GB transferred"

# Failure
~/.config/opencode/context-registry/scripts/mark-complete.sh \
  "proc_20260301_223000_abc" \
  --success false \
  --error "Disk full at 95%"
```

### Querying Incomplete

```bash
# All incomplete
~/.config/opencode/context-registry/scripts/query-incomplete.sh

# Output:
# ID                          TYPE        STATUS    AGE       LAST_HEARTBEAT
# proc_20260301_220000_xyz    delegation  running   45m       40m ago ⚠️ STALLED
# proc_20260301_221500_abc    action      pending   15m       never
# proc_20260301_222000_def    flow        running   2m        30s ago

# Statistics
~/.config/opencode/context-registry/scripts/query-incomplete.sh --stats

# Output:
# Total Processes: 74
# Complete: 68 (91.9%)
# Running: 3 (4.1%)
# Pending: 1 (1.4%)
# Stalled: 2 (2.7%) ⚠️
# Failed: 0 (0%)
```

---

## Cron Configuration

Add to crontab for automatic detection:

```bash
# Every 5 minutes: detect stalled processes
*/5 * * * * ~/.config/opencode/context-registry/scripts/detect-stalled.sh >> ~/cron-logs/stall-detection.log 2>&1

# Daily at midnight: cleanup old completed processes (30+ days)
0 0 * * * ~/.config/opencode/context-registry/scripts/cleanup-completed.sh --days 30 >> ~/cron-logs/cleanup.log 2>&1
```

---

## Integration with Existing Triggers

### `flows` Trigger Enhancement

Add "Incomplete Processes" option to the flows menu:

```json
{
  "label": "⚠️ Incomplete Processes",
  "description": "Show pending, running, and stalled processes"
}
```

### `mem-check` Trigger Enhancement

Add stalled count to memory check output:

```
Memory: 4.2GB / 8GB (52%)
Flows: 74 total, 2 stalled ⚠️
Delegations: 2 total, 1 incomplete
```

### Session Review Integration

When ending a session, prompt about incomplete items:

```
Session Summary:
- Questions asked: 12
- Tasks completed: 5
- Incomplete processes: 2 ⚠️

Would you like to review incomplete processes before ending?
```

---

## Next Steps

1. **Implement core scripts** (start-process, update-heartbeat, mark-complete)
2. **Add cron detection** with 10/30 minute thresholds
3. **Migrate existing data** marking all historical entries as complete
4. **Integrate with delegations** to fix null result fields
5. **Add UI triggers** for easy querying

---

## Conclusion

Process lifecycle tracking transforms reactive debugging into proactive monitoring. By combining:

- **Explicit lifecycle states** (pending → running → complete/failed)
- **Heartbeat updates** for real-time status
- **Automatic stall detection** via cron jobs
- **Query tools** for manual inspection

We gain complete visibility into process health. No more silent failures or mysterious stalls.

The implementation is straightforward:
- 5 new scripts (~50 lines each)
- Schema updates to 3 data files
- 1 cron job
- Integration with existing triggers

Total effort: ~2-3 hours for full implementation.

---

**Status:** Plan complete, ready for implementation  
**Priority:** Medium - improves observability and debugging  
**Dependencies:** None - builds on existing context-registry infrastructure