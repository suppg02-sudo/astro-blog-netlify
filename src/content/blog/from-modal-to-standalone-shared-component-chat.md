---
pubDatetime: 2026-04-08T00:30:00Z
title: "From Modal to Standalone: Building a Shared-Component Chat Architecture with React + GLM-5"
postSlug: "from-modal-to-standalone-shared-component-chat"
description: "From Modal to Standalone: Building a Shared-Component Chat Architecture with React + GLM-5"
tags:
  - others
---

# From Modal to Standalone: Building a Shared-Component Chat Architecture with React + GLM-5

> **Date**: 2026-04-08  
> **Tags**: React, Docker, Monorepo, AI, Chat, GLM-5, Directus

---

I started with a modal chat assistant embedded in my AImplifi dashboard — a nice little floating panel powered by Zhipu's GLM-5 model. But I wanted more: conversation history that persists, a proper sidebar, theme switching, and the flexibility to run the chat as its own app.

What emerged over the last 48 hours is a polished **monorepo architecture** where both the dashboard modal and the standalone chat share a single UI package. Same components, same rendering, same animations — built once, deployed twice.

---

## The Architecture

Three services in a single `docker-compose.yml`:

| Service | Port | Purpose |
|---------|------|---------|
| **Dashboard** | 8056 | AImplifi React app + modal chat |
| **Chat API** | 8057 | FastAPI + GLM-5 streaming |
| **Chat Standalone** | 8058 | Full-page chat app with sidebar |

The key innovation is `@aimplifi/chat-ui` — a shared npm workspace package that exports components used by **both** apps:

```
|-- packages/chat-ui/          # @aimplifi/chat-ui (shared)
|   |-- components/
|   |   |-- ChatInput.tsx      # Auto-focus textarea, drag-drop, file support
|   |   |-- ChatMessage.tsx    # Markdown rendering, shortened URLs, copy button
|   |   |-- ChatOptions.tsx    # Question cards with staggered animations
|   |   |-- IngestionRouter.tsx# URL classification + flow buttons
|   |   |-- FlowProgress.tsx   # Pipeline stage tracking
|   |   `-- ThemePicker.tsx    # 6 themes
|   |-- hooks/
|   |   |-- useChat.ts         # SSE streaming
|   |   `-- useIngestion.ts    # Flow execution
|   `-- lib/flowRegistry.ts    # Flow classification engine
|-- app/                        # Dashboard (imports from package)
`-- chat-standalone/            # Standalone app (imports from package)
```

## Key Features

### Markdown Rendering

Bot responses fully render markdown using `react-markdown` + `remark-gfm`. Headers, bold, italic, lists, tables, code blocks, blockquotes — all properly styled. URLs automatically shortened to `hostname/short/path` with external link icons.

### Conversation Persistence

Conversations stored via Directus `/sessions` API. Sidebar groups chats by date. You can rename conversations inline, delete with confirmation, and export the entire chat as a Markdown file.

### Mobile-First Design

`100dvh` adapts to virtual keyboards. 17px font prevents iOS Safari auto-zoom. Send button always pinned visible — stacking widgets scroll above it. Viewport locked to `maximum-scale=1.0`.

### Auto-Focus Architecture

The chat input stays focused through `autoFocus` on mount, `forwardRef` imperatively controlled by the parent, and a `useEffect` watching the `disabled` prop so it re-focuses when streaming stops.

### Animations

Flow buttons stagger in with 60ms delay and slide up. Hover lifts 2px and scales 3%. Option cards stagger at 80ms and slide left. Welcome screen fades in sequentially.

### 6 Theme System

Dark, Light, Ocean, Nord, Sunset, Forest — each defining CSS custom properties for backgrounds, text, accents, and borders. Persists in localStorage.

---

## Docker Gotchas

The hardest part wasn't the components — it was getting npm workspace dependencies into the Docker build. The explicit `cd packages/chat-ui && npm install` was missing, causing `react-markdown` to not make it into the bundle. You need to install the shared package's dependencies before building anything that consumes them.

## Product Potential

While this started personal, the architecture is designed for future monetization. White-label wrappers. API key auth. Embeddable widget. Usage metering. Expanded ingestion routes for news, shopping, and research flows with project targeting.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 18 + TypeScript + Vite |
| Styling | Tailwind CSS 3.x + CSS Custom Props |
| Animation | Framer Motion |
| Icons | Lucide React |
| Markdown | react-markdown + remark-gfm |
| Backend | FastAPI + SSE Streaming |
| AI Model | Zhipu GLM-5 |
| Persistence | Directus API / PostgreSQL |
| Deploy | Docker Compose + Nginx |

**The result**: a polished, mobile-friendly chat experience that works equally well as a modal in your dashboard or as its own dedicated app — all powered by a single shared component library.