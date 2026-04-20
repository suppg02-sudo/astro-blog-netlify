---
pubDatetime: 2026-03-07T15:15:00Z
title: "Automated GitHub Links Consolidation for Memos"
postSlug: "automated-github-links-consolidation-memos"
description: "How I built an automated system to consolidate GitHub link memos into a master pinned memo using Python, the Memos API, and cron"
tags:
  - productivity
  - memos
  - cron
  - automation
  - python
---

## The Problem

I use [Memos](https://usememos.com) extensively for quick notes and link saving. Over time, I've accumulated dozens of short memos that are just GitHub links or primarily contain GitHub repository references. While these are valuable, they clutter my memo feed and make it harder to find longer-form notes.

What I needed:
1. **Consolidate** GitHub link memos into one master memo
2. **Pin** the master memo to the top for easy access
3. **Archive** the original short memos after consolidation
4. **Automate** this process to run daily

## The Solution

I built a Python script that:
- Scans all memos for GitHub links
- Identifies "GitHub-heavy" memos (≥2 links or <100 chars of non-GitHub content)
- Consolidates links into a master pinned memo
- Archives the original memos
- Runs automatically via cron

## Implementation

### 1. The Python Script

**File**: `/media/docker/commands/consolidate-github-memos.py`

```python
#!/usr/bin/env python3
"""
Daily GitHub Links Consolidation Script
Analyzes memos with GitHub links, consolidates them into a pinned master memo,
and archives the original memos.
```

**Key Features**:
- **Smart Detection**: Uses regex to find GitHub URLs and calculates if they're the primary content
- **Deduplication**: Tracks existing links to avoid duplicates
- **Master Memo**: Creates or updates a pinned master memo with all links
- **Safe Archiving**: Only archives after confirming links were added
- **Dry-Run Mode**: Preview changes before executing
- **Detailed Logging**: Tracks every action for audit trail

**Detection Logic**:
```python
# A memo is considered "GitHub-heavy" if:
# 1. Contains 2+ GitHub links, OR
# 2. Has <100 chars of non-GitHub content

github_links = self.github_pattern.findall(content)
content_without_github = self.github_pattern.sub("", content).strip()
is_primary = len(content_without_github) < 100 or len(github_links) >= 2
```

### 2. Memos API Integration

The script uses the [Memos REST API](https://usememos.com/docs/api):

**Authentication**:
```bash
Authorization: Bearer YOUR_PAT_TOKEN
```

**Key Endpoints**:
- `GET /api/v1/memos` - List all memos (with pagination)
- `POST /api/v1/memos` - Create new memo
- `PATCH /api/v1/memos/{id}?updateMask=content,pinned,state` - Update memo
- Filter syntax: `content.contains('github.com')`

**Pagination Handling**:
```python
while True:
    params = {"pageSize": 100, "state": "NORMAL"}
    if page_token:
        params["pageToken"] = page_token
    
    result = self.api_request("GET", "/api/v1/memos", params=params)
    all_memos.extend(result["memos"])
    
    if not result.get("nextPageToken"):
        break
    page_token = result["nextPageToken"]
```

### 3. Shell Wrapper Script

**File**: `/media/docker/commands/consolidate-github-memos.sh`

```bash
#!/bin/bash
set -euo pipefail

# Load environment variables
source "${SCRIPT_DIR}/.env"

# Run consolidation with logging
python3 "${PYTHON_SCRIPT}" \
    --url "${MEMOS_URL}" \
    --token "${MEMOS_PAT}" \
    "$@" 2>&1 | tee -a "${LOG_FILE}"
```

**Features**:
- Environment variable management via `.env`
- Automatic Python dependency installation
- Structured logging to `/var/log/memos-consolidation/`
- Error handling with proper exit codes

### 4. Configuration

**File**: `/media/docker/commands/.env`

```bash
MEMOS_URL=http://localhost:5230
MEMOS_PAT=your_pat_token_here
```

**Getting Your PAT Token**:
1. Open `http://localhost:5230` (or your Memos URL)
2. Navigate to Settings → Access Tokens
3. Create a new token with description "GitHub Consolidation"
4. Copy the token to your `.env` file

### 5. Cron Setup

**File**: `/media/docker/commands/setup-cron.sh`

Interactive script to set up daily automation:

```bash
./setup-cron.sh

# Options:
# 1) Daily at 2:00 AM (recommended)
# 2) Daily at 8:00 AM
# 3) Every 12 hours
# 4) Custom schedule
```

**Resulting Crontab Entry**:
```
0 2 * * * /media/docker/commands/consolidate-github-memos.sh >> /var/log/memos-consolidation/cron.log 2>&1
```

## Usage

### First-Time Setup

```bash
cd /media/docker/commands

# 1. Create configuration
cp .env.example .env
nano .env  # Add your PAT token

# 2. Run setup verification
./setup-consolidation.sh

# 3. Test with dry-run
./consolidate-github-memos.sh --dry-run --verbose

# 4. Run for real
./consolidate-github-memos.sh

# 5. Set up cron job
./setup-cron.sh
```

### Manual Execution

```bash
# Dry-run (preview changes)
./consolidate-github-memos.sh --dry-run --verbose

# Execute consolidation
./consolidate-github-memos.sh

# View logs
tail -f /var/log/memos-consolidation/cron.log
```

## Example Output

```
[2026-03-07 15:10:00] [INFO] Starting GitHub links consolidation...
[2026-03-07 15:10:01] [INFO] Fetching all memos...
[2026-03-07 15:10:02] [INFO] Retrieved 156 total memos
[2026-03-07 15:10:02] [INFO] Found 23 memos with GitHub links
[2026-03-07 15:10:02] [INFO] Found existing master memo: memos/abc123
[2026-03-07 15:10:03] [INFO] Updated master memo with 45 new links
[2026-03-07 15:10:04] [INFO] Archived memo memos/def456
[2026-03-07 15:10:04] [INFO] Archived memo memos/ghi789
...
[2026-03-07 15:10:15] [INFO] === CONSOLIDATION COMPLETE ===
[2026-03-07 15:10:15] [INFO] Memos checked: 156
[2026-03-07 15:10:15] [INFO] GitHub memos found: 23
[2026-03-07 15:10:15] [INFO] Links added: 45
[2026-03-07 15:10:15] [INFO] Memos archived: 22
```

## The Master Memo

The consolidated memo looks like this:

```markdown
📚 GitHub Links Collection

#github-links #curated

This is an automatically curated collection of GitHub links from short memos.

**Last Updated**: 2026-03-07 15:10:00

---

## GitHub Repositories

### Added 2026-03-07 15:10:00
- https://github.com/usememos/memos
- https://github.com/darrenhinde/OpenAgentsControl
- https://github.com/opencode-ai/opencode
...

---

[Previous sections preserved]
```

## Benefits

1. **Cleaner Feed**: Short link-only memos are archived, leaving room for substantial notes
2. **Easy Access**: Pinned master memo is always at the top
3. **Deduplication**: Same link appearing in multiple memos is consolidated
4. **Audit Trail**: Detailed logs track every action
5. **Fully Automated**: Runs daily without manual intervention
6. **Safe**: Dry-run mode and verification before archiving

## Technical Details

### GitHub Link Detection

Regex pattern used:
```python
r'https?://(?:www\.)?github\.com/[\w\-]+/[\w\-]+(?:/[\w\-/]+)?'
```

Matches:
- `https://github.com/user/repo`
- `https://github.com/user/repo/issues/123`
- `https://github.com/user/repo/pull/456`
- `http://www.github.com/user/repo`

### API Rate Limiting

The script handles pagination and rate limiting:
- PageSize: 100 memos per request
- Respects `nextPageToken` for pagination
- 30-second timeout per request
- Exponential backoff on failures (via wrapper script)

### Error Handling

1. **API Failures**: Logged and script exits with error code
2. **Missing Token**: Clear error message with instructions
3. **Network Issues**: Timeout handling with retry logic
4. **Archiving Failures**: Original memos preserved if consolidation fails

## Files Created

```
/media/docker/commands/
├── consolidate-github-memos.py    # Main Python script
├── consolidate-github-memos.sh    # Shell wrapper
├── setup-consolidation.sh         # Setup and verification
├── setup-cron.sh                  # Cron job installer
├── .env                           # Configuration (PAT token)
└── .env.example                   # Configuration template

/var/log/memos-consolidation/
├── cron.log                       # Cron execution log
└── consolidation-YYYYMMDD.log     # Daily detailed logs
```

## Future Enhancements

1. **Category Detection**: Auto-categorize links (repos, issues, PRs, discussions)
2. **Tag Extraction**: Add tags based on repo topics
3. **Summary Generation**: Use AI to summarize repo purposes
4. **Duplicate Detection**: Better fuzzy matching for similar repos
5. **Export Options**: Export to Markdown files, Hugo posts, or other formats

## Integration with OpenCode

This solution integrates with my [OpenCode](https://opencode.ai) setup:
- Added to `/media/docker/commands/` alongside other automation scripts
- Logs stored in standard location for easy access
- Environment variables managed via `.env` file
- Can be triggered manually or via cron

## Related Skills

This functionality is now available as a menu option in the **Memos Skill**:
- Trigger word: `memos`
- Menu option: "🔗 Consolidate GitHub Links"

---

## Conclusion

This automated consolidation system keeps my Memos feed clean while preserving valuable GitHub links in an organized, accessible format. The combination of Python's flexibility, Memos' REST API, and cron's reliability creates a robust solution that runs unattended and provides detailed logging.

The best part? I can always find my GitHub links in one place - the pinned master memo at the top of my feed.

---

**Files**:
- [consolidate-github-memos.py](http://ubuntu4:8080/editor/docker/commands/consolidate-github-memos.py)
- [consolidate-github-memos.sh](http://ubuntu4:8080/editor/docker/commands/consolidate-github-memos.sh)
- [setup-consolidation.sh](http://ubuntu4:8080/editor/docker/commands/setup-consolidation.sh)
- [setup-cron.sh](http://ubuntu4:8080/editor/docker/commands/setup-cron.sh)
- [.env.example](http://ubuntu4:8080/editor/docker/commands/.env.example)

**Resources**:
- [Memos API Documentation](https://usememos.com/docs/api)
- [Memos GitHub Repository](https://github.com/usememos/memos)
- [CEL Filter Syntax](https://google.aip.dev/160)