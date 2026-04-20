---
pubDatetime: 2026-03-17T00:21:11Z
title: "SKILL.MD is Not Enough: The Hidden Science of Agentic Experience"
postSlug: "skill-md-not-enough-agentic-experience"
description: "SKILL.MD is Not Enough: The Hidden Science of Agentic Experience"
tags:
  - multimodal-agents
  - ai-agents
  - llm-research
  - skill-acquisition
  - xskill
---

The AI community has embraced "skill libraries" as a way to extend agent capabilities. But two groundbreaking research papers from 2026 reveal that a simple SKILL.md file isn't enough. True agentic intelligence requires something deeper: **procedural knowledge extraction at scale** and **continual learning from experience**.

## The Problem: Declarative vs. Procedural Knowledge

Large Language Models possess vast *declarative knowledge*—facts, definitions, and general information. But they often lack *procedural expertise*: the step-by-step workflows, failure recovery patterns, and context-specific adaptations that make an agent truly capable.

Consider this: an agent might know *what* a debugging tool does, but not *when* to apply it, *how* to recover when it fails, or *why* one approach works better in specific scenarios.

Two research teams tackled this problem from complementary angles:

1. **East China Normal University**: Mining procedural knowledge from open-source repositories
2. **HKUST/Zhejiang University**: Learning from an agent's own successes and failures

---

## Paper 1: Mining Skills from Open-Source Repositories

**"Automating Skill Acquisition through Large-Scale Mining of Open-Source Agentic Repositories"** (Bi et al., 2026) asks a compelling question: *Why hand-craft skills when thousands of developers have already solved these problems?*

### The Three-Stage Pipeline

The researchers developed a systematic approach to transform monolithic GitHub repositories into modular skill artifacts:

#### Stage 1: Structural Analysis
Using tools like `repo2AI`, the system maps directory hierarchies and identifies "orchestration scripts"—the brains of the repository—versus auxiliary modules. This separation is crucial: you want the decision logic, not just the utility functions.

#### Stage 2: Semantic Identification
A two-stage ranking process ensures quality:

- **Dense Retrieval**: Bi-encoders map code modules and task descriptions into vector space, finding candidates via cosine similarity
- **Binary Ranking**: A cross-encoder performs fine-grained relevance assessment to ensure patterns are reusable and non-obvious

#### Stage 3: Standardized Translation
The extracted knowledge is refactored into a **SKILL.md** format with progressive disclosure:

| Level | Content | Token Cost |
|-------|---------|------------|
| Level 1 | YAML metadata for discovery | Low |
| Level 2 | Procedural workflows and error-handling | Medium |
| Level 3 | Executable scripts and templates | High (loaded on demand) |

### The Formal Skill Paradigm

The paper defines a skill as a four-tuple:

$$S = (\mathcal{C}, \pi, \mathcal{T}, \mathcal{R})$$

Where:
- $\mathcal{C}$ = Applicability conditions (when to use this skill)
- $\pi$ = Policy (the "how-to" procedure)
- $\mathcal{T}$ = Termination criteria (when the skill is complete)
- $\mathcal{R}$ = Interface (inputs, outputs, dependencies)

### Key Innovation: Visual Anchor Prompting

One extracted technique from the *Code2Video* repository is particularly clever: **Visual Anchor Prompting** overlays a 10x10 grid on visual frames, allowing Vision-Language Models to perform precise spatial reasoning and layout correction.

### Results

- **40% gains in knowledge transfer efficiency** compared to baseline code generation
- Agent-generated educational content matched human-crafted tutorial quality
- Demonstrated scalability across different LLM providers without fine-tuning

---

## Paper 2: XSKILL - Learning from Experience

**"Continual Learning from Experience and Skills in Multimodal Agents"** (Jiang et al., 2026) takes a different approach: instead of mining external knowledge, why not learn from the agent's own trajectory?

### The Core Insight

