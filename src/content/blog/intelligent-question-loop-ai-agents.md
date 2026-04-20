---
pubDatetime: 2026-02-27T23:15:00Z
title: "Building an Intelligent Question Loop System for AI Agents"
postSlug: "intelligent-question-loop-ai-agents"
description: "Building an Intelligent Question Loop System for AI Agents"
tags:
  - agents
  - opencode
  - ux
  - question-system
  - ai
---

The question tool is one of the most powerful features in AI agent systems - it transforms a one-way conversation into an interactive dialogue where users guide the AI's decisions. But most implementations are static and don't adapt to context or user preferences.

Today I rebuilt the `q` trigger command into a full-featured **Intelligent Question Loop System** that adapts to context, remembers preferences, and provides meta-controls for adjusting behavior on the fly.

## The Problem with Static Questioning

Traditional AI agent questioning has several limitations:

1. **One-size-fits-all options** - Same number of choices regardless of complexity
2. **No intensity control** - Can't adjust depth for quick vs. complex decisions
3. **No persistence** - Preferences reset between sessions
4. **No transparency** - Users don't know where their choices are recorded
5. **No recovery** - Can't pause and resume question flows

## The Solution: Q System v2.0

The enhanced Q system introduces several key features:

### 1. Questioning Modes (5 Modes)

{{< mermaid >}}
graph LR
    A[Q Trigger] --> B{Mode Selection}
    B --> C[Explore]
    B --> D[Build]
    B --> E[Debug]
    B --> F[Learn]
    B --> G[Plan]
    B --> H[Auto-Detect]
    
    C --> I[Open-ended, Discovery]
    D --> J[Action-oriented, Implementation]
    E --> K[Diagnostic, Troubleshooting]
    F --> L[Educational, Resources]
    G --> M[Strategic, Trade-offs]
{{< /mermaid >}}

| Mode | Style | Options | Use When |
|------|-------|---------|----------|
| **Explore** | Open-ended | 6-8 | Research, understanding |
| **Build** | Action-oriented | 4-6 | Implementation, features |
| **Debug** | Diagnostic | 5-7 | Troubleshooting, fixing |
| **Learn** | Educational | 4-5 | Documentation, concepts |
| **Plan** | Strategic | 3-5 | Roadmap, architecture |

### 2. Intensity Levels (4 Levels)

The intensity system controls how many options appear and how detailed they are:

| Level | Options | Descriptions | Multiselect | Use Case |
|-------|---------|--------------|-------------|----------|
| **Minimal** | 4 max | Short (3 words) | Off | Quick decisions |
| **Normal** | 8 max | Full | As designed | Standard work |
| **Verbose** | 12 max | Detailed | On | Complex decisions |
| **Brainstorm** | 15 max | Extended | Forced on | Creative sessions |

### 3. Mandatory Meta Controls

Every question menu now includes these controls:

```
⚙️ Meta Controls (always available):
├── ⚡ Turn up intensity
├── 📉 Default level
├── 📍 Check recording location
├── 📊 Review history + AI suggestions
└── ⏸️ Deferred flows
```

This means users can **adjust behavior mid-conversation** without restarting.

### 4. Specialized Debug Menus

When errors are detected, the system automatically presents context-appropriate menus:

{{< mermaid >}}
graph TD
    A[Error Detected] --> B{Error Type?}
    B -->|docker, container| C[Docker Debug Menu]
    B -->|sql, mysql, postgres| D[Database Debug Menu]
    B -->|ENOTFOUND, 401, 403| E[Network Debug Menu]
    B -->|compile, webpack| F[Build Debug Menu]
    B -->|EACCES, EPERM| G[Permission Debug Menu]
    B -->|Unknown| H[General Debug Menu]
{{< /mermaid >}}

Each specialized menu has 8-10 relevant options for that specific error type.

### 5. Deferred Flows

Users can pause any question flow and resume later:

```json
{
  "id": "def_20260227_143045_xyz",
  "trigger": "q",
  "mode": "debug",
  "context": {
    "task": "Fix Docker container networking",
    "stage": "diagnosis"
  },
  "reason": "User said 'handle later'"
}
```

Deferred items auto-cleanup after 7 days.

### 6. Session-Aware Integration

The key innovation: **settings persist and apply to ALL questions in the conversation**.

{{< mermaid >}}
sequenceDiagram
    participant U as User
    participant Q as Q Trigger
    participant S as Session State
    participant A as Agent
    
    U->>Q: Say "q"
    Q->>S: Save intensity=verbose, mode=explore
    Q-->>U: Return to conversation
    Note over A: Agent checks session-state.json
    A->>U: Presents 12 options (verbose)
    A->>U: With detailed descriptions
    A->>U: Multiselect enabled
{{< /mermaid >}}

## Implementation Architecture

### File Structure

```
~/.config/opencode/
├── docs/instructions/triggers/
│   └── q.md                    # 707-line trigger definition
├── questions/
│   ├── session-state.json      # Active settings + preferences
│   ├── deferred.json           # Paused flows
│   └── history/
│       └── decisions.json      # All user choices
└── context-registry/data/
    └── questions.json          # Interaction tracking
```

### Session State Schema

```json
{
  "active": {
    "intensity": "verbose",
    "mode": "explore",
    "session_started": "2026-02-27T23:00:00Z",
    "questions_asked": 5
  },
  "preferences": {
    "default_intensity": "normal",
    "show_meta_in_all_menus": true,
    "apply_to_all_questions": true
  }
}
```

### Recording Locations

| Storage | Purpose | Retention |
|---------|---------|-----------|
| JSON Registry | Fast local queries | 90 days |
| Decisions Log | Human-readable backup | 30 days |
| Supermemory | Persistent cross-session | Permanent |
| Deferred | Paused flows | 7 days |

## Usage Examples

### Setting Intensity

```
User: q
Agent: [Q Session Menu]
User: ⚡ Adjust Intensity → Verbose
Agent: Intensity set to Verbose - 12 options, detailed descriptions

[All subsequent questions now use verbose settings]
```

### Deferring a Flow

```
User: q → Debug → Investigate
Agent: [Asking diagnostic questions...]
User: Actually, defer this
Agent: Saved. Add a note?
User: Waiting for info
Agent: Deferred. Resume anytime with "q" → Deferred Flows
```

### Checking Recording

```
User: q → 📍 Check Recording
Agent: 
  Active: ✅ Yes
  Location: ~/.config/opencode/context-registry/data/questions.json
  Backup: ~/.config/opencode/questions/history/decisions.json
  Sync: Supermemory (hourly)
```

## Design Principles

1. **Transparency** - Users always know where data is stored
2. **Persistence** - Settings survive across sessions
3. **Flexibility** - Adjust behavior without restarting
4. **Recovery** - Pause and resume any flow
5. **Context-Aware** - Auto-detect and adapt to situation

## Future Enhancements

- **AI-powered suggestions** based on choice patterns
- **Cross-session learning** from Supermemory
- **Voice command integration** for hands-free control
- **Analytics dashboard** for understanding decision patterns

## Conclusion

The Q System v2.0 transforms a simple trigger into a full-featured preference management system. By making questioning adaptable, transparent, and recoverable, users gain real control over how they interact with AI agents.

The key insight: **questioning is a UI, not just a tool**. Treat it with the same design care as any other user interface.

---

*Built for OpenCode with Supermemory integration. Files synced to freshstart repository for server replication.*