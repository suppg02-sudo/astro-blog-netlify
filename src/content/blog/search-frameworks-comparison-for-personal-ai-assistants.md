---
pubDatetime: 2026-02-08T01:47:14Z
title: "Search Frameworks Comparison for Personal AI Assistants"
postSlug: "search-frameworks-comparison-for-personal-ai-assistants"
description: "Search Frameworks Comparison for Personal AI Assistants"
tags:
  - frameworks
  - search
  - ai
  - research
---

# Comprehensive Analysis: Search Frameworks and Deep Research Tools for Personal AI Assistants

In the rapidly evolving landscape of AI-powered personal assistants, choosing the right search framework and research infrastructure is critical. This analysis compares leading search engines, deep research tools, and AI agent frameworks, evaluating them against the **TELOS infrastructure principles** for self-hosted, sovereign AI ecosystems.

## Executive Summary

| Tool Type | Best For | Self-Hosted? | TELOS Alignment |
|-----------|-----------|----------------|------------------|
| **Exa.ai** | Real-time web search API | ❌ Commercial | ⚠️ Good for augmentation |
| **Perplexity** | AI search assistant | ❌ Commercial | ⚠️ Good for augmentation |
| **SearXNG** | Privacy-focused meta-search | ✅ Self-hostable | ✅ **Highly aligned** |
| **Undermind.ai** | Academic research | ❌ Commercial | ⚠️ Good for specialized tasks |
| **AutoGPT** | Autonomous agents | ✅ Open-source | ✅ **Highly aligned** |
| **Atomic Agents** | Multi-agent systems | ✅ Open-source | ✅ **Highly aligned** |

**Key Finding**: A hybrid approach combining **self-hosted SearXNG** (primary search) with **Exa.ai API** (augmentation layer) provides the best balance of TELOS compliance and functionality.

---

## Part 1: AI Search Engines Comparison

### 1.1 Exa.ai - Real-Time AI Search Engine

**Overview**: Exa provides a powerful AI search engine with web search API, crawling API, SERP API, and deep research tools.

**Key Features**:
- Real-time search with AI-powered result ranking
- Structured content extraction from websites
- Deep research capabilities for complex queries
- RESTful API with easy integration

**TELOS Alignment Analysis**:
- **✅ Data Sovereignty**: ❌ Commercial service (API calls go to external servers)
- **✅ Open Source**: ❌ Proprietary
- **✅ Local-First**: ❌ Cloud-based
- **✅ Deterministic**: ⚠️ API responses are probabilistic but structured
- **✅ Observability**: ✅ API logging and rate limiting available

**Integration with Current Setup**:
- ✅ Already available as **grep_app_get_code_context** MCP tool
- ✅ Can be used as **augmentation layer** for specialized tasks
- ✅ Fits into TELOS "Probabilistic" layer (augmentation, not core)

**Use Case**: Ideal for **complex web research** requiring AI-powered result analysis when local search is insufficient.

**Deployment Considerations**:
```yaml
resource_usage:
  cpu: Low (API calls only)
  memory: Low (API client only)
  network: Moderate (external API calls)
  
integration_points:
  - MCP: grep_app_get_code_context (already integrated)
  - Fabric: Custom pattern for Exa-based research
  - OpenMemory: Store research results with citations

latency: 200-500ms per query
rate_limits: Check API documentation
```

---

### 1.2 Perplexity - AI-Powered Search Assistant

**Overview**: Perplexity is an AI search assistant that provides direct answers with citations, similar to a research librarian.

**Key Features**:
- Direct answers with source citations
- Contextual follow-up questions
- Multi-modal search (text, images, academic papers)
- API for programmatic access

**TELOS Alignment Analysis**:
- **✅ Data Sovereignty**: ❌ Commercial service
- **✅ Open Source**: ❌ Proprietary
- **✅ Local-First**: ❌ Cloud-based
- **✅ Deterministic**: ⚠️ Probabilistic (LLM-powered)
- **✅ Observability**: ✅ Citation tracking available

**Integration with Current Setup**:
- ❌ Not currently integrated
- ⚠️ Could be integrated via **Fabric pattern** for specialized queries
- ⚠️ Requires API key management

**Use Case**: Good for **quick answers** with citations when local RAG is insufficient.

