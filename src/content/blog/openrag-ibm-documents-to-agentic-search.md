---
pubDatetime: 2026-02-15T12:00:00Z
title: "OpenRAG: IBM's Open-Source Platform for Going from Documents to Agentic Search in Minutes"
postSlug: "openrag-ibm-documents-to-agentic-search"
description: "OpenRAG: IBM's Open-Source Platform for Going from Documents to Agentic Search in Minutes"
tags:
  - opensearch
  - rag
  - langflow
  - ibm
  - open-source
  - docling
  - ai
---

There's a growing number of RAG (Retrieval-Augmented Generation) frameworks out there, but most of them require significant setup time, configuration headaches, and a deep understanding of vector databases before you can even ask your first question. **OpenRAG**, an open-source project from IBM Research, takes a radically different approach: go from raw documents to a fully functional agentic search system in under five minutes.

The project homepage is at [openr.ag](https://www.openr.ag/) and the source is on [GitHub](https://github.com/langflow-ai/openrag).

## What Is OpenRAG?

OpenRAG is a comprehensive RAG platform that enables intelligent document search and AI-powered conversations. You upload documents, the system processes and indexes them, and then you can query them through a chat interface backed by large language models and semantic search.

What makes it stand out is the stack it's built on and how cleanly everything is integrated:

- **[OpenSearch](https://github.com/opensearch-project/OpenSearch)** for vector storage and semantic search
- **[Langflow](https://github.com/langflow-ai/langflow)** for AI workflow orchestration and visual pipeline design
- **[Docling](https://github.com/docling-project/docling)** for document ingestion and parsing
- **[Starlette](https://github.com/Kludex/starlette)** as the high-performance Python backend
- **[Next.js](https://github.com/vercel/next.js)** for the frontend UI

## The Architecture

The platform follows a clean, modular architecture where each component has a well-defined role:

{{< mermaid >}}
graph LR
    A["Documents<br/>(PDF, DOCX, etc.)"] --> B["Docling<br/>Ingestion & Parsing"]
    B --> C["OpenSearch<br/>Vector Storage & Index"]
    C --> D["Langflow<br/>Orchestration & Workflows"]
    D --> E["Starlette API<br/>Backend"]
    E --> F["Next.js<br/>Chat UI"]
    G["LLM Provider<br/>(Ollama, OpenAI, etc.)"] --> D
{{< /mermaid >}}

The key architectural decisions:

- **Docling** handles document processing with zero configuration -- it works out of the box with no setup required
- **OpenSearch** stores embeddings and handles semantic search with dynamic index creation based on the embedding model dimensions
- **Langflow** manages complex AI workflows including ingestion pipelines, chat flows, and intelligent nudges
- A **ConnectorRouter** can switch between Langflow pipelines and OpenRAG's internal processing engine

## Setup: Genuinely Fast

The installation process is refreshingly simple. You need Docker (or Podman) running, then:

```bash
mkdir openrag-workspace
cd openrag-workspace
uvx openrag
uv run openrag
```

That's it. The system creates its directory structure, pulls the required container images, and presents you with a configuration TUI (terminal UI) that helps you set up your `.env` file through clean setup screens -- covering LLM provider selection, API keys, OpenSearch passwords, and embedding model configuration.

The UI is available at `http://localhost:3000` once everything is running.

## How the Backend Works

Looking at the `main.py` in the GitHub repository, the backend follows a well-thought-out initialization sequence:

### 1. Hardware-Aware Startup

The system forces the `spawn` method for multiprocessing to ensure CUDA (GPU) compatibility. This is critical because PyTorch is not fork-safe -- if a process forks after GPU initialization, the child process inherits a corrupted state. By using `spawn`, every worker starts clean.

```python
multiprocessing.set_start_method("spawn", force=True)
```

### 2. Service Initialization

On startup, the app initializes a `SessionManager`, `DocumentService`, and `TaskService` (which manages a process pool). It waits for OpenSearch to respond before creating dynamic indexes based on the embedding model dimensions. It also auto-ingests any default files found in `/app/openrag-documents/`.

### 3. Request Lifecycle

Most endpoints follow this flow:

{{< mermaid >}}
graph TD
    A["Incoming Request"] --> B{"Auth Middleware"}
    B -->|"Valid JWT/API Key"| C{"Request Type"}
    B -->|"Invalid"| D["401 Unauthorized"]
    C -->|"Heavy Task (Upload)"| E["TaskService<br/>Background Process Pool"]
    C -->|"Chat/Search"| F["OpenSearch Query<br/>+ LLM Response"]
    E --> G["Task ID Returned<br/>Client Polls Status"]
    F --> H["Context-Aware Response"]
{{< /mermaid >}}

For heavy operations like uploading a 100-page PDF, the API doesn't block. It creates a Task ID via `TaskService`, processes the file in a background process pool, and lets the client poll for status. This keeps the chat interface responsive even during large ingestion jobs.

### 4. Authentication

The system supports both **OIDC (OpenID Connect)** for user authentication and **API Key-based** authentication for external integrations -- plus optional Google OAuth and Microsoft Graph for cloud storage connectors (Google Drive, SharePoint/OneDrive).

## GPU Acceleration with Docling

OpenRAG leverages Docling with optional CUDA acceleration for document layout analysis. The design is careful about GPU resource management:

- The process pool is initialized *before* any heavy AI imports to avoid CUDA state corruption
- Document processing is offloaded to dedicated background processes via `TaskService`
- The UI provides a toggle between CPU and GPU modes
- Large batches of PDFs can be handled without memory spikes or blocking the main application

## What Sets It Apart

Several things make OpenRAG notable compared to other RAG frameworks:

1. **Zero-configuration document processing** -- Docling handles the heavy lifting without any setup
2. **Sub-5-minute deployment** -- from `git clone` to a working system
3. **Visual pipeline editing** via Langflow -- modify ingestion and chat workflows without touching code
4. **Production-ready auth** -- OIDC, API keys, and cloud provider OAuth out of the box
5. **Clean separation of concerns** -- each component (search, orchestration, ingestion, UI) is independently replaceable
6. **Multiple LLM provider support** -- Ollama (local), OpenAI, Anthropic, and IBM watsonx

## Key Configuration

The `.env` file controls the entire system. Notable settings include:

| Setting | Purpose |
|---------|---------|
| `LLM_PROVIDER` | Choose between `ollama`, `anthropic`, `watsonx`, or `ibm` |
| `EMBEDDING_PROVIDER` | Choose between `watsonx`, `ibm`, or `ollama` |
| `DISABLE_INGEST_WITH_LANGFLOW` | Toggle between Langflow and traditional ingestion |
| `OPENSEARCH_PASSWORD` | Must be complex (8+ chars, upper, lower, digit, special) |
| `LANGFLOW_TIMEOUT` | Increase for large documents (default: 2400s / 40 minutes) |

## Links

- **Website**: [https://www.openr.ag/](https://www.openr.ag/)
- **Documentation**: [https://docs.openr.ag/](https://docs.openr.ag/)
- **GitHub**: [https://github.com/langflow-ai/openrag](https://github.com/langflow-ai/openrag)
- **Langflow Integration**: [https://docs.openr.ag/agents](https://docs.openr.ag/agents)

*Based on the article ["OpenRAG" From Documents to Agentic Search in Minutes](https://alain-airom.medium.com/openrag-from-documents-to-agentic-search-in-minutes-from-ibm-research-open-source-ed6bf506507b) by Alain Airom.*