---
title: "Dedicated Training Quickstart"
source: https://docs.fireworks.ai/fine-tuning/training-api/quickstart
path: fine-tuning/training-api/quickstart
---

Provision a trainer and run a custom Training API loop on dedicated Fireworks resources.

This quickstart uses [Dedicated Training](/fine-tuning/training-api/dedicated). For supported LoRA SFT or RL without provisioning, use [Serverless Training](/fine-tuning/training-api/serverless).

## Installation

Install the Fireworks Python package with training extensions:

```bash theme={null}
pip install "fireworks-ai[training]"
pip install "tinker-cookbook==0.4.1"
```

Set your credentials:

```bash theme={null}
export FIREWORKS_API_KEY="your-api-key"
```

<Tip>
  If you want ready-to-run recipes instead of writing a loop from scratch, see [The Cookbook](/fine-tuning/training-api/cookbook/overview) for config-driven GRPO, DPO, and SFT training.
</Tip>

## Your first training loop

This quickstart walks through a minimal SFT loop from scratch using only the API.

For trainer launch, the only shape-specific input you provide is the training shape ID. In most cases, use the full shared path `accounts/fireworks/trainingShapes/<shape>`. The `fireworks` account is the public shared shape catalog. The SDK-managed service client resolves the pinned version, creates or reattaches the trainer, and returns a Tinker-compatible training client.

### Step 1: Create the managed service

```python theme={null}
import os
from fireworks.training.sdk import FiretitanServiceClient

api_key = os.environ["FIREWORKS_API_KEY"]
base_url = os.environ.get("FIREWORKS_BASE_URL", "https://api.fireworks.ai")

base_model = "accounts/fireworks/models/qwen3-8b"
shape_id = "accounts/fireworks/trainingShapes/qwen3-8b-128k-h200"

service = FiretitanServiceClient.from_firetitan_config(
    api_key=api_key,
    base_url=base_url,
    base_model=base_model,
    tokenizer_model="Qwen/Qwen3-8B",
    lora_rank=0,
    training_shape_id=shape_id,
    learning_rate=1e-5,
    create_deployment=False,
    cleanup_trainer_on_close=True,
)
```

### Step 2: Create the training client

```python theme={null}
training_client = service.create_training_client(
    base_model=base_model,
    lora_rank=0,
)
print(f"Trainer job: {service.trainer_job_id}")
```

### Step 3: Build training data

Each training example is a **Datum** — a tokenized sequence with per-token weights indicating which tokens to train on.

```python theme={null}
import tinker
import torch
import transformers
from tinker_cookbook.supervised.common import datum_from_model_input_weights

tokenizer = transformers.AutoTokenizer.from_pretrained(
    "Qwen/Qwen3-8B", trust_remote_code=True,
)

conversation = [
    {"role": "user", "content": "What is the capital of France?"},
    {"role": "assistant", "content": "The capital of France is Paris."},
]

full_text = tokenizer.apply_chat_template(conversation, tokenize=False)
full_tokens = tokenizer.encode(full_text)

prompt_only = tokenizer.apply_chat_template(conversation[:1], tokenize=False)
prompt_len = len(tokenizer.encode(prompt_only))

weights = torch.zeros(len(full_tokens), dtype=torch.float32)
weights[prompt_len:] = 1.0

datum = datum_from_model_input_weights(
    tinker.ModelInput.from_ints(full_tokens),
    weights,
    max_length=4096,
)
```

### Step 4: Write a loss function and train

```python theme={null}
import tinker

def sft_loss(data, logprobs_list):
    total_loss = torch.tensor(0.0)
    n_tokens = 0
    for i, logprobs in enumerate(logprobs_list):
        weights = torch.tensor(
            data[i].loss_fn_inputs["weights"].data, dtype=torch.float32,
        )
        min_len = min(len(logprobs), len(weights))
        total_loss = total_loss - torch.dot(
            logprobs[:min_len].float(), weights[:min_len],
        )
        n_tokens += weights[:min_len].sum().item()
    loss = total_loss / max(n_tokens, 1)
    return loss, {"sft_loss": loss.item(), "n_tokens": n_tokens}

batch = [datum]
for step in range(10):
    result = training_client.forward_backward_custom(batch, sft_loss).result()
    training_client.optim_step(
        tinker.AdamParams(learning_rate=1e-5, beta1=0.9, beta2=0.999, eps=1e-8, weight_decay=0.01)
    ).result()
    print(f"Step {step}: {result.metrics}")
```

### Step 5: Save and promote

```python theme={null}
from datetime import datetime

saved = training_client.save_weights_for_sampler(
    "sft-final",
    checkpoint_type="base",
).result()
print(f"Checkpoint saved: {saved.path}")

# List control-plane checkpoints and select a promotable row.
# The public saved.path can differ from the checkpoint resource ID.
entry = max(
    (
        row
        for row in service.list_checkpoints(service.trainer_job_id)
        if row.get("promotable")
    ),
    key=lambda row: datetime.fromisoformat(
        row["createTime"].replace("Z", "+00:00")
    ),
)
model = service.promote_checkpoint(
    name=entry["name"],
    output_model_id="my-sft-model",
    base_model=base_model,
)

service.close()
```

<Tip>
  For production scripts, set cleanup flags deliberately, call `service.close()` in `try/finally`, and verify the requested final resource state. See [Cleanup and Teardown](/fine-tuning/training-api/reference/cleanup).
</Tip>

## Next steps

* [Training and Sampling](/fine-tuning/training-api/training-and-sampling) — full end-to-end lifecycle with deployment evaluation
* [Loss Functions](/fine-tuning/training-api/loss-functions) — GRPO, DPO, and custom loss function patterns
* [Vision Inputs](/fine-tuning/training-api/vision-inputs) — fine-tune vision-language models with image and text data
* [Saving and Loading](/fine-tuning/training-api/saving-and-loading) — checkpointing and weight sync details
* [The Cookbook](/fine-tuning/training-api/cookbook/overview) — ready-to-run recipes for GRPO, DPO, and SFT
