---
title: "Cookbook: Supervised fine-tuning"
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

SFT datasets are JSONL, with one example per line:

```json theme={null}
{"messages": [
  {"role": "user", "content": "What is the capital of France?"},
  {"role": "assistant", "content": "The capital of France is Paris."}
]}
```

Each line is one JSON object with a `messages` array, and optionally a `tools` array of OpenAI function definitions. This is the OpenAI chat format, so an existing OpenAI SFT dataset works without conversion.

Each message is an object:

* `role`: `system`, `user`, `assistant`, or `tool`.
* `content`: a string, or a list of parts. A text part is `{"type": "text", "text": "..."}`. A thinking part is `{"type": "thinking", "thinking": "..."}`. Image parts are under [Vision datasets](#vision-datasets).
* `tool_calls`: optional on an assistant message, and enough on its own when `content` is omitted. Use `{"type": "function", "function": {"name": "...", "arguments": ...}}`, where `arguments` is a JSON object or a JSON string. `{"name": "...", "args": {...}}` is also accepted.
* `weight`: optional number. On an assistant message, `0` excludes that message from the loss. Weights only remove loss: they can't make other roles trainable, and they don't scale the loss. `trainable` is a boolean for the same switch and wins when both are set.

The recipe trains every assistant message by default and masks system, user, and tool messages. A `tool` message returns a tool result and should set `tool_call_id`.

Assistant reasoning can also be a string field: `thinking`, `reasoning`, or `reasoning_content`. When more than one is set, `thinking` is used, then a non-empty `reasoning`, then a non-empty `reasoning_content`. Whether earlier reasoning stays in later turns depends on the base model. See [Thinking history in training](/fine-tuning/thinking-history).

```json theme={null}
{"tools": [{"type": "function", "function": {"name": "get_car_specs", "parameters": {"type": "object", "properties": {"trimid": {"type": "integer"}}}}}],
 "messages": [
   {"role": "user", "content": "Specs for trim 121?"},
   {"role": "assistant", "reasoning_content": "Look up the trim.", "tool_calls": [
     {"id": "call_1", "type": "function", "function": {"name": "get_car_specs", "arguments": "{\"trimid\": 121}"}}
   ]},
   {"role": "tool", "tool_call_id": "call_1", "content": "{\"horsepower\": 300}"},
   {"role": "assistant", "content": "300 hp.", "weight": 1}
 ]}
```

Rows that are longer than `max_seq_len` once rendered, or that have no trainable tokens, are skipped.

### Vision datasets

Vision SFT uses the same `messages` JSONL with image parts. Put images on `user` messages. Some models also accept images on other roles, and some reject them on `system`, `assistant`, or `tool` messages, depending on the model's renderer.

These parts are the same image:

* `{"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,..."}}`
* `{"type": "image_url", "image_url": "data:image/jpeg;base64,..."}`
* `{"type": "image", "image": "data:image/jpeg;base64,..."}`

```json theme={null}
{"messages": [
  {"role": "user", "content": [
    {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,..."}},
    {"type": "text", "text": "Extract the total from this receipt."}
  ]},
  {"role": "assistant", "content": "{\"total\": \"12.40\"}"}
]}
```

* A `data:image/<type>;base64,...` URI is decoded on your machine. Keep its MIME type accurate, such as `image/jpeg` or `image/png`.
* An `http` or `https` URL is downloaded by your machine while the recipe renders the row. It must be publicly reachable, and each image can be up to 20 MB.
* Image tokens count toward `max_seq_len`, so leave headroom.

Pick a base model that supports images, and set `tokenizer_model` to its Hugging Face processor. [Models](/fine-tuning/models) shows which models support vision.

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

The `init_from_checkpoint` format depends on where the trainer runs:

* **Dedicated trainer (this example):** `<job-id>:<checkpoint-name>`, or a bare checkpoint name on the current trainer.
* **[Serverless](/fine-tuning/training-api/serverless):** a bare checkpoint name for the current run, or `<account>/<run-id>/<checkpoint-name>` for a checkpoint from another run, where `run-id` is the previous run's `run-<hex>` ID. Serverless doesn't accept another run's `<job-id>:<checkpoint-name>`.

Neither accepts `cross_job://` references, URIs, or absolute paths in `init_from_checkpoint`.

## Operational guidance

* **Set `trainer.training_shape_id`** — cookbook trainer launches use training shapes.
* **Only one trainer job needed** — SFT does not require a reference trainer.
* **No sampling deployment is required by default** — optional generation evaluation uses the SDK-managed sampler.
* **Use `batch_size`** to control the number of examples per optimizer step.
* **Resume**: Attach to the same trainer with `TrainerConfig(job_id=...)` and keep the same `log_path`; the recipe restores the saved training state and data cursor. See [checkpoints](/fine-tuning/training-api/cookbook/reference#checkpoints).
* **Periodic checkpoints are disabled by default** (`dcp_save_interval=0`); successful runs save final state by default. Set a positive interval (e.g., `50`) to recover progress from an interrupted run.

## Check tokenization

If the model learns the wrong text or ignores assistant turns, check what the trainer actually sees. Set `render_samples_file` to write rendered examples to a JSONL file:

```python theme={null}
cfg = Config(
    # ... other fields ...
    render_samples_file="./sft_logs/render_samples.jsonl",
)
```

The file holds 20 examples by default. Set `render_samples_limit` to change that, or to a negative number to write every example. It's written when the run ends. Each record has the source line (`source_jsonl_line_number`), `decoded_tokens`, and `token_weights` (`0` means the token isn't trained).

| What you see | Likely cause | What to do |
| - | - | - |
| Assistant answer tokens have `token_weights` of `0` | That message has `weight: 0` or `trainable: false` | Remove the flag from the row |
| User or system tokens have positive weights | A role is wrong, or assistant text is in a `user` message | Fix the roles in the row |
| A row is missing from the file, with `render_samples_limit` set to a negative number | It was skipped: longer than `max_seq_len`, or no trainable tokens | Shorten the row, raise `max_seq_len`, or check its weights |
| Extra special tokens around messages | The model's chat template adds them | Usually expected |
| Earlier reasoning is missing from later turns | The model's thinking history mode removes it | See [Thinking history in training](/fine-tuning/thinking-history) |

To check a custom renderer against Hugging Face, use the training skill's [renderer verification reference](https://github.com/fw-ai-external/cookbook/blob/main/skills/fireworks-training/references/renderer-verification.md).

## Related guides

* [Vision datasets](#vision-datasets) — image parts and image URLs in SFT data
* [Cookbook DPO](/fine-tuning/training-api/cookbook/dpo) — preference optimization
* [Cookbook RL (GRPO)](/fine-tuning/training-api/cookbook/rl) — reinforcement learning recipes
* [Cookbook Reference](/fine-tuning/training-api/cookbook/reference) — all config classes and parameters
* [Loss Functions](/fine-tuning/training-api/dedicated#loss-functions) — API-level SFT loss details
