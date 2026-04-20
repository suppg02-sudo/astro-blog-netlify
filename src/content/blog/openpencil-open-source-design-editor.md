---
pubDatetime: 2026-04-01T08:30:00Z
title: "OpenPencil: The Open-Source Design Editor That Reads .fig Files and Ships 90+ AI Tools"
postSlug: "openpencil-open-source-design-editor"
description: "OpenPencil is a MIT-licensed design editor that opens native Figma files, includes a built-in AI assistant with 90+ tools, offers a headless CLI, MCP server, and Vue SDK — all in a ~7 MB desktop app. "
tags:
  - figma-alternative
  - design-tools
  - mcp
  - open-source
  - design-to-code
  - ai
---

# OpenPencil: The Open-Source Design Editor That Reads .fig Files and Ships 90+ AI Tools

> **TL;DR**: OpenPencil is a MIT-licensed design editor that opens native Figma files, includes a built-in AI assistant with 90+ tools, offers a headless CLI, MCP server, and Vue SDK — all in a ~7 MB desktop app. It's the programmable alternative to Figma that keeps your design files under your control.

## Quick Summary

- Opens `.fig` and `.pen` files natively — full read/write Figma compatibility
- Built-in AI chat with 90+ design tools, supporting Anthropic, OpenAI, Google AI, OpenRouter, Z.ai, and MiniMax
- Headless CLI for inspecting, linting, analyzing, and exporting design files from the terminal
- MCP server for AI coding agents (Claude Code, Cursor, Windsurf) to modify designs programmatically
- Real-time P2P collaboration via WebRTC — no server, no account required
- ~7 MB Tauri v2 desktop app for macOS, Windows, and Linux, plus browser PWA

## Why OpenPencil Matters

