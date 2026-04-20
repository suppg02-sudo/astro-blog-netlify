---
pubDatetime: 2026-02-10T23:17:51Z
title: "Entire CLI - AI Agent Workflow Integration Tool"
postSlug: "entire-cli-ai-agent-workflow-integration"
description: "Entire CLI - AI Agent Workflow Integration Tool"
tags:
  - AI
  - automation
  - cli-tools
  - git
  - development
  - cli
  - workflow
  - tools
  - anthropic
---

## Executive Summary

Entire CLI is a powerful Git workflow integration tool that captures AI agent sessions, checkpoints, and creates searchable records of development work. Designed for teams using Claude Code or other AI-assisted coding workflows, it bridges the gap between AI conversations and version control.

---

## Mermaid Diagram

{{< mermaid >}}
flowchart TD
    A[Entire CLI] --> B[Core Capabilities]
    A --> C[Session Management]
    A --> D[Checkpoint System]
    A --> E[Git Integration]
    A --> F[Multi-Agent Support]
    
    B --> B1[Session Capture]
    B --> B2[Prompts & Responses]
    B --> B3[Files Modified]
    B --> B4[Timestamps]
    
    C --> C1[Manual-Commit Strategy]
    C --> C2[Auto-Commit Strategy]
    C --> C3[Checkpoint Storage]
    C --> C4[Separate Branch]
    
    D --> D1[Claude Code Support]
    D --> D2[Gemini CLI Support]
    D --> D3[Git Hooks Integration]
    
    E --> E1[Background Service]
    E --> E2[Session Indexing]
    E --> E3[Searchable Records]
    
    F --> F1[Worktree Integration]
    F --> F2[Concurrent Sessions]
    F --> F3[Independent Tracking]
    
    style A fill:#2563eb
    style B fill:#dc3545
    style C fill:#28a745
    style D fill:#ffc107
    style E fill:#17a2b8
    style F fill:#1f77b6
{{< /mermaid >}}

---

## What is Entire CLI?

Entire is a command-line interface tool that hooks into your Git workflow to automatically capture AI agent sessions. Every time you or your AI agent interacts with your codebase, Entire records:

- All prompts and responses
- Files created or modified
- Precise timestamps
- Session metadata

This creates a comprehensive, searchable history of your development work that's indexed alongside your Git commits.

---

## Key Features

### 1. Multi-Agent Support
- **Claude Code CLI**: Native support (requires `claude` command)
- **Gemini CLI**: Alternative option (experimental, use `--agent gemini`)
- **Concurrent Sessions**: Run multiple AI sessions simultaneously without conflicts

### 2. Intelligent Checkpointing
- **Manual-Commit Strategy**: Checkpoints created when you commit manually
- **Auto-Commit Strategy**: Checkpoints created automatically after each AI response
- **Checkpoint Rewind**: Jump back to any previous state in your session

### 3. Searchable Session History
- **Session Indexing**: All sessions indexed alongside Git commits
- **Full Metadata**: Prompts, responses, files touched, timestamps
- **Git Worktree Integration**: Each worktree maintains independent session tracking

### 4. Seamless Git Integration
- **Separate Branch**: `entire/checkpoints/v1` branch for session data
- **Clean Main Branch**: Your code commits stay clean
- **Non-Destructive**: Worktrees don't interfere with your git history
- **Hooks-Based**: Git hooks handle session capture automatically

### 5. Smart Strategies
- **Auto-Commit**: Creates checkpoints after every AI response (default)
- **Manual-Commit**: Creates checkpoints only when you commit (safer)
- **Safe on Main**: Auto-commit works safely on feature branches
- **Telemetry Optional**: Optional anonymous usage statistics

---

## How It Works

### Session Architecture

```
Your Branch                entire/checkpoints/v1
     │                                  │
     ▼                                  │
[Base Commit] ────┐           │
     │                                  │
     │                                  │
     ▼                                  │
     ▼                                  │
[Your Commit] ─────────► [Session Metadata]
     │                           (transcript, prompts,
     │                            files touched)
     ▼                                  │
```

### Session ID Format

Each session gets a unique ID:
- **Format**: `YYYY-MM-DD-<UUID>` (e.g., `2026-02-10-a3b2c4d5e6f7`)
- **Purpose**: Uniquely identifies sessions across worktrees and branches
- **Stored**: Separate from commit hash for independent tracking

### Workflow Integration

Entire integrates with your existing Git workflow through:

1. **Git Hooks**: Pre-commit and post-commit hooks capture session data
2. **Git Worktrees**: Each AI session works in its own worktree
3. **Branch Strategy**: Session data lives on separate branch, keeping your main clean

