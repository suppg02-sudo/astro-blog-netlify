---
pubDatetime: 2026-02-08T18:01:00Z
title: "OpenCode Mid-Session Model Switching: How to Delegate Tasks to Different AI Models"
postSlug: "opencode-mid-session-model-switching"
description: "OpenCode Mid-Session Model Switching: How to Delegate Tasks to Different AI Models"
tags:
  - opencode
  - task-tool
  - ai-agents
  - subagents
  - context7
  - model-switching
---

## The Problem

When working with OpenCode, you're locked into whatever model started the session. If you're on Claude Opus and want GPT-5.2 to handle a specific subtask, or you want GLM-4.7 for a quick analysis, you're stuck. The conventional wisdom is: edit `opencode.json`, restart, lose your session context.

But is that actually true?

## The Investigation

Using Context7 to query the OpenCode source code directly, I read the actual Task tool implementation at `packages/opencode/src/tool/task.ts`. The critical discovery was in how the Task tool resolves which model to use.

### What the Source Code Reveals

The Task tool accepts a `subagent_type` parameter. The common assumption is this only accepts built-in types like `general`, `explore`, or `CoderAgent`. But the actual code does something more flexible:

```typescript
const agent = await Agent.get(params.subagent_type)
if (!agent) throw new Error(`Unknown agent type: ${params.subagent_type} is not a valid agent type`)
```

`Agent.get()` looks up **any agent by name** from the configuration - not just built-in ones. This means custom agents defined in `opencode.json` are valid targets for the Task tool.

### The Model Resolution Logic

Here's where it gets interesting. After resolving the agent, the Task tool decides which model to use:

```typescript
const model = agent.model ?? {
  modelID: msg.info.modelID,
  providerID: msg.info.providerID,
}
```

This is a simple null coalescing check:
- If the agent has its own `model` field defined, **use that model**
- If not, inherit the parent session's model

The OpenCode documentation confirms this:

> "If you don't specify a model, primary agents use the globally configured model, while subagents inherit the model of the primary agent that invoked them."

## The Solution: Pre-Configured Model Subagents

Define subagents with specific model assignments in `opencode.json`:

```json
{
  "agent": {
    "use-opus": {
      "mode": "subagent",
      "model": "anthropic/claude-opus-4-6",
      "description": "Delegate task to Claude Opus 4.6"
    },
    "use-gpt5": {
      "mode": "subagent",
      "model": "openai/gpt-5.2",
      "description": "Delegate task to GPT-5.2"
    },
    "use-glm": {
      "mode": "subagent",
      "model": "zhipuai-coding-plan/glm-4.7",
      "description": "Delegate task to GLM 4.7"
    }
  }
}
```

Then delegate mid-session:

```
Task(subagent_type="use-opus", prompt="Analyse this code for security vulnerabilities")
Task(subagent_type="use-gpt5", prompt="Generate test cases for this function")
```

Each delegation runs on the specified model, not the parent session's model. The result flows back to your current session seamlessly.

## What This Enables

### Multi-Model Workflows

You can now orchestrate tasks across different models within a single session:

1. **Primary session** on Claude Opus for complex reasoning
2. **Delegate** code review to GPT-5.2 for a second opinion
3. **Delegate** quick analysis to GLM-4.7-flash for speed
4. Results from all three models available in your session

### Cost Optimisation

Route tasks to the right model for the job:
- Expensive reasoning models for architecture decisions
- Faster, cheaper models for boilerplate generation
- Specialised models for domain-specific tasks

### A/B Testing Responses

Ask the same question to two different models and compare their answers, all within one session.

## Limitations

There are real constraints to be aware of:

- **Pre-configuration required**: You must define the model-specific subagents in `opencode.json` before the session starts. You cannot dynamically create agents mid-session.
- **No shared context**: Each Task delegation starts a fresh session. The subagent doesn't see your conversation history (unless you include relevant context in the prompt).
- **Session overhead**: Each delegation creates a new sub-session, which adds latency compared to direct execution.
- **Provider credentials**: The target model's provider must be configured with valid API keys in `opencode.json`.

## Available Models

OpenCode exposes 156 models across 6 providers. Run `opencode models` to see the full list, or filter by provider:

```bash
opencode models anthropic    # Claude family
opencode models openai       # GPT family
opencode models google       # Gemini family
opencode models opencode     # OpenCode hosted models
```

## Configuration Reference

### Agent Definition Schema

```json
{
  "agent": {
    "agent-name": {
      "mode": "subagent",
      "model": "provider/model-id",
      "description": "What this agent does",
      "prompt": "Optional system prompt",
      "temperature": 0.3,
      "steps": 10,
      "hidden": true,
      "tools": {
        "write": true,
        "edit": true,
        "bash": true
      },
      "permission": {
        "task": {
          "*": "deny"
        }
      }
    }
  }
}
```

Key fields:
- **mode**: Must be `"subagent"` for Task tool invocation
- **model**: `"provider/model-id"` format - this is what enables model switching
- **hidden**: Set to `true` to hide from autocomplete (still invocable by Task tool)
- **steps**: Limit the number of tool calls the subagent can make
- **tools**: Control which tools the subagent can access

### Changing the Default Session Model

For changing which model starts new sessions (not mid-session switching):

```bash
# Edit the "model" field in opencode.json
# Takes effect on next session
vi /root/.config/opencode/opencode.json

# Or start a one-off session on a different model
opencode run -m anthropic/claude-opus-4-6 "your prompt"
```

## How This Was Discovered

This finding came from reading the actual OpenCode source code via Context7 (`/anomalyco/opencode`), specifically:

- `packages/opencode/src/tool/task.ts` - Task tool implementation
- `packages/opencode/src/tool/task.txt` - Task tool description template
- `packages/web/src/content/docs/agents.mdx` - Agent configuration documentation

The documentation mentions per-agent model overrides, but doesn't explicitly connect it to mid-session model switching. The source code makes the mechanism clear: the Task tool respects the agent's `model` field, and `subagent_type` accepts any configured agent name.

## Summary

Mid-session model switching in OpenCode is possible through pre-configured subagents with model overrides. Define your model-specific agents in `opencode.json`, then delegate to them via the Task tool. Each delegation runs on the specified model and returns results to your current session.

The key insight: `subagent_type` is not limited to built-in agent types. It accepts any agent name from your configuration, and if that agent has a `model` field, the Task tool uses it.