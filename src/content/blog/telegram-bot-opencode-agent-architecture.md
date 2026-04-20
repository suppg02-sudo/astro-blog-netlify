---
pubDatetime: 2026-03-09T08:30:00Z
title: "Building a Telegram Bot Agent for OpenCode: Architecture, Debugging, and Lessons Learned"
postSlug: "telegram-bot-opencode-agent-architecture"
description: "Building a Telegram Bot Agent for OpenCode: Architecture, Debugging, and Lessons Learned"
tags:
  - debugging
  - opencode
  - systemd
  - dns
  - ai-agent
  - architecture
  - retry-logic
  - telegram
  - python
  - bot
---

## Overview

This post documents the full architecture of a Python Telegram bot that acts as a remote control for an Ubuntu server. It evolved through several iterations during a single debugging session:

1. **v1**: OpenCode CLI subprocess for everything -- slow (30-180s), "I'm Claude Code" identity leak on every response
2. **v2**: Two-mode system (chat vs trigger) -- chat still slow via OpenCode, triggers timing out
3. **v3 (current)**: Three-path architecture -- Gemini API for chat (1-3s), inline button menus for trigger words, direct shell commands for instant server info

What started as a simple message relay became a deep debugging session involving DNS resolution failures, subprocess timeouts, httpx transport errors, and the challenge of making an AI agent respond quickly enough for a chat interface.

## Architecture (v3)

### System Diagram

```
Telegram App (phone)
    |
    v
Telegram API (cloud)
    |
    v (long-polling every ~2s)
telegram-bot.service (systemd)
    |
    ├── /command → Direct handler (status, cmd, run, etc.)
    |
    └── plain text → echo() handler
            |
            ├── Single trigger word? → is_trigger()
            |       |
            |       ├── Has PREDEFINED_MENU? → Inline button menu
            |       |       (click → execute_action → command/submenu/question)
            |       |
            |       └── Has TRIGGER_HANDLER? → Direct shell output
            |               (instant formatted text response)
            |
            └── Regular message → ask_gemini()
                    |
                    ├── Conversation history (last 10 msgs)
                    ├── Custom system prompt
                    └── Google Gemini 2.5 Flash API (1-3s)
            |
            v
        send_message_with_retry()
            (5 retries, 2.5x exponential backoff)
            |
            v
        Telegram API → User's phone
```

### Three Message Paths

| Path | When | Speed | How |
|------|------|-------|-----|
| **Gemini Chat** | Any regular message | 1-3 seconds | Direct API call to Gemini 2.5 Flash with conversation memory |
| **Menu Trigger** | Single word matching a menu (e.g., `online`, `containers`) | Instant | Sends inline keyboard buttons, user clicks to execute |
| **Direct Trigger** | Single word matching a handler (e.g., `status`, `memcheck`) | 1-30 seconds | Runs shell commands directly, returns formatted text |

### Key Design Decision: Exact Single-Word Matching

Triggers only fire when the **entire message** is a single trigger word. "status" triggers, but "what's the status" goes to Gemini chat. This prevents false positives in natural conversation.

```python
def is_trigger(text: str) -> bool:
    stripped = text.strip().lower()
    return stripped in TRIGGER_HANDLERS or stripped in PREDEFINED_MENUS
```

### How It Runs

The bot runs as a systemd service on Ubuntu:

```ini
# /etc/systemd/system/telegram-bot.service
[Service]
ExecStart=/opt/telegram-bot/venv/bin/python /opt/telegram-bot/bot.py
Environment=TELEGRAM_BOT_TOKEN=<token>
Environment=TELEGRAM_CHAT_ID=<chat_id>
Environment=ALLOWED_USERS=<chat_id>
Restart=always
RestartSec=10
```

