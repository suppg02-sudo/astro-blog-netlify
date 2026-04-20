---
pubDatetime: 2026-02-12T16:30:00Z
title: "Implementing Dual-Service: OpenClaw Gateway + OpenCode Teams Integration"
postSlug: "implementing-dual-service-openclaw-opencode-teams"
description: "Complete setup guide for dual-service architecture: Running OpenClaw gateway separately and calling it from OpenCode agents via HTTP wrapper skill."
tags:
  - opencode
  - integration
  - openclaw
  - setup
  - microsoft-teams
---

## Dual-Service Implementation Guide

This guide walks you through setting up **OpenClaw Gateway + OpenCode Teams Integration** in a dual-service architecture.

## Architecture Diagram

{{< mermaid >}}
graph TB
    Teams["Microsoft Teams<br/>User Messages"]
    
    subgraph Gateway["OpenClaw Gateway<br/>Separate Server"]
        Plugin["Teams Plugin<br/>Port 3978"]
        GatewayCore["Gateway Core<br/>Port 18789"]
    end
    
    subgraph OpenCodeEnv["OpenCode Environment"]
        Skill["Teams Integration Skill<br/>HTTP Wrapper"]
        Agent["OpenCode Agent"]
    end
    
    Teams -->|Webhook| Plugin
    Plugin --> GatewayCore
    GatewayCore -->|Sessions| LLM["Pi Agent Runtime<br/>LLM Execution"]
    
    Agent -->|HTTP POST| Skill
    Skill -->|POST /api/send| GatewayCore
    
    style Gateway fill:#4a90e2,color:#fff
    style OpenCodeEnv fill:#7ed321,color:#000
    style Plugin fill:#f5a623,color:#fff
    style Skill fill:#9013fe,color:#fff
    style Agent fill:#9013fe,color:#fff
{{< /mermaid >}}

## Setup Steps

### Step 1: Install & Configure OpenClaw Gateway (Separate Machine/Server)

**On your OpenClaw server:**

```bash
# Install OpenClaw globally
npm install -g openclaw@latest

# Create config directory
mkdir -p ~/.openclaw

# Create openclaw.json config
cat > ~/.openclaw/openclaw.json << 'EOF'
{
  "gateway": {
    "port": 18789,
    "bind": "0.0.0.0",
    "auth": {
      "mode": "token",
      "token": "YOUR_SECURE_TOKEN_HERE"
    }
  },
  "channels": {
    "msteams": {
      "enabled": true,
      "appId": "YOUR_AZURE_BOT_APP_ID",
      "appPassword": "YOUR_AZURE_BOT_CLIENT_SECRET",
      "tenantId": "YOUR_AZURE_TENANT_ID",
      "webhook": {
        "port": 3978,
        "path": "/api/messages"
      }
    }
  }
}
EOF
```

**Set environment variables (instead of config file if preferred):**

```bash
# Add to ~/.bashrc or ~/.zshrc
export OPENCLAW_GATEWAY_TOKEN="YOUR_SECURE_TOKEN_HERE"
export MSTEAMS_APP_ID="YOUR_AZURE_BOT_APP_ID"
export MSTEAMS_APP_PASSWORD="YOUR_AZURE_BOT_CLIENT_SECRET"
export MSTEAMS_TENANT_ID="YOUR_AZURE_TENANT_ID"
```

**Install Teams plugin:**

```bash
openclaw plugins install @openclaw/msteams
```

**Verify installation:**

```bash
openclaw plugins list
# Should show: @openclaw/msteams
```

### Step 2: Azure Bot Setup (One-Time)

Follow the OpenClaw Teams documentation:

**Create Azure Bot:**
1. Go to [Azure Portal](https://portal.azure.com)
2. Create → Bot Resource
3. Fill in:
   - Bot handle: `openclaw-teams-bot`
   - Pricing tier: Free
   - Type: Single Tenant
4. Click Create

**Get Credentials:**
1. Go to Configuration → Microsoft App ID (copy this)
2. Click "Manage Password" → New client secret (copy this)
3. Go to Overview → Directory ID (copy this)

**These are your credentials:**
- `appId`: Microsoft App ID
- `appPassword`: Client Secret Value
- `tenantId`: Directory (tenant) ID

**Configure Messaging Endpoint:**
1. In Azure Bot → Configuration
2. Set Messaging Endpoint to: `https://YOUR_GATEWAY_DOMAIN:3978/api/messages`
   - For ngrok: `https://abc123.ngrok.io/api/messages`
   - For Tailscale Funnel: `https://your-tailscale-funnel-url/api/messages`

**Enable Teams Channel:**
1. Go to Channels
2. Click Microsoft Teams → Configure → Save

### Step 3: Start OpenClaw Gateway

**Option A: Manual Start (Testing)**

```bash
openclaw gateway --port 18789 --verbose
```

**Option B: As Systemd Service (Production)**

Create `/etc/systemd/user/openclaw-gateway.service`:

```ini
[Unit]
Description=OpenClaw Gateway for Teams Integration
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/local/bin/openclaw gateway --port 18789 --verbose
Restart=on-failure
RestartSec=10
Environment="PATH=/usr/local/bin:/usr/bin"

[Install]
WantedBy=default.target
```

Enable and start:

```bash
systemctl --user enable openclaw-gateway.service
systemctl --user start openclaw-gateway.service
systemctl --user status openclaw-gateway.service
```

**Verify it's running:**

```bash
curl -s http://localhost:18789/health
# Should return gateway status
```

### Step 4: Expose Gateway to OpenCode (Networking)

**If OpenCode is on the same machine:**
- Use `http://localhost:18789` (no exposure needed)

**If OpenCode is on different machine:**

**Option A: Tailscale (Recommended)**

```bash
# On gateway machine
tailscale serve tcp/18789

# On OpenCode machine
# Access at: http://GATEWAY_HOSTNAME:18789
```

**Option B: SSH Tunnel**

```bash
# From OpenCode machine
ssh -L 18789:localhost:18789 user@gateway-host

# Then access at: http://localhost:18789
```

**Option C: Firewall Rules (Less Secure)**

```bash
# On gateway machine
sudo ufw allow 18789/tcp
sudo ufw allow 3978/tcp
```

## Step 5: Create OpenCode Teams Skill

Create `/root/.opencode/skill/openclaw-teams/SKILL.md`:

```markdown
# Skill: OpenClaw Teams Integration

## Description

HTTP wrapper to send Microsoft Teams messages via OpenClaw Gateway.

## Environment

- Gateway URL: `http://localhost:18789` (or remote URL)
- Gateway Token: See openclaw.json or env vars
- Webhook Port: 3978 (for incoming Teams messages)

## Tools

### send_teams_message

Send a message to Teams via OpenClaw gateway.

**Parameters:**
- `target` (string, required): Teams target
  - User DM: `user:USER_ID` or `user:Display Name`
  - Channel: `channel:CHANNEL_ID` or `channel:Channel Name`
  - Group chat: `group:GROUP_ID`
- `text` (string, required): Message text (supports Markdown)
- `gateway_url` (string): Override default gateway URL
- `gateway_token` (string): Override default gateway token

**Example:**

```typescript
await send_teams_message({
  target: "user:john@company.com",
  text: "Hello from OpenCode! 👋"
})
```

### send_teams_card

Send an Adaptive Card to Teams (rich formatting).

**Parameters:**
- `target` (string, required): Teams target
- `card` (object, required): Adaptive Card JSON
- `gateway_url` (string): Override gateway URL
- `gateway_token` (string): Override gateway token

**Example:**

```typescript
await send_teams_card({
  target: "channel:My Team - General",
  card: {
    type: "AdaptiveCard",
    version: "1.4",
    body: [
      {
        type: "TextBlock",
        text: "Agent Status Report",
        weight: "bolder",
        size: "large"
      },
      {
        type: "TextBlock",
        text: "All systems operational",
        wrap: true
      }
    ]
  }
})
```

## Configuration

Add to your agent config:

```json
{
  "skills": {
    "openclaw-teams": {
      "gatewayUrl": "http://localhost:18789",
      "gatewayToken": "YOUR_SECURE_TOKEN_HERE"
    }
  }
}
```

Or use environment variables:

```bash
export OPENCLAW_GATEWAY_URL="http://localhost:18789"
export OPENCLAW_GATEWAY_TOKEN="YOUR_SECURE_TOKEN_HERE"
```

## Files

- `openclaw-teams-sdk.ts` - HTTP client for gateway
- `teams-actions.ts` - Tool implementations

Base directory: `/root/.opencode/skill/openclaw-teams/`
```

Create the TypeScript implementation `/root/.opencode/skill/openclaw-teams/openclaw-teams-sdk.ts`:

```typescript
import fetch from 'node-fetch';

export type TeamsTarget = 
  | `user:${string}` 
  | `channel:${string}` 
  | `group:${string}`;

export interface SendMessageOptions {
  target: TeamsTarget;
  text: string;
  gatewayUrl?: string;
  gatewayToken?: string;
}

export interface SendCardOptions {
  target: TeamsTarget;
  card: Record<string, any>;
  gatewayUrl?: string;
  gatewayToken?: string;
}

export async function sendTeamsMessage(options: SendMessageOptions) {
  const gatewayUrl = options.gatewayUrl || process.env.OPENCLAW_GATEWAY_URL || 'http://localhost:18789';
  const token = options.gatewayToken || process.env.OPENCLAW_GATEWAY_TOKEN;

  if (!token) {
    throw new Error('Missing OPENCLAW_GATEWAY_TOKEN');
  }

  try {
    const response = await fetch(`${gatewayUrl}/api/send`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        channel: 'msteams',
        target: options.target,
        text: options.text,
        type: 'text'
      })
    });

    if (!response.ok) {
      throw new Error(`Gateway error: ${response.status} ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    throw new Error(`Failed to send Teams message: ${error.message}`);
  }
}

export async function sendTeamsCard(options: SendCardOptions) {
  const gatewayUrl = options.gatewayUrl || process.env.OPENCLAW_GATEWAY_URL || 'http://localhost:18789';
  const token = options.gatewayToken || process.env.OPENCLAW_GATEWAY_TOKEN;

  if (!token) {
    throw new Error('Missing OPENCLAW_GATEWAY_TOKEN');
  }

  try {
    const response = await fetch(`${gatewayUrl}/api/send`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        channel: 'msteams',
        target: options.target,
        card: options.card,
        type: 'card'
      })
    });

    if (!response.ok) {
      throw new Error(`Gateway error: ${response.status} ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    throw new Error(`Failed to send Teams card: ${error.message}`);
  }
}
```

### Step 6: Test End-to-End

**Test 1: Gateway Health Check**

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:18789/api/health
```

