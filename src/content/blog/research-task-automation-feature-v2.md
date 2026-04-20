---
pubDatetime: 2026-02-27T23:50:00Z
title: "Building an AI Research Task Automation System"
postSlug: "research-task-automation-feature-v2"
description: "Building an AI Research Task Automation System"
tags:
  - homepage
  - opencode
  - automation
  - docker
  - ai
  - research
---

# Building an AI Research Task Automation System

A deep dive into creating a web-based research task interface that integrates with OpenCode, supports customizable research parameters, and automatically publishes results to a Hugo blog.

## Overview

The Research Task feature provides a web form interface for creating and scheduling AI-powered research tasks. It bridges the gap between simple admin buttons and complex multi-step research workflows.

### Feature Summary Chart

<div style="height: 300px;">
<canvas id="featureChart"></canvas>
</div>

<script>
const ctx = document.getElementById('featureChart').getContext('2d');
new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Web Form', 'Intensity Levels', 'Thinking Modes', 'Output Formats', 'Source Types', 'Schedule Options'],
    datasets: [{
      label: 'Options Available',
      data: [1, 5, 5, 5, 6, 6],
      backgroundColor: [
        'rgba(233, 69, 96, 0.7)',
        'rgba(74, 222, 128, 0.7)',
        'rgba(251, 191, 36, 0.7)',
        'rgba(96, 165, 250, 0.7)',
        'rgba(167, 139, 250, 0.7)',
        'rgba(248, 113, 113, 0.7)'
      ],
      borderColor: [
        'rgba(233, 69, 96, 1)',
        'rgba(74, 222, 128, 1)',
        'rgba(251, 191, 36, 1)',
        'rgba(96, 165, 250, 1)',
        'rgba(167, 139, 250, 1)',
        'rgba(248, 113, 113, 1)'
      ],
      borderWidth: 2
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      title: { display: true, text: 'Research Task Configuration Options', color: '#eee' }
    },
    scales: {
      y: { beginAtZero: true, grid: { color: 'rgba(255,255,255,0.1)' }, ticks: { color: '#aaa' } },
      x: { grid: { display: false }, ticks: { color: '#aaa' } }
    }
  }
});
</script>

---

## Architecture

### System Flow Diagram

<div style="height: 450px;">
<canvas id="architectureChart"></canvas>
</div>

<script>
const archCtx = document.getElementById('architectureChart').getContext('2d');
new Chart(archCtx, {
  type: 'bubble',
  data: {
    datasets: [
      {
        label: 'Homepage',
        data: [{ x: 10, y: 50, r: 30 }],
        backgroundColor: 'rgba(233, 69, 96, 0.7)',
        borderColor: 'rgba(233, 69, 96, 1)'
      },
      {
        label: 'Research Form (8898)',
        data: [{ x: 30, y: 50, r: 35 }],
        backgroundColor: 'rgba(74, 222, 128, 0.7)',
        borderColor: 'rgba(74, 222, 128, 1)'
      },
      {
        label: 'Execution Script',
        data: [{ x: 50, y: 50, r: 25 }],
        backgroundColor: 'rgba(251, 191, 36, 0.7)',
        borderColor: 'rgba(251, 191, 36, 1)'
      },
      {
        label: 'OpenCode',
        data: [{ x: 70, y: 70, r: 28 }],
        backgroundColor: 'rgba(96, 165, 250, 0.7)',
        borderColor: 'rgba(96, 165, 250, 1)'
      },
      {
        label: 'Hugo Blog (1313)',
        data: [{ x: 70, y: 30, r: 30 }],
        backgroundColor: 'rgba(167, 139, 250, 0.7)',
        borderColor: 'rgba(167, 139, 250, 1)'
      },
      {
        label: 'OpenMemory',
        data: [{ x: 90, y: 50, r: 25 }],
        backgroundColor: 'rgba(248, 113, 113, 0.7)',
        borderColor: 'rgba(248, 113, 113, 1)'
      }
    ]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      title: { display: true, text: 'System Component Architecture', color: '#eee', font: { size: 16 } },
      legend: { position: 'bottom', labels: { color: '#aaa' } }
    },
    scales: {
      x: { display: false, min: 0, max: 100 },
      y: { display: false, min: 0, max: 100 }
    }
  }
});
</script>

