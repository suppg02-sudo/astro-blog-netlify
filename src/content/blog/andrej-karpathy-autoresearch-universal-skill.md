---
pubDatetime: 2026-03-29T16:00:00Z
title: "I Turned Andrej Karpathys Autoresearch Into a Universal Skill"
postSlug: "andrej-karpathy-autoresearch-universal-skill"
description: "A technical writer adapts Andrej Karpathys autoresearch pattern into a universal skill for optimizing prompts, documentation, and anything with measurable outputs."
tags:
  - prompt-engineering
  - karpathy
  - automation
  - autoresearch
  - ai
---

# I Turned Andrej Karpathys Autoresearch Into a Universal Skill

I'm a technical writer. I spend my days in documentation repos, Markdown files, API references, style guides, and SEO audits. I don't train language models. I don't write CUDA kernels. But when Andrej Karpathy dropped his autoresearch, I couldn't stop thinking about it.

**The idea was so simple it felt obvious in hindsight:**

> Let an AI agent run experiments on its own, measure the results, keep what works, throw away what doesn't, and repeat until it's good.

I remember reading the repo and thinking: this isn't for me.

## The YouTuber That Helped Me Connect the Dots

A few days later, Nick Saraev had taken Karpathy's exact pattern and applied it to optimizing text-to-image prompts for whiteboard diagrams.

His 4 criteria were:

1. Is all the text legible? Yes/No
2. Are the colors soft pastels? Yes/No
3. Is the layout linear? Yes/No
4. Are there numbers or ordinals? Yes/No

10 diagrams, 4 questions each, max score of 40. He started at 32/40. By run 6 - about 12 minutes later - he hit 40/40.

## Vibe-Coding It Into a Skill.md

I decided to build a universal autoresearch skill that could adapt to any repository, any tech stack, any optimization goal.

## Version 1.1

The v1 skill had 5 phases:

1. Repo Discovery
2. Target Suggestions
3. Metric Definition
4. Baseline
5. Autoresearch Loop

## What the Final Version Includes

- Eval isolation
- Validation set
- Structured mutation operators
- Sample tracking
- Context window management
- Plateau breaker

## A Docs Example: SEO for Technical Documentation

Starting score: 24/40. Final score: 40/40 after 14 runs. 66.7% improvement.

## Am I in the Right Direction?

I'm a technical writer. I didn't build a startup. I took an idea from a world-class AI researcher, translated it through a YouTube video, and built production-grade tooling by having a conversation.

**This is how AI works today. Not next year. Today.**

---

*Originally published on [Medium](https://medium.com/@k.balu124/i-turned-andrej-karpathys-autoresearch-into-a-universal-skill-1cb3d44fc669) by Balasubramanyam Kosuri.