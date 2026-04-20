---
pubDatetime: 2026-04-09T20:00:00Z
title: "Trigger Registry Rebuild: From Stale Header to 32 Verified Triggers"
postSlug: "trigger-registry-rebuild-from"
description: "Trigger Registry Rebuild: From Stale Header to 32 Verified Triggers"
tags:
  - others
---

A routine `rf` (research-factory) trigger that should have worked didn't — because the entire trigger registry had degraded to a single stale line: `total_triggers: 84`. No triggers. No aliases. No categories. Just a ghost count from a previous era.

## The Problem

The Hub & Spoke restructuring on 2026-04-01 moved trigger documentation from AGENTS.md into a dedicated `trigger-words.md` context file and a `triggers.yaml` registry. The context file was rich and detailed — but the YAML registry, the machine-readable source of truth, was empty. Triggers worked only because the agent happened to recognise them from the markdown docs, not because they were registered.

When `rf` was typed and the agent didn't recognise it, the gap became obvious.

## The Fix

**Phase 1: Registry rebuild.** Scanned all 31 active skill directories for `trigger:` declarations in their SKILL.md files. Generated a complete `triggers.yaml` with proper structure — categories, aliases, descriptions, skill mappings. All 31 passed validation with zero warnings.

**Phase 2: New `nx` trigger.** Added a behaviour-type trigger that rediscovers recent files from the current session and converts them to clickable NextExplorer URLs using the volume mapping rules (`opencode`, `docker`, `freshstart`, `storage`).

**Phase 3: Discoverability fix.** The trigger table had been removed from AGENTS.md to save tokens. But triggers that aren't visible can't be discovered. Added a compact 2-column trigger table (36 triggers, +17 lines) back into AGENTS.md so every session starts with full trigger visibility — no context file loading required.

## Architecture

```
triggers.yaml (machine-readable registry)
    ↓ validates against
trigger-words.md (full protocols + detailed docs)
    ↓ referenced by
AGENTS.md (compact table — always in context)
```

Three layers, one source of truth. The YAML feeds validation. The markdown feeds detailed protocols. The AGENTS.md table feeds discoverability.

## The `nx` Trigger

One command to surface every file touched in the current session as clickable editor links:

| Path Pattern | NextExplorer URL |
|---|---|
| `~/.config/opencode/X` | `http://ubuntu4:8080/editor/opencode/X` |
| `/media/docker/X` | `http://ubuntu4:8080/editor/docker/X` |
| `/root/freshstart/X` | `http://ubuntu4:8080/editor/freshstart/X` |

No more scrolling back through conversation history to find a file reference.

## Validation

```
Total triggers:    32
Type: skill:       31
Type: behavior:     1
✓ All checks passed
```

**Tags**: triggers, infrastructure, registry, open-code, agent-configuration