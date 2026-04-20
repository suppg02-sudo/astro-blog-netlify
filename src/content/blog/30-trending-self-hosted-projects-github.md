---
pubDatetime: 2026-02-25T15:08:15Z
title: "30 Trending Self-Hosted Projects on GitHub - Complete Guide"
postSlug: "30-trending-self-hosted-projects-github"
description: "30 Trending Self-Hosted Projects on GitHub - Complete Guide"
tags:
  - self-hosted
  - youtube
  - open-source
  - docker
  - privacy
---

## Introduction

Are you tired of paying monthly subscription fees for cloud services? Do you want complete control over your data without sacrificing features? You're not alone. A growing community of developers is building incredible open-source alternatives that you can host yourself - and they're often better than their commercial counterparts.

In this comprehensive guide, we'll explore 30 trending self-hosted projects on GitHub that are revolutionizing how we approach media, monitoring, productivity, and more. From media automation to AI chat applications, these tools give you data sovereignty while saving you money. Let's dive in.

## Media & Entertainment: Take Control of Your Content

### Soul Sync - Your Playlists, Your Way

Your Spotify playlists live in the cloud, but what if you could own them? **Soul Sync** autosyncs playlists from Spotify and YouTube to your Plex server, downloading missing tracks from Soulseek in FLAC quality. The smart matching algorithm identifies exactly what you need, automatically adding album art and synced lyrics from LRClib.

Features include artist discovery, automatic library scans, and a wishlist system that retries failed downloads hourly. No more losing your playlists when cloud services change policies or shut down.

### Home Screen Hero - The Ultimate Plex Dashboard

Running multiple media servers but tired of switching between interfaces? **Home Screen Hero** brings it all together with drag-and-drop widgets that combine Tautulli streaming metrics, Jellyseerr request management, and Plex library stats in one beautiful interface.

The automated collection rotation schedules let you swap collections on your home screen using weighted or least-recently-used (LRU) strategies. Library cleanup tools automatically fix broken date-added timestamps, and you can mark shows unwatched to reset your continue watching queue.

### Kino - Terminal-Powered Media Control

Prefer the keyboard over the mouse? **Kino** is a terminal client for Plex or Jellyfin with Vim-style navigation. Use HJKL keys to move, F for global search, slash for local filtering, space for playlists, and I to inspect detailed metadata.

The app autodetects your server type, walks you through authentication on first launch, and finds/configures MPV, VLC, init, or celluloid players. Automatic resuming support ensures you never lose your place. Sort by title, date, or rating with a single keystroke.

### Fave Switch - Unified User Management

Managing users across Plex, Jellyfin, Emby, Stremio, and Audiobookshelf is a headache. **Fave Switch** solves this by letting you switch between any user on your servers from one interface, adding or removing favorites instantly.

The stats dashboard shows total favorite counts by user and media type, and unified search across all integrations comes with cache warming for fast suggestions. Works with admin API keys and runs in a single Docker container on port 5050.

### Backlogger - All Your Games in One Place

Your game library is scattered across Steam, Amazon, EA, Xbox Game Pass, and local folders. **Backlogger** aggregates everything into one dashboard with smart deduplication that shows games bought on multiple platforms only once, displaying all purchase information.

Enriched with IGDB metadata, ratings, release dates, and genres, you can filter by platform or sort by rating and play time. Finally see your complete gaming collection in one place.

### D Vinyl - Manage Your Physical Collection

Still collecting vinyl records, CDs, and cassettes? **D Vinyl** is a self-hosted collection manager with Discogs API integration. Add items by scanning barcodes or entering release IDs to get metadata and market estimates.

The unified library handles all physical media formats, includes a wishlist system, and offers authentication for sharing your collection with friends. Localized in English and French with mobile-optimized dark and light modes.

### Shelfmark - Books and Audiobooks Unified

**Shelfmark** is a web interface that aggregates books and audiobooks in one place with real-time download capabilities. Features include template-based file naming, separate configs for books and audiobooks, and hard links with custom directories for Audiobookshelf integration.

Multi-user support with admin management, per-user download destinations, and four auth methods including OIDC and OAuth make this a complete solution for book lovers.

### Calibre Web Automated - Effortless eBook Management

Combine Calibre's powerful features with Calibre Web's lightweight interface. Drop eBooks into an ingest folder for automatic analysis, conversion, and import. **Calibre Web Automated** supports 27 formats with conversion to EPUB, MOBI, AZW3, KEPub, or PDF.

UI changes to covers and metadata apply to actual ebook files, so edits show up on devices like Kindle automatically. No more manual file management or format conversions.