### Automatic vs Manual Modes

| Mode              | When Checkpoints Created | Use Case |
|------------------|-----------------------|-----------|
| **Auto-Commit** | After each AI response | Active development, frequent AI interactions |
| **Manual-Commit** | Only when you commit | Careful code reviews, testing phases |

---

## Quick Start

### Installation

```bash
# Install via Homebrew (macOS)
brew tap entireio/tap
brew install entireio/tap/entire

# Install via Go (cross-platform)
go install github.com/entireio/cli/cmd/entire@latest

# Enable in your repository
cd your-project && entire enable
```

### First Time Setup

```bash
# Check status
entire status

# Choose strategy (recommended for teams)
entire enable --strategy manual-commit

# Configure agent (Claude Code or Gemini CLI)
entire enable --agent claude  # or --agent gemini
```

### Basic Commands

```bash
# Start working session
entire start  # Or just use Claude Code CLI normally

# Check current session status anytime
entire status

# Rewind to previous checkpoint
entire rewind

# Resume latest session
entire resume

# Disable Entire (removes hooks)
entire disable
```

---

## Command Reference

### Core Commands

| Command | Description | Example |
|---------|-------------|---------|
| `entire enable` | Install hooks and enable Entire | `entire enable --strategy auto-commit` |
| `entire status` | Show current session and strategy | `entire status` |
| `entire rewind` | List and restore checkpoints | `entire rewind` |
| `entire resume` | Restore latest session metadata | `entire resume <branch>` |
| `entire start` | Begin a new session | `entire start` |
| `entire disable` | Remove hooks from repository | `entire disable` |

### Configuration Flags

| Flag | Description | Default |
|-------|-------------|--------|
| `--agent <name>` | AI agent to use | `claude` |
| `--strategy <name>` | Checkpoint strategy | `auto-commit` |
| `--force` | Force reinstall hooks | - |
| `--local` | Use local settings file | - |
| `--skip-push-sessions` | Disable automatic session pushing | - |

### Session Management Commands

```bash
# View all sessions in current worktree
entire sessions list

# View session details
entire sessions show <session-id>

# Search sessions by keyword
entire sessions search "authentication issue"
```

---

## Configuration

### Project Settings (settings.json)

```json
{
  "strategy": "auto-commit",
  "agent": "claude",
  "enabled": true
}
```

### Local Override (settings.local.json)

```json
{
  "enabled": false,
  "log_level": "debug"
}
```

### Strategy Options

| Strategy | Description | Pros | Cons |
|-----------|-------------|------|-------|
| **manual-commit** | Checkpoints only when you commit | - Clean git history<br>- Full control over checkpoints<br>- Slower workflow<br>- Manual effort required | - No automatic checkpointing<br>- Forgetting to commit creates gaps |
| **auto-commit** | Checkpoints after every AI response | - Never miss capturing work<br>- Automatic documentation<br>- Faster feedback loop | - More commits on main branch<br>- Checkpoints may include incomplete work<br>- Harder to undo specific changes |

---

## Use Cases

### 1. Solo Developer Workflows

**Scenario**: Individual developer using AI to write code

**Workflow**:
```bash
# Start session
entire start

# Work with Claude Code CLI normally
# Write code, get suggestions, make changes
```

**Benefits**:
- Automatic capture of all AI interactions
- Checkpoints let you rewind if AI makes a mistake
- Searchable history of your development decisions
- Clean separation of AI conversations from code commits

### 2. Team Collaboration

**Scenario**: Multiple developers using same codebase with different AI sessions

**Workflow**:
```bash
# Each developer enables Entire
cd /project && entire enable --strategy manual-commit

# Each works in their own session
# Sessions are tracked independently per worktree
```

**Benefits**:
- Non-conflicting AI sessions using Git worktrees
- Independent checkpoint management per developer
- Team-wide searchable history of all AI-assisted work
- Clear attribution of who contributed what code

### 3. AI-Assisted Code Review

**Scenario**: Using AI to review and refactor code

**Workflow**:
```bash
# Review phase
entire start
# Use Claude to analyze codebase
# Get suggestions, review findings

# Implementation phase
# Make changes suggested by AI
# Commit manually (manual-commit strategy)
entire rewind  # Review checkpoint
entire resume  # Continue from that point
```

**Benefits**:
- AI analysis captured as part of session
- Checkpoints preserve code review states
- Easy rollback if AI suggestions introduce bugs
- Comprehensive audit trail of review process

### 4. Debugging & Troubleshooting

**Scenario**: Investigating a bug across multiple commits

