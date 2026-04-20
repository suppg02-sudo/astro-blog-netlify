---
pubDatetime: 2026-02-13T08:00:00Z
title: "OpenCode Question Tool: A Complete Reference Guide"
postSlug: "opencode-question-tool-guide"
description: "OpenCode Question Tool: A Complete Reference Guide"
tags:
  - opencode
  - ai-agents
  - documentation
  - tools
---

## Overview

The **question tool** in OpenCode is one of the most powerful built-in tools for creating interactive AI experiences. It enables your AI agents to pause execution and ask users for input through a structured, interactive interface with multiple-choice options and custom text responses.

## What Makes the Question Tool Unique

Unlike one-way AI interactions where you provide a prompt and receive a response, the question tool transforms the relationship into a true dialogue. Your AI agent can:

- **Gather user preferences** at critical decision points
- **Clarify ambiguous instructions** by asking follow-up questions
- **Get decisions on implementation choices** as it works through a task
- **Offer choices** about what direction to take next

## How the Question Tool Works

The question tool presents a series of questions with predefined options and allows users to:

1. Select from multiple-choice options
2. Provide custom text responses by selecting "Other"
3. Select multiple answers when `multiSelect: true`
4. Navigate between multiple questions before submitting

### User Interaction Flow

When an agent calls the question tool:

1. **Questions appear** in the interface (single or multiple questions)
2. **User selects options** using keyboard or mouse
3. **Custom input allowed** - users can always type a custom answer via the "Other" option (unless disabled)
4. **Confirmation screen** shows all selected answers
5. **Agent continues** with the user's responses

## Configuration and Usage

### Basic Structure

```json
{
  "question": "What framework would you prefer?",
  "header": "Framework Choice",
  "options": [
    {
      "label": "React",
      "description": "Popular UI library with strong ecosystem"
    },
    {
      "label": "Vue",
      "description": "Progressive framework with gentle learning curve"
    },
    {
      "label": "Svelte",
      "description": "Compiler-based framework with minimal overhead"
    }
  ],
  "multiple": false,
  "custom": true
}
```

### Configuration Parameters

| Parameter | Type | Required | Purpose |
|-----------|------|----------|---------|
| `question` | string | Yes | The full question text displayed to user |
| `header` | string | Yes | Short label (max 30 chars) appearing as tab/chip |
| `options` | array | Yes | Array of choice objects with label and description |
| `multiple` | boolean | No | Allow multi-select mode (default: false) |
| `custom` | boolean | No | Allow "Other" custom input (default: true) |

### Option Structure

Each option must have:

```json
{
  "label": "Option Name",
  "description": "Explanation of what this option means"
}
```

Keep labels to 1-5 words for clarity. Descriptions should explain the trade-offs or implications of each choice.

## Advanced Features

### Multi-Select Mode

Enable multiple selections:

```json
{
  "question": "Which features do you need?",
  "multiple": true,
  "options": [...]
}
```

Users can toggle multiple options on/off before submitting.

### Recommended Options

Highlight the best choice for most users:

```json
{
  "label": "React (Recommended)",
  "description": "Most popular choice with largest ecosystem"
}
```

Place recommended options first in the list.

### Multiple Questions

Present multiple questions in sequence:

```json
[
  {
    "question": "What framework?",
    "header": "Framework",
    "options": [...]
  },
  {
    "question": "Which styling approach?",
    "header": "Styling",
    "options": [...]
  }
]
```

Users navigate between questions using left/right arrows before the final confirmation screen.

### Disable Custom Input

For strict choices where custom input isn't appropriate:

```json
{
  "custom": false,
  "options": [...]
}
```

## Practical Use Cases

### 1. Project Setup Wizard

```json
{
  "question": "Choose your project type",
  "header": "Project Type",
  "options": [
    { "label": "Full-stack web app", "description": "Frontend + API" },
    { "label": "API only", "description": "Backend without UI" },
    { "label": "Static website", "description": "HTML/CSS/JS only" }
  ]
}
```

### 2. Feature Configuration

```json
{
  "question": "What features should we enable?",
  "header": "Features",
  "multiple": true,
  "options": [
    { "label": "Authentication", "description": "User login system" },
    { "label": "Database", "description": "Data persistence" },
    { "label": "API Documentation", "description": "OpenAPI/Swagger" }
  ]
}
```

### 3. Decision Workflow

```json
{
  "question": "What's your priority?",
  "header": "Priority",
  "options": [
    { "label": "Performance (Recommended)", "description": "Optimize for speed" },
    { "label": "Developer experience", "description": "Easy to maintain" },
    { "label": "Cost efficiency", "description": "Minimize expenses" }
  ]
}
```

## Best Practices

1. **Keep it focused** - Ask one thing per question
2. **Provide context** - Use descriptions to explain implications
3. **Lead with recommendations** - Put best choice first with "(Recommended)" label
4. **Keep options concise** - 2-5 options work best
5. **Enable custom input** - Allow "Other" unless you have strict requirements
6. **Use multi-select sparingly** - Only when multiple selections make sense
7. **Group related questions** - Use multiple questions in sequence for workflows

## Integration with OpenCode

The question tool is a **built-in OpenCode tool** - no configuration or permissions needed. It's enabled by default in all OpenCode sessions and can be used by any agent.

Permission configuration:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "question": "allow"
  }
}
```

## API Details

### HTTP Routes

- `GET /question` - List pending questions
- `POST /question/:requestID/reply` - Submit answers
- `POST /question/:requestID/reject` - Dismiss question

### SDK Integration

```typescript
const opencode = new OpenCode();
const questions = await opencode.question.list();
await opencode.question.reply({ requestID, answers });
```

## Common Patterns

### Confirmation Before Action

```json
{
  "question": "Are you ready to deploy to production?",
  "header": "Deploy Confirmation",
  "options": [
    { "label": "Yes, deploy now", "description": "Proceed with deployment" },
    { "label": "Review changes first", "description": "Show me what will change" },
    { "label": "Cancel", "description": "Don't deploy yet" }
  ]
}
```

### Guided Workflow

Chain multiple questions to guide users through a process:

1. **Question 1**: Choose project type
2. **Question 2**: Select features based on type
3. **Question 3**: Configure advanced options
4. **Confirmation**: Review all selections

## Troubleshooting

### Custom Input Not Showing

Ensure `custom: true` (it's the default):

```json
{ "custom": true }  // Enables "Other" option
```

### Multi-Select Not Working

Set `multiple: true` for checkbox behavior:

```json
{ "multiple": true }
```

### Questions Not Appearing

Verify the question array is properly formatted with all required fields: `question`, `header`, and `options`.

## Conclusion

The question tool transforms OpenCode from a monologue into a conversation. By using it strategically in your agent workflows, you can:

- Create guided experiences for complex setups
- Gather precise user preferences
- Build interactive tools beyond code generation
- Implement decision workflows and confirmations

Explore using the question tool to make your OpenCode workflows more interactive and user-friendly!

---

**Source**: [OpenCode Official Tools Documentation](https://opencode.ai/docs/tools/#question)