---
pubDatetime: 2026-03-05T22:45:00Z
title: "Week in Review: Building a Personal AI Assistant Infrastructure"
postSlug: "week-in-review-personal-ai-assistant-infrastructure"
description: "Week in Review: Building a Personal AI Assistant Infrastructure"
tags:
  - openmemory
  - server-setup
  - automation
  - ai-infrastructure
  - research
---

## Executive Summary

Over the past 7 days (Feb 26 - Mar 5, 2026), this personal AI assistant server has undergone significant infrastructure expansion. The work focused on four key areas:

- **AI Infrastructure**: Deployed LiveKit Agents for voice AI, LiteLLM proxy for multi-provider LLM access, and OpenMemory MCP for persistent agent memory
- **Data Layer**: Implemented PostgreSQL + pgvector for RAG embeddings, integrated Directus CMS with vector support
- **Automation**: Migrated flow tracking to OpenMemory, configured automated research workflows, set up cron jobs for content generation
- **Tooling**: Enhanced question tool with 3-phase implementation, created new triggers (q-brainstorm, flows), added interaction counter protocol

**Current State**: 32% roadmap complete (3 of 19 phases), 10+ services operational, 1,083+ memories stored, 152 document chunks embedded for RAG.

## Major Infrastructure Additions

### AI Stack Components

{{<mermaid>}}
graph LR
    A[User Request] --> B[OpenCode Agent]
    B --> C{LLM Gateway}
    C --> D[LiteLLM Proxy]
    D --> E[z.ai GLM-5]
    D --> F[OpenAI]
    D --> G[Future: Ollama Local]
    B --> H[OpenMemory MCP]
    H --> I[SQLite HSG]
    B --> J[RAG System]
    J --> K[PostgreSQL pgvector]
    K --> L[152 Embedded Chunks]
{{</mermaid>}}

**LiteLLM Proxy** (port 4000)
- Multi-provider LLM gateway (OpenAI, z.ai, future Ollama)
- Unified API interface for all LLM calls
- Rate limiting and fallback support
- Migration path to local inference (TELOS compliance)

**OpenMemory MCP Server** (port 8081)
- Persistent AI memory storage (1,083+ memories)
- Hierarchical Semantic Graph (HSG) architecture
- 5 memory sectors: semantic, procedural, episodic, emotional, reflective
- CRUD pattern: content for search, metadata for structured data
- Temporal graph for fact tracking with confidence levels

**LiveKit Agents Starter** (agent-starter-react)
- Voice AI infrastructure with React + LiveKit SDK
- Foundation for conversational AI interfaces
- Real-time voice interaction capabilities

### Data Layer Enhancements

**PostgreSQL + pgvector for RAG**
- Database: `rag-postgres` on port 5433
- 152 document chunks embedded with text-embedding-3-small
- Semantic search across OpenCode documentation
- Scripts: `/root/rag-scripts/` (chunk_docs.py, embed_and_store.py, retrieve.py)
- Total embedding cost: <$0.01

**Directus CMS v11.15.4** (port 8055)
- Headless CMS with PostgreSQL backend
- pgvector support for vector operations
- Migration plan created: OpenMemory SQLite → Directus PostgreSQL
- 6-phase implementation with validation and rollback procedures

### LiveKit Voice AI Infrastructure

