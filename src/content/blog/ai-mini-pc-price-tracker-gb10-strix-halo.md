---
pubDatetime: 2026-03-01T15:15:00Z
title: "AI Mini PC Price Tracker: NVIDIA GB10 vs AMD Strix Halo (March 2026)"
postSlug: "ai-mini-pc-price-tracker-gb10-strix-halo"
description: "AI Mini PC Price Tracker: NVIDIA GB10 vs AMD Strix Halo (March 2026)"
tags:
  - nvidia
  - llm
  - inference
  - ai
  - amd
  - hardware
  - mini-pc
---

*Tracking pricing, availability, and developments for local AI inference hardware — specifically NVIDIA GB10-based systems and AMD Ryzen AI Max+ 395 (Strix Halo) mini PCs — for organisational deployment.*

---

## Executive Summary

The UK market for compact AI inference hardware capable of running 70B+ parameter LLMs locally has seen significant changes in March 2026:

- **Memory crisis**: DDR5/LPDDR5X prices up 90-110% in Q1 2026
- **NVIDIA DGX Spark price hike**: $3,999 → $4,699 (+18%) as of Feb 23, 2026
- **AMD Ryzen AI Halo**: Still no price announced, Q2 2026 launch unchanged
- **Best value**: Corsair AI Workstation 300 (Strix Halo) at £2,299 with full warranty

---

## Critical Market Alerts

### 1. Memory Crisis Impacting ALL 128GB Systems

The DRAM shortage is the single biggest factor affecting pricing:

| Metric | Value |
|--------|-------|
| DDR5/LPDDR5X Q1 2026 increase | **90-110%** |
| Framework 64GB DDR5 | $320 → **$780** (+144% since Nov 2025) |
| Samsung LPDDR5X to Apple | **100% price hike** (Feb 2026) |
| Per GB cost | ~$5 → **$12-16** |

**Impact**: Expect ALL 128GB unified memory systems to see price increases through Q2 2026.

### 2. NVIDIA DGX Spark Official Price Hike

| Period | US Price | EU Price |
|--------|----------|----------|
| Original (CES 2025) | $3,999 | €3,999 |
| **Current (Feb 23, 2026)** | **$4,699** | **€4,800** |

Memory shortages cited as the official reason. This affects all NVIDIA GB10-based systems.

### 3. AMD Ryzen AI Halo Status

| Factor | Status |
|--------|--------|
| **Price** | Not announced |
| **Pre-order** | Not available |
| **Launch** | Q2 2026 (April-June) |
| **UK Availability** | TBC |

AMD's official product page still shows only a sign-up form. No price, no pre-order, no specific launch date.

---

## NVIDIA GB10 UK Pricing (Updated March 2026)

All GB10 systems share these core specs:
- NVIDIA GB10 Grace Blackwell Superchip
- 20-core ARM CPU (10x Cortex-X925 + 10x Cortex-A725)
- NVIDIA Blackwell GPU with 5th-gen Tensor Cores
- 128GB LPDDR5X unified memory (273 GB/s bandwidth)
- 1 petaFLOP FP4 AI performance
- NVIDIA ConnectX-7 SmartNIC (2x 200Gbps QSFP)
- NVIDIA DGX OS (Ubuntu 24.04 LTS for ARM) — **Linux only**

### Price Comparison Table

| OEM | Model | Storage | UK Price | Change | Stock | Warranty |
|-----|-------|---------|----------|--------|-------|----------|
| **ASUS** | Ascent GX10 | 1TB | **£2,799.98** | Stable | Pre-order | None |
| **ASUS** | Ascent GX10 | 2TB | £3,199.99 | NEW | Pre-order | None |
| **ASUS** | Ascent GX10 | 4TB | £3,839.99 | NEW | Pre-order | None |
| **MSI** | EdgeXpert | 4TB | **£3,598.99** | — | In stock | Standard |
| **NVIDIA** | DGX Spark | 4TB | £3,699.98 | ↑ +£500 | Past due | Standard |
| **Lenovo** | ThinkStation PGX | 4TB | ~£3,800 | Stable | Limited | **Full business** |
| **Dell** | Pro Max GB10 | 2TB | **£4,093** | ↓ -£867 | Available | ProSupport |

