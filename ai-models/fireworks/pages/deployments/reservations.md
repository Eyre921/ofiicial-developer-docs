---
title: "Reserved capacity"
source: https://docs.fireworks.ai/deployments/reservations
path: deployments/reservations
---

Enterprise accounts can purchase reserved capacity, typically with 1 year commitments. Reserved capacity has the following advantages over ordinary [on-demand deployments](/guides/ondemand-deployments):

* Guaranteed capacity
* Higher quotas
* Lower GPU-hour prices
* Pre-GA access to newer regions
* Pre-GA access to newest hardware

## Usage and billing

Consuming a reservation is done by creating a deployment that meets the reservation parameters. For example, suppose you have a reservation for 12 H100 GPUs and create two deployments, each using 8 H100 GPUs. While both deployments are running, 12 of the H100s will count towards using your reservation, while the excess 4 H100s will be metered and billed at the on-demand rate. Follow [deploying models on-demand](/guides/ondemand-deployments) to create a deployment.

When a reservation approaches its end time, ensure that you either renew your reservation or turn down a corresponding number of deployments, otherwise you may be billed for your usage at on-demand rates.

Reservations are invoiced separately from your on-demand usage, at a frequency determined by your reservation contract
(e.g. monthly, quarterly, or yearly).

> [!NOTE]
>
> Reserved capacity will always be billed until the reservation ends, regardless of whether the reservation is
> actively used.

## Training on a reservation

Trainers created with the Training SDK or the cookbook use a matching reservation on your account by default (`use_reservation=True`). A matching reservation is an active reservation for the trainer's GPU type.

* **No matching reservation:** the trainer uses shared capacity.
* **Reservation is full:** the trainer waits for reserved GPUs and doesn't fall back to shared capacity.
* **Shared capacity instead:** set `use_reservation=False`.
* **Placement limit:** a trainer that can't be placed within 48 hours fails, on a reservation or on shared capacity.
* **Quota:** trainers on a reservation still count against your [training GPU quota](/guides/quotas_usage/account-quotas#training-gpu-quota). A trainer that would go over quota fails when you create the trainer.

### Sharing a reservation with inference

By default, inference deployments on your account use reserved GPUs first and overflow to on-demand capacity. Trainers can't move standard (non-preemptible) inference deployments off a reservation, so if standard deployments fill the reservation, new trainers wait. Leave enough reserved GPUs free for the trainers you plan to run.

## Purchasing or renewing a reservation

To purchase a reservation or increase the size or duration of an existing reservation, contact your Fireworks account
manager. If you are a new, prospective customer, please reach out to our [sales team](https://fireworks.ai/company/contact-us).

## Viewing your reservations

To view your existing reservations, run:

```
firectl reservation list
```
