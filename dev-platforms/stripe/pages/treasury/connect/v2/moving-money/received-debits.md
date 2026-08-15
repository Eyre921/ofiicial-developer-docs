---
title: "Received debits"
source: https://docs.stripe.com/treasury/connect/v2/moving-money/received-debits.md
path: treasury/connect/v2/moving-money/received-debits
---

# Received debits

Authorize and manage third-party-initiated debits.

You can authorize third parties to debit funds from a financial account. Any transaction initiated after this authorization generates a [ReceivedDebit](https://docs.stripe.com/api/v2/money-management/received-debits/object.md?api-version=preview) object on the financial account, detailing how funds were sent and from what account, where possible. Stripe supports the following types of externally-initiated debits:

| Debit type | Description |
| --- | --- |
| Card spending | Spending money on a card through [Stripe Issuing](https://docs.stripe.com/issuing/purchases/transactions.md#transactions) |
| ACH debit1 | Pulling money from a financial account into an external account using ACH debits |
| Direct debit 2 | Pulling money from a financial account into an external account using direct debits |
| Top-up | Pulling money from a platform’s financial account into that platform’s Stripe payments balance using [top-ups](https://docs.stripe.com/treasury/connect/v2/moving-money/fund-a-financial-account.md#transfer-to-other-balance). |

1  Available in the US only. [Request access](https://docs.stripe.com/treasury/connect/v2/prebuilt-embedded-finance.md)

2  Available in the UK only. [Contact support to request access](https://support.stripe.com/contact)

## Enable received debits

Receiving ACH or Bacs direct debits requires the `money_manager.capabilities.received_debits.bank_accounts` capability. You can request this capability when [creating](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=preview) or [updating](https://docs.stripe.com/api/v2/core/accounts/update.md?api-version=preview) a connected account, then complete any requirements that Stripe returns. For details, see [money_manager capabilities](https://docs.stripe.com/treasury/connect/v2/account-management/connected-accounts.md#how-capabilities-work).

## Manage mandates
Available in: GB
When a third party initiates a debit from a financial account for the first time, Stripe creates a `ReceivedDebitMandate` representing authorization for the third party to initiate such debits and sends the `v2.money_management.received_debit_mandate.created` webhook event.

When you make API calls to manage mandates on behalf of a connected account, specify the connected account’s ID in the `Stripe-Account` header.

### Retrieve a mandate

You can retrieve the mandate using the ID from the webhook event to review the details of the debit request and validate its legitimacy.

```curl
curl https://api.stripe.com/v2/money_management/received_debit_mandates/{{RECEIVED_DEBIT_MANDATE_ID}} \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-07-29.preview" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}"
```

The response includes information about the initiating party. If you don’t cancel the mandate within one day of its creation, Stripe schedules the associated debit and sends the `v2.money_management.received_debit.scheduled` webhook event.

```json
{
  "id": "rdm_1234",
  "object": "v2.money_management.received_debit_mandate",
  "livemode": false,
  "financial_account": identifier("financialAccountId"),
  "type": "bank_transfer",
  "currency": "gbp",
  "bank_transfer": {
    "network": "bacs",
    "account_holder_name" : "Rocket Rides",
    "reference": "R/1234",
    "financial_address": "{{FINANCIAL_ADDRESS_ID}}"
  },
  "status": "active",
  "status_transitions": {
    "created_at": "2026-04-26T23:12:35.952Z",
    "activated_at": "2026-04-26T23:12:35.952Z"
  }
}
```

Any subsequent debits from the third party authorized by the mandate automatically generate a `ReceivedDebit` with `scheduled` status.

### Cancel a mandate

You can cancel a mandate to end debit authorization at any time. Canceling while an upcoming debit is still `scheduled` prevents that debit from completing and also prevents any future debits from the third party without a new mandate authorization.

> #### Individual debits
> 
> You can’t cancel or decline a scheduled received debit without canceling the mandate.

```curl
curl -X POST https://api.stripe.com/v2/money_management/received_debit_mandates/{{RECEIVED_DEBIT_MANDATE_ID}}/cancel \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-07-29.preview" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}"
```

The response confirms the mandate is `pending_cancellation`. After the cancellation completes, Stripe sends the `v2.money_management.received_debit_mandate.canceled` webhook event signaling the transition to `canceled`.

### List mandates

You can retrieve the set of mandates in place for a connected account. Use inline parameters, such as `statuses=active`, to filter the results.

```curl
curl https://api.stripe.com/v2/money_management/received_debit_mandates \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-07-29.preview" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}"
```

The result includes information about each mandate’s originator and when they created it, its status and type, and the financial account it applies to.

```json
{
  "data": [
    {
      "id": "rdm_test_61UxLhI8gPhKNsOwu16Ux87t0BE9ZVFsBHMMih6wSNPM",
      "object": "v2.money_management.received_debit_mandate",
      "bank_transfer": {
        "account_holder_name": "Test Originator",
        "financial_address": "{{FINANCIAL_ADDRESS_ID}}",
        "network": "bacs",
        "reference": "R/1234"
      },
      "created": "2026-06-30T09:14:00.475Z",
      "currency": "gbp",
      "financial_account": identifier("financialAccountId"),
      "status": "active",
      "status_details": null,
      "status_transitions": {
        "activated_at": "2026-06-30T09:14:00.475Z",
        "canceled_at": null,
        "created_at": "2026-06-30T09:14:00.475Z",
        "expired_at": null,
        "pending_cancellation_at": null
      },
      "type": "bank_transfer",
      "livemode": false
    }
  ]
}
```

## Monitor received debits
Available in: GB, US
After you authorize a third party’s mandate to directly debit a financial account, you can review received debits as they occur and dispute them if necessary. Listen for [events](https://docs.stripe.com/treasury/connect/v2/moving-money/received-debits.md#webhooks) related to received debit activity and handle them accordingly.

### Retrieve a received debit

[Retrieve a received debit](https://docs.stripe.com/api/v2/money-management/received-debits/retrieve.md?api-version=preview) by its ID to review details such as the `amount`, `status`, and `type` of transfer.

```curl
curl https://api.stripe.com/v2/money_management/received_debits/{{RECEIVED_DEBIT_ID}} \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

```json
{
  "id": "rd_123",
  "object": "v2.money_management.received_debit",
  "amount": {
    "value": 5000,
    "currency": "usd"
  },
  "bank_transfer": {
    "financial_address": "{{FINANCIAL_ADDRESS_ID}}",
    "payment_method_type": "us_bank_account",
    "statement_descriptor": "Some statement descriptor",
    "us_bank_account": {
      "bank_name": "US BANK NAME",
      "network": "ach",
      "routing_number": "110000000"
    }
  },
  "created": "2026-05-28T08:21:19.751Z",
  "description": "Some description",
  "dispute_details": {
    "debit_dispute": null,
    "dispute_window_closes_at": "2026-05-30T01:45:00.000Z"
  },
  "financial_account": identifier("financialAccountId"),
  "receipt_url": "https://payments.stripe.com/transaction_receipt/session_123",
  "status": "succeeded",
  "status_details": null,
  "status_transitions": {
    "canceled_at": null,
    "failed_at": null,
    "succeeded_at": "2026-05-28T08:21:19.751Z"
  },
  "type": "bank_transfer",
  "livemode": false
}
```

### List received debits

[List received debits](https://docs.stripe.com/api/v2/money-management/received-debits/list.md?api-version=preview) to review debit transactions for a financial account. Use parameters in the request to limit responses or filter results by created date. UK users can also filter by a specific `received_debit_mandate`.

```curl
curl https://api.stripe.com/v2/money_management/received_debits \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

## Dispute a received debit

> The Debit Disputes API doesn’t support disputing a Bacs GBP direct debit. You must [contact support](https://support.stripe.com/contact) to initiate these disputes.

You can dispute a `ReceivedDebit` within the dispute window specified in `dispute_details.dispute_window_closes_at`. Create a [DebitDispute](https://docs.stripe.com/api/v2/money-management/debit-disputes/object.md?api-version=preview) to initiate the dispute process.

```curl
curl -X POST https://api.stripe.com/v2/money_management/debit_disputes \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "received_debit": "{{RECEIVED_DEBIT_ID}}",
    "bank_transfer": {
        "reason": "unauthorized"
    }
  }'
```

### Retrieve a debit dispute

[Retrieve a debit dispute](https://docs.stripe.com/api/v2/money-management/debit-disputes/retrieve.md?api-version=preview) by its ID to check its status.

```curl
curl https://api.stripe.com/v2/money_management/debit_disputes/{{DEBIT_DISPUTE_ID}} \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

### List debit disputes

[List debit disputes](https://docs.stripe.com/api/v2/money-management/debit-disputes/list.md?api-version=preview) to review all disputes for a financial account. Use parameters in the request to limit responses or filter results by `status` or `financial_account`.

```curl
curl https://api.stripe.com/v2/money_management/debit_disputes \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

## Test received debits 

`ReceivedDebit` objects represent real direct debits initiated by a third party against a financial address. Because third parties initiate them, you can’t create them through the API in live mode.

Use the [debit test helper](https://docs.stripe.com/api/v2/money-management/financial-addresses/debit.md?api-version=preview) to simulate a `ReceivedDebit` in a sandbox so you can verify that your integration handles incoming debits correctly. You can trigger a failed debit by making sure the financial account has an insufficient balance for the test payment.

If you simulate a Bacs GBP debit, the helper also creates a `ReceivedDebitMandate`.

```curl
curl -X POST https://api.stripe.com/v2/money_management/test_helpers/financial_addresses/{{FINANCIAL_ADDRESS_ID}}/debit \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "amount": {
        "value": 1000,
        "currency": "usd"
    },
    "statement_descriptor": "my descriptor",
    "network": "ach"
  }'
```

A successful response confirms the simulation was accepted:

```json
{
  "object": "v2.money_management.financial_address_debit_simulation",
  "status": "accepted",
  "livemode": false
}
```

## Webhooks

Listen for the following `v2.money_management` events to track and handle status changes related to received debits and associated disputes.

| Event | Description |
| --- | --- |
| `received_debit_mandate.created` | A third party initiated a first debit and triggered creation of a mandate. |
| `received_debit_mandate.canceled` | A received debit mandate is canceled, preventing further debits authorized by that mandate. |
| `received_debit.scheduled` | A received debit is scheduled, but hasn’t debited the financial account yet. |
| `received_debit.pending` | A received debit related to Issuing card spend is pending, but hasn’t debited the financial account yet. |
| `received_debit.succeeded` | A received debit succeeds. |
| `received_debit.failed` | A received debit fails. |
| `received_debit.canceled` | A received debit related to Issuing card spend is canceled. |
| `received_debit.updated` | A received debit is updated. |
| `debit_dispute.submitted` | A debit dispute is submitted. |
| `debit_dispute.succeeded` | A debit dispute succeeds. |
| `debit_dispute.failed` | A debit dispute fails. |

