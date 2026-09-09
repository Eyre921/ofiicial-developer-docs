---
title: "Training cost estimator"
source: https://docs.fireworks.ai/fine-tuning/cost-estimator
path: fine-tuning/cost-estimator
---

Estimate Managed Training, compare Fireworks Serverless with Dedicated, or compare Fireworks Dedicated with Tinker

<Info>
  <ul>
    <li>
      Managed and Serverless are [priced per
      token](https://fireworks.ai/pricing#training-pricing).
    </li>

    <li>
      Dedicated is [priced per allocated GPU
      hour](https://fireworks.ai/pricing#on-demand-pricing).
    </li>
  </ul>
</Info>

<TrainingCostEstimator />

<Warning>
  <ul>
    <li>Planning estimates are not quotes.</li>

    <li>
      Managed estimates can be low when rendered-token inputs omit multi-turn
      unrolling. Dedicated compute floors can be low when sequences pack poorly.
    </li>

    <li>
      Dedicated shows a saturated compute floor. Allocated GPU time spent
      initializing the model, writing checkpoints, or idle can make real jobs
      cost more. Queue wait and pre-allocation provisioning are not billed.
    </li>
  </ul>
</Warning>

## Prepare inputs with the Training Skill

The [Fireworks Training Skill](/fine-tuning/agent/use-with-coding-agents)
prepares inputs and calculates Managed and Serverless estimates from published
rates. It can inspect a local dataset or an existing job and identify
assumptions. It does not calculate Dedicated numbers. Use this page for
Dedicated planning.

The Skill does not launch a job or authorize spend while estimating. Training
still requires the Skill's complete final plan and your explicit confirmation.

## Reinforcement learning

RL cost varies with rollout shape, concurrency, reward or verifier design,
training method, and evaluation workload. [Contact the Training
team](https://fireworks.ai/contact-training) for a tailored estimate.

To compare the rollout inference cost of multi-turn agentic RL, use the separate
[rollout cost comparison](/fine-tuning/multi-turn-cost-comparison). That page
does not estimate SFT or DPO training cost.
