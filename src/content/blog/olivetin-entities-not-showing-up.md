---
pubDatetime: 2026-02-28T13:15:00Z
title: "Olivetin Entities Not Showing Up - Root Cause and Solution"
postSlug: "olivetin-entities-not-showing-up"
description: "Olivetin Entities Not Showing Up - Root Cause and Solution"
tags:
  - configuration
  - docker
  - troubleshooting
  - olivetin
---

## Investigation Summary

While working with my Olivetin installation, I noticed that **entities weren't showing up in the web interface**. After a thorough investigation, I discovered the root cause and documented the solution for anyone experiencing the same issue.

## What Are Entities in Olivetin?

Entities are **dynamic objects** - things that exist and can change over time. Unlike static actions (buttons that never change), entities represent:

- **Docker containers** (start, stop, restart each one dynamically)
- **Virtual machines** (power on/off, wake-on-LAN)
- **Servers** (hostname, IP address, control commands)
- **Systemd services** (start, stop, restart services)

### Key Entity Concepts

1. **Entity Files**: Entities are loaded from JSON or YAML files on disk
   - OliveTin watches these files for updates
   - Each entity has properties (e.g., `container.name`, `container.status`, `container.image`)

2. **Dynamic Actions**: Actions can reference entity variables to generate buttons for each entity
   ```yaml
   # This action would be generated for EACH container entity
   - title: 'Restart {{ container.name }}'
     shell: docker restart {{ container.name }}
   ```

3. **Dashboards Required**: Entities only appear in **dashboards**, not on the main action list
   - Entity actions cannot be used on the default view
   - You must create a dashboard with an `entity:` property

4. **Entity Configuration Structure**:

   ```yaml
   # In config.yaml - define entities
   entities:
     - file: /config/containers.json
       name: container

   # In config.yaml - create dashboard for entities
   dashboards:
     - title: "Container Control"
       contents:
         - type: fieldset
           entity: container
           title: 'Container: {{ container.name }}'
           contents:
             - type: display
               title: |
                 Status: {{ container.status }}
                 Image: {{ container.image }}
             - title: 'Restart {{ container.name }}'
   ```

   ```json
   # In /config/containers.json - define entity data
   [
     {"name": "homepage", "status": "running", "image": "ghcr.io/gethomepage/homepage"},
     {"name": "grafana", "status": "running", "image": "grafana/grafana"},
     {"name": "portainer", "status": "running", "image": "portainer/portainer-ce"}
   ]
   ```

## Root Cause: Entities Not Configured

After investigating my Olivetin installation at `/media/docker/olivetin/`, I found:

### Current Configuration State

**What I Had:**
- ✅ `actions:` section with 8 static buttons
- ✅ Docker socket mounted (read-only)
- ✅ Container running on port 1337

**What Was Missing:**
- ❌ **NO `entities:` section** in `config.yaml`
- ❌ **NO `dashboards:` section** in `config.yaml`
- ❌ **NO entity files** in `/media/docker/olivetin/config/` directory
- ❌ No way to dynamically generate actions from container lists

### My Current config.yaml

```yaml
# OliveTin Configuration
listenAddressSingleHTTPFrontend: 0.0.0.0:1337
logLevel: "INFO"

# Actions (buttons) to show up on WebUI
actions:
  # Container management
  - title: Restart Homepage
    icon: restart
    shell: docker restart homepage
    id: restartHomepage
    description: Restart Homepage dashboard

  - title: Restart FileBrowser
    icon: restart
    shell: docker restart filebrowser
    id: restartFileBrowser
    description: Restart FileBrowser service

  # ... more static actions ...
```

### The Problem

I had **44+ running containers** that could be controlled as entities, but:
- No entity file listing these containers
- No dashboard to display them
- Only static actions for specific containers (Restart Homepage, Restart FileBrowser)

This is why entities weren't showing up - **they simply weren't configured**.

## Solution: Configure Entities in Olivetin

To enable entities and have them show up in the Olivetin web interface, you need to complete these steps:

### Step 1: Create an Entity File

Create `/media/docker/olivetin/config/containers.json` with your container data:

```json
[
  {
    "name": "homepage",
    "status": "running",
    "image": "ghcr.io/gethomepage/homepage",
    "ports": "3000:3000"
  },
  {
    "name": "grafana",
    "status": "running",
    "image": "grafana/grafana",
    "ports": "3001:3000"
  },
  {
    "name": "portainer",
    "status": "running",
    "image": "portainer/portainer-ce",
    "ports": "9000:9443"
  }
]
```

