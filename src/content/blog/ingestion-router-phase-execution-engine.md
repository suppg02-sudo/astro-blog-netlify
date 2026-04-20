---
pubDatetime: 2026-04-08T01:43:25Z
title: "Ingestion Router — From Broken Detection to Phase Execution Engine"
postSlug: "ingestion-router-phase-execution-engine"
description: "Comprehensive review and rebuild of the ingestion router — fixing detection chains, adding file extraction, building phase engines, and wiring real skill integrations."
tags:
  - directus
  - ingestion-router
  - automation
  - architecture
  - phase-engine
---

<style>
.sev-section { border-radius: 6px; margin: 1.2rem 0; overflow: hidden; border: 1px solid; }
.sev-neutral { border-color: #6b7280; background: rgba(107,114,128,0.04); }
.sev-neutral > summary { background: rgba(107,114,128,0.08); color: #4b5563; }
.sev-positive { border-color: #22c55e; background: rgba(34,197,94,0.04); }
.sev-positive > summary { background: rgba(34,197,94,0.12); color: #16a34a; }
.sev-action { border-color: #3b82f6; background: rgba(59,130,246,0.04); }
.sev-action > summary { background: rgba(59,130,246,0.12); color: #2563eb; }
.sev-section > summary { padding: 0.6rem 1rem; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 0.5rem; list-style: none; }
.sev-section > summary::-webkit-details-marker { display: none; }
.sev-section > summary::before { content: '▶'; font-size: 0.75rem; transition: transform 0.15s; }
.sev-section[open] > summary::before { transform: rotate(90deg); }
.sev-body { padding: 0.8rem 1rem; }
.summary-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(120px,1fr)); gap: 0.6rem; margin: 0.5rem 0; }
.summary-card { border-radius: 6px; padding: 0.6rem 0.8rem; text-align: center; }
.summary-card .sc-val { font-size: 1.4em; font-weight: 700; }
.summary-card .sc-label { font-size: 0.75em; opacity: 0.7; margin-top: 0.15rem; }
.sc-red { background: rgba(239,68,68,0.1); color: #dc2626; }
.sc-amber { background: rgba(245,158,11,0.1); color: #b45309; }
.sc-green { background: rgba(34,197,94,0.1); color: #16a34a; }
.sc-blue { background: rgba(59,130,246,0.1); color: #2563eb; }
img { border-radius: 6px; }
</style>

> **TL;DR**: The ingestion router handles all URLs/files pasted into chat. We reviewed it, fixed broken detection, added file extraction, built a phase execution engine, wired real skill integrations, and visualised the architecture.

## Quick Summary

- **6 input types**: YouTube, GitHub, News, Shop, Web URL, File
- **33 flows**: Multi-select workflows with shared phase deduplication
- **3 scripts**: Transcript extraction, MeTube downloads, file processing
- **Phase engine**: 834-line Python execution engine with state tracking
- **Skill integrations**: Real calls to astro (Directus), erag (PostgreSQL), Telegram, hybrid tracker

## Architecture Overview

The ingestion router operates as a two-stage pipeline: content extraction feeds into an execution engine that orchestrates multi-skill workflows.

```
🔴 Input Detected → 🟠 Classify (6 patterns) → 🟡 Menu (multi-select) → 🟢 Phase Engine → 🔵 Report
```

<div class="summary-grid">
<div class="summary-card sc-blue"><div class="sc-val">📥 6</div><div class="sc-label">Input Types</div></div>
<div class="summary-card sc-green"><div class="sc-val">📋 33</div><div class="sc-label">Flows</div></div>
<div class="summary-card sc-green"><div class="sc-val">🎯 16</div><div class="sc-label">Phase Templates</div></div>
<div class="summary-card sc-amber"><div class="sc-val">🔧 3</div><div class="sc-label">Scripts</div></div>
</div>

## Detection Chain (Fixed)

The biggest issue found: News and Shop URLs were never matching because the generic `https://` pattern intercepted them first. Fixed by reordering the detection priority:

| Priority | Type | Pattern |
|----------|------|---------|
| 1 | 🎥 YouTube | `youtube.com/watch`, `youtu.be/`, `shorts/` |
| 2 | 🐙 GitHub | `github.com/{owner}/{repo}` |
| 3 | 📰 News | `bbc.co.uk`, `theguardian.com`, `reuters.com` |
| 4 | 🛒 Shop | `tesco.com`, `sainsburys.co.uk`, `asda.com` |
| 5 | 🌐 Web URL | Catch-all `https://` fallback |
| 6 | 📎 File | `.pdf`, `.docx`, `.csv`, `.xlsx`, `.png`, `.jpg` |

All 17 detection test cases pass after the fix.

## File Extraction (New)

Created `scripts/extract-file-content.py` — a unified processor for all file types:

| Format | Method | Notes |
|--------|--------|-------|
| PDF | `pdftotext -layout` | Preserves formatting, extracts page count |
| DOCX | Python `python-docx` | Extracts paragraphs + tables |
| CSV | Python stdlib `csv` | Structured data extraction |
| XLSX | Python `openpyxl` | Multi-sheet support |
| PNG/JPG | Tesseract OCR | Optical character recognition |
| TXT/MD | Direct read | UTF-8 with error replacement |

Output is structured JSON: `{"status": "ok", "content": "...", "words": N, "file_type": "pdf"}`

## Phase Execution Engine

The 834-line `scripts/phase_engine.py` transforms phase labels from YAML into real execution:

```
🔴 Input (file) → 🟠 2 flows selected (1 shared) → 🟢 Execute → 🔵 Report
  🔗 🟡 Extracting content...
    ✅ Done (7 words)
  🟢 Summarising...
    ✅ Done (4 words summarized)
  🟢 Ingesting to eRAG...
    ✅ Done (4 words ingested)
```

**Key capabilities:**
- **Shared phase deduplication** — extract runs once for multiple flows
- **State persistence** — full audit trail at `/tmp/flow-exec-<timestamp>/`
- **Error handling** — stops on failure, reports what succeeded
- **CLI interface** — `execute`, `status`, `history` commands

## Skill Integrations

Replaced placeholders with real skill calls:

| Phase | Integration | Status |
|-------|-------------|--------|
| extract | MeTube yt-dlp + file processor | ✅ Real |
| download | MeTube API (queue + poll) | ✅ Real |
| summarise | LLM placeholder | ⏳ Content ready |
| publish | `publish_to_directus.py` (Directus) | ✅ Real |
| notify | Telegram Bot API | ✅ Real |
| ingest | eRAG PostgreSQL + pgvector | ✅ Real |
| attach | Hybrid tracker | ✅ Real |

## Architecture: Import vs Selection

Two distinct architectures work in concert:

- **Import** (automatic) — regex detection → extract content → output JSON
- **Selection** (user-driven) — menu builder → multi-select → phase engine → orchestrate skills

The import architecture feeds structured content into the selection architecture. User choices determine what happens with that content.

## Results

- **33 flows** across 6 input types, consolidated from 34
- **16 phase templates** standardised across all flow types
- **Zero dead fields** — removed `project_target`, YAML `mandatory`
- **Standardised IDs** — all eRAG flows use `erag-research`
- **Detection working** — all 17 test cases pass
- **Visual companion** — interactive architecture diagram at port 51365
