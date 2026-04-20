---
pubDatetime: 2026-03-08T01:10:00Z
title: "Skill Output Schema Standardization: From Ad-hoc to Deterministic"
postSlug: "skill-output-schema-standardization"
description: "How we created a standardized output schema for OpenCode skills, enabling deterministic behavior across all skill levels from ad-hoc scripts to MCP servers."
tags:
  - skills
  - pydantic
  - opencode
  - schema
  - architecture
  - determinism
---

## The Problem: Ad-hoc Output Formats

Every skill was inventing its own output format. Diagnose returned one structure, containers returned another, and debugging across skills meant learning multiple formats.

```python
# Skill A
{"status": "ok", "result": {...}}

# Skill B  
{"success": true, "data": {...}}

# Skill C
{"state": "COMPLETE", "output": {...}}
```

This made:
- **Testing** difficult - each skill needed custom assertions
- **Error handling** inconsistent - no standard error codes
- **Observability** fragmented - couldn't aggregate metrics
- **MCP integration** messy - each tool needed custom schemas

## The Solution: Centralized Skill Output Schema

We created a single schema file that all Level 3+ skills use:

**Location**: `~/.config/opencode/schemas/skill_output.py`

```python
from pydantic import BaseModel, Field
from typing import Any, Optional
from datetime import datetime
from enum import Enum

class SkillStatus(str, Enum):
    SUCCESS = "success"
    PARTIAL = "partial"
    FAILED = "failed"
    PENDING = "pending"

class SkillMeta(BaseModel):
    skill_name: str
    skill_level: int = Field(default=3, ge=1, le=5)
    duration_ms: int = Field(default=0)
    timestamp: datetime = Field(default_factory=datetime.now)
    trace_id: Optional[str] = None
    cache_hit: bool = False
    tokens_used: Optional[int] = None
    version: str = "1.0.0"
    hostname: Optional[str] = None

class SkillOutput(BaseModel):
    status: SkillStatus
    success: bool
    data: Optional[dict[str, Any]] = None
    error: Optional[str] = None
    error_code: Optional[str] = None
    meta: SkillMeta
    suggestions: Optional[list[str]] = None
```

## Factory Functions for Easy Usage

Instead of manually constructing `SkillOutput`, we provide factory functions:

```python
from schemas.skill_output import create_skill_output, create_error_output, ErrorCodes
import time

# Success case
start = time.time()
# ... do work ...
result = create_skill_output(
    skill_name="containers",
    data={"running": 5, "healthy": 4},
    skill_level=3,
    start_time=start,
    suggestions=["Check unhealthy container: nginx-proxy"]
)
```

Output:
```json
{
  "status": "success",
  "success": true,
  "data": {
    "running": 5,
    "healthy": 4
  },
  "error": null,
  "error_code": null,
  "meta": {
    "skill_name": "containers",
    "skill_level": 3,
    "duration_ms": 15,
    "timestamp": "2026-03-08T01:01:04.014700",
    "trace_id": "aecc49c8",
    "cache_hit": false,
    "version": "1.0.0",
    "hostname": "ubuntu4"
  },
  "suggestions": ["Check unhealthy container: nginx-proxy"]
}
```

```python
# Error case
result = create_error_output(
    skill_name="containers",
    error="Connection refused to docker socket",
    error_code=ErrorCodes.SERVICE_UNAVAILABLE,
    suggestions=["Ensure docker service is running"]
)
```

## Standard Error Codes

```python
class ErrorCodes:
    TIMEOUT = "ERR_TIMEOUT"
    NOT_FOUND = "ERR_NOT_FOUND"
    PERMISSION_DENIED = "ERR_PERMISSION"
    INVALID_INPUT = "ERR_INVALID_INPUT"
    SERVICE_UNAVAILABLE = "ERR_SERVICE_DOWN"
    DEPENDENCY_FAILED = "ERR_DEPENDENCY"
    UNKNOWN = "ERR_UNKNOWN"
```

