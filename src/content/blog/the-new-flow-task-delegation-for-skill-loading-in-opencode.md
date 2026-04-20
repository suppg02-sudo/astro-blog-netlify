---
pubDatetime: 2026-02-04T18:30:00Z
title: "The New Flow: Task Delegation for Skill Loading in OpenCode"
postSlug: "the-new-flow-task-delegation-for-skill-loading-in-opencode"
description: "The New Flow: Task Delegation for Skill Loading in OpenCode"
tags:
  - workflow
  - skills
  - openagents
---

## Overview

After extensive debugging and testing, we've established a reliable pattern for using specialized skills in OpenCode through task delegation. This flow bypasses the skill tool bug and provides consistent, automated execution of skill protocols.

## The Pattern

### When to Use

Use task delegation when:
- Creating Hugo blog posts
- Using specialized skills (hugo, chartjs, fabric, transcription, etc.)
- Any task requiring skill protocols and validation
- Complex workflows with multiple steps

### Delegation Template

Standard pattern for all skill-based tasks:

```json
{
  "subagent_type": "OpenAgent",
  "load_skills": ["skill-name"],
  "prompt": "Detailed task description here..."
}
```

### What This Does

1. **Task tool receives request** - Main agent identifies need for specialized skill
2. **Delegates to OpenAgent** - Universal coordinator accepts task with skills
3. **Loads skill context** - Skill instructions loaded from `/root/.opencode/skill/`
4. **Executes with protocols** - Follows skill-defined workflow
5. **Validates automatically** - Gateway checks run if required
6. **Reports completion** - Returns status and results

## Available Skills

Common skills and their uses:

| Skill | Purpose | When to Use |
|--------|-----------|--------------|
| hugo | Hugo blog posts, site management | "create blog post", "add post" |
| chartjs | Chart.js visualization creation | "create chart", "add graph" |
| fabric | Fabric pattern management | "use pattern", "extract insights" |
| transcription | YouTube transcript processing | "transcribe video", "YouTube URL" |
| maintenance | System monitoring and maintenance | "check system", "monitor" |
| news | News aggregation and analysis | "get news", "tech briefing" |
| ui-ux-pro-max | UI/UX design and styling | "design UI", "create component" |
| databases | Database management and queries | "query database", "manage data" |

## Global Rules Reference

**Key Source**: `/root/.config/opencode/agents.md`

The global agents.md file contains a delegation table that specifies:

| Domain | Delegate To | Load Skills | Trigger |
|--------|-------------|--------------|---------|
| Hugo blog posts | OpenAgent | ["hugo"] | "create blog post", "publish as blog post" |
| Documentation | OpenAgent | ["hugo"] | Documentation with Hugo integration |
| Hugo operations | OpenAgent | ["hugo"] | Theme management, site configuration |
| Architecture decisions | oracle | - | Multi-system tradeoffs, unfamiliar patterns |
| Self-review | oracle | - | After completing significant implementation |
| Frontend/UI | OpenFrontendSpecialist | - | UI/UX, design, styling |
| Complex logic | ultrabrain | - | Deep reasoning, architecture decisions |

**Why Global Rules**:
- Single source of truth
- Consistent across all projects
- Easy to update and maintain
- Clear delegation patterns documented
- Prevents drift and duplication

## Verification Flow

All skill-based tasks include automatic verification:

1. **Pre-flight checks** - Verify system ready
2. **Execution** - Run main task
3. **Post-creation validation** - Check outputs
4. **Gateway verification** (if applicable):
   - Navigate to URL with Agent Browser
   - Verify HTTP 200 status
   - Check content rendering
   - Take screenshot evidence
   - Document verification results
5. **Report** - Document results

## Example Workflows

### Example 1: Create Hugo Blog Post

**User**: "Create a blog post about X"