## Monitoring & Infrastructure: Watch Everything for Free

### Checkmate - Free Monitoring That Rivals Datadog

Running servers but don't want to pay for Datadog or New Relic? **Checkmate** is open-source uptime and infrastructure monitoring that costs nothing. Monitor websites, page speed, SSL certificates, Docker containers, ports, and game servers with real-time alerts via email, Discord, Slack, or webhooks.

Includes public status pages and incident tracking. Stress tested with 1000+ monitors, it uses just 100MB RAM - incredibly lightweight for home lab environments.

### Port Tracker - Know Your Network

Tracking ports in a spreadsheet is error-prone. **Port Tracker** auto discovers every running service, container, and VM across your network, distinguishing between internal container ports and published host ports.

Add other Port Tracker instances as peers for distributed monitoring and view your entire infrastructure from one dashboard with hierarchical grouping. Finally understand what's running on your network.

### Open Workflow - Durable Workflows Without Complexity

Need workflow orchestration but don't want to deploy Temporal? **Open Workflow** provides durable workflows using your existing database without requiring an orchestration cluster.

Each operation wraps in a memoized step - if the server crashes after step completion (like charging a credit card), that step won't re-execute on resume. Workflows resume via deterministic replay, can sleep for seconds or months without resource overhead, and scale horizontally by adding workers.

### New Alert - UPS Monitoring Made Simple

Protect your servers from power issues with **New Alert**, a self-hosted monitoring system for Network UPS Tools (NUT). Connects to your NUT server, autodetects UPS devices on first launch, and generates default config automatically.

Real-time visualization of battery level, load, runtime, and input voltage on port 8087. Customizable alerts trigger on specific conditions with push notifications to Discord, Slack, email, Telegram, or Apprise.

### Kron Pulse - Monitor Your Scheduled Jobs

**Kron Pulse** is a self-hosted monitoring service for scheduled jobs. Jobs ping start and okay endpoints, and if the expected okay doesn't arrive, you get instant alerts via webhook to Slack, Discord, PagerDuty, or email.

Features SQLite database with volume persistence, full REST API with documentation, web UI on port 8000, and enterprise security including JWT auth, HTTPS via reverse proxy, and CORS restriction.

### Self-Host ROI Calculator - Quantify Your Savings

Is self-hosting actually saving you money? This **Self-Host ROI Calculator** is a single HTML file that calculates whether self-hosting saves money compared to streaming services.

Input NAS and hard drive costs, monthly power usage (watts × kilowatt price), VPS/VPN usage costs, and streaming subscriptions you'd cancel. Shows monthly difference in cost and ROI payback time in months or years. Add custom services as needed for personalized calculations.

## Security & Access Control: Protect Your Infrastructure

### Octetium - Unified Secure Access Platform

**Octetium** is a self-hosted unified secure access platform on Kubernetes. Functions include remote access VPN, ZTNA platform, API gateway, AI gateway, MCP gateway, Pass and Enrock alternative, all-in-one WireGuard, and quick tunnels for clients.

Clientless BeyondCorp mode for browsers and Layer 7 per-request access control using CEL and Open Policy Agent. No blanket network rules - granular, policy-based access for modern security needs.

### Trace - Catch Account Sharers Automatically

You share your Plex account with a friend, who shares with their roommate, who shares with their cousin. Now you're streaming to 12 people across three continents. **Trace** is a detection system that catches account sharers automatically.

Five rule types for detection: impossible travel, simultaneous locations, device velocity, concurrent stream limits, and geo restrictions. Discord webhooks fire instantly when rules trigger, so you know immediately when abuse occurs.

## Development & Productivity Tools: Work Smarter

### Outline - Notion, But Self-Hosted

**Outline** is an open-source knowledge base with real-time collaborative editing, Notion-style interface, slash commands, nested documents, collections, permissions, and version history. Markdown compatible with import/export, but you host it yourself - your infrastructure, your data.

Docker compose with PostgreSQL, Redis, and S3 storage makes deployment straightforward. Finally have a knowledge base that respects your privacy.

### FrnkMD - Markdown Blogging Without Databases

**FrnkMD** is a self-hosted markdown editor for blog writing. It's a Rails app with no database, working directly with markdown files on your file system. AI helpers for S3 image upload, Nanobanana image generation, and YouTube embed search streamline content creation.

Features CodeMirror syntax highlighting, live preview, visual table editor, offline local storage, and recovery dialogue showing side-by-side diffs after crashes. Your content is just markdown files - no database lock-in.

### Invoice Builder - Offline-First Invoicing

