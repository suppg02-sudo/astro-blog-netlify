---
pubDatetime: 2026-02-08T00:09:00Z
title: "Best Practices for AGENTS.md and Global Instructions in OpenCode"
postSlug: "best-practices-agents-md-global-instructions"
description: "Best Practices for AGENTS.md and Global Instructions in OpenCode"
tags:
  - agents
  - configuration
  - opencode
  - best-practices
---

# Best Practices for AGENTS.md and Global Instructions in OpenCode

OpenCode provides a sophisticated multi-layered instruction system through global instructions, global AGENTS.md files, and project-specific AGENTS.md files. Understanding how these files work together—and their proper use—is critical for maintaining an efficient, consistent AI agent system.

## Overview: The Three-Layer System

Your OpenCode setup uses three distinct instruction layers:

1. **Global Instructions** (`/media/docs/instructions/global-instructions.md`) - The master trigger word and protocol file
2. **Global AGENTS.md** (`/root/AGENTS.md`) - Universal agent behavior and tool usage guidelines
3. **Project AGENTS.md** (project-specific `AGENTS.md`) - Project-specific instructions and configurations

## 1. Global Instructions File

**Location**: `/media/docs/instructions/global-instructions.md`
**Purpose**: Central repository for trigger words, system protocols, and cross-project standards

### What Goes Here

- **Trigger Words**: Single-word commands that automate specific actions (e.g., `c` for containers, `gr` for rules, `mem` for memory)
- **System-Wide Protocols**: Cross-cutting rules that apply everywhere (e.g., OpenCode process restrictions, container deployment protocols)
- **Directory References**: Standardized path mappings (e.g., "docker" → `/media/docker`, "docs" → `/media/docs`)
- **Resource Registries**: Port assignments, service URLs, API endpoints

### When It's Read

- **Every Session Start**: OpenCode loads this automatically via the `instructions` array in `opencode.json`
- **Trigger Word Activation**: When you use trigger words like `c`, `gr`, `check`, the file is implicitly referenced
- **Before Every Task**: The Memory Reading Protocol instructs agents to "Read all AGENTS.md files (global and project-specific)"

### Best Practices

✅ **DO**:
- Keep trigger words short and memorable (1-2 characters preferred)
- Document directory triggers clearly with explicit paths
- Update registries when adding new services or containers
- Include clear examples in complex protocols
- Use consistent formatting (headers, bullet points, code blocks)

❌ **DON'T**:
- Add project-specific rules here (belongs in project AGENTS.md)
- Mix trigger words with system protocols (keep them in separate sections)
- Duplicate existing functionality without checking first
- Make trigger words context-dependent (they should work consistently)

## 2. Global AGENTS.md File

**Location**: `/root/AGENTS.md`
**Purpose**: Universal agent behavior, code style standards, and development protocols

### What Goes Here

- **Code Style Guidelines**: Import ordering, formatting (Black/Biome), naming conventions
- **Build/Lint/Test Commands**: Project-specific commands for testing and validation
- **Tool Usage Protocols**: How to use MCP servers, skill delegation, background tasks
- **OpenMemory Integration**: Memory storage triggers, content classification, sector definitions
- **Browser Validation Protocol**: Mandatory testing requirements for web deployments
- **Skill Creation Guidelines**: Where and how to create new skills

### When It's Read

- **Every Session Start**: Loaded automatically via the `instructions` array in `opencode.json`
- **Before Coding Tasks**: Agents check this for code style patterns and project standards
- **When Using Tools**: Referenced for proper tool usage protocols (MCP servers, skills, etc.)

### Best Practices

✅ **DO**:
- Include code style standards that apply across all projects
- Document tool usage protocols with clear step-by-step instructions
- Keep build/lint/test commands up to date
- Include OpenMemory integration requirements
- Add skill creation guidelines for consistency

❌ **DON'T**:
- Include project-specific configurations (ports, paths, local settings)
- Add temporary workarounds or hacks without documenting them as such
- Duplicate information already in global-instructions.md
- Make project-specific assumptions about file locations

## 3. Project AGENTS.md Files

**Location**: `<project-root>/AGENTS.md` or `<project-dir>/AGENTS.md`
**Purpose**: Project-specific configurations, local overrides, and team workflows

### What Goes Here

- **Project-Specific Build Commands**: Custom build/test/lint commands
- **Local Environment Variables**: Project-specific API keys or configuration
- **Team Protocols**: Project-specific workflow agreements
- **Port and Service Assignments**: Project-specific service configurations
- **Local Tool Configurations**: MCP server settings for this project only

