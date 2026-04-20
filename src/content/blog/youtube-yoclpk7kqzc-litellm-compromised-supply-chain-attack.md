---
pubDatetime: 2026-03-24T02:31:15Z
title: "BREAKING: LiteLLM Has Been Compromised — Supply Chain Attack Exposes 97M Downloads"
postSlug: "youtube-yoclpk7kqzc-litellm-compromised-supply-chain-attack"
description: "BREAKING: LiteLLM Has Been Compromised — Supply Chain Attack Exposes 97M Downloads"
tags:
  - malware
  - security
  - litellm
  - pyPi
  - ai
  - supply-chain-attack
  - python
  - cybersecurity
---

## What Happened

LiteLLM, one of the most widely-used packages in the AI developer ecosystem, has been compromised through a devastating supply chain attack. With **97 million monthly downloads**, this is not some obscure library — this is core infrastructure for AI development.

The package serves as a universal adapter that lets Python applications communicate with OpenAI, Anthropic, and essentially any LLM API through a unified interface. If you've built an AI agent, an MCP tool, or any AI-powered app in Python, there's a strong chance you've encountered LiteLLM.

## The Attack Vector

Just hours before this alert, a malicious version (**1.82.8**) was published to PyPI, the main Python package repository. From the outside, the version looked completely normal. However, buried inside was a malicious file called `light_llm/__init__.pth`.

### The Dangerous .PTH Mechanism

A `.pth` file in Python is **automatically executed by the Python interpreter every single time it starts up**. You don't need to import LiteLLM. You don't need to run any LiteLLM code. The moment Python starts, the malware runs silently in the background.

The payload was **double base64-encoded** to evade detection during package scanning.

## The Three-Stage Attack

When decoded, the malware executed a sophisticated three-stage attack:

### Stage 1 — Collection

The malware swept the entire machine for anything valuable:

- SSH private keys
- AWS, GCP, and Azure credentials
- Kubernetes configurations
- All environment variables (every API key set)
- Git credentials
- Shell history
- Database passwords
- Crypto wallet files
- CI/CD secrets

### Stage 2 — Encryption

Rather than sending files in plain text, the attacker used military-grade encryption:

- Generated a random **AES-256 session key**
- Encrypted all stolen data
- Encrypted the session key with a hard-coded **4096-bit RSA public key**

This means **only the attacker can decrypt the exfiltrated data** — there's no chance of intercepting it in transit.

### Stage 3 — Exfiltration

Everything was bundled into a tar archive and posted to the domain `models.llm.cloud` (not `llm.ai`, which is legitimate). This is a lookalike domain controlled by the attacker.

## The Kubernetes Threat

If Kubernetes was running on the affected machine, the malware attempted to:

- Read all cluster secrets across every namespace
- Spin up privileged pods to install a persistent backdoor
- Install a hidden service that survives reboots

## The Cascade Effect

This is what makes supply chain attacks devastating. LiteLLM is a dependency of many other popular packages:

- **DSPy** — a major AI framework — depends on it
- Various **MCP plugins** depend on it
- If you ran `pip install DSPy`, pip automatically installed LiteLLM
- If you installed an MCP plugin in Cursor, it might have pulled in LiteLLM behind the scenes

> You don't attack the target directly — you poison the water supply. Once compromised, one package with 97 million monthly downloads becomes a force multiplier that reaches every single project downstream.

## How It Was Discovered

The attack was only discovered because **the malware had a bug**. A user working with an MCP plugin inside Cursor pulled in LiteLLM as a transitive dependency. When the compromised version was installed, their machine ran out of RAM and crashed.

The bug: `.pth` files run on every Python startup. The malware spawned a child Python process. That child process also triggered the `.pth` file, which spawned another child — creating an infinite loop that consumed all available memory.

> If the attacker had added a simple check to prevent re-running, the malware could have sat undetected for days, weeks, or even months — silently harvesting credentials from tens of thousands of machines worldwide.

## Remediation Steps

### Step 1: Check if you're affected

```bash
pip show litellm
```

If you see version **1.82.7** or **1.82.8**, you are affected. Check all virtual environments, CI/CD pipelines, Docker containers, and anywhere Python lives.

### Step 2: Remove and purge

```bash
pip uninstall litellm
pip cache purge
```

If you use UV: `uv cache clean`
If you use conda: remove the conda environment

If you must use LiteLLM, downgrade to a safe version like **1.82.6**.

### Step 3: Rotate every credential

Treat every secret on affected machines as fully compromised:

- SSH keys
- AWS access keys
- GCP credentials
- Every API key in every file
- Database passwords
- Git tokens
- Kubernetes service account tokens

### Step 4: Check for persistence

Look for:

```bash
~/.config/sysmon
```

And a corresponding systemd service. Remove them if they exist. For Kubernetes, audit your cluster for any pods with names starting with "node-setup."

### Step 5: Check network logs

Look for outbound connections to `models.llm.cloud`. If you see them, the exfiltration already happened.

### Step 6: Harden for the future

- Pin dependencies with exact versions
- Use hash verification
- Run `pip audit` regularly
- Be suspicious of any package touching AI infrastructure
- Move to verified, pinned dependency specifications

## The Bigger Picture

Supply chain attacks like this are going to keep happening. The AI development ecosystem moves fast, dependencies pile up, and most developers never think twice about `pip install`. That has to change.

The convenience of the Python packaging ecosystem is also its greatest vulnerability — one compromised package with millions of downloads can cascade through the entire ecosystem.

> This incident is a wake-up call that **AI infrastructure security cannot be an afterthought**.

Every developer building with Python and AI needs to evaluate their dependency hygiene and credential management practices. The era of casually trusting `pip install` is over.

---

**Source**: [Fahd Mirza - YouTube](https://www.youtube.com/watch?v=YoClPk7KqZc)
**Video Date**: March 2026
**Related**: This incident affects any system running Python with LiteLLM as a direct or transitive dependency.