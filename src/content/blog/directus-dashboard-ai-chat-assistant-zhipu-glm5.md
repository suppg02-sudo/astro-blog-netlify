---
pubDatetime: 2026-03-25T21:25:00Z
title: "Building a Personal AI Chat Assistant: Directus Dashboard with Zhipu GLM-5 Integration"
postSlug: "directus-dashboard-ai-chat-assistant-zhipu-glm5"
description: "Building a Personal AI Chat Assistant: Directus Dashboard with Zhipu GLM-5 Integration"
tags:
  - directus
  - postgresql
  - opensearch
  - chat-assistant
  - docker
  - ai
  - zhipu
  - glm-5
---

Building a personal AI assistant that has access to your memories, documents, and can answer questions using your own knowledge base sounds like a complex project. But with the right architecture and modern tools, it's surprisingly achievable.

In this post, I'll walk you through how I built a complete AI chat assistant integrated into a Directus dashboard, powered by Zhipu's GLM-5 model, with access to 1,370+ memories stored in PostgreSQL and semantic document search via OpenSearch.

## The Architecture

The system consists of four main components working together:

1. **Directus CMS** (port 8055) - Backend data management
2. **React Dashboard** (port 8056) - Frontend user interface
3. **Chat API** (port 8057) - FastAPI service with GLM-5 integration
4. **Knowledge Base** - PostgreSQL with pgvector + OpenSearch

```
┌─────────────────┐
│  React Dashboard │ :8056
│   (Frontend)     │
└────────┬────────┘
         │
         ├─────────────────┐
         │                 │
         ▼                 ▼
┌─────────────────┐  ┌──────────────┐
│  Directus CMS   │  │   Chat API   │ :8057
│   (Backend)     │  │  (FastAPI)   │
└─────────────────┘  └──────┬───────┘
                           │
                    ┌──────┴──────┐
                    │             │
                    ▼             ▼
            ┌──────────────┐ ┌──────────────┐
            │  PostgreSQL  │ │  OpenSearch  │
            │  (Memories)  │ │ (Documents)  │
            └──────────────┘ └──────────────┘
```

## Component Breakdown

### 1. Directus CMS (Backend)

Directus serves as the headless CMS backend, providing:
- User authentication and permissions
- Data modeling and API generation
- Content management interface
- Direct API token access for the chat service

Running on port 8055 with PostgreSQL (pgvector) for data storage and Redis for caching.

```yaml
services:
  directus:
    image: directus/directus:11.15.4
    ports:
      - "8055:8055"
    environment:
      - DB_CLIENT=pg
      - CACHE_ENABLED=true
      - CACHE_STORE=redis
```

### 2. React Dashboard (Frontend)

A custom React application providing the user interface for:
- Chat interface with the AI assistant
- Document upload and management
- Memory browsing and search
- Dashboard configuration

The frontend is served via Nginx on port 8056, communicating with both Directus and the Chat API.

### 3. Chat API (The AI Brain)

The heart of the system is a FastAPI service that integrates with Zhipu's GLM-5 model:

```python
# Z.ai Coding Plan configuration
OPENCODE_BASE_URL = "https://api.z.ai/api/coding/paas/v4"
DEFAULT_MODEL = "glm-5"

def get_auth_headers():
    api_key = os.getenv("ZHIPU_API_KEY", "")
    if api_key:
        return {"Authorization": f"Bearer {api_key}"}
    return {}
```

**Key Features:**
- Streaming responses via Server-Sent Events (SSE)
- Tool calling for memory and document search
- Session management for conversational context
- Error handling and retry logic

### 4. Knowledge Base

Two complementary storage systems:

**PostgreSQL with pgvector** - Stores structured memories:
- Past conversations and decisions
- Actions and workflows
- Tagged and searchable with vector embeddings
- Current count: 1,370 memories

**OpenSearch** - Stores uploaded documents:
- PDFs, text files, markdown
- Semantic search capabilities
- Full-text indexing

## Available Tools

The AI assistant has access to 5 powerful tools:

### 1. memory_search
Search through stored memories in PostgreSQL using semantic similarity.

