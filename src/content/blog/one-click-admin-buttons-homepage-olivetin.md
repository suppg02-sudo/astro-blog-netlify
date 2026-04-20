---
pubDatetime: 2026-02-27T09:30:00Z
title: "One-Click Admin Buttons: Homepage + OliveTin Integration"
postSlug: "one-click-admin-buttons-homepage-olivetin"
description: "One-Click Admin Buttons: Homepage + OliveTin Integration"
tags:
  - automation
  - homelab
  - dashboard
  - docker
---

Setting up admin task buttons on your homelab dashboard shouldn't require context switching. Here's how to create one-click action buttons on Homepage that trigger OliveTin commands.

## The Problem

Homepage is great for a services dashboard, but clicking a service just opens its web UI. What if you want a button that actually **does something** - like restart a container or run a backup?

## The Solution

A simple relay service that converts Homepage's GET requests into OliveTin's POST webhooks.

## Architecture

```
Homepage (port 8765)
    │
    └── Click button → GET request
            │
            ▼
Relay Service (port 8899)
    │
    └── Converts GET → POST
            │
            ▼
OliveTin (port 1337)
    │
    └── Executes shell command
```

## Step 1: Configure OliveTin Actions

Add actions with IDs to `/media/docker/olivetin/config/config.yaml`:

```yaml
actions:
  - title: "🔄 Restart AI Stack"
    id: restart-ai-stack
    shell: docker restart openmemory-openmemory-1 n8n memos
    icon: robot
    timeout: 60
    execOnWebhook:
      - matchQ:
          action: restart-ai-stack

  - title: "🧹 Safe Docker Cleanup"
    id: docker-cleanup
    shell: docker system prune -f && docker image prune -f
    icon: trash
    timeout: 120
    execOnWebhook:
      - matchQ:
          action: docker-cleanup

  - title: "💾 Backup Configs"
    id: backup-configs
    shell: mkdir -p /config/backups && tar -czvf /config/backups/backup-$(date +%Y%m%d-%H%M%S).tar.gz -C /config . --exclude=backups
    icon: save
    timeout: 60
    execOnWebhook:
      - matchQ:
          action: backup-configs

  - title: "🏥 Health Check All"
    id: health-check
    shell: |
      echo "=== Docker Containers ===" && docker ps --format "table {{.Names}}\t{{.Status}}" | head -10
      echo "=== Memory ===" && free -h
      echo "=== Disk ===" && df -h / /media 2>/dev/null | head -5
    icon: heartbeat
    timeout: 30
    execOnWebhook:
      - matchQ:
          action: health-check
```

## Step 2: Create the Relay Service

Create `/media/docker/relay/relay.py`:

```python
#!/usr/bin/env python3
"""Simple GET to POST relay for OliveTin webhooks."""
import http.server
import socketserver
import urllib.request
import urllib.parse

OLIVETIN_URL = "http://localhost:1337/webhooks"
PORT = 8899

class RelayHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        
        if params.get('action'):
            action = params['action'][0]
            data = urllib.parse.urlencode({'action': action}).encode()
            
            try:
                req = urllib.request.Request(OLIVETIN_URL, data=data, method='POST')
                with urllib.request.urlopen(req, timeout=30) as response:
                    result = response.read().decode()
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f"""
                <html>
                <head><title>Action Triggered</title>
                <meta http-equiv="refresh" content="2;url=http://ubuntu4:8765">
                <style>
                    body {{ font-family: system-ui; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: #1a1a2e; color: #eee; }}
                    .card {{ background: #16213e; padding: 2rem; border-radius: 1rem; text-align: center; }}
                    .success {{ color: #4ade80; font-size: 3rem; }}
                </style>
                </head>
                <body>
                <div class="card">
                    <div class="success">✓</div>
                    <h2>{action}</h2>
                    <p>Action triggered successfully!</p>
                    <p><small>Returning to dashboard...</small></p>
                </div>
                </body>
                </html>
                """.encode())
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"<html><body><h1>Error</h1><pre>{e}</pre></body></html>".encode())

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), RelayHandler) as httpd:
        print(f"Relay server running on port {PORT}")
        httpd.serve_forever()
```

Create `/media/docker/relay/docker-compose.yml`:

```yaml
services:
  relay:
    image: python:3.11-alpine
    container_name: relay
    restart: unless-stopped
    command: python3 /app/relay.py
    volumes:
      - ./relay.py:/app/relay.py:ro
    network_mode: host
```

Start the relay:

```bash
cd /media/docker/relay && docker compose up -d
```

## Step 3: Add Buttons to Homepage

Add to `/media/docker/home/config/services.yaml`:

```yaml
- Admin Tasks:
    - Restart AI Stack:
        icon: https://api.iconify.design/mdi:robot.svg?color=%23ff6b6b
        href: http://ubuntu4:8899?action=restart-ai-stack
        description: ⚡ Click to execute
    - Docker Cleanup:
        icon: https://api.iconify.design/mdi:broom.svg?color=%2369db7c
        href: http://ubuntu4:8899?action=docker-cleanup
        description: ⚡ Click to execute
    - Backup Configs:
        icon: https://api.iconify.design/mdi:content-save.svg?color=%23ffd43b
        href: http://ubuntu4:8899?action=backup-configs
        description: ⚡ Click to execute
    - Health Check:
        icon: https://api.iconify.design/mdi:heart-pulse.svg?color=%23f06595
        href: http://ubuntu4:8899?action=health-check
        description: ⚡ Click to execute
```

## The Result

| Button | Action |
|--------|--------|
| 🤖 Restart AI Stack | Restarts OpenMemory, n8n, Memos |
| 🧹 Docker Cleanup | Safe prune (cache + dangling images) |
| 💾 Backup Configs | Saves OliveTin config to tar.gz |
| 💓 Health Check | Shows docker/memory/disk status |

Click any button → action executes → auto-returns to dashboard in 2 seconds.

## Why This Works

1. **Homepage** only supports GET links (no POST support)
2. **OliveTin** webhooks require POST requests
3. **Relay service** bridges the gap: GET → POST conversion
4. **User experience**: Single click, visual feedback, auto-return

No more opening separate tabs or navigating to OliveTin. Your admin tasks are now one click away from your main dashboard.