74: 
75: **agent-starter-react** - Production-ready voice AI interface
76: 
77: Deployed LiveKit's official agent-starter-react template, a comprehensive Next.js-based voice interface for conversational AI applications.
78: 
79: **Purpose**: Build real-time voice AI interfaces with support for transcriptions, virtual avatars, and multi-modal interactions.
80: 
81: **Project Details**:
82: - **Framework**: Next.js 15.5.9 with React 19
83: - **SDK**: LiveKit JavaScript SDK v2.17.2 (client-sdk-js)
84: - **UI Library**: Agents UI (shadcn/ui-based component system)
85: - **Language**: TypeScript with full type safety
86: - **Package Manager**: pnpm 9.15.9 (fast, disk-efficient)
87: - **Project Size**: 328KB lock file (lightweight dependencies)
88: 
89: **Key Features**:
90: - **Real-time Voice**: Low-latency voice interaction with AI agents via WebRTC
91: - **Video Streaming**: Camera video support for video calls and avatars
92: - **Screen Sharing**: Share screen content during conversations
93: - **Audio Visualizers**: 5 styles (bar, grid, radial, wave, aura) with customizable colors
94: - **Virtual Avatars**: Animated avatar integration for human-like interactions
95: - **Theme Support**: Light/dark mode with system preference detection
96: - **Customizable Branding**: Company name, colors, UI text via app-config.ts
97: - **Chat Transcripts**: Real-time transcript display with conversation history
98: - **Session Management**: State tracking for connected/disconnected states
99: 
100: **Architecture Flow**:
101: 
102: {{<mermaid>}}
103: graph LR
104:     A[User Browser] --> B[Next.js Frontend]
105:     B --> C[LiveKit Session]
106:     C --> D[LiveKit Cloud]
107:     D --> E[AI Agent Backend]
108:     B --> F[Agents UI Components]
109:     F --> G[Audio Visualizers]
110:     F --> H[Media Controls]
111:     F --> I[Chat Interface]
112: {{< /mermaid >}}
113: 
114: **Project Structure**:
115: ```
116: agent-starter-react/
117: ├── app/
118: │   ├── api/ - Token generation endpoint (JWT)
119: │   └── (Next.js app routes)
120: ├── components/
121: │   ├── agents-ui/ - Pre-built LiveKit components
122: │   ├── ai-elements/ - AI-specific UI elements
123: │   ├── app/ - Business logic (session management)
124: │   └── ui/ - Shadcn/ui primitives
125: ├── hooks/ - Custom React hooks for state
126: ├── lib/ - Utility functions and helpers
127: └── public/ - Static assets (logo, images)
128: ```
129: 
130: **Core Dependencies** (13 major packages):
131: - `livekit-client` (v2.17.2) - Real-time WebRTC communication
132: - `livekit-server-sdk` (v2.13.3) - Server-side token generation
133: - `@livekit/components-react` (v2.9.20) - React component library
134: - `@livekit/protocol` (v1.41.0) - Protocol definitions
135: - `next` (v15.5.9) - React framework with Turbopack
136: - `react` / `react-dom` (v19.0.0) - UI library
137: - `jose` (v6.0.12) - JWT token handling
138: - `ai` (v5.0.105) - AI SDK utilities
139: - `motion` (v12.16.0) - Animation library
140: - `tailwind-merge` - CSS utility management
141: - `lucide-react` - Icon library
142: - `@radix-ui/*` - Accessible UI primitives
143: 
144: **Configuration**:
145: 
146: **Environment Variables** (`.env.local`):
147: ```env
148: LIVEKIT_API_KEY=your_api_key
149: LIVEKIT_API_SECRET=your_api_secret
150: LIVEKIT_URL=wss://project-subdomain.livekit.cloud
151: AGENT_NAME=  # Optional: explicit agent dispatch
152: ```
153: 
154: **App Configuration** (`app-config.ts`):
155: ```typescript
156: export const APP_CONFIG_DEFAULTS: AppConfig = {
157:   companyName: 'LiveKit',
158:   pageTitle: 'LiveKit Voice Agent',
159:   supportsChatInput: true,
160:   supportsVideoInput: true,
161:   supportsScreenShare: true,
162:   isPreConnectBufferEnabled: true,
163:   logo: '/lk-logo.svg',
164:   accent: '#002cf2',
165:   audioVisualizerType: 'bar', // or 'radial', 'grid', 'wave', 'aura'
166:   agentName: undefined, // Auto-dispatch
167: };
168: ```
169: 
170: **Deployment Configuration**:
171: - **Container**: `livekit-https` (nginx reverse proxy)
172: - **Port**: 3443 (HTTPS via nginx proxy)
173: - **SSL/TLS**: Self-signed certificates with TLS 1.2/1.3
174: - **Domain**: `ubuntu4.tail75e52.ts.net` (Tailscale VPN)
175: - **Backend**: Next.js dev server (port 3000) → nginx → public HTTPS (3443)
176: - **Upstream**: `host.docker.internal:3000` (Docker networking)
177: 
178: **Nginx Configuration Highlights**:
179: ```nginx
180: upstream livekit_backend {
181:     server host.docker.internal:3000;
182: }
183: 
184: server {
185:     listen 443 ssl http2;
186:     server_name ubuntu4.tail75e52.ts.net;
187:     
188:     ssl_protocols TLSv1.2 TLSv1.3;
189:     ssl_ciphers HIGH:!aNULL:!MD5;
190:     
191:     location / {
192:         proxy_pass http://livekit_backend;
193:         proxy_http_version 1.1;
194:         # WebSocket support for real-time communication
195:     }
196: }
197: ```
198: 
199: **Current Status**: ✅ **Operational**
200: - Container running: `livekit-https` (Up 29 minutes)
201: - Accessible via: `https://ubuntu4.tail75e52.ts.net` (Tailscale VPN only)
202: - Backend: Next.js development server with hot reload
203: - Dependencies: All 328KB installed via pnpm
204: - Ready for: Connection to LiveKit Cloud or self-hosted LiveKit server
205: 
206: **Integration with TELOS Principles**:
207: - **Voice Interface**: Enables natural language interaction with AI agents
208: - **Real-time Communication**: WebSocket-based via LiveKit (currently external, migration planned)
209: - **Extensible Backend**: Can connect to Python or Node.js agent backends
210: - **Future**: Migration path to self-hosted LiveKit server for full data sovereignty
211: 
212: **Use Cases**:
213: - Conversational AI assistants with voice interfaces
214: - Real-time transcription and translation services
215: - Virtual avatar platforms for customer service
216: - Multi-modal AI interfaces (voice + video + text simultaneously)
217: - Voice-controlled smart home automation
218: - AI-powered meeting assistants with live transcription
219: 
220: **Next Steps**:
221: - Connect to self-hosted LiveKit server (TELOS compliance)
222: - Deploy Python/Node.js agent backend (e.g., agent-starter-python)
223: - Configure agent dispatch for specific use cases
224: - Test voice interaction via Tailscale VPN
225: - Explore virtual avatar integration
226: 
227: ### Supporting Services

