---
title: "Serverless Training"
source: https://docs.fireworks.ai/fine-tuning/training-api/serverless
path: fine-tuning/training-api/serverless
---

Fine-tune open models with your own Python training loop on shared Fireworks GPUs. Nothing to provision, and you pay per token.

Serverless training runs on shared Fireworks GPUs, so there is no trainer job or inference deployment to provision or delete. You can run supervised fine-tuning, preference optimization (DPO), reinforcement learning, distillation, or your own custom loop.Serverless supports LoRA training only. For full-parameter training or a model outside the serverless pool, use [Dedicated Training](/fine-tuning/training-api/dedicated). If you're not sure, [compare dedicated and serverless training](/fine-tuning/training-api/introduction#infrastructure) or [contact us](https://fireworks.ai/contact-training).## How it works1 · LocalYour Python loopBuilds batches, rewards, and optimizer requests.2 · SharedTrainerRuns remote LoRA forward, backward, and optimizer work.3 · In sessionCheckpointCaptures the current adapter weights for sampling.4 · SharedSamplerReturns rollouts for local scoring and the next step.You write the training loop in Python. Fireworks runs the forward pass, backward pass, and optimizer step on shared GPUs, then serves your latest weights for sampling in the same session. For the terms used on this page, see the [glossary](#glossary).## What you can run> [card] [Supervised fine-tuning (SFT)](/fine-tuning/training-api/cookbook/sft)
>
> Train on labeled examples with a cross-entropy loss.> [card] [Reinforcement learning (RL)](/fine-tuning/training-api/cookbook/rl)
>
> Sample, score with your own reward function, and train on the results.> [card] [Direct preference optimization (DPO)](/fine-tuning/training-api/cookbook/dpo)
>
> Train from pairs of chosen and rejected responses.> [card] [Distillation](/fine-tuning/training-api/cookbook/distillation)
>
> Train a student model from a teacher model's scores.> [card] [Custom loss](/fine-tuning/training-api/dedicated#loss-functions)
>
> Write your own loss function using the same Training API calls as dedicated training.## Quickstart**Requires Python 3.11 or later.**### Step 1: Create a key, install, and authenticateCreate an API key in the [Fireworks dashboard](https://app.fireworks.ai/settings/users/api-keys), or run `firectl api-key create` in your terminal. Then install the SDK and export the key:The example below runs from a source checkout. To import released recipes in your own project, use [the PyPI installation](/fine-tuning/training-api/cookbook/overview#installation).```bash theme={null}
git clone https://github.com/fw-ai-external/cookbook
pip install -e ./cookbook/training
pip install math-verify   # used by the DeepMath example to grade answers
export FIREWORKS_API_KEY="fw_..."   # the key you just created
```### Step 2: Run the complete serverless RL exampleThe cookbook's DeepMath example includes its dataset, reward, training loop, and metrics. It trains on math problems with reinforcement learning (RL), using Group Relative Policy Optimization (GRPO). These flags keep the first run small:```bash theme={null}
cd cookbook/training
python -m examples.rl.deepmath.train_deepmath_serverless \
  --base-model accounts/fireworks/models/muse-glimmer-30b \
  --tokenizer-model meta-models/Muse-Glimmer-30B --renderer-name muse_glimmer \
  --max-rows 32 --prompt-groups-per-step 8 --completions-per-prompt 4 \
  --max-completion-tokens 4096 --max-seq-len 8192 --lora-rank 8
