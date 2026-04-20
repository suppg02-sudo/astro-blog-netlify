---
pubDatetime: 2026-04-07T20:41:15Z
title: "Is Google Holding Back? The Hidden \"Time Travel\" Feature in Gemma 4"
postSlug: "is-google-holding-back-the-hidden-time-travel-feat"
description: "Is Google Holding Back? The Hidden \"Time Travel\" Feature in Gemma 4"
tags:
  - others
---

# Is Google Holding Back? The Hidden "Time Travel" Feature in Gemma 4

If you’ve been following the recent release of Google’s Gemma 4, you might think you know exactly what the model is capable of. It’s open, it’s efficient, and it’s widely available on platforms like Hugging Face. But what if I told you that the version of Gemma 4 currently sitting on your hard drive isn’t actually the best version?

In fact, there is a growing discussion in the AI community suggesting that Google is keeping a superior iteration of the model away from the public. And the reason why centers on a specific technical capability that essentially allows an LLM to "time travel."

No, this isn't sci-fi. It’s a technique called Multi-Token Prediction (MTP), and its absence from the standard public releases is raising some serious questions about transparency and performance.

## The Missing Piece: What Happened to MTP?

Recently, a discussion popped up on Hugging Face that caught the attention of the open-source community. A Google employee confirmed that MTP (Multi-Token Prediction) was deliberately removed from the standard Gemma 4 models available to the public (specifically the SafeTensor and GGUF formats).

The reason given was technical: Google claimed there were problems integrating MTP into `llama.cpp` and Transformers—the tools that roughly 90% of us use to run local LLMs. Because these popular tools couldn't easily support the feature, Google decided to prune it from the public models entirely.

However, there is a catch. The feature **does** exist in the versions of Gemma 4 designed for LiteRT. 

### What is LiteRT?
LiteRT is Google’s open-source framework for running models on edge devices, like Android phones or other hardware with limited compute power. 

Here is the problem: The LiteRT models are essentially pre-compiled. You can download them, but you can’t "uncompile" them to see the raw code or adapt them easily for other uses. In contrast, the standard SafeTensor and GGUF formats are incredibly popular because they are flexible and transparent.

When we look at the download numbers, the disparity is shocking. The standard Gemma 4 models have millions of downloads combined. The LiteRT version? Only about 8,000. By removing MTP from the standard formats, Google has effectively hidden a major performance boost from 99% of its users.

## Why "Pruning" MTP Hurts the Community

The excuse that MTP was removed because it wasn't working with standard tools doesn't really hold water when you look at how the open-source community operates.

If a model has a feature that a tool like `llama.cpp` can't use yet, the standard procedure isn't to delete the feature from the model. The tool simply ignores it. The model runs as usual, just without the extra speed boost. We see this right now with models like **DeepSeek V3** and **Qwen 3.5**. These models possess MTP capabilities, and while `llama.cpp` doesn't fully support it yet, the models still run perfectly fine.

By stripping MTP from the public Gemma 4 models, Google has prevented developers from implementing the feature themselves. Even if a developer wanted to write the code to unlock this "time travel" speed boost for Gemma 4, they can't, because the code is physically missing from the model weights we have access to.

## "Time Traveling" for LLMs: How MTP Works

So, what exactly is this "time travel" feature, and why is it such a big deal?

In the world of Machine Learning, this concept is often called **Speculative Decoding**. It sounds complex, but the logic is actually quite simple. Think of it as using a small model to predict tokens for the big model so the big model doesn't have to.

Here is a breakdown of how it works:

1.  **The Setup:** Imagine you are running a massive model, like a 90B parameter beast. It is slow and computationally expensive to generate a single token.
2.  **The Draft:** You also load a tiny version of the model (like a 1B parameter version). This tiny model is blazing fast—it can predict tokens at 400 or 500 tokens per second.
3.  **The Prediction:** Instead of the big model generating the next word from scratch, the tiny model "time travels" ahead, quickly drafting out a sequence of tokens (e.g., "the quick brown fox").
4.  **The Verification:** The big model then steps in, but instead of generating, it just *verifies*. It asks, "Does 'the quick brown fox' make sense?"

If the answer is yes, the big model accepts the tokens instantly. Because the big model is only verifying rather than generating, you can see massive speed increases—sometimes 2x to 3x higher tokens per second.

### The Caveats
There are some requirements for this to work. You generally need to use models from the same family because they must share the same vocabulary. If the tiny draft model is too "dumb" and makes too many errors, the big model will reject the predictions, and you lose the speed advantage. But in most cases, the net result is a significantly faster experience.

## Conclusion: A Step Backward for Open Source

The omission of Multi-Token Prediction from the standard Gemma 4 release is a disappointment. It feels like a step backward for the open-source ethos that Google claims to support.

By locking this performance boost behind their specific LiteRT framework and removing it from the standard Hugging Face releases, they have limited the model's potential. The community is great at solving integration problems—if MTP had been left in the model, developers would have eventually figured out how to support it in `llama.cpp` and other tools.

Instead, we are left with a model that is effectively hobbled compared to its "true" form. While Gemma 4 is still a capable model, it’s hard not to feel like we’ve been given a version that is slower and less capable than what Google is keeping for their own ecosystem.