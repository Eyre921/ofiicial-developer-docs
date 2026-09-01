---
title: "Price comparison vs Tinker"
source: https://docs.fireworks.ai/fine-tuning/multi-turn-cost-comparison
path: fine-tuning/multi-turn-cost-comparison
---

Estimate the cost of multi-turn agentic RL rollouts on Fireworks compared to Tinker's per-token pricing

If you're running RL or agentic post-training on a long-context model and your
provider bills you per token with **no cross-turn prefix cache**, the prefill
cost grows quadratically with the number of turns — every turn re-prefills the
full conversation history. On Fireworks Dedicated, session-affinity routing
keeps an episode pinned to one replica so the KV cache is reused across turns,
and cached prompt tokens contribute essentially zero extra compute.

The calculator below makes that difference concrete. Set your episode shape
(turns, context growth, generation length) and compare:

* **Tinker** — flat per-token billing, no cross-turn cache (re-prefill every turn)
* **Fireworks Dedicated** — on-demand GPU-hour billing; the cache savings show up as more work per hour, not as a discounted token rate

<MultiTurnCostCalculator />

## Performance and benchmarking notes

### Dedicated trainer vs pooled/serverless resourcing

Tinker runs training jobs on a **pooled/serverless** GPU fleet, which lets a
single job burst onto many more GPUs than you would dedicate to a replica on
Fireworks. That burst is what makes individual Tinker steps feel fast — but it
also **caps the maximum training speed you can buy**: you cannot pay to scale
beyond the pool's per-job allocation, and you cannot reserve isolated capacity.

Fireworks dedicated trainers take the opposite trade-off: predictable,
isolated execution with no shared-pool queueing or noisy-neighbor variance,
and the ability to scale **wall-clock time and cost independently** by
adjusting replica count. If you want faster steps on dedicated, increase
replica count and parallelize work.

For **large model training or longer rollouts**, we have consistently found
the dedicated setup like ours is **cheaper overall and can also be faster**
depending on the customer's resourcing needs.

### Context-length benchmarking caveat

Benchmark comparisons are only apples-to-apples when truncation policy and
effective context length are matched. If one system truncates `>32k` samples
and another does not, the non-truncating run is doing more work and will
appear slower.

### Replica count is a speed/cost knob

Users can trade cost and wall-clock time by scaling replicas. A quick
back-of-envelope estimate:

$$
\text{\$ / 1M tokens} \approx \frac{\text{GPU count} \cdot \text{\$ / GPU-hour}}{\text{tokens/sec(cluster)} \cdot 3600} \cdot 10^6
$$

### Check utilization before scaling

Fireworks Dedicated is billed by GPU-hour, so low rollout traffic can make a
job look slow or expensive even when the deployment has spare capacity. Before
adding replicas, first confirm whether the inference deployment is saturated or
waiting for more work from your rollout client.

Useful signals:

