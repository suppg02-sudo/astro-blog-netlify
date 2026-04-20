---
pubDatetime: 2026-03-04T05:30:00Z
title: "Building a Context-Aware Blog Publishing Flow for AI Agents"
postSlug: "context-aware-blog-publishing-flow"
description: "How we built a bp trigger that detects what just happened in a session and publishes it as a Hugo blog post — with context detection, clarifying questions, auto-testing, and link delivery."
tags:
  - openmemory
  - automation
  - triggers
  - ai-infrastructure
  - hugo
  - workflow
  - blog
---

The problem: after a long session of building, debugging, or researching, the results live in chat history and nowhere else. Publishing a blog post means manually extracting context, writing frontmatter, picking tags, saving the file, checking Hugo, and grabbing the URL. Too many steps — so it doesn't happen.

The solution: say `bp` and the agent does all of it.

## The Flow

{{< mermaid >}}
flowchart TD
    A[bp trigger] --> B[Phase 1: Context Detection]
    B --> C[Phase 2: Clarifying Questions]
    C --> D[Phase 3: Write Article]
    D --> E[Phase 3.5: Visual Enhancement]
    E --> F[Phase 4: Create Post]
    F --> G[Phase 5: Test & Verify]
    G --> H[Phase 6: Deliver Links]
{{< /mermaid >}}

Six phases, but the user only interacts at phase 2 — everything else is automatic.

## Phase 1: Context Detection

When the user says `bp`, the agent scans the current session in priority order:

| Priority | Source | Example |
|----------|--------|---------|
| 1 | Last long response | A detailed answer with tables, code, or results |
| 2 | Completed tasks | Todo items marked done this session |
| 3 | Tool outputs | Bash commands that produced meaningful output |
| 4 | Research results | Deep research, documentation lookups |
| 5 | Reports | Memory reports, system audits |
| 6 | Decisions | Architecture choices, config changes |
| 7 | Explicit topic | User said `bp <topic>` |

The agent extracts a context bundle: what happened, key data (tables, stats, code), the outcome, and suggested category/tags.

## Phase 2: One Menu

Not a chain of questions — a single menu:

```
Blog Post — "Building a Context-Aware Blog Publishing Flow"
I'll write about: Created a bp trigger system with 6-phase flow...

  1) Publish as-is (Recommended)
  2) Change title/angle
  3) Add more detail
  4) Make it shorter
  5) Change category
  6) Skip
```

Pick 1 and it goes straight to writing. Pick 2-5 for adjustments. Pick 6 to bail.

## Phase 3: Write the Article

Content rules:
- **No fluff** — every paragraph has information
- **Tables** for structured data
- **Code blocks** with language tags for commands and configs
- **Real data** — actual numbers, paths, outputs from the session
- **Scannable** — headers, short paragraphs, key takeaways

Length targets:

{{< chart >}}
{
  type: 'bar',
  data: {
    labels: ['Quick finding', 'Build log', 'Research report', 'Session summary'],
    datasets: [{
      label: 'Target Lines (Midpoint)',
      data: [150, 300, 225, 150],
      backgroundColor: ['#6366f1', '#22d3ee', '#a855f7', '#10b981'],
      borderWidth: 0
    }]
  },
  options: {
    indexAxis: 'y',
    plugins: {
      title: { display: true, text: 'Target Length by Post Type', color: '#e2e8f0' },
      legend: { display: false }
    },
    scales: {
      x: { grid: { color: '#334155' }, ticks: { color: '#e2e8f0' } },
      y: { grid: { display: false }, ticks: { color: '#e2e8f0' } }
    }
  }
}
{{< /chart >}}

| Post Type | Lines |
|-----------|-------|
| Quick finding | 100-200 |
| Build log | 200-400 |
| Research report | 150-300 |
| Session summary | 100-200 |

## Phase 4: Create the File

Filename: `{YYYY-MM-DD}-{slug}.md`

Frontmatter:
```yaml
---
title: "The Title"
slug: "the-slug"
date: 2026-03-04T05:30:00Z
draft: false
tags: ["tag1", "tag2"]
categories: ["Category"]
description: "SEO description."
---
```

Location: `/media/docker/website/content/posts/`

## Phase 5: Test & Verify

```bash
# Check if live
curl -s -o /dev/null -w "%{http_code}" http://localhost:1313/posts/{slug}/

# If 404, force Hugo rebuild
docker exec hugo hugo 2>&1 | tail -5

# Re-check
curl -s -o /dev/null -w "%{http_code}" http://localhost:1313/posts/{slug}/
```

Common fixes:
- **404 after write** → Hugo live-reload sometimes does partial builds. Force full rebuild.
- **Post not in listing** → Check date isn't in the future.
- **Broken rendering** → Unclosed code blocks or bad markdown.

## Phase 6: Deliver Links

Two links, always:

```
✅ Blog post published:

📄 Web:  http://ubuntu4:1313/posts/{slug}/
📁 File: http://ubuntu4:8080/editor/docker/website/content/posts/{filename}
```

Then store to OpenMemory for the record:

```
openmemory_store(
  content: "blog_post: {title} published to Hugo",
  metadata: {
    "type": "flow",
    "subtype": "blog_post",
    "title": "{title}",
    "slug": "{slug}",
    "url": "http://ubuntu4:1313/posts/{slug}/",
    "timestamp": "..."
  },
  tags: ["flow", "blog_post", "hugo"]
)
```

## Also Built: The Defer System

Same session, we built `defer` and `deferred` triggers for parking tasks:

- **`defer`** — Captures current context, next steps, and reason. Stores to OpenMemory with type `deferred`, status `pending`.
- **`deferred`** — Queries OpenMemory for pending items. Shows a menu to resume, complete, or cancel.

This means you can be mid-task, say `defer`, and pick it up days later with full context preserved.

## The Trigger File

The full `bp` trigger lives at `~/.config/opencode/docs/instructions/triggers/bp.md` — 224 lines covering all 6 phases with:
- Context detection priority table
- Question menu templates
- Content rules and tone guidelines
- Hugo frontmatter template
- Test and verify steps with common fixes
- Link format with NextExplorer integration
- OpenMemory storage pattern

## Key Design Decisions

1. **One menu, not a chain.** Multiple clarifying questions kill momentum. One menu with 6 options covers everything.

2. **Context detection is automatic.** The agent doesn't ask "what do you want to blog about?" — it figures it out from the session.

3. **Always test.** Hugo's live-reload sometimes misses new files. The flow always curls the URL and force-rebuilds if needed.

4. **Two links, always.** Web URL for reading, NextExplorer link for editing. Both use the Tailscale hostname so they work from any device.

5. **Store the record.** Every publication gets logged to OpenMemory so there's a searchable history of what was published and when.

---

*Trigger file: `~/.config/opencode/docs/instructions/triggers/bp.md`*
*AGENTS.md entry updated with full flow description.*