---
pubDatetime: 2026-03-01T21:46:00Z
title: "System Flow Documentation: All User Workflows Mapped"
postSlug: "system-flow-documentation-all-workflows"
description: "System Flow Documentation: All User Workflows Mapped"
tags:
  - flows
  - system-architecture
  - youtube
  - admin
  - documentation
  - research
---

This document maps all regular workflows in the system with exact component chains and data flow notation.

## Flow Notation Key

```
A > B > C > D = Sequential flow (A triggers B, which triggers C, etc.)
[A] = Optional/conditional step
{data} = Data artifact produced
--> HTTP = HTTP request
--> Shell = Shell command execution
```

---

## 1. YouTube URL via Homepage Widget

The primary flow for processing YouTube videos initiated from the dashboard.

### Exact Flow

```
Homepage Widget (custom.js)
  > Relay (port 8899) GET /?action=process-url&url=...
  > OliveTin (port 1337) POST /api/StartAction {"bindingId":"process-url"}
  > process-url-wrapper.sh (Docker container: python:3.11-slim)
  > process-url.sh (Phase 1-1B only)
  > youtube_transcript_extractor.py (Python script)
  > {transcript.json, transcript.txt} saved to ~/.config/opencode/docs/output/
  > validate-youtube-transcript.sh (Phase 1B quality gate)
  > {queue entry} appended to /root/tmp/pending-summarization.txt
```

### Components

| Component | Location | Port | Purpose |
|-----------|----------|------|---------|
| Homepage Widget | /media/docker/home/config/custom.js | 8765 | User input URL |
| Relay | /media/docker/relay/relay.py | 8899 | GET-to-POST converter |
| OliveTin | /media/docker/olivetin/ | 1337 | Action orchestrator |
| Wrapper | /media/docker/olivetin/config/scripts/process-url-wrapper.sh | - | Container launcher |
| Processor | /media/docker/olivetin/config/scripts/process-url.sh | - | Main script |
| Extractor | /media/docker/commands/youtube_transcript_extractor.py | - | Transcript extraction |
| Validator | /media/docker/commands/validate-youtube-transcript.sh | - | Quality gate |

### Data Artifacts

```
Input:  YouTube URL (e.g., https://www.youtube.com/watch?v=VIDEO_ID)
Output: ~/.config/opencode/docs/output/youtube_[slug]_[VIDEO_ID]_[timestamp].json
        ~/.config/opencode/docs/output/youtube_[slug]_[VIDEO_ID]_[timestamp].txt
        /root/tmp/pending-summarization.txt (queue entry)
```

### Flow Diagram

{{< mermaid >}}
flowchart LR
    A[Homepage Widget] -->|GET ?action=process-url| B[Relay:8899]
    B -->|POST StartAction| C[OliveTin:1337]
    C -->|Docker exec| D[process-url-wrapper.sh]
    D -->|bash| E[process-url.sh]
    E -->|python3| F[youtube_transcript_extractor.py]
    F -->|writes| G[transcript.json]
    F -->|writes| H[transcript.txt]
    E -->|validates| I[validate-youtube-transcript.sh]
    I -->|appends| J[pending-summarization.txt]
{{< /mermaid >}}

---

## 2. YouTube URL via Chat (Direct Paste)

When a YouTube URL is pasted directly into the OpenCode chat, the agent handles all phases internally.

### Exact Flow

```
User pastes YouTube URL in chat
  > Agent detects YouTube URL pattern (trigger: youtube.md)
  > Agent executes Phase 1: youtube_transcript_extractor.py (via bash)
  > Agent executes Phase 1B: validate-youtube-transcript.sh (via bash)
  > Agent reads transcript file
  > Agent generates Phase 2: Comprehensive Summary (internal LLM)
  > Agent generates Phase 3: Short Summary (internal LLM)
  > Agent creates Phase 4: Blog Post (writes to Hugo content/posts/)
  > Agent creates Phase 4B: Flow Documentation Post
  > [Phase 5: Post-processing options - optional, 10s timeout]
  > Hugo auto-rebuild (systemd: hugo-blog.service)
  > {Blog post live at http://ubuntu4:1314/posts/slug/}
```

### Components

