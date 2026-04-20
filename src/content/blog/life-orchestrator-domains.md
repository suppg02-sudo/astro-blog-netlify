---
pubDatetime: 2026-03-21T22:36:00Z
title: "Life Orchestrator: Domain Examples"
postSlug: "life-orchestrator-domains"
description: "Life Orchestrator: Domain Examples"
tags:
  - life-orchestrator
  - productivity
  - examples
  - garden
  - energy
---

# Life Orchestrator: Domain Examples

*Part 3 of 5: Real-World Applications*

---

> **This post is part of a series**
> - [Part 1: Vision](/posts/life-orchestrator-vision/) - The philosophy and why this matters
> - [Part 2: Architecture](/posts/life-orchestrator-architecture/) - Technical design and data models
> - **Part 3: Domains** (you are here) - Garden, energy, work, life examples
> - [Part 4: Implementation](/posts/life-orchestrator-implementation/) - Building the skill
> - [Part 5: Roadmap](/posts/life-orchestrator-roadmap/) - Future development

---

## Overview

This post shows the Life Orchestrator in action across five domains:

| Domain | Status | Complexity |
|--------|--------|------------|
| 🌱 **Garden** | Ready now | Medium |
| ⚡ **Energy** | Planned | High |
| 💼 **Work** | Ready now | Medium |
| 🧑 **Personal** | Ready now | Low |
| 📝 **Blog** | Ready now | Medium |

Each domain has:
- Phase definitions specific to that domain
- Example items with realistic data
- Typical workflows and reminders
- Integration with existing skills

---

## 🌱 Domain: Garden

### Why This Domain First

Garden is the **canonical example** of Plant → Grow → Harvest. It's literal. The phases map directly to real-world activities.

### Phase Definitions

| Phase | Garden Term | Activities | Duration |
|-------|-------------|------------|----------|
| **plant** | Sowing/Starting | Sow seeds, prepare beds, order supplies | 2-4 weeks |
| **grow** | Cultivation | Water, feed, ventilate, prune, train | 8-16 weeks |
| **harvest** | Picking | Harvest crops, preserve, store | 4-8 weeks |
| **rest** | Winter | Clean, repair, plan, order seeds | 12-16 weeks |

### Example Items

#### Item 1: Tomato Crop

```json
{
  "id": "garden_2026_tomato_sungold",
  "title": "Sungold Tomatoes",
  "domain": "garden",
  "phase": "grow",
  "status": "active",
  "priority": "high",
  "target_date": "2026-07-15",
  "phase_entered": "2026-03-15",
  "metadata": {
    "variety": "Sungold",
    "location": "Greenhouse bed 1",
    "quantity": 4,
    "sow_date": "2026-03-01",
    "plant_out_date": "2026-04-20",
    "expected_first_harvest": "2026-07-01"
  },
  "reminders": [
    {"type": "watering", "schedule": "daily", "time": "08:00"},
    {"type": "feeding", "schedule": "weekly", "time": "09:00", "day": "Saturday"},
    {"type": "side_shoot", "schedule": "weekly", "time": "10:00", "day": "Sunday"}
  ]
}
```

**Reminder behavior:**
- Daily: "💧 Water Sungold tomatoes (Greenhouse bed 1)"
- Weekly: "🍅 Feed Sungold tomatoes - use Tomorite"
- Weekly: "✂️ Check Sungold for side shoots to remove"

#### Item 2: Chili Plants

```json
{
  "id": "garden_2026_chili_jalapeno",
  "title": "Jalapeño Chillies",
  "domain": "garden",
  "phase": "plant",
  "status": "active",
  "priority": "medium",
  "target_date": "2026-08-01",
  "metadata": {
    "variety": "Jalapeño",
    "location": "Propagator",
    "quantity": 6,
    "sow_date": "2026-03-21",
    "germination_days": 14
  }
}
```

