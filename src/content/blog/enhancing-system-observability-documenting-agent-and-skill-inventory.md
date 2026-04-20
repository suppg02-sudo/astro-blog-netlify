---
pubDatetime: 2026-01-24T21:49:17Z
title: "Enhancing System Observability: Documenting Agent & Skill Inventory"
postSlug: "enhancing-system-observability-documenting-agent-and-skill-inventory"
description: "Enhancing System Observability: Documenting Agent & Skill Inventory"
tags:
  - Local Models
  - Observability
  - Documentation
  - Second Brain
  - TELOS
---

## Executive Summary

Today's work focused on improving observability and documentation of the OpenCode ecosystem by creating a comprehensive **Agent & Skill Inventory** in the central configuration file. This enhancement directly advances multiple TELOS constitution principles, particularly documentation, second-brain architecture, and local model instruction design.

## What Was Accomplished

Updated `/root/.config/opencode/agents.md` with a new **Agent & Skill Inventory** section that documents:

### Primary Agents (7)
- **Sisyphus** (GLM-4.7) - Orchestration and multi-agent coordination
- **Oracle** (GLM-4.7) - Architecture, debugging, and complex reasoning
- **Librarian** (GLM-4.7 Flash) - External research and documentation
- **Explore** (GLM-4.7 Flash) - Codebase exploration and pattern discovery
- **Frontend-UI-UX-Engineer** (GLM-4.7) - Frontend development and design
- **Document-Writer** (GLM-4.7 Flash) - Documentation and content generation
- **Multimodal-Looker** (GLM-4.7) - Image/document analysis

### Specialist Agents (3)
- **Hugo Specialist** - Static site management
- **Mobile App Research** - iOS/Android app discovery
- **GitHub Researcher** - Repository health analysis

### Core Skills (17)
Documented key skills including: agent-browser, databases, fabric, transcription, maintenance, todo, memos, openmemory, hugo, dokploy, portainer, activepieces, wordpress-management, affine, filebrowser, homarr, kavita, and crawl4ai.

### Integration Points
- Added reference to full skill list via `skills` trigger word
- Confirmed sub-agent delegation availability across all documented agents

## TELOS Constitution Alignment

### 1. Documentation and Observability ✅

**TELOS Principle** (Lines 232-294): "It's All About Logging Enough for Reviews"

The inventory creates a **comprehensive audit trail** of available capabilities:
- **Before Today**: Agent and skill capabilities were scattered across configuration files and documentation
- **After Today**: Centralized, searchable reference for all agents, their models, and purposes
- **Benefit**: Enables systematic review of what's available, what's redundant, and what's missing

**Impact**: The inventory supports the CAPTURE → MEASURE → ANALYSE → IMPROVE loop by making the system's toolset visible and reviewable.

---

### 2. Second Brain Architecture - Surface Layer ✅

**TELOS Principle** (Lines 59-70): The **Surface** layer retrieves relevant knowledge

The inventory directly enhances the **Surface** component by:
- Making capabilities searchable and discoverable
- Providing clear reference for which agent handles which task type
- Enabling precise routing of tasks to appropriate specialists

**System Impact**:
```
Before: Ambiguous task routing → trial-and-error delegation
After:  "Orchestration needed?" → Sisyphus
        "Research required?" → Librarian
        "UI design?" → Frontend-UI-UX-Engineer
```

This reduces cognitive load by making the correct tool obvious through documentation.

---

### 3. Local Model Instruction Design ✅

**TELOS Principle** (Lines 161-229): "Create instructions so clear and deterministic that smaller open-source models can execute tasks correctly"

The inventory advances local model capability through:

**Explicit Tool Usage Documentation** (TELOS Design Principle #1):
- Clear mapping: Agent → Model → Purpose
- No ambiguity about which tool to use for which task
- Reduces local model reasoning overhead by pre-defining capabilities

**Context Bundling** (TELOS Design Principle #6):
- All necessary agent/skill context in one location
- Minimizes external dependencies on model intuition
- Makes instructions self-contained

**Concrete Example**:
```
Task: "Research GitHub repository health"
Before (implicit): Model must discover GitHub Researcher exists, infer its purpose
After (explicit): Documented as specialist agent for "repository health analysis, code quality assessment"
→ Local model can confidently delegate without searching/scanning
```

This directly supports TELOS's migration path: refined instructions enable smaller models (z.ai 4.7 Flash) to execute tasks correctly with proper tool usage.

---

### 4. Deterministic Workflows ✅

**TELOS Principle** (Lines 36-40): "Prefer deterministic workflows where outcomes are predictable"

The inventory enables **deterministic task routing**:

| Task Type | Explicitly Routed To | Model | Outcome |
|-----------|---------------------|-------|---------|
| Multi-agent coordination | Sisyphus | GLM-4.7 | Predictable orchestration |
| External research | Librarian | GLM-4.7 Flash | Consistent results |
| Codebase exploration | Explore | GLM-4.7 Flash | Reliable pattern discovery |
| Frontend design | Frontend-UI-UX-Engineer | GLM-4.7 | Deterministic output quality |

**Why This Matters**:
- Removes ambiguity in task delegation
- Makes agent selection a lookup operation, not a reasoning task
- Enables auditing: "Which agent handled this task?" is now answerable

---

### 5. Self-Improvement Foundation ✅

**TELOS Principle** (Lines 288-294): "Continuous improvement" and "Document what you learn"

The inventory creates a baseline for measuring improvement:

**Current State** (Now Documented):
- 7 primary agents with assigned models
- 3 specialist agents for niche domains
- 17 core skills covering major operational domains
- Clear model assignments (GLM-4.7 vs. GLM-4.7 Flash)

**Future Analysis Enabled**:
- Track which agents are most frequently used
- Identify underutilized capabilities (skill gap analysis)
- Validate local model success rates by agent type
- Spot redundancies or missing capabilities

**Example Improvement Loop**:
```
1. MEASURE: Librarian (GLM-4.7 Flash) handling 80% of research tasks → 95% success rate
2. ANALYZE: Oracle rarely needed for pure research → suggests good specialization
3. IMPROVE: Consider migrating more tasks to Librarian if patterns hold
4. REPEAT: Quarterly review of agent utilization metrics
```

---

## Technical Implementation Details

### File Changes
- **Modified**: `/root/.config/opencode/agents.md`
- **Added**: Lines 7-59 (Agent & Skill Inventory section)
- **Structure**: Tables for agents, bullet lists for skills, trigger word integration

### Integration Points
- `skills` trigger word now references complete skill list
- Sub-agent delegation confirmed across all 10 agents
- Agent model assignments documented for capacity planning

### No Breaking Changes
- Existing workflows unaffected
- Documentation-only enhancement
- Backward compatible with current configuration

---

## Effort Estimate
**Quick** (<1 hour): Documentation update with no code changes

---

## Bottom Line

Today's enhancement of documenting the Agent & Skill Inventory advances the TELOS constitution by:
1. **Increasing observability** through centralized capability documentation
2. **Strengthening the Surface layer** of second-brain architecture
3. **Supporting local model instruction design** through explicit tool mapping
4. **Enabling deterministic workflows** by removing ambiguity in agent selection
5. **Creating a baseline for self-improvement** through measurable capabilities

This small documentation investment yields outsized returns in system clarity, enabling the ecosystem to move toward the TELOS goal: *"Instructions so clear and deterministic that smaller open-source models can execute tasks correctly with proper tool usage."*

---

*Published: 2026-01-24*
*Tags: TELOS, Documentation, Observability, Second Brain, Local Models*