| Component | Location | Purpose |
|-----------|----------|---------|
| Agent | OpenCode (GLM-5) | All phases 1-4B |
| Extractor | /media/docker/commands/youtube_transcript_extractor.py | Phase 1 |
| Validator | /media/docker/commands/validate-youtube-transcript.sh | Phase 1B |
| Hugo | /media/docker/website/ | Blog publishing |
| Trigger | ~/.config/opencode/docs/instructions/triggers/youtube.md | Protocol definition |

### Key Differences from Homepage Flow

| Aspect | Homepage Widget | Chat Paste |
|--------|-----------------|------------|
| Phases 1-1B | OliveTin/Docker | Agent direct bash |
| Phases 2-4B | Queued for agent | Immediate agent execution |
| Summarization | Requires manual trigger | Automatic |
| Blog creation | Separate step | Immediate |

### Flow Diagram

{{< mermaid >}}
flowchart TD
    A[YouTube URL in Chat] -->|Agent detects| B[Phase 1: Extract Transcript]
    B -->|bash| C[youtube_transcript_extractor.py]
    C -->|reads| D[Phase 1B: Validate]
    D -->|quality gate| E{Pass?}
    E -->|Yes| F[Phase 2: Comprehensive Summary]
    E -->|No| Z[ERROR: Stop]
    F -->|LLM| G[Phase 3: Short Summary]
    G -->|LLM| H[Phase 4: Create Blog Post]
    H -->|writes| I[Hugo content/posts/]
    H -->|writes| J[Phase 4B: Flow Doc Post]
    I -->|triggers| K[Hugo Rebuild]
    K -->|serves| L[Blog Live:1314]
{{< /mermaid >}}

---

## 3. Research App Flow

The Re-Search application for AI-powered research queries.

### Exact Flow

```
Homepage > Re-Search button > http://ubuntu4:8898
  > User enters research query in Flask app
  > research_engine.py processes query
  > [External API calls for data gathering]
  > Results displayed in web UI
  > [Optional: Create blog post from research]
```

### Components

| Component | Location | Port | Purpose |
|-----------|----------|------|---------|
| Homepage | /media/docker/home/config/services.yaml | 8765 | Dashboard link |
| Research App | /media/docker/research-task/ | 8898 | Flask application |
| App Logic | /media/docker/research-task/app.py | - | Main Flask routes |
| Engine | /media/docker/research-task/research_engine.py | - | Research processing |
| Scripts | /media/docker/research-task/scripts/ | - | Helper scripts |

### Container Configuration

```yaml
# /media/docker/research-task/docker-compose.yml
image: python:3.11-slim
network_mode: host
volumes:
  - ./app.py:/app/app.py:ro
  - /media/docker/website/content/posts:/media/docker/website/content/posts
```

### Flow Diagram

{{< mermaid >}}
flowchart LR
    A[Homepage:8765] -->|click| B[Re-Search:8898]
    B -->|query| C[app.py Flask]
    C -->|process| D[research_engine.py]
    D -->|gather| E[External APIs]
    E -->|results| F[Web UI Display]
    F -->|optional| G[Create Blog Post]
{{< /mermaid >}}

---

## 4. Production App Flow

The Production task management application.

### Exact Flow

```
Homepage > Production button > http://ubuntu4:8897
  > User manages production tasks
  > Flask app handles task CRUD
  > Tasks stored in config files
  > Status updates logged
```

### Components

| Component | Location | Port | Purpose |
|-----------|----------|------|---------|
| Homepage | /media/docker/home/config/services.yaml | 8765 | Dashboard link |
| Production App | /media/docker/production-task/ | 8897 | Flask application |
| App Logic | /media/docker/production-task/app.py | - | Main Flask routes |
| Config | /media/docker/production-task/config/ | - | Task configurations |

### Container Configuration

```yaml
# /media/docker/production-task/docker-compose.yml
image: python:3.11-alpine
network_mode: host
command: gunicorn + Flask
```

### Flow Diagram

{{< mermaid >}}
flowchart LR
    A[Homepage:8765] -->|click| B[Production:8897]
    B -->|CRUD| C[app.py Flask]
    C -->|read/write| D[config/]
    C -->|log| E[/var/log/production-tasks.log]
{{< /mermaid >}}

