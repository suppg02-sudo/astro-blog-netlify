---
pubDatetime: 2026-02-10T15:34:03Z
title: "Build a Multi-User AI Chat App with Convex and Claude"
postSlug: "build-multiuser-ai-chat-app-convex-claude"
description: "Learn how to build a real-time multi-user AI chat app using Convex, Anthropic Claude Haiku, and Google APIs — with tool calling, reactive subscriptions, and server-side security."
tags:
  - tanstack
  - real-time
  - tool-calling
  - vercel-ai-sdk
  - full-stack
  - convex
  - chat-app
  - ai
  - claude-haiku
  - tutorial
  - anthropic
---

> *"Technically, I gotta tell you, this project would've been a real pain in the butt without Convex."*
> — Jack Herrington, Blue Collar Coder [[00:22]](https://www.youtube.com/watch?v=FL_UiNpGgEg&t=22s)

**Source**: [How to Build a Multi-User AI Chat App with Convex](https://www.youtube.com/watch?v=FL_UiNpGgEg) by Jack Herrington (Blue Collar Coder) | 11m 29s

---

## Overview

Jack Herrington walks through the architecture of a **real-time, multi-user AI-powered dinner coordination chat app** — and the result is a masterclass in how modern full-stack AI apps are structured.

The app lets multiple users:
- Share a **synchronized chat thread** in real time
- Trigger an **AI assistant** with `@ai` to get restaurant recommendations
- Manage a **collaborative shortlist** with voting
- Visualize restaurants on a **Google Map**

The tech stack is lean but powerful: **Convex** (real-time DB + serverless backend), **Anthropic Claude Haiku** (LLM), **Vercel AI SDK** (LLM integration layer), **TanStack Start** (React UI framework), and **Google Places/Maps APIs**.

---

## Architecture Overview

{{< mermaid >}}
graph TD
    subgraph "Browser (Client)"
        UI["TanStack Start UI"]
        useChatInput["useChatInput\n(useAction hook)"]
        useUIMessages["useUIMessages\n(reactive subscription)"]
        useQuery["useQuery\n(shortlist subscription)"]
        MapPanel["Google Maps Panel"]
        ShortlistPanel["Shortlist + Voting Panel"]
    end

    subgraph "Convex Backend"
        sendMessage["sendMessage\n(public action)"]
        saveMessage["saveMessage\n(direct save)"]
        dinnerAgent["dinnerAgent\n(Convex Agent)"]
        streamText["streamText\n(Vercel AI SDK)"]
        internalMutations["Internal Mutations\n(server-only)"]
        DB[("Convex Real-Time DB")]
    end

    subgraph "External APIs"
        ClaudeHaiku["Anthropic\nClaude Haiku"]
        GooglePlaces["Google Places API"]
        GoogleMaps["Google Maps JS API"]
    end

    UI --> useChatInput
    useChatInput -->|"api.chat.sendMessage"| sendMessage
    sendMessage -->|"no @ai"| saveMessage
    sendMessage -->|"@ai trigger"| dinnerAgent
    dinnerAgent --> streamText
    streamText <-->|"tool calls"| ClaudeHaiku
    streamText -->|"searchRestaurants"| GooglePlaces
    streamText -->|"addToShortlist"| internalMutations
    internalMutations --> DB
    saveMessage --> DB
    DB -->|"real-time push"| useUIMessages
    DB -->|"real-time push"| useQuery
    useUIMessages --> UI
    useQuery --> ShortlistPanel
    GoogleMaps --> MapPanel
{{< /mermaid >}}

---

## The Architectural Philosophy [[00:45]](https://www.youtube.com/watch?v=FL_UiNpGgEg&t=45s)

Jack opens with a refreshing take on tutorials in the age of AI coding assistants:

> *"I don't think a walkthrough makes a lot of sense in the world of LLMs and agents and agentic coding. What I do think makes sense is actually just kind of walking you through the application and talking about the high level architectural points so that when you ask your agent to do stuff on your behalf, you understand what's doing."*

This is the right framing. **Understanding architecture beats memorizing syntax** — especially when your AI coding assistant can generate the boilerplate for you.

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | TanStack Start | React-based full-stack UI framework |
| **Backend** | Convex | Real-time database + serverless functions |
| **AI Model** | Anthropic Claude Haiku | Cost-efficient LLM for chat responses |
| **AI SDK** | Vercel AI SDK | Tool-calling protocol abstraction |
| **Maps** | Google Places + Maps JS API | Restaurant search + visualization |

**Why Claude Haiku?** [[02:17]](https://www.youtube.com/watch?v=FL_UiNpGgEg&t=137s) — Keeping costs lower while still providing capable AI responses for high-frequency interactive chat.

---

## Setup Requirements [[01:42]](https://www.youtube.com/watch?v=FL_UiNpGgEg&t=102s)

To run this project yourself:

1. Clone the source code from GitHub
2. Configure environment variables
3. Run `convex init` and `convex dev`
4. Obtain a **Google API key** (Places API + Maps JavaScript API enabled)
5. Obtain an **Anthropic API key**

Convex is **open-source** and can run locally or via Convex cloud hosting — no code changes required between environments.

---

## Message Flow: Non-AI Path [[03:47]](https://www.youtube.com/watch?v=FL_UiNpGgEg&t=227s)

The core message flow is elegantly simple:

1. **Browser** calls `sendMessage` on Convex via `useAction`
2. **Convex** adds the message to the database
3. **`useUIMessages`** reactive subscription automatically pushes updates to **all connected browsers**

```
Browser → api.chat.sendMessage → Convex DB → useUIMessages → All Browsers
```

The client-side code is minimal [[04:52]](https://www.youtube.com/watch?v=FL_UiNpGgEg&t=292s):

```typescript
// useChatInput — just bind useAction to the sendMessage endpoint
const sendMessage = useAction(api.chat.sendMessage);
```

No WebSocket management. No polling. No manual state sync. **Convex handles it all.**

---

## The `@ai` Trigger [[05:19]](https://www.youtube.com/watch?v=FL_UiNpGgEg&t=319s)

The server-side `sendMessage` action checks for the `@ai` mention:

- **No `@ai`** → calls `saveMessage` directly (plain chat message)
- **Has `@ai`** → fires off a request to `dinnerAgent` with the prompt, sender name, and content

This is a smart UX pattern: **users explicitly opt-in to AI**, reducing unnecessary LLM calls and costs.

**Real-time streaming** [[05:38]](https://www.youtube.com/watch?v=FL_UiNpGgEg&t=338s): `useUIMessages` subscribes with `streaming: true`, so AI response chunks arrive in real time as Claude generates them.

---

## The `dinnerAgent` and Its Tools [[06:37]](https://www.youtube.com/watch?v=FL_UiNpGgEg&t=397s)

The agent is defined as a **Convex Agent** using Anthropic via the Vercel AI SDK. It has a system prompt and six tools:

**Server-side tools** (can mutate data and call external APIs):
- `searchRestaurants` — queries Google Places API
- `getRestaurantDetails` — fetches details for a specific place
- `addToShortlist` — adds a restaurant to the collaborative list
- `removeFromShortlist` — removes from the list

**Client-side tools** (trigger UI effects):
- `showOnMap` — pans the map to a restaurant
- `highlightShortlistItem` — highlights an item in the shortlist panel

This **separation of concerns** is elegant: UI effects and data mutations are handled at the appropriate layer.

---

## Tool Calling: The Protocol Explained [[07:24]](https://www.youtube.com/watch?v=FL_UiNpGgEg&t=444s)

> *"Tool calls are the only way to really do anything cool with an LLM. Without tool calls an LLM just knows what it knows."*

The tool-calling dance works like this:

1. Browser sends `@ai` message
2. Agent calls `streamText` with messages + tool list
3. **Claude returns a tool-call instruction** (not a text response)
4. Agent executes the tool (e.g., `searchNearbyInternal` → Google Places API)
5. **JSON result appended** to the message stream
6. Claude synthesizes a **markdown response** from the tool result

The Vercel AI SDK abstracts this entire request-response-tool-result loop — without it, you'd implement this cycle manually against the Anthropic API.

### Tool Description Best Practice [[08:50]](https://www.youtube.com/watch?v=FL_UiNpGgEg&t=530s)

> *"You need to tell the LLM when and why it should call this tool. [The description is] critical."*

Use `createTool` with **highly descriptive descriptions and argument descriptions**. The LLM uses these to decide when and how to invoke each tool. Poor descriptions = unreliable tool selection.

---

## Security: Internal Mutations [[03:16]](https://www.youtube.com/watch?v=FL_UiNpGgEg&t=196s)

Convex's **internal functions** are server-locked — they cannot be invoked from the client, even if the client is compromised.

- `searchNearbyInternal` — Google Places queries stay server-side
- `addInternal` — shortlist mutations are server-only

The `addInternal` implementation [[10:33]](https://www.youtube.com/watch?v=FL_UiNpGgEg&t=633s) is just a standard `db.insert` call — but because it's marked internal, the AI can only affect state through **explicitly defined, server-validated pathways**.

---

## Real-Time Shortlist with Voting [[09:40]](https://www.youtube.com/watch?v=FL_UiNpGgEg&t=580s)

The collaborative shortlist panel uses `useQuery` to subscribe to the shortlist data:

- **AI adds restaurants** via `addToShortlist` tool → `addInternal` mutation
- **Users vote** via voting mutations
- **Panel updates automatically** whenever the shortlist changes

No manual refresh. No polling. The shortlist transforms a simple chat app into a **group decision-making tool** — AI + real-time DB enabling collaborative workflows.

---

## Key Architectural Insights

- **Reactive subscriptions eliminate complexity**: `useUIMessages` and `useQuery` replace WebSocket management, polling, and manual state sync entirely
- **`@ai` mention pattern**: Elegant UX that gives users explicit control over AI invocation, reducing unnecessary LLM calls
- **Tool descriptions are critical**: The quality of tool descriptions directly determines how reliably Claude decides when and how to use them
- **Internal mutations as security boundary**: AI-triggered state changes go through server-validated pathways only
- **Local vs. cloud Convex**: Open-source option gives flexibility for dev/test vs. production without code changes
- **Cost-conscious model selection**: Claude Haiku keeps costs manageable for high-frequency interactive chat

---

## Getting Started

Jack's call to action [[11:05]](https://www.youtube.com/watch?v=FL_UiNpGgEg&t=665s): Download the source code, use Claude Code or your preferred IDE, and build your own multi-user AI-enabled chat application.

The full source is available on GitHub (linked in the video description). The architecture patterns here — reactive subscriptions, internal mutations, tool-calling agents — are directly applicable to any real-time AI application you want to build.

---

## References

- **Video**: [How to Build a Multi-User AI Chat App with Convex](https://www.youtube.com/watch?v=FL_UiNpGgEg) — Jack Herrington, Blue Collar Coder
- **Full transcript**: `/media/docs/output/youtube_How_to_Build_a_MultiUser_AI_Chat_App_with_Convex_FL_UiNpGgEg_20260210_153403.txt`
- **Short summary**: `/media/docs/output/youtube_How_to_Build_a_MultiUser_AI_Chat_App_with_Convex_FL_UiNpGgEg_summary_short.json`