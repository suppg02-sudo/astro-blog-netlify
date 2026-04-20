---
pubDatetime: 2026-02-25T10:30:00Z
title: "Trade-off Analysis: A New Question Template for Better Decisions"
postSlug: "trade-off-analysis-question-template"
description: "Trade-off Analysis: A New Question Template for Better Decisions"
tags:
  - opencode
  - ux
  - question-system
  - decision-making
---

## Introduction

Decision-making is hard. When you're faced with competing options—each with compelling benefits and unavoidable drawbacks—how do you choose?

Today I'm introducing a new template for OpenCode's advanced question system: **Trade-off Analysis**. This template provides a structured framework for evaluating competing options, weighing pros and cons, and making balanced decisions with full visibility into trade-offs.

## The Problem: Decisions Are Rarely Binary

Most decision frameworks push us toward binary choices: yes/no, proceed/abort, accept/reject. But real-world decisions rarely work that way.

Consider these scenarios:

- **Architecture choice**: Monolith vs. microservices vs. modular monolith
- **Technology selection**: PostgreSQL vs. MongoDB vs. Hybrid approach
- **Deployment strategy**: GitHub Actions vs. self-hosted CI vs. third-party SaaS
- **Resource allocation**: Hire more developers vs. build tooling vs. outsource

Each option has genuine merits. Each has real costs. Each carries different risks. The "right" choice depends on your context, constraints, and goals.

## The Trade-off Analysis Template

The Trade-off Analysis template addresses this by providing a structured framework for:

1. **Enumerating options** (2-5 competing choices)
2. **Listing pros and cons** (3-5 of each per option)
3. **Quantifying costs** (time, money, complexity)
4. **Assessing risks** (what could go wrong)
5. **Scoring options** (weighted framework for comparison)
6. **Confirming decisions** (verification before commitment)

### Template Structure

{{< mermaid >}}
graph TD
    A[Decision Context] --> B[Enumerate Options]
    B --> C1[Option A]
    B --> C2[Option B]
    B --> C3[Option C]

    C1 --> D1[Pros, Cons, Cost, Risk]
    C2 --> D2[Pros, Cons, Cost, Risk]
    C3 --> D3[Pros, Cons, Cost, Risk]

    D1 --> E[Weighted Scoring]
    D2 --> E
    D3 --> E

    E --> F[Select Best Option]
    F --> G[Confirmation Checklist]
    G --> H[Action Plan]
    H --> I[Review Date]
{{< /mermaid >}}

The template evaluates each option along these dimensions:

- **Pros**: 3-5 genuine benefits, weighted by relevance
- **Cons**: 3-5 real drawbacks, not straw-man arguments
- **Cost**: Time, money, complexity, or opportunity cost
- **Risk**: What could go wrong, severity (Low/Medium/High)
- **Score**: Weighted calculation (40% benefits + 30% cost + 30% risk)

### Scoring Framework

Each option receives a weighted score:

```
Final Score = (Benefits × 0.4) + (Cost Efficiency × 0.3) + (Risk Mitigation × 0.3)
```

This framework ensures we prioritize **benefits** while accounting for **affordability** and **manageability**.

### Example: Database Selection

Let's walk through a real example: choosing a database for a new e-commerce platform.

**Option A: PostgreSQL (Relational)**

**Pros**:
- ACID compliance for transaction integrity
- Mature ecosystem and tools
- Strong query optimization
- JSON support for flexibility

**Cons**:
- Horizontal scaling requires sharding
- Schema migrations can be complex
- Performance impact on large JSON datasets

**Cost**: Medium (setup + expertise required)
**Risk**: LOW (proven technology)
**Score**: 7.2

**Option B: MongoDB (Document)**

**Pros**:
- Flexible schema for evolving product data
- Natural horizontal scaling
- Fast reads for document queries
- Easy JSON storage

**Cons**:
- Transaction support limited
- Complex joins require application logic
- Data size grows faster with denormalization

**Cost**: Medium (cloud costs higher)
**Risk**: MEDIUM (scaling complexity)
**Score**: 6.8

**Decision**: PostgreSQL chosen for transaction integrity, can add Redis caching later if needed.

This wasn't a "PostgreSQL is better" decision—it was a nuanced choice based on **transaction requirements** trumping **scaling flexibility** at this stage.

## Key Principles

### 1. Keep Options Balanced

Each option should have genuine merits. Don't create "obviously correct" straw-man options to make your preferred choice shine.

If Option A scores 9.5, Option B scores 4.2, and Option C scores 3.1—why even present B and C?

### 2. Quantify When Possible

Use actual numbers where available:

- ❌ "Fast response times"
- ✅ "100ms average response time under 1000 RPS"

- ❌ "Low cost"
- ✅ "$50/month on Heroku free tier"

- ❌ "Easy to maintain"
- ✅ "2 hours/week for routine maintenance"

Numbers make trade-offs **real**, not hypothetical.

### 3. Include Contextual Factors

The same option might be perfect for one team and disastrous for another. Context matters:

- **Team expertise**: Can we maintain this technology?
- **Timeline pressure**: Do we need fast wins or can we invest long-term?
- **Budget constraints**: What's affordable now vs. later?
- **Future growth**: Will this scale or need replacement?

The template captures these in the **Cost** and **Risk** fields.

### 4. Document Decision Rationale

Store the trade-off analysis in project documentation. Include:

- Why this option won over others
- What assumptions were made
- What risks were accepted
- When to revisit this decision

This creates a **decision audit trail** for retrospection and learning.

### 5. Allow for Hybrid Approaches

Sometimes the best choice is **none of the above**. The template supports:

- "Option A with Option B's caching layer"
- "Option C but starting with simplified MVP"
- "Combination approach: A for X, B for Y"

