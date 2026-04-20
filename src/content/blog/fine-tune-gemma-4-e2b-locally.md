---
pubDatetime: 2026-04-05T14:35:31Z
title: "Fine-Tune Gemma-4 E2B Locally: Complete Hands-On Tutorial"
postSlug: "fine-tune-gemma-4-e2b-locally"
description: "Fine-Tune Gemma-4 E2B Locally: Complete Hands-On Tutorial"
tags:
  - others
---

> **TL;DR**: Step-by-step guide to fine-tuning Google's smallest Gemma-4 model (2B parameters) on custom datasets using free local tools — transforming generic responses into domain-specific expertise.

## Quick Summary

- **Model**: Gemma-4 E2B (2 billion parameters, Google's smallest Gemma-4)
- **Data Format**: ShareGPT-style JSONL (human/GPT conversation pairs)
- **Fine-tuning**: Local, free — no cloud GPU required
- **Case Study**: Gandhara civilization dataset (100 detailed Q&A pairs)
- **Result**: Surface-level answers transformed into deep, domain-specific expertise

## Introduction

Large language models come with broad but shallow knowledge. Ask a base model about well-documented topics and you get competent answers. Ask something niche — like the Gandhara civilization, an ancient crossroads of Buddhist, Greek, Persian, and Indian worlds — and you get generic, surface-level responses. Fine-tuning changes that. This tutorial walks through the complete process of taking Gemma-4 E2B, Google's smallest and most accessible Gemma-4 variant, and training it on custom domain knowledge — entirely locally and for free.

The approach mirrors the broader model family work already covered: Gemma-4 31B and E24 with OpenCL and Ollama. But the E2B model deserves its own treatment because its small size changes the fine-tuning calculus entirely. What takes hours on a 31B takes minutes on 2B. What requires an A6000 for larger models runs on consumer hardware here.

## The Dataset Problem

Base models have a fundamental limitation: they know *about* things, but they don't know *your* things. The Gandhara civilisation is a perfect test case — one of history's most fascinating but underappreciated cultures, spanning the Kushan Empire, Silk Road trade, Buddhist philosophy, Gandharan art, ancient scripts, and centuries of cross-cultural exchange in what is now Pakistan.

A base model produces shallow summaries. A fine-tuned model produces deep analysis informed by 100+ detailed question-answer pairs covering every angle.

### ShareGPT JSONL Format

The dataset uses the ShareGPT conversation format in JSONL (JSON Lines). Each line is a complete conversation:

```json
{"messages":[{"role":"user","content":"What was the significance of the Silk Road in Gandharan culture?"},{"role":"assistant","content":"The Silk Road was fundamental to Gandharan development, serving as a conduit for Buddhist philosophy, Hellenistic artistic techniques from Alexander's successors, Persian administrative practices, and Indian philosophical traditions..."}]}
```

**Key characteristics:**
- Structured as `messages` array with `role` and `content` fields
- Single-turn conversations (one user question, one assistant answer)
- Each answer is rich, detailed, and authoritative
- Covers diverse sub-topics: rulers, monasteries, art, scripts, geography, decline

<details>
<summary>📊 Dataset Coverage Breakdown</summary>

The 100-pair dataset spans:
- **Kushan Empire** — political history and key rulers
- **Silk Road trade** — economic networks and cultural exchange
- **Buddhist philosophy** — doctrinal development and transmission
- **Gandharan art** — Greco-Buddhist sculpture and iconography
- **Ancient scripts** — Kharoshti, Brahmi, and bilingual inscriptions
- **Key monasteries** — Taxila, Takht-i-Bahi, and architectural traditions
- **Civilization decline** — Hun invasions, shifting trade routes, regional fragmentation

</details>

## Prerequisites

Before starting, ensure you have:

| Requirement | Details |
|------------|---------|
| **GPU** | NVIDIA GPU with CUDA support (consumer-grade sufficient for 2B model) |
| **Python** | 3.10+ with appropriate package management |
| **Disk Space** | ~10GB for model weights, checkpoints, and training artifacts |
| **Memory** | 16GB+ system RAM recommended |
| **Dataset** | Custom JSONL file in ShareGPT format |

## Step-by-Step Fine-Tuning Process

### Step 1: Install Required Libraries

The fine-tuning stack uses established Python ML libraries. Key dependencies include the transformer framework, dataset handling utilities, and fine-tuning-specific packages designed for parameter-efficient training.

```bash
pip install transformers datasets trl accelerate bitsandbytes
```

### Step 2: Load the Base Model

The Gemma-4 E2B model loads from Hugging Face with quantisation to reduce memory footprint during training:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "google/gemma-4-e2b"
tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto",
    load_in_4bit=True  # Quantisation for consumer GPUs
)
```

### Step 3: Prepare the Dataset

Load your JSONL dataset and format it for training:

```python
import json
from datasets import Dataset

