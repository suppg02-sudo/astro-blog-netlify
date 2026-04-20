---
pubDatetime: 2026-02-25T12:00:00Z
title: "Integrating OliveTin with OpenCode Skills: A Progressive Implementation Guide"
postSlug: "integrating-olivetin-opencode-skills"
description: "Integrating OliveTin with OpenCode Skills: A Progressive Implementation Guide"
tags:
  - skills
  - opencode
  - integration
  - automation
  - olivetin
---

# Introduction

OliveTin is a powerful web-based button interface that enables graphical server management 
without writing complex dashboards. When combined with OpenCode's extensive skill ecosystem, 
it provides an intuitive way to interact with automated workflows, skill menus, and system 
operations through simple button clicks.

This guide presents a phased approach to integrating OliveTin with OpenCode skills, starting from simple push/pull operations and progressively building toward advanced automation capabilities.

## Why OliveTin + OpenCode Skills?

OpenCode provides a rich ecosystem of skills for everything from server maintenance (`space`, `maintenance`) to documentation (`hugo`, `news`) and container management (`containers`). However, these skills typically require command-line execution or agent interaction. OliveTin bridges this gap by:

- **Graphical Access**: One-click execution of skill operations
- **Safety**: Pre-validated commands with built-in confirmations
- **Accessibility**: Server management without SSH access
- **Organization**: Logical grouping of related skills and operations
- **Integration**: Seamless connection with existing dashboard infrastructure

## Architecture Overview

{{< mermaid >}}
graph TD
    subgraph OliveTin_Interface
        A[Web Dashboard]
        B[Button Groups]
        C[Action Triggers]
    end

    subgraph OpenCode_Skills_Ecosystem
        D[Infrastructure Skills]
        E[Documentation Skills]
        F[Automation Skills]
        G[Utility Skills]
    end

    subgraph Backend_Execution
        H[Docker Containers]
        I[Shell Scripts]
        J[API Endpoints]
        K[Git Operations]
    end

    A --> B
    B --> C
    C --> D
    C --> E
    C --> F
    C --> G
    D --> H
    E --> I
    F --> J
    G --> K
{{< /mermaid >}}

---

# Phase 1: Simple Button Operations (Foundation)

## Objective

Build trust and familiarity with OliveTin by implementing basic Git repository synchronization operations for the homepage skill.

## Implementation

### OliveTin Container Setup

```yaml
# docker-compose.yml
version: '3.8'
services:
  olivetin:
    image: jamesread/olivetin
    container_name: olivetin
    ports:
      - "1337:1337"
    volumes:
      - /media/docker/olivetin/config:/config
      - /root/.opencode/skill:/opencode-skills:ro
      - /media/docker:/media-docker:ro
    restart: unless-stopped
```

### Basic Configuration File

```yaml
# /media/docker/olivetin/config/config.yaml
actions:
  - title: "Push Homepage Skill to Freshstart"
    icon: "upload-cloud"
    shell: cd /media/docker && git -C /root/.opencode/skill/homepage push origin main
    timeout: 30

  - title: "Pull Homepage Skill from Freshstart"
    icon: "download-cloud"
    shell: cd /media/docker && git -C /root/.opencode/skill/homepage pull origin main
    timeout: 30

  - title: "Homepage Skill Status"
    icon: "info"
    shell: git -C /root/.opencode/skill/homepage status --short
    timeout: 5
    popupOnStart: true
```

### Benefits

- **Instant Feedback**: Immediate execution of common Git operations
- **Safety Confirmation**: OliveTin's built-in confirmation dialogs
- **Visual Status**: Clear indication of operation success/failure
- **Audit Trail**: All button presses logged for accountability

## Advanced Phase 1: Multiple Skills

Expand to include other frequently updated skills:

