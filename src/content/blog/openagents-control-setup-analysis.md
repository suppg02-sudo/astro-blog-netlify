---
pubDatetime: 2026-02-01T00:03:00Z
title: "OpenCode Agents Setup Analysis: Is Your OpenAgentsControl Fully Configured?"
postSlug: "openagents-control-setup-analysis"
description: "OpenCode Agents Setup Analysis: Is Your OpenAgentsControl Fully Configured?"
tags:
  - research
  - openagents
---

# OpenCode Agents Setup Analysis: Is Your OpenAgentsControl Fully Configured?

## Executive Summary

**Installation Status**: ⚠️ **PARTIAL / CUSTOM INSTALLATION**

Your OpenCode agents setup is **NOT fully configured according to OpenAgentsControl documentation**. While you have the core infrastructure in place, critical components are missing that prevent proper agent functionality.

## What You Have vs. What You Need

### ✅ What's Working
- OpenAgentsControl repository cloned and current (v0.5.2)
- Basic agent structure installed in `/root/.opencode/agent/`
- Core agents and most specialist agents present
- All 16 subagents installed correctly

### ❌ What's Missing (Critical)
1. **Context Files** - COMPLETELY ABSENT
   - Agents cannot access coding standards, patterns, or workflows
   - Required for: Agent decision-making, consistency, quality

2. **Profile Tracking** - NO RECORD
   - No installation record for upgrades
   - No way to verify which profile (Essential, Developer, Business, Full, Advanced) is active

3. **Proper Agent Registration**
   - Custom configuration conflicts with OpenAgentsControl conventions
   - Agents not discoverable through standard mechanisms

## Installation Structure Analysis

### Repository Status
```
/media/docker/OpenAgentsControl/  ✅ Cloned, up-to-date (v0.5.2)
  ├── .opencode/                    ✅ Agent source files present
  │   ├── agent/                     ✅ 10 categories defined
  │   ├── command/                   ✅ Commands defined
  │   ├── context/                   ✅ Context files present
  │   ├── profiles/                  ✅ Profiles defined (5 profiles)
  │   ├── skill/                     ✅ Skills integration
  │   ├── tool/                     ✅ Tools present
  │   └── plugin/                   ✅ Plugin structure
  ├── install.sh                     ✅ Installer present (v1.0.0)
  ├── registry.json                  ✅ Full component registry
  └── package.json                  ✅ Package configuration
```

## Primary Agents Status

| Agent | Status | Purpose |
|--------|---------|----------|
| **OpenAgent** | ✅ Installed | Core universal coordinator |
| **OpenCoder** | ✅ Installed | Development specialist |
| **OpenCodebaseAgent** | ✅ Installed | Multi-language support |
| **OpenBackendSpecialist** | ✅ Installed | Backend/API specialist |
| **OpenFrontendSpecialist** | ✅ Installed | Frontend/UI specialist |
| **OpenDevopsSpecialist** | ✅ Installed | DevOps/infrastructure |
| **OpenTechnicalWriter** | ✅ Installed | Documentation specialist |
| **OpenCopywriter** | ✅ Installed | Marketing copy specialist |
| **OpenDataAnalyst** | ✅ Installed | Data analysis specialist |
| **OpenSystemBuilder** | ⚠️ Partial | Meta agent for system generation |
| **OpenRepoManager** | ✅ Installed | Repository management |
| **Eval Runner** | ✅ Installed | Test evaluation |

**Result**: 9 of 12 primary agents installed (75%)

## Subagents Status ✅

All 16 subagents are present and correctly installed:

- **Core**: TaskManager, ContextScout, Context Retriever, Documentation
- **Code**: CoderAgent, CodeReviewer, TestEngineer, BuildAgent, PatternAnalyst
- **System Builder**: DomainAnalyzer, AgentGenerator, ContextOrganizer, WorkflowDesigner, CommandCreator
- **Utils**: ImageSpecialist
- **Test**: SimpleResponder

## Profile Compliance Analysis

### Essential Profile
**Expected**: 12 components (1 agent + 3 subagents + 6 commands + 1 tool + 11 context files)

**Installed**: 2/12 components (17% compliance)

```
✅ agent:openagent              (Installed)
✅ subagent:task-manager        (Installed)
❌ subagent:contextscout         (MISSING - exists but not profile-tracked)
❌ subagent:documentation         (MISSING - exists but not profile-tracked)
❌ skill:task-management         (MISSING)
❌ command:context, clean, etc.  (EXISTS but not profile-linked)
❌ tool:env                     (MISSING)
❌ context:essential-patterns, etc. (ALL MISSING - 0/11 files)
```

### Developer Profile (Recommended)
**Expected**: 33 components (6 agents + 5 subagents + 7 commands + 1 tool + 14 context files + 2 configs)

**Installed**: Partial installation (agents present, but dependencies missing)

**Compliance**: ~6/33 components (18%) - agents present but context files, tools, and profile tracking missing

## Configuration Issues

### 1. oh-my-opencode.json Configuration Conflict