**Workflow**:
```bash
# Start session with debug logging
export ENTIRE_LOG_LEVEL=debug
entire start

# Reproduce bug
# Work with Claude to investigate issue

# Review session history
entire sessions list
entire sessions show <session-id>
```

**Benefits**:
- Session history includes all context from AI interactions
- Checkpoints capture exact state at each step
- Debug logs capture detailed information
- Easy to identify when bug was introduced

---

## Advanced Features

### Git Worktree Integration

Each worktree maintains independent session tracking, enabling:

- **Multiple AI agents** on same codebase without conflicts
- **Team collaboration** with separate session histories
- **Branch isolation** between AI sessions and code
- **Concurrent development** without workflow interference

### Auto-Summarization

When enabled, Entire automatically generates AI summaries at checkpoint time:

```json
{
  "strategy_options": {
    "summarize": {
      "enabled": true
    }
  }
}
```

**Summary includes**:
- Intent: What was the AI agent trying to accomplish?
- Outcome: What was achieved?
- Learnings: What insights were gained?
- Open Items: Questions or issues to address later

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|--------|----------|
| Not a Git repository | Navigate to your Git repository first |
| Entire is disabled | Run `entire enable` to re-enable hooks |
| No checkpoints found | Ensure you or AI has made at least one commit (manual-commit) or response (auto-commit) |
| Shadow branch conflicts | Run `entire reset --force` to clear shadow branch |
| SSH authentication errors | Add GitHub host keys to `~/.ssh/known_hosts` |

### Debug Mode

```bash
# Enable debug logging
export ENTIRE_LOG_LEVEL=debug
entire status

# Check detailed logs
cat ~/.entire/logs/entire.log
```

### Resetting Entire State

```bash
# Reset to clean state (use with caution)
entire reset --force

# Re-enable after reset
entire enable --force
```

---

## Comparison with Alternatives

| Feature | Entire CLI | Aider | Copilot |
|-----------|-----------|--------|----------|
| Git Integration | ✓ Native worktrees | ✗ Basic | ✗ Basic |
| Session Capture | ✓ Automatic hooks | ✗ Manual | ✗ Manual |
| Checkpointing | ✓ Automatic & manual | ✗ Limited | ✗ None |
| Multi-Agent | ✓ Concurrent sessions | ✗ Single | ✗ Limited |
| Cost | Open Source (MIT) | Free | Free | Subscription |

---

## Best Practices

### For Individuals

1. **Start with Manual-Commit**: If you're unsure, use manual-commit strategy to maintain control
2. **Commit Before Major Changes**: Create clear checkpoints before significant refactoring
3. **Use Session Search**: Regularly search sessions for context on past decisions
4. **Enable Auto-Summarization**: Save time with AI-generated summaries
5. **Keep Main Clean**: Use `manual-commit` strategy if team workflow requires clean main

### For Teams

1. **Use Git Worktrees**: Each developer gets their own session isolation
2. **Coordinate Strategies**: Agree on checkpoint strategy (auto vs manual) as a team
3. **Separate Branches**: Keep session data on dedicated branch
4. **Document Workflows**: Create internal docs on when/how your team uses Entire
5. **Regular Review**: Periodically review session history for process improvements

---

## Development & Contributing

### Building from Source

```bash
# Clone repository
git clone https://github.com/entireio/cli

# Install dependencies (requires mise)
curl https://mise.run | sh
mise install

# Build CLI
mise run build

# Run tests
mise run test
```

### Getting Help

```bash
# General help
entire --help

# Command-specific help
entire <command> --help
```

### Reporting Issues

Found a bug or have a feature request? Report issues at:
https://github.com/entireio/cli/issues

---

## Conclusion

Entire CLI represents a thoughtful approach to AI-assisted development workflows. By capturing the interaction between human developers and AI agents, it creates a rich, searchable history that bridges the gap between AI conversations and version control.

**Key strengths:**
- Seamless Git integration without dirty commits
- Flexible checkpointing strategies for different workflows
- Support for multiple AI agents
- Non-intrusive session capture
- Comprehensive command set and configuration options

**Best for:**
- Teams using AI-assisted coding workflows
- Projects requiring detailed audit trails
- Development processes that benefit from session replay

---

## Resources

- **GitHub Repository**: https://github.com/entireio/cli
- **Documentation**: https://github.com/entireio/cli#readme
- **Issues**: https://github.com/entireio/cli/issues
- **MIT License**: https://github.com/entireio/cli/blob/main/LICENSE
- **Claude Code CLI**: https://docs.anthropic.com/en/docs/claude-code
- **Gemini CLI**: https://github.com/google-gemini/gemini-cli

---

**Published Blog Post**: http://ubuntu58-1:1314/posts/entire-cli-ai-agent-workflow-integration/