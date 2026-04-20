---
pubDatetime: 2026-03-01T11:25:00Z
title: "Implementing the Context Registry: From Silent Failure to Full Recording"
postSlug: "context-registry-implementation-guide"
description: "Implementing the Context Registry: From Silent Failure to Full Recording"
tags:
  - opencode
  - ai-agents
  - tracking
  - implementation
  - context-registry
---

## The Problem: A Registry That Wasn't Recording

The Context Registry was designed to track every question tool interaction—every menu presented, every option chosen, every decision made. But when we checked the registry data, we found only **1 interaction** recorded despite weeks of usage.

This post documents the diagnosis, the fix, and the enhanced recording system we built.

## Diagnosis: Why It Wasn't Working

### Initial Investigation

```bash
cat ~/.config/opencode/context-registry/data/questions.json
```

The registry file existed. The config was correct (`tracking.questions: true`). The recording script existed. But something was missing.

### Root Cause Discovery

The system had:
- ✅ Config enabled
- ✅ Recording script ready
- ✅ Storage file prepared
- ❌ **No automatic hook to capture interactions**

The SKILL.md described hooks that *should* run:

```python
# Post-question hook (NOT IMPLEMENTED)
def after_question(question, choice):
    record_question_interaction(question, choice)
```

But OpenCode doesn't have a native "post-question hook" system. The single recorded interaction was manually added during initial setup.

### The Missing Link

Session transcripts only record **tool invocations**, not **tool results**:

```
[assistant] [tool: question]
```

The actual question text, options presented, and user's choice were never persisted anywhere searchable.

## The Fix: Adding Auto-Recording

### Step 1: Manual Recording Protocol

We first established a manual recording workflow using the existing script:

```bash
~/.config/opencode/context-registry/scripts/record-question.sh \
  <category> "<question_text>" "<choice>" <session_id> <tags>
```

Example:
```bash
~/.config/opencode/context-registry/scripts/record-question.sh \
  workflow "Next Steps" "Option A (Recommended)" ses_abc123 task,feature
```

### Step 2: AGENTS.md Integration

Added a CRITICAL section to global instructions:

```markdown
### Context Registry Recording (CRITICAL)

**After EVERY question tool invocation, record the interaction to the context registry.**
```

This ensures the recording step is part of the agent's standard workflow.

## Enhancement: Building Record-Question-V2

The original script captured basic data. We wanted more.

### What Was Missing

| Data Point | Original | Needed |
|------------|----------|--------|
| Options Presented | ❌ | ✅ All options |
| Question Description | ❌ | ✅ Full text |
| Custom Input Detection | ❌ | ✅ Flag typed answers |

### The Enhanced Script

Created `record-question-v2.sh` with expanded capabilities:

```bash
#!/bin/bash
# Usage:
./record-question-v2.sh \
  <category> "<header>" "<choice>" <session_id> "<tags>" \
  "<description>" "<option1|option2|option3>"
```

### New Features

**1. All Options Captured**
```json
"options_presented": [
  "📋 Capture All Options (Recommended)",
  "📝 Add Question Description",
  "⏱️ Decision Time Tracking",
  "✏️ Custom Input Detection",
  "✅ All Enhancements",
  "⏭️ Skip"
]
```

**2. Question Description**
```json
"question": {
  "header": "Enhance Recording",
  "description": "Which enhancements would you like to add?"
}
```

**3. Custom Input Detection**
```json
"choice": {
  "selected": ["User's typed response"],
  "is_custom_input": true
}
```

## Architecture Overview

{{< mermaid >}}
flowchart TD
    A[Question Tool Invoked] --> B[User Makes Selection]
    B --> C[Agent Receives Response]
    C --> D[Call record-question-v2.sh]
    D --> E[Update questions.json]
    E --> F[Update Analytics]
    F --> G[Sync to Supermemory]
    
    subgraph "Data Captured"
        H[Question Header]
        I[Description]
        J[All Options]
        K[User Choice]
        L[Custom Input Flag]
        M[Tags]
    end
    
    D --> H
    D --> I
    D --> J
    D --> K
    D --> L
    D --> M
{{< /mermaid >}}

## Data Structure

### Interaction Record

```json
{
  "id": "q_20260301_105507_d91o",
  "timestamp": "2026-03-01T10:55:07Z",
  "session_id": "ses_35713a6bbffeslvbvy3mw2xzR7",
  "category": "meta_controls",
  "question": {
    "header": "Enhance Recording",
    "description": "Which enhancements would you like to add?",
    "options_presented": [
      "📋 Capture All Options (Recommended)",
      "📝 Add Question Description",
      "⏱️ Decision Time Tracking",
      "✏️ Custom Input Detection",
      "✅ All Enhancements",
      "⏭️ Skip"
    ]
  },
  "choice": {
    "selected": ["📋 Capture All Options (Recommended), 📝 Add Question Description, ✏️ Custom Input Detection"],
    "is_custom_input": true
  },
  "tags": ["q", "recording", "enhance", "multi"]
}
```

### Categories

| Category | When to Use |
|----------|-------------|
| `navigation` | Menu navigation, session menu selections |
| `workflow` | Task-related decisions, implementation choices |
| `debug` | Error handling, troubleshooting choices |
| `setup` | Configuration, installation decisions |
| `skill_selection` | Choosing which skill to use |
| `confirmation` | Yes/no confirmations, proceed/stop decisions |
| `meta_controls` | Intensity changes, recording checks |

## Analytics Generated

### Most Selected Options

```json
"most_selected": {
  "🚀 Quick Start (Recommended)": 1,
  "✅ Add Auto-Recording (Recommended)": 1,
  "Check how we used to do it": 1
}
```

### Time of Day Patterns

```json
"by_time_of_day": {
  "morning": 7,
  "afternoon": 0,
  "evening": 1,
  "night": 0
}
```

### Custom Input Tracking

```json
"custom_input_count": 1
```

## Implementation Files

| File | Purpose |
|------|---------|
| `~/.config/opencode/context-registry/scripts/record-question-v2.sh` | Enhanced recording script |
| `~/.config/opencode/context-registry/data/questions.json` | Interaction storage |
| `~/.config/opencode/AGENTS.md` | Auto-recording instruction |

## Lessons Learned

### 1. Config vs. Implementation Gap

Having config flags set to `true` doesn't mean the feature works. Always verify the full implementation path.

### 2. Session Storage Limitations

Session transcripts record tool invocations, not tool results. For analytics, you need explicit recording.

### 3. Progressive Enhancement

Start with basic recording, then add features:
1. Basic: ID, timestamp, choice
2. Enhanced: Options presented, descriptions
3. Advanced: Decision timing, custom input detection

### 4. Behavior Integration

The fix only works if integrated into agent instructions. Without the AGENTS.md update, the script would never be called.

## Future Improvements

- **Decision Timing**: Track how long users take to decide
- **Option Clustering**: Group similar options for menu optimization
- **Predictive Suggestions**: Use history to predict likely choices
- **A/B Menu Testing**: Compare different option orderings

## Conclusion

The Context Registry went from 1 interaction to full recording in one session. The key was:

1. **Diagnose** why it wasn't working (missing hook)
2. **Implement** manual recording first
3. **Automate** via agent instructions
4. **Enhance** with richer data capture

The registry now builds a valuable dataset for understanding user decision patterns and improving menu design.

---

*Implementation session: March 1, 2026*
*Interactions recorded during implementation: 10*
*Script version: record-question-v2.sh*