---
pubDatetime: 2026-03-09T09:50:00Z
title: "Replacing a Broken Search Pipeline with Gemini Search Grounding"
postSlug: "telegram-bot-gemini-search-grounding"
description: "Replacing a Broken Search Pipeline with Gemini Search Grounding"
tags:
  - grounding
  - google-search
  - gemini
  - search
  - ai-agent
  - architecture
  - telegram
  - api
  - python
  - bot
---

## The Problem: DuckDuckGo Blocks Bot Traffic

The Telegram bot had two features that depended on web search: a **research pipeline** (search -> fetch sources -> synthesize with Gemini) and **inline search queries** (user types "what is..." and the bot searches the web before answering). Both were completely broken.

The original implementation scraped DuckDuckGo's HTML endpoint directly:

```python
def web_search(query: str, num_results: int = 5) -> str:
    search_url = f"https://html.duckduckgo.com/html/?q={quote_plus(query)}"
    resp = requests.get(search_url, headers=headers, timeout=15)
    soup = BeautifulSoup(resp.text, "lxml")
    for result_div in soup.select(".result"):
        # Extract title, snippet, URL from HTML...
```

This returned HTTP 202 with a CAPTCHA page: *"bots use DuckDuckGo too"*. Every request. The `lite.duckduckgo.com` endpoint was blocked identically. No User-Agent string helped.

The `duckduckgo_search` Python library (which uses an internal API endpoint rather than HTML scraping) technically worked, but returned wrong locale results -- Chinese pages from Baidu when no region was specified, and zero results with `region='uk-en'`.

The research pipeline was a 4-phase process that looked elegant on paper:

```
Phase 1: Generate 3 search queries from topic
Phase 2: Search DDG, collect unique URLs
Phase 3: Fetch top 5 URLs with BeautifulSoup
Phase 4: Concatenate source text, synthesize with Gemini
```

But Phase 2 returned nothing because DDG was blocked. Phase 3 had nothing to fetch. Phase 4 synthesized an empty context. The entire pipeline was dead.

## The Options We Considered

| Approach | Pros | Cons |
|----------|------|------|
| **Fix DDG HTML scraping** | No API key needed | Fundamentally blocked -- CAPTCHA on every request |
| **`duckduckgo_search` library** | Already installed in venv | Locale bug, may break again (unofficial API) |
| **Brave Search API** | Reliable, 2000 free queries/month | Another API key to manage, rate limits |
| **Google Custom Search API** | Official, reliable | Costs money after 100 queries/day |
| **Gemini Search Grounding** | Built into existing Gemini API, no extra key | Tied to Gemini ecosystem |

## The Solution: Gemini Search Grounding

Gemini 2.5 Flash has a built-in `google_search` tool. When enabled, Gemini autonomously decides when to search the web, what queries to run, and how to synthesize the results into its response. One API call replaces the entire search -> fetch -> synthesize pipeline.

The API change is minimal. A standard Gemini call:

```json
{
  "contents": [{"parts": [{"text": "What is..."}]}]
}
```

Becomes a grounded call by adding `tools`:

```json
{
  "contents": [{"parts": [{"text": "What is..."}]}],
  "tools": [{"google_search": {}}]
}
```

The response includes the usual `text` field plus a `groundingMetadata` object with the search queries Gemini ran, the sources it found, and rendered search chips for each query.

### Implementation: `ask_gemini_grounded()`

```python
def ask_gemini_grounded(question: str, system: str = None) -> str:
    """Ask Gemini with Google Search grounding enabled."""
    payload = {
        "system_instruction": {"parts": [{"text": system or SYSTEM_PROMPT}]},
        "contents": [{"role": "user", "parts": [{"text": question}]}],
        "tools": [{"google_search": {}}],
    }

    resp = requests.post(GEMINI_URL, json=payload, timeout=60)
    data = resp.json()

    candidate = data["candidates"][0]
    text = candidate["content"]["parts"][0]["text"]

    # Extract source attribution from grounding metadata
    chunks = candidate.get("groundingMetadata", {}).get("groundingChunks", [])
    if chunks:
        sources = []
        seen = set()
        for chunk in chunks[:5]:
            title = chunk.get("web", {}).get("title", "")
            if title and title not in seen:
                seen.add(title)
                sources.append(f"- {title}")
        if sources:
            text += "\n\nSources:\n" + "\n".join(sources)

    return text
```

