---
pubDatetime: 2026-01-30T00:48:00Z
title: "The 12 Questions That Decide Your AI Architecture"
postSlug: "12-questions-ai-architecture-framework"
description: "A comprehensive 12-question framework for making AI architecture decisions and avoiding costly rework. Based on Louis-François Bouchard's cheat sheet from Tourzi AI."
tags:
  - ai
  - openagents
---

# The 12 Questions That Decide Your AI Architecture

Most AI projects fail before implementation begins. Teams select architectures based on trends rather than requirements, choose frameworks without evaluating alternatives, and skip scoping conversations that determine success.

In this article, I'll walk through a complete decision-making framework using two real builds: a single-agent system for marketing content generation and a multi-agent pipeline for article writing. Both projects required different architectural choices based on their constraints, and both delivered working systems.

## Why AI Projects Fail

The first question that changes everything isn't about agents, models, or tools. It's about **scope**.

### What Does the Client Actually Want?

That sounds obvious, but here's what happens in practice. A request like "AI-powered marketing content generation" isn't a deliverable. You still need to pin down what success looks like:

- Do they want a production feature, an integration, a prototype, or a handoff their team will productionize?
- What about hidden requirements: demo cadence, documentation, and how much you're expected to explain your design choices?

## The Decision Framework

Once you've nailed scope, you earn the right to talk about architecture. The rule is really straightforward: **task shape dictates structure**. Don't start from "multi-agent or not." Start from how work actually unfolds.

### Understanding Task Shape

**Q1: Is your task shape sequential or branching?**

- **Sequential tasks** fit workflows
- **Branching tasks** need agents

**Q2: Is your reasoning exploratory or deterministic?**

- **Exploratory reasoning** needs flexibility
- **Deterministic reasoning** needs constraints

### Matching Architecture to Task Shape

**Q3: How many tools do you need?** (20+ = split)

If it's more than twenty, consider splitting into multiple agents or splitting tools by domain.

**Q4: Do you need internal or proprietary data?** (RAG decision)

**Q5: Do you need a persistent state?** (framework decision)

If yes, you need a framework like LangGraph. If not, a simple script is enough.

### Real Project Examples

#### Example 1: CRM Marketing System

**Task Shape**: Sequential and linear

Single agent with well-organized toolset covering:
- Retrieval tools for customer data and documentation
- Generation tools for creating content
- Validation tools for checking character limits and template syntax

The agent decided what to generate and when to validate. The tools handled the mechanics.

#### Example 2: Article Writing System

**Task Shape**: Divergent (exploratory + constrained)

Split into two agents with simple handoff:
- **Research agent**: Exploratory web search, evaluate sources, decide if enough, pivot based on findings
- **Writer agent**: Constrained writing with style guides, formatting rules, vocabulary constraints

Research outputs written to a notes file and passed directly to writer. No orchestrator needed because actual usage pattern was naturally sequential.

## Keeping Agents Thin and Tools Heavy

Now, even with the right architecture, you can still build the wrong system if the agent is doing too much.

### The Guideline: "Thin Agent, Heavy Tools"

The agent reasons, plans, and decides which tool to call. Tools execute the actual work.

This separation matters for three reasons:

1. **Debugging**: When something breaks, you know immediately whether it's a reasoning problem or an execution problem
2. **Reusability**: Well-designed tools can be shared across agents or projects
3. **Maintainability**: Other developers can add new tools without touching the agent's orchestration logic

### What Makes a Good Tool?

Each tool should:
- Do one job well
- Return structured output
- Handle its own error cases
- Return specific feedback that the agent can act on (not vague text)
- Enforce rules deterministically in code when possible

## Selecting an Orchestration Framework

Once tools are in place, the next decision is whether you need a framework to run loops or whether that's overkill.

### Framework Decision Tree

{{< mermaid >}}
graph TD
    A[Need Complex State<br/>Management?] -->|Yes| B[Use LangGraph]
    A -->|No| C{Simple Script Enough?}
    C -->|Yes| D[Build Lightweight Custom]
    C -->|No| E[Build from Scratch]

    B[Role-Based Coordination?] -->|Yes| F[Use CrewAI]
    B -->|No| G{Need Agent Loop?}
    G -->|Yes| H[Use LangChain]
    G -->|No| I[Build from Scratch]
{{< /mermaid >}}

- **LangGraph**: Complex state management (checkpointing, branching, resuming from failures)
- **CrewAI**: Role-based multi-agent coordination with defined handoffs
- **LangChain**: Straightforward agent loop with tool calling
- **Custom**: Build from scratch when overhead isn't worth it

## Model Selection Strategy

The real answer is that it depends on task. Don't default to the largest model everywhere, and don't use the cheapest model everywhere just to save costs.

### Task Difficulty Tiers

- **Planning, evaluation, and judgment tasks** → Stronger models (require consistent reasoning)
- **Narrow execution steps** (generating short-form text, cleaning, formatting) → Cheaper models

**Test cheaper models first.** Upgrade only when quality demands it.

### Real Examples

- **CRM System**: Stronger models for orchestration and evaluation; cheaper models for routine SMS/email generation
- **Article Writing**: Stronger models for source selection and writing; cheaper models for cleanup steps

