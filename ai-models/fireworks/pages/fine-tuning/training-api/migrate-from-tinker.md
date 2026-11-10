---
title: "Migrate from Tinker"
source: https://docs.fireworks.ai/fine-tuning/training-api/migrate-from-tinker
path: fine-tuning/training-api/migrate-from-tinker
---

Bring your Tinker training loop to Fireworks with native SDK clients and serverless or dedicated training.

Fireworks supports the familiar `forward`, `forward_backward`, `forward_backward_custom`, and `optim_step` training pattern. You can keep your dataset logic, rewards, and algorithm while adapting client setup, data types, sampling, and checkpoints.

The Fireworks SDK is independent of the Tinker SDK. Migration requires more than changing an API key or endpoint: the two SDKs have different Python classes and some different interfaces and behavior.

> [!TIP]
>
> **Use a coding agent to migrate your loop.** The cookbook's [Tinker migration skill](https://github.com/fw-ai-external/cookbook/tree/main/skills/migrate-tinker) contains the detailed API mappings, data conversion guidance, compatibility limitations, and validation workflow.
>
> Install it alongside the shared training references:
>
> ```bash theme={null}
> npx skills add fw-ai-external/cookbook -s migrate-tinker -s fireworks-training
> ```
>
> Then ask your agent: "Migrate this Tinker training loop to Fireworks, preserving its objective and token masks."

## Choose your training infrastructure

| | Serverless | Dedicated |
| - | - | - |
| Compute | Shared trainer pool; no provisioning | Provisioned trainer and optional rollout deployment |
| Training mode | LoRA on supported models | LoRA or full-parameter, depending on the training shape |
| Billing | Per token | Trainer and deployment time |
| Start here | [Serverless Training](/fine-tuning/training-api/serverless) | [Dedicated Training](/fine-tuning/training-api/dedicated) |

Check the [model catalog](/fine-tuning/models) for the exact model and training mode you need. For long RL rollouts, compare the full iteration cost, including trainer idle time and weight publication.

## What changes

Most changes happen around the training loop: how you connect, build data objects, and make updated weights available for sampling. Your objective, rewards, and backward/optimizer sequence can stay the same.

| Area | Migration work |
| - | - |
| SDK and authentication | Install `fireworks-ai[training]` and use a Fireworks API key. |
| Clients and data | Replace `tinker.ServiceClient` with `FiretitanServiceClient`. Build native `Datum`, `ModelInput`, and `TensorData` objects; similarly named Tinker classes are not interchangeable. Check tensor dtypes, shapes, and token masks when converting. |
| Models and tokenization | Choose a Fireworks model resource and its matching tokenizer and renderer. |
| Training loop | Keep the forward/backward and optimizer sequence. Preserve target alignment, token masks, and loss normalization. |
| Sampling | Replace Tinker's combined `save_weights_and_get_sampling_client()` helper with separate save and sampler-creation calls. Dedicated sampling also requires weight sync to a deployment. |
| Checkpoints | Distinguish resumable training state from sampler snapshots and use Fireworks checkpoint references. |
| Concurrency and cleanup | Check how many LoRA sessions your chosen trainer supports before porting parallel runs. Release serverless sessions explicitly; configure cleanup for dedicated resources. |

Newer Tinker features and arguments may need additional changes. The [migration skill](https://github.com/fw-ai-external/cookbook/tree/main/skills/migrate-tinker) covers these differences, including sparse tensors, sequence metadata, exception handling, concurrency, and resource lifecycle.

### Migration in pseudocode

This serverless sketch shows the main substitutions. `build_fireworks_batch` represents your own data conversion, returning native SDK datums with the same targets and masks as your Tinker loop. The model, tokenizer, examples, and optimizer settings come from your application.

```python theme={null}
from fireworks.training import sdk

# Replace Tinker's service setup with the Fireworks endpoint and key.
service = sdk.FiretitanServiceClient(
    api_key=fireworks_api_key,
    base_url="https://api.fireworks.ai/training/v1/serverless",
)
sampler = None
try:
    trainer = service.create_lora_training_client(base_model=base_model, rank=8)
    batch = build_fireworks_batch(examples)  # sdk.Datum / ModelInput / TensorData

    # Keep the familiar update sequence, using native optimizer parameters.
    result = trainer.forward_backward(batch, loss_fn="cross_entropy").result()
    trainer.optim_step(sdk.AdamParams(learning_rate=learning_rate)).result()

    # Replace the combined Tinker sampling helper with these two calls.
    snapshot = trainer.save_weights_for_sampler("step-1").result().path
    sampler = service.create_sampling_client(model_path=snapshot, tokenizer=tokenizer)
    # Use sampler for the next rollout or evaluation.
finally:
    try:
        if sampler is not None:
            sampler.close()
    finally:
        try:
            service.delete_training_session()
        finally:
            service.close()
```

For dedicated training, client setup also provisions or attaches to a trainer and, for sampling, a rollout deployment. Follow the [dedicated setup guide](/fine-tuning/training-api/dedicated) for that resource lifecycle.

## Validate before scaling up

Start with a small batch and one optimizer update. Check the loss inputs, returned metrics, sampler publication, checkpoint restore, and cleanup before running your full experiment. Interface compatibility does not establish numerical parity between providers.

> [!NOTE]
>
> Some older models may not support per-token logprobs for `cross_entropy` backward calls. [Contact us](https://fireworks.ai/contact-training) if you need this feature.

## Next steps

* [Tinker migration skill](https://github.com/fw-ai-external/cookbook/tree/main/skills/migrate-tinker) — detailed adaptation and validation guidance
* [Cookbook recipes](/fine-tuning/training-api/cookbook/overview) — maintained SFT, DPO, RL, and distillation loops
* [Training API reference](/fine-tuning/training-api/reference/service-client) — native SDK clients and operations
* [Contact the training team](https://fireworks.ai/contact-training) — help choosing compute or adapting a recipe