Key design choices:

- **Separate function from `ask_gemini()`**: Regular chat shouldn't trigger web search for every message. `ask_gemini()` stays fast (no grounding overhead) for conversational use. `ask_gemini_grounded()` is only called when the bot detects a search query or runs the research pipeline.
- **Custom system prompt parameter**: The research pipeline passes a research-analyst system prompt. Search queries use the default bot system prompt.
- **60-second timeout**: Grounded calls take longer than plain chat because Gemini runs search queries internally. 30 seconds wasn't enough for complex research topics.
- **Source deduplication**: The grounding metadata can contain 10+ source chunks, many from the same domain. We deduplicate by title and show the top 5.

### Simplified Research Pipeline

The old 4-phase pipeline collapsed to a single function call:

```python
def research_execute(topic: str) -> str:
    """Run research pipeline using Gemini Search Grounding."""
    research_system = (
        "You are a thorough research analyst. Use Google Search to find "
        "the most current and relevant information on the given topic."
    )

    research_prompt = (
        f"Research this topic thoroughly: {topic}\n\n"
        f"REQUIREMENTS:\n"
        f"- Search for the latest information (2025-2026)\n"
        f"- Write a structured summary with clear sections\n"
        f"- Include key findings, trends, statistics\n"
        f"- Note disagreements between sources\n"
        f"- Include a 'Key Takeaways' section\n"
        f"- Cite your sources\n"
    )

    return ask_gemini_grounded(research_prompt, system=research_system)
```

What was ~70 lines of pipeline code (search queries, URL deduplication, BeautifulSoup fetching, text concatenation, context truncation) became a single grounded API call with a well-crafted prompt.

### Updated Search Query Handler

The `echo()` handler detects search-intent messages by prefix matching ("what is...", "how to...", "search for..."):

```python
# Before: broken DDG scrape -> feed to Gemini (two calls, first broken)
search_results = web_search(text, num_results=5)
prompt = f"Here are web search results:\n{search_results}\nQuestion: {text}"
response = ask_gemini(prompt, user_id)

# After: single grounded Gemini call (searches + answers in one)
response = ask_gemini_grounded(text)
```

## What the Grounding Response Looks Like

A test query for *"What are the latest developments in AI agents in March 2026?"* returned a ~2500-character structured response with sections, bullet points, and source attribution. The `groundingMetadata` contained:

- **10 source chunks** from marketingprofs.com, joget.com, medium.com, goldmansachs.com, theblue.ai, robylon.ai, huawei.com, and others
- **5 search query chips** (the queries Gemini chose to run internally)
- **A rendered HTML search widget** (not useful for Telegram, but available)

The response quality was significantly better than the old pipeline because Gemini:
1. Chose better search queries than our hardcoded 3-query approach
2. Had access to full page content (not our 3000-char truncated fetches)
3. Could cross-reference sources during synthesis rather than getting a concatenated blob

## Code Removed

| What | Lines | Why |
|------|-------|-----|
| `web_search()` | 43 lines | DDG HTML scraping, CAPTCHA-blocked |
| Search query parsing | 18 lines | URL extraction from numbered text results |
| URL dedup logic | 12 lines | `seen_urls` set across 3 search queries |
| Source fetching loop | 8 lines | BeautifulSoup fetch of top 5 URLs |
| Fallback raw search | 3 lines | "if no sources, try more results" |
| `quote_plus` import | 1 line | Only used for DDG URL encoding |

**Total removed**: ~85 lines of broken search/fetch/parse code.

