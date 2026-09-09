---
title: "Cookbook: Agentic Reinforcement Learning"
source: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/agentic-rl
path: fine-tuning/training-api/cookbook/agentic-rl
---

Preserve exact token evidence when tool-using agents cross the token/message boundary.

Agentic RL uses the same rollout and optimization contract described in
[Cookbook: Reinforcement Learning](/fine-tuning/training-api/cookbook/rl).
The async RL recipe still owns scheduling, GRPO grouping, advantages, training,
and policy publication. The agentic adapter runs the multi-turn harness and
returns exact, loss-aligned rollout data.

## Why multi-turn RL needs TITO

An agent harness operates on messages: it reads an assistant tool call,
executes the tool, appends the result, and submits the next request. RL trains
on the exact token IDs and rollout-policy log probabilities used by inference.

For each policy turn, TITO (token-in/token-out) records:

```text theme={null}
exact prompt IDs + exact sampled action IDs + aligned logprobs + loss mask
```

The boundary matters because a sampled action must become a message before the
harness can continue. Rendering that message on the next turn is not guaranteed
to reproduce the same token IDs. Tool-argument JSON may be reserialized,
empty content may change representation, model-specific stop/message boundaries
may overlap, or the harness may compact or rewrite its history.

Messages alone cannot prove what the rollout policy sampled. If an exact prompt
diverges from the previous exact checkpoint, TITO keeps both sides valid by
closing the old training segment and starting a new one from the prompt that
actually produced the next action. The new prompt is masked context; the exact
sampled action remains trainable. All segments from one rollout keep the same
reward, GRPO group membership, and advantage.

## Choose whether online behavior may change

Fireworks supports two TITO behaviors. The meaningful distinction is whether
TITO changes the prompt used to sample the next trainable action.

| Mode                     | Effect on online inference                                                                                                                                              | Continuity check                                                                                                                                                                                                   | Trade-off                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `full_history` (default) | None. The harness sends its ordinary full-history prompt. With exact per-call token and logprob capture, TITO can materialize the trajectory offline.                   | Apply the chat template to the full message history and require the result to extend the previously recorded exact tokens. Try a bounded realignment of the latest action; split when it cannot be aligned safely. | Easier to support across renderers, and the full-render comparison guarantees that token drift is not silently treated as exact continuity. Re-rendering more history can expose more drift, causing more splits or masked spans and a lower trainable-token ratio. [slime's coding-agent trajectory manager](https://github.com/THUDM/slime/tree/main/examples/coding_agent_rl) is one public reference. |
| `incremental` (opt-in)   | Online only. The next inference prompt is the previous exact checkpoint joined with the newly rendered message suffix, so it can differ from the harness's full replay. | Render only the new suffix and validate its junction with the exact checkpoint. Split when the junction cannot be certified.                                                                                       | Usually retains more exact continuity because it does not re-render the preserved prefix, but every model/template junction needs explicit implementation and verification. [Miles session v2](https://github.com/radixark/miles/tree/main/miles/rollout/session/v2) is one public reference.                                                                                                             |

`full_history` continuity handling may run after the rollout if every call
already recorded its actual prompt IDs, sampled IDs, and logprobs. Re-rendering
messages later is not sufficient. `incremental` must run before inference
because constructing a different prompt after an action was sampled cannot
change what the model saw.

Neither mode makes a genuine history rewrite—such as compaction, pruning, or a
subagent handoff—continuous without changing its meaning.

## Fireworks support

The public [Fireworks Cookbook](https://github.com/fw-ai/cookbook/tree/main/training/examples/rl/harbor)
separates the environment, harness, and task recipe. They are independent
parts of one rollout rather than one Harbor integration.

### Overall RL environment: Harbor

[Harbor](https://harborframework.com/) is the trial and environment layer. It
loads a task, starts its Docker container or E2B sandbox, runs the verifier,
produces the reward and artifacts, and tears the environment down. In the
reference integration, the TITO sidecar runs inside that sandbox beside the
agent harness.

```text theme={null}
task dataset -> Harbor trial -> Docker or E2B sandbox
                                |- agent harness -> TITO sidecar -> inference
                                `- verifier -> reward and artifacts
```

### Supported harness adapters

The reference adapters support
[OpenCode](https://github.com/fw-ai/cookbook/tree/main/training/examples/rl/harbor/opencode),
[Pi](https://github.com/fw-ai/cookbook/tree/main/training/examples/rl/harbor/pi),
and [Mini-SWE-Agent](https://github.com/fw-ai/cookbook/tree/main/training/examples/rl/harbor/mini_swe)
over the same Harbor/TITO contract.

### Supported task datasets

The Cookbook includes support for DABstep, Terminal-Bench 2.0, and DeepSWE.

### Example: Pi with DABstep

Use the [Pi+DABstep training script](https://github.com/fw-ai/cookbook/blob/main/training/examples/rl/harbor/recipes/dabstep/train_pi.py)
as the complete reference entrypoint. The Cookbook also provides task
preparation scripts for [Terminal-Bench](https://github.com/fw-ai/cookbook/blob/main/training/examples/rl/harbor/opencode/prepare_tasks.py)
and [DeepSWE](https://github.com/fw-ai/cookbook/blob/main/training/examples/rl/harbor/recipes/deep_swe/prepare_tasks.py).

These task entrypoints plug into the async RL lifecycles described in
[Cookbook: Reinforcement Learning](/fine-tuning/training-api/cookbook/rl); this
page does not repeat the dedicated and serverless execution choices.

Both prompt-construction modes use the same TITO engine, exact-token sampler
boundary, artifact format, and `RolloutRun` materializer. Prompt construction
defaults to `full_history`; select `incremental` explicitly with
`--tito-prompt-mode incremental` only for a renderer/tokenizer contract that
qualifies the additional suffix and junction behavior. An ordinary SFT/DPO
renderer does not automatically qualify a model for agentic TITO.

## The sidecar is a reference placement

The Cookbook starts one lightweight TITO sidecar inside every agent sandbox:

```text theme={null}
agent in a Docker container or E2B sandbox
  -> loopback OpenAI-compatible endpoint
  -> TITO sidecar
  -> Fireworks inference over HTTP
```

This placement requires no user-operated middleware fleet, public callback, or
central stateful gateway. It also keeps each trajectory's state and failure
domain with its sandbox.

The TITO invariants do not require this placement:

| Placement                      | Supported behavior                                                 | Main trade-off                                                                                  |
| ------------------------------ | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| Per-sandbox sidecar            | `full_history` and `incremental`                                   | Simple isolation and startup; the sidecar process must be reliable in every sandbox.            |
| Centralized long-lived gateway | `full_history` and `incremental`                                   | Shared lifecycle and observability; adds stateful routing, scaling, and a wider failure domain. |
| Offline materializer           | `full_history` only, with exact per-call token and logprob capture | No online middleware; cannot replace a prompt after inference has occurred.                     |

The Cookbook sidecar is the maintained reference implementation, not the only
valid TITO architecture. A custom integration may use offline materialization
or a centralized gateway as long as it preserves the exact prompt, action,
logprob, loss-mask, and rollout-identity contracts.