**Current Configuration** uses legacy agent names:
- `sisyphus` (should be `OpenAgent`)
- `oracle` (should be `OpenCoder`)
- `librarian` (should be `OpenCodebaseAgent`)
- `explore` (not a standard OpenAgentsControl agent)

**Issue**: Custom configuration conflicts with OpenAgentsControl naming conventions and prevents proper agent discovery.

### 2. No Agent Registration in opencode.json

**File**: `/root/.config/opencode/opencode.json`

**Issue**: No agent configuration present. OpenAgentsControl agents should be discoverable and selectable through OpenCode's agent selection system.

### 3. Missing Profile Tracking

**Issue**: No installation record for which profile was installed. This creates maintenance difficulties and no clear upgrade path.

## Impact Assessment

### High Risk 🚨
**Missing context files** means agents cannot:
- Access coding standards and patterns
- Load workflow definitions
- Apply consistent architectural decisions
- Maintain code quality standards

### Medium Risk ⚠️
- **No profile tracking** makes upgrades difficult
- **Configuration conflicts** may cause agent selection failures
- **Missing tools** reduce agent capabilities

### Low Risk
- **Product & Learning agents** have incomplete structure but aren't critical for day-to-day operation

## Recommended Fix

### Step 1: Clean Reinstall with Profile

```bash
cd /media/docker/OpenAgentsControl

# Option A: Reinstall with Developer profile (RECOMMENDED)
./install.sh developer --install-dir /root/.opencode

# Option B: Reinstall with Full profile
./install.sh full --install-dir /root/.opencode

# Option C: Interactive mode to choose components
./install.sh
```

**Why**: This ensures all dependencies, context files, commands, and tools are properly installed and profile-tracked.

### Step 2: Validate Installation

After reinstall, run validation:

```bash
# Check all agents are present
find /root/.opencode/agent -name "*.md" -type f | wc -l  # Should be ~30+ files

# Check context files are present
find /root/.opencode/context -name "*.md" -type f | wc -l  # Should be ~50+ files

# Verify profile components
cat /root/.opencode/profile.json  # Should show installed profile
```

### Step 3: Update Configuration

Clean up `oh-my-opencode.json`:
```bash
# Backup current config
cp /root/.config/opencode/oh-my-opencode.json \
   /root/.config/opencode/oh-my-opencode.json.backup-$(date +%Y%m%d)

# Remove conflicting custom agent definitions
# Let OpenAgentsControl manage agent registration
```

### Step 4: Test Agent Access

```bash
# Verify agents are discoverable in OpenCode
cd /media/docker  # Test from project directory

# Test specific agent invocation (when available)
opencode --agent OpenAgent
opencode --agent OpenCoder
```

## Expected Results After Fix

### Essential Profile (Minimal)
| Component Type | Expected | Current | After Fix |
|---------------|----------|---------|------------|
| Primary Agents | 1 | 1 | ✅ 1 |
| Subagents | 3 | 4+ | ✅ 3 (tracked) |
| Skills | 1 | 0 | ✅ 1 |
| Commands | 6 | 7 | ✅ 6 (tracked) |
| Tools | 1 | 0 | ✅ 1 |
| Context Files | 11 | 0 | ✅ 11 |
| Configs | 1 | 0 | ✅ 1 |

**Target Compliance**: 12/12 components (100%)

### Developer Profile (Recommended)
| Component Type | Expected | Current | After Fix |
|---------------|----------|---------|------------|
| Primary Agents | 6 | 9 | ✅ 6 |
| Subagents | 5 | 16 | ✅ 5 |
| Skills | 1 | 0 | ✅ 1 |
| Commands | 7 | 7 | ✅ 7 (tracked) |
| Tools | 1 | 0 | ✅ 1 |
| Context Files | 14 | 0 | ✅ 14 |
| Configs | 2 | 0 | ✅ 2 |

**Target Compliance**: 33/33 components (100%)

## Summary

### Current State
- ✅ OpenAgentsControl repository present and current
- ✅ Core agent infrastructure in place
- ✅ Most primary agents installed (9/12)
- ✅ All subagents present (16/16)
- ❌ **CRITICAL**: No context files (0/25)
- ❌ **CRITICAL**: No profile tracking
- ❌ **HIGH**: Configuration conflicts
- ❌ **MEDIUM**: Missing tools and skill integration

### What's at Risk
Without context files, agents cannot:
- Apply coding standards consistently
- Follow architectural patterns
- Access workflow definitions
- Make informed decisions about code quality

### Next Steps
1. **Priority 1**: Reinstall OpenAgentsControl with Developer profile
2. **Priority 2**: Validate context files are installed and accessible
3. **Priority 3**: Clean up oh-my-opencode.json configuration
4. **Priority 4**: Test agent invocation and delegation workflows
5. **Priority 5**: Update global instructions with correct agent names

---

**Analysis Date**: February 1, 2026
**OpenAgentsControl Version**: 0.5.2
**Analysis Method**: File structure inspection, registry comparison, profile compliance checking