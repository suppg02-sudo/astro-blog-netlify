---
pubDatetime: 2026-02-26T12:00:00Z
title: "Context as a Budget: Progressive Disclosure and Unified Analytics for AI Agents"
postSlug: "context-registry-progressive-disclosure-ai-agents"
description: "How to build a two-part system that reduces context bloat through progressive disclosure while gaining deep insights into agent behavior through unified analytics."
tags:
  - analytics
  - opencode
  - ai-agents
  - sqlite
  - opentelemetry
  - observability
  - progressive-disclosure
---

## The Hidden Cost of AI Agents

Here's a number that should concern anyone building AI agent systems: **8,317 lines**.

That's the size of one skill file in my OpenCode setup. Every time the agent considers using that skill—even just to check if it's relevant—those 8,317 lines potentially enter the context window.

The problem isn't just one file. It's the accumulation:

- openrag: 8,317 lines
- astro: 2,560 lines
- dashboard: 1,833 lines
- diagnose: 1,432 lines

Fifteen skills exceed 500 lines. When the agent loads context for a simple task, it's often loading megabytes of documentation, troubleshooting guides, and reference material it doesn't need.

But context bloat is only half the problem. The other half is invisibility.

When an AI agent completes a task, what do you know about what happened? Which skills worked? Which failed? Where did the user have to correct the agent? What tasks get abandoned halfway through?

Most agent systems are black boxes. They run, they produce output, but they don't tell you how to make them better.

This post describes a two-part solution:

1. **Progressive disclosure** - Load context in levels, only what's needed when it's needed
2. **Unified context registry** - Capture everything, learn from patterns, improve continuously

The guiding principle: **Context is a budget, not unlimited storage.**

---

## Progressive Disclosure: Four Levels of Context

The key insight behind progressive disclosure is simple: not all context is needed all the time.

When an agent starts a session, it needs to know what skills exist. It doesn't need the full documentation for every skill. When a skill is triggered, it needs metadata—commands, dependencies, configuration. Only when executing does it need the full documentation, scripts, and templates.

Here's the four-level model:

| Level | Name | When Loaded | Size Target | Content |
|-------|------|-------------|-------------|---------|
| **0** | Capability | Session start | ~2KB total | Skill names, triggers, one-liners |
| **1** | Metadata | On trigger word | ~500B/skill | YAML config, commands, dependencies |
| **2** | Working | On execution | 2-10KB | Full docs, scripts, templates |
| **3** | Reference | On demand | Unlimited | Deep docs, troubleshooting, examples |

### Level 0: Capability Index

This is always loaded. It's a lightweight index of all available skills:

```json
{
  "skill_index": {
    "hugo": {
      "name": "hugo",
      "description": "Create and publish blog posts on Hugo static site",
      "triggers": ["hugo", "bp"],
      "category": "content"
    },
    "openrag": {
      "name": "openrag",
      "description": "Manage OpenRAG document retrieval stack",
      "triggers": ["openrag", "rag"],
      "category": "rag"
    },
    "containers": {
      "name": "containers",
      "description": "Docker container management with docker-compose",
      "triggers": ["containers"],
      "category": "infrastructure"
    }
  }
}
```

Total size for 50+ skills: about 2KB. The agent knows what's available without loading everything.

### Level 1: Skill Metadata

When a trigger word is detected or a skill is being considered, load the metadata:

```yaml
name: hugo
version: 5.1.0
dependencies:
  - hugo binary
  - website repository
commands:
  - hugo new
  - hugo publish
  - hugo validate
prerequisites:
  - hugo installed
  - content directory exists
```

This tells the agent how to invoke the skill correctly—about 500 bytes per skill.

### Level 2: Working Context

When the skill is actually executing, load the full SKILL.md file, scripts, and templates. This is the 2-10KB range where you include examples, step-by-step instructions, and working scripts.

### Level 3: Reference Material

Only load deep documentation, troubleshooting guides, and extensive examples when explicitly needed—usually when something goes wrong or the user asks for detailed help.

### The Impact

For a simple status check on OpenRAG:

| Before | After |
|--------|-------|
| Load 8,317 lines | Load ~100 lines (Level 0-1) |
| ~50KB context | ~3KB context |
| Slower startup | Instant availability |

The skill still has all its documentation. It's just structured so the agent loads it progressively rather than all at once.

---

## Context Registry Architecture

Progressive disclosure solves the loading problem. But we still need to understand what's happening inside our agents.

The context registry is a three-layer system that captures, stores, and analyzes agent behavior:

