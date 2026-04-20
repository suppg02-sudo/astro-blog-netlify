---
pubDatetime: 2026-02-09T20:20:00Z
title: "Backing Up Memos to GitHub: SQLite Database Export and Restore Strategy"
postSlug: "backing-up-memos-database-to-github"
description: "Backing Up Memos to GitHub: SQLite Database Export and Restore Strategy"
tags:
  - github
  - memos
  - backup
  - sqlite
  - note-taking
  - database
  - devops
  - git
---

## The Challenge: Backing Up a Note-Taking Database

Unlike blog posts stored as markdown files, **Memos stores everything in a SQLite database**. This means:

- ✅ All notes, tags, metadata in one file
- ✅ Efficient storage and querying
- ❌ Can't just `git add *.md` to version control
- ❌ Database is binary — not human-readable in git diffs

Today I solved this by creating a **SQL export backup strategy** that captures all your Memos data in a restorable format.

## The Architecture

{{< mermaid >}}
graph TD
    A["Memos Container<br/>Port 5230"] -->|"Reads/Writes"| B["SQLite Database<br/>memos_prod.db"]
    B -->|"Export"| C["SQL Dump<br/>memos_prod_backup_*.sql"]
    C -->|"Commit"| D["Git Repository<br/>/media/docker/memos"]
    D -->|"Push"| E["GitHub<br/>suppg022312/memos-backup"]
    E -->|"Restore"| F["New memos_prod.db<br/>or Query specific notes"]
{{< /mermaid >}}

## What's Being Backed Up

| Component | Location | Size | Backed Up? |
|-----------|----------|------|-----------|
| **SQLite Database** | `/media/docker/memos/data/memos_prod.db` | 200KB | ✅ Via SQL export |
| **SQL Dump** | `/media/docker/memos/data/memos_prod_backup_*.sql` | 97KB | ✅ Direct commit |
| **Docker Config** | `/media/docker/memos/docker-compose.yml` | 1KB | ✅ Committed |
| **Documentation** | `/media/docker/memos/AGENTS.md`, `SETUP.md` | 20KB | ✅ Committed |
| **Thumbnails** | `/media/docker/memos/data/.thumbnail_cache/` | ~1MB | ❌ Regenerable |

## The Backup Process

### Step 1: Export Current Database to SQL

```bash
cd /media/docker/memos/data
sqlite3 memos_prod.db ".dump" > memos_prod_backup_$(date +%Y%m%d_%H%M%S).sql
```

This creates a timestamped SQL file containing:
- All table schemas
- Every note with content, metadata, timestamps
- User information and permissions
- Tags and relationships
- Complete database state

### Step 2: Commit to Git

```bash
cd /media/docker/memos
git add data/memos_prod_backup_*.sql docker-compose.yml AGENTS.md SETUP.md
git commit -m "Add Memos database backup and configuration to version control"
```

### Step 3: Push to GitHub

```bash
git remote add github https://github.com/suppg022312/memos-backup.git
git push -u github main
```

## Restoring Your Memos

### Scenario 1: Full Database Restore

If your `memos_prod.db` is corrupted or lost, restore from the SQL backup:

```bash
# Stop the Memos container
docker stop memos

# Backup the corrupted database (just in case)
cp /media/docker/memos/data/memos_prod.db /media/docker/memos/data/memos_prod.db.corrupted

# Create a fresh database from the SQL dump
sqlite3 /media/docker/memos/data/memos_prod.db < /media/docker/memos/data/memos_prod_backup_20260209_201727.sql

# Restart the container
docker start memos

# Verify Memos is accessible
curl http://localhost:5230/api/v1/ping
```

### Scenario 2: Extract a Single Memo

If you need to recover just one specific memo without restoring the entire database:

```bash
# Query the SQL dump for a specific memo by title
sqlite3 /media/docker/memos/data/memos_prod_backup_20260209_201727.sql \
  "SELECT id, content, created_ts, updated_ts FROM memo WHERE content LIKE '%search-term%';"
```

Or extract by memo ID:

```bash
sqlite3 /media/docker/memos/data/memos_prod_backup_20260209_201727.sql \
  "SELECT content FROM memo WHERE id = 123;"
```

### Scenario 3: Export All Memos as Markdown

Create a markdown file from all your memos:

