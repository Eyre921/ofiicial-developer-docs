---
title: "Training Overview"
source: https://docs.fireworks.ai/fine-tuning/finetuning-intro
path: fine-tuning/finetuning-intro
---

Fireworks helps you fine-tune models to improve quality and performance for your product use cases, without the burden of building & maintaining your own training infrastructure.

<Info>
  **Coming from OpenAI?** Fireworks uses the same **OpenAI-compatible chat completion format** for training data — the same `messages` array with `role`, `content`, `tool_calls`, and `weight` fields. You can use your existing SFT datasets with no conversion required. See the [SFT dataset format](/fine-tuning/fine-tuning-models#fine-tuning-a-model-using-sft) for the full schema and examples.
</Info>

## Before managed or dedicated training: account tier and GPU quota

Managed jobs and dedicated Training API runs need training GPU quota, granted automatically by [spending tier](/guides/quotas_usage/account-quotas#training-gpu-quota):

| Tier              | How to reach it                          | B200 / B300 (Blackwell) | H200 | H100 / A100 |
| ----------------- | ---------------------------------------- | :---------------------: | :--: | :---------: |
| No payment method | —                                        |            0            |   0  |      0      |
| Tier 1            | Valid payment method and billing profile |            0            |  16  |      8      |
| Tier 2            | Spend or add \$50 in credits             |            16           |  16  |      16     |
| Tier 3            | Spend or add \$500 in credits            |            24           |  24  |      24     |
| Tier 4            | Spend or add \$5,000 in credits          |            32           |  32  |      32     |

Check your quota with the Fireworks CLI (`firectl quota list`). A job rejected with HTTP 429 `quota_exceeded` (sometimes a `403` on the job poll) is a tier issue, not a dataset/config problem.

[Serverless Training](/fine-tuning/training-api/serverless) uses a shared pool with its own model, concurrency, and rate limits instead of dedicated training GPU quota.

<Note>
  Need more training quota than your tier allows? [Reach out for enterprise support](https://fireworks.ai/contact-training) and we'll help size the right allocation for your workload.
</Note>

## Start here

Use [Choose a Training Path](/fine-tuning/choose-training-path) to select the right workflow. That page owns the detailed workflow, infrastructure, and interface decisions.

<CardGroup>
  <Card title="Choose a training path" icon="route" href="/fine-tuning/choose-training-path">
    Compare workflows, infrastructure, and interfaces.
  </Card>

  <Card title="Agent Skills" icon="robot" href="/fine-tuning/agent/use-with-coding-agents">
    Configure, run, and troubleshoot training with your agent.
  </Card>
</CardGroup>

For a side-by-side comparison of SFT, DPO, and RL — the data each needs and what each is good for — see [Choose a method](/fine-tuning/choose-training-path#choose-a-method).

For custom losses, rollouts, per-step control, or algorithm research, continue to the [Training API overview](/fine-tuning/training-api/introduction).
