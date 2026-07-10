---
pubDatetime: 2026-07-10T00:30:00Z
title: "Building a Self-Maintaining Knowledge Wiki That an AI Agent Actually Keeps Updated"
postSlug: "agent-wiki-self-maintaining-knowledge-system"
description: "A deep dive into a personal knowledge wiki that uses an inbox-audit-publish pipeline to let an AI agent capture, curate, and publish knowledge autonomously — without garbage data. Covers architecture, the 14 MCP tools, failure modes, and concrete improvements."
tags:
  - AI
  - knowledge-management
  - agents
  - wiki
  - MCP
  - opencode
  - LLM
---

# Building a Self-Maintaining Knowledge Wiki That an AI Agent Actually Keeps Updated

> **TL;DR**: Most "AI knowledge bases" are landfills — the agent dumps everything in, nothing gets curated, and the signal-to-noise ratio collapses within a week. Here's a working alternative: an inbox-audit-publish pipeline where the AI submits knowledge to a queue, a review step filters quality, and only vetted content reaches the published wiki. Built on flat Markdown files, 14 MCP tools, and zero databases.

## The Problem with AI-Managed Knowledge

Every developer who's used an AI agent for more than a week hits the same wall: **the agent learns things, then immediately forgets them**. You spend 40 minutes debugging a LiteLLM configuration issue, the agent helps you fix it, and next session — blank slate. The knowledge is gone.

The obvious solution is a knowledge base. But here's what happens when you give an AI agent write access to a wiki:

1. **Day 1**: Agent adds a useful page about a bug fix
2. **Day 3**: Agent starts adding "session summaries" that are just verbose transcripts
3. **Day 7**: The wiki is 80% noise, 20% signal, and you've stopped trusting it
4. **Day 14**: You abandon the wiki entirely

The failure mode is always the same: **uncontrolled write access degrades quality to zero**. It's the tragedy of the commons applied to a personal knowledge base.

## The Architecture: Inbox → Audit → Publish

The fix is a pipeline borrowed from editorial publishing:

```
Chat conversation / analysis / research
         │
         ▼
    ┌─────────────┐
    │   INBOX     │  ← Raw submission, unstructured
    │  (queue)    │
    └──────┬──────┘
           │
           ▼
    ┌─────────────┐
    │   AUDIT     │  ← Classify, critique, route
    │   LOOP      │
    └──────┬──────┘
           │
     ┌─────┴─────┐
     ▼           ▼
  APPROVE      REJECT
     │
     ▼
  ┌─────────────────┐
  │  PUBLISHED WIKI  │  ← Category directories, frontmatter, cross-links
  │  /root/wiki/     │
  └─────────────────┘
```

Every piece of knowledge goes through this pipeline. The agent can **submit** freely — low friction, no gatekeeping at the point of capture. But nothing reaches the published wiki without going through review and approval.

This is the core insight: **separate the capture step from the publish step**, with an audit loop in between.

## How It Actually Works

### 1. The Wiki Structure

The wiki lives at `/root/wiki/` as flat Markdown files — no database, no CMS, no external service. Categories are just directories:

```
/root/wiki/
├── README.md          # Overview
├── SCHEMA.md          # Conventions and frontmatter spec
├── index.md           # Content catalogue
├── log.md             # Append-only action log
├── inbox/             # Pending submissions (queue)
├── domain/            # Domain knowledge, stack analyses
├── system/            # System improvements, session logs
├── entities/          # Entity definitions, key concepts
├── improvements/      # Improvement proposals
├── projects/          # Project-specific knowledge
├── answers/           # Q&A snapshots
└── templates/         # Reusable page templates
```

Every page has YAML frontmatter:

```yaml
---
title: Next AI Draw.io Stack Analysis
created: 2026-07-10
updated: 2026-07-10
type: domain
tags: [stack-analysis, drawio, ai-sdk]
confidence: high
---
```