## Integration with Diagnose Skill (Level 5)

The diagnose skill is our reference implementation for Level 5 (MCP/Deterministic):

```python
# In mcp_server.py
from schemas.skill_output import SkillOutput, SkillStatus, SkillMeta

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> List[TextContent]:
    start_time = time.time()
    
    try:
        result = safe_run_script("quick-check.sh", timeout=30)
        
        # Wrap in standardized output
        output = SkillOutput(
            status=SkillStatus.SUCCESS,
            success="error" not in result,
            data=result,
            meta=SkillMeta(
                skill_name="diagnose",
                skill_level=5,
                duration_ms=int((time.time() - start_time) * 1000)
            )
        )
        return [TextContent(type="text", text=output.json(indent=2))]
        
    except Exception as e:
        error_output = create_error_output(
            skill_name="diagnose",
            error=str(e),
            error_code=ErrorCodes.UNKNOWN
        )
        return [TextContent(type="text", text=error_output.json(indent=2))]
```

## The 2026 Determinism Formula

This schema is part of our larger determinism strategy:

```
Determinism = Schema Validation + State Reducer + Tool Mocks + Policy Gates
```

**Key insight**: Setting `temperature=0` on your LLM does NOT achieve determinism. True reliability comes from:

1. **Schema Validation** - Pydantic ensures structured outputs
2. **State Reducers** - Pure functions with predictable outputs
3. **Tool Mocks** - Testable without external dependencies
4. **Policy Gates** - Guardrails at each evolution level

## Skill Maturity Levels

The schema applies to Level 3+ skills:

| Level | Name | Schema Usage |
|-------|------|--------------|
| **1** | Raw | No schema (documentation only) |
| **2** | Structured | No schema (YAML frontmatter) |
| **3** | Script-Attached | **Schema required** |
| **4** | API-Integrated | **Schema + OpenAPI spec** |
| **5** | MCP/Deterministic | **Schema + MCP tool schemas** |

## Quality Gates

Each skill evolution level has a gate:

```
Work → [SKILL GATE] → Scripts → [SCRIPT GATE] → API → [API GATE] → MCP
```

| Gate | Validation |
|------|------------|
| **Skill Gate** | YAML metadata, sections, examples |
| **Script Gate** | Error handling, exit codes, timeout handling |
| **API Gate** | OpenAPI spec, health checks, error schema |
| **MCP Gate** | Tool JSON schemas, capability declaration |

## Files Created

```
~/.config/opencode/schemas/
├── __init__.py              # Package exports
└── skill_output.py          # Schema definitions

~/.config/opencode/AGENTS.md # Updated with schema reference
```

## Usage in Your Skills

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path.home() / ".config" / "opencode"))

from schemas.skill_output import create_skill_output, create_error_output, ErrorCodes

def my_skill_function():
    start = time.time()
    
    try:
        data = do_something()
        return create_skill_output(
            skill_name="my-skill",
            data=data,
            skill_level=3,
            start_time=start
        )
    except TimeoutError:
        return create_error_output(
            skill_name="my-skill",
            error="Operation timed out",
            error_code=ErrorCodes.TIMEOUT
        )
```

## Benefits Achieved

1. **Consistent Testing** - Same assertions work across all skills
2. **Unified Error Handling** - Standard error codes enable programmatic handling
3. **Observability** - `meta.duration_ms`, `meta.trace_id` for distributed tracing
4. **MCP Integration** - Clean tool schemas without duplication
5. **Documentation** - Schema is self-documenting with Pydantic descriptions

## Next Steps

- Update remaining L3+ skills to use schema
- Add `test_skill_output.py` with comprehensive tests
- Create Grafana dashboard for skill metrics
- Document in Supermemory for persistence

---

**Schema Location**: `~/.config/opencode/schemas/skill_output.py`

**Reference Implementation**: `~/.config/opencode/skills/diagnose/mcp_server.py`

**AGENTS.md Section**: "Standardized Output Schema" (lines 1308-1365)