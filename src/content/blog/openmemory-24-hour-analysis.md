---
pubDatetime: 2026-03-06T00:45:00Z
title: "OpenMemory Storage Analysis: What Got Recorded in 24 Hours"
postSlug: "openmemory-24-hour-analysis"
description: "A look at 32 OpenMemory entries recorded over 24 hours, showing what types of data are automatically captured and when."
tags:
  - data-storage
  - openmemory
  - context-tracking
  - memory-analysis
  - ai-infrastructure
---

We recently enabled auto-recording for OpenMemory, and after 24 hours, we have a clear picture of what's being stored. This analysis shows the breakdown of memory types, timestamps, and patterns in how context is being captured.

## The Numbers

In the last 24 hours, **32 entries** were recorded across **10 different types**:

| Type | Count | Description |
|------|-------|-------------|
| `initiative` | 10 | Configuration updates, implementations, enhancements |
| `flow` | 8 | Blog posts, task completions, automations |
| `setup` | 2 | WAL checkpoint cron, hourly monitor |
| `roadmap` | 3 | Phase additions, enhancement plans |
| `conversation` | 2 | Session notes, auto-record discovery |
| `menu_choice` | 2 | Brainstorm selections |
| `deferred` | 1 | Directus metadata brainstorm (parked) |
| `workflow` | 1 | Migration plan SQLite → PostgreSQL |
| `documentation` | 1 | q-brainstorm.md update |
| `unknown` | 2 | Legacy entries |

{{< chart >}}
{
  type: 'bar',
  data: {
    labels: ['initiative', 'flow', 'roadmap', 'setup', 'conversation', 'menu_choice', 'deferred', 'workflow', 'documentation', 'unknown'],
    datasets: [{
      label: 'Entry Count',
      data: [10, 8, 3, 2, 2, 2, 1, 1, 1, 2],
      backgroundColor: ['#6366f1', '#22d3ee', '#f59e0b', '#10b981', '#ec4899', '#a855f7', '#ef4444', '#94a3b8', '#3b82f6', '#64748b']
    }]
  },
  options: {
    indexAxis: 'y',
    plugins: {
      title: { display: true, text: 'Memory Types Recorded (Last 24 Hours)', color: '#e2e8f0' },
      legend: { display: false }
    },
    scales: {
      x: { ticks: { color: '#94a3b8' }, grid: { color: '#334155' } },
      y: { ticks: { color: '#e2e8f0' }, grid: { color: '#334155' } }
    }
  }
}
{{< /chart >}}

## Timeline of Activity

Here's when entries were recorded (most recent first):

| Time | Type | What Was Recorded |
|------|------|-------------------|
| 03/06 00:36 | `setup` | OpenMemory WAL checkpoint cron job configured |
| 03/06 00:29 | `conversation` | Auto-record enabled for OpenMemory |
| 03/06 00:27 | `conversation` | Session 2026-03-06 - Discovery of recording issue |
| 03/05 23:41 | `flow` | Task completed: Week in Review blog post |
| 03/05 23:40 | `deferred` | Directus metadata brainstorm parked |
| 03/05 23:38 | `flow` | Blog post: Question Tool Enhancement System |
| 03/05 22:34 | `roadmap` | Added Phase 12 - User Onboarding |
| 03/05 22:34 | `initiative` | Mandatory question tool display added |
| 03/05 22:34 | `initiative` | WeasyPrint Docker container setup |
| 03/05 22:34 | `workflow` | Migration plan: SQLite → PostgreSQL |
| 03/05 21:29 | `menu_choice` | Brainstorm session: Question Templates |
| 03/05 21:15 | `initiative` | Question Tool Enhancement Complete |
| 03/05 21:14 | `initiative` | Phase 3: Smart Question Generation |
| 03/05 21:07 | `initiative` | Phase 2: Chained Questions |
| 03/05 20:59 | `initiative` | Phase 1: Question Templates |
| 03/05 20:54 | `roadmap` | Question Tool Enhancement Plan |
| 03/05 20:46 | `initiative` | Updated Local File Links in AGENTS.md |
| 03/05 19:47 | `initiative` | RAG System Implementation Complete |
| 03/05 19:42 | `flow` | Weekly memory report cron configured |

## Key Patterns

### Initiative Dominance (31% of entries)

The `initiative` type leads with 10 entries. These capture:
- Configuration updates to AGENTS.md
- Implementation completions (Question Tool phases)
- System enhancements (RAG, WeasyPrint)

This makes sense — we're actively developing and configuring the system, so implementation milestones are the most frequent event type.

### Flow Entries (25% of entries)

`flow` entries track:
- Blog post publications
- Task completions
- Automation runs

These are outcome-focused, capturing when something was delivered rather than the work-in-progress.

### Conversation Entries (New Addition)

The `conversation` type is new — added when auto-recording was enabled. These capture:
- Session summaries
- Discovery moments (finding that auto-record wasn't working)
- Key exchanges worth remembering

### Deferred Items

The single `deferred` entry shows the brainstorm session that was parked for later. This is useful for resuming work — the context is preserved with:
- What was being discussed (Directus metadata management)
- Where we stopped (Build phase of brainstorm)
- What the next steps are

## What This Tells Us

### Good Coverage

The spread across 10 types suggests the memory system is capturing a healthy variety of context:
- **Work**: initiatives, flows, workflows
- **Planning**: roadmaps, deferred items
- **Interaction**: conversations, menu choices
- **System**: setup, documentation

### Temporal Clustering

Most entries (20+) were recorded between 19:35 and 23:41 on March 5th — an active development session. The early morning hours (00:27-00:36) captured the auto-recording setup and initial test.

### Gaps to Watch

Missing types that might be useful:
- `error-solution` — When we fix something, capture the error and solution
- `learned-pattern` — Discoveries about how the system works
- `preference` — User preferences that emerge over time

## Querying the Data

To retrieve recent memories yourself:

```bash
curl -s -X POST http://localhost:8081/mcp \
  -H "Authorization: Bearer openmemory-secret-key-2025" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"openmemory_list","arguments":{"limit":50}},"id":1}'
```

For semantic search:

```bash
curl -s -X POST http://localhost:8081/mcp \
  -H "Authorization: Bearer openmemory-secret-key-2025" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"openmemory_query","arguments":{"query":"question tool implementation","limit":10}},"id":1}'
```

## Takeaways

1. **Initiative and flow types dominate** — work and outcomes are well-tracked
2. **Auto-recording is working** — conversations and exchanges are now being captured
3. **Temporal clustering** — active sessions generate 20+ entries, quiet periods generate fewer
4. **Type coverage is good** — 10 types provide useful categorization
5. **Deferred items persist** — parked tasks retain full context for resumption

The 24-hour snapshot shows a healthy, active memory system that's capturing development work, decisions, and session context automatically.

---

**Total memories in system**: ~1,083