```This is a real paid run. It first evaluates the base model, then trains, then evaluates again.### Step 3: Clean upThe run keeps one of your training slots until you delete its session. You can still list and [promote](#promote-a-sampler-checkpoint-to-a-model) its checkpoints after you delete the session, while the session/trainer records and checkpoint artifacts remain available, but promote the ones you want to keep soon after training. Training checkpoints stay loadable from a new run for about 30 days (see [Checkpoint retention](#checkpoint-retention)). Then delete the session, using the training session name the example printed (`accounts/<ACCOUNT_ID>/trainingSessions/<SESSION_ID>`):```bash theme={null}
curl -X DELETE \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  https://api.fireworks.ai/v1/accounts/<ACCOUNT_ID>/trainingSessions/<SESSION_ID>
```To write your own loop instead of running the example, see [Write your own training loop](#write-your-own-training-loop).## Supported modelsServerless supports these base models. For dedicated and managed options, see the [Models catalog](/fine-tuning/models).

\<table><thead><tr><th>Base model</th>
              \<th>Model ID</th>
              \<th>Max context</th></tr></thead>
          \<tbody /></table>

## PricingServerless training is billed per token, across three meters:- **Prefill:** prompt tokens the sampler reads. Repeated prefixes bill at the lower cached prefill rate.
- **Sample:** tokens the sampler generates.
- **Train:** tokens you train on (passed through `forward_backward`).Rates are USD per 1 million tokens. Available models and rates can change, so verify current availability in the [Models catalog](/fine-tuning/models) and the [pricing page](https://fireworks.ai/pricing) before launch.| Base model | Context | Prefill | Cached prefill | Sample | Train |
| - | - | - | - | - | - |
| Muse Spark Open | 256K | \$6.19 | \$1.239 | \$15.48 | \$18.58 |
| DeepSeek V4.1 Flash 1017 | 256K | \$0.60 | \$0.12 | \$3.60 | \$4.98 |
| NVIDIA Nemotron 3.5 Super VL 120B | 256K | \$0.57 | \$0.114 | \$1.44 | \$2.32 |
| GLM 5.3 Flash | 195K | \$2.96 | \$0.593 | \$7.41 | \$8.89 |
| GLM 5.3 | 256K | \$4.86 | \$0.972 | \$12.15 | \$14.58 |
| Qwen 3.6 35B A3B | 256K | \$0.45 | \$0.09 | \$1.335 | \$2.14 |
| Qwen 3.8 27B | 128K | \$1.86 | \$0.372 | \$5.595 | \$4.103 |
| Kimi K3.1 Pro | 256K | \$2.40 | \$0.24 | \$12.00 | \$25.00 |
| Kimi K3 | 192K | \$10.87 | \$2.17 | \$27.11 | \$32.55 |
| Muse Glimmer 30B | 128K | \$1.96 | \$0.39 | \$4.88 | \$5.86 |Nemotron 3.5 Super VL uses the current Tinker 256K card, which includes a limited-time 50% discount.## Write your own training loopThe DeepMath example wraps a loop you can write yourself with the SDK. To use the SDK without the cookbook, install it on its own:```bash theme={null}
pip install "fireworks-ai[training]"
```### Connect to a serverless sessionRun this Python script:```python theme={null}
import os
from fireworks.training.sdk import FiretitanServiceClient

service = FiretitanServiceClient(
    api_key=os.environ["FIREWORKS_API_KEY"],
    base_url="https://api.fireworks.ai/training/v1/serverless",
)

base_model = "accounts/fireworks/models/qwen3p8-27b"
max_seq_len = 131072  # enforce this when rendering prompts and training datums
training_client = service.create_lora_training_client(base_model=base_model, rank=8)

print(f"session={service.training_session_id} run={training_client.run_id}")
```If it prints a session ID that starts with `ts-`, your setup works. The session holds a training slot until you delete it.### Train, checkpoint, and sampleEach training step follows the order below. This excerpt doesn't run on its own: it continues from the code above and uses `datums`, `tokenizer`, `prompt`, and `params`, which a complete loop such as the [DeepMath example](https://github.com/fw-ai-external/cookbook/blob/main/training/examples/rl/deepmath/train_deepmath_serverless.py) defines.```python theme={null}
from fireworks.training.sdk import AdamParams

# One optimizer step
training_client.forward_backward(datums, "importance_sampling").result()
training_client.optim_step(
    AdamParams(learning_rate=2.5e-5, beta1=0.9, beta2=0.95, eps=1e-8, weight_decay=0.0)
).result()

