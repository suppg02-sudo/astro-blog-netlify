---
pubDatetime: 2026-03-01T13:25:00Z
title: "Unified Flow Tracking: Recording Agent Delegations, Skill Invocations, and Homepage Actions"
postSlug: "unified-flow-tracking-system"
description: "Unified Flow Tracking: Recording Agent Delegations, Skill Invocations, and Homepage Actions"
tags:
  - opencode
  - automation
  - docker
  - telemetry
---

## The Problem

You have multiple tracking systems across your environment:

| System | What It Tracks | Data Location | Status |
|--------|----------------|---------------|--------|
| Questions | Q&A interactions | `context-registry/data/questions.json` | 15 entries |
| Decisions | User decisions | `questions/history/decisions.json` | 3 entries |
| Menu History | Menu selections | `skills/menu-system/history/menu-history.json` | 6 entries |
| Skills | Skill invocations | `context-registry/data/skills.json` | Empty |
| **OliveTin Actions** | Button clicks → scripts | Docker logs only | **NOT TRACKED** |
| **Agent Delegations** | task() calls | Nothing | **NOT TRACKED** |

The data was scattered. Hard to query holistically.

## The Solution

A **unified flow tracking system** that consolidates all tracking types into a single, queryable registry.

## Architecture

{{< mermaid >}}
flowchart LR
    A[Homepage Button] --> B[Relay :8899]
    B --> C[OliveTin :1337]
    C --> D[Script Execution]
    D --> E[Context Registry]
    E --> F[flows.json]
{{< /mermaid >}}

## Implementation

### New Data Files Created

| File | Purpose |
|------|---------|
| `context-registry/data/flows.json` | Unified flow schema |
| `context-registry/data/delegations.json` | Agent delegation tracking |
| `context-registry/data/actions.json` | OliveTin/Relay action tracking |
| `context-registry/scripts/query-flows.sh` | Unified query interface |
| `context-registry/scripts/record-delegation.sh` | Record agent delegations |
| `context-registry/scripts/record-action.sh` | Record external actions |

### Relay Integration

The relay service (`/media/docker/relay/relay.py`) was modified to record all Homepage button clicks directly to JSON:

```python
def record_action(source, action_id, trigger, success, exit_code=0, 
                  output_length=0, duration_ms=0, error=None):
    """Record action directly to context-registry JSON files."""
    # Writes to actions.json and flows.json
```

## Usage

### Query Commands

```bash
# View recent flows
flows recent 10

# View by type
flows type delegation
flows type action
flows type skill

# View statistics
flows stats

# Search
flows search hugo
```

## Flow Chain Example

When you click a "Health Check" button on Homepage:

1. Homepage sends GET request to relay (port 8899)
2. Relay forwards to OliveTin API (port 1337)
3. OliveTin executes the `health-check.sh` script
4. Script completes, relay records to actions.json
5. Result appears in unified flows.json

## Sample Recorded Flow

```json
{
  "id": "act_20260301_131830_6eb2",
  "timestamp": "2026-03-01T13:18:30Z",
  "source": "relay",
  "action_id": "health-check",
  "trigger": "webhook",
  "chain": [
    {"step": 1, "component": "homepage", "action": "button_click"},
    {"step": 2, "component": "relay", "action": "forward"},
    {"step": 3, "component": "olivetin", "action": "trigger"}
  ],
  "result": {
    "success": true,
    "exit_code": 0,
    "duration_ms": 143
  }
}
```

## Benefits

- **Single source of truth**: All tracking data in one registry
- **Persistent history**: Actions survive container restarts
- **Correlation IDs**: Link related flows across systems
- **Query interface**: Unified search across all tracking types
- **Duration tracking**: Execution time in milliseconds
- **Success/failure tracking**: Exit codes and error messages

## Files Modified

- `/media/docker/relay/relay.py` - Added native JSON recording
- `/media/docker/relay/docker-compose.yml` - Added context-registry volume
- `~/.config/opencode/AGENTS.md` - Added new triggers (`flows`, `record-delegation`, `record-action`)

## Related

- [Context Registry Skill](http://ubuntu4:8765)
- [OliveTin](http://ubuntu4:1337)
- [Homepage Dashboard](http://ubuntu4:8765)