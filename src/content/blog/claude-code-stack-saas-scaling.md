---
pubDatetime: 2026-02-24T15:07:38Z
title: "Claude Code Stack: Build SaaS That Scales to Millions"
postSlug: "claude-code-stack-saas-scaling"
description: "Claude Code Stack: Build SaaS That Scales to Millions"
tags:
  - startup
  - youtube
  - scalability
  - convex
  - posthog
  - clerk
  - saas
---

Building a SaaS product that can scale from thousands to millions of users is a dream for many developers. But traditional scaling challenges—database management, server configuration, DevOps overhead—can make this dream feel out of reach. What if there was a complete technology stack that handled all of this for you?

## The "God Stack" Concept

Until recently, I wouldn't have felt comfortable claiming I could scale to 10,000 users, let alone 100,000. But with the stack I'm about to show you, I'm confident I could scale all the way up to a million users.

This isn't just theoretical. My current project, Harbor SEO.ai, has **2,370 active users** and runs efficiently on this stack. Let me break down exactly what makes it work and why you might want to use it too.

## Convex: The Backend Foundation

Convex is an absolute godsend for backend development. It handles your database, API, and real-time updates—all in one hosted service.

### What Makes Convex Different

Works seamlessly with modern frontend frameworks including Next.js, Tanstack, React, Remix, Vue, and Svelte. The standout feature? **Automated data refresh**—your app updates in real-time without complex websocket code.

### Development vs. Production

One of Convex's killer features is seamless environment separation:

- **Development instance**: Runs locally when you execute `npx convex dev`
- **Production instance**: Separate Convex project for your live app
- **Same login, different projects**: Both instances live under your same account but remain completely isolated

This separation makes local development trivial. No more struggling with JWT tokens or environment configuration just to test changes locally.

### Real-World Usage: 2,370 Users for Less Than $20

Harbor's current usage on Convex demonstrates why this approach is scalable:

- **250 GB hours allowed**: Using less than 1/5
- **25 million function calls**: Plenty of headroom
- **50 GB database storage**: With 50 GB bandwidth
- **Cost**: Around $20/month (possibly free tier)

That's for 2,370 active users. Doing the math, you can scale a SaaS to **1,000+ users for free** with Convex.

### The Traditional Alternative

Compare this to Digital Ocean or similar VPS providers. At similar scale, you'd pay **$3,000+ just for bandwidth**—not including servers, databases, or DevOps time.

### The Trade-off

Using Convex means putting faith in a third party for your backend. This is a decision you need to make consciously. But for many developers, the trade-off—automatic scaling vs. owning infrastructure—is worth it.

## User Base Value: Why 2,370 Users Matters

Before diving into the rest of the stack, let me explain why Harbor's user base is significant.

### Companies Buy Users, Not Revenue

Harbor generates minimal revenue right now. But its 2,370 users make it worth **$1 million or more**. Why?

Because established SaaS companies acquire products primarily to increase their user count. If a company has 10,000 users and buys an app with 2,500 users, they've just increased their user base by 25%.

This isn't theoretical—OpenClaw sold to OpenAI for **$1+ billion** despite having zero revenue. OpenAI bought users, not profit.

## Clerk: Authentication That Scales

Clerk handles user authentication and provides something you can't easily build yourself: **GDPR compliance**.

### Why GDPR Compliance Matters

Clerk is fully GDPR compliant with:
- EU-based data hosting
- Data privacy framework for US transfers
- User data deletion tools
- Data residency controls
- Privacy policy and data handling infrastructure

If you're doing user authentication yourself, you won't get these guarantees. This matters for enterprise customers and European markets.

### The Most Important Metric: Retained Users

Clerk's dashboard shows two key numbers:
- **New users**: People who signed up
- **Retained users**: People who came back

Retained users are more important than new users. Why? Because retained users are the ones who convert to paid plans.