Multimodal agents (like those using Gemini or GPT-4V) typically operate in **isolated episodes**. Even if they solve a complex task once, they don't remember the optimal workflow for next time.

XSkill solves this by distilling two distinct types of knowledge:

#### Task-Level Skills (The "Strategy")
Structured Markdown documents containing high-level workflows and reusable code/tool templates. These provide the "big picture" of how to solve a class of problems.

#### Action-Level Experiences (The "Tactics")
JSON-based insights that capture specific "if-then" scenarios:

> "If the image is blurry, use the forensic crop tool first."

These handle context-specific failure modes that the high-level strategy might miss.

### The Two-Phase Lifecycle

```
┌─────────────────────────────────────────────────────────────┐
│  PHASE I: ACCUMULATION                                      │
│  ┌──────────┐    ┌─────────────────┐    ┌──────────────┐   │
│  │ Rollouts │ -> │ Visually-Grounded│ -> │ Skill Library │  │
│  │ (attempts)│    │ Summarization    │    │ Experience Bank│ │
│  └──────────┘    └─────────────────┘    └──────────────┘   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  PHASE II: INFERENCE                                        │
│  ┌──────────┐    ┌──────────┐    ┌───────────────────────┐ │
│  │ New Task │ -> │ Retrieve │ -> │ Adapt & Inject        │ │
│  │          │    │ Relevant │    │ (to current context)  │ │
│  │          │    │ Skills   │    │                       │ │
│  └──────────┘    └──────────┘    └───────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### Key Innovations

1. **Visually-Grounded Knowledge Extraction**: Unlike previous methods, XSkill's knowledge includes visual observations, ensuring the agent understands *why* a tool was used based on what it "saw."

2. **Hierarchical Consolidation**: It doesn't store every attempt; it merges similar insights and filters for quality, preventing "memory bloat."

3. **Context-Aware Adaptation**: It doesn't copy-paste old code; it adapts tool parameters (like bounding box coordinates) to the new image.

### Results

| Metric | Improvement |
|--------|-------------|
| Performance on VisualToolBench | +2.58 to +6.71 points |
| Tool execution errors | Reduced from 29.9% to 15.3% |
| Zero-shot transfer | 2-3 points above baselines |

The error reduction is particularly significant: using proven skill templates instead of guessing syntax cut execution errors nearly in half.

---

## The Convergence: What This Means for Agent Development

Both papers point to the same conclusion: **skill acquisition requires more than documentation**.

### The Old Model
```
SKILL.md → Agent reads → Agent executes
```

### The New Model
```
Repository Mining ─┐
                   ├→ Skill Library → Context-Aware Retrieval → Adapted Execution
Experience Bank ───┘
```

### Practical Implications

1. **Don't just document workflows**—capture the conditions under which they succeed or fail
2. **Include visual context** in skill definitions when working with multimodal agents
3. **Structure skills hierarchically**: high-level strategy + low-level tactics
4. **Enable progressive disclosure**: load detailed resources only when needed
5. **Build feedback loops**: let agents learn from their own trajectories

---

## Looking Forward

The skill library ecosystem is evolving rapidly. We're moving from:

- **Static documentation** → **Procedural knowledge extraction**
- **Hand-crafted skills** → **Mined and learned capabilities**
- **Isolated episodes** → **Continual learning systems**

The SKILL.md format remains valuable, but it's now the *container*, not the *content*. The real innovation lies in how we fill that container—with knowledge extracted from repositories, distilled from experience, and adapted to context.

---

## References

- **XSKILL Paper**: [arXiv:2603.12056](https://arxiv.org/abs/2603.12056) | [Project Page](https://xskill-agent.github.io/xskill_page/)
- **Repository Mining Paper**: [arXiv:2603.11808](https://arxiv.org/abs/2603.11808)
- **Video Source**: [Discover AI - YouTube](https://www.youtube.com/watch?v=FzVC9IUUK60)