---
pubDatetime: 2026-03-08T12:00:00Z
title: "Skill Architecture Explained: From Raw Documentation to MCP Server"
postSlug: "skill-architecture-explained"
description: "A comprehensive guide to the OpenCode skill system architecture, including maturity levels, components, and evolution pathways."
tags:
  - skills
  - opencode
  - automation
  - architecture
  - mcp
---

## Overview

The OpenCode skill system uses a **Knowledge Crystallization Pipeline** - converting probabilistic LLM interactions into deterministic, reusable components. This post explains the complete architecture.

## Skill Maturity Levels

Skills evolve through five distinct levels of maturity:

```mermaid
flowchart TD
    subgraph L1["Level 1: Raw"]
        A1[SKILL.md only]
        A2[Documentation-focused]
        A3[No automation]
    end
    
    subgraph L2["Level 2: Structured"]
        B1[YAML frontmatter]
        B2[Structured sections]
        B3[Commands section]
    end
    
    subgraph L3["Level 3: Script-Attached"]
        C1[Shell/Python scripts]
        C2[Error handling]
        C3[--help flags]
    end
    
    subgraph L4["Level 4: API-Integrated"]
        D1[REST endpoints]
        D2[Health checks]
        D3[Structured output]
    end
    
    subgraph L5["Level 5: MCP/Deterministic"]
        E1[MCP server]
        E2[Typed tools]
        E3[Deterministic execution]
    end
    
    L1 -->|Add metadata| L2
    L2 -->|Add scripts| L3
    L3 -->|Add API| L4
    L4 -->|Add MCP| L5
    
    style L1 fill:#ffcccc
    style L2 fill:#ffe6cc
    style L3 fill:#ffffcc
    style L4 fill:#ccffcc
    style L5 fill:#ccccff
```

## Skill Directory Structure

```mermaid
graph TD
    subgraph SkillDirectory["skill-name/"]
        MD[SKILL.md<br/>Required: Main documentation]
        
        subgraph Config["config/"]
            YAML[skill.yaml<br/>Metadata, version, dependencies]
            MENU[menu.json<br/>Interactive menu definitions]
            CREDS[credentials.sh<br/>Sensitive credentials]
            CRON[cron-jobs.txt<br/>Scheduled job definitions]
        end
        
        subgraph Scripts["scripts/"]
            SH1[status.sh]
            SH2[backup.sh]
            SH3[*.py / *.sh]
        end
        
        subgraph Data["data/"]
            JSON[Exported data JSON]
        end
        
        subgraph History["history/"]
            USAGE[usage/]
            AUDIT[audit/]
            REPORTS[reports/]
        end
        
        subgraph Templates["templates/"]
            TPL[Output templates L4+]
        end
        
        BACKUPS[backups/<br/>Configuration backups]
    end
    
    MD --> Config
    Config --> Scripts
    Scripts --> Data
    Scripts --> History
    Config --> Templates
    Config --> BACKUPS
```

## Quality Gates Between Levels

```mermaid
flowchart LR
    subgraph G1["Skill Gate"]
        SG1[YAML metadata]
        SG2[Sections defined]
        SG3[Examples provided]
        SG4[Working directory set]
    end
    
    subgraph G2["Script Gate"]
        SG5[Error handling]
        SG6[Exit codes]
        SG7[Timeout handling]
        SG8[Tests written]
    end
    
    subgraph G3["API Gate"]
        SG9[OpenAPI spec]
        SG10[Health checks]
        SG11[Error response schema]
    end
    
    subgraph G4["MCP Gate"]
        SG12[Tool JSON schemas]
        SG13[Capability declaration]
        SG14[Transport config]
    end
    
    WORK[Ad-hoc Work] --> G1
    G1 --> SCRIPTS[Scripts]
    SCRIPTS --> G2
    G2 --> API[API Layer]
    API --> G3
    G3 --> MCP[MCP Server]
    MCP --> G4
    G4 --> PRODUCTION[Production Ready]
```

## Skill Loading Precedence