# Save weights and open a sampler bound to that exact snapshot
snapshot = training_client.save_weights_for_sampler("step-0001").result().path
sampler = service.create_sampling_client(model_path=snapshot, tokenizer=tokenizer)
completions = sampler.sample(
    prompt=prompt,
    num_samples=8,
    sampling_params=params,
).result()
sampler.close()
```> [!WARNING]
>
> * Training and sampling calls return futures. Call `.result()` on each, or errors can go unnoticed.
> * The tokenizer must match `base_model`. It formats prompts and decodes samples on your machine, so a mismatch silently corrupts your rewards.
> * Give each checkpoint a different name. Saving twice with the same name points to the same snapshot.When you finish, close your clients and delete the session.For a complete RL loop, see the [DeepMath example](https://github.com/fw-ai-external/cookbook/blob/main/training/examples/rl/deepmath/train_deepmath_serverless.py) from the quickstart. For async scheduling and custom rollout functions, use the experimental [`async_rl_loop_serverless`](https://github.com/fw-ai-external/cookbook/blob/main/training/recipes/experiment/async_rl_loop_serverless.py) recipe. For other RL losses, see the [cookbook RL recipes](/fine-tuning/training-api/cookbook/rl).## Saving and loading checkpointsServerless training writes **two different kinds of checkpoint**, and they are not interchangeable:| | **Training checkpoint** | **Sampler checkpoint** |
| - | - | - |
| Saved by | `save_state(name)` | `save_weights_for_sampler(name)` |
| Contains | Adapter weights **and** optimizer state | Current adapter weights only |
| Resumable — the trainer can load it back and keep training | ✅ Yes | ❌ No |
| Promotable to a deployable model | ❌ No | ✅ Yes |> [!WARNING]
>
> Only **sampler checkpoints** can be promoted to a final model, and only **training checkpoints** can be loaded back by the trainer to resume. A training checkpoint cannot be served or promoted. A sampler checkpoint cannot restore training state (weights + optimizer).Checkpoint storage is currently included at no charge.For the full SDK-level checkpoint reference (base/delta sampler types, weight sync, and cross-job resolution), see [Dedicated Training](/fine-tuning/training-api/dedicated#saving-and-loading) and the [Cookbook Reference](/fine-tuning/training-api/cookbook/reference#checkpoints).### Save and resume training checkpointsSave training checkpoints periodically so an interrupted run can continue:```python theme={null}
# Save a training checkpoint (adapter weights + optimizer) for resume
training_client.save_state("step-0100").result()

# Resume inside the same run: restores weights and optimizer state
training_client.load_state_with_optimizer("step-0100").result()