### Key Observations

- **ASUS has NO warranty** — sold "as is"
- **Lenovo ThinkStation PGX** — only option with full business warranty
- **Dell dropped significantly** — 2TB now £4,093 (well below baseline)
- **Stock is LIMITED** across all retailers

---

## AMD Strix Halo UK Pricing (Updated March 2026)

All Strix Halo systems share these core specs:
- AMD Ryzen AI Max+ 395 APU
- 16x Zen 5 CPU cores, 32 threads, boost to 5.1GHz
- Radeon 8060S iGPU (40 RDNA 3.5 CUs)
- XDNA 2 NPU (50 TOPS dedicated, 126 TOPS total system)
- Up to 128GB LPDDR5x-8000 unified memory
- Up to 96GB allocatable as GPU VRAM
- **Windows 11 + Linux** dual-boot capable

### Price Comparison Table

| OEM | Model | RAM | Storage | UK Price | Change | Stock |
|-----|-------|-----|---------|----------|--------|-------|
| **Corsair** | AI Workstation 300 | 128GB | 4TB | **£2,299.99** | NEW | In stock |
| **Beelink** | GTR9 Pro | 128GB | 2TB | ~£1,550-1,700 | Stable | Available |
| **Minisforum** | MS-S1 Max | 128GB | 2TB | £2,639 | ↑ +£240 | **SOLD OUT** |
| **GMKtec** | EVO-X2 | 128GB | 2TB | £2,599-2,759 | — | Available |
| **Framework** | Desktop | 128GB | BYO | ~£1,700-2,000 | Pre-order | Available |

### Key Observations

- **Corsair AI Workstation 300** — best value with 2-year warranty
- **Minisforum MS-S1 Max** — price increased due to memory shortage, now sold out
- **Beelink GTR9 Pro** — cheapest option at ~£1,550

---

## ROCm vs CUDA: The Inference Ecosystem Analysis

For organisations considering GB10 (CUDA) vs Strix Halo (ROCm), the software ecosystem is as important as hardware specs.

### Ecosystem Maturity

{{< mermaid >}}
graph TD
    subgraph "NVIDIA CUDA"
        A1[PyTorch Native] --> A2[TensorRT-LLM]
        A2 --> A3[Production Ready]
        A1 --> A4[CUDA-X Libraries]
        A4 --> A5[20+ AI/HPC Libraries]
    end
    
    subgraph "AMD ROCm"
        B1[PyTorch via HIP] --> B2[vLLM ROCm]
        B2 --> B3[Improving Rapidly]
        B1 --> B4[llama.cpp HIP]
        B4 --> B5[Stable on RDNA3+]
    end
    
    style A3 fill:#90EE90
    style B3 fill:#FFD700
{{< /mermaid >}}

### Framework Support Comparison

| Framework | CUDA Status | ROCm Status | Notes |
|-----------|-------------|-------------|-------|
| **llama.cpp** | Excellent | Good | ROCm HIP backend matured significantly in late 2025 |
| **vLLM** | Excellent | Good | AMD co-developed 7 attention backends for ROCm (Feb 2026) |
| **TensorRT-LLM** | Excellent | N/A | NVIDIA-exclusive, no AMD alternative |
| **PyTorch** | Native | Via HIP | CUDA is first-party; ROCm requires compilation |
| **Ollama** | Excellent | Good | Both platforms supported |
| **LM Studio** | Excellent | Good | Both platforms supported |

### Real-World Performance

**Key Finding**: The "CUDA gap" — NVIDIA's software optimization improves hardware performance beyond raw specs. AMD's MI300X with 32% theoretical advantage often underperforms due to software optimization gaps.

#### Strix Halo Specific Benchmarks

