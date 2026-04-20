---
pubDatetime: 2026-03-08T14:00:00Z
title: "Qwen 3.5 35B & Nemotron 30B on Instinct MI50, RX 7900 XTX, and RTX 3090"
postSlug: "qwen35-nemotron-mi50-7900xtx-3090"
description: "Qwen 3.5 35B & Nemotron 30B on Instinct MI50, RX 7900 XTX, and RTX 3090"
tags:
  - rtx-3090
  - amd-mi50
  - instinct-mi50
  - gpu-benchmarks
  - llama-cpp
  - mixture-of-experts
  - qwen-3-5
  - rx-7900-xtx
  - rocm
  - cuda
  - nemotron
  - local-llm
  - open-source-ai
---

## Overview

David from Country Boy Computers tests two of the newest LLMs of 2026 -- NVIDIA's **Nemotron 3 Nano (30B)** and Alibaba's **Qwen 3.5 (35B)** -- across three very different GPU architectures: the 7-year-old AMD Instinct MI50, the Radeon RX 7900 XTX, and the NVIDIA RTX 3090. The video is a hands-on exploration of what it takes to get cutting-edge models running on older hardware using llama.cpp and ROCm 7.x, with practical build fixes and honest results.

## Test Hardware

| GPU | VRAM | Platform | Notes |
|-----|------|----------|-------|
| **AMD Instinct MI50** | 16GB HBM2 | ROCm 7.1 (GFX906) | Enterprise card from 2018 |
| **AMD Radeon RX 7900 XTX** | 24GB GDDR6 | Vulkan backend | RDNA3 consumer card |
| **NVIDIA GeForce RTX 3090** | 24GB GDDR6X | CUDA 12.8 | Ampere architecture |

CPU for MI50 bench: Intel i7-5960X (8C/16T)

## Qwen 3.5 35B: Success on MI50

### The Problem

Qwen 3.5 uses **Gated Delta Networks** -- a newer mathematical approach that the MI50's GFX906 architecture doesn't natively support. Loading the model on a fresh llama.cpp build causes a **segmentation fault**.

### The Fix

Edit `ggml-cuda.cu` in the llama.cpp source before building:

1. Open `llama-cpp/ggml/src/ggml-cuda/ggml-cuda.cu`
2. Search for `solve_try` -- there are **4 locations**
3. Comment out or set to `false`:
   - `case ggml_op_solve_try: return false`
   - Comment out `#include cuda_sol_try.ch`
   - Comment out the `case ops_solve_try` block (3 lines)
   - Comment out the 4th solve_try reference
4. Rebuild llama.cpp for GFX906

This disables the Gated Delta calculation on the GPU and falls back to CPU for those operations.

### MI50 Results - Qwen 3.5 35B

| Metric | Result |
|--------|--------|
| **Prompt processing** | ~400 tokens/sec |
| **Token generation** | **50 tokens/sec** |
| **Power draw** | 175-250W (variable) |
| **Status** | Fully working |

One gotcha: the model can get into a **response loop** around mid-generation. Fix with `--repeat-penalty 1.1` flag.

The Gated Delta offload to CPU does slow things down noticeably on the older i7-5960X, but the model runs and responds correctly.

## Nemotron 3 Nano 30B: The Unsolved Mystery

Nemotron uses a **Mamba-2 + Transformer MoE** hybrid architecture with Gated Linear Attention. This proved far more problematic across all three GPUs.

### MI50 (ROCm / HIP)

| Metric | Result |
|--------|--------|
| **Benchmark speed** | 96 tokens/sec (llama-bench) |
| **Prompt processing** | 314-325 tokens/sec |
| **Actual inference** | Outputs `special_30` tokens in an infinite loop |
| **Status** | Benchmark works, inference broken |

The model loads, benchmarks run impressively fast, but it produces no coherent text -- just repeating `special_30` tokens endlessly.

### MI50 (Vulkan)

| Metric | Result |
|--------|--------|
| **Benchmark speed** | 165-190 tokens/sec |
| **Actual inference** | Same `special_30` loop |
| **Status** | Broken |

### RX 7900 XTX (Vulkan)

| Metric | Result |
|--------|--------|
| **Benchmark speed** | **152 tokens/sec** |
| **Prompt processing** | 327-349 tokens/sec |
| **Actual inference** | 8,091 tokens generated, no coherent response |
| **Status** | Broken |

Even on a modern RDNA3 card, Nemotron fails to produce actual text output.

### RTX 3090 (CUDA 12.8)

| Metric | Result |
|--------|--------|
| **Benchmark speed** | **100 tokens/sec** |
| **Prompt processing** | 1,600-2,000 tokens/sec |
| **Actual inference** | Same `special_30` loop |
| **Context limit** | Had to reduce to 4K context, then offload 51/53 layers |
| **Status** | Broken -- even on native NVIDIA hardware |

### LM Studio (Vulkan + CUDA)

Both backends in LM Studio also fail. The model loads into VRAM but produces no coherent output regardless of backend.

### Verdict on Nemotron

Nemotron 3 Nano 30B appears to be fundamentally broken in llama.cpp at the time of recording. It's not an AMD/ROCm issue -- it fails identically on NVIDIA CUDA hardware. David suspects there's a similar trick to the Qwen fix but hasn't found it yet, and is asking the community for help.

## Key Takeaways

1. **Qwen 3.5 35B runs on a 7-year-old MI50** -- you just need to disable Gated Delta in the llama.cpp source before building for GFX906
2. **50 tokens/sec on MI50** for a 35B parameter model is genuinely impressive for 2018 hardware
3. **Nemotron 3 Nano 30B is broken across all platforms** in llama.cpp -- benchmarks run fine but inference produces garbage tokens
4. **MoE architecture saves VRAM** -- these 30-35B parameter models fit in 16-24GB because only a fraction of parameters are active per token
5. **ROCm GFX906 tensor files** are back on Arch Linux repos (they had briefly disappeared)
6. The gap between cutting-edge LLM software and older hardware can be bridged, but it takes source-level patching

## Bonus: eBay "Did You Know"

David shares an interesting aside: when you make a lowball offer on an eBay listing, if it's below the seller's secret minimum, eBay automatically rejects it -- and then **tells the buyer what the seller's minimum price is**. He questions the ethics of this from a negotiation standpoint, comparing it to his real estate background where minimum acceptable prices are kept confidential.

---

**Source**: [Country Boy Computers](https://www.youtube.com/watch?v=BIzl_kfZP6k) - Testing local LLMs on budget and enterprise AMD/NVIDIA hardware.