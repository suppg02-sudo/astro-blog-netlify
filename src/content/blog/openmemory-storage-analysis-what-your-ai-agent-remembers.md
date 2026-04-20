---
pubDatetime: 2026-03-04T12:00:00Z
title: "OpenMemory Storage Analysis: What Your AI Agent Remembers"
postSlug: "openmemory-storage-analysis-what-your-ai-agent-remembers"
description: "OpenMemory Storage Analysis: What Your AI Agent Remembers"
tags:
  - openmemory
  - ai-agents
  - automation
  - memory-storage
  - crud-pattern
  - hsg
---

## The Question Every AI Agent Owner Asks

When you run an AI agent day after day, a natural question emerges: **What exactly is being remembered?** Is it storing your coffee preferences? Your project decisions? Every button click on your dashboard?

Today I conducted a comprehensive investigation into OpenMemory—the persistent memory system powering this AI infrastructure. The results reveal a sophisticated, structured approach to long-term agent memory.

## The Numbers

**1,083 memories** stored in a SQLite database with hierarchical semantic indexing.

But raw numbers don't tell the story. The real insight is *what types* of memories exist and *how* they're automatically captured.

## Memory Types: The Eight Context Categories

OpenMemory uses a structured type system with eight defined context types:

{{< mermaid >}}
graph TD
    A[OpenMemory Context Types] --> B[flow]
    A --> C[workflow]
    A --> D[skill]
    A --> E[conversation]
    A --> F[initiative]
    A --> G[decision]
    A --> H[menu_choice]
    A --> I[deferred]
    
    B --> B1[237 entries]
    B --> B2[Delegations, actions, blog posts]
    
    C --> C1[199 entries]
    C --> C2[Multi-step processes, maintenance]
    
    D --> D1[199 entries]
    D --> D2[Skill configurations, usage]
    
    E --> E1[195 entries]
    E --> E2[Session summaries]
    
    F --> F1[88 entries]
    F --> F2[Active projects, goals]
    
    G --> G1[25 entries]
    G --> G2[Architecture choices, fixes]
    
    H --> H1[30+ entries]
    H --> H2[Question tool interactions]
    
    I --> I1[5 entries]
    I --> I2[Parked tasks]
{{< /mermaid >}}

### Flow (237 entries)
The largest category. Captures:
- **Blog post publications**: Every `bp` trigger creates a memory with title, URL, word count, and metadata
- **Agent delegations**: When Sisyphus delegates to explore, quick, or other agents
- **Relay actions**: Homepage button clicks that trigger OliveTin webhooks

### Workflow (199 entries)
Multi-step processes and maintenance tasks:
- Emergency repairs
- System upgrades
- Configuration changes

### Decision (25 entries)
Architecture and design decisions with full rationale:
- Why a particular technology was chosen
- Configuration changes and their reasons
- Trade-off analyses

### Menu Choice (30+ entries)
Every question tool interaction:
- What question was asked
- What options were presented
- What choice was made
- Timestamp and session context

## The HSG Sector System

OpenMemory uses Hierarchical Semantic Graph (HSG) with five memory sectors, each with different decay rates:

| Sector | Decay Lambda | Use For | Salience Range |
|--------|-------------|---------|----------------|
| `semantic` | 0.005 | Facts, knowledge, context types | 0.4-1.0 |
| `procedural` | 0.008 | How-to, processes, configurations | 0.4-0.99 |
| `episodic` | 0.015 | Events, sessions, interactions | varies |
| `emotional` | 0.020 | Preferences, frustrations, satisfaction | 0.49 |
| `reflective` | 0.001 | Meta-knowledge, patterns, insights | 0.4 |

**Key insight**: Reflective memories decay slowest (0.001), preserving meta-patterns for the long term.

## Automatic Storage: What Gets Remembered Without You Asking

### 1. Every Question Tool Interaction

```json
{
  "type": "menu_choice",
  "question": "What would you like to do next?",
  "choice": "Publish as-is (Recommended)",
  "options": ["Publish as-is", "Change title", "Skip"],
  "timestamp": "2026-03-04T15:30:00Z"
}
```

This happens automatically when the agent presents options and you select one.

### 2. Blog Post Publications

```json
{
  "type": "flow",
  "subtype": "blog_post",
  "title": "Server Setup Roadmap 2026: Building a Self-Hosted AI Infrastructure",
  "word_count": 3500,
  "url": "http://ubuntu4:1313/posts/...",
  "mermaid_enabled": true,
  "chart_enabled": true
}
```

Every blog post trigger creates a permanent record.

### 3. Homepage Button Clicks

The investigation revealed **149 relay actions** from Homepage:

- Health checks
- System audits
- Theme changes
- Service restarts
- Performance reports

Each captured with:
- Action source (relay, manual, oliveTin)
- Trigger type (webhook, button)
- Success/failure status
- Duration in milliseconds
- Exit code

### 4. Agent Delegations

When Sisyphus delegates work:

```json
{
  "type": "flow",
  "subtype": "delegation",
  "from_agent": "sisyphus",
  "to_agent": "explore",
  "task": "Find auth patterns in codebase",
  "skills_loaded": ["git"],
  "timestamp": "2026-03-04T12:59:07Z"
}
```