**Flow**:
1. Agent identifies: Need Hugo skill
2. Agent uses task tool:
   ```json
   {
     "subagent_type": "OpenAgent",
     "load_skills": ["hugo"],
     "prompt": "Create a blog post about X"
   }
   ```
3. OpenAgent loads hugo skill from `/root/.opencode/skill/hugo/SKILL.md`
4. Creates post with proper frontmatter (no H1 in body)
5. Verifies with Agent Browser
6. Takes screenshot
7. Reports completion

### Example 2: Extract YouTube Transcript

**User**: "Transcribe this YouTube video: [URL]"

**Flow**:
1. Agent identifies: Need transcription skill
2. Agent uses task tool:
   ```json
   {
     "subagent_type": "OpenAgent",
     "load_skills": ["transcription"],
     "prompt": "Transcribe YouTube video: [URL]"
   }
   ```
3. OpenAgent loads transcription skill
4. Extracts transcript using CLI or API
5. Stores in OpenMemory with tags
6. Saves to output folder

### Example 3: Use Fabric Pattern

**User**: "Extract insights from this text"

**Flow**:
1. Agent identifies: Need Fabric pattern
2. Agent uses task tool:
   ```json
   {
     "subagent_type": "OpenAgent",
     "load_skills": ["fabric"],
     "prompt": "Extract insights: [text]"
   }
   ```
3. OpenAgent loads fabric skill
4. Selects appropriate pattern (extract_insights)
5. Executes pattern via Fabric API
6. Returns formatted results

## Key Principles

1. **Never use skill tool** - It has a bug, use task delegation instead
2. **Always use task tool** - Delegate with load_skills parameter
3. **Follow global agents.md** - Use documented patterns
4. **Trust the flow** - Delegation handles all protocols automatically
5. **Verify results** - Gateway validation is automatic
6. **Project files extend, don't duplicate** - Keep global rules as source of truth

## Benefits

### Reliability
- ✅ Skill loading works every time (no bug impact)
- ✅ Complete protocol execution (frontmatter, validation, testing)
- ✅ Consistent behavior (global agents.md ensures uniformity)
- ✅ Easy maintenance (single source of truth)

### Automation
- ✅ Gateway verification enforced automatically
- ✅ Screenshots captured for evidence
- ✅ HTTP status checks performed
- ✅ Content rendering verified
- ✅ Results documented consistently

### Consistency
- ✅ Same delegation pattern across all skills
- ✅ Same verification process
- ✅ Same error handling
- ✅ Same reporting format

## The Complete Flow

```
User Request
    ↓
Agent Identifies Skill Need
    ↓
Agent Uses task Tool
    ↓
Delegates to OpenAgent with load_skills
    ↓
OpenAgent Loads Skill Context
    ↓
Executes Task with Skill Protocols
    ↓
Automatic Verification (if required)
    ↓
Reports Completion
    ↓
Done
```

## Summary

The new flow is simple and reliable:

1. **Identify need for skill** - Agent determines specialized capability required
2. **Use task tool to delegate** - Specify OpenAgent and skills to load
3. **Provide task prompt** - Detailed description of what to do
4. **OpenAgent handles the rest** - Loads skill, executes protocols, validates

This pattern works consistently across all skill-based tasks in OpenCode and has been thoroughly tested with Hugo blog post creation.

## Lessons Learned

1. **Tool bugs exist** - The skill tool returns numbers instead of skill names
2. **Workarounds are available** - Task delegation bypasses the bug entirely
3. **Documentation is critical** - Global agents.md provides single source of truth
4. **Automation is valuable** - Gateway validation ensures quality every time
5. **Testing confirms solutions** - Multiple test cases validate the approach
6. **Process matters more than tools** - The flow and delegation pattern are key

## Going Forward

This pattern is now:
- Documented in global agents.md
- Tested with multiple skills
- Verified with gateway validation
- Stored as reference for future use

When you need to use a specialized skill in OpenCode, always use task delegation with OpenAgent and specify the skills to load.