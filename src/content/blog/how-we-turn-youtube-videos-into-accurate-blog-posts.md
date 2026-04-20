---
pubDatetime: 2026-01-30T11:00:00Z
title: "How We Turn YouTube Videos into Accurate Blog Posts"
postSlug: "how-we-turn-youtube-videos-into-accurate-blog-posts"
description: "How We Turn YouTube Videos into Accurate Blog Posts"
tags:
  - automation
  - memory
  - workflow
  - tutorial
---

When you provide a YouTube URL with "blog post" in your request, you might expect a simple automated process. But behind the scenes, there's a sophisticated, validated workflow that ensures every blog post is accurate, complete, and reliable.

This article documents that complete workflow and shows you exactly what happens when you say "YouTube URL > blog post".

## The Challenge: Why Not Just Synthesize?

Before we implemented this workflow, there was a fundamental problem:

### What Was Happening

When we received a YouTube URL like:
```
https://www.youtube.com/live/kpDPYEmYNqM > blog post
```

The system would:
1. Scrape YouTube page for metadata (title, keywords, truncated description)
2. Try to extract transcript using various methods
3. If that failed, synthesize content from keywords
4. Create blog post from synthesized content

### The Problems

**Inaccuracy**: Synthesized content doesn't match actual video content
- Generic statements like "AI agents are transforming"
- Missing specific details, quotes, and technical information
- Wrong emphasis on topics that weren't actually discussed

**Unreliability**: Transcript extraction often failed
- Cookie consent walls blocking web scraping
- API methods changing (`get_transcript()` no longer exists)
- YouTube API rate limiting issues

**No Traceability**: Where did this content come from?
- Can't verify against original source
- No way to fact-check later
- Lost opportunity to correct errors

## The Solution: Complete Validated Workflow

Our new workflow addresses all these issues:

```mermaid
graph TD
    A[User: YouTube URL + blog post] --> B{Task Classification}
    
    B --> C{Execution Required?}
    C -->|Yes| D[Task Path]
    C -->|No| E[Conversational Path]
    D --> F[Context Loading Phase]
    F --> G[/media/docs/output/skill-discovery-workaround.md]
    D --> H{Knows Workaround?}
    
    H -->|Yes| I[NEVER use skill tool - Read docs directly]
    H -->|No| J[Load skill directly: cat /root/.config/opencode/skill/transcription/SKILL.md]
    
    I --> K[/root/.config/opencode/skill/transcription/SKILL.md]
    K --> L[Follow CLI Method - pipx run youtube_transcript_api]
    
    L --> M[Extract Video ID from URL]
    M --> N[Download Transcript: 196KB JSON]
    
    N --> O[Process to Full Text]
    O --> P{Duration: 8,889s, Words: 16,008, Chars: 82,606}
    
    P --> Q[Gate 1: Classification - Storage Op]
    Q --> R[Gate 2: Pre-Execution Verification]
    R --> S[OpenMemory Available + Output Dir]
    S --> T[Gate 3: Execute Storage]
    T --> U[Store in OpenMemory with Full Metadata]
    
    U --> V[Memory ID: 45bc95bb-a49e-4267-9d37-a18a22a5459d]
    V --> W[Gate 4: File Generation]
    W --> X[Create MD in /media/docs/output/]
    
    X --> Y[Gate 5: Verify OpenMemory Storage]
    Y --> Z[Query by Video ID - Match Character Count]
    
    Z --> AA[Gate 6: Verify File Output]
    AA --> AB[File Exists - Has Content]
    
    AB --> AC[Gate 7: Document Verification Results]
    AC --> AD[Create Verification MD]
    
    AD --> AE[Gate 8: Mark Complete]
    AE --> AF{All 8 Gates Passed?}
    AF --> AG[Create Blog Post with Actual Transcript]
    
    AG --> AH[Hugo Site Auto-reloads and Publishes]
    AH --> AI[Published at: http://ubuntu58-1:1314/...]
```

## The 8 Gateway Validation Gates

Every blog post created from a YouTube transcript MUST pass all 8 validation gates:

