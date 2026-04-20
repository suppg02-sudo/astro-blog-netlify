---
pubDatetime: 2026-01-24T00:02:00Z
title: "Building a Sovereign AI Assistant: Architecture & Orchestration"
postSlug: "building-sovereign-ai-assistant"
description: "Building a Sovereign AI Assistant: Architecture & Orchestration"
tags:
  - agents
  - fabric
  - opencode
  - architecture
  - mcp
  - hugo
  - orchestration
---

## Introduction

What does it take to build a sovereign, self-hosted AI assistant that functions as a true "second brain"? Over the past year, I've been building exactly that—a multi-agent orchestration system that combines OpenCode, Fabric patterns, MCP servers, and local-first AI models.

This article walks through the complete architecture, from user request to task completion, and explains how all the pieces fit together.

## The Big Picture

```mermaid
flowchart TD
    A[User Request] --> B[Sisyphus<br/>Orchestration Agent]
    B --> C[Intent Gate<br/>Classification]
    C --> D{Complexity?}
    D -->|Simple| E[Direct Execution<br/>with Tools]
    D -->|Complex| F[Parallel Agents<br/>Explore + Librarian]
    F --> G[OMA Delegation<br/>with Skills]
    G --> H[MCP Servers<br/>External Capabilities]
    H --> I[Execution &<br/>Verification]
    I --> J[OpenMemory<br/>Storage]
    J --> K[Document Output]
```

At the center sits **Sisyphus**, an orchestration agent that coordinates everything. But before diving into the flow, let's understand the foundational layers.

## Layer 1: Global Instructions & Context

Every interaction starts with **global-instructions.md** (`/media/docs/instructions/global-instructions.md`). This is the primary instruction file loaded by OpenCode, containing:

- Core protocols (MUST-DO rules)
- Memory reading protocols
- Skill & pattern creation references
- OpenMemory usage protocols
- MCP server authentication

Before any task, agents must:
1. Read `global-instructions.md`
2. Read project-specific `AGENTS.md`
3. Check OpenMemory for relevant context
4. Consult relevant documentation

This ensures every agent operates with full context and follows established protocols.

## Layer 2: Architecture Philosophy - TELOS

The system is guided by **TELOS** (`/media/docs/instructions/telos.md`), a constitutional document defining:

- **Mission**: Build sovereign, open-source AI infrastructure as a true "second brain"
- **Core Principles**: Data sovereignty, open source by default, local-first AI
- **Ultimate Goal**: Design instructions so clear and deterministic that smaller open-source models can execute tasks correctly

The current focus is migrating from proprietary models to local inference (z.ai 4.7 Flash) through improved instruction clarity. Librarian and Hugo agents already run on local models via provider.

## Layer 3: Skills & Patterns

### OpenCode Skills

Skills are specialized instruction bundles loaded when delegating tasks. Located at `/root/.config/opencode/skill/[name]/SKILL.md`, they provide domain expertise:

- **hugo** - Hugo static site generator operations
- **agent-browser** - Browser automation (95% success rate)
- **portainer** - Container management
- **dokploy** - Deployment platform
- And 20+ more...

Each skill follows a structured format:
```markdown
## [Skill Name]
### Purpose
### Required Tools
### Success Criteria
### Task Workflow (Must follow exactly)
### Constraints (MUST DO/MUST NOT DO)
### Error Handling
### Examples
```

### Fabric Patterns

The **Fabric AI Framework** (`/media/docker/fabric`) provides 200+ reusable patterns for:

- **Analysis**: `analyze_incident`, `analyze_paper`
- **Creation**: `create_pattern`, `create_hugo_post`, `create_visualization`
- **Extraction**: `extract_wisdom`, `extract_patterns`, `extract_insights`
- **Improvement**: `improve_writing`, `improve_prompt`
- **Summarization**: `summarize`, `summarize_git_changes`

Accessed via CLI (`/root/.local/bin/fabric`) or API (port 8085).

## Layer 4: MCP Servers - The External Layer

MCP (Model Context Protocol) servers provide tools for agents to interact with external systems. Configured in `/root/.config/opencode/opencode.json`:

```mermaid
flowchart LR
    A[Agents] --> B[OpenCode]
    B --> C[MCP Protocol]
    C --> D[Brave Search<br/>Web Search]
    C --> E[Context7<br/>Library Docs]
    C --> F[OpenMemory<br/>Semantic Memory]
    C --> G[Crawl4AI<br/>Web Crawling]
    C --> H[Hugo MCP<br/>Site Operations]
    C --> I[Exa Code<br/>GitHub Search]
    C --> J[Agent Browser<br/>Automation]
    C --> K[Zread<br/>GitHub Research]
    C --> L[SerpAPI<br/>Universal Search]
```

### Key MCP Servers

**OpenMemory** (`http://localhost:8080/mcp`)
- Purpose: Semantic memory storage and retrieval
- Tools: `store`, `query`, `reinforce`, `list`, `get`
- Auth: Bearer token `openmemory-secret-key-2024`
- Known Issue: Content truncation bug (98%+ data loss on long content)
  - Workaround: Store large content in `/media/docs/output/`, use OpenMemory for metadata

**Context7**
- Purpose: Search documentation, libraries, SDKs
- Tools: `resolve-library-id`, `query-docs`
- Use case: When working with unfamiliar libraries or frameworks

**Brave Search**
- Purpose: Web search capabilities
- Tools: `brave_web_search`, `brave_local_search`

**Agent Browser** (Preferred over Playwright MCP)
- Purpose: Browser automation
- Success rate: 95% vs 80% for Playwright MCP
- Tools: Navigation, actions, forms, screenshots, snapshots

**Other Servers**: Crawl4AI (web crawling), Hugo MCP (site ops), Exa Code (GitHub), Zread (GitHub), SerpAPI (universal search), Z.ai MCP (Z.ai API)

## Layer 5: Multi-Agent Orchestration (OMA)

**Oh My Open Code** orchestrates 8 specialized AI agents via domain-optimized models:

| Agent | Model | Purpose |
|-------|-------|---------|
| **Sisyphus** | GLM-4.7 | Orchestration and coordination |
| **Oracle** | GLM-4.7 | Read-only consultation for architecture/debugging |
| **Librarian** | GLM-4.7-Flash | Research - external docs, OSS, GitHub |
| **Explore** | GLM-4.7-Flash | Codebase analysis and pattern discovery |
| **Frontend-UI-UX** | GLM-4.7 | UI/UX design and styling |
| **Document-Writer** | GLM-4.7-Flash | Documentation and technical writing |
| **Multimodal-Looker** | GLM-4.7 | Media analysis (PDFs, images, diagrams) |
| **Hugo-Specialist** | GLM-4.7-Flash | Hugo static site generator operations |

### Delegation Protocol

When delegating to subagents, I include 6 mandatory sections:

1. **TASK**: Atomic, specific goal
2. **EXPECTED OUTCOME**: Concrete deliverables with success criteria
3. **REQUIRED TOOLS**: Explicit tool whitelist
4. **MUST DO**: Exhaustive requirements
5. **MUST NOT DO**: Forbidden actions
6. **CONTEXT**: File paths, existing patterns, constraints

**Critical: Session Continuity**
Every delegation returns a `session_id`. I **always resume** for follow-ups to preserve full conversation context, saving 70%+ tokens.

```python
# Resume preserved context
delegate_task(
  resume="{session_id}",
  prompt="Also: check this specific edge case"
)
```

## Complete Task Execution Flow

### Step 1: Task Reception
User provides request to Sisyphus (orchestration agent)

### Step 2: Intent Gate & Classification
Check triggers:
- External library mentioned? → Fire Librarian background
- 2+ modules involved? → Fire Explore background
- "Look into" + "create PR"? → Full implementation cycle

Classify: Trivial, Explicit, Exploratory, Open-ended, Ambiguous

### Step 3: Context Gathering (Parallel)
```python
# Fire parallel background agents
delegate_task(subagent_type="explore", run_in_background=True,
  prompt="Find auth implementations in codebase")
delegate_task(subagent_type="librarian", run_in_background=True,
  prompt="Find JWT best practices in docs")

# Continue working...
# Collect results with background_output()
```

### Step 4: Delegation Decision
- **Simple task**: Execute directly with tools
- **Complex task**: Delegate to OMA agent with appropriate category + skills
- **Multi-system/architecture**: Consult Oracle first
- **After 2+ failures**: Consult Oracle

