---
title: "Nexus model guidance"
source: https://docs.pinecone.io/guides/nexus/models
path: guides/nexus/models
---

Learn how Pinecone Nexus uses models for generation, curation, and retrieval, and how to choose the right one.

Pinecone Nexus uses models at several points, and you choose them based on your deployment. You bring your own models in BYOC, or use a Pinecone-managed catalog during the invite-only trial. Everything on this page applies to both.

## Model roles

* **Generation** composes the answer to a query, using a generation model from the catalog.
* **Curation** builds artifacts from your sources, using your configured models (covered below).
* **Embedding and rerank** power retrieval, using Pinecone-hosted models by default.

All are configurable through the model catalog, which is backed by [LiteLLM](https://docs.litellm.ai/docs/providers) and references each model by its `provider/model` identifier. In BYOC, you supply the keys, so see [Deploy Nexus BYOC](/guides/nexus/byoc/deploy).

## Default models

Each chat model call belongs to a work area, and each work area has a default model:

* **Query** answers queries, and also runs Optimize.
* **Curation** builds artifacts from your sources.
* **System** runs background workflows, such as Explore.

A call that doesn't name a model runs on its work area's default, so generation runs on the Query default unless a query names a model.

> [!NOTE]
>
> In the invite-only Nexus trial, Pinecone sets the defaults from its managed catalog:
>
> * **Query**: Claude Sonnet 5
> * **Curation**: Gemini 3.5 Flash Lite
> * **System**: Claude Sonnet 5

## Choose a model per query

A query can run on any model enabled for Query instead of the default. In a context's **Query** tab, the model selector lists those models. In the API, name a model by its catalog ID in the query's `model` field. `GET /models` lists the catalog IDs and the current defaults.

Match the model to the question rather than the size of the context. A cheaper, faster model suits simple or high-volume queries, and the most capable model suits complex, multi-step reasoning. The query [trace](/guides/nexus/query-tracing) reports the tokens and latency behind each answer, so you can compare models on your own questions and settle on the one that fits.

## Curation models

Curation runs your embedding model and the Curation default across your sources to build artifacts. Because it processes every source, curation is the most cost-sensitive step, so choose the Curation default with cost in mind. See [Data flows and residency](/guides/nexus/byoc/reference#data-flows-and-residency) for what content each model sees.

## Configure models in BYOC

In your own deployment, you configure the models yourself. You choose the default model for each work area, and the shipped catalog uses Google Gemini. You can bring any model a LiteLLM-supported provider offers, and point generation, embedding, or rerank at a different provider or an endpoint inside your own boundary, each with its own key. A chat model must support the OpenAI `tools` and `response_format` parameters, because Nexus relies on both. Align to your cloud provider where it helps:

* **Azure** deployments typically use Azure OpenAI or AI Foundry models.
* **AWS** deployments typically use Amazon Bedrock models.

You don't have to stay within one provider. Because the available models depend on your deployment and the keys you provide, model selection for BYOC happens with Pinecone during setup rather than from a fixed published list.

### Bedrock on AWS

Bedrock models don't need a key. A Bedrock model can sign its calls with the inference proxy's own AWS identity, an IAM role attached to the proxy's Kubernetes service account, so no long-lived AWS secret sits in your model configuration. This role is attached during BYOC setup and needs `bedrock:InvokeModel*` for generation and embedding models and `bedrock:Rerank` for rerank models.

Name a Bedrock rerank model by its full foundation-model ARN, for example `bedrock/arn:aws:bedrock:<region>::foundation-model/cohere.rerank-v3-5:0`.

### Set default models

Your model catalog sets the default model for each work area in `phase_defaults`. On the **Deployment** tab of the console's **Settings** page, the **Default models** card shows these defaults read-only, because the catalog reapplies them on every settings pull. To change a default, edit the catalog and redeploy. A default must be a model that's enabled for its work area, which the **Models** list shows for each model. Usage reports spend by stage, and calls on the System model appear under the `system` stage.
