---
pubDatetime: 2026-04-04T08:54:45Z
title: "Beyond @clack/prompts: Finding Better CLI Question Tools for AI Agents"
postSlug: "beyond-clack-prompts-cli-question-tools"
description: "Testing OpenCode question tool reveals critical gaps—disabled options selectable, no hint display, max options unvalidated. We explore four alternatives including @inquirer (21M weekly downloads) and "
tags:
  - opencode
  - prompts
  - ai-agents
  - nodejs
  - cli
  - development-tools
---

# Beyond @clack/prompts: Finding Better CLI Question Tools for AI Agents

**TL;DR**: Our comprehensive testing of OpenCode's question tool uncovered significant gaps—disabled options can be selected, hint text never displays, and the 10-option max rule goes unenforced. We discovered four alternatives that fix these issues, led by @inquirer/prompts with 21M weekly downloads.

---

## The Problem

When building AI agents that interact with users via CLI, the question tool is critical. It's how agents present choices, gather preferences, and confirm actions. We've been using @clack/prompts in OpenCode, but systematic testing revealed several concerning gaps.

## What We Tested

We conducted an exhaustive test suite across 35+ scenarios covering:

- Single and multi-select modes
- Numbered options
- Hints and descriptions
- Disabled options
- Label truncation
- Unicode and emojis
- Mobile-friendly patterns
- Edge cases (empty labels, duplicate values, escape sequences)

## Key Findings

### What Works ✅

| Feature | Status |
|---------|--------|
| Single/multi-select | ✅ Working |
| Manual numbering | ✅ Working |
| Emoji labels | ✅ Working |
| Unicode support | ✅ Working |
| Falsy values (0, false, "") | ✅ Working |

### What's Broken ❌

| Issue | Severity | Impact |
|-------|----------|--------|
| **Disabled options selectable** | Critical | Users can select unavailable options |
| Hint text not displayed | High | Contextual guidance invisible |
| Max 10 options unvalidated | Medium | Menus can exceed limits |
| Initial value not shown | Low | Default selection unclear |

### Mobile Mode Challenge

Our testing confirmed mobile terminals need special treatment:
- **Max 4-5 options** per menu (user mandate)
- **Short labels** — emojis, single letters, 1-2 words
- First option should be "Mobile Off" to switch to desktop

## The Alternatives

We found four drop-in replacements worth considering:

### 1. @inquirer/prompts — The Standard (21M weekly downloads)

The official Inquirer prompt library. Mature, well-documented, and feature-complete.

**Pros:**
- All prompt types (select, multiselect, checkbox, editor, etc.)
- Proper disabled option support
- Hint text displayed inline
- Extensive customization
- Massive community

**Cons:**
- More dependencies than modern alternatives
- Slightly older architecture

### 2. enquirer — Feature-Rich (4M weekly downloads)

Battle-tested with rich prompt types and elegant API.

**Pros:**
- Extensive prompt types (scale, sort, quiz, snippet)
- Auto-complete support
- Choice hints and disabled states
- Plugin ecosystem

**Cons:**
- Not as actively maintained as @inquirer
- Some deprecated APIs

### 3. @agentine/elicit — Zero-Dependency Modern (NEW)

Lightweight replacement for prompts and enquirer. TypeScript-first with zero dependencies.

```javascript
import elicit from '@agentine/elicit';

const response = await elicit([
  { type: 'select', name: 'color', choices: [
    { title: 'Red', value: 'red' },
    { title: 'Blue', value: 'blue', disabled: true }
  ]}
]);
```

**Pros:**
- Zero dependencies (smaller bundle)
- TypeScript-first design
- Drop-in replacement for prompts/enquirer
- Supports disabled choices, hints

**Cons:**
- Newer project (less battle-tested)
- Smaller community

### 4. @agentine/parley — Enquirer Replacement (NEW)

Same @agentine organization, focused as a drop-in enquirer replacement.

**Pros:**
- Enquirer-compatible API
- Additional prompt types (scale, sort, quiz, snippet)
- Zero dependencies
- ESM + CJS dual package

**Cons:**
- Very new (v0.1.0 March 2026)
- No production track record

## Our Recommendations

For AI agent frameworks like OpenCode:

1. **Immediate**: Fix @clack/prompts gaps — disable enforcement, hint display
2. **Short-term**: Consider @agentine libraries for zero-dep benefits
3. **Long-term**: @inquirer/prompts is the proven choice for production systems

## What Changed

Based on testing, we've updated OpenCode menu conventions:

- **Mobile-first mode** — Start with max 4-5 options
- **First option**: "Mobile Off" to switch to desktop
- **Numbered labels** — Users can type "1" to select option 1

---

## Conclusion

The @clack/prompts library serves well for basic needs, but AI agents with nuanced UI requirements will benefit from alternatives. @inquirer/prompts offers the most mature solution with proper disabled state handling and hints, while @agentine libraries provide modern zero-dependency options for teams prioritizing bundle size.

**Tags**: cli, prompts, ai-agents, opencode, nodejs, development-tools
**Categories**: Development Tools, AI Automation, Tutorials