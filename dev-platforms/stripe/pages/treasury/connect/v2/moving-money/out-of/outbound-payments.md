---
title: "Send money to recipients and financial accounts you don't own"
source: https://docs.stripe.com/treasury/connect/v2/moving-money/out-of/outbound-payments.md
path: treasury/connect/v2/moving-money/out-of/outbound-payments
---

# Send money to recipients and financial accounts you don't own

Learn how to create outbound payments to move money out of financial accounts to third parties.

[OutboundPayment](https://docs.stripe.com/api/v2/money-management/outbound-payments/object.md?api-version=preview) objects represent push-based transfers from:

- A platform’s financial accounts to a financial account owned by connected accounts.
- Financial accounts owned by one connected account to a financial account owned by another connected account under the same platform.
- Financial accounts of a connected account to one of the platform’s financial accounts.
- Financial accounts of a connected accounts any third party recipient.

> To move funds between financial accounts and other accounts owned by the same entity, use [OutboundTransfers](https://docs.stripe.com/treasury/connect/v2/moving-money/out-of/outbound-transfers.md) instead.

#### Source currency - GBP

You can create the following types of `OutboundPayment`:

| From a financial account to: | Payout method | Recipient capability | Expected arrival time |
| --- | --- | --- | --- |
| Another financial account under a different account | — | — | Immediate |
| An external UK recipient (third party payout) | Faster Payments (FPS) | `bank_accounts.local` | Immediate |
| An external recipient (third party payout) with FX | Cross-border | Varies by country | Typically 1-7 days (varies by country) |

## Move money from a platform to connected account

To move funds from your platform’s financial account to a connected account’s financial account, create an OutboundPayment without the `Stripe-Context` header:

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_payments \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "gbp"
    },
    "to": {
        "payout_method": "{{CONNECTED_ACCOUNT_FINANCIAL_ACCOUNT_ID}}",
        "recipient": "{{CONNECTED_ACCOUNT_ID}}",
        "currency": "gbp"
    },
    "amount": {
        "value": 30000,
        "currency": "gbp"
    },
    "description": "Funds transfer from platform to connected account"
  }'
```

> When moving funds from your platform’s financial account, don’t include the `Stripe-Context` header. The platform financial account is automatically used as the source of funds.

## Move money between connected accounts’ financial accounts

Use [Outbound Payments](https://docs.stripe.com/api/v2/money-management/outbound-payments/create.md?api-version=preview) to create an outbound payment:

This example creates an outbound payment between two financial accounts of different connected accounts (under your platform). Set the `recipient_notification.setting` to `none` so that a Stripe notification isn’t sent to the recipient.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_payments \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "gbp"
    },
    "to": {
        "payout_method": "{{RECIPIENT_FINANCIAL_ACCOUNT_ID}}",
        "recipient": "{{RECIPIENT_CONNECTED_ACCOUNT_ID}}",
        "currency": "gbp"
    },
    "amount": {
        "value": 30000,
        "currency": "gbp"
    },
    "description": "Payout to a financial account of another connected account",
    "recipient_notification": {
        "setting": "none"
    }
  }'
```

> To move funds from your platform’s financial account to a connected account’s financial account, don’t specify the `Stripe-Context` header.

Use a similar request to move funds from your connected account’s financial account to your platform’s financial account.

## Create an OutboundPayment to a third party recipient

To pay a third party recipient, first create and onboard a [recipient-configured connected account](https://docs.stripe.com/treasury/connect/v2/build-an-integration.md#create-a-recipient) to generate an account ID and a payout method ID that you need for the transaction.

Then [create an outbound payment](https://docs.stripe.com/api/v2/money-management/outbound-payments/create.md?api-version=preview).

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_payments \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "gbp"
    },
    "to": {
        "recipient": "{{RECIPIENTACCOUNTID_ID}}",
        "payout_method": "{{RECIPIENTPAYOUTMETHODID_ID}}",
        "currency": "gbp"
    },
    "amount": {
        "value": 30000,
        "currency": "gbp"
    },
    "description": "Streamer earnings"
  }'
