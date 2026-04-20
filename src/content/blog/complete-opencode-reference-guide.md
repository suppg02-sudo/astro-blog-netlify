---
pubDatetime: 2026-01-24T00:01:00Z
title: "Complete Reference Guide: My OpenCode Configuration, Aliases, Triggers, and Skills"
postSlug: "complete-opencode-reference-guide"
description: "Complete Reference Guide: My OpenCode Configuration, Aliases, Triggers, and Skills"
tags:
  - opencode
  - automation
  - documentation
  - reference
---

# Complete Reference Guide: My OpenCode Configuration

This guide serves as a comprehensive reference to my entire OpenCode environment, including shell aliases, trigger words, agent commands, response patterns, and skills.

---

## 🖥 Shell Aliases

### Bash Aliases
Located in `~/.bashrc`:

| Alias | Command | Purpose |
|--------|----------|---------|
| `oc` | `opencode` | OpenCode CLI shortcut |
| `ls` | `ls --color=auto` | Colorized directory listing |
| `grep` | `grep --color=auto` | Colorized grep output |
| `fgrep` | `fgrep --color=auto` | Colorized fixed string grep |
| `egrep` | `egrep --color=auto` | Colorized extended regex grep |
| `ll` | `ls -alF` | Detailed directory listing |
| `la` | `ls -A` | List all including hidden |
| `l` | `ls -CF` | Columnized directory listing |

### Environment Variables
- `OPENMEMORY_API_KEY`: OpenMemory authentication key
- `BUN_INSTALL`: Bun JavaScript runtime path
- `COMPOSIO_INSTALL_DIR`: Composio CLI installation directory
- `Z_AI_API_KEY`: Z.ai API key for AI models

---

## 🎯 Trigger Words & Commands

### Single-Word Triggers

| Trigger | Description |
|---------|-------------|
| **o** | Save most recent AI response to `/media/docs/output` as timestamped markdown file |
| **co** | Continue with current task or resume work |
| **memos** | Refers to Memos note-taking service or general notes/memories in OpenMemory |
| **todo** | Invoke todo skill for managing todo lists stored in OpenMemory with Memos synchronization |
| **mem** | Quick access to OpenMemory statistics (total count, sector breakdown, recent activity) |
| **c** | **containers** - Review all Docker containers and native system services status |
| **c7** | Use Context7 MCP server for additional context |
| **u** | Update instructions/documentation to reflect successful changes |
| **init** | Common OpenCode initialization command for project-specific setup |
| **api** | Use environment variable for z.ai API URL and key |
| **opencode.json** | Refers to OpenCode configuration file at `/root/.config/opencode/opencode.json` |
| **files** | Show subfolder structure and files in `/media` (excluding `/media/docker/folder` and `/media/docs/output`) |
| **smooth** | Fix and smooth out recent task for reliable future execution |
| **mem check** | Comprehensive memory system status check (usage, OOM, OpenMemory, monitoring) |
| **url** | Provide clickable URLs using Tailscale hostname format (`http://ubuntu58-1:<port>`) |
| **pw** | Test websites with Vercel Agent Browser (ALWAYS use this for front-end testing) |
| **clarity** | Ask clarifying questions about current task to ensure understanding |
| **advise** | Provide actionable advice on improvements, next steps, errors, design, strategy |
| **perf** | Serious review of recent performance history (disk I/O, network latency) |
| **commands** | List trigger words in global instructions file |
| **process check** | Run comprehensive process and system status check |
| **blog post** | Use Hugo skill for creating and managing blog posts |
| **skills** | Display available skill menu with descriptions and usage instructions |
| **cleanup** | Run safe automated disk space cleanup via `/root/scripts/disk-cleanup.sh` |
| **cron** | Generate comprehensive cron job status report with execution history |
| **opencodeskill** | Use opencodeskill for OpenCode configuration expertise |
| **apischeck** | Check all containers for available APIs, verify documentation, provide recommendations |
| **check** | Run comprehensive system check (OpenMemory, agent status, containers, resources, cron) |

### Context Triggers

