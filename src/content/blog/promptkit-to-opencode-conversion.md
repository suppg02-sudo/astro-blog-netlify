---
pubDatetime: 2026-02-20T12:00:00Z
title: "PromptKit to OpenCode: Converting 42 Prompts to 5 Skills"
postSlug: "promptkit-to-opencode-conversion"
description: "PromptKit to OpenCode: Converting 42 Prompts to 5 Skills"
tags:
  - skills
  - opencode
  - triggers
  - conversion
  - promptkit
---

# PromptKit to OpenCode: Converting 42 Prompts to 5 Skills

Recently converted all 42 PromptKit prompts into 5 OpenCode skills with global triggers, making advanced prompt engineering techniques instantly accessible.

## What is PromptKit?

PromptKit is a portable prompt library for AI-assisted software development, featuring 42 organized prompts based on 2025 prompt engineering research. It includes core techniques like Chain of Thought (4x improvement on GSM8K benchmarks), advanced methods like Chain-of-Table (8-9% benchmark improvement), and complete agile development workflows.

## The Challenge

While PromptKit provided excellent prompt templates, they were:
- Scattered across multiple markdown files
- Not integrated with OpenCode tools
- No automatic loading mechanism
- Required manual browsing and copying

## The Solution

Created 5 OpenCode skills with hybrid integration:
- **promptkit-foundations** (5 prompts) - Core prompt engineering
- **promptkit-advanced** (5 prompts) - Research-backed reasoning
- **promptkit-agile** (21 prompts) - Agile development & modernization
- **promptkit-claude** (8 prompts) - Permissions & templates
- **promptkit-workflows** (2 prompts) - Development lifecycles

## Global Triggers

Added 20+ trigger words to `/media/docs/instructions/global-instructions.md`:

```bash
cot debug this function              # Load promptkit-foundations
cotable analyze sales.csv           # Load promptkit-advanced
tot Should we use microservices?    # Load promptkit-advanced
sprint plan this backlog           # Load promptkit-agile
refactor this function              # Load promptkit-agile
autonomous implement feature         # Load promptkit-claude
tdd Implement auth endpoint        # Load promptkit-workflows
workflow Execute 5-phase          # Load promptkit-workflows
```

## What Each Skill Provides

### promptkit-foundations

Core prompt engineering techniques:
- **Chain of Thought** - Step-by-step reasoning for complex problems
- **Few-Shot Examples** - Learning from examples for consistent output
- **Output Prefilling** - Structured output control for APIs and JSON
- **Role Prompting** - Adopting expert personas for specialized tasks
- **XML Structured** - Using XML tags for multi-part requests

**Best for**: Debugging, analysis, mathematical problems, logic puzzles

### promptkit-advanced

Research-backed techniques from 2025:
- **Chain of Table** - SQL-like operations for tabular data analysis
  - Operations: SELECT, FILTER, GROUP BY, SORT, DERIVE, JOIN
  - 8-9% benchmark improvement on table tasks
- **Tree of Thought** - Exploring multiple reasoning paths
  - Generate 3+ solution paths independently
  - Compare and select best approach
- **Self-Consistency** - Multiple sampling for verification
  - Generate 3-5 independent solutions
  - 10-20% improvement on reasoning tasks
- **Meta-Prompting** - Prompt engineering for prompts
- **Prompt Chaining** - Multi-step prompt sequences

**Best for**: Tabular data, decision-making, critical tasks

### promptkit-agile

Complete agile development toolkit (21 prompts):

**Sprint Management**:
- Sprint Planning - Capacity calculation and scope recommendation
- Backlog Grooming - Prioritization and refinement
- Velocity Estimation - Story point forecasting
- Retrospective Facilitator - Sprint feedback gathering

**Requirements & Planning**:
- User Story Generator - Structured stories with acceptance criteria
- Acceptance Criteria Generator - Testable Given-When-Then scenarios
- Definition of Done - DoD criteria for teams
- Stakeholder Updates - Status reports

