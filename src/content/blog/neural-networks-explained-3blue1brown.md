---
pubDatetime: 2026-02-28T00:30:00Z
title: "Neural Networks Explained: A Summary of 3Blue1Brown's Introduction"
postSlug: "neural-networks-explained-3blue1brown"
description: "Neural Networks Explained: A Summary of 3Blue1Brown's Introduction"
tags:
  - educational
  - machine-learning
  - neural-networks
  - "3blue1brown"
---

*Summary of [3Blue1Brown's "But what is a neural network?"](https://www.youtube.com/watch?v=aircAruvnKk) (18 min)*

## The Basic Concept

Neural networks are computational models inspired by the brain, where "neurons" are simple units that hold a number between 0 and 1. In a network designed to recognize handwritten digits, the first layer contains 784 neurons—one for each pixel in a 28x28 grayscale image—whose activations represent pixel brightness. The final layer has 10 neurons, each corresponding to a digit, with their activations indicating the network's confidence in that digit being the correct answer.

## Hidden Layers

Between the input and output layers are "hidden layers," whose role is to detect increasingly abstract features:

1. **Early hidden layers** detect simple patterns like edges
2. **Middle layers** combine these into shapes or loops
3. **Later layers** piece these together into recognizable digits

This layered approach mirrors how humans break down visual recognition into subcomponents.

## How Neurons Work

The network's behavior is determined by **weights** and **biases**:

- Each neuron in one layer connects to all neurons in the previous layer
- Each connection has a weight
- The neuron computes a weighted sum of its inputs, adds a bias
- The result passes through a sigmoid function to squash it into the 0-1 range

This process repeats across layers, forming a complex function with roughly 13,000 parameters (weights and biases) that can be tuned.

## Training the Network

Training means adjusting these parameters so the network's output matches the correct digit for many example images. While the exact internal workings can be opaque, understanding the structure—how layers transform data through weighted sums and nonlinearities—provides insight into how neural networks learn to recognize patterns.

## Key Takeaways

| Concept | Description |
|---------|-------------|
| **Neuron** | Unit holding a value 0-1 |
| **Weights** | Connection strengths between neurons |
| **Biases** | Threshold adjustments |
| **Sigmoid** | Function to squash values to 0-1 range |
| **Hidden layers** | Intermediate processing layers |
| **Training** | Adjusting weights/biases from examples |

## Why This Matters

This foundational understanding explains how modern AI systems work at their core. From image recognition to language models, the basic principle remains: layers of neurons transforming data through learned weights and biases.

---

*This summary was generated using the [Summarize CLI](https://github.com/steipete/summarize) with OpenRouter's free models.*