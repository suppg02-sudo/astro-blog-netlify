---
pubDatetime: 2026-04-18T19:00:00Z
title: "From Riding Microsoft to Owning Your Stack: The MSP's Open-Source Migration Play"
postSlug: "from-riding-microsoft-to-ownin"
description: "From Riding Microsoft to Owning Your Stack: The MSP's Open-Source Migration Play"
tags:
  - msp
---

The previous post in this series argued for a hybrid: build the Karpathy Loop in open source, run it on Microsoft surfaces, use Copilot as the agent brain. Ride the stack your clients pay for while owning the improvement engine underneath.

But here is what happens next. The MSP builds its first loop — ticket triage in Python, running overnight, proposing changes to classification rules in a git repo. It works. Misroutes drop from 40% to 15%. Technicians get time back.

Then someone asks: "Where do the experiment logs live?" A SQLite database. "Can we see them in a dashboard?" So you stand up Grafana. "Can we share the dashboard with clients?" So you add authentication. "Can we automate the reporting?" So you build a pipeline.

Six months later, you have a small open-source stack running alongside Microsoft. And you realise something: these tools are not just internal infrastructure. They are productisable services.

## The Natural Accumulation

This is not a planned migration. It is what happens when you solve real problems with open-source tools:

| Problem | Tool You Reach For | What It Becomes |
|---------|-------------------|-----------------|
| "Where do experiment logs go?" | PostgreSQL | Client reporting database, analytics backend |
| "We need dashboards" | Grafana | Client-visible NOC dashboards (replace expensive SolarWinds reports) |
| "Our SOPs need a proper home" | Directus (headless CMS) | Knowledge base for clients, SOP portal for technicians |
| "We should publish client-facing docs" | Astro | Client documentation sites, status pages |
| "The loop needs workflow orchestration" | n8n or Activepieces | Automation platform you can resell as managed service |
| "Our scripts need a registry" | Gitea or Forgejo | Private code registry — eventually offered to clients as managed git |
| "We need monitoring that is not Azure Monitor" | Prometheus + Uptime Kuma | Infrastructure monitoring you can white-label for clients |
| "Passwords are a mess" | Vaultwarden | Managed password service for clients |
| "File sharing for internal stuff" | Nextcloud | Secure file sync — alternative to SharePoint for non-M365 clients |
| "Internal tools are needed" | Appsmith or Tooljet | Low-code internal tools — eventually client self-service portals |
| "Zero-trust networking between sites" | Tailscale or WireGuard | Managed secure connectivity for clients with multiple sites |
| "Container hosting for the above" | Docker + Portainer | Managed container platform — the foundation everything else runs on |

None of these require the client to leave Microsoft. The MSP runs its own stack internally while still managing the client's Microsoft environment. But over time, some clients will ask: "Can you host our wiki too?" "Can we get that dashboard you showed us?" "Do you do password management?"

That is when the open-source stack stops being internal infrastructure and becomes a revenue stream.

## The Three Phases

### Phase 1: Internal Only (Months 1-6)

Build the loop infrastructure. Stand up the minimum tools needed to make it work. Nothing is client-facing. Everything runs on a single server or small VM cluster.

| Component | Tool | Purpose |
|-----------|------|---------|
| Loop engine | Python + git | The Karpathy Loop itself |
| Database | PostgreSQL | Experiment logs, ticket history, eval results |
| Dashboards | Grafana | Internal visibility into loop performance |
| SOP storage | Directus | Structured SOP management with versioning |
| Workflow | n8n | Connect PSA/RMM APIs to loop engine |
| Container hosting | Docker + Portainer | Everything above runs in containers |

**Cost**: One server, $50-100/month. Same as a rounding error in any MSP's Azure bill.

**Client impact**: Zero. They see nothing. The MSP just gets better at its job.

### Phase 2: Dogfooding (Months 6-12)

Start using the open-source tools for MSP internal operations that were previously on Microsoft. Not replacing Microsoft — augmenting it where Microsoft is expensive, slow, or missing features.

