---
pubDatetime: 2026-03-26T23:28:25Z
title: "Schemas: Guardrails & Quality Gates"
postSlug: "schemas-guardrails-quality-gat"
description: "Schemas: Guardrails & Quality Gates"
tags:
  - json-schema
  - ai
  - schemas
  - validation
---

> **Series**: Knowledge Crystallization | **Post**: 4/5 | **Complexity**: L4
>
> 📍 Breadcrumb: [Series Home](/posts/knowledge-crystallization-seri) › [1. Problem](/posts/the-problem-why-your-ai-assist) › [2. Architecture](/posts/architecture-progressive-discl) › [3. Meta-Skills](/posts/meta-skills-skills-that-create) › **4. Schemas**

---

## The Role of Schemas

Schemas are **contracts**. They define what's valid before execution begins.

```
┌─────────────────────────────────────────────────────────────┐
│                    SCHEMA ROLE                               │
│                                                              │
│   Without schemas:                                           │
│   Input ───► [AI] ───► ??? (undefined behavior)            │
│                                                              │
│   With schemas:                                              │
│   Input ───► [VALIDATE] ───► [AI] ───► [VALIDATE] ───► Output
│                 │                        │                  │
│                 ▼                        ▼                  │
│            Fail fast              Verify structure          │
│            Clear errors           Type safety               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Quality Gates

Quality gates are checkpoints in the evolution pipeline:

```
Work ───► [SKILL GATE] ───► Scripts ───► [SCRIPT GATE] ───► API ───► [API GATE] ───► MCP
              │                            │                      │
              ▼                            ▼                      ▼
     ┌────────────────┐        ┌────────────────┐      ┌────────────────┐
     │ YAML metadata  │        │ Error handling │      │ OpenAPI spec   │
     │ Sections       │        │ Exit codes     │      │ Health checks  │
     │ Examples       │        │ Timeouts       │      │ Error schemas  │
     │ Working dir    │        │ Tests pass     │      │ Rate limits    │
     └────────────────┘        └────────────────┘      └────────────────┘
```

| Gate | Level | Validation Criteria | When Applied |
|------|-------|---------------------|--------------|
| **Skill Gate** | L1→L2 | YAML metadata, sections, examples | After skill creation |
| **Script Gate** | L2→L3 | Error handling, exit codes, tests | Before script attachment |
| **API Gate** | L3→L4 | OpenAPI spec, health checks | Before API integration |
| **MCP Gate** | L4→L5 | Tool schemas, capability declaration | Before MCP deployment |

---

## The Skill Schema

Every L3+ skill validates against a JSON Schema:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Skill Configuration Schema",
  "type": "object",
  "required": ["name", "version", "maturity"],
  "properties": {
    "name": {
      "type": "string",
      "pattern": "^[a-z][a-z0-9-]*$
    },
    "version": {
      "type": "string",
      "pattern": "^\\d+\\.\\d+\\.\\d+$
    },
    "maturity": {
      "type": "string",
      "enum": ["L1", "L2", "L3", "L4", "L5"]
    }
  }
}
```

<details>
<summary>📖 Deep Dive: Schema Validation (L1)</summary>

### Why Schemas Matter

1. **Fail Fast**: Catch errors before execution
2. **Clear Errors**: Know exactly what's wrong
3. **Type Safety**: Prevent runtime surprises
4. **Documentation**: Schema IS documentation
5. **Determinism**: Same input → same validation → same result

### Validation Example

**Invalid skill.yaml**:
```yaml
name: MySkill
version: 1.0
maturity: L6
```

**Validation Error**:
```
Error at /name: does not match pattern "^[a-z][a-z0-9-]*$
  - "MySkill" should be "my-skill

Error at /version: does not match pattern "^\d+\.\d+\.\d+$
  - "1.0" should be "1.0.0

Error at /maturity: not in enum ["L1", "L2", "L3", "L4", "L5"]
  - "L6" is not a valid maturity level
```

</details>

---

<details>
<summary>🔧 Implementation: Pydantic Models (L2)</summary>

```python
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from enum import Enum

class MaturityLevel(str, Enum):
    L1 = "L1
    L2 = "L2
    L3 = "L3
    L4 = "L4
    L5 = "L5

class SkillInput(BaseModel):
    name: str = Field(..., pattern=r"^[a-z][a-z0-9-]*$")
    version: str = Field(..., pattern=r"^\d+\.\d+\.\d+$")
    maturity: MaturityLevel = Field(default=MaturityLevel.L2)
    triggers: List[str] = Field(default_factory=list, min_items=1)
    
    @validator('name')
    def name_not_reserved(cls, v):
        reserved = ['test', 'temp', 'tmp']
        if v in reserved:
            raise ValueError(f"'{v}' is a reserved name")
        return v

class SkillOutput(BaseModel):
    success: bool
    data: Optional[dict]
    error: Optional[str]
    meta: dict

# Usage
try:
    skill = SkillInput(name="my-skill", version="1.0.0")
    print(skill.json())
except ValidationError as e:
    print(f"Invalid: {e}")
```

