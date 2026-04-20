---
pubDatetime: 2026-02-23T12:00:00Z
title: "Adding OpenMemory Installation Guide to Freshstart Repository"
postSlug: "adding-openmemory-installation-guide-to-freshstart"
description: "Adding OpenMemory Installation Guide to Freshstart Repository"
tags:
  - openmemory
  - freshstart
  - installation
  - docker
  - guide
---

I've created a comprehensive OpenMemory installation guide and integrated it into the freshstart repository structure. This guide allows you to easily install the latest version of OpenMemory v1.2.3 on new machines with Docker and Tailscale pre-installed.

## Overview

The integration adds a complete OpenMemory installation system to your freshstart repository that:
- Provides guided installation with agent support
- Uses the question tool to present options to users
- Includes all necessary files and scripts
- Follows a standardized structure for future extensibility

## What Was Created

### File Structure

The integration creates a new `INSTALLATION-GUIDES/` directory in the freshstart repository:

```
freshstart/
├── README.md
├── setup.md                          # Updated with menu integration
├── INSTALLATION-GUIDES/                # New directory
│   ├── README.md                     # Index of all guides
│   └── openmemory-installation.md     # OpenMemory guide
└── [existing files...]
```

### Installation Guide Components

**1. INSTALLATION-GUIDES/README.md** (Index File)
- Lists all available installation guides
- Describes each guide with features and prerequisites
- Provides quick start instructions
- Includes framework for adding future guides

**2. INSTALLATION-GUIDES/openmemory-installation.md** (Complete Guide)
- Comprehensive OpenMemory v1.2.3 installation instructions
- 12-phase installation process with verification
- User question prompts (hostname, API key, preferences)
- Optional components (OpenCode integration, automation scripts)
- Full troubleshooting guide
- Quick reference commands

**3. setup.md Integration** (Menu System)
- Installation guides menu section
- Question tool integration for presenting options
- Agent instructions for menu flow
- Reference to INSTALLATION-GUIDES directory

## How It Works

### User Flow

The installation system follows this flow:

{{< mermaid >}}
graph LR
    A[User runs setup.md] --> B[Agent presents menu]
    B --> C{User selects OpenMemory}
    C --> D[Agent reads INSTALLATION-GUIDES]
    D --> E[Ask user questions]
    E --> F[Execute installation]
    F --> G[Verify and test]
    G --> H[Report completion]
{{< /mermaid >}}

### Question Tool Integration

When a user selects "OpenMemory Installation" from the menu:

1. **Agent presents options** using question tool
2. **User answers configuration questions**:
   - What is this machine's Tailscale hostname?
   - Do you have an OpenAI API key for embeddings?
   - Should OpenCode integration be configured automatically?
   - Which automation scripts should be installed (all/backup/none)?

3. **Agent executes installation** following the guide step-by-step
4. **Optional components** are configured based on user's choices
5. **Agent reports completion** with access URLs

## Installation Phases

The OpenMemory guide includes 12 comprehensive phases:

### Phase 1: Pre-Installation Verification
- Check Docker status
- Verify Tailscale connectivity
- Confirm disk space and RAM availability

### Phase 2: Clone Repository
- Clone OpenMemory from GitHub
- Checkout latest main branch
- Verify version

### Phase 3: Configuration Setup
- Create .env file with all required variables
- Configure OpenAI API key (or use synthetic embeddings)
- Set up database and tier settings

### Phase 4: Port Selection
- Auto-select available API port (8080-8099)
- Auto-select available Dashboard port (13120-13199)
- Update docker-compose.yml with selected ports

### Phase 5: Build and Deploy
- Build Docker containers
- Start OpenMemory API and Dashboard
- Verify container health

### Phase 6: Verification
- Test API health endpoint
- Test MCP server endpoint
- Verify Dashboard accessibility

### Phase 7: Testing
- Store test memory via API
- Retrieve and verify memory
- Test semantic search functionality

### Phase 8: Optional OpenCode Integration
- Update ~/.config/opencode/opencode.json
- Configure MCP server settings
- Verify integration works

### Phase 9: Optional Automation Scripts
Based on user's choice:
- **Option A**: Install all scripts (backup, WAL monitoring, decay stats)
- **Option B**: Install backup script only
- **Option C**: No automation (manual management)

