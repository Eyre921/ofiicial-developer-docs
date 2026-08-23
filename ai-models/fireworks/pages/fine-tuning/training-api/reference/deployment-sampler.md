---
title: "DeploymentSampler"
source: https://docs.fireworks.ai/fine-tuning/training-api/reference/deployment-sampler
path: fine-tuning/training-api/reference/deployment-sampler
---

Client-side tokenized sampling for Training API rollouts and evaluation.

## Overview

`DeploymentSampler` handles client-side tokenization via a HuggingFace tokenizer and returns structured `SampledCompletion` objects with token IDs, logprobs, and completion metadata. Serverless and dedicated Training API sampling clients both use this implementation after their infrastructure-specific setup. Use it in training scripts that need token-level outputs (e.g. GRPO, DPO).

```python theme={null}
from fireworks.training.sdk import DeploymentSampler
```

## Constructor

```python theme={null}
from transformers import AutoTokenizer
from fireworks.training.sdk import DeploymentSampler, AdaptiveConcurrencyController

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-8B", trust_remote_code=True)

# Adaptive concurrency (recommended) — auto-tunes based on server load
sampler = DeploymentSampler(
    inference_url="https://api.fireworks.ai",
    model="accounts/<account-id>/deployments/<deployment-id>",
    api_key="<FIREWORKS_API_KEY>",
    tokenizer=tokenizer,
    concurrency_controller=AdaptiveConcurrencyController(initial_window=16),
)
```

