---
pubDatetime: 2026-02-28T00:25:00Z
title: "Summarize CLI: Fast Summaries for URLs, YouTube, Podcasts & Files"
postSlug: "summarize-cli-setup-guide"
description: "Summarize CLI: Fast Summaries for URLs, YouTube, Podcasts & Files"
tags:
  - llm
  - openrouter
  - cli
  - summarization
  - tools
---

## What is Summarize?

Summarize is a CLI tool and browser extension that provides fast, streaming summaries of web pages, files, and media. It supports URLs, PDFs, images, audio/video, YouTube, podcasts, and RSS feeds, with intelligent extraction and transcript-first processing for media sources.

**Repository:** [https://github.com/steipete/summarize](https://github.com/steipete/summarize)

## Installation

### Prerequisites

- Node.js 22+ (required for SQLite support)
- yt-dlp, ffmpeg (for media processing)
- tesseract (optional, for slide OCR)
- uv/uvx (for PDF preprocessing)

```bash
# Install Node.js 22
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt-get install -y nodejs

# Install media tools
apt-get install -y tesseract-ocr

# Install uv for PDF processing
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Install the CLI

```bash
npm i -g @steipete/summarize@latest
```

## Configuration

Create `~/.summarize/config.json`:

```json
{
  "env": {
    "OPENROUTER_API_KEY": "your-key-here"
  },
  "model": "free",
  "models": {
    "free": {
      "rules": [{
        "candidates": [
          "openrouter/qwen/qwen3-next-80b-a3b-instruct:free",
          "openrouter/arcee-ai/trinity-large-preview:free"
        ]
      }]
    }
  }
}
```

### Refresh Free Models

```bash
summarize refresh-free
```

This fetches available free models from OpenRouter and tests them.

## Usage Examples

### Web Pages

```bash
summarize "https://example.com"
summarize "https://example.com" --length long
```

### YouTube Videos

```bash
summarize "https://www.youtube.com/watch?v=..." --youtube web
```

### Podcasts (RSS)

```bash
summarize "https://feeds.npr.org/500005/podcast.xml"
```

### PDFs

```bash
summarize "https://arxiv.org/pdf/2301.00001.pdf"
summarize "/path/to/local.pdf"
```

### Stdin (Piped Content)

```bash
echo "What is machine learning?" | summarize -
cat document.txt | summarize -
```

## CLI Options

| Option | Description |
|--------|-------------|
| `--length` | short, medium, long, xl, xxl, or character count |
| `--model` | Provider/model ID (e.g., `free`, `openai/gpt-4`) |
| `--youtube` | Transcript source: auto, web, yt-dlp, apify |
| `--extract` | Print extracted content only, no summary |
| `--json` | Structured JSON output with metrics |
| `--verbose` | Debug information |
| `--slides` | Extract slides from YouTube/direct video |

## Key Features

- **Streaming output** with Markdown rendering and metrics
- **YouTube slide extraction** with timestamped cards and OCR
- **Transcript-first processing** for media sources
- **Smart defaults** - returns content as-is when shorter than requested
- **Multiple providers**: OpenAI, Anthropic, Google, xAI, OpenRouter
- **Chrome/Firefox extensions** with Side Panel integration

## Troubleshooting

### TLS Certificate Issues

If you see `fetch failed` with certificate errors:

```bash
export NODE_EXTRA_CA_CERTS=/etc/ssl/certs/ca-certificates.crt
```

Add to `~/.bashrc` for persistence.

### Node.js Version

The tool requires Node.js 22+ for SQLite support. If you see `No such built-in module: node:sqlite`, upgrade Node:

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt-get install -y nodejs
```

## Resources

- [GitHub Repository](https://github.com/steipete/summarize)
- [Chrome Web Store](https://chromewebstore.google.com/detail/summarize/cejgnmmhbbpdmjnfppjdfkocebngehfg)
- [OpenRouter](https://openrouter.ai/) for free model access