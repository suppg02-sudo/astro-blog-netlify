---
pubDatetime: 2026-03-15T08:00:17Z
title: "Question Tool Ecosystem Weekly Digest - Week of March 08, 2026"
postSlug: "question-tool-ecosystem-weekly-digest-2026-03-15"
description: "Question Tool Ecosystem Weekly Digest - Week of March 08, 2026"
tags:
  - ecosystem
  - question-tool
  - weekly-digest
  - monitoring
  - research
---

## 📊 Week of March 08, 2026 to March 15, 2026

This weekly digest aggregates daily research findings, tracks repository activity, and identifies trending patterns in the question tool ecosystem.

---

## 🏆 Ecosystem Overview

| Project | Stars | Weekly Commits | Open Issues | Trend |
|---------|-------|----------------|-------------|-------|
| [n8n](https://github.com/n8n-io/n8n) | 179,181 | 50 | 1429 | 📈 |
| [opencode](https://github.com/anomalyco/opencode) | 122,342 | 50 | 6863 | 📈 |
| [gemini-cli](https://github.com/google-gemini/gemini-cli) | 97,762 | 50 | 2924 | 📈 |
| [claude-code](https://github.com/anthropics/claude-code) | 78,056 | 9 | 6453 | 📈 |
| [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | 40,063 | 50 | 372 | 📈 |
| [directus](https://github.com/directus/directus) | 34,480 | 23 | 388 | 📈 |
| [mux](https://github.com/coder/mux) | 1,355 | 50 | 169 | 📈 |
| [talkcody](https://github.com/talkcody/talkcody) | 421 | 3 | 9 | 📊 |

---

## 📈 Notable Changes This Week

### n8n

**Commits (50):**
- fix(Notion Node): Allow underscores in page URL slug validation (#27051)

Co-aut... (2026-03-14)
- fix(Airtable Node): Revert flattening output from search and get operations (#26... (2026-03-13)
- feat(editor): Enable project editors to view external secret vaults (#27007)... (2026-03-13)

**Issues (20):**
- [#27057] fix(OracleNode): Prevent 'Maximum call stack size exceeded' when handling large query result sets (closed)
- [#27056] fix(core): Fix custom node icon path resolution (open)
- [#27055] fix(editor): Prevent Safari text selection on canvas drag (open)

### opencode

**Commits (50):**
- chore(permission): delete legacy permission module (#17534)... (2026-03-15)
- fix(question): clean up pending entry on abort (#17533)... (2026-03-15)
- remove sighup exit (#17254)... (2026-03-14)

**Issues (20):**
- [#17567] fix(opencode): don't double-count OpenAI reasoning tokens in cost calculation (open)
- [#17566] OpenAI reasoning tokens double-counted in cost calculation (open)
- [#17565] fix: filter empty message content for all providers to prevent LiteLLM proxy sanitization artifact (open)

### gemini-cli

**Commits (50):**
- fix(core): merge user settings with extension-provided MCP servers (#22484)... (2026-03-15)
- fix(cli): improve command conflict handling for skills (#21942)... (2026-03-14)
- Add ModelDefinitions to ModelConfigService (#22302)... (2026-03-14)

**Issues (20):**
- [#22507] plan mode always stuck (open)
- [#22506] feat(voice): implement hands-free voice mode with Live API, VAD, audio capture, and TTS (open)
- [#22505] Fix/scroll overflow v2 (open)

### oh-my-opencode

**Commits (50):**
- @idrekdon has signed the CLA in code-yeongyu/oh-my-openagent#2572... (2026-03-14)
- @robinmordasiewicz has signed the CLA in code-yeongyu/oh-my-openagent#2563... (2026-03-14)
- remove ai slops... (2026-03-14)

**Issues (20):**
- [#2575] fix(delegate-task): add subagent turn limit and model routing transparency (open)
- [#2573] [Feature]: Model inherit from Sisyphus (open)
- [#2572] fix(doctor): count intelephense in LSP detection (open)

### mux

**Commits (50):**
- 🤖 feat: add browser sidebar tab for live agent-browser viewing (#2951)

## Summa... (2026-03-14)
- 🤖 fix: isolate transcript quote boundaries (#2956)

## Summary
Refactor transcri... (2026-03-14)
- 🤖 feat: fork workspaces from assistant responses (#2953)

## Summary
Add a Fork ... (2026-03-14)

**Issues (20):**
- [#2961] 🤖 fix: show portable desktop warning on settings routes (open)
- [#2960] 🤖 fix: add browser launcher fallbacks and update install hint (open)
- [#2959] 🤖 fix: suppress notifications for auto-follow-up handoffs (open)

---

## 🎯 Trending Patterns

| Pattern | Evidence | Adoption |
|---------|----------|----------|
| Pagination | n8n, local implementation | High |
| 3-State Selection | Q-Brainstorm | Medium |
| Context Injection | n8n introMessage | Medium |
| Pre-Filled Answers | Coder Mux | Low |
| Context7 Integration | oh-my-opencode, upstash | Medium |

---

## 📊 Weekly Metrics

| Metric | Value |
|--------|-------|
| **Total Commits** | 285 |
| **Total Issues** | 142 |
| **Active Repos** | 8 |
| **Daily Research Posts** | 0 |

---

## 🔍 Key Insights

- **High Activity**: Ecosystem is actively evolving with {total_commits} commits this week
- **Active Discussions**: {total_issues} issues opened, indicating community engagement
- **Most Active**: n8n leads with 50 commits

---

## 🚀 Next Week Focus

- Monitor new implementations of pagination patterns
- Track adoption of 3-state selection beyond brainstorming
- Identify new Context7 integrations
- Watch for question tool usage in emerging AI agent frameworks

---

*Weekly digest generated at 2026-03-15T08:00:17Z*
*Sources: GitHub API, Daily Research Posts*