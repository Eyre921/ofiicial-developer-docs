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

<Note>
  **Serving a LoRA fine-tune:** Fine-tuned adapters are served on [dedicated endpoints](/docs/fine-tuning/deployment), not through the per-token serverless API. Serverless LoRA inference (including Serverless Multi-LoRA) has been discontinued. To serve several adapters on shared hardware, [attach them to a single LoRA-enabled dedicated endpoint](/docs/dedicated-endpoints/v1/lora-adapter).
</Note>

## Choose a method

Use LoRA when:

* **You're starting a new fine-tune:** LoRA gets you a working model fastest and at the lowest cost.
* **You want to ship multiple adapters from the same base:** Adapters are small and can be swapped on a single hosted base model.
* **You're tuning style, format, or domain vocabulary:** These are the kinds of updates that LoRA handles best.

Use full fine-tuning when:

* **The base behavior needs a substantial change:** A model that doesn't know the task you're training for may need every weight updated, not only an adapter.
* **LoRA results plateau below your target:** Try increasing `lora_r` and `lora_alpha` first, and if quality still falls short, switch to full fine-tuning.

## Set the method on your job

The `lora` parameter defaults to `True`. Pass `lora=False` (or `--no-lora` on the CLI) to run a full fine-tune instead. Everything else about the job stays the same.

<CodeGroup>
  ```bash CLI theme={null}
  # LoRA (default)
  tg fine-tuning create \
    --training-file "<FILE_ID>" \
    --model "Qwen/Qwen3.5-27B" \
    --lora

  # Full fine-tuning
  tg fine-tuning create \
    --training-file "<FILE_ID>" \
    --model "Qwen/Qwen3.5-27B" \
    --no-lora
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()

  # LoRA (default) — lora=True is optional
  job = client.fine_tuning.create(
      training_file="<FILE_ID>",
      model="Qwen/Qwen3.5-27B",
      lora=True,
  )

  # Full fine-tuning
  job = client.fine_tuning.create(
      training_file="<FILE_ID>",
      model="Qwen/Qwen3.5-27B",
      lora=False,
  )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  // LoRA (default) — lora: true is optional
  const loraJob = await client.fineTuning.create({
    training_file: "<FILE_ID>",
    model: "Qwen/Qwen3.5-27B",
    lora: true,
  });

  // Full fine-tuning
  const fullJob = await client.fineTuning.create({
    training_file: "<FILE_ID>",
    model: "Qwen/Qwen3.5-27B",
    lora: false,
  });
  ```
</CodeGroup>

## LoRA settings

For the parameters that tune LoRA itself (`lora_r`, `lora_alpha`, `lora_dropout`, `lora_trainable_modules`), see the [fine-tuning API reference](/reference/post-fine-tunes).

## Default target modules

When you don't set `lora_trainable_modules`, it defaults to `all-linear`, which applies LoRA to the modules listed for each model in the tables below. To customize, pass a comma-separated list of module names instead.

Each module you list must appear in the model's allow-list. Whitespace around module names is ignored, but a non-empty value that parses to no modules (for example `","` or `" , "`) is rejected.

