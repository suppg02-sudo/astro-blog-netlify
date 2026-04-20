---
pubDatetime: 2026-02-25T10:00:00Z
title: "Ingenious Integrations: Homepage, OpenCode, OliveTin & Astro"
postSlug: "ingenious-integrations-homepage-opencode-olivetin-astro"
description: "Creative ideas for integrating your Homepage dashboard, OpenCode CLI/API, OliveTin command runner, and Astro blog into a unified automation powerhouse."
tags:
  - homepage
  - opencode
  - integration
  - automation
  - astro
  - dashboard
  - ai
  - olivetin
---

What if your dashboard could talk to your AI assistant? What if a button click could trigger an AI skill, publish a blog post, or analyze your entire infrastructure? This post explores **ingenious integration ideas** that connect your Homepage dashboard, OpenCode CLI, OliveTin command runner, and Astro blog into a cohesive automation ecosystem.

## The Four Pillars

Before diving into integrations, let's understand what each tool brings to the table:

| Tool | Superpower | Port | Key Feature |
|------|------------|------|-------------|
| **Homepage** | Visual dashboard | 8765 | Custom widgets, API displays, service links |
| **OpenCode** | AI-powered CLI | 4096 (web) | `opencode run`, skills, headless mode |
| **OliveTin** | Command buttons | 1337 | Shell scripts as clickable actions |
| **Astro** | Static blog | 1314 | Markdown posts, instant deployment |

## Integration Architecture

{{< mermaid >}}
graph TB
    subgraph "User Interface Layer"
        HP[Homepage Dashboard<br/>Port 8765]
        OT[OliveTin<br/>Port 1337]
        AB[Astro Blog<br/>Port 1314]
    end
    
    subgraph "AI & Automation Layer"
        OC[OpenCode CLI/API<br/>Port 4096]
        SK[OpenCode Skills]
        OM[OpenMemory]
    end
    
    subgraph "Infrastructure Layer"
        DK[Docker]
        FS[Filesystem]
        CR[Cron Jobs]
    end
    
    HP -->|Custom API| OC
    HP -->|Custom Widgets| OM
    OT -->|Shell Commands| OC
    OT -->|Docker| DK
    OC -->|Skills| SK
    OC -->|Publish| AB
    SK -->|Actions| FS
    CR -->|Scheduled| OT
{{< /mermaid >}}

---

## Integration Idea #1: Homepage AI Command Widget

**Concept**: Add a text input field directly on your Homepage dashboard that sends prompts to OpenCode and displays the response.

### Implementation

Homepage supports **custom HTML widgets** via the `custom` widget type. Create an HTML file that POSTs to OpenCode's headless endpoint:

```html
<!-- /media/docker/homepage/config/custom/ai-widget.html -->
<div class="ai-command-widget">
  <h3>🤖 Ask OpenCode</h3>
  <form id="ai-form">
    <input type="text" id="ai-prompt" placeholder="Enter your prompt..." style="width: 100%; padding: 8px;">
    <button type="submit" style="margin-top: 8px; padding: 8px 16px; background: #4CAF50; color: white; border: none; cursor: pointer;">
      Execute
    </button>
  </form>
  <div id="ai-response" style="margin-top: 10px; padding: 10px; background: #1a1a1a; border-radius: 4px; min-height: 50px;"></div>
</div>

<script>
document.getElementById('ai-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const prompt = document.getElementById('ai-prompt').value;
  const responseDiv = document.getElementById('ai-response');
  responseDiv.innerHTML = '<em>Processing...</em>';
  
  // Call OpenCode in headless mode
  const result = await fetch('http://ubuntu58-1:4096/api/execute', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt, agent: 'sisyphus' })
  });
  
  const data = await result.json();
  responseDiv.innerHTML = data.response || data.error;
});
</script>
```

Add to `widgets.yaml`:

```yaml
- custom:
    name: AI Command
    file: custom/ai-widget.html
```

### Use Cases
- Quick code questions without opening terminal
- Natural language Docker commands ("restart the blog container")
- System status queries in plain English

---

## Integration Idea #2: OliveTin OpenCode Skill Launcher

**Concept**: Create clickable buttons in OliveTin that trigger specific OpenCode skills.

### Implementation

Add actions to `/media/docker/olivetin/config/config.yaml`:

```yaml
actions:
  # OpenCode Skill Triggers
  - title: "📝 Create Blog Post"
    icon: edit
    shell: |
      cd /media/docker/website && \
      opencode run "Create a blog post about the latest Docker container statistics from the last 24 hours. Include charts if relevant." \
        --agent document-writer
    id: createBlogPost
    description: Generate a blog post from system statistics
    timeout: 300

  - title: "🔍 Analyze Logs"
    icon: search
    shell: |
      opencode run "Analyze the last 100 lines of Docker logs from all containers and summarize any errors or warnings" \
        --agent explore
    id: analyzeLogs
    description: AI-powered log analysis
    timeout: 120

  - title: "📊 System Health Report"
    icon: assessment
    shell: |
      opencode run "Generate a comprehensive system health report including disk usage, memory, running containers, and recent errors. Save to /media/docs/output/health-report-$(date +%Y%m%d).md" \
        --agent sisyphus
    id: healthReport
    description: Generate AI health report
    timeout: 180

  - title: "🧠 Store to Memory"
    icon: brain
    shell: |
      opencode run "Store today's important events and configurations to OpenMemory with tags: daily, infrastructure" \
        --agent librarian
    id: storeMemory
    description: Save daily state to persistent memory
    timeout: 60

  - title: "🚀 Deploy Latest Changes"
    icon: rocket
    shell: |
      cd /media/docker/website && \
      git pull && \
      opencode run "Validate the Hugo build and restart the container if successful" \
        --agent sisyphus && \
      docker restart hugo-blog
    id: deployChanges
    description: Pull and deploy latest blog changes
    timeout: 120
```

### Visual Result

Your OliveTin dashboard becomes an AI command center:

```
┌─────────────────────────────────────┐
│  🤖 OpenCode Actions                │
├─────────────────────────────────────┤
│  [📝 Create Blog Post]              │
│  [🔍 Analyze Logs]                  │
│  [📊 System Health Report]          │
│  [🧠 Store to Memory]               │
│  [🚀 Deploy Latest Changes]         │
└─────────────────────────────────────┘
```

---

## Integration Idea #3: Homepage OpenMemory Widget

**Concept**: Display your recent memories and AI learnings directly on the dashboard.

### Implementation

OpenMemory has a REST API. Add a custom API widget to Homepage:

```yaml
# widgets.yaml
- customapi:
    url: http://ubuntu58-1:8080/api/memories/recent?limit=5
    title: 🧠 Recent Memories
    mappings:
      - field: memories
        label: Latest
        format: list
```

For more control, create a custom HTML widget:

```html
<!-- /media/docker/homepage/config/custom/memory-widget.html -->
<div class="memory-widget">
  <h3>🧠 Recent AI Memories</h3>
  <div id="memories-list"></div>
</div>

<script>
async function loadMemories() {
  const response = await fetch('http://ubuntu58-1:8080/api/memories/recent?limit=5');
  const data = await response.json();
  const list = document.getElementById('memories-list');
  
  list.innerHTML = data.memories.map(m => `
    <div style="padding: 8px; margin: 4px 0; background: #2a2a2a; border-radius: 4px; font-size: 12px;">
      <strong>${m.tags?.join(', ') || 'memory'}</strong>
      <p style="margin: 4px 0; color: #aaa;">${m.content.substring(0, 100)}...</p>
    </div>
  `).join('');
}

loadMemories();
setInterval(loadMemories, 60000); // Refresh every minute
</script>
```

---

## Integration Idea #4: Astro Blog Auto-Publish via Webhook

**Concept**: Create a webhook endpoint that triggers blog post creation from external sources.

### Implementation

Create a small webhook server that receives content and triggers OpenCode:

```python
# /media/docker/webhook-server/publish_hook.py
from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/webhook/publish', methods=['POST'])
def publish_blog():
    data = request.json
    
    # Required fields
    title = data.get('title')
    content = data.get('content')
    tags = data.get('tags', ['auto-published'])
    
    if not title or not content:
        return jsonify({'error': 'Missing title or content'}), 400
    
    # Trigger OpenCode to create and validate the post
    prompt = f"""
    Create a Hugo blog post with:
    Title: {title}
    Tags: {tags}
    Content: {content}
    
    Save to /media/docker/website/content/posts/ with proper frontmatter.
    Validate the build succeeds.
    """
    
    result = subprocess.run(
        ['opencode', 'run', prompt, '--agent', 'document-writer'],
        capture_output=True,
        text=True,
        cwd='/media/docker/website'
    )
    
    return jsonify({
        'status': 'success' if result.returncode == 0 else 'error',
        'output': result.stdout,
        'error': result.stderr
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8766)
```

Add to OliveTin for manual triggering:

```yaml
- title: "📢 Publish Draft Post"
  icon: publish
  shell: |
    curl -X POST http://ubuntu58-1:8766/webhook/publish \
      -H "Content-Type: application/json" \
      -d @/media/docker/drafts/latest-draft.json
  id: publishDraft
  description: Publish the latest draft post
```

---

