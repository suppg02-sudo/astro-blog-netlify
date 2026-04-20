---
pubDatetime: 2026-01-31T14:49:00Z
title: "Advanced AI Instruction Techniques: Beyond Task Lists"
postSlug: "advanced-ai-instruction-techniques"
description: "Exploring 18+ sophisticated AI instruction patterns beyond simple task lists, from gateway validation to Ralph loops and XML prompt engineering."
tags:
  - workflow
  - development
  - openagents
---

When working with AI agents, we often think of "instructions" as simple task lists or todo items. But sophisticated AI systems like OpenCode use **advanced instruction techniques** that go far beyond basic checklists.

## Beyond Task Lists: A Multi-Layered Architecture

After analyzing my OpenCode system, I discovered **18+ different instruction techniques** organized into a sophisticated, multi-layered architecture. Task lists are just one technique among many.

Here's what I found:

{{< mermaid >}}
mindmap
  root((AI Instruction Techniques))
    Validation & Safety
      Gateway Validation
      HITL Checkpoints
      Guardrails
    Structured Prompting
      XML Prompt Engineering
      Priority Systems
      Conditional Workflows
      Role-Based Prompting
    Orchestration & Automation
      Ralph Loops
      Multi-Agent Orchestration
      Stage-Based Workflows
      Task Lists & Checklists
      Agent Templates
      Workflow Tracing
    Knowledge Management
      Context Engineering
      Fabric Patterns
      Tool Protocols
      Evidence-Based Research
{{< /mermaid >}}

## Layer 1: Validation & Safety

### Gateway Validation Pattern

The **Gateway Validation** technique we discussed earlier is part of a larger validation ecosystem. It prevents agents from marking tasks complete without verification.

**Structure:**
```
Gate 1: Operation Classification (Critical?)
    ↓
Gate 2: Pre-Execution Check (Tools available?)
    ↓
Gate 3: Execute Verification (Browser testing)
    ↓
Gate 4: Verify Results (200 OK, content check)
    ↓
Gate 5: Document Verification (Evidence in session)
    ↓
Gate 6: Mark Complete ONLY IF all pass
    ↓ NO → Report failure, await user direction
```

**Use Case**: Critical operations (web deployments, database changes, theme updates)

**Skills Using**: `hugo-with-gates`, `memos`, `transcription`

---

### HITL (Human-in-the-Loop) Checkpoint Framework

This technique standardizes **human decision points** in AI workflows with 5 checkpoint types:

**Checkpoint Types:**
1. **Review Checkpoint** - AI presents analysis, human validates
2. **Approval Checkpoint** - Human approves before execution
3. **Selection Checkpoint** - Choose from AI-generated options
4. **Refinement Checkpoint** - Iterate on feedback
5. **Decision Checkpoint** - Final go/no-go

**Features:**
- Confidence scoring (0-100%)
- Decision options with clear actions
- Pattern learning integration
- Audit trail for accountability

**Use Case**: Complex workflows requiring human oversight

---

### Guardrails & Safety Patterns

Techniques for creating **ethical boundaries** on AI outputs:

- Basic pattern matching via `/api/safety/check`
- Vercel JSON guardrails approach
- Declarative UI protocols
- Ethical OSINT guardrails

**Use Case**: Preventing unsafe/harmful outputs, people research

---

## Layer 2: Structured Prompting

### XML-Based Prompt Engineering

This is perhaps the most sophisticated technique I found. It uses **structured XML tags** for LLM instruction optimization.

**Key XML Elements:**

```xml
<critical_rules priority="absolute" enforcement="strict">
  <rule id="position_sensitivity">
    Critical instructions MUST appear in first 15% of prompt
  </rule>
  <rule id="nesting_limit">
    Maximum nesting depth: 4 levels
  </rule>
  <rule id="instruction_ratio">
    Instructions should be 40-50% of total prompt
  </rule>
</critical_rules>

<context>
  <system_context>AI-powered prompt optimization</system_context>
  <domain_context>LLM prompt engineering</domain_context>
  <task_context>Transform prompts into high-performance agents</task_context>
</context>

<execution_priority>
  <tier level="1" desc="Research-Backed Patterns">
    - Position sensitivity (critical rules in first 15%)
    - Nesting depth reduction (≤4 levels)
    - Instruction ratio optimization (40-50%)
  </tier>
  <tier level="2" desc="Structural Improvements">
    - Component ordering (context→role→task→instructions)
    - Explicit prioritization systems
  </tier>
  <conflict_resolution>Tier 1 always overrides Tier 2/3</conflict_resolution>
</execution_priority>
```

**Benefits:**
- Explicit rule positioning
- Priority-based conflict resolution (3 tiers)
- Conditional logic for adaptive complexity
- Nesting limits for clarity

