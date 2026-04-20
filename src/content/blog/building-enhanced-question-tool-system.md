---
pubDatetime: 2026-03-05T00:00:00Z
title: "Building an Enhanced Question Tool System: Templates, Workflows, and AI-Powered Suggestions"
postSlug: "building-enhanced-question-tool-system"
description: "Building an Enhanced Question Tool System: Templates, Workflows, and AI-Powered Suggestions"
tags:
  - opencode
  - question-tool
  - automation
  - templates
  - ai-infrastructure
  - workflow
  - python
---

We just completed a major enhancement to the OpenCode question tool system. What started as a brainstorming session evolved into a complete 3-phase implementation project with 13 new files and ~2,500 lines of code. Here's how we built it.

## The Problem

The question tool is central to how we interact with AI agents. But we were asking the same types of questions repeatedly, navigating multi-step workflows manually, and lacking intelligent suggestions based on context.

We needed:
- **Reusable templates** for common question patterns
- **Chained workflows** for multi-step decision processes
- **Smart suggestions** that adapt to context (with the ability to dial it down when too much)
- **Auto-complete** for faster input

## The Solution: 3-Phase Implementation

### Phase 1: Question Templates

**Goal:** Create reusable question templates that can be loaded, customized, and shared across sessions.

We built a complete template system with:

| Component | Purpose |
|-----------|---------|
| **Template Schema** | YAML schema defining template structure |
| **Template Loader** | Python script to load and convert templates to question tool format |
| **Default Templates** | 3 templates (decision, prioritization, feedback) |
| **Registry** | Auto-generated JSON registry of all templates |

**Template Schema (simplified):**

```yaml
id: decision-simple
name: Simple Decision
description: Binary yes/no/maybe decision with optional notes
version: 1.0.0
tags: [decision, simple, binary, defer]

question:
  header: Decision
  text: |
    ## 🎯 Decision Required
    
    **Context**: {context}
    
    What would you like to do?
  multiple: true
  options:
    - label: "Yes, proceed"
      description: "Commit to this decision"
      value: "yes"
      icon: "✅"
    
    - label: "Maybe, defer"
      description: "Save for later review"
      value: "maybe"
      icon: "⏸️"
    
    - label: "No, skip"
      description: "Don't proceed"
      value: "no"
      icon: "❌"
```

**Usage:**

```bash
# List templates
python3 ~/.config/opencode/questions/scripts/template_loader.py list

# Use template with context
python3 ~/.config/opencode/questions/scripts/template_loader.py use decision-simple context="Deploy to production?"
```

**Output:**

```json
{
  "questions": [{
    "header": "Decision",
    "question": "🎯 Decision Required\n\n**Context**: Deploy to production?\n\nWhat would you like to do?",
    "multiple": true,
    "options": [
      {"label": "✅ Yes, proceed", "description": "Commit to this decision"},
      {"label": "⏸️ Maybe, defer", "description": "Save for later review"},
      {"label": "❌ No, skip", "description": "Don't proceed"}
    ]
  }]
}
```

### Phase 2: Chained Questions

**Goal:** Create workflows where each answer triggers the next contextual question.

We implemented a complete workflow system with:

| Component | Purpose |
|-----------|---------|
| **Chain Schema** | YAML schema defining workflow steps and branches |
| **Chain Executor** | Python script with state management and conditional branching |
| **Example Chains** | 2 workflows (deployment, feature-approval) |
| **History Tracking** | Execution logs with full state history |

**Chain Definition (simplified):**

```yaml
id: deployment-workflow
name: Deployment Workflow
description: Guided deployment decision workflow
version: 1.0.0

steps:
  - id: confirm-deploy
    template: decision-simple
    context:
      context: "Ready to deploy to {environment}?"
    on_answer:
      save_to: deploy_decision
    branches:
      - when: "'yes' in str(answer)"
        next: select-strategy
      - when: "'maybe' in str(answer)"
        next: defer-reason
      - when: "default"
        next: cancel-deployment
  
  - id: select-strategy
    template: decision-simple
    context:
      context: "Select deployment strategy for {environment}"
    on_answer:
      save_to: strategy
    branches:
      - when: "default"
        next: confirm-final
```

**Key Features:**

- **State Management**: Variables persist across steps
- **Conditional Branching**: Python expressions for routing logic
- **Context Interpolation**: `{variable}` syntax for dynamic content
- **History Tracking**: Every step logged with timestamps

**Usage:**

```bash
# Start chain
python3 ~/.config/opencode/questions/scripts/chain_executor.py start deployment-workflow environment=production

# Execute step with answer
python3 ~/.config/opencode/questions/scripts/chain_executor.py step deployment-workflow confirm-deploy "yes" environment=production
```

### Phase 3: Smart Generation with Intensity Controls