Pages cross-link using `[[wikilinks]]`, and every page is supposed to link to at least two others. This creates a graph of connected knowledge rather than isolated documents.

### 2. The Submission Flow

When the agent produces something worth keeping — a stack analysis, a bug fix, a research summary — it calls `wiki_submit`:

```
Agent: "I just analyzed the Next AI Draw.io application stack"
  → structures the content with frontmatter
  → wiki_submit(content=structured_markdown, source="chat-analysis")
  → returns inbox_id
```

At this point, the content is in the inbox but **not published**. It's pending review.

### 3. The Audit Loop

The audit loop is the quality gate. When triggered, it:

1. Pulls pending items from the inbox
2. **Classifies** each item — what type of content is this? Where does it belong?
3. **Critiques** each item — is this worth keeping? Is it a duplicate? Is the quality sufficient?
4. Returns a routing decision: approve (with target slug and category) or reject (with reason)

The classification uses semantic understanding, not keyword matching. A submission about "LiteLLM model benchmarks" gets classified as `system/` because it's operational infrastructure knowledge. A submission about "Harness-Aware Self-Evolving agentic RL" gets classified as `domain/` because it's domain research.

### 4. The 14 MCP Tools

The entire wiki is managed through MCP (Model Context Protocol) tools. Here's the full toolkit:

**Reading (no approval needed):**

| Tool | Purpose |
|------|---------|
| `wiki_status()` | Page counts, inbox depth, health summary |
| `wiki_index()` | Full catalogue of all pages |
| `wiki_search(query, limit)` | Semantic + full-text search across all pages |
| `wiki_read(slug)` | Read a page by its slug |
| `wiki_backlinks(slug)` | Find all pages that reference a given page |
| `wiki_recent(days)` | Pages updated in the last N days |

**Writing (goes through inbox):**

| Tool | Purpose |
|------|---------|
| `wiki_submit(content, source, metadata)` | Submit content to the inbox queue |
| `wiki_inbox_list(status)` | List inbox items (pending, approved, rejected) |
| `wiki_inbox_review(inbox_id)` | Full details of a specific inbox item |
| `wiki_inbox_approve(inbox_id, edits)` | Approve and write to the wiki |
| `wiki_inbox_reject(inbox_id, reason)` | Reject with documented reason |

**Maintenance:**

| Tool | Purpose |
|------|---------|
| `wiki_audit_process(limit)` | Run the audit loop on pending items |
| `wiki_lint(fix)` | Health checks — broken links, missing frontmatter, stale index |
| `wiki_compile_system()` | Compile evolution artefacts into system pages |

The separation matters: **reading tools are free** (any agent can query the wiki at any time), but **writing tools always go through the inbox**. There's no `wiki_write_directly()` tool. The pipeline is enforced at the API level.

### 5. A Real Example

Here's what happened in a recent session:

1. **User asks**: "Check the stack of my Next AI Draw.io software"
2. **Agent investigates**: Docker inspect, package.json, source code analysis, compares with LibreChat
3. **Agent produces analysis**: Full stack breakdown — Next.js 16, Vercel AI SDK 6.0, 20+ providers, React 19, Electron desktop apps
4. **User says**: "Put it in the wiki"
5. **Agent submits**: Structures content with frontmatter, calls `wiki_submit()`
6. **User approves**: Agent calls `wiki_inbox_approve()`
7. **Published**: Content lands at `/root/wiki/domain/next-ai-draw-io-stack-analysis.md`

Total time: about 30 seconds from "put it in the wiki" to published page. The friction is low enough that it actually happens, but the quality gate exists.

## What's Actually In the Wiki (After 6 Weeks)

After running this system for about six weeks, the wiki has **29 published pages** across 6 categories:

| Category | Pages | Content Examples |
|----------|-------|------------------|
| `system/` | 14 | LiteLLM capability matrix, config tuning, memory audit, session logs, patterns, anti-patterns |
| `domain/` | 7 | Draw.io stack analysis, RAG research, YouTube pipeline fixes, HAZ research, control plane patterns |
| `improvements/` | 3 | Improvement proposals and logs |
| `projects/` | 2 | Project dashboard completion records |
| `entities/` | 1 | Key entity definitions |
| `answers/` | 1 | Consultation snapshots |

The content quality is high because of the audit gate. The system logs capture operational fixes (container OOM tuning, LiteLLM config changes). The domain pages capture research findings (agentic RL papers, agent harness safety analysis). This is knowledge that would have been lost without the wiki.

## Issues I've Found

After auditing the system, here are the concrete problems:

### Issue 1: The Index is Severely Stale

The `index.md` file — the content catalogue — lists only **4 pages**. The wiki has **29**. It was created on day one and never updated. The audit loop doesn't update the index when it publishes new pages.

**Impact**: Browsing the wiki by index shows almost nothing. Search still works, but the catalogue is useless.

**Fix needed**: `wiki_inbox_approve` should automatically update `index.md` with the new page's title and category.

### Issue 2: 59 Orphaned Inbox Files

While there are only 5 *pending* items in the inbox, the inbox directory contains **59 files** total — including processed (approved/rejected) items that were never cleaned up. The inbox is functioning as an append-only log instead of a queue.

**Impact**: `status.sh` reports misleadingly high inbox counts. Storage grows unbounded.

**Fix needed**: Processed items should be archived or purged after a retention period (e.g., 30 days).

### Issue 3: Categories Are Underutilized

Of the 7 category directories, only 2 are in active use (`system/` and `domain/` hold 21 of 29 pages). The `entities/`, `answers/`, and `templates/` directories have 1 page each. The schema defines these categories but the audit loop doesn't route to them well.

**Impact**: Knowledge that should be in `entities/` (e.g., "What is LiteLLM?") ends up in `system/` instead. Categorical browsing is weak.

**Fix needed**: Better classification prompts in the audit loop, or merge underused categories.

### Issue 4: No Automatic Cross-Linking

The schema says "each page links to at least 2 others" but this is entirely manual. The agent adds `[[wikilinks]]` when it remembers to, but many pages have zero outbound links. There's no validation at publish time.

**Impact**: The wiki is a collection of documents, not a connected graph. You can't navigate by links — you have to search.

**Fix needed**: `wiki_lint` should flag pages with fewer than 2 cross-links, and the approval step should suggest relevant pages to link to.

### Issue 5: No Versioning or Diff History

When a page is updated (re-approved with edits), the old content is overwritten. There's no git history because the wiki directory isn't a git repo. If the agent publishes something wrong and it overwrites a good page, the good content is gone.

**Impact**: Permanent data loss on bad edits. No way to see what changed over time.

**Fix needed**: Init `/root/wiki/` as a git repo with automatic commits on every approval.

### Issue 6: No Deduplication

The audit loop doesn't check whether similar content already exists. If the agent submits a page about "LiteLLM configuration" and there's already a page called "LiteLLM config tuning applied," both get published as separate pages.

**Impact**: Knowledge fragments across multiple pages about the same topic. The wiki grows without consolidating.

**Fix needed**: The audit loop should use `wiki_search` on the submitted content's title/tags before approving, and flag potential duplicates for merging.

## Suggested Improvements

### Improvement 1: Auto-Update the Index

The highest-impact fix. When `wiki_inbox_approve` writes a page, it should also append an entry to `index.md` under the appropriate category heading. One line:

```markdown
- [[page-slug]] — Brief description from frontmatter
```

This would make the index useful again with zero ongoing maintenance.

### Improvement 2: Git-Backed Versioning

Initialize the wiki as a git repository:

```bash
cd /root/wiki && git init
```

Then every `wiki_inbox_approve` call does:

```bash
git add -A && git commit -m "wiki: publish {slug}"
```

This gives full diff history, revert capability, and the ability to sync to a remote for backup. The flat-file architecture makes this trivial — no database export needed.

