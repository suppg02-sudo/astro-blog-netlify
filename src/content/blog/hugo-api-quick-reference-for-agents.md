---
pubDatetime: 2026-02-25T02:55:00Z
title: "Hugo API: Quick Reference for AI Agents"
postSlug: "hugo-api-quick-reference-for-agents"
description: "Hugo API: Quick Reference for AI Agents"
tags:
  - automation
  - hugo
  - api
  - reference
---

A minimal guide for AI agents to create blog posts via the Hugo API.

## The Basics

```
URL:     http://localhost:8092
Key:     X-API-Key: dev-secret-key
Health:  GET /health → {"status":"ok"}
```

## Create a Post

**Endpoint**: `POST /api/posts`

**Headers**:
```
Content-Type: application/json
X-API-Key: dev-secret-key
```

## Three Input Types

### 1. YouTube URL

```bash
curl -X POST http://localhost:8092/api/posts \
  -H "Content-Type: application/json" \
  -H "X-API-Key: dev-secret-key" \
  -d '{"youtube_url": "https://www.youtube.com/watch?v=VIDEO_ID"}'
```

### 2. Webpage URL

```bash
curl -X POST http://localhost:8092/api/posts \
  -H "Content-Type: application/json" \
  -H "X-API-Key: dev-secret-key" \
  -d '{"webpage_url": "https://example.com/article"}'
```

### 3. Markdown Content

```bash
curl -X POST http://localhost:8092/api/posts \
  -H "Content-Type: application/json" \
  -H "X-API-Key: dev-secret-key" \
  -d '{"markdown_content": "# Title\n\nBody text here."}'
```

## Response

```json
{
  "status": "success",
  "title": "Extracted Title",
  "post_url": "http://ubuntu58-1:1314/posts/slug/"
}
```

## Agent Workflow

1. Check health: `curl http://localhost:8092/health`
2. POST to `/api/posts` with one input type
3. Check `status` field is `"success"`
4. Visit `post_url` to verify

## Errors

| Code | Fix |
|------|-----|
| 401 | Add `X-API-Key: dev-secret-key` header |
| 503 | Crawl4AI down (webpage URLs only) |

## Dependencies

- **Crawl4AI** (port 11235) - Required for webpage URLs
- **YouTube Extractor** - Built-in for YouTube URLs

That's it. One endpoint, one header, three input types.