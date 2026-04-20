#!/bin/bash
set -euo pipefail

DIRECTUS_URL="http://localhost:8055"
DIRECTUS_TOKEN="direct-api-ef6f6891c6ffe9b8"
REPO_DIR="/root/astro-blog-netlify"
BLOG_DIR="$REPO_DIR/src/content/blog"

echo "=== Sync Posts: Fetching public posts from Directus ==="

POSTS_JSON=$(curl -s "$DIRECTUS_URL/items/posts?filter[tags][_contains]=public&filter[status][_eq]=published&sort=-date_published&limit=500" \
  -H "Authorization: Bearer $DIRECTUS_TOKEN")

POST_COUNT=$(echo "$POSTS_JSON" | jq '.data | length')
echo "Found $POST_COUNT public posts"

if [ "$POST_COUNT" -eq 0 ]; then
  echo "No public posts found. Exiting."
  exit 0
fi

mkdir -p "$BLOG_DIR"

# Clear existing posts
rm -f "$BLOG_DIR"/*.md

echo "$POSTS_JSON" | jq -c '.data[]' | while read -r post; do
  TITLE=$(echo "$post" | jq -r '.title')
  SLUG=$(echo "$post" | jq -r '.slug')
  CONTENT=$(echo "$post" | jq -r '.content')
  EXCERPT=$(echo "$post" | jq -r '.excerpt // .title')
  DATE_PUBLISHED=$(echo "$post" | jq -r '.date_published')
  
  # Get tags array and filter out 'public'
  TAGS=$(echo "$post" | jq -r '.tags // ["others"] | if type == "array" then . else [. + "others"] end | map(select(. != "public")) | .[]' 2>/dev/null | sort -u)

  if [ -z "$DATE_PUBLISHED" ] || [ "$DATE_PUBLISHED" = "null" ]; then
    echo "SKIP: $TITLE (no date_published)"
    continue
  fi

  PUB_DATETIME=$(date -d "$DATE_PUBLISHED" -u +"%Y-%m-%dT%H:%M:%SZ")

  # Build tags YAML
  TAGS_YAML=""
  while IFS= read -r tag; do
    if [ -n "$tag" ]; then
      TAGS_YAML="$TAGS_YAML
  - $tag"
    fi
  done <<< "$TAGS"

  if [ -z "$TAGS_YAML" ]; then
    TAGS_YAML="
  - others"
  fi

  # Escape double quotes in content
  CONTENT_ESCAPED=$(echo "$CONTENT" | sed 's/"/\\"/g')
  EXCERPT_ESCAPED=$(echo "$EXCERPT" | sed 's/"/\\"/g')
  TITLE_ESCAPED=$(echo "$TITLE" | sed 's/"/\\"/g')

  cat > "$BLOG_DIR/${SLUG}.md" << HEREDOC
---
pubDatetime: $PUB_DATETIME
title: "$TITLE_ESCAPED"
postSlug: "$SLUG"
description: "$EXCERPT_ESCAPED"
tags:$TAGS_YAML
---

$CONTENT
HEREDOC

  echo "SYNCED: $TITLE → ${SLUG}.md"
done

echo ""
echo "=== Committing and pushing ==="

cd "$REPO_DIR"
git add -A
CHANGED=$(git diff --cached --name-only | head -20)
if [ -z "$CHANGED" ]; then
  echo "No changes to commit."
  exit 0
fi

git commit -m "sync: update public posts ($(date +%Y-%m-%d))"
git push origin main

echo "=== Done! Netlify will auto-build. ==="
