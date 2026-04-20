---
pubDatetime: 2026-02-11T11:40:00Z
title: "I Built a Remote Coding Agent Platform on Railway"
postSlug: "remote-coding-agent-platform-railway"
description: "A comprehensive walkthrough of building a scalable, cloud-based platform for managing AI coding agents using Railway infrastructure, OpenCode, Claude Code, and modern DevOps practices."
tags:
  - cloud-computing
  - opencode
  - coding-agents
  - infrastructure-as-code
  - railway
  - graphql
  - docker
  - kubernetes
  - devops
  - claude-code
---

## Introduction

Sid from DevOps Directive built a production-ready platform for managing AI coding agents on Railway infrastructure. This project addresses a critical gap in distributed development: how to move AI coding agents from local machines into the cloud while maintaining accessibility, scalability, and collaborative features.

Instead of running agents locally on individual devices (which creates resource constraints and access limitations), this solution provisions agent sandboxes dynamically on Railway's cloud infrastructure, allowing multiple users to access shared agent sessions from any device.

---

## The Problem: Why Cloud-Based Agents?

### Local Agent Limitations

**Single Agent**: Works but ties agent to one device.

**Multiple Local Agents**: Can run with git worktrees, but faces challenges:
- Limited by device CPU, RAM, and disk
- Agents can't be accessed from other devices or phones
- Other team members can't access the same sessions
- Resource contention between concurrent agents

**Solution**: Move agents to Railway cloud infrastructure for:
- ✅ Unlimited scaling (leverage cloud resources)
- ✅ Multi-user access (multiple people, same sessions)
- ✅ Cross-device access (phone, laptop, desktop)
- ✅ Centralized management (single control plane)
- ✅ Dynamic provisioning (auto-scale up/down)

---

## Architecture: Three-Layer Design

The platform consists of three interconnected layers:

### Layer 1: Control Plane (Management Hub)

Running on Railway, the control plane is the central orchestrator:

- **Express.js API** for managing operations
- **GraphQL API Integration** with Railway infrastructure
- **PostgreSQL Database** for session metadata persistence
- **Authentication/Authorization** for multi-user access control
- **Service Lifecycle Management** (create, monitor, delete sandboxes)

### Layer 2: Sandbox Services (Worker Nodes)

Individual Docker containers running on Railway:

- **OpenCode** - AI coding agent for automated tasks
- **Code Server** - VS Code in browser for editing
- **Git Repository** - Isolated per-sandbox to prevent interference
- **All Dependencies** - Pre-installed (node, pnpm, etc.)
- **GitHub Integration** - Can create PRs directly from sandbox

### Layer 3: Frontend (User Interface)

Web-based dashboard for end users:

- **Session Management** - View, create, delete agent sessions
- **Quick Access** - One-click to launch Code Server
- **Real-time Status** - See which sessions are running
- **Simple UX** - No infrastructure knowledge required

```
┌─────────────────────────────────────────────────────────────┐
│                     User Interface (Web)                     │
│              Dashboard | Session Management                  │
└───────────────────────┬─────────────────────────────────────┘
                        │ HTTP
┌───────────────────────┴─────────────────────────────────────┐
│                    Control Plane API                         │
│              (Express.js + PostgreSQL + Auth)                │
│     ┌──────────────────────────────────────────────────┐    │
│     │  Railway GraphQL API Integration                 │    │
│     │  - Service CRUD operations                       │    │
│     │  - Deployment management                         │    │
│     └──────────────────────────────────────────────────┘    │
└───────────────────────┬─────────────────────────────────────┘
                        │ Railway API Calls
        ┌───────────────┼───────────────┬────────────────┐
        │               │               │                │
    Sandbox 1      Sandbox 2      Sandbox 3         Sandbox N
 ┌──────────────┐┌──────────────┐┌──────────────┐
 │ OpenCode     ││ OpenCode     ││ OpenCode     │
 │ Code Server  ││ Code Server  ││ Code Server  │
 │ Git Repo     ││ Git Repo     ││ Git Repo     │
 └──────────────┘└──────────────┘└──────────────┘
```