**Phase transition trigger:** Once germinated → move to "grow" phase

### Garden Workflow

{{< mermaid >}}
gantt
    title Tomato Lifecycle 2026
    dateFormat  YYYY-MM-DD
    section Plant
    Sow seeds           :done, 2026-03-01, 14d
    Germinate           :done, 2026-03-08, 7d
    Pot on              :2026-03-15, 14d
    section Grow
    Harden off          :2026-04-01, 14d
    Plant out           :2026-04-15, 1d
    Train and feed      :2026-04-16, 84d
    section Harvest
    First fruits        :2026-07-08, 1d
    Peak harvest        :2026-07-15, 60d
    section Rest
    Clear plants        :2026-10-01, 7d
    Clean greenhouse    :2026-10-08, 7d
{{< /mermaid >}}

### Integration with Existing Skills

| Skill | Garden Integration |
|-------|-------------------|
| **reminder** | Daily watering, weekly feeding |
| **telegram** | Frost warnings, harvest notifications |
| **cron** | Seasonal task schedules |
| **lifeplan** | "Start growing food" goal linked to garden items |

---

## ⚡ Domain: Energy (Future)

### Why This Domain

Solar panels and energy monitoring need **continuous tracking**. The orchestrator can:
- Monitor daily generation vs targets
- Alert on anomalies (low generation = panel issue?)
- Track ROI and savings
- Schedule maintenance

### Phase Definitions

| Phase | Energy Term | Activities | Duration |
|-------|-------------|------------|----------|
| **plant** | Installation | Install panels, configure monitoring | 1-4 weeks |
| **grow** | Generation | Monitor output, optimize usage | Ongoing |
| **harvest** | Savings | Calculate ROI, export credits | Monthly |
| **rest** | Maintenance | Clean panels, check connections | Annual |

### Example Items

#### Item 1: Solar Array

```json
{
  "id": "energy_2026_solar_array",
  "title": "4kW Solar Array",
  "domain": "energy",
  "phase": "grow",
  "status": "active",
  "priority": "medium",
  "target_date": null,
  "metadata": {
    "capacity_kw": 4.0,
    "install_date": "2025-06-15",
    "inverter_model": "SolarEdge SE4000",
    "panel_count": 12,
    "orientation": "South",
    "tariff": "Octopus Flux",
    "export_rate": 15.0
  },
  "reminders": [
    {"type": "daily_summary", "schedule": "daily", "time": "20:00"},
    {"type": "monthly_report", "schedule": "monthly", "day": 1, "time": "09:00"}
  ]
}
```

**Reminder behavior:**
- Daily: "☀️ Today's generation: 18.2 kWh (Target: 15 kWh) ✅"
- Monthly: "📊 Monthly report: 420 kWh generated, £63 saved"

#### Item 2: Energy Target

```json
{
  "id": "energy_2026_target_100_percent",
  "title": "100% Solar Coverage (Summer)",
  "domain": "energy",
  "phase": "grow",
  "status": "active",
  "priority": "low",
  "target_date": "2026-08-31",
  "metadata": {
    "target_type": "self_sufficiency",
    "target_percent": 100,
    "current_percent": 65,
    "season": "summer"
  }
}
```

### Energy Workflow

```
Daily:
  06:00 - Check overnight consumption
  12:00 - Midday generation peak check
  20:00 - Daily summary notification

Weekly:
  Monday - Week comparison vs last week

Monthly:
  1st - Full report: generation, savings, ROI
```

### Integration Points

| Data Source | Integration |
|-------------|-------------|
| **Solar inverter API** | Pull generation data every 15 mins |
| **Smart meter** | Consumption data |
| **Weather API** | Predict tomorrow's generation |
| **Tariff API** | Calculate real-time savings |

---

## 💼 Domain: Work

### Why This Domain

Work tasks have deadlines, dependencies, and phases. The orchestrator provides:
- Project lifecycle tracking
- Deadline reminders that escalate
- Cross-project visibility

