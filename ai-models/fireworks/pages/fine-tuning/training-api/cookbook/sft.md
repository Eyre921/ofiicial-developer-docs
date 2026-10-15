---
title: "Supervised fine-tuning with the sft_loop cookbook recipe"
source: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/sft
path: fine-tuning/training-api/cookbook/sft
---

Run supervised fine-tuning on Fireworks using the cookbook sft_loop recipe to handle dataset loading, tokenization, gradient accumulation, and checkpointing.

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

`batch_size` controls examples per optimizer batch. SFT keeps controlled dataset
batches and does not need rollout streaming.

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

The recipe automatically tokenizes conversations using the chat template, masking context tokens and normalizing trainable response loss within each example.

### Vision datasets

The SFT recipe also supports vision-language model training. Use multimodal `content` arrays with `image_url` objects in your JSONL, and specify a VLM training shape and tokenizer. See [Vision Inputs](/fine-tuning/models) for dataset format details and a full walkthrough.

## Checkpointing and resume

By default, `sft_loop` needs only a trainer. It supports DCP checkpointing and resume; optional `generation_eval=True` samples held-out text after training using SDK-managed sampling resources:

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
* **No sampling deployment is required by default** — optional generation evaluation uses the SDK-managed sampler.
* **Use `batch_size`** to control the number of examples per optimizer step.
* **Resume**: Attach to the same trainer with `TrainerConfig(job_id=...)` and keep the same `log_path`; the recipe restores the saved training state and data cursor. See [checkpoints](/fine-tuning/training-api/cookbook/reference#checkpoints).
* **Periodic checkpoints are disabled by default** (`dcp_save_interval=0`); successful runs save final state by default. Set a positive interval (e.g., `50`) to recover progress from an interrupted run.

## Related guides

* [Vision Inputs](/fine-tuning/models) — VLM training with image and text data
* [Cookbook DPO](/fine-tuning/training-api/cookbook/dpo) — preference optimization
* [Cookbook RL (GRPO)](/fine-tuning/training-api/cookbook/rl) — reinforcement learning recipes
* [Cookbook Reference](/fine-tuning/training-api/cookbook/reference) — all config classes and parameters
* [Loss Functions](/fine-tuning/training-api/dedicated#loss-functions) — API-level SFT loss details
