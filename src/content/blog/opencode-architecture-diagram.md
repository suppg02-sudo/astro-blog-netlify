---
pubDatetime: 2026-02-08T00:01:00Z
title: "OpenCode Architecture Diagram"
postSlug: "opencode-architecture-diagram"
description: "OpenCode Architecture Diagram"
tags:
  - agents
  - opencode
  - architecture
  - diagram
---

Have you ever wondered how OpenCode's agent system works under the hood? Today I'm sharing a comprehensive architecture diagram that visualizes the complete system - from trigger commands to task delegation, skills, and everything in between.

{{< mermaid >}}
graph TB
    subgraph User_Layer["User Interaction Layer"]
        U1[User]
        TW[Trigger Commands<br/>o, co, gr, c, c7, u, init, api, files, smooth, mem, skills, skill, cleanup, cron, check, pw]
    end

    subgraph Global_Layer["Global Layer"]
        GR[Global Rules<br/>/media/docs/instructions/global-instructions.md]
        MCP[MCP Servers<br/>brave-search, context7, openmemory, playwright, webfetch, websearch, codesearch]
    end

    subgraph Skills_Layer["Skills Layer"]
        S1[opencodeskill]
        S2[homarr-configuration]
        S3[update-gr]
        S4[hugo]
        S5[chartjs]
        S6[databases]
        S7[dashboard]
        S8[fabric]
        S9[dokploy]
        S10[portainer]
        S11[activepieces]
        S12[affine]
        S13[freya]
        S14[copyparty]
        S15[filebrowser]
        S16[mindsdb]
        S17[crawl4ai]
        S18[kavita]
    end

    subgraph Agent_System["OpenCode Agent System"]
        MA[Main Agent<br/>Current session agent]
        SA[Sub Agents<br/>Created via Task tool delegation]
    end

    subgraph Agent_Config["Agent Configuration Layer"]
        GA[Global Agent Instructions<br/>In Global Rules]
        PA[Project AGENTS.md Files<br/>Per-project instructions]
    end

    subgraph Task_Delegation["Task Delegation Flow"]
        TD1[User Request]
        TD2[Trigger Word Match]
        TD3[Agent Processing]
        TD4[Task Tool Delegation]
        TD5[Sub Agent Execution]
        TD6[Result Return]
    end

    subgraph Skill_Delegation["Skill Delegation Flow"]
        SD1[Task Requires Specialization]
        SD2[Check Skills First<br/>Priority Rule]
        SD3[Skill Match Found]
        SD4[Load Skill]
        SD5[Execute Task with Skill]
        SD6[No Skill Match<br/>Check Fabric Patterns]
    end

    subgraph Fabric_Layer["Fabric Pattern Layer"]
        FP1[Fabric Patterns<br/>Supplement Skills]
        FP2[Pattern Discovery]
        FP3[Instruction Generation]
        FP4[ZAI API Direct Call]
    end

    subgraph Memory_Layer["Memory & Persistence Layer"]
        OM[OpenMemory MCP<br/>Semantic Storage]
        OM1[Store Key Interactions]
        OM2[Reinforce Memories]
        OM3[Query Memories]
        OM4[Memory Sectors<br/>Episodic, Semantic, Procedural, Emotional, Reflective]
    end

    subgraph Project_Layer["Project Layer"]
        P1[Project AGENTS.md Files]
        P2[Project Rules<br/>projectrules.md]
        P3[Documentation]
        P4[Container Configs]
    end

    subgraph Execution_Layer["Execution & Tools Layer"]
        T1[Bash Tool]
        T2[Read/Write/Edit Tools]
        T3[Glob/Grep Tools]
        T4[Web Tools<br/>WebFetch, GoogleSearch]
        T5[Batch Tool]
        T6[Task Tool]
        T7[Skill Tool]
    end

    U1 --> TD1
    TW --> TD2
    TD2 --> TD3
    TD3 --> SD1

    TD3 --> TD4
    TD4 --> TD5
    TD5 --> TD6
    TD6 --> U1

    SD1 --> SD2
    SD2 -->|Priority Check| SD3
    SD3 --> SD4
    SD4 --> SD5
    SD3 -->|Fallback| SD6
    SD6 --> FP2
    FP2 --> FP3
    FP3 --> FP4
    FP4 --> TD5

    GR --> TD3
    GR --> GA
    GA --> MA
    MA --> TD4
    MA --> SA
    PA --> MA
    P1 --> PA

    MCP --> TD3
    MCP --> SD5
    S1 --> SD5
    S2 --> SD5
    S3 --> SD5
    S4 --> SD5
    S5 --> SD5
    S6 --> SD5
    S7 --> SD5
    S8 --> SD5
    S9 --> SD5
    S10 --> SD5
    S11 --> SD5
    S12 --> SD5
    S13 --> SD5
    S14 --> SD5
    S15 --> SD5
    S16 --> SD5
    S17 --> SD5
    S18 --> SD5

    OM1 --> OM
    OM2 --> OM
    OM3 --> OM
    OM4 --> OM
    TD5 --> OM1
    TD6 --> OM2
    TD1 --> OM3

    T1 --> TD5
    T2 --> TD5
    T3 --> TD5
    T4 --> TD5
    T5 --> TD5
    T6 --> TD5
    T7 --> SD4

    classDef layer fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef user fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef global fill:#fff9c4,stroke:#f57f17,stroke-width:2px
    classDef skill fill:#c8e6c9,stroke:#1b5e20,stroke-width:2px
    classDef fabric fill:#ffccbc,stroke:#bf360c,stroke-width:2px
    classDef memory fill:#b2dfdb,stroke:#004d40,stroke-width:2px
    classDef exec fill:#e0e0e0,stroke:#424242,stroke-width:2px

    class User_Layer user
    class Global_Layer global
    class Skills_Layer skill
    class Fabric_Layer fabric
    class Memory_Layer memory
    class Agent_System layer
    class Agent_Config layer
    class Task_Delegation layer
    class Skill_Delegation layer
    class Project_Layer layer
    class Execution_Layer exec
{{< /mermaid >}}