## Integration Idea #5: Homepage Service Health AI Monitor

**Concept**: Homepage displays service health, but what if it could also show AI-analyzed insights?

### Implementation

Create a cron job that runs AI analysis and stores results:

```bash
# /etc/cron.d/ai-health-monitor
*/30 * * * * root opencode run "Analyze the health of all services listed in Homepage. Check ports, response times, and recent errors. Generate a JSON status file at /var/cache/service-health.json with scores and recommendations." --agent sisyphus
```

Add widget to Homepage:

```yaml
- customapi:
    url: file:///var/cache/service-health.json
    title: 🩺 AI Health Analysis
    mappings:
      - field: overall_score
        label: Health Score
      - field: recommendations
        label: AI Recommendations
        format: list
```

---

## Integration Idea #6: Interactive Blog Feedback Loop

**Concept**: Add a Homepage widget that lets visitors submit blog topic suggestions, which automatically create tasks for OpenCode.

### Implementation

```html
<!-- /media/docker/homepage/config/custom/blog-suggest.html -->
<div class="blog-suggestion-widget">
  <h3>💡 Suggest a Blog Topic</h3>
  <form id="suggest-form">
    <input type="text" id="topic" placeholder="What should I write about?" style="width: 100%; padding: 8px;">
    <textarea id="details" placeholder="Additional details..." style="width: 100%; padding: 8px; margin-top: 8px; height: 60px;"></textarea>
    <button type="submit" style="margin-top: 8px; padding: 8px 16px; background: #2196F3; color: white; border: none; cursor: pointer;">
      Submit Suggestion
    </button>
  </form>
  <p id="suggest-status" style="margin-top: 8px; font-size: 12px;"></p>
</div>

<script>
document.getElementById('suggest-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const topic = document.getElementById('topic').value;
  const details = document.getElementById('details').value;
  const status = document.getElementById('suggest-status');
  
  // Store to OpenMemory as a task
  const response = await fetch('http://ubuntu58-1:8080/api/memories', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      content: `Blog Suggestion: ${topic}\nDetails: ${details}`,
      tags: ['blog-suggestion', 'user-request', 'pending'],
      sector: 'semantic'
    })
  });
  
  if (response.ok) {
    status.innerHTML = '✅ Suggestion saved! I\'ll consider it for future posts.';
    document.getElementById('topic').value = '';
    document.getElementById('details').value = '';
  } else {
    status.innerHTML = '❌ Failed to save suggestion.';
  }
});
</script>
```

---

## Integration Idea #7: OliveTin Chain Reactions

**Concept**: Single button that triggers a sequence of actions across multiple services.

### Implementation

```yaml
# OliveTin config
actions:
  - title: "🌅 Morning Routine"
    icon: wb_sunny
    shell: |
      # 1. Pull latest changes
      cd /media/docker/website && git pull
      
      # 2. Generate daily summary
      opencode run "Create a daily summary of system events, container restarts, and errors from the last 24 hours. Save as /media/docs/output/daily-summary-$(date +%Y%m%d).md" --agent sisyphus
      
      # 3. Store memory snapshot
      opencode run "Store yesterday's key events and learnings to OpenMemory with tags: daily, routine" --agent librarian
      
      # 4. Restart stale containers
      docker restart homepage hugo-blog
      
      # 5. Notify
      echo "Morning routine complete at $(date)" >> /var/log/morning-routine.log
    id: morningRoutine
    description: Run morning automation sequence
    timeout: 300

  - title: "🌙 Night Mode"
    icon: bedtime
    shell: |
      # Backup critical data
      opencode run "Backup all important configuration files and databases. Store metadata in OpenMemory." --agent sisyphus
      
      # Generate tomorrow's task list
      opencode run "Review OpenMemory for pending tasks and generate tomorrow's priority list" --agent librarian
      
      # Clean up temp files
      rm -rf /tmp/*.tmp 2>/dev/null
      
      # Log completion
      echo "Night mode complete at $(date)" >> /var/log/night-mode.log
    id: nightMode
    description: Run end-of-day automation
    timeout: 180
```

---

## Integration Idea #8: Cross-Service URL Dashboard

**Concept**: Generate a dynamic URL page that aggregates all your services with AI-enhanced descriptions.

### Implementation

Create an OliveTin action that generates an Astro page:

```yaml
- title: "🔗 Generate URL Hub"
  icon: link
  shell: |
    opencode run "
    1. Scan all running Docker containers and their port mappings
    2. Query Homepage services.yaml for service metadata
    3. Check each service's health endpoint
    4. Generate a beautiful Astro page at /hub/ with:
       - Service cards with status indicators
       - Quick action buttons
       - AI-generated descriptions for each service
    5. Save to /media/docker/astro-fresh/src/pages/hub.astro
    " --agent frontend-ui-ux-engineer
  id: generateUrlHub
  description: Generate interactive service hub page
  timeout: 180
```

