---
pubDatetime: 2026-02-04T00:02:00Z
title: "The Power of OpenAgentsControl: Unlocking Progressive Disclosure with Skills and Context"
postSlug: "openagentscontrol-progressive-disclosure-skills-context"
description: "The Power of OpenAgentsControl: Unlocking Progressive Disclosure with Skills and Context"
tags:
  - skills
  - openagents
---

## Introduction: Beyond Simple Chatbots

The evolution of AI agents has moved from simple chatbots to sophisticated systems capable of complex task orchestration. At the forefront of this evolution stands **OpenAgentsControl (OAC)**, an open-source framework built on top of OpenCode that transforms how AI agents work, manage context, and scale capabilities.

This article explores the potential of OAC, how it leverages skills and context management, and most importantly, how **progressive disclosure** techniques make agentic systems both powerful and usable.

## What is OpenAgentsControl?

OpenAgentsControl is designed to extend OpenCode with specialized agents, context management, and team workflows for AI-assisted development and automation. Built on research-backed principles from Anthropic and the broader AI community, OAC provides:

### Core Features

- **Specialized Agents**: Pre-configured agents like `OpenAgent` (general tasks) and `OpenCoder` (programming-specific tasks), each with distinct capabilities and optimization
- **Lazy Initialization**: Sessions and resources created only when needed to optimize performance and reduce overhead
- **Approval Gates**: Security features where agent actions (like file writes or bash commands) require explicit user approval
- **Context Management**: Advanced handling of project context so agents understand the codebase they're working on
- **Live Documentation**: Framework pulls live documentation from official sources (GitHub, npm, docs sites) to ensure agents use up-to-date information

### Research-Backed Architecture

OAC isn't just another agent framework—it's built on actual research findings from Anthropic's 2025 multi-agent studies:

1. **Single Agent + Tools > Multi-Agent** for coding tasks (code is sequential, not parallelizable)
2. **Minimal Prompts at "Right Altitude"**—clear heuristics with examples, not exhaustive rule lists
3. **Just-in-Time Context**—tools load context on demand, not pre-loaded
4. **Outcome-Focused Testing**—measure success by "does it solve the task?" not "did it follow exact steps?"

## The Skills System: Modular Capabilities

At the heart of OAC's extensibility is the **skills system**. Skills are modular, reusable capabilities stored in `/root/.opencode/skill/[skill_name]/` that can be loaded on-demand.

### Skill Structure

Each skill follows a standardized structure:

```
/root/.opencode/skill/[skill_name]/
├── SKILL.md              (Main documentation - required)
├── QUICK_START.md        (Optional - quick reference)
├── CONFIG.md             (Optional - configuration)
└── EXAMPLES.md           (Optional - usage examples)
```

This structure ensures discoverability and consistency. The SKILL.md file contains comprehensive documentation while optional files provide quick references and examples without cluttering the main documentation.

### Skill Discovery Protocol

OAC implements automatic skill discovery with a priority-based hierarchy:

**Priority 1: OpenCode Skills** (Direct Load)
- Check available OpenCode skills for domain-specific needs
- Decision matrix matches task type to appropriate skill
- Examples: Hugo/blog posts, memory management, Docker containers, system monitoring

**Priority 2: Fabric Patterns** (via Agent)
- Content creation, analysis, or extraction tasks trigger Fabric pattern discovery
- Patterns for extracting insights, creating content, analyzing claims

**Priority 3: OpenAgentsControl Agents** (via Delegation)
- Specialized agents with specific expertise
- OpenAgent (coordination), OpenCoder (coding), TestEngineer (testing)

### Benefits of the Skills Approach

1. **Modularity**: Each skill is a self-contained capability that can be developed, tested, and updated independently
2. **Discoverability**: Skills follow naming conventions that make them searchable and identifiable
3. **Progressive Loading**: Skills load only when needed, reducing initial context window requirements
4. **Reusability**: Skills can be shared across agents and projects
5. **Maintainability**: Changes to a skill automatically benefit all agents that use it

## The Context Folder: Progressive Disclosure in Action

