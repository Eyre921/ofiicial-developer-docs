---
title: "Are there extra fees for serving trained models?"
source: https://docs.fireworks.ai/faq-new/billing-pricing/are-there-extra-fees-for-serving-fine-tuned-models
path: faq-new/billing-pricing/are-there-extra-fees-for-serving-fine-tuned-models
---

Trained (LoRA) models require a dedicated deployment to serve. Here's what you need to know:

**What you pay for**:

* **Deployment costs** on a per-GPU-second basis for hosting the model
* **The training process** itself, if applicable

**Deployment options**:

* **Live-merge deployment**: Deploy your LoRA model with weights merged into the base model for optimal performance
* **Multi-LoRA deployment**: Deploy up to 100 LoRA models as addons on a single base model deployment

<Tip>
  For more details on deploying trained models, see the [Deploying Trained Models guide](/fine-tuning/deploying-loras).
</Tip>
