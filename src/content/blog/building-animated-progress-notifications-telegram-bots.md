---
pubDatetime: 2026-03-10T00:42:00Z
title: "Building Animated Progress Notifications for Telegram Bots"
postSlug: "building-animated-progress-notifications-telegram-bots"
description: "How to implement Git-style animated progress indicators with color-coded status, progress bars, and real-time statistics in Telegram bot notifications"
tags:
  - ux
  - automation
  - telegram
  - python
  - asyncio
---

## Overview

This guide shows how to create animated progress notifications for long-running tasks in Telegram bots. We'll build a backup progress screen with:

- **Git-style status indicators** (🟡 active, 🟢 completed)
- **Visual progress bar** with percentage
- **Real-time countdown timer** (MM:SS format)
- **Statistics extraction** from process output
- **Color-coded step transitions** for clear visual feedback

## The Problem

When users trigger long-running operations like backups in Telegram, they see:
- No indication of progress
- No estimated completion time
- No feedback on what's happening
- Generic "success" or "failed" messages

This creates anxiety and uncertainty. Users don't know if the bot is working or frozen.

## The Solution

Animated notifications using Telegram's `edit_message_text()` API to update a single message in place, showing progressive status changes.

## Architecture

### Key Components

1. **Initial Message** - Send message with initial state
2. **Update Function** - Async function to edit message in place
3. **Progress Phases** - Time-based state transitions
4. **Process Execution** - Async subprocess to avoid blocking
5. **Statistics Extraction** - Parse output for real data
6. **Final Status** - Show actual results

### Visual Design

```
💾 System Backup
[████████████████░░░░] 80%

🟢 ✓ Preparing backup

🟡 → Executing backup
   Compressing data...

⏱️ 00:06
```

**Visual Elements:**
- Progress bar: `[████░░░░]` (filled/empty blocks)
- Status indicators: `🟡` (yellow = active), `🟢` (green = completed)
- Arrow: `→` points to current step
- Checkmark: `✓` marks completed steps
- Countdown: `⏱️ MM:SS` shows time remaining

## Implementation

### 1. Progress Bar Function

```python
def progress_bar(remaining: int, total: int) -> str:
    """Create visual progress bar with 20 blocks."""
    elapsed = total - remaining
    percent = int((elapsed / total) * 100)
    filled = int(percent / 5)  # 20 blocks total
    empty = 20 - filled
    return f"[{'█' * filled}{'░' * empty}] {percent}%"
```

**Output**: `[████████████████░░░░] 80%`

### 2. Animated Notification Function

```python
async def backup_animated_notification(bot, chat_id: int) -> tuple:
    """Send animated backup progress with countdown timer."""
    total_time = 30  # Animation duration in seconds
    
    # Send initial message
    initial_text = (
        f"<b>💾 System Backup</b>\n"
        f"<code>{progress_bar(total_time, total_time)}</code>\n\n"
        f"<code>🟡 → Preparing backup</code>\n"
        f"<code>   Initializing...</code>\n\n"
        f"<code>⏱️ {total_time // 60:02d}:{total_time % 60:02d}</code>"
    )
    
    msg = await bot.send_message(
        chat_id=chat_id,
        text=initial_text,
        parse_mode="HTML",
    )
    
    # Update function
    async def update_animated(text: str):
        try:
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=msg.message_id,
                text=text,
                parse_mode="HTML",
            )
        except Exception as e:
            logger.warning(f"Failed to update: {e}")
    
    # ... rest of implementation
```

**Key Points:**
- Use `parse_mode="HTML"` for `<code>` and `<b>` tags
- Wrap updates in try/except (Telegram may reject rapid edits)
- Store message ID for subsequent updates

### 3. Countdown Loop with Phases

```python
process = None  # Will hold async subprocess

for remaining in range(total_time, 0, -1):
    time_str = f"{remaining // 60:02d}:{remaining % 60:02d}"
    progress = progress_bar(remaining, total_time)
    
    if remaining > 20:
        # Phase 1: Preparing (30-20s)
        phase_text = (
            f"<b>💾 System Backup</b>\n"
            f"<code>{progress}</code>\n\n"
            f"<code>🟡 → Preparing backup</code>\n"
            f"<code>   Initializing...</code>\n\n"
            f"<code>⏱️ {time_str}</code>"
        )
    elif remaining > 10:
        # Phase 2: Executing (20-10s)
        if remaining == 20:
            # Start backup script asynchronously
            process = await asyncio.create_subprocess_exec(
                "/root/scripts/backup.sh",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
        
        phase_text = (
            f"<b>💾 System Backup</b>\n"
            f"<code>{progress}</code>\n\n"
            f"<code>🟢 ✓ Preparing backup</code>\n\n"
            f"<code>🟡 → Executing backup</code>\n"
            f"<code>   Archiving files...</code>\n\n"
            f"<code>⏱️ {time_str}</code>"
        )
    elif remaining > 5:
        # Phase 3: Compressing (10-5s)
        phase_text = (
            f"<b>💾 System Backup</b>\n"
            f"<code>{progress}</code>\n\n"
            f"<code>🟢 ✓ Preparing backup</code>\n\n"
            f"<code>🟡 → Executing backup</code>\n"
            f"<code>   Compressing data...</code>\n\n"
            f"<code>⏱️ {time_str}</code>"
        )
    else:
        # Phase 4: Verifying (5-0s)
        phase_text = (
            f"<b>💾 System Backup</b>\n"
            f"<code>{progress}</code>\n\n"
            f"<code>🟢 ✓ Preparing backup</code>\n\n"
            f"<code>🟢 ✓ Executing backup</code>\n\n"
            f"<code>🟡 → Verifying backup</code>\n"
            f"<code>   Finalizing...</code>\n\n"
            f"<code>⏱️ {time_str}</code>"
        )
    
    await update_animated(phase_text)
    await asyncio.sleep(1)
```

