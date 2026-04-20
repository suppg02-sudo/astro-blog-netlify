---
pubDatetime: 2026-03-08T12:00:00Z
title: "Flow System Architecture: Unified Tracking for AI Agent Interactions"
postSlug: "flow-system-architecture"
description: "A comprehensive guide to the OpenCode flow system for tracking agent interactions, decisions, and execution paths."
tags:
  - flows
  - opencode
  - observability
  - architecture
  - tracking
---

## Overview

The Flow System provides **unified tracking** for all agent interactions, decisions, and execution paths. It enables observability, debugging, and continuous improvement of AI agent workflows.

## Flow System Architecture

```mermaid
flowchart TB
    subgraph Sources["Flow Sources"]
        S1[OpenCode Agent]
        S2[Homepage Dashboard]
        S3[Cron Jobs]
        S4[Manual Trigger]
        S5[OliveTin Relay]
    end
    
    subgraph FlowTypes["Flow Types"]
        T1[question]
        T2[decision]
        T3[menu]
        T4[skill]
        T5[delegation]
        T6[action]
    end
    
    subgraph Registry["Flow Data Registry"]
        JSON[flows.json]
        QUERY[query-flows.sh]
    end
    
    subgraph Skills["Associated Skills"]
        FLOW[flow skill<br/>Execution analysis]
        CRON[cronflow skill<br/>Scheduled analysis]
        BLOG[blog-post-creator<br/>Output generation]
    end
    
    S1 --> T1
    S1 --> T2
    S1 --> T3
    S1 --> T4
    S1 --> T5
    S2 --> T6
    S3 --> T6
    S4 --> T6
    S5 --> T6
    
    T1 --> Registry
    T2 --> Registry
    T3 --> Registry
    T4 --> Registry
    T5 --> Registry
    T6 --> Registry
    
    Registry --> FLOW
    Registry --> CRON
    FLOW --> BLOG
```

## Flow Data Schema

```mermaid
classDiagram
    class Flow {
        +String id
        +DateTime timestamp
        +FlowType type
        +String source
        +String trigger
        +ChainStep[] chain
        +Result result
        +String correlation_id
        +String session_id
        +String[] tags
    }
    
    class ChainStep {
        +Int step
        +String component
        +String action
        +String detail
        +DateTime timestamp
    }
    
    class Result {
        +Boolean success
        +String outcome
        +Int duration_ms
    }
    
    class FlowType {
        <<enumeration>>
        question
        decision
        menu
        skill
        delegation
        action
    }
    
    Flow "1" --> "*" ChainStep
    Flow "1" --> "1" Result
    Flow --> FlowType
```

## Flow JSON Schema

```json
{
  "id": "flow_YYYYMMDD_HHMMSS_hash",
  "timestamp": "2026-03-08T12:00:00Z",
  "type": "question|decision|menu|skill|delegation|action",
  "source": "opencode|homepage|cron|manual|relay",
  "trigger": "what initiated this flow",
  "chain": [
    {
      "step": 1,
      "component": "component name",
      "action": "what happened",
      "detail": "additional info",
      "timestamp": "2026-03-08T12:00:01Z"
    }
  ],
  "result": {
    "success": true,
    "outcome": "description",
    "duration_ms": 1500
  },
  "correlation_id": "links related flows",
  "session_id": "opencode session if applicable",
  "tags": ["tag1", "tag2"]
}
```

## Flow Types Reference

```mermaid
graph TD
    subgraph TypeDefinitions["Flow Types"]
        Q[question<br/>Question tool interactions]
        D[decision<br/>User decisions recorded]
        M[menu<br/>Menu selection history]
        S[skill<br/>Skill invocations]
        DL[delegation<br/>Agent delegations]
        A[action<br/>OliveTin/webhook actions]
    end
    
    subgraph Sources["Primary Sources"]
        OC[OpenCode Agent]
        HP[Homepage]
        CR[Cron]
        RL[Relay/OliveTin]
    end
    
    OC --> Q
    OC --> D
    OC --> M
    OC --> S
    OC --> DL
    HP --> A
    CR --> A
    RL --> A
```

## Execution Flow Format

The flow system uses an **A>B>C>D>E** notation for execution paths:

```mermaid
flowchart TD
    subgraph FlowChain["Execution Flow Chain"]
        A["[A] User Request<br/>'Create a blog post about AI ethics'<br/>Classification: writing<br/>Complexity: medium"]
        B["[B] Agent Selection: sisyphus<br/>Category: writing<br/>Rationale: Task matches specialization"]
        C["[C] Global Rules Applied<br/>Protocol: Fabric pattern loaded<br/>Check: Structure validation passed"]
        D["[D] Skill Selection: hugo<br/>Skills Evaluated: [hugo, fabric, transcription]<br/>Skills Selected: [hugo]"]
        E["[E] Execution & Outcome: success<br/>Duration: 2m 15s<br/>Final: Blog post created, published"]
    end
    
    A --> B
    B --> C
    C --> D
    D --> E
    
    style A fill:#e1f5fe
    style B fill:#fff3e0
    style C fill:#f3e5f5
    style D fill:#e8f5e9
    style E fill:#c8e6c9
```

## Cronflow Architecture