Figma is a closed platform that actively fights programmatic access. Their MCP server is read-only. [figma-use](https://github.com/dannote/figma-use) added full read/write automation via CDP — then [Figma 126 killed CDP](https://forum.figma.com/report-a-problem-6/remote-debugging-port-not-working-in-figma-desktop-126-1-2-50858). Your design files live in a proprietary binary format that only their software can fully read. Your workflows break when they ship a point release.

OpenPencil is the alternative: open source under MIT, reads `.fig` files natively, every operation is scriptable, and your data never leaves your machine.

## The Editor

OpenPencil is a full-featured design editor built with Vue 3 and Skia (CanvasKit WASM) rendering. It supports:

- **Drawing tools**: Rectangle, Ellipse, Line, Polygon, Star, Pen (vector networks with bezier curves)
- **Rich text**: Inline editing with per-character formatting (bold, italic, underline), style runs, and CJK/RTL support
- **Auto layout**: Flex and CSS Grid via Yoga WASM, with gap, padding, alignment, and track sizing
- **Components**: Components, instances, component sets with live sync and override preservation
- **Variables**: Collections, modes, color bindings, and alias chains
- **Effects**: Drop shadow, inner shadow, shadow spread, layer blur, background blur
- **Multi-page documents**: Independent viewport state, tabbed interface
- **Export**: PNG, JPG, WEBP, SVG, JSX/Tailwind, and `.fig` output

The app weighs ~7 MB thanks to Tauri v2 (Rust backend), runs on macOS, Windows, and Linux, and also works as a browser-based PWA at [app.openpencil.dev](https://app.openpencil.dev).

## The AI Layer

Press `Cmd+J` to open the built-in AI assistant. It has 90+ tools that can create shapes, set fills and strokes, manage auto-layout, work with components and variables, run boolean operations, analyze design tokens, and export assets. You bring your own API key for OpenRouter, Anthropic, OpenAI, Google AI, Z.ai, or MiniMax. No backend, no account.

The AI workflow uses a skeleton-first approach: plan the layout, generate a skeleton, fill content via `replace_id`, then polish. Batched tools like `calc`, `stock_photo`, and `batch_update` keep interactions efficient. Visual feedback shows a blue pulsing border on nodes being modified and a green flash on completion.

### Coding Agents

On desktop, you can use Claude Code, Codex, or Gemini CLI directly in the chat panel. The agent connects to the editor's MCP server and uses all 90+ design tools. This means your AI coding assistant can inspect designs, export assets, analyze tokens, and modify `.fig` files headlessly.

## The CLI

The `@open-pencil/cli` package turns design files into programmable artifacts:

```bash
# Inspect the node tree
open-pencil tree design.fig

# Find all text nodes
open-pencil find design.fig --type TEXT

# XPath queries
open-pencil query design.fig "//FRAME[@width < 300]"
open-pencil query design.fig "//TEXT[contains(@name, 'Button')]"

# Export as Tailwind JSX
open-pencil export design.fig -f jsx --style tailwind

# Lint naming, layout, accessibility
open-pencil lint design.fig

# Analyze design tokens
open-pencil analyze colors design.fig
open-pencil analyze typography design.fig
open-pencil analyze clusters design.fig

# Script with Figma Plugin API
open-pencil eval design.fig -c "figma.currentPage.selection.forEach(n => n.opacity = 0.5)" -w
```

When the desktop app is running, the CLI connects via RPC and operates on the live canvas — useful for automation scripts, CI pipelines, or AI agents.

## The MCP Server

Connect any MCP client to inspect, modify, and export design documents headlessly:

```bash
bun add -g @open-pencil/mcp
```

Configure in Claude Code, Cursor, or Windsurf:

```json
{
  "mcpServers": {
    "open-pencil": {
      "command": "openpencil-mcp"
    }
  }
}
```

Or run as an HTTP server for scripts and CI:

```bash
openpencil-mcp-http  # http://localhost:3100/mcp
```

The MCP server exposes 90 tools (87 core + 3 file management) covering node CRUD, layout, variables, boolean operations, vector paths, analysis, and export.

## The Vue SDK

For building custom editors or embedding OpenPencil into other applications, the `@open-pencil/vue` package provides headless components and composables. This lets you create workflow-specific editing surfaces without reimplementing the rendering engine, scene graph, or file format handling.

## Real-Time Collaboration

Share a link to co-edit in real time. Peers connect directly via WebRTC using Trystero + Yjs CRDT. No server, no account — cursors, selections, and edits sync peer-to-peer. Click a collaborator's avatar to follow their viewport.

## The Tech Stack

| Layer | Technology |
|-------|-----------|
| Rendering | Skia (CanvasKit WASM) |
| Layout | Yoga WASM (flex + grid) |
| UI | Vue 3, Reka UI, Tailwind CSS 4 |
| File format | Kiwi binary + Zstd + ZIP |
| Collaboration | Trystero (WebRTC P2P) + Yjs (CRDT) |
| Desktop | Tauri v2 (Rust) |
| AI/MCP | Multi-provider, MCP SDK, Hono |

## Design-to-Code Export

OpenPencil exports selections as JSX with Tailwind CSS v4 utility classes:

```bash
open-pencil export design.fig -f jsx --style tailwind
```

Output:
```jsx
<div className="flex flex-col gap-4 p-6 bg-white rounded-xl">
  <p className="text-2xl font-bold text-[#1D1B20]">Card Title</p>
  <p className="text-sm text-[#49454F]">Description text</p>
</div>
```

This works from the Code panel in the editor, the CLI, or the MCP server — making it straightforward to go from design to code in any workflow.

<details>
<summary>Deep Dive: Project Structure and Testing</summary>

### Project Structure

```
packages/
  core/           @open-pencil/core — engine (scene graph, renderer, layout, file formats, tools)
  vue/            @open-pencil/vue — headless Vue SDK
  cli/            @open-pencil/cli — headless CLI
  mcp/            @open-pencil/mcp — MCP server (stdio + HTTP)
  docs/           Documentation site (openpencil.dev)
src/              Vue app (components, composables, stores)
desktop/          Tauri v2 (Rust + config)
tests/            E2E (188 tests) + unit (764 tests)
```

### Quality

The project has 188 E2E tests and 764 unit tests, visual regression testing via Playwright, and linting via oxlint. Recent releases show rapid iteration — v0.1.0-alpha shipped March 1, 2026, and v0.11.2 followed on March 30, with 1,027 commits across 20 releases.

### Getting Started

```bash
# Clone and run
git clone https://github.com/open-pencil/open-pencil.git
cd open-pencil
bun install
bun run dev        # Dev server at localhost:1420
bun run tauri dev  # Desktop app (requires Rust)
```

Or install via Homebrew:

```bash
brew install open-pencil/tap/open-pencil
```

</details>

<details>
<summary>References & Further Reading</summary>

- [OpenPencil GitHub Repository](https://github.com/open-pencil/open-pencil) — Source code, issues, releases
- [OpenPencil Documentation](https://openpencil.dev) — User guide, reference, architecture docs
- [Try it Online](https://app.openpencil.dev/demo) — No installation required
- [MCP Tools Reference](https://openpencil.dev/reference/mcp-tools) — Full list of 90 MCP tools
- [Vue SDK Documentation](https://openpencil.dev/programmable/sdk/) — Headless SDK for custom editors
- [AI Agent Skills](https://skills.sh) — Teach AI coding agents to use OpenPencil via `npx skills add open-pencil/skills@open-pencil`
- [Yoga Grid Fork](https://github.com/open-pencil/yoga/tree/grid) — CSS Grid support for Yoga layout engine
- [figma-use](https://github.com/dannote/figma-use) — Predecessor project for Figma automation via CDP

</details>

**Tags**: open-source, design-tools, figma-alternative, ai, mcp, design-to-code
**Categories**: AI Automation, Open Source Spotlight