# Weights-only load (optimizer resets to zero — a warm start)
training_client.load_state("step-0100").result()
```Save and load calls return futures — call `.result()` to block and surface failures. `save_state` also accepts a `timeout` to bound the wait. Give each checkpoint a distinct name: overwriting an existing name (`overwrite=True`) is not supported.> [!WARNING]
>
> **Keep checkpoint names to 17 characters or fewer.** The server-side ID is `run-<32-hex>-<your-name>-<8-hex>` and must fit in 63 characters, leaving 17 for your name.
>
> This is only checked at promote time, so an overlong name fails after training completes. Recovery is `load_state` into a fresh session and re-saving under a shorter name.To see what checkpoints a run has saved, use the session-scoped control-plane list in [Promote a sampler checkpoint to a model](#promote-a-sampler-checkpoint-to-a-model) below — the trainer-local `training_client.list_checkpoints()` is not routed on the serverless surface.> [accordion] Resume a new run from a training checkpoint
>
> To fork a new run from a previous run's training checkpoint, use `create_training_client_from_state` on the service client. The SDK reads the base model and LoRA configuration from the checkpoint itself, creates a fresh run, and loads the saved state:
>
> ```python theme={null}
> # Continue a previous run's training checkpoint in a new run (weights + optimizer)
> resumed_client = service.create_training_client_from_state_with_optimizer(
>     "<account>/<run-id>/step-0100",
> )
>
> # Or warm start from those weights with a fresh optimizer
> resumed_client = service.create_training_client_from_state(
>     "<account>/<run-id>/step-0100",
> )
> ```
>
> Checkpoint references are fully qualified as `<account>/<run-id>/<checkpoint-name>`, where `run-id` is the previous run's `training_client.run_id` (`run-<hex>`). `weights_access_token` is not supported — load checkpoints accessible to your API key.### Checkpoint retention- **Training checkpoints** are kept for about 30 days after you save them. Load one into a new run with `<account>/<run-id>/<checkpoint-name>`, as in [Resume a new run from a training checkpoint](#save-and-resume-training-checkpoints), even after the original session has expired or been deleted.
- **Listing and promoting** keep working after the session expires or is deleted, while the session/trainer records and checkpoint artifacts remain available. Promote the sampler checkpoints you want to keep soon after training.
- **Sessions** expire once they've had no active runs for 10 minutes. Expiry is checked every 5 minutes.
- **Unsaved progress** isn't saved for you. If the trainer unloads your run, the weights and optimizer state since your last `save_state` are lost, so save at regular intervals.### Promote a sampler checkpoint to a modelPromotion turns a **sampler checkpoint** into a deployable Fireworks model (a standard LoRA addon model). Training checkpoints are not promotable — save a sampler checkpoint first.**1. Save a sampler checkpoint during training**```python theme={null}
snapshot = training_client.save_weights_for_sampler("final").result().path
```Save one at the end of training, and at any intermediate step you may want to deploy later.**2. List the session's checkpoints**Listing and promotion are session-scoped control-plane operations on `FireworksClient` (against the regular API gateway, not the serverless base URL). The session resource name is available as `service.training_session_name`:```python theme={null}
import os
from datetime import datetime
from fireworks.training.sdk import FireworksClient

fw_client = FireworksClient(api_key=os.environ["FIREWORKS_API_KEY"])

rows = fw_client.list_training_session_checkpoints(service.training_session_name)
target = max(
    (row for row in rows if row.get("promotable")),
    key=lambda row: datetime.fromisoformat(row["createTime"].replace("Z", "+00:00")),
)
```> [accordion] About the checkpoint list fields
>
> Each row carries `name` (the full 4-segment resource name), `checkpointName`, `checkpointType`, `promotable`, and `createTime`. Two things to know about the values:
>
> * `checkpointName` is the server-side checkpoint ID, **not** the bare name you passed: it is prefixed with the source run ID and, for sampler checkpoints, suffixed with an 8-hex-char session ID — a save named `final` surfaces as `run-<hex>-final-<8hex>`. Select rows on `promotable` + `createTime` as above, or with a prefix/substring test — never by equality with your logical name. The composed ID caps your own name at [17 characters](#save-and-resume-training-checkpoints).
> * `checkpointType` is a server enum string: `CHECKPOINT_TYPE_TRAINING_LORA` for training checkpoints, `CHECKPOINT_TYPE_INFERENCE_LORA` for sampler checkpoints. Treat it as opaque and filter on `promotable`, which is authoritative.**3. Promote the checkpoint**```python theme={null}
model = fw_client.promote_session_checkpoint(
    name=target["name"],  # accounts/<a>/trainingSessions/<s>/checkpoints/<c>
    output_model_id="my-serverless-lora",
    base_model="accounts/fireworks/models/qwen3p8-27b",
)
````output_model_id` must be 1-63 characters of lowercase a-z, 0-9, and hyphens. The promoted model appears in your account's model list like any other trained model.> [!NOTE]
>
> Session-scoped list and promote keep working after the session expires or is deleted, while the session/trainer records and checkpoint artifacts remain available. Once they're gone, both calls return `NOT_FOUND` and the checkpoints are no longer reachable through this API, so promote any checkpoint you want to keep soon after training. Cross-run training-checkpoint resume (above) is resolved per run and is not subject to this limit.### Deploy the promoted model to productionA promoted model deploys like any LoRA model trained on Fireworks: with **live merge**, Fireworks merges the adapter into the base weights at deployment time, so the deployment performs identically to the base model.Deploy the promoted model directly:```bash theme={null}
firectl deployment create "accounts/<account-id>/models/my-serverless-lora" \
  --deployment-shape default
