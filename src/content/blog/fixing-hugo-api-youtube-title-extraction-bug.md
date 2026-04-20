---
pubDatetime: 2026-02-25T02:50:00Z
title: "Fixing Hugo API YouTube Title Extraction Bug"
postSlug: "fixing-hugo-api-youtube-title-extraction-bug"
description: "Fixing Hugo API YouTube Title Extraction Bug"
tags:
  - bug-fix
  - hugo
  - api
  - python
  - debugging
---

A recent bug in the Hugo API had YouTube URLs returning "Untitled Video" instead of actual video titles. This post documents the debugging process, root cause, and fix—hopefully saving others from similar JSON parsing headaches.

## The Problem

When users submitted YouTube URLs to the Hugo API's `/api/posts` endpoint, the resulting blog posts had titles like "Untitled Video" instead of the actual video titles. The API was clearly receiving the YouTube URL, processing it, but failing to extract the meaningful title.

```bash
# API call
POST /api/posts
{
  "youtube_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}

# Result - title was generic, not the actual video title
```

## Root Cause Analysis

The issue was a **JSON structure mismatch** between what the YouTube extractor returned and what the API code expected.

### What the API Code Assumed

The API was looking for the title at the top level of the result:

```python
# Original (broken) code
title = result.get("title", "Untitled Video")
```

### What the Extractor Actually Returned

The YouTube extractor returns a nested JSON structure with metadata in a separate object:

```json
{
  "success": true,
  "metadata": {
    "title": "Actual Video Title Here",
    "description": "Video description...",
    "author": "Channel Name",
    "duration": 212
  },
  "transcript": "Full transcript text..."
}
```

The `title` field wasn't at the root level—it was nested inside `metadata`. The API's `result.get("title")` call returned `None`, triggering the fallback to "Untitled Video".

## The Fix

The fix was a simple one-line change to access the nested structure:

```python
# Fixed code
title = result.get("metadata", {}).get("title", "Untitled Video")
```

This change:
1. Gets the `metadata` object (or an empty dict if missing)
2. Extracts the `title` from within metadata
3. Falls back to "Untitled Video" only if both levels are missing

### Git Commit

The fix was committed as `4cbc5c2` in `/media/docker/hugoapi/content_processor.py`.

## Additional Fixes Discovered

While debugging, we found and fixed two related issues:

### 1. Crawl4AI URL Configuration

The extractor was using an incorrect URL for the Crawl4AI service. The correct format uses the Tailscale hostname:

```python
# Before (wrong)
CRAWL4AI_URL = "http://localhost:8000"

# After (correct)
CRAWL4AI_URL = "http://ubuntu58-1:8000"
```

### 2. Response Parsing

The response handling was also updated to properly parse the JSON structure returned by the extractor service.

## Testing and Verification

After applying the fix:

1. **Unit test**: Called the extractor directly with a YouTube URL
2. **Integration test**: Made a full API call to `/api/posts` with a YouTube URL
3. **Browser verification**: Confirmed the generated blog post displayed the correct video title

```bash
# Test command
curl -X POST http://ubuntu58-1:5000/api/posts \
  -H "Content-Type: application/json" \
  -d '{"youtube_url": "https://www.youtube.com/watch?v=EXAMPLE"}'

# Result: Blog post created with correct title ✅
```

## Key Takeaway

**Always verify JSON structures when integrating external tools.**

This bug was caused by making assumptions about API response formats without validating them. The fix took seconds once we inspected the actual JSON being returned.

### Best Practices to Avoid Similar Bugs

1. **Log raw responses** during development to see actual JSON structure
2. **Use defensive access patterns** like `.get("key", {}).get("nested")`
3. **Write integration tests** that validate the full data flow
4. **Document expected schemas** for all external service responses
5. **Don't assume**—verify with actual data

## How to Use the Hugo API (Quick Reference for Agents)

This section provides simple, actionable instructions for AI agents to create blog posts via the Hugo API.

### Service Details

```
Container:     hugoapi
Port:          8092
Base URL:      http://localhost:8092
API Key:       dev-secret-key
```

### Authentication

Every request must include the API key header:

```
X-API-Key: dev-secret-key
```

### Health Check

```bash
curl http://localhost:8092/health
# Expected: {"status":"ok"}
```

### Create Blog Post

**Endpoint**: `POST /api/posts`

**Headers**:
```
Content-Type: application/json
X-API-Key: dev-secret-key
```

### Three Ways to Create Posts

#### 1. From Markdown Content

```bash
curl -X POST http://localhost:8092/api/posts \
  -H "Content-Type: application/json" \
  -H "X-API-Key: dev-secret-key" \
  -d '{
    "markdown_content": "# My Title\n\nThis is the body content."
  }'
```

#### 2. From Webpage URL

```bash
curl -X POST http://localhost:8092/api/posts \
  -H "Content-Type: application/json" \
  -H "X-API-Key: dev-secret-key" \
  -d '{
    "webpage_url": "https://example.com/article"
  }'
```

#### 3. From YouTube URL

```bash
curl -X POST http://localhost:8092/api/posts \
  -H "Content-Type: application/json" \
  -H "X-API-Key: dev-secret-key" \
  -d '{
    "youtube_url": "https://www.youtube.com/watch?v=VIDEO_ID"
  }'
```

### Response Format

```json
{
  "status": "success",
  "message": "Content processed successfully",
  "content_type": "youtube|webpage|markdown",
  "title": "Extracted or provided title",
  "summary": "Brief summary of content",
  "processed_content": "Full markdown content",
  "post_url": "http://ubuntu58-1:1314/posts/slug-here/"
}
```

### Agent Workflow

1. **Check health**: `GET /health` → confirm `{"status":"ok"}`
2. **Submit content**: `POST /api/posts` with one of the three content types
3. **Check response**: Look for `"status": "success"`
4. **Verify post**: Navigate to `post_url` from response to confirm publication

### Error Handling

| Status | Meaning | Action |
|--------|---------|--------|
| 200 | Success | Post created, check `post_url` |
| 401 | Unauthorized | Check `X-API-Key` header |
| 422 | Validation error | Check request body format |
| 503 | Service unavailable | Check Crawl4AI container for webpage URLs |

### Dependencies

| Service | Port | Required For |
|---------|------|--------------|
| Crawl4AI | 11235 | Webpage URL processing |
| Hugo Blog | 1314 | Post viewing (not creation) |

### Common Issues

**"Untitled Video" for YouTube**: Fixed in commit `4cbc5c2`. If this appears, the fix needs to be applied.

**Crawl4AI unavailable**: Check `docker ps | grep crawl4ai` and `curl http://localhost:11235/health`

**API key rejected**: Verify `.env` file in `/media/docker/hugoapi/` contains correct key.

---

## Conclusion

A one-line JSON path fix resolved an issue that made YouTube-sourced blog posts look broken. The lesson: when integrating with external services, take time to understand their actual response structures rather than assuming based on documentation or previous experience.

---

*Filed under: debugging, API integration, Python, Hugo, bug fixes*