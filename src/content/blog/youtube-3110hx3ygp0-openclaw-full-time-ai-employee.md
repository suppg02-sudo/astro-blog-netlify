---
pubDatetime: 2026-02-26T10:07:12Z
title: "How OpenClaw Became a Full-Time AI Employee: 5 Billion Tokens Later"
postSlug: "youtube-3110hx3ygp0-openclaw-full-time-ai-employee"
description: "How OpenClaw Became a Full-Time AI Employee: 5 Billion Tokens Later"
tags:
  - productivity
  - automation
  - ai-agent
  - claude-ai
  - openclaw
---

What happens when you give an AI agent its own email address, workspace, and employee status? Matthew Berman found out after processing **5 billion tokens** through OpenClaw—and the results are extraordinary.

After a month of daily intensive use, Berman has transformed OpenClaw from a helpful assistant into a full-time team member that autonomously handles sponsorship management, CRM operations, meeting intelligence, knowledge management, and more.

## The Sponsorship Email Pipeline

The centerpiece of Berman's OpenClaw setup is a fully automated sponsorship email system. He gave OpenClaw its own identity:

- **Separate email address** and workspace account
- **Added to public-facing sponsorship group email**
- **Processes all incoming requests autonomously**

### The Scoring Rubric

OpenClaw evaluates every sponsorship email across five dimensions:

| Dimension | What It Measures |
|-----------|------------------|
| **Fit** | Relevance to audience |
| **Clarity** | Clear value proposition |
| **Budget** | Financial viability |
| **Seriousness** | Legitimacy of inquiry |
| **Company Trust** | Verifiable company presence |

Based on the combined score, OpenClaw takes automated action:

- **Exceptional (80+)**: Escalate immediately to team
- **High**: Escalate non-urgent
- **Medium**: Reply with qualification questions
- **Low**: Send polite decline
- **Spam**: Ignore completely

### Sender Research

Before scoring, OpenClaw automatically researches each sender:

- Verifies company website legitimacy
- Checks for social proof and reviews
- Looks up people at the company
- Detects suspicious signals (Gmail addresses claiming corporate domains)

When confidence is low, it sends a Telegram alert for human review—allowing Berman to approve or provide feedback that improves future scoring.

## Multi-Model Prompt Management

One of the most sophisticated aspects of Berman's setup is handling different AI models with different prompting styles.

**The Problem**: Claude Opus 4.6 and GPT 5.2 require opposite approaches. Claude over-indexes on instructions and dislikes all-caps emphasis. GPT prefers the opposite.

**The Solution**: Dual prompt stacks.

```
[config directory]           → Claude-optimized prompts (natural language)
/codeex/         → GPT-optimized prompts (all-caps friendly)
```

A nightly sync review ensures both stacks stay aligned, checking for:
- Each stack following its model's best practices
- No drift between versions (same operational facts)
- Automatic Telegram alerts if discrepancies found

This means the longest prompts are ever out of sync is ~24 hours.

## Document Organization

Berman follows a strict organizational structure to prevent prompt drift:

| File | Purpose |
|------|---------|
| `agents.md` | Operational rules, security, safety, task execution |
| `soul.md` | Agent identity and philosophy (5-10 lines) |
| `user.md` | Information about the user |
| `tools.md` | Environment-specific values (IDs, tokens) |
| `heartbeat.md` | Periodic cron configuration |
| `memory.md` | Private memories (user-only access) |
| `prd.md` | Product requirements document |

**Key Principle**: One place for every piece of information. No duplication.

## Context Optimization with Telegram Topics

Memory issues are a common complaint with AI agents. Berman's solution: **Telegram groups with topics**.

Each use case gets its own topic:
- General, CRM, Knowledge Base, Cron Updates
- Self-Improvement, Daily Brief, Earnings
- Video Research, Food Journal

This means each thread maintains its own focused context rather than one bloated conversation history.

**Pro Tip**: Use `/status` to monitor context fullness. At 89% capacity, either increase message expiry rate or clear the context.

## The CRM System

OpenClaw's CRM is a sophisticated integration of multiple data sources:

1. **Contact Discovery Pipeline** - Scans Gmail and calendar, filters spam/marketing
2. **SQLite + Vectors** - Enables both SQL queries and semantic search
3. **Proactive Research** - Daily news scanning for contact companies
4. **Relationship Intelligence** - Cross-references all data sources
5. **Automatic Follow-ups** - Nudges and summaries