Mark these as "Combination" in the analysis and score based on combined pros/cons.

## Integration with Question System

The Trade-off Analysis template fits seamlessly into OpenCode's question system at `/root/.config/opencode/questions/templates/`.

### Usage Flow

```
1. Detect decision context (architecture, tech choice, resource allocation)
2. Load Trade-off Analysis template
3. Present 2-5 competing options with pros/cons/cost/risk
4. Calculate weighted scores
5. User selects best option
6. Confirmation checklist (cost acceptable? risk acceptable?)
7. Generate action plan and review date
```

### Session Summary

After completing the analysis, the template generates a comprehensive summary:

```markdown
## Trade-off Analysis Complete

**Decision Context**: Choosing database for e-commerce platform

**Options Analyzed**:
- Option A (Score: 7.2): PostgreSQL - ACID compliant, proven technology
- Option B (Score: 6.8): MongoDB - Flexible schema, scales horizontally
- Option C (Score: 6.5): Hybrid - Best of both worlds, double complexity

**Key Trade-offs**:
- Benefit vs. Cost: PostgreSQL maximizes transaction integrity
- Risk vs. Reward: MongoDB offers scaling at complexity cost
- Short-term vs. Long-term: Hybrid invests for future scale

**Decision**: Option A (PostgreSQL)

**Rationale**:
1. Primary factor: ACID compliance required for financial transactions
2. Secondary factor: Team has PostgreSQL expertise
3. Risk mitigation: Can add Redis caching layer if needed

**Action Plan**:
- Immediate: Set up PostgreSQL with read replicas
- Short-term: Implement caching strategy (3 months)
- Long-term: Evaluate sharding if traffic exceeds threshold (beyond 3 months)

**Review Date**: 2026-08-25
```

## Real-World Examples

### Example 1: Deployment Strategy

A small startup choosing between GitHub Actions, self-hosted GitLab CI, and CircleCI.

**GitHub Actions** won on:
- Zero cost (free for public repos)
- Tight GitHub integration
- Minimal maintenance overhead

**Self-hosted GitLab CI** lost on:
- Server maintenance burden for 2-person team
- No clear benefit given scale

**CircleCI** lost on:
- Pricing tiers become expensive at scale
- Vendor lock-in concerns

**Decision**: Start with GitHub Actions, evaluate needs as team grows.

### Example 2: Architecture Pattern

A SaaS company debating monolith vs. microservices.

**Monolith** won on:
- Faster development velocity (single codebase)
- Simpler deployment (one artifact)
- Easier debugging (no distributed tracing needed yet)

**Microservices** lost on:
- Premature optimization (team size < 10)
- Distributed systems complexity (no immediate need)
- Operational overhead (multiple deployments, monitoring)

**Decision**: Start as monolith, extract services when boundaries are clear.

## Best Practices

### ✅ DO

- Present 2-5 genuinely competitive options
- Use real numbers (cost, time, performance metrics)
- Weight benefits higher than cost (40% vs. 30%)
- Document assumptions and constraints
- Set review dates for decision re-evaluation

### ❌ DON'T

- Create "straw man" options to bias the decision
- Use vague qualitative descriptors ("fast", "easy")
- Ignore contextual factors (team, budget, timeline)
- Make decisions without considering opportunity cost
- Treat decisions as permanent (set review dates!)

## Anti-Patterns to Avoid

### False Trichotomy

Don't artificially create 3 options when 1 or 2 are real choices.

**Bad**:
- Option A: The right choice
- Option B: Obviously terrible
- Option C: Even worse

**Good**:
- Option A: Best for teams < 10
- Option B: Best for teams 10-50
- Option C: Best for teams > 50

### Confirmation Bias

Don't skew pros/cons to favor your preferred option. If Option A is your preference, ensure its cons are **real**, not trivial.

### Paralysis by Analysis

Don't add so many options or factors that decision becomes impossible. More than 5 options or 10 factors usually signals analysis paralysis.

### Ignoring Opportunity Cost

Always consider: "What else could we do with these resources?"

Choosing Option A means **not** doing B, C, D, and E. Is A worth the opportunity cost?

## Extension: Multi-Criteria Decision Analysis (MCDA)

For complex decisions with 5+ options, the template extends to full MCDA:

```json
{
  "criteria": ["Cost", "Performance", "Scalability", "Maintainability", "Security"],
  "weights": [0.25, 0.30, 0.20, 0.15, 0.10],
  "options": [
    {
      "name": "Option A",
      "scores": [8, 7, 6, 9, 8]
    }
  ]
}
```

Each option receives scores against all criteria, weighted by importance. Total score determines the winner.

## Conclusion

The Trade-off Analysis template brings structure to unstructured decisions. It doesn't guarantee perfect choices—but it guarantees **intentional** choices with full visibility into trade-offs.

By enumerating options, quantifying costs, assessing risks, and documenting rationale, we create decision audit trails that improve with retrospection and experience.

The template is now available at `/root/.config/opencode/questions/templates/trade-off-analysis.md`. Use it whenever you're facing competing options with no clear winner.

## Next Steps

Try the template for your next complex decision:

1. Identify 2-5 competing options
2. List 3-5 pros and cons for each
3. Estimate costs and risks
4. Calculate weighted scores
5. Confirm decision with checklist
6. Document rationale and set review date

Better decisions start with better decision-making frameworks. This template is your framework.

---

**Resources**:
- Trade-off Analysis Template: `http://ubuntu58-1:3001/editor/root/.config/opencode/questions/templates/trade-off-analysis.md`
- Question System Overview: `http://ubuntu58-1:3001/editor/root/.config/opencode/questions/README.md`
- Other Templates: decision-3way, drill-down, verification-checklist, progressive-disclosure