The most powerful yet underutilized aspect of OAC is the **context folder** system located at `/root/.config/opencode/context/`. This implements progressive disclosure at the technical architecture level.

### How Context Works

Instead of pre-loading thousands of files into the agent's context window (which causes token bloat and hallucinations), OAC uses a layered approach:

1. **Discovery Phase**: Agent sees only high-level metadata (table of contents, file listings)
2. **Planning Phase**: Agent identifies what specific files or documentation it needs
3. **Just-in-Time Loading**: Agent loads only the files needed for the current task
4. **Execution Phase**: Agent operates with minimal, relevant context

### Context File Types

OAC organizes context into several categories:

**System Context**
- Global instructions and protocols
- System-wide policies (e.g., docker cleanup restrictions, evidence-based research requirements)

**Project Context**
- Project-specific agent instructions (in each project's AGENTS.md)
- Code patterns and conventions unique to the project
- Architecture decisions and design choices

**Domain Context**
- Development-specific patterns (e.g., AI/mastra-ai/concepts)
- Technology stack information
- Best practices and patterns

**Skill Context**
- Skill-specific documentation and usage patterns
- Examples and reference implementations

### The CLAUDE.md Pattern

A particularly powerful pattern in OAC is the CLAUDE.md context file, which provides a single, comprehensive source of truth for agents working on a project:

```markdown
# Project Context

## Key Commands
- npm run dev: Start development server
- npm run test: Run test suite
- npm run build: Production build

## File Structure
- src/components/: React components
- src/api/: API endpoints
- src/utils/: Utility functions

## Code Style
- Use TypeScript strict mode
- Follow ESLint rules
- Prefer functional components with hooks

## Workflow Rules
- All changes must have tests
- PR requires code review
- Never commit .env files

## Common Patterns
- State management: Use Context API
- Data fetching: Use React Query
- Error handling: Use ErrorBoundary components
```

Instead of agents having to discover these patterns through trial and error, they load the CLAUDE.md file on-demand and immediately understand project conventions.

## Progressive Disclosure: The Secret Sauce

Progressive disclosure is the design principle that makes OAC both powerful and usable. It operates on two levels:

### Level 1: UI/UX Progressive Disclosure

What the human user sees is kept simple, with complexity revealed only when needed:

- **Expandable Reasoning Logs**: Instead of showing the AI's full "Chain of Thought" by default, interfaces show a status indicator (e.g., *"Searching..."*) with an optional "Show steps" toggle
- **Intermediate Results & Previews**: In long-running tasks (e.g., writing a 10-page report), UI discloses drafts or outline snippets as they're generated
- **Contextual Tool Discovery**: Rather than showing 50 possible skills at once, interface only highlights tools relevant to the current conversation
- **Confidence Scores & Uncertainty**: Disclosing AI's confidence level only when it falls below a certain threshold

### Level 2: Technical Progressive Disclosure (Context Management)

How the AI manages its own data and context window:

- **The Skills Pattern**: Instead of feeding agents 1,000 pages of documentation, the system provides a table of contents (metadata). The agent "discloses" full technical details to itself only when it decides a specific skill is needed
- **Model Context Protocol (MCP)**: Dynamic fetching from external sources (databases, local files) on a need-to-know basis rather than loading everything initially
- **Layered Prompts**: Breaking complex goals into stages (Discovery → Planning → Execution). The agent only sees "Execution" instructions once the "Planning" phase is confirmed

### Benefits of Progressive Disclosure

1. **Reduced Hallucinations**: By limiting active context to only what's relevant, the agent is less likely to get confused by "noise" in the data
2. **Token Efficiency**: Disclosing information only when necessary significantly reduces token usage, lowering the cost of running the agent
3. **User Trust**: Complete transparency can be overwhelming and look "messy." Progressive disclosure creates a "magical" experience (simple UI) while maintaining an "auditable" back-end (detailed logs)
4. **Scalability**: As the system grows (more skills, more context files, more agents), progressive disclosure prevents the system from collapsing under its own weight

## Setting Up OpenAgentsControl

### Installation

Prerequisites: You must have OpenCode CLI installed.

```bash
curl -fsSL https://raw.githubusercontent.com/darrenhinde/OpenAgentsControl/main/install.sh | bash -s developer
```

### Configuration

OAC configuration lives in `/root/.config/opencode/opencode.json`. Here's a sample configuration:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "openagent": {
      "mode": "primary",
      "model": "anthropic/claude-sonnet-4-20250514",
      "prompt": "{file:./prompts/openagent.md}",
      "tools": {
        "write": true,
        "edit": true,
        "bash": true
      }
    }
  },
  "permission": {
    "edit": "allow",
    "bash": "allow"
  },
  "mcp": {
    "context7": {
      "type": "local",
      "enabled": true
    },
    "openmemory": {
      "type": "remote",
      "url": "http://localhost:8080/mcp",
      "enabled": true
    }
  }
}
```

### Setting Up Skills

1. **Create Skill Directory**:
```bash
mkdir -p /root/.opencode/skill/my-new-skill/
```

2. **Create SKILL.md** (required):
```bash
cat > /root/.opencode/skill/my-new-skill/SKILL.md << 'EOF'
# My New Skill

