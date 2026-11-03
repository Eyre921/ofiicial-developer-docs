---
title: "Fireworks AI with Nexus BYOC"
source: https://docs.pinecone.io/guides/nexus/byoc/fireworks/overview
path: guides/nexus/byoc/fireworks/overview
---

Learn how Fireworks AI open models fit into a Nexus BYOC deployment and why you'd use them for generation and curation.

> [!NOTE]
>
> Nexus BYOC is available only on [Enterprise plans](https://www.pinecone.io/pricing/).

[Fireworks AI](https://fireworks.ai/) is an inference and training platform for open models, including Kimi, DeepSeek, GLM, Qwen, MiniMax, and gpt-oss. In a Pinecone Nexus Bring Your Own Cloud (BYOC) deployment, you can serve Nexus's chat models, and optionally its embedding model, from Fireworks instead of the Google Gemini models the shipped catalog uses.

## Fireworks AI features

* **Serverless inference:** Call models on shared capacity and pay per token.
* **Dedicated deployments:** Reserve capacity for a model when you need predictable throughput.
* **Fine-tuning:** Tune a model on your own data and serve the tuned model from the same platform.

## Nexus integration

Nexus uses models at several points, which [Nexus model guidance](/guides/nexus/models) describes. In BYOC, the inference proxy routes every model call according to your model catalog, `inference-proxy-models.toml`. Each catalog entry names an upstream model, the endpoint that serves it, and the secret that holds its API key. Fireworks exposes an OpenAI-compatible endpoint, so a Fireworks model is a catalog entry with `api_style = "openai"` pointed at that endpoint.

Once Fireworks models are in the catalog, they behave like any other model:

* **Work-area defaults:** The catalog's `phase_defaults` assigns a default model to each work area (Query, Curation, and System). A call that names no model runs on its work area's default.
* **Per-query selection:** A query can name any enabled model by its catalog ID, and the model selector on a context's **Query** tab lists every model enabled for Query.
* **Embeddings:** You can optionally route the default embedding model to Fireworks. The setup guide keeps reranking on a Pinecone-hosted model.

## Benefits

* **Lower curation cost:** Curation runs a model across every source, which makes it the most cost-sensitive step in Nexus. A fast open model as the Curation default keeps that cost down as your corpus grows.
* **Open models for every work area:** You can run Query, Curation, and System on open models, and compare them against closed models on your own questions.
* **Fine-tuned models:** You can fine-tune a model on Fireworks and serve it to Nexus by adding it to your catalog.

## Key concepts

| Concept | Fireworks AI | Nexus BYOC |
| - | - | - |
| Model | A model path, such as `accounts/fireworks/models/kimi-k3`. | A catalog entry under `[llm_models.<id>]` or `[embedding_models.<id>]`, referenced by its catalog ID. |
| Endpoint | The OpenAI-compatible endpoint, `https://api.fireworks.ai/inference/v1`. | The `base_url` on the catalog entry. |
| API key | The key that authenticates each request. | The `nexus-provider-keys.<ref>` stack secret that the entry's `api_key_ref` names. |
| Generation | Serves the chat model that composes each answer. | The Query default, or the model a query names. |
| Curation | Serves the chat model that reads sources and builds artifacts. | The Curation default. |
| Embeddings | Serves embedding models, such as Qwen3 Embedding 8B. | The default embedding model, which is Pinecone-hosted unless you change it. |

To set up Fireworks models, see [Use Fireworks AI models in Nexus BYOC](/guides/nexus/byoc/fireworks/use-models). For supported models and catalog fields, see the [Fireworks AI reference](/guides/nexus/byoc/fireworks/reference).