```yaml
  - title: "Push All Skills to Freshstart"
    icon: "upload-cloud"
    shell: |
      cd /media/docker
      for skill in homepage hugo containers space maintenance; do
        git -C /root/.opencode/skill/$skill push origin main
      done
    timeout: 60

  - title: "Update Homepage Skill from Freshstart"
    icon: "refresh-cw"
    shell: |
      cd /media/docker
      git -C /root/.opencode/skill/homepage pull origin main
      systemctl restart homepage  # Restart service after update
    timeout: 60
```

---

# Phase 2: Skill Menu Integration

## Objective

Provide one-click access to commonly used skill operations, organize skills by category, and display skill status.

## Implementation

### Categorized Button Groups

```yaml
groups:
  - title: "Infrastructure"
    color: "#3b82f6"
    actions:
      - Push Homepage Skill
      - Pull Homepage Skill
      - Homepage Skill Status
      - Restart Homepage Service

  - title: "System Maintenance"
    color: "#ef4444"
    actions:
      - Run Space Analysis
      - Clean Docker Cache
      - System Health Check

  - title: "Documentation"
    color: "#10b981"
    actions:
      - Create Blog Post
      - Hugo Build Preview
      - View Hugo Logs

  - title: "Utilities"
    color: "#f59e0b"
    actions:
      - Git Status
      - View Container Logs
      - Check Disk Usage
```

### Skill Status Display

```yaml
  - title: "Skills Health Check"
    icon: "activity"
    shell: |
      echo "=== Skill Status ==="
      for skill_dir in /root/.opencode/skill/*/; do
        skill=$(basename "$skill_dir")
        if [ -f "$skill_dir/SKILL.md" ]; then
          echo "✓ $skill: Available"
        else
          echo "✗ $skill: Missing SKILL.md"
        fi
      done
    timeout: 10
    popupOnStart: true
```

### Quick Documentation Access

```yaml
  - title: "View Homepage Skill Documentation"
    icon: "file-text"
    exec: "/usr/bin/xdg-open"
    arguments: "http://ubuntu58-1:3001/editor/root/.opencode/skill/homepage/SKILL.md"

  - title: "Open GitHub Repository"
    icon: "github"
    exec: "/usr/bin/xdg-open"
    arguments: "https://github.com/suppg02-sudo/freshstart"
```

## Benefits

- **Logical Organization**: Skills grouped by function
- **Quick Reference**: One-click access to documentation
- **Status Monitoring**: Real-time skill health checks
- **Reduced Complexity**: Users don't need to remember command syntax

---

# Phase 3: Multi-Step Workflows

## Objective

Create button sequences that execute complex operations involving multiple steps, with pre-flight checks and progress tracking.

## Implementation

### Sequential Workflow: Update System

```yaml
  - title: "Complete System Update"
    icon: "zap"
    shell: |
      set -e  # Exit on error

      echo "=== Phase 1: Update OPENSOURCE ==="
      cd /media/docker/OPENSOURCE
      git pull origin main

      echo "=== Phase 2: Update OPENSOURCE-LITE ==="
      cd /media/docker/OPENSOURCE-LITE
      git pull origin main

      echo "=== Phase 3: Update Homepage Skill ==="
      cd /media/docker
      git -C /root/.opencode/skill/homepage pull origin main

      echo "=== Phase 4: Restart Homepage Service ==="
      systemctl restart homepage
      sleep 3

      echo "=== Phase 5: Verify Status ==="
      systemctl is-active homepage

      echo "=== Update Complete ==="
    timeout: 120
    confirmation:
      title: "System Update"
      text: "This will update OPENSOURCE, OPENSOURCE-LITE, and Homepage skill. Continue?"
```

### Multi-Button Workflow with Dependencies

