---
pubDatetime: 2026-02-24T12:00:00Z
title: "SSH Keys Setup Guide: Secure GitHub Authentication and Server Access"
postSlug: "ssh-keys-setup-guide-github-authentication"
description: "SSH Keys Setup Guide: Secure GitHub Authentication and Server Access"
tags:
  - security
  - ssh
  - git
  - tutorial
---

## Introduction

SSH (Secure Shell) keys provide a more secure and convenient way to authenticate with remote servers and Git repositories compared to traditional password authentication. When working with GitHub, VPS servers, or VPN connections like Tailscale, SSH keys offer superior security and streamlined workflows.

## Why SSH Keys Are Important

### Security Benefits

**SSH keys are significantly more secure than passwords for several reasons:**

- **Cryptographic strength**: Uses public-private key pairs instead of predictable passwords
- **Resistance to brute force**: Private keys are 256+ bits, making attacks computationally infeasible
- **No credential exposure**: Private key never leaves your machine
- **Granular control**: Each server or service can have its own key pair

### Practical Advantages

Beyond security, SSH keys improve daily workflows:

- **No password prompts**: Authenticate seamlessly after initial key setup
- **Single sign-on**: One key works across multiple services (GitHub, servers, VPNs)
- **Automated workflows**: Perfect for cron jobs, CI/CD pipelines, and backup scripts
- **Speed**: Eliminates typing passwords repeatedly

## Generating SSH Keys

### Recommended Algorithm: Ed25519

Ed25519 is the modern, recommended algorithm for SSH keys:

- **Strong security**: 256-bit elliptic curve cryptography
- **Small key size**: Public keys are concise and easy to share
- **Fast performance**: Signatures are computed quickly
- **Future-proof**: Widely supported across modern systems

### Step-by-Step Key Generation

```bash
# Generate a new SSH key pair using ed25519
ssh-keygen -t ed25519 -C "your_email@example.com"

# Output example:
# Generating public/private ed25519 key pair.
# Enter file in which to save the key (/root/.ssh/id_ed25519):
# Enter passphrase (empty for no passphrase):
# Enter same passphrase again:
```

**Command breakdown:**

- `-t ed25519`: Specifies key type as Ed25519 (recommended)
- `-C "your_email@example.com"`: Adds a comment (usually your email) for identification

**When prompted:**

1. **File location**: Press Enter to accept default (`~/.ssh/id_ed25519`)
2. **Passphrase**: Enter a strong passphrase for additional security, or leave empty for automation workflows

### Understanding Key Files

After generation, you'll have two files in `~/.ssh/`:

```
~/.ssh/
├── id_ed25519      # Private key (NEVER share this!)
└── id_ed25519.pub   # Public key (safe to share)
```

| File | Purpose | Security |
|------|---------|----------|
| `id_ed25519` | Private authentication key | **NEVER** share, upload, or expose |
| `id_ed25519.pub` | Public verification key | Safe to share with services like GitHub |

## Adding Your Public Key to GitHub

### View Your Public Key

```bash
# Display your public key content
cat ~/.ssh/id_ed25519.pub

# Output example:
# ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBjGf7hZm9... your_email@example.com
```

### Add to GitHub Account

1. **Copy the public key** (entire line, including `ssh-ed25519` prefix)
2. **Navigate to GitHub Settings**: https://github.com/settings/keys
3. **Click "New SSH key"**
4. **Paste your public key** into the "Key" field
5. **Add a descriptive title** (e.g., "Ubuntu Server" or "MacBook Pro")
6. **Click "Add SSH key"**

**Key added!** You can now authenticate with GitHub without passwords.

## Configuring SSH Agent

The SSH agent manages your keys and provides them to SSH connections, avoiding repeated passphrase prompts.

### Start SSH Agent

```bash
# Start SSH agent and set environment variables
eval "$(ssh-agent -s)"
```

### Add Your Key to Agent

```bash
# Add your private key to the agent
ssh-add ~/.ssh/id_ed25519

# If you set a passphrase during key generation,
# you'll be prompted to enter it once per session
```

### Verify Agent Has Your Key

```bash
# List all identities currently in the agent
ssh-add -l

# Output example:
# 256 SHA256:abc123... your_email@example.com (ED25519)
```

## Using SSH Keys with Git

### SSH Authentication Format

GitHub supports two authentication methods:

| Method | URL Format | Pros | Cons |
|---------|-------------|-------|-------|
| **SSH** | `git@github.com:username/repo.git` | No password prompts, more secure | Requires initial key setup |
| **HTTPS** | `https://github.com/username/repo.git` | No key setup needed | Password prompts, less secure for automation |

### Example: Cloning via SSH

```bash
# Clone a repository using SSH authentication
git clone git@github.com:username/repo.git

# No password required - SSH key handles authentication
```

### Example: Pushing via SSH

```bash
cd /media/docker/website
git remote add origin git@github.com:username/hugo-blog.git
git push -u origin main

# Authentication handled automatically via SSH key
```

## Common Use Cases

### GitHub Authentication

Used for:
- Cloning repositories
- Pushing code changes
- Pull requests and merge operations
- GitHub Actions authentication

**Example from git remote setup:**

```bash
cd /media/docs
git remote add origin git@github.com:yourusername/docs.git
git push -u origin main
```