Freelancers need reliable invoicing without cloud dependencies. **Invoice Builder** is an offline-first invoicing desktop app. Create invoices and quotations, export PDFs, and configure number and date formatting.

Your data stays in a local database file - choose SQLite for single-user or PostgreSQL for multi-device by connecting your own server. Optional Docker deployment for self-hosting, built with React and NodeJS.

### Veraritos Kanban - Kanban with Markdown Files

**Veraritos Kanban** is a lightweight Kanban board where tasks are plain markdown files. Full REST API for agent integration with built-in agent service using OpenClaw orchestration.

Click "start agent" on a code task - the server writes to an agent queue, the agent picks up work, updates status, tracks time, commits code, and calls completion endpoint when done. Productivity meets automation.

### Doppelganger - Browser Automation Made Visual

**Doppelganger** is a self-hosted browser automation platform built on Playwright with a drag-and-drop block editor for automation workflows. Actions include clicks, typing, waits, hovers, and JavaScript execution.

Features proxy rotation with HTTP and SOCKS support, automatic IP switching per task, one-click proxy list imports, auto captures screenshots and recordings, and stores cookies with a captures tab for viewing or downloading assets. Browser automation made accessible.

### Ask For Me - Human-in-the-Loop Simplified

Need a human decision mid-workflow but don't want to build an entire approval system? **Ask For Me** gives you human-in-the-loop in one synchronous request.

Send an API call with buttons or text input. Get a notification link on your phone via Serverchan or Apprise. Click a button or type text, and the original HTTP Longpoll request receives result immediately. Perfect for workflows requiring human approval at specific points.

### PAM - SQL Query Manager

**PAM** is a CLI tool for saving and executing SQL queries. Built with bubbletea, it stores queries with tags and descriptions and executes them across PostgreSQL, MySQL, SQLite, SQL Server, or Oracle.

File-based storage - no external database. Queries stored as files. Cross-platform single Go binary. Install with `go install` or use Nix flake for NixOS. Simplify database operations across multiple platforms.

## File Management & Storage: Share Securely

### DD Wrap - Make DD Safe and Easy

The `dd` command is powerful but dangerous. **DD Wrap** is a lightweight Qt wrapper around DD written in Python. Select source image and target device graphically with real-time progress showing percentage and estimated time remaining.

Final confirmation dialog shows device capacity, partition layout, and smart health data before writing. Displays actual DD command being executed for transparency. Makes disk writing operations safe and user-friendly.

### Safebucket - Secure File Sharing on Your Infrastructure

Sharing files with clients from AWS S3 means downloading, emailing, and credential risks. **Safebucket** gives you secure file sharing on existing infrastructure. Open source platform creates buckets with role-based access on any S3-compatible storage.

Works with AWS S3, Google Cloud Storage, MinIO - whatever you use. Plug in corporate SSO to eliminate local login. Users share files with existing identities - no credential sharing required.

### Hash (Calendar) - Client-Side Calendar Sharing

**Hash** is a client-side calendar app that stores all events, settings, and time zones in a compressed URL hash. Share URL to give someone full calendar with no backend sync required.

Optional password protection uses AES-GCM encryption without server involvement. Multiple views, world clock with saved time zones, QR codes for mobile handoff, and browser notifications. Calendar sharing that respects privacy.

## AI & Automation: Intelligence You Control

### Price Ghost - Multi-Method Price Tracking

**Price Ghost** is a self-hosted price tracker that runs four extraction methods in parallel: JSON-LD, metatags, CSS selectors, and AI. Each method "votes" on the price.

When they agree, you're set. When they disagree, you see all candidates with context and make the final call. AI verification catches mistakes like scraping savings amount instead of actual price. Works without AI using multiple scraping strategies as fallback.

### Neatmail - AI Email Organization

**Neatmail** is an AI-powered email organizer that watches your Gmail in real time via Pub/Sub webhooks, classifies emails with GPT-4 as they arrive, and applies labels in your Gmail interface automatically.

Preset categories include action needed, pending response, automated alerts, discussion, and marketing. Create custom labels with custom colors. 95% confidence threshold - only labels when AI is confident. Email management on autopilot.

### XPrivo - Private AI Chat Without Logging

**XPrivo** is an open-source AI chat app that stores conversations in browser local storage with zero logging and no account required. Self-host or use the hosted version at xprivo.com with EU-hosted Mistral 3 and DeepSeek v3.2.

Two models guarantee zero data retention. Bring your own API keys from OpenAI or Anthropic to use their models directly, or connect Llama for offline operation. Private AI conversations that stay on your device.

