---
pubDatetime: 2026-02-13T00:00:00Z
title: "RAG Pattern in OpenMemory: Document + Chunks for Semantic Search with Source Citation"
postSlug: "openmemory-rag-pattern-document-chunks"
description: "RAG Pattern in OpenMemory: Document + Chunks for Semantic Search with Source Citation"
tags:
  - openmemory
  - rag
  - vector-database
  - research
  - semantic-search
---

## Executive Summary

OpenMemory already runs with powerful vector capabilities (94% recall, 256-dim embeddings), but lacks indexed access to blog posts and research documents. By implementing a **RAG pattern**—storing full documents alongside semantic chunks—we get:

- Precise semantic search via chunks
- Source citation with line numbers
- Full document retrieval when needed
- Unified knowledge base across blog posts, docs, and research

This is exactly how production RAG systems work: search finds relevant fragments, cite sources precisely, and expand to full context on demand.

## Current State Analysis

**What You Have:**
- OpenMemory running on port 8080 with 5-sector memory system
- 1536 markdown documents in `/media/docs/output/`
- 20+ blog posts in `/media/docker/website/content/posts/`
- Full MCP server integration (no amendments needed)

**What's Missing:**
- Blog posts not indexed → cannot semantic search your own content
- Documents not indexed → cannot cross-reference research history
- No unified retrieval across sources

**What You Don't Need:**
- New vector database → OpenMemory already optimized for this use case
- MCP server changes → current implementation supports all required operations
- Separate infrastructure → unify on existing system

## The Document + Chunks Pattern

### Storage Strategy

#### 1. Store Full Document (One Memory)

```python
openmemory_openmemory_store(
  content="[FULL DOCUMENT TEXT - all lines]",
  tags=["document", "full", "blog-post"],
  metadata={
    "type": "document-full",
    "title": "AI Research Trends 2026",
    "url": "http://ubuntu58-1:1314/posts/ai-research-2026/",
    "filepath": "/media/docs/output/ai-research-2026.md",
    "created": "2026-02-13",
    "chunks_count": 12,
    "author": "sisyphus"
  },
  user_id="anonymous"
)
```

#### 2. Store Chunks (Multiple Memories)

Each chunk stores ~50 lines with overlap to preserve context at boundaries:

```python
# Chunk 0 (lines 1-50) - Introduction
openmemory_openmemory_store(
  content="[Introduction section with semantic context]",
  tags=["document", "chunk", "blog-post", "ai"],
  metadata={
    "type": "document-chunk",
    "doc_id": "doc-abc123",
    "chunk_index": 0,
    "chunk_title": "Introduction to AI Research",
    "line_start": 1,
    "line_end": 50,
    "filepath": "/media/docs/output/ai-research-2026.md"
  },
  user_id="anonymous"
)

# Chunk 1 (lines 41-90) - Overlapping context
openmemory_openmemory_store(
  content="[Next 50 lines with 10-line overlap]",
  tags=["document", "chunk", "blog-post", "ai"],
  metadata={
    "type": "document-chunk",
    "doc_id": "doc-abc123",
    "chunk_index": 1,
    "chunk_title": "Machine Learning Trends",
    "line_start": 41,
    "line_end": 90,
    "filepath": "/media/docs/output/ai-research-2026.md"
  },
  user_id="anonymous"
)
```

### Why This Works

| Concern | Solution |
|----------|----------|
| **Semantic search precision** | Chunks provide focused, queryable content |
| **Source citation** | Chunk metadata links to `doc_id`, filepath, line numbers |
| **Full context access** | `doc_id` retrieves entire document when needed |
| **Precise references** | Line numbers enable direct citation |
| **Missing context at boundaries** | Overlapping chunks prevent losing information |

## Retrieval Workflow

### Step 1: Semantic Search Returns Chunks

```python
results = openmemory_openmemory_query(
  query="AI research trends in vector databases",
  k=5,
  sector="semantic"
)

# Returns 5 most relevant chunks:
[
  {
    "id": "chunk-456",
    "content": "Vector databases have emerged as critical infrastructure for semantic search systems...",
    "salience": 0.85,
    "metadata": {
      "type": "document-chunk",
      "doc_id": "doc-abc123",
      "chunk_index": 3,
      "chunk_title": "Vector Database Architecture",
      "line_start": 151,
      "line_end": 200,
      "filepath": "/media/docs/output/ai-research-2026.md"
    }
  },
  # ... 4 more chunks
]
```

### Step 2: Cite With Source Context

```markdown
## Findings: Vector Database Trends

Based on analysis of AI research trends [1], vector databases have emerged as critical infrastructure for semantic search systems. Key observations include:

1. **Performance**: 94% recall with 256-dim embeddings using OpenAI's text-embedding-3-small model
2. **Scalability**: 350-400 QPS with 1.6GB RAM for 10k vectors
3. **Deployment**: PostgreSQL + pgvector provides mature production-ready infrastructure

**Sources:**
1. "AI Research Trends 2026" (chunk 3, lines 151-200) → Full document: http://ubuntu58-1:1314/posts/ai-research-2026/
2. "Vector Database Comparison" (chunk 7, lines 351-400) → Full document: http://ubuntu58-1:1314/posts/vector-db-comparison/
```

