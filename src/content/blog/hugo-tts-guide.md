---
pubDatetime: 2026-02-02T09:00:00Z
title: "Hugo Blog Audio System: Complete TTS Integration Guide"
postSlug: "hugo-tts-guide"
description: "Hugo Blog Audio System: Complete TTS Integration Guide"
tags:
  - tts
  - hugo
  - blog
---

Hugo Blog Audio System: Complete TTS Integration Guide

## Overview

This guide documents the complete Text-to-Speech (TTS) integration for Hugo blog posts, enabling automatic audio generation for all your content using Google's free gTTS engine.

{{< audio src="/posts/audio/system-update-january-25-2026.mp3" title="Listen to this guide" >}}

## ✅ System Status

**Fully Operational**: February 2, 2026
**Engine**: Google Text-to-Speech (gTTS) - 100% FREE
**Cost**: $0.00 (no API fees, completely free)

## Core Components

### 1. TTS Conversion Script

**Location**: `/media/docker/tts-service/blog-to-audio.py`

**Purpose**: Converts Hugo markdown posts to MP3 audio files

**Key Features**:
- Smart markdown cleaning (removes code blocks, frontmatter, images)
- Automatic chunking for long posts (max 4500 chars)
- Progress bars with tqdm
- Batch conversion support for multiple posts
- Single post conversion with `--force` flag

**Python Dependencies**:
- `gtts` - Google Text-to-Speech API
- `tqdm` - Progress bars
- `beautifulsoup4` - HTML parsing

