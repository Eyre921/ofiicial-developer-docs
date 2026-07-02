---
title: "Inference for RL Rollouts"
source: https://docs.fireworks.ai/guides/rollout-inference
path: guides/rollout-inference
---

Session affinity, KV-cache behavior, weight-swap behavior, and MoE Router Replay for rollout traffic on Fireworks inference deployments.

When you use Fireworks inference to collect RL rollouts, the regular [`/v1/completions`](/api-reference/post-completions) and [`/v1/chat/completions`](/api-reference/post-chatcompletions) endpoints expose a few extra features tailored to multi-turn, stateful rollout traffic. You can use these whether or not the underlying deployment is a hot-load deployment.

<Note>
  These features are fully compatible with the OpenAI SDKs — they're all
  attached as either request headers or optional body fields, so no SDK upgrade
  is required.
</Note>

## Session affinity

Multi-turn rollouts typically reuse a long prefix between turns (same system prompt, same trajectory so far). To get the KV cache to hit, all turns of a trajectory should land on the same inference replica. Two headers are relevant here:

* `x-multi-turn-session-id` — identifies the agent trajectory. Set this once per trajectory and keep it constant across turns. If both headers are present, Fireworks currently prefers this value when deriving the request's session-affinity key.
* `x-session-affinity` — fallback sticky routing key when `x-multi-turn-session-id` is absent. In most RL rollout setups, set it to the same trajectory ID.