**Deployment Considerations**:
```yaml
resource_usage:
  cpu: Low (API calls only)
  memory: Low (API client only)
  network: Moderate (external API calls)
  
integration_points:
  - Fabric: Pattern for Perplexity-powered research
  - OpenMemory: Store answers with citations
  - MCP: Custom wrapper for Perplexity API

latency: 500-1000ms per query
rate_limits: Check API documentation
```

---

### 1.3 SearXNG - Self-Hosted Meta-Search Engine

**Overview**: SearXNG is a privacy-respecting, hackable metasearch engine that aggregates results from multiple search services.

**Key Features**:
- Self-hosted (privacy-preserving)
- Aggregates results from 70+ engines (Google, Bing, DuckDuckGo, Wikipedia, etc.)
- Category-based search (general, images, videos, files, IT, science)
- JSON API for programmatic access
- Highly customizable and extensible

**TELOS Alignment Analysis**:
- **✅ Data Sovereignty**: ✅ **Self-hosted, no data leaves infrastructure**
- **✅ Open Source**: ✅ **AGPL-3.0 license**
- **✅ Local-First**: ✅ **Runs entirely on local infrastructure**
- **✅ Deterministic**: ✅ **Search results are deterministic**
- **✅ Observability**: ✅ **Full logging and query tracking**

**Integration with Current Setup**:
- ✅ **Already deployed** as `searxng` container (port 8081)
- ✅ Accessible at `http://ubuntu58-1:8081`
- ✅ Can be integrated via **custom MCP server** or **Fabric pattern**
- ✅ Fits perfectly into TELOS "Deterministic" layer

**Use Case**: **Primary search engine** for all web queries, providing sovereign and privacy-preserving search.

**Current Deployment Status**:
```yaml
container: searxng
port: 8081 (external)
url: http://ubuntu58-1:8081
status: ✅ Running
health_check: Available via web interface

configuration:
  search_engines: 70+ (Google, Bing, DuckDuckGo, Wikipedia, etc.)
  categories: general, images, videos, files, IT, science
  api_format: JSON
  rate_limiting: Built-in
```

**Enhancement Recommendations**:
1. **Create SearXNG MCP Server**: Wrap SearXNG JSON API as MCP tool for seamless integration
2. **Add Custom Engine Configurations**: Configure engines relevant to user's interests
3. **Implement Query Caching**: Cache common queries in Redis (already deployed)
4. **Add Result Ranking**: Implement custom result ranking based on user preferences

---

### 1.4 DuckDuckGo AI Search Assist - Privacy-Focused

**Overview**: DuckDuckGo's AI Search Assist provides AI-powered search with privacy protections.

**Key Features**:
- Privacy-focused (no tracking)
- AI-generated summaries
- Instant Answers integration
- Familiar search interface

**TELOS Alignment Analysis**:
- **✅ Data Sovereignty**: ⚠️ Privacy-focused but still external service
- **✅ Open Source**: ❌ Proprietary
- **✅ Local-First**: ❌ Cloud-based
- **✅ Deterministic**: ⚠️ Probabilistic (AI summaries)
- **✅ Observability**: ✅ Query logging possible

**Integration with Current Setup**:
- ✅ Available via **Brave Local Search MCP** (`brave-search_brave_local_search`)
- ⚠️ Can fall back to web search if no local results

**Use Case**: Good for **privacy-conscious quick searches** when SearXNG is unavailable.

---

### 1.5 Andi - Straightforward AI Search

**Overview**: Andi provides an easy-to-understand AI search interface for beginners.

**Key Features**:
- Simple, intuitive interface
- AI-powered search
- Beginner-friendly
- Similar experience to Bing/Google

**TELOS Alignment Analysis**:
- **✅ Data Sovereignty**: ❌ Commercial service
- **✅ Open Source**: ❌ Proprietary
- **✅ Local-First**: ❌ Cloud-based
- **✅ Deterministic**: ⚠️ Probabilistic (AI-powered)
- **✅ Observability**: ✅ Query logging available

**Integration with Current Setup**:
- ❌ Not currently integrated
- ⚠️ Could be integrated via API wrapper

**Use Case**: Good for **simpler queries** when other search engines are unavailable.

---

## Part 2: Deep Research Tools

### 2.1 Undermind.ai - Academic Research Assistant

**Overview**: Undermind is an AI-powered personal research assistant that reads relevant literature, generates custom tables, traces citations, and notifies of relevant new publications.

