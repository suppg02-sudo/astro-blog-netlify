---
pubDatetime: 2026-02-28T15:30:00Z
title: "Environment Components Workflow"
postSlug: "environment-components-workflow"
description: "Environment Components Workflow"
tags:
  - automation
  - components
  - architecture
  - workflow
---

A visual guide to how the key environment components connect: Research, Summarization, Question Tool, Menu & Skill History, Decision Tracking, Cron Jobs, and Blog Publishing.

## High Level Layers

```mermaid
flowchart TB
    OUTPUT["📤 Presentation / Output Layer"]
    TRACKING["📊 Tracking Layer"]
    PROCESSING["⚙️ Processing Layer"]
    MEMORY["🧠 Memory Layer"]
    CONTEXT["📚 Context Layer"]
    INPUT["📥 Input Layer"]
    SCHEDULING["⏰ Scheduling Layer"]
    
    SCHEDULING --> INPUT
    INPUT --> CONTEXT
    CONTEXT --> MEMORY
    MEMORY --> PROCESSING
    PROCESSING --> TRACKING
    TRACKING --> OUTPUT
    
    style OUTPUT fill:#10b981,stroke:#fff,color:#fff
    style TRACKING fill:#8b5cf6,stroke:#fff,color:#fff
    style PROCESSING fill:#f97316,stroke:#fff,color:#fff
    style MEMORY fill:#ec4899,stroke:#fff,color:#fff
    style CONTEXT fill:#1e3a5f,stroke:#fff,color:#fff
    style INPUT fill:#3b82f6,stroke:#fff,color:#fff
    style SCHEDULING fill:#64748b,stroke:#fff,color:#fff
```

---


## Component Overview

```mermaid
flowchart TB
    subgraph CONTEXT["📚 Context Layer"]
        direction LR
        Roadmap["🗺️ Roadmap"]
        Telos["📜 TELOS"]
        Registry["📋 Registries"]
        Domain["🎯 Domain"]
        VectorDB["🕸️ Vector/Graph DB"]
    end

    subgraph MEMORY["🧠 Memory Layer"]
        direction LR
        OpenMem["OpenMemory"]
        ContextReg["Context Registry"]
    end

    subgraph SCHEDULING["⏰ Scheduling Layer"]
        direction LR
        Cron["Cron Jobs"]
    end

    subgraph INPUT["📥 Input Layer"]
        direction LR
        URL["URLs"]
        User["User"]
    end

    subgraph PROCESSING["⚙️ Processing Layer"]
        direction LR
        Research["Research"]
        Summarize["Summarize"]
    end

    Question["❓ Question Tool<br/><small>(Cross-Cutting)</small>"]

    subgraph TRACKING["📊 Tracking Layer"]
        direction LR
        Menu["Menu History"]
        Skills["Skill Usage"]
        Decisions["Decisions"]
    end

    subgraph OUTPUT["📤 Output Layer"]
        direction LR
        Hugo["Hugo Blog"]
        Astro["Astro Site"]
    end

    %% Top layer connections (Context + Memory)
    CONTEXT -.->|"provides context"| PROCESSING
    MEMORY -.->|"retrieves patterns"| PROCESSING
    MEMORY -.->|"provides history"| TRACKING
    
    %% Vertical flow
    SCHEDULING -.->|"triggers"| PROCESSING
    SCHEDULING -.->|"triggers"| TRACKING
    
    INPUT --> PROCESSING
    PROCESSING --> TRACKING
    TRACKING --> OUTPUT
    
    %% Store back to memory
    OUTPUT --> MEMORY
    TRACKING --> MEMORY
    
    User -.-> Question
    Question -.-> PROCESSING
    Question -.-> Decisions

    style CONTEXT fill:#1e3a5f,stroke:#fff,color:#fff
    style MEMORY fill:#ec4899,stroke:#fff,color:#fff
    style SCHEDULING fill:#64748b,stroke:#fff,color:#fff
    style INPUT fill:#3b82f6,stroke:#fff,color:#fff
    style PROCESSING fill:#f97316,stroke:#fff,color:#fff
    style TRACKING fill:#8b5cf6,stroke:#fff,color:#fff
    style OUTPUT fill:#10b981,stroke:#fff,color:#fff
    style Question fill:#dc2626,stroke:#fff,stroke-dasharray: 5 5,color:#fff
```

---

## 1. Research Workflow

The Research skill gathers information from multiple sources, synthesizes findings, and publishes to the blog.