def load_jsonl_data(filepath):
    conversations = []
    with open(filepath, 'r') as f:
        for line in f:
            conv = json.loads(line)
            conversations.append(conv)
    return Dataset.from_list(conversations)

dataset = load_jsonl_data('gandhara_dataset.jsonl')
print(f"Loaded {len(dataset)} training examples")
```

### Step 4: Configure Fine-Tuning Parameters

The training configuration balances quality, speed, and memory efficiency:

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Learning Rate** | 2e-4 | Conservative for stable convergence on small datasets |
| **Epochs** | 3-5 | Enough to learn patterns without overfitting on 100 examples |
| **Batch Size** | 4-8 | Fits in consumer GPU memory with quantisation |
| **LoRA Rank** | 8-16 | Parameter-efficient — trainable subset of weights |
| **Max Sequence Length** | 2048 | Accommodates detailed Q&A responses |

```python
from trl import SFTTrainer
from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="./gemma4-gandhara-finetuned",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    fp16=True,
    logging_steps=10,
    save_steps=50,
    save_total_limit=2,
)

trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    tokenizer=tokenizer,
    dataset_text_field="text",
    max_seq_length=2048,
)
```

### Step 5: Run Training

Execute the training loop and monitor convergence:

```python
trainer.train()
trainer.save_model("./gemma4-gandhara-finetuned/final")
```

Training completes in minutes rather than hours thanks to the 2B parameter count and LoRA efficiency.

### Step 6: Test the Fine-Tuned Model

Compare before and after responses:

**Before Fine-Tuning (Base Model):**
> "The Gandhara civilization was an ancient culture in what is now Pakistan and Afghanistan. It was known for its Buddhist art and architecture..."

**After Fine-Tuning:**
> "The Gandhara civilisation flourished from roughly the 6th century BCE to the 11th century CE in the region encompassing modern-day Khyber Pakhtunkhwa, northern Punjab, and eastern Afghanistan. Its significance lies in serving as the crucial nexus where four major cultural spheres — Buddhist, Hellenistic, Persian, and Indic — converged into something entirely original. The Kushan Empire, particularly under Emperor Kanishka (c. 127-150 CE), elevated Gandhara from a regional power to a civilisation of trans-Asian significance. Kanishka's patronage of Buddhism, his convening of the Fourth Buddhist Council at Kundalwan in Kashmir, and his establishment of the capital at Purushapura (modern Peshawar) transformed the region into one of the great intellectual centres of the ancient world. Gandharan art represents perhaps the most visible legacy of this synthesis..."

The difference is substantial. The fine-tuned model produces specific names, dates, locations, and contextual analysis rather than generic summaries.

## Key Technical Considerations

### Why Gemma-4 E2B?

The 2-billion-parameter model is uniquely suited for local fine-tuning:

| Factor | E2B Advantage |
|--------|---------------|
| **Memory** | Fits in 8GB VRAM with 4-bit quantisation |
| **Training Time** | Minutes, not hours |
| **Quality** | Inherits Gemma-4's architectural improvements |
| **Accessibility** | Free, open weights, no API costs |

### Overfitting Prevention

With only 100 training examples, overfitting is the primary risk. Mitigation strategies include:

- **Low learning rate** (2e-4) — gradual weight updates, not dramatic shifts
- **Limited epochs** (3-5) — enough to learn patterns, not memorise examples
- **LoRA** — trains a small adapter layer, preserving base model knowledge
- **Validation** — test with questions not in the training set

### Dataset Quality Over Quantity

A hundred detailed, authoritative Q&A pairs outperform thousands of shallow ones. Each training example teaches the model not just *what* to say but *how* to say it — the depth, structure, and authority level expected for the domain.

<details>
<summary>🔬 Deep Dive: ShareGPT Format Variations</summary>

While single-turn Q&A works for factual domains, conversation-format datasets enable more nuanced training:

```json
{"messages":[
  {"role":"user","content":"Tell me about Gandharan art."},
  {"role":"assistant","content":"Gandharan art represents a unique synthesis..."},
  {"role":"user","content":"How does it differ from earlier Buddhist art?"},
  {"role":"assistant","content":"The key distinction lies in the anthropomorphic representation..."}
]}
```

Multi-turn conversations teach the model conversational flow, follow-up handling, and contextual reasoning — valuable for customer service, tutoring, and dialogue applications.

</details>

## Results and Performance

After fine-tuning, the model demonstrates measurable improvement:

- **Answer depth** — from 2-3 sentence summaries to paragraph-level analysis
- **Specificity** — names, dates, locations, and proper nouns appear naturally
- **Coherence** — responses maintain logical flow and don't contradict themselves
- **Domain authority** — tone shifts from encyclopedic summary to knowledgeable expert

The E2B model after fine-tuning outperforms larger base models on domain-specific queries, proving that targeted training beats scale alone.

## When to Use This Approach

Fine-tuning makes sense when:

| Scenario | Fit | Alternative |
|----------|-----|-------------|
| **Domain expertise needed** | ✅ Ideal | RAG for factual lookup only |
| **Tone/style matters** | ✅ Ideal | Prompt engineering insufficient |
| **Latency requirements** | ✅ Ideal | Local inference, no API calls |
| **Data privacy** | ✅ Ideal | Nothing leaves your machine |
| **Broad general knowledge** | ❌ Skip | Use base model with good prompts |
| **Rapidly changing information** | ❌ Skip | RAG with live data retrieval |

## Next Steps

The pipeline scales naturally:

1. **Expand the dataset** — add more topics while maintaining quality standards
2. **Merge adapters** — combine multiple fine-tuned adapters for multi-domain expertise
3. **Deploy with Ollama** — serve the fine-tuned model via API for applications
4. **Evaluate rigorously** — benchmark against base model and competing approaches

<details>
<summary>📚 Resources & Further Reading</summary>

- Google Gemma Models — [https://ai.google.dev/gemma](https://ai.google.dev/gemma)
- ShareGPT Dataset Format — [https://sharegpt.com](https://sharegpt.com)
- LoRA: Low-Rank Adaptation — [https://arxiv.org/abs/2106.09685](https://arxiv.org/abs/2106.09685)
- Hugging Face Fine-Tuning Guide — [https://huggingface.co/docs/transformers/training](https://huggingface.co/docs/transformers/training)
- TRL (Transformer Reinforcement Learning) — [https://huggingface.co/docs/trl](https://huggingface.co/docs/trl)

**Video Source**: [Fine-Tune Gemma-4 on Your Own Dataset Locally](https://www.youtube.com/watch?v=cHpB0PTRx5A) by Fahd Mirza (Apr 3, 2026)

</details>

---

*This post was generated from a YouTube video transcript and edited for clarity. Original video by Fahd Mirza covers the complete walkthrough with live demonstrations.*