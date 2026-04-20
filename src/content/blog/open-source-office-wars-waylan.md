---
pubDatetime: 2026-04-04T09:32:05Z
title: "Open Source Office Wars, Wayland Milestones, and Linux Gaming Breaks 5%"
postSlug: "open-source-office-wars-waylan"
description: "Open Source Office Wars, Wayland Milestones, and Linux Gaming Breaks 5%"
tags:
  - others
---

A packed week in the Linux and open-source world: office suite drama erupts on multiple fronts as OnlyOffice battles its European fork, Collabora clashes with The Document Foundation, and GitHub Copilot sneaks ads into pull requests. Meanwhile, Wayland notches two major protocol wins, Linux gaming hits a historic milestone on Steam, and Nvidia pushes forward with HDR and color management support.

## Quick Summary

- **OnlyOffice vs EuroOffice**: Licensing dispute over AGPL fork with Nextcloud partnership suspended
- **Collabora ejected from Document Foundation**: Major LibreOffice contributor removed, plans separate desktop office
- **Wayland session restore**: Protocol officially merged after 6 years — desktops can now restore window positions on login
- **Wayland fractional scaling v2**: Fixes visual gaps and inconsistencies in scaled displays
- **GitHub Copilot ad scandal**: 1.5M pull requests injected with product ads, quickly reversed after backlash
- **Ubuntu MATE seeks new maintainer**: 12-year lead steps down, LTS qualification skipped
- **GNOME drops Google Drive**: Unmaintained library forces removal after years of broken integration
- **Linux hits 5% on Steam**: Historic market share milestone driven by SteamOS and Windows 11 frustration
- **Nvidia HDR preview**: Color management API support with AI-generated driver code
- **Wine explores Zink**: OpenGL over Vulkan for better performance and future-proofing

## The Open Source Office Suite Wars

This week saw open-source office suites descend into outright conflict on two separate fronts, threatening to fracture already fragile competition against Microsoft Office.

### OnlyOffice vs EuroOffice: The AGPL Licensing Dispute

EuroOffice, a new EU-backed office suite backed by Nextcloud, Proton, and others, forked OnlyOffice's codebase citing opaque development processes, unreliable build instructions, and concerns about the Russian company's potential government ties. OnlyOffice retaliated, accusing EuroOffice of violating additional licensing terms layered on top of the AGPL v3 — specifically around branding and attribution requirements.

The situation escalated when OnlyOffice suspended its partnership with Nextcloud for participating in the fork "without permission." EuroOffice counters that AGPL v3 explicitly forbids adding extra conditions on redistribution — a familiar tension in open-source licensing, reminiscent of the Red Hat Enterprise Linux source redistribution controversy.

No legal action has been filed yet, but the damage is done: two office suites that should be collaborating are now in open conflict, and the real loser is the open-source ecosystem's credibility as a Microsoft Office alternative.

### Collabora vs The Document Foundation

Simultaneously, the Document Foundation ejected all Collabora staff from membership — including their top 10 contributors to LibreOffice. Collabora, a major open-source contributor and maker of Collabora Online, had been in heated dispute with TDF over the relaunch of LibreOffice Online (a competitor built on what Collabora calls an unmaintained, outdated codebase).

Collabora accuses TDF of being stacked with non-technical staff, overturning board decisions, threatening contributors over LibreOffice trademark usage, failing to pay contributors for delivered code, and altering bylaws and election processes. In response, Collabora plans to build a separate Collabora Office for desktop — a newer codebase without Java dependencies and web-based toolkits — hosted on their own repository.

## Wayland's Big Week: Two Major Protocol Wins

### Session Restore Protocol — Officially Merged

After six years of development, the Wayland session management protocol has been merged into the official Wayland protocols. This allows desktops to restore the position and state of application windows after logout, restart, or crash. KDE's KWin already supports it; GNOME pushed implementation to version 51.

For years, this was one of the most-cited missing features for Wayland adoption. Six years is an extraordinarily long merge time for such a critical capability, but it's finally here.

### Fractional Scaling v2 — Fixing Visual Glitches

A new version of the fractional scaling protocol aims to fix visual inconsistencies that have plagued Wayland — gaps between maximized windows and panels, misaligned elements, and rendering artifacts when using non-integer scale factors. The updated protocol allows unscaled pixels to exist properly instead of relying on integer-based logical coordinate spaces. KWin has an implementation ready for review.

## GitHub Copilot's Ad Injection Scandal

Microsoft's Copilot was caught injecting advertisements into GitHub pull request descriptions — product recommendations for Raycast, VS Code, Visual Studio, JetBrains, Eclipse, and Copilot itself. Over 1.5 million pull requests were affected across thousands of repositories.

The ads were added via hidden HTML comments in PR markdown that instructed Copilot to insert "coding agent tips." Developers were furious — the ads appeared as if they had written them personally, polluting their project histories.

GitHub called it a "bug" and disabled the feature. The community isn't buying it — this was clearly intentional code designed to inject promotional content into developer workflows. The incident raises serious questions about platform trust and the boundary between AI assistance and advertising.

## Ubuntu MATE Loses Its Maintainer

Martin Wimpress, who led Ubuntu MATE for 12 years, has stepped down citing loss of passion and competing interests. The flavor did not apply for LTS qualification for Ubuntu 26.04, releasing only a non-LTS version instead. This continues a trend of Ubuntu flavors losing steam — Lubuntu is in maintenance mode and Ubuntu Unity lacks a dedicated developer.

## GNOME Drops Google Drive Integration

GNOME has officially removed Google Drive support after the underlying library (libgdata) went unmaintained four years ago. The integration had been broken for years on most distributions — GNOME disabled it ages ago, but some distros kept shipping the libraries anyway. The community consensus: it's Google's responsibility to ship a Linux client, not GNOME's job to maintain reverse-engineered integrations.

## Linux Gaming Hits Historic 5% on Steam

Linux surpassed 5% market share on Steam for the first time — hitting 5.33% versus macOS at 2.35% and Windows at 92.33%. SteamOS accounts for roughly 25% of Linux gaming. The trajectory has been steep since Valve launched Proton, accelerated by widespread dissatisfaction with Windows 11. While 5% might seem modest, the growth rate and user sentiment suggest continued momentum.

## Nvidia's HDR and Color Management Preview

Nvidia announced preview support for the DRM per-plane color pipeline API on Linux — enabling proper HDR, color accuracy, and mixed SDR/HDR content on Wayland. Interestingly, Nvidia revealed that much of this driver code was written using AI tools (specifically Claude). The preview is available for compositor developers to begin integration work.

## Wine Could Move to Zink for OpenGL Over Vulkan

A merge request proposes using Zink (developed by Collabora) as Wine's OpenGL backend, translating OpenGL calls to Vulkan. This would leverage the fact that driver developers focus on Vulkan optimization, not OpenGL. Benefits include better performance, automatic driver improvements, and resilience for devices that lack OpenGL drivers entirely. Legacy software compatibility gets a significant boost.

**Tags**: linux, open-source, wayland, office-suites, gaming, nvidia, gnome, github
**Categories**: Linux Weekly News, Open Source