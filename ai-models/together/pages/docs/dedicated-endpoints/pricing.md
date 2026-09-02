---
title: "Pricing"
source: https://docs.together.ai/docs/dedicated-endpoints/pricing
path: docs/dedicated-endpoints/pricing
---

Billing and pricing details for dedicated model inference.

Dedicated model inference (DMI) bills based on the hardware your deployments run on, regardless of model or request volume:

* **Billed by the minute:** A deployment bills for as long as it runs, not per token or per request. The model you serve affects cost only through the hardware it needs (a larger model requires more or bigger GPUs), not through how many tokens or requests you push through it.
* **Per replica:** Each running replica bills independently. A deployment running three replicas bills three times the single-replica rate.
* **Only ready replicas:** A replica bills only while it's ready and able to serve traffic. Time spent provisioning or [cold-starting](/docs/dedicated-endpoints/concepts#cold-starts) isn't billed, and neither is a replica that isn't ready, such as while a deployment is [`DEGRADED`](/docs/dedicated-endpoints/manage#deployment-states).
* **Stops when scaled down:** A replica stops billing as soon as it scales down. A deployment scaled to zero replicas, or stopped, costs nothing.

Because cost tracks running replicas, you keep your cost down by running only as many replicas as you need for your workload, and by stopping a deployment or setting its [replica bounds](/docs/dedicated-endpoints/scaling#replica-bounds) to zero when you don't need it. Endpoints run until you stop them; there is no automatic idle shutdown at launch. See [Configure autoscaling](/docs/dedicated-endpoints/scaling) for details.

## Supported hardware

The following table lists the available hardware types. Where a single-GPU per-hour price is listed, multi-GPU configs cost proportionally more (a four-GPU config costs four times the single-GPU rate). For hardware without a listed price, [contact sales](https://www.together.ai/contact-sales) for a quote.

| GPU         | Hardware ID            | Cost/hour                                              |
| ----------- | ---------------------- | ------------------------------------------------------ |
| H100 80GB   | `1xnvidia-h100-80gb`   | \$3.99                                                 |
| H200 141GB  | `1xnvidia-h200-141gb`  | [Contact sales](https://www.together.ai/contact-sales) |
| B200 180GB  | `1xnvidia-b200-180gb`  | \$8.99                                                 |
| GB300 280GB | `1xnvidia-gb300-280gb` | [Contact sales](https://www.together.ai/contact-sales) |
| B300 280GB  | `1xnvidia-b300-280gb`  | [Contact sales](https://www.together.ai/contact-sales) |

Hardware and GPU count are set by the [config](/docs/dedicated-endpoints/configs) you select when you create a deployment.

## How scaling affects cost

Billing is proportional to the number of ready replicas across all deployments in your project, which you can track as `status.readyReplicas` when you [poll deployment status](/docs/dedicated-endpoints/manage#poll-deployment-status). For a given deployment, you control how much it costs with its [replica bounds](/docs/dedicated-endpoints/scaling#replica-bounds), and by stopping it when you don't need it:

* **`minReplicas`:** This sets the floor for a deployment's cost. These replicas will run and bill continuously, so set it to the lowest count that meets your latency target.
* **`maxReplicas`:** This sets the ceiling for a deployment's cost. The deployment never bills for more than this many replicas, so set it to a high enough count to handle your peak traffic.
* **Stop when idle:** [Stop a deployment](/docs/dedicated-endpoints/manage#stop-a-deployment) or set both replica bounds to zero when you don't need it. It bills nothing while stopped, and you restart it (requiring a [cold start](/docs/dedicated-endpoints/concepts#cold-starts)) by raising the replica bounds.

See [Configure autoscaling](/docs/dedicated-endpoints/scaling) for more details.

## On-demand vs. reserved

Dedicated model inference offers two pricing options:

* **On-demand:** Pay the per-minute rate for as long as your replicas run, with no commitment. Capacity scales up and down within your replica bounds. Best for variable traffic and prototyping.
* **Reserved:** Commit to capacity for a set term at a lower effective rate, with guaranteed hardware availability. Best for steady, predictable production traffic. To set up reserved capacity, [contact us](https://www.together.ai/forms/monthly-reserved).

## DMI vs. serverless

[Serverless models](/docs/serverless/overview) bill per token, while dedicated model inference bills per-minute for each running replica, regardless of how many tokens you push through. When comparing the two, consider how busy a replica would be for your workload:

1. Work out your DMI cost from the per-minute rate: A single H100 replica at \$5.49/hour costs about \$132/day, or roughly \$3,950 over a 30-day month, if running continuously.
2. Estimate your serverless cost at the same volume: Monthly tokens multiplied by the model's serverless per-token price.

**DMI is usually cheaper** when a replica would stay busy most of the day. The fixed per-minute cost is spread across high throughput, and you also get reserved capacity and predictable latency.

**Serverless is usually cheaper** when traffic is low or bursty enough such that a dedicated replica would be sitting idle most of the time. You pay only for the tokens you use, so you lose nothing during an idle window.

Stopping a deployment when it's idle narrows the gap, but won't help if your deployment receives steady low-volume traffic around the clock.

## Next steps

<CardGroup>
  <Card title="Manage deployments" icon="tool" href="/docs/dedicated-endpoints/manage">
    Create and manage deployments to serve your model.
  </Card>

  <Card title="Configure autoscaling" icon="arrows-maximize" href="/docs/dedicated-endpoints/scaling">
    Control cost with replica bounds.
  </Card>
</CardGroup>
