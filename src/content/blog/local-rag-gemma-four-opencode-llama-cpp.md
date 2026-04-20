---
pubDatetime: 2026-04-04T09:02:15Z
title: "Building a Local RAG App with Gemma 4, OpenCode & llama.cpp"
postSlug: "local-rag-gemma-four-opencode-llama-cpp"
description: "Building a Local RAG App with Gemma 4, OpenCode & llama.cpp"
tags:
  - opencode
  - gemma-4
  - rag
  - llama-cpp
  - langchain
  - ollama
  - local-ai
  - streamlit
---

# Building a Local RAG App with Gemma 4, OpenCode & llama.cpp

> **TL;DR**: Venelin Valkov live-streams building an entire local RAG application using Gemma 4 (26B) inside OpenCode, powered by llama.cpp on an M4 MacBook with 48GB unified memory — achieving 57 tokens/second with 4-bit quantization and delivering a working Streamlit app in under an hour.

## Quick Summary

- Google's Gemma 4 (26B, MoE with 4B active) ranks competitively on Arena AI leaderboards — above some 400B models on textual tasks
- Running on llama.cpp with 4-bit quantization: ~57 tok/s on M4 MacBook (48GB unified memory)
- A full RAG application was built with OpenCode using Streamlit, LangChain, ChromaDB, and Ollama
- Embedding model choice critically impacted retrieval quality — switching from default to Cohere v3 embeddings fixed RAG accuracy
- Effective model sizes are misleading: the "4B effective" model requires loading all 26B parameters into memory

## The Setup: Gemma 4 on Local Hardware

Valkov demonstrates running the **Gemma 4 26B parameter model** (4-bit quantized, MoE architecture with 4B active parameters) via **llama.cpp** on an M4 MacBook Pro with 48GB of unified memory. The key configuration:

- **Provider**: llama.cpp server with AI SDK (Vercel) providing an OpenAI-compatible API
- **Context window**: 256K tokens
- **Quantization**: 4-bit (Q4) — a step down from 8-bit, delivering ~57 tok/s vs ~40 tok/s
- **OpenCode config**: `opencode.json` pointing to local llama.cpp server with full model name specified

> [!WARNING] Effective vs Real Parameter Counts
> Google markets "effective" sizes (2B, 4B), but you must load the full weights. The 4B effective model is actually 8B real parameters, and the 26B model requires all 26B in memory regardless of MoE routing. This catches many developers off guard.

## Benchmark Performance

On **Arena AI** (open-source models only, textual tasks), Gemma 4 performs impressively:

| Model | Ranking |
|-------|---------|
| Gemma 4 (full) | Above Qwen 3.5 400B |
| Gemma 4 26B (4B active) | Close to top-tier models |

While benchmarks should be taken with caution, Valkov's hands-on testing confirmed the model is genuinely capable for coding tasks.

## Building the RAG Application

The project goal: a **fully local RAG app** with three core features:

1. **PDF upload** — convert to local markdown
2. **Chat with selected PDFs** — retrieval-augmented generation
3. **Model selection** — choose from locally available Ollama models

**Tech stack chosen by Gemma 4**:

| Component | Choice |
|-----------|--------|
| UI Framework | Streamlit |
| PDF Conversion | PyMuPDF4LLM |
| Vector Database | ChromaDB (local persist) |
| LLM Engine | LangChain + Ollama |
| Embeddings | Initially nomic-embed-text, later Cohere v3 |

## The Good: What Worked

### Rapid Prototyping

OpenCode + Gemma 4 generated a working Streamlit application with multiple modules in a single session — PDF processor, vector store manager, RAG engine, and chat interface. The model created the project structure, wrote all the code, and even ran `uv sync` to install dependencies.

### PDF to Markdown Conversion

The PyMuPDF4LLM library chosen by the model produced reasonable markdown output from academic papers, preserving structure like abstracts, sections, and some LaTeX formatting.

### Speed of 4-bit Quantization

At 57 tokens/second, the coding experience felt responsive. Valkov noted this was significantly better than the 40 tok/s with 8-bit quantization from the previous day's stream.

## The Bad: What Went Wrong

### Stale Library Knowledge

The model installed **outdated LangChain versions** (0.3.x instead of current 1.2.x), causing import errors with `langchain.chains`. This required manual debugging and re-importing from the correct module paths (`langchain_ollama`, `langchain_core.prompts`, etc.).

### Embedding Quality Crisis

The initial embedding model produced chunks that were essentially **garbage** — a chunk labeled "introduction" with no useful content. Switching to **Cohere v3 embeddings** (600M parameters) completely transformed retrieval quality, correctly surfacing the exact chunk containing the answer.

### RAG Accuracy Failures

Before the embedding fix, the RAG system failed basic retrieval: asked "what GPU was used for testing?" it returned "no information found" despite the answer being clearly present in the paper. The fix: smaller chunk size (halved) + more chunks retrieved + better embeddings.

### Context Degradation

As the conversation grew longer, the model's performance degraded — a common issue with open-weight models. The "chain broke" during extended debugging sessions, producing progressively worse results.

## Key Takeaways

<details>
<summary>Technical Lessons Learned</summary>

1. **Embeddings matter more than you think** — The difference between nomic-embed-text and Cohere v3 was night and day for RAG accuracy
2. **Effective model sizes are marketing** — Plan for the full parameter count, not the "active" count
3. **Library versions matter** — Gemma 4's training data includes older LangChain APIs; always verify imports
4. **4-bit quantization is the sweet spot** for local development on consumer hardware
5. **Chunk strategy is critical** — Smaller chunks + higher retrieval count improved accuracy significantly

</details>

<details>
<summary>Hardware Requirements</summary>

| Config | VRAM Needed | Speed | Notes |
|--------|-------------|-------|-------|
| M4 48GB + Q4 | ~26GB | ~57 tok/s | Works well |
| M4 48GB + Q8 | ~26GB | ~40 tok/s | More accurate |
| RTX 4090 24GB | ~24GB | 100-140 tok/s | Only 20K context |
| 16GB VRAM + Q4 | ~16GB | Slow/fails | Borderline |

For mobile/IoT deployment, Valkov recommends models under 1B real parameters — the "effective 2B" Gemma 4 models won't run on consumer mobile devices.

</details>

## The Verdict

Despite hiccups with stale library knowledge and embedding quality, the combination of **Gemma 4 + OpenCode + llama.cpp** proved capable of building a functional RAG application in a single live session. The MoE architecture's ability to punch above its weight class is impressive, but the effective-vs-real parameter size marketing is genuinely misleading for developers planning deployments.

The biggest insight? **Your embedding model choice can make or break your RAG system** — arguably more than your generative model choice.

---

*Based on [Venelin Valkov's live stream](https://www.youtube.com/watch?v=-_hC-C_Drcw). Code available in the linked GitHub repository.*

**Tags**: gemma-4, rag, opencode, llama-cpp, local-ai, streamlit, langchain, ollama
**Categories**: AI Engineering, Tutorials
