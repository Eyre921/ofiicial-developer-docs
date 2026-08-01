---
title: "Dedicated Training and Sampling"
source: https://docs.fireworks.ai/fine-tuning/training-api/training-and-sampling
path: fine-tuning/training-api/training-and-sampling
---

Detailed dedicated SDK lifecycle: provision resources, train, checkpoint, weight-sync, and sample through a deployment.

## What this is

This is the detailed [Dedicated Training](/fine-tuning/training-api/dedicated) lifecycle for research loops that need serving-quality evaluation during training: create an SDK-managed trainer and deployment, run iterative updates, save sampler weights, sync those weights to the deployment, then sample through the deployment.

If you do not need provisioned trainer and deployment resources, [compare serverless and dedicated training](/fine-tuning/training-api/choose-infrastructure).

For production RL, prefer the [cookbook recipes](/fine-tuning/training-api/cookbook/overview). They wrap this same SDK-managed service path and handle batching, reference clients, checkpoints, reconnect, and configuration-specific cleanup.

## Workflow

1. **Create the managed service** with `FiretitanServiceClient.from_firetitan_config(...)`.
2. **Create a training client** with `service.create_training_client(...)`.
3. **Create a deployment sampler** with `service.create_deployment_sampler(...)`.
4. **Run train steps**: `forward_backward_custom(...)` + `optim_step(...)`.
5. **Save sampler weights** with `training_client.save_weights_for_sampler(...).result()`.
6. **Refresh the sampler** with `service.create_deployment_sampler(model_path=saved.path, ...)`.
7. **Sample and evaluate** through the deployment endpoint.