**Architecture & Design**:
- Architecture Decision Records (ADR) - Documenting decisions
- Dependency Analysis - Identifying dependencies and impact
- Integration Planning - System integrations and API boundaries

**Legacy Modernization**:
- Legacy Code Analysis - Understanding old codebases
- Code Migration Plans - Migration strategies
- Modernization Roadmaps - Phased modernization
- API Documentation - Auto-generating docs from legacy code

**Code Quality**:
- Technical Debt Triage - Managing and prioritizing debt
- Refactoring Strategy - Safe refactoring with patterns
- Test Generation - Testing untested legacy code

**Change Management**:
- Change Management Plans - Managing code changes
- Risk Assessment - Identifying and mitigating risks
- Knowledge Transfer - Handoffs and onboarding

**Best for**: Project management, legacy modernization, team workflows

### promptkit-claude

Claude Code permissions and project templates (8 prompts):

**5 Spaceballs-themed Permission Modes**:
| Mode | Name | Trigger | Description |
|------|------|----------|-------------|
| 1 | Light Speed | `/safe` | Read-only, maximum safety |
| 2 | Ridiculous | `/normal` | Standard dev work |
| 3 | Autonomous | `/autonomous` | Full dev access |
| 4 | YOLO | `/yolo` | Almost everything |
| 5 | Ludicrous | `/ludicrous` | No restrictions |

**Project Templates**:
- CLAUDE.md Project Template - Project setup
- Django Project Template - Django configuration
- Full Autonomous Mode - Maximum automation workflows

**Best for**: Agent autonomy control, project setup

### promptkit-workflows

Complete software development lifecycles (2 prompts):

**23-Step TDD Cycle**:
- Phase 1: Planning & Questions (Steps 1-6)
- Phase 2: Test-Driven Development (Steps 7-10)
- Phase 3: Code Quality & Documentation (Steps 11-14)
- Phase 4: Git Workflow (Steps 15-18)
- Phase 5: Review & Iteration (Steps 19-23)

**5-Phase Development Workflow**:
- Phase 1: SPEC (Planning & Requirements)
  - Client Approval Gate #1
- Phase 2: BUILD (Implementation)
  - Internal Quality Gate
- Phase 3: VALIDATION (Pre-Commit Quality Gate)
  - All checks must pass
- Phase 4: ACCEPTANCE TEST (Client Validation)
  - Client Approval Gate #2
- Phase 5: SHIP (Deployment)
  - Epoch Complete

**Best for**: Feature implementation, complete projects with client approval gates

## Usage Examples

### Foundation Techniques

```bash
cot debug this function
→ Loads promptkit-foundations
→ Applies Chain of Thought reasoning
→ Step-by-step: Given info → Identify problem → Break down → Solve → Verify
```

### Advanced Reasoning

```bash
cotable analyze /data/sales.csv
→ Loads promptkit-advanced
→ Applies SQL-like operations
→ SELECT → GROUP BY → DERIVE margin → SORT → Answer

tot Should we use monolith or microservices?
→ Loads promptkit-advanced
→ Explores 3 paths: Monolith, Microservices, Modular Monolith
→ Compares and recommends best approach
```

### Agile Workflows

```bash
sprint plan this backlog
→ Loads promptkit-agile
→ Calculates team capacity
→ Recommends sprint scope (70-85% of capacity)
→ Generates sprint plan table
→ Assesses risks and dependencies

refactor this function, it's too long
→ Loads promptkit-agile
→ Identifies code smells
→ Creates safe refactoring sequence
→ Shows before/after code
→ Adds verification checkpoints
```

### Permissions

```bash
safe Analyze this codebase
→ Loads promptkit-claude, Mode 1
→ Read-only operations only
→ No writing, no executing commands

autonomous Implement this feature
→ Loads promptkit-claude, Mode 3
→ Full development access
→ Execute build/test/lint commands
→ Commit locally
→ Ask before pushing to main
```

