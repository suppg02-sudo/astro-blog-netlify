---
pubDatetime: 2026-04-06T13:24:55Z
title: "Self-Improving Architecture #6: The Experiment Controller Is Live"
postSlug: "self-improving-architecture-experiment-controller-live"
description: "Self-Improving Architecture #6: The Experiment Controller Is Live"
tags:
  - control-plane
  - experiment-controller
  - reconciliation
  - self-improving
  - postgresql
---

## The Experiment Controller Is Live

Three PostgreSQL tables. One `reconcile()` function. A database row that knows it's drifting.

The **Experiment Controller** — the first real controller in the AI Agent Control Plane — is now operational.

### What Changed

| Before | After |
|---|---|
| Autonomous experiments were ad-hoc | Every experiment is a governed resource |
| Drift was invisible | Drift is computed and auditable |
| No history | Every reconciliation action logged |
| Karpathy's autoresearch was a one-off pattern | The pattern is now a first-class Kind |

### The Stack

Three new tables in the memory database:

```sql
resource_types  — Schema Registry (what Kinds exist)
resources       — Resource Store (spec vs status per instance)
change_log      — Audit Trail (every controller action)
```

One Python script: [`reconcile.py`](http://ubuntu4:8080/editor/opencode/skills/autoresearch/scripts/reconcile.py)

```python
# 1. Read desired state (spec)
# 2. Read observed state (status)
# 3. Compute drift
# 4. If drift != NONE, correct and log
```

### First Detection

The very first reconciliation run found drift immediately:

```
📦 Experiment/nanochat-autoresearch
   Current drift: NONE
   ⚠️  [HIGH] spec.initial_state.baseline_commit: expected a commit hash, got None
      → Run baseline experiment
   ✅ Drift updated: NONE → HIGH
```

The system knows it's incomplete. That's not a bug — it's the whole point. **A controller that can't detect absence is no controller at all.**

### The Audit Trail

Every action is logged:

```
 id | resource_kind |             controller      | operation | drift_before | drift_after
----+---------------+-----------------------------+-----------+--------------+-------------
  1 | Experiment    | experiment-controller       | CREATE    |              | NONE
  2 | Experiment    | experiment-controller       | RECONCILE | NONE         | HIGH
```

Not a feature. A principle. *"Every reconciliation cycle is auditable."*

### Schema Registry

The `resource_types` table now tracks schema-to-controller mappings. The Experiment Kind was registered first, but the `--register-all` flag syncs every YAML schema in the ecosystem:

```bash
python3 reconcile.py --register-all
# Registered/updated N Kind(s)
```

### What's Next

The controller detects drift. It doesn't yet *fix* it. The next step is auto-actuation — when drift=HIGH on an experiment, the controller actually runs the baseline instead of just flagging it.

Then: Skill Controller, Agent Controller, Menu Controller. Every resource type, governed the same way.

The control plane is no longer theory. It's tables.
