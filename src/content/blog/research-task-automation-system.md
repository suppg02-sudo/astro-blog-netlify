---
pubDatetime: 2026-02-28T15:00:00Z
title: "Building an Automated Research Task System with Brave Search and GitHub APIs"
postSlug: "research-task-automation-system"
description: "Building an Automated Research Task System with Brave Search and GitHub APIs"
tags:
  - github-api
  - automation
  - hugo
  - research
  - brave-search
  - python
---

# Building an Automated Research Task System

A complete walkthrough of how I fixed a broken research automation system and rebuilt it with API-based research instead of CLI dependencies.

## The Problem

A research task submitted from the Homepage interface created an empty stub blog post instead of actual research:

```
[2026-02-27 23:40:49] OpenCode CLI not found, creating research directly
/config/scripts/execute-research.sh: line 190: docker: command not found
```

The root cause: The research-task container (`python:3.11-alpine`) didn't have OpenCode CLI available, and the script silently fell back to creating placeholder content.

## The Solution

Replaced the OpenCode CLI dependency with a **Python-based research engine** that uses external APIs directly.

### Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Homepage Form  │────▶│  Research API    │────▶│   Hugo Blog     │
│  (port 8898)    │     │  (Python/Flask)  │     │   (port 1313)   │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        ▼                      ▼                      ▼
   ┌─────────┐           ┌──────────┐          ┌──────────┐
   │  Brave  │           │ Context7 │          │  GitHub  │
   │  Search │           │   Docs   │          │   API    │
   └─────────┘           └──────────┘          └──────────┘
```

### Key Components

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Research Engine** | Python script | Orchestrates API calls, synthesizes results |
| **Web Search** | Brave API | Current news, blog posts, tutorials |
| **Code Examples** | GitHub API | Real implementation examples |
| **Output** | Hugo markdown | Blog posts with frontmatter |
| **UI** | Flask web app | Form submission + history viewer |

## Implementation

### 1. Python Research Engine

```python
class ResearchEngine:
    def __init__(self, brave_api_key: str, github_token: str = None):
        self.brave_api_key = brave_api_key
        self.github_token = github_token
        
    def brave_search(self, query: str, count: int = 10) -> List[Dict]:
        """Search the web using Brave Search API."""
        url = "https://api.search.brave.com/res/v1/web/search"
        headers = {
            'Accept': 'application/json',
            'X-Subscription-Token': self.brave_api_key
        }
        # ... API call implementation
        
    def github_search(self, query: str, count: int = 10) -> List[Dict]:
        """Search GitHub for repositories."""
        url = "https://api.github.com/search/repositories"
        # ... API call implementation
```

### 2. Docker Compose Configuration

```yaml
services:
  research-task:
    image: python:3.11-slim
    container_name: research-task
    volumes:
      - ./app.py:/app/app.py:ro
      - ./research_engine.py:/app/research_engine.py:ro
      - ./scripts:/config/scripts:ro
      - /tmp:/tmp
      - /var/log:/var/log
      - /media/docker/website/content/posts:/media/docker/website/content/posts
      - /root/.opencode.env:/root/.opencode.env:ro
    network_mode: host
    environment:
      - HUGO_CONTENT_DIR=/media/docker/website/content/posts
```

Note: Changed from `python:3.11-alpine` to `python:3.11-slim` because Alpine uses musl libc which can't run glibc binaries.

### 3. Scheduled Research Topics

```json
{
  "topics": [
    {
      "id": "daily-ai-news",
      "topic": "latest AI news and developments",
      "intensity": "quick",
      "schedule": "daily",
      "cron": "0 8 * * *"
    },
    {
      "id": "weekly-ecosystem",
      "topic": "AI coding agent ecosystem updates",
      "intensity": "standard",
      "schedule": "weekly",
      "cron": "0 8 * * 1"
    }
  ]
}
```

Cron jobs added:
```bash
0 8 * * * /media/docker/research-task/scripts/run-scheduled-research.sh daily-ai-news
0 8 * * 1 /media/docker/research-task/scripts/run-scheduled-research.sh weekly-ecosystem
0 9 * * 2 /media/docker/research-task/scripts/run-scheduled-research.sh weekly-rag-developments
0 8 1 * * /media/docker/research-task/scripts/run-scheduled-research.sh monthly-agent-tools
```

### 4. Research History Web UI

Added `/history` endpoint to view past research:

```python
@app.route('/history')
def history():
    return render_template_string(HISTORY_TEMPLATE)

@app.route('/api/history')
def api_history():
    # Parse Hugo posts and return JSON
    posts = []
    for filepath in glob.glob(f'{posts_dir}/*.md'):
        # Parse frontmatter, extract title, date, tags
        # Return preview and URL
    return jsonify({'posts': posts[:50]})
```

## Results

### Test Run

```
Topic: OpenCode AI agent framework
Web Sources: 7
GitHub Sources: 5
Confidence: high
Blog Post: http://ubuntu4:1313/posts/opencode-ai-agent-framework/
```

### Generated Blog Post Structure

```markdown
---
title: "Research: OpenCode AI agent framework"
date: 2026-02-28T14:46:25Z
tags: [research, ai, coding]
---

## Executive Summary
- Found 5 relevant web resources
- Top sources include: Agents | OpenCode, GitHub repos
- Trending repositories: OpenAgentsControl, kelos, AgentStack

## Key Findings
### 1. Agents | OpenCode
[Content from Brave search results...]

## Trending Repositories
| Repository | Stars | Description |
|------------|-------:|-------------|
| darrenhinde/OpenAgentsControl | 2,280 | AI agent framework... |

## Sources
### Web Resources
- [Agents | OpenCode](https://opencode.ai/docs/agents/)
- [GitHub - opencode-ai/opencode](https://github.com/opencode-ai/opencode)

### GitHub Repositories
- darrenhinde/OpenAgentsControl - 2,280 stars
```

## URLs

| Feature | URL |
|---------|-----|
| New Research Form | http://ubuntu4:8898 |
| Research History | http://ubuntu4:8898/history |
| History API | http://ubuntu4:8898/api/history |
| Scheduled Topics API | http://ubuntu4:8898/api/scheduled |

## Lessons Learned

1. **Alpine vs Debian**: Alpine uses musl libc which can't run glibc binaries. Use `python:3.11-slim` for compatibility.

2. **Gzip encoding**: Brave API returns gzipped content even when not requested. Handle `Content-Encoding: gzip` in the response.

3. **Silent failures are dangerous**: The original script created stubs instead of failing loudly. Always exit with error code when something goes wrong.

4. **API-first approach**: Using APIs directly instead of CLI tools makes automation more reliable and container-friendly.

## Files Created/Modified

| File | Purpose |
|------|---------|
| `research_engine.py` | API-based research engine |
| `scripts/execute-research.sh` | Updated for Python engine |
| `scripts/run-scheduled-research.sh` | Cron runner |
| `recurring-topics.json` | Topic configuration |
| `app.py` | Added history routes |
| `docker-compose.yml` | Simplified configuration |

---

*This system now runs fully automated research tasks with scheduled daily, weekly, and monthly topics, generating Hugo blog posts automatically.*