```bash
sqlite3 /media/docker/memos/data/memos_prod_backup_20260209_201727.sql \
  "SELECT '# ' || content || '\n\n' || datetime(created_ts, 'unixepoch') || '\n\n---\n\n' FROM memo ORDER BY created_ts DESC;" \
  > all_memos_export.md
```

### Scenario 4: Restore to a Different Machine

Clone the backup repo and restore on a new server:

```bash
# Clone the backup repository
git clone https://github.com/suppg022312/memos-backup.git
cd memos-backup

# Create the data directory
mkdir -p data

# Restore the database
sqlite3 data/memos_prod.db < data/memos_prod_backup_20260209_201727.sql

# Start Memos with Docker
docker-compose up -d

# Verify
curl http://localhost:5230/api/v1/ping
```

## Advanced: Querying the SQL Dump

The SQL dump is a complete SQLite database schema. You can query it without restoring:

### Get all memos with their tags

```bash
sqlite3 /media/docker/memos/data/memos_prod_backup_20260209_201727.sql << 'EOF'
SELECT 
  m.id,
  m.content,
  GROUP_CONCAT(t.tag_name, ', ') as tags,
  datetime(m.created_ts, 'unixepoch') as created
FROM memo m
LEFT JOIN memo_tag mt ON m.id = mt.memo_id
LEFT JOIN tag t ON mt.tag_id = t.id
GROUP BY m.id
ORDER BY m.created_ts DESC;
EOF
```

### Count memos by month

```bash
sqlite3 /media/docker/memos/data/memos_prod_backup_20260209_201727.sql \
  "SELECT strftime('%Y-%m', datetime(created_ts, 'unixepoch')) as month, COUNT(*) as count FROM memo GROUP BY month ORDER BY month DESC;"
```

### Find memos by date range

```bash
sqlite3 /media/docker/memos/data/memos_prod_backup_20260209_201727.sql \
  "SELECT content, datetime(created_ts, 'unixepoch') FROM memo WHERE created_ts BETWEEN 1707000000 AND 1707086400 ORDER BY created_ts DESC;"
```

## Automation: Regular Backups

To ensure your Memos are always backed up, add a cron job:

```bash
# Edit crontab
crontab -e

# Add this line to backup daily at 2 AM
0 2 * * * cd /media/docker/memos/data && sqlite3 memos_prod.db ".dump" > memos_prod_backup_$(date +\%Y\%m\%d_\%H\%M\%S).sql && cd /media/docker/memos && git add data/memos_prod_backup_*.sql && git commit -m "Daily Memos backup" && git push github main 2>&1 | logger -t memos-backup
```

This will:
- Export the database daily
- Commit new backups to git
- Push to GitHub automatically
- Log any errors

## The Complete Backup Strategy

{{< mermaid >}}
graph LR
    subgraph "Local"
        A["Memos Container<br/>Port 5230"]
        B["SQLite DB<br/>memos_prod.db"]
        C["Git Repo<br/>/media/docker/memos"]
    end
    subgraph "GitHub"
        D["suppg022312/memos-backup<br/>Private Repository"]
    end
    subgraph "Restore Options"
        E["Full DB Restore"]
        F["Single Memo Extract"]
        G["Markdown Export"]
        H["Query via SQL"]
    end
    A -->|"Stores data"| B
    B -->|"Export to SQL"| C
    C -->|"Push"| D
    D -->|"Clone"| E
    D -->|"Query"| F
    D -->|"Transform"| G
    D -->|"Direct SQL"| H
{{< /mermaid >}}

## Key Takeaways

1. **SQLite databases need special handling** — they're binary files, so export to SQL for version control
2. **SQL dumps are portable** — restore on any machine with SQLite installed
3. **Queries work on dumps** — no need to restore to extract specific data
4. **Automation is essential** — daily backups ensure you never lose recent notes
5. **GitHub provides redundancy** — your data is now in three places: local, git history, and GitHub

## Repository

- **Backup Repo**: [github.com/suppg022312/memos-backup](https://github.com/suppg022312/memos-backup) (private)
- **Latest Backup**: `memos_prod_backup_20260209_201727.sql`
- **Restore Command**: `sqlite3 memos_prod.db < memos_prod_backup_20260209_201727.sql`

Your Memos are now safely backed up and restorable! 🎉