```yaml
  - title: "Skill Deployment Workflow"
    icon: "workflow"
    iconColor: "#8b5cf6"
    actions:
      - Pull Latest Changes
      - Update Dependencies
      - Run Tests
      - Deploy to Production
      - Verify Deployment

  - title: "Pull Latest Changes"
    icon: "download"
    shell: |
      cd /media/docker
      git -C /root/.opencode/skill/$SKILL_NAME pull origin main
    timeout: 30

  - title: "Update Dependencies"
    icon: "package"
    shell: |
      cd /media/docker/$PROJECT_DIR
      npm install 2>/dev/null || pip install -r requirements.txt 2>/dev/null || echo "No dependencies"
    timeout: 60

  - title: "Run Tests"
    icon: "test"
    shell: |
      cd /media/docker/$PROJECT_DIR
      make test 2>/dev/null || npm test 2>/dev/null || pytest 2>/dev/null || echo "No tests"
    timeout: 120

  - title: "Deploy to Production"
    icon: "rocket"
    shell: |
      cd /media/docker/$PROJECT_DIR
      docker-compose down
      docker-compose pull
      docker-compose up -d
    timeout: 180
    confirmation:
      title: "Deploy to Production"
      text: "This will restart the service. Confirm deployment?"

  - title: "Verify Deployment"
    icon: "check-circle"
    shell: |
      sleep 5
      curl -f http://ubuntu58-1:$PORT/health || exit 1
      echo "Deployment successful!"
    timeout: 30
```

### Conditional Execution

```yaml
  - title: "Smart Update"
    icon: "refresh-cw"
    shell: |
      # Check if updates are available
      cd /media/docker
      if git -C /root/.opencode/skill/homepage fetch --dry-run 2>&1 | grep -q updates; then
        echo "Updates available, pulling..."
        git -C /root/.opencode/skill/homepage pull origin main
        systemctl restart homepage
      else
        echo "No updates available"
      fi
    timeout: 30
```

## Benefits

- **Error Handling**: Automatic rollback on failure
- **Progress Tracking**: Clear feedback on each step
- **Safety Nets**: Confirmation dialogs for destructive operations
- **Efficiency**: Automated multi-step processes

---

# Phase 4: Contextual Dashboard

## Objective

Create dynamic button groups based on current project context, show project-specific skills, and integrate with existing dashboard infrastructure.

## Implementation

### Dynamic Project Detection

```yaml
  - title: "Current Project: {{CURRENT_PROJECT}}"
    icon: "folder"
    shell: |
      # Detect project from current directory or environment
      cd /media/docker
      PROJECT=$(basename $(pwd))
      echo "Current Project: $PROJECT"
      echo "Skills Available:"
      ls -1 /root/.opencode/skill/ | grep -E "(hugo|containers|space|maintenance)" || echo "No project-specific skills"
    timeout: 10
```

### Project-Specific Skill Loading

```yaml
  - title: "Load Hugo Project Skills"
    icon: "book"
    shell: |
      cd /media/docker/website
      echo "=== Hugo Project Skills Loaded ==="
      echo "• Blog Post Management"
      echo "• Content Preview"
      echo "• Theme Customization"
      echo "• SEO Optimization"
    timeout: 5

  - title: "Load Container Skills"
    icon: "box"
    shell: |
      echo "=== Container Management Skills ==="
      docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
    timeout: 10
```

### Integration with Existing Dashboard

```yaml
  - title: "Open Portainer"
    icon: "server"
    exec: "/usr/bin/xdg-open"
    arguments: "https://ubuntu58-1:9443"

  - title: "Open Homepage Dashboard"
    icon: "layout"
    exec: "/usr/bin/xdg-open"
    arguments: "http://ubuntu58-1:8765"

  - title: "Open OpenMemory"
    icon: "database"
    exec: "/usr/bin/xdg-open"
    arguments: "http://ubuntu58-1:8080"
```

### Environment-Specific Actions

