---
pubDatetime: 2026-03-07T14:50:00Z
title: "System Coherence Analysis: Detecting Architectural Drift in AI Agent Orchestration"
postSlug: "system-coherence-analysis"
description: "System Coherence Analysis: Detecting Architectural Drift in AI Agent Orchestration"
tags:
  - opencode
  - cron
  - automation
  - telos
  - architecture
---

## Overview

As AI agent systems grow in complexity, maintaining coherence across documentation, configuration, and implementation becomes critical. This post introduces a **System Coherence Analysis** system that automatically detects architectural drift, TELOS principle violations, and documentation gaps.

## The Problem

Modern AI orchestration systems have multiple interacting layers:

- **Flow**: Primary orchestration with gates, tasks, and state management
- **Control Planes**: Coordination mechanisms for agent behavior
- **Memory**: Persistent storage with semantic search
- **Scheduling**: Cron jobs and automation

When these layers drift out of alignment, subtle bugs emerge:
- Documentation says one thing, code does another
- TELOS principles get violated by convenience
- Roadmap claims "pending" but features are already live

## The Solution

A cron job that runs daily, analyzing four key documents:

1. **telos.md** — TELOS constitution (6 principles)
2. **environment.md** — Running services and configuration
3. **AGENTS.md** — Global rules and agent behavior
4. **roadmap.json** — Project phases and progress

## Architecture Diagram

{{< mermaid >}}
graph TB
    subgraph FLOW["<b>FLOW LAYER</b> - Primary Orchestration"]
        F1[flow/SKILL.md<br/>Meta-analytical tool]
        F2[cronflow/SKILL.md<br/>Scheduled analysis]
        F3[triggers/flows.md<br/>User interface]
        F4[query-flows.sh<br/>Unified query]
    end
    
    subgraph CONTROL["<b>CONTROL PLANES</b> - Coordination"]
        C1[AGENTS.md<br/>Global rules]
        C2[context-registry<br/>Progressive disclosure]
        C3[tracking<br/>8 context types]
        C4[questions<br/>Menu system]
        C5[menu-system<br/>Enhancement]
    end
    
    subgraph MEMORY["<b>MEMORY LAYER</b> - Persistence"]
        M1[OpenMemory MCP<br/>Vector store + HSG]
        M2[SQLite: memories.db<br/>1,083 records]
        M3[hybrid_memory.py<br/>Fast local cache]
    end
    
    subgraph SCHEDULING["<b>SCHEDULING LAYER</b> - Automation"]
        S1[cronflow<br/>Periodic analysis]
        S2[overnight_indexing<br/>Background sync]
        S3[memory-report<br/>8h stats]
        S4[automation-health<br/>5m monitoring]
    end
    
    %% Connections
    F1 --> C1
    F2 --> S1
    C1 --> M1
    C2 --> M2
    C3 --> M2
    M1 --> S3
    S2 --> M1
    
    %% Cross-layer communication
    F4 -.-> M2
    C4 -.-> M1
{{< /mermaid >}}

## TELOS Principles Checked

The analysis validates against 6 core principles:

| Principle | Description |
|-----------|-------------|
| **Data Sovereignty** | Self-hosted infrastructure is default |
| **Open Source** | Prefer open-source alternatives |
| **Local-First AI** | Local LLM inference via Ollama is primary |
| **Deterministic Workflows** | Outcomes are predictable and auditable |
| **Observability** | All actions produce logs for analysis |
| **Self-Understanding** | System understands itself through natural language |

## Detection Capabilities

### 1. TELOS Compliance Checking

Scans all documents for violation patterns:

```python
# Example violations detected
"proprietary" → violates open_source
"external api" → violates data_sovereignty
"openai api" → violates local_first_ai
```

### 2. Cross-Document Consistency

- Roadmap status vs. environment.md implementation
- TELOS references in AGENTS.md
- Service documentation coverage

### 3. Gap Analysis

- Skills referenced but not documented
- Features implemented but marked pending
- Documentation drift from reality

## Implementation

### Main Script

```bash
# Location
/root/scripts/system-coherence-analysis.py

# Run manually
python3 /root/scripts/system-coherence-analysis.py --verbose
```

### Cron Job

```cron
# System Coherence Analysis - Daily at 5:00 AM UTC
0 5 * * * /usr/bin/python3 /root/scripts/system-coherence-analysis.py >> /root/cron-logs/system-coherence.log 2>&1
```

### Output Report

Reports are saved to `/root/cron-logs/system-coherence-YYYYMMDD_HHMMSS.md` with:

- TELOS compliance score (0-100)
- Misalignments by severity (high/medium/low)
- Gap analysis with recommendations
- Architecture diagram (Mermaid)
- Recent work patterns from SQLite

## First Run Results

Running against a real OpenCode system:

| Metric | Value |
|--------|-------|
| **TELOS Compliance** | 50.0/100 |
| **Total Misalignments** | 16 |
| **Gaps Identified** | 42 |

### Top Issues Found

1. **External API references** — Conflicts with local-first AI principle
2. **Missing TELOS references** — environment.md doesn't link all 6 principles
3. **Roadmap drift** — Some pending phases appear implemented

## Best Practices Applied

Based on research from production systems:

| Source | Pattern Applied |
|--------|----------------|
| **MXCP** | Baseline snapshot comparison |
| **ruflo** | architectural_drift analysis type |
| **FluentDocs** | Documentation drift detection |
| **TechDebt.guru** | AI architecture drift patterns |

## OpenMemory Integration

Results are automatically stored to OpenMemory with structured metadata:

```json
{
  "type": "flow",
  "subtype": "coherence_analysis",
  "telos_compliance_score": 50.0,
  "total_misalignments": 16,
  "gaps_identified": 42
}
```

This enables:
- Historical trend tracking
- Semantic search for past issues
- Pattern recognition across runs

## Conclusion

System coherence analysis transforms documentation maintenance from a manual, error-prone process into an automated, measurable practice. By running daily checks against TELOS principles and cross-document consistency, we catch drift before it becomes technical debt.

The 5-layer architecture (Flow → Control → Memory → Scheduling → MCP) provides clear separation of concerns, making it easier to identify where misalignments originate.

---

**Files Created**:
- Script: `/root/scripts/system-coherence-analysis.py`
- Cron: Daily at 05:00 UTC
- Reports: `/root/cron-logs/system-coherence-*.md`

**Key Metrics**:
- TELOS Compliance: 50.0/100
- Issues Found: 16 misalignments, 42 gaps
- Analysis Time: ~5 seconds