**Tip**: You can generate this file automatically from your running containers:

```bash
docker ps --format '{"name":"{{.Names}}","status":"{{.Status}}","image":"{{.Image}}"}' \
  | jq -s '.' > /media/docker/olivetin/config/containers.json
```

### Step 2: Add Entities Section to config.yaml

Add the `entities:` section to your configuration:

```yaml
# OliveTin Configuration
listenAddressSingleHTTPFrontend: 0.0.0.0:1337
logLevel: "INFO"

# Define entities
entities:
  - file: /config/containers.json
    name: container

# Actions (buttons) to show up on WebUI
actions:
  # Existing static actions...
```

### Step 3: Add Dashboard Section

Create a dashboard that references the entities:

```yaml
# OliveTin Configuration
# ... previous sections ...

# Define dashboards with entity support
dashboards:
  - title: "Container Control"
    contents:
      - type: fieldset
        entity: container
        title: 'Container: {{ container.name }}'
        contents:
          # Display container information
          - type: display
            title: |
              Status: <strong>{{ container.status }}</strong><br/>
              Image: <strong>{{ container.image }}</strong><br/>
              Ports: <strong>{{ container.ports }}</strong>

          # Dynamic actions for each container
          - title: 'Restart {{ container.name }}'
            icon: restart
            shell: docker restart {{ container.name }}
            id: restartContainer

          - title: 'Stop {{ container.name }}'
            icon: stop
            shell: docker stop {{ container.name }}
            id: stopContainer

          - title: 'Start {{ container.name }}'
            icon: play
            shell: docker start {{ container.name }}
            id: startContainer
```

### Step 4: Restart Olivetin

Apply the configuration changes:

```bash
cd /media/docker/olivetin
docker-compose restart olivetin
```

Or if running with Docker:

```bash
docker restart olivetin
```

### Step 5: Verify Entities Appear

1. Navigate to `http://ubhost:1337`
2. Click on **Dashboards** in the navigation
3. You should see a **"Container Control"** dashboard
4. Each container from your `containers.json` file will appear as a separate panel
5. Each container panel has:
   - Display information (status, image, ports)
   - Restart, Stop, Start buttons (one per container)

## Common Troubleshooting

### Entities Still Not Showing

1. **Check entity file path**: Ensure `/config/containers.json` is mounted correctly
   ```bash
   docker exec olivetin ls -la /config/
   docker exec olivetin cat /config/containers.json
   ```

2. **Verify config syntax**: Check for YAML indentation errors
   ```bash
   docker logs olivetin | grep -i error
   ```

3. **Confirm dashboard section**: Entities require a dashboard - they won't appear on the default action list
   ```bash
   curl -s http://localhost:1337/api/DumpActionMap | jq .
   ```

4. **Check file permissions**: Ensure Olivetin can read the entity file
   ```bash
   ls -la /media/docker/olivetin/config/containers.json
   ```

### Entity File Not Updating

OliveTin watches entity files for changes, but the web interface may need a manual refresh to see updates. This is expected behavior.

To debug entity loading:

```yaml
# Enable debugging in config.yaml (for troubleshooting only)
logLevel: "DEBUG"
InsecureAllowDumpVars: true
```

Then visit:
- `http://ubhost:1337/api/DumpVars` - See all entity variables
- `http://ubhost:1337/api/DumpActionMap` - See all generated actions

## Key Takeaways

1. **Entities are not automatic** - you must configure them explicitly
2. **Entity files** contain the data (JSON/YAML format)
3. **Entities section** in `config.yaml` defines which files to load
4. **Dashboards section** is required to display entities in the UI
5. **Entity actions** are generated dynamically based on entity properties
6. **Static actions** (regular buttons) work without entities, but can't scale

## Resources

- [OliveTin Entities Documentation](https://docs.olivetin.app/entities/intro.html)
- [Container Control Panel Example](https://docs.olivetin.app/solutions/container-control-panel/index.html)
- [OliveTin GitHub Repository](https://github.com/OliveTin/OliveTin)

## My Next Steps

With entities properly configured, I'll now be able to:
- Dynamically control all 44+ containers from a single dashboard
- Generate start/stop/restart actions for each container automatically
- Scale my container management without hardcoding each container
- Add new containers to `containers.json` and have them appear automatically

---

**Note**: This investigation was conducted on a server running Olivetin v3000.10.0 in a Docker container configuration.