Harbor's January metrics:
- 1,447 active users
- 241 retained users
- **38% retention rate** (not great, but it's the baseline)

February shows improvement:
- 230 retained users
- 30 reactivated users
- **Retention trending upward** despite fewer new sign-ups

This improvement comes directly from product changes and user experience improvements.

## PostHog: Analytics That Actually Helps

PostHog is the tool I use more than any other. It's basically a Google Analytics alternative—and I can't stand Google Analytics.

PostHog is **one of the best tools I've ever used**. Here's why it's indispensable.

### Track Feature Usage Immediately

Every time I add a new feature, the first thing I do is add tracking in PostHog via Claude Code:

```
"Please add an insight about site health feature on Harbor Ultimate dashboard"
```

That's it. PostHog tracks usage automatically. I don't have to touch the app code.

### Why This Matters

If you're adding features without tracking whether people use them, you're wasting your time. I spent 10-20 hours building Harbor's site health feature—but I only know it's valuable because PostHog shows people are actually using it.

### The Metric I'm Obsessing Over: Returning Users

This is the single most important number:

- Weekly returning users: 60 → 53 → 59 → 56 → **77** (upward trend)
- Goal: 100 returning users per week
- **Projected monthly**: ~11,600 active users

Why does this matter? Because users who return to your tool repeatedly are much more likely to become paying customers. Users who press "generate" once and never come back? They won't pay.

### Conversion Optimization

PostHog revealed a critical insight: time to first generate.

Previously: **5 hours** from signup to first generate
Now: Much faster due to improved onboarding flow

This makes sense—users create an account, come back 2-3 days later, write an article, then they're much more likely to actually use the generate feature.

### Session Replay: Seeing How Users Actually Use Your Product

PostHog's session replay lets you watch exactly how people interact with your tool. This reveals truths about user behavior you'd never guess.

I literally live on this page. It's essential for understanding:
- Which features are being used
- Where users get stuck
- What UI patterns cause confusion
- Where to place new features

### Error Tracking: Zero Visibility Without It

You have absolutely zero visibility on your app's errors unless you use error tracking.

PostHog shows me:
- When errors occur (e.g., "2 hours ago")
- How often they repeat
- Whether they're new or recurring

This enables rapid response. When I see an error appeared 4 hours ago for the first time, I know it's a new problem that needs immediate attention.

### Feature Placement Over Feature Count

Here's a product management truth I learned the hard way: stop thinking "more features = better product."

I considered adding site health to the sidebar. But Harbor's dashboard is intentionally slim—only six main items. Adding another sidebar option would clutter the UI.

Instead, the site health feature appears in exactly two strategic places:
- As a small "scan my site" button on the dashboard
- In the "Advanced Tools" section as an extended option

The result? Users actually use it because they can find it. 20 hours of development isn't wasted because the feature is discoverable.

## Resend: Email That Drives Retention

Resend handles automated email campaigns for user nurturing.

### The "We Miss You" Campaign

When users haven't returned in about a week, they receive a personalized email:

*"We miss you, Hamish. It's been a while. We noticed you haven't been back in a week. Your content opportunities are still waiting and your free tokens are ticking. Even one article can make a difference. Pick up where you left off and get back to writing."*

This works. It converts dormant users back to active users. And active users become paying users.

### Why Resend Is Essential

Email nurturing is essential for improving retention. Clerk shows the retained users metric. Resend provides the mechanism to improve that metric.

## Linear: Structured Product Management

Linear handles project management, bug tracking, and feature requests.

### The Workflow

1. Product manager creates jobs in Linear
2. I review jobs and discuss them with Claude Code
3. Implementation follows the discussion

This is a structured approach to development prioritization. You don't just build random features—you build what's planned, tracked, and discussed.

### Claude Code Integration

When I include code in Claude Code and execute `/mcp`, I can fetch all jobs from Linear directly:

```
"Get all jobs from Linear"
```

This keeps development organized and ensures nothing falls through the cracks.

## The Complete Stack: What Makes It Work Together

Here's why this combination creates a scalable, production-ready SaaS:

| Component | Role | Why It Matters |
|------------|--------|----------------|
| **Convex** | Backend + Database | Automatic scaling, dev/prod separation, predictable costs |
| **Clerk** | Authentication | GDPR compliance, retention analytics, user management |
| **PostHog** | Analytics | Feature tracking, error visibility, conversion optimization |
| **Resend** | Email Nurturing | Improves retention, reactivates dormant users |
| **Linear** | Project Management | Structured development, Claude Code integration |

This stack eliminates scaling anxiety. You don't need DevOps expertise. You don't need to worry about database sharding, load balancing, or server configuration.

Each service handles its domain. You focus on building features, while the infrastructure scales automatically.

## Key Takeaways

### For Solo Developers

- You don't need a DevOps team to scale to thousands of users
- Hosted services (Convex, Clerk, PostHog) handle the complexity
- Free tiers support 1,000+ users—test before paying

### For Product Managers

- **Track everything**: Features without tracking are wasted development time
- **Retention > acquisition**: Returning users drive revenue, not sign-ups
- **Feature placement matters**: 10 hours on a well-placed feature > 50 hours on an unused one

### For SaaS Founders

- **User base has value**: 2,500 users can be worth $1M+ even with minimal revenue
- **GDPR compliance matters**: Clerk provides guarantees you can't build yourself
- **Error visibility is critical**: PostHog shows errors in real-time for rapid response

## Final Thoughts

This stack isn't about using specific technologies for their own sake. It's about using tools that work together to solve the real problems of scaling a SaaS product.

- Convex handles infrastructure so you don't have to
- Clerk ensures compliance so you can sell globally
- PostHog provides visibility so you know what to build
- Resend drives retention so users become customers
- Linear keeps development organized so you ship consistently

With this stack, I'm confident building for millions of users. You can be too.

---

**Want to try Harbor?** It's free for about another week at harborseo.ai. Try out the SEO tools, connect your Search Console, and see what this stack enables in practice.