| Model | Quantization | Tokens/sec | Notes |
|-------|--------------|------------|-------|
| Qwen 2.5 72B | Q4_K_M | ~25-30 | Usable for interaction |
| Llama 3.1 70B | Q4 | ~15-20 | Slower but functional |
| GPT-OSS 120B | MXFP4 | ~28-32 | Requires ROCm 7.x |
| Qwen3 30B MoE | Q4_K_M | ~86 | Best performance/quality |

**Critical Note**: "Running a 70B model at 3 tokens per second isn't very practical" — for 70B+ models at usable speeds, GB10 is the clear choice.

### Stability Issues

#### Current ROCm Challenges (2025-2026)

| Issue | Status | Impact |
|-------|--------|--------|
| System freezes (ROCm 7.2.0 + PyTorch) | Known bug | Critical |
| ComfyUI crashes (Kernel 6.18) | Known bug | High |
| RDNA3 HSA queue failures | Under investigation | Medium |
| bitsandbytes compilation on Strix Halo | Workaround available | Medium |

#### CUDA Advantages

- Mature driver ecosystem with 15+ years of development
- Long-term support cycles
- Enterprise-grade validation
- Extensive Stack Overflow documentation

### Recommendation Matrix

| Use Case | Recommended Platform | Reasoning |
|----------|---------------------|-----------|
| **Production/Enterprise** | NVIDIA GB10 | Stability, TensorRT-LLM, support |
| **70B+ models at speed** | NVIDIA GB10 | Memory bandwidth, ecosystem maturity |
| **Budget experimentation** | Strix Halo | 50% cost, acceptable for ≤30B models |
| **Open source contribution** | Strix Halo | Unified memory, open ecosystem |
| **Learning/Development** | Either | Both functional with effort |

---

## LLM Performance Comparison

### Benchmark Data (70B Models)

| Metric | GB10 (DGX Spark) | Strix Halo | Difference |
|--------|-------------------|------------|------------|
| **70B Q4 tokens/sec** | ~20 t/s | ~15 t/s | GB10 +33% |
| **GPT-OSS 120B tokens/sec** | ~32 t/s | ~28 t/s | GB10 +14% |
| **Price (cheapest)** | £2,800 | £1,550 | Strix 45% cheaper |
| **Price (with warranty)** | £3,810 | £2,300 | Strix 40% cheaper |
| **$/token efficiency** | Higher | **Lower** | Strix wins |

**Key insight**: Strix Halo delivers approximately **75% of the performance at 50% of the cost**.

---

## GB300: The Longer-Term Option

For awareness — not comparable to consumer mini PCs:

| Spec | GB300 DGX Station |
|------|-------------------|
| Memory | 784GB coherent (496GB LPDDR5X + 288GB HBM3e) |
| GPU | Blackwell Ultra |
| Networking | 2x 400Gb/s ConnectX-8 |
| **Price** | **$50,000-80,000+** |
| Availability | Q1 2026 shipping |

**Verdict**: GB300 is in a completely different price tier — not relevant for this decision.

---

## Decision Framework

### Weighted Criteria for Organisational Purchase

| Criterion | Weight | GB10 Advantage | Strix Halo Advantage |
|-----------|--------|----------------|---------------------|
| **Price** | 30% | | ✅ Significantly cheaper |
| **LLM inference speed (70B)** | 25% | ✅ Tensor cores + FP4 | Competitive but slower |
| **Warranty/support** | 15% | Lenovo only | Corsair, others |
| **OS flexibility** | 10% | | ✅ Windows + Linux |
| **Software ecosystem** | 10% | ✅ CUDA maturity | ROCm improving |
| **Networking/clustering** | 5% | ✅ ConnectX-7 200Gbps | Standard Ethernet |
| **General compute** | 5% | | ✅ x86, more versatile |

---

## Final Recommendations

### If You Must Buy NOW

| Priority | Option | Price | Why |
|----------|--------|-------|-----|
| **1** | **Corsair AI Workstation 300** | £2,300 | Best value Strix Halo, in stock, 2yr warranty |
| **2** | **Lenovo ThinkStation PGX** | £3,810 | Best GB10 for business (full warranty) |
| **3** | **MSI EdgeXpert 4TB** | £3,599 | Only GB10 in stock with warranty |

