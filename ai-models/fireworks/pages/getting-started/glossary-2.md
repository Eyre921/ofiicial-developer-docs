---
title: "Glossary"
source: https://docs.fireworks.ai/getting-started/glossary
path: getting-started/glossary
---

Definitions for key terms used across Fireworks AI documentation.

This glossary covers terms you'll encounter when working with the Fireworks AI platform — across inference, training, deployments, security, and the API.

***

## Account & Billing

**Account**\
Your Fireworks AI organization identity. All deployments, models, training jobs, and API keys belong to an account. Referenced as `accounts/<your-account>` in firectl and the API.

**Credit**\
The unit used for prepaid usage on Fireworks. Credits are consumed as you use inference and training resources.

**Rate limiting / 429 errors**\
A `429 Too Many Requests` response means your account or deployment has hit a concurrency or request-per-minute limit. On serverless, limits scale automatically with usage tier. On dedicated deployments, adding replicas or adjusting autoscaling increases capacity.

**Quota**\
A per-account cap on a resource — such as requests per minute (RPM), GPU hours, or concurrent replicas. Quotas can be increased by contacting support.

**ZDR (Zero Data Retention)**\
The default behavior for all open model inference on Fireworks: no prompts, completions, or request logs are stored after the response is returned. ZDR is on by default — it is not an opt-in feature.

**BYOC (Bring Your Own Cloud)**\
An enterprise option to run inference entirely within your own cloud account. Your data never touches Fireworks-managed infrastructure. Contact sales for availability.

***

## Fireworks Platform

**Serverless inference**\
Pay-per-token inference with no deployment management. Requests are routed globally by default; [US-only Serverless](/serverless/us-only-serverless) serves supported models from the US. Dedicated deployments support explicit placement with the **`--region`** flag on `firectl deployment create` (for example `GLOBAL`, `US`, `EUROPE`, `APAC`).

**Dedicated deployment**\
A deployment you provision and manage, with reserved GPU capacity. Gives you control over model, hardware, placement, autoscaling, and addon support. Created with `firectl deployment create`.

**Multi-region deployment**\
A dedicated deployment configured to run replicas across multiple datacenters. Enabled with `--region GLOBAL` (or a specific mega-region: `US`, `EUROPE`, `APAC`) on `firectl deployment create`. Increases availability and throughput.

**Placement**\
Controls which regions a dedicated deployment is allowed to schedule replicas in. On the CLI, set at creation time with **`--region`** (`GLOBAL`, `US`, `EUROPE`, `APAC`, or a specific region id). Cannot be changed after deployment creation — recreate the deployment to change placement. If not specified, the deployment pins to a single datacenter at creation time.

**Deployment shape**\
The hardware and precision configuration used when creating a dedicated deployment. Shapes encode GPU type, count, precision (BF16, FP8, FP4), and other settings. Specified with `--deployment-shape`. Some shapes do not support LoRA addons.

**Deployment state**\
The lifecycle status of a deployment: `CREATING`, `DEPLOYING`, `DEPLOYED`, `SCALING`, `UPDATING`, `FAILED`, `DELETING`, `DELETED`.

**Replica**\
A single instance of a deployed model. Adding replicas increases concurrency. Replicas can be scaled manually or via autoscaling rules.

**Autoscaling**\
Automatic adjustment of replica count based on traffic. Configured with scale-to-zero, minimum replicas, maximum replicas, and scale-up/down thresholds.

**firectl**\
The Fireworks command-line tool for managing models, deployments, training jobs, and account resources.

***

## Models & Inference

**Base model**\
A foundation model available on Fireworks for inference or training. Referenced as `accounts/fireworks/models/<model-id>`.

**Addon**\
A LoRA adapter loaded on top of a base model deployment at inference time. Enabled on a deployment with `--enable-addons`. The adapter is specified per request by passing the adapter model ID. FP8 and FP4 quantized shapes do not support addons — use a BF16 shape for LoRA addon inference.

**Multi-LoRA**\
A single base model deployment that serves multiple LoRA adapters. The adapter is selected per request. One deployment, multiple trained behaviors.

**Quantization**\
Reducing the numerical precision of model weights to decrease memory usage and increase throughput, with some quality tradeoff.

**BF16 (BFloat16)**\
A 16-bit floating point format used for model weights. Provides good quality with moderate memory usage. BF16 deployment shapes support LoRA addons.

**FP8**\
An 8-bit floating point format. Faster and more memory-efficient than BF16, with a small quality tradeoff. FP8 deployment shapes do not support LoRA addons.

**FP4**\
A 4-bit floating point format. Faster and cheaper than FP8, with a larger quality tradeoff. FP4 deployment shapes do not support LoRA addons.

**Speculative decoding**\
An inference acceleration technique where draft tokens are verified by the target model in parallel. It reduces generation latency when the target accepts enough proposed tokens per verification step to offset draft generation and verification overhead; see [Speculative Decoding](/deployments/speculative-decoding).

**KV cache**\
Key-value cache that stores intermediate attention computations across tokens. Reduces re-computation cost on repeated or shared prefixes. Cache hit percentage is reflected in billing. Configurable with `--kv-cache-fraction`.

**Context window**\
The maximum number of tokens (input + output) the model can process in a single request.

**`max_tokens`**\
API parameter that caps how many tokens the model will generate in a single response. Always set this explicitly in agentic workflows — without it, reasoning models and large models may generate very long outputs.

**TTFT (Time to First Token)**\
Latency from when a request is sent to when the first output token is received. Key metric for interactive applications.

**TPS (Tokens Per Second)**\
Throughput metric measuring how many output tokens are generated per second.

**Batch inference**\
Asynchronous large-scale inference via the Fireworks Batch API. Submit a JSONL file of requests; results are returned when the job completes. Lower cost than real-time inference, higher latency, no streaming.

