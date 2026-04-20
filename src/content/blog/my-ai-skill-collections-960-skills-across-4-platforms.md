---
pubDatetime: 2026-02-03T00:00:00Z
title: "My AI Skill Collections: 960+ Skills Across 4 Platforms"
postSlug: "my-ai-skill-collections-960-skills-across-4-platforms"
description: "My AI Skill Collections: 960+ Skills Across 4 Platforms"
tags:
  - skills
  - openagents
  - automation
  - tools
---

As I continue building my AI infrastructure, I've accumulated an impressive collection of skills, patterns, and agent capabilities across multiple platforms. Here's a comprehensive overview of what I'm working with.

## Overview

**Total Skills**: 960+ across 4 major platforms

| Platform | Skills | Type | Status |
|-----------|---------|------|--------|
| OpenCode | 39 | Agent skills | Active |
| Fabric | 200+ | Content patterns | Active |
| OpenClaw | 672 | Agent skills | Downloaded |
| Docker Projects | 50+ | Project-specific | Scattered |

---

## 1. OpenCode Skills (39 Skills)

**Location**: `/root/.opencode/skill/`

OpenCode skills are automatically available to all agents and provide specialized domain knowledge.

### Production-Ready Skills

**`openmemory`** ⭐⭐⭐⭐ (95% Maturity)
- **Description**: Comprehensive OpenMemory management, configuration, troubleshooting, and optimization
- **Use For**: System architecture, MCP integration, memory decay configuration

**`opencode`** ⭐⭐⭐⭐ (98% Maturity)
- **Description**: OpenCode configuration, agents, skills, and plugin setup
- **Use For**: Configuration management, agent setup, skill development

**`research`** ⭐⭐⭐⭐⭐ (95% Maturity)
- **Description**: Enterprise-grade research methodology with evidence-based synthesis
- **Use For**: Technical research, documentation gathering, source validation

**`homarr`** ⭐⭐⭐⭐ (90% Maturity)
- **Description**: Homarr dashboard container management
- **Use For**: Dashboard configuration, container lifecycle, database operations

### Other Notable Skills
- **agent-browser** - Browser automation with 95% success rate
- **hugo** - Blog post creation and site management
- **chartjs** - Chart.js integration for visualizations
- **task-management** - CLI for tracking feature subtasks

---

## 2. Fabric Patterns (200+ Patterns)

**Location**: `/root/.config/fabric/patterns/`

Fabric patterns are content creation and analysis workflows that can be chained together for complex operations.

### Pattern Categories

**Analysis Patterns** (35+)
- `analyze_claims` - Analyze claims with evidence-based reasoning
- `analyze_paper` - Academic paper analysis
- `analyze_risk` - Risk assessment and mitigation
- `analyze_threat_report` - Cyber threat analysis

**Creation Patterns** (38+)
- `create_hugo_post` - Generate blog posts in Hugo format
- `create_pattern` - Create new Fabric patterns
- `create_summary` - Generate concise summaries
- `create_visualization` - Create Mermaid diagrams and charts

**Extraction Patterns** (30+)
- `extract_wisdom` - Extract wisdom from documentation
- `extract_insights` - Extract key insights from content
- `extract_patterns` - Identify patterns in existing content
- `extract_ideas` - Extract and organize ideas

**Summarization Patterns** (11+)
- `summarize` - General purpose summarization
- `summarize_meeting` - Meeting notes and action items
- `summarize_paper` - Academic paper summaries

**Writing Patterns** (8+)
- `write_essay` - Comprehensive essay writing
- `write_latex` - LaTeX document generation
- `write_pull_request` - Create PR descriptions

### Pattern Creation Protocol

All new patterns follow a strict structure based on `create_pattern`:
- IDENTITY - Pattern purpose and expertise
- GOAL - What the pattern achieves
- STEPS - Step-by-step execution
- INSTRUCTIONS - Detailed guidance
- OUTPUT - Expected deliverables

Reference: `/media/docs/instructions/skill-pattern-creation.md`

---

## 3. OpenClaw Skills (672 Skills)

**Location**: `/media/docs/clawd/`

OpenClaw (formerly Clawdbot) is an open-source AI assistant that runs 24/7 with built-in cron job scheduling for overnight automation.

### Skill Categories (28 Total)

**AI & LLMs** (38 skills)
- `gemini` - Gemini CLI for Q&A and generation
- `gemini-computer-use` - Browser control with Playwright
- `gemini-deep-research` - Long-running research tasks
- `perplexity` - AI-powered web search
- `model-router` - Automatic model selection

**Calendar & Scheduling** (16 skills) ⭐ **Overnight Jobs Focus**
- `morning-email-rollup` - Daily morning email/calendar summaries at 8am
- `remind-me` - Natural language reminders with automatic cron jobs
- `apple-calendar` - Apple Calendar integration
- `clippy` - Microsoft 365/Outlook CLI

**Clawdbot Tools** (17 skills) ⭐ **Cron Management**
- `auto-updater` - Daily automatic updates of Clawdbot and skills
- `claude-connect` - Keep Claude connected 24/7
- `clawdhub` - Search, install, and update agent skills
- `skills-search` - Search skills.sh registry