| Trigger | Description |
|---------|-------------|
| **mem** (end of sentence) | Check your memory for topic mentioned in sentence |
| **remember** (end of sentence) | Make sure you save this to OpenMemory |
| **mem** (on its own) | Store user preferences, long prompts (>20 words), important decisions, successful procedures to OpenMemory |

### Review Triggers

| Trigger | Description |
|---------|-------------|
| **review weekly** | Run weekly storage quality review for agent and skill operations |
| **review monthly** | Run comprehensive monthly audit of storage quality with HTML report generation |
| **review quarterly** | Run strategic quarterly review for policy effectiveness assessment |

---

## 🤖 Agents

### Hugo Specialist Agent
**File**: `/root/.config/opencode/agent/hugo-specialist.md`

**Description**: Specialized Hugo static site management expert with theme expertise, Mermaid diagram support, and blog post workflow.

**Model**: GLM-4.7 Flash (zhipuai-coding-plan/glm-4.7-flash)

**Core Responsibilities**:
- Manage Hugo themes (list, install, activate, update)
- Create and manage blog posts with proper frontmatter
- Ensure Mermaid diagrams render correctly across all themes
- Test and verify Hugo site functionality
- Optimize content for SEO and performance
- Manage Hugo server operations (preview, build, deploy)

**Working Directory**: `/media/docker/website`

**Port**: 1314 (`http://ubuntu58-1:1314`)

**Preferred Subagent**: document-writer for blog content creation

---

### Mobile App Research Agent
**File**: `/root/.config/opencode/agent/mobile-app-research.md`

**Description**: Specialized agent for researching mobile apps, integrations, and workflow automation tools. Focus on iOS/iPhone and Android applications that enhance programming workflows.

**Core Competencies**:
- Mobile App Discovery (App Store, GitHub, developer platforms)
- Integration Research (API integrations, sync capabilities, connection methods)
- Workflow Analysis (practical use cases for developers and power users)
- Cross-Platform Focus (iOS/Android integration with macOS/Windows/Linux desktop)
- IDE Integration (remote control apps for VS Code, JetBrains, Cursor)
- AI Assistant Integration (ChatGPT, GitHub Copilot, Cursor companions)
- Terminal & SSH Apps (iOS clients, session persistence)
- Automation Frameworks (iOS Shortcuts, IFTTT, Zapier)
- Documentation Search (official docs, API references)
- User Reviews Analysis (Reddit, Product Hunt)
- Cost & Licensing Analysis (free, freemium, subscription models)

**Usage**: Invoke when researching mobile apps for development workflows, remote IDE control, terminal access, code snippet management.

---

## 🧩 Skills

### Core Skills

#### Hugo Skill
**File**: `/root/.config/opencode/skill/hugo/SKILL.md`

**Description**: Manage Hugo static site generator with theme management, Mermaid diagrams, and enhanced readability.

**Current Status**:
- **Container**: hugo_site (klakegg/hugo:ext-alpine)
- **Version**: v0.154.5 (Latest)
- **Working Directory**: `/media/docker/website`
- **Active Theme**: kit-main
- **Port**: 1314 (`http://ubuntu58-1:1314`)

**Capabilities**:
- Theme management (list, install, update, activate)
- Blog post creation with Mermaid diagram support
- Site preview and build operations
- SEO optimization
- Custom CSS styling and accessibility improvements

**MCP Tools Available**:
- `hugo-mcp_list_themes` - Browse Hugo themes
- `hugo-mcp_get_theme_details` - Get theme information
- `hugo-mcp_install_theme` - Install theme to site
- `hugo-mcp_update_theme` - Update installed theme
- `hugo-mcp_create_post` - Create new blog post
- `hugo-mcp_list_content` - List content in Hugo site
- `hugo-mcp_build_site` - Build for production
- `hugo-mcp_start_preview` - Start preview server
- `hugo-mcp_stop_preview` - Stop preview server

---

#### Agent Browser Skill
**File**: `/root/.config/opencode/skill/agent-browser/SKILL.md`

**Description**: Advanced browser automation with 95% success rate. Condenses site structures into interactive references for reliable agent interaction.

