---
title: "Test Stripe Invoicing"
source: https://docs.stripe.com/invoicing/integration/testing.md
path: invoicing/integration/testing
---

# Test Stripe Invoicing

Learn how to test your Invoicing integration.

Use the following scenarios to test your Invoicing integration before you go live.

## Test webhook notifications 

Stripe triggers event notifications when an *invoice’s* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) [status changes](https://docs.stripe.com/invoicing/integration/workflow-transitions.md#status-transitions-endpoints). Use either of the following methods to test your webhook integration:

- Use the [Stripe CLI](https://docs.stripe.com/cli.md) to trigger event notifications. To get started, install the Stripe CLI and log in to your Stripe account. For a complete list of events, see [invoice event types](https://docs.stripe.com/api/events/types.md#event_types-invoice.created).

- Use the Dashboard to [create invoices](https://dashboard.stripe.com/test/invoices/create) in a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes).

To add a webhook endpoint and view the events it receives, go to the [Webhooks tab](https://dashboard.stripe.com/workbench/webhooks) in [Workbench](https://docs.stripe.com/workbench.md). Verify webhook signatures to confirm that events came from Stripe. See [verify events](https://docs.stripe.com/webhooks.md#verify-events).

### Test events with fake data 

When you use the Stripe CLI to trigger events, your server receives event notifications as they arrive. This lets you test your webhook integration directly, without complicating factors such as network tunnels or firewalls. Events that you trigger with the Stripe CLI contain fake data that doesn’t correspond to your invoice information.

### Test events with real data 

To test with real data, create invoices for existing customers in a sandbox and handle the corresponding events. This is the most reliable way to test webhook notifications.

## Test payment failures 

To trigger invoice payment failures, use the test card numbers in [Declined payments](https://docs.stripe.com/testing.md#declined-payments). To simulate a declined payment for a card that’s successfully attached to a customer, set `4000 0000 0000 0341` as the customer’s default payment method.

Depending on your [retry settings](https://docs.stripe.com/invoicing/automatic-collection.md), the first retry attempt might not happen for a day or more. To test a successful retry, update the customer’s payment method to a working test card during this waiting period.

## Test payments that require 3D Secure 

To simulate 3D Secure authentication for invoice payments, use the `4000 0027 6000 3184` [regulatory test card](https://docs.stripe.com/testing.md#regulatory-cards). When Stripe requests 3D Secure authentication, use the dialog that opens to complete or fail authentication. If authentication succeeds, the invoice is paid. If authentication fails, the payment attempt fails and the invoice remains `open`.

## Test bank transfer payments 

To test manual payments on invoices through bank transfers:

1. In a sandbox, create an invoice with `collection_method` set to `send_invoice` and `payment_settings[payment_method_types]` set to `[customer_balance]`.
2. Find the invoice in the Dashboard and click **Send**. Stripe generates a unique virtual bank account number for the customer.
3. Use the [Customer Balance Funding Instructions API](https://docs.stripe.com/payments/customer-balance/funding-instructions.md#create-funding-instructions) to retrieve the customer’s virtual bank account number. You can also find the virtual bank account details on the hosted invoice page and in the invoice PDF.

## Test customer tax ID verification 

Use these magic tax IDs to trigger certain verification conditions in testing environments. The tax ID type must be the Australian Business Number (ABN), EU VAT Number, or UK Value-Added-Tax (GB VAT) number.

| Number | Type |
| --- | --- |
| `000000000` | Successful verification |
| `111111111` | Unsuccessful verification |
| `222222222` | Verification remains pending indefinitely |