**Use Case**: Prompt optimization, improving agent instruction quality

---

### Priority-Based Conflict Resolution

**3-tier priority system** for resolving instruction conflicts:

| Tier | Description | When to Override |
|-------|-------------|-----------------|
| **Tier 1** (Absolute) | Critical rules, safety, position sensitivity | Always overrides Tier 2/3 |
| **Tier 2** (Core Workflow) | Structural improvements, execution flow | Overrides Tier 3 |
| **Tier 3** (Enhancement) | Optimization features, optional enhancements | Never overrides |

**Use Case**: Preventing ambiguous or conflicting instructions

---

### Conditional Workflow Instructions

XML `<if>` tags for **task-specific routing**:

```xml
<if condition="simple_prompt">Basic step-by-step w/ validation checkpoints</if>
<if condition="moderate_prompt">Multi-step workflow w/ decision points</if>
<if condition="complex_prompt">Full stage-based workflow w/ routing intelligence</if>
```

**Use Case**: Adaptive instruction complexity based on prompt characteristics

---

### Role-Based Prompting with Expert Personas

`<role>` tags defining expert identity:

```markdown
<role>Expert Prompt Architect applying research-backed optimization patterns</role>
<role>Research Agent with evidence-based methodology</role>
<role>Frontend-UI-UX-Engineer specializing in visual design</role>
```

**Use Case**: Context-aware behavior, specialized knowledge activation

---

## Layer 3: Orchestration & Automation

### Ralph Loop Mining

**Autonomous iterative development** using multi-agent orchestration:

{{< mermaid >}}
flowchart TD
    A[Task Decomposition] --> B[Parallel Execution]
    B --> C[Iterative Refinement]
    C --> D{Completion Detected?}
    D -->|No| C
    D -->|Yes| E[Mark Complete]
    F[Safety Controls]
    C -.-> F
{{< /mermaid >}}