<Note>
  **Keep each logical batch in one API call.** Pass all datums that should run together to one `forward(...)`, `forward_backward(...)`, or `forward_backward_custom(...)` call. The SDK may submit forward, backward, or combined forward/backward chunks in parallel, but it ensures that all chunks from the call run together as one trainer batch. Separate calls can fragment the work into smaller batches and reduce trainer throughput. See [Logical batches and parallel submission](/fine-tuning/training-api/reference/service-client#logical-batches-and-parallel-submission) for details.
</Note>

The SDK owns trainer provisioning, deployment provisioning, bucket wiring, base-vs-delta sampler checkpoint selection, and weight sync. It performs teardown according to configured cleanup flags; resources are not deleted or scaled down unless those flags request it. You do not construct `TrainerJobManager`, `DeploymentManager`, or `WeightSyncer` for the normal SDK flow.

## End-to-end example

The only training-shape input you choose below is the shape ID. The SDK resolves the versioned trainer shape and linked deployment shape before launch.

### 1. Bootstrap trainer and deployment

```python theme={null}
import os
import tinker

from transformers import AutoTokenizer
from fireworks.training.sdk import (
    AdaptiveConcurrencyController,
    FiretitanServiceClient,
)

api_key = os.environ["FIREWORKS_API_KEY"]
base_url = os.environ.get("FIREWORKS_BASE_URL", "https://api.fireworks.ai")

base_model = "accounts/fireworks/models/qwen3-8b"
tokenizer_model = "Qwen/Qwen3-8B"
shape_id = "accounts/fireworks/trainingShapes/qwen3-8b-128k"

service = FiretitanServiceClient.from_firetitan_config(
    api_key=api_key,
    base_url=base_url,
    base_model=base_model,
    tokenizer_model=tokenizer_model,
    lora_rank=0,
    training_shape_id=shape_id,
    deployment_id="research-serving",
    learning_rate=1e-5,
    replica_count=1,  # deployment replicas for rollout/eval throughput
    cleanup_trainer_on_close=True,
    cleanup_deployment_on_close="scale_to_zero",
)

training_client = service.create_training_client(base_model=base_model, lora_rank=0)

tokenizer = AutoTokenizer.from_pretrained(tokenizer_model, trust_remote_code=True)
concurrency = AdaptiveConcurrencyController(initial_window=16)
sampler = service.create_deployment_sampler(
    tokenizer=tokenizer,
    concurrency_controller=concurrency,
)

print({"trainer_job_id": service.trainer_job_id, "deployment_id": service.deployment_id})
```

### 2. Train step with custom objective

```python theme={null}
def objective(data, logprobs_list):
    loss = compute_objective(data=data, logprobs_list=logprobs_list)
    return loss, {"loss": float(loss.item())}

for step in range(total_steps):
    # Accumulate gradients client-side: run N forward/backward calls, then one optim_step.
    micro_batches = build_micro_batches(step)
    for micro_batch in micro_batches:
        training_client.forward_backward_custom(micro_batch, objective).result()

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

### 3. Save, sync, sample, evaluate

```python theme={null}
import asyncio

if step % eval_interval == 0:
    saved = training_client.save_weights_for_sampler(f"step_{step:05d}").result()

    # Passing model_path syncs the saved snapshot into the SDK-managed
    # deployment and returns a sampler backed by that deployment.
    sampler = service.create_deployment_sampler(
        model_path=saved.path,
        tokenizer=tokenizer,
        concurrency_controller=concurrency,
    )

    completions = asyncio.run(
        sampler.sample_with_tokens(
            messages=eval_prompts,
            n=1,
            max_tokens=512,
        )
    )
    score = evaluate_responses(completions)
    print({"step": step, "checkpoint": saved.path, "eval_score": score})
```

`save_weights_for_sampler(...)` returns a future whose `.result().path` is a public sampler snapshot identity, not a raw storage URI. `create_deployment_sampler(model_path=...)` consumes that identity, syncs it to the deployment, and returns the FireTitan-native deployment sampler. Use `service.create_sampling_client(model_path=...)` instead if you need the Tinker-shaped sampling client wrapper.

## Concurrency control

`sample_with_tokens(n=K)` fans out K concurrent requests. A concurrency controller prevents overloading the deployment:

* **`AdaptiveConcurrencyController`** (recommended) — automatically adjusts the concurrency window based on the server's prefill queue latency. Starts at `initial_window` and grows or shrinks during rollout sampling and at step boundaries using AIMD.
* **`FixedConcurrencyController`** — a static semaphore with a fixed maximum. Use when you already know the right concurrency for your deployment.

See [DeploymentSampler — Concurrency Control](/fine-tuning/training-api/reference/deployment-sampler#concurrency-control) for full details and configuration options.

## Reference clients

For DPO, GRPO with KL, or any objective that needs frozen-reference logprobs, ask the service for a reference client:

```python theme={null}
reference_client = service.create_reference_client(base_model, lora_rank=0)
ref = reference_client.forward(datums, "cross_entropy").result()
```

The SDK chooses the backing automatically:

* LoRA policy with no explicit `reference_training_shape_id` reuses the policy trainer session with adapters disabled.
* Full-parameter policy, or any explicit `reference_training_shape_id`, uses a separate forward-only reference trainer owned by the service.

## Reconnecting to a running trainer

If your client disconnects, re-create the service with the existing trainer job ID. The SDK waits for the trainer, reconnects the training client, and can reuse or reattach the deployment:

```python theme={null}
service = FiretitanServiceClient.from_firetitan_config(
    api_key=api_key,
    base_url=base_url,
    base_model=base_model,
    tokenizer_model=tokenizer_model,
    lora_rank=0,
    training_shape_id=shape_id,
    trainer_job_id="<existing-trainer-job-id>",
    deployment_id="research-serving",
)
training_client = service.create_training_client(base_model=base_model, lora_rank=0)
```

For DCP train-state resume, load a saved state after creating the client:

```python theme={null}
training_client.load_state_with_optimizer("step-100").result()
```

## Cleanup

Set cleanup flags deliberately, call `service.close()` from `try/finally`, and verify the requested final resource state. The canonical cleanup modes and examples live in [Cleanup and Teardown](/fine-tuning/training-api/reference/cleanup).

## Operational guidance

* **Start from cookbook recipes** for SFT, DPO, ORPO, GRPO, IGPO, and async RL; fork them when you need custom loop behavior.
* **Use the managed service as the provisioning boundary** in direct SDK code. Manager classes are documented only for compatibility and advanced lifecycle debugging.
* **Service mode supports both full-parameter and LoRA tuning.** Set `lora_rank=0` for full-parameter or a positive integer for LoRA.
* **Use `save_weights_for_sampler(...)` for normal sampler refresh.** The SDK tracks the base/delta chain and performs weight sync through `create_sampling_client(model_path=...)` or `create_deployment_sampler(model_path=...)`.
* **Use `save_state(...)` for DCP resume checkpoints.** Sampler checkpoints are for serving/evaluation and promotion; DCP checkpoints restore training state.
* **Store the exact prompt set and sampler snapshot path** for every evaluation sweep.

## Related guides

* [Loss Functions](/fine-tuning/training-api/loss-functions) — built-in and custom loss function patterns
* [Vision Inputs](/fine-tuning/training-api/vision-inputs) — fine-tune VLMs with image and text data
* [Saving and Loading](/fine-tuning/training-api/saving-and-loading) — checkpoint types and weight sync details
* [DeploymentSampler reference](/fine-tuning/training-api/reference/deployment-sampler) — sampling API details
* [Cleanup and Teardown](/fine-tuning/training-api/reference/cleanup) — managed service cleanup