| Service | Purpose | Port |
|---------|---------|------|
| **OliveTin** | Web-based script execution | 1337 |
| **WeasyPrint** | HTML/CSS to PDF conversion | Docker |
| **pgAdmin** | PostgreSQL management UI | 80 |
| **Homepage** | Service dashboard | 8765 |
| **Nginx Proxy Manager** | Reverse proxy management | 80/443 |
| **Memos** | Note-taking application | 5230 |
| **NextExplorer** | File browser | 8080 |
| **FileBrowser** | File management | 8766 |
| **Hugo** | Primary blog (this site) | 1314 |
| **Astro** | Backup blog | 4321 |
| **FreshRSS** | RSS feed reader | Docker |
| **Excalidraw** | Diagram drawing tool | Docker |

## Automation & Workflow Systems

### Flow Tracking Migration

Migrated from JSON file-based flow tracking to OpenMemory-based system:

**Before**: `/root/.config/opencode/context-registry/data/flows.json`

**After**: OpenMemory MCP Server with semantic search

{{<mermaid>}}
graph TD
    A[Flow Triggered] --> B[flows_app Script]
    B --> C[OpenMemory MCP]
    C --> D[Store: type=flow]
    D --> E[HSG Indexing]
    E --> F[Semantic Search Ready]
    G[Query Flows] --> H[openmemory_query]
    H --> I[Retrieve Related Context]
    I --> J[Synthesis & Analysis]
{{</mermaid>}}

**Benefits**:
- Semantic search across all flows (not just keyword matching)
- Memory decay with salience scoring
- Context-aware flow recommendations
- Cross-session pattern recognition

### Cron Automation Setup

Configured 12 automated tasks for Phase 6 (Personal Cron Job Automation):

| Task | Schedule | Purpose |
|------|----------|---------|
| Weekly Memory Report | Sunday 10:00 AM UTC | OpenMemory stats → Hugo blog |
| Daily AI Ecosystem Research | Daily 8:00 AM UTC | GitHub stats, HN trends → Blog |
| Hourly Issue Monitor | Hourly | System health checks |
| Roadmap Progress Reminder | Daily | Phase completion tracking |
| Deferred Tasks Alert | Daily | Review parked tasks |
| Weekly Goals Review | Weekly | Progress assessment |
| Evening Memory Stats | Daily | End-of-day summary |
| Context Registry Sync | Hourly | Keep registries updated |
| Weekly Ecosystem Research | Weekly | AI/LLM ecosystem trends |
| Weekly RAG Developments | Weekly | RAG technology updates |
| Monthly Agent Tools | Monthly | New agent tooling review |
| Cron Job Dashboard Widget | Real-time | Homepage integration |
| Cron Failure Notifications | Immediate | Alert on failures |