### Phase Definitions

| Phase | Work Term | Activities | Duration |
|-------|-----------|------------|----------|
| **plant** | Planning | Define scope, assign resources | 1-2 weeks |
| **grow** | Execution | Build, test, iterate | Variable |
| **harvest** | Delivery | Deploy, demo, handoff | 1-2 weeks |
| **rest** | Retrospective | Review, document, archive | 1 week |

### Example Items

#### Item 1: Client Project

```json
{
  "id": "work_2026_client_portal",
  "title": "Client Portal Redesign",
  "domain": "work",
  "phase": "grow",
  "status": "active",
  "priority": "high",
  "target_date": "2026-04-30",
  "metadata": {
    "client": "Acme Corp",
    "project_manager": "Self",
    "milestones": [
      {"name": "Design approved", "date": "2026-03-15", "status": "completed"},
      {"name": "Alpha release", "date": "2026-04-10", "status": "in_progress"},
      {"name": "Beta release", "date": "2026-04-20", "status": "pending"},
      {"name": "Go live", "date": "2026-04-30", "status": "pending"}
    ]
  }
}
```

**Reminder behavior:**
- 14 days before: "📅 Alpha release in 2 weeks - on track?"
- 7 days before: "⚠️ Alpha release in 1 week - any blockers?"
- 1 day before: "🚨 Alpha release TOMORROW"

### Work Workflow

{{< mermaid >}}
graph LR
    A[Plant: Scope] --> B[Grow: Build]
    B --> C[Harvest: Deploy]
    C --> D[Rest: Review]
    D --> E[New Project]
    
    B --> B2[Blocked?]
    B2 --> |Yes| B3[Escalate]
    B3 --> B
{{< /mermaid >}}

---

## 🧑 Domain: Personal

### Why This Domain

Personal goals often fail because they lack:
- Clear phases (people skip "plant" and jump to "grow")
- Regular reminders during the long "grow" phase
- Celebration at "harvest"

### Phase Definitions

| Phase | Personal Term | Activities | Duration |
|-------|---------------|------------|----------|
| **plant** | Commitment | Define goal, commit publicly | 1 week |
| **grow** | Habit Building | Daily practice, track progress | 66+ days |
| **harvest** | Achievement | Reach milestone, celebrate | 1 day |
| **rest** | Reflection | Evaluate, adjust, next goal | 1 week |

### Example Items

#### Item 1: Fitness Goal

```json
{
  "id": "personal_2026_fitness_5k",
  "title": "Run 5K in under 25 minutes",
  "domain": "personal",
  "phase": "grow",
  "status": "active",
  "priority": "medium",
  "target_date": "2026-06-01",
  "metadata": {
    "goal_type": "fitness",
    "current_pb": "28:30",
    "target_time": "25:00",
    "training_days": ["Tuesday", "Thursday", "Sunday"],
    "streak": 12
  },
  "reminders": [
    {"type": "training", "schedule": "specific_days", "days": ["Tuesday", "Thursday", "Sunday"], "time": "07:00"}
  ]
}
```

**Reminder behavior:**
- Training day: "🏃 Training day - 5K practice (Streak: 12 🔥)"
- Weekly: "📊 Week progress: 3/3 sessions completed"

#### Item 2: Retirement Goal

```json
{
  "id": "personal_2026_retirement",
  "title": "Retirement - December 2026",
  "domain": "personal",
  "phase": "grow",
  "status": "active",
  "priority": "urgent",
  "target_date": "2026-12-15",
  "metadata": {
    "goal_type": "life_event",
    "months_remaining": 9,
    "checklist": [
      {"task": "Pension review", "status": "completed"},
      {"task": "Financial advisor meeting", "status": "in_progress"},
      {"task": "Healthcare planning", "status": "pending"},
      {"task": "Housing decision", "status": "pending"}
    ]
  }
}
```