**Streaming**\
Real-time token-by-token output delivery via server-sent events (SSE). Enabled with `stream=True`. Not available in batch inference.

**Tool calling / Function calling**\
The ability for a model to request that the client execute a function and return the result, enabling agentic and multi-step workflows.

**Structured output**\
Model output constrained to a specific JSON schema. Fireworks supports constrained decoding to guarantee valid JSON matching your schema.

**`reasoning_effort`**\
API parameter that controls how much thinking a reasoning model performs before generating its response. Set to `"none"` to disable extended reasoning (useful as a workaround for models prone to reasoning loops).

***

## Training

**SFT (Supervised Fine-Tuning)**\
Training a model on labeled input-output pairs to adapt it to a specific task or style. Available via the Fireworks managed training pipeline.

**LoRA (Low-Rank Adaptation)**\
A parameter-efficient fine-tuning technique that trains a small set of adapter weights rather than the full model. The adapter can be loaded on top of the base model at inference time.

**LoRA rank**\
A hyperparameter that controls the size of the LoRA adapter. Higher rank = more capacity but larger adapter and more training compute.

**GRPO (Group Relative Policy Optimization)**\
A reinforcement learning variant used in RFT. Optimizes model outputs using group-relative reward scoring rather than a separate value model.

**RFT (Reinforcement Fine-Tuning)**\
Fine-tuning using reinforcement learning signals rather than labeled examples. Trains the model to maximize a reward function — useful for tasks with verifiable outcomes such as math, code, and reasoning.

**Training shape**\
A validated trainer configuration for one base model and one training method. It fixes the GPU type and count per trainer replica, plus the maximum training context length. On the [Training API](/fine-tuning/training-api/training-shapes) you pass a shape ID such as `accounts/fireworks/trainingShapes/qwen3-8b-128k`; managed training jobs select a compatible shape for you.

**`dcp_save_interval`**\
RFT training parameter that controls how often full training state (weights + optimizer) is checkpointed. Default is `0` (disabled). Set to a positive integer to enable full checkpoint-and-resume including optimizer state.

**Epoch**\
One complete pass through the training dataset.

**Step**\
A single gradient update during training.

**Checkpoint**\
A saved snapshot of model state (and optionally optimizer state) at a point during training.

**`ppo_kl` vs `ref_kld`**\
Two KL divergence metrics logged during GRPO/RFT training. `ppo_kl` measures divergence between current and previous policy — stays near zero with one minibatch per rollout, which is expected. `ref_kld` measures divergence from the reference/base model — this is the metric to monitor for policy drift.

***

## Deployment

**Cold start**\
The latency incurred when a deployment scales up from zero replicas or provisions a new replica.

**Scale-to-zero**\
A deployment configuration where replica count drops to zero when there is no traffic. Eliminates idle costs but introduces cold-start latency.

**GPU hours**\
The billing unit for dedicated deployment capacity. Charged per GPU per hour of replica uptime.

**Prometheus metrics**\
Per-deployment performance and utilization metrics exposed via a Prometheus-compatible endpoint. Includes TTFT, TPS, GPU utilization, queue depth, and error rates.

***

## API & SDK

**API key**\
An authentication token used to make requests to the Fireworks API. Generated in the Fireworks console under Account > API Keys.

**OpenAI-compatible API**\
The Fireworks inference API is compatible with the OpenAI Chat Completions API format. Use the OpenAI Python SDK with Fireworks by changing `base_url` and `api_key`.

**`reconnect_and_wait()`**\
SDK method for recovering a training job that has been interrupted by pod preemption or a network error. Use in your training loop to make jobs resilient to transient interruptions.

**JSONL**\
JSON Lines format — one JSON object per line. Used for batch inference input files and training dataset uploads.

***

## Security & Compliance

**ISO 27001**\
International standard for information security management systems (ISMS). Fireworks has achieved ISO 27001 certification. Certificate available at [trust.fireworks.ai](https://trust.fireworks.ai).

**ISO 27701**\
Extension to ISO 27001 covering privacy information management. Fireworks has achieved ISO 27701 certification. Certificate available at [trust.fireworks.ai](https://trust.fireworks.ai).

**ISO 42001**\
International standard for AI management systems. Fireworks has achieved ISO 42001 certification. Certificate available at [trust.fireworks.ai](https://trust.fireworks.ai).

**SOC 2 Type II**\
An auditing standard that verifies a company's security, availability, and confidentiality controls over time. Fireworks maintains SOC 2 Type II compliance.

**HIPAA**\
U.S. healthcare data regulation. Fireworks supports HIPAA-compliant deployments for covered entities. Contact sales for Business Associate Agreement (BAA) details.

**Audit logs**\
A record of API activity on your account. Useful for security review and compliance reporting. Available via the Fireworks console and API.

**Trust Center**\
Fireworks' central repository for security documentation, compliance certificates, and data handling policies. Available at [trust.fireworks.ai](https://trust.fireworks.ai).

***

## Inference Parameters

**Temperature**\
Controls randomness in token sampling. `0.0` = deterministic. Higher values increase diversity.

**Top-p (nucleus sampling)**\
Limits token sampling to the smallest set of tokens whose cumulative probability exceeds `p`.

**Top-k**\
Limits token sampling to the top `k` most probable tokens at each step.

**Frequency penalty**\
Reduces the likelihood of tokens that have already appeared in the output. Discourages repetition.

**Presence penalty**\
Reduces the likelihood of tokens that have appeared at all in the output. Encourages the model to introduce new topics.

**Stop sequences**\
One or more strings that cause the model to stop generating when produced. Useful for controlling output format.

**System prompt**\
An instruction prepended to the conversation that sets the model's persona, task, or constraints.
