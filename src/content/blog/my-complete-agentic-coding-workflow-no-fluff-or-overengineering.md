---
pubDatetime: 2026-02-24T01:42:38Z
title: "My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)"
postSlug: "my-complete-agentic-coding-workflow-no-fluff-or-overengineering"
description: "My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)"
tags:
  - AI workflow
  - productivity
  - agentic coding
  - framework
  - software development
  - Claude Code
  - PIV loop
---

## Introduction

Everyone knows that you need a framework for working with coding agents, but not many people have one that's simple, really their own, and something they can evolve over time. There are a lot of overengineered frameworks out there on GitHub—all these multi-agent systems people are creating. While I respect what people are working on, a lot of times you just need something really simple that just gets the job done for you.

The reason is simple: you have good ideas that you want to build, and you don't want to spend more time creating your agentic coding workflows than you do actually coding.

This is my dead-simple framework that I use every single time I'm starting a new project with my coding agent. Brownfield development (working on an existing codebase) is slightly different—that's for another video. Here, we're focusing on greenfield development. We want a simple framework to get our feet on the ground running as fast as possible building anything new.

## What Is the AI Layer?

Your AI layer is all assets in your codebase that you created to be context for your coding agent. This includes:

- **PRD (Product Requirements Document)**: Initial scope of work to create minimum viable product
- **Global Rules (agents.mmd)**: Constraints, conventions, tech stack, project structure, code patterns
- **Reference Folder**: On-demand context for specific tasks like API endpoints or frontend components
- **Commands**: Reusable workflows that you invoke yourself
- **Skills**: Context files that the agent decides to read based on task type

The AI layer is about creating structure—making it repeatable. Everything I'm covering here is universal. These principles will apply no matter which coding agent you're using.

## Part 1: Creating Your PRD

The first step is initial planning—creating what's called a PRD. This is the initial scope of work that defines what we need to create to build a minimum viable product for our application.

### The Brain Dump

Start with a casual conversation. Tell your coding agent about your idea, some ideas you have for tech stack and architecture. Keep it unstructured at first—it makes it easy to get started. Use a speech-to-text tool like Aquavo, WhisperFlow, or Epicenter Whisper. You can promise yourself you'll never be able to type 226 words per minute.

### Agent Research and Questioning

This is the most important part. When you give your brain dump to the agent, have it spin off sub-agents to do research. For example:

- Research best practices for the type of application you're building
- Research specific tech stack choices
- Research architecture approaches

Then—and this is critical—have the agent come back to you with questions. A LOT of questions. Every single question you answer removes an assumption from your coding agent.

The golden rule: **One bad line of code is just one bad line. One bad line of a plan is maybe 100 lines of bad code. But one bad line in a PRD could be a thousand bad lines of code.** Because that's when you have misalignment.

Use the agent's question tool—it can give you multiple-choice options where you can also type your own answer. Blitz through it. It might take 20-25 questions, but every single question you answer could save you from having hundreds of lines of bad code.

### Structured PRD Creation

Once you've answered all the questions, use a command to create a structured PRD. The PRD should include:

- MVP scope (what to build)
- Out of scope (what not to build right now)
- Tech stack
- Architecture
- Directory structure
- Phases of work

The PRD is the only thing that's going to survive from this initial conversation. Make sure all your answers are captured here.

## Part 2: Setting Up Global Rules

After your PRD is created, you need to set up global rules. This goes in a file typically called `agents.mmd` (universal standard for naming). This file contains:

- Tech stack
- Commands to run your application
- Testing strategy
- Logging strategy
- Project structure (codebase index)
- Architecture
- Code patterns (naming conventions, validation strategies)

### The Progressive Disclosure Pattern

This is crucial for context management. The principle is: load minimal context upfront, then point to on-demand context when needed.

Keep your `agents.mmd` concise—video example shows just 233 lines. Use a reference folder for larger documents:

- `claw.md`: General reference, loaded always
- `api.md`: Loaded when working on API routes
- `components.md`: Loaded when building frontend components

This way, the agent can discover context progressively based on what it's currently working on, keeping context consumption efficient.

## Part 3: The Commands System

**Commandify everything.** If you do something more than twice, make it a command.

There's a distinction:

- **Commands**: Things you invoke yourself (e.g., `/commit`, `/prime`)
- **Skills**: Things the agent decides to read based on task context

Key commands for the framework:

- `/create PRD`: Generates structured PRD from conversation context
- `/create rules`: Discovers codebase, does web research, generates global rules
- `/prime`: Codebase exploration and context sync at start of every new session
- `/commit`: Creates standardized git commit messages
- `/plan feature <name>`: Creates structured plan with task list and validation strategy

## Part 4: The Prime Command

At the start of every new conversation with a coding assistant, you need it to catch itself up to speed on codebase state. The `/prime` command handles this:

1. Reads documentation
2. Explores codebase structure
3. Uses sub-agents for analysis
4. Checks git log (your long-term memory)
5. Reads core files
6. Identifies main entry points
7. Outputs understanding report

The git log is your long-term memory. When your agent runs `/prime` later, it can see the history of what you built recently, which guides what comes next and helps it understand patterns it should follow.