**Key Features**:
- AI expert that has read relevant literature
- Custom table generation for research support
- In-line citation tracing to source papers
- Sortable and filterable results
- Notifications for relevant new publications

**TELOS Alignment Analysis**:
- **✅ Data Sovereignty**: ❌ Commercial service (external servers)
- **✅ Open Source**: ❌ Proprietary
- **✅ Local-First**: ❌ Cloud-based
- **✅ Deterministic**: ⚠️ Probabilistic (AI-powered analysis)
- **✅ Observability**: ✅ Citation tracking and research history

**Integration with Current Setup**:
- ❌ Not currently integrated
- ⚠️ Could be integrated via **custom Fabric pattern**
- ⚠️ Requires API key management

**Use Case**: Ideal for **academic research** and **literature review** tasks requiring paper-level analysis.

**Deployment Considerations**:
```yaml
resource_usage:
  cpu: Low (API calls only)
  memory: Low (API client only)
  network: Moderate (external API calls)
  
integration_points:
  - Fabric: Pattern for Undermind-powered literature review
  - OpenMemory: Store research results with citations
  - Hugo: Automatically publish research findings as blog posts

latency: 1-3 seconds per query
rate_limits: Check API documentation
```

---

### 2.2 Glean - Enterprise Work AI

**Overview**: Glean is a Work AI platform connected to enterprise data, enabling finding, creating, and automating anything.

**Key Features**:
- Enterprise data integration
- Knowledge base search
- Task automation
- Document discovery
- Collaboration features

**TELOS Alignment Analysis**:
- **✅ Data Sovereignty**: ⚠️ Self-hosted enterprise option available
- **✅ Open Source**: ❌ Proprietary (enterprise)
- **✅ Local-First**: ✅ Self-hosted option
- **✅ Deterministic**: ✅ Enterprise search is deterministic
- **✅ Observability**: ✅ Enterprise logging and analytics

**Integration with Current Setup**:
- ❌ Not currently deployed
- ⚠️ Overkill for **personal AI assistant** use case
- ⚠️ Better suited for **enterprise** environments

**Use Case**: Good for **enterprise knowledge management** but excessive for personal infrastructure.

---

## Part 3: AI Agent Frameworks

### 3.1 AutoGPT - Autonomous Agent Framework

**Overview**: AutoGPT is an autonomous agent framework that turns GPT chatbots into self-planning, goal-driven assistants.

**Key Features**:
- Autonomous task planning
- Self-directed goal pursuit
- Multi-step reasoning
- Tool integration
- Reward-based learning

**TELOS Alignment Analysis**:
- **✅ Data Sovereignty**: ✅ **Self-hosted, local execution**
- **✅ Open Source**: ✅ **MIT license, active community**
- **✅ Local-First**: ✅ **Runs entirely locally**
- **✅ Deterministic**: ⚠️ Probabilistic (LLM-powered planning)
- **✅ Observability**: ✅ **Full logging of thoughts and actions**

**Integration with Current Setup**:
- ✅ Already available in `/media/docker/auto-gpt/` (if deployed)
- ✅ Fits perfectly into TELOS "Orchestration" layer
- ✅ Can integrate with **existing MCP servers** (SearXNG, OpenMemory, Fabric)
- ✅ Supports **local LLMs** (z.ai 4.7 Flash)

**Use Case**: **Autonomous multi-step workflows** requiring planning and goal pursuit.

**Current Deployment Status**:
```yaml
container: auto-gpt (if deployed)
status: Check docker ps
resource_requirements:
  cpu: Moderate (LLM inference)
  memory: High (8GB shared, allocate carefully)
  storage: Moderate (state persistence)

integration_points:
  - MCP: All available tools (SearXNG, OpenMemory, Fabric)
  - OpenCode: Task delegation and orchestration
  - Fabric: Pattern-based task decomposition
```

**Enhancement Recommendations**:
1. **Deploy AutoGPT Container**: Set up AutoGPT in Docker with local LLM backend
2. **Create AutoGPT MCP Integration**: Expose AutoGPT as MCP tool for seamless integration
3. **Implement Deterministic Workflows**: Wrap AutoGPT in deterministic patterns for specific tasks
4. **Add Observability**: Log all AutoGPT thoughts and actions to OpenMemory

---

### 3.2 Atomic Agents - Multi-Agent Library

**Overview**: Atomic Agents is an open-source library designed to simplify creation of multi-agent systems with distributed agents for tailored applications.

