#!/usr/bin/env python3
"""Sync public posts from Directus to the Netlify Astro blog repo.

Fetches ALL published posts, filters for 'public' tag client-side
(because Directus _contains doesn't work on JSON fields), paginates
through all results, writes markdown files, and git pushes.
"""
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

DIRECTUS_URL = os.environ.get("DIRECTUS_URL", "http://localhost:8055")
DIRECTUS_TOKEN = os.environ.get("DIRECTUS_TOKEN", "direct-api-ef6f6891c6ffe9b8")
REPO_DIR = Path(os.environ.get("REPO_DIR", "/root/astro-blog-netlify"))
BLOG_DIR = REPO_DIR / "src" / "content" / "blog"
BATCH_SIZE = 100
HEADERS = {
    "Authorization": f"Bearer {DIRECTUS_TOKEN}",
    "Content-Type": "application/json",
}

SAFE_FILENAME_RE = re.compile(r"[^\w\-.]")


def fetch_all_published_posts():
    """Fetch ALL published posts from Directus with pagination."""
    all_posts = []
    offset = 0
    while True:
        url = (
            f"{DIRECTUS_URL}/items/posts"
            f"?filter[status][_eq]=published"
            f"&sort=-date_published"
            f"&limit={BATCH_SIZE}"
            f"&offset={offset}"
            f"&fields=id,title,slug,content,excerpt,tags,date_published"
        )
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        data = resp.json().get("data", [])
        if not data:
            break
        all_posts.extend(data)
        print(f"  Fetched {len(data)} posts (total: {len(all_posts)})")
        if len(data) < BATCH_SIZE:
            break
        offset += BATCH_SIZE
    return all_posts


def is_public(post):
    """Check if post has 'public' tag in its JSON tags array."""
    tags = post.get("tags")
    if not tags:
        return False
    if isinstance(tags, str):
        try:
            tags = json.loads(tags)
        except (json.JSONDecodeError, TypeError):
            return "public" in tags.lower() if tags else False
    if isinstance(tags, list):
        return "public" in tags
    return False


def slug_to_filename(slug):
    """Convert slug to a safe filename, truncating if needed."""
    if not slug:
        return None
    safe = SAFE_FILENAME_RE.sub("-", slug).strip("-")
    if len(safe) > 80:
        safe = safe[:80]
    return safe


def write_post(post):
    """Write a single post as markdown with frontmatter."""
    slug = post.get("slug")
    if not slug:
        print(f"  SKIP: no slug for post id={post.get('id')}")
        return False

    title = post.get("title", "Untitled")
    content = post.get("content", "")
    excerpt = post.get("excerpt") or title
    date_published = post.get("date_published")

    if not date_published:
        print(f"  SKIP: {title} (no date_published)")
        return False

    try:
        dt = datetime.fromisoformat(date_published.replace("Z", "+00:00"))
        pub_dt = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    except (ValueError, AttributeError):
        print(f"  SKIP: {title} (bad date_published: {date_published})")
        return False

    tags = post.get("tags", [])
    if isinstance(tags, str):
        try:
            tags = json.loads(tags)
        except (json.JSONDecodeError, TypeError):
            tags = []
    if not isinstance(tags, list):
        tags = []
    filtered_tags = [t for t in tags if t != "public"]
    if not filtered_tags:
        filtered_tags = ["others"]

    tags_yaml = "\n".join(f"  - {t}" for t in filtered_tags)

    title_escaped = title.replace('"', '\\"')
    excerpt_escaped = excerpt.replace('"', '\\"').replace("\n", " ")[:200]

    filename = slug_to_filename(slug) or slug_to_filename(title) or f"post-{post.get('id', 'unknown')}"
    filepath = BLOG_DIR / f"{filename}.md"

    frontmatter = f"""---
pubDatetime: {pub_dt}
title: "{title_escaped}"
postSlug: "{slug}"
description: "{excerpt_escaped}"
tags:
{tags_yaml}
---

{content}"""

    filepath.write_text(frontmatter, encoding="utf-8")
    return True


def git_push():
    """Stage, commit, and push changes."""
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        cwd=REPO_DIR,
        capture_output=True,
        text=True,
    )
    if not result.stdout.strip():
        result2 = subprocess.run(
            ["git", "diff", "--name-only"],
            cwd=REPO_DIR,
            capture_output=True,
            text=True,
        )
        if not result2.stdout.strip():
            print("No changes to commit.")
            return False

    subprocess.run(["git", "add", "-A"], cwd=REPO_DIR, check=True)

    changed = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        cwd=REPO_DIR,
        capture_output=True,
        text=True,
    )
    if not changed.stdout.strip():
        print("No changes to commit.")
        return False

    changed_count = len(changed.stdout.strip().split("\n"))
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    subprocess.run(
        ["git", "commit", "-m", f"sync: {changed_count} posts ({date_str})"],
        cwd=REPO_DIR,
        check=True,
    )
    token = subprocess.run(
        ["gh", "auth", "token"], capture_output=True, text=True
    ).stdout.strip()
    if token:
        remote_url = f"https://suppg02-sudo:{token}@github.com/suppg02-sudo/astro-blog-netlify.git"
        subprocess.run(
            ["git", "remote", "set-url", "origin", remote_url],
            cwd=REPO_DIR, check=True,
        )
    subprocess.run(["git", "push", "origin", "main"], cwd=REPO_DIR, check=True)
    print(f"Pushed {changed_count} file changes.")
    return True


def main():
    dry_run = "--dry-run" in sys.argv

    print("=== Netlify Blog Sync ===")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print(f"Repo: {REPO_DIR}")
    print(f"Blog dir: {BLOG_DIR}")
    print()

    print("Fetching all published posts from Directus...")
    all_posts = fetch_all_published_posts()
    print(f"Total published: {len(all_posts)}")

    public_posts = [p for p in all_posts if is_public(p)]
    print(f"Public-tagged: {len(public_posts)}")

    if not public_posts:
        print("No public posts found. Exiting.")
        return

    BLOG_DIR.mkdir(parents=True, exist_ok=True)

    if not dry_run:
        print(f"\nClearing {BLOG_DIR}...")
        for f in BLOG_DIR.glob("*.md"):
            f.unlink()

    written = 0
    skipped = 0
    for post in public_posts:
        if dry_run:
            title = post.get("title", "?")
            slug = post.get("slug", "?")
            print(f"  WOULD WRITE: {title} -> {slug}.md")
            written += 1
        else:
            if write_post(post):
                written += 1
            else:
                skipped += 1

    print(f"\nResults: {written} written, {skipped} skipped")

    if dry_run:
        print("\nDry run complete. No files written.")
        return

    print("\nPushing to GitHub...")
    pushed = git_push()
    if pushed:
        print("=== Sync complete! Netlify will auto-build. ===")
    else:
        print("=== No changes needed. ===")


if __name__ == "__main__":
    main()
