---
pubDatetime: 2026-04-08T19:00:00Z
title: "Google Cloud Director's Agent-Skills: A 7-Step Vibe Engineering Workflow"
postSlug: "google-agent-skills-vibe-engineering-workflow"
description: "Google Cloud Director's Agent-Skills: A 7-Step Vibe Engineering Workflow"
tags:
  - agent-skills
  - addy-osmani
  - vibe-engineering
  - tdd
  - ai-coding
  - vertical-slicing
---

# Google Cloud Director's Agent-Skills: A 7-Step Vibe Engineering Workflow

Addy Osmani, director of Google Cloud, recently released a production-grade agent-skills library that brings Google's internal software development best practices to AI coding workflows. Sean Kochel put it through its paces in a 31-minute walkthrough, building a complete recipe forking feature from scratch. Here's what makes this library different from the growing pile of AI coding orchestration tools.

> **TL;DR**: The `agent-skills` library provides 19 skills across 7 slash commands that take you from vague idea to deployed code. It uses vertical slicing, test-driven development, and structured review phases — all within a framework flexible enough to adapt to any project.

## The Problem It Solves

Most AI coding orchestration tools are getting more complicated without necessarily doing things better. You tell an LLM what you want, it makes assumptions, and you get a result that may or may not work. The agent-skills library takes the opposite approach: it quizzes you, plans carefully, builds incrementally, and verifies at every step.

## The 7-Step Pipeline

The workflow follows a structured pipeline that resembles GitHub's SpecKit:

**Define → Plan → Build → Verify → Review → Ship**

Each step has dedicated skills that handle specific concerns:

| Stage | Skills | Output |
|-------|--------|--------|
| **Define** | Idea Refine, Spec Driven Dev | Refined concept + PRD |
| **Plan** | Planning & Task Breakdown | Phased task list with acceptance criteria |
| **Build** | Incremental Implementation, Frontend UI Engineering, API & Interface Design, Context Engineering | Working vertical slices |
| **Verify** | Browser Testing, Debugging Workflows | Tested, debugged code |
| **Review** | Code Quality, Simplification, Security & Hardening, Performance Optimization | Production-ready code |
| **Ship** | CI/CD Pipeline Setup | Deployed with guardrails |

## Vertical Slicing vs Horizontal Slicing

The library enforces vertical slicing — a concept worth understanding if you're new to structured AI development.

**Horizontal slicing** (what most people do): Build all frontend components, then all backend logic, then connect them. The problem? Nothing works until everything works.

**Vertical slicing** (what agent-skills does): Build one complete feature slice at a time — frontend, backend, database schema, API — so each piece is independently testable and verifiable.

The demo shows this clearly: Phase 1 was foundation (database + types), Phase 2 was core backend, Phase 3 was the chat UI, and Phase 4 was integration. Each phase produced working, testable code.

## Test-Driven Development Built In

The incremental build skill follows a strict red-green-refactor cycle:

1. **Red** — Write a failing test first
2. **Green** — Write the minimal logic that makes the test pass
3. **Refactor** — Clean up while keeping tests green

This isn't optional — it's baked into the build command. When the demo built the fork context API, it wrote the failing tests first, confirmed they failed, then implemented the logic to pass them.

## The Demo: Recipe Forking Feature

Sean built a recipe forking system for his app "ForkCast" using the full pipeline:

1. **Idea Refine** — Started with a vague concept (git-style forking for recipes), answered 5 clarifying questions about triggers, display, permissions, nesting depth, and scope
2. **Spec Driven Dev** — Generated a full PRD with objectives, acceptance criteria, tech stack, code conventions, and boundaries
3. **Planning** — Created a phased build plan with dependency graph and vertical slices
4. **Build (Phase 1-4)** — Executed each phase separately (critical for context window management), using frontend and backend skills as needed
5. **Debug** — Hit a bug where variants weren't rendering; the debugging skill identified a null field in the root recipe ID and fixed it
6. **Review** — Ran the five-axis review (correctness, readability, architecture conformance, security, performance) and caught issues like missing SQL injection protection
7. **Ship** — Set up GitHub Actions CI/CD with feature branch → development → master pipeline

## Key Takeaways

- **Always specify which phase to build** — If you don't, the library tries to build the entire plan at once, which destroys your context window
- **Explicitly invoke skills you need** — Don't rely on the system to choose the right skill; tell it to use frontend or API skills when you know they're relevant
- **The review phase catches real issues** — The five-axis review found security vulnerabilities (SQL injection via missing ORM) that Claude Code introduced
- **CI/CD setup is automated** — The shipping skill generates GitHub Actions configs with proper branching strategies based on your project's actual testing setup

## Environment Integration: How This Maps to Your Stack

This library is directly relevant if you're running AI-powered development workflows:

- **The skill structure mirrors your existing superpowers system** — agent-skills uses `.claude/skills/` with markdown files, similar to your `~/.config/opencode/skills/` setup
- **The review pipeline maps to your validation gates** — Your `validate-delivery` and `verification-before-completion` skills serve a similar purpose to the five-axis review
- **Vertical slicing aligns with your phase-based execution** — Your `executing-plans` skill already implements phased task execution
- **The CI/CD skill could enhance your deployment** — If you're not already running automated test gates before container rebuilds, the shipping skill's approach is worth adopting

## The Resource

The library is open source and available at [github.com/addyosmani/agent-skills](https://github.com/addyosmani/agent-skills).

**Tags**: ai-coding, vibe-engineering, agent-skills, addy-osmani, tdd, vertical-slicing, ci-cd
**Categories**: AI Automation, Developer Tools
