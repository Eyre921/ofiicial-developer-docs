---
title: "Split traffic across deployments"
source: https://docs.together.ai/docs/dedicated-endpoints/split-traffic
path: docs/dedicated-endpoints/split-traffic
---

Run multiple deployments on one endpoint and split requests between them by weight.

Running more than one deployment on an endpoint lets you serve traffic across them for high availability, providing redundancy in case one of them fails. To split traffic between multiple deployments, list each with its relative weight.

A weight sets a deployment's share of traffic relative to its capacity: the actual share a deployment receives is proportional to its weight times its number of ready replicas.

<Tabs>
  <Tab title="CLI">
    Set each weight with `endpoints update --traffic-weight`, passing the deployment ID (`dep_...`). The CLI resolves its parent endpoint and preserves the other deployments' weights, so run it once per deployment:

    ```bash Shell theme={null}
    tg beta endpoints update dep_abc123 --traffic-weight 70
    tg beta endpoints update dep_def456 --traffic-weight 30
    ```

    <Note>
      When each deployment has the same number of ready replicas, the weights behave like a direct ratio. For example, with equal replica counts, the weights in the example above send roughly 70% of traffic to one deployment and 30% to the other.
    </Note>
  </Tab>

  <Tab title="Console">
    <ConsoleButton href="https://api.together.ai/endpoints">Endpoints</ConsoleButton>

    On a live endpoint's **Overview** tab, the status card shows the current traffic split. Select **Edit traffic weights** to set a weight for every deployment at once, then **Save changes**. At least one deployment must have a weight above 0.

    You can also set each deployment's **Traffic weight** in its **Deployment configuration** (open the deployment, select **Edit**, then **Save changes**), or set all weights together in the create form's **Traffic weights** card when you create an endpoint with more than one deployment.

    While a [rollout](/docs/dedicated-endpoints/rollouts) is active (including pending or paused), the **Overview** status card shows rollout progress instead of **Edit traffic weights**, and the **Traffic weight** field is disabled in each deployment's **Edit** dialog and in **New deployment**. Complete or cancel the rollout before editing weights manually.
  </Tab>
</Tabs>

Weights are relative ratios, not percentages, so they don't have to sum to any particular number: a split of `7` and `3` is equivalent to a split of `70` and `30`. But weight sets *relative capacity*, not a fixed percentage. Each weight must be non-negative and finite.

Two deployments with the same weight but different replica counts do not receive equal traffic. A deployment with weight `1` and two ready replicas draws the same traffic as one with weight `2` and a single ready replica.

A deployment receives no traffic if it has a weight of `0`, is absent from the split, or has zero ready replicas. Scaling a deployment to zero replicas takes it out of rotation even when it keeps a non-zero weight. Requests to an endpoint with no routable deployment return HTTP `400` with the error code `endpoint_not_configured`.

## Shift traffic with replica counts

Treat weights as a stable definition of each deployment's relative capacity, and shift traffic between deployments by changing their [replica counts](/docs/dedicated-endpoints/scaling#replica-bounds) rather than editing weights. Because a deployment's share tracks its ready replicas, scaling one deployment up (or another down) moves traffic without you having to recompute a set of weights.

To migrate traffic from one deployment to another on live traffic, use a [rollout](/docs/dedicated-endpoints/rollouts) instead of shifting the split by hand: it moves traffic in controlled steps, can gate each step on live metrics, and drains the source when it completes.

A deployment's weight is remembered when it scales to zero and reapplies automatically when it scales back up, so you don't need to re-add it to the split after a scale-down.

## Troubleshooting

* **Update traffic split returns `409` with `cannot update traffic_split while rollout ... is active`:** A [rollout](/docs/dedicated-endpoints/rollouts) in any non-terminal state (including pending or paused) owns the endpoint's traffic split. Complete, cancel, or delete the rollout before editing weights.
* **Update traffic split returns `400` with `the deployment is a shadow experiment target and cannot serve live traffic; remove the shadow target first`:** The deployment is registered as a target in an active [shadow experiment](/docs/dedicated-endpoints/shadow-experiments). Remove it from the experiment (or delete the experiment) before giving it a non-zero weight in the traffic split.

## Next steps

<CardGroup>
  <Card title="Route traffic" icon="route" href="/docs/dedicated-endpoints/route-traffic">
    Understand how an endpoint resolves each request to a deployment.
  </Card>

  <Card title="Configure autoscaling" icon="arrows-maximize" href="/docs/dedicated-endpoints/scaling">
    Set the replica bounds that shift traffic between deployments.
  </Card>

  <Card title="Run an A/B test" icon="test-pipe" href="/docs/dedicated-endpoints/ab-tests">
    Compare a candidate deployment against a baseline on live traffic.
  </Card>

  <Card title="Manage deployments" icon="server" href="/docs/dedicated-endpoints/manage">
    Create, poll, scale, stop, and delete deployments.
  </Card>
</CardGroup>
