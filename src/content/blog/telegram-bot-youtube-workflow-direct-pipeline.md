---
pubDatetime: 2026-03-09T10:40:00Z
title: "Replacing a Broken YouTube Delegation with a 33-Second Direct Pipeline"
postSlug: "telegram-bot-youtube-workflow-direct-pipeline"
description: "Replacing a Broken YouTube Delegation with a 33-Second Direct Pipeline"
tags:
  - youtube
  - pipeline
  - gemini
  - architecture
  - python
  - telegram-bot
---

When I added YouTube URL detection to my Telegram bot, the obvious approach was to delegate the heavy lifting to OpenCode - the AI coding agent already running on the server. It had a 5-phase YouTube trigger skill that handled everything from transcript extraction to blog publishing. What could go wrong?

Three things, as it turned out. All at once.

## The Broken Delegation

The original `youtube_workflow()` was a thin wrapper around `opencode run`:

```python
def youtube_workflow(url: str) -> tuple:
    result = subprocess.run(
        [OPENCODE_BIN, "run", url],
        capture_output=True, text=True, timeout=300,
        env={**os.environ, "HOME": "/root"},
        cwd="/root"
    )
```

This failed for three independent reasons:

1. **Wrong model**: OpenCode's default model (Claude Haiku) didn't follow the YouTube trigger instructions. Even Sonnet recognized the trigger but improvised tool usage instead of following the prescribed 5-phase script.

2. **yt-dlp was broken**: Both Haiku and Sonnet tried to use `yt-dlp` for transcript extraction, which was getting HTTP 400 errors from YouTube's player APIs. Meanwhile, the prescribed `youtube_transcript_extractor.py` script using `youtube-transcript-api` worked perfectly.

3. **Permission rejection**: `opencode run` in non-interactive mode auto-rejects tool calls that need confirmation, so even when the agent picked the right approach, it couldn't execute file reads or writes.

Three problems, one subprocess call, zero successful runs.

## The Direct Approach

The fix was to stop delegating and do the work directly in the bot process. All the pieces already existed:

- `youtube-transcript-api` was installed in the bot's venv
- `requests` could fetch video metadata via YouTube's oEmbed API
- `ask_gemini()` was already working for chat and search
- `publish_blog_post()` was already publishing research articles

The new implementation is three focused functions:

### 1. Metadata Fetch (~110ms)

```python
def youtube_get_metadata(video_id: str) -> dict:
    oembed_url = (
        f"https://www.youtube.com/oembed"
        f"?url=https://www.youtube.com/watch?v={video_id}&format=json"
    )
    resp = requests.get(oembed_url, timeout=10)
    if resp.status_code == 200:
        data = resp.json()
        metadata["title"] = data.get("title", "Unknown")
        metadata["author"] = data.get("author_name", "Unknown")
```

YouTube's oEmbed endpoint is fast and reliable. No API key needed. Returns title and author, which is all we need for the blog post frontmatter and Gemini prompt context.

### 2. Transcript Extraction (~900ms)

```python
def youtube_get_transcript(video_id: str) -> str | None:
    from youtube_transcript_api import YouTubeTranscriptApi
    api = YouTubeTranscriptApi()

    for langs in (['en'], []):
        try:
            fetched = api.fetch(video_id, languages=langs) if langs else api.fetch(video_id)
            break
        except Exception:
            continue

    raw = fetched.to_raw_data()
    lines = [entry.get("text", "").strip() for entry in raw if entry.get("text", "").strip()]
    return " ".join(lines)
```

The `youtube-transcript-api` library fetches captions directly from YouTube's internal API - no browser automation, no `yt-dlp`, no OAuth. It tries English first, falls back to any available language, then falls back to listing all available transcripts. For a 20-minute video, this returns ~3,500 words in under a second.

### 3. Gemini Summarization (~17 seconds)

The transcript goes to Gemini 2.5 Flash with a structured prompt requesting:
- Overview paragraph (who, what, why it matters)
- Sections with headings for main topics
- Key quotes with context
- Key Takeaways bullet points
- 800-1200 word target

For a 3,455-word transcript, Gemini returned a 1,227-word summary in ~17 seconds. The prompt includes the video title and author so Gemini can frame the summary properly.

### 4. Blog Publishing (~15 seconds)

The summary gets wrapped in Hugo frontmatter with YouTube-specific metadata:

```yaml
title: "YouTube: How to Use Claude Skills 2.0 Better than 99% of People"
categories: ["YouTube"]
tags: ["youtube", "video-summary", "claude", "skills", "better", "people"]
```

A video header block links back to the original:

```markdown
> **Video**: [Title](url) by **Author**
> **Transcript**: 3,455 words
```

Then `docker exec hugo hugo --minify` rebuilds the site. The Hugo rebuild is the second-longest step at ~15 seconds.

## Timing Breakdown

Here's the actual timing from the first successful run:

| Step | Duration | What Happens |
|------|----------|--------------|
| URL detection | <1ms | Regex match in `echo()` handler |
| Metadata fetch | 110ms | YouTube oEmbed API |
| Transcript extraction | 900ms | `youtube-transcript-api` |
| Gemini summarization | 16.8s | Full transcript to structured summary |
| Blog file write | 6ms | Markdown to disk |
| Hugo rebuild | 15.5s | Static site regeneration |
| Telegram response | 170ms | Send blog URL back |
| **Total** | **~33s** | End-to-end |

The old OpenCode delegation had a 5-minute timeout and never completed successfully. The new direct pipeline runs in 33 seconds with zero external process dependencies.

## Architecture Lesson

The instinct to delegate to a more capable agent (OpenCode with its full skill system) was wrong here. The YouTube workflow needed:

- **Determinism**: Same input, same output, every time
- **Speed**: Under a minute for a good user experience
- **Reliability**: No model behavior variance, no permission issues

All three are properties of direct code execution, not agent delegation. The agent pattern works for open-ended tasks where you need reasoning and adaptation. For a fixed pipeline (fetch transcript -> summarize -> publish), a function call chain is simpler, faster, and more reliable.

The 5-phase OpenCode workflow was elegant in design but brittle in practice. Three functions and 130 lines of Python replaced it entirely.

---

*Part of the Telegram Bot series: [v3 Architecture](/posts/telegram-bot-opencode-agent-architecture/) | [Gemini Search Grounding](/posts/telegram-bot-gemini-search-grounding/) | YouTube Pipeline (this post)*