---

## 📝 Domain: Blog

### Why This Domain

Content creation has a clear lifecycle:
1. **Idea** (plant) - Capture, research
2. **Draft** (grow) - Write, edit, enhance
3. **Publish** (harvest) - Deploy, promote
4. **Review** (rest) - Analytics, plan follow-ups

### Phase Definitions

| Phase | Blog Term | Activities | Duration |
|-------|-----------|------------|----------|
| **plant** | Ideation | Capture idea, research, outline | 1-7 days |
| **grow** | Creation | Write draft, add visuals, edit | 1-14 days |
| **harvest** | Publication | Final edit, publish, promote | 1 day |
| **rest** | Analysis | Review analytics, plan follow-ups | 7 days |

### Example Items

#### Item 1: This Blog Series

```json
{
  "id": "blog_2026_life_orchestrator",
  "title": "Life Orchestrator Series",
  "domain": "blog",
  "phase": "grow",
  "status": "active",
  "priority": "high",
  "target_date": "2026-03-21",
  "metadata": {
    "series": true,
    "total_parts": 5,
    "completed_parts": 3,
    "source": "User idea",
    "word_count": 8000
  },
  "reminders": [
    {"type": "complete_series", "schedule": "once", "date": "2026-03-22"}
  ]
}
```

**Reminder behavior:**
- "📝 Life Orchestrator series: 3/5 complete - write parts 4 & 5"

### Blog Workflow

{{< mermaid >}}
graph TD
    A[Idea] --> B{Research needed?}
    B -->|Yes| C[Research]
    B -->|No| D[Outline]
    C --> D
    D --> E[Write Draft]
    E --> F[Edit & Enhance]
    F --> G[Publish]
    G --> H[Promote]
    H --> I[Review Analytics]
    I --> J[Follow-up Ideas]
    J --> A
{{< /mermaid >}}

---

## Cross-Domain Queries

### The Power of Unification

Once all domains use the same model, you can query across them:

```sql
-- Everything in "plant" phase right now
SELECT domain, title, target_date
FROM orchestrator_items
WHERE phase = 'plant' AND status = 'active'
ORDER BY domain, target_date;
```

**Result:**
| domain | title | target_date |
|--------|-------|-------------|
| blog | Life Orchestrator Part 4 | 2026-03-22 |
| garden | Jalapeño Chillies | 2026-08-01 |
| work | New Client Proposal | 2026-04-05 |

```sql
-- Everything due this week
SELECT domain, title, phase, target_date
FROM orchestrator_items
WHERE target_date BETWEEN CURRENT_DATE AND CURRENT_DATE + 7
  AND status = 'active'
ORDER BY target_date;
```

**Result:**
| domain | title | phase | target_date |
|--------|-------|-------|-------------|
| blog | Life Orchestrator Series | grow | 2026-03-21 |
| work | Client Portal Alpha | grow | 2026-04-10 |

---

## What's Next

With domains defined, we can build the skill. In the next post:

- **Directory structure** - Files and organization
- **Scripts** - CLI commands and automation
- **Menu system** - Interactive interface
- **Cron jobs** - Scheduled tasks
- **Testing** - Verification steps

**Continue to [Part 4: Implementation →](/posts/life-orchestrator-implementation/)**

---

## Quick Reference: Domain Summary

| Domain | Key Metadata | Primary Reminder | Phase Duration |
|--------|--------------|------------------|----------------|
| 🌱 Garden | variety, location, quantity | Daily watering | Seasonal |
| ⚡ Energy | capacity, tariff, panel_count | Daily summary | Ongoing |
| 💼 Work | client, milestones | Deadline alerts | Project-based |
| 🧑 Personal | goal_type, streak | Habit reminders | 66+ days |
| 📝 Blog | series, word_count | Draft deadlines | 1-14 days |

---

*Each domain is different, but they all grow. The Orchestrator speaks their common language.*