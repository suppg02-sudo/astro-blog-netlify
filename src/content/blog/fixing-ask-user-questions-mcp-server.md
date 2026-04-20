---
pubDatetime: 2026-02-20T18:00:00Z
title: "Fixing and Testing the AskUserQuestions MCP Server"
postSlug: "fixing-ask-user-questions-mcp-server"
description: "Fixing and Testing the AskUserQuestions MCP Server"
tags:
  - testing
  - development
  - mcp
  - troubleshooting
---

Recently, I needed to fix and test the `ask-user-questions` MCP server on my system. This server provides a dual-process architecture for asking users interactive questions during AI execution. Here's the complete fix process and test results.

## Problem Statement

The `ask-user-questions` MCP server was disabled in my OpenCode configuration, preventing agents from using the `ask_user_questions` tool to gather user preferences or clarify requirements during execution. Additionally, the session directory contained 12+ orphaned sessions from previous test runs.

## Architecture Overview

The AskUserQuestions MCP server uses a **dual-process architecture**:

```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│                 │         │                  │         │                 │
│   AI Agent      │────────>│   MCP Server     │────────>│  Session Dir   │
│                 │  stdio  │   (stdio)        │  files  │  (~/.local/share)│
└─────────────────┘         └──────────────────┘         └────────┬────────┘
                                                                │
                                                                │ files
                                                                │
                                                  ┌─────────────▼─────────────┐
                                                  │                           │
                                                  │      TUI Process          │
                                                  │   (interactive terminal)    │
                                                  │                           │
                                                  └───────────────────────────┘
```

### Process Flow

1. **AI Agent** calls `ask_user_questions` tool via MCP protocol
2. **MCP Server** (via stdio) creates a session directory with:
   - `request.json` - Questions and metadata
   - `status.json` - Session status (pending)
3. **TUI Process** (running separately) detects new session and displays questions
4. **User** answers questions in TUI
5. **TUI** writes `answers.json` to session directory
6. **MCP Server** detects `answers.json` and returns formatted response to AI

## Fix Implementation

### 1. Enabled MCP Server in Configuration

**File**: `/root/.config/opencode/opencode.json`
**Change**: Set `"enabled": true` for `ask-user-questions` MCP server
**Lines**: 774-784

```json
"ask-user-questions": {
  "type": "local",
  "command": [
    "npx",
    "-y",
    "auq-mcp-server",
    "server"
  ],
  "enabled": true,
  "timeout": 60000
}
```

### 2. Cleaned Up Stale Sessions

Removed 12+ orphaned sessions from `~/.local/share/auq/sessions/`. These were from previous test runs that were never completed due to missing TUI process.

### 3. Validated Core Functionality

All diagnostic tests passed:

| Test | Status |
|------|--------|
| Session Directory | ✅ |
| Session Manager Initialization | ✅ |
| Questions Schema Validation | ✅ |
| Session File Creation | ✅ |
| Session Cleanup | ✅ |
| MCP Server Binary | ✅ |
| End-to-End Workflow | ✅ |

## Session File Structure

Each session creates a directory: `~/.local/share/auq/sessions/<sessionId>/`

```
<sessionId>/
├── request.json    # Questions, callId, workingDirectory, timestamp, status
├── status.json     # createdAt, lastModified, sessionId, status, totalQuestions
└── answers.json   # answers, sessionId, submittedAt, callId (created by TUI)
```

## How to Use

### With OpenCode (Recommended)

1. **Start TUI in a separate terminal:**
   ```bash
   npx -y auq-mcp-server
   ```
   The TUI will show a waiting screen.

2. **Use `ask_user_questions` tool from OpenCode:**
   The agent can now use tool to ask questions.

3. **Answer questions in TUI terminal:**
   Questions will appear automatically when MCP server creates sessions.

### Standalone CLI Testing

```bash
# Ask questions via CLI (requires interactive terminal)
echo '{"questions": [{"prompt": "Which framework?", "title": "Framework", "options": [{"label": "React"}, {"label": "Vue"}, {"label": "Svelte"}], "multiSelect": false}]}' | npx -y auq-mcp-server ask
```

## Test Results

### Diagnostic Test

All core functionality validated successfully:
- ✅ Session directory exists and is writable (`~/.local/share/auq/sessions/`)
- ✅ Session Manager initializes correctly
- ✅ Questions schema validation works
- ✅ Session file creation works
- ✅ Session cleanup works
- ✅ MCP Server binary is functional

### End-to-End Test

Complete workflow validation:
- ✅ Questions validated successfully
- ✅ Session created and files written
- ✅ User answers simulated (manual answer file creation)
- ✅ MCP server detected answers
- ✅ Answers read and validated
- ✅ Response formatted correctly

**Sample Formatted Response:**

```
Here are the user's answers:

1. Which deployment method do you prefer?
→ Docker Compose (Recommended) — Simple and portable deployment
```

## Important Notes

According to my global instructions, the **native `question` tool** should be preferred for production use. The `ask-user-questions` MCP server is now available for testing, development, and debugging purposes.

### When to Use MCP Server

The MCP server can be useful for:
- Testing MCP functionality
- Understanding dual-process architecture
- Development and debugging
- Cases where native question tool is unavailable

## Configuration

The session directory can be customized:

```bash
export AUQ_SESSION_DIR=/custom/path/to/sessions
```

Default locations:
- Linux: `~/.local/share/auq/sessions/`
- macOS: `~/Library/Application Support/auq/sessions/`
- Windows: `%APPDATA%/auq/sessions/`

## Summary

The `ask-user-questions` MCP server is now **fully functional** and ready to use. The fix involved:

1. ✅ Enabling the server in OpenCode configuration
2. ✅ Cleaning up stale session data
3. ✅ Validating all core functionality
4. ✅ Creating comprehensive test scripts
5. ✅ Documenting usage and troubleshooting

**Next Steps:**
1. Start TUI: `npx -y auq-mcp-server`
2. Use `ask_user_questions` tool from OpenCode
3. Answer questions in TUI terminal

The server is now ready for use whenever you need an interactive question interface during AI execution.