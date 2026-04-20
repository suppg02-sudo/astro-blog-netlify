---
pubDatetime: 2026-02-24T22:30:57Z
title: "Dead Simple Framework for Working with AI Coding Agents"
postSlug: "dead-simple-framework-ai-coding-agents"
description: "Dead Simple Framework for Working with AI Coding Agents"
tags:
  - frameworks
  - productivity
  - coding-agents
  - ai
  - claude-code
---

A practical, straightforward framework for working with AI coding assistants when building new projects from scratch. This approach emphasizes simplicity over complexity, focusing on creating reliable and repeatable workflows.

## The Core Problem

Many developers spend more time creating agentic coding workflows than actually coding. Over-engineered multi-agent frameworks on GitHub are powerful but difficult to customize. What most developers need is something simple that just works—and can evolve over time.

## The Solution: A Dead Simple Framework

This framework consists of two main parts: building your **AI Layer** and executing **PIV Loops** (Plan, Implement, Validate).

## Part 1: The AI Layer

Your AI Layer is all the assets in your codebase created to provide context to your coding agent:

| Component | Purpose |
|-----------|---------|
| **PRD** | What to build - complete scope for MVP |
| **Global Rules** | How to build - constraints and conventions |
| **Commands** | Reusable workflows (/prime, /commit, /plan-feature) |
| **Reference Docs** | On-demand context for specific tasks |

**Key principle**: Start with generic commands, then evolve them for your specific use case as your codebase grows.

## The Four Golden Rules

### 1. Context is Precious

Context is your most valuable resource when working with AI coding assistants. Protect it by:
- Resetting context between planning and implementation phases
- Keeping global rules concise (~230 lines recommended)
- Using progressive disclosure for specialized context

### 2. Commandify Everything

If you do something more than twice, make it a command. This includes:
- `/create-prd` - Generate structured product requirements
- `/create-rules` - Set up global rules
- `/plan-feature` - Create detailed feature plans
- `/execute` - Run implementation from plan
- `/commit` - Standardize commit messages

### 3. Git History is Long-Term Memory

Your commit history serves as the coding agent's memory across sessions:
- Standardize commit messages for consistency
- Use git log in your prime command to understand project history
- This helps the agent understand patterns and recent changes

### 4. System Evolution Mindset

When bugs occur, don't just fix the code—fix the AI layer:
- Add to style guides or rules
- Create new on-demand context
- Add end-to-end tests to commands

**The compound effect**: Your codebase, test base, and AI layer all evolve together.

## Part 2: The PIV Loop

PIV stands for **Plan, Implement, Validate**—the core execution cycle for building features.

### Phase 1: Plan

1. Start with unstructured conversation ("vibe planning")
2. Spin up sub-agents for research
3. **Critical**: Ask the agent to return with questions
4. Create structured plan with:
   - Goal and success criteria
   - Reference documentation
   - Detailed task list
   - Validation strategy (defined BEFORE coding)

### Phase 2: Implement

- **Context Reset**: Start fresh with only the structured plan
- Delegate all coding to the agent
- Pre-set environment variables (critical!)
- Agent handles: code, migrations, server startup, testing

### Phase 3: Validate

The validation pyramid:
- Type checking and linting
- Unit testing
- Integration testing
- End-to-end testing with browser automation

Always do human validation: code review + manual testing. Trust but verify.

## The Power of Questions

**Your #1 goal in planning is to reduce assumptions.**

> One line of bad code = one line of bad code.  
> One line of bad plan = 100 lines of bad code.  
> One line of bad PRD = 1000 lines of bad code.

**Solution**: Have the agent ask you a flurry of questions. Use multiple choice for speed, type your own answers when you need to clarify.

## Sub-Agents: When to Use Them

| Use For | Don't Use For |
|---------|---------------|
| Research | Implementation |
| Codebase exploration | Writing code |
| Web research | File editing |

**Reason**: Sub-agents load massive context for exploration, but you only need their summary. Implementation needs full context of files being edited.

## Practical Tips

### Environment Variables

Set up environment variables BEFORE implementation:
- Create `.env.example` for reference
- Set actual values before agent starts
- Prevents mock testing instead of real validation

### The Prime Command

Run `/prime` at the start of every session:
1. Read documentation (PRD, rules)
2. Explore codebase structure
3. Check git history
4. Identify current state and next phase
5. Output understanding for validation

### Regression Testing

As you build more features, ensure old features don't break:
- Create commands that replay end-to-end tests
- Use tools like QA.tech for AI-powered test evolution
- Tests should grow alongside your codebase

## The Workflow Diagram

```
Initial Planning → PIV Loop → System Evolution
      │               │              │
      ▼               ▼              ▼
  Brain dump      Plan          Fix AI layer
  Questions       Implement     Add tests
  Create PRD      Validate      Update docs
  Create Rules    Commit            │
                      │             │
                      └─────────────┘
                            │
                      Next PIV Loop
```

## Key Takeaways

1. **Start simple** - Avoid over-engineered multi-agent frameworks
2. **Make it your own** - Customize and evolve the framework
3. **Context is precious** - Protect it, reset between phases
4. **Commandify everything** - Make repeatable processes explicit
5. **Reduce assumptions** - Have agent ask questions, answer thoroughly
6. **Trust but verify** - Human validation is always required
7. **Evolve continuously** - Fix the system, not just the code

## Conclusion

The power of this framework compounds over time. As you build your codebase, you simultaneously evolve your test base and AI layer. Each PIV loop becomes faster and more reliable because of the work you put into planning.

This framework works with any AI coding assistant—Claude Code, Cursor, Windsurf, or others. The principles are universal.

---

*Source: [Dead Simple Framework for Working with Coding Agents](https://youtu.be/goOZSXmrYQ4) by Cole Medin*