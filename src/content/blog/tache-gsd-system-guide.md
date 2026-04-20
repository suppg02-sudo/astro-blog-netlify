---
pubDatetime: 2026-02-13T10:00:00Z
title: "Tache GSD: The Ultimate Get-Shit-Done Meta Prompt System"
postSlug: "tache-gsd-system-guide"
description: "Tache GSD: The Ultimate Get-Shit-Done Meta Prompt System"
tags:
  - productivity
  - tache
  - gsd
  - meta-prompts
  - claude-code
---

## Overview

**Tache GSD** (Get-Shit-Done) is a brilliant meta-prompt system created by @glittercowboy that transforms Claude Code into a productivity powerhouse. GSD is a collection of organized, tested prompts designed to help you accomplish complex tasks through structured workflows.

## What is Tache GSD?

Tache GSD is not a tool—it's a **system of system prompts**. Each prompt is carefully crafted to:

- Define a specific role or context
- Establish clear workflows
- Use Claude Code's built-in tools effectively
- Guide the AI through structured problem-solving

The genius is in the **meta-level thinking**: Instead of writing prompts for specific tasks, Tache creates prompts that generate prompts, which then solve your actual problems.

## The Philosophy Behind GSD

The core idea: **Most productivity problems aren't technical—they're organizational.**

GSD provides organization through:

1. **Role-based prompts** - "You are a project manager"
2. **Workflow prompts** - "Follow this 5-step process"
3. **Tool-integrated prompts** - "Use the question tool to gather information"
4. **Meta-prompts** - "Create a prompt that solves X"

## Key Components of GSD

### 1. The Meta-Prompt Framework

A meta-prompt is a prompt that creates prompts. Example:

```
"Create a prompt for a {role} that helps users {goal}.
The prompt should:
- Ask clarifying questions
- Break the task into steps
- Provide concrete examples
- Use the question tool for user input"
```

Running this generates a ready-to-use prompt for that specific role.

### 2. Role-Based Organization

GSD organizes prompts by role:

- **Project Manager** - Planning, scope definition, timeline management
- **Technical Lead** - Architecture decisions, code review guidance
- **Writer** - Content planning, editing, style consistency
- **Designer** - Layout, color, typography decisions
- **Developer** - Code generation, debugging, optimization
- **Life Coach** - Goal setting, decision making, accountability
- **Business Analyst** - Requirements gathering, stakeholder management

Each role has specific prompts tailored to that function.

### 3. Workflow Integration

GSD prompts leverage Claude Code's tools:

- **Question tool** - Gather user input interactively
- **File operations** - Read, write, edit files
- **Execution** - Run commands and scripts
- **Iterative refinement** - Multiple rounds of improvement

## How to Use Tache GSD

### Step 1: Find the Right Prompt

Browse the Tache repository to find a prompt matching your need. Categories include:

- Project Management
- Software Development
- Content Creation
- Decision Making
- Learning & Development
- Problem Solving

### Step 2: Copy the Prompt

```bash
# Clone the Tache GSD repository
git clone https://github.com/glittercowboy/get-shit-done.git
cd get-shit-done

# Find your prompt
ls -la prompts/
```

### Step 3: Use in Claude Code

Paste the prompt into Claude Code:

```bash
claude < prompts/project-manager.md
```

Or with a custom query:

```bash
claude --system-prompt "$(cat prompts/project-manager.md)" \
  "Help me plan my Q1 roadmap"
```

### Step 4: Interact with the Workflow

Most GSD prompts will:

1. **Ask clarifying questions** using the question tool
2. **Gather information** about your specific situation
3. **Create a plan** tailored to your answers
4. **Generate artifacts** (documents, specs, checklists)
5. **Iterate** based on your feedback

## Real-World GSD Workflows

### Workflow 1: Project Planning

```
Start: "I need to plan a new feature"
  ↓
GSD asks: "What's the feature? Who are users? What's the timeline?"
  ↓
Creates: Feature specification, task breakdown, timeline, resource plan
  ↓
Output: Detailed project plan ready for execution
```

### Workflow 2: Content Strategy

```
Start: "I need to create a blog strategy"
  ↓
GSD asks: "Target audience? Topics? Frequency? Formats?"
  ↓
Creates: Content calendar, post outlines, SEO strategy, distribution plan
  ↓
Output: 12-month content roadmap with specific posts
```

### Workflow 3: Decision Making

```
Start: "Should we switch to a new tech stack?"
  ↓
GSD asks: "Current pain points? Requirements? Constraints? Team skills?"
  ↓
Creates: Pro/con analysis, risk assessment, migration plan
  ↓
Output: Decision framework with recommendation
```

### Workflow 4: Code Review Guidance

```
Start: "Review this pull request"
  ↓
GSD asks: "What's the change? What concerns do you have?"
  ↓
Creates: Detailed review with suggestions, security checks, performance notes
  ↓
Output: Comprehensive review with actionable feedback
```

## Benefits of Using GSD

### 1. Consistency

Every project uses the same proven workflow structure.

### 2. Completeness

You won't forget important steps because the prompt guides you through them.

### 3. Quality

Prompts are battle-tested by the community and continuously refined.

### 4. Speed

You don't write prompts—you just answer questions and get results.

### 5. Scalability

Same prompt works for 1 task or 100 tasks. Just change the inputs.

### 6. Collaboration

