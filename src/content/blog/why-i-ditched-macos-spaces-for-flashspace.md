---
pubDatetime: 2026-04-10T12:00:00Z
title: "Why I Ditched macOS Spaces for FlashSpace"
postSlug: "why-i-ditched-macos-spaces-for-flashspace"
description: "I fought macOS Spaces for years. Then I found FlashSpace, and it rewired how I think about workspace management on macOS."
tags:
  - productivity
  - workspace-manager
  - macos
  - open-source
  - swift
---

I fought macOS Spaces for years. You know the drill: three-finger swipe, wait for the animation, land on the wrong desktop, swipe back, wait again. Multiply that by a hundred switches per day and you've burned minutes on nothing. Then I found FlashSpace, and it rewired how I think about workspace management on macOS.

## The Problem With Native Spaces

macOS Spaces sounds great in theory. Virtual desktops, separate spaces per display, Mission Control for the bird's-eye view. In practice, it's sluggish and opinionated in all the wrong ways.

The animation delay alone kills flow state. Every switch costs you ~300ms of visual transition plus the cognitive reset. And the configuration is fragile. Plug in an external monitor and your carefully arranged spaces shuffle themselves like a deck of cards. Unplug? Shuffled again. I've watched my "work" space end up on Desktop 5 more times than I care to admit.

Worse, Spaces treats every app window as a first-class citizen. You can't say "these five apps belong together, hide everything else." You can move windows between spaces, but you can't define a workspace as a cohesive unit. It's manual window herding, every single time.

## Enter FlashSpace

[FlashSpace](https://github.com/wojciech-kulik/FlashSpace) takes a radically different approach. Instead of managing desktops, it manages **apps**. You define a workspace as a named collection of applications assigned to a specific display. When you activate that workspace, FlashSpace shows those apps and hides everything else on that display. Instantly. No animations. No transitions.

```bash
# Install via Homebrew — that's it
brew install flashspace
```

The setup is refreshingly simple. You move all your apps to a single macOS space per display (yes, just one native space), then let FlashSpace handle the virtual layering on top. You create workspaces, assign apps, set hotkeys, and you're done.

## Why This Works Better

The insight FlashSpace exploits is that macOS already has a perfectly good `show`/`hide` API for applications. It's native, it's fast, and it doesn't break things like Mission Control. FlashSpace doesn't fight the operating system — it orchestrates it.

This design decision cascades into several concrete benefits:

**Speed.** Workspace switching is essentially instantaneous because it's just toggling app visibility. No desktop animation, no window server round-trips. Press `Cmd+1` and your coding workspace appears. Press `Cmd+2` and your communication workspace takes over. The README calls it "blazingly fast" and it's not marketing spin — it genuinely feels instant.

**Stability.** Because FlashSpace uses the standard `hide`/`unhide` mechanism, nothing breaks. Tiling window managers that move windows around constantly fight with popup dialogs, floating tool windows, and apps that resize themselves. FlashSpace sidesteps all of that by simply not managing windows it doesn't own.

**Battery friendliness.** No continuous window event polling, no repositioning loops. Show and hide. Done. Your MacBook doesn't need to work harder because you want cleaner workspace management.

## The Conscious Trade-offs

What FlashSpace deliberately does **not** do is as important as what it does:

**No per-window workspaces.** You can't put individual windows of the same app in different workspaces. An app is either in a workspace or it isn't. This sounds limiting until you realise it's what makes the whole system reliable. Per-window management would require hacky workarounds (moving windows to screen corners, minimising) that break constantly.

**No layouts.** FlashSpace doesn't resize, tile, or position windows. It's not a tiling window manager. The author explicitly calls this out: the app follows the UNIX philosophy of doing one thing well. Pair it with Rectangle, Magnet, or even macOS 15's built-in window snapping for layout management.

**No disruption.** If you activate a workspace and then open an unassigned app, it simply appears on top. No glitches, no forced reordering. You can interact with it, close it, and you're back to your workspace. This non-disruptive behaviour is a feature, not a bug.

## Dynamic Mode: The Multi-Monitor Game Changer

For multi-display setups, FlashSpace offers a **dynamic display assignment** mode where each workspace automatically maps to whichever displays its apps are currently on. This means you can physically drag a window to another monitor and the workspace follows. No manual reconfiguration.

In static mode (the default), each workspace is pinned to a specific display — ideal for fixed desk setups. Dynamic mode shines when you're hot-desking or frequently changing your monitor arrangement.

## Integration With Your Existing Tools

FlashSpace plays well with the broader macOS ecosystem:

- **SketchyBar integration** — run custom scripts on workspace changes to update your menu bar
- **CLI for automation** — `flashspace list-workspaces`, switch workspaces, manage profiles from the terminal
- **SKHD compatibility** — define complex hotkey combos via the SKHD daemon
- **Space Control** — a visual grid overlay (think Mission Control but actually useful) with keyboard navigation
- **Workspace Switcher** — `Option+Tab` between workspaces like the macOS app switcher

The CLI is particularly powerful for scripting. You can build automation that switches workspaces based on context — morning standup activates your meetings workspace, opening a terminal in a project directory activates the relevant dev workspace.

## What I Learned From Switching

Three principles emerged from using FlashSpace that apply beyond workspace management:

1. **Layer, don't replace.** FlashSpace doesn't try to replace macOS Spaces entirely. It runs on top of a single space per display and adds virtual workspace management. This layered approach is more resilient than wholesale replacement.

2. **Use the platform's primitives.** The `hide`/`show` API has been in macOS for over a decade. It's battle-tested, battery-efficient, and doesn't break with OS updates. Building on platform primitives beats fighting against them.

3. **Scope creates quality.** By refusing to handle window layouts, per-window assignment, or window movement, FlashSpace delivers a rock-solid core experience. Every feature it does have works reliably because the scope is bounded.

If you spend your day switching between contexts — code, communication, design, research — and you're tired of macOS Spaces' sluggish dance, FlashSpace is worth thirty minutes of your time. Install it, define three workspaces, set hotkeys, and feel the difference instant switching makes. You won't go back.