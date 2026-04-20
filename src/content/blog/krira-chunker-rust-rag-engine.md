---
pubDatetime: 2026-02-28T22:26:00Z
title: "Krira Chunker: Production-Grade Rust Chunking Engine for RAG Pipelines"
postSlug: "krira-chunker-rust-rag-engine"
description: "Krira Chunker: Production-Grade Rust Chunking Engine for RAG Pipelines"
tags:
  - chunking
  - rag
  - rust
  - open-source
  - ai
---

A new open-source project from Krira Labs is tackling one of the most overlooked bottlenecks in RAG (Retrieval-Augmented Generation) pipelines: **document chunking**. Meet Krira Chunker — a high-performance Rust-based engine that processes gigabytes of text in seconds with **O(1) memory usage**.

## The Problem

Traditional chunking solutions like LangChain's text splitters work fine for small documents, but they struggle at scale. Processing large datasets often means:

- Slow performance (Python-based implementations)
- High memory consumption
- Limited format support
- No streaming capabilities

## The Solution

Krira Chunker is built in Rust with a Python wrapper, delivering:

- **40x faster** than LangChain
- **O(1) memory usage** — constant memory regardless of file size
- **47.51 MB/s** throughput in benchmarks
- **42.4 million chunks** processed in 113.79 seconds

## Installation

```bash
pip install krira-augment
```

## Quick Start

```python
from krira_augment.krira_chunker import Pipeline, PipelineConfig, SplitStrategy

config = PipelineConfig(
    chunk_size=512,
    strategy=SplitStrategy.SMART,
    clean_html=True,
    clean_unicode=True,
)

pipeline = Pipeline(config=config)
result = pipeline.process("sample.csv", output_path="output.jsonl")

print(f"Chunks Created: {result.chunks_created}")
print(f"Execution Time: {result.execution_time:.2f}s")
print(f"Throughput: {result.mb_per_second:.2f} MB/s")
```

## Architecture

{{< mermaid >}}
graph LR
    A[Input Files] --> B[Format Detection]
    B --> C[Rust Core Engine]
    C --> D[Smart Chunking]
    D --> E[Output Generator]
    E --> F[JSONL/Stream]
    
    subgraph "Supported Formats"
        G[CSV]
        H[PDF]
        I[JSON/JSONL]
        J[DOCX]
        K[XLSX]
        L[URLs]
    end
    
    G --> A
    H --> A
    I --> A
    J --> A
    K --> A
    L --> A
{{< /mermaid >}}

## Supported Formats

| Format | Extension | Method |
|--------|-----------|--------|
| CSV | `.csv` | Direct processing |
| Text | `.txt` | Direct processing |
| JSONL | `.jsonl` | Direct processing |
| JSON | `.json` | Auto-flattening |
| PDF | `.pdf` | pdfplumber extraction |
| Word | `.docx` | python-docx extraction |
| Excel | `.xlsx` | openpyxl extraction |
| XML | `.xml` | ElementTree parsing |
| URLs | `http://` | BeautifulSoup scraping |

## Streaming Mode

For real-time pipelines, Krira Chunker offers a streaming mode that processes chunks without saving to disk:

```python
# No intermediate file created
for chunk in pipeline.process_stream("data.csv"):
    # Process each chunk immediately
    embedding = model.encode(chunk["text"])
    vector_store.upsert(chunk["metadata"], embedding)
```

### Streaming vs File-Based

| Feature | File-Based | Streaming |
|---------|------------|-----------|
| **Disk I/O** | Creates chunks.jsonl | None |
| **Memory Usage** | O(1) constant | O(1) constant |
| **Speed** | Chunking + Embedding | Overlapped (faster) |
| **Use Case** | Large files, batch processing | Real-time, no storage |

## Vector Store Integrations

Krira Chunker works seamlessly with popular vector databases:

### Local (Free)
- **ChromaDB** + SentenceTransformers
- **FAISS** + Hugging Face

### Cloud (Paid)
- **Pinecone** + OpenAI/Cohere
- **Qdrant** + OpenAI/Cohere
- **Weaviate** + OpenAI

### Complete Example: ChromaDB (Free)

```python
from krira_augment.krira_chunker import Pipeline, PipelineConfig
from sentence_transformers import SentenceTransformer
import chromadb

# Chunk
config = PipelineConfig(chunk_size=512, chunk_overlap=50)
pipeline = Pipeline(config=config)
result = pipeline.process("sample.csv", output_path="chunks.jsonl")

# Embed and store (all local, no API keys)
model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.Client()
collection = client.get_or_create_collection("my_rag_db")

with open("chunks.jsonl", "r") as f:
    for line_num, line in enumerate(f, 1):
        chunk = json.loads(line)
        embedding = model.encode(chunk["text"])
        collection.add(
            ids=[f"chunk_{line_num}"],
            embeddings=[embedding.tolist()],
            documents=[chunk["text"]]
        )
```

## Why Rust?

The choice of Rust enables:

1. **Memory Safety** — No garbage collection pauses
2. **Zero-Cost Abstractions** — High-level code, low-level performance
3. **Fearless Concurrency** — Safe parallel processing
4. **Small Binary Size** — Minimal deployment footprint

The Python wrapper via PyO3/Maturin makes it accessible to the ML/AI community while maintaining Rust's performance benefits.

## Error Handling (Production Ready)

```python
for chunk in pipeline.process_stream("data.csv"):
    try:
        response = client.embeddings.create(
            input=chunk["text"],
            model="text-embedding-3-small"
        )
        index.upsert(vectors=[(f"chunk_{count}", embedding, metadata)])
    except Exception as e:
        error_count += 1
        if "rate_limit" in str(e).lower():
            time.sleep(60)  # Back off and retry
```

## Links

- **GitHub**: [https://github.com/Krira-Labs/krira-chunker](https://github.com/Krira-Labs/krira-chunker)
- **Website**: [https://www.kriralabs.com](https://www.kriralabs.com)
- **PyPI**: `pip install krira-augment`

## Summary

Krira Chunker fills a critical gap in the RAG ecosystem by providing production-grade chunking performance. If you're building retrieval systems at scale, this Rust-powered engine offers the speed, memory efficiency, and format flexibility that Python-only solutions can't match.

The combination of **O(1) memory**, **streaming mode**, and **broad format support** makes it particularly valuable for teams processing large document corpora or building real-time ingestion pipelines.