---

## Integration Idea #9: AI-Powered Log Triage

**Concept**: When errors occur, automatically analyze and suggest fixes.

### Implementation

```yaml
# OliveTin
- title: "🚨 Triage Errors"
  icon: emergency
  shell: |
    # Get recent errors
    ERRORS=$(journalctl -p err -n 20 --no-pager)
    DOCKER_ERRORS=$(docker logs --tail 50 $(docker ps -q) 2>&1 | grep -i error || true)
    
    opencode run "
    Analyze these system and Docker errors:
    
    SYSTEM ERRORS:
    $ERRORS
    
    DOCKER ERRORS:
    $DOCKER_ERRORS
    
    For each error:
    1. Identify the root cause
    2. Suggest a fix
    3. Rate severity (1-5)
    4. Recommend immediate action if critical
    
    Save results to /media/docs/output/error-triage-$(date +%Y%m%d-%H%M).md
    " --agent sisyphus
  id: triageErrors
  description: AI-powered error analysis
  timeout: 120
```

---

## Integration Idea #10: Smart Blog Metrics Dashboard

**Concept**: Display blog statistics with AI insights on Homepage.

### Implementation

```yaml
# widgets.yaml
- customapi:
    url: http://ubuntu58-1:1314/api/stats.json
    title: 📊 Blog Metrics
    mappings:
      - field: total_posts
        label: Total Posts
      - field: words_written
        label: Words Written
      - field: avg_read_time
        label: Avg Read Time
```

Create a cron job to generate the stats:

```bash
# Generate blog stats hourly
0 * * * * root opencode run "Analyze all blog posts in /media/docker/website/content/posts/ and generate statistics: post count, word count, reading time, top tags, recent activity. Save JSON to /media/docker/astro-fresh/public/api/stats.json" --agent librarian
```

---

## Complete Integration Diagram

{{< mermaid >}}
flowchart LR
    subgraph Inputs
        A[User Input]
        B[Webhook]
        C[Schedule/Cron]
        D[Homepage Widget]
    end
    
    subgraph Processing
        E[OliveTin<br/>Button Press]
        F[OpenCode<br/>AI Processing]
        G[Skills<br/>Specialized Actions]
    end
    
    subgraph Outputs
        H[Astro Blog<br/>Published Post]
        I[OpenMemory<br/>Stored Knowledge]
        J[Homepage<br/>Updated Widget]
        K[Reports<br/>Generated Files]
    end
    
    A --> E
    B --> F
    C --> E
    D --> F
    E --> F
    F --> G
    G --> H
    G --> I
    G --> J
    G --> K
{{< /mermaid >}}

---

## Quick Start Implementation

Want to get started immediately? Here's a minimal setup:

### Step 1: Add Basic OliveTin Actions

```bash
cat >> /media/docker/olivetin/config/config.yaml << 'EOF'

  # OpenCode Integration
  - title: "🤖 Quick AI Task"
    icon: smart_toy
    shell: opencode run "Help me with a quick task" --agent sisyphus
    id: quickAITask
    description: Launch OpenCode for quick assistance
EOF

docker restart olivetin
```

### Step 2: Add Homepage Memory Widget

```bash
cat >> /media/docker/homepage/config/widgets.yaml << 'EOF'

- customapi:
    url: http://ubuntu58-1:8080/health
    title: 🧠 OpenMemory
    mappings:
      - field: status
        label: Memory Status
EOF

docker restart homepage
```

### Step 3: Test the Integration

```bash
# Via OliveTin: Click "🤖 Quick AI Task"
# Via Homepage: View the OpenMemory widget
# Via Terminal: opencode run "Summarize the integration between Homepage, OliveTin, and this system"
```

---

## Conclusion

The combination of **Homepage** (visual interface), **OpenCode** (AI intelligence), **OliveTin** (action execution), and **Astro** (content publishing) creates a powerful automation ecosystem. Each tool amplifies the others:

- Homepage becomes an **AI command center**
- OliveTin becomes a **skill launcher**
- OpenCode becomes a **universal connector**
- Astro becomes an **AI-powered publishing platform**

The key insight is that these tools don't just coexist—they **orchestrate** each other. A button click can trigger AI analysis, which can publish content, which updates the dashboard, which displays new metrics. It's a living, breathing automation system that learns and improves over time.

**What integration will you build first?**

---

*Published: February 25, 2026 | Tags: integration, automation, homepage, opencode, olivetin, astro, dashboard, ai*