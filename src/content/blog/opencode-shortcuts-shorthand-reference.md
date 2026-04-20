---
pubDatetime: 2026-03-24T02:31:15Z
title: "OpenCode Shortcuts and Shorthand: A Complete Reference Guide"
postSlug: "opencode-shortcuts-shorthand-reference"
description: "OpenCode Shortcuts and Shorthand: A Complete Reference Guide"
tags:
  - productivity
  - opencode
  - shortcuts
  - cli
  - workflow
---

## Why Shortcuts Matter

When you spend hours in a CLI-based AI coding agent, every keystroke counts. OpenCode's trigger system turns single words and two-letter abbreviations into powerful commands — launching skills, managing containers, writing blog posts, and navigating complex workflows without typing full sentences.

This post documents the complete shorthand system, the naming conventions behind it, and the recent improvements that make it more consistent and discoverable.

## The Shortcut System

OpenCode uses a **trigger word** system. Type a word (or abbreviation) on its own, and the agent recognises it as a command rather than a conversation. Triggers are defined in `AGENTS.md` and optionally backed by dedicated trigger files with detailed routing logic.

There are three tiers of shortcuts:

| Tier | Length | Count | Purpose |
|------|--------|-------|---------|
| **Single character** | 1 char | 5 | Most frequent actions |
| **Two-letter** | 2 chars | 16 | Common skills and tools |
| **Full word** | 3+ chars | 20+ | Self-documenting commands |

### Single-Character Triggers

These are reserved for the actions you use most often:

| Trigger | Action |
|---------|--------|
| `?` | Show the shortcut reference card |
| `a` | Browser automation (with URL) |
| `r` | Deep research mode |
| `q` | Intelligent question loop |
| `u` | Update instructions after changes |
| `o` | Save most recent response to file |

Single-character triggers are intentionally scarce. Each one earns its place through frequency of use.

### Two-Letter Shortcuts

The bulk of the shorthand system. These follow a loose convention: **first letters of the full name**, or the most recognisable abbreviation.

#### Quick Actions

| Short | Full | What It Does |
|-------|------|-------------|
| `co` | carry on | Continue with current task |
| `ga` | agents.md | AGENTS.md review menu |
| `c7` | Context7 | Load Context7 MCP for documentation |
| `>t` | send to Telegram | Forward last response via Telegram |

#### System & Infrastructure

| Short | Full | What It Does |
|-------|------|-------------|
| `ct` | containers | Docker container management menu |
| `sp` | space | Disk space analysis and cleanup |
| `cp` | checkpoint | Interactive checkpoint management |

#### Communication

| Short | Full | What It Does |
|-------|------|-------------|
| `tg` | telegram | Telegram bot integration |

#### Research & Learning

| Short | Full | What It Does |
|-------|------|-------------|
| `bs` | brainstorm | Quick or structured brainstorming |

#### Content

| Short | Full | What It Does |
|-------|------|-------------|
| `bp` | blog post | Create Hugo blog post |

#### Memory

| Short | Full | What It Does |
|-------|------|-------------|
| `cr` | context-registry | Context tracking and disclosure |

#### Skills & Discovery

| Short | Full | What It Does |
|-------|------|-------------|
| `sd` | skill discovery | Central skill discovery menu |
| `sf` | skill-factory | Meta-skill for creating/updating skills |
| `mf` | menu-factory | Menu validation and learning |
| `ml` | menu-learning | Adaptive menu learning system |
| `ta` | tool audit | Tool usage analysis |
| `dr` | daily-research | Automated AI ecosystem research |

#### Services

| Short | Full | What It Does |
|-------|------|-------------|
| `lp` | lifeplan | Personal life planning and goals |

#### Workflow

| Short | Full | What It Does |
|-------|------|-------------|
| `ru` | roundup | Session review and system health check |

### Full-Word Triggers

Some commands are self-documenting and don't need abbreviation. These tend to be less frequent or more complex:

| Trigger | Action |
|---------|--------|
| `setup` | Guided server setup (7 phases) |
| `plan` | Activate Plan Agent |
| `flow` | Execution flow analysis |
| `menu` | Global menu configuration |
| `roadmap` | Server setup progress |
| `rules` | Rules review |
| `telos` | TELOS constitution menu |
| `markets` | Financial market analysis |
| `remind` | Schedule reminders |
| `orch` | Life orchestrator |
| `bible` | Biblical text comparison |
| `geo` | Geopolitics research |
| `rag` | OpenRAG document retrieval |
| `mem` | Memory system gateway |
| `smooth` | Fix and smooth recent task |
| `files` | Show folder structure |
| `notify` | Send Telegram notification |
| `reply` | Show Telegram ReplyKeyboard |

