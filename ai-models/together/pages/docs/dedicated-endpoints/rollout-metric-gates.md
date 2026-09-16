---
title: "Gate rollouts with metrics"
source: https://docs.together.ai/docs/dedicated-endpoints/rollout-metric-gates
path: docs/dedicated-endpoints/rollout-metric-gates
---

Pause a canary rollout automatically when the new deployment regresses.

When you create a [canary rollout](/docs/dedicated-endpoints/rollouts), you can configure a metric gate to pause the rollout automatically when the target deployment regresses, for example when it serves traffic more slowly than the source or has a higher error rate.

A metric gate monitors live metrics as the rollout shifts traffic. After each step, the rollout holds the traffic split during the "soak window", a waiting period (set by `--interval` in the CLI, or **Step interval** in the console) during which traffic stays at the current split level so the metric can settle and accumulate samples.

At the end of the window, the gate evaluates its rules against the target deployment and either advances the rollout or pauses it for review.

<Warning>
  **Metric gates require traffic on the endpoint:** The gate compares live traffic on the target against the source. If the endpoint is serving traffic but the target accumulates no samples, the gate reports the metric as unavailable and the rollout pauses for review. A fully idle endpoint (no traffic on either deployment) skips the gate entirely and the rollout proceeds ungated.
</Warning>

## Configure a metric gate

Metric gates are canary-only. Blue-green and rolling strategies have no soak window, so a gate is rejected at create time.

