---
pubDatetime: 2026-02-24T10:45:00Z
title: "Homepage Skill Design: Full Automation for gethomepage Dashboard"
postSlug: "homepage-skill-design"
description: "Homepage Skill Design: Full Automation for gethomepage Dashboard"
tags:
  - skills
  - opencode
  - automation
  - dashboard
  - docker
---

# Homepage Skill Design: Full Automation for gethomepage Dashboard

We've just completed the design phase for a comprehensive Homepage skill that will bring full automation to managing gethomepage dashboards. Here's what the skill will deliver.

## Overview

The Homepage skill provides expert guidance for managing gethomepage (https://gethomepage.dev) dashboards running on Docker at `http://ubuntu58-1:8765`. The skill focuses on:

- Setup and configuration from scratch
- Icon management with automated utilities
- Full automation for service configuration
- Backup and restore capabilities
- Docker integration for service discovery

## Architecture

The skill follows a modular structure with clear separation between documentation and automation utilities:

```
homepage skill directory:
├── SKILL.md                 # Complete documentation
├── scripts/                 # Automation utilities
│   ├── download-icons.sh    # Download icons from URLs
│   ├── organize-icons.sh     # Auto-organize existing icons
│   ├── backup-homepage.sh   # Backup all configuration
│   ├── restore-homepage.sh  # Restore from backup
│   ├── discover-services.sh  # Docker auto-discovery
│   ├── add-service.sh      # Quick service addition
│   └── validate-config.sh  # YAML syntax validation
├── templates/               # YAML templates
│   ├── service-template.yaml
│   ├── widget-template.yaml
│   ├── settings-template.yaml
│   └── bookmarks-template.yaml
└── examples/                # Working examples
    ├── services-full.yaml
    └── widgets-full.yaml
```

## Key Features

### 1. Icon Management Utilities

**download-icons.sh**: Automatically downloads icons from URLs and places them in the correct directory with proper validation and format detection.

**organize-icons.sh**: Auto-organizes existing icon files by category/type, creating subdirectories and standardizing filenames.

### 2. Service Configuration Automation

**discover-services.sh**: Scans running Docker containers and suggests service definitions for `services.yaml`, detecting ports, labels, and generating proper YAML structure.

**add-service.sh**: Quick service addition with validation, port checking, and automatic homepage container restart.

### 3. Backup and Restore

**backup-homepage.sh**: Comprehensive backup capturing:
- All YAML configuration files
- Icon files and directory structure
- Docker compose configuration
- Custom CSS and JS files
- Logs (optional)
- Backup metadata with checksums

**restore-homepage.sh**: Restore process with:
- Backup integrity validation
- Pre-restore rollback capability
- YAML syntax verification
- Automatic container restart

### 4. Configuration Templates

Pre-built templates prevent YAML errors:
- `service-template.yaml`: Service definitions with all optional fields
- `widget-template.yaml`: Common widget types
- `settings-template.yaml`: Homepage configuration options
- `bookmarks-template.yaml`: Bookmark structures

### 5. Validation Utilities

**validate-config.sh**: Checks:
- YAML syntax errors
- Service URL format
- Icon file existence
- Ping endpoint accessibility
- Duplicate service names
- Required fields presence

## Current Homepage State

**Container**: homepage (ghcr.io/gethomepage/homepage:latest)
**Port**: 8765
**Web Interface**: http://ubuntu58-1:8765
**Current Services**: 27 across 7 categories:
- Critical Infrastructure (7 services)
- Web Applications (8 services)
- AI/ML Services (2 services)
- Monitoring Stack (5 services)
- Utilities (2 services)
- Media Services (1 service)
- Development (2 services)

## Implementation Phases

### Phase 1: Core Documentation
Complete SKILL.md with all sections, basic templates, and current status documentation.

### Phase 2: Icon Utilities
Implement download-icons.sh and organize-icons.sh with full error handling and documentation.

### Phase 3: Service Automation
Create discover-services.sh and add-service.sh with Docker integration and YAML generation.

### Phase 4: Backup/Restore
Build backup-homepage.sh and restore-homepage.sh with comprehensive capture and rollback capabilities.

### Phase 5: Polish
Complete examples, advanced templates, and error handling improvements.

## Why This Matters

Currently, managing homepage requires:
- Manual YAML editing
- Searching for icons online
- Remembering port numbers
- Manual backups
- No service discovery automation

The new Homepage skill will:
- Automate service addition via Docker discovery
- Download and organize icons automatically
- Provide one-command backup/restore
- Validate configurations before applying
- Prevent YAML errors with templates

## Success Criteria

The skill will be complete when:
- Users can add services with minimal manual editing
- Icons can be downloaded and organized automatically
- Configuration can be backed up and restored reliably
- Docker containers can be auto-discovered as services
- All utilities work independently or from skill context
- Error handling prevents data loss
- Backups validate before restore

## Next Steps

The design document has been saved to `/media/docs/plans/2026-02-24-homepage-skill-design.md`. The next step is to invoke the `writing-plans` skill to create a detailed implementation plan with specific tasks and dependencies.

## Key Questions for Implementation

1. Should `discover-services.sh` automatically add services or just suggest them?
2. What backup retention policy? (Currently: last 10 backups)
3. Should `backup-homepage.sh` include logs by default?
4. Icon format preferences? (PNG vs SVG vs both)
5. Should we support environment variable configuration for backup paths?

---

**Design Status**: Complete and ready for implementation planning
**Document Location**: `/media/docs/plans/2026-02-24-homepage-skill-design.md`
**Current Homepage**: http://ubuntu58-1:8765 (27 services, 7 categories)