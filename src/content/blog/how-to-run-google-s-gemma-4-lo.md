---
pubDatetime: 2026-04-13T19:00:00Z
title: "How to Run Google's Gemma 4 Locally: A Practical Guide"
postSlug: "how-to-run-google-s-gemma-4-lo"
description: "How to Run Google's Gemma 4 Locally: A Practical Guide"
tags:
  - "3"
---

The economics of AI just shifted. Google released Gemma 4 — a family of four open-source, multimodal models licensed under Apache 2 — and the smallest one runs on a phone with zero internet. Here's how to get it running on your own hardware in under ten minutes.

## What You're Getting

Gemma 4 isn't one model. It's four, each targeting different hardware:

| Model | Parameters | Active Params | Runs On | Best For |
|-------|-----------|---------------|---------|----------|
| E2B | ~2B effective | 2B | Phone, Raspberry Pi, browser | Quick tasks, edge AI |
| E4B | ~4B effective | 4B | Single T4 GPU, edge devices | Balanced edge performance |
| 26B MoE | 26B total | ~4B active | Laptop, desktop | Flagship quality, laptop-friendly |
| 31B Dense | 31B | 31B | High-end GPU | Maximum capability |

All four handle text natively. The E2B and E4B handle images and audio. The 26B and 31B add video understanding. Every model includes built-in function calling (not prompt engineering — actual special tokens in the architecture) and step-by-step thinking mode.

The Apache 2 license is the key differentiator: commercial use, modification, fine-tuning, and redistribution — all permitted with no permissions needed. This is a first for Google.

## Step 1: Install Ollama

Download from [ollama.com](https://ollama.com/download) for your platform (macOS, Linux, or Windows). The installer handles everything — no dependencies to manage.

If you prefer the terminal:

```bash
# Linux
curl -fsSL https://ollama.com/install.sh | sh

# macOS (Homebrew)
brew install ollama
```

Launch Ollama after installation. You'll see a clean interface with no models loaded yet.

## Step 2: Pull the Model

The 26B MoE variant is the sweet spot for most people. It has the knowledge of a 25B parameter model but only uses the compute of a 4B model at inference time:

```bash
ollama pull gemma4:26b
```

Download takes roughly 5-6 minutes on a standard connection. For edge devices, use `gemma4:e2b` or `gemma4:e4b` instead.

## Step 3: Run Your First Query

Open Ollama, start a new chat, and select your pulled model. Or use the CLI directly:

```bash
ollama run gemma4:26b
```

Try a test prompt to verify everything works:

```
> Explain the difference between a mixture of experts model and a dense model in two sentences.
```

You should see the model think for a few seconds before generating a response. Everything runs locally — no API calls, no data leaving your machine.

## Step 4: Connect to an Agent Framework

Gemma 4 plugs into Open WebUI, OpenClaw, and similar agent frameworks for autonomous workflows — browsing, file management, code execution, multi-step chains — all running locally through Ollama.

For a zero-install option, Hugging Face hosts a WebGPU demo where you can run Gemma 4 directly in your browser.

## Validation: What to Expect

Here's what the benchmarks show for the 31B dense model:

- **AIM 2026 Math**: 89.2% (4.3x improvement over Gemma 3's 20.8%)
- **Live Code Bench**: 80%
- **GPQA Diamond (graduate science)**: 84.3%
- **Arena AI Elo**: 1452 — ranked #3 among all open-source models, ahead of Llama, DeepSeek, and Qwen

The edge models perform similarly relative to their size. The E2B scores 37.5% on AIM math while fitting on a phone. On a Raspberry Pi 5 ($80), it hits 133 prefill tokens/second and 7.6 decode tokens/second on CPU alone.

## Common Mistakes

**Mistake 1: Expecting closed-model quality for complex tasks.** The edge models (E2B, E4B) struggle with complex multi-step reasoning, deep code analysis, and production-grade document understanding. Use the 31B or stick with closed models for those workloads.

**Mistake 2: Ignoring quantization trade-offs.** Benchmarks are measured at full precision. When you compress to 4-bit or 2-bit to fit on a phone, quality drops. Quantized versions are good, not identical.

**Mistake 3: Assuming ecosystem parity with Llama.** Gemma 4 has been public for days. Llama has years of community fine-tunes, adapters, and tooling. The ecosystem will grow, but today Llama's is deeper.

**Mistake 4: Expecting video on edge models.** Only the 26B and 31B handle video. The E2B and E4B cover text, image, and audio only.

## When This Makes Sense

Use Gemma 4 when you need zero API costs, zero data egress, zero vendor lock-in, and the quality gap between open and closed is acceptable for your use case. For most business applications — chatbots, document summarisation, code assistance, scene description — the 26B MoE delivers frontier-adjacent quality at zero marginal cost.

Stick with closed models when you need absolute peak performance on hard tasks and cost isn't a constraint. The gap is shrinking fast, but for production-grade complex reasoning, the closed models are still meaningfully ahead.

**Tags**: gemma-4, google, open-source-ai, ollama, local-ai, edge-computing, llm