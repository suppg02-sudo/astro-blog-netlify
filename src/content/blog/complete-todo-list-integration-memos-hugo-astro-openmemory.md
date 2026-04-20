---
pubDatetime: 2026-02-03T12:00:00Z
title: "Complete Todo List Integration: Memos + Hugo/Astro + OpenMemory"
postSlug: "complete-todo-list-integration-memos-hugo-astro-openmemory"
description: "Complete Todo List Integration: Memos + Hugo/Astro + OpenMemory"
tags:
  - memory
  - hugo
---

# 📋 Complete Todo List Integration: Memos + Hugo/Astro + OpenMemory

Looking for a checkbox-based todo list with persistent memory? You already have **Memos** running and it's the perfect solution! This guide shows you how to integrate Memos with your Hugo/Astro sites and OpenMemory for a complete, productive workflow system.

**What You'll Get:**
- ✅ Built-in checkbox support with visual feedback
- ✅ Markdown-based todo lists (future-proof, portable)
- ✅ Powerful tagging system (`#work`, `#personal`, `#urgent`, `#high`, etc.)
- ✅ Pinned items to keep important todos at top
- ✅ Memo organizer for project-based organization
- ✅ REST API for Hugo/Astro integration
- ✅ Webhook support for automatic site updates
- ✅ OpenMemory integration for storing decisions and best practices

**Why Memos is Perfect:**
- Already self-hosted and running
- Privacy-first (zero telemetry)
- Full control over your data
- No vendor lock-in
- Works perfectly with your existing environment

___

## 📋 Why Use Memos for Todos?

### Already Installed ✅

**Access Now:** http://ubuntu58-1:5230

**Version:** `neosmemo/memos:stable` (latest stable release)

### Key Features for Todo Lists

| Feature | How It Works | Benefit |
|----------|---------------|---------|
| **Checkboxes** | Markdown format: `- [ ] Task` | Visual completion feedback |
| **Tags** | Add tags: `#work`, `#personal`, `#urgent` | Filter and organize easily |
| **Pinned Items** | Click pin icon to keep at top | Keep critical items visible |
| **Memo Organizer** | Create folders in sidebar | Group related tasks together |
| **Payload Field** | Store JSON metadata | Track completion state, due dates |
| **Visibility** | PUBLIC or PRIVATE | Control access per memo |
| **REST API** | Fetch programmatically | Integrate with Hugo/Astro |

___

## 🏗️ Integration with Hugo/Astro Sites

You have two main options for displaying Memos todos on your static sites:

### Option 1: Real-time API Fetch (Recommended) ⭐

Best for live websites with frequent updates.

**For Hugo Sites:**

Add this JavaScript to any Hugo layout or page:

```html
<!-- Add to your Hugo layouts/partials or content files -->
<script>
const MEMOS_URL = 'http://ubuntu58-1:5230/api/v1';
const MEMOS_TOKEN = 'your-api-token'; // Get from Memos Settings → Access Tokens

async function fetchTodos() {
  try {
    const response = await fetch(`${MEMOS_URL}/memo/list`, {
      headers: {
        'Authorization': `Bearer ${MEMOS_TOKEN}`
      }
    });

    const data = await response.json();
    const todos = data.filter(memo => memo.tags.includes('todo'));

    displayTodos(todos);
  } catch (error) {
    console.error('Failed to fetch todos:', error);
  }
}

async function displayTodos(todos) {
  const container = document.getElementById('todo-list');
  container.innerHTML = '';

  todos.forEach(todo => {
    const li = document.createElement('li');
    li.className = 'todo-item';

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = todo.payload?.completed || false;
    checkbox.onchange = async () => {
      await toggleTodo(todo.id, checkbox.checked);
    };

    const span = document.createElement('span');
    span.textContent = todo.content;

    if (todo.tags.includes('high')) {
      li.style.color = '#e74c3c';
    } else if (todo.tags.includes('urgent')) {
      li.style.color = '#f59e0b';
    }

    li.appendChild(checkbox);
    li.appendChild(span);
    container.appendChild(li);
  });
}

async function toggleTodo(id, completed) {
  // Update via Memos API
  await fetch(`${MEMOS_URL}/memo/${id}`, {
    method: 'PATCH',
    headers: {
      'Authorization': `Bearer ${MEMOS_TOKEN}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      content: todo.content,
      payload: JSON.stringify({
        completed: completed
      })
    })
  });
}