```mermaid
flowchart LR
    subgraph Input["Input"]
        SESSION[Session Data]
        LOGS[Execution Logs]
    end
    
    subgraph Modules["Cronflow Modules"]
        RECON[flow_reconstructor.py<br/>Reconstructs execution flows]
        PATTERN[pattern_detector.py<br/>Identifies recurring patterns]
        METRICS[metrics_calculator.py<br/>Calculates KPIs]
        REC[recommendation_engine.py<br/>Generates suggestions]
        REPORT[report_generator.py<br/>Produces reports]
    end
    
    subgraph Output["Output"]
        JSON_OUT[JSON Reports]
        MARKDOWN[Markdown Summaries]
        BLOG[Hugo Blog Posts]
    end
    
    SESSION --> RECON
    LOGS --> RECON
    RECON --> PATTERN
    PATTERN --> METRICS
    METRICS --> REC
    REC --> REPORT
    REPORT --> JSON_OUT
    REPORT --> MARKDOWN
    REPORT --> BLOG
```

## Associated Components

```mermaid
graph TB
    subgraph Core["Core Components"]
        FLOWS[flows.json<br/>Flow Data Registry]
        FLOW_SKILL[flow skill<br/>Execution analysis tool]
        CRONFLOW[cronflow skill<br/>Scheduled analysis]
    end
    
    subgraph Scripts["Utility Scripts"]
        QUERY[query-flows.sh<br/>Query flows by type/source/date]
    end
    
    subgraph Integrations["Integrations"]
        BLOG[blog-post-creator<br/>Output generation]
        RESEARCH[research skill<br/>Research flow integration]
        YOUTUBE[youtube trigger<br/>YouTube workflow flow]
    end
    
    subgraph Output["Output Documents"]
        DOCS[Flow Restructuring Summaries]
        REPORTS[Session Reports]
    end
    
    FLOWS --> QUERY
    FLOWS --> FLOW_SKILL
    FLOWS --> CRONFLOW
    FLOW_SKILL --> BLOG
    CRONFLOW --> REPORTS
    FLOW_SKILL --> DOCS
    RESEARCH --> FLOWS
    YOUTUBE --> FLOWS
```

## Skill YAML Frontmatter (Flow Skill)

```yaml
---
name: flow
description: Execution flow analysis and transparency tool
color: "#808080"
license: MIT
compatibility: opencode
trigger_words:
  - "flow"
  - "smooth"
  - "review"
  - "session review"
  - "execution analysis"
metadata:
  category: analysis
  scope: meta-analysis
  output_format: markdown
  last_updated: 2026-02-09
  version: 1.2.0
  dependencies:
    - global_instructions: /media/docs/instructions/global-instructions.md
---
```

## Flow Query Interface

```bash
# Query flows by type
./query-flows.sh --type question

# Query flows by source
./query-flows.sh --source opencode

# Query flows by date range
./query-flows.sh --from 2026-03-01 --to 2026-03-08

# Query with correlation ID
./query-flows.sh --correlation-id "abc123"
```

## Flow Analysis Workflow

```mermaid
sequenceDiagram
    participant User
    participant Agent
    participant FlowRegistry
    participant FlowSkill
    participant Output
    
    User->>Agent: Execute task
    Agent->>FlowRegistry: Record flow steps
    Agent->>FlowRegistry: Record result
    Agent->>User: Return response
    
    User->>Agent: "flow" trigger
    Agent->>FlowSkill: Load flow skill
    FlowSkill->>FlowRegistry: Query recent flows
    FlowRegistry-->>FlowSkill: Return flow data
    FlowSkill->>FlowSkill: Analyze patterns
    FlowSkill->>FlowSkill: Identify inefficiencies
    FlowSkill->>Output: Generate report
    Output-->>User: Display analysis
```

## Key Metrics Tracked

| Metric | Description | Purpose |
|--------|-------------|---------|
| **Duration** | Time to complete flow | Performance optimization |
| **Success Rate** | Percentage of successful flows | Reliability monitoring |
| **Chain Length** | Number of steps in flow | Complexity analysis |
| **Correlation Count** | Related flows | Dependency tracking |
| **Tag Distribution** | Most common tags | Usage patterns |

## Benefits of Flow Tracking

1. **Observability**: See exactly what the agent did and why
2. **Debugging**: Trace failures through execution chains
3. **Optimization**: Identify bottlenecks and inefficiencies
4. **Audit Trail**: Complete history of agent decisions
5. **Continuous Improvement**: Learn from patterns and mistakes

## Integration with Skills

```mermaid
flowchart LR
    subgraph SkillsThatGenerate["Skills That Generate Flows"]
        S1[research]
        S2[blog-post-creator]
        S3[youtube trigger]
        S4[question tool]
    end
    
    subgraph SkillsThatConsume["Skills That Consume Flows"]
        C1[flow]
        C2[cronflow]
        C3[smooth]
    end
    
    subgraph Registry["Flow Registry"]
        F[flows.json]
    end
    
    S1 --> F
    S2 --> F
    S3 --> F
    S4 --> F
    
    F --> C1
    F --> C2
    F --> C3
```

---

*The Flow System enables TELOS compliance through complete observability and deterministic tracking of all agent interactions.*