**Test 2: Send Message via OpenCode**

In an OpenCode agent:

```typescript
import { sendTeamsMessage } from './openclaw-teams-sdk.ts';

await sendTeamsMessage({
  target: 'user:john@company.com',
  text: 'Test message from OpenCode! 🚀'
});
```

**Test 3: Full Conversation Flow**

```bash
# 1. User sends message in Teams
# 2. Teams webhook hits gateway:3978
# 3. Gateway routes to OpenCode agent
# 4. Agent processes request
# 5. Agent calls Teams skill to send response
# 6. Response appears in Teams
```

## Troubleshooting

### Gateway Not Starting

```bash
# Check if port 18789 is in use
ss -tlnp | grep 18789

# Check logs
journalctl --user -u openclaw-gateway.service -f
```

### Teams Webhook Not Reaching Gateway

```bash
# Test messaging endpoint
curl -X POST https://YOUR_MESSAGING_ENDPOINT/api/messages \
  -H "Content-Type: application/json" \
  -d '{"type":"message","text":"test"}'
```

### OpenCode Can't Connect to Gateway

```bash
# Test gateway connectivity
curl http://GATEWAY_URL:18789/health

# Check firewall
sudo ufw status
sudo ufw allow 18789/tcp
```

### Invalid Token

```bash
# Verify token matches config
cat ~/.openclaw/openclaw.json | grep token

# Check env var
echo $OPENCLAW_GATEWAY_TOKEN
```

## Summary

| Component | Purpose | Port |
|-----------|---------|------|
| **Azure Bot** | Teams integration point | (managed by Azure) |
| **OpenClaw Gateway** | Teams plugin + WebSocket server | 18789 |
| **Teams Webhook** | Incoming message receiver | 3978 |
| **OpenCode Skill** | HTTP wrapper for gateway calls | (same as agent) |

---

**Next Steps:**
1. Install OpenClaw on your server
2. Create Azure Bot + get credentials
3. Configure openclaw.json
4. Start gateway service
5. Create OpenCode Teams skill
6. Test message send/receive

This dual-service architecture gives you:
- ✅ Full Teams support via OpenClaw
- ✅ OpenCode agent integration via HTTP
- ✅ Separation of concerns
- ✅ Easy to scale (add more OpenCode agents)