<Accordion title="Default target modules by model">
  ### Text models

  | Model                                                | Default target modules                                                                                                                                                                            |
  | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16` | `w_up`, `w_down`                                                                                                                                                                                  |
  | `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`      | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `moonshotai/Kimi-K2.7-Code`                          | `q_a_proj`, `q_b_proj`, `kv_a_proj_with_mqa`, `kv_b_proj`, `mlp.gate_proj`, `mlp.up_proj`, `mlp.down_proj`                                                                                        |
  | `moonshotai/Kimi-K2.6`                               | `q_a_proj`, `q_b_proj`, `kv_a_proj_with_mqa`, `kv_b_proj`, `mlp.gate_proj`, `mlp.up_proj`, `mlp.down_proj`                                                                                        |
  | `zai-org/GLM-5.1`                                    | `q_a_proj`, `q_b_proj`, `kv_a_proj_with_mqa`, `kv_b_proj`, `o_proj`                                                                                                                               |
  | `openai/gpt-oss-20b`                                 | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `openai/gpt-oss-120b`                                | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `deepseek-ai/DeepSeek-V4-Flash`                      | `q_a_proj`, `q_b_proj`, `kv_proj`, `o_b_proj`, `shared_experts.gate_proj`, `shared_experts.up_proj`, `shared_experts.down_proj`                                                                   |
  | `deepseek-ai/DeepSeek-V3.1`                          | `q_a_proj`, `q_b_proj`, `kv_a_proj_with_mqa`, `kv_b_proj`, `mlp.gate_proj`, `mlp.up_proj`, `mlp.down_proj`                                                                                        |
  | `meta-llama/Llama-4-Scout-17B-16E-Instruct`          | `k_proj`, `o_proj`, `q_proj`, `v_proj`, `shared_expert.gate_proj`, `shared_expert.up_proj`, `shared_expert.down_proj`, `feed_forward.gate_proj`, `feed_forward.up_proj`, `feed_forward.down_proj` |
  | `meta-llama/Llama-4-Maverick-17B-128E-Instruct`      | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `meta-llama/Llama-3.3-70B-Instruct-Reference`        | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `meta-llama/Meta-Llama-3.1-8B-Instruct-Reference`    | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `mistralai/Mixtral-8x7B-Instruct-v0.1`               | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `google/gemma-4-31B-it`                              | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `google/gemma-4-26B-A4B-it`                          | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3.5-35B-A3B`                               | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3.5-35B-A3B-Base`                          | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3.5-122B-A10B`                             | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3.5-397B-A17B`                             | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3.6-35B-A3B`                               | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |

  ### Multimodal models

  | Model                                               | Default target modules                                                                                                                                                                            |
  | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `meta-llama/Llama-4-Scout-17B-16E-Instruct-VLM`     | `k_proj`, `o_proj`, `q_proj`, `v_proj`, `shared_expert.gate_proj`, `shared_expert.up_proj`, `shared_expert.down_proj`, `feed_forward.gate_proj`, `feed_forward.up_proj`, `feed_forward.down_proj` |
  | `meta-llama/Llama-4-Maverick-17B-128E-Instruct-VLM` | `k_proj`, `o_proj`, `q_proj`, `v_proj`                                                                                                                                                            |
  | `Qwen/Qwen3.5-0.8B`                                 | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3.5-2B`                                   | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3.5-4B`                                   | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3.5-9B`                                   | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3.5-27B`                                  | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `Qwen/Qwen3.6-27B`                                  | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
  | `google/gemma-4-31B-it-VLM`                         | `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`                                                                                                                       |
</Accordion>

## Target MoE expert layers

On mixture-of-experts (MoE) models, you can apply LoRA to the expert feed-forward projections instead of the attention projections. Set `lora_trainable_modules` to the expert modules `w_up`, `w_gate`, and `w_down` (or `w_up` and `w_down` on gateless models such as Nemotron). Together uses a compact shared-factor adapter layout across experts, so the adapter stays small even on very large models.

Use expert targeting when your task depends on the model's domain knowledge (the feed-forward experts) rather than its attention patterns. For example, adapting an MoE base to a new domain or task family.

<CodeGroup>
  ```bash CLI theme={null}
  tg fine-tuning create \
    --training-file "<FILE_ID>" \
    --model "moonshotai/Kimi-K2.7-Code" \
    --lora \
    --lora-trainable-modules "w_up,w_gate,w_down"
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()

  job = client.fine_tuning.create(
      training_file="<FILE_ID>",
      model="moonshotai/Kimi-K2.7-Code",
      lora=True,
      lora_trainable_modules="w_up,w_gate,w_down",
  )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const job = await client.fineTuning.create({
    training_file: "<FILE_ID>",
    model: "moonshotai/Kimi-K2.7-Code",
    lora: true,
    lora_trainable_modules: "w_up,w_gate,w_down",
  });
  ```
</CodeGroup>

You can't combine expert and attention modules in one job. Pass either the attention projections (the default) or the expert projections, not both, or the job fails validation.

Expert LoRA is available on these models:

* Mixtral: `mistralai/Mixtral-8x7B-Instruct-v0.1`.
* DeepSeek / Kimi: `deepseek-ai/DeepSeek-V3.1`, `moonshotai/Kimi-K2.6`, `moonshotai/Kimi-K2.7-Code`.
* Nemotron (gateless, `w_up` and `w_down` only): `nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16`, `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`.

