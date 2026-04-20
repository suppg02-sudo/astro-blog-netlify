---
pubDatetime: 2026-02-27T02:35:00Z
title: "OpenCode Skill System Evolution: Roundup, Constitution & Menu Enhancement"
postSlug: "opencode-roundup-constitution-menu-system"
description: "OpenCode Skill System Evolution: Roundup, Constitution & Menu Enhancement"
tags:
  - skills
  - opencode
  - constitution
  - automation
  - menu-system
  - triggers
---

## Session Overview

This session focused on evolving the OpenCode skill system with three major additions:

1. **Roundup Skill** - Comprehensive session review and system health check
2. **Constitution File** - Structural conventions and best practices
3. **Menu System** - Global menu enhancement with intensity levels

---

## Roundup Skill

### Purpose

A comprehensive daily review system that audits the entire OpenCode environment:

- Activity timeline (last 48 hours)
- Cron job status
- Backup health
- Skill/trigger audit
- Freshstart repository sync
- Performance issues
- Error logs

### Blueprint Compliance

The skill follows the complete blueprint architecture:

| Feature | Status |
|---------|--------|
| YAML Frontmatter | ✅ |
| Progressive Disclosure | ✅ 4 levels |
| Menu System | ✅ 12 options |
| Cron Support | ✅ Non-interactive mode |
| History System | ✅ Usage logs |
| Skill Interop | ✅ diagnose, hugo, space |

### Cron Integration

```cron
# Daily roundup at 03:00 UTC
0 3 * * * ROUNDUP_CRON_MODE=true /root/.config/opencode/skills/roundup/scripts/cron-executor.sh --quiet
```

**Key Rule:** No menus in cron mode - silent execution only.

### Menu Options

| Option | Description |
|--------|-------------|
| 📋 Full Report | Complete 2-day activity report |
| 🔧 Install | First-time setup with cron job |
| 📅 Activity Summary | Quick overview of recent work |
| 🔍 Skill/Trigger Audit | Check for missing updates |
| 🔄 Freshstart Sync | Compare with GitHub repo |
| ⏰ Cron Job Status | Review all cron jobs |
| 💾 Backup Status | Check backup health |
| ⚡ Performance Issues | OOM events, resource alerts |
| ❌ Error Log Review | System/container errors |
| 📝 Publish Blog Post | Generate blog post |
| 📜 Decision History | Review recorded decisions |

---

## Constitution File

### Why?

As the skill system grew, patterns emerged that needed documentation. The constitution captures:

- File locations
- Trigger format conventions
- Skill blueprint compliance
- Menu system rules
- Naming conventions
- URL formatting
- Error handling patterns

### Key Principles

#### 1. Documentation Hierarchy

```
AGENTS.md (Global Rules)
    └── Brief triggers (~3 lines max)
    └── Points to trigger files

triggers/*.md (Trigger Files)
    └── Full workflow details
    └── Menu options, cron support

skills/*/SKILL.md (Skill Documentation)
    └── Complete architecture
    └── Progressive disclosure
```

#### 2. Trigger Format (AGENTS.md)

```markdown
**trigger-name** (on its own)
 Brief one-line description
 Location: `~/.config/opencode/docs/instructions/triggers/trigger-name.md`
```

**Maximum: 3 lines per trigger.** Details go in the trigger file.

#### 3. File Locations

| Content Type | Location |
|--------------|----------|
| Global rules | `~/.config/opencode/AGENTS.md` |
| Trigger definitions | `~/.config/opencode/docs/instructions/triggers/*.md` |
| Skills | `~/.config/opencode/skills/*/SKILL.md` |
| Decision history | `~/.config/opencode/questions/history/decisions.json` |
| Cron logs | `~/cron-logs/` |

---

## Menu Enhancement System

### Features

| Feature | Description |
|---------|-------------|
| **Intensity Levels** | Minimal / Normal / Verbose / Brainstorm |
| **Multiselect Mode** | Toggle batch operations |
| **Menu History** | Recent selections and outcomes |
| **Smart Suggestions** | AI-powered option improvements |
| **Menu Heartbeat** | Health check for menu system |

### Intensity Levels

| Level | Options | Descriptions | Multiselect |
|-------|---------|--------------|-------------|
| Minimal | 4 max | Short | Off |
| Normal | 8 max | Full | As designed |
| Verbose | 12 max | Detailed | On |
| Brainstorm | 15 max | Extended | Forced on |

### Access Methods

1. **Dedicated Trigger:** `menu` (on its own)
2. **Footer Option:** Add `⚙️ Menu Settings` to all menus

### Standard Menu Footer

Every menu should include:

```json
{"label": "⚙️ Menu Settings", "description": "Intensity, history, suggestions"},
{"label": "⏹️ Exit", "description": "Return to previous context"}
```

---

## Files Created This Session

| File | Purpose |
|------|---------|
| `skills/roundup/SKILL.md` | Main skill documentation |
| `skills/roundup/scripts/cron-executor.sh` | Cron-compatible execution |
| `skills/roundup/scripts/full-report.sh` | Interactive report generator |
| `skills/roundup/config/menu.json` | Menu definitions |
| `triggers/roundup.md` | Trigger definition |
| `CONSTITUTION.md` | Structural conventions |
| `skills/menu-system/SKILL.md` | Menu enhancement skill |
| `skills/menu-system/config/settings.json` | Menu settings |
| `skills/menu-system/history/menu-history.json` | Selection tracking |
| `triggers/menu.md` | Menu trigger definition |
| `questions/history/decisions.json` | Decision recording |

---

## Performance Issues Detected

The roundup skill identified critical system issues:

| Issue | Status | Details |
|-------|--------|---------|
| **Memory** | 🔴 CRITICAL | 93% used (1.8GB total, 120MB free) |
| **Swap** | 🔴 HIGH | 2.1GB / 5GB used |
| **OOM Kills** | 🔴 18 events | Node, gunicorn, celery processes killed |

### Recommendations

1. Review container memory limits
2. Consider stopping non-essential containers
3. Increase swap or add physical RAM
4. Monitor with `roundup` daily

---

## Next Steps

1. **Create missing trigger files** - 12 triggers need documentation
2. **Sync to freshstart** - Commit new skills to repository
3. **Monitor memory** - Address OOM issues
4. **Add menu footer** - Update all existing skills with ⚙️ Menu Settings

---

## Quick Reference

```bash
# Run roundup
roundup

# Access menu settings
menu

# Run daily report manually
~/.config/opencode/skills/roundup/scripts/cron-executor.sh

# View constitution
cat ~/.config/opencode/CONSTITUTION.md

# View menu history
cat ~/.config/opencode/skills/menu-system/history/menu-history.json
```

---

*Generated from OpenCode session on 2026-02-27*