**Critical Points:**
- Use `asyncio.create_subprocess_exec()` NOT `subprocess.run()` (blocks animation)
- Start process at appropriate phase transition
- Update message every second for smooth animation
- Show clear step transitions (yellow → green, arrow → checkmark)

### 4. Extract Real Statistics

```python
# After countdown completes
file_count = 0
total_size_bytes = 0
total_size = "0B"

if process:
    stdout, stderr = await process.communicate()
    output = stdout.decode("utf-8", errors="ignore")
    
    # Parse output for stats
    for line in output.split("\n"):
        if "Total files:" in line:
            try:
                file_count = int(line.split(":")[1].strip())
            except:
                pass
        
        # Parse sizes like "✓ opencode-configs: 1.8M"
        if "✓" in line and ":" in line:
            try:
                parts = line.split(":")
                size_str = parts[-1].strip().upper()
                
                # Convert to bytes
                if 'G' in size_str:
                    total_size_bytes += float(size_str.replace('G', '')) * 1024**3
                elif 'M' in size_str:
                    total_size_bytes += float(size_str.replace('M', '')) * 1024**2
                elif 'K' in size_str:
                    total_size_bytes += float(size_str.replace('K', '')) * 1024
                else:
                    total_size_bytes += float(size_str)
            except:
                pass
    
    # Format total size
    if total_size_bytes >= 1024**3:
        total_size = f"{total_size_bytes / 1024**3:.1f}G"
    elif total_size_bytes >= 1024**2:
        total_size = f"{total_size_bytes / 1024**2:.1f}M"
    elif total_size_bytes >= 1024:
        total_size = f"{total_size_bytes / 1024:.1f}K"
    else:
        total_size = f"{int(total_size_bytes)}B"
    
    success = process.returncode == 0
```

**Why This Matters:**
- Shows actual backup data (e.g., "10 files (40.1M)")
- Better than generic "Backup successful!"
- Users see real impact of the operation

### 5. Final Status Message

```python
final_progress = progress_bar(0, total_time)

if success:
    final_text = (
        f"<b>💾 System Backup</b>\n"
        f"<code>{final_progress}</code>\n\n"
        f"<code>🟢 ✓ Preparing backup</code>\n\n"
        f"<code>🟢 ✓ Executing backup</code>\n\n"
        f"<code>🟢 ✓ Verifying backup</code>\n\n"
        f"<code>✅ {file_count} files backed up ({total_size})</code>"
    )
else:
    final_text = (
        f"<b>💾 System Backup</b>\n\n"
        f"<code>❌ Backup failed</code>"
    )

await update_animated(final_text)
return msg.message_id, success
```

## Integration with Telegram Bot

### Menu Callback Handler

```python
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "backup_now":
        # Call animated notification
        msg_id, success = await backup_animated_notification(
            bot=context.bot,
            chat_id=query.message.chat_id
        )
        
        # Log result
        logger.info(f"Backup completed: success={success}")
```

### Menu Registration

```python
backup_menu = {
    "title": "💾 Backup Management",
    "buttons": [
        {"text": "Check Last Backup", "callback_data": "backup_check"},
        {"text": "Run Backup Now", "callback_data": "backup_now"},
        {"text": "List Recent Backups", "callback_data": "backup_list"},
        {"text": "Exit", "callback_data": "exit"},
    ]
}
```

## Design Principles

### 1. **Progressive Disclosure**
Show information gradually as it becomes available:
- Start with "Preparing"
- Transition to "Executing" with details
- Show "Verifying" at the end
- Final message with statistics

### 2. **Color Coding**
Use consistent visual language:
- 🟡 Yellow = In progress (active step)
- 🟢 Green = Completed (finished step)
- ❌ Red = Error
- ✅ Green check = Success

### 3. **Clear Transitions**
Make phase changes obvious:
- Arrow `→` indicates current focus
- Checkmark `✓` marks completion
- Empty line between steps for readability
- Progress bar fills left-to-right

### 4. **Time Feedback**
Countdown timer provides:
- Estimated completion time
- Sense of progress (even if slow)
- Urgency as time runs low

