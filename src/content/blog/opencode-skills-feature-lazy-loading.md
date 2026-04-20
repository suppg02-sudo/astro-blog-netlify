---
pubDatetime: 2026-02-11T11:36:00Z
title: "OpenCode Skills Feature - The Lazy Loading Game Changer"
postSlug: "opencode-skills-feature-lazy-loading"
description: "Master OpenCode's Skills feature for lazy context loading, dynamic workflows, and parameterized agent tools. Learn setup, best practices, and advanced patterns like Smart Router."
tags:
  - agents
  - skills
  - opencode
  - lazy-loading
  - automation
  - workflow
---

## Introduction

OpenCode's new Skills feature provides a powerful way to create reusable, modular tools that agents can discover and invoke on-demand. Released just days before this video, it enables **lazy context loading** - a game-changing approach to managing agent complexity and efficiency.

If you've been wondering how to implement something similar to Claude Code Skills in OpenCode, this comprehensive guide covers everything you need to know.

## What Are OpenCode Skills?

Skills are self-contained, single-file modules that enable agents to execute scripts, run commands, or perform complex workflows. Unlike loading all instructions upfront, skills use **lazy loading** - they're discovered and loaded only when agents need them.

### Core Characteristics

- **Single File**: Each skill is defined in a `SKILL.md` file
- **Lazy Discovery**: Agents use search tools to find available skills
- **Dynamic Loading**: Skills load into context only when invoked
- **Reusable**: A single skill can be used across multiple agents
- **Parameterizable**: Skills can change behavior based on configuration

## Skill File Structure

### The Mandatory Naming Convention

The most important rule: **your file must be named `SKILL.md`** (exact case and format).

```
.opencode/
└── skill/
    └── [skill-name]/
        └── SKILL.md
```

When you define the skill in agent configuration, you reference the skill name (the folder), which maps to the `SKILL.md` file inside it.

### How OpenCode Discovers Skills

OpenCode searches your local project for skill folders and automatically makes skills available to agents. The discovery process works like this:

1. Agent receives a request
2. Agent uses a search tool to discover available skills
3. OpenCode returns skill definitions and descriptions
4. Agent chooses and invokes appropriate skill(s)
5. Skill executes and returns results

**Key Insight**: Skills are injected into agent context dynamically, not upfront. This keeps context efficient while giving agents full access to available tools.

## Skill Types: From Simple to Complex

### 1. Hello Skill (Bash Execution)

The simplest skill type - execute a bash command:

```yaml
name: hello-skill
description: Basic bash command execution
commands:
  - bash -c "echo 'hello from tier one skill'"
```

**Use Case**: Simple command execution, system checks, basic automation

### 2. Step Skill (Directory-Specific Scripts)

Run scripts from a specific working directory:

```yaml
name: step-skill
description: Execute scripts from project root
script: ./scripts/step.sh
workdir: /path/to/project
```

**Use Case**: Scripts that depend on project-specific paths or dependencies

### 3. Workflow Skill (Sequential Execution)

Execute multiple scripts or skills in defined order:

```yaml
name: workflow-skill
description: Multi-step sequential workflow
workflow:
  - script: ./scripts/script1.sh
  - script: ./scripts/script2.sh
  - script: ./scripts/script3.sh
  - script: ./scripts/script4.sh
```

**Use Case**: Multi-step processes, build pipelines, deployment workflows

### 4. TypeScript Skill (Runtime Execution)

Execute TypeScript or Node.js code:

```yaml
name: ts-skill
description: Run TypeScript with Deno runtime
runtime: deno
script: ./examples/example.ts
workdir: /base/directory
```

**Critical Point**: Must run from a directory where dependencies are available. The agent needs proper environment setup (Node, Deno, Python, etc.).

### 5. Smart Router Skill (Dynamic Parameterization)

The game-changer - create completely different behaviors from a single skill using configuration:

```yaml
name: smart-router-skill
description: Dynamic behavior based on character and mission selection
config:
  character: yoda  # or: tony-stark, sherlock-holmes
  mission: 1       # or: 2, 3, etc.
scripts:
  yoda:
    mission_1: "Defend the Republic - Jedi strategy"
    mission_2: "Infiltrate the Sith - Undercover operation"
  tony_stark:
    mission_1: "Tech-based defense system"
    mission_2: "Infiltration with tech support"
  sherlock:
    mission_1: "Logical defense analysis"
    mission_2: "Deductive investigation approach"
```

## The Smart Router Pattern: A Real Example

This pattern demonstrates the power of parameterized skills:

### Mission 1: Defend the Republic (Yoda)

When `mission: 1` is configured:
- **Personality**: Wise Jedi Master
- **Strategy**: Fortify temple defenses, train padawans, council strategy
- **Output Style**: Protective, strategic, thoughtful
- **Result**: "Phase one, train the padawans. Phase two, fortify the temple defenses."

### Mission 2: Infiltrate the Sith (Yoda)

When `mission: 2` is configured:
- **Personality**: Still Yoda, but tactical operative
- **Strategy**: Study the dark side, establish cover identity, gather intelligence
- **Output Style**: Covert, analytical, intelligence-focused
- **Result**: "Undercover operation. Infiltrate the Sith. Study the dark side. Establish a cover identity."

**The Magic**: By changing a single configuration variable, you get completely different skill behavior without duplicating logic. The script contains conditional checks:

```bash
if [ "$MISSION" = "1" ]; then
  echo "Defend the Republic..."
elif [ "$MISSION" = "2" ]; then
  echo "Infiltrate the Sith..."
fi
```

## Configuration and Permissions

### Default Behavior

By default, all skills are available to all agents. The agent uses the search tool to discover them.