```
┌─────────────────────────────────────────────────────────────┐
│ Layer 1: JSON Event Capture (Immediate, Non-blocking)       │
│ Location: ~/.config/opencode/context-registry/data/         │
│ Purpose: Fast writes, no impact on agent performance        │
└────────────────────────┬────────────────────────────────────┘
                         │ Hourly sync + on-demand
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ Layer 2: SQLite Analytics (Query Power)                     │
│ Location: ~/.config/opencode/context-registry/analytics.db  │
│ Purpose: SQL queries, aggregations, pattern detection       │
└────────────────────────┬────────────────────────────────────┘
                         │ Daily extraction
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ Layer 3: Persistent Memory (Supermemory/OpenMemory)         │
│ Purpose: Cross-session learning, semantic retrieval         │
│ Types: learned-pattern, preference, error-solution          │
└─────────────────────────────────────────────────────────────┘
```

### What Gets Captured

The registry captures events at key decision points:

| Event Type | Trigger | Data Captured |
|------------|---------|---------------|
| `skill_invocation` | After skill completes | skill, action, success, duration, context |
| `menu_choice` | User selects option | category, options presented, selected, time |
| `agent_session` | Session ends | agents used, skills invoked, outcome |
| `tool_execution` | Tool completes | tool, success, duration, error (from OTEL) |
| `user_correction` | User redirects agent | original approach, corrected approach |
| `delegation` | Agent delegates | from_agent, to_agent, reason, complexity |
| `task_abandoned` | Incomplete task | last action, errors, abandonment point |

### Event Schema

All events flow through a unified schema:

```json
{
  "id": "evt_20260226_143045_abc1",
  "timestamp": "2026-02-26T14:30:45Z",
  "session_id": "ses_xyz123",
  "event_type": "skill_invocation",
  "data": {
    "skill": "hugo",
    "action": "create",
    "success": true,
    "duration_ms": 4200,
    "context": {
      "trigger": "bp",
      "task": "Create blog post about progressive disclosure"
    }
  },
  "tags": ["blog", "hugo", "content"]
}
```

This unified format makes it easy to query across event types and correlate related actions.

---

## Beyond Basic Tracking: Learning from Behavior

Basic tracking tells you *what* happened. The context registry goes further—it captures signals that help you understand *why* and *how to improve*.

### User Corrections: The Learning Goldmine

Every time a user says "no, do it this way" or "actually, use the other template," that's a learning opportunity. The registry captures these corrections:

```json
{
  "event_type": "user_correction",
  "data": {
    "skill": "hugo",
    "original_approach": "Use default blog template",
    "corrected_approach": "Use research-summary template instead",
    "correction_type": "refinement",
    "should_learn": true
  }
}
```