### Server Access

Connect to remote servers without passwords:

```bash
# SSH into remote server using key authentication
ssh user@server.example.com

# Example with Tailscale hostname
ssh root@ubuntu58-1
```

### Tailscale VPN

Tailscale leverages SSH keys for secure, encrypted connections to devices on your private network:

```bash
# Access device via Tailscale using SSH key
ssh user@device-tailscale-name

# Example: Primary backup host
ssh user@ubhost
```

## Troubleshooting Common Issues

### Permission Denied (Public Key)

**Error:** `Permission denied (publickey)`

**Causes:**
1. Public key not added to GitHub account
2. Wrong key file specified (`~/.ssh/id_ed25519` vs `id_rsa`)
3. SSH agent not running or key not loaded

**Solutions:**
```bash
# 1. Verify public key is added to GitHub
cat ~/.ssh/id_ed25519.pub

# 2. Check which key files exist
ls -la ~/.ssh/

# 3. Ensure SSH agent is running
ssh-add -l

# 4. If empty, start agent and add key
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

### GitHub Fails with Port 22 Issues

**Error:** `ssh: connect to host github.com port 22: Connection timed out`

**Solution:** Check network connectivity and firewall rules
```bash
# Test GitHub SSH connectivity
ssh -T git@github.com

# Expected output: Hi username! You've successfully authenticated...
```

### Multiple GitHub Accounts

When using multiple GitHub accounts (personal vs organization):

```bash
# Create SSH config for multiple accounts
cat >> ~/.ssh/config << 'EOF'
Host github-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_personal

Host github-work
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_work
EOF

# Clone using specific account
git clone git@github-personal:username/repo.git
git clone git@github-work:orgname/repo.git
```

## Security Best Practices

### 1. Protect Private Keys

**NEVER share your private key:**

```bash
# Ensure correct permissions on private key
chmod 600 ~/.ssh/id_ed25519

# Ensure correct permissions on .ssh directory
chmod 700 ~/.ssh/
```

### 2. Use Strong Passphrases

Add a passphrase to your private key:

```bash
# Regenerate with passphrase
ssh-keygen -t ed25519 -C "your_email@example.com"

# When prompted, enter a strong passphrase
# This adds an extra layer of security even if private key is compromised
```

### 3. Disable Password Authentication

On servers, disable password authentication after SSH key is configured:

```bash
# Edit SSH daemon config
sudo nano /etc/ssh/sshd_config

# Change or add:
PasswordAuthentication no

# Restart SSH service
sudo systemctl restart sshd
```

### 4. Regular Key Rotation

Update SSH keys periodically:

```bash
# Generate new key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add new public key to GitHub
# Remove old keys from GitHub settings

# Test new authentication
ssh -T git@github.com
```

### 5. Audit SSH Authorized Keys

On servers, review which keys have access:

```bash
# View all authorized public keys
cat ~/.ssh/authorized_keys

# Remove unknown or outdated keys
```

## Automated Workflows with SSH Keys

### Cron Jobs

SSH keys enable automated scripts without password prompts:

```bash
# Example: Automated git backup script (runs via cron)
#!/bin/bash
cd /media/docs
git add .
git commit -m "Auto-backup $(date)"
git push origin main

# Works seamlessly because SSH key handles authentication
```

### Git Remote Setup Automation

From the GitHub remote setup instructions:

```bash
# Configure multiple remotes using SSH keys
cd /media/docs && git remote add origin git@github.com:$USERNAME/docs.git && git push -u origin main
cd /media/docker/commands && git remote add origin git@github.com:$USERNAME/commands.git && git push -u origin main
cd ~/backups/opencode-config && git remote add origin git@github.com:$USERNAME/opencode-config.git && git push -u origin main
```

### Backup Scripts

SSH keys enable automated VPS backups:

```bash
# SSH into backup host without password prompts
ssh user@ubhost "rsync -avz /data/ /mnt/backup/"

# Perfect for cron-scheduled backups
```

## Summary

SSH keys provide a secure, automated way to authenticate with GitHub, servers, and VPN services:

**Key Takeaways:**

1. **Generate Ed25519 keys**: `ssh-keygen -t ed25519 -C "your_email@example.com"`
2. **Add public key to GitHub**: Copy `~/.ssh/id_ed25519.pub` to GitHub settings
3. **Configure SSH agent**: Use `ssh-add` to manage keys per session
4. **Use SSH format for Git**: `git@github.com:username/repo.git`
5. **Protect private keys**: Never share, use correct permissions (`chmod 600`)
6. **Automate workflows**: SSH keys enable cron jobs and CI/CD pipelines

**Files Created:**
- Private key: `~/.ssh/id_ed25519`
- Public key: `~/.ssh/id_ed25519.pub`
- SSH config: `~/.ssh/config` (for multiple accounts)

With SSH keys properly configured, you'll have seamless, password-free authentication for GitHub, Tailscale, and remote servers—making automated backups, deployments, and development workflows significantly more efficient.

## Additional Resources

- [GitHub SSH Key Documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [OpenSSH Manual](https://man.openbsd.org/ssh)
- [Tailscale Documentation](https://tailscale.com/kb/1082/ssh)
- [SSH Key Security Best Practices](https://www.ssh.com/academy/ssh/key)