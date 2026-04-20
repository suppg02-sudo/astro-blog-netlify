---
pubDatetime: 2026-03-31T01:11:27Z
title: "Distributed Computing at the Individual Scale: Storage, Compute, and LLM Inference"
postSlug: "distributed-computing-at-the-i"
description: "Distributed Computing at the Individual Scale: Storage, Compute, and LLM Inference"
tags:
  - others
---

A practical walkthrough of the distributed systems landscape across storage, compute, memory, and GPU inference — with a focus on what actually matters at the homelab and individual scale, from Ceph and GlusterFS to Exo's peer-to-peer model splitting.

## Distributed Storage

The two heavyweights remain **Ceph** and **GlusterFS**, both mature and battle-tested, but they sit at very different points on the complexity curve.

**GlusterFS** is the simpler option for small-scale setups. It's a POSIX-compliant distributed filesystem that aggregates storage across nodes using peer-to-peer replication. The underlying files on each brick remain plain, recognisable files on the local filesystem — which is a genuine advantage in disaster recovery scenarios. Installation is minimal compared to Ceph. The trade-off is that it doesn't scale as gracefully beyond a handful of nodes and lacks Ceph's object/block flexibility.

**Ceph** provides unified object, block, and file storage under a single cluster via RADOS. It's the more versatile option — particularly if you need S3-compatible object storage (via RGW) alongside block devices — but it has significantly more moving parts: monitors, OSDs, metadata servers, and the manager daemon. For a homelab with 3+ nodes it's viable, but you'll spend more time on setup and tuning.

For Docker Swarm setups across VPS hosts, **MinIO** is also worth noting — it's a lightweight S3-compatible object store that's trivially easy to deploy in distributed mode and performs well at small scale. It doesn't replace a filesystem, but for blob storage (backups, model weights, document stores) it's very effective.

**Longhorn** (from Rancher/SUSE) is worth a mention if you ever move toward Kubernetes — it's designed specifically for cloud-native persistent storage and is much simpler than Ceph in that context.

**IPFS** sits in a different category — it's a content-addressed distributed filesystem designed for decentralised sharing rather than high-performance block/file storage. Interesting for data sovereignty and deduplication, but not a practical replacement for Ceph/Gluster in infrastructure terms.

## Distributed Compute

Three frameworks dominate here:

**Ray** (from Anyscale/UC Berkeley) has become the de facto standard for distributed Python/ML workloads. It provides a clean actor-based model with `@ray.remote` decorators, a built-in distributed object store using shared memory, and high-level libraries for training (Ray Train), serving (Ray Serve), hyperparameter tuning (Ray Tune), and reinforcement learning (RLlib). OpenAI uses it to coordinate ChatGPT training. It scales from a single laptop to thousands of GPUs with the same code. The key strength is that Ray can orchestrate heterogeneous compute — mixing CPU and GPU nodes in the same pipeline.

**Dask** is Python-native and lighter weight. It mirrors the NumPy/Pandas/Scikit-learn APIs, making it a drop-in replacement for scaling existing data science code. It's ideal when your problem is "my DataFrame doesn't fit in memory" or "I need to parallelise this across cores/machines." Dask can also run on top of Ray via `dask_on_ray`.

**Apache Spark** remains dominant for large-scale ETL and data pipelines but is heavier-weight and JVM-based. Less relevant at individual scale.

For agent orchestration, RAG pipelines, and batch inference — Ray is probably the most natural fit, especially given its inference serving capabilities.

## Distributed Memory

This is a less distinct category but worth touching on:

**Redis** (and its forks like **Valkey** since the licence change) provides distributed in-memory key-value storage with clustering support. **Dragonfly** is a modern Redis-compatible drop-in replacement that's significantly faster on multi-core machines — worth considering as a cache layer.

**Apache Arrow Flight** enables zero-copy sharing of columnar data across processes and nodes, which is relevant if you're moving tensors or embeddings between services.

Ray's own distributed object store uses shared memory with zero-copy local reads, which handles inter-process data sharing well within a Ray cluster.

## Distributed GPU and LLM Inference

This is where the small-scale/individual angle gets genuinely exciting. There are several layers:

### Enterprise and Cloud-Scale Frameworks

**NVIDIA Dynamo** was released at GTC 2025 as an open-source inference serving framework for deploying generative AI models in large-scale distributed environments. It supports disaggregated serving — separating prefill and decode phases onto distinct GPU devices — and works with vLLM, SGLang, and TensorRT-LLM.

**llm-d** is a Kubernetes-native distributed inference stack, founded by Google Cloud alongside Red Hat, IBM, NVIDIA, and CoreWeave. It builds on vLLM's engine, adding a vLLM-aware inference scheduler, disaggregated serving, and multi-tier KV cache. Early tests showed 2x improvements in time-to-first-token for code completion workloads.

These are powerful but designed for production clusters, not homelabs.

### The Peer-to-Peer Consumer Hardware Frontier

