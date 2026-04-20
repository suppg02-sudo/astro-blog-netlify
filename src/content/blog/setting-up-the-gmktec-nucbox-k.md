---
pubDatetime: 2026-03-31T20:54:39Z
title: "Setting Up the GMKtec NucBox K8 Plus for Local LLM Inference"
postSlug: "setting-up-the-gmktec-nucbox-k"
description: "Setting Up the GMKtec NucBox K8 Plus for Local LLM Inference"
tags:
  - others
---

A practical, step-by-step guide to getting your K8 Plus (Ryzen 7 8845HS, 32GB DDR5) running local AI models with Ollama — from bare hardware to running Qwen3-Coder.

## Quick Summary

- Install Ubuntu Server 24.04 LTS
- Enable IOMMU and power performance in BIOS
- Install Ollama, pull your first model, test it
- Optionally add Open WebUI for a ChatGPT-like interface
- With 32GB RAM, MoE models are your sweet spot — avoid full-density 32B+ models

## Hardware Prep

Unbox and install RAM and NVMe if you got the barebone unit:

1. Flip the K8 Plus upside, remove the four rubber feet screws
2. Pop the bottom cover off
3. Install your DDR5 SODIMM sticks (supports up to 64GB — 2x32GB DDR5 5600MHz)
4. Install your M.2 2280 NVMe SSD
5. Close it up, plug in power and ethernet

**Note on RAM**: 32GB is plenty for MoE models. If you later want to run full 32B+ dense models, you can upgrade to 64GB with 2x32GB DDR5-5600 sticks (~£110-130).

**Recommended SSD**: Any Gen4 NVMe (Lexar NM790, Crucial P3 Plus, WD Black SN850X) — 1TB minimum, 2TB ideal for models.

## BIOS Configuration

