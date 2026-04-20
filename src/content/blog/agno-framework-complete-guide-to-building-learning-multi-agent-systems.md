---
pubDatetime: 2026-02-07T14:45:26Z
title: "Agno Framework: Complete Guide to Building Learning Multi-Agent Systems"
postSlug: "agno-framework-complete-guide-to-building-learning-multi-agent-systems"
description: "Agno Framework: Complete Guide to Building Learning Multi-Agent Systems"
tags:
  - multi-agent
  - framework
  - ai-agents
  - agentos
  - agno
  - python
---

# Agno Framework: Complete Guide to Building Learning Multi-Agent Systems

**Agno** (formerly **Phidata**) is an open-source Python framework for building multi-agent systems that learn and improve with every interaction. It provides a complete production stack including a framework for building agents, a runtime for deployment, and a control plane for monitoring and management.

**Key Stats:**
- **GitHub Stars:** 37.6k (as of Feb 2026)
- **Forks:** 5k+
- **Contributors:** 399
- **License:** Apache-2.0
- **Primary Language:** Python (99.7%)
- **Latest Release:** v2.4.8 (Feb 3, 2026)

---

## What Makes Agno Different?

### Core Philosophy
Most AI agents are **stateless** - they reason, respond, and forget. Session history helps, but they're exactly as capable on day 1000 as they were on day 1.

**Agno agents are different:**
- ✅ Remember users across sessions
- ✅ Accumulate knowledge across conversations
- ✅ Learn from decisions
- ✅ Share insights across users (the system gets smarter over time)
- ✅ Everything runs in **your cloud** (data never leaves your environment)

---

## Architecture Overview

Agno provides a **complete infrastructure** for building multi-agent systems:

### Three-Layer Stack

| Layer | What It Does | Components |
|--------|--------------|-------------|
| **Framework** | Build agents with learning, tools, knowledge, and guardrails | Agents, Teams, Workflows, Models, Tools |
| **Runtime** | Run agents in production | AgentOS Runtime (FastAPI-based API layer) |
| **Control Plane** | Monitor and manage deployments | AgentOS UI (Web dashboard at os.agno.com) |

---

## Core Features & Capabilities

### 1. Learning & Memory

```python
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIResponses

agent = Agent(
    model=OpenAIResponses(id="gpt-5.2"),
    db=SqliteDb(db_file="tmp/agents.db"),
    learning=True,  # ← One line enables learning!
)
```

**Features:**
- **User Profiles** - Persist across sessions
- **User Memories** - Accumulate over time
- **Learned Knowledge** - Transfers across users
- **Learning Modes** - Always or agentic

### 2. Model Agnostic

Supports 40+ model providers with **one-line swap**:

```python
# OpenAI
from agno.models.openai import OpenAIChat
model = OpenAIChat(id="gpt-5.2")

# Anthropic
from agno.models.anthropic import Claude
model = Claude(id="claude-sonnet-4-5")

# Google
from agno.models.google import Gemini
model = Gemini(id="gemini-3-flash-preview")

# Local (Ollama, vLLM, etc.)
from agno.models.ollama import OllamaChat
model = OllamaChat(id="llama3")
```

### 3. Type-Safe I/O

```python
from pydantic import BaseModel

class UserInput(BaseModel):
    name: str
    age: int

class AgentResponse(BaseModel):
    greeting: str
    personalized_message: str

agent = Agent(
    model=model,
    input_schema=UserInput,
    output_schema=AgentResponse,
)
```

### 4. Async-First

Built for long-running tasks with **unified API**:
- Same agent for sync & async
- Minimal code changes
- No event loop headaches
- High performance

### 5. Multimodal by Default

Natively handles:
- ✅ Text
- ✅ Images
- ✅ Audio
- ✅ Video
- ✅ Files

---

## Key Components

### Agents (The Atomic Unit)
The foundation of Agno - single AI agent with tools, memory, knowledge, and learning.

**Capabilities:**
- Tool calling (100+ built-in tools)
- RAG with 20+ vector stores
- Structured outputs
- Session persistence
- Guardrails & validation
- Human-in-the-loop

### Teams (Multi-Agent Coordination)

Coordinate multiple specialized agents:

```python
from agno.team import Team

hn_researcher = Agent(name="HackerNews Researcher", tools=[HackerNewsTools()])
article_reader = Agent(name="Article Reader", tools=[Newspaper4kTools()])

team = Team(
    model=Claude(id="claude-sonnet-4-5"),
    members=[hn_researcher, article_reader],
)

team.print_response("Research AI trends and summarize")
```

**Modes:**
- **Coordinate** - Orchestrated collaboration
- **Route** - Dynamic task routing
- **Consensus** - Agreement-based decisions

### Workflows (Process Orchestration)

Chain agents, teams, and functions into automated pipelines:

```python
from agno.workflow import Workflow

researcher = Agent(name="Researcher", tools=[DuckDuckGoTools()])
writer = Agent(name="Writer", instructions="Write engaging content")

workflow = Workflow(
    name="Content Workflow",
    steps=[researcher, writer],
)

workflow.print_response("Create a blog post", stream=True)
```

