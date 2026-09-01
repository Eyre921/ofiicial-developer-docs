---
title: "Cookbook: Agentic Reinforcement Learning"
source: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/agentic-rl
path: fine-tuning/training-api/cookbook/agentic-rl
---

Run tool-using agents with environment-local TITO sidecars and return exact-token trajectories to async RL.

Agentic RL adds a rollout adapter around either the dedicated
[`async_rl_loop`](/fine-tuning/training-api/cookbook/rl) or its experimental
`async_rl_loop_serverless` sibling. The adapter runs an agent in an environment,
records its policy turns, applies the environment reward, and returns one
`RolloutRun`. The selected async loop still owns scheduling, GRPO grouping,
advantages, optimization, evaluation, and policy publication.

The Harbor/TITO stack below is the Cookbook's structured agentic integration,
not a requirement of the async loop. You can supply another rollout adapter as
long as it returns the same aligned `RolloutRun` contract.

<Note>
  `TITOSidecar` requires `fireworks-ai[training]>=1.2.11` and a compatible
  Cookbook revision. Pin the Cookbook commit and SDK version for a production
  run.
</Note>

## Architecture

The Cookbook's production integration uses one SDK `TITOSidecar` inside each
agent environment:

```text theme={null}
async_rl_loop or async_rl_loop_serverless
  -> rollout_fn
    -> Harbor trial (local Docker or E2B)
      -> Pi, OpenCode, or Mini-SWE-Agent
        -> loopback TITOSidecar
          -> Fireworks sampler
```

The harness sends OpenAI-compatible messages and tools only to the loopback
endpoint. The sidecar applies the certified model renderer, sends exact prompt
token IDs through the sampler supplied by the selected loop, and records exact
completion IDs, aligned log probabilities, and optional Router Replay data.
Because it is colocated with the harness, local Docker and E2B use the same
protocol and E2B needs no callback URL, public tunnel, or Fireworks-hosted
stateful gateway.

The sidecar is harness-neutral. Harbor owns the trial and verifier; the harness
adapter owns agent-specific commands, events, timeouts, and call
classification; the renderer owns chat-template and assistant/tool parsing;
the async loop owns training. One sidecar may host multiple independent linear
trajectory engines, but V1 does not model branches or a shared trajectory tree.

## Dedicated and serverless execution

Both loops use the same `rollout_fn_factory(setup) -> rollout_fn` boundary and
can run Harbor/TITO trajectories:

| Path                       | Sampling and publication                                               | DABstep example                                                  |
| -------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `async_rl_loop`            | SDK-managed trainer plus a hot-load deployment                         | `harbor/recipes/train_pi.py` with Pi and E2B; DABstep by default |
| `async_rl_loop_serverless` | Shared serverless training/sampling pool with session-scoped snapshots | `harbor/recipes/dabstep/train.py` with OpenCode                  |

The serverless adapter is experimental and remains separate pending a shared
weight-publication contract. TITO captures the same exact-token evidence in
either path; only trainer, sampler, and publication lifecycle differ.

## Exact-token trajectory rules

For every policy turn, TITO preserves the exact token arrays observed at
inference. Prompt, system, user, tool-result, and repaired-context tokens are
masked; only sampled policy completion tokens are trainable. Token IDs,
log probabilities, loss masks, and requested routing data must stay aligned.
The adapter never decodes and retokenizes a sampled completion to manufacture
training data.

Full-history prompt construction is the default:

1. Render the incoming messages and tools with the certified chat template.
2. If the prompt exactly extends the active segment, append the new completion.
3. If a small, semantically equivalent rewrite starts inside the latest
   assistant response, the configured drift policy may replace and mask that
   tail (`realign`).
4. Otherwise, close the valid segment and start a new segment from the incoming
   full render (`new_segment`).

