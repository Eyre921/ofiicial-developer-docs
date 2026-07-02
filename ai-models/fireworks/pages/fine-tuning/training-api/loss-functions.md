---
title: "Loss Functions"
source: https://docs.fireworks.ai/fine-tuning/training-api/loss-functions
path: fine-tuning/training-api/loss-functions
---

Built-in loss functions and custom objectives via forward_backward_custom.

## What this is

The Training API supports two ways to compute loss:

1. **Built-in losses** via `forward_backward` with a string identifier (e.g. `"cross_entropy"`) — fastest, no extra forward pass needed.
2. **Custom losses** via `forward_backward_custom` with an arbitrary Python function — flexible, supports any differentiable objective at the cost of an additional forward pass.

## Built-in loss: cross\_entropy

For supervised fine-tuning, use the built-in `cross_entropy` loss via `forward_backward`:

```python theme={null}
result = training_client.forward_backward(datums, "cross_entropy").result()
```

This computes standard next-token prediction loss on the server side — no extra forward pass or local loss computation needed.

For built-in `cross_entropy`, the SDK backfills `result.metrics["response_tokens"]` so you can compute a mean loss from sum-style metrics when needed.

<Warning>
  Built-in `cross_entropy` requires datums with `target_tokens` in `loss_fn_inputs`. Datums built with `datum_from_model_input_weights` (weight-based) will fail with `"missing required field 'target_tokens'"`. For built-in `cross_entropy`, use the target-token `tinker.Datum` format in the `Using tinker.Datum directly (target-token-based)` section below. If you want to keep weight-based datums, use `forward_backward_custom` with the weight-based format in [Building datums](#building-datums) and the custom-loss pattern in [Example: simple cross-entropy](#example-simple-cross-entropy).
</Warning>

For a **forward-only pass** (e.g. to compute reference logprobs without updating weights):

```python theme={null}
result = training_client.forward(datums, "cross_entropy").result()
ref_logprobs = [result.loss_fn_outputs[i]["logprobs"].data for i in range(len(datums))]
```

## Custom losses: forward\_backward\_custom

`forward_backward_custom` lets you implement any objective function in Python. You provide the loss computation; the API handles the forward pass on remote GPUs, passes logprobs back to your function, then sends the computed gradients back for the backward pass.

### How it works

1. You call `training_client.forward_backward_custom(datums, loss_fn)`.
2. The trainer runs a forward pass on the GPU and returns per-token logprobs.
3. The logprobs are converted to PyTorch tensors with `requires_grad=True`.
4. Your `loss_fn` is called with the datums and logprobs.
5. The API calls `loss.backward()` to compute `d_loss/d_logprob` gradients.
6. Gradients are sent back to the trainer GPU for the model backward pass.

Your loss function runs **locally** (on your machine), while the forward and backward passes run on **remote GPUs**.

<Note>
  `forward_backward_custom` does an extra forward pass compared to `forward_backward`, requiring \~1.5x FLOPs and up to \~3x wall time per step.
</Note>

### Embedding-space custom losses

For objectives that operate on pooled hidden states instead of logprobs, pass `output="embedding"` and `pooling="mean"` or `"last"`:

```python theme={null}
def embedding_loss(data, embeddings):
    loss = compute_embedding_objective(embeddings)
    return loss, {"embedding_loss": float(loss.item())}

result = training_client.forward_backward_custom(
    datums,
    embedding_loss,
    output="embedding",
    pooling="mean",
).result()
```

### Loss function signature

```python theme={null}
def loss_fn(
    data: list[tinker.Datum],
    logprobs_list: list[torch.Tensor],
) -> tuple[torch.Tensor, dict[str, float]]:
    """
    Args:
        data: The same datums you passed to forward_backward_custom.
              Access token weights via data[i].loss_fn_inputs["weights"].data
        logprobs_list: Per-token log-probabilities from the forward pass.
              Each tensor has requires_grad=True. Shape: (seq_len,) per sequence.

    Returns:
        loss: A scalar tensor. Must be differentiable w.r.t. logprobs_list entries.
        metrics: A dict of float values for logging (not used for training).
    """
```

### Key rules

* **`logprobs_list[i]`** has `requires_grad=True` — your loss must be differentiable through it.
* **Use `torch.dot()`** to compute weighted sums — this correctly propagates gradients through the logprobs.
* **Return a scalar tensor** as the loss, and a `dict[str, float]` as metrics.
* **Access token weights** via `data[i].loss_fn_inputs["weights"].data` — these are `0` for prompt tokens and `1` for response tokens.

## Building datums

### Using tinker\_cookbook (weight-based)

`datum_from_model_input_weights` constructs datums with explicit token weights:

```python theme={null}
import tinker
import torch
from tinker_cookbook.supervised.common import datum_from_model_input_weights

tokens = [101, 2054, 2003, ...]
weights = torch.zeros(len(tokens), dtype=torch.float32)
weights[prompt_len:] = 1.0  # Only train on response tokens

datum = datum_from_model_input_weights(tinker.ModelInput.from_ints(tokens), weights, max_length=8192)
```

### Using tinker.Datum directly (target-token-based)

For RL-style objectives where you need per-completion control (e.g. routing matrices, custom `loss_fn_inputs`), construct datums directly:

```python theme={null}
import tinker

model_input_len = len(tokens) - 1
datum = tinker.Datum(
    model_input=tinker.ModelInput.from_ints(tokens[:-1]),
    loss_fn_inputs={
        "target_tokens": tinker.TensorData(
            data=tokens[1:], dtype="int64", shape=[model_input_len],
        ),
    },
)
```

### Multi-target cross-entropy

For sparse distillation objectives, built-in `cross_entropy` also supports
multiple candidate target tokens per model position. In this mode,
`target_tokens` has shape `[N, K]`, where:

* `N` is the number of model input positions.
* `K` is the number of candidate targets per position.
* `target_tokens.data` is flattened row-major and must contain `N * K` token ids.

If you provide `weights`, it must describe the same flattened target entries as
`target_tokens.data`. That means `weights.data` must contain exactly the same
number of values as `target_tokens.data` (`N * K` values), in the same row-major
order, with one weight per candidate target.

```python theme={null}
import tinker

tokens = [101, 2054, 2003, 1029]
model_input = tokens[:-1]

# Two candidate next-token targets for each model input position.
target_tokens_NK = [
    2054, 2055,  # candidates for position 0
    2003, 2004,  # candidates for position 1
    1029, 1030,  # candidates for position 2
]

weights_NK = [
    0.9, 0.1,
    0.8, 0.2,
    1.0, 0.0,
]

datum = tinker.Datum(
    model_input=tinker.ModelInput.from_ints(model_input),
    loss_fn_inputs={
        "target_tokens": tinker.TensorData(
            data=target_tokens_NK,
            dtype="int64",
            shape=[len(model_input), 2],
        ),
        "weights": tinker.TensorData(
            data=weights_NK,
            dtype="float32",
            shape=[len(model_input), 2],
        ),
    },
)

result = training_client.forward_backward([datum], "cross_entropy").result()
```

<Warning>
  If `target_tokens.shape == [N, K]`, any supplied `weights` must have the same
  flattened length and layout as `target_tokens.data`. `weights` is optional, but
  when supplied it must have one value per flattened candidate target (`N * K`
  values), aligned with `target_tokens.data`.

  A common mistake is sending one weight per model position (`N` values) while
  `target_tokens` contains multiple candidate targets per position (`N * K`
  values). Any other mismatch in flattening, padding, truncation, or filtering
  between these two fields is also invalid.
</Warning>

## Example: simple cross-entropy

```python theme={null}
def cross_entropy_loss(data, logprobs_list):
    total_loss = torch.tensor(0.0)
    for i, logprobs in enumerate(logprobs_list):
        weights = torch.tensor(data[i].loss_fn_inputs["weights"].data, dtype=torch.float32)
        min_len = min(len(logprobs), len(weights))
        weighted_sum = torch.dot(logprobs[:min_len].float(), weights[:min_len])
        total_loss = total_loss - weighted_sum  # Negative log-likelihood
    loss = total_loss / len(logprobs_list)
    return loss, {"cross_entropy": loss.item()}

result = training_client.forward_backward_custom(datums, cross_entropy_loss).result()
```

## Example: GRPO with KL penalty

```python theme={null}
def make_grpo_loss(rewards, ref_logprobs, kl_beta=0.001):
    advantages = compute_advantages(rewards)
    ref_tensors = [torch.tensor(lp, dtype=torch.float32) for lp in ref_logprobs]

    def loss_fn(data, logprobs_list):
        total_loss = torch.tensor(0.0)
        for i in range(len(logprobs_list)):
            weights = torch.tensor(data[i].loss_fn_inputs["weights"].data, dtype=torch.float32)
            pi = logprobs_list[i][:len(weights)]
            ref = ref_tensors[i][:len(weights)]

            pg_loss = -advantages[i] * torch.dot(pi.float(), weights)
            kl_term = torch.dot((pi - ref).float(), weights)
            total_loss = total_loss + pg_loss + kl_beta * kl_term

        return total_loss / len(logprobs_list), {"loss": (total_loss / len(logprobs_list)).item()}

    return loss_fn
```

## Example: DPO margin loss

```python theme={null}
import torch.nn.functional as F

def make_dpo_loss(ref_chosen, ref_rejected, beta=0.1):
    ref_c = torch.tensor(ref_chosen, dtype=torch.float32)
    ref_r = torch.tensor(ref_rejected, dtype=torch.float32)

    def loss_fn(data, logprobs_list):
        pi_c, pi_r = logprobs_list[0], logprobs_list[1]
        w_c = torch.tensor(data[0].loss_fn_inputs["weights"].data, dtype=torch.float32)
        w_r = torch.tensor(data[1].loss_fn_inputs["weights"].data, dtype=torch.float32)

        margin = (torch.dot(pi_c.float(), w_c) - torch.dot(ref_c, w_c)) - \
                 (torch.dot(pi_r.float(), w_r) - torch.dot(ref_r, w_r))

        return -F.logsigmoid(beta * margin), {"margin": margin.item()}

    return loss_fn
```

## Built-in loss methods: GRPO vs DAPO vs GSPO-token

When using the managed RFT flow or the cookbook's RL recipe, three built-in loss methods are available via `--rl-loss-method`:

| Method           | Clipping                      | KL penalty    | Loss aggregation    | Importance sampling |
| ---------------- | ----------------------------- | ------------- | ------------------- | ------------------- |
| `grpo` (default) | Symmetric `[0.8, 1.2]`        | Yes (`0.001`) | Token-mean          | Token-level         |
| `dapo`           | Asymmetric `[0.8, 1.28]`      | No            | Token-mean          | Token-level         |
| `gspo-token`     | Very tight `[1-3e-4, 1+4e-4]` | No            | Seq-mean-token-mean | Sequence-level      |

**GRPO** ([arXiv:2402.03300](https://arxiv.org/abs/2402.03300)) is the safe default with KL regularization.

**DAPO** ([arXiv:2503.14476](https://arxiv.org/abs/2503.14476)) removes KL and uses asymmetric clipping to allow more aggressive exploration in the improve direction.

**GSPO-token** ([arXiv:2507.18071](https://arxiv.org/abs/2507.18071)) uses sequence-level importance ratios and extremely tight clipping. The `seq-mean-token-mean` aggregation normalizes per-sequence before averaging, reducing bias toward longer responses.

For Training API users implementing custom loss functions via `forward_backward_custom`, these methods serve as reference implementations. You can replicate or modify their behavior in your custom loss function. See [Parameter Tuning](/fine-tuning/parameter-tuning#loss-method) for detailed guidance on when to choose each method.

## Applying the optimizer step

After `forward_backward_custom`, call `optim_step` to update weights:

```python theme={null}
training_client.forward_backward_custom(datums, loss_fn).result()
training_client.optim_step(
    tinker.AdamParams(
        learning_rate=1e-5,
        beta1=0.9,
        beta2=0.999,
        eps=1e-8,
        weight_decay=0.01,
    )
).result()
```

For gradient accumulation, call `forward_backward_custom` multiple times before calling `optim_step`:

```python theme={null}
for micro_batch in micro_batches:
    training_client.forward_backward_custom(micro_batch, loss_fn).result()

# One optimizer step after accumulating gradients
training_client.optim_step(tinker.AdamParams(learning_rate=1e-5, ...)).result()
```

<Note>
  Advanced optimizer-step controls such as server-side gradient accumulation normalization are intentionally kept out of this user-facing guide. See the [cookbook skill reference](https://github.com/fw-ai/cookbook/blob/main/skills/dev/references/rl/gradient-accumulation.md) for agent-facing operational guidance.
</Note>

## Common pitfalls

* **Token-weight misalignment** can silently break objective semantics — always verify that `len(logprobs)` and `len(weights)` are compatible (truncate to `min_len`).
* **Ignoring per-step diagnostics** makes instability hard to attribute — log metrics from every train step.
* **Forgetting `.result()`** — all Tinker API calls return futures. Without `.result()`, errors are silently swallowed.
* **Non-differentiable loss**: If your loss doesn't depend on `logprobs_list` entries through differentiable ops, gradients will be zero.

## Related guides

* [Training and Sampling](/fine-tuning/training-api/training-and-sampling) — end-to-end workflow
* [Saving and Loading](/fine-tuning/training-api/saving-and-loading) — checkpoint and weight sync
* [Cookbook RL recipe](/fine-tuning/training-api/cookbook/rl) — GRPO with full reward pipeline
* [Cookbook DPO recipe](/fine-tuning/training-api/cookbook/dpo) — DPO with preference data
