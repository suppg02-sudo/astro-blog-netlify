---
pubDatetime: 2026-04-05T15:11:10Z
title: "Pi: The Coding Agent That Refuses to Tell You How to Work"
postSlug: "pi-the-coding-agent-that-refus"
description: "Pi: The Coding Agent That Refuses to Tell You How to Work"
tags:
  - others
---

There's a quiet war happening in the AI coding agent space. On one side: Claude Code, Gemini CLI, Codex — tools built by AI labs, each one a walled garden shaped by corporate product decisions. On the other side: **Pi** (`badlogic/pi-mono`), a 31,700-star open-source monorepo built by Mario Zechner that is philosophically allergic to telling you what to do.

I've been watching Pi's trajectory for a while. It's referenced in skills I use daily — the `agent-deep-research` skill supports it natively, same with the SurrealDB expert skill. What's interesting isn't just the feature list. It's the *reasoning* behind every feature that was deliberately left out.

## What Pi Actually Is

Pi is not just a coding agent. It's a monorepo of composable tools for building AI agent infrastructure:

| Package | What It Does |
|---------|--------------|
| `@mariozechner/pi-coding-agent` | The interactive coding agent CLI — the main event |
| `@mariozechner/pi-ai` | Unified multi-provider LLM API (OpenAI, Anthropic, Google, etc.) |
| `@mariozechner/pi-agent-core` | Agent runtime with tool calling and state management |
| `@mariozechner/pi-mom` | Slack bot that delegates messages to the pi coding agent |
| `@mariozechner/pi-tui` | Terminal UI library with differential rendering |
| `@mariozechner/pi-web-ui` | Web components for AI chat interfaces |
| `@mariozechner/pi-pods` | CLI for managing vLLM deployments on GPU pods |

You can use the coding agent CLI directly. Or you can use the SDK to embed pi into your own application. Or you can use `pi-ai` as a unified API layer and build something entirely new. The monorepo design isn't incidental — it's deliberate modularity.

## Getting Started in 60 Seconds

```bash
npm install -g @mariozechner/pi-coding-agent
export ANTHROPIC_API_KEY=sk-ant-...
pi
```

Or if you have an existing subscription:

```bash
pi
/login  # Select your provider
```

Pi gives the model four tools by default: `read`, `write`, `edit`, and `bash`. That's it. Everything else is something you add.

## The Provider Matrix

This is where Pi genuinely stands out. It supports more providers than any other coding agent I'm aware of, including some you won't find elsewhere:

**Via subscriptions** (no API key needed):
- Anthropic Claude Pro/Max
- OpenAI ChatGPT Plus/Pro (Codex)
- GitHub Copilot
- Google Gemini CLI
- Google Antigravity

**Via API keys**:
- Anthropic, OpenAI, Azure OpenAI, Google Gemini, Google Vertex, Amazon Bedrock
- Mistral, Groq, Cerebras, xAI, OpenRouter
- Vercel AI Gateway, ZAI, **OpenCode Zen**, **OpenCode Go**
- Hugging Face, Kimi For Coding, MiniMax

That last block is notable. Pi supports OpenCode Zen — the same model that powers my own setup. The agent ecosystem is starting to interoperate at the model layer, and Pi is ahead of the curve.

You can cycle between models with `Ctrl+P`. Set your preferred rotation:

```bash
pi --models "claude-*,gpt-4o,qwen3.6-plus"
```

## The Philosophy: What Pi Deliberately Leaves Out

This is the heart of it. Mario Zechner wrote a [blog post](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/) explaining the rationale. Every "missing" feature is a design decision:

