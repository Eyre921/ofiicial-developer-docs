---
title: "Managed Training Overview"
source: https://docs.fireworks.ai/fine-tuning/managed-finetuning-intro
path: fine-tuning/managed-finetuning-intro
---

Train models with Fireworks-managed infrastructure — no custom code required.

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
  <Card title="Supervised Fine-Tuning" href="/fine-tuning/fine-tuning-models" icon="message">
    Train text and vision models with labeled examples of desired outputs
  </Card>

  <Card title="Preference Optimization (DPO / ORPO)" href="/fine-tuning/dpo-fine-tuning" icon="arrows-left-right">
    Train on preferred and non-preferred response pairs using DPO or ORPO
  </Card>

  <Card title="Reinforcement Fine-Tuning" href="/fine-tuning/reinforcement-fine-tuning-models" icon="brain">
    Train models using custom reward functions for complex reasoning tasks
  </Card>
</CardGroup>

## Supported base models

Fireworks supports training for major open source model families, including DeepSeek, Qwen, Kimi, Gemma, GLM, and Llama. Eligibility is decided per model and per method: a model can support SFT without supporting DPO or RFT.

[**Models**](/fine-tuning/models) is the live per-model matrix: the surfaces and methods each base model is enabled for, the training shapes behind it, and each shape's maximum context length. Check it before creating a job, and set the job context from a shape that supports the method you picked, using `firectl sftj create`, `firectl dpo-job create`, or the corresponding RFT command.

Custom models uploaded by users are not automatically tunable. To use managed training with an uploaded custom base model, the model must have a corresponding Hugging Face URL. Fireworks uses that URL to infer the training renderer and locate compatible training shapes. A custom model is supported only when Fireworks can resolve both a supported renderer and at least one compatible training shape. After the Hugging Face URL is set, tunability is refreshed by a background operation that runs about every 30 minutes, so the model may take up to 30 minutes to show as `Tunable: true`. We are working to make this refresh faster.

To browse the broader catalog (including non-tunable inference models), visit the [Model Library for text models](https://app.fireworks.ai/models?filter=LLM\&tunable=true) or [vision models](https://app.fireworks.ai/models?filter=vision\&tunable=true).

## Tuning modes and context length

Managed training runs **[Low-Rank Adaptation (LoRA)](https://arxiv.org/abs/2106.09685)** only. It supports the full context lengths exposed by the available training shapes, matching the same long-context capabilities used by cookbook recipes.

LoRA gives you efficient adapter training and flexible deployment, including [multiple LoRAs](/fine-tuning/deploying-loras#multi-lora-deployment) on a single base model deployment. For full-parameter tuning, use the [Training API](/fine-tuning/training-api/introduction).

<Warning>
  **Deprecation notice:** The `deployedModel` request key for routing to LoRA addons is deprecated and will not be supported for any new deployments. Please migrate to the `model` field with the `<model_name>#<deployment_name>` format described in [Routing requests to LoRA addons](/fine-tuning/deploying-loras#multi-lora-deployment).
</Warning>
