---
pubDatetime: 2026-03-07T23:34:47Z
title: "Plano: Free Local LLM Routing, Guardrails & Observability"
postSlug: "plano-local-llm-routing-guardrails-observability"
description: "Plano: Free Local LLM Routing, Guardrails & Observability"
tags:
  - llm-routing
  - guardrails
  - ollama
  - observability
  - plano
  - production-ai
  - local-ai
---

## The Production Problem in Agentic AI

Building agentic AI applications is relatively easy. Shipping them to production is where things fall apart. Every development team eventually faces the same reality: they end up writing the same boilerplate code over and over again—routing logic to direct requests to the right agent, guardrail hooks for safety, observability glue for tracing, and scattered model provider adapters.

This is the exact problem that **Plano** aims to solve. Instead of embedding this middleware directly in your application code, Plano extracts it into a standalone, out-of-process data plane that sits between your user interface, your agents, and your LLM provider.

## What Is Plano?

Plano is an open-source tool that serves as a comprehensive middleware layer for agentic AI systems in production. It handles three critical concerns that every team eventually needs to implement:

- **Routing Logic**: Directing user queries to the appropriate agent or model
- **Guardrails**: Filtering and modifying queries before they reach your LLM for safety
- **Observability**: Capturing traces, signals, and telemetry without writing custom monitoring code

The architecture is elegantly simple: your application code never touches routing, moderation, or observability. Plano handles all of this transparently in the middle, allowing your agents to focus exclusively on business logic.

## How Plano Works

Plano operates as a **dual-proxy system** that intercepts and manages AI requests:

1. **First Proxy (Guardrails)**: Receives the initial user query and applies guardrail filters, potentially modifying the query before it ever reaches your agents
2. **Agent Processing**: The clean, filtered query is routed to the appropriate agent, which could be built with LangChain, CrewAI, or any other framework
3. **Second Proxy (Gateway)**: The agent's LLM call passes through another Plano proxy acting as the model gateway
4. **Response Capture**: The gateway proxies the call to any upstream LLM, captures the response, generates traces and agentic signals, then returns the result back through the agent to the user

### Technical Foundation

- **Built on Envoy**: Uses Envoy proxy technology, ensuring scalability and reliability
- **Framework Agnostic**: Supports any programming language or framework
- **Efficient Routing**: Uses a lightweight 4B parameter model for routing decisions instead of burning expensive API calls to OpenAI or Anthropic
- **Universal Provider Support**: Works with any LLM provider, including local models like Ollama

## Installation and Setup

Getting Plano up and running is straightforward. The video demonstrates the complete process:

### Prerequisites

First, ensure you have **UV** installed (a modern Python package installer):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Source it in your shell to make it available:

```bash
source ~/.bashrc
```

### Install Plano

Install the Plano CLI tool using UV:

```bash
uv tool install plano
```

### Configuration

Create a YAML configuration file that specifies your model and connection details:

```yaml
base_model: "your-model-name"
base_url: "http://localhost:11434"  # Ollama endpoint or remote URL
access_key: "any-string"             # Simple authentication
listen_port: 12000                    # Port for Plano gateway
```

### Start the Service

Launch Plano with your configuration:

```bash
plano start --config plano-config.yml
```

Once running, you'll see both the proxy and gateway active, ready to intercept and manage AI requests.

## Testing with Local Models

The demonstration shows Plano working seamlessly with **Ollama**, running locally on an Ubuntu system with an NVIDIA A6000 GPU (48GB VRAM) and the GLM 4.7 Flash model.

A simple test script sends a chat request to the Plano gateway on port 12000. Plano intercepts the request, applies guardrail filters, routes it to the local Ollama model, and returns the response—all while automatically capturing traces and signals without a single line of observability code.

The performance is impressive: GLM 4.7 Flash responds quickly through the Plano middleware, demonstrating that the additional proxy layer introduces minimal overhead.

## Real-World Use Cases

It's important to note that Plano is designed for **large-scale enterprise applications**, not small projects. As the presenter emphasizes, "Don't try to kill a mosquito from a cannon." This tool makes sense primarily when you're serving hundreds of thousands of users and hosting your infrastructure on Kubernetes.

### Customer Support Agents

Production customer support systems need robust guardrails to block jailbreak attempts and filter malicious queries before they reach your LLM. Plano handles this automatically, protecting your system without requiring custom security code.

### Multi-Agent Travel Assistants

Complex multi-agent systems often require manual routing functions to direct flight queries to one agent and hotel queries to another. Plano eliminates this boilerplate by intelligently routing requests based on their content.

### Fintech Applications

Financial technology applications often need to swap between different models dynamically or switch between "thinking" and "non-thinking" models depending on the query complexity. Plano provides this flexibility while maintaining compliance with regulatory requirements through comprehensive observability.

### Enterprise Deployments

Large-scale deployments serving massive user bases require robust middleware for routing, safety, and monitoring. Plano is purpose-built for this scenario, particularly when infrastructure is hosted on Kubernetes.

## The Local-First Advantage

One of Plano's most compelling features is its ability to work entirely with local models. The demonstration uses no API keys, no vendor logins, and no external dependencies. Everything runs locally with Ollama, offering several benefits:

- **Data Sovereignty**: Your data never leaves your infrastructure
- **Zero Vendor Lock-in**: You're not dependent on any specific cloud provider
- **Cost Control**: No ongoing API expenses or token billing
- **Privacy Compliance**: Easier to meet regulatory requirements when data stays local

This local-first approach aligns with a growing trend in AI development—prioritizing data sovereignty and reducing dependency on cloud providers.

## A Maturing Ecosystem

The presenter notes that LLM routing is not a new concept. Over the past two years, they've covered similar tools like Arch Router, Claw Router, and LLM Router. This suggests a maturing ecosystem of AI infrastructure tools, with Plano representing the latest evolution in this space.

The recurring need for routing, guardrails, and observability middleware speaks to a fundamental truth about production AI systems: model inference is only one piece of the puzzle. Comprehensive infrastructure for safety, monitoring, and reliability is essential for real-world deployments.

## Is Plano Right for You?

The key question is whether your use case justifies the complexity of Plano. For small projects or proof-of-concept applications, the overhead may not be worth it. You're better off keeping things simple and adding middleware only as needed.

However, for enterprise teams building production agentic AI systems at scale, Plano offers a compelling value proposition:

- **Focus on Business Logic**: Your agents contain only domain-specific code, not infrastructure glue
- **Zero Observability Boilerplate**: Tracing and telemetry happen automatically
- **Built-in Safety**: Guardrails protect your LLMs without custom security code
- **Universal Compatibility**: Works with any language, framework, or LLM provider
- **Local-First Option**: Run entirely on local models for data sovereignty

## Getting Started

If you're considering Plano for your production AI systems, here's the recommended approach:

1. **Evaluate Your Scale**: Are you serving thousands or hundreds of thousands of users?
2. **Assess Your Middleware Needs**: Do you already have routing, guardrails, and observability in place?
3. **Test Locally**: Start with Ollama or a local model to understand the architecture
4. **Measure Impact**: Compare developer productivity and system reliability before and after implementation
5. **Scale Gradually**: Begin with a subset of your agents and expand as needed

Plano is open source and free to run locally. The repository includes examples and documentation to help you get started.

## Resources

- Plano GitHub repository
- Ollama for local LLM hosting
- UV for Python package management
- Related tools: Arch Router, Claw Router, LLM Router

## Full transcript and short summary available in resources