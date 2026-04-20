---
pubDatetime: 2026-02-04T16:30:00Z
title: "Skill Tool Bug Workaround: Using Task Delegation for Skill Loading"
postSlug: "skill-tool-bug-workaround-task-delegation"
description: "Skill Tool Bug Workaround: Using Task Delegation for Skill Loading"
tags:
  - skills
  - openagents
---

## The Problem: Skill Tool Bug

In OpenCode, the `skill` tool has a critical bug where it returns numbers (0-30) instead of actual skill names when attempting to load a skill. This prevents agents from loading skill instructions and context properly.

**Symptom**: When calling `skill(name: "hugo")`, the tool responds with an error or returns a number ID instead of the skill.

## The Solution: Task Delegation

The reliable workaround is to use the `task` tool to delegate work to a subagent, specifying the `load_skills` parameter. This ensures:

1. Skills load correctly by name
2. Skill context is available throughout execution
3. Skill protocols and validation gates are enforced automatically

### Task Delegation Pattern

```json
{
  "subagent_type": "openagent",
  "load_skills": ["hugo"],
  "prompt": "Create a blog post about [topic] with title '[Title]'"
}
```

The `openagent` is the general-purpose coordinator that can load any skill and execute tasks.

## Benefits of Task Delegation

### 1. Reliable Skill Loading

Task tool correctly passes skill names to the subagent, avoiding the skill tool bug entirely.

### 2. Automated Protocol Execution

Skills define complete workflows with:
- Pre-flight checks
- Verification steps
- Gateway validation
- Error recovery procedures
- Testing requirements

The subagent follows these automatically.

### 3. Better Error Handling

When a task fails, the subagent can:
- Retry with different approaches
- Suggest alternative solutions
- Provide detailed error context
- Document the issue for future reference

### 4. Gateway Validation Enforcement

Many skills (like Hugo) have mandatory gateway validation protocols:
- Navigate to web page
- Verify HTTP status
- Take screenshot evidence
- Check content rendering

Task delegation ensures these steps are never skipped.

## Benefits of Global agents.md

Centralized behavioral protocols in `/root/.config/opencode/agents.md` provide:

### 1. Consistency Across Projects

All agents follow the same rules regardless of which project they're working in. This means:
- Same delegation patterns everywhere
- Same verification standards
- Same error handling approaches

### 2. Single Source of Truth

Global rules are updated once and apply everywhere. When we discover a better pattern:
- Update global agents.md
- All future sessions benefit immediately
- No need to update multiple project files

### 3. Project-Specific Extensions

Project-specific files (like `/media/docker/website/AGENTS.md`) can extend global rules without duplicating them. This separation:
- Prevents drift between projects
- Makes maintenance easier
- Keeps project files focused on unique requirements

### 4. Easy Maintenance

When behavioral rules change:
- Update one file (global agents.md)
- Change propagates to all contexts
- No need to hunt down scattered instructions

## Updated Delegation Patterns

Global agents.md now includes a comprehensive table of when and how to delegate:

| Domain | Delegate To | Load Skills | Trigger |
|--------|-------------|--------------|---------|
| Hugo blog posts | `openagent` | `["hugo"]` | "create blog post", "write post" |
| Documentation | `openagent` | `["hugo"]` | Documentation with Hugo integration |
| Hugo operations | `openagent` | `["hugo"]` | Theme management, site configuration |

### General Pattern

For most specialized tasks:
```json
{
  "subagent_type": "openagent",
  "load_skills": ["skill-name"],
  "prompt": "Detailed task description..."
}
```

## Key Takeaways

1. **Never use the `skill` tool** - It has a bug that prevents proper skill loading
2. **Always use `task` tool** - Delegate to `openagent` with `load_skills` parameter
3. **Follow global agents.md** - Centralized rules ensure consistency
4. **Project AGENTS.md is for extensions** - Don't duplicate global rules, only add project-specific ones
5. **Delegation provides complete execution** - Subagents follow full skill protocols including validation

## Impact

This workaround has been successfully tested with:
- Hugo blog post creation (with gateway validation)
- Mermaid diagram rendering verification
- Multiple skill loading scenarios

The pattern is deterministic and can be reliably reproduced across sessions.

## Future Improvements

When the skill tool bug is fixed, we can:
- Simplify the delegation pattern
- Remove workaround documentation
- Revert to direct skill loading

Until then, task delegation remains the reliable method.