### If You Can Wait

| Option | Timeline | Potential Benefit |
|--------|----------|-------------------|
| **AMD Ryzen AI Halo** | Q2 2026 (1-3 months) | Could be £1,200-1,700 |
| **Memory price cooling** | Q2-Q3 2026 | 10-20% system price drops |

### For 70B+ Models Specifically

Given the benchmark data and ROCm stability concerns:
- **Production use**: NVIDIA GB10 (Lenovo ThinkStation PGX recommended)
- **Budget/experimental**: Strix Halo with ROCm 7.1+ (expect debugging)

---

## Active Monitoring Alerts

| Trigger | Status | Action |
|---------|--------|--------|
| ASUS GX10 below £2,500 | Not triggered (£2,800) | Monitor |
| Minisforum MS-S1 Max restock | SOLD OUT | Watch for restock |
| AMD Halo price announced | Pending | Monitor weekly |
| GB10 with warranty below £3,000 | Not triggered | MSI closest at £3,599 |
| ROCm 7.3 stability release | Pending | Monitor GitHub |

---

## Next Update: Week of 8 March 2026

**Priority sources:**
1. AMD Ryzen AI Halo product page — any price announcement
2. Scan UK — ASUS/MSI stock and price changes
3. Minisforum UK — MS-S1 Max restock status
4. ROCm GitHub — stability improvements for RDNA 3.5

---

## Sources

### Hardware Pricing
- [Scan UK - ASUS Ascent GX10](https://www.scan.co.uk/products/asus-ascent-gx10-desktop-ai-supercomputer-gb10-blackwell-superchip-128gb-lpddr5x-1tb-ssd-cx7)
- [Minisforum UK](https://www.minisforum.uk/products/minisforum-ms-s1-max)
- [Corsair UK - AI Workstation 300](https://www.corsair.com/uk/en/p/gaming-computers/cs-9080002-pe/)
- [NVIDIA Forums - Price Change](https://forums.developer.nvidia.com/t/2-23-2026-price-change-announcement/361713)

### Memory Pricing
- [NotebookCheck - Samsung LPDDR5X Price Hike](https://www.notebookcheck.net/Samsung-slaps-Apple-with-100-price-increase-for-LPDDR5X-memory-modules.1235631.0.html)
- [TechRadar - DRAM Prices to Double](https://www.techradar.com/pro/dram-prices-set-to-almost-double-by-march-2026)
- [PCMag - Framework Price Increases](https://www.pcmag.com/news/ugh-framework-needs-to-raise-prices-again-blaming-memory-shortage)

### ROCm vs CUDA Analysis
- [GPUnex - NVIDIA vs AMD GPUs 2026](https://www.gpunex.com/blog/nvidia-vs-amd-gpus-2026/)
- [AIMultiple - CUDA vs ROCm 2026](https://research.aimultiple.com/cuda-vs-rocm/)
- [vLLM Blog - ROCm Attention Backend](https://blog.vllm.ai/2026/02/27/rocm-attention-backend.html)
- [Hardware Corner - Strix Halo LLM Performance](https://www.hardware-corner.net/how-fast-ai-max-395-llm-20250317/)
- [Tom's Hardware - AMD ROCm CES 2026](https://www.tomshardware.com/pc-components/gpu-drivers/amd-rocm-ces-2026-press-q-and-a-roundtable-transcript)

### Benchmarks
- [GitHub/visorcraft - Strix Halo LLM Performance](https://github.com/visorcraft/strix-halo-llm-perf)
- [Hardware-Corner.net - DGX Spark Benchmarks](https://www.hardware-corner.net/first-dgx-spark-llm-benchmarks/)
- [ServeTheHome - MS-S1 Max Review](https://www.servethehome.com/minisforum-ms-s1-max-review-the-best-ryzen-ai-max-mini-pc-yet/)

---

*Research completed: 1 March 2026, 15:15 UTC*
*Next update scheduled: 8 March 2026*