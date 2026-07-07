---
title: "LoRA vs. full fine-tuning"
source: https://docs.together.ai/docs/fine-tuning/lora-vs-full
path: docs/fine-tuning/lora-vs-full
---

Choose between LoRA and full fine-tuning, then tune LoRA's rank and target modules.

Together AI supports two fine-tuning implementations:

* **LoRA:** Trains a small set of adapter weights on top of the frozen base model.
* **Full fine-tuning:** Updates every weight in the base model.

LoRA is the default on Together AI, because it trains 0.1% to 1% of the parameters that full fine-tuning would, costs less, and produces a compact adapter rather than a full set of model weights.

Both [supervised fine-tuning](/docs/fine-tuning/supervised) and [preference fine-tuning](/docs/fine-tuning/preference-tuning) support LoRA and full fine-tuning.

## Choose a method

Use LoRA when:

* **You're starting a new fine-tune:** LoRA gets you a working model fastest and at the lowest cost.
* **You want to ship multiple adapters from the same base:** Adapters are small and can be swapped on a single hosted base model.
* **You're tuning style, format, or domain vocabulary:** These are the kinds of updates that LoRA handles best.

Use full fine-tuning when:

* **The base behavior needs a substantial change:** A model that doesn't know the task you're training for may need every weight updated, not just an adapter.
* **LoRA results plateau below your target:** Try increasing `lora_r` and `lora_alpha` first, and if quality still falls short, switch to full fine-tuning.

## Set the method on your job

