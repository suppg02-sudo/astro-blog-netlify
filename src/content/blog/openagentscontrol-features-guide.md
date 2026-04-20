---
pubDatetime: 2026-02-06T00:00:00Z
title: "OpenAgentsControl: The Plan-First Framework for Transparent AI Development"
postSlug: "openagentscontrol-features-guide"
description: "A comprehensive guide to OpenAgentsControl's revolutionary plan-first, approval-based agent framework with 12 primary agents, semantic memory integration, and transparent AI development workflows."
tags:
  - openagentscontrol
  - multi-agent
  - openmemory
  - ai-agents
  - fabric-patterns
  - automation
  - development
  - transparency
---

## Introduction

Traditional AI development tools operate like black boxes—you give them a task and hope the results are correct. **OpenAgentsControl** flips this paradigm on its head with a **plan-first, approval-based framework** that puts you in complete control of every step your AI agents take.

Instead of agents autonomously making code changes, OpenAgentsControl's agents propose detailed plans, wait for your approval, and execute only what you've explicitly authorized. It's the difference between hiring a consultant who asks before acting versus one who just starts making changes and tells you afterward.

In this guide, we'll explore what makes OpenAgentsControl different, how its sophisticated multi-agent system works, and why it's becoming the framework of choice for developers who want AI assistance without sacrificing control or transparency.

---

## The Core Philosophy: Control Without Compromise

At its heart, OpenAgentsControl solves a fundamental problem in AI-assisted development:

**How do you get the speed and intelligence of AI while maintaining the safety and transparency of manual development?**

The answer: **Plan-First Development**

### The Plan-First Workflow

1. **User Request**: "Add JWT authentication middleware"
2. **Agent Planning**: The agent analyzes your codebase and proposes:
   - Step 1: Install required dependencies
   - Step 2: Create authentication utility functions
   - Step 3: Add middleware to request pipeline
   - Step 4: Write comprehensive tests
   - Step 5: Update documentation
3. **User Approval**: You review the plan, modify if needed, then approve
4. **Execution**: Agent executes approved steps sequentially
5. **Validation**: Automatic testing, code review, quality checks
6. **Completion**: Agent reports what changed and test results

This eliminates the fear of "hallucinated" code breaking your project. Every change happens through explicit approval.

---

## Key Differentiators

### 1. Editable, Markdown-Based Agents

Unlike traditional frameworks where agent behavior is hardcoded in proprietary plugins, **OpenAgentsControl agents are defined in plain Markdown files**.

Your agents live in:
- **Project-specific**: `.opencode/agents/`
- **Global**: `~/.config/opencode/agents/`

You can edit them directly:

```markdown
# OpenCoder Agent

## Capabilities
- Multi-file code refactoring
- Architecture design and implementation
- Type checking and validation
- Code quality enforcement

## Instructions
When implementing features:
1. Analyze existing patterns
2. Propose architecture changes
3. Wait for user approval
4. Execute changes following code-quality.md standards
```

**No vendor lock-in**. Your agent logic isn't trapped in proprietary systems.

### 2. Live Documentation Retrieval

Your agents fetch real-time documentation instead of relying on stale training data:

- ✅ Latest npm package APIs
- ✅ Current GitHub documentation
- ✅ Official framework docs (React, Django, etc.)
- ✅ Your internal documentation

This ensures agents always use the latest API versions and best practices, not outdated knowledge from training data.

### 3. Approval-Based Execution

Nothing happens without your say-so:

```
Plan Proposed → User Review → Modification (optional) → Explicit Approval → Execution Only
```

This is fundamentally different from autonomous agents that execute first and ask questions later.

---

## The Agent Ecosystem: 12 Primary Agents + 16 Subagents

OpenAgentsControl provides a sophisticated multi-agent system, each specialized for different types of work.

### Core Agents

#### **OpenAgent** (The Coordinator)
- **Role**: Universal coordinator and default choice
- **Best For**: Most day-to-day tasks and conversations
- **Capabilities**:
  - Conversational responses to questions
  - Task coordination and delegation
  - Multi-step workflow orchestration
  - Automatic skill detection and loading
  - Intelligent delegation to specialists

When you need something done and aren't sure which specialized agent to use, start with OpenAgent. It recognizes what you're asking for and routes to the appropriate specialist.

#### **OpenCoder** (Development Specialist)
- **Role**: Complex coding and multi-file refactoring
- **Best For**: Architecture changes affecting multiple components
- **Capabilities**:
  - Multi-file code refactoring
  - Architecture design and implementation
  - Type checking and validation
  - Code quality enforcement
  - Cross-file consistency maintenance

Example: "Refactor authentication module from session-based to JWT tokens across entire codebase"