**Exo** (ExoLabs) takes a fundamentally different approach: instead of running a model on one device, it splits the model across multiple devices connected peer-to-peer. The Exo framework (42.7k GitHub stars) uses peer-to-peer topology with automatic device discovery and dynamic model partitioning. The founder demonstrated 671B parameter models running across Mac Mini clusters. Exo uses UDP broadcast for zero-configuration peer discovery — nodes announce themselves every 2.5 seconds. It scores nodes based on available memory, compute TFLOPS, and latency to peers, then partitions model layers accordingly. The inference backends are MLX for Apple Silicon and Tinygrad for CUDA/ROCm/CPU.

This is particularly interesting because you could theoretically combine a Beelink SER8 with any other machines you have lying around to run larger models than any single device could handle. The catch is that inter-node bandwidth becomes the bottleneck — model parallelism across a network is fundamentally latency-limited compared to a single machine with enough VRAM.

**Petals** is a system for inference and fine-tuning of large models collaboratively by joining the resources of multiple parties. It demonstrated running inference of BLOOM-176B on consumer GPUs at roughly 1 step per second, which is enough for many interactive LLM applications. Petals uses a BitTorrent-style protocol where each server hosts a subset of transformer blocks. It currently supports distributed Llama 3.1 (up to 405B), Mixtral (8x22B), Falcon (40B+), and BLOOM (176B). The client runs locally (even on CPU) and relies on the swarm to execute transformer blocks.

**Parallax** is a newer research project that improves on Petals with a two-phase scheduling algorithm that adapts to each GPU's compute power and interconnected network bandwidth, addressing Petals' limitation of being bottlenecked by the slowest participant.

### The Practical Reality at Individual Scale

For a specific situation — a Beelink SER8 with 64GB DDR5, running Devstral Small 2 and Qwen3-Coder 30B-A3B — the honest assessment is:

**Single-node inference via Ollama/llama.cpp is still the path of least resistance.** llama.cpp (98.6k GitHub stars) is the C/C++ inference engine underneath Ollama, LM Studio, GPT4All, and KoboldCpp. The ggml/llama.cpp team joined Hugging Face in February 2026. For MoE models like Qwen3 30B-A3B, which only activate ~3B parameters per token, a single 64GB DDR5 machine should handle inference comfortably.

**Exo becomes interesting when you want to run models that exceed a single node's capacity** — say you wanted to run full DeepSeek V3 (671B total) for experimentation. You'd cluster your Beelink with other machines and Exo would partition the layers. But for most planned models, this is overkill.

**Petals is most useful as a public swarm** — contributing your GPU to (and drawing from) a collective pool. Less applicable for private/sovereign inference.

**Ray Serve is the right layer if you want to build a proper inference service** that integrates with an agent pipeline — it handles request routing, batching, model scaling, and can sit in front of vLLM or Ollama as the inference backend.

<details>
<summary>Technology Comparison Matrix</summary>

| Technology | Category | Best For | Complexity | Scale |
|------------|----------|----------|------------|-------|
| GlusterFS | Storage | Simple file replication | Low | Small-medium |
| Ceph | Storage | Unified object/block/file | High | Medium-large |
| MinIO | Storage | S3-compatible blob storage | Low | Small |
| Longhorn | Storage | K8s persistent volumes | Medium | Small-medium |
| Ray | Compute | ML orchestration + serving | Medium | Any |
| Dask | Compute | DataFrame parallelism | Low | Small-medium |
| Spark | Compute | Large-scale ETL | High | Large |
| Redis/Valkey | Memory | Distributed caching | Low | Any |
| Dragonfly | Memory | High-perf Redis replacement | Low | Small-medium |
| Exo | LLM Inference | P2P model splitting | Low | Small |
| Petals | LLM Inference | Collaborative swarm inference | Low | Distributed |
| NVIDIA Dynamo | LLM Inference | Enterprise disaggregated serving | High | Large |
| llm-d | LLM Inference | K8s-native inference | High | Large |
| llama.cpp/Ollama | LLM Inference | Single-node inference | Low | Individual |

</details>

<details>
<summary>Key Links and Resources</summary>

- [Exo GitHub](https://github.com/exo-explore/exo) - Peer-to-peer AI inference (42.7k stars)
- [Petals GitHub](https://github.com/bigscience-workshop/petals) - Collaborative inference
- [llama.cpp GitHub](https://github.com/ggerganov/llama.cpp) - C/C++ LLM inference (98.6k stars)
- [Ray Framework](https://ray.io/) - Distributed compute for AI
- [MinIO](https://min.io/) - S3-compatible object storage
- [Ceph](https://ceph.io/) - Unified distributed storage
- [GlusterFS](https://www.gluster.org/) - Scale-out filesystem
- [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo) - Enterprise inference serving

</details>

The bottom line: at individual scale, the biggest practical gains right now come from MoE model architectures (which give you big-model quality with small-model inference costs) running on single nodes via llama.cpp/Ollama, rather than from distributing inference across nodes. The network overhead of multi-node inference only pays off when models genuinely exceed what one machine can hold. But Exo is the project to watch if you ever want to cluster consumer hardware together — it's the closest thing to "just plug in another box and it works."

**Tags**: distributed-systems, llm-inference, homelab, ai-infrastructure, exo, ray, ceph
**Categories**: AI Automation, Infrastructure