The magic happens when everything connects. When a new sponsor email arrives, OpenClaw can:
- Reference previous conversations with similar companies
- Pull relevant knowledge base articles
- Check CRM history
- Draft contextually aware responses

## Meeting Intelligence

Using Fathom for transcription, OpenClaw automatically processes every meeting:

1. Pull transcript via API after meeting ends
2. Match attendees to CRM records
3. Extract insights and action items
4. Generate local embeddings (Nomic model)
5. Send action items to Telegram for approval
6. Approved items sync to Todoist + HubSpot with correct assignees

## Knowledge Base Architecture

Articles, videos, and interesting content get ingested through a secure pipeline:

1. User sends content to Telegram
2. **Pre-flight security check** (deterministic sanitizer)
3. **Sandbox quarantine** with frontier model scan
4. Chunk and embed locally (zero cost)
5. Store in SQLite database
6. Cross-post to team's AI trends channel

This enables natural language queries like "What did I save about AI agents last month?"

## Security Architecture

Berman takes security seriously with multiple defense layers:

### Layer 1: Network Gateway
- Token-based authentication
- Never exposed to internet
- Weekly verification via heartbeat

### Layer 2: Channel Access Control
- DMs: Can share any info
- Group channels: Redacts sensitive info
- Emails: Strictest policy

### Layer 3: Prompt Injection Defense
1. **Deterministic Sanitizer** - Detects attack patterns
2. **Frontier Scanner** - Best model scans content in sandbox
3. **Risk Scoring** - Elevates suspicious content

Additional measures include outbound redaction (secrets, PII), pre-commit hooks blocking API keys, and encrypted databases.

## Cron Strategy

Heavy jobs run overnight to preserve daytime quota:

| Time | Job |
|------|-----|
| 1:00 AM | Instagram analytics |
| 1:15 AM | X/Twitter analytics |
| 1:30 AM | YouTube analytics |
| 2:00 AM | CRM updates |
| 3:20 AM+ | Additional async jobs |

This spreads usage across the 5-hour Claude subscription window.

## Notification Batching

To reduce Telegram noise, notifications are batched by priority:

- **Critical**: Immediate delivery
- **High**: Hourly batches (CRM updates, cron failures)
- **Medium**: Every 3 hours (routine updates)

## Cost Optimization Strategies

1. **Local Embeddings** - Nomic model on MacBook Air (zero cost)
2. **Model Tiering** - Sonnet for most tasks, Opus for complex ones
3. **Quota Spreading** - Heavy jobs overnight
4. **Prompt Caching** - Built into workflow
5. **Context-Aware Polling** - Pull data only when signals indicate changes

## Nightly Councils

Automated review systems run every night:

- **Platform Council**: Cron health, code quality, test coverage, prompt quality
- **Security Council**: File permissions, gateway configs, secrets scanning
- **Innovation Scout**: Searches web for new OpenClaw use cases and generates ideas

## The Agents SDK Migration

When Anthropic banned OAuth usage outside their products, Berman discovered the Agents SDK still works:

1. Create shared SDK wrapper
2. Resolve OAuth token from existing location
3. Wrap all calls with auto-retry and logging
4. Centralize routing through `llm_router.js`

**Result**: Zero OAuth problems since migration.

## Key Takeaways

1. **Give AI its own identity** - Email, workspace, employee status
2. **Build progressively** - Start small, add authority over time
3. **Log everything** - Enables self-healing and debugging
4. **Use topics/threads** - Optimizes context and memory
5. **Multi-layer security** - Deterministic + AI-based defenses
6. **Dual prompt stacks** - Different models need different prompting
7. **Local embeddings** - Free and capable on modern hardware
8. **Nightly councils** - Automated quality and innovation checks
9. **Backup everything** - Encrypted, documented, restorable

## Conclusion

OpenClaw can function as a legitimate team member when properly configured. The combination of clear document organization, robust security, progressive authority delegation, and comprehensive logging creates a system that genuinely augments human capabilities.

The key insight? **Logging everything enables self-healing**. Every morning, Berman simply says "look at the logs from overnight and fix any issues"—and OpenClaw handles the rest.

---

*This post summarizes content from [Matthew Berman's YouTube video](https://www.youtube.com/watch?v=3110hx3ygp0). For the complete details and prompts mentioned, check the video description.*