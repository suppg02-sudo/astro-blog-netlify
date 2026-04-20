---
pubDatetime: 2026-04-05T12:00:00Z
title: "Signals, Analysis, and Self-Improvement as Schema Resources"
postSlug: "signals-analysis-self-improvement-schema-resources"
description: "Signals, Analysis, and Self-Improvement as Schema Resources"
tags:
  - control-plane
  - schema-design
  - observability
  - kubernetes
  - self-improvement
---

# Signals, Analysis, and Self-Improvement as Schema Resources

## Why Observability Belongs in the Schema, Not in Side Files

Last week the Menu Controller went live. It runs observe → diff → act on 59 menu resources every Sunday. It pruned 123 dead options. It logged every change to an audit trail. It works.

But something bothered me.

The controller reads signals from a flat JSON file (`signals.json`). The analysis logic is hardcoded inside `optimize.py`. The self-improvement — adjusting thresholds, tuning detection sensitivity — is entirely manual. The reconciliation loop closes for individual resources, but it doesn't close for itself.

This post is about fixing that. About making **signals, analysis, and self-improvement** first-class resources in the schema — the same way Kubernetes makes ConfigMaps, Deployments, and Services first-class resources — so the control plane can observe and improve its own operation.

## The Problem with Ad-Hoc Observability

Here's what the current system looks like:

```
Signal Recording (flat JSON) → Detection Functions (hardcoded) → Controller (observe/diff/act) → Change Log (PostgreSQL)
```

The signals are a side effect. The detection patterns are code, not configuration. The thresholds are constants. The only structured part is the output end — the resource registry and change log.

This means:

- **You can't query signal history** — it's aggregated into counters, losing granularity
- **You can't change detection rules** without editing Python code
- **You can't measure controller effectiveness** — did pruning that option actually improve selection rates?
- **You can't compose analyses** — each controller runs its own detections independently
- **You can't tune the system** — thresholds are magic numbers in source files

Kubernetes solved this for infrastructure by making every operational concept a resource. Argo Rollouts solved it for deployment analysis by introducing AnalysisTemplate and AnalysisRun as custom resources. Crossplane solved it for infrastructure composition by adding connection details and health checks to the resource envelope.

The same pattern applies here.

## The Missing Resource Kinds

We need five new resource kinds to close the loop:

### 1. SignalSource — Where Signals Come From

A SignalSource declares where observability data originates. It's the equivalent of a Prometheus scrape config or a Datadog monitor — it says "watch this thing, record these events."

```yaml
apiVersion: opencode/v1
kind: SignalSource
metadata:
  name: menu-signal-source
  labels:
    domain: menu-optimization
spec:
  type: event_stream
  provider: signal.py
  events:
    - name: menu_presented
      fields: [skill, options, mode, timestamp]
    - name: menu_selected
      fields: [skill, option, position, time_to_select_ms]
  retention:
    raw_days: 30
    aggregate_after_days: 7
    aggregate_granularity: daily
  output:
    store: controlplane.signals
    format: jsonb
status:
  phase: Active
  events_recorded: 2847
  last_event: 2026-04-06T09:00:00Z
  conditions:
    - type: Ready
      status: "True"
      reason: ReceivingEvents
    - type: Healthy
      status: "True"
      reason: EventRateNormal
```

Why this matters: Right now, signal recording is scattered across scripts (`record_signal.py`, `signal.py`, the `present`/`select` commands). A SignalSource makes the pipeline declarative. You can see what's being recorded, how long it's retained, and whether it's healthy — just by querying the resource.

### 2. Signal (Individual Event) — The Raw Data

Individual signal events, stored in PostgreSQL. These are ephemeral by design — they roll up into aggregates — but they exist as queryable rows.

```yaml
apiVersion: opencode/v1
kind: Signal
metadata:
  name: sig-2026-04-06-a1b2c3
  labels:
    source: menu-signal-source
    skill: skill-factory
spec:
  event: menu_presented
  payload:
    skill: skill-factory
    options: ["Create", "Update", "Diagnose"]
    mode: mobile
    session_id: sess-abc123
status:
  timestamp: 2026-04-06T09:15:32Z
  processed: true
  aggregated: false
```

The signals table already partially exists in our system (`signals.json`), but as a flat file with no schema enforcement. Making them proper resources means:

- You can query them with SQL: `SELECT COUNT(*) FROM controlplane.signals WHERE event='menu_selected' AND created_at > NOW() - INTERVAL '7 days'`
- You can set retention policies declaratively
- You can track whether the signal pipeline is healthy (are events flowing?)

