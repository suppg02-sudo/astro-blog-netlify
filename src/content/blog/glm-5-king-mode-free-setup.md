---
pubDatetime: 2026-02-15T17:08:23Z
title: "GLM-5 KING MODE: I Left Opus & Codex for This Fully Free Setup"
postSlug: "glm-5-king-mode-free-setup"
description: "GLM-5 KING MODE: I Left Opus & Codex for This Fully Free Setup"
tags:
  - youtube
  - AI
  - GLM-5
  - King Mode
  - Verdant
  - coding
---

In this post, I'll show you exactly how to pair GLM-5 with the King Mode prompt and why this specific combination might be the most powerful free coding setup in 2026.

## Why This Pairing Makes Sense

If you've been following my channel, you know I've been obsessed with two things lately: GLM-5 (which I genuinely believe is the best open model ever released) and the King Mode system prompt (which I've been using to eliminate the lazy parts of every model I touch). But I never combined the two properly—until now.

The results are insane.

### GLM-5: The Best Open Model

The ZAI team designed GLM-5 as the first **open-source system architect model**. Here's what makes it special:

- **Architecture**: 744 billion parameter mixture of experts with 40 billion active per pass
- **Capabilities**: It thinks like an architect, plans automatically, and asks follow-up questions when your prompt is vague
- **Performance**: Scored #1 on my agentic leaderboard, beating Opus 4.6 on Spelt Conban, NookStack Overflow clone, Expo movie tracker—basically everything
- **Cost**: Currently fully free in Kilo Code

### The Problem: Smart vs. Disciplined

After a week of heavy use, I noticed something important: GLM-5 is incredible at long-running tasks (40 minutes, even 3 hours on complex apps). But sometimes, especially on medium complexity tasks, it overthinks.

The ZAI team even acknowledged this: the model tries to be too good on simpler tasks, which actually hurts performance. It's not great at chat or small talk—it's trained heavily on code and system architecture. Sometimes it gives you unnecessarily verbose explanations when you just want code.

**Smart and disciplined are two different things.**

## King Mode: The Solution

King Mode doesn't make the model smarter—it makes it more **focused**.

### Key Components

#### The UltraThink Trigger

This tells the model to stop and assess complexity. It decides whether the task needs:

- Deep architectural reasoning, OR
- Quick execution

Then it commits to a path.

#### Zero Fluff Directive

This strips away the "I hope this helps" filler and forces the model to give you output, not conversation. It eliminates unnecessary explanations instantly.

### The Perfect Metaphor

> **GLM-5 is a brilliant architect who sometimes talks too much and occasionally overthinks small jobs.**
>
> **King Mode is the project manager who walks in and says, "Focus, deliver, no fluff."**

## Why Verdant is Essential

If you just paste King Mode into a regular chatbot or even a single agent editor, you get a better model. That's what I showed in my GLM-4.7 Ultra video. It works, but you're still limited to one task at a time.

**Verdant changes that equation completely.**

Verdant lets you run multiple agents in parallel, each with their own isolated git worktree. That means I can have one GLM-5 agent doing backend architecture while another GLM-5 agent handles the frontend—and they don't step on each other's toes. They each get the full King Mode context, run independently, and each produces senior-level code.

You basically go from having one brilliant architect to having an entire team of brilliant architects.

## Setup Instructions

The setup is surprisingly simple:

### Step 1: Configure Verdant

Open Verdant, go to your model settings, and select GLM-5.

### Step 2: Inject the King Mode Prompt

In Verdant, you can add this to your project rules or the system instructions area. Just paste the full King Mode prompt in there.

**Pro Tip**: You don't need to add the front-end design skill this time. I used to combine King Mode with the front-end skill for GLM-4.7 because that model needed help with design taste. GLM-5 is different—since it's a system architect model, it's already better at structured code and layout logic. If you overload it with too many style constraints, it conflicts with its own reasoning.

Keep the rules lean. King Mode alone is enough for GLM-5. If you want a specific aesthetic, just describe it in your prompt instead of injecting an entire design system.

### Step 3: Use the UltraThink Keyword

This is the important part—use the `ultrathink` keyword at the start of your prompts. This is what actually activates the deep reasoning behavior from King Mode. Without it, the model will still follow the zero fluff rules, but it won't do the full architectural breakdown.

## In Action: Building a Full Stack SaaS Dashboard

For this demo, I'm building a full-stack SaaS dashboard with authentication, a database layer, and a realtime analytics view.

Instead of typing one big prompt and waiting, I spun up three agents simultaneously.

### Agent 1: Backend

```
ultrathink set up a Supabase backend for a SaaS analytics dashboard.
Create the database schema with users, events, and sessions tables.
Implement RLS security policies and create edge functions for data ingestion.
```

Agent 1 starts working. But because of the UltraThink trigger, it doesn't just dump SQL. It pauses, reasons about data relationships, and decides: "Since we need real-time analytics, we should use Supabase realtime subscriptions on the events table. RLS needs to filter by organization ID to support multi-tenancy."

It's architecting the system before writing a single line of code. That's the difference. Without King Mode, GLM-5 would still be good, but it might jump into the SQL first and think about security later. The UltraThink trigger forces it to frontload the thinking.

### Agent 2: Frontend

```
ultrathink. Initialize a Next.js 14 project with Tailwind.
Build the main dashboard layout with a sidebar navigation,
a top metrics bar showing active users, total events, and average session duration,
and a main content area with a real-time line chart.
```

Meanwhile, Agent 2 is setting up the frontend. Because it also has the King Mode context, it's not making a generic dashboard. It's considering component structure, setting up proper error boundaries, and using memoization on the chart components because it knows realtime data means frequent rerenders.

### Agent 3: Integration

```
Ultrathink. Review the current codebase.
Backend is in the Supabase folder and frontend is in the app folder.
Connect them. Create a server action to fetch analytics data and wire it into dashboard components.
Add proper error handling and loading states.
```

This third agent reads both the backend and frontend code, understands the relationship (GLM-5 is genuinely great at grasping full architectures now), and connects everything. It even added a custom hook for the realtime subscription that I didn't ask for—but that makes total sense given the setup.

## The Results

The whole thing—backend, frontend, and integration—took me about **5 minutes** of actual interaction time. The agents did the rest.

When I looked at the diffs in Verdant's diff lens:
- The backend schema was clean
- The RLS policies were actually correct (which is impressive because most models mess up Supabase security policies)
- The frontend was well structured with proper separation of concerns

### Why This Beats GLM-4.7

With GLM-4.7, I had to combine King Mode and the front-end skill to get good results. That model was great at visuals but weak at architecture. So I needed two crutches.

GLM-5 only needs one. King Mode alone unlocks the model's full potential because the architectural intelligence is already built in. The model already plans, already debugs, already asks follow-up questions. King Mode just removes the noise and forces the model to be consistent about it.

And with Verdant's parallel agents, you multiply that effect. Instead of one focused architect, you get a whole team. Each agent runs the same disciplined workflow, each has isolated context, and you're the project manager just assigning tasks and reviewing the output.

## Configuration Guidelines

### Reasoning Effort Levels

GLM-5 is a reasoning model with effort levels. I generally keep the reasoning effort at **medium** for most tasks and switch to **high** for really complex architecture decisions.

If you combine high reasoning effort with the UltraThink trigger from King Mode, the model will think very deeply—but it will also be slower. For most coding tasks, **medium effort plus UltraThink is the sweet spot**.

### For Simple Questions

Remember what I said about GLM-5 not being great with simple chat. If you're using Verdant just to ask a quick question, don't use the UltraThink prefix. Just ask normally. King Mode's zero fluff rules will still apply, but you won't trigger the full architectural reasoning for a one-liner.

### Cost Considerations

GLM-5 is going to be a bit more expensive than GLM-4.7 because it's almost double the parameters. But the coding plans from ZAI should still be at a similar price point. Even if the API cost goes up a bit, you're getting Opus-level or better output for a fraction of what Anthropic charges—and the model will be open weights, which is awesome.

## The Bottom Line

This combination effectively turns a cheap open model into a full development team. The setup takes 10 seconds, but the difference in output quality is night and day.

**GLM-5 for intelligence, King Mode for discipline, Verdant for orchestration.**

You set up the King Mode prompt once in your project rules, prefix your complex prompts with `ultrathink`, and let Verdant's parallel agents handle the multitasking.

---

**Full Transcript**: [transcript file in resources]
**Short Summary**: [summary file in resources]

*Source: https://youtu.be/JRuwxLNXfcY*
*Channel: AICodeKing*
*Video Duration: 14m 47s*