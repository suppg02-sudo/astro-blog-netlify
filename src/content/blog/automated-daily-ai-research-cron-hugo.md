---
pubDatetime: 2026-02-24T23:15:00Z
title: "How to Set Up Automated Daily AI Research with Cron and Hugo"
postSlug: "automated-daily-ai-research-cron-hugo"
description: "How to Set Up Automated Daily AI Research with Cron and Hugo"
tags:
  - cron
  - automation
  - hugo
  - ai
  - tutorial
  - python
---

## Overview

This guide shows how to create an automated daily research system that:

1. Fetches latest stats from GitHub repositories
2. Gathers AI news from Hacker News
3. Generates a blog post automatically
4. Publishes to Hugo without manual intervention

## Prerequisites

- Hugo blog installed and running
- Python 3.x
- Cron (usually pre-installed on Linux)
- GitHub API access (no token needed for public repos, but rate-limited)

## Step 1: Create the Research Script

Create the main Python script at `/root/scripts/daily-research/ai_ecosystem_research.py`:

```python
#!/usr/bin/env python3
"""
AI Ecosystem Daily Research - Automated Blog Publisher

Fetches data from GitHub repos and Hacker News,
generates a blog post, and validates it's accessible.
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError

# Configuration
BLOG_DIR = Path("/media/docker/website/content/posts")
LOG_DIR = Path("/root/cron-logs")

REPOS = [
    "anomalyco/opencode",
    "code-yeongyu/oh-my-opencode",
    "darrenhinde/OpenAgentsControl",
    "gsd-build/get-shit-done",
    "CaviraOSS/OpenMemory",
    "mem0ai/mem0",
    "thedotmack/claude-mem",
    "letta-ai/letta",
    "supermemoryai/supermemory",
    "google/adk-python",
]

def fetch_json(url: str) -> dict:
    """Fetch JSON from URL."""
    req = Request(url)
    req.add_header("Accept", "application/json")
    req.add_header("User-Agent", "Daily-Research/1.0")
    try:
        with urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode())
    except:
        return {}

def get_repo_data(repo: str) -> dict:
    """Get repository data from GitHub API."""
    data = fetch_json(f"https://api.github.com/repos/{repo}")
    return {
        "name": repo.split("/")[-1],
        "full_name": repo,
        "stars": data.get("stargazers_count", 0),
        "updated": data.get("pushed_at", "unknown")[:10],
        "language": data.get("language", "unknown"),
    }

def get_hacker_news_top(limit: int = 10) -> list:
    """Get top Hacker News stories."""
    try:
        ids = fetch_json("https://hacker-news.firebaseio.com/v0/topstories.json")
        stories = []
        for sid in ids[:limit]:
            story = fetch_json(f"https://hacker-news.firebaseio.com/v0/item/{sid}.json")
            if story:
                stories.append({
                    "title": story.get("title", ""),
                    "url": story.get("url", f"https://news.ycombinator.com/item?id={sid}"),
                    "score": story.get("score", 0),
                })
        return stories
    except:
        return []

def generate_blog_post(repos_data: list, hn_stories: list) -> tuple[str, str]:
    """Generate blog post content."""
    today = datetime.now()
    date_str = today.strftime("%Y-%m-%d")
    slug = f"ai-ecosystem-daily-research-{date_str}"
    datetime_iso = today.strftime("%Y-%m-%dT%H:%M:%SZ")
    
    repos_data.sort(key=lambda x: x["stars"], reverse=True)
    
    # Build frontmatter
    content = f'''---
title: "AI Ecosystem Daily Research - {today.strftime('%B %d, %Y')}"
slug: "{slug}"
date: {datetime_iso}
draft: false
tags: ["research", "ai-ecosystem", "daily"]
categories: ["Daily Research"]
---

## Ecosystem Snapshot

| Project | Stars | Updated | Language |
|---------|-------|---------|----------|
'''
    
    for repo in repos_data:
        content += f'| [{repo["name"]}](https://github.com/{repo["full_name"]}) | {repo["stars"]:,} | {repo["updated"]} | {repo["language"]} |\n'
    
    # Add AI news from HN
    ai_keywords = ["ai", "llm", "claude", "gpt", "agent", "model"]
    ai_stories = [s for s in hn_stories if any(k in s["title"].lower() for k in ai_keywords)]
    
    if ai_stories:
        content += "\n---\n\n## AI News from Hacker News\n\n"
        for story in ai_stories[:5]:
            content += f'- [{story["title"]}]({story["url"]}) ({story["score"]} pts)\n'
    
    content += f"\n---\n\n*Generated at {datetime_iso}*"
    
    return content, slug

def main():
    today = datetime.now()
    date_str = today.strftime("%Y-%m-%d")
    log_file = LOG_DIR / f"daily-research-{date_str}.log"
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    
    print(f"[{datetime.now()}] Starting daily research...")
    
    # Fetch repo data
    repos_data = [get_repo_data(repo) for repo in REPOS]
    repos_data = [r for r in repos_data if r["stars"] > 0]
    
    # Fetch HN stories
    hn_stories = get_hacker_news_top(20)
    
    # Generate blog post
    content, slug = generate_blog_post(repos_data, hn_stories)
    
    # Write to Hugo
    blog_file = BLOG_DIR / f"{date_str}-{slug}.md"
    BLOG_DIR.mkdir(parents=True, exist_ok=True)
    blog_file.write_text(content)
    
    print(f"[{datetime.now()}] Blog post written: {blog_file}")
    
    # Wait for Hugo rebuild
    import time
    time.sleep(3)
    
    # Verify
    result = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
         f"http://localhost:1313/posts/{slug}/"],
        capture_output=True, text=True
    )
    
    if result.stdout.strip() == "200":
        print(f"SUCCESS: http://localhost:1313/posts/{slug}/")
    else:
        print(f"WARNING: HTTP {result.stdout.strip()}")

if __name__ == "__main__":
    main()
```