```To pick a specific shape instead of `default`, see [Deployment shapes](/guides/ondemand-deployments#deployment-shapes).Then send requests with the model name:```python theme={null}
from fireworks import Fireworks

client = Fireworks()
response = client.chat.completions.create(
    model="accounts/<account-id>/models/my-serverless-lora",
    messages=[{"role": "user", "content": "Hello!"}],
)
```For deployment configuration, performance, and troubleshooting, see [Deploying trained models](/fine-tuning/deploying-loras).If the base model is [supported on serverless](/serverless/specialized-model-inference/overview#supported-models-and-limits), you can skip the deployment and serve the promoted model on serverless with [Specialized Model Inference](/serverless/specialized-model-inference/overview), paying per token.## Sampling without a training clientSample from a checkpoint during or after a run to evaluate it. The sampler is not a chat endpoint for your adapter: to evaluate through the chat completions API, promote the checkpoint and evaluate it on serverless with [Specialized Model Inference](/serverless/specialized-model-inference/overview) if its base model is supported, or on a preemptible deployment. Serverless sampling does not work for adapters produced by dedicated training. See [Evaluating trained models](/fine-tuning/evaluating-fine-tuned-models).Sampling does not need `create_lora_training_client`. A fresh `FiretitanServiceClient` can sample a base model in the serverless pool, or any sampler checkpoint your account saved with `save_weights_for_sampler`, including checkpoints from a run that has already ended. These samplers create no training run and do not use a [concurrent-run](#capacity-and-rate-limits) slot, so evaluation workers can open and close them freely. Sampled tokens are billed per token like other serverless training sampling.> [!NOTE]
>
> Requires SDK version 1.2.29 or later: `pip install --upgrade "fireworks-ai[training]>=1.2.29"`.### Sample a base model```python theme={null}
import os
from fireworks.training.sdk import FiretitanServiceClient, types

service = FiretitanServiceClient(
    api_key=os.environ["FIREWORKS_API_KEY"],
    base_url="https://api.fireworks.ai/training/v1/serverless",
)
sampler = service.create_sampling_client(
    base_model="accounts/fireworks/models/qwen3p8-27b",
    tokenizer=tokenizer,
)
result = sampler.sample(
    prompt=types.ModelInput.from_ints(tokenizer.encode("The weather today is")),
    num_samples=1,
    sampling_params=types.SamplingParams(max_tokens=20, temperature=0.7),
).result()
sampler.close()
```### Sample a saved checkpointPass the path that `save_weights_for_sampler` returned, `<account>/<run-id>/<checkpoint-name>`. The process that saved it can be gone:```python theme={null}
# In the training process
path = training_client.save_weights_for_sampler("step-0100").result().path

