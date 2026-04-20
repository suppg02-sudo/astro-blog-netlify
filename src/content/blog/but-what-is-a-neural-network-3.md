---
pubDatetime: 2026-04-07T22:59:48Z
title: "But What Is a Neural Network? — 3Blue1Brown Deep Learning Chapter 1"
postSlug: "but-what-is-a-neural-network-3"
description: "But What Is a Neural Network? — 3Blue1Brown Deep Learning Chapter 1"
tags:
  - others
---

> **TL;DR**: 3Blue1Brown's Grant Sanderson explains the structure of neural networks from first principles, using handwritten digit recognition as a motivating example. A beautifully visual introduction to neurons, layers, weights, biases, and the math underlying deep learning.

## Quick Summary

- Neural networks are organized in layers: input (784 neurons for 28x28 pixel images), hidden layers, and output (10 neurons for digits 0-9)
- Each neuron holds an "activation" value between 0 and 1, representing how much it "lights up"
- Weights and biases control how activations flow from one layer to the next
- The network learns by adjusting these weights and biases to correctly classify inputs
- The ReLU (Rectified Linear Unit) activation function has largely replaced sigmoid in modern networks

## How the Network Works

Sanderson uses the classic MNIST handwritten digit recognition problem. The input is a 28x28 pixel grid (784 pixels = 784 input neurons). The goal is to output which digit (0-9) the image represents.

Each neuron in a hidden layer is essentially a mathematical function: it takes all activations from the previous layer, multiplies each by a weight, sums them, adds a bias, and passes the result through an activation function (ReLU or sigmoid). This produces a single activation value for that neuron.

The key insight is that **each neuron in a hidden layer can be thought of as detecting a specific pattern** — edge detection is a concrete example. A neuron might "light up" when it sees a horizontal edge in the top-left of the image. Later layers combine these low-level detections into higher-level recognitions.

### The Math

For a neuron in layer L with index k:

```
activation(k) = σ( Σ(w_i · a_i) + b_k )
```

Where `w_i` are weights, `a_i` are activations from the previous layer, `b_k` is the bias, and `σ` is the activation function. Written in matrix form, this is simply `W·a + b` — a linear algebra operation that GPUs excel at.

### Why Layers?

The layered structure is what gives neural networks their power. Early layers detect simple patterns (edges), middle layers detect combinations (loops, intersections), and final layers detect complex structures (complete digits). A network with just one hidden layer can theoretically approximate any function, but deeper networks learn more efficiently.

### ReLU vs Sigmoid

The video originally introduced sigmoid (0 to 1 smoothly) but notes that modern networks predominantly use ReLU (`max(0, x)`). ReLU is simpler, faster to compute, and avoids the "vanishing gradient" problem that plagues sigmoid in deep networks.

## What "Learning" Means

The structure described here is just the inference part — given trained weights and biases, the network produces an output. "Learning" is the process of finding the right weights and biases by showing the network thousands of labelled examples and adjusting parameters to reduce errors. That's the topic of Chapter 2.

---

*Source: [3Blue1Brown — But what is a neural network?](https://www.youtube.com/watch?v=aircAruvnKk) by Grant Sanderson*

<details>
<summary>📚 References &amp; Further Reading</summary>

- [3Blue1Brown: Neural Networks Interactive Series](https://www.3blue1brown.com/topics/neural-networks) — Written/interactive form of the video series
- [Neural Networks and Deep Learning (Michael Nielsen)](https://goo.gl/Zmczdy) — Free online book that walks through the same digit recognition example with code
- [GitHub: neural-networks-and-deep-learning](https://github.com/mnielsen/neural-networks-and-deep-learning) — Michael Nielsen's companion code repository
- [Colah's Blog](http://colah.github.io/) — Chris Olah's renowned blog on neural network visualizations and concepts
- [Distill](https://distill.pub/) — Beautiful, interactive publications on machine learning research
- [GitHub: Manim](https://github.com/3b1b/manim) — The open-source Python library used to create the animations in this video
- [3Blue1Brown on Patreon](https://www.patreon.com/3blue1brown) — Support future 3Blue1Brown projects
- [Welch Labs: Machine Learning Series](https://youtu.be/i8D90DkCLhI) — Another recommended video series on ML fundamentals

</details>

**Tags**: neural-networks, deep-learning, 3blue1brown, machine-learning, education
**Categories**: AI Automation, Tutorials