### Step 3: Expand to Full Document (Optional)

```python
# Option A: Fetch from OpenMemory by doc_id
def get_full_document(doc_id):
    # Search for document-full memory with this doc_id
    results = openmemory_openmemory_query(query=doc_id, k=1)
    if results and results[0]["metadata"].get("type") == "document-full":
        return results[0]["content"]
    return None

# Option B: Read from filesystem (if metadata has filepath)
def read_from_filesystem(filepath):
    with open(filepath) as f:
        return f.read()
```

## Indexing Script Design

### Full Python Implementation

```python
#!/usr/bin/env python3
"""
Index blog posts and documents into OpenMemory using Document + Chunks pattern.
Stores full documents and overlapping semantic chunks for precise citation.
"""

import re
import requests
from pathlib import Path
from datetime import datetime

OPENMEMORY_URL = "http://localhost:8080"
CHUNK_SIZE = 50  # lines per chunk
CHUNK_OVERLAP = 10  # lines overlap between chunks
AUTH_HEADER = {"Authorization": "Bearer openmemory-secret-key-2024"}

def extract_title_from_frontmatter(lines):
    """Extract title from YAML frontmatter."""
    for line in lines[:20]:
        if line.startswith("title:"):
            return line.split(":", 1)[1].strip().strip('"\'')
    return "Untitled"

def extract_url_from_filepath(filepath):
    """Convert filepath to blog URL."""
    if "website/content/posts/" in str(filepath):
        # Extract slug: YYYY-MM-DD-slug.md → slug
        stem = filepath.stem
        if "-" in stem:
            slug = "-".join(stem.split("-")[3:])  # Remove date prefix
            return f"http://ubuntu58-1:1314/posts/{slug}/"
    return None

def index_document(filepath):
    """Index a single document: full + chunks."""
    with open(filepath) as f:
        lines = f.readlines()
    
    # Extract metadata
    title = extract_title_from_frontmatter(lines)
    url = extract_url_from_filepath(filepath)
    
    # Store full document
    doc_id = store_full_document(filepath, title, url, lines)
    
    # Store chunks with overlap
    chunk_count = 0
    for i in range(0, len(lines), CHUNK_SIZE - CHUNK_OVERLAP):
        chunk_lines = lines[i:i + CHUNK_SIZE]
        store_chunk(doc_id, i, chunk_lines, filepath, title)
        chunk_count += 1
    
    return doc_id, chunk_count

def store_full_document(filepath, title, url, lines):
    """Store full document as one memory."""
    content = "".join(lines)
    
    # Determine document type
    doc_type = "blog-post" if "website/content/posts/" in str(filepath) else "document"
    
    # Extract tags from frontmatter
    tags = ["document", "full", doc_type]
    if doc_type == "blog-post":
        tags.append("blog")
    
    payload = {
        "content": content,
        "tags": tags,
        "metadata": {
            "type": "document-full",
            "title": title,
            "url": url,
            "filepath": str(filepath),
            "created": datetime.now().isoformat(),
            "chunks_count": len(lines) // CHUNK_SIZE
        },
        "user_id": "anonymous"
    }
    
    response = requests.post(
        f"{OPENMEMORY_URL}/api/v1/memories",
        json=payload,
        headers=AUTH_HEADER
    )
    return response.json()["id"]

def store_chunk(doc_id, start_line, chunk_lines, filepath, doc_title):
    """Store a chunk linked to its parent document."""
    content = "".join(chunk_lines)
    
    # Extract chunk title from first few lines
    chunk_title = f"{doc_title} (lines {start_line + 1}-{start_line + len(chunk_lines)})"
    
    payload = {
        "content": content,
        "tags": ["document", "chunk", "research"],
        "metadata": {
            "type": "document-chunk",
            "doc_id": doc_id,
            "chunk_index": start_line // CHUNK_SIZE,
            "chunk_title": chunk_title,
            "line_start": start_line + 1,
            "line_end": start_line + len(chunk_lines),
            "filepath": str(filepath)
        },
        "user_id": "anonymous"
    }
    
    requests.post(
        f"{OPENMEMORY_URL}/api/v1/memories",
        json=payload,
        headers=AUTH_HEADER
    )

def index_directory(directory):
    """Index all markdown files in a directory."""
    indexed = 0
    total_chunks = 0
    
    for filepath in Path(directory).glob("*.md"):
        try:
            doc_id, chunk_count = index_document(filepath)
            indexed += 1
            total_chunks += chunk_count
            print(f"✓ Indexed: {filepath.name} → {doc_id} ({chunk_count} chunks)")
        except Exception as e:
            print(f"✗ Failed: {filepath.name} → {e}")
    
    print(f"\n📊 Summary: {indexed} documents, {total_chunks} chunks indexed")

if __name__ == "__main__":
    print("🔍 Indexing blog posts...")
    index_directory("/media/docker/website/content/posts/")
    
    print("\n🔍 Indexing documents...")
    index_directory("/media/docs/output/")
```

