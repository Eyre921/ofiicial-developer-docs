---
title: "Supported models"
source: https://docs.together.ai/docs/fine-tuning/supported-models
path: docs/fine-tuning/supported-models
---

Every base model available for fine-tuning, with context length and batch size limits.

The tables below list every model available through the fine-tuning API. Context lengths are the maximum for that model in SFT and DPO modes. Batch sizes refer to packed batches for text formats. See [data preparation](/docs/fine-tuning/data-preparation) for details on packing.

<Warning>
  Some models can be fine-tuned but cannot be deployed as dedicated endpoints. To verify deployability before training, confirm the base model appears in the [supported models](/docs/dedicated-endpoints/models) list for dedicated model inference (or run `tg beta models configs <BASE_MODEL>`). If it isn't listed there, the fine-tune can't be hosted on a dedicated endpoint.
</Warning>

[Fill out this form](https://www.together.ai/forms/model-requests) to request a model that isn't in the list.

<Columns>
  <Card title="LoRA fine-tuning" icon="adjustments-horizontal" href="#lora-fine-tuning" />

  <Card title="Full fine-tuning" icon="stack-2" href="#full-fine-tuning" />

  <Card title="Vision-language" icon="eye" href="#vision-language-models" />

  <Card title="LoRA target modules" icon="target" href="#lora-target-modules" />
</Columns>

## LoRA fine-tuning

| Organization | Model                                              | API ID                                               | Context (SFT) | Context (DPO) | Max batch (SFT) | Max batch (DPO) | Min batch | Grad accum | Max LoRA rank |
| ------------ | -------------------------------------------------- | ---------------------------------------------------- | ------------- | ------------- | --------------- | --------------- | --------- | ---------- | ------------- |
| DeepSeek     | DeepSeek V4 Flash                                  | `deepseek-ai/DeepSeek-V4-Flash`                      | 131072        | 32768         | 1               | 1               | 1         | 8          | 64            |
| DeepSeek     | DeepSeek V3.1                                      | `deepseek-ai/DeepSeek-V3.1`                          | 65536         | 32768         | 2               | 2               | 2         | 8          | 16            |
| NVIDIA       | NVIDIA Nemotron 3 Nano Omni 30B A3B Reasoning BF16 | `nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16` | 65536         | 32768         | 8               | 8               | 8         | 1          | 64            |
| NVIDIA       | NVIDIA Nemotron 3 Super 120B A12B BF16             | `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`      | 49152         | 24576         | 4               | 4               | 4         | 2          | 64            |
| Qwen         | Qwen3.5 397B A17B                                  | `Qwen/Qwen3.5-397B-A17B`                             | 32768         | 16384         | 16              | 16              | 16        | 1          | 64            |
| Qwen         | Qwen3.5 122B A10B                                  | `Qwen/Qwen3.5-122B-A10B`                             | 65536         | 32768         | 16              | 16              | 16        | 1          | 64            |
| Qwen         | Qwen3.5 35B A3B                                    | `Qwen/Qwen3.5-35B-A3B`                               | 65536         | 32768         | 8               | 8               | 8         | 1          | 64            |
| Qwen         | Qwen3.5 35B A3B Base                               | `Qwen/Qwen3.5-35B-A3B-Base`                          | 65536         | 32768         | 8               | 8               | 8         | 1          | 64            |
| Qwen         | Qwen3.5 27B                                        | `Qwen/Qwen3.5-27B`                                   | 32768         | 16384         | 16              | 16              | 16        | 1          | 64            |
| Qwen         | Qwen3.5 9B                                         | `Qwen/Qwen3.5-9B`                                    | 65536         | 49152         | 8               | 8               | 8         | 1          | 64            |
| Qwen         | Qwen3.5 4B                                         | `Qwen/Qwen3.5-4B`                                    | 131072        | 65536         | 8               | 8               | 8         | 1          | 64            |
| Qwen         | Qwen3.5 2B                                         | `Qwen/Qwen3.5-2B`                                    | 131072        | 131072        | 8               | 8               | 8         | 1          | 64            |
| Qwen         | Qwen3.5 0.8B                                       | `Qwen/Qwen3.5-0.8B`                                  | 131072        | 131072        | 8               | 8               | 8         | 1          | 64            |
| Qwen         | Qwen3.6 35B A3B                                    | `Qwen/Qwen3.6-35B-A3B`                               | 65536         | 32768         | 8               | 8               | 8         | 1          | 64            |
| Qwen         | Qwen3.6 27B                                        | `Qwen/Qwen3.6-27B`                                   | 32768         | 16384         | 16              | 16              | 16        | 1          | 64            |
| Moonshot AI  | Kimi K2.7 Code                                     | `moonshotai/Kimi-K2.7-Code`                          | 32768         | 16384         | 4               | 4               | 4         | 8          | 16            |
| Moonshot AI  | Kimi K2.6                                          | `moonshotai/Kimi-K2.6`                               | 32768         | 16384         | 4               | 4               | 4         | 8          | 16            |
| Z.ai         | GLM 5.1                                            | `zai-org/GLM-5.1`                                    | 50688         | 25344         | 1               | 1               | 1         | 1          | 16            |
| OpenAI       | GPT-OSS 20B                                        | `openai/gpt-oss-20b`                                 | 131072        | 65536         | 1               | 1               | 1         | 8          | 64            |
| OpenAI       | GPT-OSS 120B                                       | `openai/gpt-oss-120b`                                | 65536         | 32768         | 2               | 2               | 2         | 8          | 64            |
| Meta         | Llama 4 Scout 17B 16E Instruct                     | `meta-llama/Llama-4-Scout-17B-16E-Instruct`          | 65536         | 12288         | 8               | 8               | 8         | 1          | 64            |
| Meta         | Llama 4 Scout 17B 16E Instruct VLM                 | `meta-llama/Llama-4-Scout-17B-16E-Instruct-VLM`      | 32768         | 32768         | 8               | 8               | 8         | 1          | 64            |
| Meta         | Llama 4 Maverick 17B 128E Instruct                 | `meta-llama/Llama-4-Maverick-17B-128E-Instruct`      | 16384         | 24576         | 16              | 16              | 16        | 1          | 64            |
| Meta         | Llama 4 Maverick 17B 128E Instruct VLM             | `meta-llama/Llama-4-Maverick-17B-128E-Instruct-VLM`  | 16384         | 16384         | 16              | 16              | 16        | 1          | 64            |
| Meta         | Llama 3.3 70B Instruct Reference                   | `meta-llama/Llama-3.3-70B-Instruct-Reference`        | 24576         | 12288         | 8               | 8               | 8         | 1          | 64            |
| Meta         | Meta Llama 3.1 8B Instruct Reference               | `meta-llama/Meta-Llama-3.1-8B-Instruct-Reference`    | 131072        | 65536         | 8               | 8               | 8         | 1          | 64            |
| Google       | Gemma 4 31B IT                                     | `google/gemma-4-31B-it`                              | 49152         | 24576         | 4               | 4               | 4         | 2          | 64            |
| Google       | Gemma 4 31B IT VLM                                 | `google/gemma-4-31B-it-VLM`                          | 24576         | 12288         | 8               | 8               | 8         | 1          | 64            |
| Google       | Gemma 4 26B A4B IT                                 | `google/gemma-4-26B-A4B-it`                          | 49152         | 24576         | 4               | 4               | 4         | 2          | 64            |
| Mistral      | Mixtral 8x7B Instruct v0.1                         | `mistralai/Mixtral-8x7B-Instruct-v0.1`               | 32768         | 16384         | 8               | 8               | 8         | 1          | 64            |

## Full fine-tuning

| Organization | Model                                | API ID                                            | Context (SFT) | Context (DPO) | Max batch (SFT) | Max batch (DPO) | Min batch |
| ------------ | ------------------------------------ | ------------------------------------------------- | ------------- | ------------- | --------------- | --------------- | --------- |
| Qwen         | Qwen3.5 27B                          | `Qwen/Qwen3.5-27B`                                | 32768         | 16384         | 16              | 16              | 16        |
| Qwen         | Qwen3.5 9B                           | `Qwen/Qwen3.5-9B`                                 | 65536         | 49152         | 8               | 8               | 8         |
| Qwen         | Qwen3.5 4B                           | `Qwen/Qwen3.5-4B`                                 | 131072        | 65536         | 8               | 8               | 8         |
| Qwen         | Qwen3.5 2B                           | `Qwen/Qwen3.5-2B`                                 | 131072        | 131072        | 8               | 8               | 8         |
| Qwen         | Qwen3.5 0.8B                         | `Qwen/Qwen3.5-0.8B`                               | 131072        | 131072        | 8               | 8               | 8         |
| Qwen         | Qwen3.6 27B                          | `Qwen/Qwen3.6-27B`                                | 32768         | 16384         | 16              | 16              | 16        |
| Meta         | Llama 3.3 70B Instruct Reference     | `meta-llama/Llama-3.3-70B-Instruct-Reference`     | 24576         | 12288         | 32              | 32              | 32        |
| Meta         | Meta Llama 3.1 8B Instruct Reference | `meta-llama/Meta-Llama-3.1-8B-Instruct-Reference` | 131072        | 65536         | 8               | 8               | 8         |
| Google       | Gemma 4 31B IT                       | `google/gemma-4-31B-it`                           | 49152         | 24576         | 8               | 8               | 8         |
| Google       | Gemma 4 31B IT VLM                   | `google/gemma-4-31B-it-VLM`                       | 24576         | 12288         | 16              | 16              | 16        |
| Mistral      | Mixtral 8x7B Instruct v0.1           | `mistralai/Mixtral-8x7B-Instruct-v0.1`            | 32768         | 16384         | 16              | 16              | 16        |

## Vision-language models

For the list of models that support vision-language fine-tuning on image and text data, along with the dataset schema and the `train_vision` parameter, see [vision fine-tuning](/docs/fine-tuning/vision).

## LoRA target modules

See [LoRA vs. full fine-tuning](/docs/fine-tuning/lora-vs-full#default-target-modules) for the default target modules per model. Pass `lora_trainable_modules="all-linear"` to train every linear layer.