**Key Features**:
- Simplified multi-agent creation
- Distributed agent architecture
- Tailored agent specialization
- Easy agent composition
- Modular design

**TELOS Alignment Analysis**:
- **✅ Data Sovereignty**: ✅ **Self-hosted, local execution**
- **✅ Open Source**: ✅ **Open-source license**
- **✅ Local-First**: ✅ **Runs entirely locally**
- **✅ Deterministic**: ✅ **Agent composition is deterministic**
- **✅ Observability**: ✅ **Agent logging and state tracking**

**Integration with Current Setup**:
- ❌ Not currently deployed
- ✅ Fits perfectly into TELOS "Orchestration" layer
- ✅ Can integrate with **existing MCP servers**
- ✅ Supports **local LLMs**

**Use Case**: **Multi-agent systems** requiring specialized agent collaboration.

**Deployment Considerations**:
```yaml
resource_requirements:
  cpu: Moderate (multi-agent orchestration)
  memory: High (multiple agent states)
  storage: Moderate (agent persistence)

integration_points:
  - MCP: All available tools
  - OpenCode: Multi-agent coordination
  - Fabric: Agent specialization patterns

latency: Depends on task complexity
scalability: Supports distributed agents
```

**Enhancement Recommendations**:
1. **Deploy Atomic Agents**: Set up Atomic Agents library in Python container
2. **Create Specialized Agents**: Build domain-specific agents (search, research, writing, automation)
3. **Implement Agent Communication**: Set up inter-agent communication via Redis (already deployed)
4. **Add Observability**: Log all agent interactions to OpenMemory

---

### 3.3 Botpress - AI Agent Framework Platform

**Overview**: Botpress is an AI agent framework platform that scales to research experiments, human-in-the-loop processes, and autonomous workflows.

**Key Features**:
- Low-code + code options
- Scales to research experiments
- Human-in-the-loop processes
- Autonomous workflows
- Tracks agent reasoning end-to-end

**TELOS Alignment Analysis**:
- **✅ Data Sovereignty**: ✅ **Self-hosted options available**
- **✅ Open Source**: ✅ **Open-source community edition**
- **✅ Local-First**: ⚠️ Self-hosted option available
- **✅ Deterministic**: ✅ **Workflows are deterministic**
- **✅ Observability**: ✅ **End-to-end reasoning tracking**

**Integration with Current Setup**:
- ❌ Not currently deployed
- ⚠️ Overkill for **personal AI assistant** use case
- ⚠️ Better suited for **enterprise** or **research** environments

**Use Case**: Good for **complex workflow automation** and **research experiments** but excessive for personal infrastructure.

---

## Part 4: Current Environment Analysis

### 4.1 TELOS Infrastructure Overview

The current environment follows **TELOS principles** with a focus on **data sovereignty**, **open source**, and **local-first** design.

**Core Principles**:
1. **Data Sovereignty First** ✅: Self-hosted infrastructure is default
2. **Open Source by Default** ✅: Prefer open-source alternatives
3. **Local-First AI** ✅: Local LLM inference via z.ai 4.7 Flash
4. **Deterministic Over Probabilistic** ✅: Prefer deterministic workflows
5. **Observability** ✅: Comprehensive logging and monitoring

### 4.2 Current Technical Stack

**Infrastructure**:
- **Host OS**: Ubuntu VPS (8GB RAM, ~80 containers)
- **Containerisation**: Docker (highly tuned, compose-based)
- **Networking**: Tailscale mesh network
- **Reverse Proxy**: Traefik/Caddy (service discovery, SSL)