# Later, in any process with an API key for the same account
service = FiretitanServiceClient(
    api_key=os.environ["FIREWORKS_API_KEY"],
    base_url="https://api.fireworks.ai/training/v1/serverless",
)
sampler = service.create_sampling_client(model_path=path, tokenizer=tokenizer)
```* You can only sample checkpoints that belong to your own account. A path for another account fails before any request is sent.
* To keep a checkpoint as a deployable model, [promote it](#promote-a-sampler-checkpoint-to-a-model).
* On a service that has already created a training client, `create_sampling_client(model_path=...)` for that run's checkpoints, and `base_model=...` for the session's base weights, sample through the training session as before.> [accordion] Share a sampler across processes
>
> `FiretitanSamplingClient` works with Python multiprocessing. Create it once in the main process and pass it to workers. The same instance can be shared by several processes.
>
> **Pickle the client.** The pickle carries the connection state, including the API key and headers, so workers need no environment of their own. Each worker gets its own event loop, HTTP connections, and concurrency controller. A fixed concurrency limit carries over.
>
> ```python theme={null}
> from concurrent.futures import ProcessPoolExecutor
>
> def evaluate(sampler, prompt):
>     return sampler.sample(prompt=prompt, num_samples=1, sampling_params=params).result()
>
> with ProcessPoolExecutor(max_workers=8) as pool:
>     results = list(pool.map(evaluate, [sampler] * len(prompts), prompts))
> ```
>
> **Pass a sampler handle.** To avoid putting credentials in a pickle, pass a string handle instead. It carries no API key or credential headers. The receiving process authenticates with `api_key=` or its own `FIREWORKS_API_KEY`.
>
> ```python theme={null}
> handle = sampler.get_sampler_handle()  # str: store it, queue it, send it anywhere
>
> # In the worker
> from fireworks.training.sdk import FiretitanSamplingClient
> sampler = FiretitanSamplingClient.from_sampler_handle(handle, tokenizer=tokenizer)
> ```
>
> | Method | Description |
> | - | - |
> | Pickling | Carries the connection state, API key, headers, and tokenizer. Each unpickled copy gets its own event loop, HTTP connections, and concurrency controller. A fixed concurrency limit carries over. |
> | `get_sampler_handle() -> str` | A pickle-free string handle to the same sampler, with no API key or credential headers. |
> | `FiretitanSamplingClient.from_sampler_handle(handle, *, api_key=None, tokenizer=None)` | Creates a client for the sampler behind `handle`, in any process and any number of times. Authenticates with `api_key`, or `FIREWORKS_API_KEY` from the environment. |
>
> Keep `FiretitanServiceClient` and training clients in the main process. Only sampling clients are meant to cross process boundaries.> [accordion] Prompt caching for RL rollouts
>
> For RL rollouts, pass a stable trajectory ID so repeated prompts reuse the KV cache. This requires SDK 1.2.9 or later: versions 1.2.0 through 1.2.8 replaced per-request session values with one derived from the checkpoint. Upgrade with `pip install --upgrade "fireworks-ai[training]>=1.2.9"` and restart the client process. See [Inference for RL rollouts](/guides/rollout-inference) and [`DeploymentSampler` RL rollout sampling](/fine-tuning/training-api/reference/deployment-sampler#rl-rollout-sampling).## Capacity and rate limits- **Concurrent runs:** The default is 8 active runs per account, although account overrides may differ. Some pool models also limit active runs per account on that base model, and managed fine-tuning jobs on the same model count toward it. Over either limit, new runs fail with HTTP 429 (`RATE_LIMIT_EXCEEDED`) and a message such as `maximum concurrent serverless training runs for base model <MODEL> exceeded: in use 1, limit 1`. A run holds its slot until its session is deleted or expires. [Sampling without a training client](#sampling-without-a-training-client) uses no slot.
- **Free a slot now:** Closing the client does not end the session. Promote any checkpoint you need, then delete the session as in [Step 3: Clean up](#step-3-clean-up).
- **Request and token limits:** Contact Fireworks for the current limits on your account.
- **Shared-pool capacity:** if the pool is full, `create_lora_training_client` returns an out-of-capacity error. Retry, or switch to the dedicated path.
- **Sampling speed:** serverless sampling runs on a pool shared with other customers, so the time each training step spends sampling varies with overall load. For predictable rollout throughput, use [Dedicated Training](/fine-tuning/training-api/dedicated).## Troubleshooting| Symptom | Cause | Fix |
| - | - | - |
| `create_lora_training_client` fails with `out of capacity` | The shared pool for that base model is full. | Retry shortly, or use [Dedicated Training](/fine-tuning/training-api/dedicated). |
| A new run fails with HTTP 429: `maximum concurrent serverless training runs … exceeded` | Your account is at its concurrent-run limit, overall or for that base model. Finished runs keep their slot until you delete their session. Managed fine-tuning jobs on the same model count toward it. | Promote any checkpoint you need, then delete finished sessions as in [Step 3: Clean up](#step-3-clean-up). |
| Creating the training client fails on rank | Serverless is LoRA only, and rank 0 means full-parameter training. | Pass a positive `rank`, such as `rank=8`. For full-parameter training, use [Dedicated Training](/fine-tuning/training-api/dedicated). |
| Sampling fails right after you connect | `base_url` does not end in `/training/v1/serverless`. | Set `base_url="https://api.fireworks.ai/training/v1/serverless"`. A working session ID starts with `ts-`. |
| The loop runs, but nothing changes and no error appears | A remote call's result was never read, so its failure was never raised. | Call `.result()` on every `forward_backward`, `optim_step`, save, and sample call. |
| Rewards or decoded samples look wrong | The tokenizer does not match `base_model`. | Load the tokenizer for the exact base model you train. |
| Promotion fails on name length after training finishes | The checkpoint name is longer than 17 characters. | Load the training checkpoint into a fresh session with `load_state` and save it again under a shorter name. Keep names to 17 characters or fewer. |
| Listing or promoting checkpoints returns `NOT_FOUND` | The session/trainer records or checkpoint artifacts are no longer available. | Promote checkpoints soon after training. Use the session-scoped checkpoint name from `list_training_session_checkpoints`. |
| Two saves return the same snapshot path | Both saves used the same checkpoint name. | Give every checkpoint a distinct name. |## Next steps* [DeepMath serverless example](https://github.com/fw-ai-external/cookbook/blob/main/training/examples/rl/deepmath/train_deepmath_serverless.py): runnable serverless RL loop
* [Prompt-router serverless notebook](https://github.com/fw-ai-external/cookbook/blob/main/training/case-studies/sft_prompt_router/prompt_router_serverless.ipynb): dataset preparation, LoRA SFT, checkpoint sampling, and evaluation on Qwen 3.8 27B
* [Choose infrastructure](/fine-tuning/training-api/introduction#infrastructure): compare serverless and dedicated
* [Dedicated Training](/fine-tuning/training-api/dedicated): the provisioned path from setup through teardown
* [The Cookbook](/fine-tuning/training-api/cookbook/overview): ready-to-run recipes> [accordion] Video walkthrough: Train a prompt router
>
> This video uses the deprecated Qwen 3.5 9B pool and is kept for conceptual reference. Use Qwen 3.8 27B for current Serverless Training runs, as in the notebook above.
>
> The walkthrough trains a model with LoRA SFT to classify prompts and route them to a small or large model. It covers the local Python loop, the pooled serverless trainer, checkpoint evaluation, and the before-and-after comparison.
>
> [Train a prompt router with Fireworks Serverless Training](https://www.youtube.com/embed/0NMrs9X36mg)## Glossary- **Session:** your attachment to a shared trainer for a base model, created with your training client. Its ID (`service.training_session_id`) starts with `ts-`. Your adapter lives in the session, and the session holds a training slot until you delete it.
- **Run:** one training trajectory, with its steps and checkpoints (`training_client.run_id`).
- **LoRA adapter:** a small set of weights trained on top of the frozen base model. Serverless trains LoRA only: pass a positive `rank`, such as `rank=8`.
- **Checkpoint:** saved adapter weights. `save_weights_for_sampler(name)` returns a path you can sample from or promote. See [Saving and loading checkpoints](#saving-and-loading-checkpoints).
- **Sampling:** generating completions from a base model or checkpoint, for rollouts and evaluation. Any process can sample a saved checkpoint. See [Sampling without a training client](#sampling-without-a-training-client).
