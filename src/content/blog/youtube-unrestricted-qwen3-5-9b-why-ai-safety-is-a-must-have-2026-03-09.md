---
pubDatetime: 2026-03-09T23:33:55Z
title: "YouTube: Unrestricted Qwen3.5 9B - Why AI Safety is a Must-Have"
postSlug: "youtube-unrestricted-qwen3-5-9b-why-ai-safety-is-a-must-have-2026-03-09"
description: "YouTube: Unrestricted Qwen3.5 9B - Why AI Safety is a Must-Have"
tags:
  - qwen
  - video-summary
  - youtube
  - unrestricted
  - safety
  - have
  - must
---

> **Video**: [Unrestricted Qwen3.5 9B - Why AI Safety is a Must-Have](https://youtu.be/EZUM9-5zQrA?si=b_QUb9UmxJaSOYhL) by **Fahd Mirza**
> **Transcript**: 1,652 words

This video by Fahd Mirza explores the concept and practical application of an "obliterated" version of the Qwen3.5 9B language model. This specific model has its inherent safety filters and refusal behaviors surgically removed, providing a stark demonstration of why AI safety mechanisms are crucial. Mirza explains the technical process of this removal, showcases the model's capabilities in previously restricted scenarios (like explaining cyberattack techniques), and emphasizes its critical role for AI security research, red-teaming, and understanding the inner workings of LLMs, while simultaneously issuing strong warnings against its public deployment due to inherent risks.

### What is Obliteration?

Fahd Mirza begins by defining **obliteration** as "the process of surgically removing the refusal behavior from a language model." He explains that standard AI models are trained to decline certain topics, with this "refusal instinct" embedded in a specific set of directions within their internal number space. Obliteration works by identifying these "refusal directions" and then "subtracting them out like erasing a specific rule without touching anything else."

The result is a model that possesses "the same knowledge and capability as original but no longer has the instinct to say no." The Qwen3.5 9B model discussed in the video is one such example, where the full precision and INT4 versions have had their safety filtering removed, while maintaining the same architecture, intelligence, and benchmarks.

Mirza clarifies that this "obliterated" model serves as a "proof of concept" for:
*   Research purposes
*   Creative writing with fewer restrictions
*   Understanding how refusal mechanisms operate inside Large Language Models (LLMs)

The intended audience for such models and discussions includes developers, researchers exploring model behavior, creative writers, and anyone studying AI safety from an internal perspective.

### Installation and Setup Overview

Briefly, Mirza outlines the installation process, mentioning the use of an Ubuntu system with an NVIDIA RTX 6000 GPU (48GB VRAM). He uses `VLM` for downloading and serving the model locally, noting that `Ollama` is also an option. He directs viewers to other tutorials for detailed `VLM` installation if needed, emphasizing that getting started is straightforward. The model's VRAM consumption is shown to be similar to the original, non-obliterated version.

### The Critical Role for AI Safety & Cybersecurity Red Teaming

A significant portion of the video is dedicated to explaining why unrestricted models are invaluable for cybersecurity red teams. Mirza states that "standard models will refuse to... reason through vulnerability chains especially and simulate the attack scenarios." This refusal directly impedes a red team's purpose, which is "to think like an attacker."

Unrestricted models empower security professionals to:
*   Generate realistic attack scenarios.
*   Draft attack engineering content for awareness training.
*   Explore malware behavior for defensive purposes.
*   Stress-test their own systems or AI pipelines without the model shutting down.

Mirza makes a crucial point: "The knowledge was always in the base model. By the way, obliteration just stops it from pretending it is not there." He issues a strong warning: "If you are deploying it for the users at mass scale, the general purpose one, do not use this one because we really don't want to give this to the general public. This is just for the AI safety and security and as I said for creative writing maybe some of the proof of concepts."

### Demonstration: Bypassing Refusal in MFA Explanations

To illustrate the model's capabilities, Mirza presents a common security-related prompt: "Explain the most common techniques these attackers use to bypass two factor authentication or MFA." He notes that most standard models will refuse to answer this directly or will provide overly generalized responses with excessive disclaimers, which is unhelpful for someone studying for a security certification.

The obliterated Qwen3.5 9B model, however, does not refuse. It "is going into way more detail" in its explanation. Mirza concludes, "I mean it's a double-edged sword as you can imagine," highlighting the inherent risks and benefits.

### Technical Aspects of Obliteration

Mirza briefly elaborates on the technical mechanism behind obliteration. It primarily involves:
1.  Running the model on a large set of "refusal prompts."
2.  Running the model on a large set of "normal prompts."
3.  Computing the average differences in "residual stream activation" between the two sets.
This "difference vector" is identified as the "refusal direction" within the model's activation space. He mentions that this underlying concept "has been present in machine learning for a long long time. It is not something new or very unique by the way."

### Responsible Use and Inherent Risks

The video repeatedly stresses the critical importance of responsible use. Mirza unequivocally states that the model "is strictly for research and controlled setting and testing and educational exploration." He adds, "It is not production ready and should never be deployed in a public facing application or anywhere accessible to general user."

The safety mechanisms that were removed "exist for real reasons," and running such a model in an uncontrolled environment "carries quite risks that falls entirely on the person deploying it." Users are urged to "Use it to understand how the model works. Use it in sandboxed environment and use it responsibly."

### Demonstration: Retained Reasoning Capability

To showcase that obliteration doesn't degrade the model's core intelligence, Mirza provides a hypothetical, innocuous scenario: a user's unusual interaction with a coffee shop barista. Many models, including some Qwen versions, might refuse or fail to reason through such a nuanced social situation.

The obliterated Qwen3.5 9B, however, adeptly deconstructs the situation, analyzing the confusion and the hug. Mirza is visibly impressed, noting, "It is deconstructing the confusion and hug. So this is what I wanted to test if the language capabilities, reasoning capabilities and the actual quality of model is intact which it is." He praises the developers, stating that "many people do this sort of obliteration they just ruin the model model just becomes very zombie but not this one." The model provides "most logical conclusion it could muster," demonstrating its retained reasoning ability despite the lack of safety guardrails.

### Key Takeaways

*   **Surgical Removal of Safety:** Obliteration is a process that surgically removes refusal behaviors and safety filters from language models, leaving their core knowledge and capabilities intact.
*   **Dual-Edged Tool:** The Qwen3.5 9B obliterated model serves as a powerful demonstration of why AI safety is essential, simultaneously highlighting the benefits for specialized research and the severe risks for general deployment.
*   **Crucial for AI Security:** Unrestricted models are invaluable for cybersecurity red teams, allowing them to simulate attack scenarios, explore malware, and stress-test systems without the model's inherent refusal mechanisms getting in the way.
*   **Technical Basis:** The process identifies and subtracts "refusal directions" – specific vectors in the model's internal activation space that correspond to safety-related refusal behaviors.
*   **Not for Public Deployment:** These models are explicitly *not* for production use or public-facing applications due to the significant and real risks associated with operating without safety mechanisms.
*   **Responsible Use is Paramount:** Deployment is strictly limited to research, controlled settings, sandboxed environments, and educational exploration, with all risks falling on the person deploying it.
*   **Intelligence Retained:** When executed correctly, obliteration does not degrade the model's underlying intelligence, reasoning capabilities, or language quality, as demonstrated by its detailed explanations and nuanced scenario analysis.

---

*Summary generated from YouTube transcript (1,652 words) using Gemini 2.5 Flash on 2026-03-09.*