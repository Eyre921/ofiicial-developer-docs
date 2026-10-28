---
title: "Models"
source: https://docs.fireworks.ai/fine-tuning/models
path: fine-tuning/models
---

Base models supported for fine-tuning on Fireworks, with per-model training surfaces (managed, Training API, serverless, dedicated) and method availability.

Managed training, the Training API, and serverless training all draw from the same base model catalog, but availability is decided per model: managed jobs by method (SFT and DPO), Training API jobs by parameter mode (LoRA or full-parameter) and method (SFT, DPO, and RL).

> [!NOTE]
>
> Muse Glimmer 30B SFT is free to train until 11/30.\
> No credit card required. [Start here](https://app.fireworks.ai/dashboard/fine-tuning/create?type=supervised\&baseModel=accounts/fireworks/models/muse-glimmer-30b)

## Model availability

Pick a model to see the surfaces and methods it is enabled for, plus any training shapes that back it. Switch to **All models** for the full matrix.

## Vision and multimodal support

Vision support is model- and surface-specific. Use the catalog above to confirm that the selected VLM has a compatible managed method or Training API shape before preparing data.

* Managed VLM SFT dataset schema and launch flow: [Supervised Fine-Tuning: Vision](/fine-tuning/fine-tuning-models#vision-training)
* Training API VLM loops: start from a VLM-compatible shape and the same cookbook SFT, DPO, or RL recipe used for text, replacing the text tokenizer with the model processor
* Inference request formats after deployment: [Vision-language models](/guides/querying-vision-language-models)

## Next steps

> **[Managed Training](/fine-tuning/managed-finetuning-intro)**
>
> Hand Fireworks your data and let the platform run the job

> **[Training API](/fine-tuning/training-api/introduction)**
>
> Write your own training loop against a Tinker-compatible API

> **[Serverless Training](/fine-tuning/training-api/serverless)**
>
> Train on shared pooled infrastructure with per-token billing

> **[Training Shapes](/fine-tuning/training-api/training-shapes)**
>
> What a shape pins and how to reference one

> **[Dedicated Training](/fine-tuning/training-api/dedicated)**
>
> Provision a trainer and sampler on reserved GPU capacity

> **[Pricing](https://fireworks.ai/pricing)**
>
> Current rates across training and inference
