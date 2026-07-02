---
title: "Understanding LoRA performance"
source: https://docs.fireworks.ai/guides/understanding_lora_performance
path: guides/understanding_lora_performance
---

Understand the performance impact of LoRA fine-tuning, optimization strategies, and deployment considerations.

# Why is my LoRA slower than base model inference?

This guide explores why LoRA (Low-Rank Adaptation) fine-tuned models can exhibit slower inference times compared to base models, addresses key factors affecting performance, and provides actionable advice on optimizing deployments. It also delves into the implications of concurrent LoRA adapters and when to merge weights versus serving multiple adapters.

## Key concepts and definitions

* **LoRA (Low-Rank Adaptation)**: A fine-tuning technique that updates weights of the large model by approximating the delta as a product of two low-rank ("narrow") matrices.
* **PEFT (Parameter-Efficient Fine-Tuning)**: A set of approaches for model adaptation that change only part of the model and thus can be trained and served more efficiently. LoRA is the most popular technique in PEFT family.
* **Weight Merging**: Combining LoRA-tuned weights with the base model to create a standalone model.
* **Speculative Decoding (SD)**: An optimization technique using a smaller "draft" model to precompute and speed up text generation.

## Q\&A: Addressing common questions

### Q1: Why is the LoRA fine-tuned model slower than the base model?

Three factors contribute to the observed slowdown:

1. **Unmerged LoRA weights**: Serving LoRA adapters dynamically adds computational overhead during inference. Merging weights removes this overhead.
2. **Speculative decoding**: Base models often use speculative decoding to optimize generation speed. Without SD, LoRA fine-tuned models can lag behind.

### Q2: Does the number of concurrent LoRA adapters affect performance?

1. TTFT increase - any request against an unmerged LoRA model has some initial overhead for loading model weights (on the order of tens of milliseconds) and increases the prompt processing time by about 10-30%. This manifests as increased time to first token. Repeated requests might amortize some of these overheads.

2. Generation speed overheads for unmerged LoRA models increase with higher request concurrency. For a deployment serving a few requests per second, the overhead might be minimal, but relative overhead increases with a higher level of load. As a corollary, on-demand deployments with LoRA adapters have lower maximum throughput.

3. Performance is mostly independent of the total number of LoRA adapters deployed at a single deployment.

### Q3: How can performance be improved?

To address latency issues and optimize performance:

1. **Weight merging (live merge)**:
   * Deploy your LoRA model with live merge, which automatically merges LoRA weights at deployment time to eliminate runtime overhead.
2. **Speculative decoding**:
   * Utilize speculative decoding for fine-tuned models with a custom draft model. This can achieve better-than-base performance.

### Q4: When should I merge weights vs. serve multiple LoRA adapters?

| **Scenario**             | **Multi-LoRA (Unmerged)**            | **Merged LoRA**                       |
| ------------------------ | ------------------------------------ | ------------------------------------- |
| **Use case**             | Serving multiple fine-tuned variants | Low-latency, single-model deployments |
| **Hardware needs**       | Shared or dedicated hardware         | Dedicated hardware                    |
| **Performance impact**   | Overhead per adapter                 | Equivalent to base model              |
| **Concurrency handling** | Efficient for experimentation        | Limited to one fine-tuned model       |

### Q5: What is the performance impact of weight merging?

Merging weights creates a new standalone model indistinguishable from a fully fine-tuned model. Once merged:

* Latency matches the base model.
* Memory usage is reduced since adapters are no longer dynamically applied.

### Q6: What does it take for fine-tuning to match the performance of the base deployment?

To match or exceed base model performance, consider these steps:

1. **Speculative decoding**:
   * Train a custom draft model optimized for your fine-tuned setup.
2. **Weight merging**:
   * Merge LoRA weights to eliminate inference overhead.

## Implementation guide for optimizing LoRA performance

### Steps to improve performance

1. **Fine-Tune with LoRA**:
   * Use LoRA for efficient parameter updates. See our guide on [uploading custom models](https://docs.fireworks.ai/models/uploading-custom-models) for more information.
2. **Deploy with live merge**:
   * Deploy your LoRA fine-tuned model directly with live merge, which automatically merges LoRA weights at deployment time. See the [deploying LoRAs guide](/fine-tuning/deploying-loras) for details.
3. **Deploy on dedicated hardware**:
   * Deploy merged models for consistent low-latency performance, [like in this guide](https://docs.fireworks.ai/guides/ondemand-deployments).
4. **Use speculative decoding**:
   * Train and deploy a draft model to further reduce latency.
     <Info>This is currently an enterprise feature, please reach out for more information. </Info>
