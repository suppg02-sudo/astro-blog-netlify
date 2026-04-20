---
pubDatetime: 2026-03-21T22:37:00Z
title: "Life Orchestrator: Implementation Guide"
postSlug: "life-orchestrator-implementation"
description: "Life Orchestrator: Implementation Guide"
tags:
  - life-orchestrator
  - skill-development
  - opencode
  - implementation
---

# Life Orchestrator: Implementation Guide

*Part 4 of 5: Building the Skill*

---

> **This post is part of a series**
> - [Part 1: Vision](/posts/life-orchestrator-vision/) - The philosophy and why this matters
> - [Part 2: Architecture](/posts/life-orchestrator-architecture/) - Technical design and data models
> - [Part 3: Domains](/posts/life-orchestrator-domains/) - Garden, energy, work, life examples
> - **Part 4: Implementation** (you are here) - Building the skill
> - [Part 5: Roadmap](/posts/life-orchestrator-roadmap/) - Future development

---

## Overview

This post covers the practical implementation of the Life Orchestrator skill:

1. **Directory structure** - How to organize files
2. **Database setup** - PostgreSQL tables and indexes
3. **Scripts** - CLI commands for daily use
4. **Menu system** - Interactive interface
5. **Cron jobs** - Automated tasks
6. **Testing** - Verification steps

---

## Directory Structure

```
~/.config/opencode/skills/orchestrator/
├── SKILL.md                    # Skill definition (this is what you're reading)
├── context/
│   ├── domains.json            # Domain definitions
│   ├── config.json             # User preferences
│   └── state.json              # Current view state (cached)
├── scripts/
│   ├── orchestrator.sh         # Main CLI
│   ├── add-item.py             # Add new item
│   ├── list-items.py           # Query and list items
│   ├── update-item.py          # Modify item
│   ├── transition-phase.py     # Move item between phases
│   ├── check-reminders.py      # Generate due reminders
│   ├── send-notifications.py   # Deliver via Telegram
│   └── generate-report.py      # Create summaries
├── sql/
│   ├── schema.sql              # Database schema
│   ├── migrations/             # Schema migrations
│   └── queries/                # Common queries
├── templates/
│   ├── item-template.json      # New item template
│   ├── domain-template.json    # New domain template
│   └── report-template.md      # Report format
├── docs/
│   ├── api-reference.md        # Script API docs
│   └── domain-guide.md         # How to add domains
└── history/
    └── changes.log             # Change history
```

---

## Database Setup

### Schema (PostgreSQL)

```sql
-- File: sql/schema.sql

CREATE TABLE IF NOT EXISTS orchestrator_items (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    domain TEXT NOT NULL,
    phase TEXT NOT NULL CHECK (phase IN ('plant', 'grow', 'harvest', 'rest')),
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'completed', 'deferred', 'archived')),
    priority TEXT NOT NULL DEFAULT 'medium' CHECK (priority IN ('urgent', 'high', 'medium', 'low')),
    created TIMESTAMPTZ DEFAULT NOW(),
    updated TIMESTAMPTZ DEFAULT NOW(),
    target_date DATE,
    phase_entered TIMESTAMPTZ DEFAULT NOW(),
    metadata JSONB DEFAULT '{}',
    history JSONB DEFAULT '[]',
    reminders JSONB DEFAULT '[]',
    tags TEXT[] DEFAULT '{}'
);

-- Indexes for common queries
CREATE INDEX IF NOT EXISTS idx_items_domain ON orchestrator_items(domain);
CREATE INDEX IF NOT EXISTS idx_items_phase ON orchestrator_items(phase);
CREATE INDEX IF NOT EXISTS idx_items_status ON orchestrator_items(status);
CREATE INDEX IF NOT EXISTS idx_items_target_date ON orchestrator_items(target_date);
CREATE INDEX IF NOT EXISTS idx_items_domain_phase ON orchestrator_items(domain, phase);

-- Full-text search on title
CREATE INDEX IF NOT EXISTS idx_items_title_search ON orchestrator_items USING GIN (to_tsvector('english', title));

-- Trigger to update 'updated' timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER orchestrator_items_updated
    BEFORE UPDATE ON orchestrator_items
    FOR EACH ROW
    EXECUTE FUNCTION update_timestamp();
```

### Initialize Database