## Purpose
Brief description of what this skill does

## When to Use
- Situation 1
- Situation 2

## How to Use
Step-by-step instructions
EOF
```

3. **Add Optional Files**:
- `QUICK_START.md`: Quick reference guide
- `CONFIG.md`: Configuration options
- `EXAMPLES.md`: Usage examples

### Setting Up Context

1. **Create Project-Specific AGENTS.md**:
```bash
cat > /media/docker/my-project/AGENTS.md << 'EOF'
# My Project Agents

## Agent Instructions
Project-specific agent instructions

## Tool Usage Protocols
- Skill Delegation: When to delegate
- Background Task Management: How to handle tasks
- Task Scoping: What's in scope

## OpenMemory Integration
All OpenMemory operations follow the storage policy
EOF
```

2. **Create Domain Context Files**:
```bash
mkdir -p /root/.config/opencode/context/development/
cat > /root/.config/opencode/context/development/my-technology-stack.md << 'EOF'
# Technology Stack Context

## Key Commands
- Command 1: Description
- Command 2: Description

## Common Patterns
- Pattern 1: When to use
- Pattern 2: When to use
EOF
```

## Managing OpenAgentsControl: Commands and Workflows

Once OAC is installed, you have access to a comprehensive set of commands for managing agents, skills, and context. Here's a practical guide to the most common management tasks.

### Agent Management

**List Configured Agents**:
```bash
# View all available agents
cat /root/.config/opencode/opencode.json | jq -r '.agent | keys[]'

# Check specific agent configuration
cat /root/.config/opencode/opencode.json | jq '.agent.openagent'
```

**Use Specific Agents**:
```bash
# Universal coordinator (recommended for most tasks)
opencode --agent=openagent

# Complex development and multi-file refactoring
opencode --agent=opencoder

# Research specialist
opencode --agent=researcher
```

**Create New Agent**:
```bash
# Use the built-in agent creator command
/new-agents <agent-name>

# Example: Create a Python development specialist
/new-agents python-dev
```

The agent creator follows research-backed best practices:
- Minimal prompts at "right altitude" (~500 tokens)
- Clear tool definitions (purpose, when to use, when not to use)
- 8 comprehensive tests (planning, context loading, implementation, etc.)
- Just-in-time context loading

### Skills Management

**List Installed Skills**:
```bash
# View all available skills
ls /root/.opencode/skill/

# Check skill structure
ls -la /root/.opencode/skill/hugo/
```

**Create New Skill**:
```bash
# 1. Create skill directory
mkdir -p /root/.opencode/skill/my-new-skill/

# 2. Create SKILL.md (required)
cat > /root/.opencode/skill/my-new-skill/SKILL.md << 'EOF'
---
description: "Brief description of what this skill does"
mode: primary
temperature: 0.7
---

# My New Skill

## Purpose
Clear, concise description of what this skill accomplishes

## When to Use
- Use case 1: When you need to do X
- Use case 2: When you need to do Y
- Use case 3: When you need to do Z