## Step 2: Make Script Executable

```bash
chmod +x /root/scripts/daily-research/ai_ecosystem_research.py
```

## Step 3: Test the Script

Run manually to verify it works:

```bash
python3 /root/scripts/daily-research/ai_ecosystem_research.py
```

Expected output:
```
[2026-02-24 23:00:45] Starting daily research...
[2026-02-24 23:00:54] Blog post written: /media/docker/website/content/posts/2026-02-24-ai-ecosystem-daily-research-2026-02-24.md
SUCCESS: http://localhost:1313/posts/ai-ecosystem-daily-research-2026-02-24/
```

## Step 4: Add Cron Job

Edit crontab:

```bash
crontab -e
```

Add this line to run daily at 8:00 AM UTC:

```
0 8 * * * /usr/bin/python3 /root/scripts/daily-research/ai_ecosystem_research.py >> /root/cron-logs/daily-research.log 2>&1
```

Or add programmatically:

```bash
(crontab -l 2>/dev/null | grep -v "daily-research"; echo "0 8 * * * /usr/bin/python3 /root/scripts/daily-research/ai_ecosystem_research.py >> /root/cron-logs/daily-research.log 2>&1") | crontab -
```

## Step 5: Create Log Directory

```bash
mkdir -p /root/cron-logs
```

## Step 6: Verify Cron Job

```bash
crontab -l | grep daily-research
```

## Customization

### Change Schedule

Edit the cron timing:

| Schedule | Cron Expression |
|----------|-----------------|
| Every day at 8 AM | `0 8 * * *` |
| Every day at 6 AM | `0 6 * * *` |
| Every 12 hours | `0 */12 * * *` |
| Every Monday at 9 AM | `0 9 * * 1` |

### Add More Repositories

Edit the `REPOS` list in the script:

```python
REPOS = [
    "owner/repo-name",
    # Add your repos here
]
```

### Change Blog Directory

Update the `BLOG_DIR` variable:

```python
BLOG_DIR = Path("/path/to/your/hugo/content/posts")
```

## Monitoring

### Check Logs

```bash
# View today's log
cat /root/cron-logs/daily-research.log

# View specific date
cat /root/cron-logs/daily-research-20260224.log
```

### Check Blog Posts

```bash
ls -la /media/docker/website/content/posts/*daily-research*
```

### Verify URL

```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:1313/posts/ai-ecosystem-daily-research-$(date +%Y-%m-%d)/
```

## Troubleshooting

### Script Not Running

1. Check cron is running: `systemctl status cron`
2. Check script permissions: `ls -la /root/scripts/daily-research/ai_ecosystem_research.py`
3. Check Python path: `which python3`

### Blog Post Not Generated

1. Check Hugo is running: `curl http://localhost:1313`
2. Check directory exists: `ls -la /media/docker/website/content/posts/`
3. Check file permissions

### API Rate Limits

GitHub API has rate limits for unauthenticated requests (60/hour). For higher limits, add a token:

```python
def fetch_json(url: str) -> dict:
    req = Request(url)
    req.add_header("Authorization", "token YOUR_GITHUB_TOKEN")
    # ...
```

## Summary

| File | Purpose |
|------|---------|
| `/root/scripts/daily-research/ai_ecosystem_research.py` | Main research script |
| `/root/cron-logs/daily-research.log` | Combined log file |
| `/root/cron-logs/daily-research-YYYYMMDD.log` | Daily log files |
| `/media/docker/website/content/posts/YYYY-MM-DD-slug.md` | Generated blog posts |

---

*Tutorial published: February 24, 2026*