The `lora` parameter defaults to `True`. Pass `lora=False` (or `--no-lora` on the CLI) to run a full fine-tune instead. Everything else about the job stays the same.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  # LoRA (default) — lora=True is optional
  job = client.fine_tuning.create(
      training_file="<FILE_ID>",
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
      lora=True,
  )

  # Full fine-tuning
  job = client.fine_tuning.create(
      training_file="<FILE_ID>",
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
      lora=False,
  )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  // LoRA (default) — lora: true is optional
  const loraJob = await client.fineTuning.create({
    training_file: "<FILE_ID>",
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
    lora: true,
  });

  // Full fine-tuning
  const fullJob = await client.fineTuning.create({
    training_file: "<FILE_ID>",
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
    lora: false,
  });
  ```

  ```bash CLI theme={null}
  # LoRA (default)
  tg fine-tuning create \
    --training-file "<FILE_ID>" \
    --model "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference" \
    --lora

  # Full fine-tuning
  tg fine-tuning create \
    --training-file "<FILE_ID>" \
    --model "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference" \
    --no-lora
  ```
</CodeGroup>

## LoRA settings

For the parameters that tune LoRA itself (`lora_r`, `lora_alpha`, `lora_dropout`, `lora_trainable_modules`), see the [fine-tuning API reference](/reference/post-fine-tunes).

## Default target modules

When you don't set `lora_trainable_modules`, it defaults to `all-linear`, which applies LoRA to the modules listed for each model in the tables below. To customize, pass a comma-separated list of module names instead.

<Accordion title="Default target modules by model">
  ### Text models

  | Model                                                   | Default target modules                                                                                                                                                                            |
  | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `togethercomputer/llama-2-7b-chat`                      | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Meta-Llama-3-8B`                            | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Meta-Llama-3-8B-Instruct`                   | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Meta-Llama-3-70B-Instruct`                  | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Meta-Llama-3.1-8B-Reference`                | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Meta-Llama-3.1-8B-Instruct-Reference`       | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Meta-Llama-3.1-8B-131k-Reference`           | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Meta-Llama-3.1-8B-131k-Instruct-Reference`  | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Meta-Llama-3.1-70B-Reference`               | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Meta-Llama-3.1-70B-Instruct-Reference`      | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Meta-Llama-3.1-70B-32k-Reference`           | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Meta-Llama-3.1-70B-32k-Instruct-Reference`  | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Meta-Llama-3.1-70B-131k-Reference`          | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Meta-Llama-3.1-70B-131k-Instruct-Reference` | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Llama-3.2-1B`                               | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Llama-3.2-1B-Instruct`                      | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Llama-3.2-3B`                               | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Llama-3.2-3B-Instruct`                      | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Llama-3.3-70B-Instruct-Reference`           | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Llama-3.3-70B-32k-Instruct-Reference`       | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Llama-3.3-70B-131k-Instruct-Reference`      | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Llama-4-Scout-17B-16E`                      | `k_proj`, `o_proj`, `q_proj`, `v_proj`, `shared_expert.gate_proj`, `shared_expert.up_proj`, `shared_expert.down_proj`, `feed_forward.gate_proj`, `feed_forward.up_proj`, `feed_forward.down_proj` |
  | `meta-llama/Llama-4-Scout-17B-16E-Instruct`             | `k_proj`, `o_proj`, `q_proj`, `v_proj`, `shared_expert.gate_proj`, `shared_expert.up_proj`, `shared_expert.down_proj`, `feed_forward.gate_proj`, `feed_forward.up_proj`, `feed_forward.down_proj` |
  | `meta-llama/Llama-4-Maverick-17B-128E`                  | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `meta-llama/Llama-4-Maverick-17B-128E-Instruct`         | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `mistralai/Mistral-7B-v0.1`                             | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `mistralai/Mistral-7B-Instruct-v0.2`                    | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `mistralai/Mixtral-8x7B-v0.1`                           | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `mistralai/Mixtral-8x7B-Instruct-v0.1`                  | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen2-1.5B`                                       | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen2-1.5B-Instruct`                              | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen2-7B`                                         | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen2-7B-Instruct`                                | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen2-72B`                                        | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen2-72B-Instruct`                               | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen2.5-1.5B`                                     | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen2.5-1.5B-Instruct`                            | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen2.5-3B`                                       | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen2.5-3B-Instruct`                              | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen2.5-7B`                                       | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen2.5-7B-Instruct`                              | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen2.5-14B`                                      | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen2.5-14B-Instruct`                             | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen2.5-32B`                                      | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen2.5-32B-Instruct`                             | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen2.5-72B`                                      | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen2.5-72B-Instruct`                             | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3-0.6B-Base`                                  | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3-0.6B`                                       | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3-1.7B-Base`                                  | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3-1.7B`                                       | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3-4B-Base`                                    | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3-4B`                                         | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3-8B-Base`                                    | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3-8B`                                         | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3-14B-Base`                                   | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3-14B`                                        | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3-32B`                                        | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3-30B-A3B-Base`                               | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3-30B-A3B`                                    | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3-30B-A3B-Instruct-2507`                      | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3-235B-A22B`                                  | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3-235B-A22B-Instruct-2507`                    | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3-Coder-30B-A3B-Instruct`                     | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3-Coder-480B-A35B-Instruct`                   | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3-Next-80B-A3B-Instruct`                      | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3-Next-80B-A3B-Thinking`                      | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `google/gemma-3-270m`                                   | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `google/gemma-3-270m-it`                                | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `google/gemma-3-1b-it`                                  | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `google/gemma-3-1b-pt`                                  | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `google/gemma-3-4b-it`                                  | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `google/gemma-3-4b-pt`                                  | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `google/gemma-3-12b-it`                                 | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `google/gemma-3-12b-pt`                                 | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `google/gemma-3-27b-it`                                 | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `google/gemma-3-27b-pt`                                 | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B`             | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`              | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `deepseek-ai/DeepSeek-R1-Distill-Llama-70B`             | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `deepseek-ai/DeepSeek-R1-Distill-Llama-70B-32k`         | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `deepseek-ai/DeepSeek-R1-Distill-Llama-70B-131k`        | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `deepseek-ai/DeepSeek-V3`                               | `q_a_proj`, `q_b_proj`, `kv_a_proj_with_mqa`, `kv_b_proj`, `mlp.gate_proj`, `mlp.up_proj`, `mlp.down_proj`                                                                                        |
  | `deepseek-ai/DeepSeek-R1`                               | `q_a_proj`, `q_b_proj`, `kv_a_proj_with_mqa`, `kv_b_proj`, `mlp.gate_proj`, `mlp.up_proj`, `mlp.down_proj`                                                                                        |
  | `deepseek-ai/DeepSeek-V3-Base`                          | `q_a_proj`, `q_b_proj`, `kv_a_proj_with_mqa`, `kv_b_proj`, `mlp.gate_proj`, `mlp.up_proj`, `mlp.down_proj`                                                                                        |
  | `deepseek-ai/DeepSeek-V3-0324`                          | `q_a_proj`, `q_b_proj`, `kv_a_proj_with_mqa`, `kv_b_proj`, `mlp.gate_proj`, `mlp.up_proj`, `mlp.down_proj`                                                                                        |
  | `deepseek-ai/DeepSeek-R1-0528`                          | `q_a_proj`, `q_b_proj`, `kv_a_proj_with_mqa`, `kv_b_proj`, `mlp.gate_proj`, `mlp.up_proj`, `mlp.down_proj`                                                                                        |
  | `deepseek-ai/DeepSeek-V3.1-Base`                        | `q_a_proj`, `q_b_proj`, `kv_a_proj_with_mqa`, `kv_b_proj`, `mlp.gate_proj`, `mlp.up_proj`, `mlp.down_proj`                                                                                        |
  | `deepseek-ai/DeepSeek-V3.1`                             | `q_a_proj`, `q_b_proj`, `kv_a_proj_with_mqa`, `kv_b_proj`, `mlp.gate_proj`, `mlp.up_proj`, `mlp.down_proj`                                                                                        |
  | `moonshotai/Kimi-K2-Instruct`                           | `q_a_proj`, `q_b_proj`, `kv_a_proj_with_mqa`, `kv_b_proj`, `mlp.gate_proj`, `mlp.up_proj`, `mlp.down_proj`                                                                                        |
  | `moonshotai/Kimi-K2-Thinking`                           | `q_a_proj`, `q_b_proj`, `kv_a_proj_with_mqa`, `kv_b_proj`, `mlp.gate_proj`, `mlp.up_proj`, `mlp.down_proj`                                                                                        |
  | `moonshotai/Kimi-K2-Base`                               | `q_a_proj`, `q_b_proj`, `kv_a_proj_with_mqa`, `kv_b_proj`, `mlp.gate_proj`, `mlp.up_proj`, `mlp.down_proj`                                                                                        |
  | `moonshotai/Kimi-K2-Instruct-0905`                      | `q_a_proj`, `q_b_proj`, `kv_a_proj_with_mqa`, `kv_b_proj`, `mlp.gate_proj`, `mlp.up_proj`, `mlp.down_proj`                                                                                        |
  | `moonshotai/Kimi-K2.5`                                  | `q_a_proj`, `q_b_proj`, `kv_a_proj_with_mqa`, `kv_b_proj`, `mlp.gate_proj`, `mlp.up_proj`, `mlp.down_proj`                                                                                        |
  | `openai/gpt-oss-20b`                                    | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `openai/gpt-oss-120b`                                   | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `zai-org/GLM-4.6`                                       | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `zai-org/GLM-4.7`                                       | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |

  ### Multimodal models

  | Model                                               | Default target modules                                                                                                                                                                            |
  | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `meta-llama/Llama-4-Scout-17B-16E-Instruct-VLM`     | `k_proj`, `o_proj`, `q_proj`, `v_proj`, `shared_expert.gate_proj`, `shared_expert.up_proj`, `shared_expert.down_proj`, `feed_forward.gate_proj`, `feed_forward.up_proj`, `feed_forward.down_proj` |
  | `meta-llama/Llama-4-Maverick-17B-128E-Instruct-VLM` | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3-VL-8B-Instruct`                         | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3-VL-32B-Instruct`                        | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3-VL-30B-A3B-Instruct`                    | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3-VL-235B-A22B-Instruct`                  | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3.5-35B-A3B`                              | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3.5-35B-A3B-Base`                         | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3.5-122B-A10B`                            | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3.5-397B-A17B`                            | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `google/gemma-3-4b-it-VLM`                          | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `google/gemma-3-12b-it-VLM`                         | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `google/gemma-3-27b-it-VLM`                         | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `google/gemma-4-31B-it-VLM`                         | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
</Accordion>

## What to expect from full fine-tuning

* **Supported models:** Full fine-tuning is available for a subset of the models that support LoRA. Large mixture-of-experts models, long-context variants, and some vision-language models are LoRA-only. See [supported models](/docs/fine-tuning/supported-models) for the per-model breakdown.
* **Smaller batch sizes:** Because full fine-tuning updates every weight, it carries a larger memory footprint, so the maximum batch size for a given model is generally smaller than the LoRA equivalent.
* **Higher cost:** Full fine-tuning trains every parameter rather than the 0.1% to 1% a LoRA job touches, so it consumes more compute and costs more. See [pricing](/docs/fine-tuning/pricing) for details.

## Serve your model

How you deploy depends on the method:

* **LoRA:** After the job completes, deploy the merged model on a dedicated endpoint, or upload just the adapter and serve it on a dedicated endpoint that runs it on top of the base model. See [deployment](/docs/fine-tuning/deployment) and [adapter upload](/docs/dedicated-endpoints/adapter).
* **Full fine-tuning:** The job produces a complete model rather than a compact adapter. Deploy it on a dedicated endpoint, or download the weights for local use. See [deployment](/docs/fine-tuning/deployment).