```json
{
  "name": "memory_search",
  "description": "Search through the user's stored memories",
  "parameters": {
    "query": "string"
  }
}
```

**Example**: "What did I decide about the database migration?" → Searches memories and returns relevant decisions.

### 2. document_search
Search uploaded documents using OpenSearch semantic search.

```json
{
  "name": "document_search",
  "description": "Search through uploaded documents",
  "parameters": {
    "query": "string"
  }
}
```

### 3. list_memories
Browse stored memories with optional filters.

```json
{
  "name": "list_memories",
  "parameters": {
    "memory_type": "action|decision|conversation|exchange",
    "limit": 10
  }
}
```

### 4. get_memory_stats
Get statistics about stored knowledge.

```json
{
  "name": "get_memory_stats",
  "description": "Get statistics about stored memories"
}
```

**Current stats:**
- Total: 1,370 memories
- By type: 560 actions, 674 conversations, 68 decisions, 68 exchanges
- Recent activity: 44 new memories in last 7 days

### 5. ask_user
Interactive questioning with predefined options.

```json
{
  "name": "ask_user",
  "parameters": {
    "question": "string",
    "header": "string",
    "options": [{"label": "...", "description": "..."}],
    "multiple": false
  }
}
```

## Testing the Assistant

After setup, here's what I tested:

### Basic Conversation
```bash
curl -X POST http://localhost:8057/chat/stream \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"Hello, introduce yourself"}]}'
```

**Response** (streaming):
```
Hello! I'm your personal AI assistant with access to your knowledge base. 
I can help you:
- **Search your memories** - Find past conversations, decisions, and actions
- **Search your documents** - Look through uploaded PDFs and text files
- **Browse stored information** - Review what's been saved
- **Answer questions** - Using information from your memories and documents
```

### Memory Search
```bash
curl -X POST http://localhost:8057/chat/stream \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"What do you know about directus?"}]}'
```

**Result**: The assistant automatically called `memory_search` and returned 6 relevant memories about Directus setup, configuration, and related decisions.

### Direct API Calls

You can also call the tools directly:

```bash
# Search memories
curl -X POST http://localhost:8057/memory/search \
  -H "Content-Type: application/json" \
  -d '{"query":"directus","limit":3}'

# Get stats
curl http://localhost:8057/memory/stats

# List indices
curl http://localhost:8057/documents/indices
```

## Technical Implementation Details

### Streaming Architecture

The chat API uses Server-Sent Events (SSE) for real-time streaming:

```python
@router.post("/stream")
async def chat_stream(request: ChatRequest):
    async def event_generator():
        async for event in generate_response(request):
            yield {"event": "message", "data": event}
    
    return EventSourceResponse(event_generator())
```

The response includes different event types:
- `{"type": "content", "delta": "..."}` - Text chunks
- `{"type": "tool_result", "tool_name": "...", "result": {...}}` - Tool outputs
- `{"type": "done"}` - Stream complete

### Tool Calling Flow

When the user asks a question:

1. **Intent Detection** - GLM-5 analyzes the query
2. **Tool Selection** - Decides which tool(s) to call
3. **Tool Execution** - Backend executes the tool (e.g., memory search)
4. **Result Integration** - Tool results fed back to the model
5. **Response Generation** - Final answer synthesized

### Docker Compose Setup

```yaml
services:
  chat-api:
    build:
      context: ./chat-api
      dockerfile: Dockerfile
    ports:
      - "8057:8057"
    environment:
      - ZHIPU_API_KEY=${ZHIPU_API_KEY:-}
      - OPENCODE_ZEN_API_KEY=${OPENCODE_ZEN_API_KEY:-}
      - PGVECTOR_HOST=host.docker.internal
      - PGVECTOR_PORT=5432
      - PGVECTOR_USER=memory_user
      - PGVECTOR_PASSWORD=${DB_PASSWORD}
      - PGVECTOR_DB=memory_db
      - OPENSEARCH_HOST=os
      - OPENSEARCH_PORT=9200
      - DIRECTUS_URL=http://directus:8055
      - DIRECTUS_TOKEN=${DIRECTUS_TOKEN}
    networks:
      - directus_default
    extra_hosts:
      - "host.docker.internal:host-gateway"
```

