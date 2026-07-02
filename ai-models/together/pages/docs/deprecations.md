---
title: "Deprecations"
source: https://docs.together.ai/docs/deprecations
path: docs/deprecations
---

Together AI's model lifecycle policy, including upgrades, redirects, and deprecation schedules.

Together AI regularly updates the platform with new open-source models. This page describes the model lifecycle policy and lists active redirects and scheduled deprecations.

## Model lifecycle policy

Together AI follows a structured approach to introducing new models, upgrading existing models, and deprecating older versions, so you can rely on predictable behavior.

### Model upgrades (redirects)

An **upgrade** is a model release that is materially the same model lineage with targeted improvements and no fundamental changes to how developers use or reason about it.

A model qualifies as an upgrade when **one or more** of the following are true (and none of the "new model" criteria apply):

* Same modality and task profile (e.g., instruct → instruct, reasoning → reasoning).
* Same architecture family (e.g., DeepSeek-V3 → DeepSeek-V3-0324).
* Post-training or fine-tuning improvements, bug fixes, safety tuning, or small data refresh.
* Behavior is strongly compatible (prompting patterns and evals are similar).
* Pricing change is none or small (≤10% increase).

**Outcome:** The current endpoint redirects to the upgraded version after a **3-day notice**. The old version remains available via dedicated endpoints.

### New models (no redirect)

A **new model** is a release with materially different capabilities, costs, or operating characteristics, so a silent redirect would be misleading.

Any of the following triggers classification as a new model:

* Modality shift (e.g., reasoning-only ↔ instruct/hybrid, text → multimodal).
* Architecture shift (e.g., Qwen3 → Qwen3-Next, Llama 3 → Llama 4).
* Large behavior shift (prompting patterns, output style, or verbosity materially different).
* Experimental flag by provider (e.g., DeepSeek-V3-Exp).
* Large price change (>10% increase or pricing structure change).
* Benchmark deltas that meaningfully change task positioning.
* Safety policy or system prompt changes that noticeably affect outputs.

**Outcome:** No automatic redirect. Together AI announces the new model and deprecates the old one on a **2-week timeline** (both are available during this window). You must explicitly switch model IDs.

## Active model redirects

The following models are redirected to newer versions. Requests to the original model ID are automatically routed to the upgraded version:

| Original model                       | Redirects to                              | Notes                                     |
| :----------------------------------- | :---------------------------------------- | :---------------------------------------- |
| `mistralai/Mistral-7B-Instruct-v0.3` | `mistralai/Ministral-3-14B-Instruct-2512` | Same lineage, upgraded version            |
| `Kimi-K2`                            | `Kimi-K2-0905`                            | Same architecture, improved post-training |
| `DeepSeek-V3`                        | `DeepSeek-V3.1`                           | Same architecture, targeted improvements  |
| `DeepSeek-V3-0324`                   | `DeepSeek-V3.1`                           | Same architecture, targeted improvements  |
| `DeepSeek-R1`                        | `DeepSeek-R1-0528`                        | Same architecture, targeted improvements  |

<Tip>
  If you need to use the original model version, you can always deploy it as a [dedicated endpoint](/docs/dedicated-endpoints).
</Tip>

## Deprecation policy

| Model type                   | Deprecation notice                  | Notes                                                    |
| :--------------------------- | :---------------------------------- | :------------------------------------------------------- |
| Preview model                | \<24 hours of notice, after 30 days | Clearly marked in docs and playground with "Preview" tag |
| Serverless endpoint          | 2 or 3 weeks\*                      |                                                          |
| On-demand dedicated endpoint | 2 or 3 weeks\*                      |                                                          |

\*Depends on usage and whether a newer version of the model is available.

* If you use a model scheduled for deprecation, you receive an email notification.
* All changes appear on this page.
* Each deprecated model has a specified removal date.
* After the removal date, the model is no longer available via its serverless endpoint, but migration options are described below.

## Migration options

When a model is deprecated on the serverless platform, you have three options:

1. **On-demand dedicated endpoint** (if supported):
   * Reserved solely for you. You choose the underlying hardware.
   * Charged on a price-per-minute basis.
   * Endpoints can be dynamically spun up and down.
2. **Monthly reserved dedicated endpoint:**
   * Reserved solely for you.
   * Charged on a month-by-month basis.
   * Can be requested via this [form](https://together.ai/monthly-reserved).
3. **Migrate to a newer serverless model:**
   * Switch to an updated model on the serverless platform.

## Migration steps

1. Review the deprecation table below to find your current model.
2. Check if on-demand dedicated endpoints are supported for your model.
3. Decide on your preferred migration option.
4. If you choose a new serverless model, test your application thoroughly before migrating.
5. Update your API calls to use the new model or dedicated endpoint.

## Deprecation history

The table below lists all deprecations, most recent first.

| Removal date | Model                                               | Supported by on-demand dedicated endpoints                                                             |
| :----------- | :-------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| 2026-06-26   | `zai-org/GLM-5.1`                                   | Yes                                                                                                    |
| 2026-06-26   | `meta-llama/Llama-Guard-4-12B`                      | No                                                                                                     |
| 2026-06-26   | `meta-llama/Meta-Llama-3-8B-Instruct-Lite`          | Yes                                                                                                    |
| 2026-06-26   | `google/gemma-3n-E4B-it`                            | Yes                                                                                                    |
| 2026-06-26   | `Qwen/Qwen3-235B-A22B-Instruct-2507-tput`           | Yes                                                                                                    |
| 2026-06-29   | `Qwen/Qwen3.5-397B-A17B`                            | Yes                                                                                                    |
| 2026-06-22   | `zai-org/GLM-5`                                     | Yes                                                                                                    |
| 2026-06-11   | `mistralai/Voxtral-Mini-3B-2507`                    | Yes                                                                                                    |
| 2026-06-04   | `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`           | Yes                                                                                                    |
| 2026-05-27   | `black-forest-labs/FLUX.1-krea-dev`                 | No                                                                                                     |
| 2026-05-21   | `moonshotai/Kimi-K2.5`                              | Yes                                                                                                    |
| 2026-05-14   | `deepseek-ai/DeepSeek-R1`                           | No                                                                                                     |
| 2026-05-14   | `deepseek-ai/DeepSeek-V3.1`                         | No                                                                                                     |
| 2026-05-14   | `Qwen/Qwen3-Coder-Next-FP8`                         | Yes                                                                                                    |
| 2026-04-16   | `Qwen/Qwen3-VL-8B-Instruct`                         | Yes                                                                                                    |
| 2026-04-16   | `Qwen/Qwen3-235B-A22B-Thinking-2507`                | Yes                                                                                                    |
| 2026-04-16   | `mistralai/Mixtral-8x7B-Instruct-v0.1`              | Yes                                                                                                    |
| 2026-04-03   | `ServiceNow-AI/Apriel-1.5-15b-Thinker`              | Yes                                                                                                    |
| 2026-04-03   | `ServiceNow-AI/Apriel-1.6-15b-Thinker`              | Yes                                                                                                    |
| 2026-04-02   | `zai-org/GLM-4.5-Air-FP8`                           | Yes                                                                                                    |
| 2026-04-02   | `zai-org/GLM-4.7`                                   | Yes                                                                                                    |
| 2026-04-02   | `mistralai/Mistral-Small-24B-Instruct-2501`         | Yes                                                                                                    |
| 2026-04-02   | `Qwen/Qwen3-Next-80B-A3B-Instruct`                  | Yes                                                                                                    |
| 2026-03-31   | `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Yes                                                                                                    |
| 2026-03-06   | `mixedbread-ai/Mxbai-Rerank-Large-V2`               | No                                                                                                     |
| 2026-03-06   | `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo`       | Yes                                                                                                    |
| 2026-03-06   | `Qwen/Qwen3-235B-A22B-Thinking-2507`                | Yes                                                                                                    |
| 2026-03-06   | `moonshotai/Kimi-K2-Thinking`                       | Yes                                                                                                    |
| 2026-03-06   | `moonshotai/Kimi-K2-Instruct-0905`                  | No                                                                                                     |
| 2026-03-06   | `meta-llama/Llama-3.2-3B-Instruct-Turbo`            | No                                                                                                     |
| 2026-02-25   | `black-forest-labs/FLUX.1-dev`                      | No                                                                                                     |
| 2026-02-25   | `black-forest-labs/FLUX.1-dev-lora`                 | No                                                                                                     |
| 2026-02-25   | `black-forest-labs/FLUX.1-Kontext-dev`              | No                                                                                                     |
| 2026-02-25   | `Qwen/Qwen3-VL-32B-Instruct`                        | Yes                                                                                                    |
| 2026-02-25   | `meta-llama/Llama-3.2-3B-Instruct-Turbo-Classifier` | No                                                                                                     |
| 2026-02-25   | `mistralai/Ministral-3-14B-Instruct`                | Yes                                                                                                    |
| 2026-02-25   | `Qwen/Qwen3-Next-80B-A3B-Thinking`                  | Yes                                                                                                    |
| 2026-02-25   | `Alibaba-NLP/gte-modernbert-base`                   | No                                                                                                     |
| 2026-02-25   | `BAAI/bge-base-en-v1.5-vllm`                        | No                                                                                                     |
| 2026-02-25   | `meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo`      | Yes                                                                                                    |
| 2026-02-25   | `meta-llama/Llama-Guard-3-11B-Vision-Turbo`         | No                                                                                                     |
| 2026-02-25   | `meta-llama/LlamaGuard-2-8b`                        | No                                                                                                     |
| 2026-02-25   | `marin-community/Marin-8B-Instruct`                 | No                                                                                                     |
| 2026-02-25   | `nvidia/Nvidia-Nemotron-Nano-9B-v2`                 | Yes                                                                                                    |
| 2026-02-06   | `togethercomputer/m2-bert-80M-32k-retrieval`        | No                                                                                                     |
| 2026-02-06   | `Salesforce/Llama-Rank-V1`                          | Yes                                                                                                    |
| 2026-02-06   | `togethercomputer/Refuel-Llm-V2`                    | No                                                                                                     |
| 2026-02-06   | `togethercomputer/Refuel-Llm-V2-Small`              | No                                                                                                     |
| 2026-02-06   | `Qwen/Qwen3-235B-A22B-fp8-tput`                     | Yes                                                                                                    |
| 2026-02-06   | `qwen-qwen2-5-14b-instruct-lora`                    | Yes                                                                                                    |
| 2026-02-06   | `meta-llama/Llama-4-Scout-17B-16E-Instruct`         | Yes                                                                                                    |
| 2026-02-06   | `Qwen/Qwen2.5-72B-Instruct-Turbo`                   | Yes                                                                                                    |
| 2026-02-06   | `meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo`     | Yes                                                                                                    |
| 2026-02-06   | `BAAI/bge-large-en-v1.5`                            | No                                                                                                     |
| 2026-02-03   | `deepseek-ai/DeepSeek-R1-0528-tput`                 | No                                                                                                     |
| 2026-01-05   | `Qwen/Qwen2.5-VL-72B-Instruct`                      | Yes                                                                                                    |
| 2025-12-23   | `deepseek-ai/DeepSeek-R1-Distill-Llama-70B`         | Yes                                                                                                    |
| 2025-12-23   | `meta-llama/Meta-Llama-3-70B-Instruct-Turbo`        | Yes                                                                                                    |
| 2025-12-23   | `black-forest-labs/FLUX.1-schnell-free`             | No                                                                                                     |
| 2025-12-23   | `meta-llama/Meta-Llama-Guard-3-8B`                  | No                                                                                                     |
| 2025-11-19   | `deepcogito/cogito-v2-preview-deepseek-671b`        | No                                                                                                     |
| 2025-07-25   | `arcee-ai/caller`                                   | No                                                                                                     |
| 2025-07-25   | `arcee-ai/arcee-blitz`                              | No                                                                                                     |
| 2025-07-25   | `arcee-ai/virtuoso-medium-v2`                       | No                                                                                                     |
| 2025-11-17   | `arcee-ai/virtuoso-large`                           | No                                                                                                     |
| 2025-11-17   | `arcee-ai/maestro-reasoning`                        | No                                                                                                     |
| 2025-11-17   | `arcee_ai/arcee-spotlight`                          | No                                                                                                     |
| 2025-11-17   | `arcee-ai/coder-large`                              | No                                                                                                     |
| 2025-11-13   | `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`          | Yes                                                                                                    |
| 2025-11-13   | `mistralai/Mistral-7B-Instruct-v0.1`                | Yes                                                                                                    |
| 2025-11-13   | `Qwen/Qwen2.5-Coder-32B-Instruct`                   | Yes                                                                                                    |
| 2025-11-13   | `Qwen/QwQ-32B`                                      | Yes                                                                                                    |
| 2025-11-13   | `deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free`    | No                                                                                                     |
| 2025-11-13   | `meta-llama/Llama-3.3-70B-Instruct-Turbo-Free`      | No                                                                                                     |
| 2025-08-28   | `Qwen/Qwen2-VL-72B-Instruct`                        | Yes                                                                                                    |
| 2025-08-28   | `nvidia/Llama-3.1-Nemotron-70B-Instruct-HF`         | Yes                                                                                                    |
| 2025-08-28   | `perplexity-ai/r1-1776`                             | No (coming soon!)                                                                                      |
| 2025-08-28   | `meta-llama/Meta-Llama-3-8B-Instruct`               | Yes                                                                                                    |
| 2025-08-28   | `google/gemma-2-27b-it`                             | Yes                                                                                                    |
| 2025-08-28   | `Qwen/Qwen2-72B-Instruct`                           | Yes                                                                                                    |
| 2025-08-28   | `meta-llama/Llama-Vision-Free`                      | No                                                                                                     |
| 2025-08-28   | `Qwen/Qwen2.5-14B`                                  | Yes                                                                                                    |
| 2025-08-28   | `meta-llama-llama-3-3-70b-instruct-lora`            | No (coming soon!)                                                                                      |
| 2025-08-28   | `meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo`    | No (coming soon!)                                                                                      |
| 2025-08-28   | `NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO`       | Yes                                                                                                    |
| 2025-08-28   | `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B`         | Yes                                                                                                    |
| 2025-08-28   | `black-forest-labs/FLUX.1-depth`                    | No (coming soon!)                                                                                      |
| 2025-08-28   | `black-forest-labs/FLUX.1-redux`                    | No (coming soon!)                                                                                      |
| 2025-08-28   | `meta-llama/Llama-3-8b-chat-hf`                     | Yes                                                                                                    |
| 2025-08-28   | `black-forest-labs/FLUX.1-canny`                    | No (coming soon!)                                                                                      |
| 2025-08-28   | `meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo`    | No (coming soon!)                                                                                      |
| 2025-06-13   | `gryphe-mythomax-l2-13b`                            | No (coming soon!)                                                                                      |
| 2025-06-13   | `mistralai-mixtral-8x22b-instruct-v0-1`             | No (coming soon!)                                                                                      |
| 2025-06-13   | `mistralai-mixtral-8x7b-v0-1`                       | No (coming soon!)                                                                                      |
| 2025-06-13   | `togethercomputer-m2-bert-80m-2k-retrieval`         | No (coming soon!)                                                                                      |
| 2025-06-13   | `togethercomputer-m2-bert-80m-8k-retrieval`         | No (coming soon!)                                                                                      |
| 2025-06-13   | `whereisai-uae-large-v1`                            | No (coming soon!)                                                                                      |
| 2025-06-13   | `google-gemma-2-9b-it`                              | No (coming soon!)                                                                                      |
| 2025-06-13   | `google-gemma-2b-it`                                | No (coming soon!)                                                                                      |
| 2025-06-13   | `gryphe-mythomax-l2-13b-lite`                       | No (coming soon!)                                                                                      |
| 2025-05-16   | `meta-llama-llama-3-2-3b-instruct-turbo-lora`       | No (coming soon!)                                                                                      |
| 2025-05-16   | `meta-llama-meta-llama-3-8b-instruct-turbo`         | No (coming soon!)                                                                                      |
| 2025-04-24   | `meta-llama/Llama-2-13b-chat-hf`                    | No (coming soon!)                                                                                      |
| 2025-04-24   | `meta-llama-meta-llama-3-70b-instruct-turbo`        | No (coming soon!)                                                                                      |
| 2025-04-24   | `meta-llama-meta-llama-3-1-8b-instruct-turbo-lora`  | No (coming soon!)                                                                                      |
| 2025-04-24   | `meta-llama-meta-llama-3-1-70b-instruct-turbo-lora` | No (coming soon!)                                                                                      |
| 2025-04-24   | `meta-llama-llama-3-2-1b-instruct-lora`             | No (coming soon!)                                                                                      |
| 2025-04-24   | `microsoft-wizardlm-2-8x22b`                        | No (coming soon!)                                                                                      |
| 2025-04-24   | `upstage-solar-10-7b-instruct-v1`                   | No (coming soon!)                                                                                      |
| 2025-04-14   | `stabilityai/stable-diffusion-xl-base-1.0`          | No (coming soon!)                                                                                      |
| 2025-04-04   | `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo-lora`  | No (coming soon!)                                                                                      |
| 2025-03-27   | `mistralai/Mistral-7B-v0.1`                         | No                                                                                                     |
| 2025-03-25   | `Qwen/QwQ-32B-Preview`                              | No                                                                                                     |
| 2025-03-13   | `databricks-dbrx-instruct`                          | No                                                                                                     |
| 2025-03-11   | `meta-llama/Meta-Llama-3-70B-Instruct-Lite`         | No                                                                                                     |
| 2025-03-08   | `Meta-Llama/Llama-Guard-7b`                         | No                                                                                                     |
| 2025-02-06   | `sentence-transformers/msmarco-bert-base-dot-v5`    | No                                                                                                     |
| 2025-02-06   | `bert-base-uncased`                                 | No                                                                                                     |
| 2024-10-29   | `Qwen/Qwen1.5-72B-Chat`                             | No                                                                                                     |
| 2024-10-29   | `Qwen/Qwen1.5-110B-Chat`                            | No                                                                                                     |
| 2024-10-07   | `NousResearch/Nous-Hermes-2-Yi-34B`                 | No                                                                                                     |
| 2024-10-07   | `NousResearch/Hermes-3-Llama-3.1-405B-Turbo`        | No                                                                                                     |
| 2024-08-22   | `NousResearch/Nous-Hermes-2-Mistral-7B-DPO`         | [Yes](https://api.together.xyz/models/NousResearch/Nous-Hermes-2-Mistral-7B-DPO#dedicated_endpoints)   |
| 2024-08-22   | `SG161222/Realistic_Vision_V3.0_VAE`                | No                                                                                                     |
| 2024-08-22   | `meta-llama/Llama-2-70b-chat-hf`                    | No                                                                                                     |
| 2024-08-22   | `mistralai/Mixtral-8x22B`                           | No                                                                                                     |
| 2024-08-22   | `Phind/Phind-CodeLlama-34B-v2`                      | No                                                                                                     |
| 2024-08-22   | `meta-llama/Meta-Llama-3-70B`                       | [Yes](https://api.together.xyz/models/meta-llama/Meta-Llama-3-70B#dedicated_endpoints)                 |
| 2024-08-22   | `teknium/OpenHermes-2p5-Mistral-7B`                 | [Yes](https://api.together.xyz/models/teknium/OpenHermes-2p5-Mistral-7B#dedicated_endpoints)           |
| 2024-08-22   | `openchat/openchat-3.5-1210`                        | [Yes](https://api.together.xyz/models/openchat/openchat-3.5-1210#dedicated_endpoints)                  |
| 2024-08-22   | `WizardLM/WizardCoder-Python-34B-V1.0`              | No                                                                                                     |
| 2024-08-22   | `NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT`       | [Yes](https://api.together.xyz/models/NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT#dedicated_endpoints) |
| 2024-08-22   | `NousResearch/Nous-Hermes-Llama2-13b`               | [Yes](https://api.together.xyz/models/NousResearch/Nous-Hermes-Llama2-13b#dedicated_endpoints)         |
| 2024-08-22   | `zero-one-ai/Yi-34B-Chat`                           | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-34b-Instruct-hf`               | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-34b-Python-hf`                 | No                                                                                                     |
| 2024-08-22   | `teknium/OpenHermes-2-Mistral-7B`                   | [Yes](https://api.together.xyz/models/teknium/OpenHermes-2-Mistral-7B#dedicated_endpoints)             |
| 2024-08-22   | `Qwen/Qwen1.5-14B-Chat`                             | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-14B-Chat#dedicated_endpoints)                       |
| 2024-08-22   | `stabilityai/stable-diffusion-2-1`                  | No                                                                                                     |
| 2024-08-22   | `meta-llama/Llama-3-8b-hf`                          | [Yes](https://api.together.xyz/models/meta-llama/Llama-3-8b-hf#dedicated_endpoints)                    |
| 2024-08-22   | `prompthero/openjourney`                            | No                                                                                                     |
| 2024-08-22   | `runwayml/stable-diffusion-v1-5`                    | No                                                                                                     |
| 2024-08-22   | `wavymulder/Analog-Diffusion`                       | No                                                                                                     |
| 2024-08-22   | `Snowflake/snowflake-arctic-instruct`               | No                                                                                                     |
| 2024-08-22   | `deepseek-ai/deepseek-coder-33b-instruct`           | No                                                                                                     |
| 2024-08-22   | `Qwen/Qwen1.5-7B-Chat`                              | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-7B-Chat#dedicated_endpoints)                        |
| 2024-08-22   | `Qwen/Qwen1.5-32B-Chat`                             | No                                                                                                     |
| 2024-08-22   | `cognitivecomputations/dolphin-2.5-mixtral-8x7b`    | No                                                                                                     |
| 2024-08-22   | `garage-bAInd/Platypus2-70B-instruct`               | No                                                                                                     |
| 2024-08-22   | `google/gemma-7b-it`                                | [Yes](https://api.together.xyz/models/google/gemma-7b-it#dedicated_endpoints)                          |
| 2024-08-22   | `meta-llama/Llama-2-7b-chat-hf`                     | [Yes](https://api.together.xyz/models/meta-llama/Llama-2-7b-chat-hf#dedicated_endpoints)               |
| 2024-08-22   | `Qwen/Qwen1.5-32B`                                  | No                                                                                                     |
| 2024-08-22   | `Open-Orca/Mistral-7B-OpenOrca`                     | [Yes](https://api.together.xyz/models/Open-Orca/Mistral-7B-OpenOrca#dedicated_endpoints)               |
| 2024-08-22   | `codellama/CodeLlama-13b-Instruct-hf`               | [Yes](https://api.together.xyz/models/codellama/CodeLlama-13b-Instruct-hf#dedicated_endpoints)         |
| 2024-08-22   | `NousResearch/Nous-Capybara-7B-V1p9`                | [Yes](https://api.together.xyz/models/NousResearch/Nous-Capybara-7B-V1p9#dedicated_endpoints)          |
| 2024-08-22   | `lmsys/vicuna-13b-v1.5`                             | [Yes](https://api.together.xyz/models/lmsys/vicuna-13b-v1.5#dedicated_endpoints)                       |
| 2024-08-22   | `Undi95/ReMM-SLERP-L2-13B`                          | [Yes](https://api.together.xyz/models/Undi95/ReMM-SLERP-L2-13B#dedicated_endpoints)                    |
| 2024-08-22   | `Undi95/Toppy-M-7B`                                 | [Yes](https://api.together.xyz/models/Undi95/Toppy-M-7B#dedicated_endpoints)                           |
| 2024-08-22   | `meta-llama/Llama-2-13b-hf`                         | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-70b-Instruct-hf`               | No                                                                                                     |
| 2024-08-22   | `snorkelai/Snorkel-Mistral-PairRM-DPO`              | [Yes](https://api.together.xyz/models/snorkelai/Snorkel-Mistral-PairRM-DPO#dedicated_endpoints)        |
| 2024-08-22   | `togethercomputer/LLaMA-2-7B-32K-Instruct`          | [Yes](https://api.together.xyz/models/togethercomputer/Llama-2-7B-32K-Instruct#dedicated_endpoints)    |
| 2024-08-22   | `Austism/chronos-hermes-13b`                        | [Yes](https://api.together.xyz/models/Austism/chronos-hermes-13b#dedicated_endpoints)                  |
| 2024-08-22   | `Qwen/Qwen1.5-72B`                                  | No                                                                                                     |
| 2024-08-22   | `zero-one-ai/Yi-34B`                                | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-7b-Instruct-hf`                | [Yes](https://api.together.xyz/models/codellama/CodeLlama-7b-Instruct-hf#dedicated_endpoints)          |
| 2024-08-22   | `togethercomputer/evo-1-131k-base`                  | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-70b-hf`                        | No                                                                                                     |
| 2024-08-22   | `WizardLM/WizardLM-13B-V1.2`                        | [Yes](https://api.together.xyz/models/WizardLM/WizardLM-13B-V1.2#dedicated_endpoints)                  |
| 2024-08-22   | `meta-llama/Llama-2-7b-hf`                          | No                                                                                                     |
| 2024-08-22   | `google/gemma-7b`                                   | [Yes](https://api.together.xyz/models/google/gemma-7b#dedicated_endpoints)                             |
| 2024-08-22   | `Qwen/Qwen1.5-1.8B-Chat`                            | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-1.8B-Chat#dedicated_endpoints)                      |
| 2024-08-22   | `Qwen/Qwen1.5-4B-Chat`                              | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-4B-Chat#dedicated_endpoints)                        |
| 2024-08-22   | `lmsys/vicuna-7b-v1.5`                              | [Yes](https://api.together.xyz/models/lmsys/vicuna-7b-v1.5#dedicated_endpoints)                        |
| 2024-08-22   | `zero-one-ai/Yi-6B`                                 | [Yes](https://api.together.xyz/models/zero-one-ai/Yi-6B#dedicated_endpoints)                           |
| 2024-08-22   | `Nexusflow/NexusRaven-V2-13B`                       | [Yes](https://api.together.xyz/models/Nexusflow/NexusRaven-V2-13B#dedicated_endpoints)                 |
| 2024-08-22   | `google/gemma-2b`                                   | [Yes](https://api.together.xyz/models/google/gemma-2b#dedicated_endpoints)                             |
| 2024-08-22   | `Qwen/Qwen1.5-7B`                                   | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-7B#dedicated_endpoints)                             |
| 2024-08-22   | `NousResearch/Nous-Hermes-llama-2-7b`               | [Yes](https://api.together.xyz/models/NousResearch/Nous-Hermes-llama-2-7b#dedicated_endpoints)         |
| 2024-08-22   | `togethercomputer/alpaca-7b`                        | [Yes](https://api.together.xyz/models/togethercomputer/alpaca-7b#dedicated_endpoints)                  |
| 2024-08-22   | `Qwen/Qwen1.5-14B`                                  | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-14B#dedicated_endpoints)                            |
| 2024-08-22   | `codellama/CodeLlama-70b-Python-hf`                 | No                                                                                                     |
| 2024-08-22   | `Qwen/Qwen1.5-4B`                                   | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-4B#dedicated_endpoints)                             |
| 2024-08-22   | `togethercomputer/StripedHyena-Hessian-7B`          | No                                                                                                     |
| 2024-08-22   | `allenai/OLMo-7B-Instruct`                          | No                                                                                                     |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-7B-Instruct`     | No                                                                                                     |
| 2024-08-22   | `togethercomputer/LLaMA-2-7B-32K`                   | [Yes](https://api.together.xyz/models/togethercomputer/LLaMA-2-7B-32K#dedicated_endpoints)             |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-7B-Base`         | No                                                                                                     |
| 2024-08-22   | `Qwen/Qwen1.5-0.5B-Chat`                            | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-0.5B-Chat#dedicated_endpoints)                      |
| 2024-08-22   | `microsoft/phi-2`                                   | [Yes](https://api.together.xyz/models/microsoft/phi-2#dedicated_endpoints)                             |
| 2024-08-22   | `Qwen/Qwen1.5-0.5B`                                 | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-0.5B#dedicated_endpoints)                           |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-7B-Chat`         | No                                                                                                     |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-Chat-3B-v1`      | No                                                                                                     |
| 2024-08-22   | `togethercomputer/GPT-JT-Moderation-6B`             | No                                                                                                     |
| 2024-08-22   | `Qwen/Qwen1.5-1.8B`                                 | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-1.8B#dedicated_endpoints)                           |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-Instruct-3B-v1`  | No                                                                                                     |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-Base-3B-v1`      | No                                                                                                     |
| 2024-08-22   | `WhereIsAI/UAE-Large-V1`                            | No                                                                                                     |
| 2024-08-22   | `allenai/OLMo-7B`                                   | No                                                                                                     |
| 2024-08-22   | `togethercomputer/evo-1-8k-base`                    | No                                                                                                     |
| 2024-08-22   | `WizardLM/WizardCoder-15B-V1.0`                     | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-13b-Python-hf`                 | [Yes](https://api.together.xyz/models/codellama/CodeLlama-13b-Python-hf#dedicated_endpoints)           |
| 2024-08-22   | `allenai-olmo-7b-twin-2t`                           | No                                                                                                     |
| 2024-08-22   | `sentence-transformers/msmarco-bert-base-dot-v5`    | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-7b-Python-hf`                  | [Yes](https://api.together.xyz/models/codellama/CodeLlama-7b-Python-hf#dedicated_endpoints)            |
| 2024-08-22   | `hazyresearch/M2-BERT-2k-Retrieval-Encoder-V1`      | No                                                                                                     |
| 2024-08-22   | `bert-base-uncased`                                 | No                                                                                                     |
| 2024-08-22   | `mistralai/Mistral-7B-Instruct-v0.1-json`           | No                                                                                                     |
| 2024-08-22   | `mistralai/Mistral-7B-Instruct-v0.1-tools`          | No                                                                                                     |
| 2024-08-22   | `togethercomputer-codellama-34b-instruct-json`      | No                                                                                                     |
| 2024-08-22   | `togethercomputer-codellama-34b-instruct-tools`     | No                                                                                                     |

**Notes on model support:**

* Models marked "Yes" in the on-demand dedicated endpoint support column can be spun up as dedicated endpoints with customizable hardware.
* Models marked "No" are not available as on-demand endpoints and require migration to a different model or a monthly reserved dedicated endpoint.

## Recommended actions

* Regularly check this page for updates on model deprecations.
* Plan your migration well in advance of the removal date to ensure a smooth transition.
* If you have any questions or need assistance with migration, contact the Together AI support team.

For the most up-to-date information on model availability, support, and recommended alternatives, check the API documentation or contact the Together AI support team.