---

## 5. Admin Task Flows

All administrative tasks triggered from Homepage > Admin section.

### 5.1 Health Check

```
Homepage > Health Check button
  > http://ubuntu4:8899?action=health-check
  > Relay GET > OliveTin POST > health-check.sh
  > Script runs: docker ps, systemctl status, disk checks
  > {results logged to /var/log/}
```

### 5.2 System Audit (Last 10 Minutes)

```
Homepage > Audit last 10 mins button
  > http://ubuntu4:8899?action=system-audit
  > Relay GET > OliveTin POST > system-audit.sh
  > Script analyzes: logs, processes, network, errors
  > {report generated}
```

### 5.3 Last Hour Performance

```
Homepage > Last Hour Performance button
  > http://ubuntu4:8899?action=last-hour-performance
  > Relay GET > OliveTin POST > last-hour-performance.sh
  > Script analyzes: CPU, memory, disk I/O, Docker stats
  > {performance report generated}
```

### 5.4 Daily System Report

```
Homepage > Daily System Report button
  > http://ubuntu4:8899?action=daily-system-report
  > Relay GET > OliveTin POST > daily-system-report.sh
  > Script generates: comprehensive daily report
  > {report saved and logged}
```

### 5.5 Restart Portainer

```
Homepage > Restart Portainer button
  > http://ubuntu4:8899?action=restart-portainer
  > Relay GET > OliveTin POST > restart-portainer.sh
  > Script: docker restart portainer
  > {container restarted}
```

### 5.6 Reinstall Plugins

```
Homepage > Reinstall Plugins button
  > http://ubuntu4:8899?action=reinstall-plugins
  > Relay GET > OliveTin POST > reinstall-plugins.sh
  > Script reinstalls: oh-my-opencode, OAC agents
  > {plugins reinstalled, OpenCode restarted}
```

### 5.7 Reboot Server

```
Homepage > Reboot Server button
  > http://ubuntu4:8899?action=reboot-server
  > Relay GET > OliveTin POST > reboot-server.sh
  > Script: sudo reboot (with safety checks)
  > {server reboots}
```

### 5.8 Theme Switcher

```
Homepage > Theme dropdown (footer)
  > Select theme > http://ubuntu4:8899?action=theme-dark-blue
  > Relay GET > OliveTin POST > set-dark-blue.sh
  > Script updates: /media/docker/home/config/settings.yaml
  > {Homepage reloads with new theme}
```

### Admin Flow Diagram

{{< mermaid >}}
flowchart TD
    subgraph Homepage
        A[Admin Section]
    end
    
    subgraph Relay
        B[:8899]
    end
    
    subgraph OliveTin
        C[:1337]
    end
    
    subgraph Scripts
        D[health-check.sh]
        E[system-audit.sh]
        F[last-hour-performance.sh]
        G[daily-system-report.sh]
        H[restart-portainer.sh]
        I[reinstall-plugins.sh]
        J[reboot-server.sh]
        K[set-theme-*.sh]
    end
    
    A -->|action=| B
    B -->|POST| C
    C --> D
    C --> E
    C --> F
    C --> G
    C --> H
    C --> I
    C --> J
    C --> K
{{< /mermaid >}}

---

## 6. Summarization Flow (Auto-Summarize)

Processing queued YouTube videos for summarization.

### Exact Flow

```
Trigger: 'summarize' or 'pending' in chat
  OR
Homepage > Auto-Summarize button > http://ubuntu4:8899?action=auto-summarize-pending
  > Relay handles summarize action directly (no OliveTin)
  > relay.py executes: python3 /commands/auto_summarize.py
  > auto_summarize.py reads: /root/tmp/pending-summarization.txt
  > For each queued video:
    > Read transcript file
    > Call Zhipu GLM API (glm-4-flash) for comprehensive summary
    > Call API again for short summary
    > Update blog post with summaries
    > Mark queue entry as 'processed'
  > Hugo rebuild
  > {Summarized blog posts live}
```

### Components