Key properties:
- **Auto-restart**: If the bot crashes, systemd restarts it within 10 seconds
- **Isolated Python venv**: Dependencies (python-telegram-bot, httpx) don't conflict with system Python
- **Long-polling**: No webhooks, no open ports, no SSL certificates needed
- **Single-user**: Locked to one Telegram user ID via the `authorized()` decorator

## The Bot Code (bot.py)

### Entry Point and Handler Registration

```python
def main() -> None:
    app = Application.builder().token(TOKEN).post_init(post_init).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("ask", ask))
    app.add_handler(CommandHandler("cmd", cmd))
    app.add_handler(CommandHandler("run", run_action))
    app.add_handler(CommandHandler("remember", remember))
    app.add_handler(CommandHandler("memory", memory))
    app.add_handler(CommandHandler("notify", notify))
    app.add_handler(CallbackQueryHandler(button_callback))  # Inline button clicks
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling(allowed_updates=Update.ALL_TYPES)
```

Messages are routed by type:
- `/command` messages go to their specific handler
- Button clicks go to `button_callback()`
- Plain text falls through to `echo()`, the catch-all handler

### The Nine Slash Commands

| Command | What it does | Backend |
|---------|-------------|---------|
| `/start`, `/help` | Shows help text | Static text |
| `/status` | Runs uptime/load/mem/disk/containers | Direct shell |
| `/ask <question>` | Ask a question | Gemini API |
| `/cmd <command>` | Runs arbitrary shell command | Direct shell |
| `/run <action>` | Runs predefined action (health, space, uptime, etc.) | Direct shell |
| `/remember <cat> <text>` | Saves text to memory file | Local filesystem |
| `/memory [cat]` | Reads memory files | Local filesystem |
| `/notify <msg>` | Echo test | Direct reply |

### The Authorization Decorator

```python
def authorized(func):
    async def wrapper(update, context):
        user_id = str(update.effective_user.id)
        if user_id not in ALLOWED_USERS:
            await update.message.reply_text(f"Unauthorized. Your ID: {user_id}")
            return
        return await func(update, context)
    return wrapper
```

Every handler is wrapped with `@authorized`. Only the configured user ID can interact with the bot.

### The Three-Path Routing System

This is the key design decision. When a plain text message arrives, the `echo()` handler checks if it's a single trigger word. If yes, it routes to a menu or direct handler. If not, it goes to Gemini for AI chat:

```python
TRIGGER_HANDLERS = {
    "status": trigger_status,
    "containers": trigger_containers,
    "space": trigger_space,
    "online": trigger_online,
    "memcheck": trigger_memcheck,
    "openrag": trigger_openrag,
    "services": trigger_services,
    "files": trigger_files,
    "url": trigger_url,
    "triggers": trigger_help_triggers,
    # ... plus aliases like "docker" -> trigger_containers
}

def is_trigger(text: str) -> bool:
    stripped = text.strip().lower()
    return stripped in TRIGGER_HANDLERS or stripped in PREDEFINED_MENUS
```

**Path 1: Gemini Chat** (regular messages):
- Direct API call to Google Gemini 2.5 Flash
- Custom system prompt: conversational, concise, no identity leak
- 10-message conversation memory per user (deque)
- 1-3 second response times
- No tool use, no subprocess overhead

**Path 2: Menu Trigger** (e.g., `online`, `research`, `telos`):
- Matches against `PREDEFINED_MENUS` dictionary (12 main + 6 sub-menus)
- Sends inline keyboard buttons to Telegram
- User clicks a button, which routes to `execute_action()` in `menu_actions.py`
- Actions can run commands, show sub-menus, ask questions, or call OpenCode
- Instant display, action speed depends on what the button does

**Path 3: Direct Trigger** (e.g., `status`, `memcheck`, `files`):
- Matches against `TRIGGER_HANDLERS` dictionary (18 handler functions)
- Runs shell commands directly in Python -- no subprocess, no AI, no network calls
- Returns formatted text immediately (1-30 seconds depending on command)

