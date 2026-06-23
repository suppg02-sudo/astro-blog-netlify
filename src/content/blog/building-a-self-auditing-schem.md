---
pubDatetime: 2026-04-10T19:00:00Z
title: "Building a Self-Auditing Schema Hierarchy: A Step-by-Step Architecture Guide"
postSlug: "building-a-self-auditing-schem"
description: "Building a Self-Auditing Schema Hierarchy: A Step-by-Step Architecture Guide"
tags:
  - "3"
  - "1"
  - "2"
---

> **Mental model**: Your data structures should be their own runtime. A schema shouldn't just describe shape — it should contain the rules for verifying it, the actions agents can take, and the questions they should ask before starting.

## Who This Is For

You're building a system with multiple entity types — research projects, published content, skills, menus — and you need each type to have its own validation rules, agent interfaces, and improvement loops. You've tried static JSON Schema or YAML configs, and they validate shape but don't *do* anything. You want schemas that are alive.

This guide walks through building a three-tier schema hierarchy (seed → factory → instance) backed by PostgreSQL, with automated auditing, improvement bubbling, and dynamic agent prompt generation.

## Step 1: Map Your Stores

Before designing anything, list where data lives and what each store owns:

| Store | Owns | Good At |
|-------|------|---------|
| PostgreSQL (`aimplifi_schemas`) | Schema hierarchy (seed, factories, instances) | JSONB queries, hierarchical relations, audit logs |
| Filesystem (`~/.config/opencode/skills/`) | Skill definitions, scripts, configs | Version control, human editing |
| CLI (`pghfactory`) | CRUD operations on schemas | Shell integration, cron automation |
| Evolution Engine (`evolution_artefacts`) | Cross-domain improvement tracking | Quality scoring, LLM-assisted improvement |

The key insight: PostgreSQL owns the *live* schema state. Files own the *source code*. The CLI is the bridge between them.

## Step 2: Define the Seed Schema

The seed is the genome. Every factory and instance inherits from it. Define the shared `$defs` that all entities must carry:

```json
{
  "schemaIdentity": {
    "name": "string",
    "version": "semver",
    "purpose": "string",
    "maturity": "L1-L5"
  },
  "auditSpec": {
    "cadence": "on_complete|daily|weekly|on_demand",
    "criteria": [
      {"id": "string", "name": "string", "check": "string", "severity": "error|warning|info", "auto_fixable": "boolean"}
    ],
    "improvement_log": [
      {"date": "ISO 8601", "author": "string", "finding": "string"}
    ]
  },
  "agentInterface": {
    "entry_questions": [{"question": "string", "purpose": "string"}],
    "available_actions": [{"action": "string", "description": "string", "produces": "string"}],
    "context_requirements": ["string"]
  },
  "lifecycle": {
    "phases": ["string"],
    "default_phase": "string"
  }
}
```

**Check**: Can every factory in your system be described by these five sections? If a factory needs something not covered here, add it to the seed. If only one factory needs it, put it in the factory's own schema under a namespaced key.

## Step 3: Create Factory Schemas with Domain DNA

Each factory inherits the seed's `$defs` and adds domain-specific rules. The research factory, for example, defines 8 generation rules:

```json
{
  "identity": {"name": "Research Factory", "version": "0.1.0"},
  "factory": {
    "generation_rules": [
      {"rule": "Every research project must begin with a clearly stated primary question.", "rationale": "A topic is not a question. Research without a question is browsing."},
      {"rule": "Decompose the primary question into 2-5 sub-questions before searching.", "rationale": "Sub-questions create structure for evidence gathering and prevent drift."},
      {"rule": "Maintain an explicit tensions register. Do not resolve tensions prematurely.", "rationale": "Premature resolution is the enemy of understanding."}
    ]
  },
  "audit": {
    "criteria": [
      {"id": "r-audit-01", "name": "Question clarity", "check": "Verify primary question is specific and answerable.", "severity": "error"},
      {"id": "r-audit-05", "name": "Tension register", "check": "If 5+ sources and zero tensions, flag as suspicious.", "severity": "info"},
      {"id": "r-audit-07", "name": "Gaps documented", "check": "Verify gaps section is non-empty.", "severity": "warning"}
    ]
  }
}
```

**Validation checkpoint**: After creating a factory schema, run it through the prompt builder. If the output reads like a coherent system prompt — entry questions make sense, actions are actionable, rules have rationale — the DNA is healthy. If it reads like config file noise, the rules aren't specific enough.

## Step 4: Build the Auto-Audit Loop

The audit loop is where schemas become alive. It's a script that runs on a schedule, finds active instances, and checks them against their parent factory's criteria.

```python
def auto_audit(dry_run=False):
    instances = get_active_instances()  # tier='instance', lifecycle_state='active'
    for iid, slug in instances:
        verify_out = subprocess.run(["pghfactory", "verify", slug], capture_output=True, text=True)
        if verify_out.returncode != 0 or has_error_in_stderr(verify_out.stderr):
            log_improvement(slug, f"Audit FAILED: {verify_out.stderr}", author="auto_audit")
        else:
            log_improvement(slug, "Automated audit completed successfully.", author="auto_audit")
```

**Common mistake #1**: Scanning stdout for the word "ERROR". Your verify command outputs audit criteria text, which contains severity labels like `[ERROR]` and `[WARNING]`. Those are not command errors — they're part of the criteria output. Only check `returncode` and `stderr`.

**Common mistake #2**: Only logging successes. If an instance fails verification and you skip it, the failure vanishes. No record, no improvement proposal, no way to detect patterns. Log failures with detail — that's where the learning happens.