**Script Capabilities**:
```
Smart Text Processing:
- Removes YAML frontmatter (between --- markers)
- Strips code blocks (```)
- Removes inline code (`) markdown syntax
- Removes image links ![alt](url)
- Removes HTML tags
- Cleans extra whitespace

Chunking Strategy:
- Maximum 4500 characters per chunk
- Long posts automatically split
- Each chunk converted separately
- Maintains audio quality limits
```

### 2. Hugo Audio Shortcode

**Location**: `/media/docker/website/layouts/shortcodes/audio.html`

**Purpose**: Embeds styled audio player in blog posts

**Shortcode Syntax**:
```markdown
{{< audio src="/posts/audio/filename.mp3" title="Listen to this post" >}}
```

**Shortcode Features**:
- Custom title support
- Styled audio controls
- Download MP3 link
- Responsive design
- Clean, modern styling

**Audio Player Styling**:
```html
- Background: Light gray (#f5f5f5)
- Border: Blue accent (#007bff)
- Left border accent: 4px solid blue
- Padding: 20px
- Rounded corners: 8px
- Full audio controls (play, pause, seek, volume)
```

### 3. Automated Workflow Scripts

#### Quick Converter Script

**Location**: `/media/docker/tts-service/convert-post.sh`

**Usage Examples**:
```bash
cd /media/docker/tts-service

# Convert all posts
./convert-post.sh all

# Reconvert all posts (force regeneration)
./convert-post.sh all --force

# Convert specific post
./convert-post.sh "2026-02-01-my-post"

# Reconvert specific post (force regeneration)
./convert-post.sh "2026-02-01-my-post" --force
```

#### Auto-Watcher Script

**Location**: `/media/docker/tts-service/watch-posts.sh`

**Purpose**: Automatically converts new/modified posts

**Status**: Ready to use (inotify-tools installed)

**Usage**:
```bash
cd /media/docker/tts-service

# Runs in background, monitors posts directory
./watch-posts.sh &
```

**How It Works**:
- Monitors `/media/docker/website/content/posts/` for changes
- Automatically detects new .md files
- Triggers audio conversion for new posts
- Skips existing audio files (no regeneration)
- Runs continuously in background

## Directory Structure

```
/media/docker/tts-service/
├── venv/                      # Python virtual environment
│   ├── bin/python3          # Python 3.12.3 with gTTS
│   └── lib/python*/site-packages/
│       ├── gtts/              # Google Text-to-Speech
│       ├── tqdm/              # Progress bars
│       └── beautifulsoup4/    # HTML parsing
├── blog-to-audio.py           # Main conversion script
├── watch-posts.sh              # Auto-watcher (ready)
├── convert-post.sh             # Quick converter (ready)
└── README.md                  # Full documentation

/media/docker/website/
├── content/posts/
│   ├── **/*.md               # Your blog posts
│   └── audio/               # Generated MP3 files (auto-created)
│       └── **/*.mp3
└── layouts/shortcodes/
    └── audio.html             # Hugo audio shortcode
```

## Usage Guide

### Option 1: Manual Conversion (Quick)

**Step 1: Write your blog post** normally in Hugo

**Step 2: Convert to audio**:
```bash
cd /media/docker/tts-service
./convert-post.sh "2026-02-01-my-post"
```

**Step 3: Add audio to post**:
```markdown
---
title: "My Blog Post"
date: 2026-02-01T12:00:00Z
draft: false
tags: ["tag1", "tag2"]
categories: ["Category"]
---

{{< audio src="/posts/audio/2026-02-01-my-post.mp3" title="Listen to this post" >}}

## Content

Your blog content here...
```

**Step 4: Publish** - Audio player appears automatically!

### Option 2: Automatic Workflow (Recommended)

**Step 1: Start the auto-watcher** (runs in background):
```bash
cd /media/docker/tts-service
./watch-posts.sh &
```

**Step 2: Write blog post** in Hugo as usual

**Step 3: Auto-convert** - Script detects new .md file and converts to audio

**Step 4: Add audio shortcode** (optional, but recommended)

**Step 5: Done** - Audio ready when you finish writing!

### Option 3: Batch Convert All Posts

```bash
cd /media/docker/tts-service
./convert-post.sh all
```

## Performance Benchmarks

**Conversion Speeds**:
- **Small posts** (<1000 chars): 1-2 seconds
- **Medium posts** (1K-5K chars): 30-45 seconds
- **Large posts** (5K-20K chars): 2-4 minutes
- **Very large** (>20K chars): Scales with content

**Average audio file size**: 1-4 MB per post

## Audio Player Features

The Hugo shortcode provides:

- ✅ **Styled container** with light gray background
- ✅ **Custom title support** with "Listen:" prefix
- ✅ **Full audio controls** (play, pause, seek, volume)
- ✅ **Download link** for offline listening
- ✅ **Responsive design** - works on mobile
- ✅ **HTML5 compatible** - works in all modern browsers

## Important Notes

### File Naming Convention

Audio files automatically match markdown files:
```
2026-02-01-my-post.md → 2026-02-01-my-post.mp3
```

### Automatic Skipping Rules

- **Short posts** (<50 chars): Automatically skipped - too brief for meaningful audio
- **Existing audio**: Automatically skipped to avoid regenerating
- **Code blocks**: Removed from audio - only readable content is converted

### Content Filtering

The TTS script intelligently filters content:
- ✅ **YAML frontmatter**: Excluded from audio conversion automatically
- ✅ **Code blocks**: Stripped to avoid reading syntax aloud
- ✅ **Image links**: Excluded (alt text might be read if present)
- ✅ **HTML tags**: Removed for clean audio

## Production Deployment

### Systemd Service (For auto-start on boot)

**Create service file**:
```bash
sudo nano /etc/systemd/system/hugo-audio-watcher.service
```

**Paste this content**:
```ini
[Unit]
Description=Hugo Blog Audio Watcher
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/media/docker/tts-service
ExecStart=/media/docker/tts-service/watch-posts.sh
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**Enable and start**:
```bash
sudo systemctl daemon-reload
sudo systemctl enable hugo-audio-watcher
sudo systemctl start hugo-audio-watcher
```

**Check status**:
```bash
sudo systemctl status hugo-audio-watcher
```

## Integration with Hugo

### Permalink Structure

Audio files are accessible via Hugo's permalink structure:
```
/posts/audio/filename.mp3
```

This matches the standard Hugo permalink configuration:
```toml
[permalinks]
  posts = "/:year/:month/:day/:slug/"
```

### Audio Directory Location

Audio files are stored in `/media/docker/website/content/posts/audio/` which gets:

1. **Built into** `/media/docker/website/public/posts/audio/`
2. **Accessible at**: `http://ubuntu58-1:1314/posts/audio/filename.mp3`
3. **Served as**: Static MP3 files

## Complete Documentation

Full documentation available at:
```
/media/docs/output/hugo-blog-audio-setup-complete.md
/media/docker/tts-service/README.md
```

## Summary

Your Hugo blog now has full audio conversion capabilities:

1. **Write posts** normally in markdown
2. **Convert to audio** manually or automatically
3. **Embed audio player** with simple shortcode
4. **Publish** - Readers can listen to your posts!

**Total Cost**: $0.00 (completely free!)
**Setup Time**: ~15 minutes
**Maintenance**: Minimal (auto-watches for new posts)

---

**Created**: February 2, 2026
**Status**: ✅ Production Ready
**Audio Engine**: Google Text-to-Speech (gTTS)
**Integration**: Hugo Shortcode + Python Automation