#### **OpenFrontendSpecialist** (UI/UX Expert)
- **Role**: Frontend development and design
- **Best For**: React, Vue, and modern CSS work
- **Capabilities**:
  - Component design and implementation
  - Responsive design implementation
  - Accessibility compliance (WCAG)
  - Performance optimization
  - Tailwind CSS, styled-components expertise
  - Browser testing with Agent Browser

#### **OpenBackendSpecialist** (Server-Side Expert)
- **Role**: API design and database architecture
- **Best For**: Backend development and API creation
- **Capabilities**:
  - RESTful API design and implementation
  - Database schema design and optimization
  - Authentication and authorization systems
  - Server-side business logic
  - API documentation generation

#### **OpenDevopsSpecialist** (Infrastructure Expert)
- **Role**: CI/CD, Docker, and deployment automation
- **Best For**: DevOps tasks and infrastructure management
- **Capabilities**:
  - CI/CD pipeline design
  - Docker and Kubernetes configuration
  - Infrastructure as code (Terraform, etc.)
  - Monitoring and alerting setup
  - Deployment automation

#### **OpenTechnicalWriter** (Documentation Expert)
- **Role**: Technical writing and documentation
- **Best For**: Creating comprehensive documentation
- **Capabilities**:
  - API documentation generation
  - Technical guides and tutorials
  - README and contributing guides
  - Code comments and docstrings
  - Hugo blog post integration

#### **OpenCopywriter** (Marketing Expert)
- **Role**: Marketing copy and brand messaging
- **Best For**: Marketing materials and product positioning
- **Capabilities**:
  - Compelling marketing copy
  - Product descriptions
  - Brand voice consistency
  - Landing page content
  - Email campaigns

#### **OpenDataAnalyst** (Analytics Expert)
- **Role**: Data analysis and visualization
- **Best For**: Analyzing data and creating visualizations
- **Capabilities**:
  - Statistical analysis and insights
  - Chart and dashboard generation
  - Data pattern recognition
  - Reporting and summarization
  - Predictive modeling

#### **OpenSystemBuilder** (Meta-Level)
- **Role**: Generate complete AI systems
- **Best For**: Creating custom AI architectures
- **Capabilities**:
  - System architecture design
  - Agent definition generation
  - Context file creation
  - Workflow design
  - Integration planning

#### **OpenRepoManager** (Meta-Level)
- **Role**: Repository management and coordination
- **Best For**: Repository maintenance and release management
- **Capabilities**:
  - Repository organization
  - Development workflow management
  - CI/CD configuration
  - Release management
  - Issue and PR triage

### 16 Specialized Subagents

Beyond the primary agents, OpenAgentsControl includes specialized subagents for specific tasks:

| Subagent | Purpose |
|----------|---------|
| **TaskManager** | Breaks complex features into verifiable subtasks |
| **ContextScout** | Discovers and retrieves needed context files |
| **Context Retriever** | Generic context search and retrieval |
| **CodeReviewer** | Performs code review with security checks |
| **TestEngineer** | Writes unit and integration tests |
| **CoderAgent** | Executes coding subtasks sequentially |
| **BuildAgent** | Type checks and validates builds |
| **PatternAnalyst** | Analyzes and implements codebase patterns |
| **DocWriter** | Creates and updates documentation |
| **ImageSpecialist** | Generates and edits images using Gemini AI |
| **DomainAnalyzer** | Analyzes domains and recommends architectures |
| **AgentGenerator** | Generates XML-optimized agent files |
| **ContextOrganizer** | Organizes and generates context files |
| **WorkflowDesigner** | Designs complete workflow definitions |
| **CommandCreator** | Creates custom slash commands |

---

## Multi-Agent Coordination

One of OpenAgentsControl's most powerful features is how agents work together intelligently.

### Automatic Delegation

When a task is complex, agents automatically delegate to specialists:

```
User: "Implement complete authentication system"
    ↓
OpenAgent recognizes multi-component task
    ↓
Delegates to TaskManager
    ↓
TaskManager breaks into subtasks:
  • Subtask 01: Database schema → CoderAgent
  • Subtask 02: API endpoints → CoderAgent
  • Subtask 03: Frontend forms → FrontendSpecialist
  • Subtask 04: Testing → TestEngineer
  • Subtask 05: Documentation → DocWriter
    ↓
Executes subtasks (parallel where possible)
    ↓
Validates and integrates results
    ↓
Reports completion with test results
```

### Quality Assurance Pipeline

Every code change goes through automatic validation:

```
Code Changes
    ↓
Type Checking (BuildAgent)
    ↓
Linting (BuildAgent)
    ↓
Testing (TestEngineer)
    ↓
Code Review (CodeReviewer)
    ↓
✅ Only if all pass → Merge/Deploy
```

This ensures quality without requiring manual intervention at each step.

---

## Custom Skill Integration

OpenAgentsControl agents seamlessly work with custom skills you create. Agents automatically detect and load relevant skills based on trigger words.