Segmentation does not create another rollout or another GRPO completion. Every
segment from one `rollout_fn` call stays in the same `RolloutRun`, receives the
same verifier reward, and shares one group membership and advantage. This is
the same loss-preserving split/realign tradeoff used by
[Slime's coding-agent RL example](https://github.com/THUDM/slime/tree/main/examples/coding_agent_rl),
adapted to an environment-local sidecar.

An experimental `incremental` prompt mode follows the linear construction in
[Miles Session v2](https://github.com/radixark/miles/tree/main/miles/rollout/session/v2):
it joins the previous exact checkpoint to a renderer-certified suffix instead
of replaying the entire history. It intentionally does not include Miles's
central service placement or session tree. Incremental mode is opt-in and
requires separate suffix-and-junction certification; it does not change the
default full-history path.

## Length, identity, and retries

Use `max_completion_tokens` to cap one assistant turn and `max_seq_len` for the
total prompt-plus-output window and training-retention boundary. Evaluation
inherits both values from the same rollout setup.

Keep these identities distinct:

| Identity             | Purpose                                                                |
| -------------------- | ---------------------------------------------------------------------- |
| `RolloutRun.run_id`  | Reward, metrics, and GRPO group membership                             |
| Harbor trial ID      | Environment and verifier lifecycle                                     |
| TITO trajectory ID   | Selects one linear engine inside the sidecar                           |
| Serving-affinity key | Routes policy calls from one attempt to a compatible inference replica |
| Attempt ID           | Prevents retry state from leaking into a fresh environment             |

A retry creates a fresh Harbor trial, TITO trajectory, credential, and
serving-affinity key. Transient environment or transport failures may retry the
whole attempt within a bounded budget. After exhaustion, return `None` so the
async loop drops that draw. A valid timeout, agent exit, malformed model tool
call, or other terminal task outcome may still carry the verifier's numeric
reward; a broken or misaligned trace must never be converted into a synthetic
zero reward.

## Artifacts and debugging

Every trial retains a compact `.tito` artifact as the authoritative record for
training and routine analysis. It contains trajectory status, segments, exact
turn data, prompt dispositions, call outcomes, and reducible metrics. Optional
debug mode adds plain JSONL events for troubleshooting; debug logs supplement
the compact artifact and are not a second training-data path. Credentials and
authorization headers are not persisted.

Before training, run sampling-only calibration and inspect long, tool-heavy,
retried, high-reward, low-reward, realigned, and split traces. Confirm that
array lengths align, split segments retain one logical reward and advantage,
and low-frequency valid task failures are distinguishable from systemic
renderer or infrastructure failures.

## Start from an example

The
[Harbor RL directory](https://github.com/fw-ai/cookbook/tree/main/training/examples/rl/harbor)
is the out-of-the-box starting point for agentic RL and separates four layers:

| Layer                 | Cookbook location                                                                                | Responsibility                                                         |
| --------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| Task recipe           | `harbor/recipes/`                                                                                | Dataset preparation, task selection, and training configuration        |
| Harness adapter       | `harbor/pi/`, `harbor/opencode/`, `harbor/mini_swe/`                                             | Agent-specific lifecycle and semantics                                 |
| Harbor + TITO adapter | `harbor/tito/`                                                                                   | Trial, sidecar bundle, exact-token artifact, reward, and cleanup       |
| Async RL recipe       | `training/recipes/async_rl_loop.py` or `training/recipes/experiment/async_rl_loop_serverless.py` | Fan-out, grouping, loss, optimizer, evaluation, and weight publication |

Start with
[Terminal-Bench](https://github.com/fw-ai/cookbook/tree/main/training/examples/rl/harbor/recipes/terminal_bench)
for a coding/tool-use OpenCode workflow, or the
[DABstep recipes](https://github.com/fw-ai/cookbook/tree/main/training/examples/rl/harbor/recipes/dabstep)
for managed Pi on E2B and experimental serverless OpenCode. If your tasks are
already in Harbor format, keep their environment and verifier configuration:
choose the
[OpenCode](https://github.com/fw-ai/cookbook/tree/main/training/examples/rl/harbor/opencode)
or [Pi](https://github.com/fw-ai/cookbook/tree/main/training/examples/rl/harbor/pi)
adapter, prepare the task images with the pinned harness, run sampling-only
calibration, then use the same rollout function for training.

Pi is the default reference harness for DeepSWE and for the managed DABstep
recipe. OpenCode drives the existing DABstep serverless recipe; Mini-SWE-Agent
is another adapter over the same Harbor/TITO boundary. Local Docker and E2B are
environment choices, not separate rollout implementations. The shipped sidecar
support is narrower than the general SFT/DPO renderer registry; use only
model/renderer pairs explicitly certified by the integration. A chat template
or offline renderer alone is not TITO certification.

For operational details and the full validation checklist, read the
[agentic RL skill reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/rl-agentic.md).
For scheduling, failure classification, metrics, and resume semantics, read
the [async RL skill reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/rl-async.md).
