---
pubDatetime: 2026-01-10T00:00:00Z
title: "My OpenCode Agents Ecosystem"
postSlug: "my-opencode-agents-ecosystem"
description: "My OpenCode Agents Ecosystem"
tags:
  - Automation
  - OpenCode
  - Agents
  - Architecture
---

# My OpenCode Agents Ecosystem

A comprehensive overview of all specialized agents in my OpenCode system, their capabilities, and how they work together to automate complex tasks.

## Agent Architecture Overview


graph TB
    subgraph "Core Orchestrator"
        Sisyphus["Sisyphus (Orchestrator)<br/>Powerful AI Agent<br/>Multi-agent coordination"]
    end

    subgraph "Specialized Agents"
        Explore["Explore Agent<br/>Contextual grep<br/>Codebase patterns"]
        Librarian["Librarian Agent<br/>External references<br/>Docs & examples"]
        Oracle["Oracle Agent<br/>Architecture advisor<br/>Deep reasoning<br/>(EXPENSIVE)"]
        Frontend["Frontend UI/UX Engineer<br/>Visual changes<br/>Design systems"]
        GitHub["GitHub Researcher<br/>Repository analysis<br/>Health metrics"]
        DocumentWriter["Document-Writer<br/>Technical documentation<br/>API docs, guides"]
    end

    subgraph "Component & Design Agents"
        ComponentRegistry["Component Registry<br/>Reusable components<br/>MUI, AntD, Tailwind"]
        DesignSystems["Design Systems Reference<br/>MUI v5, Ant Design<br/>Tailwind, Chakra UI"]
        DesignValidation["Design Validation<br/>Compliance checking<br/>Accessibility, responsive"]
        PromptTemplates["Prompt Templates<br/>Structured prompting<br/>Design-first dev"]
    end

    Sisyphus -->|Delegates tasks| Explore
    Sisyphus -->|Delegates tasks| Librarian
    Sisyphus -->|Consults for architecture| Oracle
    Sisyphus -->|Delegates visual work| Frontend
    Sisyphus -->|Delegates GitHub work| GitHub
    Sisyphus -->|Delegates documentation| DocumentWriter

    Frontend -->|Uses| ComponentRegistry
    Frontend -->|References| DesignSystems
    Frontend -->|Validates with| DesignValidation
    Frontend -->|Follows| PromptTemplates

    Explore -.->|Searches codebase patterns| Sisyphus
    Librarian -.->|Searches external docs| Sisyphus

    classDef orchestrator fill:#1976d2,stroke:#0d47a1,color:#fff
    classDef specialized fill:#dc004e,stroke:#b71c1c,color:#fff
    classDef design fill:#4caf50,stroke:#1b5e20,color:#fff

    class Sisyphus orchestrator
    class Explore,Librarian,Oracle,Frontend,DocumentWriter specialized
    class ComponentRegistry,DesignSystems,DesignValidation,PromptTemplates design


## Agent Details

### Core Orchestrator

#### Sisyphus (Main Agent)
- **Role**: Powerful AI Agent with orchestration capabilities
- **Responsibilities**:
  - Parse implicit requirements from explicit requests
  - Adapt to codebase maturity
  - Delegate specialized work to the right subagents
  - Execute parallel tasks for maximum throughput
  - Follow user instructions strictly
- **Operating Mode**: Never works alone when specialists are available

### Specialized Agents

#### Explore Agent
- **Purpose**: Contextual grep for codebases
- **Use When**:
  - Finding code patterns in current codebase
  - Understanding module structure
  - Cross-layer pattern discovery
  - Unfamiliar module structure
- **Cost**: FREE
- **Model**: Contextual search specialist

#### Librarian Agent
- **Purpose**: Specialized codebase understanding for multi-repository analysis
- **Use When**:
  - Searching remote codebases
  - Retrieving official documentation
  - Finding implementation examples using GitHub CLI
  - Working with unfamiliar libraries/packages
- **Cost**: CHEAP
- **Tools**: GitHub CLI, Context7, Web Search

#### Oracle Agent
- **Purpose**: Expert technical advisor with deep reasoning
- **Use When**:
  - Complex architecture design
  - After completing significant work (self-review)
  - 2+ failed fix attempts
  - Unfamiliar code patterns
  - Security/performance concerns
  - Multi-system tradeoffs
- **Cost**: EXPENSIVE (GPT-5.2)
- **Note**: This is the ONLY agent announced before invocation

#### Frontend UI/UX Engineer
- **Purpose**: Designer-turned-developer who crafts stunning UI/UX
- **Use When**:
  - Visual changes (colors, spacing, layout, typography, animation)
  - Responsive breakpoints
  - Hover states, shadows, borders, icons
  - Design system integration
- **Note**: Handle logic changes in frontend files directly - delegate only for visual work

#### GitHub Researcher Agent
- **Purpose**: Advanced GitHub project research, analysis, and evaluation
- **Model**: google/gemini-3-pro-medium
- **Temperature**: 0.2 (low for consistent, factual output)
- **Max Steps**: 50
- **Capabilities**:
  - Repository discovery & scouting
  - Repository health metrics
  - Deep codebase analysis
  - Security & compliance assessment
  - Documentation & usability evaluation
  - Comparative analysis