### When It's Read

- **When Working in a Project Directory**: Automatically loaded when agent navigates to a project folder
- **Before Project Tasks**: Agents check for project-specific overrides to global rules
- **Trigger Word Context**: Project AGENTS.md can define project-specific trigger words

### Best Practices

✅ **DO**:
- Use for project-specific customizations that shouldn't be global
- Document why you're overriding global rules (with comments)
- Keep it minimal—only what's truly project-specific
- Reference global rules explicitly when you're following them
- Update it when project requirements change

❌ **DON'T**:
- Replicate global code style guidelines (belongs in global AGENTS.md)
- Redefine system-wide trigger words (conflicts with global-instructions.md)
- Add general system protocols (belongs in global-instructions.md)
- Create conflicting rules with global files

## Avoiding Overlap and Duplication

### Current Duplication Issues

In your setup, I identified several areas of overlap:

1. **OpenMemory Integration Protocol**: Duplicated across all three files
   - Found in: global-instructions.md (lines 6-37)
   - Found in: global-instructions.md (lines 225-255)
   - Found in: global AGENTS.md (lines 17-43)
   - **Fix**: Keep the master protocol in global-instructions.md, reference it from other files

2. **Build/Lint/Test Commands**: Partially duplicated
   - Global AGENTS.md has general commands
   - Project AGENTS.md should override with project-specific commands
   - **Fix**: Document project-specific commands in project files only

3. **MCP Server Descriptions**: Mixed locations
   - Full list in global-instructions.md (lines 411-438)
   - Brief mention in global AGENTS.md
   - **Fix**: Keep comprehensive list in one place, reference from others

### Best Practice: Single Source of Truth

For each piece of information, decide its canonical location:

| Information Type | Best Location | Reference From Other Files |
|----------------|----------------|--------------------------|
| **Trigger Words** | global-instructions.md | Reference via "gr" trigger |
| **Code Style** | global AGENTS.md | Reference from project files if needed |
| **System Protocols** | global-instructions.md | Reference everywhere |
| **Project Build Commands** | project AGENTS.md | Override global defaults |
| **Memory Protocols** | global-instructions.md | Reference from all AGENTS.md files |
| **Service URLs/Ports** | global-instructions.md | Reference from project files |

## Understanding Read Frequency and Loading

### Loading Order (Based on opencode.json Configuration)

From your `opencode.json` configuration:

```json
"instructions": [
  "/media/docs/instructions/global-instructions.md"
]
```

This means:
1. **Session Initialization**: OpenCode loads global-instructions.md at session start
2. **Agent Spawn**: Each new agent receives the global instructions as base context
3. **Directory Navigation**: When agents navigate to project directories, they load local AGENTS.md if present

### Memory Reading Protocol

From your global-instructions.md, line 12:

> "2. **Project Context**: Read all AGENTS.md files (global and project-specific). If an AGENTS.md file does not exist in the current project directory, create one with project-specific agent instructions and configurations."

This means:
- **Every Task Start**: Agents are instructed to read ALL AGENTS.md files
- **Automatic Creation**: Missing project AGENTS.md files should be created automatically
- **Combined Context**: Both global and project rules apply simultaneously

### Priority Resolution

When rules conflict between files:

1. **Project AGENTS.md wins** for project-specific settings (local overrides global)
2. **Global AGENTS.md wins** for code style and general agent behavior (universal standards)
3. **Global-instructions.md wins** for system-wide protocols and trigger words (cross-cutting concerns)

## Recommended Content Distribution

### Global Instructions File (~900 lines)

```
[HEADER] # Title and purpose

[TRIGGER WORDS] (20-30 lines)
- List all single-word commands
- Brief description of each
- Example usage where helpful

[MEMORY PROTOCOLS] (50-100 lines)
- OpenMemory integration requirements
- Storage triggers and classification
- Sector definitions

[SYSTEM PROTOCOLS] (200-400 lines)
- OpenCode process restrictions
- Container deployment protocols
- Web server testing requirements

[RESOURCE REGISTRIES] (100-200 lines)
- Port assignments
- Service URLs
- API documentation references

[DIRECTORY TRIGGERS] (50-100 lines)
- Path mappings (docs, docker, config, etc.)
- Usage examples for each

[SKILL & MCP INFO] (50-100 lines)
- Available skills list
- MCP server configurations
- Tool usage guidelines
```

### Global AGENTS.md File (~200 lines)