### Network Configuration

Key issue solved: OpenSearch container needed to be on the same network as the chat API:

```bash
docker network connect directus_default os
```

This allows the chat API to reach OpenSearch at `os:9200` for document searches.

## Challenges and Solutions

### Challenge 1: Rate Limiting on Free Tier
**Problem**: Initial testing hit 429 errors on OpenCode Zen free tier.

**Solution**: Switched to Zhipu GLM-5 Coding Plan with dedicated endpoint:
- Endpoint: `https://api.z.ai/api/coding/paas/v4`
- Model: `glm-5`
- Requires valid API key with credits

### Challenge 2: Model Not Found
**Problem**: "Unknown Model" errors when using incorrect model names.

**Solution**: Updated default model from `nemotron-3-super-free` to `glm-5` in both the service layer and request schema.

### Challenge 3: Network Isolation
**Problem**: Chat API couldn't reach OpenSearch for document searches.

**Solution**: Connected OpenSearch container to the `directus_default` network, enabling inter-container communication.

### Challenge 4: Async Response Handling
**Problem**: AttributeError when handling error responses (`response.atext()` doesn't exist).

**Solution**: Use synchronous `response.text` for error details in async context.

## Performance Observations

- **Response Time**: 7-8 seconds for initial token (GLM-5 streaming)
- **Memory Search**: ~100ms for semantic search across 1,370 memories
- **Document Search**: ~200ms for OpenSearch queries
- **Tool Calling**: Automatic and transparent to the user

## Access Points

Once deployed, access the system at:

| Service | URL | Purpose |
|---------|-----|---------|
| Dashboard UI | http://ubuntu4:8056 | Chat interface |
| Chat API | http://ubuntu4:8057 | API endpoint |
| API Docs | http://ubuntu4:8057/docs | Swagger UI |
| Health Check | http://ubuntu4:8057/health | Service status |
| Directus Admin | http://ubuntu4:8055 | CMS backend |

## Future Improvements

### Short Term
- [ ] Add document upload via chat interface
- [ ] Implement conversation history persistence
- [ ] Add more specialized tools (web search, code execution)
- [ ] Improve error messages and retry logic

### Medium Term
- [ ] Multi-model support (switch between GLM-5, GPT-4, Claude)
- [ ] Voice input/output integration
- [ ] Mobile-responsive chat interface
- [ ] Export conversations to markdown/PDF

### Long Term
- [ ] Fine-tune GLM-5 on personal knowledge base
- [ ] Implement RAG (Retrieval Augmented Generation) pipeline
- [ ] Add collaborative features (share knowledge bases)
- [ ] Build plugin system for custom tools

## Cost Analysis

**Zhipu GLM-5 Coding Plan**:
- $10/month for coding scenarios
- Dedicated API endpoint
- Higher rate limits than free tier
- Compatible with OpenAI SDK format

**Infrastructure** (already running):
- PostgreSQL with pgvector: Existing server
- OpenSearch: Existing cluster
- Docker containers: Minimal overhead
- Redis caching: Improves performance

**Total additional cost**: $10/month for GLM-5 API access

## Conclusion

Building a personal AI assistant with access to your own knowledge base is now practical and affordable. The combination of:

- **Directus** for backend management
- **React** for the frontend
- **FastAPI** for the chat service
- **GLM-5** for intelligence
- **PostgreSQL + OpenSearch** for knowledge storage

...creates a powerful system that learns from your conversations, remembers your decisions, and can search through your documents.

The key insight is that modern AI models with tool-calling capabilities can seamlessly integrate with your existing data infrastructure. You don't need to build complex RAG pipelines from scratch—the model handles the orchestration automatically.

Whether you're building a personal assistant, a customer support bot, or an internal knowledge tool, this architecture provides a solid foundation that's both powerful and extensible.

---

**Source Code**: Configuration files available in `/media/docker/dashboard/`
**Live Demo**: http://ubuntu4:8056 (requires network access)
**API Documentation**: http://ubuntu4:8057/docs

---

*Built with Directus 11.15.4, FastAPI, React, Zhipu GLM-5, PostgreSQL with pgvector, and OpenSearch*