**Knowledge Management**:
- **Notes**: Memos (http://ubuntu58-1:5230)
- **Static Sites**: Hugo (http://ubuntu58-1:1314)
- **Library**: Kavita (http://ubuntu58-1:5000)
- **Memory**: OpenMemory (http://ubuntu58-1:8080)

**Integration Layer**:
- **MCP Servers**: 10+ active servers (SearXNG, Crawl4AI, OpenMemory, Hugo, etc.)
- **Fabric**: Pattern library and skills management
- **APIs**: Document conversion, data transformation
- **Webhooks**: Event-driven automation

**Search Capabilities (Current)**:
- ✅ **SearXNG** (self-hosted meta-search)
- ✅ **Brave Web Search MCP** (external augmentation)
- ✅ **Google Search MCP** (external augmentation)
- ✅ **Crawl4AI** (web scraping and extraction)
- ✅ **Exa Code Context** (code search via Exa.ai API)

**Observability**:
- **OpenTelemetry Collector** (http://ubuntu58-1:4567)
- **Grafana** (http://ubuntu58-1:3003)
- **Jaeger** (http://ubuntu58-1:16686)
- **Prometheus** (via node-exporter)
- **cAdvisor** (http://ubuntu58-1:8083)

### 4.3 Resource Constraints

**Current Constraints**:
```yaml
memory:
  total: 8GB
  allocated: ~6GB across 80 containers
  available: ~2GB for new services
  
cpu:
  cores: 4 (unspecified, typical for 8GB VPS)
  utilization: ~60-70% average
  
storage:
  capacity: Sufficient (not specified)
  usage: High (many containers and data stores)
  
network:
  bandwidth: Standard VPS tier
  latency: Low (local services)
```

**Critical Consideration**: Adding new services requires careful resource allocation and potential container consolidation.

---

## Part 5: Integration Recommendations

### 5.1 Proposed Search Architecture

{{< mermaid >}}
graph TD
    A[User Query] --> B{Query Type?}
    B -->|General Web Search| C[SearXNG - Self-Hosted]
    B -->|Complex Research| D[Exa.ai API - Augmentation]
    B -->|Academic Papers| E[Undermind.ai API]
    B -->|Privacy Critical| F[Brave Local Search]
    B -->|Code Search| G[Exa Code Context]
    
    C --> H[Result Ranking]
    D --> H
    E --> H
    F --> H
    G --> H
    
    H --> I[OpenMemory Storage]
    I --> J[Fabric Pattern Processing]
    J --> K[Formatted Output]
    
    style C fill:#90EE90
    style D fill:#FFD700
    style E fill:#FFD700
    style F fill:#FFD700
    style G fill:#FFD700
    style I fill:#ADD8E6
    style J fill:#ADD8E6
{{< /mermaid >}}

**Architecture Explanation**:

1. **Primary Search Layer (Deterministic)**: **SearXNG** (self-hosted)
   - Handles all general web searches
   - Privacy-preserving, sovereign
   - Fits TELOS "Deterministic" layer

2. **Augmentation Layer (Probabilistic)**: **External APIs** (Exa.ai, Undermind, Brave)
   - Handles complex research, academic papers, specialized queries
   - Used only when SearXNG is insufficient
   - Fits TELOS "Probabilistic" layer

3. **Specialized Search**: **Code Context** (Exa Code Context)
   - Handles code-related searches
   - Already integrated as MCP tool
   - Fits TELOS "Orchestration" layer

4. **Knowledge Storage**: **OpenMemory**
   - Stores all search results with metadata
   - Enables semantic retrieval and citation tracking
   - Fits TELOS "Capture → Process → Store" architecture

5. **Processing Layer**: **Fabric Patterns**
   - Transforms raw search results into formatted output
   - Extracts insights, summaries, and recommendations
   - Fits TELOS "Process" architecture

---

### 5.2 Implementation Roadmap

#### Phase 1: Optimize Current Setup (Week 1-2)

**Task 1.1: Create SearXNG MCP Server**
```bash
# Create MCP server for SearXNG integration
cd /media/docker
mkdir -p searxng-mcp

# Create MCP server configuration
cat > searxng-mcp/config.json << 'EOF'
{
  "name": "searxng-mcp",
  "version": "1.0.0",
  "description": "SearXNG self-hosted meta-search MCP server",
  "endpoints": [
    {
      "name": "searxng_search",
      "method": "GET",
      "path": "/search",
      "description": "Search SearXNG with query"
    },
    {
      "name": "searxng_categories",
      "method": "GET",
      "path": "/categories",
      "description": "List available search categories"
    }
  ]
}
EOF

# Create Python MCP server implementation
cat > searxng-mcp/server.py << 'EOF'
# SearXNG MCP Server Implementation
import httpx
from mcp.server import Server

app = Server("searxng-mcp")

@app.tool()
async def searxng_search(query: str, category: str = "general") -> str:
    """Search SearXNG with query"""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "http://localhost:8081/search",
            params={"q": query, "format": "json", "categories": category}
        )
        return response.text

@app.tool()
async def searxng_categories() -> str:
    """List available search categories"""
    return ["general", "images", "videos", "files", "it", "science"]
EOF
```

**Task 1.2: Integrate SearXNG into Fabric Patterns**
```bash
# Create Fabric pattern for SearXNG-powered search
mkdir -p /root/.config/fabric/patterns/searxng-search

cat > /root/.config/fabric/patterns/searxng-search/system.md << 'EOF'
# SearXNG Search Pattern

You are a sovereign search assistant using SearXNG (self-hosted meta-search).

## Instructions:
1. Search SearXNG for the user's query
2. Aggregate results from multiple engines (Google, Bing, DuckDuckGo, etc.)
3. Rank results by relevance and quality
4. Present top 10 results with:
   - Title
   - URL
   - Snippet
   - Source engine
5. Store results in OpenMemory with metadata

## Privacy Principles:
- No tracking or logging
- Self-hosted, no data leaves infrastructure
- Anonymous search queries

## Success Criteria:
- 10 relevant results with citations
- Results ranked by quality and relevance
- Metadata stored in OpenMemory
EOF
```

**Task 1.3: Add SearXNG to Global Instructions**
```bash
# Update global-instructions.md with SearXNG as primary search
cat >> /media/docs/instructions/global-instructions.md << 'EOF'

## Search Protocol

### Primary Search: SearXNG (Self-Hosted)
- **URL**: http://ubuntu58-1:8081
- **Purpose**: Primary search engine for all web queries
- **TELOS Alignment**: ✅ Self-hosted, sovereign, deterministic
- **MCP Server**: searxng-mcp (to be created)

### Augmentation Layer: External APIs (Use Sparingly)
- **Exa.ai**: Complex research requiring AI-powered analysis
- **Undermind.ai**: Academic research and literature review
- **Brave Search**: Privacy-focused quick searches
- **Google Search**: Backup when other sources fail

### Search Decision Matrix:
1. **General web search** → SearXNG (primary)
2. **Complex research** → Exa.ai API (augmentation)
3. **Academic papers** → Undermind.ai (specialized)
4. **Code search** → Exa Code Context MCP
5. **Privacy critical** → Brave Local Search
EOF
```

#### Phase 2: Deploy AI Agent Framework (Week 3-4)

**Task 2.1: Deploy AutoGPT**
```bash
# Create AutoGPT container setup
cd /media/docker
mkdir -p auto-gpt

# Create docker-compose.yml
cat > auto-gpt/docker-compose.yml << 'EOF'
version: '3.8'

services:
  auto-gpt:
    image: sigmasolutions/auto-gpt:latest
    container_name: auto-gpt
    restart: unless-stopped
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - LLM_PROVIDER=openai
      - TEMPERATURE=0.7
      - FAST_LLM=llama-3-8b
      - SMART_LLM=llama-3-70b
    volumes:
      - ./data:/app/auto_gpt_workspace
      - ./logs:/app/logs
    ports:
      - "8000:8000"
    networks:
      - openmemory-network
    depends_on:
      - redis

networks:
  openmemory-network:
    external: true
EOF

# Deploy AutoGPT
cd auto-gpt
docker-compose up -d
```

**Task 2.2: Create AutoGPT Fabric Pattern**
```bash
# Create Fabric pattern for AutoGPT task delegation
mkdir -p /root/.config/fabric/patterns/autogpt-delegate

cat > /root/.config/fabric/patterns/autogpt-delegate/system.md << 'EOF'
# AutoGPT Task Delegation Pattern

You are a task orchestrator that delegates complex multi-step workflows to AutoGPT.

## Instructions:
1. Analyze the user's request for complexity
2. If task requires multi-step planning and goal pursuit:
   a. Decompose task into sub-goals
   b. Create AutoGPT task specification
   c. Delegate to AutoGPT via MCP server
   d. Monitor AutoGPT execution
   e. Retrieve results and format for user
3. If task is simple, execute directly

## AutoGPT Integration:
- **URL**: http://ubuntu58-1:8000
- **MCP Server**: autogpt-mcp (to be created)
- **Use Cases**: Autonomous multi-step workflows, goal pursuit

## Success Criteria:
- Task decomposed into actionable sub-goals
- AutoGPT executes tasks autonomously
- Results retrieved and formatted for user
- All actions logged to OpenMemory
EOF
```

#### Phase 3: Deep Research Integration (Week 5-6)

**Task 3.1: Create Undermind.ai Fabric Pattern**
```bash
# Create Fabric pattern for Undermind-powered research
mkdir -p /root/.config/fabric/patterns/undermind-research

cat > /root/.config/fabric/patterns/undermind-research/system.md << 'EOF'
# Undermind Research Pattern

You are an academic research assistant using Undermind.ai for literature review.

## Instructions:
1. Understand the user's research question
2. Query Undermind.ai for relevant academic papers
3. Extract key findings, methodologies, and conclusions
4. Generate custom research tables comparing papers
5. Trace citations to source papers
6. Format results as:
   - Executive summary
   - Detailed paper analysis
   - Comparison tables
   - Citation list

## Undermind Integration:
- **API**: Undermind.ai API (key required)
- **Use Cases**: Academic research, literature review, paper analysis

## Success Criteria:
- 10-20 relevant academic papers
- Custom research tables comparing methodologies
- In-line citations to source papers
- Results stored in OpenMemory
EOF
```

**Task 3.2: Integrate with Auto-Publish Workflow**
```bash
# Create workflow that publishes research as blog post
cat > /media/docs/output/auto-research-to-blog.sh << 'EOF'
#!/bin/bash

# Auto-Research-to-Blog Workflow
# Uses Fabric patterns to research and publish as Hugo blog post

RESEARCH_TOPIC="$1"

if [[ -z "$RESEARCH_TOPIC" ]]; then
  echo "Usage: $0 'research topic'"
  exit 1
fi

echo "📚 Researching: $RESEARCH_TOPIC"
echo "🔍 Using Undermind.ai for academic search..."
echo "📝 Creating comprehensive research document..."
echo "🚀 Publishing as Hugo blog post..."

# Execute Fabric pattern for research
RESEARCH_OUTPUT=$(fabric --pattern undermind-research "$RESEARCH_TOPIC")

# Create Hugo post via hugo-task
POST_TITLE="Research: $RESEARCH_TOPIC"
POST_SLUG=$(echo "$POST_TITLE" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd 'a-z0-9-')

# Create post file
hugo-task create "$POST_TITLE" --categories="Research" --draft=false

# Add research content
POST_FILE="/media/docker/website/content/posts/$(date +%Y-%m-%d)-$POST_SLUG.md"
echo "$RESEARCH_OUTPUT" >> "$POST_FILE"

echo "✅ Research published: http://ubuntu58-1:1314/$(date +%Y)/$(date +%m)/$(date +%d)/$POST_SLUG/"
EOF

chmod +x /media/docs/output/auto-research-to-blog.sh
```

---

### 5.3 Resource Optimization Strategy

**Current Resource Challenge**: 8GB RAM shared across ~80 containers is near capacity.

**Optimization Strategy**:

1. **Container Consolidation**:
   ```yaml
   priority_containers:
     - hugo_site: Critical (blog publishing)
     - openmemory: Critical (knowledge storage)
     - memos: Critical (note-taking)
     - searxng: Critical (sovereign search)
     - openllmetry: Critical (monitoring)
   
   low_priority_containers:
     - astro-fresh: Can sleep
     - ai-consultancy-v2: Can sleep
     - slidev_presentations: Can sleep
   
   strategy: Sleep low-priority containers during resource-intensive tasks
   ```

2. **AutoGPT Resource Allocation**:
   ```yaml
   autogpt_resource_profile:
     cpu: 1-2 cores (25-50%)
     memory: 512MB-1GB
     storage: 500MB
   
   deployment:
     - Run only when needed (on-demand)
     - Auto-sleep after task completion
     - Wake via Fabric pattern or MCP trigger
   ```

3. **SearXNG Optimization**:
   ```yaml
   searxng_resource_profile:
     cpu: 1 core (25%)
     memory: 256MB
     caching: Redis integration
   
   optimization:
     - Enable result caching in Redis (already deployed)
     - Rate limit external search engines
     - Prune low-quality engines
   ```

---

## Part 6: Final Recommendations

### 6.1 Recommended Stack

Based on TELOS alignment, current infrastructure, and resource constraints, the **recommended search stack** is:

| Layer | Solution | TELOS Alignment | Priority |
|-------|----------|------------------|-----------|
| **Primary Search** | **SearXNG** (self-hosted) | ✅ **Perfect** | P0 (Implement immediately) |
| **Augmentation** | **Exa.ai API** (complex research) | ⚠️ Good | P1 (Implement Q1) |
| **Academic Research** | **Undermind.ai** (literature review) | ⚠️ Good | P2 (Implement Q2) |
| **Code Search** | **Exa Code Context MCP** | ✅ Good | P0 (Already integrated) |
| **Agent Orchestration** | **AutoGPT** (multi-step workflows) | ✅ **Perfect** | P1 (Implement Q1) |

### 6.2 Implementation Priority

**P0 - Immediate (This Week)**:
1. ✅ Create **SearXNG MCP Server** for seamless integration
2. ✅ Add **SearXNG Fabric Pattern** for standardized search
3. ✅ Update **global-instructions.md** with search protocol
4. ✅ Create **SearXNG monitoring dashboard** in Grafana

**P1 - Short-Term (Next 4 Weeks)**:
1. Deploy **AutoGPT** container with resource constraints
2. Create **AutoGPT MCP Server** for task delegation
3. Add **AutoGPT Fabric Pattern** for autonomous workflows
4. Integrate **Exa.ai API** as augmentation layer
5. Create **exa-research Fabric Pattern** for complex queries

**P2 - Medium-Term (Next 8 Weeks)**:
1. Integrate **Undermind.ai API** for academic research
2. Create **undermind-research Fabric Pattern**
3. Implement **auto-research-to-blog workflow**
4. Add **research result storage** in OpenMemory
5. Create **research analytics dashboard**

### 6.3 TELOS Compliance Scorecard

| Solution | Data Sovereignty | Open Source | Local-First | Deterministic | Observability | Total Score |
|----------|-----------------|-------------|-------------|---------------|----------------|-------------|
| **SearXNG** | ✅ 5 | ✅ 5 | ✅ 5 | ✅ 5 | ✅ 5 | **25/25** |
| **AutoGPT** | ✅ 5 | ✅ 5 | ✅ 5 | ⚠️ 3 | ✅ 5 | **23/25** |
| **Exa.ai API** | ⚠️ 2 | ❌ 0 | ❌ 0 | ⚠️ 3 | ✅ 4 | **9/25** |
| **Undermind.ai** | ⚠️ 2 | ❌ 0 | ❌ 0 | ⚠️ 3 | ✅ 4 | **9/25** |
| **Brave Search** | ⚠️ 3 | ❌ 0 | ❌ 0 | ⚠️ 3 | ✅ 4 | **10/25** |

**Key Insight**: **SearXNG** and **AutoGPT** are the only solutions with perfect or near-perfect TELOS alignment. External APIs (Exa.ai, Undermind.ai) are valuable as **augmentation layers** but should not replace self-hosted solutions.

---

## Conclusion

This comprehensive analysis reveals that the current TELOS-based infrastructure is well-positioned to implement a sovereign, open-source AI assistant ecosystem with powerful search and research capabilities.

### Key Findings:

1. **SearXNG** is already deployed and perfectly aligned with TELOS principles
2. **AutoGPT** provides autonomous multi-agent orchestration with high TELOS alignment
3. **External APIs** (Exa.ai, Undermind.ai) are valuable as augmentation layers
4. **Current resource constraints** require careful optimization and container consolidation
5. **Integration with OpenMemory and Fabric** provides a complete "Capture → Process → Store → Surface → Act" pipeline

### Recommended Next Steps:

1. **Create SearXNG MCP Server** (immediate)
2. **Deploy AutoGPT** with resource constraints (next 4 weeks)
3. **Integrate External APIs** as augmentation layer (next 8 weeks)
4. **Optimize Resource Usage** via container consolidation (ongoing)
5. **Monitor and Iterate** via OpenTelemetry and Grafana (continuous)

By following this roadmap, the infrastructure will evolve into a truly sovereign, local-first AI assistant ecosystem that maintains data ownership while leveraging powerful AI capabilities through deterministic workflows and probabilistic augmentation layers.

---

## References

- **TELOS Constitution**: `/media/docs/instructions/telos.md`
- **Global Instructions**: `/media/docs/instructions/global-instructions.md`
- **SearXNG Documentation**: https://docs.searxng.org/
- **Exa.ai API**: https://docs.exa.ai/
- **Undermind.ai**: https://www.undermind.ai/
- **AutoGPT**: https://github.com/Significant-Gravitas/Auto-GPT
- **Atomic Agents**: https://www.shakudo.io/blog/top-9-ai-agent-frameworks

---

*Published: February 8, 2026*  
*Analysis based on TELOS infrastructure principles and current deployment status*