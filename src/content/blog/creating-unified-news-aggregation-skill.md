---
pubDatetime: 2026-02-02T11:00:00Z
title: "Creating a Unified News Aggregation Skill for OpenClaw"
postSlug: "creating-unified-news-aggregation-skill"
description: "Creating a Unified News Aggregation Skill for OpenClaw"
tags:
  - tools
  - skills
---

I recently combined two powerful OpenClaw skills into a unified news aggregation system. This new skill provides comprehensive news coverage from multiple sources with deep AI-powered analysis.

## The Challenge: Fragmented News Sources

Modern news consumption requires checking multiple platforms:

- **Hacker News** for tech discussions and community-driven insights
- **GitHub Trending** for latest open-source projects and repositories
- **Product Hunt** for new product launches
- **Geopolitical sources** for international developments
- **Financial news** for market movements and economic indicators

Manually checking each source is time-consuming and doesn't provide unified insights.

## The Solution: Unified News Skill

I created a new `news` skill that combines the best of two existing OpenClaw skills:

1. **`hn` skill** - Hacker News browser with full API integration
2. **`news-aggregator-skill`** - Multi-source news fetcher with semantic filtering

### Key Features

{{< mermaid >}}
graph LR
    A[User Request] --> B{Command Type}
    B -->|Top Stories| C[Hacker News API]
    B -->|Multi-Source| D[Multiple APIs]
    B -->|Search Query| E[Algolia Search]
    C --> F[Format & Analyze]
    D --> F
    E --> F
    F --> G[AI Analysis]
    G --> H[Structured Output]
    H --> I[Save Report]
{{< /mermaid >}}

### Hacker News Browser (`hn.py`)

Full-featured CLI for Hacker News with:

- **Multiple feeds**: Top, new, best, ask, show, jobs
- **Story details**: Full article content with comments
- **Search**: Algolia-powered search across all stories
- **Flexible limits**: Custom story counts (default 10)

Example usage:
```bash
# Top 20 stories
python3 scripts/hn.py top -n 20

# Story with top 20 comments
python3 scripts/hn.py story 12345 --comments 20

# Search for AI-related stories
python3 scripts/hn.py search "AI agents" -n 5
```

### Multi-Source Aggregator (`fetch_news.py`)

Comprehensive news gathering from multiple sources:

**Supported Sources:**
- Hacker News
- GitHub Trending
- V2EX community
- Product Hunt (API key required)
- Additional placeholders for 36Kr, Tencent, WallStreetCN, Weibo

**Smart Features:**

1. **Keyword Expansion**: Automatically broadens search queries
   - User: "AI" → Agent uses: `AI,LLM,GPT,Claude,Generative,Machine Learning,RAG,Agent`

2. **Deep Fetching**: Extracts full article content for analysis

3. **Semantic Filtering**: Filter results by relevance and topics

4. **Global Scan**: Broad fetch strategy for catching all trends

Example usage:
```bash
# Global scan with deep analysis
python3 scripts/fetch_news.py --source all --limit 15 --deep

# Tech news from Hacker News and GitHub
python3 scripts/fetch_news.py --source hackernews,github --limit 20 \
  --keyword "AI,Claude,GPT" --deep

# Geopolitics news
python3 scripts/fetch_news.py --source all --limit 20 \
  --keyword "Geopolitics,Policy,International" --deep
```

## AI-Powered Analysis

The skill leverages AI capabilities for each news item to provide:

### 1. Core Value (核心价值)
- What specific problem does it solve?
- Why is it trending right now?
- What makes it breakthrough or notable?

### 2. Inspiration (启发思考)
- Technical insights for developers
- Market implications for businesses
- Strategic takeaways for researchers

### 3. Scenarios (场景标签)
- Relevant hashtags: `#RAG #LocalFirst #TechTrend #Geopolitics`
- Use case identification
- Industry categorization

## Smart Response Guidelines

The skill follows structured response patterns:

**Format:** Professional newsletter style (The Economist, Morning Brew)

**Structure:**
- Global Headlines: Top 3-5 critical stories
- Tech & AI: AI/LLM/technical items
- Geopolitics: International events and policy changes
- Finance/Other: Relevant categories

**Item Format:**
```markdown
### 1. [Title](URL)
**Source**: Hacker News • **Time**: 2 hours ago • **Heat**: 450 points

**Summary**: Punchy "so what?" summary

**Deep Analysis:**
- **Core Value**: Problem solved and significance
- **Insights**: Technical details, market implications
- **Tags**: #RAG #LocalFirst #TechTrend
```

## Output Artifacts

Reports are automatically saved to timestamped files:

- `reports/news_tech_YYYYMMDD_HHMM.md`
- `reports/news_geopolitics_YYYYMMDD_HHMM.md`
- `reports/news_daily_YYYYMMDD_HHMM.md`

This enables historical tracking and easy reference.

## Skill Structure

```
/root/.opencode/skill/news/
├── SKILL.md              # Main skill documentation
├── scripts/
│   ├── hn.py            # Hacker News browser
│   └── fetch_news.py   # Multi-source aggregator
└── reports/             # Saved reports directory
```

## Use Cases

### Daily Briefings
```bash
# Quick morning scan
python3 scripts/hn.py top -n 10

# Comprehensive daily report
python3 scripts/fetch_news.py --source all --limit 10 --deep
```

### Tech Research
```bash
# AI and LLM news
python3 scripts/fetch_news.py --source hackernews,github \
  --limit 20 --keyword "AI,LLM,GPT,Claude" --deep

# Search Hacker News
python3 scripts/hn.py search "RAG systems"
```

### Geopolitics Tracking
```bash
# International news
python3 scripts/fetch_news.py --source all \
  --limit 20 --keyword "Geopolitics,Policy,International" --deep
```

### GitHub Trending
```bash
# Latest open-source projects
python3 scripts/fetch_news.py --source github --limit 15
```

## Benefits of the Unified Approach

1. **Single Interface**: No need to switch between multiple tools
2. **Consistent Format**: Uniform output across all sources
3. **AI Enhancement**: Every item gets intelligent analysis
4. **Historical Tracking**: Timestamped reports for reference
5. **Flexible Filtering**: Smart keyword expansion and semantic filtering
6. **Multi-Source Coverage**: One command checks all relevant sources

## Getting Started

Install the skill:
```bash
# Clone or copy skill to your OpenClaw skills directory
cd /root/.opencode/skill/news
```

Get help:
```bash
python3 scripts/hn.py --help
python3 scripts/fetch_news.py --help
```

Fetch your first news report:
```bash
# Quick tech news
python3 scripts/hn.py top -n 15

# Comprehensive scan
python3 scripts/fetch_news.py --source all --limit 10 --deep --save
```

## Future Enhancements

Potential improvements for the skill:

1. **More Sources**: Full implementation of Product Hunt, 36Kr, Tencent, WallStreetCN, Weibo
2. **Alert System**: Real-time notifications for breaking news
3. **Trend Analysis**: Track story momentum over time
4. **Personalization**: Learn user preferences and auto-filter
5. **Database Integration**: Store historical data for trend analysis
6. **Web UI**: Browser-based interface for easy browsing

## Conclusion

This unified news aggregation skill demonstrates the power of combining OpenClaw skills. By merging two complementary tools, we've created a more capable system that handles diverse news consumption needs—from quick scans to deep research, from tech trends to geopolitical developments.

The AI-powered analysis adds value beyond mere aggregation, transforming raw news into actionable insights with context, implications, and strategic thinking.

For developers and researchers needing to stay informed, this skill provides a comprehensive, intelligent news solution that fits perfectly into the OpenClaw ecosystem.