Wire it to cron:
```bash
# Daily at 8:30 UTC
30 8 * * * /usr/bin/python3 auto_audit.py >> /root/cron-logs/auto-audit.log 2>&1
```

**Validation checkpoint**: Create a test instance, run the audit, verify both pass and fail paths log correctly. Delete the test instance after.

## Step 5: Build the Improvement Bubbler

Instances collect improvement log entries. The bubbler aggregates them upward to the parent factory, grouping by finding and proposing version bumps.

```python
def bubble_up(factory_slug):
    instances = get_child_instances(factory_slug)
    all_improvements = []
    for inst in instances:
        log = inst.schema_json.get("auditSpec", {}).get("improvement_log", [])
        all_improvements.extend(log)
    
    # Group by finding
    grouped = {}
    for imp in all_improvements:
        key = imp["finding"][:60]
        grouped.setdefault(key, []).append(imp)
    
    # Propose version bump
    current = factory.identity.get("version", "0.0.0")
    major, minor, patch = current.split(".")
    proposed = f"{major}.{minor}.{int(patch) + 1}"
```

**Common mistake #3**: Assuming consistent key names. Your aspirational design docs say `schemaIdentity`. Your database says `identity`. Your code needs to check both:

```python
identity = data.get("schemaIdentity", data.get("schema_identity", data.get("identity", {})))
```

Every lookup is a fallback chain. This is the tax you pay for schema evolution — the system changed its naming conventions, and the code has to speak all dialects.

**Validation checkpoint**: Add improvement entries to an instance, run the bubbler, verify the grouping count matches and the version proposal increments correctly.

## Step 6: Build the Agent Prompt Builder

This is where the hierarchy becomes useful. The prompt builder extracts a factory's `agentInterface` and formats it as a system context block that any LLM can consume.

```python
def build_prompt(factory_slug):
    factory = load_factory(factory_slug)
    interface = factory.get("agentInterface", factory.get("agent_interface", {}))
    
    sections = []
    sections.append(format_identity(factory))
    sections.append(format_entry_questions(interface.get("entry_questions", [])))
    sections.append(format_actions(interface.get("available_actions", [])))
    sections.append(format_generation_rules(factory.get("factory", {}).get("generation_rules", [])))
    sections.append(format_audit_criteria(factory.get("audit", {}).get("criteria", [])))
    return "\n".join(sections)
```

The output for the research factory is 49 lines: 3 entry questions, 7 available actions, 8 generation rules with rationale, 7 audit criteria with severity badges. All extracted from the schema — no manual prompt engineering.

**Validation checkpoint**: Run the prompt builder against every aligned factory. If any produces an empty section, the factory is missing DNA.

## Step 7: Integrate with the Evolution Engine

The schema hierarchy becomes a domain in the Evolution Engine's adapter pattern. Five methods:

| Method | What It Does |
|--------|-------------|
| `capture()` | Scans all factories and instances, scores DNA completeness |
| `analyse()` | Identifies missing identity, audit criteria, or agent interface |
| `improve()` | Proposes alignment spec for factories with incomplete DNA |
| `monitor()` | Reports alignment rate (e.g., 5/9 factories) |
| `approve()` | Applies proposed changes |

```python
@register_adapter
class SchemasAdapter(DomainAdapter):
    domain = "schemas"
    
    def monitor(self):
        factories = get_factories()
        aligned = sum(1 for f in factories if score_factory(f) >= 4)
        return {
            "total_factories": len(factories),
            "aligned_factories": aligned,
            "alignment_rate": f"{aligned}/{len(factories)}"
        }
```

The adapter registers alongside existing domains (prompts, menus, skills, roadmap). When the Evolution Engine's cron fires, the schema domain runs in parallel with all others.

**Validation checkpoint**: Run `evolved capture --domains schemas` and verify it reports all factories with correct DNA scores.

## Common Mistakes

1. **Scanning stdout for error keywords** — Audit criteria contain severity labels like `[ERROR]`. Check `returncode` and `stderr` only.
2. **Only logging audit successes** — Failures are the valuable data. Without them, the bubbler has nothing to learn from.
3. **Assuming consistent key names** — `schemaIdentity`, `schema_identity`, and `identity` all refer to the same thing. Code must check all variants.
4. **Treating schemas as static** — The whole point is that schemas evolve. The bubbler proposes version bumps. The adapter detects drift. If you freeze the schema, you've built a corpse.
5. **Skipping the prompt builder validation** — If the prompt builder produces garbage, the DNA is wrong. It's the canary in the schema coal mine.

## Generalisation

This pattern applies beyond AI agent systems:

| Domain | Seed | Factory | Instance | Audit |
|--------|------|---------|----------|-------|
| Microservices | Service contract | Service template | Deployed service | Health checks + SLA |
| Database schemas | Base column types | Table templates | Actual tables | Constraint validation |
| API endpoints | Base response format | Endpoint pattern | Deployed endpoint | Integration tests |
| CI/CD pipelines | Base stage definitions | Pipeline templates | Running pipeline | Stage gate checks |
| Compliance frameworks | Control objectives | Policy templates | Implemented controls | Audit evidence |

The core principle is the same: define the genome once (seed), let each domain specialise (factory), track compliance automatically (audit), learn from deviations (bubbler), and make the structure actionable for consumers (prompt builder).

The schemas read themselves, evaluate themselves, and write their own evolution proposals. The cron job runs at 8:30 AM. Nobody has to remember to check. The system remembers for you.

**Tags**: architecture, schemas, postgresql, self-improving-systems, evolution-engine, ai-agents
**Categories**: AI Automation, Tutorials, Architecture