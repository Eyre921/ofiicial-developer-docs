---
title: "What is the difference between serverless and on-demand?"
source: https://docs.fireworks.ai/faq-new/models-inference/what-is-the-difference-between-serverless-and-on-demand
path: faq-new/models-inference/what-is-the-difference-between-serverless-and-on-demand
---

Serverless is pay-per-token inference on shared Fireworks capacity. On-demand is a deployment on GPUs reserved for your account.

**Serverless** is shared inference. You send a request to `api.fireworks.ai` and pay per token. You do not choose the GPU or the replica count. Use it for models Fireworks already hosts.

**On-demand** is a deployment on GPUs reserved for your account. You pay for GPU time, and you choose the model, hardware, and scaling. Use it for a custom model, a LoRA adapter, or a latency target Serverless does not meet. Docs also call this a dedicated deployment.

The comparison table is on [Serverless overview](/serverless/overview#serverless-vs-on-demand). To start, use the [Serverless quickstart](/getting-started/quickstart) or the [on-demand quickstart](/getting-started/ondemand-quickstart).