```mermaid
flowchart TB
    subgraph SOURCES["🌐 Information Sources"]
        Web["🌐 Web Search<br/>(Brave/Exa)"]
        Docs["📚 Context7<br/>Official Docs"]
        GitHub["🐙 GitHub<br/>Code Examples"]
        Academic["🎓 Academic<br/>Papers"]
    end

    subgraph GATHER["📥 Parallel Gathering"]
        Gather["Multi-Source<br/>Collection"]
    end

    subgraph VERIFY["✅ Verification"]
        Cred["CRAAP<br/>Evaluation"]
        Cross["Cross-Reference<br/>Check"]
        Conflict["Conflict<br/>Resolution"]
    end

    subgraph SYNTHESIZE["🧠 Synthesis"]
        Synth["Evidence-Based<br/>Synthesis"]
        Conf["Confidence<br/>Assessment"]
    end

    subgraph OUTPUT["📤 Output"]
        Report["📄 Research<br/>Report"]
        Blog["📝 Hugo<br/>Blog Post"]
        Memory["🧠 OpenMemory<br/>Storage"]
    end

    Web --> Gather
    Docs --> Gather
    GitHub --> Gather
    Academic --> Gather
    
    Gather --> Cred
    Cred --> Cross
    Cross --> Conflict
    Conflict --> Synth
    Synth --> Conf
    
    Conf --> Report
    Report --> Blog
    Report --> Memory

    style Gather fill:#3b82f6,stroke:#fff,color:#fff
    style Synth fill:#f97316,stroke:#fff,color:#fff
    style Blog fill:#ff4081,stroke:#fff,color:#fff
```

### Research Tools

| Tool | Purpose | Status |
|------|---------|--------|
| **Brave Search** | Real-time web search | ✅ MCP Connected |
| **Context7** | Official documentation | ✅ MCP Connected |
| **GitHub Search** | Code examples | ✅ Available |
| **Crawl4AI** | Web scraping | ✅ MCP Connected |

### Research Implementation

**Skill Location:** `~/.config/opencode/skills/research/SKILL.md`

**Web Form Interface:** http://ubuntu4:8898

| Feature | Description |
|---------|-------------|
| Static Dropdowns | Intensity, thinking, format options |
| Topic Input | Text field with optional context |
| Source Selection | Web, Docs, GitHub, Academic, News |
| Cron Scheduling | Now, Hourly, Daily, Weekly, Monthly |
| Auto Publishing | Creates Hugo blog post |

**Scheduled Research Tasks:**

```bash
# Cron jobs configured
0 8 * * *   daily-ai-news        # Daily AI ecosystem
0 8 * * 1   weekly-ecosystem     # Monday ecosystem review
0 9 * * 2   weekly-rag-developments  # Tuesday RAG news
0 8 1 * *   monthly-agent-tools  # Monthly agent tools
```

**Key Scripts:**

| Script | Location | Purpose |
|--------|----------|--------|
| Daily Research | `~/scripts/daily-research/ai_ecosystem_research.py` | Fetches 12 repos + HN stories |
| Research Engine | `/media/docker/research-task/research_engine.py` | Core research execution |
| Scheduled Runner | `/media/docker/research-task/scripts/run-scheduled-research.sh` | Cron task runner |
| OliveTin Executor | `/media/docker/olivetin/config/scripts/execute-research.sh` | Manual task execution |

---

## 2. Summarization Flow

URLs and content are summarized for quick consumption and storage.

```mermaid
flowchart LR
    subgraph INPUT["📥 Input"]
        URL["URL/Link"]
        Content["Long Content"]
        Video["Video/Media"]
    end

    subgraph EXTRACT["⚙️ Extraction"]
        Crawl["Crawl4AI<br/>Scraping"]
        Transcribe["Transcription<br/>(if needed)"]
    end

    subgraph PROCESS["🧠 Processing"]
        AI["AI Summarization<br/>(GLM-5)"]
        Structure["Structure<br/>Extraction"]
    end

    subgraph OUTPUT["📤 Output"]
        Summary["📝 Summary"]
        Blog["Blog Post"]
        Tags["Auto-Tags"]
    end

    URL --> Crawl
    Content --> AI
    Video --> Transcribe
    
    Crawl --> AI
    Transcribe --> AI
    AI --> Structure
    
    Structure --> Summary
    Summary --> Blog
    Structure --> Tags
    style Summary fill:#10b981,stroke:#fff,color:#fff
```

### Summarize Tool Implementation

**Tool:** `@steipete/summarize` (v0.11.1)

**Installation:**
```bash
npm i -g @steipete/summarize@latest
```