## How to Use
1. Step 1: First action
2. Step 2: Second action
3. Step 3: Third action

## Key Commands
- `command1`: What it does
- `command2`: What it does

## Common Patterns
- Pattern 1: When and how to use
- Pattern 2: When and how to use

## Troubleshooting
- **Issue**: Problem description
  - **Solution**: How to fix it
EOF

# 3. Add optional files
# QUICK_START.md - Quick reference guide
# CONFIG.md - Configuration options and parameters
# EXAMPLES.md - Usage examples and scenarios
```

**Skill Structure Standards**:
- `SKILL.md` - Required main documentation with frontmatter
- `QUICK_START.md` - Optional quick reference
- `CONFIG.md` - Optional configuration guide
- `EXAMPLES.md` - Optional usage examples

### Context Management

**List Context Files**:
```bash
# View all context files
find /root/.config/opencode/context/ -name "*.md"

# Check project-specific contexts
find /media/docker/*/AGENTS.md 2>/dev/null
```

**Create Project-Specific Context**:
```bash
# Create AGENTS.md for a project
cat > /media/docker/my-project/AGENTS.md << 'EOF'
# My Project Agents

## Agent Instructions
- Use OpenAgent for general coordination tasks
- Use OpenCoder for complex refactoring
- Always read this file before making changes

## Tool Usage Protocols
- **Skill Delegation**: Only delegate to specialists for truly independent tasks
- **Background Task Management**: Use task tool for multi-step workflows
- **Task Scoping**: Always clarify scope before starting

## OpenMemory Integration
All OpenMemory operations follow the storage policy in global-instructions.md

## Code Style
- Use TypeScript strict mode
- Follow ESLint rules
- Write tests for all new features
EOF
```

**Create Domain Context**:
```bash
# Create domain-specific context
mkdir -p /root/.config/opencode/context/development/
cat > /root/.config/opencode/context/development/my-stack.md << 'EOF'
# My Technology Stack

## Key Commands
- `npm run dev`: Start development server on port 3000
- `npm test`: Run Jest test suite
- `npm run build`: Production build with optimizations
- `npm run lint`: Run ESLint checks

## File Structure
- `src/components/`: React components
- `src/api/`: API client and endpoints
- `src/utils/`: Utility functions
- `src/hooks/`: Custom React hooks

## Code Style
- Use functional components with hooks
- Prefer composition over inheritance
- Write descriptive variable names
- Add JSDoc comments for complex functions

## Workflow Rules
- All changes require tests
- Run linter before committing
- Use conventional commit messages
- Never commit .env files or secrets

## Common Patterns
- **State Management**: Use React Context API for global state
- **Data Fetching**: Use React Query for server state
- **Error Handling**: Use ErrorBoundary components for graceful failures
EOF
```

### Testing Agents

**Run All Tests**:
```bash
cd /media/docker/OpenAgentsControl
npm test
```

**Test Specific Agent**:
```bash
# Test OpenAgent with different models
npm run test:openagent:claude      # Claude Sonnet 4.5 (best quality)
npm run test:openagent:grok        # Grok (free tier, fast)
npm run test:openagent:gpt4         # GPT-4 Turbo

# Test OpenCoder
npm run test:opencoder:claude
npm run test:opencoder:grok
```

**Test by Category**:
```bash
# Developer tests (code, docs, tests)
npm run test:openagent:developer

# Context loading tests
npm run test:openagent:context

# Business/conversation tests
npm run test:openagent:business
```

**View Test Results**:
```bash
# Launch interactive dashboard
npm run dashboard:open

# View latest results
cat evals/results/latest.json

# View specific agent results
npm run results:openagent
```

The test dashboard provides:
- ✅ Real-time test results visualization
- ✅ Filter by agent, category, status
- ✅ Detailed violation tracking
- ✅ CSV export functionality
- ✅ Historical results tracking

### Configuration Reference

**Key Configuration Files**:
- `/root/.config/opencode/opencode.json` - Main OpenCode configuration
- `/root/.config/opencode/agents.md` - Agents configuration
- `/root/.opencode/skill/[skill-name]/SKILL.md` - Skill definitions
- `/root/.config/opencode/context/*.md` - Context files
- `/root/.config/opencode/commands/[command-name].md` - Command definitions
- `/media/docker/[project]/AGENTS.md` - Project-specific instructions

**Common Configuration Tasks**:
```bash
# Edit main configuration
nano /root/.config/opencode/opencode.json

# Reload OpenCode to apply changes
# Restart OpenCode server if running

# Validate JSON syntax
cat /root/.config/opencode/opencode.json | jq .
```

### Daily Workflow Example

Here's how you might use OAC commands in a typical development session:

```bash
# 1. Check available agents
ls /root/.opencode/skill/

# 2. Start OpenAgent for general coordination
opencode --agent=openagent

# 3. During session, OAC automatically:
#    - Loads relevant skills on-demand
#    - Delegates to specialists when needed
#    - Pulls context from AGENTS.md files
#    - Executes with approval gates

# 4. After major changes, run tests
cd /media/docker/OpenAgentsControl
npm run test:openagent:claude

# 5. Review results in dashboard
npm run dashboard:open

# 6. If tests pass, verify with agent browser
/media/docs/output/agent-browser-working.sh navigate "http://localhost:3000"
```

## Assessment: Are You Using All OAC Features?

Based on current setup analysis, here's a checklist of OAC features and their potential utilization:

### ✅ You're Likely Using:
- **OpenCode Configuration**: Basic opencode.json with MCP servers
- **Global Instructions**: agents.md with behavioral protocols
- **Skills Directory**: Some skills installed at `/root/.opencode/skill/`
- **Context Folder**: Some context files exist at `/root/.config/opencode/context/`

### ⚠️ Partially Configured:
- **OAC-Specific Agents**: No dedicated `/root/.config/opencode/agents/` directory found
- **Skill Permissions**: No skill permission patterns defined in opencode.json
- **Agent-Specific Context**: Limited project-specific AGENTS.md files

### ❌ Potentially Missing:
- **Progressive Disclosure Patterns**: No evidence of layered prompting or just-in-time context loading
- **Skill Discovery Automation**: Manual skill loading vs. automatic discovery
- **Approval Gates**: No documented approval strategies for dangerous operations
- **Test Coverage**: No evidence of automated agent testing

### Recommendations to Fully Leverage OAC:

1. **Create Specialized Agents**: Define agents for specific domains (e.g., `python-dev`, `frontend-specialist`, `api-tester`)

2. **Implement Skill Permissions**: Add skill permission patterns to opencode.json to control which skills agents can access

3. **Expand Context Files**: Create comprehensive CLAUDE.md files for major projects to reduce discovery overhead

4. **Enable Progressive Disclosure**: Refactor agents to use layered prompts (Discovery → Planning → Execution)

5. **Set Up Approval Gates**: Configure approval strategies for dangerous operations (file deletion, bash commands)

6. **Implement Agent Testing**: Create test suites for agents following OAC's 8-test framework

## Conclusion

OpenAgentsControl represents a paradigm shift in how we think about AI agents. By combining modular skills, intelligent context management, and progressive disclosure techniques, it enables agents that are:

- **Powerful**: Access to specialized capabilities through skills
- **Efficient**: Minimal token usage through just-in-time context loading
- **Trustworthy**: Approval gates and auditable logs
- **Scalable**: Progressive disclosure prevents collapse under complexity
- **Maintainable**: Modular skills and context files that can be developed independently

The key insight is that **more complexity doesn't mean more complexity for the user**. Through progressive disclosure, OAC hides the complexity while providing all the power when needed.

The setup described in this article provides a foundation, but the true potential comes from continuous iteration—creating more skills, refining context files, and discovering new progressive disclosure patterns. The journey of building an agentic system is never complete, but OAC provides the right framework to make it a successful one.

---

## Further Reading

- [OpenAgentsControl Repository](https://github.com/darrenhinde/OpenAgentsControl)
- [OpenCode Documentation](https://opencode.ai/docs)
- [Anthropic Multi-Agent Research](https://www.anthropic.com/research)
- [Model Context Protocol](https://modelcontextprotocol.io/)