---
pubDatetime: 2026-02-11T19:30:00Z
title: "Complete Trigger Commands Reference Guide"
postSlug: "trigger-commands-reference"
description: "Complete numbered list and detailed reference guide for all 39 trigger commands and keywords used in the Claude Code system for efficient workflow management."
tags:
  - productivity
  - commands
  - workflow
  - claude-code
  - reference
---

## Introduction

This comprehensive reference guide documents all **39 trigger commands** available in your Claude Code system. These trigger words provide quick shortcuts for common tasks, system operations, and workflow management. Learn how to use each command effectively for maximum productivity.

---

## Quick Command Summary

| # | Command | Category | Purpose |
|---|---------|----------|---------|
| 1 | **o** | File Management | Save document to /media/docs/output |
| 2 | **a** | Validation | Check with agent browser (Hugo blog) |
| 3 | **co** | Workflow | Continue with current task |
| 4 | **gr** | Reference | Refer to global rules documentation |
| 5 | **c** / **containers** | System | Review containers and web services |
| 6 | **c7** | Context | Use context7 MCP server |
| 7 | **u** | Documentation | Update instructions for successful changes |
| 8 | **/init** / **init** | Setup | OpenCode initialization |
| 9 | **api** | Configuration | Use z.ai environment variables |
| 10 | **opencode.json** / **global config** | Configuration | Reference OpenCode config file |
| 11 | **files** | File System | Show /media subfolder structure |
| 12 | **smooth** | Protocol | Execute Smooth Protocol |
| 13 | **mem check** / **memory** | System | Memory system status check |
| 14 | **openmemory backup analysis** | Memory | Database backup analysis |
| 15 | **system verification** | Memory | OpenMemory status verification |
| 16 | **check** | System | Comprehensive system check |
| 17 | **mem** (at end) | Memory | Check memory for topic |
| 18 | **remember** | Memory | Save to OpenMemory |
| 19 | **review weekly** | Analytics | Weekly storage quality review |
| 20 | **review monthly** | Analytics | Monthly audit of storage |
| 21 | **review quarterly** | Analytics | Quarterly strategic review |
| 22 | **clarity** | Task Planning | Ask clarifying questions |
| 23 | **advise** / **advice** | Guidance | Provide advice on improvements |
| 24 | **menu** / **m** | Navigation | Access menu management system |
| 25 | **checkpoint** / **ch** | Backup | Interactive checkpoint management |
| 26 | **perf** | Performance | Review performance history |
| 27 | **commands** | Reference | List trigger words |
| 28 | **process check** | System | Process and system status |
| 29 | **skills** | Skill Management | Display available skills menu |
| 30 | **skill** / **skills** | Skill Management | Interactive skill options |
| 31 | **cleanup** | Maintenance | Run disk space cleanup |
| 32 | **cron** | Scheduling | Generate cron job status |
| 33 | **git** | Backup | Load git-backup-strategy skill |
| 34 | **memo** / **memos** / **todo** | Task Management | Manage memos and todos |
| 35 | **research** / **r** | Research | Start Deep-Research agent |
| 36 | **opencodeskill** | Configuration | OpenCode expertise reference |
| 37 | **apischeck** / **apis check** | API Management | Check container APIs |
| 38 | **versions** | Version Control | Check git backup versions |
| 39 | **YouTube URL** | Content Creation | Execute YouTube workflow |

---

## Detailed Command Reference

### File & Document Management

#### **o** - Save to Output
- **Usage**: Use at end of session or when creating documents
- **Function**: Saves all content as markdown file to `/media/docs/output`
- **When to use**: After creating scripts, documents, or completing tasks
- **Example**: Create document → "o" → file saved to output directory

---

### Validation & Testing

