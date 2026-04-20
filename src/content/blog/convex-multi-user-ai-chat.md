---
pubDatetime: 2026-02-10T22:02:54Z
title: "Building Real-Time Multi-User AI Chat Apps with Convex"
postSlug: "convex-multi-user-ai-chat"
description: "Building Real-Time Multi-User AI Chat Apps with Convex"
tags:
  - Convex
  - AI
  - Real-time
  - React
  - Tutorial
---

Building real-time, multi-user applications with AI capabilities used to be a complex challenge. But with modern tools like Convex, creating applications that sync across multiple users and integrate with large language models has become surprisingly accessible.

In this guide, I'll walk you through building a multi-user dinner coordination chat application powered by Convex's real-time database, Anthropic's Claude LLM, and Google's Places and Maps APIs. We'll explore the architecture, see how tool calling enables AI to interact with real-world APIs, and understand how to secure your application by running sensitive operations server-side.

## What We're Building

Our application is a dinner coordination system where multiple users can:

- **Chat in real-time** with synchronized UI across all participants
- **Get AI-powered restaurant recommendations** by tagging messages with `@ai`
- **View restaurants on an interactive map** using Google Maps integration
- **Vote on restaurant options** using a shared shortlist system
- **See instant updates** as any user adds messages, restaurants, or votes

The demo shows two users, "Jacksone" and "Joe", chatting simultaneously with their UIs perfectly synchronized. This real-time sync happens automatically through Convex's subscription system—no manual polling or refresh needed.

## Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| Frontend | TanStack Start | React-based UI framework |
| Database | Convex | Real-time database with subscriptions |
| AI/LLM | Anthropic Claude Haiku | Restaurant recommendations and chat AI |
| AI SDK | Vercel AI SDK | Tool calling and LLM integration |
| Maps | Google JavaScript Maps API | Restaurant location display |
| Places | Google Places API | Restaurant search and details |

This combination gives us real-time synchronization, AI capabilities, and external API access—all while maintaining security by keeping sensitive operations server-side.

## Setting Up the Project

### Prerequisites

Before diving in, you'll need:

1. **Convex account** — Create a free account or run Convex locally (it's open source)
2. **Google API key** — Requires access to Google Places API and JavaScript Maps API
3. **Anthropic API key** — We'll use Claude Haiku for cost efficiency
4. **Source code** — Clone the repository from GitHub (link in the video description)

### Initial Setup

Once you've cloned the repository:

1. Run `npm install` to install dependencies
2. Execute `convex init` and `convex dev` to initialize your Convex deployment
3. Set environment variables in Convex configuration:
   - `ANTHROPIC_API_KEY` — Your Claude API key
   - `GOOGLE_API_KEY` — Your Google API key for Places and Maps

The Convex configuration is where the magic happens. All AI operations and API calls run on the Convex server, not on the client. This is crucial for security—your API keys stay protected because the client never directly accesses them.

## Architecture Overview

### The Convex Real-Time Database

Convex is the backbone of this application. It provides:

- **Automatic real-time sync** — Subscriptions push updates to all connected users
- **Server-side functions** — Run queries, mutations, and actions on the server
- **Function locking** — Restrict sensitive operations to server-only execution
- **Streaming support** — Get incremental updates as they happen

### Key Data Models

- **Thread** — Conversation metadata for each chat session
- **Messages** — Individual chat messages with content, sender, timestamp, and AI flag
- **Shortlist** — Restaurants being voted on with vote counts
- **Votes** — Individual votes for restaurants in the shortlist

### Security by Design

Convex supports "locking" functions so they can only run on the server. This is powerful for security:

- **Locked functions** — Places requests and database mutations are server-only
- **API key protection** — Client can't access sensitive API keys
- **Controlled surface area** — You decide exactly what clients can access

If someone hacks the client, they can't run locked functions or access your API keys because those operations only execute on the server.

## How Messages Flow

### Sending a Message

The message flow is elegantly simple:

1. **User sends message** — Browser calls `sendMessage` function via Convex
2. **Server processing** — Message is processed on Convex server
3. **AI detection** — Server checks if message contains `@ai` tag
4. **Routing**:
   - **Without `@ai`** — Direct save to message list via `saveMessage`
   - **With `@ai`** — Forwarded to `dinnerAgent` for LLM processing
5. **Real-time updates** — All subscribed browsers receive updates automatically

### Client-Side Code

On the client, sending a message is straightforward:

```javascript
import { useAction } from "convex/react";

const sendMessage = useAction(api.chat.sendMessage);

// Invoke with message
sendMessage(messageText);
```

### Subscribing to Messages

Subscribing to updates is equally simple:

```javascript
import { useQuery } from "convex/react";

// Subscribe to all messages in the thread
const messages = useQuery(api.chat.listAllMessages, { threadId: "thread-id" }, {
  streaming: true  // Enable real-time updates
});
```

The `streaming: true` option is what enables real-time synchronization. When any user adds a message, all subscribed clients receive the update automatically—no manual refresh needed.

## AI Integration and Tool Calling

### What Happens When You Use `@ai`

When a user sends a message tagged with `@ai` (like "@ai Thai restaurants?"):

1. Message sent to Convex server via `sendMessage`
2. Server detects `@ai` and forwards to `dinnerAgent`
3. Agent fires request to Anthropic LLM via Vercel AI SDK
4. LLM may make tool calls (searchRestaurants, getRestaurantDetails, etc.)
5. Tool results returned to LLM
6. LLM formats response in markdown
7. Response displayed in chat

### The AI Agent Configuration

The `dinnerAgent` is defined with:

- **System prompt** — Defines the agent's behavior and role
- **Language model** — Anthropic Claude (via Vercel AI SDK)
- **Tools** — Set of callable functions for real-world interactions
- **Name** — Identifier for the agent

### Tool Calling: The "Choreographed Dance"

Tool calling is what enables an LLM to interact with the real world—beyond just its training data. The flow works like this:

1. **Browser** sends `@ai` message to server
2. **Agent** calls `streamText` with message and tools
3. **LLM** analyzes message and decides it needs data
4. **LLM** adds formatted tool call request to message stream
5. **Agent** executes the requested tool (e.g., `searchRestaurants`)
6. **Tool handler** makes actual API call (Google Places)
7. **Results** packaged as JSON and returned to LLM
8. **LLM** formats response using tool data
9. **Markdown response** displayed in chat

The Vercel AI SDK handles this "choreographed dance" automatically—you just define your tools and descriptions, and the SDK manages the back-and-forth with the LLM.

### Defining Tools

Tools need clear, descriptive definitions. The LLM uses these descriptions to understand when and why to call each tool:

```javascript
const searchRestaurants = createTool({
  description: "Search for restaurants in Portland based on a query",
  parameters: {
    query: {
      type: "string",
      description: "The search query (e.g., 'Thai restaurants', 'Greek food near downtown')"
    }
  },
  handler: async ({ query }) => {
    // Call Google Places API via internal function
    return await searchNearbyInternal(query);
  }
});
```

### Available Tools in the App

1. **searchRestaurants** — Search Google Places for restaurants
2. **getRestaurantDetails** — Get detailed information about a specific restaurant
3. **addToShortlist** — Add restaurant to voting shortlist (server-side mutation)
4. **removeFromShortlist** — Remove restaurant from shortlist (server-side mutation)
5. **showOnMap** — Display restaurant on map (client-side tool)
6. **highlightShortlistItem** — Highlight item in shortlist (client-side tool)

## Real-Time Shortlist and Voting

The shortlist feature demonstrates the real-time capabilities perfectly:

- Users can ask the AI to add restaurants to the shortlist
- Restaurants appear on both the map and the shortlist panel
- Users vote on restaurants using the voting interface
- All changes sync across all connected users instantly

### Server-Side Mutations

Adding to the shortlist uses an internal mutation:

```javascript
export const addInternal = mutation({
  handler: async (ctx, args) => {
    // Only server can execute this
    return await ctx.db.insert("shortlist", {
      restaurantId: args.restaurantId,
      name: args.name,
      votes: 0
    });
  }
});
```

This is a locked function—only the server can execute it. The client requests the operation via a tool, but the actual database write happens server-side, providing security.

### Subscribing to the Shortlist

On the client, subscribing to shortlist updates is automatic:

```javascript
const shortlist = useQuery(api.shortlist.list, {}, {
  streaming: true  // Real-time updates
});
```

Whenever any user adds, removes, or votes on a restaurant, all connected clients see the update immediately.

## Key Takeaways

### For Developers

1. **Convex simplifies real-time** — Real-time synchronization is automatic with subscriptions—no manual implementation needed
2. **Server-side AI** — Run all AI operations on server to protect API keys and ensure security
3. **Tool calling is essential** — It's how LLMs interact with the real world through APIs and databases
4. **Security by design** — Lock sensitive functions to server-only execution to control your API surface
5. **Vercel AI SDK integration** — Works seamlessly with Convex for tool calling and LLM streaming

### Architectural Insights

1. **Agentic coding approach** — Focus on understanding architecture rather than code details when working with LLMs
2. **Real-time first design** — Build applications with automatic synchronization from the start
3. **Separation of concerns** — Frontend handles UI, backend handles AI and APIs
4. **API surface security** — Control what clients can access through function locking

### Convex Advantages

- **Simplified development** — No manual real-time implementation needed
- **Security** — Built-in function locking for API protection
- **Scalability** — Handles real-time subscriptions efficiently
- **Developer experience** — Clean API for queries, mutations, and actions

## Getting Started

To build your own multi-user AI chat application:

1. **Clone the repository** — Get the source code from the GitHub link in the video description
2. **Set up a Convex account** — Create a free tier account to get started
3. **Obtain API keys** — Get Google and Anthropic API keys
4. **Experiment locally** — Run the app and test with multiple browser windows to see real-time sync in action
5. **Customize for your use case** — Modify the agent and tools for your own multi-user chat scenario
6. **Explore Convex documentation** — Learn more about Convex's real-time capabilities

## Conclusion

Building real-time, multi-user AI applications doesn't have to be complex. With Convex handling the real-time synchronization and server-side execution, Vercel AI SDK managing tool calling, and modern APIs providing AI and mapping capabilities, you can focus on creating engaging user experiences rather than wrestling with infrastructure.

The combination of real-time sync, AI integration, and secure server-side execution opens up possibilities for collaborative AI applications—from dinner coordination to project management to customer support and beyond.

The future of web applications is real-time and AI-powered. Tools like Convex are making that future accessible today.

---

## References

- **Full transcript**: `/media/docs/output/youtube_How_to_Build_a_MultiUser_AI_Chat_App_with_Convex_FL_UiNpGgEg_20260210_220254.txt`
- **Short summary**: `/media/docs/output/youtube_How_to_Build_a_MultiUser_AI_Chat_App_with_Convex_FL_UiNpGgEg_20260210_220254_summary_short.md`