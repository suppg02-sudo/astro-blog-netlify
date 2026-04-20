---
pubDatetime: 2026-03-01T21:10:03Z
title: "YouTube Processing Flow: Iran Reality - Chase Hughes"
postSlug: "youtube-flow-l7kwbnoudfu"
description: "YouTube Processing Flow: Iran Reality - Chase Hughes"
tags:
  - youtube
  - flow-documentation
  - system-reference
---

## Processing Summary

**Video:** BREAKING: The REALITY The Media Isn't Telling You About Iran
**Author:** Chase Hughes
**Duration:** 11:38
**Processed:** 2026-03-01T21:10:03Z

## Processing Flow

```mermaid
graph LR
    A[YouTube URL] --> B[Phase 1: Extract Transcript]
    B --> C[Phase 1B: Validate Quality]
    C --> D[Phase 2: Generate Summary]
    D --> E[Phase 3: Create Short Summary]
    E --> F[Phase 4: Create Blog Post]
    F --> G[Phase 4B: Flow Documentation]
    G --> H[Published]
```

## Files Generated

| File | Path | Size |
|------|------|------|
| Transcript (JSON) | `~/.config/opencode/docs/output/youtube_breaking-the-reality..._l7kwBnOudfU_20260301_210853.json` | Metadata |
| Transcript (TXT) | `~/.config/opencode/docs/output/youtube_breaking-the-reality..._l7kwBnOudfU_20260301_210853.txt` | 10,367 chars |
| Comprehensive Summary | `~/.config/opencode/docs/output/youtube_..._summary.md` | Full analysis |
| Short Summary | `~/.config/opencode/docs/output/youtube_..._summary_short.md` | Condensed |
| Blog Post | `/media/docker/website/content/posts/youtube-l7kwBnOudfU-.../index.md` | Hugo format |

## Quality Gate Results

- Timestamp count: **274** ✓
- Character count: **10,367** ✓
- Word count: **1,785** ✓
- Validation: **PASSED** ✓

## Blog Post URL
**Content:** http://ubuntu4:1313/posts/youtube-l7kwbnoudfu-iran-reality-chase-hughes/

## Processing Duration
~2 minutes

## Notes
- All phases completed successfully
- No diversions or fallbacks required
- Hugo syntax validation passed