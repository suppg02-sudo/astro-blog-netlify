---
pubDatetime: 2026-04-12T08:00:11Z
title: "AI Coding Agent Ecosystem — Week of 12 April 2026"
postSlug: "ai-ecosystem-weekly-2026-04-12"
description: "AI Coding Agent Ecosystem — Week of 12 April 2026"
tags:
  - agents
  - ecosystem
  - weekly
---

# AI Coding Agent Ecosystem — Week of 05 Apr

> **Generated**: 2026-04-12 08:00 UTC

## Ecosystem News

No significant news this week.

## New Releases This Week

### [openai/codex](openai/codex) — rust-v0.120.0

Published: *2026-04-11*

> ## New Features
- Realtime V2 can now stream background agent progress while work is still running and queue follow-up responses until the active response completes (#17264, #17306)
- Hook activity in the TUI is easier to scan, with live running hooks shown separately and completed hook output kept 

[View Release](https://github.com/openai/codex/releases/tag/rust-v0.120.0)

### [openai/codex](openai/codex) — rust-v0.121.0-alpha.2

Published: *2026-04-11*

> Release 0.121.0-alpha.2



[View Release](https://github.com/openai/codex/releases/tag/rust-v0.121.0-alpha.2)

### [openai/codex](openai/codex) — rust-v0.121.0-alpha.1

Published: *2026-04-11*

> Release 0.121.0-alpha.1



[View Release](https://github.com/openai/codex/releases/tag/rust-v0.121.0-alpha.1)

### [openai/codex](openai/codex) — rust-v0.120.0-alpha.3

Published: *2026-04-11*

> Release 0.120.0-alpha.3



[View Release](https://github.com/openai/codex/releases/tag/rust-v0.120.0-alpha.3)

### [openai/codex](openai/codex) — rust-v0.119.0

Published: *2026-04-10*

> ## New Features

- Realtime voice sessions now default to the v2 WebRTC path, with configurable transport, voice selection, native TUI media support, and app-server coverage for the new flow (#16960, #17057, #17058, #17093, #17097, #17145, #17165, #17176, #17183, #17188).
- MCP Apps and custom MCP s

[View Release](https://github.com/openai/codex/releases/tag/rust-v0.119.0)

### [anthropics/claude-code](anthropics/claude-code) — v2.1.101

Published: *2026-04-10*

> ## What's changed

- Added `/team-onboarding` command to generate a teammate ramp-up guide from your local Claude Code usage
- Added OS CA certificate store trust by default, so enterprise TLS proxies work without extra setup (set `CLAUDE_CODE_CERT_STORE=bundled` to use only bundled CAs)
- `/ultrapl

[View Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.101)

### [anthropics/claude-code](anthropics/claude-code) — v2.1.100

Published: *2026-04-10*

> 


[View Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.100)

### [anthropics/claude-code](anthropics/claude-code) — v2.1.98

Published: *2026-04-09*

> ## What's changed

- Added interactive Google Vertex AI setup wizard accessible from the login screen when selecting "3rd-party platform", guiding you through GCP authentication, project and region configuration, credential verification, and model pinning
- Added `CLAUDE_CODE_PERFORCE_MODE` env var:

[View Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.98)

### [anthropics/claude-code](anthropics/claude-code) — v2.1.97

Published: *2026-04-08*

> ## What's changed

- Added focus view toggle (`Ctrl+O`) in `NO_FLICKER` mode showing prompt, one-line tool summary with edit diffstats, and final response
- Added `refreshInterval` status line setting to re-run the status line command every N seconds
- Added `workspace.git_worktree` to the status li

[View Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.97)

### [anthropics/claude-code](anthropics/claude-code) — v2.1.96

Published: *2026-04-08*

> ## What's changed

- Fixed Bedrock requests failing with `403 "Authorization header is missing"` when using `AWS_BEARER_TOKEN_BEDROCK` or `CLAUDE_CODE_SKIP_BEDROCK_AUTH` (regression in 2.1.94)


[View Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.96)

### [langchain-ai/langgraph](langchain-ai/langgraph) — 1.1.7a1

Published: *2026-04-10*

> Changes since 1.1.6

* release(langgraph): 1.1.7a1 (#7476)
* test(langgraph): use monotonic clock in flaky streaming test (#7477)
* feat(langgraph): add graph lifecycle callback handlers (#7429)
* chore(deps): bump cryptography from 46.0.6 to 46.0.7 in /libs/langgraph (#7457)
* chore: update conform

[View Release](https://github.com/langchain-ai/langgraph/releases/tag/1.1.7a1)

### [langchain-ai/langgraph](langchain-ai/langgraph) — cli==0.4.21

Published: *2026-04-08*

> Changes since cli==0.4.20

* chore(cli): add validate command (#7438)

[View Release](https://github.com/langchain-ai/langgraph/releases/tag/cli%3D%3D0.4.21)

### [langchain-ai/langgraph](langchain-ai/langgraph) — cli==0.4.20

Published: *2026-04-08*

> Changes since cli==0.4.19

* release(cli): lockfile (#7436)
* chore: uv lock resolution (#7342)
* chore: bump langgraph version to 1.1.5 in CI and examples (#7435)
* chore(deps-dev): bump the minor-and-patch group in /libs/cli with 2 updates (#7378)
* chore(deps): bump the minor-and-patch group in /

[View Release](https://github.com/langchain-ai/langgraph/releases/tag/cli%3D%3D0.4.20)

### [langchain-ai/langgraph](langchain-ai/langgraph) — sdk==0.3.13

Published: *2026-04-07*

> Changes since sdk==0.3.12

* chore: validate reconnect url (#7434)
* feat(sdk-py): add langsmith_tracing param to runs.create/stream/wait (#7431)
* release: langgraph 1.1.6 (#7407)
* release: prebuilt 1.0.9 and langgraph 1.1.5 (#7401)
* release(langgraph): 1.1.4 (#7356)
* chore(deps): bump pygments 

[View Release](https://github.com/langchain-ai/langgraph/releases/tag/sdk%3D%3D0.3.13)

### [crewAIInc/crewAI](crewAIInc/crewAI) — 1.14.2a2

Published: *2026-04-10*

> ## What's Changed

### Features
- Add checkpoint TUI with tree view, fork support, and editable inputs/outputs
- Enrich LLM token tracking with reasoning tokens and cache creation tokens
- Add `from_checkpoint` parameter to kickoff methods
- Embed `crewai_version` in checkpoints with migration frame

[View Release](https://github.com/crewAIInc/crewAI/releases/tag/1.14.2a2)

### [crewAIInc/crewAI](crewAIInc/crewAI) — 1.14.2a1

Published: *2026-04-08*

> ## What's Changed

### Bug Fixes
- Fix emission of flow_finished event after HITL resume
- Fix cryptography version to 46.0.7 to address CVE-2026-39892

### Refactoring
- Refactor to use shared I18N_DEFAULT singleton

### Documentation
- Update changelog and version for v1.14.1

## Contributors

@gr

[View Release](https://github.com/crewAIInc/crewAI/releases/tag/1.14.2a1)

### [crewAIInc/crewAI](crewAIInc/crewAI) — 1.14.1

Published: *2026-04-08*

> ## What's Changed

### Features
- Add async checkpoint TUI browser
- Add aclose()/close() and async context manager to streaming outputs

### Bug Fixes
- Fix regex for template pyproject.toml version bumps
- Sanitize tool names in hook decorator filters
- Fix checkpoint handlers registration when Ch

[View Release](https://github.com/crewAIInc/crewAI/releases/tag/1.14.1)

### [crewAIInc/crewAI](crewAIInc/crewAI) — 1.14.1rc1

Published: *2026-04-08*

> ## What's Changed

### Features
- Add async checkpoint TUI browser
- Add aclose()/close() and async context manager to streaming outputs

### Bug Fixes
- Fix template pyproject.toml version bumps using regex
- Sanitize tool names in hook decorator filters
- Bump transformers to 5.5.0 to resolve CVE-

[View Release](https://github.com/crewAIInc/crewAI/releases/tag/1.14.1rc1)

### [crewAIInc/crewAI](crewAIInc/crewAI) — 1.14.0

Published: *2026-04-07*

> ## What's Changed

### Features
- Add checkpoint list/info CLI commands
- Add guardrail_type and name to distinguish traces
- Add SqliteProvider for checkpoint storage
- Add CheckpointConfig for automatic checkpointing
- Implement runtime state checkpointing, event system, and executor refactor

###

[View Release](https://github.com/crewAIInc/crewAI/releases/tag/1.14.0)

### [microsoft/semantic-kernel](microsoft/semantic-kernel) — python-1.41.2

Published: *2026-04-08*

> ## What's Changed
* Python: Improve prompt-template msg serialize and sample usage by @moonbox3 in https://github.com/microsoft/semantic-kernel/pull/13738
* Python: Update redis[hiredis] requirement from ~=6.0 to >=6,<8 in /python by @dependabot[bot] in https://github.com/microsoft/semantic-kernel

[View Release](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.41.2)

### [pydantic/pydantic-ai](pydantic/pydantic-ai) — v1.80.0

Published: *2026-04-10*

> <!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Add `CapabilityOrdering` (`innermost`, `outermost`, `wraps`, wrapped_by`, `requires`) by @DouweM in https://github.com/pydantic/pydantic-ai/pull/5036
* `Hooks` ordering parame

[View Release](https://github.com/pydantic/pydantic-ai/releases/tag/v1.80.0)

### [pydantic/pydantic-ai](pydantic/pydantic-ai) — v1.79.0

Published: *2026-04-10*

> <!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Full support for AG-UI 0.1.13 and 0.1.15: reasoning, multi-modal, `dump_messages` by @dsfaccini in https://github.com/pydantic/pydantic-ai/pull/3971
* Replace HTTP client cach

[View Release](https://github.com/pydantic/pydantic-ai/releases/tag/v1.79.0)

### [pydantic/pydantic-ai](pydantic/pydantic-ai) — v1.78.0

Published: *2026-04-08*

> <!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Add cached token span attributes per OTel spec by @alexmojaki in https://github.com/pydantic/pydantic-ai/pull/5013
* feat: add `return_schema` and `function_signature` to `Too

[View Release](https://github.com/pydantic/pydantic-ai/releases/tag/v1.78.0)


## Tracked Projects (11 total)

| Repo | Description | Stars | Language | Updated |
|------|-------------|-------|----------|---------|
| [openai/codex](https://github.com/openai/codex) | Lightweight coding agent that runs in your termina | 74,699 | Rust | 2026-04-12 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Build resilient language agents as graphs. | 28,995 | Python | 2026-04-12 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Framework for orchestrating role-playing, autonomo | 48,647 | Python | 2026-04-12 |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | User-friendly AI Interface (Supports Ollama, OpenA | 131,344 | Python | 2026-04-11 |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | Integrate cutting-edge LLM technology quickly and  | 27,689 | C# | 2026-04-11 |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | AI Agent Framework, the Pydantic way | 16,289 | Python | 2026-04-11 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude Code is an agentic coding tool that lives i | 112,728 | Shell | 2026-04-10 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Model Context Protocol Servers | 83,526 | TypeScript | 2026-03-29 |
| [TabbyML/tabby](https://github.com/TabbyML/tabby) | Self-hosted AI coding assistant | 33,405 | Rust | 2026-03-02 |
| [cursor/cursor](https://github.com/cursor/cursor) | The AI Code Editor | 32,624 | None | 2026-01-31 |
| [autogenhub/autogen](https://github.com/autogenhub/autogen) | A programming framework for agentic AI. Discord: h | 139 | Jupyter Notebook | 2025-02-05 |

## Metrics

| Metric | Value |
|--------|-------|
| Articles | 0 |
| Tracked Projects | 11 |
| New Releases | 23 |

---

*Report generated: 2026-04-12 08:00 UTC*