</details>

---

## Standardized Output Schema

All L3+ skills should use structured output:

```python
from pydantic import BaseModel
from typing import Optional

class SkillOutput(BaseModel):
    success: bool
    data: Optional[dict]
    error: Optional[str]
    meta: dict  # duration, tokens, cache_hit, trace_id
```

**Example output**:
```json
{
  "success": true,
  "data": {
    "documents_found": 5,
    "query": "progressive disclosure
  },
  "error": null,
  "meta": {
    "duration_ms": 234,
    "tokens_used": 1234,
    "cache_hit": false,
    "trace_id": "flow_20260326_abc123
  }
}
```

---

## The Three-Layer Guardrail Model

For L4-L5 skills, implement multiple guardrail layers:

| Layer | Purpose | Latency | When to Use |
|-------|---------|---------|-------------|
| **Rule-Based** | Schema, format, types | <10ms | Always |
| **ML Classifier** | Toxicity, bias, anomalies | 50-200ms | User-facing, public |
| **LLM Validation** | Semantic correctness | 300ms-2s | High-stakes only |

<details>
<summary>🔧 Implementation: Policy Gate Pipeline (L2)</summary>

```python
from typing import Callable, Any
from dataclasses import dataclass
import time

@dataclass
class GateResult:
    passed: bool
    reason: str
    latency_ms: int

def schema_gate(data: dict, schema: dict) -> GateResult:
    """Layer 1: Schema validation - always runs""
    start = time.time()
    try:
        from jsonschema import validate
        validate(instance=data, schema=schema)
        return GateResult(passed=True, reason="Valid", latency_ms=int((time.time() - start) * 1000))
    except Exception as e:
        return GateResult(passed=False, reason=str(e), latency_ms=int((time.time() - start) * 1000))

def ml_classifier_gate(text: str, checks: list) -> GateResult:
    """Layer 2: ML classification - optional""
    start = time.time()
    # Simulate ML classification
    time.sleep(0.05)  # 50ms latency
    
    if "toxic" in checks and "badword" in text.lower():
        return GateResult(passed=False, reason="Toxic content detected", latency_ms=50)
    
    return GateResult(passed=True, reason="Clean", latency_ms=50)

def llm_validation_gate(input_text: str, output_text: str) -> GateResult:
    """Layer 3: LLM validation - high-stakes only""
    start = time.time()
    # Secondary LLM call to verify output
    time.sleep(0.3)  # 300ms latency
    return GateResult(passed=True, reason="Semantically valid", latency_ms=300)

class PolicyPipeline:
    def __init__(self, gates: list):
        self.gates = gates
    
    def run(self, data: Any) -> GateResult:
        for gate_name, gate_func, gate_args in self.gates:
            result = gate_func(data, **gate_args)
            if not result.passed:
                return result
        return GateResult(passed=True, reason="All gates passed", latency_ms=0)
```

</details>

---

## The Complete Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    COMPLETE DETERMINISM ARCHITECTURE                     │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                         INPUT LAYER                               │   │
│  │                                                                   │   │
│  │   User Input ───► [Schema Validation] ───► Validated Input       │   │
│  │                          │                                        │   │
│  │                          ▼                                        │   │
│  │                    Policy Gate 1                                  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                    │                                    │
│                                    ▼                                    │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                        PROCESSING LAYER                           │   │
│  │                                                                   │   │
│  │   State ───► Action ───► [State Reducer] ───► New State          │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                    │                                    │
│                                    ▼                                    │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                         OUTPUT LAYER                              │   │
│  │                                                                   │   │
│  │   Output ───► [Schema Validation] ───► [Policy Gate 2] ───► User │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  Result: Same input → Same state transitions → Same output              │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## What's Next?

In [Post 5: Determinism](/posts/the-2026-determinism-formula), we'll reveal:

- The 2026 Determinism Formula
- Why temperature=0 isn't enough
- State reducers and tool mocks
- The complete deterministic stack

---

## Navigation

- ⬅️ [← Previous: Meta-Skills](/posts/meta-skills-skills-that-create)
- 🏠 [Series Home](/posts/knowledge-crystallization-seri)
- ➡️ [Next: Determinism →](/posts/the-2026-determinism-formula)