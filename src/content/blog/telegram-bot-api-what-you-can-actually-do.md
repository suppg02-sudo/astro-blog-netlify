---
pubDatetime: 2026-03-09T12:05:00Z
title: "Telegram Bot API: Everything You Can Actually Do in 2026"
postSlug: "telegram-bot-api-what-you-can-actually-do"
description: "A practical deep dive into what the Telegram Bot API can really do - media, documents, video, iPhone triggers, menus, payments, Mini Apps, and the things nobody tells you don't work."
tags:
  - home-server
  - self-hosted
  - automation
  - bot-api
  - telegram
---

I've been building a Telegram bot to control my home server - Gemini AI chat, inline menus, news pipelines, YouTube summarisation, blog publishing. Along the way I've dug deep into the Bot API (currently v9.5, March 2026) and discovered what actually works, what's surprisingly powerful, and what looks good on paper but falls flat in practice.

This is everything I've found.

## Media: What You Can Send and Receive

Telegram bots can send and receive virtually every media type:

| Type | Method | Max Size | Notes |
|------|--------|----------|-------|
| **Photos** | `sendPhoto` | 10MB | Auto-compressed, multiple sizes returned |
| **Videos** | `sendVideo` | 50MB (2GB local API) | Supports streaming, thumbnails |
| **Video notes** | `sendVideoNote` | Round video messages (like voice notes but video) |
| **Animations** | `sendAnimation` | GIFs and silent MP4s |
| **Audio** | `sendAudio` | 50MB | With metadata (title, performer, duration) |
| **Voice** | `sendVoice` | OGG/Opus format |
| **Documents** | `sendDocument` | 50MB (2GB local API) | Any file type |
| **Stickers** | `sendSticker` | Static, animated, video stickers |
| **Location** | `sendLocation` | Live location with updates |
| **Contact** | `sendContact` | Phone number + name |
| **Poll** | `sendPoll` | Multiple choice, quiz mode, anonymous |
| **Dice** | `sendDice` | Animated random value (dice, darts, basketball, football, bowling, slot machine) |
| **Paid media** | `sendPaidMedia` | Photos/videos behind a paywall (Telegram Stars) |

### Media Groups

You can send up to 10 photos or videos as a single grouped album using `sendMediaGroup`. Each item can have its own caption.

### Video Streaming

As of Bot API 9.4, videos now include a `qualities` field showing available quality levels. Telegram transcodes uploaded videos server-side and offers multiple resolutions to viewers.

### Can You Embed Video Streams?

**Not directly.** Telegram doesn't support embedding live video streams (RTSP, HLS, DASH) in bot messages. However, you can:

- Send a video file that Telegram will stream progressively (users don't need to download the whole file first)
- Send a URL button that opens a streaming page in the browser
- Build a Mini App (see below) that embeds an HTML5 video player with full streaming support
- Use `sendAnimation` for short looping clips

For actual live streaming, the practical path is a Mini App with an embedded player.

## Documents and Files

Bots are solid document handlers:

- **Send any file type** up to 50MB (or 2GB with a self-hosted local Bot API server)
- **Receive files** from users - photos, documents, voice messages, anything Telegram supports
- **Download files** via `getFile` - returns a file path you can download over HTTPS
- **File IDs are reusable** - once uploaded, you can resend the same file by ID without re-uploading (but file IDs are bot-specific)

### Local Bot API Server

If the 50MB limit is a problem, you can run Telegram's open-source Bot API server locally. Benefits:

| Feature | Cloud API | Local API |
|---------|-----------|-----------|
| Download limit | 20MB | Unlimited |
| Upload limit | 50MB | 2GB |
| Webhook URL | HTTPS only | HTTP allowed |
| Webhook port | 443, 80, 88, 8443 | Any port |
| File path | Requires download | Local path returned directly |

Source: [github.com/tdlib/telegram-bot-api](https://github.com/tdlib/telegram-bot-api)

## Triggering Things from Your iPhone (or Any Phone)

This is where Telegram bots genuinely shine as a remote control. Every message you send to the bot arrives as a JSON update that your server processes. This means:

### Single-Word Triggers

Type a word, server does something:

```
"status"    → runs uptime/disk/memory check, returns summary
"backup"    → runs backup script, returns result
"containers"→ shows Docker container status
"reboot"    → (with confirmation) reboots the server
```

These are instant. You're in a taxi, you type "status" on your phone, and 2 seconds later you have your server health. No SSH, no VPN app, no terminal.

### Shell Commands

```
/cmd docker ps
/cmd df -h
/cmd systemctl restart nginx
```

Full shell access from your phone. Obviously, restrict this to your user ID only.

### Inline Button Menus

Instead of remembering commands, present tappable buttons:

```
[View Status] [Run Backup] [Check Logs]
[Install Container] [Disk Space] [Exit]
```

Buttons can chain to sub-menus, ask follow-up questions, run commands, call APIs, or invoke AI. It's a full GUI built from JSON.

### iOS Shortcuts Integration

Telegram supports URL schemes (`tg://msg?to=@yourbotname&text=backup`), which means you can create iOS Shortcuts that:

- Send a trigger word to your bot with one tap
- Add a home screen shortcut that runs a server command
- Trigger automations based on time, location, or NFC tags
- Chain with other shortcuts (get result, process it, send another command)

### Siri Integration

Via iOS Shortcuts, you can say "Hey Siri, check my server" and have it send "status" to your bot. The response shows up as a notification.

### Apple Watch

Telegram on Apple Watch can send and receive messages to bots. Quick replies and voice dictation work. You can literally check your server from your wrist.

## Menus, Keyboards, and Choices

Telegram offers two completely different keyboard systems:

### 1. Inline Keyboards (Below Messages)

Buttons attached to a specific message. When tapped, they send a callback to your bot without posting anything to the chat.

```python
InlineKeyboardMarkup([
    [InlineKeyboardButton("Status", callback_data="status")],
    [InlineKeyboardButton("Backup", callback_data="backup")],
    [InlineKeyboardButton("Blog", url="https://example.com")],
])
```

Features:
- **Callback buttons** - send data back to bot silently
- **URL buttons** - open a link (must be a proper FQDN - local hostnames like `http://myserver:8080` get rejected)
- **Button styles** (Bot API 9.4) - `"primary"` (blue), `"success"` (green), `"danger"` (red) via the `style` field
- **Grid layout** - multiple buttons per row
- **Editable** - update buttons on an existing message without sending a new one
- **Sub-menus** - one button opens another set of buttons

### 2. Reply Keyboards (Replaces Phone Keyboard)

A persistent keyboard at the bottom of the chat that replaces the standard keyboard:

```python
ReplyKeyboardMarkup([
    ["status", "backup"],
    ["news", "menu"],
    ["containers", "space"]
])
```

Features:
- **Always visible** - sits at the bottom, one-tap access
- **Auto-hide** - `one_time_keyboard=True` hides after selection
- **Resize** - `resize_keyboard=True` fits to button content
- **Placeholder text** - custom text in the input field
- **Selective** - only show to specific users in groups

### Native Polls

For choosing between options, native polls look cleaner than buttons:

```python
await bot.send_poll(
    chat_id=CHAT_ID,
    question="Which topic for today's blog?",
    options=["AI News", "Claude Code", "ESP32", "Geopolitics"],
    is_anonymous=False
)
```

The bot receives the user's vote as a `poll_answer` update.

### Menu Button

Every bot chat has a menu button (hamburger icon) near the input field. You can customise it to show commands or launch a Mini App. Set via BotFather or `setChatMenuButton`.

## Blog Publishing Pipeline

One of the most practical things I've built: trigger → AI → blog post → notification, all from Telegram.

### How It Works

1. Type a trigger word or send a URL
2. Bot processes content (Gemini AI summarisation, grounded search, transcript extraction)
3. Generates Hugo frontmatter and markdown
4. Writes to Hugo content directory
5. Triggers Hugo rebuild
6. Sends you back a clickable link to the published post

### Working Pipelines

| Trigger | Pipeline | Output |
|---------|----------|--------|
| YouTube URL | Extract transcript → Gemini summarise → Hugo post | Blog post with video summary |
| `news` menu | Gemini grounded search → journalist prompt → Hugo post | News article |
| `research` menu | Topic → grounded search → research analyst prompt → Hugo post | Research summary |
| Any URL | Fetch page → extract text → Gemini analyse → Hugo post | URL analysis |

The key insight: Telegram is the trigger layer, not the publishing layer. Don't dump 2000-word articles into chat. Publish to a proper platform and send the link back.

## Formatting Messages

Telegram supports two formatting modes:

### Markdown (MarkdownV2)

```
*bold* _italic_ `code` ```pre``` [link](url) ~strikethrough~ ||spoiler||
```

### HTML

```html
<b>bold</b> <i>italic</i> <code>code</code> <pre>pre</pre>
<a href="url">link</a> <s>strike</s> <tg-spoiler>spoiler</tg-spoiler>
```

### What You Can't Do

- **No text colours** - there is no way to colour text in Telegram messages
- **No font size control** - everything is the same size
- **No images inline with text** - photos are separate from text messages
- **No tables** - you have to fake them with monospace text
- **Custom emoji** - requires the bot owner to have Telegram Premium or purchased usernames on Fragment

### Bot API 9.5: DateTime Entity

New in March 2026 - `MessageEntity` type `date_time` lets you show formatted dates that adapt to the user's timezone and locale.

## Streaming Responses (sendMessageDraft)

Bot API 9.3 (December 2025) added `sendMessageDraft`, which lets bots stream partial messages to users while they're being generated. As of Bot API 9.5, this is available to all bots.

This is ideal for AI chat bots - instead of waiting 5 seconds for a complete response, users see text appearing progressively. Think ChatGPT-style streaming but in Telegram.

## Payments and Monetisation

Bots can process payments natively:

- **Telegram Stars** - digital currency for in-app purchases (required for digital goods per store policies)
- **Third-party providers** - Stripe, etc. for physical goods
- **Paid media** - photos/videos behind a paywall
- **Subscriptions** - recurring payments with multiple tiers
- **Revenue sharing** - 50% of Telegram Ads revenue in your bot's chat

For a home server bot this is mostly irrelevant, but if you're building a service bot it's properly built into the platform.

## Mini Apps (Web Apps)

This is Telegram's most powerful feature and the one most people overlook. Mini Apps are full web applications (HTML/CSS/JavaScript) that run inside Telegram.

### What They Can Do

- **Full HTML5 interface** - any website can become a Mini App
- **Seamless auth** - user identity passed automatically, no login required
- **Theme matching** - CSS variables sync with user's Telegram theme in real time
- **Full-screen mode** - landscape and portrait, immersive games
- **Biometric auth** - fingerprint/face ID via native API
- **QR code scanner** - native scanner popup
- **Clipboard access** - read text from clipboard
- **Geolocation** - GPS access with user permission
- **Device sensors** - accelerometer, gyroscope, device orientation
- **Haptic feedback** - vibration patterns
- **Cloud storage** - per-bot key-value storage in Telegram's cloud
- **Device storage** - persistent local storage on user's device
- **Secure storage** - encrypted local storage for sensitive data
- **Home screen shortcuts** - add app icon to phone's home screen
- **Emoji status** - set user's Telegram status from within the app
- **Share to Stories** - share media directly to Telegram Stories
- **File downloads** - native download popup
- **Payments** - full Telegram Stars integration
- **Inline mode** - launch from any chat, not just the bot's chat

### Practical Use Cases for Home Server

- **Dashboard** - server metrics, container status, live graphs (impossible in regular messages)
- **File browser** - navigate and manage files with a real UI
- **Log viewer** - scrollable, searchable, colour-coded log viewer
- **Configuration editor** - forms with validation for editing config files
- **Camera viewer** - embed RTSP/HLS streams in an HTML5 player
- **Terminal** - web-based terminal (xterm.js) accessible from Telegram

### How to Create One

1. Host a web page on your server (any HTTP server works)
2. Include `<script src="https://telegram.org/js/telegram-web-app.js?60"></script>`
3. Set the URL in BotFather or via `setChatMenuButton`
4. Access `window.Telegram.WebApp` for theme, user data, and all native features

Mini Apps even work in the Telegram test environment with HTTP (no TLS required), which is perfect for home server development.

## Things That Don't Work (or Have Catches)

After building extensively with the Bot API, here are the gotchas:

### URL Buttons Reject Local Hostnames

`InlineKeyboardButton(url="http://myserver:8080")` → Error: "wrong http url". Telegram validates URLs and rejects anything without a proper TLD. Workaround: use full domain names or callback buttons that send the URL as text.

### Clickable Links Need Real Domains

HTML `<a>` tags in messages work, but the URL must have a recognisable TLD. `http://ubuntu4:1313/` won't be clickable. Use your Tailscale FQDN or a real domain.

### "Open Link?" Confirmation

Telegram shows a confirmation dialog every time you tap a link from a bot. Users can tick "Always allow" to disable it per-bot, but there's no way to skip it programmatically.

### Privacy Mode in Groups

By default, bots in groups only see commands directed at them (`/command@yourbot`), replies to their messages, and service messages. To see all messages, you need to disable privacy mode in BotFather and re-add the bot to the group.

### File IDs Are Bot-Specific

A `file_id` from one bot can't be used by another bot. If you run a test bot alongside your production bot, files must be re-uploaded separately.

### No Background Execution

Bots only process incoming updates. There's no "keep alive" or background thread on Telegram's side. Your server needs to implement scheduling (cron, asyncio timers) independently.

### Rate Limits

- ~30 messages per second to different chats
- ~20 messages per minute to the same chat
- ~1 message per second to the same group
- Inline query results: no specific documented limit but throttled

## iPhone-Specific Tips

### Notification Control

- Pin your bot chat for quick access
- Set custom notification sound for your bot's chat
- Use Telegram's "Mute" per-chat to silence non-urgent bots
- iOS Focus modes can filter which Telegram notifications come through

### Widgets

Telegram has iOS widgets that show recent chats. Pin your bot chat and it'll appear in the widget for one-tap access.

### Share Sheet

You can share URLs, text, and files to your Telegram bot via the iOS share sheet. This means any content from any app can be forwarded to your bot for processing.

### Background Notifications

Telegram push notifications work even when the app is closed. Your bot can send alerts about server issues, backup completions, or anything else, and you'll get them immediately.

## What's New in 2026

### Bot API 9.5 (March 2026)

- `sendMessageDraft` now available to all bots (streaming responses)
- New `date_time` message entity type
- Chat member tags

### Bot API 9.4 (February 2026)

- **Button styles** - `"primary"`, `"success"`, `"danger"` colour buttons
- **Custom emoji on buttons** - if bot owner has Premium
- Bot profile photo management via API

### Bot API 9.3 (December 2025)

- Topics in private chats with bots
- `sendMessageDraft` introduced (was restricted, now open)
- Forum topic management in private chats

## Summary

Telegram's Bot API is far more capable than most people realise. For a home server, the killer combination is:

1. **Trigger words** for instant server control from your phone
2. **Inline menus** for structured interaction without remembering commands
3. **AI integration** (Gemini, etc.) for intelligent responses and content generation
4. **Blog publishing** pipelines triggered from chat
5. **Mini Apps** for anything that needs a real interface

The main limitation is formatting - no colours, no tables, no inline images. For anything visual, Mini Apps are the answer. For everything else, the bot API with inline keyboards and callback handlers is remarkably powerful.

---

*Running Bot API 9.5 with python-telegram-bot 22.5 on Ubuntu, controlling a home server via Tailscale VPN. All services self-hosted, all data local.*