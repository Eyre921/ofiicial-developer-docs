---
title: "Pause payment collection"
source: https://docs.stripe.com/billing/subscriptions/pause-payment.md
path: billing/subscriptions/pause-payment
---

# Pause payment collection

Learn how to pause payment collection on subscriptions.

You can pause payment collection to temporarily offer a customer your services for free. This is sometimes called a grace period—for example, when a customer needs more time to pay or can’t pay for one or more billing periods.

When you pause payment collection, the *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)  remains `active` and *invoices* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) continue to generate, but Stripe doesn’t collect payment. Your customer retains access to the service during this time.

## Before you begin

- If you want to pause customer access to the service, pause payment collection, and also pause invoices, see [Pause subscriptions](https://docs.stripe.com/billing/subscriptions/pause.md) instead.
- If you want to permanently stop renewal, see [Cancel subscriptions](https://docs.stripe.com/billing/subscriptions/cancel.md) instead.
- Invoices created before you pause subscriptions continue to be [retried](https://docs.stripe.com/invoicing/automatic-collection.md) unless you [void](https://docs.stripe.com/api/invoices/void.md) them.

## Pause payment collection

Use the Dashboard or the API to pause payment collection.

You can choose to pause payment collection indefinitely or automatically resume payment collection at a specific time in the future. During the time that payment collection is paused, Stripe won’t send any upcoming invoice emails or webhooks for these invoices and the subscription’s status remains unchanged.

When you pause payment collection for a subscription, you have three options for how to handle invoices during the paused timeframe:

|  |
| **Keep invoices as drafts** (`keep_as_draft`) | - Invoices are created in `draft` status with `auto_advance` set to false.
- You can finalize and collect payment later.
  > If you have custom logic that finalizes invoices, you might need to disable or modify it so that it doesn’t conflict with these settings. |
| **Mark invoices uncollectible** (`mark_uncollectible`) | - Invoices are marked as uncollectible. No payment are collected for these periods. Stripe doesn’t send any upcoming invoice emails or webhooks for these invoices.
- Despite this pause, Stripe applies any existing customer balance to invoices. This behavior helps use available funds before we mark an invoice as uncollectible. If the invoice’s total is paid off entirely using customer balance, then the invoice’s status is set to `paid`. Otherwise, the invoice’s status is set to `uncollectible`. |
| **Void invoices** (`void`) | Invoices are voided. No record of charges is created for these periods. |

To pause payment collection for a subscription:

#### Dashboard

1. On the [Subscriptions](https://dashboard.stripe.com/subscriptions) page, select the subscription.

2. Click the overflow menu (⋯) and select **Pause payment collection**.

3. Choose the duration:

   - **Indefinite**: We keep payment collection paused until you resume it.
   - **Until a custom date**: We automatically resume payment collection on the date you choose.

4. Choose the Invoice behavior:

   - **Keep invoices as drafts**: Invoices are created as drafts. You can finalize and collect payment later.
   - **Mark invoices uncollectible**: Invoices are marked uncollectible. No payment is collected for these periods.
   - **Void invoices**: Invoices are voided. No record of charges is created for these periods.

5. Click **Pause**.

#### API

To pause payment collection for a subscription, [update the subscription](https://docs.stripe.com/api/subscriptions/update.md) and set `pause_collection[behavior]`. Optionally, set `pause_collection[resumes_at]` to automatically resume payment collection at a specific time.

```curl
curl https://api.stripe.com/v1/subscriptions/{{SUBSCRIPTION_ID}} \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "pause_collection[behavior]=keep_as_draft"
```

### pause_collection[behavior]

Choose how to handle invoices created while payment collection is paused:

- `keep_as_draft`: Keeps all invoices in draft status while collection is paused.
- `mark_uncollectible`: Marks all invoices as uncollectible while collection is paused.
- `void`: Voids all invoices while collection is paused.

### pause_collection[resumes_at]

A Unix timestamp after which the subscription resumes collecting payments.

If you don’t set `resumes_at`, payment collection remains paused until you unset `pause_collection`.

> If you pause a subscription that’s managed by a subscription schedule, scheduled updates still take effect. A subscription schedule phase transition doesn’t automatically remove `pause_collection` behavior that was set directly on the subscription.

## Resume payment collection 

You can resume payment collection at any time using the Dashboard or API for a subscription or for invoices kept as drafts.

### Resume collection from a subscription

#### Dashboard

To resume payment collection in the Dashboard:

1. On the [Subscriptions](https://dashboard.stripe.com/subscriptions) page, find the applicable subscription.
2. Click the overflow menu (⋯), and select **Resume payment collection**.

#### API

To resume payment collection, [update the subscription](https://docs.stripe.com/api/subscriptions/update.md) and unset `pause_collection`. You can unset individual keys by posting an empty value to them:

#### curl

```bash
curl https://api.stripe.com/v1/subscriptions/sub_GTbTiykEwMRog0 \
  -u <<YOUR_SECRET_KEY>>: \
  -d "pause_collection"= 
```

### Collect payment on draft invoices

After you resume payment collection from a subscription, set `auto_advance=true` on each draft invoice. If you don’t have the invoice IDs, look them up using the subscription ID with `status=draft` as a filter.

#### Dashboard

After you resume payment collection from a subscription, for each draft invoice:

1. Go to the [Invoices page](https://dashboard.stripe.com/invoices/) in the Dashboard, and click the invoice to see its details page.
2. Click the overflow menu (⋯).
3. Click **Turn on automatic collection**. This changes the `auto_advance` property on the invoice to `true`.

#### API

Retrieve the draft invoices for the subscription:

```curl
curl -G https://api.stripe.com/v1/invoices \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "subscription={{SUBSCRIPTION_ID}}" \
  -d status=draft
```

Then, for each draft invoice, set `auto_advance` to `true`:

```curl
curl https://api.stripe.com/v1/invoices/{{INVOICE_ID}} \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d auto_advance=true
```

## See also

- [Pause subscriptions](https://docs.stripe.com/billing/subscriptions/pause.md)