**Key Advantages**:
- **95% first-try success rate** (vs 80% for Playwright MCP)
- Reference-based navigation (uses `@ref:` prefix for clickable refs)
- Self-recovering with automatic retries
- Token efficient (sends condensed structure)
- Multi-engine support (Chromium, WebKit, Firefox)

**Usage**:
- **Navigation**: `open`, `back`, `forward`, `reload`
- **Interaction**: `click`, `type`, `fill`, `check`, `select`, `press`
- **Information**: `snapshot`, `get text`, `get html`, `get attribute`
- **State Checks**: `is visible`, `is enabled`, `is checked`
- **Screenshots**: `screenshot`, `pdf`
- **Session**: `connect`, `close`

**Critical**: **ALL web server and front-end testing MUST use Vercel Agent Browser** - never use curl or manual browsers.

---

#### Fabric Skill
**File**: `/root/.config/opencode/skill/fabric/SKILL.md`

**Description**: Fabric AI framework integration with pattern/strategy management, retrieval, and storage. Note: REST API provides pattern storage/retrieval - direct ZAI API required for pattern execution (port 8002).

**Architecture**:
- **REST API** (port 8085): Pattern storage, retrieval, management
- **ZAI API** (port 8002): Direct LLM execution using glm-4.7 model
- **Fabric CLI**: Available for low-level operations (not required for pattern execution)

**Current Status**:
- **Fabric API Container**: Running on port 8085
- **Web Interface**: `http://ubuntu58-1:8085`
- **Working Directory**: `/media/docker/fabric`
- **Available Patterns**: 233+ crowdsourced prompts

**Capabilities**:
- List all 233 available patterns
- Get pattern definitions and descriptions
- List 9 reasoning strategies (CoT, AoT, reflection, etc.)
- Store/retrieve custom patterns, sessions, and contexts
- **Skill Discovery**: Automatic intent detection using `find_skill` pattern
- Direct pattern execution via ZAI API (no Docker CLI overhead)

**Pattern Categories**:
- **Summarization**: 15+ patterns (summarize, summarize_paper, summarize_meeting)
- **Extraction**: 30+ patterns (extract_wisdom, extract_insights, extract_ideas)
- **Analysis**: 25+ patterns (analyze_claims, analyze_prose, analyze_paper)
- **Creation**: 40+ patterns (write_essay, write_micro_essay, create_blog_post)
- **Code**: 15+ patterns (explain_code, review_code, create_coding_feature)
- **Review**: 10+ patterns (review_code, review_design, rate_content)

**Reasoning Strategies**:
- `cot` - Chain of Thought (step-by-step reasoning)
- `aot` - Atom of Thought (break into sub-problems)
- `tot` - Tree of Thought (multiple reasoning paths)
- `ltm` - Least-to-Most (build from simple to hard)
- `reflexion` - Self-Critique (critique and refine)
- `self-refine` - Iterative Refine (initial → critique → improve)
- `standard` - Direct Answer (simple tasks)

**fabric-exec Script**: `/usr/local/bin/fabric-exec` - Direct API wrapper for pattern execution with streaming support, temperature control, and skill discovery integration.

---

#### OpenMemory Skill
**File**: `/root/.config/opencode/skill/openmemory/SKILL.md`

**Description**: Comprehensive OpenMemory management, configuration, troubleshooting, and optimization. Contains complete knowledge of OpenMemory's architecture, MCP integration, memory decay systems, cron jobs, API settings, agent history storage system.

**System Architecture**:
- **Backend**: Node.js/TypeScript application with Express server
- **Database**: SQLite with vector storage capabilities
- **Embedding Provider**: OpenAI text-embedding-3-small (256 dimensions)
- **Memory Sectors**: episodic, semantic, procedural, emotional, reflective

**Current Status**:
- **API Container**: `openmemory-openmemory-1` on port 8080
- **Dashboard Container**: `openmemory-dashboard-1` on port 3006
- **Database**: SQLite at `/data/openmemory.sqlite`
- **Data Volume**: `/media/docker/openmemory-data`