Correction types:
- **refinement**: User adjusted approach (use different template, add more detail)
- **rejection**: User stopped action entirely (don't delete those files)
- **clarification**: User provided missing context (I meant the staging server)

These corrections feed into Supermemory as `learned-pattern` entries, so future sessions can avoid the same mistakes.

### Delegation Events: Understanding Agent Selection

When the main agent delegates to a subagent, why did it make that choice?

```json
{
  "event_type": "delegation",
  "data": {
    "from_agent": "sisyphus",
    "to_agent": "sisyphus-junior",
    "reason": "simple_file_read",
    "task_description": "Read config.json and extract database URL",
    "task_complexity": "low",
    "delegate_success": true
  }
}
```

This data reveals patterns:
- Which agents handle which task types well
- Whether complexity assessments are accurate
- If delegation is overused or underused

### Abandoned Tasks: Finding Friction Points

Tasks that start but never finish reveal friction:

```json
{
  "event_type": "task_abandoned",
  "data": {
    "task_description": "Set up OpenRAG cluster",
    "task_started_at": "2026-02-26T10:00:00Z",
    "last_skill_invoked": "diagnose",
    "last_tool_used": "bash",
    "abandonment_point": "after_error",
    "skills_attempted": ["openrag", "diagnose"],
    "errors_encountered": ["port 9200 already in use"]
  }
}
```

Common abandonment patterns indicate:
- Skills that need better error handling
- Configuration issues in the environment
- Tasks that are genuinely too complex

---

## Integration with OpenTelemetry

If you already have OpenTelemetry instrumentation, you might wonder: isn't this duplicating what OTEL already captures?

The answer is: partially, but each system has distinct strengths.

### What OTEL Captures (Keep It)

OpenTelemetry operates at the SDK level, automatically capturing:

- Session lifecycle (start, end, duration)
- All tool executions (before/after with timing)
- Agent switches (when agent identity changes)
- Errors with full context

```
OTEL Span: tool.bash
├── tool.name: bash
├── tool.success: true
├── tool.duration_ms: 234
├── session.id: ses_xyz123
└── agent.name: sisyphus
```

This is valuable for debugging and performance analysis. Jaeger traces show you exactly what happened in a session.

### What the Registry Adds

OpenTelemetry doesn't know about:

- **Skill names**: OTEL sees `tool.task` but not that it invoked the `hugo` skill
- **Menu choices**: No visibility into what options were presented or selected
- **User corrections**: Can't detect when user redirects the agent
- **Delegation decisions**: Doesn't capture why one agent delegates to another
- **Abandoned tasks**: No concept of task completion vs abandonment

### The Integration Pattern

```
┌─────────────────────────────────────────────────────────────┐
│                    Data Sources                             │
├──────────────────────┬──────────────────────────────────────┤
│   OpenTelemetry      │   Context Registry Hooks             │
│   (Automatic)        │   (Agent-Level)                      │
├──────────────────────┼──────────────────────────────────────┤
│ • session.start/end  │ • skill_invocation                   │
│ • tool.execute       │ • menu_choice                        │
│ • agent.switch       │ • user_correction                    │
│                      │ • delegation_event                   │
│                      │ • task_abandoned                     │
└──────────┬───────────┴──────────────┬───────────────────────┘
           │                          │
           │  Hourly sync             │  Immediate
           ▼                          ▼
┌─────────────────────────────────────────────────────────────┐
│              SQLite Analytics Database                       │
│  Unified schema with source tagging:                        │
│  - source: "otel" | "registry"                              │
│  - Correlate by session_id                                  │
└─────────────────────────────────────────────────────────────┘
```

A sync script pulls OTEL traces from Jaeger into SQLite:

```bash
#!/bin/bash
# scripts/sync-otel-to-sqlite.sh

# Query Jaeger for recent traces
TRACES=$(curl -s "http://localhost:16686/api/traces?service=opencode-agent&lookback=1h")

# Extract tool executions and sessions
echo "$TRACES" | jq -r '.data[] | ...' | while read trace; do
    # Insert into SQLite with source="otel"
    sqlite3 analytics.db "INSERT INTO otel_sessions ..."
done
```

Now you can query across both sources:

```sql
-- Correlate OTEL sessions with skill usage
SELECT 
    o.session_id,
    o.total_duration_ms / 1000 / 60 as duration_min,
    s.skill,
    s.success
FROM otel_sessions o
JOIN skill_usage s ON o.session_id = s.session_id
WHERE o.started_at > date('now', '-7 days')
ORDER BY o.started_at DESC;
```

---

## Implementation: SQLite Schema

Here's the complete schema for the analytics database:

```sql
-- Skill invocations
CREATE TABLE skill_usage (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    skill TEXT NOT NULL,
    action TEXT,
    success BOOLEAN,
    duration_ms INTEGER,
    session_id TEXT,
    agent TEXT,
    context_tags TEXT,      -- JSON array
    error_message TEXT
);
CREATE INDEX idx_skill_name ON skill_usage(skill);
CREATE INDEX idx_skill_timestamp ON skill_usage(timestamp);
CREATE INDEX idx_skill_session ON skill_usage(session_id);

-- Menu choices
CREATE TABLE menu_choices (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    category TEXT,              -- workflow, debug, skill_selection, etc.
    question_header TEXT,
    options_count INTEGER,
    options_selected TEXT,      -- JSON array of what user chose
    selection_time_ms INTEGER,
    session_id TEXT
);
CREATE INDEX idx_menu_category ON menu_choices(category);

-- User corrections (learning opportunities)
CREATE TABLE user_corrections (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    session_id TEXT,
    skill_invoked TEXT,
    original_approach TEXT,
    correction_type TEXT,       -- refinement, rejection, clarification
    corrected_approach TEXT,
    should_learn BOOLEAN DEFAULT 1
);

-- Delegation events
CREATE TABLE delegation_events (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    session_id TEXT,
    from_agent TEXT,
    to_agent TEXT,
    reason TEXT,                -- complexity, specialization, parallel
    task_description TEXT,
    task_complexity TEXT,       -- low, medium, high
    delegate_success BOOLEAN,
    delegate_duration_ms INTEGER
);

-- Abandoned tasks
CREATE TABLE abandoned_tasks (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    session_id TEXT,
    task_started_at DATETIME,
    task_description TEXT,
    last_skill_invoked TEXT,
    last_tool_used TEXT,
    abandonment_point TEXT,     -- after_skill, after_tool, mid_execution
    skills_attempted TEXT,      -- JSON array
    errors_encountered TEXT     -- JSON array
);

-- OTEL sessions (synced from Jaeger)
CREATE TABLE otel_sessions (
    session_id TEXT PRIMARY KEY,
    started_at DATETIME,
    ended_at DATETIME,
    primary_agent TEXT,
    tool_count INTEGER,
    total_duration_ms INTEGER,
    synced_at DATETIME
);

-- Daily aggregates (pre-computed for fast reports)
CREATE TABLE daily_summaries (
    date DATE PRIMARY KEY,
    total_sessions INTEGER,
    total_skill_invocations INTEGER,
    total_tool_executions INTEGER,
    top_skills TEXT,            -- JSON: [{"skill": "hugo", "count": 12}, ...]
    top_tools TEXT,             -- JSON
    top_agents TEXT,            -- JSON
    success_rate REAL,
    avg_session_duration_min REAL,
    detected_workflows TEXT,    -- JSON: ["blog-workflow", "debug-flow", ...]
    recommendations TEXT        -- JSON: ["Improve X", "Fix Y", ...]
);

-- Workflow patterns (detected sequences)
CREATE TABLE workflow_patterns (
    id INTEGER PRIMARY KEY,
    pattern_name TEXT,
    sequence TEXT,              -- JSON: ["research", "hugo", "git"]
    occurrences INTEGER,
    last_seen DATE,
    avg_duration_min REAL,
    success_rate REAL
);
```

### Design Decisions

**Why JSON columns for arrays?** SQLite's JSON support is excellent (`json_extract`, `json_each`). The flexibility of storing arrays as JSON outweighs the normalization benefits for analytics use cases.

**Why daily_summaries?** Pre-computing aggregates makes reports instant. Instead of counting millions of events, query one row per day.

**Why separate tables instead of one events table?** The unified `events` table captures everything, but denormalized tables make common queries simpler and faster.

---

## Non-Interactive Execution: Running Skills via Cron

Not every skill execution involves a user making choices. Many skills run scheduled via cron—daily news reports, weekly cleanup tasks, hourly health checks.

The context registry needs to handle both modes:

| Mode | Session ID | Menu Choices | Tracking Focus |
|------|------------|--------------|----------------|
| **Interactive** | `ses_xyz123` | Captured | User preferences, workflow patterns |
| **Cron** | `cron_20260226_060000` | Skipped | Success rate, timing, errors |

### Skill Design for Dual Modes

Skills should accept CLI flags for non-interactive execution:

```bash
# Interactive (with menu)
./skills/news/scripts/run.sh

# Non-interactive (skip menu, use action)
./skills/news/scripts/run.sh --action=daily-report --no-menu
```

The skill checks for these flags:

```bash
#!/bin/bash
ACTION="${1:-}"
NO_MENU="${2:-}"

if [ "$NO_MENU" = "--no-menu" ] || [ -n "$ACTION" ]; then
    # Non-interactive mode
    ACTION="${ACTION#--action=}"
    SESSION_ID="cron_$(date +%Y%m%d_%H%M%S)"
else
    # Interactive mode - present menu
    ACTION=$(show_menu)
    SESSION_ID="$CURRENT_SESSION"
fi

# Execute with determined action
execute_action "$ACTION"
```

### Cron Configuration

```bash
# /etc/cron.d/opencode-skills

# Daily news report at 6 AM
0 6 * * * root /root/.config/opencode/skills/news/scripts/run.sh --action=daily-report --no-menu >> /root/cron-logs/news.log 2>&1

# Daily research at 7 AM
0 7 * * * root /root/.config/opencode/skills/research/scripts/run.sh --action=ai-ecosystem --no-menu >> /root/cron-logs/research.log 2>&1

# Weekly cleanup (Sunday 5 AM)
0 5 * * 0 root /root/.config/opencode/skills/maintenance/scripts/run.sh --action=cleanup --no-menu >> /root/cron-logs/maintenance.log 2>&1
```

### Tracking Cron Sessions

The registry records cron sessions differently:

```bash
~/.config/opencode/context-registry/scripts/record-skill.sh \
    "news" \
    "$SUCCESS" \
    "cron:daily-report" \
    "cron_20260226_060000" \
    "cron,scheduled,daily-report"
```

This creates distinct records:

```sql
-- Query to separate modes
SELECT 
    CASE WHEN session_id LIKE 'cron_%' THEN 'scheduled' ELSE 'interactive' END as mode,
    skill,
    COUNT(*) as runs,
    AVG(duration_ms) as avg_duration_ms,
    100.0 * SUM(CASE WHEN success THEN 1 ELSE 0 END) / COUNT(*) as success_rate
FROM skill_usage
GROUP BY mode, skill;
```

Output:

| mode | skill | runs | avg_duration_ms | success_rate |
|------|-------|------|-----------------|--------------|
| interactive | hugo | 45 | 2100 | 98% |
| interactive | flow | 32 | 900 | 100% |
| scheduled | news | 28 | 4500 | 100% |
| scheduled | maintenance | 4 | 12000 | 75% |

This separation reveals:
- **Scheduled tasks**: Reliability matters more than UX
- **Interactive tasks**: User preferences and workflow patterns matter

### Analytics Report Enhancement

The daily report separates scheduled vs interactive:

```markdown
## Today's Activity

### Interactive Sessions (3)
| Session | Skills Used | Duration | Outcome |
|---------|-------------|----------|---------|
| ses_abc | hugo, research | 8 min | Success |
| ses_def | containers | 12 min | 1 correction |

### Scheduled Tasks (4)
| Task | Scheduled | Result | Duration |
|------|-----------|--------|----------|
| news: daily-report | 06:00 | Success | 4.2s |
| research: ai-ecosystem | 07:00 | Success | 3.8s |
| maintenance: cleanup | 05:00 | Failed | 12s |
| openrag: index-check | 00:00 | Success | 1.2s |

Warning: maintenance: cleanup failed - check /root/cron-logs/maintenance.log
```

---

## Daily Analytics and Automated Insights

The real value of tracking is in the analysis. A daily cron job generates reports:

```bash
# /etc/cron.d/context-registry
0 6 * * * root /root/.config/opencode/context-registry/scripts/daily-analytics.sh
```

### Report Structure

The daily report includes:

**Summary Metrics**
```markdown
## Summary

| Metric | Today | 7-Day Avg | Trend |
|--------|-------|-----------|-------|
| Sessions | 5 | 4.2 | up |
| Skill Invocations | 23 | 18.5 | up |
| Success Rate | 94% | 91% | up |
| Avg Session Duration | 12.3 min | 10.8 min | up |
```

**Top Skills**
```markdown
## Top Skills Used

| Skill | Count | Success | Avg Duration |
|-------|-------|---------|--------------|
| hugo | 8 | 100% | 2.1s |
| flow | 6 | 100% | 0.9s |
| containers | 4 | 75% | 3.2s |
```

**Workflow Patterns**
```markdown
## Detected Workflows

| Pattern | Sequence | Occurrences |
|---------|----------|-------------|
| morning-routine | news -> maintenance -> space | 3 |
| blog-workflow | research -> hugo -> git | 2 |
| debug-flow | diagnose -> flow -> databases | 1 |
```

**User Corrections**
```markdown
## Learning Opportunities

| Session | Skill | What Changed |
|---------|-------|--------------|
| ses_abc | hugo | Used research-summary template instead of default |
| ses_def | containers | Stopped aggressive Docker cleanup |
```

### Automated Recommendations

The analytics script generates actionable recommendations:

```markdown
## Recommendations

1. Warning: containers skill has 75% success rate
   - Error: "Docker socket permission denied"
   - Suggested fix: Check docker group membership

2. Opportunity: research + hugo used together 89% of the time
   - Consider creating combined trigger: bp-research

3. Menu optimization: "Exit" selected 35% of the time
   - Consider simplifying menu structure

4. Improved: Success rate up 3% this week
   - Previous errors with openrag resolved
```

These recommendations close the feedback loop: tracking -> analysis -> improvement -> better outcomes.

---

## Putting It Together

The complete system looks like this:

```
+-------------------------------------------------------------+
|                    AGENT EXECUTION                          |
+-------------------------------------------------------------+
|  1. Load Level 0 (skill index)                              |
|  2. Detect trigger -> Load Level 1 (metadata)               |
|  3. Execute skill -> Load Level 2 (working context)         |
|  4. On error/demand -> Load Level 3 (reference)             |
+-----------------------------+-------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|                    EVENT CAPTURE                            |
+-------------------------------------------------------------+
|  * skill_invocation (after task completes)                  |
|  * menu_choice (after user selection)                       |
|  * user_correction (when user redirects)                    |
|  * delegation (when agent delegates)                        |
|  * task_abandoned (incomplete tasks)                        |
|  * tool_execution (from OTEL sync)                          |
+-----------------------------+-------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|                    STORAGE LAYERS                           |
+-------------------------------------------------------------+
|  JSON (immediate) -> SQLite (analytics) -> Supermemory (LTM)|
+-----------------------------+-------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|                    OUTPUTS                                  |
+-------------------------------------------------------------+
|  * Daily analytics reports                                  |
|  * Workflow pattern detection                               |
|  * Automated recommendations                                |
|  * Supermemory learned patterns                             |
+-------------------------------------------------------------+
```

---

## Benefits Summary

| Problem | Solution | Impact |
|---------|----------|--------|
| Context bloat | Progressive disclosure | 90%+ reduction in loaded context |
| Black box agents | Event capture | Full visibility into behavior |
| Repeated mistakes | User correction tracking | Learning from feedback |
| Unknown friction | Abandoned task detection | Identify blockers |
| No improvement path | Daily recommendations | Data-driven optimization |
| Duplicated effort | OTEL integration | Unified analytics, no redundancy |

---

## Getting Started

1. **Create the SQLite schema** - Run the schema above to create `analytics.db`

2. **Add event capture hooks** - Instrument your agent to call recording scripts after key events

3. **Build the Level 0 index** - Scan your skills and extract metadata into a lightweight index

4. **Set up the daily cron** - Schedule the analytics script to run each morning

5. **Review and iterate** - Check the daily reports, implement recommendations, measure improvement

The goal isn't perfect tracking from day one. Start with skill invocations and menu choices, then add user corrections and delegation events as you see value.

---

## Flow Analysis: From Logs to Queries

If you already have a flow analysis system that parses session logs, you might wonder how it relates to the context registry. The answer: they complement each other.

### What Flow Analysis Does Well

Traditional flow analysis works by parsing session logs after execution:

- **Decision rationale**: Captures why the agent made specific choices
- **Divergence detection**: Identifies where execution deviated from expected paths
- **Session narrative**: Tells the story of what happened in human-readable form
- **On-demand analysis**: Run when you want to understand a specific session

### What the Registry Adds

The context registry provides what log parsing cannot:

| Capability | Log Parsing | Context Registry |
|------------|-------------|------------------|
| Data source | Session logs (post-hoc) | Real-time event capture |
| When analysis happens | On-demand | Continuous + scheduled |
| Historical queries | Single session | SQL across all sessions |
| Pattern detection | Session-level | Cross-session analytics |
| Precision | Depends on log format | Millisecond timing |
| Aggregations | Manual | Pre-computed daily |

### The Hybrid Approach

The most powerful setup uses both: the registry for data, flow analysis for narrative.

```
+-------------------------------------------------------------+
|                    Flow Analysis (Enhanced)                 |
+-------------------------------------------------------------+
|  1. Query context registry for session data                 |
|  2. Add narrative layer and decision rationale              |
|  3. Generate improvement recommendations                    |
|  4. Compare to historical patterns                          |
+-----------------------------+-------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|                 Context Registry (SQLite)                   |
+-------------------------------------------------------------+
|  * skill_usage        * menu_choices                        |
|  * tool_executions    * user_corrections                    |
|  * delegation_events  * abandoned_tasks                     |
|  * otel_sessions      * workflow_patterns                   |
+-------------------------------------------------------------+
```

### Enhanced Flow Query Script

Instead of parsing logs, flow analysis queries the registry:

```bash
#!/bin/bash
# scripts/flow-from-registry.sh

SESSION_ID="${1:-last}"

if [ "$SESSION_ID" = "last" ]; then
    SESSION_ID=$(sqlite3 analytics.db "
        SELECT session_id FROM skill_usage 
        ORDER BY timestamp DESC LIMIT 1
    ")
fi

echo "## Flow Analysis: $SESSION_ID"
echo ""

# Skills used
echo "### Skills Invoked"
sqlite3 -header -column analytics.db "
    SELECT skill as Skill,
           CASE WHEN success THEN 'OK' ELSE 'FAIL' END as Status,
           duration_ms || 'ms' as Duration,
           COALESCE(error_message, '-') as Error
    FROM skill_usage 
    WHERE session_id = '$SESSION_ID'
"

# Tools used
echo ""
echo "### Tools Executed"
sqlite3 -header -column analytics.db "
    SELECT tool_name as Tool,
           CASE WHEN success THEN 'OK' ELSE 'FAIL' END as Status,
           duration_ms || 'ms' as Duration
    FROM tool_executions 
    WHERE session_id = '$SESSION_ID'
    ORDER BY timestamp
"

# Pattern match
echo ""
echo "### Pattern Detection"
SKILLS=$(sqlite3 analytics.db "
    SELECT json_group_array(skill) FROM (
        SELECT skill FROM skill_usage 
        WHERE session_id = '$SESSION_ID' ORDER BY timestamp
    )
")
PATTERN=$(sqlite3 analytics.db "
    SELECT pattern_name, occurrences 
    FROM workflow_patterns 
    WHERE sequence = '$SKILLS'
")
if [ -n "$PATTERN" ]; then
    echo "Matched: $PATTERN"
else
    echo "New pattern detected"
fi

# Session metrics
echo ""
echo "### Session Metrics"
sqlite3 analytics.db "
    SELECT 
        'Total Duration: ' || (SUM(duration_ms) / 1000) || 's' as Metric
    FROM skill_usage WHERE session_id = '$SESSION_ID'
    UNION ALL
    SELECT 
        'Success Rate: ' || (
            100.0 * SUM(CASE WHEN success THEN 1 ELSE 0 END) / COUNT(*)
        ) || '%'
    FROM skill_usage WHERE session_id = '$SESSION_ID'
"
```

### Sample Output

```markdown
## Flow Analysis: ses_abc123

### Skills Invoked
Skill     Status  Duration  Error
--------  ------  --------  -----
research  OK      4500ms    -
hugo      OK      2100ms    -

### Tools Executed
Tool  Status  Duration
----  ------  --------
bash  OK      120ms
read  OK      15ms
write OK      8ms

### Pattern Detection
Matched: blog-workflow (12 previous uses)

### Session Metrics
Total Duration: 6.6s
Success Rate: 100%
```

### Why This Matters

With the registry powering flow analysis, you can:

- **Query any historical session** instantly
- **Compare sessions** to find patterns
- **Generate flow reports on demand** without log parsing
- **Correlate skills with outcomes** across weeks or months
- **Identify improvement opportunities** from aggregated data

The narrative layer (decision rationale, divergence detection) still requires agent-level instrumentation. But the data layer—what happened, when, how long, success or failure—comes from the registry.

---

## Self-Optimizing Menus: Learning from Choices

The `menu_choices` table captures every decision point: what options were presented, what the user selected, and how long they took to decide. This data enables systematic menu improvement over time.

### What the Data Reveals

```sql
-- Sample menu analytics query
SELECT 
    category,
    question_header,
    COUNT(*) as presentations,
    AVG(options_count) as avg_options,
    AVG(selection_time_ms) as avg_decision_time,
    100.0 * SUM(CASE WHEN options_selected LIKE '%Exit%' THEN 1 ELSE 0 END) / COUNT(*) as exit_rate
FROM menu_choices
WHERE timestamp > date('now', '-30 days')
GROUP BY category, question_header;
```

Sample output:

| category | question_header | presentations | avg_options | avg_decision_time | exit_rate |
|----------|-----------------|---------------|-------------|-------------------|-----------|
| workflow | Task Active | 156 | 5 | 2340ms | 22% |
| skill | Select Skill | 89 | 8 | 5200ms | 8% |
| confirm | Proceed? | 234 | 2 | 800ms | 5% |
| debug | Error Recovery | 12 | 4 | 8900ms | 42% |

### Optimization Strategies

Each metric suggests a specific action:

| Metric | Threshold | Problem | Action |
|--------|-----------|---------|--------|
| `avg_decision_time > 5000ms` | Slow decisions | Too many options or unclear wording | Reduce options, clarify labels |
| `exit_rate > 30%` | High abandonment | Menus are interrupting flow | Reduce menu frequency |
| `avg_options > 6` | Choice overload | Decision paralysis | Split into sub-categories |
| Single option > 80% | Dominant choice | Menu is unnecessary | Make it default, skip prompt |
| Option never selected | Dead option | Clutter | Remove entirely |

### Weekly Menu Optimization Report

```bash
#!/bin/bash
# scripts/menu-optimizer.sh

echo "# Menu Optimization Report - $(date +%Y-%m-%d)"

# Slow menus
echo ""
echo "## Slow Decision Menus (>5s avg)"
sqlite3 analytics.db "
    SELECT category || ' / ' || question_header as Menu,
           ROUND(avg_time/1000.0, 1) || 's' as 'Avg Time'
    FROM (
        SELECT category, question_header, 
               AVG(selection_time_ms) as avg_time
        FROM menu_choices
        WHERE timestamp > date('now', '-7 days')
        GROUP BY category, question_header
    )
    WHERE avg_time > 5000
    ORDER BY avg_time DESC
"

# High exit rates
echo ""
echo "## High Exit Rates (>30%)"
sqlite3 analytics.db "
    SELECT category || ' / ' || question_header as Menu,
           ROUND(100.0 * exits / total, 1) || '%' as 'Exit Rate'
    FROM (
        SELECT category, question_header,
               SUM(CASE WHEN options_selected LIKE '%Exit%' THEN 1 ELSE 0 END) as exits,
               COUNT(*) as total
        FROM menu_choices
        WHERE timestamp > date('now', '-7 days')
        GROUP BY category, question_header
    )
    WHERE 100.0 * exits / total > 30
"

# Suggested reordering
echo ""
echo "## Suggested Option Reordering (by popularity)"
sqlite3 analytics.db "
    SELECT category,
           GROUP_CONCAT(option, ' -> ') as 'Top to Bottom'
    FROM (
        SELECT category, 
               json_extract(options_selected, '\$[0]') as option,
               COUNT(*) as count
        FROM menu_choices
        WHERE timestamp > date('now', '-30 days')
          AND json_extract(options_selected, '\$[0]') != 'Exit'
        GROUP BY category, option
        ORDER BY count DESC
    )
    GROUP BY category
"
```

### Advanced Menu Capabilities

Beyond basic optimization, the data enables sophisticated adaptive behavior:

**Context-Aware Ordering**

Options reorder based on current context. If the user is in a blog workflow, content-related skills appear first:

```python
def load_menu(category, context):
    # Get recent selections in similar contexts
    history = query("""
        SELECT options_selected, COUNT(*) as count
        FROM menu_choices mc
        JOIN skill_usage su ON mc.session_id = su.session_id
        WHERE mc.category = ? 
          AND su.skill IN (SELECT skill FROM current_context_skills)
        GROUP BY options_selected
        ORDER BY count DESC
    """, category)
    
    return reorder_options(default_options, history)
```

**Time-Based Adaptation**

Menu preferences vary by time of day. Morning sessions might prioritize news and maintenance; evening sessions might favor content creation:

```sql
-- Learn time-of-day preferences
SELECT 
    CASE 
        WHEN strftime('%H', timestamp) BETWEEN 6 AND 12 THEN 'morning'
        WHEN strftime('%H', timestamp) BETWEEN 12 AND 18 THEN 'afternoon'
        ELSE 'evening'
    END as time_of_day,
    options_selected,
    COUNT(*) as count
FROM menu_choices
GROUP BY time_of_day, options_selected
ORDER BY time_of_day, count DESC;
```

**Auto-Default with Confidence**

When one option dominates (>80%), skip the menu entirely but offer an easy undo:

```python
def should_skip_menu(category):
    top_choice = query("""
        SELECT options_selected, 
               100.0 * COUNT(*) / SUM(COUNT(*)) OVER() as rate
        FROM menu_choices
        WHERE category = ? AND timestamp > date('now', '-30 days')
        GROUP BY options_selected
        ORDER BY rate DESC
        LIMIT 1
    """, category)
    
    if top_choice.rate > 80:
        return {
            "skip": True,
            "auto_select": top_choice.option,
            "confidence": top_choice.rate,
            "undo_available": True
        }
    return {"skip": False}
```

**Progressive Disclosure for Menus**

Large menus (8+ options) split into levels. First show top 4 by popularity, then "More options..." for the rest:

```
Level 1 (shown first):
  [hugo]           - 45 selections
  [containers]     - 23 selections  
  [research]       - 18 selections
  [flow]           - 12 selections
  [More options...] 

Level 2 (on demand):
  [diagnose]       - 8 selections
  [maintenance]    - 5 selections
  [databases]      - 3 selections
  [telegram]       - 1 selection
```

**Fatigue Detection**

Track decision quality over session duration. As users tire, they default to "Exit" or quick choices. Reduce menu frequency in late-session stages:

```sql
-- Detect decision fatigue
SELECT 
    session_id,
    CASE 
        WHEN julianday(timestamp) - julianday(session_start) < 0.01 THEN 'early'
        WHEN julianday(timestamp) - julianday(session_start) < 0.03 THEN 'mid'
        ELSE 'late'
    END as session_stage,
    AVG(selection_time_ms) as avg_time,
    100.0 * SUM(CASE WHEN options_selected LIKE '%Exit%' THEN 1 ELSE 0 END) / COUNT(*) as exit_rate
FROM menu_choices
GROUP BY session_stage;

-- Result: late-stage exit_rate often 2-3x higher than early-stage
```

**A/B Testing Menus**

Test different menu structures and measure which performs better:

```sql
-- Compare menu variants
SELECT 
    menu_variant,
    COUNT(*) as presentations,
    AVG(selection_time_ms) as avg_time,
    100.0 * SUM(CASE WHEN outcome = 'success' THEN 1 ELSE 0 END) / COUNT(*) as success_rate
FROM menu_choices
WHERE category = 'workflow'
  AND timestamp > date('now', '-14 days')
GROUP BY menu_variant;
```

### Implementation Roadmap

| Phase | Capability | Automation Level |
|-------|------------|------------------|
| 1 | Weekly optimization report | Manual review |
| 2 | Auto-reorder by popularity | Semi-automatic |
| 3 | Remove unused options | Semi-automatic |
| 4 | Auto-default for dominant choices | Automatic (with undo) |
| 5 | Context-aware ordering | Automatic |
| 6 | Time-based adaptation | Automatic |
| 7 | Fatigue detection | Automatic |
| 8 | A/B testing framework | Semi-automatic |

The key insight: menus aren't static. They should evolve based on how users actually interact with them. The context registry provides the data; you provide the optimization logic.

---

## Future Directions

This system enables several advanced capabilities:

**Predictive Loading**: Use workflow patterns to pre-load likely skills before the user asks. If `research -> hugo` happens 89% of the time, start loading hugo metadata when research completes.

**Cross-Session Learning**: When a user corrects the agent, store that as a `learned-pattern` in Supermemory. Future sessions can retrieve and apply that learning automatically.

**Automated Skill Restructuring**: Skills over 500 lines get flagged for restructuring. The analytics could suggest specific sections to move to Level 3 (reference) vs Level 2 (working).

**Agent Performance Benchmarking**: Compare different agents on similar tasks. If `sisyphus-junior` completes simple file reads 50% faster than `sisyphus`, route more of those tasks that way.

---

## Conclusion

AI agents are powerful tools, but they're also opaque. Without visibility into what they're doing and why, you can't improve them.

Progressive disclosure treats context as a budget, loading only what's needed when it's needed. The context registry captures what happens, learns from patterns, and generates actionable recommendations.

Together, they create a feedback loop: better context management leads to faster execution, which produces more data, which enables better analysis, which drives improvement.

Start with the schema. Add hooks incrementally. Let the data tell you what to optimize.

Your agents will get better. And you'll know why.