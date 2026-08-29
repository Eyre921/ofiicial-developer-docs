---
title: "Models"
source: https://docs.fireworks.ai/fine-tuning/models
path: fine-tuning/models
---

Which base models you can train on Fireworks and the surfaces each one is available on.

Managed training, the Training API, and serverless training all draw from the same base model catalog, but availability is decided per model: managed jobs by method (SFT, DPO, RFT), Training API jobs by parameter mode (LoRA or full-parameter).

## Model availability

Pick a model to see the surfaces and methods it is enabled for, plus any training shapes that back it. Switch to **All models** for the full matrix.

<ModelsCatalog />

## Vision and multimodal support

Vision support is model- and surface-specific. Use the catalog above to confirm that the selected VLM has a compatible managed method or Training API shape before preparing data.

* Managed VLM SFT dataset schema and launch flow: [Supervised Fine-Tuning: Vision](/fine-tuning/fine-tuning-models#vision-training)
* Training API VLM loops: start from a VLM-compatible shape and the same cookbook SFT, DPO, or RL recipe used for text, replacing the text tokenizer with the model processor
* Inference request formats after deployment: [Vision-language models](/guides/querying-vision-language-models)

## Next steps

<CardGroup>
  <Card title="Managed Training" href="/fine-tuning/managed-finetuning-intro" icon="wand-magic-sparkles">
    Hand Fireworks your data and let the platform run the job
  </Card>

  <Card title="Training API" href="/fine-tuning/training-api/introduction" icon="code">
    Write your own training loop against a Tinker-compatible API
  </Card>

  <Card title="Serverless Models" href="/fine-tuning/training-api/serverless#models" icon="bolt">
    Serverless Training API model catalog with per-token pricing
  </Card>

  <Card title="Training Shapes" href="/fine-tuning/training-api/training-shapes" icon="microchip">
    What a shape pins and how to reference one
  </Card>

  <Card title="Dedicated Training" href="/fine-tuning/training-api/dedicated" icon="server">
    Provision a trainer and sampler on reserved GPU capacity
  </Card>

  <Card title="Pricing" href="https://fireworks.ai/pricing" icon="tag">
    Current rates across training and inference
  </Card>
</CardGroup>