### AgentOS (Production Runtime)

Turn agents into production infrastructure:

```python
from agno.os import AgentOS

agent_os = AgentOS(
    description="Powerful Agent System",
    agents=[knowledge_agent, support_agent],
    teams=[research_team],
    workflows=[social_media_workflow],
    interfaces=[Slack(), AISdk(), AGUI()],
)

app = agent_os.get_app()  # FastAPI ready to deploy
```

**Deployment Interfaces:**
- Web APIs
- Slack
- WhatsApp
- Discord
- AGUI (custom interface)

---

## Knowledge & RAG

### Agentic RAG

Advanced retrieval with multiple strategies:

**Chunking Strategies:**
- Semantic
- Recursive
- Agentic

**Hybrid Search:**
- Vector search
- Keyword search
- Reranking

**Vector Stores (20+):**
- LanceDB, Pgvector, Pinecone, Qdrant
- SingleStore, SurrealDB, MongoDB, Redis
- And more...

**Data Sources:**
- URLs
- S3
- Google Cloud Storage
- YouTube
- PDFs
- And more...

---

## Tools & Integrations

### 100+ Built-in Toolkits
- **Web Search:** DuckDuckGo, Tavily, Exa
- **Social:** Discord, Slack, HackerNews
- **Data:** SQL, CSV, Excel
- **Email:** Gmail, SMTP
- **Files:** S3, GCS, local files
- **Finance:** YFinance
- **Custom:** Use `@tool` decorator

```python
from agno.tools import tool

@tool
def get_weather(location: str) -> str:
    """Get current weather for a location."""
    # Implementation here
    return "Weather data..."

agent = Agent(tools=[get_weather])
```

### Observability Integrations
- Langfuse
- Arize Phoenix
- AgentOps
- LangSmith
- And more...

### MCP & A2A Support
First-class support for:
- **MCP** (Model Context Protocol)
- **A2A** (Agent-to-Agent communication)

---

## Security & Guardrails

### Built-in Safety Features

```python
from agno.guardrails import Guardrail

agent = Agent(
    model=model,
    guardrails=[
        Guardrail(type="pii", action="block"),  # Block PII
        Guardrail(type="prompt_injection", action="sanitize"),
    ],
)
```

**Capabilities:**
- PII detection
- Prompt injection prevention
- Input validation
- Output filtering
- Custom safety rules

### Human-in-the-Loop

Require user confirmation for sensitive operations:

```python
agent = Agent(
    model=model,
    tools=[sensitive_tools],
    human_confirmation=True,  # Require approval
)
```

---

## Production & Deployment

### AgentOS Runtime

Production-ready API layer built on **FastAPI**:

**Features:**
- Secure sandboxed execution
- Performance monitoring
- Token usage tracking
- Latency monitoring
- Error rate tracking

### AgentOS Control Plane

Web-based management interface (os.agno.com):

**Capabilities:**
- Chat with agents
- View execution traces
- Manage knowledge bases
- Monitor memories
- Track performance metrics
- Session management

### Deployment Options

**Local Development:**
```bash
python cookbook/00_quickstart/run.py
# Visit os.agno.com and add http://localhost:7777
```

**Cloud Deployment:**
- Docker (recommended)
- Kubernetes
- AWS / Azure / GCP
- Cloud platforms (TrueFoundry, etc.)

**Environment Variables:**
```bash
export AGNO_API_KEY=your_api_key
export AGNO_RUNTIME_URL=http://your-runtime-url.com
```

---

## Evaluation & Testing

### Built-in Evals Framework

**Metrics:**
- **Accuracy** - LLM-as-judge
- **Performance** - Latency, memory
- **Reliability** - Expected tool calls
- **Agent-as-judge** patterns

```python
from agno.evals import Eval

eval = Eval(
    agent=agent,
    dataset=test_data,
    metrics=["accuracy", "latency"],
)

results = eval.run()
print(results)
```

---

## Installation & Setup

### Quick Start

```bash
# Clone repo
git clone https://github.com/agno-agi/agno.git
cd agno

# Create virtual environment
uv venv .quickstart --python 3.12
source .quickstart/bin/activate

# Install dependencies
uv pip install -r cookbook/00_quickstart/requirements.txt

# Set API key
export GOOGLE_API_KEY=your-key

# Run example
python cookbook/00_quickstart/agent_with_tools.py
```

### Installation

```bash
pip install -U agno
```

---

## Cookbook Structure

The repository includes **hundreds of examples** organized by category:

### Quick Start (00_quickstart)
12 examples covering fundamentals:
1. Tools and data fetching
2. Structured output
3. Typed I/O
4. Storage (conversation persistence)
5. Memory (user preferences)
6. State management
7. Knowledge base with hybrid search
8. Custom tools
9. Guardrails
10. Human-in-the-loop
11. Multi-agent teams
12. Sequential workflows

