---
title: "Cookbook: Agentic Reinforcement Learning"
source: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/agentic-rl
path: fine-tuning/training-api/cookbook/agentic-rl
---

Turn multi-turn agent and environment interactions into exact, trainer-ready trajectories without prescribing one agent architecture.

Agentic RL adds a trajectory adapter around an RL loop. The adapter runs the
agent and environment, records each policy generation, assigns the environment
reward, and returns trainer-ready data. The RL loop still owns scheduling,
grouping, advantages, optimization, and weight publication.

The cookbook's
[`async_rl_loop`](/fine-tuning/training-api/cookbook/rl) works with agentic
rollouts, but it does not require a particular agent framework, environment,
session service, or history-reconciliation policy.

## Correctness boundary

For each logical trajectory, the adapter should:

* preserve the exact generated token IDs and their aligned log probabilities;
* mask prompts, tool results, and environment observations out of the loss;
* keep every segment under one reward, GRPO group member, and advantage;
* define what happens when a later prompt is not an exact token append;
* distinguish an environment outcome from a broken or incomplete trace.

Never silently truncate or positionally zip mismatched token, log-probability,
loss-mask, or routing data. Either repair the trace using an explicit policy or
drop it before training.

## Choose a trajectory architecture

There is no required architecture. Common choices include:

| Approach                    | Behavior                                                                                                              | Tradeoff                                                                                                                                                                                                                                                          |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Split on token divergence   | Start another physical training segment when exact token ancestry breaks. The segments remain one logical trajectory. | Simple and lossless, but creates more trainer sequences. This is the policy used by the cookbook's Harbor/OpenCode example.                                                                                                                                       |
| Realign or fork             | Repair a small, well-defined drift and mask the replaced span; fork for larger or earlier divergence.                 | Preserves longer contiguous sequences, but the repair heuristic must be model- and renderer-safe. [Slime's coding-agent trajectory manager](https://github.com/THUDM/slime/tree/main/examples/coding_agent_rl) is one reference.                                  |
| Session service             | Put message validation, token accumulation, retry rollback, and sample assembly beside the inference router.          | Can preserve prefix caching and reduce client-side trace movement at scale, but adds a stateful service and stricter chat-template integration. [Miles' TITO session server](https://github.com/radixark/miles/tree/main/miles/rollout/session) is one reference. |
| Reject non-append histories | Require strict append-only behavior and retry or drop any violation.                                                  | Strongest invariant and simplest trainer input, but may discard valid agent work.                                                                                                                                                                                 |

Choose and test the policy for your harness. A history rewrite caused by a
subagent, retry, dynamic system field, or context management is not inherently
an error, and should not be labeled as compaction without evidence.

## Logical trajectories and physical segments

One `rollout_fn` call is one logical trajectory and one completion in its prompt
group. It may return multiple physical `RolloutSample` segments when histories
branch or token ancestry diverges. Those segments retain the same reward and
advantage; they do not become extra GRPO completions. If branches share a
generated prefix, train that prefix once and keep it as masked context on later
branches.

Treat retry and failure behavior as an algorithm decision. A malformed trace
should normally be retried within a bounded budget and then dropped. Assigning
reward zero is appropriate only when the environment defines the failure as a
real task outcome, not as a substitute for missing or misaligned training data.

## Start from an example

The [Harbor + OpenCode example](https://github.com/fw-ai/cookbook/tree/main/training/examples/rl/harbor_rl_opencode)
runs local Docker environments, records OpenCode model calls through a policy
adapter, builds a per-attempt token tree, and splits non-append token histories.
It is one integration pattern, not a required Harbor or OpenCode dependency.

For the loop itself, read
[Cookbook: Reinforcement Learning](/fine-tuning/training-api/cookbook/rl). For
detailed implementation choices, calibration checks, failure policy, and
session/cache guidance, read the [agentic RL skill reference](https://github.com/fw-ai/cookbook/blob/main/skills/fireworks-training/references/rl-agentic.md).