---

## Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Cloud Platform** | Railway | Infrastructure, hosting, API |
| **Agent** | OpenCode | AI-powered coding tasks |
| **Code Editing** | Code Server (VS Code) | Browser-based editing interface |
| **Backend Framework** | Express.js | REST API implementation |
| **Database** | PostgreSQL | Session metadata, user data |
| **ORM/Query Builder** | Drizzle | Database abstraction layer |
| **Containerization** | Docker | Environment isolation, deployment |
| **Version Management** | Mise | Tool versioning (node, pnpm, CLI) |
| **API Style** | GraphQL | Infrastructure API queries/mutations |
| **Image Registry** | DockerHub | Container image storage and versioning |

---

## Implementation: Step-by-Step

### Step 1: Local Setup with OpenCode

**Goal**: Containerize OpenCode agent for deployment.

**Process**:
1. Use **Mise** to declare tool versions (node, pnpm, opencode, railway CLI)
2. Create Dockerfile with OpenCode install script
3. Configure entry point: `opencode --web --port 3000 --hostname 0.0.0.0`
4. Build and test locally with Docker

**Key Insight**: Using Mise ensures reproducible builds across developers and CI/CD systems.

### Step 2: Deploy to Railway (Initial)

**Goal**: Get containerized OpenCode running on Railway.

**Process**:
1. Connect GitHub repository to Railway project
2. Configure `RAILWAY_DOCKERFILE_PATH` environment variable for subdirectory builds
3. Railway auto-detects git push → triggers build and deploy
4. Railway auto-generates public domain for access

**Result**: OpenCode agent accessible via public URL.

### Step 3: Optimize with Pre-built Images

**Goal**: Reduce deployment time by building images locally.

**Process**:
1. Build container locally for AMD64 architecture (Railway uses AMD64, not ARM)
2. Push to DockerHub with semantic versioning (v1.0.0, v1.1.0, etc.)
3. Create Railway service that pulls from DockerHub image
4. Skip the build step → faster deployments (seconds vs minutes)

**Benefit**: Enables rapid iteration during development. Build locally in 1 minute, deploy in 10 seconds.

### Step 4: Add Code Server

**Goal**: Provide VS Code interface for code editing alongside agent.

**Process**:
1. Add Code Server installation to Dockerfile
2. Disable authentication (`--auth none`) since control plane handles auth
3. Expose on port 8080 (distinct from agent port 3000)
4. Rebuild and re-deploy

**Result**: Users can view code while agent modifies it in real-time.

### Step 5: Railway API Integration

**Goal**: Programmatically manage service lifecycle via Railway's GraphQL API.

**Process**:

1. Generate Railway API token (account-scoped or project-scoped)
2. Query Railway GraphQL schema to discover available operations
3. Implement key mutations:
   - `serviceCreate`: Provision new sandbox
   - `serviceDelete`: Tear down unused sandbox
4. Test with API client (Postman, Jack, or curl)

**Example Mutation** (Create Service):
```graphql
mutation {
  serviceCreate(input: {
    projectId: "PROJECT_ID"
    environmentId: "ENV_ID"
    name: "sandbox-001"
    source: { image: "docker.io/user/opencode:v1.0.0" }
  }) {
    id
    name
    status
  }
}
```

### Step 6: Build Control Plane API

**Goal**: Create centralized management API for session lifecycle.

**Components**:
- **Express.js Backend**: REST endpoints for frontend
- **Drizzle ORM**: Database schema for sessions, users, metadata
- **PostgreSQL**: Persistent data storage
- **Railway API Client**: Wrapper around GraphQL API
- **Auth Middleware**: Validate user requests

**Core Endpoints** (to be implemented):
- `POST /sessions` → Create new sandbox via Railway API
- `GET /sessions` → List user's sandboxes
- `DELETE /sessions/:id` → Delete sandbox via Railway API
- `GET /sessions/:id/details` → Get connection info

---

## Key Technical Decisions

### 1. Architecture: Separate Control Plane from Sandboxes

**Why**: Enables independent scaling. Control plane is lightweight; sandboxes are resource-intensive.