### How Skill Integration Works

```
User: "create blog post about AI trends"
    ↓
OpenAgent scans skill files for trigger words
    ↓
Finds Hugo skill with trigger: ["create blog post", "write a blog post"]
    ↓
Loads Hugo skill context
    ↓
Identifies hugo-mcp MCP server
    ↓
Calls hugo-mcp_create_post with parameters
    ↓
Creates blog post with proper frontmatter
    ↓
Confirms completion
```

### Integrated Skills

OpenAgentsControl works with skills for:

- **Hugo** - Static site and blog generation
- **Git Master** - Version control operations
- **Agent Browser** - Website testing and automation
- **Databases** - PostgreSQL, MySQL, Redis, MongoDB operations
- **Docker** - Container management (Portainer, Dokploy)
- **Transcription** - YouTube video transcription
- **Frontend UI/UX** - Component and design generation

Your custom skills integrate automatically through trigger detection.

---

## OpenMemory: The Semantic Memory System

A new integration with **OpenMemory** adds persistent, semantic memory to agents.

### What OpenMemory Provides

- **Vector Database**: Store embeddings for semantic similarity search
- **Temporal Knowledge Graph**: Track facts with time relationships
- **5 Memory Sectors**:
  - **Episodic**: Events and experiences ("User preferred Docker over Kubernetes")
  - **Semantic**: Facts and concepts ("JWT tokens should use RS256 algorithm")
  - **Procedural**: Workflows and processes ("Git workflow: feature → PR → review → merge")
  - **Emotional**: User preferences and satisfaction ("User loves fast build times")
  - **Reflective**: Insights and lessons learned ("Session optimization discovered 40% faster builds")

### Practical Benefits

- **Cross-Session Learning**: Agents remember decisions from previous sessions
- **Context Awareness**: Agents understand your preferences and constraints
- **Smart Retrieval**: Find relevant information by semantic meaning, not keywords
- **Salience Tracking**: Important memories stay prominent; trivial ones fade
- **No Training Data Needed**: Learn from your actual usage patterns

Example: An agent remembers you prefer PostgreSQL over MongoDB and automatically recommends PostgreSQL for future projects, understanding the semantic context of "relational database for structured data."

---

## Fabric Pattern System Integration

OpenAgentsControl integrates with **Fabric**, a framework providing 242+ community-vetted prompt patterns.

### Pattern Categories

- **Extract Patterns**: Extract wisdom, insights, and patterns from documents
- **Create Patterns**: Generate content, summaries, essays
- **Analyze Patterns**: Analyze claims, risk, prose quality
- **Improve Patterns**: Enhance prompts and writing

### Automatic Pattern Selection

Agents automatically select appropriate patterns based on task intent:

```
Task: "Extract key insights from research paper"
    ↓
Agent recognizes extraction intent
    ↓
Selects Fabric extract_insights pattern
    ↓
Applies pattern to document
    ↓
Returns structured insights
```

This leverages community expertise without requiring manual pattern selection.

---

## Multi-Language Support

OpenAgentsControl fully supports development across multiple languages:

- ✅ **TypeScript** - Full support with type checking
- ✅ **Python** - Complete framework expertise
- ✅ **Go** - Concurrent programming patterns
- ✅ **Rust** - Safety and performance optimization
- ✅ **And more** - Language-specific patterns for others

Agents understand language-specific idioms, best practices, and frameworks.

---

## Real-World Workflows

### Workflow 1: Blog Post Creation

**Agent**: OpenTechnicalWriter
**Skill**: Hugo
**Time to Complete**: ~5 minutes

```
User: "create blog post about OpenAgentsControl features"
    ↓
OpenAgent detects "blog post" trigger
    ↓
Loads Hugo skill
    ↓
Agent creates post with:
  • Compelling title and slug
  • SEO-optimized frontmatter
  • Well-structured content
  • Proper Markdown formatting
  • Category and tag suggestions
    ↓
Copies to /media/docs/output/
    ↓
Post available at: http://ubuntu58-1:1314/YYYY/MM/DD/slug/
```

### Workflow 2: Feature Implementation

**Agent**: OpenCoder (with TaskManager)
**Time to Complete**: 30 minutes to 2 hours

```
User: "Add real-time notifications to user dashboard"
    ↓
OpenCoder proposes plan:
  1. Database schema for notifications table
  2. WebSocket server setup
  3. Backend API endpoints
  4. Frontend notification component
  5. Real-time update logic
  6. Test coverage (99%+)
  7. Documentation updates
    ↓
User reviews and approves plan
    ↓
TaskManager delegates to specialists:
  • CoderAgent handles database and backend
  • FrontendSpecialist handles UI component
  • TestEngineer writes comprehensive tests
  • CodeReviewer validates quality
    ↓
All subtasks execute in parallel where possible
    ↓
Integration testing validates end-to-end flow
    ↓
Feature complete with full documentation
```