## Benefits

✅ **All 42 prompts accessible** via 5 well-organized skills

✅ **Global triggers** for instant access (20+ trigger words)

✅ **Hybrid integration** - PromptKit content preserved, OpenCode tools utilized

✅ **Reference maintained** - Original prompts still available at `/root/.opencode/skill/promptkit/prompts/`

✅ **Modular design** - Easy to update individual skills

✅ **Research-backed** - Includes 2025 advanced techniques (CoT-Table: 8-9% improvement)

✅ **Real examples** - Practical workflows with OpenCode tool usage

✅ **Permission control** - 5 Spaceballs-themed permission levels

✅ **Complete workflows** - 23-step TDD + 5-phase SDLC

## File Structure

```
/root/.opencode/skill/
├── promptkit/                          # Original promptkit library
│   ├── SKILL.md                        # Updated with skills summary
│   ├── README.md                        # Conversion documentation
│   ├── list.sh                          # List all 42 prompts
│   └── prompts/                         # 42 original prompts
│       ├── foundations/                   # 5 core techniques
│       ├── advanced/                      # 5 research-backed
│       ├── agile-legacy/                  # 21 agile workflows
│       ├── claude-code/                   # 8 permissions + templates
│       └── workflows/                     # 2 development cycles
├── promptkit-foundations/               # NEW: Core techniques
│   └── SKILL.md
├── promptkit-advanced/                  # NEW: Advanced reasoning
│   └── SKILL.md
├── promptkit-agile/                     # NEW: Agile workflows
│   └── SKILL.md
├── promptkit-claude/                    # NEW: Permissions
│   └── SKILL.md
└── promptkit-workflows/                  # NEW: Development cycles
    └── SKILL.md

/media/docs/instructions/
└── global-instructions.md               # UPDATED: Added PromptKit triggers
```

## Commands Reference

```bash
# List all PromptKit prompts
/root/.opencode/skill/promptkit/list.sh

# Use via triggers (automatic)
cot debug this function              # Load promptkit-foundations
cotable analyze sales.csv           # Load promptkit-advanced
tot Should we use microservices?    # Load promptkit-advanced
sprint plan this backlog           # Load promptkit-agile
refactor this function              # Load promptkit-agile
autonomous implement feature         # Load promptkit-claude
tdd Implement auth endpoint        # Load promptkit-workflows
workflow Execute 5-phase          # Load promptkit-workflows
```

## Research References

The conversion preserved all research-backed techniques from PromptKit:

- **Wei et al. (2022)** - Chain of Thought prompting (4x improvement on GSM8K)
- **Wang et al. (2024)** - Chain-of-Table (8-9% benchmark improvement)
- **Yao et al. (2023)** - Tree of Thought reasoning
- **Wang et al. (2022)** - Self-Consistency (10-20% improvement)
- **Zhou et al. (2022)** - Least-to-Most prompting (related to chaining)
- **Anthropic Best Practices** - Official prompt engineering guidance

## Next Steps

Optional enhancements being considered:

1. **Create trigger workflow script** - Automate skill loading based on triggers
2. **Add prompt validation** - Verify prompt format before use
3. **Create conversion tool** - Automate promptkit → OpenCode skill conversion
4. **Add usage analytics** - Track which prompts are most used
5. **Create interactive CLI** - Browse and use prompts via command line

## Conclusion

The PromptKit to OpenCode conversion successfully integrates 42 research-backed prompts into the OpenCode ecosystem through 5 well-organized skills with global triggers. All prompt engineering techniques are now instantly accessible via simple trigger words, preserving the original content while providing OpenCode tool integration and practical workflow examples.

**Status**: ✅ Complete
**Total Time**: ~30 minutes
**Skills Created**: 5
**Prompts Integrated**: 42