### 3. AnalysisTemplate — What Patterns to Detect

This is the key abstraction from Argo Rollouts, adapted for our domain. An AnalysisTemplate declares *what to look for* in signal data, *what thresholds trigger action*, and *what the remediation should be*.

```yaml
apiVersion: opencode/v1
kind: AnalysisTemplate
metadata:
  name: dead-option-detection
  labels:
    domain: menu-optimization
    risk: safe
spec:
  description: "Detect menu options that have never been selected"
  signal_source: menu-signal-source
  query: |
    SELECT m.option_label, COUNT(s.id) as selections
    FROM controlplane.signals s
    CROSS JOIN LATERAL jsonb_array_elements(s.payload->'options') AS m(option_label)
    WHERE s.event = 'menu_selected'
      AND s.payload->>'skill' = '{{ .skill_name }}'
      AND s.created_at > NOW() - INTERVAL '{{ .window }}'
    GROUP BY m.option_label
  window: 30d
  thresholds:
    trigger:
      selections: 0
      min_presentations: 10
  auto_correct: true
  correction:
    action: prune
    risk: safe
    description: "Remove option with zero selections in the analysis window"
  produces:
    drift_pattern: dead_option
    severity: LOW
status:
  runs_completed: 12
  findings_total: 47
  corrections_applied: 47
  false_positive_rate: 0.02
  last_run: 2026-04-06T09:00:00Z
  conditions:
    - type: Ready
      status: "True"
      reason: TemplateValid
    - type: Healthy
      status: "True"
      reason: FalsePositiveRateAcceptable
```

Compare this to Argo Rollouts' AnalysisTemplate — the structure is the same:

| Argo Rollouts | OpenCode Control Plane |
|---------------|----------------------|
| `metrics[].provider.prometheus.query` | `spec.query` |
| `metrics[].successCondition` | `spec.thresholds.trigger` |
| `metrics[].failureLimit` | `spec.auto_correct` + `spec.correction` |
| `spec.args` | `{{ .skill_name }}`, `{{ .window }}` |

The difference is that Argo analyzes *deployment health* (error rates, latency). We analyze *configuration health* (selection rates, usage patterns, drift). The pattern is identical.

Right now, the 8 detection patterns in `optimize.py` are hardcoded functions. Each one is effectively an AnalysisTemplate that exists only as Python code. Making them declarative means:

- You can add new detection patterns without writing code
- You can tune thresholds by editing a YAML resource
- You can see *all* detection rules by listing AnalysisTemplates
- You can track the effectiveness of each template over time

### 4. AnalysisRun — An Instance of Analysis

When a controller runs reconciliation, it creates AnalysisRun resources — one per AnalysisTemplate per resource being reconciled. This is the audit trail for *why* a controller made a decision.

```yaml
apiVersion: opencode/v1
kind: AnalysisRun
metadata:
  name: run-dead-option-skill-factory-2026-04-06
  labels:
    template: dead-option-detection
    resource_kind: menu
    resource_name: skill-factory-menu
spec:
  template_ref: dead-option-detection
  resource_ref:
    kind: menu
    name: skill-factory-menu
  args:
    skill_name: skill-factory
    window: 30d
status:
  phase: Successful
  started_at: 2026-04-06T09:00:01Z
  finished_at: 2026-04-06T09:00:01Z
  findings:
    - option: "Create"
      selections: 0
      presentations: 15
      pattern: dead_option
    - option: "Update"
      selections: 0
      presentations: 15
      pattern: dead_option
  correction_applied:
    action: prune
    items: ["Create", "Update"]
    auto: true
  conditions:
    - type: Successful
      status: "True"
      reason: AnalysisComplete
    - type: Corrected
      status: "True"
      reason: AutoPrune
```

This is critical for the feedback loop. Right now, the change_log records *what* changed. AnalysisRun records *why* it changed — what query was run, what data it found, what threshold was triggered. This lets you answer:

- "Why was the Create option removed?" → Check the AnalysisRun
- "Was that a good decision?" → Check the selection data after removal
- "Should we lower the dead_option threshold?" → Check the false_positive_rate on the AnalysisTemplate

### 5. ControllerHealth — The Controller Observing Itself

This is where self-improvement becomes real. A ControllerHealth resource tracks the controller's own effectiveness. It's the controller observing the observer.