**Key Implementation**: `memory-report.py --quiet` publishes weekly Hugo blog automatically (1349 words, comprehensive analysis with Mermaid diagrams).

### YouTube → Blog Pipeline

Automated workflow for converting YouTube videos to blog posts:

{{<mermaid>}}
sequenceDiagram
    participant User
    participant YouTube
    participant Transcript
    participant Agent
    participant Hugo
    
    User->>YouTube: Provide URL
    YouTube->>Transcript: Extract captions
    Transcript->>Agent: Send text
    Agent->>Agent: Generate summary
    Agent->>Agent: Create frontmatter
    Agent->>Hugo: Write markdown file
    Hugo->>Hugo: Auto-rebuild
    Hugo->>User: Published post
{{</mermaid>}}

**Successes**:
- "Wes Roth Reacts: Cal Newport Gets AI Progress Exactly Backwards" (video: uWLt81SgM78)
- Automatic transcript extraction and summarization
- Hugo blog post creation with proper frontmatter
- Validation via agent browser automation

**Challenges Identified**:
- Silent failures in automation pipeline
- Need for better error propagation
- Stall point debugging required

### Research Task Automation

**Web Interface** (port 8898)
- Research Task web form with scheduling options
- Intensity levels: minimal, normal, verbose, brainstorm
- Source selection: Web, Docs, GitHub, Academic, News
- Cron scheduling: Now, Hourly, Daily, Weekly, Monthly, Custom
- Auto-publishing to Hugo blog

**API Endpoints**:
```
GET  /                    # Web form
POST /api/execute         # Execute/schedule research task
GET  /api/status/<id>     # Check task status
GET  /health              # Health check
```

**Execution Script**: `/media/docker/olivetin/config/scripts/execute-research.sh`

## Configuration & Tooling Enhancements

### Question Tool Enhancement (3 Phases + Quick Win)

**Phase 1: Templates System** ✅
- Template schema with YAML validation
- 3 default templates (deployment, research, troubleshooting)
- Template loader with registry
- Location: `~/.config/opencode/questions/templates/`

**Phase 2: Chained Questions** ✅
- Chain schema for multi-step workflows
- 2 example chains: deployment-workflow, feature-approval
- Chain executor with state management
- Branching logic support
- Location: `~/.config/opencode/questions/chains/`

**Phase 3: Smart Generation** ✅
- Context analyzer for session awareness
- Question generator with intensity controls
- Intensity levels: off, minimal, normal, verbose
- History optimization for relevance
- Scripts: `context_analyzer.py`, `question_generator.py`

**Quick Win: Auto-Complete** ✅
- Fuzzy matching for option selection
- Keyboard navigation support

**Total Files Created**: 13 (schemas, scripts, templates, chains)

### New Triggers

**q-brainstorm** (Enhanced Question Workflow)
- Always-multiselect mode for brainstorming
- 3-state selection: Yes / Maybe / Skip
- Conflict detection between selections
- Auto-defer for parking items
- Custom text input handling
- Location: `~/.config/opencode/docs/instructions/triggers/q-brainstorm.md`

**flows** (Flow Management Menu)
- Analyse Recent Flow
- Simulate Flow
- Popular Flows → Blog
- What Was Recorded?
- Stats & Analytics
- Search Flow History
- Session Review
- Intensity/Mode controls
- Recording status check

### Interaction Counter Protocol

**Purpose**: Track user-agent exchanges and prevent runaway sessions