### Workflow 3: Codebase Refactoring

**Agent**: OpenCoder
**Time to Complete**: 1-4 hours

```
User: "Refactor authentication to use JWT instead of sessions"
    ↓
OpenCoder analyzes codebase for:
  • All session-related code
  • Authentication checks
  • Security implications
  • Test coverage needed
    ↓
Proposes multi-phase plan:
  1. Install JWT library
  2. Create JWT generation/validation utilities
  3. Update login endpoint
  4. Migrate session checks to JWT validation
  5. Update middleware
  6. Rewrite authentication tests
  7. Update API documentation
    ↓
User approves with feedback
    ↓
OpenCoder executes with automatic:
  • Type checking at each step
  • Test execution after each change
  • Code quality validation
  • Cross-file consistency checks
    ↓
Final validation:
  • All tests pass
  • No type errors
  • Code review approval
  • Documentation complete
```

---

## Why OpenAgentsControl Stands Out

### vs. Autonomous Agents

| Aspect | OpenAgentsControl | Autonomous Agents |
|--------|------------------|-------------------|
| **Execution Model** | Plan-first, approval-based | Execute first, ask later |
| **User Control** | Full visibility and approval | Black-box automation |
| **Transparency** | Every step visible | Hidden processes |
| **Risk Management** | Low (approved plans only) | High (unpredictable changes) |
| **Debugging** | Easy (approved plan as reference) | Hard (unclear why change made) |

### vs. Traditional Frameworks

| Aspect | OpenAgentsControl | Traditional Agents |
|--------|------------------|-------------------|
| **Customization** | Editable Markdown files | Hardcoded plugins |
| **Documentation** | Live real-time docs | Stale training data |
| **Memory** | Semantic (OpenMemory) | Stateless |
| **Patterns** | 242+ Fabric patterns | Limited |
| **Coordination** | Multi-agent with handoff | Single agent |
| **Vendor Lock-in** | None (local files) | Proprietary systems |

---

## Getting Started with OpenAgentsControl

### Basic Setup

1. **Install OpenCode** (hosts OpenAgentsControl)
2. **Access Agent Selection**:
   - For general tasks: Use **OpenAgent**
   - For coding: Use **OpenCoder**
   - For frontend: Use **OpenFrontendSpecialist**
   - For documentation: Use **OpenTechnicalWriter**

3. **Make a Request**:
   ```
   User: "implement feature X"
     ↓
   Agent proposes plan
     ↓
   You review and approve
     ↓
   Agent executes
   ```

### Advanced Setup

- **Custom Skills**: Create `.opencode/skill/[name]/SKILL.md` for custom automations
- **Context Files**: Define standards in `.opencode/context/` for consistency
- **OpenMemory Integration**: Enable semantic memory for learning across sessions
- **Fabric Patterns**: Integrate community patterns for specialized tasks

---

## The Future of AI-Assisted Development

OpenAgentsControl represents a shift in how we think about AI in development:

- ❌ **Old Model**: AI makes autonomous decisions (risky, unpredictable)
- ✅ **New Model**: AI proposes, humans decide, AI executes (safe, transparent)

This isn't about limiting AI capability—it's about aligning AI with human values and risk tolerance. The fastest way to build is together, with the AI handling complexity and the human making decisions.

With 12 primary agents, 16 specialized subagents, semantic memory integration, and a rich ecosystem of skills and patterns, OpenAgentsControl provides everything you need for intelligent, transparent, controlled AI-assisted development.

---

## Conclusion

OpenAgentsControl transforms AI-assisted development from a black-box proposition into a collaborative partnership where you maintain full visibility and control. By combining:

- **Plan-first workflows** (transparent, approachable)
- **Multiple specialized agents** (expertise without context limits)
- **Custom skill integration** (extensibility)
- **Semantic memory** (learning and context awareness)
- **Quality assurance pipelines** (guaranteed quality)

...OpenAgentsControl enables you to move faster without sacrificing safety, control, or understanding.

Whether you're building a new feature, refactoring existing code, creating documentation, or managing infrastructure, there's a specialized agent ready to help—with complete transparency and your explicit approval at every step.

The future of development isn't about replacing developers with AI. It's about augmenting developers with intelligent partners who propose, wait for approval, and execute with precision.

That's OpenAgentsControl.

---

**Learn More**:
- [OpenAgentsControl GitHub](https://github.com/darrenhinde/OpenAgentsControl)
- [OpenMemory Documentation](https://openmemory.ai/)
- [Fabric Pattern Library](https://github.com/danielmiessler/fabric)

**Questions?** Check the [OpenAgentsControl Agents Guide](/media/docs/output/openagentscontrol-agents-guide-20260128.md) for detailed agent specifications.