#### **a** - Agent Browser Check
- **Usage**: Type "a" on its own
- **Function**: Opens agent browser session and navigates to Hugo blog (http://ubuntu58-1:1314)
- **Validates**: 
  - Blog functionality
  - Content rendering
  - Hugo build status
- **Output**: Screenshot and page content report

---

### Workflow Control

#### **co** - Continue Task
- **Usage**: Type "co" when pausing work
- **Function**: Resume current task or work in progress
- **Equivalent**: Saying "carry on"
- **Use case**: When you want to continue after interruption

---

### Reference & Documentation

#### **gr** - Global Rules
- **Usage**: Type "gr" when referencing global rules
- **Points to**: `/media/docs/instructions/global-instructions.md`
- **Contains**: All system-wide rules, protocols, and guidelines
- **Use case**: When you need to understand system policies

#### **commands** - List All Triggers
- **Usage**: Type "commands" to see trigger words
- **Function**: Lists all available trigger words from global rules
- **Output**: Complete list with descriptions

---

### System Operations

#### **c** or **containers** - Container Review
- **Usage**: Type "c" or "containers" on its own
- **Function**: Comprehensive container and system service review
- **Reports**:
  1. Docker Container Summary (by category)
  2. Native System Services
  3. Statistics (totals, health status)
  4. Quick Access Links
  5. Issues Summary with recommendations
- **Output**: Formatted tables with status indicators

#### **check** - Comprehensive System Check
- **Usage**: Type "check" on its own
- **Components Checked**:
  - OpenMemory MCP status
  - Oh-My-OpenCode agent/skill status
  - Container status (stopped/failed)
  - Docker monitoring services
  - Disk space remaining
  - CPU load average (5-min)
  - Memory usage breakdown
  - Kernel memory settings
  - Monitoring log status
  - OOM killer activity
- **Output**: Organized sections with assessment and recommendations

#### **process check** - Process & System Status
- **Usage**: Type "process check" on its own
- **Function**: Run comprehensive process status check
- **Includes**: System-wide process information and resource allocation

---

### Context & Research

#### **c7** - Context7 MCP Server
- **Usage**: Type "c7" when needing additional context
- **Function**: Use context7 MCP server for knowledge lookup
- **Best for**: Code examples, library documentation, technical references

#### **research** or **r** - Deep-Research Agent
- **Usage**: 
  - Standalone: "research" → prompts "What would you like to research?"
  - With topic: "research [topic]" → asks if you want to use Deep-Research agent
- **Function**: Activate Deep-Research agent for comprehensive research
- **Outputs**:
  1. Research findings
  2. Blog post creation
  3. OpenMemory storage of summary
- **URL**: Published blog post at http://ubuntu58-1:1314/posts/[slug]/

---

### Memory & Knowledge Management

#### **mem** - Check Memory
- **Usage**: Add "mem" at end of sentence
- **Example**: "Tell me about Docker mem" → checks memory for Docker topics
- **Function**: Retrieve relevant memories from OpenMemory for topic

#### **remember** - Save to Memory
- **Usage**: Type "remember" at start or end
- **Function**: Save important information to OpenMemory
- **Stored with**: Tags and metadata for future retrieval

#### **mem check** or **memory** - Memory Status
- **Usage**: Type "mem check" or "memory" on its own
- **Reports**:
  1. Current memory usage (free -h)
  2. System load (uptime)
  3. OOM killer messages
  4. Memory statistics
  5. Top memory-consuming processes
  6. Docker monitoring services
  7. OpenMemory database size
  8. Kernel memory settings
  9. Monitoring log status
  10. OOM-related journal entries
  11. Assessment and recommendations

#### **openmemory backup analysis** - Database Backup
- **Usage**: Trigger after backup operations
- **Reports**: Database size, memory count, sector distribution, WAL checkpoint status

#### **system verification** - Memory Verification
- **Usage**: Verify OpenMemory system status
- **Checks**: Database integrity, storage/retrieval mechanisms, checkpoint status

---

### Analytics & Reviews

#### **review weekly** - Weekly Quality Review
- **Usage**: Type "review weekly" on its own
- **Function**: Run weekly storage quality review
- **Checks**: Tag compliance, dual storage validation, granularity adherence
- **Output**: Console report + OpenMemory storage

#### **review monthly** - Monthly Audit
- **Usage**: Type "review monthly" on its own
- **Function**: Comprehensive monthly audit of storage quality
- **Includes**: Policy compliance, agent performance metrics
- **Output**: Console report + HTML file + OpenMemory

#### **review quarterly** - Quarterly Strategic Review
- **Usage**: Type "review quarterly" on its own
- **Function**: Strategic quarterly review
- **Analyzes**: Policy effectiveness, emerging patterns
- **Output**: Console report + Strategic plan MD + OpenMemory

#### **perf** - Performance Review
- **Usage**: Type "perf" on its own
- **Function**: Review recent performance history
- **Metrics**: Disk I/O stats, network latency (gateway + 8.8.8.8)
- **Focus**: Last hour of activity

---

### Configuration & Setup

#### **/init** or **init** - Initialize Project
- **Usage**: Type "/init" or "init" on its own
- **Function**: OpenCode initialization for project-specific setup
- **Creates**: agents.md file with project instructions
- **Use**: When starting new projects or setting up configurations

#### **api** - Z.ai Environment
- **Usage**: Type "api" when needing API credentials
- **Function**: Access z.ai environment variables (URL and API key)
- **Use case**: When working with API integrations

#### **opencode.json** or **global config** - Config Reference
- **Usage**: Reference when discussing configuration
- **Points to**: `[config directory]`
- **Contains**: OpenCode system configuration

#### **u** - Update Instructions
- **Usage**: Type "u" after successful changes
- **Function**: Update documentation/instructions to reflect changes
- **Triggers**: Automatic documentation update for successful operations

---

### File System Navigation

#### **files** - Media Directory Structure
- **Usage**: Type "files" on its own
- **Function**: Show subfolder structure and files in /media
- **Excludes**: /media/docker and /media/docs/output
- **Output**: Organized directory tree view

---

### Protocols & Workflows

#### **smooth** - Smooth Protocol
- **Usage**: Type "smooth" on its own
- **Function**: Load and execute Smooth Protocol
- **Workflow**:
  1. Analyze recent task
  2. Present improvements
  3. Implement changes
  4. Run 3+ test cycles
  5. Document everything
- **Source**: `/media/docs/instructions/smooth.md`
- **Goal**: Production-ready workflow optimization

---

### Task Planning

#### **clarity** - Ask Clarifying Questions
- **Usage**: Type "clarity" on its own
- **Function**: Ask clarifying questions about current task
- **When to use**: When requirements are unclear before proceeding

#### **advise** or **advice** - Get Advice
- **Usage**: Type "advise" or "advice" on its own
- **Provides**:
  1. **Improvements**: Suggestions for current work/code/configuration
  2. **Next Steps**: Recommended actions and priorities
  3. **Errors**: Highlight issues and problems
  4. **Design**: Design recommendations and architecture
  5. **Strategy**: Strategic advice and long-term recommendations

---

### Menu & Navigation

#### **menu** or **m** - Menu Manager
- **Usage**: Type "menu" or "m" on its own
- **Features**:
  - **Level 1**: Main menu with pagination (6 items per screen)
  - **Level 2**: Smart discovery (recent items first)
  - **Level 3**: Complete listing with sorting
- **Smart Ordering**: Recent first → Most used → Trending
- **Auto-Tracking**: Registry at `[config directory]`
- **Add Option**: Add custom menu items with suggestions

#### **checkpoint** or **ch** - Checkpoint Management
- **Usage**: Type "checkpoint" or "ch" on its own
- **Options**:
  1. Create new checkpoint (recommended)
  2. Analyze previous checkpoint
  3. Restore from checkpoint
  4. Generate flow analysis
  5. Create blog post
  6. Compare checkpoints
  7. List all checkpoints
  8. Export checkpoint report
  9. Sync to git backup
  10. Cancel
- **Archives**: Patterns, scripts, global rules, MCP servers
- **Output**: Organized backup with documentation

---

### Skill Management

#### **skills** - Skill Menu
- **Usage**: Type "skills" on its own
- **Function**: Display available skill menu with descriptions
- **Discovery**: Fast method using ls + batch read of SKILL.md files
- **Output**: Complete skill list with usage instructions

#### **skill** or **skills** - Interactive Skill Selection
- **Usage**: Type "skill" or "skills" on its own
- **Function**: Present interactive skill options using question tool
- **Reference**: `/media/docs/instructions/skillmenu.md` for full behavior

---

### Maintenance & Operations

#### **cleanup** - Disk Space Cleanup
- **Usage**: Type "cleanup" on its own
- **Function**: Run safe automated disk space cleanup
- **Cleans**:
  - Docker images
  - Build cache
  - Journal logs
  - APT cache
  - Optional: node_modules directories (with confirmation)
- **Output**: Before/after disk usage, action log
- **Log**: `[system logs]`

#### **cron** - Cron Job Status
- **Usage**: Type "cron" on its own
- **Function**: Generate comprehensive cron job status report
- **Reports**: All scheduled tasks, last execution time, success/failure status
- **Output**: Markdown report saved to `[system logs]`

---

### Backup & Version Control

#### **git** - Git Backup Strategy
- **Usage**: Type "git" on its own
- **Function**: Load git-backup-strategy skill
- **Covers**:
  - Comprehensive backup management
  - Restore procedures
  - Automation setup
  - 4 repositories (stuff, hugo-blog, memos-backup, opencode-skills)
  - GitHub account: suppg02-sudo
- **Skill Location**: `[config directory]`

#### **versions** - Git Backup Versions
- **Usage**: Type "versions" on its own
- **Function**: Check git backup versions for configuration files
- **Files**: Global instructions (gr), flow.md, smooth.md, global agents.md
- **Output**: Recent backups with commit hashes, dates, timestamps, restoration instructions

#### **apischeck** or **apis check** - API Verification
- **Usage**: Type "apischeck" or "apis check" on its own
- **Function**: Check all containers for available APIs
- **Reference**: `/media/docs/instructions/apischeck.md`
- **Verifies**: Existing API documentation and provides recommendations

---

### Task Management

#### **memo** or **memos** or **todo** - Memo Management
- **Usage**: 
  - Standalone: Present Memos skill interface
  - Part of conversation: "create a memo about X", "show my todos"
- **Function**: Manage memos, todos, and goals
- **Mandatory**: Load skill from `[config directory]` first
- **Helper Scripts**: memos-auth.sh, memos-create.sh, memos-update.sh
- **Uses**: Never bypass with direct API calls

---

### Configuration Expertise

#### **opencodeskill** - OpenCode Configuration
- **Usage**: Type "opencodeskill" on its own
- **Function**: Reference for OpenCode configuration expertise
- **Includes**: Skills, agents, MCP servers, oh-my-opencode plugin setup

---

### Content Creation

#### **YouTube URL** - YouTube Workflow
- **Usage**: Paste any YouTube URL (formats: youtube.com/watch?v=ID, youtu.be/ID, youtube.com/embed/ID)
- **Function**: Automatically execute complete YouTube workflow
- **5 Mandatory Phases**:
  1. **Phase 1**: Transcript Extraction
  2. **Phase 1B**: Transcript Validation
  3. **Phase 2**: Comprehensive Summary
  4. **Phase 3**: Short Summary
  5. **Phase 4**: Blog Post Creation
- **Post-Processing**: Optional (PDF, DOCX, condensed version, favorites)
- **Output**: Published blog post at http://ubuntu58-1:1314/posts/[slug]/

---

## Command Categories Overview

### 📋 System & Monitoring (8 commands)
- check, c/containers, mem check, process check, perf, system verification, openmemory backup analysis

### 🧠 Memory & Knowledge (5 commands)
- mem, remember, review weekly, review monthly, review quarterly

### 📚 Reference & Documentation (5 commands)
- gr, commands, c7, versions, apischeck

### ⚙️ Configuration & Setup (4 commands)
- /init, api, opencode.json, opencodeskill

### 💾 File & Backup Management (3 commands)
- o, files, git

### 🎯 Task Management & Guidance (3 commands)
- clarity, advise, u

### 🎬 Workflow & Navigation (5 commands)
- co, smooth, menu, checkpoint, skills

### 🔧 Maintenance & Operations (2 commands)
- cleanup, cron

### 🔍 Research & Content (3 commands)
- research/r, YouTube URL, memo/memos/todo

### ✅ Validation & Testing (1 command)
- a

---

## Best Practices for Using Trigger Commands

### 1. **Session Workflow**
- Start with **check** for system status
- Use **clarity** if task requirements are unclear
- Execute main tasks with relevant commands
- End with **o** to save outputs

### 2. **Memory Management**
- Use **remember** for important decisions
- Use **mem** to retrieve relevant context
- Regular **review weekly/monthly/quarterly** for storage health

### 3. **Development Workflow**
- Start with **/init** for new projects
- Use **skills** to find right tools
- Use **research** for complex topics
- Use **menu** for quick navigation

### 4. **Performance & Maintenance**
- Run **perf** to monitor system performance
- Run **cleanup** when disk space is low
- Use **cron** to verify scheduled tasks

### 5. **Content Creation**
- Use **YouTube URL** for video content
- Use **memo/memos** for idea capture
- Use **checkpoint** to save work progress

### 6. **Documentation**
- Use **u** to update docs after changes
- Use **gr** to reference system rules
- Use **commands** to see available shortcuts

---

## Key Takeaways

✅ **39 total trigger commands** available for efficient workflow management  
✅ **Organized by category** for easy discovery and learning  
✅ **Quick shortcuts** for common operations and tasks  
✅ **System integration** with OpenMemory, OpenCode, and Hugo  
✅ **Automation support** for complex multi-phase workflows  
✅ **Customizable menu system** for personalized workflows  

Keep this reference guide handy for quick command lookup and maximum productivity!

---

**Last Updated**: 2026-02-11  
**Command Count**: 39 triggers and keywords  
**Categories**: 10 main categories  
**Skill Integration**: Full OpenCode skill ecosystem integration