---
title: "Agent Tracing"
source: https://docs.fireworks.ai/fine-tuning/environments
path: fine-tuning/environments
---

Understand where your agent runs and how tracing enables reinforcement fine-tuning

## Why agent tracing is critical to doing RL

Reinforcement learning for agents depends on the entire chain of actions, tool calls, state transitions, and intermediate decisions—not just the final answer. Tracing captures this full trajectory so you can compute reliable rewards, reproduce behavior, and iterate quickly.

**Why it matters**

* **Credit assignment**: You need a complete record of each step to attribute reward to the decisions that caused success or failure.
* **Reproducibility**: Deterministic replays require the exact prompts, model parameters, tool I/O, and environment state.
* **Debuggability**: You can pinpoint where an episode fails (model output, tool error, data mismatch, timeout).

<Tip>
  Use Fireworks Tracing to drive the RL loop: emit structured logs with `FireworksTracingHttpHandler`, tag them with rollout correlation metadata, and signal completion using `Status.rollout_finished()` or `Status.rollout_error()`. When you make model calls, use the `model_base_url` issued by the trainer (it points to `https://tracing.fireworks.ai`) so chat completions are recorded as traces via an OpenAI-compatible endpoint.
</Tip>

## How Fireworks tracing works for RFT

* **Traced completions**: The trainer provides a `model_base_url` on `https://tracing.fireworks.ai` that encodes correlation metadata. Your agent uses this OpenAI-compatible URL for LLM calls; tracing.fireworks.ai records the calls as traces automatically.
* **Structured logging sink**: Your agent logs to Fireworks via `FireworksTracingHttpHandler`, including a structured `Status` when a rollout finishes or errors.
* **Join traces and logs**: The trainer polls the logging sink by `rollout_id` to detect completion, then loads the full trace. Logs and traces are deterministically joined using the same correlation tags.

### Correlation metadata

* **Correlate every log and trace** with these metadata fields provided in `/init`: `invocation_id`, `experiment_id`, `rollout_id`, `run_id`, `row_id`.
* **Emit structured completion** from your server logs:
  * Add `FireworksTracingHttpHandler` and `RolloutIdFilter` to attach the `rollout_id`
  * Log `Status.rollout_finished()` on success, or `Status.rollout_error(message)` on failure
* **Alternative**: If you run one rollout per process, set `EP_ROLLOUT_ID` in the child process instead of adding a filter.
* **Record model calls as traces** by using the `model_base_url` from the trainer. It encodes the correlation IDs so your completions are automatically captured.

### tracing.fireworks.ai base URL

* **Purpose-built for RL**: tracing.fireworks.ai is the Fireworks gateway used during RFT to capture traces and correlate them with rollout status.
* **OpenAI-compatible**: It exposes Chat Completions-compatible endpoints, so you set it as your client's `base_url`.
* **Correlation-aware**: The trainer embeds `rollout_id`, `run_id`, and related IDs into the `model_base_url` path so your completions are automatically tagged and joinable with logs.
* **Drop-in usage**: Always use the `model_base_url` provided in `/init`—do not override it—so traces and logs are correctly linked.

## End-to-end tracing setup with tracing.fireworks.ai

<Steps>
  <Step title="Receive init and configure correlation">
    Your server implements `/init` and receives `metadata` and `model_base_url`. Attach `RolloutIdFilter` or set `EP_ROLLOUT_ID` for the current rollout.
  </Step>

  <Step title="Send traced model calls through Fireworks">
    Call the model using `model_base_url` so chat completions are persisted as traces with correlation tags.
  </Step>

  <Step title="Emit structured status to logging sink">
    Attach `FireworksTracingHttpHandler` to your logger and log `Status.rollout_finished()` or `Status.rollout_error()` when the rollout concludes.
  </Step>

  <Step title="Trainer detects completion and joins data">
    The trainer polls Fireworks logs by `rollout_id`, then loads the full traces; logs and traces share the same tags and are joined to finalize results and compute rewards.
  </Step>
</Steps>

### Remote server minimal example