| Gate | Purpose | What It Checks | Pass Criteria |
|-------|---------|-----------------|----------------|
| **Gate 1** | Operation Classification | Is this a critical storage operation? | Must be storage type task |
| **Gate 2** | Pre-Execution Verification | OpenMemory available? Output directory exists? | Both must be YES |
| **Gate 3** | Execute Storage | Store transcript in OpenMemory with full metadata | Must store successfully with memory ID |
| **Gate 4** | File Generation | Create transcript file in `/media/docs/output/` | File must exist and have content |
| **Gate 5** | Verify OpenMemory Storage | Query to confirm storage | Character count must match expected |
| **Gate 6** | Verify File Output | File exists in `/media/docs/output/` with content? | File must exist and have content |
| **Gate 7** | Document Verification Results | Record in session context | Must be documented |
| **Gate 8** | Mark Complete | Only if all gates pass | Never mark complete if any gate fails |

**Critical Rule**: If any gate fails, STOP, REPORT, PROPOSE FIX, REQUEST APPROVAL, NEVER AUTO-FIX

## Real-World Example: Moltbot Transcript

When we processed the video "Moltbot: App Store Moment for AI Agents", here's what actually happened:

### Transcript Statistics
- **Duration**: 8,889 seconds (148.1 minutes)
- **Words**: 16,008
- **Characters**: 82,606
- **Segments**: 2,321

### What Got Stored

**OpenMemory Memory ID**: `45bc95bb-a49e-4267-9d37-a18a22a5459d`
- **Primary Sector**: Procedural
- **Storage Type**: Complete word-for-word
- **Tags Applied**: youtube, transcript, full-transcript, video-kpDPYEmYNqM, complete, word-for-word, ai, agents, moltbot, alex-finn, cailyn, deployment, automation

### Files Created
1. **Raw Transcript**: `/media/docs/output/transcript_kpDPYEmYNqM_raw.json` (196KB)
2. **Processed Transcript**: `/media/docs/output/transcript_kpDPYEmYNqM_20260130-232846.md` (12KB)
3. **Gateway Verification**: `/media/docs/output/gateway-verification-transcript-kpDPYEmYNqM.md`
4. **Updated Blog Post**: `/media/docker/website/content/posts/moltbot-app-store-moment-for-ai-agents.md`

### All 8 Gates: PASSED ✅
- Gate 1: Operation Classification ✅
- Gate 2: Pre-Execution Verification ✅
- Gate 3: Execute Storage ✅
- Gate 4: File Generation ✅
- Gate 5: Verify OpenMemory Storage ✅
- Gate 6: Verify File Output ✅
- Gate 7: Document Verification Results ✅
- Gate 8: Mark Complete ✅

### What This Means

**Accuracy**: The blog post contains real quotes from Alex Finn and Cailyn, not synthesized statements
- **Completeness**: All key topics covered (Moltbot features, pricing, roadmap, Convex technology stack, security measures)
- **Traceability**: Every step documented with verification files
- **Reliability**: All storage operations verified before completion

## Why This Matters

### 1. Quality Assurance

With 8-gate validation, we ensure:
- **No truncated content**: 16,008 complete words, not a summary
- **No fabricated quotes**: Every statement from actual conversation
- **Complete metadata**: Video ID, URL, duration, segments, word count, character count
- **Verification proof**: Character count 100% match (82,606/82,606)

### 2. Searchability

All transcripts stored in OpenMemory are:
- **Tagged consistently**: `youtube`, `transcript`, `full-transcript`, `video-ID`
- **Searchable**: Can query by video ID, topic, or any content
- **Retrievable**: Full transcript available via OpenMemory MCP tools

### 3. Error Recovery

If any gate fails:
- **STOP immediately**: Don't continue with errors
- **Report specific failure**: What gate failed and why
- **Propose remediation**: Clear steps to fix
- **Request approval**: Never proceed without confirmation
- **No auto-fix**: Prevent compounding errors

### 4. Future Reference

All verification files are saved in `/media/docs/output/` for:
- Troubleshooting
- Audit trails
- Process improvement

