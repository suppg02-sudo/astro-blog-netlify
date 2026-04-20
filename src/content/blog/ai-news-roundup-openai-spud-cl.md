---
pubDatetime: 2026-04-03T22:36:58Z
title: "AI News Roundup: OpenAI Spud, Claude Mythos, Major Leaks and Open Source Drops"
postSlug: "ai-news-roundup-openai-spud-cl"
description: "AI News Roundup: OpenAI Spud, Claude Mythos, Major Leaks and Open Source Drops"
tags:
  - others
---

A comprehensive look at the biggest AI developments of the week — from Anthropic's Mythos security demos and Claude Code CLI leak, to OpenAI's upcoming Spud pre-train, and a wave of powerful open-source releases including Gemma 4 and Matrix Game 3.0.

> **TL;DR**: Anthropic demonstrated Claude finding zero-day vulnerabilities live, suffered a massive CLI source code leak, and published emotion research. OpenAI teased "Spud" — a new base pre-train 2 years in the making. Meanwhile, the open-source community delivered Gemma 4, Matrix Game 3.0, and TurboQuant model compression that halves memory requirements.

## Quick Summary

- Anthropic's Claude found a zero-day in Ghost (50k stars) and the Linux kernel in 90 minutes during a live demo
- The entire Claude Code CLI source code (500k lines) leaked via a misconfigured npm map file
- OpenAI's "Spud" is a fresh 2-year pre-train expected to move the economy — not just incremental gains
- Sora shuts down April 26 (web app), API remains until September 2026
- Google released Gemma 4 open-source with strong vision capabilities
- Matrix Game 3.0 delivers 720p/40fps interactive world generation fully open-source
- TurboQuant achieves 50% memory reduction with no apparent quality loss

## Anthropic: Mythos, Leaks, and Emotion Research

### Mythos Zero-Day Demo

Anthropic demonstrated an internal model (widely believed to be Mythos) finding a blind SQL injection zero-day in Ghost — a CMS with 50,000 GitHub stars that had never had a critical vulnerability in its history. The model stole an admin API key within 90 minutes, then replicated the feat against the Linux kernel.

The implications are staggering. If consumer-grade hardware can eventually run models with this capability level, there's no real security moat left. It's a double-edged sword: the same power that finds vulnerabilities can also help build more robust systems.

### Claude Code CLI: The Great Leak

The entire Claude Code CLI source code was accidentally exposed through a misconfigured map file in Anthropic's npm package. The leak revealed:

- **900 files, 500,000+ lines** of TypeScript code
- Complete tool system and **50 slash commands**
- Multi-agent coordinator architecture
- Full terminal UI implementation

The code was quickly mirrored on GitHub and forked before Anthropic could respond. The scaffolding turned out to be less architecturally special than many assumed — a reminder that execution and iteration often matter more than novel architecture.

### Claude's Emotion Concepts

Anthropic published research showing internal representations of emotion concepts that can directly drive Claude's behavior. By artificially dialing emotion vectors up or down, researchers could steer output — suggesting these representations aren't just correlational but functionally causal.

The key insight: you can't strip emotion from task completion. Whether coding, writing, or researching, some level of emotional processing appears necessary for the model to function effectively. These aren't real emotions — they're reflections of training data — but they serve a functional purpose.

## OpenAI: Spud, Sora Sunset, and the Super App Vision

### Spud: The Next Pre-Train

Greg Brockman revealed details about "Spud" — OpenAI's latest completed pre-train. This isn't an incremental update:

- **2 years of research** baked into a single fresh pre-train
- Expected to enable genuinely **agentic, long-horizon task completion**
- Not just 20% gains — a qualitative shift in capability
- "Big model smell" — outputs that feel fundamentally smarter

The bar is high: Spud needs to not just theorize but build. Less "here's how you could do it" and more "here's the working solution." The ceiling for complex autonomous tasks is being raised yet again.

### Sora Sunsetting

Sora's web app shuts down **April 26, 2026**. The API continues until **September 24, 2026**. The move reflects OpenAI's need to refocus compute toward revenue-generating products rather than experimental tools.

