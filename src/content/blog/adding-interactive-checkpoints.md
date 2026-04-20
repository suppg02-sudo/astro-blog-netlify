---
pubDatetime: 2026-04-10T16:00:00Z
title: "Adding Interactive Checkpoints to an AI Research Pipeline"
postSlug: "adding-interactive-checkpoints"
description: "Adding Interactive Checkpoints to an AI Research Pipeline"
tags:
  - others
---

You'll build a checkpoint-gated research pipeline where the AI presents clarifying questions at three key stages — intent, steering, and output — letting the user co-pilot research instead of watching passively.

## Prerequisites

- A research pipeline with autonomous mode already working (gathering sources, synthesising, storing results)
- A session state manager (any language — Python shown here)
- A way to present structured menus to the user (CLI, API, or question tool)

## Mental Model

Think of it like a GPS. Autonomous mode (Mode A) plots the route and drives. Interactive mode (Mode B) plots the route but pauses at three roundabouts to ask: "Still want to go this way?" The user picks direction at each gate. The engine — source gathering, eRAG indexing, synthesis — never changes. Only the decision points change.

The three checkpoints map to natural pause points in any research workflow:

1. **CP1 — Before you start**: What are you trying to learn and how deep?
2. **CP2 — Mid-flight**: Sources gathered — want to redirect or focus on gaps?
3. **CP3 — Before you store**: Synthesis looks like this — approve or adjust?

## Step 1: Define Your Checkpoint Schema

Write down what data each checkpoint captures. This is your contract — every builder function and session update will follow it.

```yaml
research_session:
  mode: "B"
  status: "cp1"
  intent: ""
  depth: ""
  output_format: ""
  priority_areas: []
  direction: ""
  quality_decision: ""
  output_actions: []
```

Each field is set by exactly one checkpoint and read by exactly one downstream stage. No overlap, no ambiguity. If a field isn't populated by a checkpoint, it doesn't exist.

## Step 2: Build a Session State Manager

Create a class that persists checkpoint data across stages. The key operations are `create`, `advance`, `update_cp1/2/3`, and `complete`.

```python
class ResearchSession:
    def create(self, topic: str, mode: str = "B") -> dict:
        session_id = slugify(topic)
        data = {
            "id": session_id,
            "mode": mode,
            "status": "complete" if mode == "A" else "cp1",
            "intent": "", "depth": "", "output_format": "",
            "priority_areas": [], "direction": "",
            "quality_decision": "", "output_actions": [],
        }
        self._save(data)
        return data

    def advance(self, session_id: str, to_stage: str) -> dict:
        data = self.get(session_id)
        data["status"] = to_stage
        return self._save(data)
```

The important detail: Mode A sessions skip straight to `"complete"`. Mode B sessions start at `"cp1"`. This single field drives the branching logic — no `if mode == "B"` checks scattered everywhere.

## Step 3: Build Checkpoint Question Generators

Each checkpoint is a function that returns structured question data. Not hardcoded strings — generated from context.

```python
def build_cp1(topic, erag_coverage="none", existing_facts=0):
    intent_options = [
        {"label": "Understand concept (Recommended)", "description": "Build knowledge, identify patterns"},
        {"label": "Find implementation patterns", "description": "Code, architecture, technical details"},
        {"label": "Evaluate for integration", "description": "Decide whether to adopt"},
        {"label": "Compare alternatives", "description": "Side-by-side analysis"},
        {"label": "Just add to knowledge base", "description": "Ingest, compile, index"},
    ]
    if erag_coverage == "full":
        intent_options.append(
            {"label": "Skip research — eRAG has full coverage",
             "description": f"eRAG has {existing_facts} facts on this topic"}
        )
    return {
        "stage": "cp1",
        "questions": [
            {"header": "Research Intent", "options": intent_options},
            {"header": "Depth & Scope", "options": [
                {"label": "Broad overview (Recommended)", "description": "Multiple sources, high-level"},
                {"label": "Deep dive", "description": "Fewer sources, thorough analysis"},
                {"label": "Targeted gap-fill", "description": "Only what's missing"},
                {"label": "Quick answer", "description": "Single best source"},
            ]},
        ],
    }
```

The pattern: build options dynamically from context (eRAG coverage, gaps detected, source count). If eRAG already has full coverage, add a skip option. If gaps are detected at CP2, turn them into priority options. The questions adapt to what the system already knows.

## Validate It Works

Run the full lifecycle: create → CP1 → CP2 → CP3 → complete. Every stage must preserve data from previous stages.

```bash
python3 research_session.py create "Kubernetes operators" --mode B
python3 research_session.py update-cp1 "kubernetes-operators" --intent "understand" --depth "deep"
python3 research_session.py advance "kubernetes-operators" cp2
python3 research_session.py update-cp2 "kubernetes-operators" --direction "continue" --priority-areas "scaling"
python3 research_session.py advance "kubernetes-operators" cp3
python3 research_session.py complete "kubernetes-operators" --erag-slug "k8s-operators"
python3 research_session.py get "kubernetes-operators"
```

The final `get` must show `status: "complete"` with all CP fields populated. If any field is null, the checkpoint didn't save.

## Mistakes I Made

**Building a standalone script instead of integrating into the existing pipeline**: The first version was a monolithic `interactive_research.py` that tried to do everything — ingestion, web fetching, synthesis. It duplicated existing code and broke when the pipeline changed. The right approach: the session manager and checkpoint builders are thin coordination layers. The actual research engine never changes.

**Hardcoding questions**: Early versions had questions baked into the SKILL.md as static text. When eRAG already had full coverage on a topic, the questions were still "what do you want to research?" — useless. Dynamic generation from context (coverage level, gap list, source count) makes checkpoints relevant every time.

**Forgetting Mode A backward compatibility**: Adding `if mode == "B"` checks throughout the research workflow created fragile branching. Instead, a single `status` field handles it: Mode A sessions start at `"complete"`, Mode B at `"cp1"`. The pipeline checks status, not mode. One field, zero conditionals.

## Taking It Further

This pattern — thin checkpoint layer over an autonomous pipeline — applies beyond research. Any multi-stage AI workflow benefits from user steering gates: data processing pipelines, code generation workflows, content creation pipelines. The schema is always the same: define checkpoint data fields, build a state manager, generate questions from context, and let the existing engine do the real work.

---

**Tags**: ai-agents, research-pipeline, interactive-research, checkpoint-gates, python
**Categories**: AI Automation, Tutorials