```yaml
  - title: "Development Actions"
    icon: "code"
    shell: |
      if [ "$ENVIRONMENT" = "development" ]; then
        echo "=== Development Environment ==="
        echo "• Enable debug logging"
        echo "• Auto-reload enabled"
        echo "• Hot reload active"
      else
        echo "Production environment - no debug actions"
      fi
    timeout: 5

  - title: "Production Actions"
    icon: "shield"
    shell: |
      if [ "$ENVIRONMENT" = "production" ]; then
        echo "=== Production Environment ==="
        echo "• Health checks enabled"
        echo "• Monitoring active"
        echo "• Backup scheduled"
      else
        echo "Development environment - no production actions"
      fi
    timeout: 5
```

## Benefits

- **Context Awareness**: Actions adapt to current project/environment
- **Unified Interface**: Single dashboard for all management needs
- **Reduced Complexity**: Relevant actions shown based on context
- **Better UX**: Cleaner interface without irrelevant buttons

---

# Phase 5: Advanced Automation

## Objective

Implement scheduled triggers, conditional visibility based on system state, error handling with rollback, user roles, and API access for programmatic execution.

## Scheduled Triggers (Cron Integration)

```yaml
  - title: "Schedule Daily Backup"
    icon: "clock"
    shell: |
      # Add cron job for daily backup
      (crontab -l 2>/dev/null; echo "0 2 * * * /root/scripts/backup-docker-volumes.sh") | crontab -
      echo "Daily backup scheduled for 2:00 AM"
    timeout: 10

  - title: "Run Backup Now"
    icon: "database"
    shell: /root/scripts/backup-docker-volumes.sh
    timeout: 300

  - title: "Schedule Weekly Space Check"
    icon: "disk"
    shell: |
      # Add cron job for weekly space check
      (crontab -l 2>/dev/null; echo "0 3 * * 0 /root/.opencode/skill/space/scripts/analyze-disk-space.sh") | crontab -
      echo "Weekly space check scheduled for Sunday 3:00 AM"
    timeout: 10
```

### Conditional Button Visibility

```yaml
  - title: "Clean Old Logs (Logs > 100MB)"
    icon: "trash-2"
    shell: |
      LOG_SIZE=$(du -sh /var/log/journal 2>/dev/null | cut -f1)
      if [ "$LOG_SIZE" != "" ]; then
        echo "Current log size: $LOG_SIZE"
        journalctl --vacuum-size=100M
        echo "Logs cleaned to 100MB limit"
      else
        echo "No logs to clean"
      fi
    timeout: 30
    condition: |
      # Only show if logs > 100MB
      [ $(du -m /var/log/journal 2>/dev/null | cut -f1) -gt 100 ]

  - title: "Restart Hung Containers"
    icon: "refresh-cw"
    shell: |
      # Restart containers not responding to health checks
      for container in $(docker ps --filter "health=unhealthy" --format "{{.Names}}"); do
        echo "Restarting unhealthy container: $container"
        docker restart "$container"
      done
    timeout: 60
    condition: |
      # Only show if unhealthy containers exist
      [ $(docker ps --filter "health=unhealthy" --format "{{.Names}}" | wc -l) -gt 0 ]
```

### Error Handling with Rollback

```yaml
  - title: "Safe Service Update"
    icon: "shield"
    shell: |
      #!/bin/bash
      set -e

      SERVICE_NAME="homepage"
      BACKUP_DIR="/tmp/backup-$(date +%Y%m%d-%H%M%S)"

      echo "=== Step 1: Create Backup ==="
      mkdir -p "$BACKUP_DIR"
      cp -r /root/.opencode/skill/homepage "$BACKUP_DIR/"

      echo "=== Step 2: Update Service ==="
      cd /media/docker
      git -C /root/.opencode/skill/homepage pull origin main

      echo "=== Step 3: Test Service ==="
      systemctl restart $SERVICE_NAME
      sleep 5

      if systemctl is-active --quiet $SERVICE_NAME; then
        echo "=== Step 4: Update Successful ==="
        rm -rf "$BACKUP_DIR"
        echo "Backup removed, update completed successfully"
      else
        echo "=== Step 5: Rollback Triggered ==="
        systemctl stop $SERVICE_NAME
        rm -rf /root/.opencode/skill/homepage
        cp -r "$BACKUP_DIR/homepage" /root/.opencode/skill/
        systemctl start $SERVICE_NAME
        echo "Rollback completed, previous version restored"
        exit 1
      fi
    timeout: 120
    confirmation:
      title: "Safe Service Update"
      text: "This will create a backup, update the service, and automatically rollback if tests fail. Continue?"
```