## Part 5: PIV Loop (Plan-Implement-Validate)

This is the core execution cycle. We take focused work (usually a phase from the PRD) and run it through this entire process.

### Planning Phase

There are two layers of planning:

1. **Top-level project planning**: Already done with PRD + global rules
2. **Task-specific planning**: Structure plan for individual features

For task-specific planning, start unstructured—explore general ideas, architecture, spin off sub-agents for codebase analysis. Then convert to a structured document with:

- Goal and success criteria
- Any documentation references
- Task list (specific files to create/update)
- **Validation strategy** (most important part)

The validation strategy should be specific. Use a validation pyramid:

- Type checking and linting
- Unit testing
- End-to-end testing
- User journey testing

The key principle: **Reset context between planning and implementation** to prevent context bloat during execution.

### Implementation Phase

Delegate all coding to the AI agent. It uses the structure plan as its only context. Trust but verify.

**Environment Variable Setup**: Create an `.env.example` file with all environment variables needed. Have the agent read this during planning. Then set up your actual `.env` with secrets before implementation. This prevents the agent from getting tripped up on missing environment variables during execution.

### Validation Phase

After the agent says it's done, validate thoroughly.

The agent should run its own validation:
- Unit testing
- Integration testing
- End-to-end testing using browser automation

But you still need to do **human validation**:

- Spin up the application
- Walk through it as a user would
- Make sure everything is working
- Only then commit

The validation is the quality gate between you trusting the agent and being absolutely certain it works before shipping.

## Live Build Demonstration: Linktree Clone

To make this concrete, I built a self-hosted Linktree-style landing page builder as a demonstration. Users can create an account, set up their own landing page with links, reorder them, and view click-through analytics.

### Tech Stack

- Frontend: Next.js
- Database: Neon (PostgreSQL)
- ORM: Drizzle
- Authentication: Neon Auth
- Deployment: Vercel

### Phase 1: Foundation

Built authentication, user pages, link management, database schema, and basic persistence.

The agent validated using browser automation—spun up the backend and frontend, ran database migrations, built its own link tree, and tested like a user would. Then I did manual validation: created an account, set display name, added links (YouTube, LinkedIn, X), confirmed save and refresh works.

## Part 6: Commit Messages

Your commit history is your long-term memory. Use a `/commit` command to standardize commit messages. When your agent primes later, it checks the git log to see:

- What you built recently
- What patterns you followed
- What comes next

This consistency creates a narrative for your codebase that guides future decisions.

## Part 7: Regression Testing

As you add more features through additional PIV loops, you need to make sure old stuff doesn't break. Build a framework for regression testing.

You can create your own test harness, or use AI testing platforms like QA Tech that evolve with your codebase. They add test cases automatically as you build more features.

## Part 8: System Evolution Mindset

This is the most high-leverage part of the entire process. When you encounter a bug or misalignment, don't just fix the bug—fix the system.

Ask yourself: What can we add to the AI layer to prevent this from happening again?

Examples from the video:
- Style guide added after the agent made assumptions about frontend styling
- Components guide added for better frontend component guidance
- Regression testing commands added to ensure stability
- On-demand context files added as patterns emerged

Every bug or misalignment is an opportunity to make your agent more reliable for the next task.

## The Four Golden Rules

### 1. Context Management

Context is your most precious resource when working with AI coding assistants. Use progressive disclosure—load minimal upfront, then on-demand context for specific tasks. Keep your main context concise.

### 2. Commandify Everything

If you do something more than twice, make it a command. Creates reusable workflows that evolve with your project.

### 3. System Evolution Mindset

Don't just fix bugs, fix the system. When issues arise, update your AI layer to prevent recurrence.

### 4. Trust but Verify

Delegate coding to the agent, but validate thoroughly. Use the validation pyramid, always test manually before committing.

## Why This Framework Works

Compared to overengineered frameworks like BMAD or GitHub SpecKit, this is:

- Simpler to make your own
- Easier to evolve for your use case
- Less friction getting started
- Universal across different coding agents

The investment in planning pays massive dividends. After your first PIV loop, all subsequent loops go faster because everything is in place—rules, commands, patterns, and a shared understanding with the agent.

## Getting Started

You can start with a generic set of commands and skills. The point is that as your codebase grows, you evolve your commands to make them more powerful for your specific use case. That's the recommendation: use this as a starting point and easily evolve it for your own preferences.

This framework is dead simple on purpose. You can take it for yourself and easily evolve it. That's the goal—something that's reliable and repeatable, something you can use over and over again for new features and new codebases.

## Conclusion

This approach emphasizes planning ROI over implementation speed, context management over token consumption, and system evolution over bug fixes. By investing time upfront to create a solid AI layer with clear rules, reusable commands, and an evolvable framework, you make AI-assisted development faster, more reliable, and consistently repeatable.

The live demonstration showed that even for a real project (a Linktree clone with authentication, database, and analytics), this framework got you from zero to a working foundation in a single PIV loop with confidence because of the planning and validation.

---

## References

**Full Transcript:** `[file in resources]`

**Short Summary:** `[file in resources]`