## Other Notable Projects

### Home.OS Mac OS - Cloud-Based Operating System

**Home.OS Mac OS** is a complete cloud operating system running on anything - Raspberry Pi Zero to workstations, Linux to macOS to Windows, ARM to x86. The killer feature is Prism window manager, bringing an actual desktop experience to your browser with real multitasking, multiple themes, and simultaneous tasks.

One-click app store, preconfigured SSL, and automatic migration from Umbrel or Casa OS. Your desktop, accessible anywhere, running on your own infrastructure.

### Backlogger - Game Library Aggregator

(Self-hosted game library aggregator with smart deduplication, IGDB metadata enrichment, filtering by platform and sorting by rating or play time - covered in Media & Entertainment section above.)

## Key Trends and Takeaways

### Privacy First: Data Sovereignty is Non-Negotiable

Every project in this list emphasizes **self-hosting for privacy**. Keep your data on your own infrastructure instead of cloud services. This aligns with growing concerns about data ownership, third-party access, and arbitrary policy changes from commercial providers.

### Cost Savings: Replace Expensive Subscriptions

Multiple tools help reduce monthly subscription costs:
- **Checkmate** replaces Datadog/New Relic (free vs. hundreds per month)
- **Soul Sync** eliminates cloud music service fees
- **Home Screen Hero** removes need for multiple dashboard subscriptions
- **ROI Calculator** quantifies your actual savings from self-hosting

### Lightweight Design: Optimized for Home Labs

Projects prioritize resource efficiency:
- **Checkmate**: 100MB RAM for 1000+ monitors
- **Single HTML files**: ROI Calculator, Hash Calendar (no backend required)
- **No database options**: FrnkMD and Veraritos Kanban use markdown files directly
- **Docker containers**: Most projects deploy easily with minimal resources

### Modern Tech Stack: Go, Python, Docker, and More

Popular technologies across these projects:
- **Docker**: Primary deployment method for most services
- **Go**: Popular for CLI tools (PAM, Kino, Fave Switch)
- **Python**: Common for web services and automation (DD Wrap, Price Ghost)
- **React/NodeJS**: Frontend frameworks for desktop apps
- **SQLite**: Lightweight database for small applications

### Integration Focus: Work with What You Have

Many projects **integrate existing services** rather than replacing them:
- **Fave Switch** manages users across multiple media servers
- **Shelfmark** integrates with Audiobookshelf
- **Safebucket** works with existing S3 infrastructure
- **New Alert** connects to Network UPS Tools

## Who Should Use These Projects?

**Home Lab Enthusiasts**: If you're already running Docker containers and multiple services, these tools will level up your infrastructure with unified dashboards, better monitoring, and automation.

**Privacy-Conscious Users**: If you care about data sovereignty and don't want your information processed by third parties, these self-hosted alternatives give you complete control.

**System Administrators**: Managing multiple servers becomes easier with unified monitoring, security platforms, and automation tools.

**Developers**: Open-source alternatives to SaaS products that you can customize, contribute to, and deploy on your own terms.

**Media Collectors**: Whether you collect games, books, music, or vinyl, dedicated tools help organize and manage your collections with rich metadata.

## Getting Started

Most projects in this list are ready to deploy with minimal setup:

1. **Choose your project** based on your needs
2. **Check requirements** (Docker, specific databases, dependencies)
3. **Clone the repository** from GitHub
4. **Follow deployment instructions** (usually Docker compose)
5. **Configure** according to your environment
6. **Start enjoying** your self-hosted alternative

## Conclusion

These 30 trending self-hosted projects demonstrate that open-source alternatives aren't just "good enough" - they often **exceed commercial offerings** with innovative features like:

- Human-in-the-loop approval systems (Ask For Me)
- Multi-method consensus price tracking (Price Ghost)
- Browser-based cloud operating systems (Home.OS Mac OS)
- Zero-knowledge AI chat (XPrivo)
- Terminal-powered media control (Kino)

Whether you're running a home lab or just want privacy-focused alternatives, there's a project here for you. All are free, open-source, and give you **complete ownership of your data**.

Start small, experiment with one or two projects, and gradually build your self-hosted infrastructure. The freedom, control, and cost savings are worth the investment.

---

## Reference Files

For more detailed information about this video and its content:

- **Full Transcript**: See the complete transcript file in your resources
- **Comprehensive Summary**: Detailed breakdown of all 30 projects with technical specifications
- **Short Summary**: Quick overview with key insights and bottom line

---

*Video source: Github Awesome on YouTube (https://youtu.be/IS9PcrqLvIQ)*