<Tabs>
  <Tab title="Python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="<FIREWORKS_API_KEY>",
        base_url="https://api.fireworks.ai/inference/v1",
    )

    trajectory_id = "traj-42f1"

    for turn in trajectory:
        response = client.chat.completions.create(
            model="accounts/<account_id>/models/<model_id>",
            messages=turn.messages,
            extra_headers={
                "x-multi-turn-session-id": trajectory_id,
                "x-session-affinity": trajectory_id,
                "fireworks-deployment": "accounts/<account_id>/deployments/<deployment_id>",
            },
        )
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Authorization: Bearer <fireworks_api_key>" \
      -H "fireworks-model: accounts/<account_id>/models/<model_id>" \
      -H "fireworks-deployment: accounts/<account_id>/deployments/<deployment_id>" \
      -H "x-multi-turn-session-id: traj-42f1" \
      -H "x-session-affinity: traj-42f1" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "accounts/<account_id>/models/<model_id>",
        "messages": [{"role": "user", "content": "..."}]
      }'
    ```
  </Tab>
</Tabs>

<Tip>
  `x-session-affinity` on its own is already documented for general [prompt
  caching](/guides/prompt-caching#optimizing-inference-request-for-caching). In
  RL rollouts you typically also want `x-multi-turn-session-id` so that per-turn
  metrics (TTFT, generation latency) are aggregated by trajectory, while
  preserving the current serving preference when both headers are supplied.
</Tip>

## KV cache behavior for RL rollouts

The active request stream, the session ID, and `reset_prompt_cache` are tightly coupled in rollout workflows, but they are not the same mechanism. Keep the three layers separate:

| Layer                 | Scope                                                  | What it controls                                                        | What it does not control                               |
| --------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------- | ------------------------------------------------------ |
| Single request stream | One HTTP request that has already started decoding     | Active in-flight KV/state for that stream                               | Future prompt-prefix reuse after the stream ends       |
| Session ID            | Later requests that use the same stable trajectory key | Sticky routing to the same replica and `new_session` namespace behavior | A cache hit by itself, or active-stream recompute      |
| `reset_prompt_cache`  | Requests admitted after a checkpoint swap              | Which reusable prompt-prefix KV namespace later requests can use        | The active in-flight KV for a request already decoding |

### Active request stream

An active request stream is one in-flight HTTP request. Its active KV/state is private to that running decode.

When a checkpoint swap happens under **async transition**, the stream pauses, weights swap, and the same HTTP stream resumes with its existing active KV/state. `reset_prompt_cache` does not flush, invalidate, or recompute that active KV. Passing the same `x-multi-turn-session-id` also does not change this active-stream behavior.

When a checkpoint swap happens under **sync transition**, the server waits for in-flight requests to finish on the old weights before swapping. New requests that arrive during the swap can receive HTTP `425 Too Early` and should retry.

If every token in a turn must come from exactly one policy version, do not let a long request cross an async hot-load boundary. Use sync transition, end the turn before signaling the next snapshot, or track the streamed snapshot identity and filter rollouts accordingly.

### Session ID

For rollout traffic, use one stable session ID per trajectory:

* `x-multi-turn-session-id`: identifies the trajectory and is preferred when Fireworks derives the session-affinity key.
* `x-session-affinity`: fallback sticky routing key when `x-multi-turn-session-id` is absent. In RL rollouts, set it to the same trajectory ID.
* `user`: can also be used by general prompt-caching flows, but RL rollout traffic should use the headers above.

The session ID is coupled to prompt-cache sharing in two ways:

1. **Sticky routing:** later turns route back to the same serving replica, so they can see that replica's local prompt-prefix KV.
2. **Namespace behavior:** with `reset_prompt_cache=new_session`, later requests with an existing session ID can stay pinned to the previous prompt-cache namespace after a checkpoint swap.

A stable session ID is required for reliable reuse, but it is not sufficient by itself. A reusable prompt-prefix KV hit still requires the request to reach a replica that owns the cached prefix, the prompt tokens to match, and the prompt-cache isolation key to match.

Within one already-running HTTP stream, the session ID is not what preserves active KV. The active stream preserves its own KV/state because it is the same in-flight request.

### Behavior during weight swap

If your rollout traffic hits a hot-load deployment, a new checkpoint can arrive mid-rollout. What happens to your requests depends on the deployment's configured transition mode:

* **Async transition (recommended for RL):** in-flight requests pause then resume on the same HTTP connection using the new weights. The active turn keeps its current KV state, so it continues rather than restarting. New requests queue up. You see elevated TTFT but no errors.
* **Synchronous transition:** in-flight requests finish on the old weights; new requests get HTTP `425 Too Early` until the swap is done. Your client should retry with back-off, ideally keeping the same session-affinity key so it lands on a replica that has already finished the swap.

See [Checkpoint-swap behavior](/fine-tuning/rl-rollout-debugging#checkpoint-swap-behavior) for the full hot-load reference.

### `reset_prompt_cache`

Configure `reset_prompt_cache` per snapshot in `POST /hot_load/v1/models/hot_load`, for example:

```json theme={null}
{ "identity": "version_002", "reset_prompt_cache": "new_session" }
```

This setting applies after the checkpoint swap and controls reusable prompt-prefix KV for later requests.

| `reset_prompt_cache` | Active in-flight request crossing the swap                                                                                      | Later request with the same `x-multi-turn-session-id`          | Later request with a new session ID                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------- |
| `all` (default)      | Not recomputed by this setting. Async pauses and resumes with existing active KV; sync lets the request finish before the swap. | Recomputes prompt-prefix KV under the new snapshot namespace.  | Recomputes prompt-prefix KV under the new snapshot namespace. |
| `new_session`        | Not recomputed by this setting. Same active-stream behavior as `all`.                                                           | Can reuse eligible prompt-prefix KV for that existing session. | Recomputes prompt-prefix KV under the new snapshot namespace. |
| `none`               | Not recomputed by this setting. Same active-stream behavior as `all`.                                                           | Can reuse eligible prompt-prefix KV.                           | Can reuse eligible prompt-prefix KV.                          |

For RL rollouts, the usual policy is:

* Use `new_session` when an episode may continue across a weight sync and later turns in that same episode should keep eligible prompt-prefix reuse, while newly started episodes use the latest snapshot namespace.
* Use `all` when the next request should recompute prompt-prefix KV even if it uses the same `x-multi-turn-session-id`.
* Use `none` only when both existing and new sessions should keep using the previous prompt-cache namespace after the swap.

If you do not send a stable `x-multi-turn-session-id` for the trajectory, later requests are treated like new sessions for `new_session` semantics.

## MoE Router Replay

For Mixture-of-Experts models, training-inference divergence often comes from the router picking different top-K experts at the same token position between trainer and inference. Aligning those choices across rollouts and training is known as [Rollout Router Replay (R3)](https://arxiv.org/abs/2510.11370).

Fireworks inference supports returning the selected MoE experts for every token and every MoE layer. Pass `include_routing_matrix: true` together with `logprobs: true` on your request:

```bash theme={null}
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer <fireworks_api_key>" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "accounts/<account_id>/models/<model_id>",
    "messages": [{"role": "user", "content": "..."}],
    "include_routing_matrix": true,
    "logprobs": true
  }'
