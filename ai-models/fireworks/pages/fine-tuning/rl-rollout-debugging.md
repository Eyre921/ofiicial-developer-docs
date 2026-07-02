---
title: "Ledger & Debugging for RL Rollouts"
source: https://docs.fireworks.ai/fine-tuning/rl-rollout-debugging
path: fine-tuning/rl-rollout-debugging
---

Inspect snapshot history, reset the ledger, and understand how in-flight requests behave during a weight swap.

<Warning>
  **Early Access Feature.** This page is part of the same private-preview
  external-bucket hot-load workflow for RL rollouts. Contact Fireworks to enable
  this path on your account before using non-`FW_HOSTED` storage.
</Warning>

<Note>
  If you are using Fireworks-managed RLOR trainers with `FW_HOSTED`, the ledger
  and checkpoint-swap behavior here still matter, but you can usually ignore the
  external-bucket setup and manual upload/signaling details from the BYOT
  integration guide.
</Note>

A hot-load deployment maintains a **ledger** of every snapshot it has loaded, along with which replica finished which snapshot at what time. The ledger is the fastest way to answer "what weights is my deployment serving right now?" and to recover from a stuck state.

## Inspect snapshot history

Dump the ledger, sorted by most recent snapshot first:

```bash theme={null}
firectl get ledger <deployment_id>
```

Each row shows the `identity` you signaled, whether it was a full or delta snapshot, the per-replica `readiness` transition timestamps, and any load error.

## Inspect deployment status and failures

If the deployment itself is unhealthy (crashlooping after a bad snapshot, out-of-memory on merge, etc.), the reason is on the deployment resource itself:

```bash theme={null}
firectl deployment get <deployment_id>
```

Look at the `status`, `latestStatus.reason`, and the most recent ledger entry together to reason about whether the problem is load-side, weights-side, or infra-side.

### Snapshot config validation errors

Weight sync validates each snapshot's `config.json` against the deployment's base-model config before serving the snapshot. A validation failure means the snapshot stayed unloaded; continue serving the previous ready snapshot or fall back to a new full snapshot after fixing the files.

Common messages include:

* `Extra base model config options` or `Extra snapshot model config options`: one config has a top-level field that the other does not.
* `Config value mismatch for <field>`: both configs contain the field, but the values differ.
* `Types mismatch`: the snapshot config resolves to a different HuggingFace config class than the base model.

If the only difference is a known-safe additive metadata field, retry the weight sync request with `validation.extra_fields_ignore`, for example:

```json theme={null}
{
  "identity": "version_002",
  "validation": {
    "extra_fields_ignore": ["snapshot_only_option"]
  }
}
```

<Warning>
  Important: Ignoring model-affecting fields can cause load or serving failures; only bypass known-safe metadata fields.
</Warning>

## Reset the ledger

If the delta chain is wedged or you want to force the deployment back to the base model, you can clear server-side ledger history. This preserves the deployment itself; it just forgets every hot-loaded snapshot.

```bash theme={null}
curl -X DELETE \
  https://api.fireworks.ai/v1/accounts/<account_id>/deployments/<deployment_id>/ledger \
  -H "Authorization: Bearer <fireworks_api_key>"
```

After reset, your next signal must be a **full** snapshot (delta metadata will be rejected because there's nothing to diff against).

## Checkpoint-swap behavior

When you signal a new snapshot, Fireworks has to eventually swap weights on every replica. What happens to **in-flight** and **new** requests during the swap depends on which transition mode the deployment is configured with.

<Info>
  Both modes behave the same way for checkpoint download — it always starts immediately after the signal, in parallel with ongoing inference. The modes differ in how they handle the actual weight-swap moment.

  Set the mode at deployment create time with `--hot-load-transition-type ASYNC` or `SYNC` (default `ASYNC`). See [Create a hot-load deployment](/fine-tuning/rl-rollout-integration#1-create-a-hot-load-deployment).
</Info>

### Async transition (recommended, default for RL)

This mode is similar in spirit to [PipelineRL](https://arxiv.org/pdf/2509.19128):

* **In-flight requests**: paused for the duration of the swap, then resumed on the same HTTP connection. The active turn keeps its current KV state, so the request continues streaming instead of restarting.
* **New requests**: queued until the swap finishes. Clients observe this as elevated time-to-first-token (TTFT).
* **No 4xx or 5xx** is returned for the swap itself. Users may specify `x-fireworks-hot-load-drain-timeout` timeout request header in seconds (default `90`) to receive HTTP 425 Too Early once the timeout expires.

<img />

<img />

### Synchronous transition

* **In-flight requests**: the server waits for them to complete on the *old* weights before swapping.
* **New requests** arriving during the swap are rejected with HTTP `425 Too Early`. Your rollout client should back off and retry, ideally using the same session-affinity key so it lands on a replica that has already finished the swap.

<img />

<img />

### Prompt cache reset behavior

`reset_prompt_cache` only affects what can be reused **after** the swap. It does not interrupt the **active turn** (the in-flight HTTP stream), but it affects the next turn in the same session and new sessions.

Configure per snapshot in `POST /hot_load/v1/models/hot_load`, for example `{ "identity": "version_002", "reset_prompt_cache": "new_session" }`.

For the full RL rollout mental model across active streams, session IDs, and reset options, see [KV cache behavior for RL rollouts](/guides/rollout-inference#kv-cache-behavior-for-rl-rollouts).

## Need help?

If the ledger stops advancing, a snapshot never becomes ready, or the deployment stays unhealthy after you fall back to a full snapshot, contact Fireworks. Include the account ID, deployment ID, snapshot identity you tried to load, and the latest ledger output.

## Related pages

<CardGroup>
  <Card title="Quickstart (BYOT)" icon="rotate" href="/fine-tuning/rl-rollout-integration">
    Prerequisites, deployment setup, and the hot-load API.
  </Card>

  <Card title="Incremental snapshots" icon="layer-group" href="/fine-tuning/rl-rollout-delta-checkpoints">
    ARC2 deltas, hints, and incremental signal bodies.
  </Card>

  <Card title="Inference for RL rollouts" icon="bolt" href="/guides/rollout-inference">
    Session affinity, policy version in streams, and MoE Router Replay.
  </Card>
</CardGroup>
