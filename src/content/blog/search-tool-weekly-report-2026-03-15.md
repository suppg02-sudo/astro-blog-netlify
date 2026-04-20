---
pubDatetime: 2026-03-15T09:00:28Z
title: "Search Tool Performance Weekly Report - Week of March 08, 2026"
postSlug: "search-tool-weekly-report-2026-03-15"
description: "Search Tool Performance Weekly Report - Week of March 08, 2026"
tags:
  - weekly-report
  - search-tools
  - monitoring
  - performance
  - api-analysis
---

## 📊 Week of March 08, 2026 to March 15, 2026

Weekly analysis of search tool performance, reliability, and rate limit status across all integrated search services.

---

## 🎯 Executive Summary

| Metric | Value | Status |
|--------|-------|--------|
| **Total Tests Run** | 7 | 📊 |
| **Success Rate** | 71.4% | ⚠️ |
| **Avg Response Time** | 2055ms | 🐢 |
| **Rate Limit Hits** | 0 | ✅ |
| **Tools Skipped** | 1 | ℹ️ |

---

## 🔍 Tool-by-Tool Analysis

### 🔍 Brave Search

| Metric | Value |
|--------|-------|
| **Tests Run** | 3 |
| **Successful** | 3 |
| **Failed** | 0 |
| **Skipped** | 0 |
| **Success Rate** | 100.0% |
| **Avg Response Time** | 2423ms |
| **Rate Limited** | No ✅ |

**Test Results:**

- ✅ `OpenCode AI agent framework...` - 5342ms (10 results)
- ✅ `AI agent developments...` - 878ms
- ✅ `AI coding assistants tutorial...` - 1049ms

---

### 🌐 Exa Web Search

| Metric | Value |
|--------|-------|
| **Tests Run** | 1 |
| **Successful** | 0 |
| **Failed** | 0 |
| **Skipped** | 1 |
| **Success Rate** | 0.0% |
| **Avg Response Time** | 0ms |
| **Rate Limited** | No ✅ |

**Test Results:**

- ⚠️ `LLM prompt engineering best practices...` - 0ms - Error: API key not configured (optional)

---

### 🐙 GitHub Code Search

| Metric | Value |
|--------|-------|
| **Tests Run** | 1 |
| **Successful** | 0 |
| **Failed** | 1 |
| **Skipped** | 0 |
| **Success Rate** | 0.0% |
| **Avg Response Time** | 0ms |
| **Rate Limited** | No ✅ |

**Test Results:**

- ❌ `function async await pattern...` - 0ms - Error: HTTP 503: Service Temporarily Unavailable

---

### 📚 Context7 Documentation

| Metric | Value |
|--------|-------|
| **Tests Run** | 1 |
| **Successful** | 1 |
| **Failed** | 0 |
| **Skipped** | 0 |
| **Success Rate** | 100.0% |
| **Avg Response Time** | 0ms |
| **Rate Limited** | No ✅ |

**Test Results:**

- ✅ `How to implement authentication in Express.js...` - 0ms (1 results)

---

### 🔗 WebFetch

| Metric | Value |
|--------|-------|
| **Tests Run** | 1 |
| **Successful** | 1 |
| **Failed** | 0 |
| **Skipped** | 0 |
| **Success Rate** | 100.0% |
| **Avg Response Time** | 950ms |
| **Rate Limited** | No ✅ |

**Test Results:**

- ✅ `https://httpbin.org/json...` - 950ms (1 results)

---

## 📈 Historical Trends

### Week-over-Week Comparison

| Metric | This Week | Last Week | Change |
|--------|-----------|-----------|--------|
| **Success Rate** | 71.4% | 28.6% | 📈 42.9% |
| **Avg Response Time** | 2055ms | 591ms | 🐢 1464ms |

## 💡 Recommendations

- ⚠️ **Reliability Alert**: Success rate below 90%. Investigate failing tools.
- 🐢 **Performance Issue**: Average response time exceeds 1 second. Consider caching or alternative tools.
- ℹ️ **API Keys**: Some tools were skipped due to missing API keys. Configure EXA_API_KEY if needed.

---

## 🔧 Configuration Status

| Tool | API Key | Status |
|------|---------|--------|
| Brave Search | ✅ Configured | Active |
| Exa Search | ⚠️ Optional | Not Configured |
| GitHub Search | ✅ Public API | Active |
| Context7 | ✅ MCP Available | Active |
| WebFetch | ✅ No Auth Required | Active |

---

## 📊 Weekly Metrics Summary

```json
{
  "total_tests": 7,
  "successful_tests": 5,
  "failed_tests": 1,
  "skipped_tests": 1,
  "average_response_time_ms": 2054.76,
  "rate_limit_hits": 0,
  "tools_status": {
    "brave_search": {
      "total": 3,
      "success": 3,
      "failed": 0,
      "skipped": 0,
      "avg_response_time_ms": 2422.86,
      "rate_limited": 0
    },
    "exa_search": {
      "total": 1,
      "success": 0,
      "failed": 0,
      "skipped": 1,
      "avg_response_time_ms": 0.0,
      "rate_limited": 0
    },
    "github_search": {
      "total": 1,
      "success": 0,
      "failed": 1,
      "skipped": 0,
      "avg_response_time_ms": 0.0,
      "rate_limited": 0
    },
    "context7": {
      "total": 1,
      "success": 1,
      "failed": 0,
      "skipped": 0,
      "avg_response_time_ms": 0.0,
      "rate_limited": 0
    },
    "webfetch": {
      "total": 1,
      "success": 1,
      "failed": 0,
      "skipped": 0,
      "avg_response_time_ms": 950.43,
      "rate_limited": 0
    }
  }
}
```

---

## 🚀 Next Week's Focus

- Monitor for continued rate limiting issues
- Track response time trends
- Evaluate search result quality
- Consider adding more test queries for comprehensive coverage
- Review API usage quotas if rate limits persist

---

*Report generated at 2026-03-15T09:00:28Z*
*Script: `/root/scripts/search-tool-monitor/search_tool_monitor.py`*
*Data: `/root/scripts/search-tool-monitor/data`*