### Phase 10: Configuration Summary
- Display access URLs
- Document installed configuration
- Provide quick reference commands

### Phase 11: Troubleshooting Guide
- Common issues and solutions
- Debug commands
- Recovery procedures

### Phase 12: Maintenance
- Update procedures
- Backup strategies
- Monitoring recommendations

## Key Features

### Auto-Selected Ports
- Avoids port conflicts by auto-selecting from available ranges
- API: 8080-8099
- Dashboard: 13120-13199

### Flexible Configuration Options
- OpenAI embeddings (high quality) or synthetic mode
- Optional OpenCode integration
- Optional automation scripts (all/backup/none)
- User choice at installation time

### Comprehensive Documentation
- Prerequisites checklist
- Installation verification
- Troubleshooting guide
- Quick reference commands
- Maintenance instructions

### Extensible Structure
- Easy to add more installation guides
- Standardized format for consistency
- README.md index for all guides

## Required Information

Before starting installation, users need to have ready:

1. **Machine Hostname**: Tailscale hostname (e.g., "ubuntu4", "server-name")
2. **OpenAI API Key**: API key for embeddings (or use synthetic)
3. **OpenCode Integration**: Yes (auto-configure) or No (manual)
4. **Automation Level**: All scripts / Backup only / None

## Access URLs After Installation

| Service | URL Format | Example |
|----------|-------------|----------|
| **API** | `http://<hostname>:<api_port>` | `http://ubuntu4:8080` |
| **Dashboard** | `http://<hostname>:<dashboard_port>` | `http://ubuntu4:13120` |
| **MCP** | `http://<hostname>:<api_port>/mcp` | `http://ubuntu4:8080/mcp` |
| **Health** | `http://<hostname>:<api_port>/health` | `http://ubuntu4:8080/health` |

## What Gets Installed

### Core Components
- ✅ OpenMemory API v1.2.3 (latest)
- ✅ Web Dashboard (visual management)
- ✅ SQLite database with WAL mode
- ✅ Deep tier configuration (enhanced recall)
- ✅ OpenAI embeddings (text-embedding-3-small)
- ✅ MCP server for integration
- ✅ Memory decay system (24-hour cycles)
- ✅ Health monitoring

### Optional Components
- 🔸 OpenCode MCP integration
- 🔸 Backup automation
- 🔸 WAL monitoring
- 🔸 Decay statistics

## Files to Copy

To add this to your freshstart repository, copy these three files:

```bash
# Create INSTALLATION-GUIDES directory
mkdir -p INSTALLATION-GUIDES

# Copy files
cp /media/docs/output/INSTALLATION-GUIDES-README.md INSTALLATION-GUIDES/
cp /media/docs/output/INSTALLATION-GUIDES-openmemory-installation.md INSTALLATION-GUIDES/openmemory-installation.md

# Update setup.md with menu integration
# See setup.md-integration-instructions.md for details
```

## Future Extensibility

This structure makes it easy to add more installation guides in the future:

### Adding a New Guide

1. Create `<service>-installation.md` in INSTALLATION-GUIDES/
2. Update INSTALLATION-GUIDES/README.md with guide details
3. Add to setup.md menu as a new option
4. Test and commit

### Benefits

- Consistent format across all guides
- Centralized location for installation documentation
- Easy to maintain and update
- Scalable for multiple services

## Getting Started

### For New Machine Installation

```bash
# Navigate to freshstart repository
cd /path/to/freshstart

# Give to agent:
agent: Follow INSTALLATION-GUIDES/openmemory-installation.md to install OpenMemory
```

The agent will:
1. Present menu options
2. Ask for configuration preferences
3. Execute installation step-by-step
4. Provide access URLs and documentation

## Summary

This integration provides a complete, user-friendly installation system for OpenMemory that:

- **Guides users** through the installation process
- **Presents options** via question tool
- **Supports choices** (embeddings, integration, automation)
- **Validates installation** with comprehensive testing
- **Provides documentation** for troubleshooting and maintenance
- **Extends easily** for future installation guides

The system is now ready to use in your freshstart repository and can be extended to support additional services as needed.

---

**Related**: [OpenMemory Documentation](https://github.com/caviraoss/openmemory) | [Freshstart Repository](https://github.com/suppg02-sudo/freshstart)