**Binary Location:** `/root/.npm-global/bin/summarize`

**Configuration:** `~/.summarize/config.json`

```json
{
  "env": {
    "OPENROUTER_API_KEY": "sk-or-v1-..."
  },
  "model": "free",
  "models": {
    "free": {
      "candidates": [
        "openrouter/arcee-ai/trinity-large-preview:free"
      ]
    }
  }
}
```

**Usage Examples:**

```bash
# Summarize a webpage
summarize "https://example.com"

# Summarize YouTube video (with transcript)
summarize "https://youtube.com/watch?v=..."

# Summarize PDF (remote or local)
summarize "https://arxiv.org/pdf/....pdf"
summarize "/path/to/local.pdf"

# Summarize podcast/audio
summarize "https://feeds.npr.org/500005/podcast.xml"
summarize "/path/to/audio.mp3"

# Extract slides from video
summarize --slides "https://youtube.com/watch?v=..."
```

**Features:**

| Feature | Description |
|---------|-------------|
| Web Scraping | Automatic content extraction |
| YouTube Transcripts | Auto or manual captions |
| Audio Transcription | Whisper, Parakeet, Canary backends |
| PDF Processing | Remote URLs or local files |
| Slide Extraction | Key frames from videos |
| Podcast Support | RSS feeds and audio files |
| Caching | SQLite cache for repeated URLs |

**Output Format:**
```
## Overview
[Summary content]

## Key Points
[Bullet points]

[time] · [duration] · [word count] words · [model] · [tokens]
```

---
## 3. Question Tool & Decision Tracking

The Question Tool presents options and tracks all decisions for learning.

```mermaid
flowchart TB
    subgraph TRIGGER["🎯 Trigger"]
        Task["Task Context"]
        State["Session State"]
        User["User Input"]
    end

    subgraph DETECT["🔍 State Detection"]
        Active{"Active<br/>Task?"}
        Error{"Errors<br/>Present?"}
        Setup{"Post-Setup<br/>Mode?"}
    end

    subgraph CONTEXT["📋 Context Loading"]
        Debug["debug-context"]
        Workflow["workflow-context"]
        Migration["migration-context"]
    end

    subgraph QUESTION["❓ Question Presentation"]
        Options["Menu Options<br/>(Recommended, Alt1, Alt2, Exit)"]
    end

    subgraph TRACKING["📊 Decision Tracking"]
        Record["Record Choice<br/>+ Timestamp"]
        Category["Categorize<br/>(debug/workflow/setup)"]
        Pattern["Pattern<br/>Extraction"]
    end

    subgraph STORAGE["💾 Storage"]
        JSON["questions.json<br/>(Fast Local)"]
        Super["Supermemory<br/>(Persistent)"]
        OM["OpenMemory<br/>(Semantic)"]
    end

    Task --> Active
    Active -->|Yes| Workflow
    Active -->|No| Error
    Error -->|Yes| Debug
    Error -->|No| Setup
    Setup -->|Yes| Migration
    
    Workflow --> Options
    Debug --> Options
    Migration --> Options
    
    User --> Options
    Options --> Record
    Record --> Category
    Category --> Pattern
    
    Pattern --> JSON
    JSON --> Super
    Super --> OM

    style Options fill:#8b5cf6,stroke:#fff,color:#fff
    style Record fill:#f97316,stroke:#fff,color:#fff
    style JSON fill:#3b82f6,stroke:#fff,color:#fff
```

### Decision Categories

| Category | Trigger Patterns | Example |
|----------|-----------------|---------|
| `debug` | error, failed, fix | "I'm seeing error X" |
| `workflow` | feature, implement, refactor | "Add authentication" |
| `setup` | install, configure, setup | "Set up Docker" |
| `skill_selection` | skill names present | "Use hugo skill" |
| `confirmation` | confirm, proceed, yes/no | "Should I continue?" |
| `navigation` | menu, back, next, view | "Show me options" |

---

## 4. Menu & Skill History (Context Registry)

The Context Registry tracks all interactions with progressive disclosure.