```

The selected expert indices for each token are returned alongside logprobs. For `/v1/chat/completions` you find them at `choices[i].logprobs.content[j].routing_matrix`; for `/v1/completions` the structure is analogous. Each value is a flattened, base64-encoded `uint8` array of shape `[num_layers_with_moe, num_active_experts]`.

### Example response (DeepSeek V3)

```json theme={null}
{
  "object": "text_completion",
  "model": "...my-deepseek-v3-model...",
  "choices": [
    {
      "index": 0,
      "logprobs": {
        "content": [
          {
            "token": " ",
            "logprob": -0.00014507,
            "sampling_logprob": -0.0001450882,
            "token_id": 223,
            "routing_matrix": "CYvWPzaOl8g/o7q2XPVTMJ7w/Y8G..."
          }
        ]
      }
    }
  ]
}
```

### Decoding the routing matrix

DeepSeek V3 has 58 MoE layers (the first 3 of 61 total are dense) and selects 8 active experts per token, so each decoded buffer is `58 * 8 = 464` bytes.

```python theme={null}
import base64
import numpy as np

num_layers_with_moe = 58
num_active_experts = 8

encoded = choice["logprobs"]["content"][0]["routing_matrix"]
raw_bytes = base64.b64decode(encoded)
routing_matrix = np.frombuffer(raw_bytes, dtype=np.uint8).reshape(
    num_layers_with_moe, num_active_experts
)
# routing_matrix[layer_idx] -> array of 8 expert indices for that token
```

### Other API modes

* **Completions API (`/v1/completions`)**: same mechanism — `include_routing_matrix` and `logprobs` are top-level body fields.
* **Streaming (`stream: true`)**: `routing_matrix` is included on each streamed token chunk's `logprobs.content` entry.
* **Prompt tokens (`echo: true`)**: returns expert selection for the prompt tokens too. Combine with `echo_last: N` to only include expert selection for the last N prompt tokens.

## Policy version in responses

On **hot-load** deployments, track which snapshot served each token—useful for off-policy RL and debugging stale rollouts.

### Streaming

Each streamed chunk includes the loaded snapshot in the `model` field as `accounts/<account_id>/models/<model_id>@<snapshot_identity>`:

```text theme={null}
data: {"object":"text_completion","model":"accounts/<account_id>/models/<model_id>@version_002","choices":[{"index":0,"text":"...","finish_reason":null}],...}
```

Parse the suffix after `@` as the policy version for that token. If a weight swap happens mid-stream under async transition, later chunks may reflect the new snapshot.

### Non-streaming

Non-streaming responses are adding the same `model@snapshot_identity` convention; until your deployment shape exposes it, rely on streaming or correlate rollout timing with your hot-load poll timestamps.

## Related pages

<CardGroup>
  <Card title="Quickstart (BYOT)" icon="rotate" href="/fine-tuning/rl-rollout-integration">
    Prerequisites, hot-load deployment, and rollout loop.
  </Card>

  <Card title="Incremental snapshots" icon="layer-group" href="/fine-tuning/rl-rollout-delta-checkpoints">
    ARC2 compression and incremental hot-load signals.
  </Card>

  <Card title="Ledger & checkpoint swap" icon="bug" href="/fine-tuning/rl-rollout-debugging">
    Detailed semantics of request behavior across weight swaps.
  </Card>

  <Card title="Prompt caching" icon="memory" href="/guides/prompt-caching">
    Session-affinity patterns for general cache hit optimization.
  </Card>
</CardGroup>