```mermaid
flowchart TB
    subgraph Priority["Loading Priority (0 = Lowest)"]
        P0["0. Built-in skills<br/>(package default)"]
        P1["1. User skills<br/>(~/.config/opencode/skills/)"]
        P2["2. Project skills<br/>(./skills/)"]
        P3["3. Project-agent skills<br/>(./agents/skills/)"]
    end
    
    P0 --> P1
    P1 --> P2
    P2 --> P3
    
    P3 --> FINAL[Final Skill Loaded]
    
    style P3 fill:#90EE90
    style FINAL fill:#98FB98
```

## YAML Frontmatter Schema

```yaml
---
name: skill-name
description: Brief description of the skill
version: 1.0.0
created: 2026-03-08
status: production | development | deprecated
maturity: L1 | L2 | L3 | L4 | L5
author: AuthorName
tags: [tag1, tag2, tag3]
dependencies:
  - dependency1
  - dependency2
---
```

## Full skill.yaml Schema (L3+)

```yaml
name: router
version: 3.0.0
description: Comprehensive network management
status: production
trigger: router
aliases:
  - edgerouter
  - network
last_updated: 2026-03-07T20:40:00Z

features:
  - port_forwarding
  - dhcp_management
  - firewall_rules

cron_jobs:
  - name: daily_backup
    schedule: "0 4 * * *"
    command: "scripts/backup.sh"
    enabled: true

dependencies:
  required_tools:
    - bash
    - ssh
    - sshpass
  associated_skills:
    - name: nginx
      level: intimate
      purpose: "Monitor reverse proxy"
```

## Menu Schema (menu.json)

```json
{
  "skill": "skill-name",
  "version": "3.0.0",
  "menus": {
    "main": {
      "header": "Menu Title",
      "question": "What would you like to do?",
      "multiple": false,
      "options": [
        {
          "id": "action-id",
          "label": "📊 Label Text",
          "description": "Description of action",
          "action": "exec:scripts/action.sh"
        },
        {
          "id": "submenu",
          "label": "📋 Submenu",
          "description": "Open submenu",
          "action": "show-menu:submenu-name"
        }
      ]
    }
  }
}
```

## Standardized Output Schema (L3+)

```python
from pydantic import BaseModel

class SkillOutput(BaseModel):
    success: bool
    data: dict | None
    error: str | None
    meta: dict  # duration, tokens, cache_hit, trace_id
```

## Evolution Decision Matrix

```mermaid
graph TD
    subgraph DecisionMatrix["Evolution Target by Type"]
        SM[Service Management] -->|Target: L5| MCP1[MCP Server]
        DP[Data Processing] -->|Target: L4| API[REST API]
        AT[Automation Tasks] -->|Target: L3| SCRIPTS[Scripts]
        MT[Methodologies] -->|Target: L2| DOC[Documentation]
        PP[Physical Processes] -->|Target: L1| RAW[Raw Skill]
    end
    
    style MCP1 fill:#ccccff
    style API fill:#ccffcc
    style SCRIPTS fill:#ffffcc
    style DOC fill:#ffe6cc
    style RAW fill:#ffcccc
```

## Skill Evolution Checklist

| Transition | Actions Required |
|------------|-----------------|
| **L1→L2** | Add YAML frontmatter, structured sections, commands section |
| **L2→L3** | Create scripts/, add error handling, add --help flags |
| **L3→L4** | Document API endpoints, add curl examples, health checks |
| **L4→L5** | Create MCP server, define tool schemas, implement transport |

## 2026 Determinism Formula

```
Determinism = Schema Validation + State Reducer + Tool Mocks + Policy Gates
```

**Critical**: `temperature=0` does NOT achieve determinism. Reliability comes from **architecture + guardrails**, not better prompts.

## Current Skills Inventory

| Level | Count | Examples |
|-------|-------|----------|
| **L5** | 1 | agent-browser |
| **L4** | 2 | tracking, openrag |
| **L3** | 5 | router (13 scripts), news, cronflow |
| **L2** | 42 | research, flow, blog-post-creator |
| **L1** | 21 | versions, beautiful-mermaid |
| **L0** | 3 | Incomplete skills |

## Key Insight

Not all skills should reach Level 5. Methodology skills (research, telos) should remain at L2 (documentation-only). Service management skills should evolve to L5 for deterministic execution.

---

*This architecture enables progressive enhancement while maintaining simplicity for documentation-only skills.*