// Fetch todos on page load
fetchTodos();
// Auto-refresh every 60 seconds
setInterval(fetchTodos, 60000);
</script>

<style>
.todo-list {
  list-style: none;
  padding: 0;
}

.todo-item {
  padding: 8px;
  margin-bottom: 4px;
  background: #f5f5f5;
  border-radius: 4px;
  cursor: pointer;
}

.todo-item:hover {
  background: #e8e8e8;
}

.todo-item input[type="checkbox"] {
  margin-right: 10px;
}
</style>
```

#### For Astro Sites:

```astro
// src/components/MemosTodos.astro
___
const MEMOS_URL = 'http://ubuntu58-1:5230/api/v1';
const MEMOS_TOKEN = 'your-api-token';

interface Memo {
  id: number;
  content: string;
  payload?: {
    completed: boolean;
  };
  tags: string[];
}

let todos: Memo[] = [];

async function fetchTodos() {
  const response = await fetch(`${MEMOS_URL}/memo/list`, {
    headers: {
      'Authorization': `Bearer ${MEMOS_TOKEN}`
    }
  });

  const data = await response.json();
  todos = data.filter((memo: Memo) => memo.tags.includes('todo'));
}

function renderTodos() {
  return todos.map((todo: Memo) => `
    <div class="todo-item ${todo.tags.includes('high') ? 'high-priority' : ''}">
      <input
        type="checkbox"
        ${todo.payload?.completed ? 'checked' : ''}
        onChange={() => toggleTodo(todo.id, !todo.payload?.completed)}
      />
      <span>${todo.content}</span>
    </div>
  `).join('');
}

fetchTodos();
```

**Benefits:**
- ✅ Real-time updates when you check off items in Memos
- ✅ No site rebuilds required
- ✅ Checkbox state managed by your code
- ✅ Better UX with visual feedback

___

### Option 2: Static Markdown Generation (Alternative)

Simple and fast, but requires site rebuilds.

#### For Hugo Sites:

**Generate markdown from Memos:**

```bash
# Generate static markdown from Memos API
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://ubuntu58-1:5230/api/v1/memo/list?filter=tag:todo \
  | jq -r '.[] | "# \\(.content | gsub("\\n"; " "))\\n"' > \
  /media/docker/hugo/content/todos.md
```

**Add to Hugo template:**

```html
<!-- layouts/partials/todos.html -->
{{ if eq .Path "/todos" }}
  <div class="todos-container">
      {{ .Content }}
  </div>
{{ end }}
{{ end }}
```

**Benefits:**
- ✅ No JavaScript required
- ✅ Static site performance
- ✅ SEO-friendly
- ✅ Simple markdown editing

#### Drawbacks:
- ❌ Requires site rebuild after every todo change
- ❌ Not real-time (changes only visible after rebuild)

___

## 🧠 OpenMemory Integration

### Why Integrate with OpenMemory?

1. **Store Decisions**: Remember integration decisions for future reference
2. **Store Best Practices**: What workflow patterns work best for you
3. **Retrieve Context**: Query past decisions when planning new features

### Storing Integration Decisions

```bash
# Store integration decision using OpenMemory
curl -X POST http://localhost:8080/api/memories \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Decided to use Memos + Hugo API fetch (Option A) for todo list integration. Provides real-time updates and checkbox management without site rebuilds. Alternative was static markdown generation but API fetch gives live updates.",
    "tags": ["decision", "integration", "memos", "hugo", "web"],
    "metadata": {
      "project": "todo-list",
      "timestamp": "2026-02-03",
      "alternatives_considered": ["Static markdown", "Astro fetch", "Vikunja"],
      "selection_criteria": ["real-time", "ease_of_use", "existing_installation"]
    }
  }'
```

### Reinforcing Important Memories

```bash
# Boost salience so these decisions surface in future queries
curl -X POST http://localhost:8080/api/memories/reinforce \
  -H "Content-Type: application/json" \
  -d '{
    "id": "MEMORY_ID_TO_BOOST",
    "boost": 0.2
  }'
