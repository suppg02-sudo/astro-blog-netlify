---
pubDatetime: 2026-02-13T09:30:00Z
title: "Create Interactive AI Tools with OpenCode Question Tool"
postSlug: "create-interactive-ai-tools-opencode"
description: "Create Interactive AI Tools with OpenCode Question Tool"
tags:
  - opencode
  - interactive-tools
  - system-prompts
  - tutorial
---

## Overview

One of the most powerful yet underutilized capabilities of OpenCode is its ability to transform the **question tool** into completely different interactive experiences through **custom system prompts**.

This insight comes from an Egghead.io tutorial that demonstrates how a simple tool can become a "life coach," a "project planner," or any other specialized interface you can imagine—without modifying the tool itself.

## The Core Insight

> "You can't build your own version of this tool, but you can completely transform its behavior with a custom system prompt."

This is the key to unlocking OpenCode's interactive potential. The question tool is **foundation, not feature**. Its power comes from how you direct the agent to use it.

## Transformation Workflow

### Step 1: Understand the Tool

First, review the question tool definition to understand what it can do:

- Present multiple-choice options
- Accept custom text input (default)
- Support multi-select mode
- Handle multiple questions in sequence
- Provide confirmation screens

### Step 2: Default Behavior (Coding Assistant)

By default, OpenCode operates as a coding assistant. If you ask it to use the question tool, it presents coding-related choices:

```
User: "Use the question tool"
Agent: "What framework would you prefer?"
  → [React, Vue, Svelte]
```

### Step 3: Apply Custom System Prompt

Transform the agent's behavior completely with a new persona:

```bash
opencode \
  --system-prompt "You're a life coach" \
  "I'm stuck. Help me figure out what to do next in life using only the question tool"
```

### Step 4: Force Tool-Only Mode

Instruct the agent to **only** use the question tool to fulfill its role. This forces the agent to express its entire interaction through structured questions.

### Step 5: Engage with Multi-Step Questionnaire

The transformed agent now guides you through an interactive workflow designed around your new persona:

**Default (Coding Assistant)** → Asks about frameworks, libraries, APIs
**Transformed (Life Coach)** → Asks about goals, obstacles, priorities

## Practical Example: Life Coach Transformation

### The Command

```bash
claude \
  --system-prompt "You're a life coach" \
  --model haiku "I'm stuck. Please help me figure out what to do next in life using only the AskUserQuestion tool"
```

### The Resulting Workflow

The agent transforms into an interactive life coach:

**Question 1: What area of life?**
- [ ] Career
- [ ] Health  
- [ ] Relationships
- [ ] Personal growth
- [ ] Other

**Question 2: How long have you felt stuck?**
- [ ] Days
- [ ] Weeks
- [ ] Months
- [ ] Years
- [ ] Other

**Question 3: What's your primary goal?**
- [ ] Make a specific decision
- [ ] Get unstuck and move forward
- [ ] Plan next steps
- [ ] Understand root cause
- [ ] Other

**Question 4: What's your biggest constraint?**
- [ ] Time
- [ ] Money
- [ ] Knowledge/skills
- [ ] Emotional/mental
- [ ] Practical/logistical
- [ ] Other

The agent continues presenting questions until it has gathered enough information to provide guidance.

## Key Benefits of This Approach

### 1. Create Guided Experiences

Walk users through a structured process step-by-step:

```
Setup Wizard
  ↓ Choose project type
  ↓ Select features
  ↓ Configure options
  ↓ Review choices
  ✓ Generate project
```

### 2. Clarify Ambiguity

Instead of guessing, the agent asks for more information:

```
User: "I want to build an app"
Agent: "Tell me more!"
  → [Web app, Mobile app, Desktop app]
```

### 3. Gather User Preferences

Design adaptive workflows that change based on responses:

```
Q1: Choose category
  ↓
Q2: Features change based on category
  ↓
Q3: Advanced options appear only if needed
```

### 4. Build Beyond Code

The question tool isn't limited to programming:

- **Life Coaching**: Goal setting and decision making
- **Project Planning**: Scope definition and timeline setting
- **Product Research**: User feedback collection
- **Educational**: Guided learning paths
- **Decision Support**: Help choosing between options
- **Onboarding**: New user setup workflows

## System Prompt Patterns

### Pattern 1: Role-Based Persona

```
You're a {role}. Your job is to {goal}.
Use ONLY the question tool to {task}.
Ask questions until you understand {criteria}.
Then provide {output}.
```

**Examples**:
- "You're a startup advisor. Use only the question tool to help users validate their business ideas."
- "You're a financial planner. Use only the question tool to understand client goals."
- "You're a technical interviewer. Use only the question tool to assess candidate skills."

### Pattern 2: Guided Process