| Component | Location | Purpose |
|-----------|----------|---------|
| Trigger | AGENTS.md | 'summarize' or 'pending' keyword |
| Relay | /media/docker/relay/relay.py | Direct execution (lines 131-158) |
| Script | /media/docker/commands/auto_summarize.py | Main summarization logic |
| Queue | /root/tmp/pending-summarization.txt | Queue file |
| API | Zhipu GLM (open.bigmodel.cn) | LLM summarization |
| Hugo | /media/docker/website/ | Blog publishing |

### Queue Entry Format

```
URL|transcript_file|post_file|timestamp|status
```

Example:
```
https://youtube.com/watch?v=abc123|/root/.config/opencode/docs/output/youtube_..._abc123.txt|/media/docker/website/content/posts/youtube-abc123-slug.md|2026-03-01T12:00:00|queued
```

### Flow Diagram

{{< mermaid >}}
flowchart TD
    A[Trigger: summarize] -->|direct| B[relay.py]
    B -->|exec| C[auto_summarize.py]
    C -->|read| D[pending-summarization.txt]
    D -->|for each| E{Queued entry?}
    E -->|Yes| F[Read transcript]
    F -->|API call| G[Zhipu GLM: Comprehensive]
    G -->|API call| H[Zhipu GLM: Short]
    H -->|update| I[Blog Post]
    I -->|mark| J[processed]
    J --> E
    E -->|No more| K[Hugo rebuild]
    K -->|done| L[Complete]
{{< /mermaid >}}

---

## 7. Content Creation Apps Flow

### 7.1 Website (Astro)

```
Homepage > Website button > http://ubuntu4:8086
  > Astro development server (port 4321 mapped to 8086)
  > Container: astro-fresh
  > Live preview of Astro landing pages
```

### 7.2 Hacker News Feed

```
Homepage > Hacker News widget
  > Custom API widget fetching from FreshRSS
  > URL: http://freshrss/api/greader.php/reader/api/0/stream/contents?n=100
  > Displays top 5 stories in widget
  > Click opens original article
```

---

## 8. Daily Research Flow (Cron)

Automated daily research published as blog posts.

### Exact Flow

```
Cron: 0 8 * * * (8:00 AM UTC daily)
  > /root/scripts/daily-research/ai_ecosystem_research.py
  > Fetches stats from 12 GitHub repositories
  > Fetches trending AI stories from Hacker News
  > Generates markdown content
  > Writes to: /media/docker/website/content/posts/YYYY-MM-DD-news-ai-ecosystem.md
  > Hugo auto-rebuild
  > {Daily research post live}
```

### Components

| Component | Location | Schedule |
|-----------|----------|----------|
| Cron | crontab | 0 8 * * * |
| Script | /root/scripts/daily-research/ai_ecosystem_research.py | - |
| Output | /media/docker/website/content/posts/ | - |

---

## Summary: All Entry Points

| Entry Point | Flow Type | End Result |
|-------------|-----------|------------|
| Homepage URL Widget | YouTube > Queue | Transcript + queue entry |
| Chat YouTube URL | YouTube > Full | Blog post (2 posts) |
| Chat 'summarize' | Summarization | Updated blog posts |
| Homepage Re-Search | Research | Research results |
| Homepage Production | Task Management | Task updates |
| Homepage Admin buttons | Admin Tasks | System changes |
| Homepage Theme dropdown | UI Theme | Theme change |
| Cron daily | Auto Research | Daily blog post |

---

## Component Reference

### Core Services

| Service | Port | Container/Service |
|---------|------|-------------------|
| Homepage | 8765 | homepage (Docker) |
| Relay | 8899 | relay.py (Python) |
| OliveTin | 1337 | olivetin (Docker) |
| Hugo Blog | 1314 | hugo-blog.service (systemd) |
| Research | 8898 | research-task (Docker) |
| Production | 8897 | production-task (Docker) |
| Astro Site | 8086 | astro-fresh (Docker) |

### Key Directories

| Path | Purpose |
|------|---------|
| /media/docker/olivetin/config/scripts/ | Admin scripts |
| /media/docker/commands/ | YouTube processing scripts |
| /media/docker/website/content/posts/ | Hugo blog content |
| ~/.config/opencode/docs/output/ | Transcript & summary output |
| /root/tmp/ | Queue files |
| /var/log/ | System logs |

---

*Last updated: 2026-03-01*
*This document maps all active workflows in the ubuntu4 server environment.*