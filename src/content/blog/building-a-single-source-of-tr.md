---
pubDatetime: 2026-04-10T23:14:18Z
title: "Building a Single Source of Truth for Self-Aware AI Infrastructure"
postSlug: "building-a-single-source-of-tr"
description: "Building a Single Source of Truth for Self-Aware AI Infrastructure"
tags:
  - others
---

Every AI agent starts from zero. Every session begins with amnesia. What if your infrastructure could describe itself — to itself?

## The Problem

OpenCode has 91 skills, 21 schemas, 9 factories, 59 Docker services, and 2,888 memories. The General Agent (GA) that orchestrates all of this had no way to see itself. No map. No topology. No single document that said "here's what you are, here's what you can do, here's how the pieces connect."

Instead, context was scattered across 10+ sources: YAML files, PostgreSQL tables, a 500-line AGENTS.md, wiki pages, trigger registries, deferred option lists. The GA would load fragments in isolation, never seeing the whole. When someone asked "what did we build?", even the system couldn't answer coherently.

Worse, the Triad — the constitutional loop of Schema → Signal → Auto-Improvement that drives the entire system — was described in a philosophy document (telos.md) but never mapped to concrete subsystems. You could read the principle without knowing which signals feed which schema changes.

## What I Tried First

The first attempt was a brainstorm agent session that produced a flat 5-item list: schemas, factories, skills, services, memory. It looked clean. It was wrong.

Memory was described as "experiential context" — a utility, not a peer. The topology had no connections between subsystems. The Triad was mentioned but not attached to anything. Live counts were "weekly static refresh" — meaning the document would be stale 6 days out of 7. And the whole thing was supposed to live in a brand-new top-level file, adding yet another fragmented source.

That's when it clicked: the problem wasn't the topology itself. The problem was creating yet another source of truth that didn't reference the existing ones.

## The Solution

I rebuilt it from the architecture up, not the document down. Three artifacts, each with a distinct role:

**1. `system-topology.yaml` — The Authoritative Source**

A structured YAML file with progressive disclosure built in. Every subsystem gets a triad section (schema, signals, evolution). Memory is declared as a first-class peer — "long-term memory: decisions, patterns, lessons" — not a utility.

```yaml
subsystems:
  memory:
    role: Long-term memory — decisions, patterns, lessons
    location: PostgreSQL (pgvector)
    count: 2888
    triad:
      schema: memory_schema (structured capture with tags, type, scope)
      signals:
        - memory stored
        - memory recalled
        - recall success rate
      evolution: recall analytics, scope-based retrieval tuning
```

The menu system — an intelligent interaction layer with scoring, optimization, and signal tracking — is documented as a cross-cutting concern, not buried inside the skills subsystem. Because it isn't just a skill thing. It's used by Projects, Research, and every GA interaction.

**2. `generate_system_index.py` — The Semi-Live Generator**

A Python script that reads the YAML, queries live state (schema counts from the registry, factory counts from PostgreSQL via `docker exec`, skill counts from the directory), and produces a wiki with progressive disclosure levels.

The key insight: don't try to make the YAML live. Make the YAML authoritative and the generator semi-live. The YAML says what the system *is*. The generator enriches it with what the system *currently has*.

```python
def get_factory_count():
    """Count factories from PostgreSQL."""
    result = subprocess.run(
        ["docker", "exec", "pgvector-memory", "psql", "-U", "memory_user",
         "-d", "memory_db", "-t", "-A", "-c",
         "SELECT COUNT(*) FROM aimplifi_schemas WHERE tier = 'factory'"],
        capture_output=True, text=True
    )
    return int(result.stdout.strip()) if result.returncode == 0 else 0
```

That `docker exec` pattern is important — the PostgreSQL container isn't exposed on a port the host can reach directly. You have to exec into it. The column is `tier`, not `schema_type`. These are the details that cost 30 minutes each when you discover them at runtime.

**3. `system_identity.py` — The CLI Interface**

A command-line tool with three disclosure levels. `--level L0` gives you the elevator pitch. `--level L1` adds registries and counts. `--level L2` shows connections and the full menu signal improvement pipeline. `--stats` dumps live counts.

```
$ system_identity.py --level L0
OpenCode v2026.4 — Self-improving AI infrastructure
5 subsystems: Schemas(21) Factories(9) Skills(91) Services(59) Memory(2888)
Memory is Architecture — the system's long-term memory.
Triad: Schema → Signal → Auto-Improvement. Every subsystem participates.
```

Seven words of output. Any 7B model can parse that.

## Why This Matters

The pattern here isn't specific to OpenCode. Any system with more than 5 components will eventually face the "can't see itself" problem. The solution is always the same three layers:

1. **An authoritative source** — human-maintained, structured, version-controlled. Not auto-generated. The YAML is the constitution.
2. **A generator** — reads the source, enriches with live state, produces derived artifacts. The generator is the journalist.
3. **A CLI** — progressive disclosure at the terminal. The CLI is the diplomat — it knows how much detail you can handle.

The Triad applies recursively: the YAML defines the schema of the system. The generator produces signals (counts changing, new subsystems appearing). Those signals should eventually auto-update the YAML. That's v2. For now, a human runs `--refresh` when things change.

The biggest lesson? **Memory is not a utility.** If your system's long-term store is a "helper" or a "cache," you've architecturally guaranteed amnesia. Memory must be a named subsystem with its own triad, its own signals, its own evolution path. Otherwise, every session is groundhog day.

---

**Tags**: ai-infrastructure, system-topology, progressive-disclosure, self-aware-systems, yaml
**Categories**: AI Automation, System Design