| Parameter                | Type                                                                  | Description                                                                                                                                       |
| ------------------------ | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `inference_url`          | `str`                                                                 | Gateway URL for inference completions                                                                                                             |
| `model`                  | `str`                                                                 | Deployment model path (`accounts/<id>/deployments/<id>`)                                                                                          |
| `api_key`                | `str`                                                                 | Fireworks API key                                                                                                                                 |
| `tokenizer`              | `PreTrainedTokenizerBase`                                             | HuggingFace tokenizer matching the base model                                                                                                     |
| `concurrency_controller` | `AdaptiveConcurrencyController \| FixedConcurrencyController \| None` | Controls how many concurrent HTTP requests are in-flight. `None` (default) means no limit. See [Concurrency Control](#concurrency-control) below. |

## Concurrency Control

`sample_with_tokens(n=K)` fans out into K individual streaming requests. Without concurrency control, all requests fire simultaneously, which can overload the server. Two controllers are available:

### AdaptiveConcurrencyController (recommended)

Auto-tunes the concurrency window using AIMD (Additive Increase / Multiplicative Decrease) based on the server's `prefill_queue_duration`:

```python theme={null}
from fireworks.training.sdk import AdaptiveConcurrencyController

ctrl = AdaptiveConcurrencyController(
    initial_window=16,        # starting concurrency
    min_window=1,             # minimum window
    max_window=256,           # maximum window
    prefill_queue_target=0.5, # target prefill queue latency (seconds)
    adjustment_interval=32,   # adjust every 32 completed requests
)
sampler = DeploymentSampler(..., concurrency_controller=ctrl)

# Between training steps, flush remaining metrics and reset the interval
summary = ctrl.step_completed()
print(summary)  # {"window": 20, "avg_pq": 0.08, "cache_hit_rate": 0.95, ...}
```

The controller reads `prefill_queue_duration` from server response metrics. When the queue is below target, the window grows proportionally. When above, it halves (multiplicative decrease). By default, it adjusts after every 32 completed requests and at step boundaries. Set `adjustment_interval=0` to adjust only at step boundaries.

### FixedConcurrencyController

Static semaphore — use when you know the right concurrency for your deployment:

```python theme={null}
from fireworks.training.sdk import FixedConcurrencyController

sampler = DeploymentSampler(
    ...,
    concurrency_controller=FixedConcurrencyController(32),
)
```

## `sample_with_tokens(...)`

Sample completions and return structured results with token IDs. This method is `async`, so call it with `await` or wrap it with `asyncio.run(...)` from synchronous code:

```python theme={null}
import asyncio

async def main():
    completions = await sampler.sample_with_tokens(
        messages=[{"role": "user", "content": "Solve: 2+2="}],
        n=4,
        max_tokens=1024,
        temperature=0.7,
    )
    for c in completions:
        print(c.full_tokens)       # prompt + completion token IDs
        print(c.prompt_len)        # number of prompt tokens
        print(c.completion_len)    # number of completion tokens
        print(c.text)              # decoded completion text
        print(c.finish_reason)     # "stop", "length", etc.

asyncio.run(main())
```

### Retrieving inference logprobs

For GRPO importance sampling, pass `logprobs=True`:

```python theme={null}
import asyncio

async def main():
    completions = await sampler.sample_with_tokens(
        messages=[{"role": "user", "content": "Solve: 2+2="}],
        n=4,
        logprobs=True,
        top_logprobs=1,
    )
    for c in completions:
        print(c.inference_logprobs)  # List[float] or None

asyncio.run(main())
```

### Sequence length filtering

`sample_with_tokens` supports `max_seq_len` for automatic filtering:

```python theme={null}
import asyncio

completions = asyncio.run(
    sampler.sample_with_tokens(
        messages=input_messages,
        n=4,
        max_tokens=1024,
        max_seq_len=8192,  # filter out sequences exceeding this length
    )
)
```

Two levels of filtering are applied:

1. **Prompt pre-filter**: If the tokenized prompt already meets or exceeds `max_seq_len`, the method returns an empty list immediately — no inference call is made.
2. **Completion post-filter**: After sampling, any completion whose full token sequence (prompt + completion) exceeds `max_seq_len` is silently dropped.

## `sample_with_prompt_tokens(...)`

Use `sample_with_prompt_tokens` when your renderer has already produced prompt token IDs. Both serverless and dedicated services expose the shared `DeploymentSampler` through the sampling client:

```python theme={null}
sampling_client = service.create_sampling_client(
    model_path=snapshot,
    tokenizer=tokenizer,
)
sampler = sampling_client.deployment_sampler
```

Keep `sampling_client` alive until all calls through `sampler` have finished, then close it to release the underlying HTTP clients.

### RL rollout sampling

Use [Inference for RL rollouts](https://docs.fireworks.ai/guides/rollout-inference#inference-for-rl-rollouts) as the canonical reference for session affinity, session-ID lifecycle, and KV-cache behavior. The example below only shows how to pass a rollout session value through `DeploymentSampler` and fan out independent samples.

The following example launches two independent trajectories for every pre-tokenized prompt:

```python theme={null}
import asyncio
import secrets

sampling_client = service.create_sampling_client(
    model_path=snapshot,
    tokenizer=tokenizer,
)
sampler = sampling_client.deployment_sampler

async def sample_turn(prompt_token_ids, rollout_session_id):
    return await sampler.sample_with_prompt_tokens(
        prompt_token_ids,
        n=1,
        max_tokens=4096,
        temperature=1.0,
        logprobs=True,
        user=rollout_session_id,
    )

# Scope and retain these IDs according to "Inference for RL rollouts."
trajectory_requests = [
    (prompt_token_ids, f"rl-session-{secrets.token_hex(16)}")
    for prompt_token_ids in batch_prompt_token_ids
    for _ in range(2)
]

try:
    rollout_groups = await asyncio.gather(
        *(
            sample_turn(prompt_token_ids, rollout_session_id)
            for prompt_token_ids, rollout_session_id in trajectory_requests
        )
    )
finally:
    sampling_client.close()
```

Here, `n=1` is intentional because `sample_with_prompt_tokens(n=2, user=...)` gives both child requests the same `user` value. With 32 entries in `batch_prompt_token_ids`, the example creates 64 individual sampling requests. Follow [Inference for RL rollouts](https://docs.fireworks.ai/guides/rollout-inference#inference-for-rl-rollouts) to decide when those requests should use distinct or shared session values.

## SampledCompletion

Each completion returned by `sample_with_tokens` or `sample_with_prompt_tokens`:

| Field                | Type                  | Description                                                                      |
| -------------------- | --------------------- | -------------------------------------------------------------------------------- |
| `text`               | `str`                 | Decoded completion text                                                          |
| `full_tokens`        | `List[int]`           | Prompt + completion token IDs                                                    |
| `prompt_len`         | `int`                 | Number of prompt tokens                                                          |
| `finish_reason`      | `str`                 | `"stop"`, `"length"`, etc.                                                       |
| `completion_len`     | `int`                 | Number of completion tokens                                                      |
| `inference_logprobs` | `List[float] \| None` | Per-token logprobs (when `logprobs=True` is passed)                              |
| `logprobs_echoed`    | `bool`                | `True` when `echo=True` was used — logprobs are training-aligned (P+C-1 entries) |
| `routing_matrices`   | `List[str] \| None`   | Base64-encoded per-token routing matrices for MoE Router Replay (R3)             |

## Related guides

* [FiretitanServiceClient](/fine-tuning/training-api/reference/service-client) — create SDK-managed deployment samplers
* [Serverless Training](/fine-tuning/training-api/serverless) — create an in-session sampler from a serverless checkpoint
* [Training and Sampling](/fine-tuning/training-api/dedicated#training-and-sampling) — end-to-end workflow
* [Cookbook RL recipe](/fine-tuning/training-api/cookbook/rl) — GRPO with sampling pipeline
* [Inference for RL rollouts](https://docs.fireworks.ai/guides/rollout-inference#inference-for-rl-rollouts) — session affinity, KV-cache behavior, and rollout request fields