**MCP Tools Available**:
1. **`openmemory_query`** - Semantic retrieval (query, k, sector, min_salience, user_id)
2. **`openmemory_store`** - Persist new content (content, tags, metadata, user_id)
3. **`openmemory_reinforce`** - Boost salience for existing memory (id, boost)
4. **`openmemory_list`** - List recent memories (limit, sector, user_id)
5. **`openmemory_get`** - Fetch single memory by ID (id, include_vectors, user_id)

**Agent History Storage System**:
- **Episodic Sector**: Complete audit trail of all agent tool invocations
- **Procedural Sector**: Extracted procedures from repeated agent actions
- **Semantic Sector**: Lessons learned, patterns, insights from agent behavior
- **Automated Extraction**: Daily cron jobs for procedures and learning extraction

**Memory Decay System**:
- **Algorithm**: Exponential decay with λ = 0.02
- **Interval**: 1440 minutes (24 hours)
- **Decay Ratio**: 0.03 (3% decay per cycle)
- **Query Reinforcement**: Enabled (memories get salience boost when accessed)

**Dashboard**: `http://ubuntu58-1:3006`

---

### Additional Skills

#### Available Skills (30 Total)

| Skill | Description |
|--------|-------------|
| **hugo-mermaid-fix** | Hugo Mermaid diagram integration and fixes |
| **wordpress-management** | WordPress operations, content publishing, WP-CLI commands |
| **hugo-with-gates** | Hugo skill with gateway validation and completion gates |
| **glm-slide** | GLM-based presentation/slide generation |
| **portainer** | Docker container management via Portainer |
| **activepieces** | ActivePieces automation platform integration |
| **test-skill** | Testing framework and validation |
| **ui-ux-pro-max** | UI/UX design intelligence with 50 styles, 21 palettes |
| **filebrowser** | Web-based file manager and file operations |
| **affine** | Knowledge base and workspace management |
| **maintenance** | System monitoring, log analysis, performance optimization |
| **system-review** | System health checks and reviews |
| **skill-pattern-discoverer** | Discover and analyze skill patterns |
| **dokploy** | Application deployment, container orchestration |
| **databases** | PostgreSQL, MySQL, Redis, MongoDB management |
| **copyparty** | File server with indexing and search |
| **freya** | File synchronization and management |
| **copyparty-test** | Testing for Copyparty file server |
| **copyparty-copy** | CopyParty file operations and transfers |
| **mindsdb** | AI database and machine learning operations |
| **research** | Multi-source information gathering, evidence synthesis |
| **todo** | Todo list management with OpenMemory and Memos sync |
| **transcription** | YouTube/media transcription, audio processing |
| **openmemory-backup-restore** | OpenMemory database backup and restoration |
| **kavita** | Digital library management (comics, books, manga) |
| **memos** | Note-taking system, memo creation, tagging |
| **memorymanager** | Operational memory management, automated triggers |
| **advanced-research** | Deep research with multi-source validation |
| **ralph-loop-mine** | Self-referential development loop |
| **homarr** | Dashboard configuration and management |
| **crawl4ai** | AI-powered web crawling and extraction |
| **opencode** | OpenCode configuration and management |

---

## 📋 Response Patterns & What-To-Do Rules

### Memory Automation Protocol

**Automatic Storage Triggers** (store when ANY match):

1. **Long User Prompts** (>20 words): Store with tags `user-prompts, communication`
2. **Explicit "remember" Keyword**: Store content with tags `user-prompts, communication`
3. **User Preferences**: Phrases like "I prefer", "always use" → tag `preferences`
4. **Procedures/Workflows**: How-to content, step-by-step instructions → tag `procedural`
5. **Important Decisions**: "We decided", "I choose" → tag `semantic` with `decision=true` metadata
6. **Successful Procedures**: After complex task completion → tag `procedural` with `success=true` metadata
7. **User-Defined Patterns**: "Store this", "Save that" → explicit storage request

**Content Classification** (use appropriate sector):
- **Episodic**: Events, experiences, conversations, timestamps
- **Semantic**: Facts, knowledge, decisions, preferences, architecture choices
- **Procedural**: How-to workflows, procedures, installation steps, configuration guides
- **Emotional**: Strong feelings, moods, reactions
- **Reflective**: Insights, meta-cognition, learnings, pattern observations