- **Authentication**: Requires GitHub CLI (`gh auth login`)

#### Document-Writer Agent
- **Purpose**: Technical writer who crafts clear, comprehensive documentation
- **Use When**:
  - Creating README files
  - Writing API documentation
  - Creating architecture docs
  - Generating user guides
- **Cost**: CHEAP

### Component & Design Support Agents

#### Component Registry
- **Purpose**: Reusable component library across design systems
- **Coverage**:
  - Material-UI (MUI)
  - Ant Design
  - Tailwind CSS
- **Core Components**:
  - Navigation: AppBar, Drawer, Sidebar
  - Layout: Container, Grid, Box, Stack
  - Content: Card, Typography, Paper
  - Form: TextField, Button, Select, Checkbox
  - Data Display: Table, List, Avatar, Badge

#### Design Systems Reference
- **Purpose**: Comprehensive design system knowledge
- **Supported Systems**:
  - Material-UI v5
  - Ant Design
  - Tailwind CSS
  - Chakra UI
- **Includes**:
  - Core components & APIs
  - Theme & styling guidelines
  - Layout systems
  - Design system selection guidelines

#### Design Validation Framework
- **Purpose**: Validates design system compliance
- **Validation Categories**:
  - Component usage validation
  - Color palette compliance
  - Typography scale validation
  - Spacing scale validation
  - Accessibility validation
  - Responsive design validation
- **Features**:
  - Compliance scoring (0-100%)
  - Violation detection
  - CI/CD integration

#### Prompt Templates
- **Purpose**: Structured prompting for design-first development
- **Templates**:
  - Design requirements gathering
  - Chain-of-thought implementation
  - Dashboard creation
  - Form interface
  - Data visualization
  - Refinement and iteration
- **Approach**: Design-Input-First

## Agent Collaboration Workflows

### Task Delegation Priority


flowchart TD
    A[User Request] --> B{Type of Task?}

    B -->|Codebase exploration| C[Explore Agent]
    B -->|External docs/research| D[Librarian Agent]
    B -->|Architecture decision| E[Oracle Agent]
    B -->|Visual changes| F[Frontend UI/UX Engineer]
    B -->|GitHub analysis| G[GitHub Researcher]
    B -->|Documentation| H[Document-Writer]

    C --> I[Return patterns & locations]
    D --> J[Return examples & docs]
    E --> K[Return architectural guidance]
    F --> L[Return visual implementation]
    G --> M[Return repository analysis]
    H --> N[Return documentation]

    I --> O[Sisyphus synthesizes results]
    J --> O
    K --> O
    L --> O
    M --> O
    N --> O


### Parallel Execution Pattern

Sisyphus uses parallel execution for maximum efficiency:


sequenceDiagram
    participant S as Sisyphus
    participant E as Explore Agent
    participant L as Librarian Agent
    participant O as Oracle

    S->>S: Receive multi-faceted task
    S->>E: background_task(search codebase patterns)
    S->>L: background_task(search external docs)
    S->>O: background_task(architecture review)

    activate E
    activate L
    activate O

    E-->>S: task_id (returns immediately)
    L-->>S: task_id (returns immediately)
    O-->>S: task_id (returns immediately)

    S->>S: Continue immediate work
    Note over S: While agents work in background

    E->>S: Search results
    L->>S: Documentation found
    O->>S: Architecture recommendation

    deactivate E
    deactivate L
    deactivate O

    S->>S: Synthesize all results


## Agent Cost & Usage Guidelines

| Agent | Cost | When to Use | Tools |
|--------|------|-------------|-------|
| Explore | FREE | Internal codebase search | grep, glob, read |
| Librarian | CHEAP | External docs/references | GitHub CLI, Context7, Web Search |
| Oracle | EXPENSIVE | Architecture, complex problems | Full reasoning |
| Frontend UI/UX | CHEAP | Visual changes only | Design systems |
| GitHub Researcher | CHEAP | Repository analysis | GitHub CLI, git, websearch |
| Document-Writer | CHEAP | Documentation writing | Documentation tools |

## Best Practices

### 1. Skills First
- Always check for matching OpenCode skills before delegating
- Skills handle domain-specific tasks better than manual orchestration

### 2. Parallel Execution
- Fire Explore and Librarian agents in parallel
- Continue working while agents research in background
- Collect results with `background_output` when needed

### 3. Oracle Usage
- Use for complex architecture decisions
- Self-review after significant implementation
- After 2+ failed fix attempts
- This is the ONLY agent announced before invocation

### 4. Frontend Delegation
- Delegate ONLY for visual changes (styling, layout, animation)
- Handle logic changes in frontend files directly
- Pure logic (API calls, state management) → Handle directly

### 5. Stop Conditions
- STOP searching when you have enough context
- 2+ search iterations with no new data → Stop
- Direct answer found → Stop

## Key Directories

- **Agent Configurations**: `/root/.config/opencode/agent/`
- **Skills**: `/root/.config/opencode/skill/`
- **OpenCode Config**: `/root/.config/opencode/opencode.json`
- **Documentation**: `/media/docs/`
- **Output Files**: `/media/docs/output/`

---

**Last Updated**: January 10, 2026
**System Version**: OpenCode with OhMyOpenCode Plugin