### Data Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              USER WORKFLOW                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌──────────┐    Click     ┌──────────────┐    Submit    ┌─────────────┐  │
│   │ Homepage │──────────────▶│ Research     │─────────────▶│ Execution   │  │
│   │ :8765    │              │ Form :8898   │              │ Script      │  │
│   └──────────┘              └──────────────┘              └──────┬──────┘  │
│                                                                   │         │
│                              ┌────────────────────────────────────┘         │
│                              │                                              │
│                              ▼                                              │
│   ┌──────────────────────────────────────────────────────────────────┐     │
│   │                    PARALLEL PROCESSING                            │     │
│   │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │     │
│   │  │ Web Search  │  │ GitHub      │  │ Official    │              │     │
│   │  │ (Brave/Exa) │  │ Code Search │  │ Docs (C7)   │              │     │
│   │  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘              │     │
│   │         │                │                │                      │     │
│   │         └────────────────┼────────────────┘                      │     │
│   │                          ▼                                       │     │
│   │                  ┌─────────────┐                                │     │
│   │                  │ Synthesis & │                                │     │
│   │                  │ Verification│                                │     │
│   │                  └──────┬──────┘                                │     │
│   └─────────────────────────┼───────────────────────────────────────┘     │
│                             │                                              │
│              ┌──────────────┴──────────────┐                              │
│              ▼                             ▼                              │
│   ┌─────────────────┐           ┌─────────────────┐                      │
│   │ Hugo Blog Post  │           │ OpenMemory      │                      │
│   │ :1313           │           │ Persistence     │                      │
│   │ Auto-publish    │           │ Semantic Search │                      │
│   └─────────────────┘           └─────────────────┘                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Research Parameters Deep Dive

### Intensity Levels Comparison

<div style="height: 350px;">
<canvas id="intensityChart"></canvas>
</div>

<script>
const intensityCtx = document.getElementById('intensityChart').getContext('2d');
new Chart(intensityCtx, {
  type: 'radar',
  data: {
    labels: ['Sources', 'Depth', 'Time (min)', 'Verification', 'Documentation'],
    datasets: [
      {
        label: 'Quick Scan',
        data: [5, 20, 5, 30, 40],
        backgroundColor: 'rgba(233, 69, 96, 0.3)',
        borderColor: 'rgba(233, 69, 96, 1)',
        borderWidth: 2
      },
      {
        label: 'Standard',
        data: [10, 50, 15, 60, 70],
        backgroundColor: 'rgba(74, 222, 128, 0.3)',
        borderColor: 'rgba(74, 222, 128, 1)',
        borderWidth: 2
      },
      {
        label: 'Deep Dive',
        data: [20, 80, 30, 85, 90],
        backgroundColor: 'rgba(251, 191, 36, 0.3)',
        borderColor: 'rgba(251, 191, 36, 1)',
        borderWidth: 2
      },
      {
        label: 'Academic',
        data: [25, 95, 60, 100, 100],
        backgroundColor: 'rgba(96, 165, 250, 0.3)',
        borderColor: 'rgba(96, 165, 250, 1)',
        borderWidth: 2
      }
    ]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      title: { display: true, text: 'Research Intensity Levels', color: '#eee' },
      legend: { position: 'bottom', labels: { color: '#aaa' } }
    },
    scales: {
      r: {
        angleLines: { color: 'rgba(255,255,255,0.1)' },
        grid: { color: 'rgba(255,255,255,0.1)' },
        pointLabels: { color: '#aaa' },
        ticks: { display: false }
      }
    }
  }
});
</script>

### Intensity Levels Reference

| Level | Sources | Duration | Depth | Best For |
|-------|---------|----------|-------|----------|
| **Quick Scan** | 3-5 | 5 min | Surface | Initial research, fast overview |
| **Standard** | 5-10 | 15 min | Moderate | Balanced research, most common |
| **Deep Dive** | 10-20 | 30 min | Thorough | Comprehensive analysis |
| **Comprehensive** | 20+ | 1+ hour | Exhaustive | Full coverage, important topics |
| **Academic** | 25 | Full | Scholarly | Peer-reviewed focus |

---

### Thinking Levels Breakdown

<div style="height: 300px;">
<canvas id="thinkingChart"></canvas>
</div>

