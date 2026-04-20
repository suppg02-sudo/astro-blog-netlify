---
pubDatetime: 2026-02-08T00:06:00Z
title: "How to Use Claude Code Like the People Who Built It"
postSlug: "claude-code-interview"
description: "How to Use Claude Code Like the People Who Built It"
tags:
  - AI Programming
  - Cat Wu
  - Boris Cherny
  - Anthropic
  - Claude Code
---

## Introduction

In this insightful interview from the AI & I podcast, Dan Shipper sits down with Cat Wu and Boris Cherny—the creators of Claude Code at Anthropic—to discuss how they use the tool internally and what they've learned about maximizing its potential. Their journey offers valuable insights into the future of AI-assisted programming.

## A Paradigm Shift in AI Programming

When Dan first used Claude Code around the time of Sonnet 3.7's release, he experienced what he describes as "a completely new paradigm" for thinking about code. The key differentiator was Anthropic's bold decision to eliminate the traditional text editor entirely—reducing the interface to a simple conversation with the terminal.

> "You went all the way and just eliminated the text editor. All you do is talk to the terminal and that's it."

Previous AI programming paradigms followed a familiar pattern: text editors with AI assistants on the side, or tab-based autocomplete systems. Claude Code represents a fundamental departure from this approach.

## The Accidental Innovation

Interestingly, Boris reveals that this revolutionary approach wasn't born from grand design, but rather evolved organically:

> "I think the most important thing is it was not intentional at all. We sort of ended up with it."

Before Claude Code, there was a research prototype called "Clide" (C-L-I-D-E) at Anthropic. It was a heavyweight Python application that took about a minute to start up and required significant indexing overhead.

## Boris's Wake-Up Call

When Boris joined Anthropic, he learned a valuable lesson about using AI tools the hard way. As a new team member, he wrote his first pull request manually, "like a noob." Adam Wolf, his engineering manager and ramp-up buddy, immediately rejected the PR with a pointed question:

> "You wrote this by hand. What are you doing?"

Adam, who had been heavily involved in hacking on Clide, encouraged Boris to try the AI tool. Boris provided a task description, and Clide "one-shot" the entire implementation using what was then Sonnet 3. This experience was transformative—it demonstrated the power of giving the AI clear context and letting it handle the implementation details.

## How Anthropic Dogfoods Claude Code Internally

Anthropic doesn't just build Claude Code—they actively use it throughout their development workflow. This "dogfooding" approach provides several benefits:

1. **Immediate feedback loops**: Engineers experience the tool's limitations directly
2. **Continuous improvement**: Real-world usage drives feature development
3. **Cultural adoption**: Team members learn from each other's techniques
4. **Authentic understanding**: Developers understand user pain points firsthand

The practice of rejecting manually-written code in favor of AI-generated solutions has become part of the team culture, reinforcing the tool's value.

## Favorite Slash Commands and Usage Tips

Based on the interview insights, here are key strategies for getting the most out of Claude Code:

### Give Clear, Context-Rich Descriptions
The key to success lies in providing comprehensive context. Rather than saying "fix the bug," describe the entire scenario:

```bash
claude "In the user authentication flow, users are getting logged out after 30 seconds regardless of activity. The session timeout is set to 8 hours in config. Check Redis session storage and the middleware authentication logic."
```

### Let Claude Handle File Operations
Claude Code isn't just a code generator—it manages your entire codebase:

- Reading files with context
- Making targeted edits
- Running tests and parsing output
- Executing terminal commands

### Start Small, Scale Up
For complex tasks, break them down:

1. Start with a proof-of-concept
2. Iterate on the implementation
3. Let Claude handle refactoring
4. Use Claude for testing and validation

### Leverage Claude's Understanding
The AI excels at understanding codebases at scale:

- Ask it to explain unfamiliar code
- Request architectural overviews
- Get suggestions for improvement
- Use it for code reviews

## The Claude Code Workflow

The following diagram illustrates the typical workflow when using Claude Code effectively:

{{< mermaid >}}
graph TD
    A[User Task] --> B{Provide Context}
    B --> C[Claude Analyzes Codebase]
    C --> D{Understands?}
    D -->|Yes| E[Generate/Edit Code]
    D -->|No| F[Request Clarification]
    F --> B
    E --> G[Execute Tests]
    G --> H{Tests Pass?}
    H -->|Yes| I[Commit Changes]
    H -->|No| J[Debug]
    J --> E
    I --> K[Update Documentation]
    K --> L[Complete Task]

    style A fill:#e1f5fe
    style B fill:#fff9c4
    style C fill:#c8e6c9
    style E fill:#a5d6a7
    style I fill:#81c784
    style L fill:#66bb6a
{{< /mermaid >}}

## Key Takeaways

1. **Embrace the terminal-first approach**: Claude Code represents a fundamental shift from traditional editor-based workflows. The power comes from conversational interaction with your codebase.

2. **Provide comprehensive context**: The quality of Claude's output directly correlates with the clarity and completeness of your task description.

3. **Trust the AI's understanding**: Claude can navigate large codebases, understand relationships between files, and make informed edits.

4. **Iterate and refine**: Don't expect perfect output on the first try. Use Claude's ability to iterate and improve based on feedback.

5. **Learn from the creators**: Anthropic's internal usage demonstrates that the tool becomes more powerful with practice and cultural adoption.

## Summary

Claude Code isn't just another AI programming assistant—it's a reimagining of how developers interact with code. By eliminating the traditional text editor and replacing it with a conversational interface, Cat Wu, Boris Cherny, and the Anthropic team have created something genuinely new.

The key to success lies in providing rich context, trusting the AI's understanding, and embracing iterative refinement. As Boris learned from his first experience at Anthropic: writing code by hand when Claude can handle it faster and better isn't just inefficient—it's missing the point entirely.

The future of programming isn't about AI assisting developers—it's about developers and AI collaborating as partners in the creative process of building software.