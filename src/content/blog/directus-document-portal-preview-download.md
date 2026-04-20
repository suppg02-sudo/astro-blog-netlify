---
pubDatetime: 2026-04-03T23:40:50Z
title: "Building a Document Portal with Directus: Preview and Download in Action"
postSlug: "directus-document-portal-preview-download"
description: "A working demo of document preview and download links using the Directus DMS — with live examples from our Finance category."
tags:
  - directus
  - homelab
  - document-management
  - rest-api
  - tutorial
---

# Building a Document Portal with Directus: Preview and Download in Action

In my previous post, I walked through setting up Directus as a document management system. Now I want to show you what it looks like in practice — specifically, how to embed document previews and download links in a web portal.

This post demonstrates the exact setup: two documents stored in our Directus DMS, with both inline preview (where supported) and download links.

## The Documents in Our DMS

We have two sample documents in the Finance category:

| Document | Type | Category | File Size |
|----------|------|----------|-----------|
| Q1-Q4 2026 Financial Data | excel (CSV) | Finance | 136 bytes |
| 2026 Financial Summary | markdown | Finance | ~500 bytes |

## Live Preview and Download

Below is a working demo of document rendering in Directus. The first document is a CSV file containing quarterly financial data. Since Directus can serve any file type, but only renders images and PDFs inline, you'll see the CSV content rendered as a table below (manually parsed from the file), with a download link for the original.

### Document 1: Q1-Q4 2026 Financial Data

**File**: `q1-q4-2026-financial.csv`  
**Type**: CSV/Excel  
**Category**: Finance  
**Size**: 136 bytes  
**Uploaded**: April 3, 2026

#### Live Download Link
[📥 Download Q1-Q4 2026 Financial Data](http://ubuntu4:8055/assets/180fc12d-6dcb-4208-9e3f-28bae7b20730)

#### Rendered Preview (parsed from CSV)
```
Quarter,Revenue,Expenses,Profit
Q1 2026,50000,32000,18000
Q2 2026,55000,35000,20000
Q3 2026,62000,38000,24000
Q4 2026,68000,41000,27000
```

### Document 2: 2026 Financial Summary

**File**: `financial-summary.md`  
**Type**: Markdown  
**Category**: Finance  
**Uploaded**: April 3, 2026

#### Live Download Link
[📥 Download 2026 Financial Summary](http://ubuntu4:8055/assets/abcf8160-a239-476b-8bf5-6be4175892e7)

#### Rendered Preview

# Q1-Q4 2026 Financial Summary

## Overview
This document contains quarterly financial data for the fiscal year 2026.

## Data Summary
- **Total Revenue**: $235,000
- **Total Expenses**: $146,000
- **Net Profit**: $89,000

## Methodology
Data extracted from accounting system on December 31, 2026.

---

## How the Download Links Work

Every file uploaded to Directus gets a unique ID and is served via the `/assets/{file_id}` endpoint. Here's how to construct download links:

```
https://your-directus.com/assets/{file_id}
```

In our case, the Directus instance runs at `http://ubuntu4:8055`, so the full URLs are:

- **Q1-Q4 2026 Financial Data**: `http://ubuntu4:8055/assets/180fc12d-6dcb-4208-9e3f-28bae7b20730`
- **2026 Financial Summary**: `http://ubuntu4:8055/assets/abcf8160-a239-476b-8bf5-6be4175892e7`

These links work without authentication for public collections (or when the public role has read access). For private documents, you'd add the auth token.

## Adding Download Links to Your Own App

If you're building a portal that uses the Directus DMS, here's the pattern:

```javascript
// Fetch documents from Directus
const response = await fetch(
  'http://localhost:8055/items/documents?fields=id,title,file_id.filename_download,file_id.id',
  { headers: { 'Authorization': 'Bearer YOUR_TOKEN' } }
);
const { data } = await response.json();

// Render download links
data.forEach(doc => {
  const fileId = doc.file_id.id;
  const filename = doc.file_id.filename_download;
  console.log(`<a href="/assets/${fileId}">Download ${filename}</a>`);
});
```

The `file_id` field is a many-to-one relation to `directus_files`, so you get the full file object including `id`, `filename_download`, `filesize`, `type`, and more.

## What Renders Inline vs. What Downloads

Directus handles different file types differently:

| File Type | Inline Preview | Download Available |
|-----------|---------------|-------------------|
| Images (png, jpg, gif, webp, svg) | ✅ Yes | ✅ Yes |
| PDF | ✅ Yes | ✅ Yes |
| CSV/TXT | ❌ No | ✅ Yes |
| Markdown | ❌ No (renders as text) | ✅ Yes |
| Word/Excel/PPT | ❌ No | ✅ Yes |
| ZIP/Archives | ❌ No | ✅ Yes |

For a richer preview experience (especially for Office documents), you'd need to integrate OnlyOffice or Collabora Online — but for a lightweight document portal, the download-first approach works well.

## The CLI Makes This Easy

All of this is manageable from the command line using our `dms` tool:

```bash
# Upload a new document
dms upload quarterly-report.xlsx "Q4 2026 Report" Finance

# List all documents
dms list

# Get a specific document's details
dms get <document-id>

# Download a file
dms download <document-id> ./downloads/
```

The CLI handles file type detection, category assignment, and API interaction — giving you a terminal-first workflow for document management while the web portal handles display and downloads.

## What's Next

This document portal is functional but minimal. Possible enhancements:

- **Full-text search** — Add a search overlay that queries title, description, and tags
- **Bulk operations** — Select multiple documents for zip download
- **Version history** — Track document versions (the `version` field is already in the schema)
- **Office rendering** — Deploy OnlyOffice for in-browser Word/Excel editing
- **Preview thumbnails** — Generate preview images for documents

For now, the core workflow is solid: upload via CLI or API, categorise and tag, then serve download links from any web app. Simple, API-driven, and extensible.

**Tags**: directus, document-management, tutorial, rest-api, homelab
**Categories**: Tutorials, Infrastructure