1. Power on, mash **Delete** to enter BIOS
2. Go to **Advanced** → **AMD CBS** → **NBIO Common Options** → **GFX Configuration**
   - Set **UMA Mode** to **UMA_Specified**
   - Set **UMA Frame Buffer Size** to **8G** (reserves VRAM for the iGPU — don't go higher on 32GB or you starve the system)
3. Go to **Advanced** → **AMD PBS**
   - Set **IOMMU** to **Enabled**
4. Go to **Advanced** → **CPU Configuration**
   - Set **SVM Mode** to **Enabled**
5. Save and exit (F10)

This ensures the Radeon 780M iGPU gets dedicated memory and virtualization is ready.

## Install Ubuntu Server 24.04 LTS

1. Flash Ubuntu Server 24.04 LTS to a USB drive using Balena Etcher or `dd`
2. Boot from USB (press F7 for boot menu)
3. Install normally — choose "Install Ubuntu Server"
4. When prompted, select your timezone, create your user
5. Choose to install OpenSSH Server (say yes)
6. Complete install, reboot, remove USB

## First Boot and System Updates

```bash
# Update everything
sudo apt update && sudo apt upgrade -y

# Install essentials
sudo apt install -y curl wget git build-essential cmake

# Check your hardware is recognised
lscpu | grep "Model name"
# Should show: AMD Ryzen 7 8845HS

free -h
# Should show ~32Gi total

lspci | grep -i vga
# Should show: Advanced Micro Devices Radeon 780M
```

## Set CPU Governor to Performance

```bash
# Install cpufrequtils
sudo apt install -y cpufrequtils

# Set performance governor
sudo cpufreq-set -g performance

# Make it persistent
echo 'GOVERNOR="performance"' | sudo tee /etc/default/cpufrequtils

# Verify
cpufreq-info | grep "current policy"
```

## Install Ollama

```bash
# One-line install
curl -fsSL https://ollama.com/install.sh | sh

# Verify it's running
systemctl status ollama
```

Ollama installs as a systemd service and listens on `http://localhost:11434`.

## Pull and Run Your First Model

Start with something small to verify everything works:

```bash
# Pull a small model first (4.7GB)
ollama pull qwen3:8b

# Test it
ollama run qwen3:8b "What is the capital of France?"
```

Then move to the heavier models:

```bash
# Qwen3-Coder 30B-A3B (MoE — only activates ~3B params per token, ~18GB on disk)
ollama pull qwen3-coder:30b-a3b

# Test it
ollama run qwen3-coder:30b-a3b "Write a Python function to find prime numbers"

# Devstral Small (if available, ~14GB)
ollama pull devstral:small
```

<details>
<summary>Model Size and RAM Reference (32GB)</summary>

With 32GB total RAM, you have roughly **28-29GB usable** (after OS + frame buffer). Models need to fit in RAM with room for the context window and OS overhead.

| Model | Parameters | Active Params | Quantised Size | Fits in 32GB? |
|-------|-----------|---------------|----------------|----------------|
| Qwen3 8B | 8B | 8B | ~4.7GB (Q4) | Easily |
| Qwen3-Coder 30B-A3B | 30B total | 3B active | ~18GB (Q4) | Yes — best bang for buck |
| Qwen3 14B | 14B | 14B | ~9GB (Q4) | Comfortably |
| Gemma 3 12B | 12B | 12B | ~8GB (Q4) | Comfortably |
| Devstral Small | ~24B | ~24B | ~14GB (Q4) | Yes |
| Gemma 3 27B | 27B | 27B | ~17GB (Q4) | Tight but fits |
| Qwen3 32B | 32B | 32B | ~20GB (Q4) | Very tight — may OOM |
| Llama 3.1 70B | 70B | 70B | ~40GB (Q4) | No — too large |

The MoE models (Qwen3-Coder 30B-A3B) are the sweet spot — big-model quality with only 3B active params per token, so they run fast and fit comfortably in 32GB.

**If you want to run 32B+ dense models, upgrade to 64GB DDR5.**

</details>

## Optional: Open WebUI (ChatGPT-Like Interface)

```bash
# Install Docker if not already
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER

# Log out and back in for docker group to take effect

# Run Open WebUI connected to Ollama
docker run -d \
  --name open-webui \
  --network host \
  -v open-webui:/app/backend/data \
  -e OLLAMA_BASE_URL=http://localhost:11434 \
  --restart always \
  ghcr.io/open-webui/open-webui:main

# Access at http://YOUR-K8-IP:8080
```

## Optional: Expose Ollama to Your Network

If you want to call Ollama from other machines (your main server, laptop, etc.):

```bash
# Edit the Ollama service
sudo systemctl edit ollama

# Add these lines:
[Service]
Environment="OLLAMA_HOST=0.0.0.0"

# Restart
sudo systemctl restart ollama

# Test from another machine
curl http://K8-PLUS-IP:11434/api/tags
```

## Optional: Connect to Your Server

From your existing Ubuntu server, you can now call the K8 Plus as a remote inference endpoint:

```bash
# Set OLLAMA_HOST on your server to point to the K8 Plus
export OLLAMA_HOST=http://K8-PLUS-IP:11434

# Or add to your environment permanently
echo 'export OLLAMA_HOST=http://K8-PLUS-IP:11434' >> ~/.bashrc

# Now any Ollama call from your server routes to the K8 Plus
ollama run qwen3-coder:30b-a3b "Explain distributed systems"
```

## Performance Expectations

On the K8 Plus with 32GB DDR5 and Ryzen 7 8845HS:

| Model | Approx Speed | Notes |
|-------|-------------|-------|
| Qwen3 8B | ~30-40 tok/s | Fast, great for quick tasks |
| Qwen3 14B | ~18-25 tok/s | Solid for general chat |
| Qwen3-Coder 30B-A3B | ~15-25 tok/s | MoE — only 3B active, very usable |
| Devstral Small | ~10-15 tok/s | Good for code tasks |
| Gemma 3 27B | ~6-10 tok/s | Tight fit, slower but works |

These are CPU-only estimates. The iGPU (Radeon 780M) can help but Ollama's Vulkan backend for AMD iGPUs is still experimental — CPU inference via llama.cpp is more reliable.

## Verify Everything Is Working

```bash
# Check Ollama is running
curl http://localhost:11434/api/tags

# Check available models
ollama list

# Quick benchmark
time ollama run qwen3-coder:30b-a3b "Write a haiku about servers"
```

<details>
<summary>Troubleshooting</summary>

**Ollama won't start**: Check `journalctl -u ollama -f` for errors. Usually a permissions issue — `sudo systemctl restart ollama`.

**Slow inference**: Verify CPU governor is set to performance (`cpufreq-info`). Check RAM speed is correct (`sudo dmidecode -t memory | grep Speed`).

**Model OOM**: With 32GB you need to be more selective. Check free memory with `free -h`. Close other processes. Use a smaller quantisation (Q3 instead of Q4). Stick to MoE models or sub-14B dense models.

**Network access not working**: Check `ufw` or `iptables` — `sudo ufw allow 11434/tcp`.

**BIOS won't save settings**: Update BIOS from GMKtec's download center. Some early units had BIOS bugs.

**Want to run bigger models?**: Upgrade to 64GB DDR5 (2x32GB DDR5-5600 SODIMM, ~£110-130). It's a straightforward swap — shut down, swap sticks, boot. Enables 32B dense and 70B quantised models.

</details>

<details>
<summary>Useful Ollama Commands</summary>

```bash
# List installed models
ollama list

# Delete a model
ollama rm model-name

# Show model info
ollama show qwen3-coder:30b-a3b

# Run with specific context length
ollama run qwen3-coder:30b-a3b --ctx-size 8192

# Keep model loaded (faster repeated queries)
ollama run qwen3-coder:30b-a3b --keep-alive 30m

# Check running models
ollama ps
```

</details>

**Tags**: mini-pc, llm-inference, ollama, gmktec, homelab, local-ai
**Categories**: AI Automation, Tutorials