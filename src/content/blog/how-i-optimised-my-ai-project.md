---
pubDatetime: 2026-04-06T17:05:48Z
title: "How I Optimised My AI Project Dashboard for Sub-Second Response"
postSlug: "how-i-optimised-my-ai-project"
description: "How I Optimised My AI Project Dashboard for Sub-Second Response"
tags:
  - others
---

When you're managing 8+ projects through an AI-powered CLI, every second counts. Here's how I took the Project Factory dashboard from 3+ sequential bash calls to a single cached script with cron pre-computation.

## Quick Summary

- Consolidated 3+ bash calls into a single Python script (`pf_dashboard.py`)
- Added mtime-based caching with 30-minute TTL
- Cron job pre-computes dashboard every 30 minutes
- Dynamic menus aligned with a central menu-factory system
- Mobile-first: max 4 items, single-tap, no submit button

## The Problem

The Project Factory skill (`pf` trigger) needed to show a dashboard with project statuses, priority actions, and a dynamic menu every time it was invoked. The original implementation ran 3+ sequential bash commands:

1. List all projects
2. Parse their YAML status files
3. Build a formatted dashboard output
4. Generate dynamic menu options

On a cold run, this took 2-4 seconds. On a mobile device with limited context windows, that's painful.

## The Solution: Single Script + Cron Pre-Computation

### Step 1: Consolidated Script

I created `pf_dashboard.py` with multiple modes:

| Mode | Purpose |
|------|---------|
| `--cat` | Display cached dashboard |
| `--menu` | Output dynamic domain JSON for menu-factory |
| `--cron` | Pre-compute and refresh cache |
| `--format json\|text` | Output format control |
| `--no-cache` | Force fresh computation |
| `--compact` | Minimal output for mobile |

### Step 2: Mtime-Based Cache

The cache uses file modification timestamps. When any project YAML is newer than the cache, the cache is invalidated:

```python
def _cache_stale(self):
    if not self.cache_json.exists():
        return True
    cache_mtime = self.cache_json.stat().st_mtime
    if time.time() - cache_mtime > self.max_age:
        return True
    for pf in self.projects_dir.glob("*.yaml"):
        if pf.stat().st_mtime > cache_mtime:
            return True
    return False
```

Both JSON (for `--menu` mode) and text (for `--cat` mode) caches are maintained.

### Step 3: Cron Pre-Computation

A cron job runs every 30 minutes to keep the cache warm:

```
*/30 * * * * python3 ~/.config/opencode/skills/project-factory/scripts/pf_dashboard.py --cron
```

This means the dashboard is almost always served from cache — sub-second response time.

## Menu Alignment with Menu-Factory

The key insight was separating **domain options** from **menu assembly**. The `pf` skill now only provides 3 domain options (top priority projects), and the central `build_menu.py` handles:

- Mobile/desktop mode detection
- Global suffix options (Defer, Desktop toggle)
- Overflow handling (More arrow)
- Signal tracking for menu optimisation

### Mobile Menu Constraint

Mobile menus are capped at 4 items total. The breakdown:

| Slot | Content |
|------|---------|
| 1 | Domain option (top project) |
| 2 | Domain option (2nd project) |
| 3 | Domain option (3rd project) |
| 4 | Global suffix (Defer) |

On desktop, all 3 domain options plus full suffix are shown.

## Emoji Exception for Priority Badges

High-priority projects get a red circle badge in menu labels. This required adding `emoji_exceptions` to the global menu config:

```json
{
  "emoji_exceptions": {
    "allowed_in_labels": ["🔴"],
    "reason": "High-priority project badge in pf dashboard menus"
  }
}
```

The `menu_lint.py` validator respects this exception when checking label character limits.

## Results

| Metric | Before | After |
|--------|--------|-------|
| Dashboard render | 2-4s (3+ bash calls) | <1s (cached) |
| Menu items | Hardcoded | Dynamic from project data |
| Mobile UX | Overflow, submit off-screen | 4 items, single-tap |
| Cache invalidation | Manual | Auto (mtime + TTL) |
| Pre-computation | None | Cron every 30 min |

## Lessons Learned

1. **Pre-compute over on-demand**: Cron-based cache warming beats lazy computation for frequently-accessed data
2. **Centralise menu assembly**: Skills should only provide domain options, not build full menus
3. **Mobile-first constraints force good design**: The 4-item limit forced ruthless prioritisation
4. **Mtime > manual invalidation**: File modification timestamps are a reliable, zero-config cache strategy

**Tags**: ai-automation, opencode, project-management, performance-optimisation
**Categories**: AI Automation, Engineering