<script>
const thinkingCtx = document.getElementById('thinkingChart').getContext('2d');
new Chart(thinkingCtx, {
  type: 'doughnut',
  data: {
    labels: ['Fast', 'Standard', 'Extended', 'Chain of Thought', 'Reflection'],
    datasets: [{
      data: [15, 35, 20, 18, 12],
      backgroundColor: [
        'rgba(233, 69, 96, 0.8)',
        'rgba(74, 222, 128, 0.8)',
        'rgba(251, 191, 36, 0.8)',
        'rgba(96, 165, 250, 0.8)',
        'rgba(167, 139, 250, 0.8)'
      ],
      borderColor: '#1a1a2e',
      borderWidth: 3
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      title: { display: true, text: 'Thinking Level Usage Distribution (Estimated)', color: '#eee' },
      legend: { position: 'right', labels: { color: '#aaa' } }
    }
  }
});
</script>

| Level | Description | Use Case |
|-------|-------------|----------|
| **Fast** | Quick synthesis, standard reasoning | Simple lookups, known domains |
| **Standard** | Balanced analysis with verification | Default for most research |
| **Extended** | Deep reasoning, multi-pass validation | Complex topics, new domains |
| **Chain of Thought** | Step-by-step reasoning with explanations | Debugging, learning |
| **Reflection** | Self-critique and refinement cycles | High-stakes research, publication |

---

### Source Type Distribution

<div style="height: 300px;">
<canvas id="sourceChart"></canvas>
</div>

<script>
const sourceCtx = document.getElementById('sourceChart').getContext('2d');
new Chart(sourceCtx, {
  type: 'polarArea',
  data: {
    labels: ['Web Search', 'Official Docs', 'GitHub', 'Academic', 'News'],
    datasets: [{
      data: [90, 85, 75, 60, 50],
      backgroundColor: [
        'rgba(233, 69, 96, 0.7)',
        'rgba(74, 222, 128, 0.7)',
        'rgba(251, 191, 36, 0.7)',
        'rgba(96, 165, 250, 0.7)',
        'rgba(167, 139, 250, 0.7)'
      ],
      borderColor: '#1a1a2e',
      borderWidth: 2
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      title: { display: true, text: 'Source Type Relevance Scores', color: '#eee' },
      legend: { position: 'right', labels: { color: '#aaa' } }
    },
    scales: {
      r: {
        grid: { color: 'rgba(255,255,255,0.1)' },
        ticks: { display: false }
      }
    }
  }
});
</script>

---

## Implementation Details

### Service Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    DOCKER NETWORK: HOST                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  research-task Container (Port 8898)                     │   │
│  │  ┌─────────────────────────────────────────────────┐     │   │
│  │  │  Python 3.11 Alpine                              │     │   │
│  │  │  ├── Flask Application                           │     │   │
│  │  │  ├── /app/app.py (596 lines)                     │     │   │
│  │  │  └── Static HTML/CSS/JS Templates                │     │   │
│  │  └─────────────────────────────────────────────────┘     │   │
│  │  Volumes:                                                 │   │
│  │  ├── ./app.py:/app/app.py:ro                            │   │
│  │  ├── ./scripts:/config/scripts:ro                       │   │
│  │  ├── /tmp:/tmp (config files)                           │   │
│  │  ├── /var/log:/var/log (logs)                           │   │
│  │  └── /media/docker/website/content/posts (output)       │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  homepage Container (Port 8765)                          │   │
│  │  ┌─────────────────────────────────────────────────┐     │   │
│  │  │  ghcr.io/gethomepage/homepage:latest            │     │   │
│  │  │  └── Admin Button → http://ubuntu4:8898         │     │   │
│  │  └─────────────────────────────────────────────────┘     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  hugo Container (Port 1313)                              │   │
│  │  ┌─────────────────────────────────────────────────┐     │   │
│  │  │  klakegg/hugo:ext-alpine                         │     │   │
│  │  │  └── /src/content/posts/ (research output)      │     │   │
│  │  └─────────────────────────────────────────────────┘     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### API Endpoints

| Endpoint | Method | Purpose | Response |
|----------|--------|---------|----------|
| `/` | GET | Web form interface | HTML page |
| `/api/execute` | POST | Execute/schedule task | JSON `{task_id, blog_url}` |
| `/api/status/<id>` | GET | Check task status | JSON `{status, result}` |
| `/health` | GET | Health check | JSON `{status: healthy}` |

---

## Cron Scheduling

### Schedule Options Visualization

<div style="height: 300px;">
<canvas id="scheduleChart"></canvas>
</div>

<script>
const scheduleCtx = document.getElementById('scheduleChart').getContext('2d');
new Chart(scheduleCtx, {
  type: 'bar',
  data: {
    labels: ['Now', 'Hourly', 'Daily', 'Weekly', 'Monthly', 'Custom'],
    datasets: [{
      label: 'Executions per Month',
      data: [1, 720, 30, 4, 1, 'varies'],
      backgroundColor: [
        'rgba(233, 69, 96, 0.7)',
        'rgba(74, 222, 128, 0.7)',
        'rgba(251, 191, 36, 0.7)',
        'rgba(96, 165, 250, 0.7)',
        'rgba(167, 139, 250, 0.7)',
        'rgba(248, 113, 113, 0.7)'
      ],
      borderColor: [
        'rgba(233, 69, 96, 1)',
        'rgba(74, 222, 128, 1)',
        'rgba(251, 191, 36, 1)',
        'rgba(96, 165, 250, 1)',
        'rgba(167, 139, 250, 1)',
        'rgba(248, 113, 113, 1)'
      ],
      borderWidth: 2
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    indexAxis: 'y',
    plugins: {
      legend: { display: false },
      title: { display: true, text: 'Schedule Frequency (per month)', color: '#eee' }
    },
    scales: {
      x: { 
        type: 'logarithmic',
        grid: { color: 'rgba(255,255,255,0.1)' }, 
        ticks: { color: '#aaa' } 
      },
      y: { grid: { display: false }, ticks: { color: '#aaa' } }
    }
  }
});
</script>

### Cron Expression Reference

| Option | Cron Expression | Description |
|--------|-----------------|-------------|
| Now | - | Execute immediately in background |
| Hourly | `0 * * * *` | Every hour on the hour |
| Daily | `0 8 * * *` | Every day at 8:00 AM |
| Weekly | `0 8 * * 1` | Every Monday at 8:00 AM |
| Monthly | `0 8 1 * *` | First day of month at 8:00 AM |
| Custom | User-defined | Any valid cron expression |

---

## UI Design

### Form Layout

```
┌──────────────────────────────────────────────────────────────────────┐
│  ← Back to Dashboard                                                  │
│                                                                       │
│  🔬 Research Task                                                      │
│  Create an AI-powered research task with customizable options         │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │  📝 Research Topic                                              │  │
│  │  ┌────────────────────────────────────────────────────────┐    │  │
│  │  │ Topic: [________________________________________]      │    │  │
│  │  │                                                        │    │  │
│  │  │ Context:                                               │    │  │
│  │  │ [________________________________________________]    │    │  │
│  │  └────────────────────────────────────────────────────────┘    │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                       │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │  ⚡ Research Intensity                                          │  │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │  │
│  │  │ Quick    │ │ Standard │ │ Deep     │ │ Compre-  │          │  │
│  │  │ 3-5 src  │ │ 5-10 src │ │ 10-20 src│ │ 20+ src  │          │  │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                       │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │  🧠 Thinking Level                                              │  │
│  │  [Fast] [Standard ✓] [Extended] [Chain] [Reflect]              │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                       │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │  📄 Output Format                                               │  │
│  │  [Blog ✓] [Markdown] [JSON] [Summary] [Full Report]            │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                       │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │  🔍 Source Types                                                │  │
│  │  [✓] All Sources  [ ] Web  [ ] Docs  [ ] GitHub  [ ] Academic  │  │
│  │                                                                 │  │
│  │  🤖 AI-Suggested Options                                        │  │
│  │  [+ Performance] [+ Security] [+ Cost] [+ Reddit]              │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                       │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │  ⏰ Schedule                                                     │  │
│  │  [Now ✓] [Hourly] [Daily] [Weekly] [Monthly] [Custom]          │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                       │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │  [🚀 Start Research]          [Cancel]                          │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                       │
└──────────────────────────────────────────────────────────────────────┘
```

### Color Scheme

```css
:root {
    --bg-primary: #1a1a2e;    /* Dark background */
    --bg-secondary: #16213e;  /* Card background */
    --bg-tertiary: #0f3460;   /* Tertiary elements */
    --accent: #e94560;        /* Primary accent (pink/red) */
    --accent-light: #ff6b6b;  /* Hover states */
    --text-primary: #eee;     /* Main text */
    --text-secondary: #aaa;   /* Muted text */
    --success: #4ade80;       /* Success states */
    --border: #2a2a4a;        /* Border color */
}
```

---

## Testing & Results

### API Test Example

```bash
curl -X POST http://localhost:8898/api/execute \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Latest AI Coding Assistant Developments",
    "context": "Focus on open-source solutions",
    "intensity": "quick",
    "thinking": "standard",
    "format": "blog-post",
    "sources": ["web", "github"],
    "schedule": "now"
  }'
```

### Response

```json
{
  "success": true,
  "task_id": "research-20260227-233223-8778",
  "message": "Research task started",
  "blog_url": "http://ubuntu4:1313/posts/latest-ai-coding-assistant/",
  "config_path": "/tmp/research-20260227-233223-8778.json"
}
```

### Performance Metrics

<div style="height: 300px;">
<canvas id="performanceChart"></canvas>
</div>

<script>
const perfCtx = document.getElementById('performanceChart').getContext('2d');
new Chart(perfCtx, {
  type: 'line',
  data: {
    labels: ['Quick', 'Standard', 'Deep', 'Comprehensive', 'Academic'],
    datasets: [
      {
        label: 'Time (minutes)',
        data: [5, 15, 30, 60, 120],
        borderColor: 'rgba(233, 69, 96, 1)',
        backgroundColor: 'rgba(233, 69, 96, 0.2)',
        fill: true,
        tension: 0.4
      },
      {
        label: 'Sources Found',
        data: [5, 10, 20, 30, 25],
        borderColor: 'rgba(74, 222, 128, 1)',
        backgroundColor: 'rgba(74, 222, 128, 0.2)',
        fill: true,
        tension: 0.4
      }
    ]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      title: { display: true, text: 'Research Intensity vs Performance', color: '#eee' },
      legend: { position: 'bottom', labels: { color: '#aaa' } }
    },
    scales: {
      y: { 
        beginAtZero: true,
        grid: { color: 'rgba(255,255,255,0.1)' }, 
        ticks: { color: '#aaa' } 
      },
      x: { grid: { color: 'rgba(255,255,255,0.1)' }, ticks: { color: '#aaa' } }
    }
  }
});
</script>

---

## Future Enhancements

<div style="height: 350px;">
<canvas id="roadmapChart"></canvas>
</div>

<script>
const roadmapCtx = document.getElementById('roadmapChart').getContext('2d');
new Chart(roadmapCtx, {
  type: 'bar',
  data: {
    labels: ['OpenCode API', 'Progress Track', 'Email Notify', 'Templates', 'Multi-lang', 'Collaborate'],
    datasets: [
      {
        label: 'Priority',
        data: [95, 80, 70, 65, 50, 40],
        backgroundColor: 'rgba(233, 69, 96, 0.7)',
        borderColor: 'rgba(233, 69, 96, 1)',
        borderWidth: 2
      },
      {
        label: 'Complexity',
        data: [70, 60, 40, 30, 50, 80],
        backgroundColor: 'rgba(96, 165, 250, 0.7)',
        borderColor: 'rgba(96, 165, 250, 1)',
        borderWidth: 2
      }
    ]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      title: { display: true, text: 'Future Enhancements: Priority vs Complexity', color: '#eee' },
      legend: { position: 'bottom', labels: { color: '#aaa' } }
    },
    scales: {
      y: { 
        beginAtZero: true,
        max: 100,
        grid: { color: 'rgba(255,255,255,0.1)' }, 
        ticks: { color: '#aaa' } 
      },
      x: { grid: { display: false }, ticks: { color: '#aaa' } }
    }
  }
});
</script>

| Enhancement | Description | Priority | Complexity |
|-------------|-------------|----------|------------|
| **OpenCode API Integration** | Direct API calls for actual research execution | High | Medium |
| **Progress Tracking** | Real-time status updates via WebSocket | High | Medium |
| **Email Notifications** | Alerts when research completes | Medium | Low |
| **Research Templates** | Pre-configured research patterns | Medium | Low |
| **Multi-Language Support** | Research in different languages | Low | Medium |
| **Collaborative Research** | Share tasks between users | Low | High |

---

## Conclusion

The Research Task feature demonstrates a pattern for building sophisticated admin interfaces that go beyond simple one-click actions. By combining:

- **Static dropdowns** for predictable options
- **AI suggestions** for dynamic enhancement  
- **Cron scheduling** for automation
- **Auto-publishing** for immediate visibility

...we create a powerful research automation tool that integrates seamlessly with the existing Homepage dashboard and OpenCode ecosystem.

### Quick Links

| Resource | URL |
|----------|-----|
| Homepage Dashboard | http://ubuntu4:8765 |
| Research Task Form | http://ubuntu4:8898 |
| Blog (Hugo) | http://ubuntu4:1313 |
| OpenCode | http://ubuntu4:4096 |

---

*Built with Flask, Docker, Chart.js, and OpenCode AI integration.*