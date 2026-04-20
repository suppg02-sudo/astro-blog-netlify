---
pubDatetime: 2026-04-08T07:41:28Z
title: "The Brainplane: Building a Self-Improving AI Pipeline"
postSlug: "the-brainplane-building-a-self"
description: "The Brainplane: Building a Self-Improving AI Pipeline"
tags:
  - others
---

> **TL;DR**: We are building an autonomous knowledge engine that transforms messy raw data into a structured "Wiki" the AI can read. It doesn't just store data; it improves it.

## The Problem: Death by Information
Every day, active research projects ingest massive amounts of data from RSS feeds, transcripts, and files. Without a brain, this becomes a "wall of noise" — data that is impossible to query and too noisy to act on.

## The Architecture: 3 Tiers

<div class="summary-grid">
<div class="sc-amber"><div class="sc-val">40k+</div><div class="sc-label">Daily Tokens</div></div>
<div class="sc-green"><div class="sc-val">2</div><div class="sc-label">Cleaning Modes</div></div>
<div class="sc-blue"><div class="sc-val">3</div><div class="sc-label">Wiki Folders</div></div>
</div>

### Tier 1: Raw Ingestion (The Senses)
We collect everything: chat logs, code changes, news, and transcripts. It lands in the `raw/` directory without filtering.
**Status:** ✅ Operational.

### Tier 2: The Watchdog (The Brain)
This is the engine that transforms "Raw" into "Wiki". It operates in two modes:
*   **The Active Hook:** At the end of every work session, an Agent reviews what we did, extracts decisions/lessons, and proposes updates to `wiki/projects/`.
*   **The Nightly Sweep:** A background process reviews `raw/` data (news, logs) and updates `wiki/domain/` with synthesized facts.
**Status:** 🚧 Kernel Implemented (Script created, LLM integration pending).

### Tier 3: The Wiki (The Vault)
A structured Markdown folder that serves as the AI's long-term memory.
*   `wiki/projects/`: Operational Memory ("We pivoted the consultancy model yesterday").
*   `wiki/architecture/`: Technical Knowledge ("Here is how the Schema Registry works").
*   `wiki/domain/`: External Context ("Iran ceasefire confirmed on Apr 8").
**Status:** ✅ Operational (Structure established, population starting).

## Current Status: Building the Kernel
We have built the **Ingestion** (Tier 1), established the **Wiki Structure** (Tier 3), and implemented the **Active Hook Kernel** (Tier 2). 

The next sprint is to wire the Agent to automatically call the `brainplane_cleaner.py` at the end of sessions to keep the Wiki alive.