### The Core Function: ask_gemini()

```python
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

SYSTEM_PROMPT = (
    "You are a helpful assistant on Telegram for a server admin named Paul. "
    "Be conversational, concise, and friendly. Keep responses under 400 words. "
    "If Paul asks about his server, suggest he use trigger words like: "
    "status, containers, space, online, memcheck, openrag, services, url, triggers."
)

def ask_gemini(question: str, user_id: str = "default") -> str:
    history = get_chat_history(user_id)  # deque(maxlen=10)

    contents = list(history)
    contents.append({"role": "user", "parts": [{"text": question}]})

    payload = {
        "system_instruction": {"parts": [{"text": SYSTEM_PROMPT}]},
        "contents": contents,
    }

    resp = requests.post(GEMINI_URL, json=payload, timeout=30)
    text = resp.json()["candidates"][0]["content"]["parts"][0]["text"]

    # Save to conversation memory
    history.append({"role": "user", "parts": [{"text": question}]})
    history.append({"role": "model", "parts": [{"text": text}]})

    return text
```

The function:
1. Builds a conversation history array (Gemini's native format)
2. Sends a single HTTPS POST with the system prompt + history + new message
3. Parses the response text from Gemini's JSON
4. Saves both user message and model response to the per-user deque
5. Returns the text directly -- no ANSI stripping, no subprocess cleanup needed

**Why Gemini instead of OpenCode?** OpenCode's system prompt forces "I'm Claude Code" on every response regardless of wrapping. `opencode run` also spawns a fresh session each time with no context, skills, or memory. Direct Gemini API calls bypass both problems: custom system prompt, conversation memory, and 1-3s response times instead of 30-180s.

### Direct Trigger Handlers (11 functions)

Each trigger handler is a plain Python function that runs shell commands and formats the output:

```python
def trigger_status() -> str:
    uptime = run_cmd("uptime -p")
    load = run_cmd("cat /proc/loadavg | awk '{print $1, $2, $3}'")
    mem = run_cmd("free -h | awk '/Mem:/{print $3\"/\"$2}'")
    disk = run_cmd("df -h / | awk 'NR==2{print $3\"/\"$2\" (\"$5\")\"}'")
    containers_up = run_cmd("docker ps -q | wc -l")
    return (
        f"System Status\n{'=' * 24}\n"
        f"Uptime:     {uptime}\nLoad:       {load}\n"
        f"Memory:     {mem}\nDisk /:     {disk}\n"
        f"Containers: {containers_up} up"
    )
```

Available handlers: `status`, `containers`, `space`, `online`, `memcheck`, `openrag`, `services`, `files`, `url`, `triggers` (help), plus aliases (`docker`, `disk`, `network`, `devices`, `ports`, `urls`, `rag`, `mem-check`, `memory`, `help`).

### Inline Button Menus and Callbacks

When a trigger has a `PREDEFINED_MENU`, the bot builds an inline keyboard:

```python
async def run_trigger(text, bot, chat_id):
    word = text.strip().lower()
    if word in PREDEFINED_MENUS:
        menu = PREDEFINED_MENUS[word]
        rows = []
        for opt in menu["options"]:
            label = opt["label"]
            callback = f"menu:{word}:{label}"  # must be ≤64 bytes
            rows.append([InlineKeyboardButton(label, callback_data=callback)])
        keyboard = InlineKeyboardMarkup(rows)
        await bot.send_message(chat_id=chat_id, text=header, reply_markup=keyboard)
        return ""  # Menu sent, no text needed
    # Otherwise run direct handler
    return TRIGGER_HANDLERS[word]()
```

Button clicks are handled by `button_callback()`, which parses the callback data and routes to `execute_action()`:

```python
async def button_callback(update, context):
    query = update.callback_query
    await query.answer()
    parts = query.data.split(":", 2)  # "menu:online:List devices"
    menu_name, option = parts[1], parts[2]
    await execute_action(context.bot, chat_id, menu_name, option)
```

### The Echo Handler

```python
@authorized
async def echo(update, context):
    text = update.message.text
    chat_id = update.effective_chat.id

    if is_trigger(text):
        response = await run_trigger(text, context.bot, chat_id)
        if not response:
            return  # Menu was sent via inline buttons
    else:
        await update.message.reply_text("Thinking...")
        response = ask_gemini(text, str(update.effective_user.id))

    if len(response) > 3900:
        response = response[:3900] + "\n... (truncated)"

    result = await send_message_with_retry(
        context.bot, chat_id, response,
        parse_mode=None, max_retries=5, backoff_base=2.0
    )
```

The handler:
1. Checks if the entire message is a single trigger word
2. If trigger with menu: sends inline buttons, returns early
3. If trigger without menu: runs direct handler function
4. If regular message: sends "Thinking..." then calls Gemini API
5. Truncates response to Telegram's 4096-char limit
6. Delivers via `send_message_with_retry()` with 5 retries and exponential backoff

## The DNS Debugging Story

### The Problem

After getting the bot working, we discovered that responses were being **silently lost**. The bot would:
1. Receive user message (OK)
2. Send "Thinking..." (OK)
3. Call OpenCode and get a response (OK)
4. Try to send the response back... **httpx.ConnectError: [Errno -3] Temporary failure in name resolution**

The response was generated but never delivered. The user just saw "Thinking..." forever.

### Investigation

- DNS resolvers were correctly configured (`9.9.9.9`, `1.1.1.1` in `/etc/resolv.conf`)
- `nslookup api.telegram.org` worked fine from the shell
- `python3 -c "import socket; print(socket.gethostbyname('api.telegram.org'))"` also worked
- `systemd-resolved` was running and healthy
- No firewall rules blocking outbound DNS
- The failure was **intermittent** -- sometimes it worked, sometimes it didn't

### Root Cause

The server has ~20 Docker bridge network interfaces. Combined with Tailscale VPN, there appears to be an intermittent DNS resolution issue specific to long-running Python processes using the httpx library. The exact trigger is still unknown, but it's transient -- retrying after a few seconds usually succeeds.

### The Fix: Retry Logic

Rather than fixing the underlying DNS issue (which is transient and hard to reproduce), we made the bot resilient to it:

```python
async def send_message_with_retry(bot, chat_id, text,
    parse_mode="Markdown", max_retries=3, backoff_base=1.0):

    for attempt in range(max_retries):
        try:
            msg = await bot.send_message(chat_id=chat_id, text=text,
                                          parse_mode=prepared_mode)
            return msg
        except (OSError, socket.gaierror, ConnectionError, TimeoutError) as e:
            # Standard library network errors
            wait_time = backoff_base * (2.5 ** attempt)
            await asyncio.sleep(wait_time)
        except Exception as e:
            # httpx.ConnectError and similar transport errors
            if "name resolution" in str(e).lower():
                wait_time = backoff_base * (2.5 ** attempt)
                await asyncio.sleep(wait_time)
            else:
                # Non-network error, try plain text fallback
                msg = await bot.send_message(chat_id=chat_id,
                                              text=text, parse_mode=None)
                return msg

    return None  # All retries exhausted
```

With `max_retries=5, backoff_base=2.0`:
- Attempt 1: immediate
- Attempt 2: wait 2.0s
- Attempt 3: wait 5.0s
- Attempt 4: wait 12.5s
- Attempt 5: wait 31.25s
- Total retry window: ~50 seconds

Since deploying the retry logic, **zero responses have been lost**.

## Other Bugs Found and Fixed

### 1. Tuple Unpacking Error (bot.py line 232)

```python
# BROKEN: ask_opencode() returns a string, not a tuple
response, success = ask_opencode(question)

# FIXED:
response = ask_opencode(question)
```

### 2. Test Message Confusion

We spent significant time sending test messages via the Telegram Bot API (`bot.sendMessage`) and wondering why the echo handler never fired. Root cause: `bot.sendMessage` sends messages **from** the bot, and the bot ignores its own messages. The echo handler only fires for messages sent by a real user from the Telegram app.

### 3. Stale Timeout Message

The timeout error message said "30s" but the actual timeout was 180s. Fixed to show the correct timeout and mode.

### 4. telegram_utils.py Bugs (3 critical fixes)

- **Empty message edits**: The bot tried to edit messages with empty text, causing API errors. Added defensive validation before all API calls.
- **Network error handling**: Added socket error detection with 2.5x backoff and plain text fallback.
- **Streaming progress validation**: Added empty text checks before message updates.

## The Evolving Python Configuration

One thing that's easy to miss in a "here's the architecture" post is that the code didn't start this way. The configuration layer evolved through three distinct stages, each driven by a concrete problem.

### Stage 1: Hardcoded Everything (v1)

The first version had two constants and one subprocess call:

```python
TOKEN = "8404053172:..."
CHAT_ID = "7563541207"
OPENCODE_BIN = "/root/.opencode/bin/opencode"

def ask_opencode(question):
    result = subprocess.run([OPENCODE_BIN, "run", question], ...)
    return result.stdout
```

That's it. Token, chat ID, and the path to the OpenCode binary. Everything else was derived at runtime. Configuration was the code itself -- edit `bot.py`, restart the service. This is fine for a single-user bot on a single server. But it created a problem: the token appeared in three different files (`bot.py`, `menu_actions.py`, and `send_message.py`), and the chat ID appeared in four.

### Stage 2: Environment Variables + Fallbacks (v2)

When the bot became a systemd service, we moved secrets to environment variables:

```ini
# /etc/systemd/system/telegram-bot.service
[Service]
Environment="TELEGRAM_BOT_TOKEN=8404053172:..."
Environment="TELEGRAM_CHAT_ID=7563541207"
Environment="ALLOWED_USERS=7563541207"
```

The Python code grew a pattern: `os.environ.get()` with the hardcoded value as fallback:

```python
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "8404053172:...")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "7563541207")
ALLOWED_USERS = os.environ.get("ALLOWED_USERS", CHAT_ID).split(",")
```

This is the classic twelve-factor app pattern, and it solved the immediate problem: one place to change secrets (the systemd unit file), and the bot could run in development without setting environment variables. But it introduced a new problem: the hardcoded fallbacks still contained the real credentials, scattered across multiple files. `menu_actions.py` and `send_message.py` still had their own `TOKEN` and `CHAT_ID` constants, not even reading from environment variables.

### Stage 3: Growing Config Surface (v3)

The switch to Gemini added a new config dimension:

```python
OPENCODE_BIN = "/root/.opencode/bin/opencode"      # Legacy, still used by some menu actions
GEMINI_API_KEY = "AIzaSy..."                         # Google AI API key
GEMINI_MODEL = "gemini-2.5-flash"                    # Model name (was gemini-2.0-flash, now deprecated)
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"

SYSTEM_PROMPT = (
    "You are a helpful assistant on Telegram for a server admin named Paul. "
    "Be conversational, concise, and friendly. Keep responses under 400 words..."
)
```

Plus the conversation memory config:

```python
chat_history = {}                        # user_id -> deque
MEMORY_DIR = Path("/opt/telegram-bot/memory")
LOGS_DIR = Path("/opt/telegram-bot/logs")
```

And the direct trigger config -- a dictionary mapping 18 trigger words to Python functions:

```python
TRIGGER_HANDLERS = {
    "status": trigger_status,
    "containers": trigger_containers,
    "docker": trigger_containers,      # alias
    "space": trigger_space,
    "online": trigger_online,
    "memcheck": trigger_memcheck,
    ...
}
```

### The Multi-File Problem

The config is now split across four files with partial duplication:

| Config | bot.py | menu_actions.py | send_menu.py | send_message.py |
|--------|--------|-----------------|--------------|-----------------|
| `TOKEN` | `os.environ.get()` | Hardcoded | `os.environ.get()` | `os.environ.get()` |
| `CHAT_ID` | `os.environ.get()` | Hardcoded | `os.environ.get()` | `os.environ.get()` |
| `GEMINI_API_KEY` | Hardcoded | -- | -- | -- |
| `SYSTEM_PROMPT` | Hardcoded | -- | -- | -- |
| `TRIGGER_HANDLERS` | Dict in bot.py | -- | -- | -- |
| `PREDEFINED_MENUS` | -- | -- | Dict in send_menu.py | -- |
| `MENU_ACTIONS` | -- | Dict in menu_actions.py | -- | -- |
| `USER_CONTEXT` | Imported | Defined here | -- | -- |

`bot.py` is the main process, `menu_actions.py` handles button click logic, `send_menu.py` defines menu structures, and `send_message.py` is a standalone CLI tool. They share the token and chat ID but each has its own copy. The menu and trigger configs are split between `bot.py` (which trigger word maps to which handler) and `send_menu.py` (what buttons each menu shows) and `menu_actions.py` (what each button does).

### Why It Works Anyway

Despite the duplication, this layout actually works well for a single-server bot:

1. **`bot.py` owns the runtime** -- it's the systemd entry point, it imports everything else, and it's the only file that receives Telegram updates.
2. **`menu_actions.py` owns the actions** -- changing what a button does means editing one file.
3. **`send_menu.py` owns the menus** -- changing what buttons appear means editing one file.
4. **Changes don't cascade** -- adding a new menu option requires editing `send_menu.py` (add button) and `menu_actions.py` (add action), but never `bot.py`.

The hardcoded fallbacks are technically a security concern, but this is a root-only bot on a private server behind Tailscale VPN. The pragmatic tradeoff is: it always works, even if you forget to set environment variables.

### What's Next: Pending Question Context

The most recent addition is `USER_CONTEXT` -- a shared dictionary that tracks when a menu action asked the user a question and is waiting for their typed response:

```python
# In menu_actions.py
USER_CONTEXT = {}  # chat_id -> {"pending_action": "research_topic", "topic": None}

# In bot.py (imported)
from menu_actions import USER_CONTEXT

async def echo(update, context):
    chat_id_str = str(update.effective_chat.id)

    # Check if we're waiting for a response to a menu question
    if chat_id_str in USER_CONTEXT and USER_CONTEXT[chat_id_str].get("pending_action"):
        pending = USER_CONTEXT.pop(chat_id_str)
        await handle_pending_input(text, pending["pending_action"], context.bot, chat_id)
        return

    # Otherwise: trigger check, then Gemini chat
    ...
```

This bridges the gap between stateless inline buttons and multi-step workflows. When a menu option sets `"next": "research_topic"`, the bot stores that in `USER_CONTEXT`. The next plain text message from that user gets routed to `handle_pending_input()` instead of Gemini. The pending context is consumed on use (popped from the dict), so stale state doesn't accumulate.

The pattern will likely grow as more menu actions need follow-up input. The current handlers include: `research_topic`, `analyze_device`, `dhcp_mapping`, `openrag_bm25`, `openrag_semantic`, `send_message`, `architecture_decision`, and five `q_*` modes (explore, build, debug, learn, plan). Each maps user text to a specific action -- usually a Gemini prompt with a mode-appropriate prefix, or a direct shell command with the user's input interpolated.

## File Structure

```
/opt/telegram-bot/
├── bot.py                    # Main bot - Gemini chat, triggers, menus (702 lines)
├── telegram_utils.py         # Retry logic, streaming, chunking (803 lines)
├── menu_actions.py           # Button action handlers (473 lines)
├── send_menu.py              # PREDEFINED_MENUS definitions (265 lines)
├── send_message.py           # CLI message sender (89 lines)
├── verbose_monitor.py        # Monitoring (188 lines)
├── show_devices.sh           # Device list formatter (mobile-friendly)
├── menu_sync.py              # Sync menus with AGENTS.md triggers
├── memory/                   # Persistent notes
│   ├── user.md
│   ├── memory.md
│   └── soul.md
├── logs/                     # Application + chat logs
│   ├── bot.log
│   └── chat-YYYY-MM-DD.log
└── venv/                     # Python virtual environment
```

## Lessons Learned

### 1. AI Agents Are Too Slow for Chat -- Bypass Them

An AI agent with full tool access (file reading, command execution, web search) takes 30-180 seconds to respond via `opencode run`. That's unacceptable for a chat interface. The v2 approach of wrapping prompts to disable tools still used the subprocess. The real fix was **bypassing OpenCode entirely** and calling Gemini's API directly: 1-3s responses with a custom system prompt and conversation memory.

### 2. Three Paths Are Better Than Two

The v2 "chat vs trigger" split still routed both modes through OpenCode. v3 adds a third path: direct shell handlers that run Python functions with `subprocess.run()`. For simple server queries (status, disk space, container list), there's no reason to invoke an AI model at all. The response is deterministic and instant.

### 3. Retry Everything at the Network Boundary

Any call to an external API (Telegram, DNS resolution) can fail transiently. The bare `reply_text()` call has zero retry logic. Wrapping it in `send_message_with_retry()` with exponential backoff made the bot resilient to intermittent DNS failures that had been silently dropping responses.

### 4. httpx Exceptions Are Unusual

Python's httpx library (used by python-telegram-bot) has its own exception hierarchy that does **not** inherit from `OSError`. `httpx.ConnectError` inherits from `httpx.NetworkError` -> `httpx.TransportError` -> `Exception`. Catching `OSError` or `ConnectionError` won't catch httpx DNS failures. The retry function has to check exception class name strings or the error message text.

### 5. Test With Real Users, Not API Calls

The bot ignores messages from itself. Testing via `bot.sendMessage` API will never trigger the echo handler. Always test by sending real messages from the Telegram app.

### 6. systemd Is Your Friend

The bot runs as a systemd service with `Restart=always`. If DNS fails catastrophically, if Python crashes, if anything goes wrong -- the bot comes back within 10 seconds. Combined with the retry logic, this makes the system self-healing.

### 7. Exact Matching Prevents False Positives

The v2 trigger system matched the **first word** of a message. "What's the status" would fire the status trigger. v3 requires the **entire message** to be a single trigger word. Natural conversation flows to Gemini; only deliberate single-word commands activate triggers.

## Current Status

The bot is running in production with three fully operational message paths:

- **Gemini chat**: 1-3 second responses with conversation memory (last 10 exchanges per user)
- **Menu triggers**: 12 inline button menus with 84 options and 100% action coverage
- **Direct triggers**: 11 handler functions (18 trigger words including aliases) for instant server info

OpenCode is no longer used for any interaction path. All chat goes through Gemini, all menu actions use either direct shell commands or Gemini prompts, and all trigger words run Python functions with `subprocess.run()`. The `opencode run` subprocess approach from v1/v2 has been fully replaced.

## Useful Commands

```bash
# Check bot status
systemctl status telegram-bot

# Live logs (filtered)
journalctl -u telegram-bot -f --no-pager | grep -v getUpdates

# Restart after code changes (always validate first!)
python3 -m py_compile /opt/telegram-bot/bot.py && systemctl restart telegram-bot

# Send a test message from CLI
curl -s "https://api.telegram.org/bot<TOKEN>/sendMessage" \
  -d chat_id=<CHAT_ID> -d text="test"
```