**Implementation Rules**:
- **Don't Store**: Trivial acknowledgments (<5 words), routine commands (ls, pwd), failed attempts
- **Always Include**: User ID (`sisyphus`), descriptive tags, relevant metadata
- **Post-Task**: Reinforce successful procedures using `openmemory_reinforce`
- **Prevent Duplication**: Query similar memories before storing

---

### Browser Validation Protocol (CRITICAL)

**ALL web server and front-end testing MUST use Vercel Agent Browser.**

**When Testing Is Required**:
- Web server deployment
- Container restart
- Service configuration changes
- Front-end code changes
- API endpoint modifications
- Authentication flow updates

**Required Validation Workflow**:
1. **Pre-Validation**: Start frontend server, verify accessibility
2. **Snapshot Navigation**: Use Vercel Agent Browser to navigate and understand site structure
3. **Structure Analysis**: Run snapshot to get interactive references
4. **User Journey Testing**: Navigate through application using references from snapshot
5. **Artifact Collection**: Take screenshots at key validation points
6. **Error Detection**: Check for visual issues, broken elements, console errors
7. **Session Cleanup**: Always close browser session when validation complete

**No Exceptions**: There are no exceptions to this testing requirement. All web services must be verified with Vercel Agent Browser before being considered "deployed."

---

### Evidence-Based Research Guidelines

**CRITICAL**: When providing analysis, recommendations, or architectural guidance, ALWAYS verify claims with evidence and data BEFORE presenting conclusions.

**Required Verification Steps**:

1. **Search for Relevant Evidence**: Use `grep`, `read`, or `context7` to find actual data, code, or documentation
2. **Verify Data and Configurations**: Check actual file contents, database schemas, API responses
3. **Compare Claims vs Reality**: Document discrepancies between documentation and actual implementation
4. **Document Uncertainty**: Explicitly state when evidence is incomplete or conflicting
5. **Cite Sources**: Reference specific files, versions, or documentation sections
6. **Avoid Unverified Assumptions**: Do NOT assume configuration based on generic documentation

**Always Required For**:
- System analysis and troubleshooting
- Performance assessments
- Architecture recommendations
- Configuration changes
- Database/storage analysis
- Research into unfamiliar tools or libraries
- Security assessments

---

### Agent Constraints

#### OpenCode Process Restrictions (CRITICAL)

**NEVER restart OpenCode processes unless explicitly authorized by the user.**

**Prohibited Actions**:
- Do NOT restart any OpenCode server processes
- Do NOT restart processes on port 4096 (especially protected)
- Do NOT execute commands like: `kill <PID>`, `systemctl restart opencode`
- Do NOT modify OpenCode configuration that would trigger a restart
- Do NOT stop/start OpenCode services without explicit authorization

**Required Authorization**:
1. **STOP** and **ask for explicit confirmation**
2. **Explain exactly what operation** you're planning
3. **Wait for clear authorization** before proceeding
4. **Document reason** for restart in your response

**Exceptions**: Only when user explicitly commands or provides authorization, or system emergency.

---

#### Dangerous Command Restrictions (CRITICAL)

**NEVER execute destructive wildcard deletion commands.**

**Prohibited Actions**:
- Do NOT execute `rm -rf *` or similar wildcard deletion commands
- Do NOT execute `rm -rf /` or other recursive root deletions
- Do NOT execute destructive commands without explicit user confirmation

**Required Authorization**:
1. **STOP** and **ask for explicit confirmation**
2. **Verify current directory** and target of deletion
3. **List what would be deleted** and provide full path context
4. **Explain why deletion is needed** and what impact it will have
5. **Wait for clear authorization** before proceeding

---

#### Docker Cleanup Restrictions (CRITICAL)

**NEVER perform aggressive cleanup of Docker images under any circumstances.**

**Prohibited Actions**:
- Do NOT use `docker image prune -a` (removes all unused images)
- Do NOT use `docker system prune -a` (aggressive cleanup)
- Do NOT delete Docker images manually without explicit user authorization
- Do NOT remove images referenced by any containers

**Safe Cleanup Only**:
- Only use `/root/scripts/disk-cleanup.sh` for safe, selective cleanup
- Safe cleanup targets: Build cache, journal logs, APT cache, stopped containers without data

