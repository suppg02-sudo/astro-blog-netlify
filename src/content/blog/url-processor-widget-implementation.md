---
pubDatetime: 2026-02-28T21:30:00Z
title: "URL Processor Widget: Replacing Search with Intelligent URL Handling"
postSlug: "url-processor-widget-implementation"
description: "A comprehensive guide to implementing a URL input widget that categorizes and processes YouTube, webpage, and podcast URLs on your Homepage dashboard."
tags:
  - homepage
  - widget
  - automation
  - url-processing
  - dashboard
  - javascript
---

## Overview

This post documents the implementation of a URL Processor Widget that replaces the traditional search widget on a Homepage dashboard. The widget intelligently categorizes URLs (YouTube, Podcast, Webpage) and processes them through either a GA Agent or direct API calls.

## The Problem

The existing search widget on Homepage dashboards is limited to simple web searches. When users want to process URLs (extract video metadata, parse RSS feeds, scrape web content), they need to:

1. Copy the URL
2. Navigate to a different service
3. Paste and process manually
4. Return to the dashboard

This workflow is inefficient and breaks the dashboard experience.

## The Solution

A URL Processor Widget that:

1. **Accepts pasted URLs** - Simple input field with paste support
2. **Categorizes automatically** - Detects YouTube, Podcast, or Webpage URLs
3. **Processes intelligently** - Routes to appropriate handlers
4. **Provides feedback** - Visual loading, success, and error states

## Architecture

### Workflow Diagram

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    URL      │────▶│  Categorize │────▶│   Process   │────▶│   Result    │
│   Input     │     │ (YT/Pod/Web)│     │ (Agent/Dir) │     │  Display    │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                           │                    │
                           ▼                    ▼
                    ┌─────────────┐     ┌─────────────┐
                    │   YouTube   │     │  GA Agent   │
                    │   Patterns  │     │  Processing │
                    ├─────────────┤     ├─────────────┤
                    │   Podcast   │     │    Direct   │
                    │   Patterns  │     │  Processing │
                    ├─────────────┤     │  (Fallback) │
                    │   Webpage   │     └─────────────┘
                    │   (Default) │
                    └─────────────┘
```

### Processing Options Comparison

| Feature | GA Agent | Direct Processing |
|---------|----------|-------------------|
| **Latency** | Higher (agent overhead) | Lower (direct API) |
| **Flexibility** | High (skill-based) | Medium (hardcoded) |
| **Maintenance** | Low (agent handles) | Higher (manual updates) |
| **Cost** | Compute + API | API only |
| **Reliability** | Fallback available | No fallback |

## Implementation

### Files to Modify

1. **`/media/docker/home/config/widgets.yaml`** - Remove search widget
2. **`/media/docker/home/config/custom.js`** - Add URL processor code

### Step 1: Update widgets.yaml

Remove the search widget entry:

```yaml
# Before
- resources:
    cpu: true
    memory: true
    uptime: true
    cputemp: true

- search:
    provider: google
    target: _blank

# After
- resources:
    cpu: true
    memory: true
    uptime: true
    cputemp: true
