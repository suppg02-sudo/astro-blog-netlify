---
pubDatetime: 2026-02-11T18:30:00Z
title: "Optimizing OpenCode Search: Why Smart-Search Wasn't Being Used"
postSlug: "opencode-smart-search-optimization"
description: "Optimizing OpenCode Search: Why Smart-Search Wasn't Being Used"
tags:
  - agents
  - configuration
  - opencode
  - smart-search
  - search
---

## The Discovery

While reviewing recent research on OpenSpecKit and GitHub alternatives, I noticed something odd: the research findings cited "Google Search, Brave Search, Crawl4AI" as sources, but **no mention of @search** or the smart-search wrapper.

Given that I have a smart-search skill specifically designed to handle web searches with automatic rate limit management, this was a clear signal that the Deep-Research agent wasn't using the recommended approach.

## What is Smart-Search?

Smart-search is an OpenCode skill that wraps web searches with a bash script, providing:

- **Rate limit handling** — Automatic fallback between search providers
- **Consistent formatting** — Standardized output every time
- **Direct API calls** — One less hop (no MCP server overhead)
- **Reliability** — No 429 errors from Google rate limits

The skill enforces a simple rule: **Always use `@search` command instead of calling MCP tools directly.**

### Available Commands

- `@search "query"` — Auto-detects, uses Brave Search (no rate limits)
- `@search-brave "query"` — Force Brave Search
- `@search-google "query"` — Force Google Search (may hit rate limits)

## The Problem

When I checked the Deep-Research agent configuration in `/root/.config/opencode/opencode.json`, the issue was clear:

```json
"Deep-Research": {
  "mode": "subagent",
  "description": "Deep research agent using Claude Opus 4.6...",
  "model": "anthropic/claude-opus-4-6",
  "tools": {
    "read": true,
    "write": true,
    "skill": true,
    "webfetch": true
    // ... other tools
  }
}
```

The agent had `skill: true` permission, meaning it **could** load and use skills, but there was no explicit instruction or skills array to actually use smart-search for web searches.

As a result, the agent was calling MCP tools directly:
- `google-search` MCP tool — Rate-limited
- `brave-search_brave_web_search` MCP tool — Reliable but bypasses the wrapper

## The Solution

I updated the Deep-Research agent configuration to explicitly include smart-search:

```json
"Deep-Research": {
  "mode": "subagent",
  "description": "Deep research agent using Claude Opus 4.6 with evidence-based methodology for comprehensive investigations. MANDATORY: Always use @search command for web searches - never call MCP search tools directly (google_search, brave-search_brave_web_search). Load smart-search skill for rate limit handling.",
  "model": "anthropic/claude-opus-4-6",
  "tools": {
    "read": true,
    "write": true,
    "edit": true,
    "bash": true,
    "skill": true,
    "glob": true,
    "grep": true,
    "question": true,
    "webfetch": true
  },
  "temperature": 0.5,
  "skills": [
    "/root/.opencode/skill/smart-search"
  ]
}
```

### Key Changes

1. **Added `skills` array** — Explicitly lists smart-search path
2. **Updated description** — Added MANDATORY rule about using `@search`
3. **No other changes needed** — The `@search` command was already defined in opencode.json


## Architecture Comparison

### Without Smart-Search (Old Way)

```
Agent Request
    ↓
MCP Server (brave-search)
    ↓
Brave API
    ↓
Search Results
```

**Issues with this approach:**
- Extra hop through MCP server (latency)
- Inconsistent output formatting across different MCP servers
- Google MCP server hits rate limits frequently (429 errors)
- No unified error handling

### With Smart-Search (New Way)

```
Agent Request
    ↓
@search Command (bash wrapper)
    ↓
Brave API (direct call)
    ↓
Consistent Formatted Results
```

**Benefits of this approach:**
- Direct API call — no MCP server overhead
- Consistent output format every time
- No rate limits on primary search (Brave)
- Automatic fallback handling built into wrapper
- Better error recovery

### What the Wrapper Actually Does

The `@search` command in opencode.json points to a bash script:

```bash
/media/docs/output/search-brave.sh "{query}"
```

This script:
1. Accepts search query as argument
2. Calls Brave Search API with your configured key
3. Returns 10 formatted results with:
   - Title
   - URL
   - Description
   - Consistent formatting every time

## Does Deep-Research Still Need Other MCP Tools?

Yes! The smart-search update only affects **web searches**. Other MCP capabilities remain valuable:

**Still useful for research:**
- **context7** — Documentation lookups for libraries, APIs, frameworks
- **grep_app** — Code examples and implementations during research
- **agent-browser** — Testing web servers and APIs after deployment
- **openmemory** — Storing research findings for future reference

**No longer needed for web search:**
- ❌ `google-search` MCP tool — Use `@search` instead
- ❌ `brave-search_brave_web_search` MCP tool — Use `@search` instead

**webfetch** remains useful for fetching specific URLs directly when the URL is known (e.g., documentation pages).


## Verification Steps

After updating the Deep-Research agent configuration, I verified the changes:

### 1. JSON Syntax Validation

```bash
python3 -m json.tool /root/.config/opencode.json | grep -A 18 '"Deep-Research"'
```

Output confirmed the `skills` array was correctly added.

### 2. Configuration Persistence

The changes in `/root/.config/opencode.json` are permanent — they persist across OpenCode restarts and system reboots.

### 3. Skill File Reference

Verified smart-search skill exists at the configured path:
```
/root/.opencode/skill/smart-search/SKILL.md
```

### 4. Memory Storage

Stored the configuration change in OpenMemory with metadata:
- Agent: Deep-Research
- Skill: smart-search
- Change type: skill-loading
- Date: 2026-02-11

This ensures future sessions understand that smart-search is now part of the Deep-Research workflow.

## Key Takeaways

1. **Agents don't auto-inherit skills** — Even with `skill: true` permission, agents need explicit configuration to use specific skills
2. **Skills arrays are explicit** — Add the skill path to the agent's `skills` array to guarantee loading
3. **Descriptions matter** — Adding MANDATORY rules to agent descriptions reinforces expected behavior
4. **MCP tools vs @search** — The `@search` command wrapper provides better reliability than direct MCP tool calls for web searches
5. **Other MCP tools remain useful** — Smart-search optimization only affects web search; context7, grep_app, and agent-browser are still valuable for research

## Expected Impact

Next time the Deep-Research agent runs:

1. Automatically loads smart-search skill
2. Uses `@search "query"` for all web searches
3. Receives consistent, formatted results
4. No rate limit issues on primary search provider
5. Better error recovery if search fails

## Flow Summary

```
User Request
    ↓
Deep-Research Agent
    ↓
Loads smart-search skill ✅
    ↓
Uses @search command ✅
    ↓
Brave API (direct call) ✅
    ↓
Consistent Results ✅
```

## Related Skills

- **smart-search** — Web search wrapper with rate limit handling
- **opencodeskill** — For agent configuration and OpenCode setup
- **hugo** — For creating blog posts (like this one!)

---

**Published**: 2026-02-11  
**Skill Reference**: http://ubuntu58-1:3001/editor/root%2F.opencode%2Fskill%2Fsmart-search%2FSKILL.md