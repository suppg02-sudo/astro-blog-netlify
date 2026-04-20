---
pubDatetime: 2026-03-10T00:03:18Z
title: "YouTube: Anthropic Just Changed How Agents Call Tools. I Stole It for My Qwen3.5 Agent"
postSlug: "youtube-anthropic-just-changed-how-agents-call-tools-i-stole-it-for-2026-03-10"
description: "YouTube: Anthropic Just Changed How Agents Call Tools. I Stole It for My Qwen3.5 Agent"
tags:
  - agents
  - video-summary
  - youtube
  - just
  - call
  - changed
  - anthropic
---

> **Video**: [Anthropic Just Changed How Agents Call Tools. I Stole It for My Qwen3.5 Agent](https://youtu.be/R7OCrqyGMeY?si=9IGTOOw2YIvRLS9Z) by **The AI Automators**
> **Transcript**: 3,443 words

Here's a summary of "Anthropic Just Changed How Agents Call Tools. I Stole It for My Qwen3.5 Agent" by The AI Automators:

This video from "The AI Automators" delves into Anthropic's recent advancements in AI agent tooling, specifically highlighting programmatic tool calling and the tool search tool. While these features were released by Anthropic for their Claude API, the presenter demonstrates that they are powerful, universal agent design patterns applicable to any framework or model. The video illustrates their implementation in a custom Python and React agent, leveraging the Qwen3.5 27B parameter model, showcasing how these methods significantly reduce token usage, mitigate context window bloat, and improve tool selection and execution efficiency in complex AI agent systems.

### Introduction to Anthropic's Tooling Innovations

Last November, Anthropic introduced beta features to address significant challenges in building AI agents: excessive context window consumption by tool definitions, bloat from intermediate tool call results, and difficulty for agents to select the right tool from a large set. These features, now generally available on the Claude API with Sonnet 4.6, aim to solve these problems. Anthropic claimed an "85% reduction in token usage," leading some to dramatically declare that "Anthropic has killed tool calling, or at least traditional tool calling." The presenter, however, asserts that while dramatic, the underlying concepts—programmatic tool calling and the tool search tool—are "core agent building design patterns that you can use in any framework or with any model," not exclusive to Claude.

### The Tool Search Tool: Dynamic Tool Loading

The first feature demonstrated is the **Tool Search Tool**, designed to combat context bloat caused by loading all available tool definitions upfront. Traditionally, an agent might load dozens of tools (e.g., 60 tools consuming 13,000 tokens) even before processing a user's first query.

The Tool Search Tool's innovation is to defer tool loading. Instead of pre-loading every tool, only a minimal set (including the search tool itself) is initially in context. When the agent needs a specific tool, it uses the "tool search tool" to query a tool registry, discover the relevant tool by name or keyword, and then load its full schema into context *only when needed*. This dynamic loading dramatically reduces the initial context footprint. For instance, the demo showed an initial context reduced from 13,000 tokens (with 60 tools) to 6,300 tokens (with 12 tools and the search tool). Once a tool is loaded, it remains in context for the duration of the conversation, preventing redundant searches.

### Programmatic Tool Calling: Scripting Complex Tasks

The more impressive feature, according to the presenter, is **Programmatic Tool Calling**. This tackles the inefficiency of traditional, sequential tool execution, where an LLM must orchestrate numerous individual tool calls, leading to massive context bloat from intermediate results.

The problem is illustrated with a "budget compliance check" example: identifying team members who exceeded their Q3 travel budget. A traditional approach for 20 team members involved 56 tool calls (fetching expenses for each member), consumed 76,000 tokens, and even missed one correct answer. This sequential, LLM-orchestrated approach is inefficient for repetitive tasks.

Programmatic tool calling solves this by having the LLM generate a **script** (e.g., Python code) that encapsulates the logic for such repetitive operations. This script is then executed in an isolated sandbox. The LLM's role shifts from making individual tool calls to *generating a program* that makes those calls efficiently. While Anthropic's paper might suggest "one-shot" code generation, the demo with Claude Haiku and Qwen3.5 showed a more "realistic" iterative process where the LLM generated code, ran it, learned from errors, and refined the script to arrive at the correct answer. Even with iteration, this approach is far more efficient for scale. The presenter emphasizes, "If you had 2,000 team members, it would be a completely different story because the LLM would need to run 2,000 individual calls, which just wouldn't work anyway. So in that situation, programmatic tool calling is required." The Qwen3.5 demonstration achieved accurate results in fewer tokens (45,000 tokens over 4 tool calls) compared to Haiku, highlighting the efficiency gains.

### System Architecture: Sandbox and Tool Bridge

To enable secure and efficient programmatic tool calling, the system uses a **Docker sandbox** (leveraging the `LLM Sandbox` GitHub repo) for code execution. This sandbox is isolated and has no direct internet access, enhancing security.

A crucial component is the **Tool Bridge**. When the LLM generates a script that includes tool calls (e.g., `get_expenses()`), these calls within the sandbox are not directly executed externally. Instead, they are routed securely back to the main Python application (via FastAPI). The Python app then authenticates the request, makes the actual external API call, fetches the response, and sends it back to the sandbox. This means that "The LLM is totally out of the picture here" during the execution of multiple tool calls within the generated script, saving tokens and speeding up execution significantly. For enhanced security, using GVisor with Docker containers is recommended. The video also notes that LLMs perform better generating "vanilla Python" or TypeScript to interact with tools, rather than complex MCP schemas directly. The system converts MCPs into auto-generated Python function stubs within the sandbox, making code generation more straightforward for the LLM.

### Efficient Tool Design and Tool Use Examples

Beyond the core features, the video touches on:

*   **Efficient Tool Design:** The importance of minimizing schema bloat in tool definitions themselves. The GitHub MCP, for instance, reduced its token footprint from 26,000 to 4,000 tokens.
*   **Tool Use Examples:** JSON schemas define structure, but not usage patterns (e.g., date formats). Anthropic introduced "tool use examples" to provide specific formatting examples for parameters (e.g., `YYYY-MM-DD`). This guidance acts as "multi-shot prompting," improving accuracy on complex parameter handling from 72% to 90%.

Ultimately, Anthropic's advice (and the video's conclusion) is to **layer these features strategically**. Use Tool Search for context bloat from definitions, programmatic tool calling (with a sandbox) for large intermediate results and repetitive tasks, and Tool Use Examples for precise parameter handling.

### Key Takeaways

*   Anthropic's new tool calling features, **Tool Search** and **Programmatic Tool Calling**, are powerful, model-agnostic design patterns for building efficient AI agents.
*   The **Tool Search Tool** significantly reduces initial context window usage by dynamically loading tool definitions only when required, improving scalability.
*   **Programmatic Tool Calling** enables LLMs to generate and execute scripts in a secure, isolated sandbox, efficiently handling complex, repetitive tasks without constant LLM interaction.
*   A **secure "tool bridge" architecture** allows the sandbox to make tool calls via the main application, enhancing security and execution speed by keeping the LLM out of the loop during script execution.
*   **Efficient tool design** (minimizing schema bloat) and **Tool Use Examples** (providing parameter format guidance) further improve agent accuracy and performance.
*   These features should be **strategically applied** based on specific agent challenges, such as context bloat, intermediate result management, or accurate parameter handling.

---

*Summary generated from YouTube transcript (3,443 words) using Gemini 2.5 Flash on 2026-03-10.*