**Behavior**:
- Count increments on each user → agent exchange
- Warning at interactions 5, 10, 15, etc.
- 5-second countdown before continuing
- Question tool menu with options: Continue, Change settings, Disable for session
- Link to Homepage Dashboard (http://ubuntu4:8765/)

**Implementation**:
- Scope: Per session only
- Counter file: `/root/.config/opencode/.ga-counter` (for `ga` trigger)
- Integration: Mandatory question tool display after warning

### Configuration Updates

**Local File Links in AGENTS.md**
- Added NextExplorer clickable link format
- Reference link style for cleaner text
- Volume mapping: opencode, docker, freshstart, back, storage
- Example: `[RAG.md]: http://ubuntu4:8080/editor/opencode/docs/RAG.md`

**OpenMemory MCP Fix**
- **Problem**: `skill_mcp(openmemory)` does NOT work
- **Solution**: Use native `mcp_openmemory_*` tools directly
- **Fallback**: Direct API via curl with Bearer token
- Verified working: 2026-03-04

**Question Tool Permission Fix**
- Changed `oh-my-opencode.json` permissions from `"allow"` to `"ask"`
- Applies to all 18 agents
- Prevents mangled question displays

## Content Creation & Documentation

### Blog Posts Published

| Date | Title | Category | Word Count |
|------|-------|----------|------------|
| Mar 5 | Question Tool Enhancement Complete | Implementation | 2,500+ |
| Mar 5 | OpenMemory Storage Analysis | AI Infrastructure | 1,349 |
| Mar 5 | Microsoft Power Apps MCP Server | Enterprise AI | 1,894 |
| Mar 5 | Server Setup Roadmap 2026 | Infrastructure | 3,500 |
| Mar 4 | Flow Tracking Migration | Migration | 2,500 |
| Mar 4 | YouTube Flow Stall Points | Debugging | 1,500 |
| Mar 4 | OpenMemory: Production-Ready Memory | AI Infrastructure | 2,000+ |

**Total**: 7 major blog posts, 15,000+ words

### Documentation Updates

- **q-brainstorm.md**: Added Appendix A (Question Tool Discoveries), Appendix B (Anti-Patterns)
- **bp.md**: Removed blog post storage to OpenMemory (redundancy)
- **AGENTS.md**: Updated Local File Links section, OpenMemory CRUD pattern, MCP calling order
- **environment.md**: Living document tracking all services, dependencies, architecture
- **roadmap.json**: Phase 6 expanded from 3 to 12 tasks, Phase 12 added

### Deferred Tasks

Tasks parked for future investigation:

1. **Tier Upgrade Investigation**: OpenMemory fast → balanced (check ZAI port 8002 as embedding provider, RAM impact, temporal graph activation)
2. **WAL Checkpoint**: 36.6MB WAL file needs truncating to reclaim disk space
3. **Question Templates**: Brainstorm session on file-based + AI-generated + context-aware templates

## Current State & Progress

### Roadmap Status

**Overall Progress**: 32% (3 of 19 phases complete)

{{<mermaid>}}
pie title Roadmap Progress
    "Completed" : 3
    "In Progress" : 1
    "Pending" : 15
{{</mermaid>}}

**Completed Phases** ✅:
1. OpenCode & Foundation (Feb 22)
2. Docker Containers Setup (Feb 27)
3. OpenMemory Integration (Feb 28)

**In Progress** 🔄:
4. Telemetry & Monitoring (logging, health checks)

**Pending Phases** ⏳ (16 remaining):
- Phase 5: Database Setup (2 days)
- Phase 6: Personal Cron Job Automation (2 days) - 12 tasks configured
- Phase 7: Backup Infrastructure (2 days)
- Phase 8: Optional Skills & Tools (3 days)
- Phase 9: Performance Tuning (2 days)
- Phase 10: Job Dashboard & Monitoring UI (3 days)
- Phase 11: Tagging Strategy (2 days)
- Phase 12: User Onboarding & Preferences (1 day) - NEW
- Phase 13-19: App Stack, RAG, TELOS Compliance, Schema Documentation (~20 days)

**Estimated Remaining Work**: ~35 days

### Active Services

**Running Containers**: 10+ core services

**Resource Constraint**: 8GB RAM shared across ~50 containers

**Network**: Tailscale VPN for secure remote access (ubuntu4.tail75e52.ts.net)

### Memory System Stats

**OpenMemory Database**:
- Total memories: 1,083+
- Primary sectors: semantic, procedural, episodic, emotional, reflective
- Storage: SQLite at `/data/openmemory.sqlite`
- HSG (Hierarchical Semantic Graph) architecture
- WAL checkpoint required (38.7MB → truncated to rescue 922 memories)

**Recent Memory Types**:
- `flow`: Workflow tracking, automation runs, delegations
- `initiative`: Projects, configurations, implementations
- `decision`: Architecture choices, troubleshooting resolutions
- `menu_choice`: User selections, preferences
- `workflow`: Multi-step process tracking

## TELOS Compliance Review

### Core Principles Status

| Principle | Status | Notes |
|-----------|--------|-------|
| **Data Sovereignty** | ⚠️ Partial | All data local, but external APIs used |
| **Open Source** | ✅ Active | Prefer open-source alternatives |
| **Local-First AI** | ⚠️ Partial | z.ai GLM external, Ollama planned |
| **Deterministic Workflows** | ✅ Active | Explicit, verifiable processes |
| **Observability** | ⏳ Planned | Phase 4 in progress |

### Violations & Mitigations

| Component | Violation | Mitigation |
|-----------|-----------|------------|
| OpenAI API | External dependency | Move to local LLM (Ollama) |
| z.ai GLM | External API | Rate limiting, fallbacks, local model research |
| External Embeddings | text-embedding-3-small | Investigate local embedding models |

### Ultimate Goal Progress

**Target**: Instructions so clear that smaller open-source models (z.ai 4.7 Flash) can execute tasks correctly.

**Current State**:
- ✅ Local models work for simple agents (librarian, hugo)
- 🔄 Focus on improving instruction clarity for complex tasks
- ⏳ Gradual migration from proprietary to local inference

## Next Steps

### Immediate Priorities (Next 7 Days)

1. **Complete Phase 4** - Telemetry & Monitoring
   - Finish logging setup
   - Implement health check endpoints
   - Configure alerting

2. **Database Setup** - Phase 5
   - PostgreSQL cluster configuration
   - Redis for caching
   - Backup automation

3. **Cron Automation Activation** - Phase 6
   - Enable 12 scheduled tasks
   - Test automation workflows
   - Monitor resource usage

4. **Performance Tuning** - Phase 9
   - Memory optimization for 8GB constraint
   - Container resource limits
   - Query optimization

### Medium-Term Goals (1-2 Months)

1. **App Stack Deployment** - Phases 13-16
   - Supabase for authentication/database
   - LiteLLM as unified LLM gateway
   - Kestra for workflow orchestration
   - OpenTelemetry stack for observability

2. **RAG Enhancement** - Phase 17
   - Full RAG pipeline with pgvector
   - Document classification system
   - Query optimization

3. **TELOS Compliance** - Phase 18
   - Audit external dependencies
   - Migration plan to local LLM
   - Data sovereignty verification

### Long-Term Vision

Build a fully sovereign, open-source AI assistant infrastructure that:
- Serves as a cognitive extension (second brain)
- Maintains complete data ownership
- Runs AI models locally when possible
- Provides deterministic, reproducible workflows
- Offers full observability into system behavior

**Success Metric**: Smaller open-source models (7B-13B parameters) can execute 80% of tasks correctly with clear instructions.

## Conclusion

This week marked significant progress in building a personal AI assistant infrastructure. The focus on AI stack components (LiteLLM, OpenMemory, LiveKit), data layer enhancements (PostgreSQL + pgvector, Directus), and automation systems (flow tracking, cron jobs) has created a solid foundation for the next phases.

The 32% roadmap completion demonstrates steady progress, with 16 phases remaining over approximately 35 days of work. The TELOS principles guide the architecture toward data sovereignty, open-source solutions, and local-first AI, though current external dependencies (OpenAI, z.ai) represent temporary compromises on the path to full local inference.

Key achievements include:
- 1,083+ persistent memories with semantic search
- 152 document chunks embedded for RAG
- 7 major blog posts documenting the journey
- 12 automated tasks configured for regular workflows
- Enhanced question tool with templates, chains, and smart generation

The server is evolving from a collection of services into a coherent AI assistant infrastructure, with clear patterns for memory, automation, content creation, and observability. The next week will focus on completing telemetry setup, activating cron automation, and beginning the database infrastructure that will support the full app stack deployment.

---

**Tags**: #research #ai-infrastructure #openmemory #server-setup #automation

**Related Posts**:
- [OpenMemory Storage Analysis](http://ubuntu4:1314/posts/2026-03-04-openmemory-storage-analysis-what-your-ai-agent-remembers/)
- [Server Setup Roadmap 2026](http://ubuntu4:1314/posts/2026-03-04-server-setup-roadmap-2026-building-self-hosted-ai-infrastructure/)
- [Flow Tracking Migration](http://ubuntu4:1314/posts/flow-tracking-migration-openmemory/)
- [Question Tool Enhancement Complete](http://ubuntu4:1314/posts/question-tool-enhancement-complete/)