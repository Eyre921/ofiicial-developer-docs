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

When a reservation approaches its end time, ensure that you either renew your reservation or turn down a corresponding number of deployments, otherwise you may be billed at for your usage at on-demand rates.

Reservations are invoiced separately from your on-demand usage, at a frequency determined by your reservation contract
(e.g. monthly, quarterly, or yearly).

<Note>Reserved capacity will always be billed until the reservation ends, regardless of whether the reservation is
actively used.</Note>

## Purchasing or renewing a reservation

To purchase a reservation or increase the size or duration of an existing reservation, contact your Fireworks account
manager. If you are a new, prospective customer, please reach out to our [sales team](https://fireworks.ai/company/contact-us).

## Viewing your reservations

To view your existing reservations, run:

```
firectl reservation list
```
