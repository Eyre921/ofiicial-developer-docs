---
title: "Compatible models"
source: https://docs.fireworks.ai/fine-tuning/models
path: fine-tuning/models
---

Base models supported for fine-tuning on Fireworks, with Serverless and Dedicated Training availability and supported methods per model.

Serverless and Dedicated Training draw from the same base model catalog. Availability is set per model, by parameter mode (LoRA or full-parameter) and method (SFT, DPO, and RL).

> [!NOTE]
>
> Muse Glimmer 30B SFT is free to train until November 30, 2026.\
> [Start here](/fine-tuning/finetuning-intro#quickstart)

## Model availability

Use **Compare models** to see every model in one table, or select a row to see that model's details. **Model details** shows where you can train the model, which methods the model supports, and which training shapes back the model. The filters apply to both views.

## Vision and multimodal support

Vision support is model- and surface-specific. Use the catalog above to confirm that the selected VLM has a compatible Training API shape before preparing data.

* VLM SFT dataset schema: [Cookbook: SFT vision datasets](/fine-tuning/training-api/cookbook/sft#vision-datasets)
* Training API VLM loops: start from a VLM-compatible shape and the same cookbook SFT, DPO, or RL recipe used for text, replacing the text tokenizer with the model processor
* Inference request formats after deployment: [Vision-language models](/guides/querying-vision-language-models)

## Next steps

> [card] [Serverless Training](/fine-tuning/training-api/serverless)
>
> Train on shared pooled infrastructure with per-token billing

> [card] [Training Shapes](/fine-tuning/training-api/training-shapes)
>
> What a shape pins and how to reference one

> [card] [Dedicated Training](/fine-tuning/training-api/dedicated)
>
> Provision a trainer and sampler on reserved GPU capacity

> [card] [Pricing](https://fireworks.ai/pricing)
>
> Current rates across training and inference