### The Super App Ambition

OpenAI's vision is shifting from a collection of AI tools to a **single AI super app** — ChatGPT, Codex, browsing, and agentic systems all working as one. The strategy: turn consumer scale into enterprise dominance and position itself as core AI infrastructure.

## Open Source Highlights

### Gemma 4

Google continues to be the most prolific major lab releasing open-source models. Gemma 4 adds strong vision capabilities — paired with object detection, it delivers fast, accurate scene descriptions. Meanwhile, OpenAI has released one model (already outdated), Anthropic releases nothing, and Meta's Llama has gone quiet.

### Bonsai 1-Bit 8B on iPhone

Prism ML's Bonsai runs a dense 8B model on an iPhone 17 Pro at **40 tokens per second** using 1-bit quantization. It's impressive engineering, though the model is reportedly hallucinatory and not production-ready. Still, any LLM running locally on a phone at chat-speed is a milestone.

### TurboQuant: 50% Memory Reduction

Google's TurboQuant is being used to compress entire models — not just KV cache. Early results show **50% memory footprint reduction** allowing Qwen 3.5 27B to run on a single RTX 5060 with no apparent degradation. We're likely nowhere near the optimization ceiling.

### Matrix Game 3.0

Skywork released Matrix Game 3.0 — a fully open-source, real-time, streaming interactive world model:

- **720p at 40fps** with a 5B parameter model
- **1-minute memory consistency** (others struggle with 15-30 seconds)
- Trained on Unreal Engine, AAA games, and real-world data
- Scales to 28B (mixture of experts)
- Runs on as low as **12GB VRAM** (low mode) or 19GB for full quality

The model generates controllable gameplay footage reminiscent of Red Dead Redemption 2, GTA 5, and Cyberpunk 2077. While vehicles and fine details show AI artifacts, the temporal consistency and controllability are remarkable for an open-source project.

## Video Generation Updates

### Seedance 2.0

Rolling out widely but **not natively in the US**. HeyGen has exclusive access for generating with any character/real people via advanced safety systems.

### Wan 2.7

Available on fal.ai and ComfyUI with audio-driven generation for near-perfect audio-visual matching. Still not open-source — a missed opportunity for maximum impact.

### Grok Imagine

xAI's video and image generation both received quality mode updates. The video mode shows cinematic detail with impressive realism. Image generation now handles vast amounts of text coherently. Not yet at Seedance 2.0 level, but rapidly improving.

### Upscaling

- **Topaz Starlight Video Upscaler** — premium AI video upscaling that noticeably improves Seedance 2.0 fidelity
- **Pruna P-Image Upscale** — up to 8MP output for ~$0.005 per image via Replicate API

## The Bigger Picture

2026 is shaping up as the year companies must prove themselves. The race has no brakes:

- **Anthropic** is sitting on potentially dangerous capability (Mythos) that could revolutionize security
- **OpenAI** is refocusing from experimentation to economic impact (Spud, super app)
- **Google** is quietly winning the open-source race (Gemma 4, TurboQuant)
- **Smaller labs** are delivering breakthroughs (Matrix Game 3.0, Bonsai)
- **Optimization** is unlocking capabilities on consumer hardware we didn't think possible

The convergence of better models, better optimization, and better tooling means we're getting closer to the dream: creating complete stories, games, and applications with AI assistance that actually works end-to-end.

---

*Source: [MattVidPro AI News](https://www.youtube.com/watch?v=HODvkLEIuFE) | Timestamps: 00:00 Intro → 00:51 Anthropic Mythos/Leaks → 06:30 Sponsor → 08:39 OpenAI Spud/Sora → 14:01 Bonsai/Gemma/TurboQuant → 16:34 Matrix Game 3.0 → 20:25 Seedance 2.0 → 21:36 Upscaling/Wan/Grok → 24:27 Outro*

**Tags**: ai-news, anthropic, openai, claude, mythos, spud, gemma, open-source, video-generation, ai-models
**Categories**: AI News, Machine Learning