Every expert-LoRA job produces a LoRA adapter served on top of the base model. Unlike a standard LoRA, an expert-LoRA adapter is never merged into a full set of weights, so deploy it as an adapter on any of the models above. See [adapter upload](/docs/dedicated-endpoints/adapter).

## What to expect from full fine-tuning

* **Supported models:** Full fine-tuning is available for a subset of the models that support LoRA. Large mixture-of-experts models, long-context variants, and some vision-language models are LoRA-only. See [supported models](/docs/fine-tuning/supported-models) for the per-model breakdown.
* **Smaller batch sizes:** Because full fine-tuning updates every weight, it carries a larger memory footprint, so the maximum batch size for a given model is generally smaller than the LoRA equivalent.
* **Higher cost:** Full fine-tuning trains every parameter rather than the 0.1% to 1% a LoRA job touches, so it consumes more compute and costs more. See [pricing](/docs/fine-tuning/pricing) for details.

To check a single model before submitting a job, read `supports_full_training` from the model limits endpoint. When it's `False`, the model is LoRA-only, and passing `lora=False` returns a validation error.

```python theme={null}
from together import Together

client = Together()

limits = client.fine_tuning.model_limits(model_name="<MODEL_ID>")
print(limits.supports_full_training)
```

## Continue training from a checkpoint

Instead of starting from a base model, you can have a new job start from a previously completed job by passing `from_checkpoint`. The [quickstart](/docs/fine-tuning/quickstart#continue-from-a-checkpoint) covers the accepted formats. When the previous job is a LoRA job, the new job handles its adapter in one of two ways:

* **Continue it:** The new job picks up the same adapter and keeps training it. The result is still a single adapter on the original base model.
* **Merge it:** Together folds the adapter into the base model, producing a standalone set of weights, and the new job trains on those instead. The original adapter is no longer a separate, swappable artifact.

The outcome depends on the training type of both jobs:

| Previous job | New job                       | What happens                                                                                       |
| ------------ | ----------------------------- | -------------------------------------------------------------------------------------------------- |
| Full         | Full                          | Training continues on the full weights. No adapter is involved.                                    |
| Full         | LoRA                          | A new adapter trains on top of the previous job's full weights.                                    |
| LoRA         | Full                          | The adapter is merged into the base model, then full fine-tuning trains the merged weights.        |
| LoRA         | LoRA, same LoRA settings      | Training continues on the same adapter.                                                            |
| LoRA         | LoRA, different LoRA settings | The adapter is merged into the base model, then a new adapter with the new settings trains on top. |

The [LoRA settings](#lora-settings) (`lora_r`, `lora_alpha`, `lora_dropout`, and `lora_trainable_modules`) define the adapter's shape, so an adapter can only continue training when all four match the previous job. To guarantee a continuation, omit the training type and the LoRA settings on the new job, so it inherits all of them from the previous job. Any value you set that differs from the previous job triggers a merge instead.

The new job produces a checkpoint based on its own training type. A full fine-tune outputs full model weights (`--checkpoint-type default`). A LoRA job outputs an adapter plus merged weights (`--checkpoint-type adapter` or `merged` on [`tg fine-tuning download`](/reference/cli/finetune#download-model-weights)). The merged weights contain everything trained so far, including any parent adapter that was merged along the way. See [Choose a checkpoint type](/docs/fine-tuning/deployment#choose-a-checkpoint-type) for the SDK equivalents and what each artifact contains.

In two cases the adapter can't be merged, so the platform rejects the new job at creation unless the LoRA settings match the previous job exactly:

* **The previous job started from a Hugging Face model:** The rejection error names the settings that differ.
* **The base model supports LoRA training only:** These models never produce full weights, so there is nothing to merge the adapter into.

## Serve your model

How you deploy depends on the method:

* **LoRA:** After the job completes, deploy the merged model on a dedicated endpoint. See [deployment](/docs/fine-tuning/deployment).
* **Full fine-tuning:** The job produces a complete model rather than a compact adapter. Deploy it on a dedicated endpoint, or download the weights for local use. See [deployment](/docs/fine-tuning/deployment).
