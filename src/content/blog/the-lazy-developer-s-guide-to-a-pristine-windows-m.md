---
pubDatetime: 2026-04-07T18:30:56Z
title: "The Lazy Developer’s Guide to a Pristine Windows Machine: Automating with Boxstarter"
postSlug: "the-lazy-developer-s-guide-to-a-pristine-windows-m"
description: "The Lazy Developer’s Guide to a Pristine Windows Machine: Automating with Boxstarter"
tags:
  - others
---

# The Lazy Developer’s Guide to a Pristine Windows Machine: Automating with Boxstarter

Let’s be honest: setting up a new Windows development environment is the absolute worst.

It is a rite of passage that involves hours of clicking "Next," hunting for download links, forgetting that one essential license key, and configuring your IDE settings from memory. We tell ourselves we’ll document the process next time, but we rarely do.

That is, unless you are the maintainer of the **Orcomp/Boxstarter** repository.

This open-source project is a pragmatic, battle-tested collection of scripts designed to turn a fresh Windows installation into a fully armed and operational .NET development workstation with minimal friction.

## What is Orcomp/Boxstarter?

At its core, this repository is a collection of automation scripts utilizing **Boxstarter**, a wrapper around the popular Windows package manager **Chocolatey**.

While the official Boxstarter tools are powerful on their own, they require you to curate your own lists of software and configurations. That’s where this project comes in. It provides a "real-world" implementation of Boxstarter used by a developer who reinstalls Windows every six months.

Yes, you read that right. The author wipes their machine biannually. Why does this matter to you? Because it means these scripts aren't theoretical. They are constantly refined, stripped of bloat, and designed to get a productive environment up and running as fast as possible.

## Key Features

This isn't just a list of `choco install` commands. It is a workflow designed for stability and productivity.

### 1. The Hybrid Approach
One of the most frustrating things about automation is when it tries to do *everything* and fails at the one thing that is slightly complex. This project embraces a two-step process. It handles the bulk of utilities via Boxstarter but acknowledges that heavy-hitters like Visual Studio, SQL Server, and Microsoft Office are often best installed manually to manage specific configurations.

### 2. Repeatable Idempotency
The scripts are designed to be run multiple times. If a piece of software is already installed, the script simply skips it. This allows you to tweak the scripts and re-run them without fear of corrupting your system or creating duplicate entries.

### 3. Curated Software List
If you are new to the Windows ecosystem or just looking to optimize your toolset, this repo is a goldmine. It includes a list of "Paid Software" that the author swears by—tools like **Directory Opus** (file management), **Rider** (C# IDE), and **Fork** (Git client). It separates the "must-haves" from the noise.

### 4. Windows Configuration
Installing software is only half the battle. The repo links to Boxstarter’s WinConfig scripts, allowing you to toggle Windows features, update policies, and configure settings automatically so you don't have to dig through the Control Panel for two hours.

## How to Get Started

Getting your machine up to speed with this project is straightforward, though it requires a bit of manual oversight (which is part of the charm).

**1. The Prerequisites**
Start by checking the `docs\Checklist_NewInstall.md` file included in the repository. This ensures you have your BIOS and drivers in order before the software floodgates open.

**2. The Order of Operations**
The author provides a specific sequence to ensure stability:
*   **Phase 1:** Update Windows and Drivers.
*   **Phase 2:** Run `UpdateWindows.txt`. This is the "clean slate" script.
*   **Phase 3:** Run `InstallSoftware.txt`. The author recommends running this 2 or 3 times to ensure any network hiccups don't leave packages half-installed.
*   **Phase 4:** Manual Installs. This is where you grab Visual Studio, Office, and your IDE of choice.

**3. The Boxstarter Magic**
To run the scripts, you simply use the Boxstarter URL protocol in Internet Explorer or Edge (as detailed in the scripts). It handles the elevation of privileges and reboots automatically, so you can grab a coffee while it works.

## Why You Should Care

We often treat our local development environment as a precious snowflake—something we are terrified to break. This mindset slows us down. We accumulate digital cruft, outdated dependencies, and uninstalled updates because the thought of re-imaging our machine is terrifying.

The **Orcomp/Boxstarter** project flips that narrative. By open-sourcing their setup, the author provides a blueprint for "Infrastructure as Code" on your local laptop.

Even if you aren't a .NET developer, this repository serves as an excellent template. You can fork it, delete the specific software references, and replace them with your own stack (Node.js, Python, Rust, etc.). The logic remains: **if you can script it, you can rebuild it.**

If you are looking to declutter your digital life or just want a reliable starting point for your next Windows install, head over to the GitHub repository and give their scripts a read. You might just find that re-installing Windows isn't a chore anymore—it's a refresh.

*Check out the project here: [Orcomp/Boxstarter on GitHub](https://github.com/Orcomp/Boxstarter)*