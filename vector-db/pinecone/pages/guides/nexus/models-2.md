---
title: "Nexus model guidance"
source: https://docs.pinecone.io/guides/nexus/models
path: guides/nexus/models
---

Learn how Pinecone Nexus uses models for generation, curation, and retrieval, and how to choose the right one.

Pinecone Nexus uses models at several points, which you select based on your deployment: You bring your own models in BYOC, or use a Pinecone-managed catalog during the invite-only trial. Everything on this page applies to both.

## Where Nexus uses models

* **Generation** composes the answer to a query, using a generation model from the catalog.
* **Curation** builds artifacts from your sources, using your configured models (covered below).
* **Embedding and rerank** power retrieval, using Pinecone-hosted models by default.

All are configurable through the model catalog, which is backed by [LiteLLM](https://docs.litellm.ai/docs/providers) and references each model by its `provider/model` identifier. In BYOC, you supply the keys, so see [Deploy Nexus BYOC](/guides/nexus/byoc/deploy).

## Model tiers

Nexus groups generation models into three tiers. Start with the default and adjust from there, matching the tier to the question rather than the size of the context:

* **Standard** is the default, balanced choice. Use it when you're unsure.
* **Light** is cheaper and faster. Reach for it on simple or high-volume queries where speed and cost matter most.
* **Pro** is the most capable. Use it for complex, multi-step reasoning.

The tiers are suggested defaults, not the whole catalog. In a context's **Query** tab, the model selector marks one suggested model per tier. Choose a tier to use its suggestion, or select any other model in the catalog instead. The query [trace](/guides/nexus/query-tracing) reports the tokens, latency, and cost behind each answer, so you can compare models on your own questions and settle on the one that fits.

<Note>
  In the invite-only Nexus trial, Pinecone fills the tiers from its managed catalog:

  * **Standard**: Claude Sonnet 5
  * **Light**: Gemini 3.5 Flash Lite
  * **Pro**: Claude Opus 5
</Note>

## Curation models

Curation runs your configured embedding and generation models across your sources to build artifacts, the same models a query uses. Because it processes every source, curation is the most cost-sensitive step, so weigh curation cost when you choose your generation model. See [Data flows and residency](/guides/nexus/byoc/reference#data-flows-and-residency) for what content each model sees.

## Configure models in BYOC

In your own deployment, you configure the models yourself. You assign your own model to each tier, and generation defaults to Google Gemini. You can bring any model a LiteLLM-supported provider offers, and point generation, embedding, or rerank at a different provider or an endpoint inside your own boundary, each with its own key. Align to your cloud provider where it helps:

* **Azure** deployments typically use Azure OpenAI or AI Foundry models.
* **AWS** deployments typically use Amazon Bedrock models.

You don't have to stay within one provider. Because the available models depend on your deployment and the keys you provide, model selection for BYOC happens with Pinecone during setup rather than from a fixed published list.
