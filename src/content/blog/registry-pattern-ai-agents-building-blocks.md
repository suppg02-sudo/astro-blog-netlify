---
pubDatetime: 2026-02-27T03:50:00Z
title: "The Registry Pattern for AI Agents: Building Blocks for Deterministic behavior"
postSlug: "registry-pattern-ai-agents-building-blocks"
description: "The Registry Pattern for AI Agents: Building Blocks for Deterministic behavior"
tags:
  - opencode
  - registries
  - ai-agents
  - architecture
  - mcp
---

In the previous post, I introduced the **Central Menu System** for AI agent skills - a single source of truth for mandatory options that every skill menu must reference.

 This pattern works, but building on a Central configuration creates consistency as you add more skills.

But there's a catch: as you scales from 50 to 500+ skills, manually managing each skill becomes unwield. Registries help solve this.

## The Problem

As skill libraries grow, several problems emerge:

1. **Configuration Drift** - Each skill manages its differently
2. **No guardrails** - Agents can refuse requests, bypass validation, or act unexpectedly
3. **Knowledge duplication** - Documentation gets copied across skills
4. **Inconsistent decisions** - No record of why certain choices were made

 or how decisions impact the system

## Enter: Registries

Registries are the the problem by providing a **single source of truth** for a specific domain.

 Not just menus - they're now reference-based. More efficient.

### Registry Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Source of Truth** | Single file or database that all configuration |
| **Reference-based** | Skills don't inherit from regist, they reference it |
| **Policy + Process + Design** | All in one place |
| **Auditable** | Changes are tracked, versioned |

## The Registry Types

### What Exists now

| Registry | Example | Maturity |
|---------------|---------|--------|
| **Tool Registry** | MCP `tools/list` | ✅ Standard |
| **Configuration Registry** | LiteLLM, credentials | ✅ Common |
| **Context Registry** | Question/skill history | ✅ We built |
| **Skill Registry** | skill-discovery | ✅ New |

### What's missing (Novel patterns)

| Registry | Purpose | Key Insight |
|---------------|---------|---------|
| **Trigger Registry** | Maps words → actions | 🆕 **No standard exists** - create new patterns |
| **Decision Registry** | Records choices and rationale | 🆕 **No standard exists** - create new patterns |
| **Policy Registry** | Rules and constraints | 🆕 **No standard exists** - create new patterns |
| **Telemetry Registry** | What to track | 🆕 **Partial** - LiteLLM logs |
| **Agent Registry** | Agent capabilities | 🆕 **No standard exists** - define agent metadata |

## Why This Matters

### Determinism vs Flexibility
The - **Determinism** = Schema validation + policy gates → predictable behavior
    - **Flexibility** = Reference-based design → easier to evolve
    - **Both patterns coexist** - Registries can complement each other

### Design Principles

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  CENT Menu Registry                          │
│  ┌───────────────────────────────────────────────────────────────────┐
│  │   ├── What to do?                                   │
│  │   │   ├── 🔍 Skill Discovery                             │
│  │   │   ├── Exit                                        │
└─────────────────────────────────────────────────────────────────────────┘
│                                                            │
│  Each skill menu inherits from central registry          │
└─────────────────────────────────────────────────────────────────────┘
```

**Reference, don't inherit.** Skills don't extend a base class - they reference a central configuration.

### Proposed: Decision Registry

```json
{
  "decisions": [
    {
      "id": "dec_001",
      "timestamp": "2026-02-27T10:30:00Z",
      "context": {
        "skill": "containers",
        "session": "abc123",
        "task": "Installing Docker container"
      },
      "decision": {
        "type": "skill_selection",
        "selected": ["Install Containers", "Create new container"],
        "rationale": "User wanted to install a specific container",
        "alternatives": ["Discover projects", "Test APIs", "View Status"]
      },
      "confidence": 0.85,
      "outcome": {
        "success": true,
        "action_taken": "skill.containers.install",
        "duration_ms": 2340
      }
    }
  ]
}
```

**Every interaction with the question tool is logged to the Decision registry:**

```python
def record_decision(interaction):
    """Record every decision to the registry."""
    registry = DecisionRegistry()
    registry.record({
        timestamp: now(),
        skill: skill_name,
        choice: user_choice,
        rationale: reason,
        outcome: result
    })
```

### Decision Registry Schema

```json
{
  "schema": {
    "type": "object",
    "properties": {
      "id": {" "type": "string" },
      "timestamp": {" "type": "string", "format": "date-time" },
      "skill": {" "type": "string" },
      "session": {" "type": "string" },
      "context": {" "type": "object" },
      "decision": {
        "type": "object",
        "properties": {
          "type": {" "type": "string", "enum": ["skill_selection", "tool_selection", "routing", "information_request", "user_override", "clarification"] },
          "selected": {" "type": "array", "items": {" "type": "string" } },
          "rationale": {" "type": "string" },
          "alternatives": {" "type": "array", "items": {" "type": "string" } },
          "confidence": {" "type": "number" },
          "outcome": {
            "success": {" "type": "boolean" },
            "action_taken": {" "type": "string" },
            "duration_ms": {" "type": "number" }
          }
        },
        "required": ["timestamp", "skill", "decision", "selected"]
      }
    }
  }
}
```

## Use Cases

Let me walk through a few examples:

### Example: Installing a Container

```json
{
  "skill": "containers",
  "question": "What Docker image to install?",
  "options": [
    {"label": "Install Containers", "description": "Install from pre-configured list"},
    {"label": "Discover Projects", "description": "Search GitHub for popular images"},
    {"label": "Test/Debug APIs", "description": "Test running container APIs"},
    {"label": "View Status", "description": "Show all containers"}
  ]
}
```

**Decision recorded:**
```json
{
  "timestamp": "2026-02-27T10:35:00Z",
  "skill": "containers",
  "choice": ["Install Containers"],
  "rationale": "User wanted Portainer for GUI management",
  "alternatives": ["Discover Projects", "Test APIs", "View Status"],
  "confidence": 0.85,
  "outcome": {
    "success": true,
    "action_taken": "skill.containers.install",
    "duration_ms": 2340
  }
}
```

### Decision Registry Integration

```python
# After any decision, log to registry
decision_registry.record(decision)

# Query registry for analysis
recent_decisions = decision_registry.analyze_by_skill(
    query={
        "skill": "containers",
        "timeframe": "last_30d"
    }
    return {
        "most_common": "Install Containers",
        "least_common": "Discover Projects",
        "avg_confidence": 0.85
    }
```

This enables:
- **Audit trails** - Every decision is logged
 who, what, when
- **Policy enforcement** - Refusal gates check for policy violations
- **Improvement cycles** - Analy patterns to suggest improvements

## The Roadmap

```
Phase 1: Audit existing registries
Phase 2: Implement missing registries
Phase 3: Create trigger registry
Phase 4: Build decision registry
Phase 5: Add telemetry controls
Phase 6: Create policy registry
```

### What's Next?

1. **Tool Registry** - Adopt MCP for tool discovery
2. **Configuration Registry** - Implement centralized credentials
3. **Trigger Registry** - Create new pattern
4. **Decision Registry** - Start recording decisions
5. **Policy Registry** - Define explicit rules
6. **Telemetry Registry** - Add to context registry

 extend with labels

## Conclusion

Registries provide the scaffolding for scalable AI agent systems. While tool registry is MCP) is mature, the **trigger registry** and **Decision Registry** patterns are novel. If you build them, you're creating new patterns for the ecosystem.