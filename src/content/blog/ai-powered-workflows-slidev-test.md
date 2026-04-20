---
pubDatetime: 2026-02-03T00:30:00Z
title: "AI-Powered Workflows: Building Presentations with Slidev and AI"
postSlug: "ai-powered-workflows-slidev-test"
description: "AI-Powered Workflows: Building Presentations with Slidev and AI"
tags:
  - presentations
  - AI
  - automation
  - Slidev
  - workflows
---

# AI-Powered Workflows: Building Presentations with Slidev and AI

Today we're testing a new workflow: combining AI agents with Slidev to create professional presentations automatically.

## The Test Presentation

We created a 12-slide presentation titled "AI-Powered Workflows" using this exact workflow:

### Workflow Steps

1. **AI Generation** - Used AI to generate Slidev markdown
2. **File Creation** - Saved to `/media/docker/slidev/presentations/test-ai-workflows.md`
3. **Docker Integration** - Updated docker-compose.yml to point to new presentation
4. **Live Preview** - Accessed at http://ubuntu58-1:3030/
5. **Verification** - Screenshot captured and tested via Agent Browser

## Presentation Content

The test presentation covers:

### What Are AI Agents?
- Autonomous Systems - Execute tasks independently
- Multi-Step Planning - Break down complex problems
- Tool Integration - Access APIs, databases, file systems
- Learning Loop - Improve from feedback

### Why AI Workflows?
- Traditional development: Manual coding, tedious testing, slow iteration
- AI-Enhanced: Automated code generation, self-healing systems, rapid prototyping

### Real-World Applications
- **Slide Presentations** - AI generates Markdown → Slidev
- **Blog Posts** - Content research → Hugo publishing
- **API Development** - OpenAPI specs → Full implementation
- **Documentation** - Code analysis → Technical guides

## Technical Implementation

### Slidev Configuration

Our Slidev setup uses:
- **Image**: slidev-prebuilt (Node.js 24 Alpine)
- **Theme**: @slidev/theme-default
- **CSS Engine**: unocss
- **Port**: 3030
- **Host**: ubuntu58-1

### Docker Compose Setup

```yaml
services:
  slidev:
    image: slidev-prebuilt
    container_name: slidev_presentations
    restart: unless-stopped
    network_mode: host
    tty: true
    stdin_open: true
    environment:
      - VITE_SERVER_ORIGIN=http://ubuntu58-1:3030
      - HOST=ubuntu58-1
    volumes:
      - ./presentations:/app
      - ./logs:/app/logs
    working_dir: /app
    command: ["slidev", "test-ai-workflows.md", "--port", "3030", "--remote", "--bind", "0.0.0.0"]
```

### Critical Fixes Applied

#### 1. TTY Support
Slidev requires interactive terminal input. Fixed by adding:
```yaml
tty: true
stdin_open: true
```

#### 2. Host Block Issue
Initial error: "Blocked request. This host ('ubuntu58-1') is not allowed"

Solution: Created `/media/docker/slidev/vite.config.js`:
```javascript
module.exports = {
  server: {
    host: '0.0.0.0',
    port: 3030,
    allowedHosts: ['ubuntu58-1', 'localhost', '.local']
  }
}
```

**Note**: Must use CommonJS (`module.exports`) not ES6 (`import`) in vite.config.js.

## Access URLs

| Mode | URL |
|-------|-----|
| **Dev Server** | http://ubuntu58-1:3030/ |
| **Presenter Mode** | http://ubuntu58-1:3030/presenter/ |
| **Slides Overview** | http://ubuntu58-1:3030/overview/ |
| **Export Mode** | http://ubuntu58-1:3030/export/ |

## Creating Your Own Presentations

### Step 1: Generate Content

Use AI with this prompt template:
```
"Create a presentation about [TOPIC] with these requirements:
- Format: Slidev Markdown (frontmatter with Theme, class, etc.)
- Length: [N] slides
- Style: [professional/technical/casual]
- Include: v-click for interactive reveals
- Include: Code examples (if technical topic)
- Include: At least one layout variant (center, image-right, etc.)
- Theme: default
- Highlighter: shiki"
```

### Step 2: Save to Presentations Directory

```bash
# Save markdown file
/media/docker/slidev/presentations/your-presentation.md

# Update docker-compose.yml to point to your file
command: ["slidev", "your-presentation.md", "--port", "3030", "--remote", "--bind", "0.0.0.0"]

# Restart container
cd /media/docker/slidev && docker-compose restart
```

### Step 3: Auto-Reload Development

Slidev automatically reloads when you:
- Edit `.md` presentation files
- Save changes in `presentations/` directory
- No manual restart needed!

## Export Options

### Export to PDF
1. Navigate to http://ubuntu58-1:3030/export/
2. Download PDF directly from browser

### Export to PPTX
1. Navigate to http://ubuntu58-1:3030/export/
2. Select PPTX format for PowerPoint export

### Export to HTML SPA
```bash
cd /media/docker/slidev
docker-compose exec slidev slidev export test-ai-workflows.md
```

## Test Results

### Verification
- ✅ HTTP 200 response via http://ubuntu58-1:3030/
- ✅ Page title confirmed: "AI-Powered Workflows - Slidev"
- ✅ Screenshot captured successfully
- ✅ No "blocked host" errors
- ✅ All slides render correctly with interactive elements

### Presentation Structure
The test presentation includes:
- 12 total slides
- Multiple layouts (center, image-right, two-cols, cover)
- Interactive elements (v-click, v-clicks)
- Code blocks with syntax highlighting
- Live code examples
- Best practices section

## Key Learnings

### What Worked
1. **TTY Support** - Critical for Slidev to stay running in Docker
2. **CommonJS Config** - Vite config must use module.exports, not ES6 imports
3. **Allowed Hosts** - Must explicitly add ubuntu58-1 to allowedHosts list
4. **Volume Mounting** - Presentations directory persists to host filesystem

### Workflow Efficiency
- **Time to Create**: ~2 minutes (AI generation + file save)
- **Time to Deploy**: ~10 seconds (docker-compose restart)
- **Time to Verify**: ~15 seconds (browser navigation + screenshot)
- **Total Workflow Time**: ~3 minutes end-to-end

## Best Practices

### For Presentations
- Start with clear outline
- Use v-click for progressive reveals
- Include visual elements (images, diagrams)
- Test in presenter mode before sharing
- Export multiple formats for distribution

### For AI Generation
- Provide clear requirements upfront
- Specify slide count and style
- Request interactive elements
- Ask for code examples if technical
- Include layout variations

### For Docker Setup
- Always use TTY for interactive processes
- Configure allowedHosts for custom hostnames
- Use volume bindings for persistent content
- Test with curl before browser access

## Resources

### Documentation
- **Slidev Docs**: https://sli.dev/
- **GitHub**: https://github.com/slidevjs/slidev
- **Themes Gallery**: https://sli.dev/themes/gallery.html
- **Examples**: https://sli.dev/showcase.html

### Related Posts
- [Hugo Blog Post Creation Guide](/2026/01/30/getting-started-with-hugo/)
- [Docker Container Management](/2026/02/02/systematic-session-review-workflow/)

## Conclusion

Slidev combined with AI agents creates a powerful workflow for presentation development. The markdown-based approach makes it perfect for AI generation, while the Docker setup ensures consistent, containerized deployment.

The test presentation demonstrates that we can go from concept to live presentation in under 3 minutes, with full control over styling, interactivity, and export options.

**Status**: ✅ Working Successfully
**Presentation URL**: http://ubuntu58-1:3030/
**File Location**: `/media/docker/slidev/presentations/test-ai-workflows.md`