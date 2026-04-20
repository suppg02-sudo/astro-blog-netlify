---
pubDatetime: 2026-02-26T00:00:00Z
title: "SETUP.MD Simulation: OpenCode Freshstart Server Setup"
postSlug: "setup-md-simulation-opencode-freshstart"
description: "SETUP.MD Simulation: OpenCode Freshstart Server Setup"
tags:
  - server-setup
  - opencode
  - automation
  - devops
---

## Overview

This post documents a simulation of the OpenCode Freshstart setup process as defined in `SETUP.md`. The goal is to verify the current server state against the expected configuration and identify any gaps.

## Phase 0: Initial Choice

According to SETUP.md, the first step is to ask the user what they want to do:

| Option | Description |
|--------|-------------|
| **Fresh Start Setup** | Full guided setup from repository - clone, configure, validate |
| **Config Explorer** | Explore existing setup, health checks, compare with repo - no changes |

For this simulation, we selected **Fresh Start Setup**.

---

## Phase 1: Prerequisites Check

### System Requirements

| Check | Status | Details |
|-------|--------|---------|
| OpenCode | ✅ PASSED | v1.2.11 installed |
| git | ✅ PASSED | Available |
| rsync | ✅ PASSED | Available |
| SSH Key | ✅ PASSED | `~/.ssh/id_ed25519.pub` exists |
| RAM | ✅ PASSED | 7.1GB total, 3.8GB available |
| Disk | ⚠️ WARNING | 14GB free (93% used) |

**Note**: Disk usage at 93% is something to monitor, but not blocking for setup.

---

## Phase 2: Current State Analysis

Before running the setup, we analyzed what's already installed:

| Component | Status | Count/Details |
|-----------|--------|---------------|
| Repository | ✅ Already cloned | `~/freshstart` exists |
| Skills | ✅ Installed | **73 skills** (newer than 53 in docs) |
| Instructions | ✅ Installed | 47 instruction files |
| AGENTS.md | ✅ | 50KB, updated Feb 25 |
| opencode.json | ✅ | 903 bytes |
| oh-my-opencode.json | ✅ | 635 bytes |

---

## Phase 3: Setup Script Analysis

The `setup.sh` script performs the following actions:

1. **Creates backup** of existing OpenCode configuration
2. **Clones/updates** freshstart repository
3. **Copies skills** to `~/.config/opencode/skills/`
4. **Copies instructions** to `~/.config/opencode/docs/instructions/`
5. **Copies config files** (AGENTS.md, opencode.json, etc.)
6. **Sets up API keys** template in `~/.opencode.env`
7. **Installs cron scripts** to `~/cron-scripts/`
8. **Configures crontab** from repository
9. **Installs projects** (gsd-opencode, OpenAgentsControl, oh-my-opencode)

---

## Phase 4: Post-Install Verification

### Verification Results

| Component | Expected | Actual | Status |
|-----------|----------|--------|--------|
| **OpenCode Version** | Any | v1.2.11 | ✅ |
| **Skills Count** | 53+ | 73 | ✅ |
| **Instructions** | 26+ | 47 | ✅ |
| **AGENTS.md** | Exists | 50KB | ✅ |
| **opencode.json** | Exists | 903 bytes | ✅ |
| **oh-my-opencode.json** | Exists | 635 bytes | ✅ |
| **environment.md** | Exists | NOT FOUND | ❌ |
| **Cron Scripts** | 7 in ~/cron-scripts/ | 0 | ❌ |
| **Crontab** | Freshstart jobs | Custom jobs | ⚠️ Different |
| **gsd-opencode** | In ~/ | NOT FOUND | ❌ |
| **OpenAgentsControl** | In ~/ | NOT FOUND | ❌ |
| **oh-my-opencode** | In ~/ | NOT FOUND | ❌ |
| **Model Config** | `zai-coding-plan/glm-5` | `zhipuai-coding-plan/glm-4.7` | ⚠️ Different |

---

## Gaps Identified

### Missing Components

1. **environment.md** - Environment tracking file
2. **Cron Scripts** - No scripts in `~/cron-scripts/`
3. **Projects** - gsd-opencode, OpenAgentsControl, oh-my-opencode not installed in home

### Model Configuration Note

The current config uses `zhipuai-coding-plan/glm-4.7` but SETUP.md recommends `zai-coding-plan/glm-5`.

**Fix command:**
```bash
# Update all agents to glm-5
jq '.agents |= to_entries | map(.value.model = "zai-coding-plan/glm-5") | from_entries' \
   ~/.config/opencode/oh-my-opencode.json > /tmp/oh-my-new.json && \
mv /tmp/oh-my-new.json ~/.config/opencode/oh-my-opencode.json
```

---

## What Setup Would Do

If we ran `bash setup.sh` now, it would:

```
[INFO] Creating backup of existing OpenCode configuration...
[SUCCESS] Backup created at ~/.opencode-backup-TIMESTAMP

[INFO] Copying skills (60 skills)...
[SUCCESS] Copied 60 skills to ~/.config/opencode/skills/

[INFO] Copying instructions and triggers...
[SUCCESS] Copied 47 instruction files

[INFO] Copying OpenCode configuration files...
[SUCCESS] Copied and migrated paths for AGENTS.md
[SUCCESS] Copied and migrated paths for opencode.json
[SUCCESS] Copied and migrated paths for oh-my-opencode.json
[SUCCESS] Copied and migrated paths for environment.md

[INFO] Copying scripts...
[SUCCESS] Copied 7 scripts to ~/cron-scripts/

[INFO] Setting up crontab...
[SUCCESS] Crontab installed

[INFO] Installing gsd-opencode...
[SUCCESS] gsd-opencode installed to ~/gsd-opencode

[INFO] Installing OpenAgentsControl...
[SUCCESS] OpenAgentsControl installed to ~/OpenAgentsControl

[INFO] Installing oh-my-opencode...
[SUCCESS] oh-my-opencode installed to ~/oh-my-opencode

=== Setup Complete ===
```

---

## Summary

### What's Working ✅

- Core OpenCode installation is functional
- Skills and instructions are installed (73 skills, 47 instructions)
- Main configuration files are in place
- System prerequisites are met

### What's Missing ❌

- environment.md tracking file
- Cron scripts in ~/cron-scripts/
- Optional projects (gsd-opencode, OpenAgentsControl, oh-my-opencode)
- Model configuration alignment with recommended glm-5

### Recommendations

1. **Run setup.sh** to fill in missing components
2. **Update model config** to use glm-5
3. **Monitor disk space** (currently at 93% usage)
4. **Review crontab** to ensure all scheduled jobs are appropriate

---

## Next Steps

- Option 1: Run `bash ~/freshstart/setup.sh` to complete the setup
- Option 2: Fix model configuration manually
- Option 3: Copy missing components individually
- Option 4: Accept current state (working but incomplete)

---

*Simulation completed: 2026-02-26*