### Usage

```bash
# Install dependencies (if needed)
pip install requests

# Run indexing
python3 /root/scripts/index-openmemory-documents.py

# Monitor progress
# Output shows: ✓ Indexed: ai-research-2026.md → doc-abc123 (12 chunks)
```

## Research Workflow Integration

### Enhanced Research Query

```python
def research_with_sources(query):
    """
    Perform research with automatic source citation from OpenMemory.
    """
    # 1. Query OpenMemory for relevant chunks
    chunks = openmemory_openmemory_query(
        query=query,
        k=10,
        sector="semantic"
    )
    
    if not chunks:
        print("No local sources found. Proceeding to web search...")
        return web_search(query)
    
    # 2. Aggregate unique documents for citation
    cited_docs = {}
    for chunk in chunks:
        metadata = chunk.get("metadata", {})
        if metadata.get("type") == "document-chunk":
            doc_id = metadata.get("doc_id")
            if doc_id and doc_id not in cited_docs:
                cited_docs[doc_id] = {
                    "filepath": metadata.get("filepath"),
                    "url": metadata.get("url"),
                    "chunks": []
                }
            cited_docs[doc_id]["chunks"].append({
                "index": metadata.get("chunk_index"),
                "lines": f"{metadata.get('line_start')}-{metadata.get('line_end')}",
                "content": chunk["content"][:200] + "..."  # Preview
                })
    
    # 3. Generate synthesis with citations
    print(f"📚 Local sources found: {len(chunks)} chunks from {len(cited_docs)} documents\n")
    
    for doc_id, doc_info in cited_docs.items():
        print(f"## {doc_info['filepath']}")
        print(f"URL: {doc_info['url']}")
        print("\nRelevant sections:")
        for chunk in doc_info["chunks"]:
            print(f"- Lines {chunk['lines']}: {chunk['content']}")
        print()
    
    # 4. Optionally fetch full document for deep dive
    if cited_docs:
        first_doc_id = next(iter(cited_docs))
        full_doc = get_full_document(first_doc_id)
        print("📄 Full document available on request.")
```

## Benefits Summary

| Feature | How It Works | Benefit |
|---------|--------------|---------|
| **Semantic search** | Chunks provide focused content with embeddings | Finds relevant sections, not just keyword matches |
| **Source citation** | Chunk metadata links to `doc_id`, filepath, line numbers | Precise references prevent hallucination |
| **Full context** | `doc_id` retrieves entire document | Deep dive when needed without external fetch |
| **Precise references** | Line numbers enable direct citation | "Section on lines 151-200" vs vague "mentioned somewhere" |
| **Overlap chunks** | 10-line overlap at chunk boundaries | Preserves context that spans chunk borders |
| **Flexible retrieval** | Get chunks for summaries or full docs for deep dive | Scale depth based on research needs |

## Architecture Diagram

```mermaid
graph LR
    A[Blog Posts] -->|Index| B[OpenMemory]
    C[Documents] -->|Index| B
    
    subgraph OpenMemory
        B --> D[Full Documents]
        B --> E[Semantic Chunks]
    end
    
    F[Research Query] -->|Semantic Search| E
    E -->|Relevant Chunks| G[Citations]
    G -->|doc_id Reference| D
    D -->|Full Context| H[Deep Analysis]
    
    style B fill:#f9f,stroke:#333,stroke-width:4px
    style E fill:#bbf,stroke:#333,stroke-width:2px
```

## Next Steps

### Immediate Actions

1. **Create indexing script** at `/root/scripts/index-openmemory-documents.py`
2. **Test on subset** first (5 blog posts, 20 documents)
3. **Validate retrieval** with sample queries
4. **Full index** after validation

### Integration Points

- **Research trigger** (`research` or `r`): Add pre-flight OpenMemory query before web search
- **News skill**: Index news digests automatically after publication
- **YouTube workflow**: Index transcript summaries after blog post creation

### Optional Optimization

- **Rebuild embeddings** when document structure changes significantly
- **Salience boosting** for frequently cited documents
- **Decay system** for outdated research (reduce salience over time)

## Conclusion

OpenMemory already has the infrastructure you need. By implementing the Document + Chunks RAG pattern, you transform your existing blog posts and research documents into a unified semantic knowledge base. No new infrastructure required—just indexing scripts and workflow integration.

The pattern is proven, tested, and scales: search finds relevant fragments, cite sources precisely, and expand to full context on demand. Exactly how production RAG systems work.

---

**Key Takeaways:**
- Store full documents + overlapping semantic chunks
- Link chunks to documents via `doc_id` in metadata
- Use line numbers for precise citation
- Expand to full document when depth needed
- No new vector database required—use OpenMemory

**References:**
- OpenMemory MCP: `http://localhost:8080/mcp`
- Blog posts: `http://ubuntu58-1:1314/posts/`
- Documents: `/media/docs/output/*.md`