**Total added**: ~65 lines of `ask_gemini_grounded()` + simplified `research_execute()`.

Net result: 20 fewer lines, zero external search dependencies, and it actually works.

## Architecture After the Change

```
User message in Telegram
    |
    v
echo() handler
    |
    ├── Pending context? → handle_pending_input()
    |
    ├── Trigger word? → menu or shell handler
    |
    └── Regular message
            |
            ├── Contains URL? → fetch_url() + ask_gemini()
            |       (BeautifulSoup still used for direct URL fetching)
            |
            ├── Search intent? → ask_gemini_grounded()
            |       (Gemini searches Google internally)
            |
            └── Plain chat → ask_gemini()
                    (no search, just conversation)
```

Three distinct Gemini call paths:
- **`ask_gemini()`**: Regular chat with conversation history, no search. 1-3s.
- **`ask_gemini_grounded()`**: Search queries and research. Gemini decides what to search. 3-10s.
- **`ask_gemini()` with URL context**: User pastes a URL, we fetch it, Gemini analyzes the content. 2-5s.

## The Research Flow (End to End)

```
User sends: "research"
    → Bot shows research menu (inline buttons)
        → User clicks "Start Research"
            → Bot asks "What topic?"
                → User types: "AI agent frameworks 2026"
                    → Bot asks: "Publish as blog post?"
                        → [Research + Blog] / [Research Only] / [Cancel]
                            → ask_gemini_grounded() with research prompt
                                → Gemini searches Google, synthesizes
                                    → Summary sent to Telegram
                                    → (if blog selected) publish_blog_post()
                                        → Hugo frontmatter + write + rebuild
```

## Lessons Learned

### 1. Don't Scrape Search Engines

DuckDuckGo, Google, and Bing all actively block bot traffic to their HTML search pages. HTML scraping is fragile even when it works -- class names change, redirects break, CAPTCHAs appear. If your application needs web search, use an API: either a search API (Brave, SerpAPI) or an LLM with built-in search (Gemini grounding, Perplexity).

### 2. Let the Model Do the Searching

The old pipeline separated search, fetch, and synthesis into distinct phases. This meant we were making search query decisions (hardcoded 3 queries), URL selection decisions (top 5 by order), and content truncation decisions (3000 chars per source) that the model could make better. Gemini Search Grounding lets the model decide what to search, how many sources to consult, and what to extract from each -- all in a single API call.

### 3. Separate Grounded and Ungrounded Calls

Not every message needs web search. Adding `google_search` to every Gemini call would:
- Slow down simple chat responses (3-10s vs 1-3s)
- Add unnecessary search noise to conversational messages
- Consume more API quota

The bot explicitly detects search intent (prefix matching on "what is", "how to", "search for", etc.) and only uses grounded calls for those messages. Regular chat stays fast.

### 4. The Best Code Is Code You Delete

The old search pipeline was ~85 lines across 4 functions. It handled query generation, HTML parsing, URL deduplication, content fetching, text truncation, and fallback logic. All of it was broken because the first step (DDG search) was CAPTCHA-blocked. The replacement is a single function that delegates all of that complexity to the Gemini API. Sometimes the right fix isn't to debug the pipeline -- it's to replace it with something architecturally simpler.

## Files Changed

```
/opt/telegram-bot/bot.py
├── REMOVED: web_search()              - DDG HTML scraping (43 lines)
├── ADDED:   ask_gemini_grounded()     - Gemini + Google Search tool (65 lines)
├── CHANGED: research_execute()        - 70 lines → 30 lines (single API call)
├── CHANGED: echo() search handler     - 10 lines → 3 lines
└── REMOVED: quote_plus import         - No longer needed
```

---

*This is a companion post to [Building a Telegram Bot Agent for OpenCode](/posts/telegram-bot-opencode-agent-architecture/), which covers the full v3 architecture. This post focuses specifically on the search grounding upgrade that fixed the broken web search and research pipeline.*