```
[HEADER] # Title and purpose

[CODE STYLE] (30-50 lines)
- Import ordering conventions
- Formatting standards (Black/Biome)
- Naming conventions
- Type annotations guidelines

[BUILD COMMANDS] (20-30 lines)
- General build, lint, test commands
- Project structure standards

[TOOL PROTOCOLS] (50-80 lines)
- MCP server usage
- Skill delegation patterns
- Background task management

[OPENMEMORY INTEGRATION] (20-30 lines)
- Memory storage triggers
- Tag conventions
- Sector definitions

[BROWSER VALIDATION] (30-50 lines)
- Vercel Agent Browser workflow
- Testing requirements
- Artifact collection

[SKILL CREATION] (20-30 lines)
- Skill location requirements
- Structure templates
- Pre-creation checklists
```

### Project AGENTS.md File (~50-100 lines)

```
[HEADER] # Project title and purpose

[PROJECT CONFIG] (10-20 lines)
- Project-specific environment variables
- Custom build commands
- Local tool configurations

[OVERRIDES] (10-20 lines)
- Explicit overrides to global rules
- Justification for each override
- Impact assessment

[TEAM WORKFLOWS] (20-40 lines)
- Project-specific team agreements
- Review processes
- Deployment procedures

[PROJECT-SPECIFIC TOOLS] (10-20 lines)
- Local MCP server settings
- Project-specific skills
- Custom triggers
```

## Practical Recommendations

### For Your Current Setup

1. **Consolidate OpenMemory Protocol**
   - Keep master protocol in global-instructions.md
   - Reference it from global AGENTS.md: "Follow OpenMemory integration protocol from global-instructions.md"
   - Remove duplicate protocol sections from other files

2. **Clean Up Trigger Word Documentation**
   - Keep all trigger words in global-instructions.md
   - Add section in global AGENTS.md: "Trigger words are defined in global-instructions.md (use 'gr' to reference)"
   - Remove trigger word lists from project AGENTS.md files

3. **Standardize File References**
   - Use consistent path format: `/media/docs/...`, `/media/docker/...`, `/root/...`
   - Create reference tables for complex directory structures
   - Document when to use relative vs. absolute paths

4. **Improve Documentation Structure**
   - Add table of contents for long files
   - Use collapsible sections for optional content
   - Include "Last Updated" timestamps
   - Add change log sections for major updates

5. **Create Migration Guide**
   - Document process for moving content between files
   - Include validation checklist after migration
   - Store migration records in OpenMemory for tracking

## Testing Your Configuration

To verify your instruction hierarchy is working:

1. **Test Trigger Words**: Use `gr`, `c`, `mem check` to verify they work
2. **Test Code Style**: Create a small project, verify agents follow global AGENTS.md guidelines
3. **Test Project Overrides**: Create project AGENTS.md with overrides, verify they take precedence
4. **Test File Discovery**: Navigate to different project directories, verify AGENTS.md files are found/read
5. **Test Memory Integration**: Verify OpenMemory triggers work correctly across all contexts

## Conclusion

Your OpenCode instruction system is powerful and flexible. By maintaining clear boundaries between the three layers:

- **Global Instructions**: System-wide protocols and triggers
- **Global AGENTS.md**: Universal agent behavior and code standards
- **Project AGENTS.md**: Project-specific configurations and overrides

You can ensure efficient, consistent agent behavior while allowing for project-specific flexibility when needed. The key is to define clear responsibilities for each layer and avoid duplication by referencing rather than repeating.

---

## ⚠️ Critical Note: URL Format for Hugo Validation

**When creating blog posts with Hugo skill, ALWAYS provide the Tailscale hostname URL, not localhost:**

- ✅ **CORRECT**: `http://ubuntu58-1:1314/posts/2026/02/08/slug-name/`
- ❌ **WRONG**: `http://localhost:1314/posts/slug-name/`

This is required because:
1. **Validation**: Hugo skill must validate accessibility using the external URL format
2. **Tailscale Network**: Ensures the service is accessible from remote machines
3. **Cross-Platform Testing**: Validates real-world network connectivity
4. **Best Practice**: Always use Tailscale hostname `ubuntu58-1` for all web services

When the Hugo skill completes a blog post, verify it provides the correct URL format with `http://ubuntu58-1:port/path/`.

---

*This guide is based on analysis of your current OpenCode configuration at `/root/.config/opencode/opencode.json` and instruction files in `/root/AGENTS.md` and `/media/docs/instructions/global-instructions.md`.*