```

### Querying Context When Planning

```bash
# Before planning new features, query OpenMemory
curl -X POST http://localhost:8080/api/memories/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "memos hugo astro integration best practices",
    "k": 5,
    "sector": "procedural"
  }'
```

___

## 🪝 Memos Webhook Automation (Advanced)

### Setup Webhook Configuration

**1. Generate Access Token:**
- Open Memos: http://ubuntu58-1:5230
- Go to: Settings → Access Tokens
- Create new token with appropriate permissions

**2. Configure Webhook in Your Project:**

**For Hugo:**

Create webhook receiver:

```python
# hugo-webhook-receiver.py (add to your Hugo site)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook/memos', methods=['POST'])
def memos_webhook():
    data = request.json

    # Only process todo-related memos
    if 'tags' in data and 'todo' in data['tags']:
        # Trigger Hugo rebuild
        rebuild_hugo_site()
        return jsonify({'status': 'rebuild_triggered'}), 200

    return jsonify({'status': 'ignored'}), 200

def rebuild_hugo_site():
    import subprocess
    subprocess.run(['hugo', '--quiet'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
```

**For Astro:**

```typescript
// src/pages/api/webhook.ts
import type { APIRoute } from 'astro:api/server';

export const POST: APIRoute = async ({ request }) => {
  const data = await request.json();

  if (data.tags?.includes('todo')) {
    // Trigger Astro rebuild
    await exec('npm run build');
  }

  return new Response(JSON.stringify({ status: 'processed' }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
};
```

**3. Configure Webhook in Memos:**
- Open Memos: http://ubuntu58-1:5230
- Go to: Settings → Webhooks
- Add webhook: `http://your-hugo-site.com/webhook/memos`
- Choose events: "Memo Created", "Memo Updated", "Memo Deleted"
- Test by creating a new todo

___

## 📊 Daily Workflow Template

### Morning Setup (09:00 AM)

```markdown
## Morning Review ☀️

- [ ] Open Memos: http://ubuntu58-1:5230
- [ ] Review yesterday's completed items (#yesterday tag)
- [ ] Uncheck completed items
- [ ] Set 3 main goals for today
- [ ] Prioritize tasks by importance (High > Medium > Low)
- [ ] Plan deep work blocks (2-3 hours each)
- [ ] Schedule breaks (every 90 minutes)

## Throughout Day 🌅

### Work Tasks

#### Deep Work Block #1 (09:00 - 11:00)
- [ ] Primary task: [highest priority item]
- [ ] Secondary task: backup item if needed
- [ ] Communication: Slack/Email (limit to 15 min checks)
- [ ] Break: 10:00 AM

### Personal Tasks

- [ ] Personal errand: [time-sensitive item]
- [ ] Health check: water, snacks, movement
- [ ] Learning/Reading: 30 minutes

## Evening Wrap-up 🌆

- [ ] Review daily progress (check off completed items)
- [ ] Create tomorrow's todo list (tag with #tomorrow)
- [ ] Archive completed items (change visibility)
- [ ] Reflect on improvements (store in OpenMemory)
- [ ] Plan tomorrow's priorities (ready to start fresh)

## Weekly Review 📊 (Sunday Evening)

### Weekly Goals
- [ ] Goal 1: [weekly objective]
- [ ] Goal 2: [weekly objective]
- [ ] Goal 3: [weekly objective]

### Saturday Review
- [ ] Review completed tasks this week
- [ ] Update project status
- [ ] Plan next week's priorities

___

## 💡 Quick Tips

### Keyboard Shortcuts (in Memos web UI)
- `Ctrl/Cmd + K` - Quick create
- `Ctrl/Cmd + /` - Focus search
- `Enter` - Save memo

### Search Operators
- `tag:#work` - Filter by work tag
- `pinned:true` - Show only pinned items
- `!important` - Show important items

### Daily Workflow
1. **Morning**: Create daily plan memo
2. **Throughout day**: Check off items as completed
3. **End of day**: Create tomorrow's plan
4. **Weekly**: Archive old completed todos

___

## 🏷️ Tagging System

### Recommended Tag Categories

| Category | Tags | When to Use |
|-----------|-------|----------|
| **Priority** | `#high`, `#medium`, `#low`, `#urgent` | Indicate task importance |
| **Context** | `#work`, `#personal`, `#learning` | Separate work and life |
| **Urgency** | `#urgent` | Time-sensitive items |
| **Project** | `#project:NAME` | Project-specific tasks |
| **Status** | `#in-progress`, `#blocked`, `#waiting` | Current task state |
| **Temporal** | `#today`, `#tomorrow`, `#yesterday` | Daily planning |
| **Archive** | `#archived` | Completed/old items |

### Memos Tags for Todo Lists

- `#todo` - All todo items
- `#work` - Work-related tasks
- `#personal` - Personal items
- `#high` - High priority
- `#medium` - Medium priority
- `#low` - Low priority
- `#urgent` - Urgent items
- `#yesterday` - Items from previous day
- `#today` - Today's focus
- `#tomorrow` - Tomorrow's planning

### OpenMemory Tags for Todo Management

| Tag | Purpose | Example Memories |
|------|---------|---------------|
| `#decision` | Integration choices and rationale | Decided to use API fetch method |
| `#workflow` | Daily routines and productivity patterns | Morning review, set priorities |
| `#best-practices` | Proven todo list workflows | Tag consistently, weekly reviews |
| `#memos` | Memos-specific tips and tricks | Checkbox shortcuts, search operators |
| `#hugo` | Hugo integration configuration | Frontend code examples |
| `#astro` | Astro integration examples | Component implementation |
| `#integration` | General integration patterns | API usage, webhook setup |
| `#productivity` | General productivity strategies | Time management, focus techniques |

___

## 🚀 Getting Started Checklist

### Today (Right Now!)

- [ ] Open Memos: http://ubuntu58-1:5230
- [ ] Create your first todo: Click "New Memo" or `Ctrl/Cmd + K`
- [ ] Use checkbox format: `- [ ] Task description`
- [ ] Add tags: Use `#todo`, `#work`, `#urgent` (comma-separated)
- [ ] Complete items: Click checkbox to mark done ✅

### Week 1 Setup

- [ ] Choose integration method (API fetch or webhook)
- [ ] Create Access Token in Memos Settings
- [ ] Test Hugo/Astro integration code
- [ ] Store integration decision in OpenMemory
- [ ] Set up daily workflow habit

### Advanced (Optional)

- [ ] Set up webhook automation for site rebuilds
- [ ] Create personal tag system
- [ ] Set up weekly review routine
- [ ] Implement productivity metrics tracking

___

## 📚 Quick Reference

### Memos API Endpoints

| Method | Endpoint | Description |
|---------|-----------|-------------|
| GET | `/api/v1/memo/list?filter=tag:todo` | List all todos |
| POST | `/api/v1/memo` | Create new todo |
| PATCH | `/api/v1/memo/:id` | Update todo |
| DELETE | `/api/v1/memo/:id` | Delete todo |
| GET | `/api/v1/memo/:id` | Get single todo |

### Getting Your API Token

1. Open Memos: http://ubuntu58-1:5230
2. Go to: Settings → Access Tokens
3. Create new token
4. Copy and use in your integration code

### Daily Workflow

**Morning (09:00 AM):**
- Create daily plan
- Set priorities
- Plan deep work blocks
- Schedule breaks

**Throughout Day:**
- Focus on high-priority items
- Check off completed items
- Take regular breaks

**Evening (17:00 PM):**
- Review progress
- Create tomorrow's todo list
- Archive completed items
- Reflect on improvements

___

## 🎯 Success Metrics

**Track your productivity:**

- Daily completion rate: `[Completed todos] / [Total active todos]`
- Weekly review adherence: `[Reviews completed] / [7 days]`
- Integration reliability: `[Successful API calls] / [Total API calls]`
- Memory retrieval success: `[Helpful memories found] / [Total queries]`

___

**Ready to boost your productivity? Start by opening Memos: http://ubuntu58-1:5230!** 🎯

*Published: 2026-02-03*