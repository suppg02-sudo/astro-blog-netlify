---
pubDatetime: 2026-02-08T23:12:40Z
title: "From Agent to Blog Post: The Complete Flow Architecture"
postSlug: "from-agent-to-blog-post-the-complete-flow-architecture"
description: "From Agent to Blog Post: The Complete Flow Architecture"
tags:
  - agent-flow
  - automation
  - protocol
  - architecture
  - workflow
---

## Introduction

This post explains the complete flow that transforms a simple user request (like pasting a YouTube URL) into a published blog post. It documents how agents, protocols, scripts, and skills work together in a coordinated pipeline.

---

## The Complete Flow: Agent > URL > Protocol > Scripts > Skill > Blog Post

### 1. USER PROVIDES URL

**Starting Point**: User pastes a URL

```
USER INPUT:
https://www.youtube.com/watch?v=3GrG-dOmrLU
```

The user simply provides a YouTube link. No additional instructions needed - the system recognizes it automatically.

---

### 2. AGENT RECOGNIZES TRIGGER WORD

**Layer**: Global Instructions / Trigger Word System

The agent's global instructions contain trigger word rules that activate when specific patterns are detected.

```
GLOBAL RULES (global-instructions.md):
├─ YouTube URL trigger word defined
├─ Pattern: "youtube.com/watch", "youtu.be", etc.
└─ Action: Activate youtube-full-workflow protocol
```

**Agent Decision**:
```
IF user input contains YouTube URL
THEN load youtube-full-workflow protocol
```

---

### 3. PROTOCOL IS LOADED

**Layer**: Global Instructions / Protocol Definition

The trigger activates a complete protocol - a documented multi-phase workflow.

```
PROTOCOL: youtube-full-workflow

Phase 1: youtube-extract
  └─ Extract transcript from video
  
Phase 2: youtube-summarize
  └─ Generate summary from transcript
  
Phase 3: youtube-blog
  └─ Create and publish blog post
```

**What the Protocol Defines**:
- Which steps to execute in order
- What tools to use at each step
- Expected outputs and validation gates
- Error handling and recovery
- Memory storage requirements

---

### 4. SCRIPTS ARE EXECUTED

**Layer**: Command Line Tools / Python Scripts

The protocol calls scripts that do the actual work.

```
Phase 1 Script: youtube_transcript_extractor.py
├─ Input: Video URL
├─ Process: 
│   ├─ Fetch video ID
│   ├─ Request transcript via API
│   ├─ Extract metadata (title, author, duration)
│   └─ Save JSON + TXT files
└─ Output: Transcript files with metadata

Phase 2 Script: youtube_transcript_summarizer.py
├─ Input: Transcript JSON
├─ Process:
│   ├─ Extract key points
│   ├─ Identify themes
│   ├─ Generate SEO tags
│   └─ Create executive summary
└─ Output: Summary JSON with insights

Phase 3 Script: hugo-task (NEW!)
├─ Input: Title + content
├─ Process:
│   ├─ Generate frontmatter (YAML)
│   ├─ Create markdown file
│   ├─ Copy to Hugo content directory
│   ├─ Wait for rebuild
│   └─ Validate HTTP 200 response
└─ Output: Published blog post
```

---

### 5. SKILL IS LOADED FOR CONTEXT

**Layer**: Hugo Skill / Domain Knowledge

When the protocol reaches the blog publishing phase, a specialized skill is loaded.

```
SKILL LOADED: Hugo Skill
├─ Location: /root/.config/claude/skill/hugo/SKILL.md
├─ Knowledge About:
│   ├─ Hugo site structure
│   ├─ Post creation methods
│   ├─ Frontmatter requirements
│   ├─ Theme management
│   ├─ Troubleshooting procedures
│   └─ Gateway validation
└─ Provides Context For: Proper blog post creation
```

**Why Load a Skill**?
- Ensures correct post format
- Provides error recovery procedures
- Documents best practices
- Validates against site structure
- Knows about gateway validation requirements

**Skill Discovers**: The `hugo-task` script is available in PATH

```
Hugo Skill checks:
  ✓ Is hugo-task available?
  ✓ Can it create posts?
  ✓ Does it validate HTTP status?
  ✓ Can it handle tags/categories?
```

---