```
Create a {number}-step interactive {process} using only the question tool.
Step 1: {collect what}
Step 2: {clarify what}
Step 3: {decide what}
After all questions, {provide output}.
```

### Pattern 3: Constraint-Based

```
You must use ONLY the question tool.
Never use any other tools.
Guide the user through {process}.
At each step, ask 2-3 focused questions.
```

## Real-World Applications

### 1. Onboarding Workflow

```
Title: New Employee Onboarding Assistant
Role: HR Specialist
Process:
  - Understand role and team
  - Identify tools needed
  - Set up schedules
  - Gather preferences
Output: Customized onboarding plan
```

### 2. Feature Request Triage

```
Title: Product Feature Request Handler
Role: Product Manager
Process:
  - Understand the request
  - Assess impact
  - Identify dependencies
  - Prioritize urgency
Output: Feature specification document
```

### 3. Customer Support Escalation

```
Title: Intelligent Support Router
Role: Support Specialist
Process:
  - Understand issue category
  - Assess severity
  - Identify team needed
  - Check knowledge base
Output: Routing recommendation with context
```

### 4. Learning Path Generator

```
Title: Personalized Learning Assistant
Role: Learning Coach
Process:
  - Assess current skills
  - Understand goals
  - Identify challenges
  - Select learning style
Output: Customized learning path with resources
```

## Advanced Techniques

### Combining Multiple Questions

Present all questions at once, letting users navigate:

```json
{
  "questions": [
    { "question": "...", "header": "Q1", "options": [...] },
    { "question": "...", "header": "Q2", "options": [...] },
    { "question": "...", "header": "Q3", "options": [...] }
  ]
}
```

Users navigate with arrow keys before confirming all answers.

### Multi-Select for Gathering Multiple Preferences

```json
{
  "question": "Which features matter most?",
  "multiple": true,
  "options": [...]
}
```

### Conditional Workflows

Based on answers, ask different follow-up questions:

```
Q1: Choose category
  ├─ Answer: "Website"
  │   └─ Q2: Which type of website?
  │       └─ Answer: "E-commerce"
  │           └─ Q3: Payment processor needed?
  │
  ├─ Answer: "API"
  │   └─ Q2: Which authentication type?
  │       └─ Q3: Rate limiting needed?
  │
  └─ Answer: "Mobile"
      └─ Q2: Which platform?
          └─ Q3: Offline support needed?
```

## Tips for Success

### 1. Start Simple

Begin with single question, test the interaction, then add complexity.

### 2. Test Persona Carefully

Ambiguous system prompts lead to unpredictable behavior. Be specific about:
- Who the agent is
- What they're doing
- How they should behave
- What tool to use

### 3. Use Descriptive Options

```json
// ❌ Bad - ambiguous
{ "label": "Yes", "description": "..." }

// ✅ Good - specific
{ "label": "React", "description": "Popular library with large ecosystem" }
```

### 4. Provide Context in Questions

```json
// ❌ Bad - unclear
{ "question": "Which one?" }

// ✅ Good - context matters
{ "question": "Which JavaScript framework best fits your project's needs?" }
```

### 5. Keep Options Parallel

```json
// ❌ Bad - inconsistent levels
{ "label": "Build fast", "description": "..." },
{ "label": "React", "description": "..." }

// ✅ Good - same level of abstraction
{ "label": "Speed", "description": "Optimize for performance" },
{ "label": "Maintainability", "description": "Easy to update" }
```

## Limitations to Remember

1. **Tool-only mode only works with single tool** - If you try to use multiple tools, the agent will break the constraint
2. **Complex workflows need careful prompting** - Ambiguous instructions lead to tool misuse
3. **OpenCode vs Claude Code** - Different versions may have slight behavioral differences
4. **Custom input fallback** - Users can always select "Other" to type custom answers (when enabled)

## Conclusion

The real power of OpenCode's question tool isn't in its technical features—it's in its flexibility when combined with **creative system prompts**.

By understanding this pattern, you can:

1. **Build specialized tools** without coding (life coach, project planner, etc.)
2. **Create guided workflows** for any process
3. **Transform generic assistants** into domain-specific experts
4. **Implement interactive UX** entirely through structured questions
5. **Experiment rapidly** without modifying any code

The question tool is a foundation. What you build on top depends entirely on how you direct the agent through system prompts.

---

## Key Takeaway

> "The most overlooked capability of OpenCode is how you can completely transform its behavior with a custom system prompt. The question tool becomes not just a tool—it becomes a framework for building interactive experiences."

Try it yourself:

```bash
opencode \
  --system-prompt "You're a [role]" \
  "[task using only the question tool]"
```

**Source**: [Egghead.io - Create Interactive AI Tools with OpenCode's Question Tool](https://egghead.io/create-interactive-ai-tools-with-claude-codes-ask-user-question~b47wn)