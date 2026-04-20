---
pubDatetime: 2026-02-25T12:00:00Z
title: "OliveTin Alternatives: Top GitHub Projects for Web-Based Script Execution"
postSlug: "olivetin-alternatives-top-github-projects-web-based-script-execution"
description: "OliveTin Alternatives: Top GitHub Projects for Web-Based Script Execution"
tags:
  - self-hosted
  - automation
  - docker
  - devops
  - tools
---

Here are the most popular and relevant GitHub alternatives to OliveTin, grouped by how closely they match its core use case (web UI for running predefined shell commands):

---

## Closest matches — simple web UI for triggering scripts/commands

### 1. [bugy/script-server](https://github.com/bugy/script-server)

Probably the closest alternative. Web UI for your scripts with execution management, parameter inputs, live output streaming, access control, and scheduling. Python-based, Docker-ready.

### 2. [adnanh/webhook](https://github.com/adnanh/webhook) ⭐ ~10.5k stars

Lightweight incoming webhook server written in Go that runs shell commands. No web UI for buttons per se, but very popular for triggering commands via HTTP endpoints. JSON config.

### 3. [ncarlier/webhookd](https://github.com/ncarlier/webhookd)

Even simpler webhook server launching shell scripts. Directory structure defines the webhook URLs. Go-based, Docker-ready, real-time log streaming.

---

## Workflow/task schedulers with web UIs — more feature-rich but heavier

### 4. [dagu-org/dagu](https://github.com/dagu-org/dagu) ⭐ ~7k+ stars

Self-contained, lightweight workflow engine with a built-in web UI. YAML-defined workflows, single binary, zero external dependencies. Written in Go. This one would suit your Docker-heavy setup well.

### 5. [jhuckaby/Cronicle](https://github.com/jhuckaby/Cronicle) ⭐ ~4k+ stars

Multi-server task scheduler and runner with a web UI. Handles scheduled, repeating, and on-demand jobs with real-time stats and live log viewer. Node.js-based.

### 6. [semaphoreui/semaphore](https://github.com/semaphoreui/semaphore) ⭐ ~11k+ stars

Modern UI for Ansible, Terraform/OpenTofu, PowerShell and other DevOps tools. More opinionated but great if you're already using Ansible. Go-based.

---

## Enterprise/full server management — heavier but more capable

### 7. [rundeck/rundeck](https://github.com/rundeck/rundeck) ⭐ ~5.5k+ stars

Open source runbook automation with web console, CLI, and API. Self-service operations, RBAC, job scheduling, multi-node execution over SSH. Java-based, so heavier.

### 8. [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) ⭐ ~11k+ stars

Web-based server admin interface with a built-in terminal. Not specifically for predefined buttons, but gives full server management through the browser.

---

## Summary & Recommendations

Given your Docker-heavy self-hosted setup and preference for lightweight Go/Python tools, I'd say **script-server** and **Dagu** are probably the most interesting ones to evaluate alongside OliveTin. Script-server is the closest functional match, while Dagu gives you more workflow orchestration capability with that same YAML-config simplicity.