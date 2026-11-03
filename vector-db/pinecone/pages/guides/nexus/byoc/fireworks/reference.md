---
title: "Fireworks AI reference for Nexus BYOC"
source: https://docs.pinecone.io/guides/nexus/byoc/fireworks/reference
path: guides/nexus/byoc/fireworks/reference
---

Supported Fireworks AI models, catalog fields, and constraints for using Fireworks models in the Nexus BYOC inference catalog.

> [!NOTE]
>
> Nexus BYOC is available only on [Enterprise plans](https://www.pinecone.io/pricing/).

This page lists the Fireworks models that work with Pinecone Nexus Bring Your Own Cloud (BYOC) and the `inference-proxy-models.toml` fields a Fireworks catalog entry uses. For setup steps, see [Use Fireworks AI models in Nexus BYOC](/guides/nexus/byoc/fireworks/use-models).

## Supported models

The following serverless models work with Nexus BYOC. For the full list, including models you can run on dedicated deployments, see the [Fireworks model library](https://fireworks.ai/models).

| Model type | Catalog ID | Fireworks model path | Suggested use |
| - | - | - | - |
| Chat | `glm-5p3-flash` | `accounts/fireworks/models/glm-5p3-flash` | Curation and System defaults. |
| Chat | `deepseek-v4p1-flash` | `accounts/fireworks/models/deepseek-v4p1-flash` | Curation default. |
| Chat | `glm-5p3` | `accounts/fireworks/models/glm-5p3` | Selected per query. |
| Chat | `kimi-k3` | `accounts/fireworks/models/kimi-k3` | Query default, for complex, multi-step questions. |
| Embedding | `qwen3-embedding-8b` | `accounts/fireworks/models/qwen3-embedding-8b` | Optional default embedding model. Returns 4,096-dimensional vectors. |

You can also use `accounts/fireworks/models/gpt-oss-120b` and `accounts/fireworks/models/minimax-m3p1-flash` the same way. Set each entry's `context_window` to the model's own window, such as `131_072` for `gpt-oss-120b`. `gpt-oss-120b` is text-only, so also set `no_vision = true`. The catalog ID is the name you choose for an entry, and the examples here match it to the model name.

## Endpoint and authentication

* **Endpoint:** Set `base_url` to `https://api.fireworks.ai/inference/v1`, the Fireworks OpenAI-compatible endpoint.
* **API key:** Store your Fireworks API key as the stack secret `nexus-provider-keys.<ref>`, and set the entry's `api_key_ref` to `<ref>`. Every Fireworks entry can share one reference. Pulumi stores the secret as a Kubernetes secret, and the inference proxy reads it at startup. If the key doesn't resolve, the proxy lists the model as unavailable.

## Chat model fields

A Fireworks chat model is an `[llm_models.<id>]` entry with `api_style = "openai"`.

| Field | Required | Description |
| - | - | - |
| `api_style` | Yes | Set to `openai`. |
| `model` | Yes | The Fireworks model path, such as `accounts/fireworks/models/glm-5p3`. |
| `base_url` | Yes | The Fireworks endpoint. |
| `api_key_ref` | Yes | The name of the secret that holds your Fireworks API key. |
| `label` | Yes | The model name shown in the console and in `GET /models`. |
| `provider` | Yes | The provider tag shown in the console and in `GET /models`, such as `fireworks`. |
| `context_window` | Yes | The input token budget. |
| `max_output_tokens` | Yes | The output token cap. The proxy enforces it on every request. |
| `input_price_per_mtok` | No | The price per million input tokens. Set the price fields to have usage and the query trace report cost for the model. |
| `output_price_per_mtok` | No | The price per million output tokens. |
| `cache_read_price_per_mtok` | No | The price per million cached input tokens. |
| `cache_write_price_per_mtok` | No | The price per million tokens written to the cache. |
| `no_vision` | No | Set to `true` for a model that doesn't accept images. Defaults to `false`, which advertises the model as vision-capable. |

For current prices, see [Fireworks pricing](https://fireworks.ai/pricing).

## Embedding model fields

A Fireworks embedding model is an `[embedding_models.<id>]` entry with `api_style = "openai"`.

| Field | Required | Description |
| - | - | - |
| `api_style` | Yes | Set to `openai`. |
| `model` | Yes | The Fireworks model path, such as `accounts/fireworks/models/qwen3-embedding-8b`. |
| `base_url` | Yes | The Fireworks endpoint. |
| `api_key_ref` | Yes | The name of the secret that holds your Fireworks API key. |
| `dimension` | Yes | The width of the vectors the model returns. Set it to the model's actual output width. |
| `max_input_chars` | Yes | The length each input is truncated to before the call. |
| `max_batch_size` | Yes | The most inputs per upstream call. The proxy splits larger requests into batches of this size. |
| `provider` | No | The provider tag used to split spend by vendor, such as `fireworks`. |

## Default profile fields

The `[default]` profile controls which catalog models your deployment serves.

| Field | Description |
| - | - |
| `supported_llm_models` | The chat models the deployment serves. Every model a default or a query names must be in this list. |
| `supported_embedding_models` | The embedding models the deployment serves. |
| `supported_rerank_models` | The rerank models the deployment serves. |
| `embedding.tiers.default` | The default embedding model, set with `model_ref`. Required. |
| `rerank.tiers.default` | The default rerank model, set with `model_ref`. Required. |
| `llm.phase_defaults` | The default model for each work area: `search` for Query, `curate` for Curation, and `agent` for System. |
| `llm.tiers` | The `lite`, `standard`, and `pro` tiers, each set with `model_ref`. A work area that `phase_defaults` doesn't set falls back to a tier. |

## Constraints

* **Chat model parameters:** Every chat model must support the OpenAI `tools` and `response_format` parameters, because Nexus relies on both.
* **Default models:** Each work area's default comes from `llm.phase_defaults`, falling back to the tiers: Query from `search` or the `standard` tier, Curation from `curate` or the `lite` tier, and System from `agent` or the `standard` tier. The catalog reapplies these defaults on every settings pull, so the console's **Default models** card is read-only. To change a default, edit the catalog and run `pulumi up`.
* **Tier names in queries:** A query treats a tier name, such as `pro`, as the Query default. Name models by catalog ID instead.
* **Embedding changes:** A Pinecone index's dimension is fixed when the index is created. If you change the default embedding model, keep every embedding model a context has used in the catalog, because existing contexts look up their embedding model by ID at query time.
