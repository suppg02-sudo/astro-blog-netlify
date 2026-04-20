---
pubDatetime: 2026-03-17T00:35:34Z
title: "The Blog-Post-Creator Skill: Unified CLI for Hugo Automation"
postSlug: "the-blog-post-creator-skill-unified-cli-for-hugo-a"
description: "The Blog-Post-Creator Skill: Unified CLI for Hugo Automation"
tags:
  - opencode
  - automation
  - hugo
  - cli
  - blog
---

# The Blog-Post-Creator Skill: A Unified CLI for Hugo Automation

Creating blog posts for Hugo static sites just got a whole lot easier. The **blog-post-creator** skill provides a centralized CLI that handles frontmatter generation, validation, publishing—all from a single command.

## Why Centralized Blog Creation?

Previously, different scripts and workflows had their own blog post creation logic:

- Weekly ecosystem tracker → custom Hugo logic
- YouTube transcription → separate blog flow
- Research summaries → another custom implementation
- News digests → yet another approach

This led to:
- **Duplicated code** across multiple scripts
- **Inconsistent frontmatter** formats
- **Missing validation** in some workflows
- **Manual URL verification** required

The blog-post-creator skill consolidates all of this into one reusable CLI.

## Features

### 1. Automatic Frontmatter Generation

```yaml
---
title: "Your Blog Post Title"
date: 2026-03-17T00:00:00Z
draft: false
slug: "url-friendly-slug"
tags:
  - tag1
  - tag2
categories:
  - Category One
source: "https://optional-source-url.com"
---
```

### 2. Hugo Syntax Validation

Runs `[script resource] to catch:
- Invalid frontmatter
- Broken shortcodes
- Missing required fields

### 3. URL Verification

Automatically verifies the blog post is accessible at `http://localhost:1313/posts/{slug}/`

### 4. Telegram Notifications

Optional notifications when `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` are set.

### 5. Path Sanitization

Removes internal filesystem paths that shouldn't appear in published posts.

## CLI Usage

```bash
# Basic usage
blog-cli.sh --title "My Post" --content "# Content..." --tags "tag1,tag2"

# From file
blog-cli.sh --title "Weekly Report" --file report.md --tags "weekly"

# Full options
blog-cli.sh \
  --title "OpenCode Ecosystem Weekly" \
  --file weekly-report.md \
  --tags "opencode,ai-agents,weekly" \
  --categories "Weekly Tracker" \
  --source "https://github.com/..." \
  --validate \
  --notify

# Dry run (preview)
blog-cli.sh --title "Test" --file test.md --dry-run
```

## Options Reference

| Option | Description | Required |
|--------|-------------|----------|
| `--title` | Blog post title | Yes |
| `--content` | Content as string | Or `--file` |
| `--file` | Read content from file | Or `--content` |
| `--slug` | URL slug (auto-generated) | No |
| `--tags` | Comma-separated tags | No |
| `--categories` | Comma-separated categories | No |
| `--source` | Source URL reference | No |
| `--output` | Output directory | No |
| `--dry-run` | Preview without writing | No |
| `--validate` | Run Hugo validation | No |
| `--notify` | Send Telegram notification | No |

## Integration Examples

### Weekly Ecosystem Tracker

The weekly tracker uses the CLI for automated blog posts:

```bash
# In track_harnesses.py
python3 track_harnesses.py --publish
  → Calls blog-cli.sh with generated content
```

### Cron Jobs

```bash
# Weekly blog post (Sundays 06:00 UTC)
0 6 * * 0 /path/to/script.sh | blog-cli.sh ...
```

### Manual Posts

```bash
# Quick blog post from any markdown file
blog-cli.sh --title "Notes" --file notes.md --tags "notes" --validate
```

## Architecture

```
┌─────────────────────────────────────────────────────┐
│              BLOG-POST-CREATOR SKILL                  │
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │              blog-cli.sh                      │  │
│  │  • YAML frontmatter generation               │  │
│  │  • Hugo syntax validation                   │  │
│  │  • URL verification                         │  │
│  │  • Telegram notifications                   │  │
│  │  • JSON output for scripts                  │  │
│  └───────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
                         ▲
                         │ used by
                         │
┌────────────────────────┴────────────────────────────┐
│                                                         │
│  • Weekly Tracker (cron)                               │
│  • YouTube transcription flow                          │
│  • Research summaries                                  │
│  • Manual blog posts                                   │
│  • Any script needing blog creation                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Benefits

| Benefit | Description |
|---------|-------------|
| **Single source of truth** | All blog posts go through one CLI |
| **Consistent frontmatter** | Same YAML format everywhere |
| **Automatic validation** | Hugo syntax checked before publishing |
| **URL verification** | Confirms post is accessible |
| **Cron-ready** | JSON output for programmatic use |
| **Telegram integration** | Optional notifications |
| **No Hugo build needed** | Dev mode with live reload |

## Location

```
[config resource]
├── SKILL.md           # Full skill documentation
└── scripts/
    └── blog-cli.sh    # The CLI tool
```

---

*Created using the blog-post-creator CLI itself! 🔄*