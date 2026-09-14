---
title: "Billing & pricing"
source: https://docs.together.ai/docs/gpu-clusters-billing
path: docs/gpu-clusters-billing
---

Understand billing, pricing, and lifecycle policies for GPU clusters.

## Billing

### Compute billing

Instant clusters offer two compute billing options: **reserved** and **on-demand**.

* **Reservations:** Credits are charged upfront or deducted for the full
  reserved duration once the cluster is provisioned. Any usage beyond the reserved
  capacity is billed at on-demand rates.
* **On-demand:** Pay only for the time your cluster is running, with no upfront
  commitment.

[View current GPU Cluster pricing](https://www.together.ai/pricing#gpu-clusters).

<Note>
  The regions API and `tg beta clusters list-regions` return region availability,
  supported instance types, and driver versions. They do not return pricing. See
  the [GPU cluster pricing table](https://www.together.ai/pricing#gpu-clusters) for
  current on-demand and reserved rates.
</Note>

### Storage billing

Storage is billed on a **pay-as-you-go** basis. [View current GPU Cluster
pricing](https://www.together.ai/pricing#gpu-clusters). You can freely increase
your storage volume size, with all usage billed at the same rate.
To decrease the storage volume size, contact your account team.

### Viewing usage and invoices

You can view your current usage anytime on the [Billing page in
Settings](https://api.together.ai/settings/organization/~current/billing). Each invoice includes a
detailed breakdown of reservation, burst, and on-demand usage for compute and
storage.

### Cluster and storage lifecycles

Clusters and storage volumes follow different lifecycle policies:

* **Compute clusters:** Clusters are automatically decommissioned when their
  reservation period ends. To extend a reservation, go to the cloud console **Cluster Details** view and then select the **Extend Reservation** button.
* **Storage volumes:** Storage volumes are persistent and remain available as
  long as your billing account is in good standing. They are not automatically
  deleted. Your data persists as long as you use the static PV Together provides.

### Running out of credits

When your credits are exhausted, resources behave differently depending on their
type:

* **Reserved compute:** Existing reservations remain active until their
  scheduled end date. Any additional on-demand capacity used to scale beyond the
  reservation is decommissioned.
* **Fully on-demand compute:** Clusters are first paused and then
  decommissioned if credits are not restored.
* **Storage volumes:** Access is revoked first, and the data is later
  decommissioned.

You will receive alerts before these actions take place. For questions or
assistance, contact your billing team.

### Access billing dashboard

1. Log into [api.together.ai](https://api.together.ai)
2. Navigate to [Settings > Billing](https://api.together.ai/settings/organization/~current/billing)
3. View current usage, credits, and invoices

### Invoice breakdown

Each invoice includes detailed line items for:

* **Reserved compute:** Upfront reservation charges.
* **On-demand compute:** Hourly burst capacity usage.
* **Storage:** Shared volume usage per TiB.
* **Usage period:** Exact timeframes for each charge.

## Lifecycle policies

### Cluster lifecycle

**Reserved clusters:**

* Automatically decommissioned when the reservation period ends with a
  24-hour email notification
* Extend directly from the cloud console in the cluster view or reach out to
  support

**On-demand clusters:**

* Run until manually terminated
* Can be stopped/started anytime
* No automatic decommissioning

### Storage lifecycle

**Shared volumes:**

* Persist independently of cluster lifecycle
* Remain available across cluster creation/deletion
* Must be manually deleted if no longer needed
* Data persists as long as you use static PersistentVolumes

## Best practices

### Cost optimization

* **Use reserved capacity** for predictable baseline workloads.
* **Add on-demand** only during burst periods.
* **Right-size storage:** Start small and scale as needed.
* **Monitor usage** regularly in the billing dashboard.
* **Delete unused storage** to avoid ongoing charges.

### Budget planning

* **Reserved capacity:** Calculate total cost upfront (GPUs × hours × rate).
* **On-demand capacity:** Estimate based on expected burst hours.
* **Storage:** Account for data growth over time.
* **Buffer:** Add 10-20% for unexpected scaling needs.

Reserved capacity offers significant discounts compared to on-demand for all
tiers.

[View current GPU Cluster pricing](https://www.together.ai/pricing#gpu-clusters)

## Common questions

### Can I get a refund for unused reservation time?

No, reservations are non-refundable. The full reservation period is charged
upfront and cannot be cancelled or partially refunded.

### What happens if I scale beyond my reservation?

Additional capacity is automatically billed at on-demand rates. You'll see
separate line items on your invoice for reserved and on-demand usage.

### How is storage billed if my cluster is terminated?

Storage is billed separately and continues to accrue charges even when no
cluster is using it. Delete unused volumes to stop storage charges.

### Are there data ingress or egress fees?

No, Together AI does not charge for data transfer into or out of your cluster, so you can move datasets, checkpoints, and results freely. You pay only for
compute and storage.

### Can I pause a cluster to save costs?

Reserved clusters cannot be paused. You're charged for the full reservation
period. On-demand clusters can be terminated and recreated later, but there's
no pause function.

### When does my reservation start?

The reservation period begins immediately when the cluster is provisioned and
reaches "Ready" status.

## Support

For billing questions or issues:

* Review your invoice in [Settings > Billing](https://api.together.ai/settings/organization/~current/billing)
* Contact your account team for reservation extensions
* Email [support@together.ai](mailto:support@together.ai) for billing assistance

## Next steps

<CardGroup>
  <Card title="Capacity types" icon="scale" href="/docs/gpu-clusters-capacity-types">
    Compare reserved and on-demand capacity and how each is billed.
  </Card>

  <Card title="GPU clusters quickstart" icon="rocket" href="/docs/gpu-clusters-quickstart">
    Create your first reserved or on-demand GPU cluster.
  </Card>

  <Card title="Manage clusters" icon="server" href="/docs/gpu-clusters-management">
    Deploy workloads, manage storage, and scale a running cluster.
  </Card>
</CardGroup>
