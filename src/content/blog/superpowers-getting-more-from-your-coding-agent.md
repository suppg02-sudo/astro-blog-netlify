---
pubDatetime: 2026-03-29T22:30:00Z
title: "Superpowers: Getting More Than Just /using-superpowers From Your Coding Agent"
postSlug: "superpowers-getting-more-from-your-coding-agent"
description: "A practical guide to obra/superpowers — the agentic skills framework that automates brainstorming, TDD, subagent dispatching, and systematic debugging in Claude Code, Cursor, OpenCode, and Gemini CLI."
tags:
  - developer-tools
  - superpowers
  - coding-agents
  - ai
  - tutorial
  - claude-code
---

## Stop Saying /using-superpowers and Start Using Superpowers

If you installed [obra/superpowers](https://github.com/obra/superpowers) and all you do is type `/using-superpowers` before every conversation, you are leaving 90% of the framework on the table.

Superpowers is not a single command. It is a complete software development methodology baked into 14 composable skills that your coding agent loads and follows automatically. The `/using-superpowers` slash command is just the bootstrap — the on-ramp. The real power is that **you should never need to invoke it manually**. The skills trigger themselves.

This post walks through the full workflow, every skill in the library, advanced features most people miss, and practical tips for getting the best results.

---

## How Superpowers Actually Works

Created by [Jesse Vincent](https://blog.fsck.com) (of Keyboardio and RT/SVN fame), Superpowers installs as a plugin and injects a bootstrap prompt at session start. That bootstrap teaches your agent three things:

1. **You have skills.** They live in markdown files called SKILL.md.
2. **Search for skills before acting.** If a skill exists for what you are about to do, you must use it.
3. **Follow the skill exactly.** Skills are mandatory workflows, not suggestions.

The result: your agent stops jumping straight to code and instead follows a disciplined pipeline.

---

## The Full Workflow (7 Stages)

### Stage 1: Brainstorming

**Skill:** brainstorming | **Triggers:** Automatically when you describe something you want to build

Your agent does not start coding. It asks questions. One at a time. It explores your intent, proposes 2-3 approaches with trade-offs, and presents the design in sections you can actually read and approve.

Key behaviours:
- Asks one question per message (never overwhelms you)
- Proposes multiple approaches with a recommendation
- Presents design in chunks for incremental approval
- Offers a visual companion (browser-based mockups) for UI work
- Writes a design doc to docs/superpowers/specs/ and commits it
- Runs a self-review for placeholders, contradictions, and scope creep
- **Hard gate:** No code until you approve the design

**Pro tip:** The brainstorming skill has an anti-pattern detector. If your agent thinks "this is too simple to need a design," that is exactly when unexamined assumptions cause the most wasted work. Every project goes through the process.

### Stage 2: Git Worktrees

**Skill:** using-git-worktrees | **Triggers:** After design approval

Your agent creates an isolated git worktree on a new branch. This means you can run multiple parallel tasks on the same project without them clobbering each other. It verifies a clean test baseline before proceeding.

### Stage 3: Writing Plans

**Skill:** writing-plans | **Triggers:** After design approval

Your agent breaks the work into bite-sized tasks (2-5 minutes each). Every task includes exact file paths, complete code snippets, and verification steps. The plan is written so that "an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing" could follow it.

It enforces YAGNI (You Aren't Gonna Need It) and DRY by default.

### Stage 4: Subagent-Driven Development

**Skill:** subagent-driven-development or executing-plans | **Triggers:** After plan approval

This is where it gets really interesting. Your agent dispatches a **fresh subagent per task** — each with isolated context so there is no pollution between tasks. After each task completes, two separate review subagents check the work:

1. **Spec compliance reviewer** — Did the implementer build exactly what was asked? Nothing more, nothing less?
2. **Code quality reviewer** — Is the code well-written? Good patterns, no smells?

If either reviewer finds issues, the implementer fixes them and gets reviewed again. The loop continues until both pass.

**Pro tip:** The framework uses model selection strategically. Mechanical tasks (1-2 files, clear spec) get fast cheap models. Integration tasks get standard models. Architecture and review tasks get the most capable model. This saves tokens and increases speed.

**Pro tip 2:** After all tasks complete, a final code reviewer reviews the entire implementation holistically before the branch is finished.

### Stage 5: Test-Driven Development

**Skill:** test-driven-development | **Triggers:** During every implementation task

Subagents follow strict RED-GREEN-REFACTOR:
1. Write a failing test
2. Watch it fail
3. Write the minimal code to make it pass
4. Watch it pass
5. Commit

If a subagent writes code before tests, it deletes the code and starts over with tests first.

### Stage 6: Code Review

**Skill:** requesting-code-review | **Triggers:** Between tasks

Automated review against the plan. Issues are reported by severity. Critical issues block progress until fixed.

### Stage 7: Finishing the Branch

**Skill:** finishing-a-development-branch | **Triggers:** When all tasks complete

Verifies all tests pass, then presents you with options: merge locally, create a PR, keep the branch, or discard it. Cleans up the worktree.

---

## The Complete Skills Library

### Testing

| Skill | Purpose |
|-------|---------|
| test-driven-development | Enforces RED-GREEN-REFACTOR cycle. Includes a testing anti-patterns reference. |

### Debugging

| Skill | Purpose |
|-------|---------|
| systematic-debugging | 4-phase root cause process: investigate, analyse, hypothesise, implement. Includes root-cause tracing, defence-in-depth, and condition-based waiting techniques. |
| verification-before-completion | Ensures the fix actually worked before claiming success. |

### Collaboration

| Skill | Purpose |
|-------|---------|
| brainstorming | Socratic design refinement with visual companion support |
| writing-plans | Detailed implementation plans broken into 2-5 minute tasks |
| executing-plans | Batch execution with human review checkpoints |
| dispatching-parallel-agents | Run independent tasks concurrently via subagents |
| requesting-code-review | Pre-review checklist with severity-based issue reporting |
| receiving-code-review | Structured approach to responding to code review feedback |
| using-git-worktrees | Isolated parallel development branches |
| finishing-a-development-branch | Merge/PR/cleanup decision workflow |
| subagent-driven-development | Fresh subagent per task with two-stage review (spec + quality) |

### Meta

| Skill | Purpose |
|-------|---------|
| writing-skills | Create new skills following best practices (includes testing methodology) |
| using-superpowers | Introduction to the skills system (what /using-superpowers loads) |

---

## Advanced Features Most People Miss

### 1. Skills Trigger Automatically

You do not need to invoke skills manually. The bootstrap prompt tells your agent: "If you think there is even a 1% chance a skill might apply to what you are doing, you must invoke it." The agent checks before every task.

The only time you need `/using-superpowers` is if the bootstrap failed to inject at session start.

### 2. The Red Flag Detector

The using-superpowers skill includes a table of rationalisations your agent might use to skip skills:

| Thought | Reality |
|---------|--------|
| "This is just a simple question" | Questions are tasks. Check for skills. |
| "Let me explore the codebase first" | Skills tell you HOW to explore. Check first. |
| "This doesn't need a formal skill" | If a skill exists, use it. |
| "I'll just do this one thing first" | Check BEFORE doing anything. |
| "The skill is overkill" | Simple things become complex. Use it. |

The agent is literally trained to catch itself rationalising and stop.

### 3. Visual Companion for UI Brainstorming

The brainstorming skill can spin up a browser-based companion for showing mockups, wireframes, and architecture diagrams. It asks for consent before activating and only uses it for questions where seeing beats reading.

### 4. Model Selection Strategy

Subagent-driven development uses different model tiers for different roles:
- **Mechanical tasks** (isolated functions, clear specs): fast, cheap model
- **Integration tasks** (multi-file coordination): standard model
- **Architecture and review**: most capable model

This is not documented prominently but is built into the subagent dispatch logic.

### 5. Systematic Debugging is a Power Tool

The debugging skill is not just "read the error and fix it." It is a rigorous 4-phase process:

1. **Root Cause Investigation** — Read errors, reproduce consistently, check recent changes, gather evidence at every component boundary
2. **Pattern Analysis** — Find working examples, compare against references, identify every difference
3. **Hypothesis and Testing** — Form a single hypothesis, make the smallest possible change to test it
4. **Implementation** — Create a failing test, fix the root cause, verify

The iron law: **no fixes without root cause investigation first.** If three fixes fail in a row, the process stops and questions the architecture rather than attempting a fourth fix.

### 6. Subagent Implementer Status Codes

Implementer subagents report back with status codes that the controller handles differently:

| Status | Meaning |
|--------|---------|
| DONE | Proceed to review |
| DONE_WITH_CONCERNS | Review concerns before proceeding |
| NEEDS_CONTEXT | Provide missing info and re-dispatch |
| BLOCKED | Assess blocker — escalate model, break task down, or escalate to human |

### 7. User Instructions Always Win

Superpowers skills override default system behaviour, but your explicit instructions (CLAUDE.md, GEMINI.md, AGENTS.md) always take the highest priority. If your project config says "skip TDD" and a skill says "always TDD," your config wins.

### 8. The Brainstorming Visual Companion

When brainstorming UI work, the skill can spin up a local web server to show you live mockups, wireframes, and diagrams directly in your browser. It only activates for visual questions — text-based questions stay in the terminal. It asks for consent first and warns that it can be token-intensive.

### 9. Spec Self-Review

After writing a design doc, the brainstorming skill automatically runs a self-review checking for:
- Placeholder scan (TBD, TODO, incomplete sections)
- Internal consistency (contradictions between sections)
- Scope check (too large for a single plan?)
- Ambiguity check (requirements that could be interpreted two ways)

It fixes issues inline without bothering you.

---

## Platform Support

Superpowers works across multiple coding agent platforms:

| Platform | Install Method |
|----------|---------------|
| **Claude Code** | /plugin install superpowers@claude-plugins-official |
| **Cursor** | /add-plugin superpowers in Agent chat |
| **Codex** | Follow instructions at .codex/INSTALL.md |
| **OpenCode** | Follow instructions at .opencode/INSTALL.md |
| **Gemini CLI** | gemini extensions install https://github.com/obra/superpowers |

---

## Tips for Getting the Best Results

### 1. Let it ask questions

The biggest mistake new users make is rushing past the brainstorming phase. When your agent asks clarifying questions, answer them thoughtfully. The quality of the design doc directly determines the quality of the implementation.

### 2. Review the design doc before saying go

After brainstorming, your agent writes a spec to docs/superpowers/specs/ and asks you to review it. Actually read it. Catching a misunderstanding here costs seconds. Catching it after implementation costs hours.

### 3. Keep tasks small

The plan should break work into 2-5 minute tasks. If tasks are too large, ask your agent to decompose further. Small tasks mean subagents succeed more often and reviews catch issues earlier.

### 4. Trust the process for debugging

When you hit a bug, do not tell your agent to "just fix it." Let the systematic-debugging skill run its course. The 4-phase process has a 95% first-time fix rate versus 40% for ad-hoc guessing.

### 5. Use worktrees for parallel work

If you have multiple features to build, let Superpowers create worktrees for each. You can brainstorm and plan feature A while a subagent implements feature B.

### 6. Do not fight TDD

If you want to skip TDD for a specific task, put it in your CLAUDE.md. Otherwise, let the test-driven-development skill do its job. The tests it writes are your safety net.

### 7. Create custom skills

Use the writing-skills skill to create your own skills for domain-specific workflows. Skills are just markdown files with a YAML frontmatter. The framework will automatically discover and use them.

### 8. For large projects, decompose first

If you describe something with multiple independent subsystems (e.g., "build a platform with chat, file storage, billing, and analytics"), the brainstorming skill will flag this immediately and help you decompose into sub-projects. Each sub-project gets its own spec, plan, implementation cycle.

---

## The Philosophy

Superpowers is built on four principles:

- **Test-Driven Development** — Write tests first, always
- **Systematic over ad-hoc** — Process over guessing
- **Complexity reduction** — Simplicity as primary goal
- **Evidence over claims** — Verify before declaring success

As Jesse Vincent puts it: the plan is written for "an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing." And somehow, that plan produces senior-level output.

The framework is built on a fascinating insight from [research by Dan Shapiro and Robert Cialdini](https://gail.wharton.upenn.edu/research-and-insights/call-me-a-jerk-persuading-ai/) showing that persuasion principles (authority, commitment, scarcity, social proof) work on LLMs. Superpowers uses these same levers — not to jailbreak agents, but to make them more reliable and disciplined. The "mandatory" language, the status codes, the review loops — they are all engineered to keep the agent on track.

---

## Resources

- **GitHub:** [github.com/obra/superpowers](https://github.com/obra/superpowers)
- **Author blog post:** [Superpowers for Claude Code](https://blog.fsck.com/2025/10/09/superpowers/)
- **Discord community:** [discord.gg/Jd8Vphy9jq](https://discord.gg/Jd8Vphy9jq)
- **Issues:** [github.com/obra/superpowers/issues](https://github.com/obra/superpowers/issues)
- **Sponsor the author:** [github.com/sponsors/obra](https://github.com/sponsors/obra)