```

## Send an OutboundPayment cross-border or to a recipient in a different currency

Stripe supports sending money in local currency to recipients in many different countries. Before making a cross-border outbound payment, review:

- [Supported countries and currencies](https://docs.stripe.com/global-payouts/send-money.md?dashboard-or-api=api#payout-amounts) for country-specific information about currencies and minimum payment amounts
- [Recipient payout methods](https://docs.stripe.com/treasury/connect/v2/account-management/connected-accounts.md#recipient-payout-methods)

> To get access to cross-border Outbound Payments to external bank accounts, contact [treasury-support@stripe.com](mailto:treasury-support@stripe.com). Cross-border transfers between financial accounts are enabled by default.

Create an [`OutboundPaymentQuote`](https://docs.stripe.com/api/v2/money-management/outbound-payment-quotes/object.md?api-version=preview) to understand applicable FX and fees before making a cross-border outbound payment.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_payment_quotes \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "gbp"
    },
    "to": {
        "recipient": "{{RECIPIENTACCOUNTID_ID}}",
        "payout_method": "{{RECIPIENTPAYOUTMETHODID_ID}}",
        "currency": "eur"
    },
    "amount": {
        "value": 30000,
        "currency": "gbp"
    }
  }'
```

The response contains the estimated fees, currency exchange rate, and payout amounts prior to creating the payment. The FX quote is valid for 5 minutes. If you don’t create an outbound payment within 5 minutes, you need to request a new quote.

```json
{
  "id": "{{OUTBOUND_PAYMENT_QUOTE_ID}}",
  "object": "v2.money_management.outbound_payment_quote",
  "amount": {
    "value": 30000,
    "currency": "gbp"
  },
  "created": "2025-09-09T09:21:17.201Z",
  "delivery_options": null,
  "estimated_fees": [
    {
      "amount": {
        "value": 0,
        "currency": "gbp"
      },
      "type": "cross_border_payout_fee"
    },
    {
      "amount": {
        "value": 300,
        "currency": "gbp"
      },
      "type": "standard_payout_fee"
    },
    {
      "amount": {
        "value": 100,
        "currency": "gbp"
      },
      "type": "foreign_exchange_fee"
    }
  ],
  "from": {
    "debited": {
      "value": 30000,
      "currency": "gbp"
    },
    "financial_account": "{{FINANCIAL_ACCOUNT_ID}}"
  },
  "fx_quote": {
    "lock_duration": "five_minutes",
    "lock_expires_at": "2025-09-09T09:26:17.000Z",
    "lock_status": "active",
    "rates": {
      "gbp": {
        "exchange_rate": "1.133"
      }
    },
    "to_currency": "eur"
  },
  "to": {
    "credited": {
      "value": 34443,
      "currency": "eur"
    },
    "payout_method": "{{RECIPIENT_PAYOUT_METHOD_ID}}",
    "recipient": "{{RECIPIENT_ACCOUNT_ID}}"
  },
  "livemode": false
}
```

When creating the payout with [OutboundPayment](https://docs.stripe.com/api/v2/money-management/outbound-payments/create.md?api-version=preview), provide the quote to acknowledge the fees associated with the payout.

At this point, you have all the necessary pieces to pay the recipient from the connected account’s financial account using the [Create an OutboundPayment](https://docs.stripe.com/api/v2/money-management/outbound-payments/create.md?api-version=preview) endpoint.

See [Global payments testing](https://docs.stripe.com/global-payouts/testing.md#test-bank-account-numbers) for test payment accounts you can use to simulate successful and failed payments.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_payments \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "gbp"
    },
    "to": {
        "recipient": "{{RECIPIENTACCOUNTID_ID}}",
        "payout_method": "{{RECIPIENTPAYOUTMETHODID_ID}}",
        "currency": "eur"
    },
    "amount": {
        "value": 30000,
        "currency": "gbp"
    },
    "outbound_payment_quote": "{{OUTBOUNDPAYMENTQUOTEID_ID}}"
  }'
```

## See also

- [Build an integration](https://docs.stripe.com/treasury/connect/v2/build-an-integration.md)
- [Financial accounts](https://docs.stripe.com/treasury/connect/v2/account-management/financial-accounts.md)
- [Connected accounts](https://docs.stripe.com/treasury/connect/v2/account-management/connected-accounts.md)