### Explicit Configuration

You can control which skills agents access:

```yaml
# In agent configuration
skills:
  allow:
    - hello-skill
    - step-skill
    - smart-router-skill
  deny:
    - workflow-skill
```

### Important Permission Detail

⚠️ **Access control only works on new sessions.** If a skill is already loaded in an agent's context, changing permissions won't prevent the agent from using it. You must start a new session for permissions to take effect.

## Critical Setup Issues

### YAML Indentation (SILENT FAILURE)

This is the trickiest issue: **OpenCode doesn't report indentation errors in skills**.

If your SKILL.md has incorrect indentation:
- OpenCode appears to work fine
- Skills seem available
- But they don't function correctly
- No error message is displayed

**Solution**: Carefully verify your YAML indentation matches documentation examples exactly. Use consistent spacing throughout.

### Naming and Discoverability

Skills must follow the naming convention:
- Folder name = skill identifier (used in config)
- File name = always `SKILL.md`
- Skill name defined in file = what agents see

Inconsistencies here cause skills to not be discovered properly.

## Best Practices for Effective Skills

### ✅ Do This

1. **Test Incrementally**: Test each skill individually before combining them
2. **Clear Descriptions**: Write skill prompts that agents can understand
3. **Reasonable Names**: Avoid similar names that confuse agents (not `skill1` and `skill2`)
4. **Load Gradually**: Don't load all skills at once hoping it works
5. **Monitor Context**: Be aware of context overhead as you add skills

### ❌ Avoid

1. **Silent Indentation Errors**: Double-check YAML formatting
2. **Context Overload**: Loading 50 skills for every agent
3. **Poorly Named Skills**: Names should clearly indicate purpose
4. **Complex Prompts for Basic Agents**: Match skill complexity to agent capability
5. **Assuming Error Messages**: OpenCode may silently ignore problems

## When to Use Skills

Skills are ideal for:

- **Reusable Tools**: Creating tools used across multiple agents
- **Workflow Automation**: Multi-step processes with defined sequences
- **Script Orchestration**: Managing system scripts from agent actions
- **Dynamic Behavior**: Parameterized skills that adapt to configuration
- **Code Execution**: Running Python, TypeScript, bash from agents
- **Lazy Loading Needs**: Scenarios where all tools shouldn't be pre-loaded

## Common Mistakes and How to Avoid Them

### Mistake 1: Wrong Filename
❌ Using `skill.md` or `SKILLS.md` instead of `SKILL.md`  
✅ Always use exactly: `SKILL.md`

### Mistake 2: Indentation Problems
❌ Mixing tabs and spaces, inconsistent nesting  
✅ Validate YAML indentation carefully before deployment

### Mistake 3: Similar Names
❌ `workflow-skill` and `workflow-skill-v2` confuse agents  
✅ Use descriptive, distinct names

### Mistake 4: Too Many Skills
❌ Loading 20 skills hoping agent picks the right one  
✅ Test with 2-3 skills, verify they work, then add more

### Mistake 5: Assuming Permissions Work in Sessions
❌ Changing deny/allow and expecting immediate effect  
✅ Start new sessions for permission changes to take effect

## Architecture and Context Efficiency

### How Lazy Loading Works

```
Agent Request
    ↓
Search Available Skills (tool invocation)
    ↓
OpenCode returns matching skills + descriptions
    ↓
Agent evaluates which skill(s) needed
    ↓
Skill(s) loaded into context
    ↓
Skill(s) execute
    ↓
Results returned to agent
```

### Why This Matters

- **Context Efficiency**: Only load skill definitions when needed
- **Scalability**: Can have many skills without loading all upfront
- **Flexibility**: Agents can choose appropriate tools dynamically
- **Performance**: Faster responses with focused context

### Context Overhead Considerations

While lazy loading helps, be aware:
- Each skill description adds tokens when loaded
- Many similar skills may confuse agents
- Very complex skill descriptions take more context
- Agents need sufficient capability to use skills correctly

## Real-World Application: Building Parameterized Workflows

The Smart Router pattern shows how to create sophisticated parameterized workflows:

### Pattern: Configuration-Driven Script Logic

```
Configuration File
    ↓
Script reads config values
    ↓
Conditional execution based on config
    ↓
Different behavior, same skill code
```

This pattern eliminates duplication. Instead of creating separate skills for each variation, create one skill that branches based on configuration.

### Example Expansion

Start with one character (Yoda) and one mission pair:
- Mission 1: Defend
- Mission 2: Infiltrate

Add Tony Stark with same mission pairs → 4 outcomes, 1 skill  
Add Sherlock Holmes with same mission pairs → 6 outcomes, 1 skill

Traditional approach: 6 separate skills  
Smart Router approach: 1 skill with configuration

## Conclusion

OpenCode's Skills feature represents a significant advancement in agent tool management. By combining lazy loading, modularity, and parameterization, you can build sophisticated, flexible agent systems that scale efficiently.

The key to success is:
1. Proper file setup (`SKILL.md` in correct location)
2. Careful YAML formatting (indentation matters)
3. Clear skill descriptions for agent understanding
4. Incremental testing before full deployment
5. Awareness of context loading implications

The Smart Router pattern demonstrates how powerful parameterized skills can be - delivering maximum flexibility with minimal code duplication. Whether you're building simple command execution or complex dynamic workflows, Skills provide the foundation for scalable, maintainable agent systems.

---

## Resources

- **Full Transcript**: [Resources file in output]
- **Short Summary**: [Summary file in resources]
- **Documentation**: Visit OpenCode docs, scroll to "Agent Skills" section

---

*Video by Darren Builds AI | Extracted: 2026-02-11*