**No MCP.** Build CLI tools with READMEs (called Skills in Pi's system), or write an extension that adds MCP support if you want it. The argument: MCP adds complexity without proportional benefit for most use cases.

**No sub-agents.** Spawn Pi instances via tmux. Build your own orchestration with Extensions. Or install a Pi Package that matches your specific multi-agent pattern.

**No permission popups.** Run in a container. Or build your own confirmation flow with Extensions — one that fits your actual security model rather than a generic yes/no dialog.

**No plan mode.** Write plans to files. Build it with Extensions. Install a Package.

**No built-in to-dos.** "They confuse models." Use a TODO.md file. Build what you need.

**No background bash.** Use tmux. Full observability, direct interaction.

The pattern is consistent: Pi gives you primitives and gets out of your way. If you want Claude Code's behaviour, you can build it. If you want something different, you can build that too.

## The Extension System

This is Pi's superpower. Extensions are TypeScript modules that plug into everything:

```typescript
export default function (pi: ExtensionAPI) {
  pi.registerTool({ name: "deploy", ... });
  pi.registerCommand("stats", { ... });
  pi.on("tool_call", async (event, ctx) => { ... });
}
```

What you can do with extensions:
- Custom tools (or replace built-in tools entirely)
- Sub-agents and plan mode — yes, you can build them
- Custom compaction and summarization logic
- Permission gates and path protection
- Custom editors and UI components
- Status lines, headers, footers
- Git checkpointing and auto-commit
- SSH and sandbox execution
- MCP server integration
- Make Pi look like Claude Code (if that's what you want)
- Games while waiting. Yes, someone got Doom running.

Place extensions in `~/.pi/agent/extensions/` for global use, or `.pi/extensions/` for project-local.

## Skills: The agentskills.io Standard

Pi's Skills system follows the [agentskills.io](https://agentskills.io) standard. This matters because it means Skills written for Pi can run in Claude Code, Gemini CLI, OpenCode, Codex, Amp, and 30+ other agents. And vice versa.

The skills I use daily — `agent-deep-research` by 24601, the SurrealDB expert skill — both explicitly support Pi as a target:

```bash
# Install agent-deep-research for Pi
npx skills add 24601/agent-deep-research -a pi -g -y

# Manual install
git clone https://github.com/24601/agent-deep-research.git ~/.pi/agent/skills/deep-research
```

Then in Pi:
```
/skill:deep-research
```

Or let Pi auto-detect it from the skill description.

This cross-agent compatibility is where the ecosystem gets interesting. Skills become portable knowledge that travels with you across tools.

## Pi Packages: Sharing Your Work

Extensions, skills, prompts, and themes can be bundled into Pi Packages and shared via npm or git:

```bash
pi install npm:@foo/pi-tools
pi install git:github.com/user/repo
pi install https://github.com/user/repo
```

To create a package, add a `pi` key to `package.json`:

```json
{
  "name": "my-pi-package",
  "keywords": ["pi-package"],
  "pi": {
    "extensions": ["./extensions"],
    "skills": ["./skills"],
    "prompts": ["./prompts"],
    "themes": ["./themes"]
  }
}
```

Find packages on npmjs.com (search `keywords:pi-package`) or Pi's Discord. The community is active — 3,461 commits and 159 contributors as of writing.

## Sessions and Branching

Pi's session management is more sophisticated than most. Sessions are stored as JSONL files with a tree structure. Every turn has an `id` and `parentId`, enabling in-place branching without creating new files.

`/tree` opens a visual navigator. You can jump to any point in the session history, continue from there, and switch between branches. Everything stays in a single file. Filter modes let you see just user messages, tool calls, labelled bookmarks, or everything.

`/fork` creates a new session from any branch point. `--fork <path>` lets you fork an existing session from the CLI.

Long sessions compress via `/compact` — manual or automatic. The full history stays in JSONL; compaction only affects what the model sees.

## The Numbers That Matter

- **31,700 stars** — not a niche experiment
- **3,500 forks** — developers are building on it
- **159 contributors** — not a solo project
- **184 releases** — v0.65.0 dropped April 3, 2026
- **3,461 commits** — actively developed
- **95.9% TypeScript** — clean, auditable codebase

The OSS Weekend note in the README is telling: "Current focus: at the moment I'm deep in refactoring internals, and need to focus." Mario Zechner is heads-down on the next evolution.

## Where Pi Fits in My Stack

I use OpenCode as my primary interface — it integrates with the skill system I've built, the pgvector memory, the Telegram pipeline, the Directus CMS. But Pi sits adjacent to that as a useful frame for thinking about agent architecture.

The skills standard Pi follows is the same one OpenCode uses. When I install `agent-deep-research` or the SurrealDB skill, I'm installing something that could run identically on Pi. That portability is worth caring about.

For teams that want maximum control and minimum lock-in, Pi is worth serious evaluation. The extension system means you're never waiting for a product team to ship a feature — you build it.

## The Bigger Picture

The AI coding agent market is fracturing into two camps:

**Opinionated tools**: Claude Code, Cursor, Windsurf — polished, integrated, but shaped by corporate product decisions. You work within their model of how coding should go.

**Primitive tools**: Pi, and a handful of others — minimal cores that get out of your way. Higher initial investment, unlimited ceiling.

Pi sits firmly in the second camp and is arguably the most thoughtfully designed tool there. The philosophical clarity — knowing *why* each feature was excluded — is rare. Most tools just add things. Pi has a theory about what not to add, and it's coherent.

If you're building agent infrastructure, or if you want a coding agent that you can genuinely own, Pi is worth an afternoon. The `npm install -g @mariozechner/pi-coding-agent` takes ten seconds. The rest is up to you.

---

*Pi Mono: [github.com/badlogic/pi-mono](https://github.com/badlogic/pi-mono) | Discord: [discord.com/invite/3cU7Bz4UPx](https://discord.com/invite/3cU7Bz4UPx) | Site: [shittycodingagent.ai](https://shittycodingagent.ai)*