### Advanced Topics (02-93)
- **02_agents** - Advanced agent patterns (async, RAG, multimodal)
- **03_teams** - Multi-agent coordination
- **04_workflows** - Complex process orchestration
- **05_agent_os** - Deployment & management
- **06_storage** - Persistent storage (Postgres, SQLite, etc.)
- **07_knowledge** - RAG implementation
- **08_learning** - Learning systems
- **09_evals** - Testing & evaluation
- **10_reasoning** - Advanced reasoning (o1, o3, etc.)
- **80_memory** - User memory systems
- **90_models** - 40+ model providers
- **91_tools** - Tool integrations
- **92_integrations** - Platform integrations

---

## Evolution from Phidata to Agno

### Key Improvements (2025 Transition)

| Aspect | Phidata (Legacy) | Agno (Current) |
|---------|-------------------|-----------------|
| **Focus** | LLM Assistants | Multi-Agent Teams & Runtime |
| **Speed** | Fast | High-Performance Runtime |
| **Infrastructure** | Manual Setup | **AgentOS** (Automated) |
| **Data Types** | Primarily Text | **Multimodal** (Video/Audio/Images) |
| **Interface** | CLI/Simple UI | **AG-UI** & Dashboards |
| **API** | `phidata` namespace | `agno` namespace |

### Migration

Minimal code changes required - mostly namespace updates:

```python
# Old (Phidata)
from phidata.agent import Agent

# New (Agno)
from agno.agent import Agent
```

---

## Use Cases

### 1. Deep Research Agent
Autonomous research with web search, analysis, and report generation.

### 2. Customer Support Team
Multi-agent system with specialized agents for different domains.

### 3. Content Creation Pipeline
Workflows for research, drafting, editing, and publishing.

### 4. Data Analysis Agents
Agents that query databases, analyze data, and generate reports.

### 5. Personal Assistant
Agent with memory, learning, and integration with tools (calendar, email, etc.).

---

## Strengths

1. **Learning System** - Agents improve over time (unique capability)
2. **Model Agnostic** - 40+ providers, easy swapping
3. **Production Ready** - AgentOS provides runtime + control plane
4. **Comprehensive Tooling** - 100+ tools, observability, RAG
5. **Type Safety** - Pydantic schemas for I/O
6. **Async First** - High performance for concurrent operations
7. **Multimodal** - Native support for images, audio, video
8. **Excellent Documentation** - Hundreds of examples, comprehensive docs
9. **Active Community** - 37.6k stars, 399 contributors
10. **Open Source** - Apache-2.0 license

---

## Considerations

1. **New Framework** - Relatively new (rebranded from Phidata in 2025)
2. **Learning Complexity** - Learning features require setup (database, schemas)
3. **Control Plane SaaS** - Primary control plane is hosted (though self-hosting possible)
4. **Rapid Evolution** - API changes as framework matures
5. **Python Only** - No TypeScript/JavaScript SDK yet

---

## Resources

- **Documentation:** https://docs.agno.com
- **GitHub:** https://github.com/agno-agi/agno
- **Cookbook:** https://github.com/agno-agi/agno/tree/main/cookbook
- **AgentOS UI:** https://os.agno.com
- **Community:** https://community.agno.com/
- **Discord:** https://www.agno.com/discord
- **X (Twitter):** https://x.com/AgnoAgi
- **YouTube:** https://agno.link/youtube

---

## Comparison with Other Frameworks

| Feature | Agno | LangChain | LangGraph | CrewAI |
|---------|-------|-----------|------------|---------|
| **Learning** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Model Agnostic** | ✅ 40+ | ✅ Many | ✅ Many | ✅ Many |
| **Production Runtime** | ✅ AgentOS | ❌ Manual | ❌ Manual | ❌ Manual |
| **Control Plane UI** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Type Safety** | ✅ Native | ⚠️ Limited | ⚠️ Limited | ⚠️ Limited |
| **Async First** | ✅ Yes | ⚠️ Mixed | ⚠️ Mixed | ⚠️ Mixed |
| **Multimodal** | ✅ Native | ⚠️ Limited | ⚠️ Limited | ⚠️ Limited |
| **Tools** | 100+ | 50+ | 30+ | 20+ |
| **RAG** | ✅ 20+ DBs | ✅ Vector stores | ✅ Vector stores | ⚠️ Limited |
| **MCP Support** | ✅ First-class | ⚠️ Experimental | ❌ No | ❌ No |
| **Open Source** | ✅ Apache 2.0 | ✅ MIT | ✅ MIT | ✅ MIT |

---

## Conclusion

**Agno** is a comprehensive, production-ready framework for building multi-agent systems with **unique learning capabilities** that set it apart from other frameworks. Its three-layer architecture (framework, runtime, control plane) provides everything needed to go from prototype to production.

**Best for:**
- Teams needing production-ready agent infrastructure
- Projects requiring learning/improvement over time
- Enterprises wanting full control (self-hosted, data stays in your cloud)
- Developers wanting type safety and async performance

**Not ideal for:**
- Simple chatbots (overkill)
- Quick prototypes (framework overhead)
- Non-Python projects (no TypeScript SDK yet)

The framework is mature, well-documented, and backed by an active community. The 2025 rebrand from Phidata to Agno represents a significant evolution toward enterprise-ready multi-agent systems.

---

*Research completed February 7, 2026*