```mermaid
flowchart TB
    subgraph EVENTS["🎯 Events"]
        Q["Question<br/>Asked"]
        S["Skill<br/>Invoked"]
        C["Choice<br/>Made"]
    end

    subgraph LAYERS["📚 Three-Tier Storage"]
        L1["Layer 1: JSON Registry<br/>Fast, Local, Recent"]
        L2["Layer 2: Supermemory<br/>Persistent, Searchable"]
        L3["Layer 3: OpenMemory<br/>Semantic, Vector-Based"]
    end

    subgraph DISCLOSURE["📖 Progressive Disclosure"]
        D0["Level 0: Capability<br/>~2KB (Always Loaded)"]
        D1["Level 1: Metadata<br/>~500B (On Trigger)"]
        D2["Level 2: Working Context<br/>2-10KB (On Execute)"]
        D3["Level 3: Reference Files<br/>On Demand"]
    end

    subgraph QUERIES["🔍 Query Interface"]
        Search["Search by<br/>Category/Skill/Time/Tag"]
        Stats["Usage Statistics<br/>& Analytics"]
        Export["Export to<br/>JSON/CSV"]
    end

    Q --> L1
    S --> L1
    C --> L1
    
    L1 -->|"Sync"| L2
    L2 -->|"Extract"| L3
    
    L1 --> D0
    D0 -->|"Need More"| D1
    D1 -->|"Executing"| D2
    D2 -->|"Reference"| D3
    
    L3 --> Search
    Search --> Stats
    Stats --> Export

    style L1 fill:#3b82f6,stroke:#fff,color:#fff
    style L2 fill:#8b5cf6,stroke:#fff,color:#fff
    style L3 fill:#f97316,stroke:#fff,color:#fff
    style D0 fill:#10b981,stroke:#fff,color:#fff
```

### Storage Locations

```
~/.config/opencode/context-registry/
├── data/
│   ├── questions.json      # Question history
│   ├── skills.json         # Skill usage
│   ├── context-index.json  # Disclosure index
│   └── analytics.json      # Aggregated stats
```

---

## 5. Cron Jobs & Scheduled Tasks

Automated tasks run on schedules to keep the environment updated.

```mermaid
flowchart TB
    subgraph SCHEDULE["⏰ Schedule Triggers"]
        Hourly["Hourly<br/>*:00"]
        Daily["Daily<br/>8:00 AM"]
        Weekly["Weekly<br/>Mon/Tue"]
        Monthly["Monthly<br/>1st"]
    end

    subgraph TASKS["📋 Scheduled Tasks"]
        T1["Resource Trend<br/>Logger"]
        T2["Roundup Report<br/>System Health"]
        T3["Daily AI News<br/>Research"]
        T4["Weekly Ecosystem<br/>Research"]
        T5["Weekly RAG<br/>Developments"]
        T6["Monthly Agent<br/>Tools"]
    end

    subgraph EXECUTION["⚙️ Execution"]
        Script["Shell/Python<br/>Scripts"]
        Research["Research<br/>Skill"]
        Report["Report<br/>Generation"]
    end

    subgraph OUTPUT["📤 Output"]
        Logs["📄 Log Files"]
        Blog["📝 Hugo Blog<br/>Posts"]
        Metrics["📊 Metrics<br/>& Stats"]
    end

    Hourly --> T1
    Daily --> T2
    Daily --> T3
    Weekly --> T4
    Weekly --> T5
    Monthly --> T6
    
    T1 --> Script
    T2 --> Script
    T3 --> Research
    T4 --> Research
    T5 --> Research
    T6 --> Research
    
    Script --> Logs
    Research --> Blog
    Script --> Metrics

    style Daily fill:#f97316,stroke:#fff,color:#fff
    style Weekly fill:#3b82f6,stroke:#fff,color:#fff
    style Research fill:#8b5cf6,stroke:#fff,color:#fff
    style Blog fill:#ff4081,stroke:#fff,color:#fff
```

### Active Cron Schedule

| Schedule | Task | Output |
|----------|------|--------|
| Hourly | Resource Trend Logger | `/var/log/resource-trends.log` |
| Daily 3AM | Roundup Report | `/root/cron-logs/roundup-cron.log` |
| Daily 8AM | Daily AI News | Hugo blog post |
| Weekly Mon 8AM | Ecosystem Research | Hugo blog post |
| Weekly Tue 9AM | RAG Developments | Hugo blog post |
| Monthly 1st 8AM | Agent Tools Review | Hugo blog post |

---

## 6. Blog Publishing (Hugo & Astro)

Content flows from research and summarization to dual blog platforms.