**Process:**
1. Task Decomposition into agent-specific subtasks
2. Parallel Execution (multiple agents simultaneously)
3. Iterative Refinement (agents improve upon each other's work)
4. Completion Detection (automatic)
5. Safety Controls (prevent runaway loops)

**Use Case**: API development, refactoring, feature implementation with validation

---

### Multi-Agent Orchestration Instructions

**Decision matrix** for choosing between systems:

```
START → Need? → Git/Testing/Other
          ↓
         Parallel?  → Yes → Oh My OpenCode (Sisyphus)
                       No  → OpenAgentsControl (openagent)
```

**Use Cases:**
- **Oh My OpenCode**: Parallel execution, custom agents, complex orchestration
- **OpenAgentsControl**: Git operations, code quality, testing

---

### Stage-Based Workflow Definitions

**Explicit workflow stages** with transition rules:

```
Stage 1: Analyze → Stage 2: Discover → Stage 3: Approve → Stage 4: Execute → Stage 5: Validate → Stage 6: Summarize
```

**Features:**
- Mandatory approval before execution
- Context loading before planning
- Validation after execution
- Summary before completion

**Use Case**: Complex processes with clear transitions

---

### Task Lists & Multi-Step Checklists

As you mentioned, this is indeed a technique! Numbered or bulleted step sequences with verification checkpoints.

**Example from agents.md:**
```markdown
1. Search for Relevant Evidence
2. Verify Data and Configurations
3. Compare Claims vs Reality
4. Document Uncertainty
5. Cite Sources
6. Avoid Unverified Assumptions
```

**Use Case**: Complex workflows requiring sequential verification

---

### Agent Template System

**Reusable agent definition templates** with structured sections:

```markdown
---
description: "{one-line purpose}"
mode: primary
tools: {read, write, edit, bash, task, glob, grep}
permissions:
  bash: "rm -rf *": "ask"
---
<role>{Clear role}</role>
<approach>1. Read → 2. Think → 3. Implement → 4. Verify</approach>
<heuristics>- Decompose → Use tools → Stop on errors</heuristics>
<examples>Typical use cases with expected outcomes</examples>
```

**Use Case**: Creating new agents quickly with standardized structure

---

### Workflow Tracing & Transparency Protocol

**Complete visibility** into execution flow when "flow" trigger is used:

**Transparency Elements:**
- Task classification (conversational vs task path)
- Context loading (which files were read)
- Delegation decisions (why specific subagent was chosen)
- Skill/Pattern discovery (which resources were selected)
- Execution steps (tools used, operations performed)
- Issues encountered (errors, conflicts, resolutions)
- Session management (background tasks, cleanup status)

**Output**: Mermaid diagram showing complete request handling pipeline

**Use Case**: Debugging workflows, understanding agent decisions

---

## Layer 4: Knowledge Management

### Context Engineering with Structured Loading

**Domain/Standards/Templates structure**:

{{< mermaid >}}
graph TD
    A[.opencode/context/] --> B[core/]
    B --> C[standards/]
    B --> D[workflows/]
    B --> E[system/]
    B --> F[domain/]
    B --> G[templates/]
    C --> H[code-quality.md]
    C --> I[documentation.md]
    C --> J[test-coverage.md]
    D --> K[code-review.md]
    D --> L[task-delegation.md]
{{< /mermaid >}}

**Directory Structure:**
```
.opencode/context/
├── core/
│   ├── standards/
│   │   ├── code-quality.md
│   │   ├── documentation.md
│   │   └── test-coverage.md
│   └── workflows/
│       ├── code-review.md
│       └── task-delegation.md
├── system/
├── domain/ (project-specific knowledge)
└── templates/ (reusable components)
```

**Use Case**: Ensures agents load correct context before execution

---

### Fabric Pattern Library System

**200+ crowdsourced prompt patterns** managed via REST API:

**Pattern Categories:**
- `extract_` patterns (wisdom, insights, patterns)
- `create_` patterns (hugo_post, summary, essay)
- `analyze_` patterns (claims, prose, risk)
- `improve_` patterns (prompt, writing)

**Execution**: Direct ZAI API calls with pattern variables ({{INPUT}})

**Skill Discovery**: `find_skill` pattern for automatic intent detection

**Use Case**: Content creation, analysis, extraction workflows

---

### Tool Usage Protocols

**Explicit tool usage guidelines** with when/when-not-to-use:

```markdown
<tool name="edit">
  <purpose>Make targeted changes to existing files</purpose>
  <when_to_use>Modifying specific sections</when_to_use>
  <when_not_to_use>Creating new files (use write instead)</when_not_to_use>
</tool>
```

**Use Case**: Prevents misuse of tools, improves execution efficiency

---

### Evidence-Based Research Instructions

**MANDATORY verification steps** before presenting conclusions:

```markdown
1. Search for Relevant Evidence (grep, read, context7)
2. Verify Data and Configurations (check actual files, docker ps)
3. Compare Claims vs Reality (document discrepancies)
4. Document Uncertainty (state when evidence is incomplete)
5. Cite Sources (reference specific files, versions)
6. Avoid Unverified Assumptions (don't claim broken without testing)
```

**Use Case**: System analysis, performance assessments, architecture recommendations

---

## Why This Architecture Works

Your OpenCode system uses a **multi-layered instruction architecture**:

{{< mermaid >}}
flowchart TB
    subgraph Discovery["Discovery & Routing"]
        DS1[Context Scout]
        DS2[Cronflow]
        DS3[@skill_discovery]
        DS4[Skill Metadata]
    end

    subgraph Loading["Context Loading"]
        CL1[Domain/Standards]
        CL2[Workflows]
        CL3[System Config]
    end

    subgraph Specialized["Specialized Knowledge"]
        SK1[Gateway Validation]
        SK2[HITL Checkpoints]
        SK3[Fabric Patterns]
        SK4[Ralph Loops]
        SK5[XML Engineering]
    end

    subgraph Safety["Safety & Guardrails"]
        SF1[Approval Gates]
        SF2[Stop on Failure]
        SF3[Guardrails]
        SF4[Evidence Requirements]
    end

    Discovery --> Loading
    Loading --> Specialized
    Specialized --> Safety

    subgraph Agent["Agent Execution"]
        A1[Load Context]
        A2[Apply Technique]
        A3[Execute Task]
        A4[Validate Output]
    end

    Safety --> Agent
{{< /mermaid >}}

### Layer 1: Discovery & Routing (Automated)
- **ContextScout**: Discovers relevant context files
- **Cronflow**: Analyzes workflows and optimizes them
- **@skill_discovery**: Routes to correct skills/patterns

### Layer 2: Context Loading (Structured)
- **Domain/Standards/Templates**: Clear file structure
- **Navigation guides**: Help agents find files
- **Critical rules**: @critical_context_requirement in workflows

### Layer 3: Specialized Knowledge (Distributed)
- **Gateway Validation**: Critical operation verification
- **HITL Checkpoints**: Human oversight
- **Fabric Patterns**: Crowdsourced prompts
- **Ralph Loops**: Autonomous development

### Layer 4: Safety & Guardrails (Enforced)
- **Approval gates**: @approval_gate for destructive ops
- **Stop on failure**: @stop_on_failure for errors
- **Guardrails**: Pattern matching for ethical boundaries
- **Evidence requirements**: Verification before conclusions

---

## Key Insight: Why Not Everything in Context Files

When I analyzed whether to create a centralized catalog of all 18 techniques, I discovered **why your system doesn't need it**:

### Problem 1: Redundancy
All 18 techniques are **already well-documented** in their natural locations

### Problem 2: Context Pollution
Agents need **domain-specific, actionable guidance**, not a 18-technique taxonomy

### Problem 3: Maintenance Nightmare
Keeping a centralized catalog synced with reality creates unnecessary burden

### Problem 4: Discovery Systems Already Work
Your system already has **excellent discovery mechanisms**:
- ContextScout agent
- Cronflow skill
- @skill_discovery
- Skill metadata

These systems already route agents to the **right technique** when needed.

---

## Practical Examples

### Example 1: Using Gateway Validation

When creating a blog post:

```bash
# Agent loads hugo-with-gates skill
# Skill checks: Blog post creation = Category A (critical)
# Gate 1: PASS ✅ - Operation identified
# Gate 2: PASS ✅ - Hugo server running
# Execute: Create content file
# Gate 3: Execute verification with Agent Browser
# Gate 4: PASS ✅ - Page loads (200 OK)
# Gate 5: PASS ✅ - Results documented
# Gate 6: PASS ✅ - Verification passed
# Mark complete ✅
```

### Example 2: Using XML Prompt Engineering

When optimizing agent instructions:

```bash
# Agent uses prompt-enhancer command
# XML tags enforce:
# - Critical rules in first 15%
# - Nesting depth ≤4 levels
# - Instruction ratio 40-50%
# - 3-tier priority system
# Output: Optimized prompt with compliance score
```

### Example 3: Using Ralph Loops

When developing a complex feature:

```bash
# Agent invokes ralph-loop-mine skill
# Task decomposed into 5 subtasks
# Subtask 1: Database schema (OpenCoder)
# Subtask 2: API endpoints (OpenCodebaseAgent)
# Subtask 3: Frontend (OpenFrontendSpecialist)
# Subtask 4: Tests (TestEngineer)
# All run in parallel
# Agents iterate on each other's work
# Completion detected automatically
# Mark complete ✅
```

### Example 4: Using Fabric Patterns

When creating content:

```bash
# Agent invokes fabric skill
# Intent detection: "Create summary" → fabric:summarize pattern
# Pattern loaded from REST API
# Variables substituted: {{INPUT}} → actual content
# Generated summary returned via ZAI API
```

---

## Summary: Task Lists Are Just One Technique

Task lists and todo items are valuable, but they're **just one technique** among **18+ sophisticated patterns** in your OpenCode system.

Your system uses a **multi-layered, decentralized architecture**:

1. **Discovery Systems** → Route to correct resources
2. **Context Loading** → Ensure domain-specific guidance
3. **Specialized Knowledge** → Apply appropriate technique
4. **Safety Guardrails** → Enforce constraints
5. **Transparency** → Debug and understand decisions

**Key Principle**: Each technique lives in its natural home where it's maintained. When agents need a technique, they discover it via **skill descriptions, file names, or automatic routing**.

This creates a **sustainable, maintainable system** where:
- Techniques are easy to find and use
- No centralized catalog to maintain
- Redundancy is avoided
- Discovery systems work excellently

**Recommendation**: Keep this architecture. It's sophisticated and well-designed.

---

## Quick Reference

| # | Technique | Primary File | Complexity |
|---|-----------|----------------|------------|
| 1 | Gateway Validation | Gateway validation docs | Medium |
| 2 | HITL Checkpoints | HITL framework templates | High |
| 3 | XML Prompt Engineering | Prompt engineering templates | High |
| 4 | Agent Templates | Agent template file | Medium |
| 5 | Priority Systems | Prompt engineering templates | Medium |
| 6 | Conditional Workflows | Prompt engineering templates | Medium |
| 7 | Role-Based Prompting | Skills | Low |
| 8 | Task Lists | agents.md | Low |
| 9 | Stage-Based Workflows | agents.md | Medium |
| 10 | Ralph Loops | ralph-loop-mine skill | High |
| 11 | Fabric Patterns | fabric skill | Medium |
| 12 | Context Engineering | /root/.config/opencode/context/ | High |
| 13 | Workflow Tracing | Flow protocol docs | Medium |
| 14 | Tool Protocols | Agent template | Low |
| 15 | Evidence-Based Research | agents.md | Medium |
| 16 | Multi-Agent Orchestration | WORKFLOW-GUIDE.md | Medium |
| 17 | Checkpoint Scoring | Prompt templates | Medium |
| 18 | Guardrails | Safety patterns | High |

---

**Remember**: The power of your OpenCode system isn't just in these techniques, but in how they're **discovered, routed, and combined** to solve problems. That's true sophistication.