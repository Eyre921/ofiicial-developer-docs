---
title: "Managed Fine-Tuning Overview"
source: https://docs.fireworks.ai/fine-tuning/managed-finetuning-intro
path: fine-tuning/managed-finetuning-intro
---

Fine-tune models with Fireworks-managed infrastructure — no custom code required.

Give Fireworks your data and configuration. The platform handles scheduling, training, checkpointing, and model output. Training data uses the **OpenAI-compatible chat completion format**, so existing OpenAI SFT datasets work with no conversion required.

## How to launch managed training

These interfaces create the same underlying managed jobs:

| Interface        | Use when                                                         |
| ---------------- | ---------------------------------------------------------------- |
| **Fireworks UI** | You want guided configuration and visual monitoring              |
| **CLI or API**   | You want scripted and reproducible job operations                |
| **Your agent**   | You want help configuring, running, and troubleshooting training |

The Fireworks CLI is called `firectl`. [Install the training skill](/fine-tuning/agent/use-with-coding-agents) to use your agent, or continue with the method-specific managed guides below. For custom Python training loops, start with the [Training API overview](/fine-tuning/training-api/introduction).

## Methods

<CardGroup>
  <Card title="Supervised Fine Tuning - Text" href="/fine-tuning/fine-tuning-models" icon="message">
    Train text models with labeled examples of desired outputs
  </Card>

  <Card title="Supervised Fine Tuning - Vision" href="/fine-tuning/fine-tuning-vlm" icon="eye">
    Train vision-language models with image and text pairs
  </Card>

  <Card title="Preference Optimization (DPO / ORPO)" href="/fine-tuning/dpo-fine-tuning" icon="arrows-left-right">
    Train on preferred and non-preferred response pairs using DPO or ORPO
  </Card>

  <Card title="Reinforcement Fine Tuning" href="/fine-tuning/reinforcement-fine-tuning-models" icon="brain">
    Train models using custom reward functions for complex reasoning tasks
  </Card>
</CardGroup>

## Free Reinforcement Fine-Tuning

<Tip>
  **Reinforcement Fine-Tuning (RFT)** is free for models under 16B parameters. When creating an RFT job in the UI, filter for free tuning models in the model selection area on the [fine-tuning creation page](https://app.fireworks.ai/dashboard/fine-tuning/create). If kicking off jobs from the terminal, you can find the model ID from the [Model Library](https://app.fireworks.ai/models?filter=LLM\&tunable=true). Note: SFT and DPO jobs are billed per training token for all model sizes—see the [pricing page](https://fireworks.ai/pricing) for details.
</Tip>

When creating a **Reinforcement Fine-Tuning** job in the UI, look for the "Free tuning" filter in the model selection area:

<img alt="Free tuning filter in the model selection area" />

For SFT and DPO pricing, see the [pricing page](https://fireworks.ai/pricing).

## Supported base models

Fireworks supports fine-tuning for major open source model families, including DeepSeek, Qwen, Kimi, Gemma, GLM, and Llama. Eligibility is method and parameter-mode specific: a model can support SFT without supporting DPO, RFT, LoRA, or full-parameter training on the same shapes. Use the live [Training Shapes](/fine-tuning/training-api/training-shapes) method-support matrix before creating a job.

Custom models uploaded by users are not automatically tunable. To use managed fine-tuning with an uploaded custom base model, the model must have a corresponding Hugging Face URL. Fireworks uses that URL to infer the training renderer and locate compatible training shapes. A custom model is supported only when Fireworks can resolve both a supported renderer and at least one compatible training shape. After the Hugging Face URL is set, tunability is refreshed by a background operation that runs about every 30 minutes, so the model may take up to 30 minutes to show as `Tunable: true`. We are working to make this refresh faster.

The table below is generated from the live training shape registry. The "Max supported context length" is a catalog-level model maximum. For a job, use the maximum context of a shape that supports the selected method and tuning mode. Set it with `firectl sftj create`, `firectl dpo-job create`, or the corresponding RFT command.

| Base model                      | Max supported context length |
| ------------------------------- | ---------------------------- |
| `gemma-4-26b-a4b-it`            | 256K (262,144 tokens)        |
| `gemma-4-31b-it`                | 256K (262,144 tokens)        |
| `glm-5p1`                       | 200K (200,000 tokens)        |
| `kimi-k2p5`                     | 256K (262,144 tokens)        |
| `kimi-k2p6`                     | 256K (262,144 tokens)        |
| `llama-v3p3-70b-instruct`       | 128K (131,072 tokens)        |
| `minimax-m2p5`                  | 192K (196,608 tokens)        |
| `nemotron-nano-3-30b-a3b`       | 256K (262,144 tokens)        |
| `qwen3-235b-a22b-instruct-2507` | 128K (128,000 tokens)        |
| `qwen3-30b-a3b`                 | 128K (131,072 tokens)        |
| `qwen3-30b-a3b-instruct-2507`   | 128K (128,000 tokens)        |
| `qwen3-32b`                     | 128K (131,072 tokens)        |
| `qwen3-4b`                      | 64K (65,536 tokens)          |
| `qwen3-8b`                      | 256K (256,000 tokens)        |
| `qwen3-vl-8b-instruct`          | 256K (262,144 tokens)        |
| `qwen3p5-27b`                   | 256K (262,144 tokens)        |
| `qwen3p5-35b-a3b`               | 256K (262,144 tokens)        |
| `qwen3p5-397b-a17b`             | 256K (262,144 tokens)        |
| `qwen3p5-9b`                    | 256K (262,144 tokens)        |
| `qwen3p6-27b`                   | 256K (262,144 tokens)        |

To browse the broader catalog (including non-tunable inference models), visit the [Model Library for text models](https://app.fireworks.ai/models?filter=LLM\&tunable=true) or [vision models](https://app.fireworks.ai/models?filter=vision\&tunable=true).

## Tuning modes and context length

Managed fine-tuning supports both **[Low-Rank Adaptation (LoRA)](https://arxiv.org/abs/2106.09685)** and full-parameter tuning, depending on the model, method, and selected training shape. It also supports the full context lengths exposed by the available training shapes, matching the same long-context capabilities used by cookbook recipes.

Choose LoRA when you want efficient adapter training and flexible deployment, including [multiple LoRAs](/fine-tuning/deploying-loras#multi-lora-deployment) on a single base model deployment. Choose full-parameter tuning when you need to update all model weights for difficult reasoning, alignment, or domain adaptation tasks.

<Warning>
  **Deprecation notice:** The `deployedModel` request key for routing to LoRA addons is deprecated and will not be supported for any new deployments. Please migrate to the `model` field with the `<model_name>#<deployment_name>` format described in [Routing requests to LoRA addons](/fine-tuning/deploying-loras#routing-requests-to-lora-addons).
</Warning>