```mermaid
flowchart TB
    subgraph CONTENT["📝 Content Sources"]
        Research["Research<br/>Results"]
        Summary["Summaries"]
        YouTube["YouTube<br/>Transcripts"]
        Manual["Manual<br/>Posts"]
    end

    subgraph PROCESSING["⚙️ Processing"]
        Template["Apply<br/>Template"]
        Frontmatter["Add<br/>Frontmatter"]
        Validate["Validate &<br/>Preview"]
    end

    subgraph PRIMARY["🎯 Primary: Hugo"]
        HugoDir["/media/docker/website/<br/>content/posts/"]
        HugoBuild["Hugo Build<br/>(Auto-rebuild)"]
        HugoSite["Hugo Site<br/>:1313"]
    end

    subgraph BACKUP["🔄 Backup: Astro"]
        AstroDir["/media/docker/astro-fresh/<br/>src/content/blog/"]
        AstroBuild["Astro Build"]
        AstroSite["Astro Site<br/>:8086"]
    end

    subgraph MEMORY["🧠 Memory Storage"]
        OpenMem["OpenMemory<br/>Semantic"]
        Super["Supermemory<br/>Persistent"]
    end

    Research --> Template
    Summary --> Template
    YouTube --> Template
    Manual --> Template
    
    Template --> Frontmatter
    Frontmatter --> Validate
    
    Validate --> HugoDir
    HugoDir --> HugoBuild
    HugoBuild --> HugoSite
    
    Validate -.->|"Optional"| AstroDir
    AstroDir --> AstroBuild
    AstroBuild --> AstroSite
    
    HugoSite --> OpenMem
    HugoSite --> Super

    style HugoSite fill:#ff4081,stroke:#fff,color:#fff
    style AstroSite fill:#ff5d01,stroke:#fff,color:#fff
    style OpenMem fill:#f97316,stroke:#fff,color:#fff
```

### Blog Platforms

| Platform | Port | Purpose | Posts Directory |
|----------|------|---------|-----------------|
| **Hugo** | :1313 | Primary blog, TELOS Blog | `/media/docker/website/content/posts/` |
| **Astro** | :8086 | Backup site, Astro Fresh | `/media/docker/astro-fresh/src/content/blog/` |

---

## Complete Integration Flow

How all components work together in a typical workflow:

```mermaid
flowchart TB
    subgraph MORNING["🌅 Morning Routine"]
        Cron["Cron: 8AM<br/>Trigger"]
        Research["Research Skill<br/>Gathers AI News"]
        Synth["Synthesize<br/>Findings"]
        Post1["Auto-Create<br/>Blog Post"]
    end

    subgraph INTERACTIVE["💬 Interactive Work"]
        User["User<br/>Request"]
        Question["Question Tool<br/>Presents Options"]
        Choice["User Makes<br/>Choice"]
        Track["Context Registry<br/>Records Decision"]
        Execute["Execute<br/>Selected Action"]
    end

    subgraph PUBLISH["📤 Publishing"]
        Hugo["Hugo<br/>Rebuilds"]
        Memory["Store in<br/>OpenMemory"]
        Analytics["Update<br/>Analytics"]
    end

    Cron --> Research
    Research --> Synth
    Synth --> Post1
    
    User --> Question
    Question --> Choice
    Choice --> Track
    Track --> Execute
    
    Post1 --> Hugo
    Execute --> Hugo
    Hugo --> Memory
    Memory --> Analytics

    style Research fill:#f97316,stroke:#fff,color:#fff
    style Question fill:#8b5cf6,stroke:#fff,color:#fff
    style Hugo fill:#ff4081,stroke:#fff,color:#fff
    style Memory fill:#10b981,stroke:#fff,color:#fff
```

---

## Quick Reference

| Component | Trigger | Output | Storage |
|-----------|---------|--------|---------|
| **Research Skill** | `research` / Web Form (:8898) | Blog post | OpenMemory |
| **Summarize Tool** | `summarize "URL"` | Summary + metadata | SQLite cache |
| **Question Tool** | `q` / auto-detect | Menu options | questions.json |
| **Context Registry** | `cr` | History query | 3-tier storage |
| **Cron Jobs** | Schedule (4 tasks) | Reports + posts | Logs + blog |
| **Hugo Blog** | File write | Published page | /media/docker/website |
| **Astro Blog** | Manual | Published page | /media/docker/astro-fresh |

## Tool Quick Commands

```bash
# Research
python3 ~/scripts/daily-research/ai_ecosystem_research.py  # Run daily research
open http://ubuntu4:8898  # Open research web form

# Summarize
summarize "https://example.com"           # Summarize webpage
summarize "https://youtube.com/watch?v=..."  # Summarize video
summarize --slides "https://youtube.com/..."  # Extract slides

# Check status
curl -s http://localhost:8898/health     # Research form health
docker ps | grep research                # Research container
ls /media/docs/research/                 # Research outputs
```

---

*Last updated: February 28, 2026*