* **Per-request performance metrics:** log Fireworks response metrics such as
  prompt tokens, cached prompt tokens, time to first token, and total server
  processing time from your rollout client. Non-streaming requests include
  these in response headers; for streaming requests, set
  [`perf_metrics_in_response`](/guides/querying-text-models#usage--performance-tracking)
  to include them in the final response chunk.
* **Deployment-level metrics:** export
  [Prometheus-style metrics](/deployments/exporting-metrics) for request rate,
  prompt and cached-token rates, queue latency, KV-cache usage, and concurrent
  request count. Low request/concurrency metrics with low queueing usually mean
  the deployment can accept more traffic.
* **Training API efficiency hints:** when available, monitor
  `trainer/training_efficiency/.../effective_batch_fill_ratio:last` and
  `trainer/training_efficiency/.../trainer_waiting_for_work:last`. These are
  returned in the `metrics` dict on your `forward` / `forward_backward`
  responses, not on the deployment dashboard. Low batch fill or a
  trainer-waiting-for-work signal usually points to the rollout side not
  feeding the trainer fast enough. See
  [Reading Training API efficiency metrics](#reading-training-api-efficiency-metrics)
  below for how to access and interpret them.

If the deployment is not saturated, increase rollout traffic first. For managed
RFT and Training API jobs, the main throughput knob is concurrent rollouts; see
[`max_concurrent_rollouts`](/fine-tuning/rft-parameters-reference)
and the Training API [deployment replica guidance](/fine-tuning/training-api/reference/deployment-manager#deployment-shape-and-training-shapes).

#### Reading Training API efficiency metrics

The two `trainer/training_efficiency/...` metrics are returned in the `metrics`
dict on your `forward` / `forward_backward` responses. They do **not** appear on
inference deployment dashboards, the per-request and deployment-level signals
above are separate.

```python theme={null}
# forward / forward_backward return a future, call .result()
result = training_client.forward_backward(datums, "cross_entropy").result()

# result.metrics is a dict; it includes:
#   trainer/training_efficiency/.../effective_batch_fill_ratio:last
#   trainer/training_efficiency/.../trainer_waiting_for_work:last
print(result.metrics)
```

* **`effective_batch_fill_ratio:last`**: the number of tokens in a batch
  divided by the maximum possible. **1.0 means fully saturated**; consistently
  low values across steps indicate under-filling.
* **`trainer_waiting_for_work:last`**: how much time the trainer (GPU) sat idle
  since the last op, i.e. the gap between `forward` calls. More waiting means the
  trainer is starved for work.

Low fill or significant waiting-for-work means the rollout side isn't feeding the
trainer fast enough: raise rollout concurrency
(`max_concurrent_rollouts`) before adding deployment replicas.

## How the numbers come together

### Tinker (the cost customers describe)

Each turn re-prefills the full accumulated context:

$$
\text{Prefill tokens (Tinker)} = \sum_{t=1}^{T} P_t = T \cdot P_1 + \Delta \cdot \frac{T(T-1)}{2}
$$

…where $P_1$ is the initial prompt (system + tools + task), $\Delta$ is the
context added per turn (model response + tool result), and $T$ is the turn
count. This is **quadratic in $T$**.

$$
\text{Cost (Tinker)} = \frac{\text{Prefill tokens}}{10^6} \cdot r_{\text{prefill}} + \frac{\text{Decode tokens}}{10^6} \cdot r_{\text{sample}}
$$

### Fireworks Dedicated — GPU-hour billing

Dedicated deployments are billed per GPU-second, so the prefix cache shows up
as **higher effective throughput** rather than a discount on per-token rates.
Across one episode, each unique token is prefilled at most once — the rest of
the prompt is served from the prefix cache and contributes essentially no GPU
work. The uncached portion that actually hits prefill is:

$$
\text{Uncached prompt} = P_T = P_1 + (T - 1) \Delta
$$

On a saturated cluster:

$$
\text{Cluster-hours} = \frac{\text{Uncached prompt} / \text{prefill TPS}}{3600}
$$

$$
\text{Cost} = \text{Cluster-hours} \cdot N_{\text{GPU}} \cdot r_{\text{GPU/hr}}
$$

Because cached tokens contribute essentially nothing to wall-clock work, the
cluster's effective \$/M token rate falls as utilization rises. For continuous
RL training, where rollouts run at sustained pace, dedicated is typically the
cheapest path at scale.

<Note>
  The calculator's dedicated path uses *saturated* throughput estimates as
  defaults. A small, lightly-loaded test deployment will look more expensive
  per token than these numbers because the cluster is paid for whether it's
  busy or idle. Tune the throughput inputs in the **Advanced** panel to match
  your actual rollout pace.
</Note>

## What's covered

The calculator currently includes the four models for which Tinker publishes
per-token rates:

| Model                    | Tinker prefill / sample (per 1M) |
| ------------------------ | -------------------------------- |
| Kimi K2.6 (128K)         | $5.15 / $12.81                   |
| Kimi K2.5 (128K)         | $5.15 / $12.81                   |
| Qwen3.5-397B-A17B (256K) | $4.00 / $10.00                   |
| GPT-OSS-120B (128K)      | $0.63 / $1.54                    |

All Fireworks-side rates are taken from the public pages linked below and the
constants live in `snippets/multi-turn-cost-calculator.jsx` — update there if
either side's pricing changes.

## FAQ

### What is the fastest way to reduce wall-clock time?

Increase replicas and overlap sampling/training where your workflow allows it.
Those are usually the most direct levers for shortening end-to-end cycle time.

### How should I compare costs between providers?

Use matched assumptions for context length, truncation policy, and effective
resource allocation. The calculator at the top of this page handles the math
once you plug in your episode shape — be sure to also align truncation policy
and effective context window between providers before drawing conclusions.

## Sources

* Tinker pricing: [thinkingmachines.ai/tinker](https://thinkingmachines.ai/tinker)
* Fireworks GPU-hour pricing: [fireworks.ai/pricing](https://fireworks.ai/pricing)
* Related: [RFT Cost Estimator](/fine-tuning/reinforcement-fine-tuning-models#rft-cost-planning) — same idea, but
  for the training-side bill (Fireworks GPU-hour, no comparison column).

<Warning>
  This is an estimator, not a quote (updated). Real costs depend on your exact workload,
  cache hit rate, hardware utilization, and rate-card terms at run time.
</Warning>