### User Roles and Permissions

```yaml
  - title: "Admin: System Configuration"
    icon: "settings"
    shell: nano /etc/systemd/system/homepage.service
    timeout: 300
    allowedRoles: ["admin"]
    confirmation:
      title: "Admin Action Required"
      text: "This action requires admin privileges. Are you sure?"

  - title: "User: View Logs"
    icon: "file-text"
    shell: journalctl -u homepage -n 50 --no-pager
    timeout: 10
    allowedRoles: ["admin", "user", "readonly"]

  - title: "View Only: Container Status"
    icon: "box"
    shell: docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
    timeout: 10
    allowedRoles: ["admin", "user", "readonly"]
```

### API Access for Programmatic Execution

OliveTin provides a REST API for programmatic access:

```bash
# Execute action via API
curl -X POST http://ubuntu58-1:1337/api/actions/Push\ Homepage\ Skill

# Get action status
curl http://ubuntu58-1:1337/api/status

# List all available actions
curl http://ubuntu58-1:1337/api/actions
```

Example: Create button from AI agent

```python
import requests

def execute_olivetin_action(action_name):
    """Execute OliveTin action from Python script"""
    url = "http://ubuntu58-1:1337/api/actions/" + action_name.replace(" ", "\\ ")
    response = requests.post(url)
    return response.json()

# Usage
result = execute_olivetin_action("Push Homepage Skill")
if result["status"] == "success":
    print("Action executed successfully")
```

## Benefits

- **Automation**: Scheduled tasks without manual intervention
- **Smart Visibility**: Only show relevant buttons based on system state
- **Safety**: Automatic rollback on failure
- **Security**: Role-based access control
- **Integration**: Programmatic access from other tools and AI agents

---

# Implementation Roadmap

{{< mermaid >}}
gantt
    title OliveTin + OpenCode Integration Timeline
    dateFormat  YYYY-MM-DD
    section Phase 1
    Container Setup           :done,    p1a, 2026-02-25, 1d
    Basic Git Buttons         :active,   p1b, 2026-02-26, 2d
    section Phase 2
    Skill Categories         :          p2a, after p1b, 3d
    Status Displays         :          p2b, after p1b, 2d
    section Phase 3
    Sequential Workflows    :          p3a, after p2a, 4d
    Conditional Logic      :          p3b, after p2a, 3d
    section Phase 4
    Dynamic Dashboard      :          p4a, after p3a, 5d
    Project Integration    :          p4b, after p3a, 4d
    section Phase 5
    Scheduled Triggers   :          p5a, after p4a, 3d
    Advanced Automation   :          p5b, after p4a, 5d
{{< /mermaid >}}

---

# Best Practices

## Configuration Management

1. **Version Control**: Store OliveTin configuration in Git repository
2. **Backup**: Keep backups of working configurations
3. **Testing**: Test new buttons in development environment first
4. **Documentation**: Document each button's purpose and expected behavior

## Security Considerations

1. **Authentication**: Enable OliveTin authentication in production
2. **Permissions**: Use role-based access control for sensitive operations
3. **Audit Trail**: Enable logging for compliance and troubleshooting
4. **HTTPS**: Use reverse proxy with HTTPS for remote access

## Performance Optimization