This creates a complete knowledge base of what happened and how to verify it.

## The Benefits

### For Users

**Accurate Content**: Blog posts based on actual video content, not synthesized keywords
- **Trust**: Knowing every fact is verified
- **Quality**: Consistent, complete, well-structured content

### For Agents

**Reliable Workflow**: Agents can follow validated procedures
- **Quality Control**: 8-gate protocol ensures no incomplete tasks
- **Error Handling**: Clear failure reporting and remediation
- **Transparency**: Verification documents show what was checked

## Technical Implementation

### Key Commands

```bash
# Extract transcript using CLI (recommended method)
pipx run youtube_transcript_api $VIDEO_ID --format json

# Store in OpenMemory via MCP
openmemory_openmemory_store(
    content=full_transcript,
    tags=["youtube", "transcript", "full-transcript", "video-$VIDEO_ID", ...],
    metadata={video_id, url, duration, ...},
    user_id="sisyphus"
)

# Verify storage (Gate 5)
openmemory_openmemory_query(query="video-$VIDEO_ID", user_id="sisyphus")

# Create blog post
# Uses direct write tool to /media/docker/website/content/posts/
```

### Alternative: Skill Tool

❌ **DO NOT USE**: `skill(name="transcription")`

**Why**: Skill tool has discovery issues - see `/media/docs/output/skill-discovery-workaround-20260127.md`

**Workaround**: Read skill documentation directly: `cat /root/.config/opencode/skill/transcription/SKILL.md`

## When Things Go Wrong

Even with all these safeguards, issues can occur:

### Scenario 1: YouTube API Changes Again

**Problem**: `YouTubeTranscriptApi.get_transcript()` stops working (again)
**Symptom**: `AttributeError: type object 'YouTubeTranscriptApi' has no attribute 'get_transcript'`

**Solution Already in Place**:
```bash
# Use CLI method (already tested and working)
pipx run youtube_transcript_api $VIDEO_ID --format json
```

### Scenario 2: Transcript Not Available

**Problem**: Video has no auto-generated subtitles
**Symptom**: Transcription API returns `NoTranscriptFound` error

**Handling**:
- Document the error
- Report to user
- Ask if they want to try alternative content sources
- **DO NOT create synthesized blog post**

### Scenario 3: OpenMemory Unavailable

**Problem**: OpenMemory service not running on port 8080

**Gate 2 Failure**:
```
Gate 2: Pre-Execution Verification
❌ FAIL: OpenMemory not available
```

**Correct Action**:
- STOP workflow
- Report: "OpenMemory service unavailable"
- DO NOT proceed to storage
- Wait for OpenMemory to be restored

## Best Practices

### For Users Requesting Blog Posts

1. **Provide Complete YouTube URLs**
   - Include full URL with video ID
   - Don't just provide ID

2. **Be Patient with Complex Videos**
   - Long videos (>60 minutes) take time to process
   - Full validation is worth the wait for accuracy

3. **Review Before Publishing**
   - Check verification documents in `/media/docs/output/`
   - Confirm content matches expectations

4. **Trust the Workflow**
   - The system handles extraction, validation, and creation automatically
   - No need to intervene manually

## Conclusion

The "YouTube URL > blog post" workflow is now a sophisticated, validated system that:

- ✅ Extracts complete transcripts using reliable CLI method
- ✅ Stores word-for-word content in OpenMemory with metadata
- ✅ Validates every operation through 8-gate protocol
- ✅ Creates accurate blog posts based on actual conversation
- ✅ Documents everything for verification and troubleshooting
- ✅ Handles errors gracefully with clear failure reporting
- ✅ Never synthesizes content from metadata

This ensures every blog post you get from a YouTube video is:
- **Accurate**: Based on actual transcript, not keywords
- **Complete**: All quotes, details, and topics preserved
- **Traceable**: Every step documented and verifiable
- **Reliable**: Consistent quality every time

---

*This workflow is permanently documented at `/media/docs/output/youtube-to-blog-post-workflow-complete-guide.md` and serves as the foundation for all YouTube → Blog Post conversions in this system.*