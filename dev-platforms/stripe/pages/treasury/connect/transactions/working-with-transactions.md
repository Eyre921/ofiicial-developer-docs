---
title: "Working with Transactions"
source: https://docs.stripe.com/treasury/connect/transactions/working-with-transactions.md
path: treasury/connect/transactions/working-with-transactions
---

# Working with Transactions

Use transactions to track money movement on financial accounts.

Every movement of funds into or out of a financial account creates a [Transaction](https://docs.stripe.com/api/v2/money-management/transactions.md?api-version=preview) object. Transactions are the ledger entries for your financial accounts. They record what happened, how it affected the balance, and which resource caused the movement.

Use transactions to build account activity feeds, reconcile against your internal systems, and track money movement through your platform. You can’t create transactions directly. Stripe creates them automatically when flows such as [OutboundPayments](https://docs.stripe.com/api/v2/money-management/outbound-payments.md?api-version=preview), [OutboundTransfers](https://docs.stripe.com/api/v2/money-management/outbound-transfers.md?api-version=preview), [ReceivedCredits](https://docs.stripe.com/api/v2/money-management/received-credits.md?api-version=preview), and [ReceivedDebits](https://docs.stripe.com/api/v2/money-management/received-debits.md?api-version=preview) move money.

## Listen for transaction webhooks

Stripe sends the following event type for transactions:

| Event type | Trigger |
| --- | --- |
| `v2.money_management.transaction.created` | A flow creates a transaction on a financial account. |

This event is a thin event. The payload doesn’t contain the full transaction object. Instead, it provides a `related_object` with the transaction ID, type, and URL you can use to retrieve the full resource.

### Webhook payload example

For the transaction webhook payload schema and examples, see [Transaction event types](https://docs.stripe.com/api/v2/money-management/transactions/event-types.md?api-version=preview).

### Retrieve the transaction

Use the `related_object.url` from the event to retrieve the full transaction.

```curl
curl https://api.stripe.com/v2/money_management/transactions/trxn_7X8Y9Z0A1B2C3D4E \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-07-29.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

The response includes the transaction amount, balance impact, status, and flow that created the transaction. For the response schema and example, see [Retrieve a Transaction](https://docs.stripe.com/api/v2/money-management/transactions/retrieve.md?api-version=preview).

## Identify the source flow

Use the transaction’s `flow` property to identify the resource that caused the balance change. The `flow.type` property identifies the flow category, and the matching property contains the source resource ID.

For example, if `flow.type` is `outbound_payment`, then `flow.outbound_payment` contains the ID of the [OutboundPayment](https://docs.stripe.com/api/v2/money-management/outbound-payments/object.md?api-version=preview) that created the transaction.

Retrieve the OutboundPayment to get the full details of the flow that created the transaction, such as the recipient, amount, statement descriptor, delivery method, and status.

```curl
curl https://api.stripe.com/v2/money_management/outbound_payments/obp_3E4F5G6H7I8J9K0L \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-07-29.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

## Transaction statuses

A transaction progresses through the following statuses:

| Status | Meaning | Balance impact |
| --- | --- | --- |
| `pending` | The transaction is in progress. | `inbound_pending` or `outbound_pending` is non-zero. |
| `posted` | The transaction is complete. This is a terminal state. | Only `available` is non-zero. |
| `void` | The transaction was canceled or reversed before posting. This is a terminal state. | All balance impact values are zero. |

Stripe doesn’t add more entries to a transaction after it reaches `posted` or `void`.

