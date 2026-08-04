---
title: "Choose Serverless or Dedicated Training"
source: https://docs.fireworks.ai/fine-tuning/training-api/choose-infrastructure
path: fine-tuning/training-api/choose-infrastructure
---

Choose the Training API infrastructure that fits your model, method, workload, and cost profile.

The Training API uses the same Tinker-compatible primitives on two infrastructure paths. Choose the path before adapting a cookbook recipe.

<CardGroup>
  <Card title="Serverless Training" icon="bolt" href="/fine-tuning/training-api/serverless">
    Attach to a shared pooled trainer. There is no trainer or rollout deployment to provision.
  </Card>

  <Card title="Dedicated Training" icon="server" href="/fine-tuning/training-api/dedicated">
    Provision trainer and deployment resources for your run, with broader model and method support.
  </Card>
</CardGroup>

## Quick decision

<div aria-label="Decision guide comparing serverless and dedicated Training API infrastructure">
  <div>
    <strong>Start with Serverless Training</strong>

    <div>
      The model is supported, LoRA SFT or RL covers the task, and you want pooled compute with per-token billing.
    </div>
  </div>

  <div>
    <strong>Choose Dedicated Training</strong>

    <div>
      You need full-parameter training, DPO, explicit resume or deployment control, or sustained provisioned compute.
    </div>
  </div>
</div>

## Comparison

| Dimension         | Serverless                                                                            | Dedicated                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Provisioning      | Shared pooled trainer; no trainer or sampler deployment creation                      | SDK provisions trainer and deployment resources                                               |
| Billing           | Per token; no idle GPU charge                                                         | Time-based trainer and deployment billing                                                     |
| Parameter mode    | LoRA only                                                                             | LoRA and full-parameter                                                                       |
| Methods           | SFT and RL on the supported serverless surface                                        | SFT, DPO, ORPO, RL, distillation, and custom loops supported by the selected shape and recipe |
| Models            | [Serverless-enabled models](/fine-tuning/models)                                      | Models with an enabled dedicated training shape                                               |
| Capacity          | Shared pool and per-account limits                                                    | Resources allocated to the run, subject to account quota and platform availability            |
| Checkpoint resume | In-run and cross-run train-state resume; session-scoped checkpoint list and promotion | Explicit checkpoint, reconnect, promotion, and deployment lifecycle                           |
| Sampling          | In-session sampler, no deployment to create                                           | SDK-managed rollout or evaluation deployment                                                  |
| Teardown          | Session lifecycle is managed by the service                                           | You must close trainers and delete or scale down deployments                                  |
| Best fit          | Fast LoRA experiments and first RL iterations                                         | Full-parameter work, DPO, sustained RL, larger workloads, explicit lifecycle control          |

Always verify current models, limits, prices, and feature status in the [Serverless Training](/fine-tuning/training-api/serverless) and [Dedicated Training](/fine-tuning/training-api/dedicated) pages before launch.

## Choose serverless when

* The base model is marked as serverless-enabled on [Models](/fine-tuning/models).
* LoRA SFT or RL covers the task.
* You want to start without provisioning trainer or inference resources.
* Per-token billing fits a small or bursty experiment.
* In-session sampling is sufficient.

## Choose dedicated when

* You need full-parameter training, DPO, ORPO, distillation, or a model not on the serverless list.
* You need explicit trainer, rollout deployment, checkpoint, reconnect, or promotion control.
* You need sustained throughput or long-running rollouts.
* A highly utilized time-based deployment is more economical for the workload.
* You need to serve or evaluate through a dedicated deployment during training.

## The interface is a separate choice

Serverless and dedicated describe **how training compute is provided**. They are not separate coding-agent modes.

You can ask the [Fireworks training skill](/fine-tuning/agent/use-with-coding-agents) to choose and run either path. You can also run a Cookbook recipe with the Python SDK. Managed fine-tuning is a separate workflow for standard jobs where Fireworks owns the training loop.

## Next steps

* [Run Serverless Training](/fine-tuning/training-api/serverless)
* [Run Dedicated Training](/fine-tuning/training-api/dedicated)
* [Training API introduction](/fine-tuning/training-api/introduction)
* [Cookbook recipes](/fine-tuning/training-api/cookbook/overview)
* [Compare multi-turn costs](/fine-tuning/multi-turn-cost-comparison)
