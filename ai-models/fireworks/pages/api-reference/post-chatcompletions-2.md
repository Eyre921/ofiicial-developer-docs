---
title: "Create Chat Completion"
source: https://docs.fireworks.ai/api-reference/post-chatcompletions
path: api-reference/post-chatcompletions
---

post /v1/chat/completions
Create a completion for the provided prompt and parameters.

For RL / agent rollouts, Fireworks inference exposes additional
rollout-specific features:
[`x-session-affinity` and `x-multi-turn-session-id`](https://docs.fireworks.ai/guides/rollout-inference#session-affinity)
for multi-turn trajectories, and
[MoE Router Replay (R3)](https://docs.fireworks.ai/guides/rollout-inference#moe-router-replay)
for MoE expert tracing during rollouts.
