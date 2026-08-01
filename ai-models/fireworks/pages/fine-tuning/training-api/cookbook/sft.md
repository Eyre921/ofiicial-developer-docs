---
title: "Cookbook: SFT"
source: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/sft
path: fine-tuning/training-api/cookbook/sft
---

Supervised fine-tuning via the cookbook's sft_loop recipe.

## What this is

Supervised Fine-Tuning (SFT) trains the model to produce desired outputs by minimizing cross-entropy loss on (prompt, response) pairs. The cookbook's `sft_loop` recipe handles data loading, tokenization, batching, gradient accumulation, and checkpointing automatically.

## Using the recipe

```python theme={null}
from training.recipes.sft_loop import Config, main
from training.utils import TrainerConfig

cfg = Config(
    log_path="./sft_logs",
    base_model="accounts/fireworks/models/qwen3-8b",
    dataset="/path/to/training_data.jsonl",
    tokenizer_model="Qwen/Qwen3-8B",
    max_seq_len=4096,
    epochs=1,
    batch_size=4,
    learning_rate=1e-5,
    trainer=TrainerConfig(
        training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k",
    ),
)

main(cfg)
```

<Warning>
  **`batch_size_samples` is not supported in the V2 SFT `CookbookTrainingConfig`.**

  Passing `batch_size_samples` to the V2 config has no effect — the parameter is accepted without error but silently ignored, which can lead to unexpected step counts.

  **How batching works in V2:** Steps are calculated as:

  ```
  steps = (num_samples × num_epochs) / batch_size
  ```

  where `batch_size` is set by the training shape and the recipe’s `batch_size` field — not by `batch_size_samples`.

  **Example:** 10 samples × 5 epochs ÷ batch size of 10 = **5 steps**, not 50.

  To control training length, adjust `epochs` (and related recipe fields). Contact support for custom batch size configurations.
</Warning>

## Dataset format

SFT datasets use the standard messages format (JSONL with one example per line):

```json theme={null}
{"messages": [
  {"role": "user", "content": "What is the capital of France?"},
  {"role": "assistant", "content": "The capital of France is Paris."}
]}
```

Multi-turn conversations are supported:

```json theme={null}
{"messages": [
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "Hello"},
  {"role": "assistant", "content": "Hi! How can I help?"},
  {"role": "user", "content": "What is 2+2?"},
  {"role": "assistant", "content": "2+2 = 4"}
]}
```

The recipe automatically tokenizes conversations using the chat template, setting token weights to `0.0` for prompt tokens and `1.0` for response tokens.

### Vision datasets

The SFT recipe also supports vision-language model fine-tuning. Use multimodal `content` arrays with `image_url` objects in your JSONL, and specify a VLM training shape and tokenizer. See [Vision Inputs](/fine-tuning/training-api/vision-inputs) for dataset format details and a full walkthrough.

## Checkpointing and resume

The current `sft_loop` recipe manages the trainer-side loop only. It does **not** create a deployment or run weight sync during training, but it does expose DCP checkpointing and resume controls:

```python theme={null}
from training.utils import TrainerConfig, WandBConfig

cfg = Config(
    log_path="./sft_logs",
    base_model="accounts/fireworks/models/qwen3-8b",
    dataset="/path/to/training_data.jsonl",
    tokenizer_model="Qwen/Qwen3-8B",
    max_seq_len=4096,
    epochs=1,
    batch_size=4,
    trainer=TrainerConfig(
        training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k",
    ),
    dcp_save_interval=50,
    init_from_checkpoint="previous-job-id:step-100",  # optional
    wandb=WandBConfig(entity="my-team", project="sft-experiment"),
)

main(cfg)
```

## Operational guidance

* **Set `trainer.training_shape_id`** — cookbook trainer launches use training shapes.
* **Only one trainer job needed** — SFT does not require a reference trainer.
* **The current recipe does not provision a deployment** — use the API directly if you want deployment-side evaluation or weight sync during SFT.
* **Use `batch_size`** to control the number of examples per optimizer step.
* **Resume**: The recipe uses `checkpoint_utils.resolve_resume()` to automatically restore from the last saved state on restart.
* **DCP checkpoints are disabled by default** (`dcp_save_interval=0`). If you need to resume training from a checkpoint, you must explicitly set `dcp_save_interval` to a positive value (e.g., `dcp_save_interval=50`).

## Related guides

* [Vision Inputs](/fine-tuning/training-api/vision-inputs) — VLM fine-tuning with image and text data
* [Cookbook DPO](/fine-tuning/training-api/cookbook/dpo) — preference optimization
* [Cookbook RL (GRPO)](/fine-tuning/training-api/cookbook/rl) — reinforcement learning recipes
* [Cookbook Reference](/fine-tuning/training-api/cookbook/reference) — all config classes and parameters
* [Loss Functions](/fine-tuning/training-api/loss-functions) — API-level SFT loss details