**Benefit**: Control plane can run on small Railway service; sandboxes spin up large instances only when needed.

### 2. Pre-built Docker Images on DockerHub

**Why**: Dramatically speeds up deployments (avoids build step).

**Tradeoff**: Requires maintaining image versioning and pushing to registry.

**Benefit Worth It For**: This use case (frequent deployments, rapid iteration).

### 3. GraphQL API for Infrastructure

**Why**: Railway provides GraphQL API; alternative would require REST + custom parsing.

**Benefit**: Schema introspection allows API clients to auto-discover operations.

### 4. Code Server + OpenCode Dual Interface

**Why**: Accommodates different workflows (agents modify code, humans review).

**Result**: Both can run simultaneously; changes visible in both interfaces.

### 5. Git Isolation Per Sandbox

**Why**: Prevents sandboxes from interfering with each other.

**Implementation**: Each sandbox gets fresh git clone with independent working tree.

---

## Deployment & Operations

### Local Development
```bash
# Install tools via Mise
mis install

# Build container locally
mis run build

# Run locally with Docker
mis run dev

# Deploy to Railway (rapid iteration)
railway up
```

### Production Deployment
```bash
# Build for AMD64 architecture
docker buildx build --platform linux/amd64 -t user/opencode:v1.0.0 .

# Push to DockerHub
docker push user/opencode:v1.0.0

# Update Railway service image
# (via Dashboard or API)
```

### Scaling Strategy
1. **Control Plane**: Single small Railway service
2. **Sandboxes**: Dynamically provisioned (auto-created and destroyed)
3. **Database**: PostgreSQL managed by Railway
4. **Storage**: Local per-sandbox (ephemeral, no persistent storage needed)

---

## Real-World Impact

### Use Cases Unlocked

✅ **Distributed Development Teams**: Share agent sessions across geography
✅ **Remote Pair Programming**: Team reviews agent's work in real-time
✅ **Educational Platforms**: Multiple students using same agents
✅ **Developer Tools Companies**: Build VS Code forks with integrated agents
✅ **CI/CD Integration**: Trigger sandboxes from pipelines for code generation

### Scalability Advantages

| Scenario | Local Approach | Cloud Approach |
|----------|---|---|
| Single Agent | 1 device limited | Cloud unlimited |
| 10 Agents | Resource-starved | Provision on demand |
| Team Access | Share via SSH? | Web dashboard |
| Cross-device | SSH from phone? | Browser anywhere |
| Persistence | Manual backups | Cloud managed |

---

## Technical Highlights Demonstrated

✅ **End-to-End Deployment**: From local development to production Railway
✅ **GraphQL API Interaction**: Real queries and mutations against Railway API
✅ **Multi-Platform Builds**: Managing ARM (MacBook) → AMD64 (Railway) architecture
✅ **Container Versioning**: Semantic versioning, rollback capabilities
✅ **Database-Driven State**: PostgreSQL for session persistence
✅ **Professional DevOps**: Environment variables, secrets, configuration management

---

## Takeaways

1. **Cloud-First Thinking**: Moving agents to infrastructure unlocks collaboration and scale
2. **API-Driven Operations**: Infrastructure as code enables programmatic management
3. **Containerization Simplifies**: Docker removes "works on my machine" problems
4. **Separation of Concerns**: Control plane, services, and UI can evolve independently
5. **Developer Experience Matters**: Railway's focus on DX reduces deployment friction

---

## Related Resources

- [OpenCode GitHub](https://github.com)
- [Railway Documentation](https://railway.app/docs)
- [Code Server GitHub](https://github.com/coder/code-server)
- [Mise - Version Manager](https://mise.jdx.dev)
- [Drizzle ORM](https://orm.drizzle.team)
- [Express.js Documentation](https://expressjs.com)

---

## Full Transcript & Resources

This post summarizes a 92-minute technical deep-dive. For complete details:

- **Full Transcript**: [file in resources]
- **Short Summary**: [file in resources]
- **Video Channel**: DevOps Directive YouTube
- **Sponsor**: Railway Platform