| What Moves | From Microsoft | To Open Source | Why |
|-----------|---------------|---------------|-----|
| Internal knowledge base | SharePoint | Directus + Astro wiki | Better search, structured data, version control |
| Internal dashboards | Excel + Teams screenshots | Grafana | Real-time, automated, no manual copy-paste |
| Automation workflows | Power Automate | n8n | Cheaper, more flexible, self-hosted, no per-flow limits |
| Internal documentation sites | Confluence or nothing | Astro | Faster, developer-friendly, actually maintained |
| Script registry | Shared folder | Gitea | Version control, code review, CI/CD for scripts |
| Password management | Whatever the client uses | Vaultwarden | Standardised across the team, self-hosted |

**Cost**: Same server, maybe $20/month more in storage. 

**Client impact**: Still zero externally. But the MSP team experiences better tools internally, which builds the expertise to offer them later.

### Phase 3: Productisation (Months 12-24)

The MSP now has a working open-source stack that its own team uses daily. It is battle-tested. The team knows the failure modes, the maintenance burden, and the client communication patterns. Now you offer it as a service.

| Internal Tool | Becomes | Client Pitch |
|--------------|---------|-------------|
| Grafana dashboards | Managed monitoring dashboards | "Real-time visibility into your IT health, not monthly PDF reports" |
| Directus + Astro | Managed knowledge base | "Your company wiki, always up to date, accessible anywhere" |
| n8n workflows | Managed automation service | "We automate your business processes, not just your IT" |
| PostgreSQL + analytics | Managed data insights | "We make your IT data tell you something" |
| Vaultwarden | Managed password service | "Enterprise password security without enterprise pricing" |
| Nextcloud | Managed file sync | "Secure file sharing for teams that are not on M365" |
| Uptime Kuma + status pages | Managed status pages | "Client-facing status pages for your services" |
| Tailscale | Managed secure connectivity | "Zero-trust networking between your sites" |
| The Karpathy Loop itself | Auto-improvement as a service | "Your IT gets better every night, automatically" |

**The pricing model**: These are add-on services, not Microsoft replacements. A client stays on M365 for email and Office. The MSP adds Grafana dashboards for $200/month, a knowledge base for $150/month, automation workflows for $300/month. The client gets better service. The MSP gets recurring revenue on infrastructure it already runs.

## Why This Works for Microsoft-Heavy MSPs Specifically

The Microsoft-only MSP has a problem that the open-source MSP does not: margin compression. Microsoft licencing costs rise every year. The MSP passes those costs to clients. Clients push back. The MSP absorbs some of the increase. Margin shrinks.

Open-source add-on services solve this because:

| Factor | Microsoft Service | Open-Source Service |
|--------|------------------|-------------------|
| Licence cost to MSP | $6-22/user/month | $0 (self-hosted) |
| What client pays | Pass-through + small margin | Pure margin |
| MSP margin on the service | 10-20% | 70-90% |
| Differentiation from competitors | None (everyone sells M365) | Significant (nobody else offers this) |
| Lock-in | Microsoft controls pricing | MSP controls pricing |
| Value to client | Same M365 everyone gets | Unique service tailored to them |

A 50-client MSP adding 3 open-source services at $200-500/month each across 20 clients generates $144K-360K/year in high-margin recurring revenue. On infrastructure that costs $100-300/month to run.

## What the Stack Looks Like at Maturity

A fully mature MSP open-source stack running alongside Microsoft:

```
┌─────────────────────────────────────────────────────────┐
│                    Client-Facing Layer                    │
│  Astro docs │ Grafana dashboards │ Status pages │ Portal │
├─────────────────────────────────────────────────────────┤
│                    Service Layer                          │
│  Directus CMS │ n8n workflows │ Auth │ API gateway       │
├─────────────────────────────────────────────────────────┤
│                    Data Layer                             │
│  PostgreSQL │ pgvector │ Redis │ Object storage          │
├─────────────────────────────────────────────────────────┤
│                    Infrastructure                         │
│  Docker │ Portainer │ Tailscale │ Prometheus │ Backups   │
├─────────────────────────────────────────────────────────┤
│                    Karpathy Loop Engine                    │
│  Python scripts │ Git │ Eval harness │ Experiment logs   │
├─────────────────────────────────────────────────────────┤
│                    Microsoft Integration                  │
│  Graph API │ Azure Monitor │ Intune │ Defender │ M365   │
└─────────────────────────────────────────────────────────┘
```