```bash
#!/bin/bash
# File: scripts/init-db.sh

DB_NAME="orchestrator"

# Create database if not exists
psql -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = '$DB_NAME'" | grep -q 1 || \
    psql -U postgres -c "CREATE DATABASE $DB_NAME"

# Apply schema
psql -U postgres -d $DB_NAME -f sql/schema.sql

echo "Orchestrator database initialized"
```

---

## Scripts

### Main CLI (orchestrator.sh)

```bash
#!/bin/bash
# File: scripts/orchestrator.sh
# Main CLI for Life Orchestrator

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"

# Database connection
DB_HOST="${DB_HOST:-localhost}"
DB_NAME="${DB_NAME:-orchestrator}"
DB_USER="${DB_USER:-postgres}"

# Commands
case "$1" in
    add)
        shift
        python3 "$SCRIPT_DIR/add-item.py" "$@"
        ;;
    list)
        shift
        python3 "$SCRIPT_DIR/list-items.py" "$@"
        ;;
    update)
        shift
        python3 "$SCRIPT_DIR/update-item.py" "$@"
        ;;
    phase)
        shift
        python3 "$SCRIPT_DIR/transition-phase.py" "$@"
        ;;
    today)
        python3 "$SCRIPT_DIR/list-items.py" --today
        ;;
    week)
        python3 "$SCRIPT_DIR/list-items.py" --week
        ;;
    overdue)
        python3 "$SCRIPT_DIR/list-items.py" --overdue
        ;;
    by-phase)
        shift
        python3 "$SCRIPT_DIR/list-items.py" --phase "$1"
        ;;
    by-domain)
        shift
        python3 "$SCRIPT_DIR/list-items.py" --domain "$1"
        ;;
    report)
        shift
        python3 "$SCRIPT_DIR/generate-report.py" "$@"
        ;;
    check-reminders)
        python3 "$SCRIPT_DIR/check-reminders.py"
        ;;
    notify)
        python3 "$SCRIPT_DIR/send-notifications.py"
        ;;
    *)
        echo "Usage: orchestrator <command> [args]"
        echo ""
        echo "Commands:"
        echo "  add <domain> <title>     Add new item"
        echo "  list                    List all active items"
        echo "  update <id> [field=val] Update item"
        echo "  phase <id> <phase>      Transition item to new phase"
        echo "  today                   Show today's priorities"
        echo "  week                    Show this week's items"
        echo "  overdue                 Show overdue items"
        echo "  by-phase <phase>        Show items by phase"
        echo "  by-domain <domain>      Show items by domain"
        echo "  report [type]           Generate report (daily, weekly)"
        echo "  check-reminders         Check and queue due reminders"
        echo "  notify                  Send queued notifications"
        ;;
esac
```

### Add Item (add-item.py)

```python
#!/usr/bin/env python3
# File: scripts/add-item.py

import argparse
import json
import sys
from datetime import datetime, date
from uuid import uuid4
import psycopg2
from psycopg2.extras import Json

def generate_id(domain):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    short_uuid = str(uuid4())[:8]
    return f"{domain}_{timestamp}_{short_uuid}"

def add_item(domain, title, **kwargs):
    conn = psycopg2.connect(
        host="localhost",
        database="orchestrator",
        user="postgres"
    )
    cur = conn.cursor()
    
    item_id = generate_id(domain)
    
    cur.execute("""
        INSERT INTO orchestrator_items 
        (id, title, domain, phase, status, priority, target_date, metadata, tags)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    """, (
        item_id,
        title,
        domain,
        kwargs.get('phase', 'plant'),
        kwargs.get('status', 'active'),
        kwargs.get('priority', 'medium'),
        kwargs.get('target_date'),
        Json(kwargs.get('metadata', {})),
        kwargs.get('tags', [])
    ))
    
    conn.commit()
    cur.close()
    conn.close()
    
    return item_id

def main():
    parser = argparse.ArgumentParser(description="Add new orchestrator item")
    parser.add_argument("domain", help="Domain (garden, work, personal, etc.)")
    parser.add_argument("title", help="Item title")
    parser.add_argument("--phase", default="plant", choices=["plant", "grow", "harvest", "rest"])
    parser.add_argument("--priority", default="medium", choices=["urgent", "high", "medium", "low"])
    parser.add_argument("--target-date", help="Target date (YYYY-MM-DD)")
    parser.add_argument("--tags", nargs="*", default=[], help="Tags")
    parser.add_argument("--metadata", help="JSON metadata")
    
    args = parser.parse_args()
    
    metadata = json.loads(args.metadata) if args.metadata else {}
    target_date = date.fromisoformat(args.target_date) if args.target_date else None
    
    item_id = add_item(
        args.domain,
        args.title,
        phase=args.phase,
        priority=args.priority,
        target_date=target_date,
        tags=args.tags,
        metadata=metadata
    )
    
    print(f"Created item: {item_id}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

### List Items (list-items.py)

```python
#!/usr/bin/env python3
# File: scripts/list-items.py