### 5. Weekly Intelligence Reports

A cron job runs every Sunday at 10:00 AM UTC:

```bash
0 10 * * 0 /usr/bin/python3 /root/.config/opencode/scripts/memory-report.py
```

This generates a weekly intelligence report from memory patterns.

## The CRUD Pattern: How Metadata Survives

The critical insight from this investigation: **The `metadata` field preserves JSON exactly as-is.**

```
content: "flow: blog post created - Server Setup Roadmap 2026..."
metadata: {
  "type": "flow",
  "subtype": "blog_post",
  "title": "Server Setup Roadmap 2026",
  "word_count": 3500,
  ...
}
```

The `content` field gets processed by HSG and may be altered for semantic indexing. But `metadata` is immutable—perfect for structured queries.

**This is the CRUD pattern:**
- **Create**: Store with `content` + `metadata` + `tags`
- **Read**: Query by semantic search, then `get` for full metadata
- **Update**: Delete old + create new (no in-place updates)
- **Delete**: Remove by ID

## Today's Activity: A Memory Timeline

The investigation captured today's session in real-time:

| Time | Type | What Was Stored |
|------|------|----------------|
| 11:00 | test | Flow integration test |
| 10:30 | flow | Blog post: Microsoft Power Apps MCP Server |
| 10:51 | flow | Blog post: Server Setup Roadmap 2026 |
| 12:30 | roadmap | Phase 6 expanded (3→12 cron tasks) |
| 12:00 | roadmap | Phase 12 added (User Onboarding) |
| 08:35 | menu_choice | Blog post action menu → Exit |
| 07:55 | menu_choice | Flows menu → Analyse Recent Flow |
| 07:55 | decision | Question tool fix (no raw JSON in text) |
| 07:23 | workflow | Emergency OpenMemory repair (922 rescued) |
| 07:05 | menu_choice | Memory Management → Daily Research |
| 06:40 | fix | oh-my-opencode permissions changed |
| Earlier | workflow | Metadata backfill (943 memories) |

Every action, decision, and menu selection—automatically captured.

## Storage Sources: Where Memories Come From

Analysis of `flows.json` reveals the origin of 153 tracked flows:

| Source | Count | Description |
|--------|-------|-------------|
| `relay` | 149 | Homepage button clicks → webhooks |
| `opencode` | 2 | Agent delegations |
| `manual` | 1 | Direct triggers |
| `olivetin` | 1 | OliveTin-initiated actions |

**The vast majority of memories come from automated relay actions**—not manual logging.

## Memory Structure: Five Examples

### Blog Post Flow
```json
{
  "content": "flow: blog post created - Microsoft Power Apps MCP Server...",
  "primary_sector": "reflective",
  "salience": 0.9,
  "metadata": {
    "type": "flow",
    "subtype": "blog_post",
    "title": "Microsoft Power Apps MCP Server...",
    "word_count": 1894,
    "mermaid_enabled": true
  }
}
```

### Workflow Completion
```json
{
  "content": "completed: Emergency OpenMemory repair...",
  "primary_sector": "semantic",
  "salience": 1.0,
  "tags": ["workflow", "maintenance", "repaired"],
  "metadata": {
    "rescued_count": 922,
    "wal_cleared": true
  }
}
```

### Decision/Fix
```json
{
  "content": "fix: Changed oh-my-opencode question permissions...",
  "tags": ["fix", "opencode", "question-tool"],
  "metadata": {
    "type": "decision",
    "from": "allow",
    "to": "ask",
    "reason": "User reported auto-clicking behavior"
  }
}
```

### Relay Action
```json
{
  "content": "flow: relay/restart-opencode-full (webhook) → success",
  "metadata": {
    "action_id": "restart-opencode-full",
    "trigger": "webhook",
    "success": true,
    "duration_ms": 2
  }
}
```

### Initiative
```json
{
  "content": "{\"initiative\": \"Universal Context Registry\", \"phase\": \"planning\"}",
  "primary_sector": "procedural",
  "salience": 1.0,
  "tags": ["roadmap", "context-registry", "architecture"]
}
```

## Key Takeaways

1. **Most storage is automatic**—question tool, blog posts, relay actions
2. **Structure is preserved** via the `metadata` field's exact JSON storage
3. **Five HSG sectors** provide intelligent decay rates for different memory types
4. **Eight context types** organize memories for querying
5. **149 relay actions** show heavy automation via Homepage buttons
6. **Weekly cron job** generates intelligence reports from patterns

## What This Means for AI Agent Owners

If you're running an AI agent with persistent memory:

- **Every decision is traceable**—the `reason` field captures why choices were made
- **Automation creates audit trails**—relay actions show exactly what buttons were clicked
- **Blog posts are permanent records**—full metadata preserved for each publication
- **Memory decays intelligently**—reflective patterns last longest, emotional reactions fade fastest

The question "What does my AI remember?" has a clear answer: **structured context with automatic capture and intelligent decay.**

---

*This investigation was conducted by querying OpenMemory directly via MCP tools, analyzing context-registry JSON files, and examining cron automation. Total memories analyzed: 1,083.*