```python remote_server.py theme={null}
import logging
import os
from eval_protocol import InitRequest, Status, FireworksTracingHttpHandler, RolloutIdFilter

# Configure Fireworks logging sink once at startup
logging.getLogger().addHandler(FireworksTracingHttpHandler())

@app.post("/init")
def init(request: InitRequest):
    # Option A: add filter that injects rollout_id on every log record
    logger = logging.getLogger(f"eval.{request.metadata.rollout_id}")
    logger.addFilter(RolloutIdFilter(request.metadata.rollout_id))

    # Option B: per-process correlation (use when spawning one rollout per process)
    # os.environ["EP_ROLLOUT_ID"] = request.metadata.rollout_id

    # Make model calls via the correlated base URL so completions are traced
    # client = YourLLMClient(base_url=request.model_base_url, api_key=request.api_key)
    try:
        # ... execute rollout steps, tool calls, etc. ...
        logger.info("rollout finished", extra={"status": Status.rollout_finished()})
    except Exception as e:
        logger.error("rollout error", extra={"status": Status.rollout_error(str(e))})
```

<Info>
  Under the hood, the trainer polls the logging sink for `Status` and then loads the full trace for scoring. Because both logs and traces share the same correlation tags, Fireworks can deterministically join them to finalize results and compute rewards.
</Info>

### What to capture in a trace

* **Inputs and context**: Task ID, dataset split, initial state, seeds, and any retrieval results provided to the agent.
* **Model calls**: System/user messages, tool messages, model/version, parameters (e.g., temperature, top\_p, seed), token counts, and optional logprobs.
* **Tool and API calls**: Request/response summaries, status codes, durations, retries, and sanitized payload snippets.
* **Environment state transitions**: Key state before/after each action that affects reward or next-step choices.
* **Rewards**: Per-step shaping rewards, terminal reward, and component breakdowns with weights and units.
* **Errors and timeouts**: Exceptions, stack traces, and where they occurred in the trajectory.
* **Artifacts**: Files, code, unit test results, or other outputs needed to verify correctness.

<Warning>
  Never record secrets or raw sensitive data in traces. Redact tokens, credentials, and PII. Store references (IDs, hashes) instead of full payloads whenever possible.
</Warning>

### How tracing powers the training loop

1. **Rollout begins**: Trainer creates a rollout and sends it to your environment (local or remote) with a unique identifier.
2. **Agent executes**: Your agent emits spans for model calls, tool calls, and state changes; your evaluator computes step and terminal rewards.
3. **Rewards aggregate**: The trainer consumes your rewards and updates the policy; traces are stored for replay and analysis.
4. **Analyze and iterate**: You filter traces by reward, failure type, latency, or cost to refine prompts, tools, or reward shaping.

### How RemoteRolloutProcessor uses Fireworks Tracing

1. **Remote server logs completion** with structured status: `Status.rollout_finished()` or `Status.rollout_error()`.
2. **Trainer polls Fireworks Tracing** by `rollout_id` until completion status is found.
3. **Status extracted** from structured fields (`code`, `message`, `details`) to finalize the rollout result.

### Best practices

* **Make it deterministic**: Record seeds, versions, and any non-deterministic knobs; prefer idempotent tool calls or cached fixtures in test runs.
* **Keep signals bounded**: Normalize rewards to a consistent range (e.g., \[0, 1]) and document your components and weights.
* **Summarize, don’t dump**: Log compact summaries and references for large payloads to keep traces fast and cheap.
* **Emit heartbeats**: Send periodic status updates so long-running rollouts are observable; always finalize with success or failure.
* **Use consistent schemas**: Keep field names and structures stable to enable dashboards, filters, and automated diagnostics.

## Next steps

<CardGroup>
  <Card title="Connect remote environment" icon="server" href="/fine-tuning/connect-environments">
    Implement `/init`, tracing, and structured status for remote agents
  </Card>

  <Card title="Small model quickstart" icon="bolt" href="/fine-tuning/quickstart-math">
    Build and deploy a local evaluator in under 10 minutes
  </Card>

  <Card title="Launch training" icon="rocket" href="/fine-tuning/cli-reference">
    Launch your RFT job
  </Card>

  <Card title="Evaluator best practices" icon="code" href="/fine-tuning/evaluators">
    Design effective reward functions for your task
  </Card>
</CardGroup>