import argparse
import sys
from datetime import date, timedelta
import psycopg2
from tabulate import tabulate

def list_items(filters=None):
    conn = psycopg2.connect(
        host="localhost",
        database="orchestrator",
        user="postgres"
    )
    cur = conn.cursor()
    
    query = "SELECT id, title, domain, phase, priority, target_date, status FROM orchestrator_items WHERE status = 'active'"
    params = []
    
    if filters:
        if 'domain' in filters:
            query += " AND domain = %s"
            params.append(filters['domain'])
        if 'phase' in filters:
            query += " AND phase = %s"
            params.append(filters['phase'])
        if 'today' in filters:
            query += " AND (target_date = %s OR target_date IS NULL)"
            params.append(date.today())
        if 'week' in filters:
            query += " AND target_date BETWEEN %s AND %s"
            params.extend([date.today(), date.today() + timedelta(days=7)])
        if 'overdue' in filters:
            query += " AND target_date < %s"
            params.append(date.today())
    
    query += " ORDER BY target_date NULLS LAST, priority DESC"
    
    cur.execute(query, params)
    rows = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return rows

def display_items(rows):
    if not rows:
        print("No items found")
        return
    
    headers = ["ID", "Title", "Domain", "Phase", "Priority", "Target", "Status"]
    print(tabulate(rows, headers=headers, tablefmt="simple"))

def main():
    parser = argparse.ArgumentParser(description="List orchestrator items")
    parser.add_argument("--domain", help="Filter by domain")
    parser.add_argument("--phase", help="Filter by phase")
    parser.add_argument("--today", action="store_true", help="Today's items")
    parser.add_argument("--week", action="store_true", help="This week's items")
    parser.add_argument("--overdue", action="store_true", help="Overdue items")
    parser.add_argument("--all", action="store_true", help="All items (including non-active)")
    
    args = parser.parse_args()
    
    filters = {}
    if args.domain:
        filters['domain'] = args.domain
    if args.phase:
        filters['phase'] = args.phase
    if args.today:
        filters['today'] = True
    if args.week:
        filters['week'] = True
    if args.overdue:
        filters['overdue'] = True
    
    rows = list_items(filters if filters else None)
    display_items(rows)
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

### Phase Transition (transition-phase.py)

```python
#!/usr/bin/env python3
# File: scripts/transition-phase.py

import argparse
import json
import sys
from datetime import datetime
import psycopg2
from psycopg2.extras import Json

def transition_phase(item_id, new_phase, note=None):
    conn = psycopg2.connect(
        host="localhost",
        database="orchestrator",
        user="postgres"
    )
    cur = conn.cursor()
    
    # Get current item
    cur.execute("SELECT phase, history FROM orchestrator_items WHERE id = %s", (item_id,))
    row = cur.fetchone()
    if not row:
        print(f"Item not found: {item_id}")
        return False
    
    old_phase, history = row
    history = history or []
    
    # Add to history
    history.append({
        "date": datetime.now().isoformat(),
        "action": "phase_change",
        "from": old_phase,
        "to": new_phase,
        "note": note
    })
    
    # Update item
    cur.execute("""
        UPDATE orchestrator_items 
        SET phase = %s, phase_entered = NOW(), history = %s
        WHERE id = %s
    """, (new_phase, Json(history), item_id))
    
    conn.commit()
    cur.close()
    conn.close()
    
    print(f"Transitioned {item_id}: {old_phase} → {new_phase}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Transition item to new phase")
    parser.add_argument("item_id", help="Item ID")
    parser.add_argument("phase", choices=["plant", "grow", "harvest", "rest"], help="New phase")
    parser.add_argument("--note", help="Note for history")
    
    args = parser.parse_args()
    
    success = transition_phase(args.item_id, args.phase, args.note)
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
```

---

## Menu Configuration