**Authorization Required**:
1. **STOP** and **ask for explicit confirmation**
2. **List** which images would be affected and why
3. **Verify** images are not referenced by any containers
4. **Wait for clear authorization** before proceeding

---

### Skill Delegation Protocol

**When invoking a skill, agent must trust the skill to complete its entire workflow.**

**Allowed Pattern**:
- Skill invocation itself constitutes authorization for workflow that skill defines
- Agent: Load skill → Wait for completion → Report completion to user

**Forbidden Pattern**:
- Do NOT use manual tools (bash, read, etc.) during skill execution
- Do NOT attempt to "help" skill by doing parts of its job
- Only intervene if skill reports error/timeout or user requests manual override

**Examples**:
- ✅ YouTube URL → Load transcription skill → Extract transcript → Store in OpenMemory → Ask for next action
- ✅ Database operation → Databases skill loads → Execute query/backup → Report results
- ❌ Load skill → Immediately use bash to download (VIOLATION)

---

### Background Task Management

**Background tasks must be managed efficiently without excessive polling.**

**Allowed Patterns**:
- ✅ Launch task → Continue with other work → Collect results once
- ✅ Launch multiple parallel tasks → Collect all results together
- ✅ Launch task → Work on other things → Check after X minutes

**Forbidden Patterns**:
- ❌ Launch task → Immediately poll output (within 10 seconds)
- ❌ Poll same task multiple times in single message
- ❌ Poll before task has time to complete

**Minimum Wait Time**: Wait **minimum 30 seconds** before first `background_output` call. Do not poll more than once per 60-second interval.

---

## 🔍 Verification & Quality Assurance

### Evidence Requirements

A task is complete when:

- ✅ File edit: `lsp_diagnostics` clean on changed files
- ✅ Build command: Exit code 0
- ✅ Test run: Pass (or explicit note of pre-existing failures)
- ✅ Delegation: Agent result received and verified

**NO EVIDENCE = NOT COMPLETE**

---

### Before Delivering Final Answer

- Cancel ALL running background tasks: `background_cancel(all=true)`
- This conserves resources and ensures clean workflow completion

---

## 📚 Quick Reference

### Essential URLs

| Service | URL | Purpose |
|---------|-----|---------|
| Hugo Site | http://ubuntu58-1:1314 | Static website |
| Fabric API | http://ubuntu58-1:8085 | AI pattern management |
| OpenMemory API | http://localhost:8080/mcp | Memory storage |
| OpenMemory Dashboard | http://ubuntu58-1:3006 | Memory visualization |
| Agent Dashboard | http://localhost:4096 | OpenCode interface |

### Common Commands

```bash
# Quick system check
check

# Memory statistics
mem

# Container status
c

# URL list
url

# Disk cleanup
cleanup

# Cron status
cron

# API documentation check
apischeck
```

### Todo Management

```bash
# List available skills
skills

# Blog post creation (triggers Hugo skill)
create a blog post

# Research topic
fabric research [topic]

# Use Fabric patterns
fabric [pattern_name]
```

---

## 📝 Summary

This comprehensive guide documents:

- **Shell Aliases**: 7 aliases for common operations (oc, ls, grep, ll, la, l)
- **Trigger Words**: 30+ single-word and context triggers (o, co, mem, c, u, init, check, etc.)
- **Agents**: 2 specialized agents (hugo-specialist, mobile-app-research)
- **Skills**: 30 skills covering Hugo, Fabric, OpenMemory, databases, WordPress, file management, and more
- **Response Patterns**: Memory automation protocols, browser validation rules, evidence-based research guidelines
- **Agent Constraints**: Process restrictions, dangerous command blocks, Docker cleanup rules

**Key Principles**:
- Evidence-based research (verify claims before presenting)
- Automatic memory storage for important interactions
- Vercel Agent Browser for all web testing (95% success rate)
- Safe, authorized operations only (no destructive commands without confirmation)
- Efficient background task management (minimum 30s wait time)

**Last Updated**: 2026-01-24
**Environment**: Ubuntu with Docker, OpenCode, and 67+ containerized services