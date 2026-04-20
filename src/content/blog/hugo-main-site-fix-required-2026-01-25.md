---
pubDatetime: 2026-01-25T15:00:00Z
title: "Hugo Main Site Fix Required"
postSlug: "hugo-main-site-fix-required-2026-01-25"
description: "Hugo Main Site Fix Required"
tags:
  - hugo
  - docker
  - troubleshooting
  - critical
---

## Critical Issue

Hugo main site container `hugo_site` is stuck in an infinite restart loop and cannot start the Hugo server.

## Current State

**Container Status**: "Restarting (1)" (for 57+ minutes)

**Error in Logs**:
```
ERROR Rebuild failed: assemble: failed to create page from pageMetaSource 
"/posts/test-blog-post-workflow-verification-2026-01-25": [1:8] mapping value is not allowed in this context
```

**Port Configuration**:
- Internal: 1313
- External: 1314
- Config shows correct: `--port=1313`, `--bind=0.0.0.0:1313`

## What's Working

**docsy-site** (port 1318): ✅ Working perfectly
- test-site (port 1316): ✅ Working perfectly

**Main Site** (port 1314): ❌ Not working

## Root Cause

The test blog post filename `/posts/test-blog-post-workflow-verification-2026-01-25/` has `[1:8]` in it. Hugo is interpreting `[1:8]` as a mapping syntax which is invalid for page metadata.

This causes Hugo to fail every rebuild with "mapping value is not allowed in this context" error.

## Required Fix

Remove or fix the test blog post causing Hugo build failures.

## Workaround

Use docsy-site (port 1318) for creating new blog posts until main site is fixed.

## Next Steps

1. Delete problematic test blog post
2. Restart Hugo container
3. Verify site is accessible
4. Test creating new blog post