```json
{
  "questions": [{
    "question": "🌿 Life Orchestrator - What would you like to do?",
    "header": "Orchestrator",
    "options": [
      {"label": "📅 Today's Priorities (Recommended)", "description": "What needs attention today"},
      {"label": "📋 This Week", "description": "Upcoming items and deadlines"},
      {"label": "🌱 By Phase", "description": "View items by lifecycle phase"},
      {"label": "🏷️ By Domain", "description": "Garden, work, personal, blog, energy"},
      {"label": "➕ Add New Item", "description": "Create a new tracked item"},
      {"label": "🔄 Update Item", "description": "Modify or transition an item"},
      {"label": "⚠️ Overdue Items", "description": "Items past their target date"},
      {"label": "📊 Generate Report", "description": "Daily or weekly summary"},
      {"label": "⚙️ Settings", "description": "Configure domains and preferences"},
      {"label": "🔍 Skill Discovery", "description": "Related docs, improve menu"},
      {"label": "Exit", "description": "Return to previous context"}
    ],
    "multiple": false
  }]
}
```

---

## Cron Jobs

```bash
# File: /etc/cron.d/orchestrator

# Daily reminder check at 8 AM
0 8 * * * root /root/.config/opencode/skills/orchestrator/scripts/orchestrator.sh check-reminders

# Send notifications at 8:05 AM
5 8 * * * root /root/.config/opencode/skills/orchestrator/scripts/orchestrator.sh notify

# Daily report at 9 PM
0 21 * * * root /root/.config/opencode/skills/orchestrator/scripts/orchestrator.sh report daily

# Weekly report on Monday at 9 AM
0 9 * * 1 root /root/.config/opencode/skills/orchestrator/scripts/orchestrator.sh report weekly
```

---

## Testing

### Unit Tests

```python
#!/usr/bin/env python3
# File: scripts/test_orchestrator.py

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from add_item import add_item
from list_items import list_items
from transition_phase import transition_phase

class TestOrchestrator(unittest.TestCase):
    
    def test_add_item(self):
        item_id = add_item(
            domain="test",
            title="Test Item",
            phase="plant",
            priority="medium"
        )
        self.assertTrue(item_id.startswith("test_"))
    
    def test_list_items(self):
        rows = list_items({"domain": "test"})
        self.assertIsInstance(rows, list)
    
    def test_phase_transition(self):
        # First add an item
        item_id = add_item(
            domain="test",
            title="Transition Test",
            phase="plant"
        )
        
        # Then transition it
        success = transition_phase(item_id, "grow", "Test transition")
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
```

### Integration Test

```bash
#!/bin/bash
# File: scripts/test-integration.sh

set -e

echo "Testing Orchestrator integration..."

# Test add
echo "1. Testing add..."
ID=$(./orchestrator.sh add test "Integration Test Item" --priority high)
echo "   Created: $ID"

# Test list
echo "2. Testing list..."
./orchestrator.sh list --domain test

# Test phase transition
echo "3. Testing phase transition..."
./orchestrator.sh phase $ID grow --note "Test transition"

# Test report
echo "4. Testing report..."
./orchestrator.sh report daily

# Cleanup
echo "5. Cleanup..."
psql -U postgres -d orchestrator -c "DELETE FROM orchestrator_items WHERE domain = 'test'"

echo "All tests passed!"
```

---

## SKILL.md Header

```yaml
---
name: orchestrator
version: 1.0.0
description: Unified lifecycle management for garden, energy, work, personal, and blog domains
trigger: orch, orchestrator, life
maturity: L2
created: 2026-03-21
updated: 2026-03-21
dependencies:
  - reminder
  - telegram
  - cron
  - tracking
author: OpenCode
tags: [orchestration, lifecycle, productivity, automation]
---
```

---

## What's Next

With implementation complete, we can plan the future. In the next post:

- **Energy domain** - Solar monitoring integration
- **Mobile interface** - Telegram bot commands
- **Analytics** - Lifecycle pattern analysis
- **AI suggestions** - Smart recommendations
- **Community** - Sharing domain templates

**Continue to [Part 5: Roadmap →](/posts/life-orchestrator-roadmap/)**

---

## Quick Reference: Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `orch add` | Create new item | `orch add garden "Tomatoes" --priority high` |
| `orch list` | List items | `orch list --domain garden` |
| `orch today` | Today's priorities | `orch today` |
| `orch week` | This week | `orch week` |
| `orch phase` | Transition phase | `orch phase item_123 grow` |
| `orch report` | Generate report | `orch report weekly` |

---

*Implementation is the easy part. The hard part is remembering to use it every day.*