The Microsoft layer is still there. The MSP still manages it for clients. But the MSP owns the layers above it — the intelligence, the data, the services, and the client experience.

## The Risks and How to Mitigate Them

| Risk | Reality | Mitigation |
|------|---------|-----------|
| "Clients will not want non-Microsoft tools" | Clients want outcomes, not brands. They do not care if the dashboard is Grafana or Power BI as long as it shows their SLA status. | Never lead with the tool. Lead with the outcome. "Real-time SLA dashboard" sells. "We installed Grafana" does not. |
| "Our team does not know open source" | They know more than they think. PowerShell is scripting. Python is scripting. Docker is packaging. The jump is smaller than it appears. | Start with one tool. One team member. One problem. Do not boil the ocean. |
| "Maintenance burden" | Self-hosted tools require maintenance. This is real. | Run everything in Docker with automated updates. Budget 4 hours/month for maintenance across the entire stack. Most months it takes 1 hour. |
| "Security concerns" | Self-hosted means you are responsible for patching. | Same tools the MSP already uses for client patching apply here. Container images update in minutes. |
| "What if open-source projects die?" | Some will. Pick tools with active communities (1000+ GitHub stars, recent commits). | Always have an export strategy. PostgreSQL data can go anywhere. Grafana dashboards are JSON. Directus content is in the database. No lock-in. |
| "Microsoft account team pushes back" | They will suggest Azure equivalents for everything. | Point out that your open-source stack costs $100/month while the Azure equivalent costs $2,000/month. The business case speaks for itself. |

## The Sequence That Minimises Risk

| Month | Add This | Why This Order |
|-------|---------|---------------|
| 1 | Docker + Portainer | Foundation. Everything else runs in containers. |
| 1 | PostgreSQL | Database for loop logs. Everything else reads from it. |
| 2 | Grafana | Visualise what the loop is doing. Internal only. |
| 3 | Gitea | Version control for scripts and configs. |
| 4 | n8n | Connect the PSA and RMM APIs to the loop. |
| 5 | Directus | Structured SOP management. |
| 6 | Astro | Publish internal documentation. |
| 6-12 | Dogfood everything. Break things internally. Learn. |
| 12+ | Start offering Grafana dashboards as a service. |
| 15+ | Offer Directus/Astro knowledge bases as a service. |
| 18+ | Offer n8n workflow automation as a service. |
| 24+ | Offer the full managed open-source stack as a service tier. |

Each addition solves an immediate internal problem first. No tool is offered to clients until the MSP team has used it daily for 6+ months and can support it confidently.

## The Deeper Play: Stack as Moat

Every MSP manages Microsoft. Every MSP can sell M365. Every MSP can deploy Intune. There is no differentiation in being a Microsoft MSP — it is table stakes.

The MSP that builds its own open-source service layer on top of the Microsoft foundation creates something competitors cannot copy quickly:

| Competitive Dimension | Microsoft-Only MSP | MSP with Open-Source Service Layer |
|----------------------|-------------------|-----------------------------------|
| Client dashboards | Monthly PDF reports exported from PSA | Real-time Grafana dashboards, custom per client |
| Knowledge management | SharePoint folder nobody updates | Structured wiki that auto-updates from tickets |
| Automation | Power Automate flows with per-user licencing | n8n workflows, unlimited, self-hosted |
| IT improvement | Quarterly reviews, manual recommendations | Auto-improvement loops running nightly |
| Data insights | "Here is your ticket count" | "Here is what your IT data tells us about your business" |
| Pricing power | Margins compressed by Microsoft licencing | 70-90% margin on self-hosted services |
| Switching cost for client | Low (any MSP can manage M365) | High (custom dashboards, automations, knowledge bases that do not transfer) |

The open-source stack is not just infrastructure. It is a moat. The MSP that builds it first in its market has a 12-18 month head start before competitors catch up. And by the time they do, the first-mover has already accumulated client-specific data, custom workflows, and trust that are expensive to replicate.

## The Honest Summary

Should the MSP introduce its own open-source stack? Yes — but not as a replacement for Microsoft. As an augmentation that becomes a product.

Start with the loop. Add tools as problems demand them. Dogfood everything for six months. Then offer the ones that work as managed services.

