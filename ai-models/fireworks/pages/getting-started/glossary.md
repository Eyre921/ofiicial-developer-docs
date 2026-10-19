---
title: "Glossary"
source: https://docs.fireworks.ai/getting-started/glossary
path: getting-started/glossary
---

Glossary of key Fireworks AI terms across serverless, deployments, fine-tuning, and inference, with concise definitions to help you navigate the documentation.

This glossary covers terms you'll encounter when working with the Fireworks AI platform — across inference, training, deployments, security, and the API.

Start with the words in an API call. The later sections cover how Fireworks runs a model, then training, billing, and security.

## Start here

**Inference**\
A request that sends tokens to a model and gets tokens back. On Fireworks, inference is either [Serverless](/serverless/overview) (pay per token) or [on-demand](/guides/ondemand-deployments) (pay for GPUs you reserve).

**Token**\
The unit a model reads and writes. A token is a piece of a word, not a whole word. Fireworks bills Serverless usage in tokens: uncached input, cached input, and generated output. See [Serverless pricing](/serverless/pricing).

**Prompt tokens**\
The tokens you send, including the system prompt, conversation, and tool definitions. Also called input tokens.

**Cached prompt tokens**\
Prompt tokens served from [prompt caching](/guides/prompt-caching) because they repeat a prefix Fireworks already computed. They cost less than uncached prompt tokens. The discount depends on the model.

**Generated tokens**\
The tokens the model writes back. Also called output tokens or completion tokens.

**Open-weight model**\
A model whose weights you can run yourself. Fireworks hosts open-weight models such as DeepSeek, GLM, Kimi, and Qwen. A closed model, such as Claude or GPT, stays on that provider's API.

**Model ID**\
The string that names a model in a request. A Fireworks base model looks like `accounts/fireworks/models/glm-5p3-flash`. A short ID such as `glm-latest` can point at the current model in a family. See [Which model should I use?](/guides/recommended-models).

**Chat Completions API**\
The request format for a conversation: a list of `messages` with roles such as `system`, `user`, and `assistant`. Fireworks accepts the OpenAI Chat Completions shape at `https://api.fireworks.ai/inference/v1`.

**Serverless**\
Shared, Fireworks-managed inference. You send a request and pay per token. You do not choose the GPU or the replica count. See [Serverless overview](/serverless/overview).

**On-demand deployment**\
A deployment on GPUs reserved for your account. You pay for GPU time, including idle replicas, and you choose the model, hardware, and scaling. Docs also call this a dedicated deployment. LoRA adapters run on on-demand deployments.

**Standard, Priority, and Fast**\
Three Serverless modes. Standard is the default. Priority is more likely to stay available when Fireworks is busy, at a higher price. Fast is a separate high-speed model ID, such as `accounts/fireworks/routers/glm-5p3-fast`. See [Serverless Modes](/serverless/serverless-modes).

**Prompt caching**\
Reuse of a repeated prompt prefix so the next request starts faster. It is on by default. Cached prompt tokens are billed at a model-specific discount. See [Prompt caching](/guides/prompt-caching).

**Embedding**\
A list of numbers that represents a piece of text, used for search and similarity. Fireworks serves embedding models at `/v1/embeddings`. See [Embeddings and reranking](/guides/querying-embeddings-models).

**Reranker**\
A model that reorders search results by how well each passage matches a query. It does not write a chat reply.

**Instruct model**\
A model trained to follow chat instructions. Use it with Chat Completions. A base model that only continues raw text is a better fit for the [Completions API](/guides/completions-api).

**Reasoning model**\
A model that can spend extra tokens thinking before it answers. `reasoning_effort` controls that work. The thinking tokens still count as generated tokens.

**Vision model**\
A model that accepts images as well as text. Video and audio support depends on the model. See [Vision models](/guides/querying-vision-language-models) and [Video and audio inputs](/guides/video-audio-inputs).

**TPM (tokens per minute)**\
The Serverless rate-limit unit. Fireworks limits total prompt tokens per minute and generated tokens per minute. A `429` means you crossed a limit. A `503` means Fireworks is overloaded. See [Serverless rate limits](/serverless/rate-limits).

**Managed Training**\
Fireworks runs the training loop for you. You supply data and a method. Managed Training currently accepts SFT, DPO, and ORPO. It is LoRA-only. See [Managed Training](/fine-tuning/managed-finetuning-intro).

**Training API**\
You write the training loop in Python, and Fireworks runs it on GPUs. Use it for custom losses, full-parameter training, and reinforcement learning. See [Training API](/fine-tuning/training-api/introduction).