Share prompts with your team. Everyone uses the same workflow.

## Adapting GSD for OpenCode

Since OpenCode has the `question` tool instead of Claude Code's `AskUserQuestion`, small adaptations are needed:

### Change 1: Tool Name

**Claude Code**:
```json
{ "tool": "AskUserQuestion" }
```

**OpenCode**:
```json
{ "tool": "question" }
```

### Change 2: Option Format

Both are similar, but ensure header length is under 30 characters for OpenCode.

### Change 3: Multi-Question Support

Both support multiple questions, but syntax differs slightly:

**Claude Code**:
```
Ask multiple questions in sequence
```

**OpenCode**:
```json
{
  "questions": [
    { "question": "Q1", "header": "Q1", "options": [...] },
    { "question": "Q2", "header": "Q2", "options": [...] }
  ]
}
```

## Creating Custom GSD Prompts

You can create your own GSD-style prompts:

### Template: Role-Based GSD Prompt

```
You are a {role}.
Your goal is to help users {accomplish what}.

You operate in phases:

**Phase 1: Understand**
Use the question tool to ask about:
- Current situation
- Goals
- Constraints
- Success criteria

**Phase 2: Plan**
Based on answers, create a detailed plan with:
- Step-by-step tasks
- Timeline
- Resources needed
- Potential risks

**Phase 3: Execute**
Guide the user through execution:
- Check progress
- Adjust as needed
- Remove blockers

**Phase 4: Review**
Assess outcomes:
- What worked?
- What didn't?
- Lessons learned?

After each phase, use the question tool to get feedback before moving to the next phase.
```

### Template: Workflow-Based GSD Prompt

```
Help users through a {workflow name} using this 5-step process:

1. **Discovery** - Use questions to understand the problem
2. **Analysis** - Break down the problem into components
3. **Planning** - Create a solution blueprint
4. **Implementation** - Guide execution step-by-step
5. **Validation** - Verify the solution works

At each step, present options, gather input, and adapt the process based on responses.
```

## Advanced GSD Techniques

### 1. Chaining Prompts

Use one GSD prompt to generate another:

```
Meta-prompt: "Create a GSD prompt for a {role}"
  ↓
Output: New GSD prompt
  ↓
Use new prompt: For the actual task
```

### 2. Custom Personas

Combine GSD with custom system prompts:

```bash
claude \
  --system-prompt "$(cat gsd-base.md) + You work for a startup" \
  "Plan our product launch"
```

### 3. Interactive Refinement

GSD prompts support multiple iterations:

```
Round 1: Get initial plan
Round 2: Refine based on constraints
Round 3: Add detail and timelines
Round 4: Finalize and validate
```

## Community & Resources

### Official Repository

**Tache GSD**: https://github.com/glittercowboy/get-shit-done

Contains:
- 50+ ready-to-use prompts
- Meta-prompt templates
- Workflow examples
- Community contributions

### Variations

Community members have created variations:

- **GSD for Startups** - Business-focused versions
- **GSD for Developers** - Code-specific workflows
- **GSD for Managers** - Team management prompts
- **GSD for Writers** - Content creation workflows

## Tips for Success with GSD

### 1. Start Simple

Begin with basic prompts before customizing.

### 2. Iterate

GSD prompts work best with feedback loops. Answer questions, get output, refine.

### 3. Document Results

Save successful prompts and workflows. Build your personal GSD library.

### 4. Share with Teams

GSD's power multiplies when teams use the same prompts.

### 5. Adapt, Don't Copy

Customize prompts for your specific context rather than using them verbatim.

### 6. Measure Outcomes

Track what works. GSD is most valuable when results are measurable.

## Limitations & When Not to Use GSD

### When GSD Works Best

✅ Structured problems with clear steps
✅ Recurring tasks that benefit from consistency
✅ Projects needing multiple stakeholder input
✅ Decisions requiring systematic analysis
✅ Complex workflows that need documentation

### When GSD May Not Be Ideal

❌ Highly creative work (poetry, art, music)
❌ Real-time problem-solving under extreme time pressure
❌ Tasks requiring deep domain expertise beyond the prompt
❌ One-off problems that won't repeat
❌ Problems best solved through exploration rather than structure

## The Future of GSD

GSD represents a shift in how we work with AI:

- **From prompts to systems** - Moving beyond single prompts to integrated workflows
- **From individual to team** - Sharing proven workflows across organizations
- **From generic to specific** - Customizing for context and constraints
- **From single-turn to iterative** - Multiple rounds of refinement and feedback

As AI agents become more capable, GSD-style systems will become the norm.

## Conclusion

**Tache GSD** is more than a prompt collection—it's a **productivity methodology** that leverages Claude Code's capabilities to help you accomplish complex tasks through structured workflows.

Whether you use GSD for project management, content creation, decision-making, or software development, the core value is the same: **Proven workflows that work.**

Start with an existing prompt, experience the workflow, then customize for your specific needs. The real power of GSD is in the systematic approach to problem-solving it embodies.

---

**Resources**:
- **GitHub**: https://github.com/glittercowboy/get-shit-done
- **Creator**: @glittercowboy
- **License**: MIT (share and modify freely)
- **Community**: Discussion and variations welcome

**Next Steps**:
1. Clone the repository
2. Pick a prompt that matches your next task
3. Run it in Claude Code
4. Experience the workflow
5. Customize for your needs
6. Share your improvements with the community