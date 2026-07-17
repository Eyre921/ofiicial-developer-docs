---
title: "Changelog"
source: https://docs.together.ai/docs/changelog
path: docs/changelog
---

<Update label="July 16, 2026">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `thinkingmachines/Inkling`: 552.8B parameters, 524,288 context length, NVFP4 quantization. Pricing: \$1.00 input / \$4.05 output / \$0.17 cached input (per 1M tokens).

  ## Dedicated model inference

  [Dedicated model inference](/docs/dedicated-endpoints/overview) (DMI) serves a model on reserved GPUs, giving you higher throughput, lower latency, and predictable performance with no hard rate limits. It uses the same [inference APIs](/docs/inference/overview#shared-inference-api) as serverless, so you can prototype on serverless and deploy on dedicated hardware without changing your application code.

  **What's new:**

  * **Deploy in one command:** `tg beta endpoints deploy` creates an endpoint, attaches a deployment, and routes all traffic to it.
  * **New resource model:** Compose models, configs, endpoints, deployments, and traffic splits to control how your model is served. See [Concepts](/docs/dedicated-endpoints/concepts).
  * **A/B tests and shadow experiments:** [Split live traffic across variants](/docs/dedicated-endpoints/ab-tests), or [mirror traffic to a new deployment](/docs/dedicated-endpoints/shadow-experiments) without serving its responses.
  * **Autoscaling and serving controls:** Scale on request or GPU metrics, scale to zero on idle, and tune serving behavior per deployment. See [Configure autoscaling](/docs/dedicated-endpoints/scaling).

  <Note>
    If you're already using dedicated endpoints, you can migrate to the v2 API by following the [migration guide](/docs/dedicated-endpoints/migrate-from-v1).
  </Note>

  ## Image inputs for evaluations

  You can now evaluate vision-capable models on image datasets. Add an `image_data_urls` column to your evaluation dataset — a base64 image data URL, or a list of them — and the images are attached to the model and judge requests alongside the text prompt.

  See [Prepare your dataset](/docs/ai-evaluations#1-prepare-your-dataset) for details.
</Update>

<Update label="July 10, 2026">
  ## Model deprecations

  The following models have been deprecated and are no longer available on serverless:

  * `Qwen/Qwen3-235B-A22B-Instruct-2507-tput`. Available as an on-demand dedicated endpoint.
  * `meta-llama/Meta-Llama-3-8B-Instruct-Lite`. Available as an on-demand dedicated endpoint.
  * `zai-org/GLM-5.1`. Available as an on-demand dedicated endpoint.

  See [Deprecations](/docs/deprecations) for migration options.
</Update>

<Update label="July 9, 2026">
  ## TorchTitan training health check

  You can now run a TorchTitan training health check on your GPU clusters. It runs a short training benchmark on one or more nodes and measures steady-state model FLOPs utilization (MFU) to validate end-to-end training throughput. This feature is in preview and runs on demand on NVIDIA B200 (Blackwell) nodes.

  See [Health checks](/docs/health-checks) for the available tests, thresholds, and results.
</Update>

<Update label="July 9, 2026">
  ## Storage performance health check

  You can now run a storage performance health check on your GPU clusters. It uses `fio` to validate data integrity and measure sequential read and write bandwidth on the cluster's storage volumes, and it also runs automatically during cluster acceptance testing.

  See [Health checks](/docs/health-checks) for the available tests, thresholds, and results.

  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `LiquidAI/LFM2.5-8B-A1B`: 32,768 context length. Pricing: \$0.03 input / \$0.12 output (per 1M tokens).

  ## Model deprecations

  The following model has been deprecated and is no longer available on serverless:

  * `LiquidAI/LFM2-24B-A2B`. Recommended replacement: `LiquidAI/LFM2.5-8B-A1B`.

  See [Deprecations](/docs/deprecations) for migration options.
</Update>

<Update label="July 8, 2026">
  ## Provisioned throughput

  [Provisioned throughput](/docs/inference/provisioned-throughput) is now available, allowing you to reserve inference capacity for frontier open models. Commit to a one-month-or-longer term, and Together commits to throughput and reliability targets for traffic within your purchased capacity.

  At launch, provisioned throughput is available for `MiniMaxAI/MiniMax-M3` and `zai-org/GLM-5.2`.

  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `HappyHorse/HappyHorse-1.0-T2V` (text-to-video).

  ## Reasoning API field

  The `reasoning` field is now symmetric for input and output on reasoning models. Pass prior assistant reasoning back under `reasoning` for preserved thinking and multi-turn tool calling. The older `reasoning_content` key is still accepted on input for backward compatibility.

  See [Reasoning](/docs/inference/chat/reasoning#handle-reasoning-tokens) for details.

  ## Usage object shape

  The `usage` object varies by model. Reasoning models nest cached and reasoning token counts under `prompt_tokens_details` and `completion_tokens_details`, while some non-reasoning models return `cached_tokens` at the top level. Read both shapes defensively so clients do not silently report zero.

  See [OpenAI compatibility](/docs/inference/openai-compatibility#response-shape-differences) for examples.
</Update>

<Update label="July 7, 2026">
  ## Project slug editing

  Project Admins can now change a Project's slug from Project Settings. The new slug takes effect immediately. You can also copy any Project's slug from the Projects list in Organization Settings.

  Changing a slug can break API requests, scripts, and integrations that reference resources by their slug-qualified path. Update any references that rely on the old slug.

  See [Projects](/docs/projects#changing-a-project-slug) for details.

  ## GPU cluster creation region selection

  The create cluster flow now defaults the **Region** field to **Any region**. Together picks the region with the most available capacity for your GPU type at create time. Changing the GPU type resets the region to **Any region** and clears any selected shared volume.

  See the [GPU Clusters quickstart](/docs/gpu-clusters-quickstart) for the full create flow.
</Update>

<Update label="July 6, 2026">
  ## New models available for fine-tuning

  You can now fine-tune the following vision-language model:

  * `google/gemma-4-31B-it-VLM`.

  See [Supported models](/docs/fine-tuning/supported-models) for the full list.
</Update>

<Update label="July 2, 2026">
  ## Bring your own model: Transformers v5

  [BYOM fine-tuning](/docs/fine-tuning/byom) now supports Hugging Face models built with Transformers v5 or earlier.
</Update>

<Update label="July 1, 2026">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `google/flash-image-3.1-lite` (Gemini 3.1 Flash-Lite Image).
  * `Qwen/Qwen3.6-35B-A3B-Lora`: 262,144 context length.
  * `alibaba/happyhorse-1.1-i2v` (image-to-video).
  * `alibaba/happyhorse-1.1-r2v` (reference-to-video).
  * `alibaba/happyhorse-1.1-t2v` (text-to-video).
</Update>

<Update label="June 29, 2026">
  ## Model deprecations

  The following model has been deprecated and is no longer available on serverless:

  * `Qwen/Qwen3.5-397B-A17B`.

  See [Deprecations](/docs/deprecations) for migration options.
</Update>

<Update label="June 26, 2026">
  ## Model deprecations

  The following models have been deprecated and are no longer available on serverless:

  * `zai-org/GLM-5.1`. Available as an on-demand dedicated endpoint.
  * `meta-llama/Meta-Llama-3-8B-Instruct-Lite`. Available as an on-demand dedicated endpoint.
  * `google/gemma-3n-E4B-it`. Available as an on-demand dedicated endpoint.
  * `Qwen/Qwen3-235B-A22B-Instruct-2507-tput`. Available as an on-demand dedicated endpoint.
  * `meta-llama/Llama-Guard-4-12B`.

  See [Deprecations](/docs/deprecations) for migration options.
</Update>

<Update label="June 25, 2026">
  ## Seedance 2.0 adds 4K video

  `ByteDance/Seedance-2.0` now supports a `4k` resolution tier (up to 3840x2160), alongside the existing 480p, 720p, and 1080p tiers. Pass `resolution: "4k"` to generate at the new tier.

  Pricing for the higher tiers (per second of output):

  * 1080p: \$0.40 (text/image-to-video), from \$0.48 (video-to-video).
  * 4K: \$0.836 (text/image-to-video), from \$1.050 (video-to-video).

  See [Seedance 2.0](/docs/seedance2.0-quickstart) for details.
</Update>

<Update label="June 24, 2026">
  ## Automatic node repair for GPU clusters

  GPU clusters now support passive health checks and automatic node repair. Passive checks monitor your nodes continuously in the background, and when they (or active checks) detect a node-level issue, the system generates a repair recommendation for you to review and accept from the new **Repairs** tab. Together then handles the cordon, drain, remediation, and node rejoin.

  See [Health checks](/docs/health-checks) and [Node repair](/docs/node-repair) for details.

  ## Estimate fine-tuning job cost via API

  A new endpoint, `POST /fine-tunes/estimate-price`, returns the estimated total price of a fine-tuning job before you launch it, along with estimated training and evaluation token counts and your remaining credit limit. Call it from the Python SDK or TypeScript SDK with the same parameters you plan to submit to the create-job endpoint.

  See [Fine-tuning pricing](/docs/fine-tuning/pricing#estimate-job-cost) for details.

  ## New models available for fine-tuning

  You can now fine-tune the following models:

  * `moonshotai/Kimi-K2.7-Code`.
  * `moonshotai/Kimi-K2.6`.

  See [Supported models](/docs/fine-tuning/supported-models) for the full list.
</Update>

<Update label="June 23, 2026">
  ## Whoami API endpoint

  Use `GET /whoami` to confirm which API key, Project, and Organization are authenticating a request. The response includes the Project slug used in dedicated endpoint model names.

  See [Whoami](/reference/whoami) for details.

  ## Early stopping for fine-tuning

  Fine-tuning jobs now support early stopping, which halts training when validation loss stops improving. This reduces cost and helps avoid overfitting on long runs.

  Enable it by setting `early_stopping_enabled=true` on job creation along with a `validation_file` and `n_evals >= early_stopping_patience + early_stopping_warmup_evals + 1`. Tune behavior with `early_stopping_patience`, `early_stopping_min_delta`, and `early_stopping_warmup_evals`.

  When training halts early, the job still finishes with status `completed`. The response sets `early_stopped=true` and exposes the winning checkpoint via `early_stopping_best_step` and `early_stopping_best_metric`.

  See [Early stopping](/docs/fine-tuning/early-stopping) for details.

  ## Audio transcription upload limit

  Direct (binary) audio uploads for transcription and translation are now capped at 80 MB per request. For larger files, host the audio at a public HTTPS URL and pass that URL as the `file` field, which supports up to 1 GB. When sending a binary upload, place the `model` form field before the `file` field in the multipart body.

  See [Transcribe audio](/docs/inference/transcription/overview#limits) for details.
</Update>

<Update label="June 22, 2026">
  ## Attach LoRA adapters to a dedicated endpoint

  You can now attach multiple LoRA adapters to a single LoRA-enabled dedicated endpoint so they share the same hardware, instead of deploying one endpoint per adapter. Manage bindings from the [Python SDK](/python-library), the TypeScript SDK, the CLI, or the API:

  * `together endpoints adapters add <endpoint_id> <endpoint_name>:<adapter_model_name>`
  * `together endpoints adapters list <endpoint_id>`
  * `together endpoints adapters remove <endpoint_id> <endpoint_name>:<adapter_model_name>`

  This feature is in preview. See [Attach a LoRA adapter to an endpoint](/docs/dedicated-endpoints/v1/lora-adapter).
</Update>

<Update label="June 22, 2026">
  ## Model deprecations

  The following model has been deprecated and is no longer available on serverless:

  * `zai-org/GLM-5`. Recommended replacement: `zai-org/GLM-5.2`.

  See [Deprecations](/docs/deprecations) for migration options.
</Update>

<Update label="June 17, 2026">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `zai-org/GLM-5.2`: 262K context length, FP4 quantization. Pricing: \$1.40 input / \$4.40 output / \$0.26 cached input (per 1M tokens). Supports function calling and structured outputs.

  ## Organization and Project role labels

  Organization members now use the Admin and Developer labels, and Project collaborators now use Admin and Editor labels. Permissions are unchanged, but the labels make Organization-wide access and Project-scoped editing clearer.

  See [Roles & permissions](/docs/roles-permissions) for details.
</Update>

<Update label="June 15, 2026">
  ## Model deprecations

  The following models are scheduled for deprecation and will no longer be available on serverless after June 29, 2026:

  * `Qwen/Qwen3.5-397B-A17B`. Recommended replacement: `MiniMaxAI/MiniMax-M3`, available as an on-demand dedicated endpoint.

  See [Deprecations](/docs/deprecations) for migration options.
</Update>

<Update label="June 13, 2026">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `moonshotai/Kimi-K2.7-Code`: 262,144 context length, FP4 quantization. Pricing: \$0.95 input / \$4.00 output / \$0.19 cached input (per 1M tokens). Supports function calling and structured outputs.
</Update>

<Update label="June 12, 2026">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `MiniMaxAI/MiniMax-M3`: 524,288 context length, FP4 quantization. Pricing: \$0.30 input / \$1.20 output / \$0.06 cached input (per 1M tokens).
</Update>

<Update label="June 11, 2026">
  ## Model deprecations

  The following model has been deprecated and is no longer available on serverless:

  * `mistralai/Voxtral-Mini-3B-2507`. Available as an on-demand dedicated endpoint.

  See [Deprecations](/docs/deprecations) for migration options.
</Update>

<Update label="June 9, 2026">
  ## Pricing update

  The following changes are effective June 9, 2026:

  **New cached input pricing** (per 1M tokens):

  * `zai-org/GLM-5.1`: \$0.26 cached input (81% discount from \$1.40 standard input).
  * `Qwen/Qwen3.5-397B-A17B`: \$0.35 cached input (42% discount from \$0.60 standard input).

  **Price decrease** for `deepseek-ai/DeepSeek-V4-Pro` (per 1M tokens):

  * Input: \$2.10 → \$1.74.
  * Output: \$4.40 → \$3.48.
  * Cached input: \$0.20 (unchanged).

  See [Serverless models](/docs/serverless/models) for the full pricing catalog.
</Update>

<Update label="June 8, 2026">
  ## Server-side validation for fine-tuning datasets

  Files uploaded for fine-tuning now go through full server-side schema validation during ingestion, with the result exposed on the file object. Poll the Files API and read `processing_status` (`COMPLETED`, `INVALID_FORMAT`, or `FAILED`) plus `validation_report` to detect dataset issues programmatically before launching a job, like missing `role` fields or malformed conversation turns.

  Errors include a user-facing reason, so you can fix the dataset and re-upload without trial-and-error training runs. For example:

  ```
  Line 7: messages[1] must contain a role field
  ```
</Update>

<Update label="June 4, 2026">
  ## Model deprecations

  The following model has been deprecated and is no longer available on serverless:

  * `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`. Recommended replacement: `MiniMaxAI/MiniMax-M2.7`, available as an on-demand dedicated endpoint.

  See [Deprecations](/docs/deprecations) for migration options.
</Update>

<Update label="June 1, 2026">
  ## Fine-tuning job metrics API

  A new API endpoint, `GET /fine-tunes/{id}/metrics`, returns training metrics for a fine-tuning job (e.g. loss curves and other per-step values) so you can monitor progress programmatically without opening the dashboard. See the [API reference](/reference/get-fine-tunes-id-metrics) and [Fine-tuning training metrics](/docs/fine-tuning-training-metrics) for details.

  ## Slurm startup scripts for GPU Clusters

  GPU clusters now support Slurm startup scripts (lifecycle hook scripts that run at node startup, job allocation, and job completion). Use them to install packages at boot, configure SSH sessions, or run per-job prolog and epilog actions across worker, login, and controller nodes. See [Slurm startup scripts](/docs/slurm-startup-scripts) for details.

  ## Evaluations: Single-pass compare mode

  The `compare` evaluator now accepts a `disable_position_bias_correction` parameter. By default, the judge runs each comparison twice (A→B then B→A) and reconciles verdicts to cancel position bias. Setting `disable_position_bias_correction` to `true` runs a single pass, cutting judge cost and latency in half. See [AI evaluations](/docs/ai-evaluations) for details.

  ## Billing documentation updates

  Updated billing docs for multiple payment methods, separate invoice addresses, ACH payment behavior, auto-recharge limits with bank transfers, and prepaid-only access (no negative balance limits). See [Payment methods & invoices](/docs/billing-payment-methods), [Credits](/docs/billing-credits), and [Billing troubleshooting](/docs/billing-troubleshooting).
</Update>

<Update label="May 29, 2026">
  ## Pricing update

  The following models have updated pricing, effective May 29, 2026. All usage from that date forward will be billed at the new rates (per 1M tokens):

  * `Qwen/Qwen3.5-9B`: \$0.10 → \$0.17 (input), \$0.15 → \$0.25 (output).
  * `meta-llama/Meta-Llama-3-8B-Instruct-Lite`: \$0.10 → \$0.14 (input), \$0.10 → \$0.14 (output).
  * `meta-llama/Llama-3.3-70B-Instruct-Turbo`: \$0.88 → \$1.04 (input), \$0.88 → \$1.04 (output).

  See [Serverless models](/docs/serverless/models) for the full pricing catalog.
</Update>

<Update label="May 27, 2026">
  ## Model deprecations

  The following model has been deprecated and is no longer available on serverless:

  * `black-forest-labs/FLUX.1-krea-dev`.

  See [Deprecations](/docs/deprecations) for migration options.
</Update>

<Update label="May 25, 2026">
  ## New serverless models

  The following image and video models are now available on [serverless](/docs/serverless/models):

  **Image**

  * `ByteDance/Seedream-5.0-lite`.

  **Video**

  * `alibaba/happyhorse-1.0-i2v` (image-to-video).
  * `alibaba/happyhorse-1.0-r2v` (reference-to-video).
  * `google/veo-3.1`.
  * `google/veo-3.1-lite`.

  ## New dedicated endpoint models

  The following models are now available for deployment on [dedicated endpoints](/docs/dedicated-endpoints/models):

  * `google/gemma-3-1b-it`.
  * `google/gemma-3-27b-it`.
  * `google/gemma-3-27b-it-lora`.
  * `google/gemma-4-31B-it-lora`.
  * `google/medgemma-27b-text-it`.
  * `allenai/Molmo-7B-D-0924`.
  * `meta-llama/Llama-3.2-3B-Instruct`.
  * `meta-llama/Llama-4-Scout-17B-16E-Instruct-FP8-Lora`.
  * `Qwen/Qwen2.5-14B`.
  * `Qwen/Qwen2.5-32B`.
  * `Qwen/Qwen3-235B-A22B-Instruct-2507-FP8`.
  * `Qwen/Qwen2-72B`.
  * `arcee-ai/trinity-mini`.
  * `BAAI/bge-base-en-v1.5`.
  * `minimax/speech-2.8-turbo`.
  * `rime-labs/rime-mist-v3`.
  * `rime-labs/rime-mist-v3-omni`.

  ## Seedance 2.0 quickstart

  A quickstart is now available for [Seedance 2.0](/docs/seedance2.0-quickstart), ByteDance's unified multimodal audio-video generation model. The guide covers text-to-video, image-to-video, video extension, and instruction-based editing.
</Update>

<Update label="May 22, 2026">
  ## GPU Clusters: External OIDC authentication and RBAC

  GPU clusters now support external OpenID Connect (OIDC) authentication, allowing each team member to access the cluster's Kubernetes API using their organization's identity provider — Google, Okta, Auth0, Microsoft Entra ID, and others.

  With OIDC enabled, access is managed through standard Kubernetes RBAC: admins bind permissions to individual user identities, and each user authenticates via their browser using SSO. This replaces shared kubeconfig credentials with per-user tokens, per-user audit trails, and clean revocation. Currently this feature is only supported for Kubernetes clusters.

  OIDC must be configured at cluster creation time. See [Set up OIDC authentication](/docs/cluster-oidc) for the full setup guide.
</Update>

<Update label="May 22, 2026">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `Qwen/Qwen3.7-Max`. Pricing: \$2.50 input / \$7.50 output (per 1M tokens).
</Update>

<Update label="May 21, 2026">
  ## Model deprecations

  The following model has been deprecated and is no longer available on serverless:

  * `moonshotai/Kimi-K2.5`.

  See [Deprecations](/docs/deprecations) for migration options.
</Update>

<Update label="May 15, 2026">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `pearl-ai/gemma-4-31b-it`: 32,000 context length, INT8 quantization. Pricing: \$0.28 input / \$0.86 output (per 1M tokens).
</Update>

<Update label="May 14, 2026">
  ## Model deprecations

  The following models have been deprecated and are no longer available on serverless:

  * `deepseek-ai/DeepSeek-R1`.
  * `deepseek-ai/DeepSeek-V3.1`.
  * `Qwen/Qwen3-Coder-Next-FP8`.

  ## Upcoming pricing update

  The following model will have updated pricing, effective May 21, 2026:

  * `google/gemma-4-31b-it`: \$0.20 → \$0.39 (input), \$0.50 → \$0.97 (output) per 1M tokens.

  All usage from that date forward will be billed at the new rate.
</Update>

<Update label="May 8, 2026">
  ## External collaborators for projects

  You can now invite users from outside your organization to collaborate on a project. Enable **Allow external collaborators** on the project's settings page, then add them like any other collaborator. The feature is currently in beta. See [roles & permissions](/docs/roles-permissions#external-collaborators-beta) for more details.

  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `alibaba/happyhorse-1.0-t2v`: \$0.24/sec at 1080p.
  * `ByteDance/Seedance-2.0`: \$0.16/sec at 720p.
</Update>

<Update label="May 7, 2026">
  ## Together CLI v2.10

  The Together CLI has been updated with `tg` as the canonical command name and a refreshed command tree. Subcommands are now clearer and more consistent across fine-tuning, endpoints, evals, files, clusters, and jig.

  See [CLI reference](/reference/cli/getting-started) for details.

  ## Speech-to-text and translation: new audio formats

  The `/v1/audio/transcriptions` and `/v1/audio/translations` endpoints now accept `.ogg`, `.opus`, and `.aac` files in addition to `.wav`, `.mp3`, `.m4a`, `.webm`, and `.flac`.

  ## Speech-to-text: task field is now optional in verbose JSON responses

  The `task` field has been removed from the required fields of `AudioTranscriptionVerboseJsonResponse` and `AudioTranslationVerboseJsonResponse`. Clients that previously asserted on its presence should treat it as optional.
</Update>

<Update label="May 6, 2026">
  ## Slurm-on-Kubernetes v1.0 for all new Slurm clusters

  All newly provisioned Slurm GPU clusters now run on a new Slurm-on-Kubernetes stack with significant reliability improvements. Existing clusters can be migrated in place.

  **What's new:**

  * **Self-healing worker daemons:** The Slurm worker daemon is now supervised and auto-restarts on crash, so transient failures recover without operator intervention or impact on healthy nodes.
  * **Durable job accounting:** Job history (`sacct`) is now persisted on durable, PVC-backed storage. Restarts and pod reschedules no longer wipe accounting data.
  * **Correct process tracking and cleanup:** Job processes (including daemonized children) are tracked at the kernel cgroup level and reliably cleaned up at job completion. No more orphaned processes holding GPU memory or `/dev/shm`.
  * **Zombie reaping:** A dedicated init process reaps orphaned children, preventing PID-table exhaustion from blocking new jobs.
  * **GPU state correctness:** The Slurm GPU view is rebuilt fresh on every node start, eliminating "GPU not found" failures after pod reschedules.
  * **Per-cluster GPU utilization metrics:** DCGM metrics are now exposed in your cluster's Grafana dashboards for fine-grained utilization visibility.

  See [Slurm configuration](/docs/slurm-configuration) for more details.
</Update>

<Update label="May 1, 2026">
  ## Model deprecations

  The following model has been deprecated and is no longer available on serverless:

  * `MiniMaxAI/MiniMax-M2.5`.
</Update>

<Update label="April 30, 2026">
  ## Text-to-speech: pronunciation\_dict parameter

  A new `pronunciation_dict` parameter is available for TTS requests. Pass a list of `"<source>/<replacement>"` rules (e.g., `["omg/oh my god"]`) to override how the model pronounces specific tokens.

  ## Together Deployments: custom metric autoscaling

  Deployments can now autoscale on any Prometheus metric exposed by your worker's `/metrics` endpoint. Set `metric = "CustomMetric"` and provide a `custom_metric_name` (e.g., `vllm:num_requests_running`) along with a `target` to scale on application-specific signals.
</Update>

<Update label="April 28, 2026">
  ## Fine-tuning: new supported models

  The following models are now available for fine-tuning:

  * `Qwen/Qwen3.6-35B-A3B`.
  * `google/gemma-4-31B-it`.
  * `google/gemma-4-26B-A4B-it`.
</Update>

<Update label="April 24, 2026">
  ## DeepSeek-V4-Pro on serverless

  `deepseek-ai/DeepSeek-V4-Pro` has been added to serverless.

  * Context length: 512,000.
  * Pricing: \$2.10 input / \$4.40 output / \$0.20 cached input (per 1M tokens).
  * Quantization: FP4.
  * Function calling and structured outputs supported.

  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `deepcogito/cogito-v2-1-671b`.
  * `google/veo-3.1-test-debug`.
  * `vidu/vidu-q3`.
  * `vidu/vidu-q3-turbo`.
  * `Wan-AI/wan2.7-i2v`.
  * `Wan-AI/wan2.7-r2v`.

  ## Pricing update: no-packing fine-tuning jobs

  We rolled out a pricing update for no-packing fine-tuning jobs. When the no-packing option is chosen, the number of training dataset tokens is now calculated as `len(dataset) * max_seq_length` to account for the compute used by packing-free jobs.

  * `max_seq_length` is configurable in both the SDK and UI.
  * Price prediction reflects these changes, so if no-packing is chosen you can control the cost of the job by adjusting the sequence length.
</Update>

<Update label="April 22, 2026">
  ## Dynamic rate limits and prepaid billing

  * Build Tiers 1–5, Scale, and Enterprise tier labels have been retired. Dynamic rate limits are now live for all users.
  * Billing has moved to a fully prepaid model.
  * Model-specific tier gates have been removed. The platform-wide \$5 credit purchase is the only gate.

  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `moonshotai/Kimi-K2.6`.
</Update>

<Update label="April 15, 2026">
  ## Pricing update

  The following model has updated pricing, effective April 15, 2026:

  * **`google/gemma-3n-E4B-it`:** \$0.02 → \$0.06 (input), \$0.04 → \$0.12 (output) per 1M tokens.
</Update>

<Update label="April 14, 2026">
  ## Model deprecations

  The following models have been deprecated and are no longer available:

  * `Qwen/Qwen3-VL-8B-Instruct`.
  * `Qwen/Qwen3-235B-A22B-Thinking-2507`.
  * `mistralai/Mixtral-8x7B-Instruct-v0.1`.
</Update>

<Update label="April 11, 2026">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `MiniMaxAI/MiniMax-M2.7`.
</Update>

<Update label="April 8, 2026">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `google/gemma-4-31B-it`.
  * `zai-org/GLM-5.1`.
</Update>

<Update label="April 2, 2026">
  ## Model deprecations

  The following models have been deprecated and are no longer available:

  * `zai-org/GLM-4.5-Air-FP8`.
  * `zai-org/GLM-4.7`.
  * `Qwen/Qwen3-Next-80B-A3B-Instruct`.
</Update>

<Update label="March 31, 2026">
  ## Model deprecations

  The following model has been deprecated and is no longer available:

  * `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8`.
</Update>

<Update label="March 10, 2026">
  ## Cached input token pricing

  Cached input token pricing is now available:

  * `MiniMaxAI/MiniMax-M2.5`: \$0.06 per 1M cached input tokens (80% off standard input price).
</Update>

<Update label="March 7, 2026">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `Qwen/Qwen3.5-9B`.
</Update>

<Update label="March 6, 2026">
  ## Model deprecations

  The following models have been deprecated and are no longer available:

  * `mixedbread-ai/Mxbai-Rerank-Large-V2`.
  * `moonshotai/Kimi-K2-Thinking`.
  * `meta-llama/Llama-3.2-3B-Instruct-Turbo`.
  * `moonshotai/Kimi-K2-Instruct-0905`.
</Update>

<Update label="February 25, 2026">
  ## Model deprecations

  The following models have been deprecated and are no longer available:

  * `black-forest-labs/FLUX.1-dev`.
  * `black-forest-labs/FLUX.1-dev-lora`.
  * `black-forest-labs/FLUX.1-kontext-dev`.
  * `Qwen/Qwen3-VL-32B-Instruct`.
  * `mistralai/Ministral-3-14B-Instruct-2512`.
  * `Qwen/Qwen3-Next-80B-A3B-Thinking`.
  * `Alibaba-NLP/gte-modernbert-base`.
  * `BAAI/bge-base-en-v1.5`.
  * `meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo`.
  * `meta-llama/Llama-Guard-3-11B-Vision-Turbo`.
  * `meta-llama/LlamaGuard-2-8b`.
  * `marin-community/marin-8b-instruct`.
  * `nvidia/NVIDIA-Nemotron-Nano-9B-v2`.
</Update>

<Update label="February 16, 2026">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `Qwen/Qwen3.5-397B-A17B`.
</Update>

<Update label="February 15, 2026">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `MiniMaxAI/MiniMax-M2.5`.
</Update>

<Update label="February 13, 2026">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `zai-org/GLM-5`.
</Update>

<Update label="February 12, 2026">
  ## Dedicated Container Inference launch

  Together AI has officially launched [Dedicated Container Inference](https://www.together.ai/dedicated-container-inference) (DCI), formerly known as BYOC. DCI lets you containerize, deploy, and scale custom models on Together AI.

  * [Blog post](https://www.together.ai/blog/dedicated-container-inference).
  * [Documentation](/docs/dedicated-container-inference).
  * [Getting started](/docs/containers-quickstart#example-guides).
</Update>

<Update label="February 6, 2026">
  ## Model deprecations

  The following models have been deprecated and are no longer available:

  * `togethercomputer/m2-bert-80M-32k-retrieval`.
  * `Salesforce/Llama-Rank-V1`.
  * `togethercomputer/Refuel-Llm-V2`.
  * `togethercomputer/Refuel-Llm-V2-Small`.
  * `Qwen/Qwen3-235B-A22B-fp8-tput`.
  * `qwen-qwen2-5-14b-instruct-lora`.
  * `meta-llama/Llama-4-Scout-17B-16E-Instruct`.
  * `Qwen/Qwen2.5-72B-Instruct-Turbo`.
  * `meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo`.
  * `BAAI/bge-large-en-v1.5`.
</Update>

<Update label="February 4, 2026">
  ## Python SDK v2.0 general availability

  Together AI is releasing the **Python SDK v2.0**, a new, type-safe, OpenAPI-driven client designed to be faster, easier to maintain, and ready for everything we're building next.

  * **Install:** `pip install together` or `uv add together`.
  * **Migration guide:** A detailed [Python SDK Migration Guide](/docs/pythonv2-migration-guide) covers API-by-API changes, type updates, and troubleshooting tips.
  * **Code and docs:** Access the [Together Python v2 repo](https://github.com/togethercomputer/together-py) and [reference docs](/reference/chat-completions-1) with code examples.
  * **Main goal:** Replace the legacy v1 Python SDK with a modern, strongly-typed, OpenAPI-generated client that matches the API surface more closely and stays in lock-step with new features.
  * **Net new:** All new features will be built in version 2 moving forward. This first version already includes beta APIs for our Instant Clusters.
</Update>

<Update label="February 3, 2026">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `Qwen/Qwen3-Coder-Next-FP8`.

  ## Model deprecations

  The following models have been deprecated and are no longer available:

  * `deepseek-ai/DeepSeek-R1-0528-tput`.
</Update>

<Update label="January 29, 2026">
  ## Model redirects

  The following models are now being automatically redirected to their upgraded versions. See our [Model Lifecycle Policy](/docs/deprecations#model-lifecycle-policy) for details.

  | Original model                       | Redirects to                              |
  | :----------------------------------- | :---------------------------------------- |
  | `mistralai/Mistral-7B-Instruct-v0.3` | `mistralai/Ministral-3-14B-Instruct-2512` |
  | `zai-org/GLM-4.6`                    | `zai-org/GLM-4.7`                         |

  These are same-lineage upgrades with compatible behavior. If you need the original version, deploy it as a [dedicated endpoint](/docs/dedicated-endpoints).
</Update>

<Update label="January 27, 2026">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `moonshotai/Kimi-K2.5`.
</Update>

<Update label="January 23, 2026">
  ## Model redirects

  The following models are now being automatically redirected to their upgraded versions. See our [Model Lifecycle Policy](/docs/deprecations#model-lifecycle-policy) for details.

  | Original model     | Redirects to    |
  | :----------------- | :-------------- |
  | `DeepSeek-V3-0324` | `DeepSeek-V3.1` |

  These are same-lineage upgrades with compatible behavior. If you need the original version, deploy it as a [dedicated endpoint](/docs/dedicated-endpoints).
</Update>

<Update label="January 21, 2026">
  ## Prompt caching now enabled by default for dedicated model inference

  Prompt caching is now **automatically enabled** for all newly created dedicated endpoints. This change improves performance and reduces costs by default.

  **What's changing:**

  * The `disable_prompt_cache` field (API), `--no-prompt-cache` flag (CLI), and related SDK parameters are now **deprecated**.
  * Prompt caching will always be enabled. The field is accepted but ignored after deprecation.

  **Timeline:**

  * **Now:** Field is deprecated; setting it has no effect (prompt caching is always on).
  * **February 2026:** Field will be removed.

  **Action required:**

  * `--no-prompt-cache` in CLI commands has no effect. You can remove it.
  * `disable_prompt_cache` from API requests has no effect. You can remove it.
  * SDK calls that set this parameter have no effect. You can remove it.

  No changes are required for existing endpoints. This only affects endpoint creation.
</Update>

<Update label="January 9, 2026">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `zai-org/GLM-4.7`.
</Update>

<Update label="January 5, 2026">
  ## Model deprecations

  The following models have been deprecated and are no longer available:

  * `Qwen/Qwen2.5-VL-72B-Instruct`.
</Update>

<Update label="December 23, 2025">
  ## Model deprecations

  The following models have been deprecated and are no longer available:

  * `deepseek-ai/DeepSeek-R1-Distill-Llama-70B`.
  * `meta-llama/Meta-Llama-3-70B-Instruct-Turbo`.
  * `black-forest-labs/FLUX.1-schnell-free`.
  * `meta-llama/Meta-Llama-Guard-3-8B`.
</Update>

<Update label="December 17, 2025">
  ## Model redirects

  The following models are now being automatically redirected to their upgraded versions. See our [Model Lifecycle Policy](/docs/deprecations#model-lifecycle-policy) for details.

  | Original model | Redirects to       |
  | :------------- | :----------------- |
  | `Kimi-K2`      | `Kimi-K2-0905`     |
  | `DeepSeek-V3`  | `DeepSeek-V3-0324` |
  | `DeepSeek-R1`  | `DeepSeek-R1-0528` |

  These are same-lineage upgrades with compatible behavior. If you need the original version, deploy it as a [dedicated endpoint](/docs/dedicated-endpoints).
</Update>

<Update label="December 12, 2025">
  ## Python SDK v2.0 release candidate

  Together AI is releasing the **Python SDK v2.0 Release Candidate**, a new, OpenAPI-generated, strongly-typed client that replaces the legacy v1.0 package and brings the SDK into lock-step with the latest platform features.

  * **Install:** `pip install together==2.0.0a9`.
  * **RC period:** The v2.0 RC window starts today and will run for approximately one month. During this time we'll iterate quickly based on developer feedback and may make a few small, well-documented breaking changes before GA.
  * **Type-safe, modern client:** Stronger typing across parameters and responses, keyword-only arguments, explicit `NOT_GIVEN` handling for optional fields, and rich `together.types.*` definitions for chat messages, eval parameters, and more.
  * **Redesigned error model:** Replaces `TogetherException` with a new `TogetherError` hierarchy, including `APIStatusError` and specific HTTP status code errors such as `BadRequestError (400)`, `AuthenticationError (401)`, `RateLimitError (429)`, and `InternalServerError (5xx)`, plus transport (`APIConnectionError`, `APITimeoutError`) and validation (`APIResponseValidationError`) errors.
  * **New Jobs API:** Adds first-class support for the Jobs API (`client.jobs.*`) so you can create, list, and inspect asynchronous jobs directly from the SDK without custom HTTP wrappers.
  * **New Hardware API:** Adds the Hardware API (`client.hardware.*`) to discover available hardware, filter by model compatibility, and compute effective hourly pricing from `cents_per_minute`.
  * **Raw response and streaming helpers:** New `.with_raw_response` and `.with_streaming_response` helpers make it easier to debug, inspect headers and status codes, and stream completions via context managers with automatic cleanup.
  * **Code Interpreter sessions:** Adds session management for the Code Interpreter (`client.code_interpreter.sessions.*`), enabling multi-step, stateful code-execution workflows that were not possible in the legacy SDK.
  * **High compatibility for core APIs:** Most core usage patterns, including `chat.completions`, `completions`, `embeddings`, `images.generate`, audio transcription/translation/speech, `rerank`, `fine_tuning.create/list/retrieve/cancel`, and `models.list`, are designed to be drop-in compatible between v1 and v2.
  * **Targeted breaking changes:** Some APIs (Files, Batches, Endpoints, Evals, Code Interpreter, select fine-tuning helpers) have updated method names, parameters, or response shapes; these are fully documented in the Python SDK Migration Guide and Breaking Changes notes.
  * **Migration resources:** A dedicated Python SDK Migration Guide is available with API-by-API before/after examples, a feature parity matrix, and troubleshooting tips to help teams smoothly transition from v1 to v2 during the RC period.
</Update>

<Update label="December 8, 2025">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `mistralai/Ministral-3-14B-Instruct-2512`.
</Update>

<Update label="November 10, 2025">
  ## New serverless models

  The following models are now available on [serverless](/docs/serverless/models):

  * `zai-org/GLM-4.6`.
  * `moonshotai/Kimi-K2-Thinking`.
</Update>

<Update label="November 3, 2025">
  ## Real-time text-to-speech and speech-to-text

  Together AI expands audio capabilities with real-time streaming for both TTS and STT, new models, and speaker diarization.

  * **Real-time text-to-speech:** WebSocket API for lowest-latency interactive applications.
  * **New TTS models:** Orpheus 3B (`canopylabs/orpheus-3b-0.1-ft`) and Kokoro 82M (`hexgrad/Kokoro-82M`), supporting REST, streaming, and WebSocket endpoints.
  * **Real-time speech-to-text:** WebSocket streaming transcription with Whisper for live audio applications.
  * **Voxtral model:** New Mistral AI speech recognition model (`mistralai/Voxtral-Mini-3B-2507`) for audio transcriptions.
  * **Speaker diarization:** Identify and label different speakers in audio transcriptions with a free `diarize` flag.
  * **TTS WebSocket endpoint:** `/v1/audio/speech/websocket`.
  * **STT WebSocket endpoint:** `/v1/realtime`.

  See the [Text-to-speech guide](/docs/inference/text-to-speech/overview) and [Speech-to-text guide](/docs/inference/transcription/overview).
</Update>

<Update label="October 31, 2025">
  ## Image model deprecations

  The following image models have been deprecated and are no longer available:

  * `black-forest-labs/FLUX.1-pro` (calls to FLUX.1-pro will now redirect to FLUX.1.1-pro).
  * `black-forest-labs/FLUX.1-Canny-pro`.
</Update>

<Update label="October 21, 2025">
  ## Video generation API and 40+ new image and video models

  Together AI expands into multimedia generation with comprehensive video and image capabilities. [Read more](https://www.together.ai/blog/40-new-image-and-video-models).

  * **New video generation API:** Create high-quality videos with models like OpenAI Sora 2, Google Veo 3.0, and Minimax Hailuo.
  * **40+ image and video models:** Including Google Imagen 4.0 Ultra, Gemini Flash Image 2.5 (Nano Banana), ByteDance SeeDream, and specialized editing tools.
  * **Unified platform:** Combine text, image, and video generation through the same APIs, authentication, and billing.
  * **Production-ready:** Serverless endpoints with transparent per-model pricing and enterprise-grade infrastructure.
  * **Video endpoints:** `/videos/create` and `/videos/retrieve`.
  * **Image endpoint:** `/images/generations`.
</Update>

<Update label="September 15, 2025">
  ## Improved Batch Inference API

  * **Streamlined UI:** Create and track batch jobs in an intuitive interface. No complex API calls required.
  * **Universal model access:** The Batch Inference API now supports all serverless models and private deployments, so you can run batch workloads on exactly the models you need.
  * **Massive scale jump:** Rate limits are up from 10M to 30B enqueued tokens per model per user, a 3,000x increase. Need more? We'll work with you to customize.
  * **Lower cost:** For most serverless models, the Batch Inference API runs at 50% the cost of our real-time API, making it the most economical way to process high-throughput workloads.
</Update>

<Update label="September 13, 2025">
  ## Qwen3-Next-80B models

  New Qwen3-Next-80B models are now available for both thinking and instruction tasks.

  * Model ID: `Qwen/Qwen3-Next-80B-A3B-Thinking`.
  * Model ID: `Qwen/Qwen3-Next-80B-A3B-Instruct`.
</Update>

<Update label="September 10, 2025">
  ## Fine-tuning: new large models supported

  Enhanced fine-tuning capabilities with expanded model support. [Read more](https://www.together.ai/blog/fine-tuning-updates-sept-2025).

  * `openai/gpt-oss-120b`.
  * `deepseek-ai/DeepSeek-V3.1`.
  * `deepseek-ai/DeepSeek-V3.1-Base`.
  * `deepseek-ai/DeepSeek-R1-0528`.
  * `deepseek-ai/DeepSeek-R1`.
  * `deepseek-ai/DeepSeek-V3-0324`.
  * `deepseek-ai/DeepSeek-V3`.
  * `deepseek-ai/DeepSeek-V3-Base`.
  * `Qwen/Qwen3-Coder-480B-A35B-Instruct`.
  * `Qwen/Qwen3-235B-A22B` (context length 32,768 for SFT and 16,384 for DPO).
  * `Qwen/Qwen3-235B-A22B-Instruct-2507` (context length 32,768 for SFT and 16,384 for DPO).
  * `meta-llama/Llama-4-Maverick-17B-128E`.
  * `meta-llama/Llama-4-Maverick-17B-128E-Instruct`.
  * `meta-llama/Llama-4-Scout-17B-16E`.
  * `meta-llama/Llama-4-Scout-17B-16E-Instruct`.

  ## Fine-tuning: increased maximum context lengths

  ### DeepSeek models

  * DeepSeek-R1-Distill-Llama-70B: SFT 8,192 → 24,576; DPO 8,192 → 8,192.
  * DeepSeek-R1-Distill-Qwen-14B: SFT 8,192 → 65,536; DPO 8,192 → 12,288.
  * DeepSeek-R1-Distill-Qwen-1.5B: SFT 8,192 → 131,072; DPO 8,192 → 16,384.

  ### Google Gemma models

  * gemma-3-1b-it: SFT 16,384 → 32,768; DPO 16,384 → 12,288.
  * gemma-3-1b-pt: SFT 16,384 → 32,768; DPO 16,384 → 12,288.
  * gemma-3-4b-it: SFT 16,384 → 131,072; DPO 16,384 → 12,288.
  * gemma-3-4b-pt: SFT 16,384 → 131,072; DPO 16,384 → 12,288.
  * gemma-3-12b-pt: SFT 16,384 → 65,536; DPO 16,384 → 8,192.
  * gemma-3-27b-it: SFT 12,288 → 49,152; DPO 12,288 → 8,192.
  * gemma-3-27b-pt: SFT 12,288 → 49,152; DPO 12,288 → 8,192.

  ### Qwen models

  * Qwen3-0.6B / Qwen3-0.6B-Base: SFT 8,192 → 32,768; DPO 8,192 → 24,576.
  * Qwen3-1.7B / Qwen3-1.7B-Base: SFT 8,192 → 32,768; DPO 8,192 → 16,384.
  * Qwen3-4B / Qwen3-4B-Base: SFT 8,192 → 32,768; DPO 8,192 → 16,384.
  * Qwen3-8B / Qwen3-8B-Base: SFT 8,192 → 32,768; DPO 8,192 → 16,384.
  * Qwen3-14B / Qwen3-14B-Base: SFT 8,192 → 32,768; DPO 8,192 → 16,384.
  * Qwen3-32B: SFT 8,192 → 24,576; DPO 8,192 → 4,096.
  * Qwen2.5-72B-Instruct: SFT 8,192 → 24,576; DPO 8,192 → 8,192.
  * Qwen2.5-32B-Instruct: SFT 8,192 → 32,768; DPO 8,192 → 12,288.
  * Qwen2.5-32B: SFT 8,192 → 49,152; DPO 8,192 → 12,288.
  * Qwen2.5-14B-Instruct: SFT 8,192 → 32,768; DPO 8,192 → 16,384.
  * Qwen2.5-14B: SFT 8,192 → 65,536; DPO 8,192 → 16,384.
  * Qwen2.5-7B-Instruct: SFT 8,192 → 32,768; DPO 8,192 → 16,384.
  * Qwen2.5-7B: SFT 8,192 → 131,072; DPO 8,192 → 16,384.
  * Qwen2.5-3B-Instruct: SFT 8,192 → 32,768; DPO 8,192 → 16,384.
  * Qwen2.5-3B: SFT 8,192 → 32,768; DPO 8,192 → 16,384.
  * Qwen2.5-1.5B-Instruct: SFT 8,192 → 32,768; DPO 8,192 → 16,384.
  * Qwen2.5-1.5B: SFT 8,192 → 32,768; DPO 8,192 → 16,384.
  * Qwen2-72B-Instruct / Qwen2-72B: SFT 8,192 → 32,768; DPO 8,192 → 8,192.
  * Qwen2-7B-Instruct: SFT 8,192 → 32,768; DPO 8,192 → 16,384.
  * Qwen2-7B: SFT 8,192 → 131,072; DPO 8,192 → 16,384.
  * Qwen2-1.5B-Instruct: SFT 8,192 → 32,768; DPO 8,192 → 16,384.
  * Qwen2-1.5B: SFT 8,192 → 131,072; DPO 8,192 → 16,384.

  ### Meta Llama models

  * Llama-3.3-70B-Instruct-Reference: SFT 8,192 → 24,576; DPO 8,192 → 8,192.
  * Llama-3.2-3B-Instruct: SFT 8,192 → 131,072; DPO 8,192 → 24,576.
  * Llama-3.2-1B-Instruct: SFT 8,192 → 131,072; DPO 8,192 → 24,576.
  * Meta-Llama-3.1-8B-Instruct-Reference: SFT 8,192 → 131,072; DPO 8,192 → 16,384.
  * Meta-Llama-3.1-8B-Reference: SFT 8,192 → 131,072; DPO 8,192 → 16,384.
  * Meta-Llama-3.1-70B-Instruct-Reference: SFT 8,192 → 24,576; DPO 8,192 → 8,192.
  * Meta-Llama-3.1-70B-Reference: SFT 8,192 → 24,576; DPO 8,192 → 8,192.

  ### Mistral models

  * mistralai/Mistral-7B-v0.1: SFT 8,192 → 32,768; DPO 8,192 → 32,768.
  * teknium/OpenHermes-2p5-Mistral-7B: SFT 8,192 → 32,768; DPO 8,192 → 32,768.

  ## Fine-tuning: Hugging Face integrations

  * Fine-tune any \< 100B parameter CausalLM from Hugging Face Hub.
  * Support for DPO variants such as LN-DPO, DPO+NLL, and SimPO.
  * Support fine-tuning with maximum batch size.
  * Public `fine-tunes/models/limits` and `fine-tunes/models/supported` endpoints.
  * Automatic filtering of sequences with no trainable tokens (e.g., if a sequence prompt is longer than the model's context length, the completion is pushed outside the window).
</Update>

<Update label="September 9, 2025">
  ## Together Instant Clusters general availability

  Self-service NVIDIA GPU clusters with API-first provisioning. [Read more](https://www.together.ai/blog/together-instant-clusters-ga).

  * New API endpoints for cluster management:
    * `/v1/gpu_cluster`: Create and manage GPU clusters.
    * `/v1/shared_volume`: High-performance shared storage.
    * `/v1/regions`: Available data center locations.
  * Support for NVIDIA Blackwell (HGX B200) and Hopper (H100, H200) GPUs.
  * Scale from single-node (8 GPUs) to hundreds of interconnected GPUs.
  * Pre-configured with Kubernetes, Slurm, and networking components.
</Update>

<Update label="September 8, 2025">
  ## Serverless LoRA and dedicated model inference support for evaluations

  You can now run evaluations:

  * Using [Serverless LoRA](/docs/lora-inference#serverless-lora-inference) models, including supported LoRA fine-tuned models.
  * Using [dedicated model inference](/docs/dedicated-endpoints), including fine-tuned models deployed via dedicated endpoints.
</Update>

<Update label="September 5, 2025">
  ## Kimi-K2-Instruct-0905

  Upgraded version of Moonshot's 1 trillion parameter MoE model with enhanced performance. [Read more](https://www.together.ai/models/kimi-k2-0905).

  * Model ID: `moonshot-ai/Kimi-K2-Instruct-0905`.
</Update>

<Update label="August 27, 2025">
  ## DeepSeek-V3.1

  Upgraded version of DeepSeek-R1-0528 and DeepSeek-V3-0324. [Read more](https://www.together.ai/blog/deepseek-v3-1-hybrid-thinking-model-now-available-on-together-ai).

  * **Dual modes:** Fast mode for quick responses; thinking mode for complex reasoning.
  * **671B total parameters**, with 37B active parameters.
  * Model ID: `deepseek-ai/DeepSeek-V3.1`.

  ## Model deprecations

  The following models have been deprecated and are no longer available:

  * `meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo`.
  * `black-forest-labs/FLUX.1-canny`.
  * `meta-llama/Llama-3-8b-chat-hf`.
  * `black-forest-labs/FLUX.1-redux`.
  * `black-forest-labs/FLUX.1-depth`.
  * `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B`.
  * `NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO`.
  * `meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo`.
  * `meta-llama-llama-3-3-70b-instruct-lora`.
  * `Qwen/Qwen2.5-14B`.
  * `meta-llama/Llama-Vision-Free`.
  * `Qwen/Qwen2-72B-Instruct`.
  * `google/gemma-2-27b-it`.
  * `meta-llama/Meta-Llama-3-8B-Instruct`.
  * `perplexity-ai/r1-1776`.
  * `nvidia/Llama-3.1-Nemotron-70B-Instruct-HF`.
  * `Qwen/Qwen2-VL-72B-Instruct`.
</Update>

<Update label="August 19, 2025">
  ## GPT-OSS fine-tuning support

  Fine-tune OpenAI's open-source models to create domain-specific variants. [Read more](https://www.together.ai/blog/fine-tune-gpt-oss-models-into-domain-experts-together-ai).

  * Supported models: `gpt-oss-20B` and `gpt-oss-120B`.
  * Supports 16K context SFT and 8K context DPO.
</Update>

<Update label="August 5, 2025">
  ## OpenAI GPT-OSS models

  OpenAI's first open-weight models are now accessible through Together AI. [Read more](https://www.together.ai/blog/announcing-the-availability-of-openais-open-models-on-together-ai).

  * Model IDs: `openai/gpt-oss-20b`, `openai/gpt-oss-120b`.
</Update>

<Update label="July 29, 2025">
  ## VirtueGuard

  Enterprise-grade guard model for safety monitoring with **8ms response time**. [Read more](https://www.together.ai/blog/virtueguard).

  * Real-time content filtering and bias detection.
  * Prompt injection protection.
  * Model ID: `VirtueAI/VirtueGuard-Text-Lite`.
</Update>

<Update label="July 28, 2025">
  ## Together Evaluations framework

  Benchmarking platform using LLM-as-a-judge methodology for model performance assessment. [Read more](https://www.together.ai/blog/introducing-together-evaluations).

  * Create custom LLM-as-a-judge evaluation suites for your domain.
  * Supports `compare`, `classify`, and `score` functionality.
  * Compare models, prompts, and LLM configs; score and classify LLM outputs.
</Update>

<Update label="July 25, 2025">
  ## Qwen3-Coder-480B

  Agentic coding model with top SWE-Bench Verified performance. [Read more](https://www.together.ai/blog/qwen-3-coder).

  * **480B total parameters**, with 35B active (MoE architecture).
  * **256K context length** for entire codebase handling.
  * **Leading SWE-Bench scores** on software engineering benchmarks.
  * Model ID: `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`.
</Update>

<Update label="July 17, 2025">
  ## NVIDIA HGX B200 hardware support

  Record-breaking serverless inference speed for DeepSeek-R1-0528 using NVIDIA's Blackwell architecture. [Read more](https://www.together.ai/blog/fastest-inference-for-deepseek-r1-0528-with-nvidia-hgx-b200).

  * Dramatically improved throughput and lower latency.
  * Same API endpoints and pricing.
  * Model ID: `deepseek-ai/DeepSeek-R1`.
</Update>

<Update label="July 14, 2025">
  ## Kimi-K2-Instruct

  Moonshot AI's 1 trillion parameter MoE model with frontier-level performance. [Read more](https://www.together.ai/blog/kimi-k2-leading-open-source-model-now-available-on-together-ai).

  * Excels at tool use and multi-step tasks, with strong multilingual support.
  * Strong agentic and function calling capabilities.
  * Model ID: `moonshotai/Kimi-K2-Instruct`.
</Update>

<Update label="July 10, 2025">
  ## Whisper speech-to-text APIs

  High-performance audio transcription that's 15x faster than OpenAI, with support for files over 1 GB. [Read more](https://www.together.ai/blog/speech-to-text-whisper-apis).

  * Multiple audio formats with timestamp generation.
  * Speaker diarization and language detection.
  * Use the `/audio/transcriptions` and `/audio/translations` endpoints.
  * Model ID: `openai/whisper-large-v3`.
</Update>

<Update label="July 8, 2025">
  ## SOC 2 Type II compliance certification

  Achieved enterprise-grade security compliance through an independent audit of security controls. [Read more](https://www.together.ai/blog/soc-2-compliance).

  * Simplified vendor approval and procurement.
  * Reduced due diligence requirements.
  * Support for regulated industries.
</Update>
