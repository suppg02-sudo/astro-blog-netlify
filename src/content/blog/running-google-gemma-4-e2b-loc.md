---
pubDatetime: 2026-04-03T21:59:24Z
title: "Running Google Gemma 4 E2B Locally with Hermes Agent and vLLM"
postSlug: "running-google-gemma-4-e2b-loc"
description: "Running Google Gemma 4 E2B Locally with Hermes Agent and vLLM"
tags:
  - others
---

Google's Gemma 4 E2B is a compact multimodal model that punches well above its weight. With just 2 billion effective parameters, it handles text, vision, and audio on a single GPU. This walkthrough shows how to serve it locally with vLLM and connect it to Hermes Agent for autonomous AI capabilities.

> **TL;DR**: Install vLLM, download Gemma 4 E2B from Hugging Face, serve it locally, then connect it to Hermes Agent for agentic workflows — all running on a single GPU with under 8GB VRAM base consumption.

## Quick Summary

- **Model**: Google Gemma 4 E2B IT (instruction-tuned) — a 2-billion effective parameter multimodal model
- **Runtime**: vLLM for high-throughput serving with tool call support
- **Agent**: Hermes Agent — an agentic harness competing with OpenCrew, offering 70+ pre-loaded skills
- **Hardware**: Tested on NVIDIA RTX 6000 (48GB VRAM) — model loads in under 8GB
- **Modalities**: Text, image understanding, and audio transcription in 100+ languages

## Step 1: Install and Upgrade vLLM

vLLM support for Gemma 4 is only available in the latest version. If you already have vLLM installed, upgrade it:

```bash
pip install --upgrade vllm
```

Verify the version supports Gemma 4:

```bash
python -c "import vllm; print(vllm.__version__)"
```

<details>
<summary>Why vLLM?</summary>

vLLM is a high-throughput inference engine that supports continuous batching, PagedAttention, and tool calling. It's become the de facto standard for serving LLMs locally because it handles concurrent requests efficiently and supports the OpenAI-compatible API format out of the box.

</details>

## Step 2: Download the Model

Pull Google's Gemma 4 E2B from Hugging Face to a local directory:

```bash
# Clone the model to a local folder
huggingface-cli download google/gemma-4-E2B-it --local-dir ./gemma-4-e2b
```

You can use any other model from the Gemma 4 family if the E2B variant doesn't suit your needs.

## Step 3: Serve the Model with vLLM

Launch the model server with tool calling enabled:

```bash
vllm serve ./gemma-4-e2b \
  --host 0.0.0.0 \
  --port 8000 \
  --max-model-len 8192 \
  --enable-tool-call \
  --gpu-memory-utilization 0.9
```

Key flags explained:

| Flag | Purpose |
|------|---------|
| `--max-model-len 8192` | Sets context window size (reduce if VRAM is tight) |
| `--enable-tool-call` | Enables function calling for agent integration |
| `--gpu-memory-utilization 0.9` | Uses up to 90% of available GPU memory |

The model loads in under 8GB of VRAM. During active inference, total VRAM usage peaks around 43GB on a 48GB card.

## Step 4: Install and Configure Hermes Agent

Install Hermes Agent with a single command:

```bash
curl -fsSL https://hermes.dev/install.sh | bash
```

During setup, the installer will ask for:

1. **Model provider** — Select "Custom Endpoint"
2. **Base URL** — Enter your vLLM endpoint: `http://localhost:8000/v1`
3. **API key** — Leave blank (local serving)
4. **Model name** — Hermes auto-detects the model; confirm when prompted

After installation, source your shell:

```bash
source ~/.bashrc
hermes --version
```

Verify the configuration points to your local model:

```bash
hermes config show
```

<details>
<summary>Hermes Agent vs Other Agentic Harnesses</summary>

Hermes Agent positions itself as a competitor to frameworks like OpenCrew. Key differentiators include:

- **70+ pre-loaded skills** available immediately on launch
- **Multi-channel support** — Telegram, WhatsApp, and more
- **Local-first design** — works with any OpenAI-compatible endpoint
- **Tool calling** — native support for function calling through the model

For this setup, we're keeping everything local without configuring external channels, but the framework supports them if needed.

</details>

## Step 5: Test the Agent

Launch Hermes and start interacting:

```bash
hermes
```

The agent starts with its pre-loaded skills and connects to your locally-served Gemma 4 model. You can ask questions directly and Hermes will use its tools behind the scenes to research and respond.

### Multimodal Testing Outside Hermes

Since Hermes doesn't have native audio passthrough, you can test audio capabilities directly through the vLLM endpoint with Python:

```python
import requests

# Audio transcription test
response = requests.post(
    "http://localhost:8000/v1/audio/transcriptions",
    files={"file": open("sample.mp3", "rb")},
    data={"language": "en"}
)
print(response.json())
```

Gemma 4 E2B supports transcription in over 100 languages. Testing across multiple languages shows solid performance for a model of this size.

### Image Understanding

For vision tasks, send images through the API:

```python
import base64
import requests

with open("newspaper.jpg", "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode()

response = requests.post(
    "http://localhost:8000/v1/chat/completions",
    json={
        "model": "gemma-4-E2B-it",
        "messages": [{
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}},
                {"type": "text", "text": "Extract all headlines and summarize the main story in three sentences."}
            ]
        }]
    }
)
print(response.json()["choices"][0]["message"]["content"])
```

Testing with newspaper images shows the model can extract headlines and summarize stories, though it may occasionally hallucinate small details in dense text regions.

## Performance Considerations

| Metric | Value |
|--------|-------|
| Base VRAM | Under 8GB |
| Peak VRAM (inference) | ~43GB on 48GB card |
| Model size | 2B effective parameters |
| Context window | Configurable (default 8192) |
| Languages (audio) | 100+ |

## What This Means for Local AI

A 2-billion parameter model handling text, vision, and audio would have required a much larger model just months ago. Gemma 4 E2B represents a significant efficiency leap — making multimodal AI accessible on consumer hardware when paired with an efficient serving engine like vLLM.

Combined with an agentic framework like Hermes, you get autonomous AI capabilities running entirely on your own hardware with no cloud dependencies.

**Tags**: gemma-4, vllm, hermes-agent, local-ai, multimodal, nvidia
**Categories**: AI, Tutorials, Local AI