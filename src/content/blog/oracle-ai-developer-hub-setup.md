---
pubDatetime: 2026-03-20T10:26:59Z
title: "Oracle AI Developer Hub - First Steps"
postSlug: "oracle-ai-developer-hub-setup"
description: "Oracle AI Developer Hub - First Steps"
tags:
  - agents
  - rag
  - development
  - oracle
  - ai
---

I recently stumbled upon Oracle's official AI Developer Hub repository and decided to take it for a spin. Here's what I've found and how far I've got.

## What is the Oracle AI Developer Hub?

The [oracle-ai-developer-hub](https://github.com/oracle-devrel/oracle-ai-developer-hub) is Oracle's official repository of technical resources for AI developers. It contains working examples, notebooks, and guides for building AI applications using Oracle AI Database (23ai/26ai) and OCI services.

The repository has 139 stars and 56 forks, with 490 commits from 16 contributors.

### What's Inside

The repository is well-structured with three main areas:

**Apps (7 total)**

- **FitTracker** - Gamified fitness platform using Oracle JSON Duality Views
- **agentic_rag** - Intelligent RAG system with multi-agent Chain of Thought reasoning
- **agent-reasoning** - Interactive demos for agent reasoning patterns
- **oci-generative-ai-jet-ui** - Full-stack app with Oracle JET UI
- **oracle-database-vector-search** - Vector search capabilities
- **ragcli** - CLI tool for RAG over documents
- **picooraclaw** - Pico ORA/C LAw integration

**Notebooks (24 total)**

The notebooks cover a wide range of topics:

- RAG implementation tutorials (zero-to-hero, with evals, hybrid search)
- Agent memory systems (filesystem vs database, Google integration)
- Reasoning pattern demonstrations (11 cognitive architectures)
- Oracle 26ai unique features
- Cross-cloud integrations (AWS Bedrock, Azure OpenAI)

**Guides (2 PDFs)**

- Enterprise AI agent architecture - Brain and backbone strategies
- Memory engineering for agents - The discipline behind memory augmentation

## Setting It Up

I cloned the repository and installed the development dependencies:

```bash
git clone https://github.com/oracle-devrel/oracle-ai-developer-hub.git
cd oracle-ai-developer-hub
pip install -r requirements-dev.txt
pre-commit install
```

The repo uses:

- **Ruff** for Python linting/formatting
- **Prettier** for JS/TS/JSON/YAML/MD files
- Standard pre-commit hooks

Pre-commit installed successfully and the hooks are now active.

## The Catch

Here's the reality check - this isn't a standalone project. To actually run most of the apps and notebooks, you need:

1. **Oracle 23ai/26ai Database** - The vector search and AI features require Oracle's latest database releases
2. **OCI Account** - For Generative AI service access
3. **App-specific dependencies** - Each app has its own requirements.txt

When I tried to install the `agentic_rag` app dependencies, the full requirements list includes:

- langchain-oracledb
- chromadb
- torch
- sentence-transformers
- docling
- ollama

These are heavy packages, and without an Oracle database, they're pretty useless for their intended purpose.

## The Research: Alternatives Without Oracle

After some digging, I found several options to run this content without Oracle:

### Option 1: Oracle 26ai Free Docker Container

**Good news**: Oracle actually offers a **free Docker container** for 26ai!

```bash
docker pull container-registry.oracle.com/database/free:latest
docker run -d --name oracle-26ai \
  -p 1521:1521 -p 5500:5500 \
  -e ORACLE_PWD=Welcome1 \
  -v ${PWD}/oracle-data:/opt/oracle/oradata \
  container-registry.oracle.com/database/free:latest
```

This gives you a full Oracle 26ai instance locally with vector search support. The free tier has resource limits but is perfect for development and learning.

### Option 2: PostgreSQL + pgvector (Recommended for Most)

The most pragmatic alternative is PostgreSQL with the pgvector extension:

```bash
# Install pgvector
CREATE EXTENSION vector;

# Vector type with 1536 dimensions (OpenAI ada-002)
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    content TEXT,
    embedding vector(1536)
);

# HNSW index for fast similarity search
CREATE INDEX ON documents USING hnsw (embedding vector_cosine_ops);
```

LangChain integration is straightforward:

```python
from langchain_postgres import PGVector

vector_store = PGVector(
    connection_string="postgresql://user:pass@localhost:5432/vectordb",
    collection_name="my_docs",
    embedding_function=embeddings
)
```

**Why pgvector wins**:
- Zero new infrastructure if you already use Postgres
- ACID compliance and SQL joins
- HNSW indexing handles millions of vectors
- Best for <50M vectors (90% of use cases)
- LangChain, LlamaIndex, and LangGraph all support it

### Option 3: ChromaDB (Quickest Setup)

The Oracle repo already includes ChromaDB in its dependencies! This embedded vector DB is the fastest way to get started:

```python
from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name="my_docs",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)
```

**Pros**: `pip install chromadb` and you're running in 30 seconds
**Cons**: Single-node, not designed for high-concurrency production

### Option 4: Self-Hosted Options

For more advanced needs:

| Database | Best For | Open Source |
|----------|---------|------------|
| **Qdrant** | Rich filtering, Rust performance | Yes (Apache 2.0) |
| **Weaviate** | Hybrid keyword + vector search | Yes (BSD-3) |
| **Milvus** | Billion-vector scale, GPU acceleration | Yes (Apache 2.0) |

### Option 5: Graph Databases (GraphRAG)

This is where it gets interesting. **GraphRAG** solves the biggest failure mode of standard vector RAG: isolated chunk lookup that misses relationships between facts.

Instead of just embedding text chunks and doing cosine similarity, GraphRAG stores **entities and their connections** in a knowledge graph, then traverses the graph at query time to answer multi-hop questions.

**Neo4j** is the leader here:

```bash
# Docker setup
docker run -d --name neo4j \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/password \
  neo4j:latest
```

LangChain integration:

```python
from langchain_neo4j import Neo4jVector

# Vector + graph hybrid
vector_store = Neo4jVector.from_existing_graph(
    embedding=embeddings,
    url="bolt://localhost:7687",
    username="neo4j",
    password="password",
    node_label="Document",
    text_node_property="text",
    embedding_property="embedding"
)
```

**Why GraphRAG wins**:
- Answers **multi-hop questions** that vector search gets wrong
- Understands relationships between entities
- Explains WHY an answer was found (traversal path)
- Can combine with vector search (HybridRAG) for best of both

**Memgraph** is another option for GraphRAG with similar capabilities.

For Oracle's agentic_rag focus, graph databases are particularly relevant - agents benefit from understanding entity relationships and traversing knowledge graphs.

## My Current Status

- Repository cloned to `/root/oracle-ai-developer-hub/`
- Development dependencies installed (pre-commit, ruff)
- Pre-commit hooks configured
- Full app dependencies not installed (timed out on large packages)
- No Oracle database to test the actual features

## What's Next?

To really get value from this repo, I have several paths:

1. **Oracle 26ai Free Docker** - Run Oracle locally without cloud dependency
2. **PostgreSQL + pgvector** - Drop-in replacement using existing Postgres
3. **ChromaDB** - Quick local development using what the repo already supports
4. **Neo4j + GraphRAG** - For multi-hop reasoning and knowledge graph RAG

The content looks solid - real enterprise-grade examples, proper architectures, and good documentation. But it's clearly aimed at teams already invested in Oracle infrastructure.

## Resources

- [GitHub Repository](https://github.com/oracle-devrel/oracle-ai-developer-hub)
- [Oracle AI Database Docs](https://docs.oracle.com/en/database/oracle/oracle-database/)
- [OCI Generative AI](https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm)
- [Oracle 26ai Free Container](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/autonomous-database-container-free.html)
- [LangChain pgvector Docs](https://python.langchain.com/docs/integrations/vectorstores/pgvector)
- [pgvector GitHub](https://github.com/pgvector/pgvector)
- [GraphRAG with Neo4j Guide](https://markaicode.com/graphrag-knowledge-graph-enhanced-retrieval-guide/)
- [LangChain Neo4j Integration](https://python.langchain.com/docs/integrations/graph/neo4j)
- [HybridRAG with Memgraph](https://memgraph.com/blog/why-hybridrag)

*Have you got Oracle database access? I'd love to hear if the notebooks work as advertised.*