## The Help Card

Type `?` or `help` to get a compact reference card showing every shortcut at a glance:

```
╔══════════════════════════════════════════════════════╗
║              OPENCODE SHORTCUTS                      ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  ⚡ QUICK ACTIONS                                    ║
║  ?/help  This card        o   Save response          ║
║  co      Carry on         >t  Send via Telegram      ║
║  c7      Context7         api Show API info           ║
║  ga      AGENTS.md menu   gsd GSD agents             ║
║                                                      ║
║  🏗️ SYSTEM                                           ║
║  a [url] Browser auto     ct  Containers             ║
║  sp      Disk space       cp  Checkpoint             ║
║  setup   Server setup     url Generate URLs          ║
║                                                      ║
║  📡 COMMS                                            ║
║  tg      Telegram         >t  Send last via TG       ║
║  notify  TG notification  reply  ReplyKeyboard       ║
║                                                      ║
║  🗒️ RESEARCH                                         ║
║  r       Deep research    bs  Brainstorm             ║
║  q       Question loop    geo Geopolitics            ║
║  bible   Biblical texts                              ║
║                                                      ║
║  📝 CONTENT                                          ║
║  bp      Blog post        u   Update instructions    ║
║  files   Show structure   smooth  Fix recent task    ║
║                                                      ║
║  🧠 MEMORY                                           ║
║  mem     Memory gateway   mem-quick  Quick stats     ║
║  cr      Context registry mem-check  Full check      ║
║                                                      ║
║  🛠️ SERVICES                                         ║
║  rag     OpenRAG          lp  Lifeplan               ║
║  orch    Orchestrator     telos  Constitution        ║
║  markets Finance          remind  Reminders          ║
║                                                      ║
║  📚 SKILLS                                           ║
║  sd      Skill discovery  sf  Skill factory          ║
║  mf      Menu factory     ml  Menu learning          ║
║  ta      Tool audit       dr  Daily research         ║
║                                                      ║
║  🔄 WORKFLOW                                         ║
║  plan    Plan agent       flow  Flow analysis        ║
║  menu    Global menu      ru  Roundup/review         ║
║  roadmap Progress         rules  Rules review        ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
```

This card is always one keystroke away. No scrolling through documentation, no searching through config files.

## Naming Conventions

The shorthand system follows these patterns (loosely, not rigidly):

1. **Initials** — Take the first letter of each word: `bp` (blog post), `sf` (skill factory), `mf` (menu factory)
2. **First two letters** — When the name is a single word: `bs` (brainstorm), `ct` (containers), `sp` (space), `cp` (checkpoint), `tg` (telegram), `ru` (roundup)
3. **Established abbreviations** — Use what people already know: `mem` (memory), `rag` (retrieval-augmented generation), `geo` (geopolitics)
4. **Symbolic** — Special characters for special purposes: `?` (help), `>t` (pipe to Telegram)

## Recent Improvements

The shortcut system was recently audited and improved:

- **6 new shortcuts added**: `bs`, `ct`, `tg`, `ru`, `sp`, `cp` — filling gaps where common commands had no shorthand
- **Help trigger created**: `?` and `help` now display the compact reference card
- **Brainstorm Quick mode**: `bs` now goes directly to fast brainstorming without the superpowers approval gate
- **Consistent naming**: All new shortcuts follow the two-letter convention

## Design Philosophy

The trigger system reflects a few principles:

**Frequency determines length.** The most-used commands get the shortest triggers. You shouldn't have to type `brainstorm` when `bs` will do.

**Discoverability matters.** The `?` trigger exists because no one memorises 40+ shortcuts. Having a reference card one keystroke away removes the memorisation burden.

**Convention over configuration.** Two-letter abbreviations are predictable. If you know the skill name, you can usually guess the shortcut.

**Escape hatches exist.** Every trigger also works as its full name. `containers` and `ct` do the same thing. The long form is always there for clarity.

## What's Next

The shortcut system continues to evolve:

- **Auto-routing**: Typing `bs redis vs postgres` should skip the mode menu and go straight to Quick Think analysis
- **Telegram menu sync**: Ensuring all shortcuts are available as Telegram bot buttons
- **Collision detection**: Automated checking that new shortcuts don't conflict with existing ones

The goal is simple: reduce the friction between thinking and doing. Every shortcut saved is cognitive load freed for the actual work.