### 6. BLOG POST IS CREATED

**Layer**: Direct File Creation + Hugo Rebuild + Gateway Validation

The skill leverages the hugo-task script to create the post.

```
EXECUTION:
┌─────────────────────────────────────┐
│ 1. hugo-task create "Title"         │
│    ↓                                │
│ 2. Generate YAML frontmatter        │
│    ↓                                │
│ 3. Write to /media/docker/website/  │
│    content/posts/YYYY-MM-DD-slug.md │
│    ↓                                │
│ 4. Wait 3 seconds (Hugo rebuild)    │
│    ↓                                │
│ 5. Verify HTTP 200 response         │
│    ↓                                │
│ 6. Check content rendering          │
│    ↓                                │
│ 7. Report success/failure           │
└─────────────────────────────────────┘

OUTPUT:
✓ Post created: 2026-02-08-title.md
✓ HTTP Status: 200 OK
✓ URL: http://ubuntu58-1:1314/2026/02/08/title/
✓ Post is live and accessible
```

---

## Key Components Explained

### Agent Layer
- **Role**: Recognizes user input and triggers workflows
- **Decision**: When to activate which protocol
- **Knowledge**: Global instructions, trigger words

### Protocol Layer
- **Role**: Defines complete multi-phase workflows
- **Stored In**: `global-instructions.md`
- **Example**: `youtube-full-workflow` protocol
- **Contains**: Phase definitions, tool selections, validation gates

### Script Layer
- **Role**: Execute actual work (extract, summarize, create)
- **Technologies**: Python, Bash, external APIs
- **Output**: Structured data (JSON, files, HTTP responses)

### Skill Layer
- **Role**: Provide domain expertise and context
- **File Format**: Markdown with YAML frontmatter
- **Location**: `/root/.config/claude/skill/[skill-name]/SKILL.md`
- **Purpose**: Best practices, troubleshooting, tool recommendations

### Tool Layer (hugo-task Script)
- **Role**: Direct interaction with system (file creation, validation)
- **Location**: `/usr/local/bin/hugo-task`
- **Capabilities**: Create posts, validate status, generate slugs
- **Gateway Validation**: Confirms success before marking complete

---

## Why This Architecture Works

### 1. **Separation of Concerns**
Each layer has a specific responsibility:
- Agents recognize patterns
- Protocols define workflows
- Scripts do the work
- Skills provide guidance
- Tools interact with the system

### 2. **Reusability**
The same components can be combined in different ways:
```
YouTube URL → youtube-full-workflow → Hugo Skill → Blog Post
GitHub Issue → github-processing-workflow → Ticket Skill → Issue Tracker
Research Query → research-workflow → Research Skill → Report
```

### 3. **Transparency**
Every step is documented and visible:
```
AGENT > PROTOCOL > SCRIPT > SKILL > TOOL > OUTPUT
  ↓       ↓         ↓       ↓       ↓       ↓
Visible Visible   Logging Logged  Logged  Verified
```

### 4. **Fault Tolerance**
If one script fails, fallbacks exist:
```
Primary: hugo-task create
Fallback: Direct file creation
Fallback: Manual post creation
```

### 5. **Extensibility**
New workflows can be added by:
- Adding trigger words to global instructions
- Creating protocol definitions
- Writing new scripts
- Loading appropriate skills
- Testing with new tools

---

## Real-World Example: This Article

This blog post was created using this exact flow:

```
1. USER said: "create me a blog post that explains this flow"
   ↓
2. AGENT recognized: blog post creation request
   ↓
3. PROTOCOL: blog-post-creation-workflow
   ↓
4. SCRIPTS: mcp_bash (file creation), mcp_write (markdown)
   ↓
5. SKILL: Hugo skill loaded for context
   ↓
6. TOOL: hugo-task create "From Agent to Blog Post..." --draft=false
   ↓
7. RESULT: Blog post published
```

---

## Conclusion

The flow from Agent > URL > Protocol > Scripts > Skill > Blog Post represents a **layered, composable architecture** that enables **intelligent automation**.

✅ Recognizes user intent automatically  
✅ Executes complex multi-phase workflows  
✅ Provides domain expertise through skills  
✅ Validates success before completion  
✅ Maintains transparency at every step  

*This post explains the system architecture that made it possible to create itself.*