**Communication** (26 skills)
- `wacli` - WhatsApp CLI for messaging and history
- `linkedin` - LinkedIn automation for messaging and profiles
- `discord-voice` - Real-time Discord voice conversations
- `tootbot` - Publish content to Mastodon
- `walkie-talkie` - WhatsApp voice transcription and TTS

**DevOps & Cloud** (41 skills)
- `portainer` - Docker container management via API
- `dokploy` - Deployment platform management
- `tailscale` - Tailnet management
- `vercel` - Application deployment
- `kubernetes` - Complete cluster management

**Finance** (29 skills)
- `nordpool-fi` - Electricity prices with optimal EV charging windows
- `watch-my-money` - Bank transaction analysis and budgeting
- `ynab` - YNAB budget management
- `monarch-money` - Financial tracking

**Productivity & Tasks** (41 skills)
- Task management, workflow automation
- Time tracking and reminders
- Goal setting and progress monitoring

**Other Categories**:
- Apple Apps & Services (14)
- Browser & Automation (11)
- CLI Utilities (41)
- Coding Agents & IDEs (15)
- Git & GitHub (9)
- Health & Fitness (25)
- Image & Video Generation (20)
- Marketing & Sales (42)
- Media & Streaming (29)
- Notes & PKM (44)
- PDF & Documents (12)
- Personal Development (27)
- Search & Research (23)
- Security & Passwords (6)
- Self-Hosted & Automation (11)
- Shopping & E-commerce (22)
- Smart Home & IoT (31)
- Speech & Transcription (21)
- Transportation (34)
- Web & Frontend Development (14)
- iOS & macOS Development (13)

### OpenClaw Cron System

OpenClaw's Gateway has built-in **cron job scheduling** for overnight automation:

**Features**:
- Jobs persist in `~/.openclaw/cron/jobs.json` (restart-safe)
- Two execution modes: main session or isolated agent turns
- Delivery to Slack, WhatsApp, Telegram, Discord, etc.
- Supports recurring schedules (e.g., `0 7 * * *` = 7 AM daily)

**Example Overnight Job**:
```bash
openclaw cron add \
  --name "Morning brief" \
  --cron "0 7 * * *" \
  --tz "America/Los_Angeles" \
  --session isolated \
  --message "Summarize overnight updates." \
  --deliver \
  --channel whatsapp
```

---

## 4. Docker Project Skills (50+)

**Locations**: Scattered across multiple projects

Notable locations:
- `/media/docker/homarrr/skills/`
- `/media/docker/research/researcher_agent/venv/lib/python3.12/site-packages/litellm/skills/`
- `/media/docker/kuse_cowork/.claude/skills/`
- `/media/docker/openagents/.opencode/`
- `/media/docker/OpenAgentsControl/.opencode/`
- `/media/docker/ui-ux-pro-max-skill/.claude/skills/`

These are project-specific skills for particular applications and workflows.

---

## Overnight Automation Capabilities

With these collections, overnight automation is possible through multiple platforms:

### OpenClaw Cron Jobs
- Morning briefings at scheduled times
- Price monitoring and alerts
- Email summaries and calendar rollups
- Daily updates and status reports

### Fabric Pattern Chains
- Create daily newsletters from multiple sources
- Generate reports and documentation overnight
- Process and analyze large datasets
- Content curation and publishing

### OpenCode Skills
- System maintenance and monitoring
- Memory optimization and organization
- Research and documentation tasks
- Agent orchestration and coordination

---

## Key Insights

### Strengths
1. **Diverse Platforms**: Multiple ecosystems provide different capabilities
2. **Rich Selection**: 960+ skills/patterns to choose from
3. **Specialization**: Each platform excels in specific areas
   - OpenClaw: 24/7 automation and cron scheduling
   - Fabric: Content creation and analysis patterns
   - OpenCode: Agent orchestration and system integration
4. **Community-Driven**: Most skills are community-built and tested

### Opportunities for Integration
1. **Cross-Platform Workflows**: Combine Fabric patterns with OpenCode skills
2. **Unified Orchestration**: Use OpenCode to orchestrate OpenClaw cron jobs
3. **Pattern Sharing**: Migrate successful patterns between platforms
4. **Documentation**: Create comprehensive guides for skill combinations

### Next Steps
1. **Audit**: Review and catalog all Docker project skills
2. **Consolidate**: Consider consolidating scattered skill collections
3. **Standardize**: Create unified patterns for common tasks
4. **Document**: Build a comprehensive skills ecosystem guide
5. **Automate**: Set up overnight jobs using OpenClaw cron system

---

## Resources

- **OpenCode Skills Inventory**: `/media/docs/setup/opencode-skills-inventory.md`
- **OpenClaw Skills**: `/media/docs/clawd/skills-by-category.md`
- **Fabric Pattern Guide**: `/media/docs/instructions/skill-pattern-creation.md`
- **Agent Instructions**: `/root/.config/opencode/agents.md`

---

*This blog post was generated by analyzing my local skill collections across OpenCode, Fabric, and OpenClaw platforms.*