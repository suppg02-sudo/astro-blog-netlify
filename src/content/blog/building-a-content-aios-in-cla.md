---
pubDatetime: 2026-03-31T23:44:52Z
title: "Building a Content AIOS in Claude Code — From Idea to Published on Every Platform"
postSlug: "building-a-content-aios-in-cla"
description: "Building a Content AIOS in Claude Code — From Idea to Published on Every Platform"
tags:
  - others
---

> **TL;DR**: Wayne Ergle demonstrates his Content Engine AIOS — a content operating system built entirely in Claude Code that plans, writes, publishes, and gets smarter with every session.

## Quick Summary

- Non-developers can build real production systems in Claude Code by describing what they need
- The Content Engine AIOS automates the full content lifecycle: planning, writing, graphics, and publishing across 5+ platforms
- The system self-improves — each session learns from previous ones, making session 100 smarter than session 1

## The Problem: Content Creation Is a Never-Ending Loop

Every content creator knows the cycle: brainstorm ideas, write posts, reformat for each platform, create images, schedule everything — then start over. Wayne Ergle built a system to break this loop entirely using Claude Code as the orchestrating brain.

## What Is Content Engine AIOS?

Content Engine AIOS is a full content operating system built inside Claude Code (running in VS Code). It's not a traditional application with a codebase — it's a collection of documents, skills, and profiles that Claude reads and acts upon. The entire system lives in a single folder on the creator's computer with no traditional code files.

The architecture follows a hub-and-spoke model with Claude sitting at the center, orchestrating multiple services:

- **Airtable** — Primary interface for content management, planning, and review
- **WordPress** — CMS for blog posts and pillar pages
- **Bluair (Blateo)** — Social media scheduling and publishing
- **Google Drive** — Image storage
- **Data** — SEO keyword research

## How It Works: The Full Workflow

### Step 1: Content Planning

You give Claude a topic — in this demo, "non-developers building real systems in Claude Code." Claude researches your brand documents, then creates a comprehensive content plan that spans all your marketing platforms: pillar pages for your website, cluster articles, Twitter/X posts (with types like observations and threads), LinkedIn stories, YouTube scripts, and TikTok content.

### Step 2: Content Creation

Inside Airtable, you set the status of content pieces to "Write." Claude detects these, writes the content, and updates Airtable automatically. This includes:

- Twitter/X posts with hooks and full text
- LinkedIn stories with narrative structure
- Blog posts and pillar pages (3,000-5,000 words)
- Supporting articles for hub-and-spoke SEO architecture

### Step 3: Visual Assets

Claude generates graphics to accompany the written content. These are stored and associated with the relevant posts in Airtable.

### Step 4: Review and Approval

The Airtable interface provides a clear review workflow with statuses: Draft → In Progress → In Review → Needs Revision → Approved → Scheduled → Published → Delete. You review the content, add notes if needed, and mark pieces as Approved.

### Step 5: Publishing

Using a slash command (`/publish`), Claude pushes approved content to Bluair for social media scheduling. Content goes live on LinkedIn, Twitter/X, and other platforms — with URLs and publish confirmations tracked in Airtable.

## The Pillar Page Strategy

A standout feature is the hub-and-spoke content architecture. Claude creates 3,000-5,000 word pillar pages with table of contents, structured headings, tables, and formatting optimized for AI search platforms. Supporting articles link back to the pillar page, signaling authority to Google and other search engines.

## Self-Improving System: The Compound Effect

Perhaps the most impressive feature is that the system gets smarter with every session. Claude documents what goes right and wrong during each session, then implements improvements at session end. After 29 sessions, session 30 has the benefit of all previous learning. After 100 sessions, 99 contribute to making the system better.

This self-improvement extends to context window management — the system is designed to use the context window efficiently, preventing the common problem of AI losing track of earlier conversation.

## How to Get Content Engine AIOS

Wayne offers three paths:

1. **Build it yourself** — Follow his upcoming video series and documentation
2. **Join the Stack Engine community** — Access all systems and workflows as a member
3. **Jump Start service** — Wayne sets up the system for you, including a live content sprint that can produce 2-4 weeks of content in one session

## Key Takeaway

The demo proves a powerful point: non-developers — content marketers, SEO specialists, business operators — can build real production systems in Claude Code. They're not writing code. They're describing what they need, and Claude Code builds it. The bottleneck was never code — it was knowing what to ask for.

<details>
<summary>Video Details & Source</summary>

- **Video**: [From Idea to Published on Every Platform — One Folder AIOS in Claude Code](https://www.youtube.com/watch?v=MLv9EdhnOXM)
- **Channel**: [Wayne Ergle](https://www.youtube.com/@wayneergle)
- **Tools mentioned**: Claude Code, VS Code, Airtable, WordPress, Bluair/Blateo, Google Drive
- **Concept**: AIOS (AI Operating System) for content marketing automation

</details>

**Tags**: claude-code, ai-content, content-marketing, ai-automation, airtable
**Categories**: AI Automation, Content Marketing