### Step 5: Delegation with Skills
```python
delegate_task(
  category="visual-engineering",  # Domain-optimized
  load_skills=["hugo", "agent-browser"],  # ALL relevant
  prompt="1. TASK: ... 2. EXPECTED OUTCOME: ... 3. REQUIRED TOOLS: ... 4. MUST DO: ... 5. MUST NOT DO: ... 6. CONTEXT: ..."
)
```

### Step 6: Verification
- Run `lsp_diagnostics` on changed files
- Run build/test commands if applicable
- Verify all evidence requirements met

### Step 7: Cleanup
- Cancel ALL background tasks: `background_cancel(all=True)`
- Store important interactions in OpenMemory
- Copy generated documents to `/media/docs/output/`

## MCP vs. Direct Tools Decision Matrix

| Use MCP Servers When | Use Direct Tools When |
|---------------------|---------------------|
| Need external web search | Known file location |
| Need library documentation | Single keyword/pattern search |
| Need semantic memory | Simple bash commands |
| Need browser automation | LSP operations |
| Need GitHub research | File editing (Write, Edit) |
| Need web crawling | Git operations via bash |

## Key File Locations

### Configuration Files
- `/media/docs/instructions/global-instructions.md` - Primary instructions
- `/media/docker/commands/AGENTS.md` - Project-specific instructions
- `/media/docs/instructions/telos.md` - Architecture constitution
- `/root/.config/opencode/opencode.json` - MCP server configuration
- `/root/.config/opencode/oh-my-opencode.json` - OMA agent configurations

### Skills & Patterns
- `/root/.config/opencode/skill/[name]/SKILL.md` - OpenCode skills
- `/root/.config/fabric/patterns/[name]/system.md` - Fabric patterns

### Memory & Output
- `/media/docker/openmemory-data/openmemory.sqlite` - OpenMemory database
- `/media/docs/output/` - Generated documents storage
- `/media/docs/apis/` - API documentation

## OpenMemory Quick Reference

```bash
# Health check
curl http://localhost:8080/health

# Store memory
curl -X POST http://localhost:8080/mcp \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer openmemory-secret-key-2024" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "openmemory_store",
      "arguments": {
        "content": "...",
        "tags": ["tag"],
        "user_id": "sisyphus"
      }
    }
  }'

# Query memories
curl -X POST http://localhost:8080/mcp \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer openmemory-secret-key-2024" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "openmemory_query",
      "arguments": {
        "query": "search terms",
        "k": 10,
        "user_id": "sisyphus"
      }
    }
  }'
```

## Fabric CLI Quick Reference

```bash
# List patterns
fabric --listpatterns

# Run pattern
fabric --pattern extract_wisdom --input "content here"

# Create post
fabric --pattern create_hugo_post --input "topic"
```

## What Makes This Different?

### 1. Deterministic Over Probabilistic
The system prefers explicit, auditable workflows over black-box AI. When AI is used, inputs/outputs are logged for reproducibility.

### 2. Local-First AI
Ollama is the primary AI compute layer. The goal is to run everything locally while using proprietary models only for complex reasoning.

### 3. Session Continuity
Every delegation preserves conversation context through session resumption, dramatically reducing token usage and maintaining task coherence.

### 4. Parallel Exploration
Multiple agents run simultaneously to gather context, saving time and providing comprehensive coverage.

### 5. Specialized Agents
Domain-optimized models handle tasks within their expertise (UI/UX, research, documentation, infrastructure), rather than forcing one model to do everything.

## Conclusion

This infrastructure provides:

1. **Deterministic Orchestration**: Sisyphus coordinates agents with clear protocols
2. **Specialized Expertise**: OMA agents with domain-optimized models
3. **External Capabilities**: MCP servers integrate web search, documentation, memory, automation
4. **Pattern Library**: 200+ Fabric patterns for AI augmentation
5. **Skill System**: Reusable skill bundles for specialized tasks
6. **Memory Persistence**: OpenMemory for long-term context and graph relationships
7. **Documentation**: Comprehensive docs for APIs, MCP servers, and system protocols

**The Key Innovation**: Design instructions so clear that smaller open-source models can execute complex tasks correctly, enabling truly sovereign, self-hosted AI infrastructure.

The system is a living project—always evolving, always improving. Future work includes expanding local model capabilities, adding more MCP integrations, and refining skill patterns for even greater determinism.

---

*This article was generated using the system described—meta!*