### 5. **Real Data**
Show actual results:
- File count from backup output
- Size calculated from individual archives
- Better than generic success messages

## Common Pitfalls

### 1. **Blocking Animation with Sync Calls**

❌ **Wrong:**
```python
# This blocks the animation loop!
result = subprocess.run(["/path/to/script"], capture_output=True)
```

✅ **Correct:**
```python
# This runs in background, animation continues
process = await asyncio.create_subprocess_exec(
    "/path/to/script",
    stdout=asyncio.subprocess.PIPE,
    stderr=asyncio.subprocess.PIPE,
)
```

### 2. **Update Rate Too Fast**

Telegram limits edit frequency. Don't update more than once per second:

❌ **Wrong:**
```python
await asyncio.sleep(0.1)  # Too fast!
```

✅ **Correct:**
```python
await asyncio.sleep(1)  # One update per second
```

### 3. **No Error Handling**

❌ **Wrong:**
```python
await bot.edit_message_text(...)  # May throw exception
```

✅ **Correct:**
```python
try:
    await bot.edit_message_text(...)
except Exception as e:
    logger.warning(f"Edit failed: {e}")
```

### 4. **Generic Success Message**

❌ **Wrong:**
```python
final_text = "✅ Backup successful!"
```

✅ **Correct:**
```python
final_text = f"✅ {file_count} files backed up ({total_size})"
```

## Testing

### Manual Testing

1. Start bot with animated notification
2. Trigger backup from Telegram menu
3. Verify animation updates every second
4. Check phase transitions are clear
5. Confirm final message shows real stats

### Validation Checklist

- [ ] Initial message appears immediately
- [ ] Progress bar fills smoothly
- [ ] Countdown timer decrements every second
- [ ] Phase transitions are visually obvious
- [ ] Arrow moves to next step
- [ ] Completed steps turn green with checkmark
- [ ] Final message shows actual statistics
- [ ] Error handling works (test with failing script)

## Reusability

This pattern works for any long-running task:

### YouTube Video Processing
```
📺 Processing Video
[████████████░░░░░░░░] 40%

🟢 ✓ Extracting transcript

🟡 → Summarizing content
   Using Gemini AI...

⏱️ 00:36
```

### Docker Container Deployment
```
🚀 Deploying Container
[████████████████░░░░] 80%

🟢 ✓ Pulling image

🟢 ✓ Creating container

🟡 → Starting services
   Health check...

⏱️ 00:04
```

### Data Migration
```
📊 Migrating Database
[██████████████████░░] 90%

🟢 ✓ Exporting data (1.2M rows)

🟢 ✓ Transforming schema

🟡 → Importing to target
   1,180,000 / 1,200,000 rows

⏱️ 00:02
```

## Implementation Checklist

For another OpenCode instance to implement this:

1. **Create progress bar function**
   - 20 blocks (filled/empty)
   - Percentage display
   - Returns formatted string

2. **Create animated notification function**
   - Accepts `bot` and `chat_id` parameters
   - Sends initial message
   - Creates async update function
   - Implements countdown loop with phases
   - Starts subprocess asynchronously
   - Extracts statistics from output
   - Returns message ID and success status

3. **Design phase transitions**
   - Define clear phases (e.g., prepare → execute → verify)
   - Set timing thresholds for each phase
   - Update status indicators at transitions
   - Show relevant details per phase

4. **Parse process output**
   - Extract file counts
   - Parse size information
   - Handle different formats (K/M/G)
   - Convert to human-readable format

5. **Integrate with bot**
   - Add to menu callback handler
   - Register menu option
   - Test with real operations

6. **Deploy and monitor**
   - Restart bot service
   - Test in production
   - Monitor logs for errors
   - Gather user feedback

## Files Modified

- `/opt/telegram-bot/bot.py` - Added `backup_animated_notification()` function
- Bot menu configuration - Added "Run Backup Now" callback

## Dependencies

- `python-telegram-bot` library (v20+)
- `asyncio` (standard library)
- Process must output parseable statistics

## Performance

- Animation: 30 seconds (configurable)
- Update rate: 1 Hz (once per second)
- Message edits: 30 updates total
- No rate limiting issues observed

## Conclusion

Animated progress notifications transform the user experience from uncertainty to clarity. Users see:

1. **What's happening** - Current step with details
2. **How far along** - Progress bar and percentage
3. **When it finishes** - Countdown timer
4. **What was done** - Real statistics

This pattern is reusable across any long-running operation in Telegram bots. The key is using async subprocess execution to avoid blocking the animation loop, and parsing real data from output to show meaningful results.

## References

- [Telegram Bot API - editMessageText](https://core.telegram.org/bots/api#editmessagetext)
- [Python asyncio subprocess](https://docs.python.org/3/library/asyncio-subprocess.html)
- [python-telegram-bot documentation](https://docs.python-telegram-bot.org/)

---

**Published**: 2026-03-10  
**Tags**: telegram, python, asyncio, ux, automation  
**Category**: development