The Microsoft stack pays the bills today. The open-source stack builds the moat for tomorrow. And the Karpathy Loop — the overnight optimisation engine that started all of this — is the thin end of the wedge that makes the whole migration feel natural rather than revolutionary.

Nobody at the MSP wakes up one morning and says "let's rebuild our entire infrastructure in open source." They wake up and say "the loop needs a database." Then "the database needs a dashboard." Then "the dashboard should be visible to clients." Then "clients want dashboards too." And suddenly you have a product.

That is how you eat an elephant. Not in one bite. In a thousand tiny bites, each one solving a real problem, each one justified on its own merits, each one moving you two percent closer to owning your own stack.

## Get Your Own House in Order First

Every MSP says "we use AI." Almost none can show you their own experiment logs, their own metric trajectories, their own before/after dashboards. The MSP that can has a fundamentally different sales conversation.

The sequence is not optional:

1. **Get your own signals right.** What are you measuring? Is it the right metric? Do you trust the data? If your ticket categorisation is messy, if your alert tagging is inconsistent, if your SOPs have never been measured against actual outcomes — you do not have signals. You have noise. Fix your own data first.

2. **Get your own observability right.** Can you see what is happening in your own operations in real-time? Not a monthly PDF exported from the PSA. Live dashboards. Experiment logs. Baseline measurements. Metric trajectories over time. If you cannot observe your own improvement, you cannot prove it happened.

3. **Run the loops on yourself.** Ticket triage. Alert tuning. Script library. Run the Karpathy Loop on your own MSP operations for six months minimum. Accumulate the data. The metric trajectories. The experiment logs. The before and after.

4. **Accumulate the evidence.** "We reduced our own ticket misroutes by 60%. We cut alert noise by 50%. Our script failure rate dropped from 8% to 1%. Our NOC team reclaimed 1,500 hours per year. Here is the data, here are the experiment logs, here is the dashboard showing the improvement curve." This is not a pitch deck. This is proof.

5. **Then offer it to clients.** Not as a slide in a quarterly review. As a demo. "This is what we did to ourselves. This is what it looks like. We can do it for you." The sales conversation changes from "trust us, AI works" to "look at what we measured, here is the evidence, here is how it compounds."

The principle is eat your own dog food — but with instrumentation. It is not enough to use your own tools. You must measure yourself using them, prove they work with data, and then show clients the proof.

This is the thread that connects everything in this series. The SOPs must be machine-readable before the loop can run on them. The stack must serve the loop, not the other way around. The SOC sister company's ML expertise helps with eval discipline but does not build the loops. And the open-source tools accumulate naturally if you solve problems sequentially rather than planning a grand migration.

But underneath all of it: prove it on yourself first. The MSP that can show a client its own Grafana dashboard with its own improvement trajectory, its own experiment logs with its own hit rates, and its own before/after metrics from its own operations — that MSP does not need to say "we use AI." The evidence speaks.

---

*Final part of the Karpathy Loop for MSPs series: [Part 1: Where Auto-Improvement Lands](http://ubuntu4:3002/posts/the-karpathy-loop-for-msps-whe/) | [Part 2: SOC ML Overlap and Gaps](http://ubuntu4:3002/posts/when-your-sister-company-alrea/) | [Part 3: SOPs as Program.md](http://ubuntu4:3002/posts/sops-are-the-program-md-why-st/) | [Part 4: Microsoft/Open-Source Stack Decision](http://ubuntu4:3002/posts/the-microsoft-msp-dilemma-buil/) | [Reference Guide](http://ubuntu4:3002/posts/the-karpathy-loop-reference-guide/)*
- [Beyond IT: Extending the Loop to Every Business Function](http://ubuntu4:3002/posts/beyond-it-extending-the-karpat/)
- [Taking the Loop to Client Environments](http://ubuntu4:3002/posts/taking-the-karpathy-loop-to-cl/)
- [The LLM-Wiki Pattern for MSP Knowledge Management](http://ubuntu4:3002/posts/the-llm-wiki-pattern-write-tim/)

**Tags**: msp, open-source, stack-migration, karpathy-loop, postgresql, directus, grafana, managed-services, self-hosted, business-strategy
**Categories**: AI Automation, Business Strategy