---
pubDatetime: 2026-04-09T16:36:33Z
title: "LoRA and QLoRA Explained: The Complete Guide to Efficient LLM Fine-Tuning"
postSlug: "lora-and-qlora-explained-the-c"
description: "LoRA and QLoRA Explained: The Complete Guide to Efficient LLM Fine-Tuning"
tags:
  - others
---

Fine-tuning large language models used to mean updating billions of parameters — an expensive, impractical process for most teams. Sunny Savita's comprehensive guide covers the technique that changed everything: Low-Rank Adaptation (LoRA), and its quantised cousin QLoRA.

## The LLM Training Pipeline

Every LLM goes through three training stages:

1. **Pre-training** — Train on internet-scale data (billions/trillions of tokens) to learn language patterns
2. **Instruction fine-tuning** — Teach the model to follow specific instructions and behave properly
3. **Preference alignment** — Align model outputs with human preferences (RLHF, DPO, GRPO, ORPO)

The critical insight: you can pick up a model at **any stage** and perform custom fine-tuning on your own data. A pre-trained base model, an instruction-tuned model, or even a fully preference-aligned model — all are valid starting points.

## Full Parameter Fine-Tuning vs PEFT

### Full Parameter Fine-Tuning

In full fine-tuning, you update **every weight** in the model. For a 7 billion parameter model, that's 7 billion weights to update — for every epoch. For a 70 billion parameter model, that's 70 billion. This approach:

- Requires massive GPU memory (storing weights + gradients + optimizer states)
- Is extremely expensive computationally
- Risks catastrophic forgetting of pre-trained knowledge
- Is impractical for most organisations

### Parameter-Efficient Fine-Tuning (PEFT)

PEFT methods freeze the original model weights and only train a small set of additional parameters. LoRA is the most popular PEFT method, but others include:

- **Prefix tuning** — Add trainable tokens to the input
- **Prompt tuning** — Learn soft prompts
- **P-Tuning** — Trainable continuous embeddings
- **Adapter layers** — Insert small trainable modules between transformer layers
- **DoRA** — Decomposed weight adaptation (a newer variant)

## Understanding Weights in Transformers

To understand LoRA, you need to understand where weights live in a transformer. A transformer architecture has:

- **Self-attention layers** with query (Q), key (K), value (V) weight matrices
- **Feed-forward neural network layers** with their own weight matrices
- **Layer normalisation** parameters
- **Embedding matrices**

Each weight matrix can be enormous. For example, in a model with hidden dimension 4096, a single weight matrix is 4096 x 4096 = ~16.7 million parameters. A full transformer has many such matrices stacked across multiple layers.

## Matrix Rank: The Key to LoRA

A matrix's **rank** measures how much independent information it contains. A rank-1 matrix can be expressed as the product of two much smaller vectors. This is the mathematical foundation of LoRA.

If a weight matrix W has dimensions d x d (say 4096 x 4096), but its effective rank is only r (say r = 8), then we can approximate the weight update as:

```
ΔW = A × B

Where:
  A has dimensions d × r  (4096 × 8)
  B has dimensions r × d  (8 × 4096)
  
Instead of updating 16.7M parameters, we update 65,536 parameters — a 250x reduction.
```

This is LoRA. Instead of updating the full weight matrix, we decompose the update into two low-rank matrices and only train those.

## How LoRA Works

1. **Freeze the pre-trained model weights** — The original model is completely untouched
2. **Add low-rank adapter matrices** — Small A and B matrices alongside each weight
3. **Train only the adapters** — Only the A and B matrices get updated during backpropagation
4. **Merge at inference** — The trained adapters can be merged back into the original weights for zero inference overhead

### The LoRA Adapter

The adapter consists of:
- Matrix A (down-projection): Reduces dimension from d to r
- Matrix B (up-projection): Expands dimension from r back to d
- Scaling factor α/r: Controls the magnitude of the update

The output becomes: `output = W·x + (α/r)·B·A·x`

### Benefits of LoRA

| Benefit | Details |
|---------|---------|
| **Memory efficient** | Train adapters on single GPUs instead of clusters |
| **Fast training** | Fewer parameters = faster convergence |
| **No inference penalty** | Merge adapters into base weights for zero-cost serving |
| **Swappable adapters** | Hot-swap different fine-tunes without loading multiple full models |
| **Composable** | Stack multiple LoRA adapters for different capabilities |
| **Preserves base model** | Original weights untouched — no catastrophic forgetting |

## QLoRA: LoRA with Quantisation

QLoRA adds 4-bit quantisation on top of LoRA, reducing memory requirements even further:

- **4-bit NormalFloat (NF4)** — A data type optimised for normally-distributed neural network weights
- **Double quantisation** — Quantise the quantisation constants themselves to save additional memory
- **Paged optimisers** — Use CPU RAM for optimizer states to avoid GPU memory spikes

The result: fine-tune a 65 billion parameter model on a single 48GB GPU.

## Practical Implementation

Using Hugging Face's PEFT library:

```python
from peft import LoraConfig, get_peft_model

config = LoraConfig(
    r=8,                    # Rank of the adapter
    lora_alpha=16,          # Scaling factor
    target_modules=[        # Which layers to apply LoRA to
        "q_proj", "v_proj", "k_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj"
    ],
    lora_dropout=0.05,      # Dropout probability
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(base_model, config)
# Result: Only ~0.1% of parameters are trainable
```

### Key Hyperparameters

| Parameter | Typical Range | Effect |
|-----------|---------------|--------|
| `r` (rank) | 4-64 | Higher = more capacity, more memory |
| `lora_alpha` | 8-32 | Scaling factor (usually 2x rank) |
| `lora_dropout` | 0-0.1 | Regularisation |
| `target_modules` | Varies | More modules = better quality, slower |

## LoRA vs QLoRA vs DoRA

| Method | Precision | Memory | Quality | Speed |
|--------|-----------|--------|---------|-------|
| **LoRA** | FP16/BF16 | Moderate | High | Fast |
| **QLoRA** | 4-bit NF4 | Low | Near-LoRA | Slower |
| **DoRA** | FP16/BF16 | Moderate+ | Highest | Moderate |

DoRA (Weight-Decomposed Analysis) decomposes weights into magnitude and direction, applying LoRA only to the directional component. This often achieves better quality than standard LoRA at the cost of slightly more computation.

## Optimisers and Weight Updates

After adding LoRA adapters, the training process uses standard optimisers:

- **AdamW** — The default choice, maintains per-parameter momentum
- **Paged AdamW (QLoRA)** — Offloads optimizer states to CPU when GPU memory is tight
- **Gradient accumulation** — Simulate larger batch sizes without proportional memory increase

The key difference from full fine-tuning: optimiser states are only maintained for the adapter parameters, not the full model.

## Key Takeaways

1. **LoRA decomposes weight updates into low-rank matrices** — reducing trainable parameters by 100-1000x
2. **Freeze the base model, train only adapters** — preserve pre-trained knowledge
3. **QLoRA adds 4-bit quantisation** — enabling fine-tuning on consumer hardware
4. **Adapters can be merged for zero inference cost** — no production penalty
5. **Target the right modules** — attention projections (Q, K, V, O) and feed-forward layers benefit most
6. **Rank r is your quality/cost knob** — start at 8-16, increase if quality plateaus
7. **LoRA adapters are swappable** — one base model, many specialised adapters

> LoRA didn't just make fine-tuning cheaper — it made it accessible. What used to require a GPU cluster can now run on a single card.

**Tags**: lora, qlora, fine-tuning, llm, peft, parameter-efficient, transformers, ai-engineering
**Categories**: AI Automation, Tutorials