---
title: "FLUX image generation"
source: https://docs.fireworks.ai/faq-new/models-inference/flux-image-generation
path: faq-new/models-inference/flux-image-generation
---

## Can I generate multiple images in a single API call?

No, FLUX serverless supports only one image per API call. For multiple images, send separate parallel requests—these will be automatically load-balanced across our replicas for optimal performance.

## Does FLUX support image-to-image generation?

No, image-to-image generation is not currently supported. We are evaluating this feature for future implementation. If you have specific use cases, please share them with our support team to help inform development.

## Can I create custom LoRA models with FLUX?

Inference on FLUX-LoRA adapters is currently supported. However, managed training on Fireworks with FLUX is not, although this feature is under development. Updates about our managed LoRA training service will be announced when available.