## Determining Whether You Need RAG

Do you even need RAG in your system? Retrieval-Augmented Generation is powerful, but retrieval is not always the right tool.

### RAG Decision Tree

{{< mermaid >}}
graph TD
    A[Need External Data<br/>at Generation Time?] -->|No| B[No RAG Needed]
    A -->|Yes| C[What Type of Data?]

    C -->|Unstructured Text<br/>Documentation<br/>Examples| D[Use Retrieval<br/>Embeddings + Vector Search]
    C -->|Structured Records<br/>Customer Data<br/>Product Catalogs] E[Use SQL or API]

    F[Reference Material Fits<br/>Context Window?] -->|Yes + Direct Loading OK| G[Load Directly]
    F -->|No + Need Consistency| H[Use Retrieval]

    style A fill:#90EE90,stroke:#3333
    style B fill:#FFC4E2D,stroke:#3333
    style C fill:#FFD9F3,stroke:#3333
    style D fill:#FFE6E8,stroke:#3333
    style E fill:#FFE6E8,stroke:#3333
    style F fill:#FFF3E8,stroke:#3333
    style G fill:#FFE6E6,stroke:#3333
{{< /mermaid >}}

- **Retrieval Problem**: Large unstructured text, need runtime snippets → embeddings and vector search
- **Query Problem**: Structured records (customer data, products) → SQL or API
- **Context-Fit Problem**: Fits in context window + need consistency → direct loading

## Building Validation Loops

You cannot hope an LLM gets it right every time on the first try. If outputs matter, you need explicit checks and a structured way to fix failures.

### The Rule: Build Generate-Validate-Fix Loops

{{< mermaid >}}
graph LR
    A[Generate Output]
    B[Check Hard Constraints<br/>Length, Syntax, Fields, Format]
    C[Check Soft Checks<br/>Tone, Style, Factual Accuracy]
    D[Validation Passes?]

    A --> B
    B --> C
    C --> D

    D -->|Yes| E[Specific Feedback<br/>to Agent]
    D -->|No| F[Vague Quality Score<br/>Return to Generate]
    E --> A
    F --> A

    style A fill:#90EE90,stroke:#3333
    style B fill:#FFC4E2D,stroke:#3333
    style C fill:#FFD9F3,stroke:#3333
    style D fill:#FFE6E8,stroke:#3333
    style E fill:#FFE6E8,stroke:#3333
    style F fill:#FFF3E8,stroke:#3333
{{< /mermaid >}}

### Validation Layers

1. **Hard Constraints** (Fast, deterministic)
   - Length limits
   - Syntax validity
   - Required fields
   - Format compliance

2. **Soft Checks** (Slower, LLM-as-judge)
   - Tone adherence
   - Style consistency
   - Factual accuracy

3. **Actionable Feedback**
   - "Too long by 15 characters"
   - "Syntax error on line three"
   - "Tone is too formal for this audience"

4. **Human-in-the-Loop Checkpoints**
   - Plan deliberate checkpoints
   - Review before expensive steps
   - Review before irreversible actions

## The 12 Questions

### First, Understanding Task

- [ ] Q1: Is your task shape sequential or branching?
- [ ] Q2: Is your reasoning exploratory or deterministic?

### Second, System Design

- [ ] Q3: How many tools do you need?
- [ ] Q4: Do you need internal or proprietary data?
- [ ] Q5: Do you need a persistent state?

### Third, Quality and Constraints

- [ ] Q6: Do your outputs need validation loops or quality gates?
- [ ] Q7: How much human-in-the-loop do you need, and where should those checkpoints be?
- [ ] Q8: Do you have evaluation data?

### Fourth, Operational Constraints

- [ ] Q9: What are your latency tolerances?
- [ ] Q10: What's your budget per task?
- [ ] Q11: How will you do observability?

### Fifth, Clean Decomposition

- [ ] Q12: Can your problem be decomposed cleanly into distinct competencies?

## Applying the Framework

Don't treat this like a form where you fill in all twelve answers in order. Use it as a thinking tool.

- Start with a few questions
- Follow where answers lead
- Revisit them as your project evolves

Because your understanding of the project and different challenges might change. You might start with a single agent and later realize you need to split it. You might start with a workflow and later realize you need more flexibility. That's normal.

### One Habit That Matters Most

**Document your decisions.** Don't just document what you chose. Document why.

When someone asks, "Why are we using this framework instead of that one?" you should be able to answer in terms of:

- Task shape
- State needs
- Tool complexity
- Quality requirements
- Operational constraints

That documentation also helps new team members on board and helps you remember the reasoning behind your build at the end or years after.

## Resources

The complete cheat sheet is available for free at [Louis-François Bouchard's website](https://www.louisbouchard.ai/12-questions-ai-architecture/).

For hands-on training in building these systems, Tourzi Academy offers:

- [Agent AI Course](https://links.louisbouchard.ai/)
- [Full Stack AI Engineering Course](https://links.louisbouchard.ai/)

Both courses focus on practical implementation where you build systems, deploy them, and learn trade-offs by actually running into them.

---

*Based on Louis-François Bouchard's cheat sheet from Tourzi AI, January 29, 2026*