```yaml
apiVersion: opencode/v1
kind: ControllerHealth
metadata:
  name: menu-controller-health
  labels:
    controller: menu-controller
spec:
  controller_ref: menu-controller
  metrics:
    - name: reconciliation_success_rate
      query: |
        SELECT COUNT(*) FILTER (WHERE status->>'phase' = 'Reconciled')
             / COUNT(*)::float
        FROM controlplane.resources
        WHERE kind = 'menu'
      target: 0.99
      alert_below: 0.95

    - name: auto_correction_revert_rate
      query: |
        SELECT COUNT(*) FILTER (WHERE operation = 'reverted')
             / COUNT(*) FILTER (WHERE auto = true)::float
        FROM controlplane.change_log
        WHERE controller = 'menu-controller'
      target: 0.0
      alert_above: 0.05

    - name: false_positive_rate
      query: |
        SELECT
          (SELECT COUNT(*) FROM controlplane.analysis_runs
           WHERE status->>'correction_reverted' = 'true')
          / COUNT(*)::float
        FROM controlplane.analysis_runs
        WHERE template_ref IN (SELECT name FROM controlplane.resources WHERE kind = 'analysistemplate')
      target: 0.02
      alert_above: 0.10

    - name: mean_time_to_detect_drift
      query: |
        SELECT AVG(EXTRACT(EPOCH FROM (r.updated_at - r.last_reconciled)))
        FROM controlplane.resources r
        WHERE r.kind = 'menu' AND r.drift != 'NONE'
      target: 3600
      alert_above: 86400

    - name: selection_rate_trend
      description: "Are selection rates improving after corrections?"
      query: |
        WITH corrections AS (
          SELECT resource_name, created_at
          FROM controlplane.change_log
          WHERE controller = 'menu-controller' AND auto = true
        )
        SELECT
          AVG(CASE WHEN s.created_at > c.created_at THEN 1 ELSE 0 END)
        FROM controlplane.signals s
        JOIN corrections c ON s.payload->>'skill' = REPLACE(c.resource_name, '-menu', '')
        WHERE s.event = 'menu_selected'
      target: 0.6
      alert_below: 0.3

  evaluation_interval: 3600
  alert_channel: telegram
status:
  phase: Healthy
  last_evaluated: 2026-04-06T09:00:00Z
  metric_results:
    - name: reconciliation_success_rate
      value: 1.0
      status: ok
    - name: auto_correction_revert_rate
      value: 0.0
      status: ok
    - name: false_positive_rate
      value: 0.02
      status: ok
    - name: mean_time_to_detect_drift
      value: 120
      status: ok
    - name: selection_rate_trend
      value: 0.68
      status: ok
  overall_health: Healthy
  conditions:
    - type: Healthy
      status: "True"
      reason: AllMetricsWithinTarget
    - type: Degrading
      status: "False"
      reason: NoMetricDegrading
```

## The Self-Improvement Loop

With these five resource kinds, the system can close the loop on itself:

```
SignalSource records events
    → Signals stored in PostgreSQL
        → AnalysisTemplates define what to detect
            → AnalysisRuns execute detection queries
                → Findings become DriftItems on resources
                    → Controller acts (auto-correct or propose)
                        → Change Log records the mutation
                            → ControllerHealth measures outcomes
                                → AnalysisTemplates get tuned
                                    → Loop continues
```

The key insight: **every step in this loop is a resource with spec + status + conditions**. That means every step is observable, queryable, and reconcilable by its own controller.

The SignalSource controller checks that events are flowing. The AnalysisTemplate controller checks that templates are producing valid findings. The AnalysisRun controller tracks execution history. The ControllerHealth controller monitors effectiveness and raises alerts when metrics degrade.

Each controller is itself a resource. Each has its own ControllerHealth. The observability stack observes itself.

## The PostgreSQL Schema

To make this concrete, here's the minimal PostgreSQL extension to the existing `controlplane` schema:

```sql
-- Signal sources (declarative signal pipeline configuration)
CREATE TABLE controlplane.signal_sources (
    name TEXT PRIMARY KEY,
    spec JSONB DEFAULT '{}',
    status JSONB DEFAULT '{}',
    conditions JSONB DEFAULT '[]',
    phase TEXT DEFAULT 'Pending',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Individual signal events
CREATE TABLE controlplane.signals (
    id SERIAL PRIMARY KEY,
    source TEXT NOT NULL REFERENCES controlplane.signal_sources(name),
    event TEXT NOT NULL,
    payload JSONB DEFAULT '{}',
    session_id TEXT,
    processed BOOLEAN DEFAULT false,
    aggregated BOOLEAN DEFAULT false,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_signals_source_event ON controlplane.signals(source, event);
CREATE INDEX idx_signals_created ON controlplane.signals(created_at);

-- Analysis templates (declarative detection rules)
CREATE TABLE controlplane.analysis_templates (
    name TEXT PRIMARY KEY,
    spec JSONB DEFAULT '{}',
    status JSONB DEFAULT '{}',
    conditions JSONB DEFAULT '[]',
    phase TEXT DEFAULT 'Active',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Analysis runs (execution history)
CREATE TABLE controlplane.analysis_runs (
    id SERIAL PRIMARY KEY,
    template_ref TEXT NOT NULL REFERENCES controlplane.analysis_templates(name),
    resource_kind TEXT NOT NULL,
    resource_name TEXT NOT NULL,
    spec JSONB DEFAULT '{}',
    status JSONB DEFAULT '{}',
    conditions JSONB DEFAULT '[]',
    phase TEXT DEFAULT 'Pending',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    finished_at TIMESTAMPTZ
);
CREATE INDEX idx_runs_template ON controlplane.analysis_runs(template_ref);

-- Controller health (meta-observability)
CREATE TABLE controlplane.controller_health (
    controller TEXT PRIMARY KEY,
    spec JSONB DEFAULT '{}',
    status JSONB DEFAULT '{}',
    conditions JSONB DEFAULT '[]',
    phase TEXT DEFAULT 'Pending',
    last_evaluated TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

Five tables. Same structure as the existing resource envelope: spec (desired), status (observed), conditions (state machine), phase (lifecycle). The pattern holds.

## Why Not Just Use Prometheus?

A reasonable question. Prometheus already does metrics, alerting, and (with Alertmanager) auto-remediation. Why build this into the schema?

Three reasons:

**1. Prometheus measures infrastructure. We measure configuration.**

Prometheus tracks CPU, memory, request latency, error rates. Our signals track *which menu options get selected, which skills get invoked, whether a menu violates its size constraint, whether a template has drifted from its definition.* These are configuration health metrics, not infrastructure health metrics. They need their own schema because they answer different questions.

**2. Prometheus doesn't have a spec/status model.**

Prometheus alerting rules are one-directional: measure → alert. There's no concept of desired state vs observed state. There's no drift computation. There's no reconciliation loop. Our AnalysisTemplates produce DriftItems that feed into the same controller pipeline that manages resources. The analysis output becomes controller input.

**3. Self-improvement requires meta-observability.**

Prometheus can monitor itself (scrape its own metrics). But it can't tune its own alerting rules based on observed effectiveness. Our ControllerHealth resource does exactly this — it measures whether corrections actually improved things, and feeds that back into template tuning. That requires the analysis to be a resource in the same schema as the things it's analyzing.

## Implementation Order

The full schema evolution is a multi-step project. Here's the priority order:

| Phase | What | Why |
|-------|------|-----|
| 1 | Create the 5 PostgreSQL tables | Foundation — everything reads/writes from here |
| 2 | Migrate `signal.py` to write to `controlplane.signals` | Replace flat JSON with structured rows |
| 3 | Convert the 8 detection functions to AnalysisTemplate resources | Make detection rules declarative |
| 4 | Update `menu_controller.py` to read templates instead of hardcoded functions | Controller becomes template-driven |
| 5 | Create ControllerHealth for menu-controller | Start measuring effectiveness |
| 6 | Build a meta-controller that auto-tunes templates based on ControllerHealth | Close the self-improvement loop |

Phases 1–4 are mechanical — moving existing behavior into the new schema. Phase 5 is where it gets interesting. Phase 6 is where the system starts improving itself.

## The Bigger Picture

This pattern — making every operational concept a resource — is exactly what Kubernetes did for infrastructure. Every ConfigMap, every Deployment, every Service, every Ingress is a resource with spec and status. Every controller reads resources, reconciles, and writes status back.

Argo Rollouts extended this to deployment analysis. AnalysisTemplate and AnalysisRun are resources that declare what to measure and record what was found. They compose with Rollout resources — the analysis output feeds back into deployment decisions.

Crossplane extended it to infrastructure composition. XRDs (Composite Resource Definitions) declare what infrastructure looks like. Compositions declare how to build it. Connection details and health checks make the composed infrastructure observable.

We're extending it to AI agent configuration. Skills, Menus, Agents, Research Projects are resources. SignalSources, AnalysisTemplates, AnalysisRuns, and ControllerHealth make those resources observable and self-improving.

The pattern is the same. The domain is different. The payoff — systems that maintain themselves — is universal.

---

*The schema designs and PostgreSQL DDL in this post are the next evolution of the OpenCode Control Plane. The existing controller (`menu_controller.py`) implements phases 1–4 of the original design. The 5 new resource kinds described here represent the next iteration: making the control plane self-observing and self-improving.*