### Improvement 3: Smart Deduplication in Audit

Before approving, the audit loop should:

1. Extract the title and tags from the submission
2. Run `wiki_search(title)` to find similar pages
3. If similarity is high, suggest a **merge** instead of creating a new page
4. Present the merge candidate to the user with a diff preview

This would prevent knowledge fragmentation and keep the wiki dense rather than sprawling.

### Improvement 4: Automatic Cross-Link Suggestions

When publishing a new page, the system should:

1. Extract key terms from the content
2. Search the wiki for pages matching those terms
3. Suggest `[[wikilinks]]` to add at the bottom
4. Optionally, add backlinks from the matched pages to the new page

This turns the wiki from a document collection into an actual knowledge graph.

### Improvement 5: Quality Scoring

Each published page should get a quality score based on:

| Factor | Points |
|--------|--------|
| Has complete frontmatter | 2 |
| Has 2+ outbound cross-links | 2 |
| Has 2+ inbound backlinks | 2 |
| Content length > 500 words | 1 |
| Has been read/searched in last 30 days | 2 |
| Updated within last 90 days | 1 |

Pages below a threshold (e.g., 4 points) get flagged for review or deletion. This creates a self-pruning mechanism — stale, unlinked, never-read pages get surfaced for cleanup.

### Improvement 6: Inbox Retention Policy

Processed inbox items should follow a lifecycle:

- **Pending**: Lives in inbox indefinitely (or until manually resolved)
- **Approved**: Moved to published wiki, inbox copy archived to `inbox/archive/` for 30 days, then purged
- **Rejected**: Archived for 7 days, then purged

This keeps the inbox as a queue rather than a landfill.

### Improvement 7: Blog Cross-Pollination

After auditing the blog and wiki, the most striking finding was that **they operate as completely separate systems**. The blog had 16 news digest posts (all drafts, zero lasting value) while the wiki had genuinely interesting research (LiteLLM benchmarks, HAZ agentic RL, draw.io stack analysis) that never made it to the blog.

The fix: when a wiki page is published with high quality score and high-interest tags (benchmarks, analysis, research), suggest cross-posting to the blog. The wiki stores the technical detail; the blog gets the polished narrative version.

## The Deeper Insight: Capture Friction is Everything

The reason most knowledge management systems fail isn't technology — it's friction. If capturing knowledge requires opening a specific app, navigating to the right folder, choosing a template, and formatting content, you won't do it. The knowledge stays in chat history and evaporates.

This wiki system works because the capture friction is near zero. The agent is already in the conversation. It already produced the analysis. Saying "put it in the wiki" triggers one tool call. The structuring, categorization, and frontmatter happen automatically. The only manual step is approval — a single confirmation.

The audit pipeline ensures that low capture friction doesn't translate into low published quality. You can submit freely because the inbox is disposable. But publishing requires intentionality.

## Conclusion

After six weeks of real use, the wiki has captured 29 pages of genuine knowledge — container tuning fixes that would have been re-debugged from scratch, LiteLLM benchmarks that would have been re-run, research findings that would have been forgotten. The inbox-audit-publish pipeline successfully prevents the quality death spiral that killed previous attempts at AI-managed knowledge bases.

The system isn't perfect — stale indexes, no versioning, weak cross-linking, and inbox bloat are real problems. But the architecture is sound: flat files, MCP tools, editorial pipeline. The fixes are incremental improvements to an already-working system, not fundamental redesigns.

The takeaway for anyone building an AI knowledge system: **don't give the agent direct write access**. Use a queue. Audit before publishing. Separate capture from commitment. The agent's greatest strength — tireless content generation — is also its greatest threat to knowledge quality. A pipeline channels that energy productively.

---

*The agent-wiki skill and all 14 MCP tools are open and running on this system. If you want to explore the wiki structure, the schema lives at `SCHEMA.md` and the full index (once updated) lives at `index.md`.*
