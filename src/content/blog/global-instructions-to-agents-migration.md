---
pubDatetime: 2026-01-24T20:07:24Z
title: "Global Instructions to Agents.md Migration - Clean Separation of Concerns"
postSlug: "global-instructions-to-agents-migration"
description: "Analysis of major restructuring to achieve cleaner separation of concerns between system-level protocols and agent behavioral rules"
tags:
  - global-instructions.md
  - migration
  - documentation
  - architecture
  - agents.md
---

**Date**: January 24, 2026
**Type**: Restructuring Analysis

## Executive Summary

Successfully completed a major restructuring of OpenCode's instruction system to achieve cleaner separation of concerns between:
- **System-level protocols** (core rules, infrastructure) → \`global-instructions.md\`
- **Agent behavioral rules** (how agents work, triggers, constraints) → \`agents.md\`

This migration reduces \`global-instructions.md\` from **1,541 lines to 286 lines** (81% reduction) while creating a focused 505-line agent behavior file.

## The Problem

Before this migration, \`global-instructions.md\` contained both:
1. **Infrastructure documentation** (system paths, directories, containers, ports)
2. **Agent behavioral protocols** (triggers, validation, constraints)

This created several issues:
- **File bloat**: Single file trying to be everything for everyone (1,541 lines)
- **Maintainability burden**: Updating agent behaviors required editing core infrastructure file
- **Confusion**: Behavioral rules buried deep in PART 4 of a 1,541-line file
- **Circular dependencies**: Core rules referenced agent behaviors, agent behaviors referenced core rules

## The Solution

### New File Structure

Created \`/root/.config/opencode/agents.md\` (505 lines) containing:

- **Behavioral Protocols**: Evidence-based research, verification steps, research prioritization
- **Command Reference**: All trigger words (o, co, memos, todo, mem, c, c7, u, init, api, files, smooth, mem check, url, pw, clarity, advise, perf, commands, process check, blog post, skills, cleanup, cron, opencodeskill, apischeck, check)
- **Context Triggers**: Memory automation, reviews (weekly/monthly/quarterly)
- **Testing Protocols**: Mandatory browser testing (Vercel Agent Browser), agent constraints
- **Agent Constraints**: OpenCode process restrictions, dangerous commands, Docker cleanup

### Updated \`global-instructions.md\` (286 lines) containing:

- **PART 1**: Core Protocols (kept) - Skill/pattern creation, memory reading, file output, global rules, OpenMemory usage
- **PART 2**: Removed - Now contains reference: "For behavioral protocols, trigger word reference, and agent constraints, refer to agents.md file"
- **PART 3**: Removed - Now contains reference: "For complete trigger word reference, command behaviors, and memory automation triggers, refer to agents.md file"
- **PART 4**: Infrastructure Reference - Simplified to remove behavioral constraint sections (now contains AGENTS.md update protocol, OpenCode log locations, key directories)
- **PART 5**: Domain-Specific Protocols (kept) - Container management, port management, deployment protocols