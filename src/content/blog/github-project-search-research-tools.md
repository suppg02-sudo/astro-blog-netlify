---
pubDatetime: 2026-03-16T23:53:53Z
title: "GitHub Project Search TITLE_PLACEHOLDER Research Tools - Biweekly Digest (March 16, 2026)"
postSlug: "github-project-search-research-tools"
description: "GitHub Project Search TITLE_PLACEHOLDER Research Tools - Biweekly Digest (March 16, 2026)"
tags:
  - github
  - biweekly
  - mcp
  - cli
  - ai
  - research
  - tools
---

This biweekly digest covers tools for searching and researching GitHub repositories.

## Quick Decision Matrix

| Your Need | Best Tool |
|-----------|-----------|
| AI agent integration | `octocode-mcp` or `github-mcp-server` |
| Quick repo health check | AI Codebase Analyst (Apify) |
| Bulk organization analysis | `gh-stats` or `OSSInsight` |
| Self-hosted code search | Sourcebot or Zoekt |
| Security reconnaissance | Gitxray |

---

## 1. MCP Servers

| Server | Stars | Install |
|--------|-------|---------|
| [github-mcp-server](https://github.com/github/github-mcp-server) | 27,949+ | `docker pull ghcr.io/github/github-mcp-server` |
| [octocode-mcp](https://github.com/bgauryy/octocode-mcp) | 753+ | `npx octocode-mcp` |

---

## 2. AI Research Agents

| Agent | Repository | Features |
|-------|------------|----------|
| DeepGit | [zamalali/DeepGit](https://github.com/zamalali/DeepGit) | LangGraph, ColBERT |
| OpenHands | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | Autonomous fixes |

---

## 3. CLI Tools

```bash
# Essential gh extensions
gh extension install meiji163/gh-search
gh extension install dlvhdr/gh-dash

# Search repos
gh search repos "topic:mcp-server" --stars ">100"
```

---

## 4. Self-Hosted Search

| Engine | Repository | Use Case |
|--------|------------|----------|
| Sourcebot | [sourcebot-dev/sourcebot](https://github.com/sourcebot-dev/sourcebot) | Sourcegraph alternative |
| Zoekt | [google/zoekt](https://github.com/google/zoekt) | Google's engine |

---

## Resources

- [awesome-gh-cli-extensions](https://github.com/kodepandai/awesome-gh-cli-extensions) (474+)
- [best-of-mcp-servers](https://github.com/tolkonepiu/best-of-mcp-servers) (410+)

---

*Updated: 2026-03-16T23:53:53Z*