1. **Timeout Values**: Set appropriate timeout values for long-running operations
2. **Parallel Execution**: Use independent actions that can run in parallel
3. **Caching**: Cache frequently accessed information (skill status, container lists)
4. **Resource Limits**: Monitor CPU and memory usage of long-running operations

## User Experience

1. **Clear Labels**: Use descriptive button titles and icons
2. **Confirmation**: Add confirmation dialogs for destructive operations
3. **Feedback**: Show progress and completion status
4. **Error Messages**: Provide helpful error messages with resolution steps

---

# Troubleshooting

## Common Issues

### Button Not Executing

**Problem**: Clicking button shows no response

**Solutions**:
- Check OliveTin container is running: `docker ps | grep olivetin`
- Verify configuration syntax: `docker logs olivetin`
- Check shell script permissions: Ensure scripts are executable

### Action Timeout

**Problem**: Button execution times out

**Solutions**:
- Increase timeout value in configuration
- Check if operation requires interactive input
- Review logs for specific error messages

### Permission Denied

**Problem**: "Permission denied" error in action output

**Solutions**:
- Ensure container has correct volume mounts
- Check file permissions on mounted volumes
- Use `sudo` inside shell commands if needed

### Git Operation Fails

**Problem**: Git push/pull operations fail

**Solutions**:
- Verify SSH keys are configured: `ssh -T git@github.com`
- Check network connectivity
- Ensure repository URL is correct

---

# Next Steps and Recommendations

## Immediate Actions (Phase 1)

1. Deploy OliveTin container using provided docker-compose.yml
2. Create basic push/pull buttons for homepage skill
3. Test Git operations through web interface
4. Document successful operations

## Short-term Goals (Phase 2-3)

1. Categorize skills by function (Infrastructure, Documentation, Utilities)
2. Implement multi-step workflows for common tasks
3. Add pre-flight checks and confirmation dialogs
4. Create documentation for each button group

## Long-term Vision (Phase 4-5)

1. Integrate with existing dashboard infrastructure (Homepage, Portainer)
2. Implement scheduled maintenance tasks
3. Add role-based access control
4. Create API integrations with other tools (CI/CD, monitoring)
5. Build custom dashboards for specific projects

## Future Enhancements

1. **AI-Powered Suggestions**: Recommend actions based on system state
2. **Historical Analytics**: Track button usage patterns and optimize workflows
3. **Mobile Integration**: Responsive design for mobile devices
4. **Custom Themes**: Branding and customization options
5. **Multi-Server Support**: Manage multiple servers from single dashboard

---

# Conclusion

Integrating OliveTin with OpenCode skills provides a powerful, intuitive interface for server management and automation. By following this phased approach, you can start with simple operations and progressively build toward advanced automation capabilities.

The key benefits include:

- **Reduced Complexity**: One-click execution of complex operations
- **Improved Accessibility**: Graphical interface for non-technical users
- **Enhanced Safety**: Built-in confirmations and rollback mechanisms
- **Better Organization**: Logical grouping of related operations
- **Integration**: Seamless connection with existing infrastructure

Whether you're managing a single server or multiple environments, OliveTin + OpenCode skills combination provides the flexibility and power needed for modern server management.

---

## Additional Resources

- [OliveTin Documentation](https://olivetin.app/)
- [OliveTin GitHub Repository](https://github.com/OliveTin/OliveTin)
- [OpenCode Skills Directory](http://ubuntu58-1:3001/editor/root/.opencode/skill/)
- [Homepage Dashboard](http://ubuntu58-1:8765)
- [Portainer Container Management](https://ubuntu58-1:9443)

## Support and Feedback

For issues, questions, or suggestions regarding this integration guide:

1. Check OliveTin logs: `docker logs olivetin`
2. Review OpenCode skill documentation
3. Test shell commands manually before adding to OliveTin
4. Enable OliveTin debug mode for troubleshooting
5. Submit feedback to project maintainers

---

*Last Updated: February 25, 2026*
*Author: OpenCode Integration Team*