---
title: "Parameter Tuning"
source: https://docs.fireworks.ai/fine-tuning/parameter-tuning
path: fine-tuning/parameter-tuning
---

Learn how training parameters affect model behavior and outcomes

## Overview

Reinforcement fine-tuning uses two categories of parameters to control model training: **training parameters** that govern how the model learns, and **rollout (sampling) parameters** that control how the model generates responses during training.

Most experiments converge well with the default values. Adjust parameters only when you have a clear hypothesis based on your training metrics and reward curves.

## Training Parameters

Core parameters that control how your model learns during the training process.

<Warning>
  RFT V1 still uses `batch_size` as its packed-token budget. Do not send a nonzero `batch_size` in new SFT or DPO/ORPO Training V2 requests; use `batch_size_samples` for those job types instead. See [Deprecated parameters](/fine-tuning/fine-tuning-models#deprecated-parameters) for the path-specific migration list.
</Warning>

<AccordionGroup>
  <Accordion title="Learning Rate">
    **What it does**: Controls how aggressively the model updates its weights during each training step. Think of it as the "step size" when descending the loss landscape.

    **Default**: `1e-4` (0.0001)\
    **Valid range**: `1e-5` to `5e-4`

    **How it affects outcome**:

    * **Too high** → Unstable training where reward spikes briefly then collapses as the model overshoots optimal weights.
    * **Too low** → Painfully slow convergence. The reward curve plateaus too early before reaching optimal performance.
    * **Just right** → Steady, consistent reward improvement throughout training.

    **When to adjust**:

    * **Decrease** when you see reward spikes followed by crashes in your training metrics
    * **Increase** when the reward curve plateaus too early and stops improving
    * Keep changes within 2× of the default value
  </Accordion>

  <Accordion title="Epochs">
    **What it does**: The number of complete passes through your training dataset. Each epoch processes every example once.

    **Default**: `1`\
    **Valid range**: `1` to `10` (whole numbers only)

    **How it affects outcome**:

    * **Too few** → The model hasn't had enough exposure to learn patterns from your data
    * **Too many** → Overfitting risk where the model memorizes the training set instead of generalizing
    * **Just right** → Reward curve shows steady improvement and plateaus near the end of training

    **When to adjust**:

    * **Add 1-2 more epochs** if the reward is still climbing steadily at the end of training
    * **Keep at 1** for most tasks—the default works well
    * Watch your reward curves to detect when adding more epochs stops helping
  </Accordion>

  <Accordion title="LoRA Rank">
    **What it does**: Controls the number of trainable parameters in your LoRA adapter. LoRA (Low-Rank Adaptation) adds small adapter layers to the base model rather than training all weights. Higher rank means more capacity to learn new behaviors.

    **Default**: `8`\
    **Valid range**: `4` to `32` (must be powers of 2: 4, 8, 16, 32)

    **How it affects outcome**:

    * **Lower rank (4-8)** → Faster training, but may lack capacity for complex tasks
    * **Just right (8-16)** → Balances capacity and efficiency for most tasks
    * **Higher rank (32)** → More learning capacity, but requires significantly more GPUs and risks overfitting

    **When to adjust**:

    * **Increase** for complex reasoning tasks or when the model struggles to learn desired behaviors
    * Consider task complexity: simple style changes need lower rank, complex reasoning needs higher
  </Accordion>

  <Accordion title="Legacy Token Batch Size (RFT)">
    **What it does**: `batch_size` sets the maximum number of packed tokens in each RFT V1 microbatch.

    <Note>
      This field is active for managed RFT V1 and is not replaced by `batch_size_samples`. The two controls work together: `batch_size` limits packed tokens per microbatch, while `batch_size_samples` optionally limits rollout samples per gradient batch. For example, an 8k max sequence length and a 64k token budget allow up to 8 full-length sequences in a packed microbatch.
    </Note>

    **Default**: `32k tokens`

    **How it affects outcome**:

    * **Smaller batches** → Noisier gradient updates that may help exploration, but slower training throughput
    * **Larger batches** → Smoother, more stable updates and faster training throughput

    **When to adjust**:

    * Most users should stick with the default. Modify if you want a smaller/larger amount of tokens per train step
  </Accordion>

  <Accordion title="Chunk Size">
    **What it does**: Sets the minimum number of prompts rolled out before each GRPO training step. Controls how on-policy the training is by determining how often the model is updated relative to rollout generation — a chunk is a slice of the dataset that the trainer fully rolls out *before* taking a training step, after which the next chunk's rollouts are generated from the updated policy.

    **Default**: `200` (auto-applied only when the dataset has at least `2 × chunk_size` examples; datasets with fewer examples run without chunking)
    **Valid values**: `-1` to disable chunking, any positive integer to set an explicit size. Setting `0` (or leaving unset) uses the default behavior above.

    **On-policy spectrum**:

    * **Small chunk size** → more frequent training steps, rollouts stay close to the policy being trained (more on-policy), but more forward/backward passes per epoch and slower wall-clock time.
    * **Large chunk size** (or `chunk_size = dataset_size`) → fewer training steps, rollouts become stale relative to the updated policy (more off-policy), faster wall-clock but potentially lower sample efficiency.
    * **Fully online RL**: `chunk_size=1` (generate one prompt's rollouts → train → repeat). Not typically recommended in practice.
    * **Fully offline RL**: `chunk_size = dataset_size` (generate all rollouts first, then train — equivalent to 1 epoch with no mid-epoch updates).

    **Epoch/chunk interaction**

    An epoch is still a full pass through the entire dataset. `chunk_size` controls how frequently the model gets a GRPO training step *within* each epoch. For example, with `chunk_size=200`, `dataset_size=1000`, `epochs=2`, and `response_candidates_count=8`:

    ```
    epoch 0 chunk 0 (prompts 1-200)    × 8 rollouts → train
    epoch 0 chunk 1 (prompts 201-400)  × 8 rollouts → train
    epoch 0 chunk 2 (prompts 401-600)  × 8 rollouts → train
    epoch 0 chunk 3 (prompts 601-800)  × 8 rollouts → train
    epoch 0 chunk 4 (prompts 801-1000) × 8 rollouts → train
    epoch 1 chunk 0 (prompts 1-200)    × 8 rollouts → train
    ...
    ```

    That is, 5 chunks × 2 epochs = 10 GRPO training steps total, each preceded by 200 × 8 = 1600 rollouts.

    **Relationship with legacy `gradient_accumulation_steps`**

    These two are orthogonal:

    * `chunk_size` controls how many prompts are rolled out **before each GRPO training step** — i.e., how on-policy the training is.
    * `gradient_accumulation_steps` controls how many forward/backward passes accumulate **within a single chunk's training step** before each optimizer update. This field is also deprecated; use `batch_size_samples` in new integrations.

    <Note>
      `--chunk-size` is only exposed via the `firectl` / `eval-protocol` CLI. It is not configurable from the Web UI.
    </Note>
  </Accordion>
</AccordionGroup>

## Loss Method

Parameters that control the policy optimization algorithm used during training.

<AccordionGroup>
  <Accordion title="RL Loss Method">
    **What it does**: Controls the policy optimization algorithm used during training. Different methods trade off exploration aggressiveness, stability, and KL regularization.

    **Default**: `grpo`
    **Valid values**: `grpo`, `dapo`, `gspo-token`

    **GRPO** (default) — Group Relative Policy Optimization ([arXiv:2402.03300](https://arxiv.org/abs/2402.03300)). The conservative baseline used by most RFT jobs.

    * **Symmetric clipping:** Clips the policy ratio to `[0.8, 1.2]`, limiting how much the policy can change in a single step in either direction.
    * **KL penalty:** Includes a small KL divergence penalty (`kl_loss_coef=0.001`) that keeps the trained policy close to the reference model. This prevents mode collapse but limits how far the model can deviate from its starting behavior.
    * **Token-level loss aggregation:** Loss is summed over valid tokens and divided by total valid token count (`token-mean`).

    Best for: Most tasks. Start here unless you have a specific reason to use another method.

    **DAPO** — Decoupled Alignment Preference Optimization ([arXiv:2503.14476](https://arxiv.org/abs/2503.14476)). A more aggressive variant that removes KL regularization and uses asymmetric clipping.

    * **Asymmetric clipping:** Clips the policy ratio to `[0.8, 1.28]` — the upper bound is higher than the lower bound, allowing the policy to take larger steps in the "improve" direction while being more conservative about degradation.
    * **No KL penalty:** `kl_loss_coef` is set to 0. The trained policy is not penalized for diverging from the reference model.
    * **Token-level loss aggregation:** Same `token-mean` mode as GRPO.

    Best for: Tasks where the base model is far from optimal and you want to allow larger policy updates. Useful when GRPO converges too slowly or plateaus early.

    <Warning>
      `--rl-kl-beta` is incompatible with DAPO. Setting a non-zero `--rl-kl-beta` when `--rl-loss-method dapo` is specified will cause job creation to fail with: `loss_config.kl_beta must be 0/unset when method is DAPO`.
    </Warning>

    **What DAPO does NOT include from the original paper:**

    * **Overlong reward shaping** is not implemented. The separate `--length-norm` flag exists but is not DAPO-specific.
    * **Dynamic sampling (overgeneration)** is not implemented. Zero-variance groups are filtered out (see [Zero-Variance Group Filtering](#zero-variance-group-filtering) below), but filtered prompts are dropped from the batch, not replaced with new prompts.

    **GSPO-token** — Group Sequence Policy Optimization, token-level variant ([arXiv:2507.18071](https://arxiv.org/abs/2507.18071)). Uses sequence-level importance sampling with very tight clipping for conservative, stable updates.

    * **Sequence-level importance sampling:** Computes a sequence-level KL proxy and broadcasts it to token-level ratios, rather than computing ratios independently per token. This better captures how entire responses differ from the reference policy.
    * **Very tight clipping:** Clips the policy ratio to `[1 - 0.0003, 1 + 0.0004]` — much tighter than GRPO or DAPO, making each training step very conservative.
    * **No KL penalty:** `kl_loss_coef` is set to 0.
    * **Sequence-mean-token-mean aggregation:** Loss is first averaged per-sequence, then averaged across sequences. This prevents longer responses from dominating the loss.

    Best for: Stability-sensitive training or when working with long-form outputs where per-sequence normalization matters. The very small clip range means you may need more training steps to converge.

    <Warning>
      `--rl-kl-beta` is incompatible with GSPO-token. Setting a non-zero `--rl-kl-beta` when `--rl-loss-method gspo-token` is specified will cause job creation to fail with: `loss_config.kl_beta must be 0/unset when method is GSPO_TOKEN`.
    </Warning>

    **When to use each method:**

    | Goal                                            | Recommended method             |
    | ----------------------------------------------- | ------------------------------ |
    | Safe default for most tasks                     | `grpo`                         |
    | Faster convergence, more aggressive exploration | `dapo`                         |
    | Maximum stability, long-form outputs            | `gspo-token`                   |
    | Keep policy close to reference model            | `grpo` with `--rl-kl-beta > 0` |
  </Accordion>

  <Accordion title="KL Beta">
    **What it does**: Overrides the KL divergence penalty coefficient for GRPO. Higher values keep the policy closer to the reference model; lower values allow more divergence.

    **Default**: `0` (uses the loss method's built-in default: `0.001` for GRPO)
    **Valid range**: `>= 0`

    <Note>
      `--rl-kl-beta` only applies to `--rl-loss-method grpo`. It is rejected for `dapo` and `gspo-token`, which are designed to operate without KL penalties.
    </Note>

    **When to adjust**:

    * **Increase** if the model diverges too far from the base model's capabilities (catastrophic forgetting)
    * **Decrease or set to 0** if you want the model to explore more freely
    * Leave at default for most tasks
  </Accordion>
</AccordionGroup>

## Rollout (Sampling) Parameters

Parameters that control how the model generates responses during training rollouts.

<AccordionGroup>
  <Accordion title="Temperature">
    **What it does**: Controls the randomness of the model's token selection during generation. Higher temperature = more random/creative, lower = more deterministic/focused.

    **Default**: `0.7`\
    **Valid range**: `0.1` to `2.0` (must be >0)

    **How it affects outcome**:

    * **0.0-0.1 (near-greedy)** → Deterministic outputs with no exploration. Leads to mode collapse and repetitive text. **Avoid in RFT.**
    * **0.5-1.0 (sweet spot)** → Good balance of exploration and coherence. Ideal for most RLHF applications.
    * **>1.2 (high randomness)** → Very creative but potentially incoherent outputs

    **When to adjust**:

    * **Lower (0.3-0.5)** for tasks requiring precision, factual accuracy, or safety (less toxic outputs)
    * **Raise (1.0-1.2)** for creative tasks like story generation or when you need more diverse rollout exploration
    * **Never use 0.0**—greedy sampling breaks RFT by eliminating exploration
  </Accordion>

  <Accordion title="Top-p (Nucleus Sampling)">
    **What it does**: Dynamically limits token sampling to the smallest set of tokens whose cumulative probability exceeds threshold p. Only considers the most probable tokens that together make up the top p% of probability mass.

    **Default**: `1.0` (considers all tokens)\
    **Valid range**: `0` to `1`

    `top_p` and `top_k` are both optional and not mutually exclusive. If both are set, `top_k` filters first, then `top_p` narrows by cumulative probability.

    **How it affects outcome**:

    * Lower values (0.2-0.5) filter out long-tail, low-probability tokens that often cause hallucinations
    * Higher values (0.9-1.0) allow more diversity in outputs
    * Prevents the model from selecting very unlikely tokens that may be nonsensical

    **When to adjust**:

    * **Lower to 0.2-0.5** when your reward function penalizes hallucinations or factual errors
    * **Keep at 0.9-1.0** for creative tasks that benefit from diverse vocabulary
    * Works well in combination with temperature for fine-grained control
  </Accordion>

  <Accordion title="Top-k">
    **What it does**: Limits sampling to only the K most probable tokens at each step. A fixed-size cutoff (unlike top-p which is dynamic).

    **Default**: `40`\
    **Valid range**: `0` to `100` (0 = disabled)

    `top_p` and `top_k` are both optional and not mutually exclusive. If both are set, `top_k` filters first, then `top_p` narrows by cumulative probability.

    **How it affects outcome**:

    * Similar to top-p but uses a fixed number of candidates instead of a probability threshold
    * Lower k = more focused, less diverse outputs
    * Higher k = more exploration and creativity

    **When to adjust**:

    * **Combine with temperature** (e.g., temp 0.8 + top-k 40) for balanced creative exploration
    * **Keep ≤50** to maintain reasonable inference latency
    * Consider using top-p instead for most use cases—it adapts better to varying probability distributions
  </Accordion>

  <Accordion title="Number of Rollouts (Response Candidates Count)">
    **What it does**: How many different responses the model generates for each prompt during training. In GRPO terminology, this is the **group size** — the set of completions per prompt used to compute group-relative advantages. The policy optimization algorithm compares these candidates to compute advantages and learn which responses are better. Exposed as `--response-candidates-count` in both `firectl` and the `eval-protocol` CLI.

    **Default**: `8` (server-side default applied when the field is unset by any client)
    **Valid range**: Minimum `2`, no hard upper bound

    **How it affects outcome**:

    * **n=1** → **Not allowed.** Policy optimization requires multiple candidates to learn from comparisons
    * **n=2-4** → Minimal viable exploration. Faster and cheaper but less signal for learning
    * **n=8** → Recommended default. Good balance of learning signal and cost for most tasks
    * **n=16** → Higher quality signal at higher cost. Consider for complex tasks with nuanced evaluators
    * **n>16** → Diminishing returns in most cases. Linearly increases cost and rollout time

    **When to adjust**:

    * **Increase to 8-16** when you need higher quality learning signal and cost is acceptable
    * **Keep at 8** for most experiments—it's the recommended starting point
    * **Never set to 1**—this will cause job creation to fail
    * Consider the cost tradeoff: each chunk produces `chunk_size × response_candidates_count` rollouts before a training step (e.g., `chunk_size=200` with `n=8` → 1600 rollouts), so higher values linearly increase wall-clock time. See [Chunk Size](#chunk-size) for how chunks and epochs interact.

    <Note>
      Higher values of n increase per-prompt memory usage in both the rollout phase and the training step. While there is no enforced maximum, very high values (e.g., >32) may encounter memory pressure depending on model size and sequence length. Values of 8 and 16 are well-tested.
    </Note>
  </Accordion>

  <Accordion title="Max Tokens">
    **What it does**: The maximum number of tokens the model can generate in a single response during rollouts.

    **Default**: `2048`\
    **Valid range**: `16` to `16384`

    **How it affects outcome**:

    * Directly affects task completion: too short and the model can't finish complex tasks
    * Longer responses improve reward on summarization, story generation, and reasoning tasks
    * Linearly increases training cost—every token generated costs compute

    **When to adjust**:

    * **Increase** when your tasks require longer reasoning chains, detailed summaries, or complex multi-step solutions
    * **Decrease** to reduce costs for tasks with naturally short outputs (classification, short-form Q\&A)
    * Monitor your reward curves: if the model is cutting off mid-response, increase max tokens
  </Accordion>

  <Accordion title="Max Concurrent Rollouts">
    **What it does**: Controls how many rollout completions run in parallel during the rollout phase of training. This is a **throughput parameter only** — it does not affect training dynamics, gradient computation, or model quality.

    **Default**: Inherited from the evaluator's `@evaluation_test` decorator if not set on the CLI. If the decorator also doesn't set it, the SDK default of `96` applies.

    **How it affects outcome**:

    * **Higher values** → Faster rollout phase (more completions generated simultaneously)
    * **Lower values** → Slower rollout phase but less API load on the inference endpoint
    * **No effect** on training loss, advantages, or gradient updates

    **When to adjust**:

    * **Increase** to speed up the rollout phase if your inference endpoint can handle higher concurrency
    * **Decrease** if you're hitting rate limits or timeouts on the inference endpoint
    * **Leave unset** to use the evaluator's default, which is tuned for typical workloads

    <Note>
      This parameter only controls parallelism during the rollout (sampling) phase. It has no effect on training dynamics — batch composition, advantage normalization, loss computation, and gradient updates are all unaffected.
    </Note>
  </Accordion>
</AccordionGroup>

## Zero-Variance Group Filtering

During each training iteration, the model generates K response candidates per prompt (controlled by `--response-candidates-count` or `--n`). Your evaluator scores each candidate. If **all K candidates for a prompt receive the same score**, that group provides no learning signal — the model cannot distinguish better from worse responses.

**Managed RFT automatically filters out these zero-variance groups.** This applies to all loss methods (GRPO, DAPO, and GSPO-token), not just DAPO.

Important behaviors:

* Filtered prompts are **dropped from the batch**, not replaced with new prompts. This means your effective batch size may be smaller than expected when many groups are homogeneous.
* Filtering happens at both the full-group level (all K candidates same score) and at the chunk level within groups.
* If your evaluator returns the same score for all rollouts across most prompts, training will make limited progress and may trigger early stopping.

**To reduce zero-variance groups:**

* Increase `--temperature` (e.g., 0.8–1.0) to produce more diverse responses
* Increase `--response-candidates-count` to generate more candidates
* Ensure your evaluator returns a range of scores, not just 0 and 1

## Parameter Interactions

Parameters don't work in isolation—they interact in important ways.

<AccordionGroup>
  <Accordion title="Temperature + Top-p/Top-k">
    These three work together to control sampling behavior. Using all three gives you fine-grained control:

    * **Temperature** sets the overall randomness
    * **Top-p** dynamically filters by probability mass
    * **Top-k** sets a hard limit on candidate tokens

    Example: `temperature=0.8, top_p=0.9, top_k=40` gives creative but controlled outputs.
  </Accordion>

  <Accordion title="Learning Rate + Batch Size">
    Larger batch sizes provide more stable gradients, which may allow for slightly higher learning rates. However, the default learning rate is tuned for the default batch size—only adjust if you have evidence from your training curves.
  </Accordion>

  <Accordion title="LoRA Rank + Model Size">
    Larger base models (70B+) may need higher LoRA ranks to capture complex behaviors, but they also require more resources. For smaller models (\<13B), rank 8-16 is usually sufficient.
  </Accordion>
</AccordionGroup>

## Tuning Strategies

Best practices for adjusting parameters to achieve your training goals.

<AccordionGroup>
  <Accordion title="Start with Defaults">
    The default parameters are carefully tuned to work well for most RFT tasks. Don't change them unless you have a clear hypothesis based on your training metrics.

    Run at least one baseline experiment with defaults before making any adjustments. This gives you:

    * A performance benchmark to compare against
    * Understanding of whether parameter tuning is actually needed
    * Evidence about which metrics need improvement

    Many successful RFT jobs use all default parameters.
  </Accordion>

  <Accordion title="One Change at a Time">
    When you do adjust parameters, change only one at a time and measure the impact on your reward curves and evaluation metrics.

    **Good workflow:**

    1. Run baseline with defaults
    2. Identify specific issue (e.g., reward crashes, slow convergence)
    3. Change ONE parameter that should address that issue
    4. Compare results
    5. Repeat

    **Avoid:** Changing multiple parameters simultaneously—you won't know which change caused the improvement or regression.
  </Accordion>

  <Accordion title="Track Everything">
    Use Weights & Biases integration to:

    * Compare training curves across experiments
    * Track reward progression over time
    * Log all hyperparameters automatically

    This makes it easy to identify which parameter changes actually helped and which hurt performance.
  </Accordion>

  <Accordion title="Common Patterns">
    Quick reference for goal-directed parameter tuning:

    * **Faster convergence** → ↑ epochs (add 1-2), tune learning rate (stay \<2× default)
    * **Better quality** → ↑ temperature (1.0-1.2), ↑ rollouts (6-8), ↑ max tokens
    * **Safer/less toxic** → ↓ temperature (0.3-0.5), ↓ top-p (0.5), ↓ top-k
    * **More creative** → ↑ temperature (1.0-1.2), top-p = 0.9
    * **Lower cost** → ↓ rollouts, ↓ max tokens, ↓ batch size
    * **Higher capacity** → ↑ LoRA rank (16-32), but monitor memory usage
    * **Prevent overfitting** → Keep epochs = 1, consider lower LoRA rank
  </Accordion>
</AccordionGroup>

## Next Steps

<CardGroup>
  <Card title="CLI Reference" icon="terminal" href="/tools-sdks/firectl/commands/reinforcement-fine-tuning-job-create">
    Complete guide to CLI parameters and options
  </Card>

  <Card title="Launch Training" icon="rocket" href="/fine-tuning/cli-reference">
    Launch your RFT job
  </Card>

  <Card title="GSM8K Quickstart" icon="graduation-cap" href="/fine-tuning/quickstart-math">
    Hands-on tutorial showing parameter tuning in practice
  </Card>

  <Card title="RFT Overview" icon="book-open" href="/fine-tuning/reinforcement-fine-tuning-models">
    Learn about the RFT training process and workflow
  </Card>
</CardGroup>