<Tabs>
  <Tab title="CLI">
    Configure a gate by passing `--metric*` flags to the `rollout dep_target456 --canary` command. Pass a [supported metric](#supported-metrics) plus either a threshold check or a regression check. For `router_latency`, set `--metric-stat` to `avg` or a percentile. For `router_error_rate` and `inflight_requests`, omit `--metric-stat` (the platform records it as `AVG`).

    ```bash theme={null}
    # Threshold check: p95 router latency must stay under 30 seconds (in milliseconds)
    tg beta endpoints rollout dep_target456 --canary \
      --metric router_latency --metric-stat p95 \
      --metric-threshold 30000 --metric-operator lt \
      --metric-window 300s

    # Regression check: p95 router latency at most 50% worse than the source
    tg beta endpoints rollout dep_target456 --canary \
      --metric router_latency --metric-stat p95 \
      --metric-max-regression 50 --metric-direction higher-is-worse \
      --metric-window 300s

    # Ratio gate: omit --metric-stat (stored as AVG). Threshold is a 0-1 ratio (0.02 = 2%).
    tg beta endpoints rollout dep_target456 --canary \
      --metric router_error_rate \
      --metric-threshold 0.02 --metric-operator lt \
      --metric-window 300s
    ```

    `--metric-stat` picks the aggregation the gate applies over the lookback window: a percentile (`p50`, `p90`, `p95`, or `p99`) or `avg`, the mean over the window. It is required for `router_latency` and optional for the other metrics, which only aggregate one way.

    See the [CLI reference](/reference/cli/endpoints-beta#rollout) for the full flag list.
  </Tab>

  <Tab title="Console">
    <ConsoleButton href="https://api.together.ai/endpoints">Endpoints</ConsoleButton>

    Open your endpoint's **Rollouts** tab, select **New rollout**, and pick **Canary**. Under **Metric gates**, select **Add metric gate**, then set:

    1. **Metric:** One of the [supported metrics](#supported-metrics): **Router latency**, **Router error rate**, or **Inflight requests**.
    2. **Aggregation:** For **Router latency**, pick Average or Percentile (when you pick Percentile, also set **Percentile** to p50, p90, p95, or p99). For **Router error rate** and **Inflight requests**, Average is the only aggregation.
    3. **Check:** **Threshold** (set **Operator** and **Threshold**) or **Regression vs. source** (set **Direction** and **Max regression (%)**).
    4. **Window (s):** Optional [lookback window](#choose-a-lookback-window) in seconds. Leave it blank to use the default.

    Select **Add metric gate** again to attach more rules.
  </Tab>
</Tabs>

## Threshold vs. regression checks

Each gate uses one of the following checks to evaluate the target at the end of each soak window:

* **Threshold check:** Compares the target against a fixed SLO, set with `--metric-threshold` and `--metric-operator` (`gt`, `gte`, `lt`, or `lte`). For example, "p95 router latency must stay under 30 seconds".
* **Regression check:** Compares the target against the source, set with `--metric-max-regression` (a percent) and `--metric-direction` (`higher-is-worse` or `lower-is-worse`). It fails when the target is worse than the source by more than the allowed amount. For example, "the new deployment must not be more than 50% slower than the old one".

## Supported metrics

The following metrics are supported (creating a rollout with any other metric name is rejected with a `400` error). All of them are measured at the router.

| `--metric`          | Type      | What it measures                                                                                                                                                                                                                                                                         | `--metric-stat`                 |
| ------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `router_latency`    | Histogram | Router per-attempt request duration, in milliseconds. Bimodal (the median attempt is often a fast reject), so gate on `p95` or higher rather than the mean.                                                                                                                              | Required: `avg` or a percentile |
| `router_error_rate` | Ratio     | Router 5xx responses divided by all inference responses. This is a ratio, so set the threshold as a 0-1 value, for example 0.02 for 2%.                                                                                                                                                  | Optional (stored as `AVG`)      |
| `inflight_requests` | Gauge     | Concurrent requests, i.e. requests the router has sent to the deployment's replicas that haven't yet finished, averaged over the [lookback window](#choose-a-lookback-window). This is measured per ready replica, so make sure not to size your threshold against the fleet-wide total. | Optional (stored as `AVG`)      |

For regression checks, higher values are worse for all three metrics.

## Choose a lookback window

`--metric-window` (CLI) or **Window (s)** (console) sets the lookback period over which the gate samples the metric. The minimum is `60s`. When omitted, it defaults to `300s` (five minutes).

Use at least `300s` for `router_latency` percentile gates. A short window such as `60s` falls inside the metric pipeline's ingestion lag (about 90 seconds) and will likely hold too few samples for a trustworthy percentile, causing the rollout to pause unnecessarily.

You don't need to size the step interval to fit the window: at create time, the platform grows each step's soak window to at least the metric window plus the ingestion lag, so the metric always has time to settle and accumulate samples before the target is evaluated.

## Gate on more than one rule

The CLI configures a single-rule gate. To gate on several rules at once, add multiple gates in the console's **New rollout** dialog, or [create the rollout through the API](/reference/dmi/rollouts-create) and then [start it manually](/reference/dmi/rollouts-start). A step advances only when every rule passes. If any rule regresses or its metric is unavailable, the rollout pauses instead.

You can attach both a threshold check and a regression check on the same metric. When you [retrieve the rollout](/docs/dedicated-endpoints/rollouts#monitor-progress), each configured rule appears as its own row in `status.steps[].metrics`, with its criteria and its own verdict.

## How gate results appear on retrieve

Each metric row in `status.steps[].metrics` or `status.condition.metrics` is a `MetricResult` object containing the rule's name, check form, criteria, optional observed values, and a verdict (`PASS`, `BREACHED`, or `UNAVAILABLE`).

* **Measured rows:** `targetValue` is set whenever the gate recorded an observation, including a legitimate `0`. `sourceValue` is set only on regression-check rows, because threshold checks never consult the source.
* **Unmeasured rules:** When the gate couldn't measure a rule (for example, no traffic reached the target), the rule still appears as a row with verdict `UNAVAILABLE` and its criteria, but no `sourceValue` or `targetValue`.
* **Completed rollouts:** A `COMPLETED` rollout never marks a step as `FAILED`. Finished steps are `PASSED`, and steps a promote jumped over are `SKIPPED`. For the full per-step state set, see [Step status on retrieve](/docs/dedicated-endpoints/rollouts#step-status-on-retrieve).

## What to do when a metric gate fails

If a metric gate fails (the target deployment doesn't meet the gate's threshold or regression criteria), the rollout pauses automatically. The traffic split that's in place when the gate fails is maintained while the rollout is paused. Review the gate verdicts for each completed step by [retrieving the rollout](/docs/dedicated-endpoints/rollouts#monitor-progress), or open the **Rollout details** drawer from the progress card or history table in the console.

The pause reason (shown on the paused rollout and on its `rollout.system_paused` [event](/docs/dedicated-endpoints/monitoring#events)) starts with one of two prefixes:

* **`metrics-regression:`** The gate confirmed the target is worse than the gate's criteria allow. The rest of the reason names the failing rule and the observed values. Investigate why the target regressed before acting. If the target itself is at fault, cancel the rollout, then [run it in reverse](/docs/dedicated-endpoints/rollouts#roll-back-to-the-source) to move traffic back to the source. If the cause was external (like a traffic surge), resume instead.
* **`metrics-unavailable:`** The gate could not get a trustworthy reading, so it paused rather than advancing on incomplete data. Common causes are gaps in the metrics pipeline (the most common), too few samples in the [lookback window](#choose-a-lookback-window), and zero ready replicas on the target or source. Most of these are transient—the platform confirms the reading before pausing and [retries automatically](/docs/dedicated-endpoints/rollouts#troubleshooting). Resume the rollout manually if the pause persists. The paused step's metrics include an `UNAVAILABLE` row for each rule the gate could not measure.

See [Troubleshooting rollouts](/docs/dedicated-endpoints/rollouts#troubleshooting) for more details on how to respond to each failure condition.

## Next steps

<CardGroup>
  <Card title="Start a rollout" icon="arrows-exchange" href="/docs/dedicated-endpoints/rollouts">
    Create and run the canary rollout a gate protects.
  </Card>

  <Card title="Observability" icon="chart-line" href="/docs/dedicated-endpoints/monitoring">
    Watch the same metrics on your endpoint's dashboards.
  </Card>
</CardGroup>