## Understanding the Architecture

This diagram breaks down OpenCode's complex system into distinct layers, each serving a specific purpose. Let's walk through each one.

### User Interaction Layer

Everything starts here. You interact with OpenCode either through natural language requests or by using trigger commands - those handy shortcuts like `c` for checking containers or `gr` for referencing global rules.

Some of my favorite trigger commands:
- `skills` - Displays available skills menu
- `mem` - Store important interactions to OpenMemory
- `check` - Runs a comprehensive system check
- `pw` - Test websites with Playwright

### Global Layer

This is the foundation. Your **Global Rules** file (`/media/docs/instructions/global-instructions.md`) contains all the system-wide protocols and behaviors. Alongside it run the **MCP Servers** - external services that extend OpenCode's capabilities with search, memory, web testing, and content fetching.

### Skills Layer

One of OpenCode's most powerful features is its skill system. There are 18+ specialized skills that can be loaded on-demand:

- **opencodeskill** - For all things OpenCode configuration
- **hugo** - Static site generation with Mermaid support
- **databases** - Database management expertise
- **dashboard** - Admin panel frameworks
- And many more for containers, APIs, monitoring, and documentation

The key insight: **Skills have priority**. When a task needs specialization, the system checks skills first before falling back to Fabric patterns.

### OpenCode Agent System

Here's where confusion often happens. Let me clarify:

**OpenCode Agents** are actual AI agent instances:
- The **Main Agent** is the current session's agent you're talking to
- **Sub Agents** are temporary AI agents created via the Task tool for specialized workflows like research or code review

These are real agents with their own contexts, tools, and capabilities.

### Agent Configuration Layer

**AGENTS.md files are NOT actual agents** - they're configuration documents.

Think of them as instruction manuals. When the main agent works in a project directory, it reads the AGENTS.md file there to understand:
- What tools and protocols to use
- Project-specific rules and requirements
- Testing procedures and workflows

This separation between agents (AI instances) and AGENTS.md (configuration) is crucial for understanding how OpenCode operates.

### Task Delegation Flow

When you request something complex, the delegation kicks in:

1. **User Request** - You submit a task
2. **Trigger Word Match** - If you used a trigger command, it's recognized
3. **Agent Processing** - The main agent processes your request
4. **Task Tool Delegation** - If needed, the Task tool creates a sub-agent
5. **Sub Agent Execution** - The sub-agent handles the specialized work
6. **Result Return** - Results flow back through the chain to you

This creates a powerful system where complex tasks are broken down and delegated appropriately.

### Skill Delegation Flow

When a task requires specialization, OpenCode follows a priority-based approach:

1. **Task Requires Specialization** - The agent recognizes specialized work is needed
2. **Check Skills First** - Priority rule: always check skills first
3. **Skill Match Found** - If a skill matches, it's loaded
4. **Execute with Skill** - The task runs with the skill's expertise
5. **Fallback to Patterns** - If no skill matches, check Fabric patterns

**Critical Design Principle:** Skills ALWAYS override similar patterns when available. This ensures that specialized, tested skills are used over generic patterns.

### Fabric Pattern Layer

Fabric patterns serve as a supplement to skills. When no skill matches your task:
1. **Pattern Discovery** - The system finds a relevant Fabric pattern
2. **Instruction Generation** - Pattern instructions are generated
3. **Direct API Call** - Instructions are executed via ZAI API (not the Fabric CLI)

This provides a robust fallback mechanism while maintaining skill priority.

### Memory & Persistence Layer

OpenMemory MCP provides semantic memory storage with five sectors:
- **Episodic** - Events and conversations with timestamps
- **Semantic** - Facts, knowledge, decisions, preferences
- **Procedural** - How-to workflows and procedures
- **Emotional** - Strong feelings and reactions
- **Reflexive** - Insights and learnings

The system automatically stores long prompts, user preferences, important decisions, and successful procedures - making OpenCode smarter with each interaction.

### Project Layer

Each project folder can have its own configuration:
- **Project AGENTS.md** - Per-project instructions
- **Project Rules** (`projectrules.md`) - Validated permanent content
- **Documentation** - Project-specific guides
- **Container Configs** - Docker and deployment settings

This allows OpenCode to adapt its behavior based on the specific project it's working in.

### Execution & Tools Layer

At the bottom are the raw tools that all agents can use:
- Bash, Read/Write/Edit, Glob/Grep
- Web tools (WebFetch, GoogleSearch)
- Batch tool for parallel operations
- Task and Skill tools for delegation

These are the building blocks that make everything above possible.

## Key Design Principles

The entire system is built on these principles:

1. **Skills First** - Always check skills before patterns
2. **Priority-Based** - Skills > Patterns > Manual execution
3. **Context Awareness** - Read AGENTS.md and project rules before tasks
4. **Memory Integration** - Auto-store important interactions
5. **Delegation Efficiency** - Use Task tool for complex workflows
6. **Modular Skills** - Load skills on-demand for specialization

## Wrapping Up

This architecture makes OpenCode incredibly flexible and powerful. The separation between agents and configuration documents, the priority-based skill system, and the comprehensive memory layer all work together to create an AI development assistant that can adapt to any project while maintaining consistency across your entire workflow.

Next time you use OpenCode, remember: there's a sophisticated system working behind the scenes to make your development experience smoother and more efficient.