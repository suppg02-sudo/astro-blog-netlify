---
pubDatetime: 2026-02-14T12:00:00Z
title: "Git + VPS Build Workflow for Hugo Staging and Production Deployment"
postSlug: "git-vps-build-workflow-hugo-staging-production-deployment"
description: "Git + VPS Build Workflow for Hugo Staging and Production Deployment"
tags:
  - devops
  - deployment
  - hugo
  - vps
  - git
---

## Introduction

When working with Hugo static sites, having a proper staging and production deployment workflow is essential. This guide covers a Git + VPS build approach that allows you to test blog posts locally and push them to a separate VPS server when ready.

The benefits of this workflow:
- **Local testing**: See changes instantly before publishing
- **Version control**: Full Git history for rollback capabilities
- **Clean separation**: Staging vs production environments
- **Automated builds**: Build on VPS, not locally

## Local Development Workflow

Testing Hugo locally with drafts is straightforward:

```bash
# Start Hugo development server
cd /media/docker/website
hugo server --buildDrafts --bind 0.0.0.0 --port 1314

# Access at: http://ubuntu58-1:1314
```

Key options:
- `--buildDrafts`: Includes draft posts in the preview
- `--bind 0.0.0.0`: Makes server accessible from external machines
- `--port 1314`: Specifies the port to listen on

When you're satisfied with your changes, stop the server and proceed to commit.

## Git Repository Setup

Your Hugo site is already initialized with Git:

```bash
cd /media/docker/website
git status
```

Current configuration:
- **Remote**: `github.com/suppg02-sudo/hugo-blog.git`
- **Branch**: `main`
- **Location**: `/media/docker/website`

## VPS Setup

Run these commands on your **VPS** to set up the deployment environment:

### Step 1: Install Hugo

```bash
sudo apt update
sudo apt install -y hugo
```

### Step 2: Clone Repository

```bash
git clone git@github.com:suppg02-sudo/hugo-blog.git /var/www/hugo-blog
cd /var/www/hugo-blog
```

### Step 3: Create Deployment Script

Create a reusable deployment script:

```bash
cat > /var/www/hugo-blog/deploy.sh << 'EOF'
#!/bin/bash

# Navigate to Hugo site directory
cd /var/www/hugo-blog

# Pull latest changes from GitHub
echo "Pulling latest changes..."
git pull origin main

# Build Hugo site with minification
echo "Building Hugo site..."
hugo --minify

# Confirm build completion
echo "Build complete! Site generated in public/"
echo "File count: $(find public -type f | wc -l)"
EOF

# Make script executable
chmod +x /var/www/hugo-blog/deploy.sh
```

## Push to Production

From your **local machine**, commit and push changes:

```bash
# Stage all changes
cd /media/docker/website
git add .

# Commit with descriptive message
git commit -m "Update blog posts and content"

# Push to GitHub
git push origin main
```

## Deploy on VPS

On your **VPS**, run the deployment script:

```bash
/var/www/hugo-blog/deploy.sh
```

What the script does:
1. Pulls latest commits from GitHub
2. Runs Hugo build with `--minify` (optimized for production)
3. Outputs static files to `public/` directory

The `public/` folder contains your ready-to-serve static site. You can serve it with nginx, Apache, or any web server.

## Optional: Automated SSH Deployment

For seamless deployment, create a local script that triggers VPS deployment via SSH:

```bash
# Create local deployment script
cat > ~/deploy-to-vps.sh << 'EOF'
#!/bin/bash

# 1. Commit and push local changes
cd /media/docker/website
git add .
git commit -m "Deploy $(date +%Y-%m-%d)"
git push origin main

# 2. Trigger VPS deployment via SSH
ssh your-vps-user@your-vps-host '/var/www/hugo-blog/deploy.sh'

echo "Deployment complete!"
EOF

# Make executable
chmod +x ~/deploy-to-vps.sh
```

Usage:
```bash
~/deploy-to-vps.sh
```

This combines local Git operations with remote VPS deployment in one command.

## Summary

The complete workflow:

1. **Local**: `hugo server --buildDrafts` - Test with drafts locally
2. **Local**: `git add . && git commit && git push` - Push changes to GitHub
3. **VPS**: `/var/www/hugo-blog/deploy.sh` - Pull and build on VPS

This setup gives you:
- Fast local development with instant previews
- Version-controlled content with rollback capability
- Production-ready builds on the VPS
- Separation of concerns (content vs build environment)

## Next Steps

To extend this workflow:
- Add CI/CD via GitHub Actions for automated deployments
- Implement staging branch for preview builds
- Add post-build optimizations (image optimization, CDN sync)
- Set up automated backups of the `public/` directory

Happy blogging with Hugo!