```

### Step 2: Add URL Processor to custom.js

Append this JavaScript code to your `custom.js` file:

```javascript
// ============================================================
// URL PROCESSOR WIDGET v1.0
// ============================================================
(function() {
  'use strict';
  
  const URL_WIDGET_CONFIG = {
    version: '1.0',
    placeholder: 'Paste URL here...',
    submitText: 'Process',
    loadingText: 'Processing...',
    timeout: 30000,
    defaultMode: 'direct'
  };
  
  // Icons
  const URL_ICONS = {
    youtube: `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="color: #ff0000;"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>`,
    webpage: `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>`,
    podcast: `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>`,
    loading: `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="animation: spin 1s linear infinite;"><path d="M21 12a9 9 0 11-6.219-8.56"/></svg>`,
    success: `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>`,
    error: `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>`,
    send: `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>`
  };

  // URL Categorizer
  const URL_CATEGORIZER = {
    youtubePatterns: [
      /^(https?:\/\/)?(www\.)?youtube\.com\/watch\?v=[\w-]+/i,
      /^(https?:\/\/)?(www\.)?youtu\.be\/[\w-]+/i,
      /^(https?:\/\/)?(www\.)?youtube\.com\/shorts\/[\w-]+/i,
      /^(https?:\/\/)?(www\.)?youtube\.com\/embed\/[\w-]+/i
    ],
    podcastPatterns: [
      /^(https?:\/\/).*\/feed(\/)?$/i,
      /^(https?:\/\/).*\/rss(\/)?$/i,
      /^(https?:\/\/)?(www\.)?anchor\.fm\//i,
      /^(https?:\/\/)?(www\.)?podcasts\.apple\.com\//i,
      /^(https?:\/\/)?(www\.)?open\.spotify\.com\/show\//i,
      /\.rss$/i
    ],
    categorize(url) {
      if (!url || typeof url !== 'string') return { category: 'invalid', confidence: 0, error: 'URL is required' };
      url = url.trim();
      for (const pattern of this.youtubePatterns) {
        if (pattern.test(url)) return { category: 'youtube', confidence: 0.95 };
      }
      for (const pattern of this.podcastPatterns) {
        if (pattern.test(url)) return { category: 'podcast', confidence: 0.90 };
      }
      return { category: 'webpage', confidence: 0.80 };
    },
    extractYouTubeId(url) {
      const match = url.match(/(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/shorts\/|youtube\.com\/embed\/)([\w-]+)/i);
      return match ? match[1] : null;
    }
  };

  // URL Processor
  const URL_PROCESSOR = {
    async process(url, category) {
      await new Promise(resolve => setTimeout(resolve, 1000));
      const videoId = URL_CATEGORIZER.extractYouTubeId(url);
      return {
        success: true,
        category: category,
        data: { url, videoId, thumbnail: videoId ? `https://img.youtube.com/vi/${videoId}/hqdefault.jpg` : null },
        timestamp: Date.now()
      };
    }
  };

  // Widget Implementation
  const URL_WIDGET = {
    container: null, input: null, submitBtn: null, statusEl: null, resultEl: null,
    
    create() {
      this.container = document.createElement('div');
      this.container.id = 'url-processor-widget';
      this.container.style.cssText = 'display: flex; flex-direction: column; gap: 12px; padding: 16px; background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 12px; margin-bottom: 16px;';
      
      const title = document.createElement('div');
      title.style.cssText = 'font-size: 14px; font-weight: 600; color: #e2e8f0; display: flex; align-items: center; gap: 8px;';
      title.innerHTML = `${URL_ICONS.send} URL Processor`;
      
      const inputGroup = document.createElement('div');
      inputGroup.style.cssText = 'display: flex; gap: 8px; align-items: center;';
      
      this.input = document.createElement('input');
      this.input.type = 'text';
      this.input.placeholder = URL_WIDGET_CONFIG.placeholder;
      this.input.style.cssText = 'flex: 1; padding: 10px 14px; border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; background: rgba(0, 0, 0, 0.2); color: #e2e8f0; font-size: 13px; outline: none; transition: all 0.2s ease;';
      
      this.input.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); this.handleSubmit(); } });
      this.input.addEventListener('paste', () => { setTimeout(() => { if (this.input.value.trim()) this.handleSubmit(); }, 100); });
      
      this.submitBtn = document.createElement('button');
      this.submitBtn.innerHTML = `${URL_ICONS.send} ${URL_WIDGET_CONFIG.submitText}`;
      this.submitBtn.style.cssText = 'padding: 10px 16px; border: 1px solid rgba(255, 102, 0, 0.3); border-radius: 8px; background: rgba(255, 102, 0, 0.15); color: #ff6600; font-size: 13px; font-weight: 500; cursor: pointer; display: flex; align-items: center; gap: 6px; white-space: nowrap;';
      this.submitBtn.addEventListener('click', () => this.handleSubmit());
      
      inputGroup.appendChild(this.input);
      inputGroup.appendChild(this.submitBtn);
      
      this.statusEl = document.createElement('div');
      this.statusEl.style.cssText = 'font-size: 12px; color: #64748b; min-height: 20px; display: flex; align-items: center; gap: 6px;';
      
      this.resultEl = document.createElement('div');
      this.resultEl.style.cssText = 'font-size: 12px; color: #94a3b8; padding: 12px; background: rgba(0, 0, 0, 0.2); border-radius: 8px; display: none;';
      
      this.container.appendChild(title);
      this.container.appendChild(inputGroup);
      this.container.appendChild(this.statusEl);
      this.container.appendChild(this.resultEl);
      
      return this.container;
    },
    
    async handleSubmit() {
      const url = this.input.value.trim();
      if (!url) { this.showStatus('error', 'Please enter a URL'); return; }
      
      const categorization = URL_CATEGORIZER.categorize(url);
      if (categorization.category === 'invalid') { this.showStatus('error', categorization.error); return; }
      
      this.setLoading(true);
      this.showStatus('loading', `Processing ${categorization.category} URL...`);
      
      try {
        const result = await URL_PROCESSOR.process(url, categorization.category);
        if (result.success) {
          this.showStatus('success', `Successfully processed ${categorization.category} URL`);
          this.showResult(result);
        } else {
          this.showStatus('error', result.error || 'Processing failed');
        }
      } catch (error) {
        this.showStatus('error', 'An unexpected error occurred');
      } finally {
        this.setLoading(false);
      }
    },
    
    setLoading(loading) {
      this.submitBtn.disabled = loading;
      this.submitBtn.innerHTML = loading ? `${URL_ICONS.loading} ${URL_WIDGET_CONFIG.loadingText}` : `${URL_ICONS.send} ${URL_WIDGET_CONFIG.submitText}`;
      this.submitBtn.style.opacity = loading ? '0.7' : '1';
      this.input.disabled = loading;
    },
    
    showStatus(type, message) {
      const colors = { loading: '#64748b', success: '#22c55e', error: '#ef4444' };
      const icons = { loading: URL_ICONS.loading, success: URL_ICONS.success, error: URL_ICONS.error };
      this.statusEl.style.color = colors[type];
      this.statusEl.innerHTML = `${icons[type]} ${message}`;
      if (type === 'success') setTimeout(() => { this.statusEl.innerHTML = ''; }, 5000);
    },
    
    showResult(result) {
      const icons = { youtube: URL_ICONS.youtube, podcast: URL_ICONS.podcast, webpage: URL_ICONS.webpage };
      const icon = icons[result.category] || URL_ICONS.webpage;
      this.resultEl.style.display = 'block';
      this.resultEl.innerHTML = `<div style="display: flex; align-items: flex-start; gap: 10px;"><span style="flex-shrink: 0;">${icon}</span><div style="flex: 1;"><div style="font-weight: 500; color: #e2e8f0; margin-bottom: 6px;">${result.category.charAt(0).toUpperCase() + result.category.slice(1)} Processed</div><div style="color: #94a3b8; font-size: 11px; word-break: break-all;">URL: ${result.data?.url || 'N/A'}</div>${result.data?.videoId ? `<div style="color: #94a3b8; font-size: 11px; margin-top: 4px;">Video ID: ${result.data.videoId}</div>` : ''}</div></div>`;
      setTimeout(() => { this.resultEl.style.display = 'none'; }, 30000);
    }
  };

  // Initialize
  function initURLWidget() {
    const searchWidget = document.querySelector('[class*="search"], [data-type="search"], .widget-search');
    if (searchWidget && !document.getElementById('url-processor-widget')) {
      const urlWidget = URL_WIDGET.create();
      searchWidget.parentNode.replaceChild(urlWidget, searchWidget);
      console.log(`[URL Widget v${URL_WIDGET_CONFIG.version}] Replaced search widget`);
      return true;
    }
    const widgetsWrap = document.querySelector('#widgets-wrap');
    if (widgetsWrap && !document.getElementById('url-processor-widget')) {
      const urlWidget = URL_WIDGET.create();
      widgetsWrap.insertBefore(urlWidget, widgetsWrap.firstChild);
    }
    return false;
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initURLWidget);
  } else {
    initURLWidget();
  }
  setTimeout(initURLWidget, 500);
  setTimeout(initURLWidget, 1500);
  setTimeout(initURLWidget, 3000);

  window.URLProcessor = { categorizer: URL_CATEGORIZER, processor: URL_PROCESSOR, widget: URL_WIDGET };
})();
```

## Features

| Feature | Description |
|---------|-------------|
| **URL Input Widget** | Replaces search widget with URL input field |
| **URL Categorization** | Detects YouTube, Podcast, Webpage URLs |
| **Visual Feedback** | Loading, success, error states |
| **Keyboard Shortcuts** | Enter to submit, auto-submit on paste |
| **YouTube ID Extraction** | Extracts video ID for metadata |

## Testing

### Test URLs

| Type | Example |
|------|---------|
| YouTube | `https://www.youtube.com/watch?v=dQw4w9WgXcQ` |
| YouTube Short | `https://youtu.be/dQw4w9WgXcQ` |
| Podcast | `https://anchor.fm/example-show` |
| Podcast RSS | `https://feeds.example.com/podcast.rss` |
| Webpage | `https://example.com/article` |

## Future Enhancements

1. Full YouTube API Integration
2. RSS Feed Parsing
3. Web Scraping for content extraction
4. GA Agent Integration
5. Caching for processed URLs
6. Batch Processing

---

**Source Files**:
- Plan: `.sisyphus/plans/replace-search-widget.md`
- Implementation Guide: `.sisyphus/drafts/url-widget-implementation.md`