**Goal:** Use AI to suggest optimal questions based on context, with the ability to dial it down when too much.

This was the key requirement — smart suggestions that don't overwhelm.

**Intensity Levels:**

| Level | Behavior | Output |
|-------|----------|--------|
| **off** | No smart generation | None |
| **minimal** | Template only | suggested_template |
| **normal** | Template + context | + stage, mode, errors |
| **verbose** | Full analysis | + alternatives, complexity, history |

**Components:**

| Component | Purpose |
|-----------|---------|
| **Context Analyzer** | Detects task type, errors, stage, complexity |
| **Question Generator** | Suggests templates based on context |
| **Intensity Controls** | Off/Minimal/Normal/Verbose levels |
| **Config Persistence** | Saves intensity preference |

**Context Analysis:**

```python
def analyze_session(self, messages: List[Dict]) -> Dict:
    return {
        "active_task": self._detect_active_task(messages),
        "recent_errors": self._detect_errors(messages),
        "stage": self._detect_stage(messages),
        "intensity": self._suggest_intensity(messages),
        "mode": self._suggest_mode(messages),
        "context_summary": self._summarize_context(messages),
        "complexity_score": self._calculate_complexity(messages)
    }
```

**Usage:**

```bash
# Set intensity
python3 ~/.config/opencode/questions/scripts/question_generator.py set-intensity minimal

# Generate question
python3 ~/.config/opencode/questions/scripts/question_generator.py generate "implement feature"

# Output (minimal mode)
{
  "suggested_template": "decision-simple",
  "task": "implement feature",
  "stage": "exploration",
  "mode": "explore"
}

# Output (verbose mode)
{
  "suggested_template": "decision-simple",
  "task": "implement feature",
  "context_summary": "implement, feature, question, templates",
  "suggested_mode": "build",
  "suggested_intensity": "verbose",
  "stage": "implementation",
  "errors": [],
  "complexity_score": 2.5,
  "alternatives": ["prioritization-list"]
}
```

### Quick Win: Auto-Complete

**Goal:** Fuzzy match user input to available options.

We implemented a fuzzy matching algorithm that handles:
- Partial matches ("bui" → "Build: Templates")
- Character sequences in order ("b c" → "Build: Chained Questions")
- Emoji prefixes ("✅ Build" matched by "bui")
- Score-based ranking

**Usage:**

```bash
# Test autocomplete
python3 ~/.config/opencode/questions/scripts/autocomplete.py "bui temp"

# Output
Input: 'bui temp'

Top suggestions:
1. ✅ Build: Templates (score: 0.80)
2. ❌ Skip: Rating System (score: 0.34)

Best match: ✅ Build: Templates
```

## File Structure

```
~/.config/opencode/questions/
├── templates/
│   ├── template.schema.yaml         # Schema definition
│   ├── decision-simple.yaml          # Decision template
│   ├── prioritization-list.yaml      # Prioritization template
│   ├── feedback-request.yaml         # Feedback template
│   ├── registry.json                 # Auto-generated registry
│   └── custom/                       # User custom templates
├── chains/
│   ├── chain.schema.yaml            # Chain schema
│   ├── deployment-workflow.yaml     # Deployment workflow
│   ├── feature-approval.yaml        # Feature approval workflow
│   └── custom/                      # User custom chains
├── scripts/
│   ├── template_loader.py           # Template loader CLI
│   ├── chain_executor.py            # Chain executor CLI
│   ├── context_analyzer.py          # Context analyzer
│   ├── question_generator.py        # AI question generator
│   └── autocomplete.py              # Auto-complete logic
├── history/
│   └── chains/                      # Chain execution logs
└── smart-gen-config.json            # Smart generation config
```

## Statistics

| Metric | Value |
|--------|-------|
| **Total Files** | 13 |
| **Total Lines** | ~2,500 |
| **Templates** | 3 |
| **Chains** | 2 |
| **Scripts** | 5 |
| **Intensity Levels** | 4 |

## Key Takeaways

1. **Templates save time** — Define once, use everywhere with context interpolation
2. **Chains enable complex workflows** — State management + conditional branching = powerful decision trees
3. **Intensity controls are critical** — Smart suggestions are great, but sometimes you just want simplicity
4. **Auto-complete improves UX** — Fuzzy matching makes selection faster
5. **Schema-driven design scales** — YAML schemas make it easy to add new templates and chains

## What's Next

The system is complete and operational. Future enhancements could include:
- **Template marketplace** for sharing templates
- **Visual chain builder** with drag-and-drop
- **AI-powered chain generation** from natural language
- **Analytics dashboard** for question effectiveness

---

**All code is tested and operational.** The question tool enhancement plan document is available at `~/.config/opencode/docs/instructions/question-tool-enhancement-plan.md` (942 lines of comprehensive documentation).