**DPO (Direct Preference Optimization)**\
Training on pairs of answers: one you prefer and one you do not. Use it when you can say which reply is better but cannot score a reply with a rule. ORPO is a related preference method. See [Preference optimization](/fine-tuning/dpo-fine-tuning).

**Full-parameter training**\
Training that updates all of the model weights, not only a LoRA adapter. This runs on the Training API.

**Fireworks Nexus**\
The product for using Fireworks models inside a coding harness, app, or gateway, with usage visibility and spend limits. See [Nexus](/nexus).

**FireConnect**\
The CLI that points a coding harness at Fireworks. The command is `fireconnect <harness>`. `fireconnect <harness> off` restores the harness settings. See [FireConnect](/nexus/fireconnect).

**FireRouter**\
One model ID, `firerouter`, that picks a model for each new user turn. Open-model turns run on Fireworks. Closed-model turns use a Provider Key. See [FireRouter](/nexus/firerouter).

**Provider Key**\
An Anthropic, OpenAI, or Amazon Bedrock key stored once on the Fireworks account so FireRouter can call a closed model. Developers still send only their Fireworks API key. Provider Keys are not available on every account. See [Provider Keys](/nexus/provider-keys).

**Session cost**\
The cost estimate Claude Code shows for the current session, through the FireConnect status line or `fireconnect claude usage`. It is an estimate, not the invoice. Account spend by model is the Cost tab on the usage page.

***

## Account & Billing

**Account**\
Your Fireworks AI organization identity. All deployments, models, training jobs, and API keys belong to an account. Referenced as `accounts/<your-account>` in firectl and the API.

**Credit**\
The unit used for prepaid usage on Fireworks. Credits are consumed as you use inference and training resources.

**Rate limiting / 429 errors**\
A `429 Too Many Requests` response means the request exceeded an adaptive Serverless token-per-minute limit. A `503` means Fireworks is overloaded. Priority mode is less likely to return a 503. On a dedicated deployment, add replicas or raise the autoscaling maximum to add capacity. See [Serverless rate limits](/serverless/rate-limits).

**Quota**\
A per-account cap on a resource, such as Serverless tokens per minute or on-demand GPUs. See [Account quotas](/guides/quotas_usage/account-quotas).

**ZDR (Zero Data Retention)**\
The default behavior for all open model inference on Fireworks: no prompts, completions, or request logs are stored after the response is returned. ZDR is on by default — it is not an opt-in feature.

**BYOC (Bring Your Own Cloud)**\
An enterprise option to run inference entirely within your own cloud account. Your data never touches Fireworks-managed infrastructure. Contact sales for availability.

***

## Fireworks Platform

**Serverless inference**\
Pay-per-token inference with no deployment management. Requests are routed globally by default; [US-only Serverless](/serverless/us-only-serverless) serves supported models from the US. Dedicated deployments support explicit placement with the **`--region`** flag on `firectl deployment create` (for example `GLOBAL`, `US`, `CANADA`, `EUROPE`, `APAC`).

**Dedicated deployment**\
A deployment you provision and manage, with reserved GPU capacity. Gives you control over model, hardware, placement, autoscaling, and addon support. Created with `firectl deployment create`.

**Multi-region deployment**\
A dedicated deployment configured to run replicas across multiple datacenters. Enabled with `--region GLOBAL` (or a specific multi-region: `US`, `CANADA`, `EUROPE`, `APAC`) on `firectl deployment create`. Increases availability and throughput. New accounts receive quota for **GLOBAL** only; other placements require quota granted by Fireworks.

**Placement**\
Controls which regions a dedicated deployment is allowed to schedule replicas in. On the CLI, set at creation time with **`--region`** (`GLOBAL`, `US`, `CANADA`, `EUROPE`, `APAC`, or a specific region id). Cannot be changed after deployment creation — recreate the deployment to change placement. If not specified, the deployment pins to a single datacenter at creation time. Only **GLOBAL** has default quota; non-GLOBAL placements require quota granted by Fireworks.

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
Fine-tuning that uses a reward signal instead of labeled examples. Managed RFT is paused and does not accept new jobs. New reinforcement learning runs on the [Training API](/fine-tuning/training-api/cookbook/rl), where you write the rollout and training loop.

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

**`ppo_kl` vs `ref_kl`**\
Two KL divergence metrics logged during GRPO/RFT training. `ppo_kl` measures divergence between current and previous policy — stays near zero with one minibatch per rollout, which is expected. `ref_kl` (logged as `train/ref_kl` by cookbook recipes when a reference model is configured) measures divergence from the reference/base model — this is the metric to monitor for policy drift.

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
