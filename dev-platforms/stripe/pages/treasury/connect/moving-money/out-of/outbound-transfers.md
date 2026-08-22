---
title: "Transfer money between same-owner accounts"
source: https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-transfers.md
path: treasury/connect/moving-money/out-of/outbound-transfers
---

# Transfer money between same-owner accounts

Learn how to transfer money from financial accounts to other accounts owned by the same business.

An [OutboundTransfer](https://docs.stripe.com/api/v2/money-management/outbound-transfers/object.md?api-version=preview) object facilitates money movement between financial accounts owned by the same entity (either the same connected account or the same platform). Use outbound transfers to send funds from a financial account to an external bank account or to move money between multiple financial accounts owned by the same entity.

> To move funds between financial accounts that different entities own (for example, from your platform financial account to a connected account’s financial account, or between two different connected accounts), use [OutboundPayment](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-payments.md) instead.

#### Source currency - GBP

You can create the following types of `OutboundTransfer`:

| From a financial account to: | Payout method | Recipient capability | Expected arrival time |
| --- | --- | --- | --- |
| Another financial account belonging to the same account | — | — | Immediate |
| External UK bank account belonging to the same account | Faster Payments (FPS) | `bank_accounts.local` | Immediate |

#### Source currency - EUR [Private preview]
Available in: AT, BE, HR, CY, EE, FI, FR, DE, GR, IE, IT, LV, LT, LU, MT, NL, PT, SK, SI, ES
You can create the following types of `OutboundTransfer`:

| From the connected account’s financial account to: | Payout method | Recipient capability | Expected arrival time |
| --- | --- | --- | --- |
| Another financial account belonging to the same account | — | — | Immediate |
| External Eurozone bank account belonging to the same account | SEPA | `bank_accounts.local` | Typically 1 business day |

#### Source currency - USD [Private preview]
Available in: US
You can create the following types of `OutboundTransfer`:

| From a financial account to: | Payout method | Recipient capability | Expected arrival time |
| --- | --- | --- | --- |
| Another financial account belonging to the same account | — | — | Immediate |
| External US bank account belonging to the same connected account user | Automated Clearing House (ACH) | `bank_accounts.local` | Typically 2-3 business days |
| Wire | `bank_accounts.wire` | Typically 1 business day |
| Instant | `card` | Immediate |

## Move money from one financial account to another financial account

Using an outbound transfer, you can move money between two financial accounts owned by the same connected account. For two financial accounts owned by the platform, exclude the `Stripe-Context` header specifying the connected account ID.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_transfers \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "to": {
        "payout_method": "{{SECOND_FINANCIAL_ACCOUNT_ID}}",
        "currency": "usd"
    },
    "amount": {
        "value": 30000,
        "currency": "usd"
    },
    "description": "Payout to own bank account"
  }'
```

## Move money from financial account to a bank account

To create an outbound transfer to a bank account your connected account owns, first create a [FinancialAddress](https://docs.stripe.com/api/v2/money-management/financial-addresses/object.md?api-version=preview) for the financial account:

Create a financial address when you need to receive funds into a financial account or enable outbound payments to third parties. Specify the `type` corresponding to the country of the financial account to make sure we provision the correct [address credentials](https://docs.stripe.com/api/v2/money-management/financial-addresses/object.md?api-version=preview#v2_financial_address_object-credentials) (such as a US routing number, British sort code, or EU IBAN).

```curl
curl -X POST https://api.stripe.com/v2/money_management/financial_addresses \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "financial_account": "{{FINANCIALACCOUNTID_ID}}",
    "type": "us_bank_account"
  }'
```

If successful, the response provides the ID for the financial address, along with the relevant credentials for the jurisdiction.

#### US

```json
{
  "id": "{{FINANCIAL_ADDRESS_ID}}",
  "object": "v2.money_management.financial_address",
  "credentials": {
    "type": "us_bank_account",
    "us_bank_account": {
      "account_number": "123456890",
      "routing_number": "110000000",
      "bic": "TSTEZ122",
      "bank_name": "STRIPE TEST BANK",
      "last4": "6890"
    }
  },
  "status": "active",
  "financial_account": "fa_6504m3x1JLdhVIIIT1A16O0lef0dSQgZ0EhGyZsQCXQ28m",
  "created": "2023-03-30T17:32:06.665Z",
  "currency": "usd"
}
```

#### UK

```json
{
  "id": "{{FINANCIAL_ADDRESS_ID}}",
  "object": "v2.money_management.financial_address",
  "created": "2025-06-19T19:17:54.607Z",
  "credentials": {
    "type": "gb_bank_account",
    "gb_bank_account": {
      "account_holder_name": "Jenny Rosen",
      "account_number": "123456890",
      "last4": "6890",
      "sort_code": "12-34-56"
    }
  },
  "currency": "gbp",
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
  "settlement_currency": "gbp",
  "status": "pending",
  "livemode": false
}
```

#### EU

```json
{
  "id": "{{FINANCIAL_ADDRESS_ID}}",
  "object": "v2.money_management.financial_address",
  "created": "2025-06-19T19:17:54.607Z",
  "credentials": {
    "type": "sepa_bank_account",
    "sepa_bank_account": {
      "account_holder_name": "Jenny Rosen",
      "bank_name": "SEPA Test Bank",
      "bic": "TSTEZ122",
      "country": "IE",
      "iban": "IE29AIBK93115212345678",
      "last4": "6890"
    }
  },
  "currency": "eur",
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
  "settlement_currency": "eur",
  "status": "pending",
  "livemode": false
}
```

After you create a financial address, it starts in a `pending` status while Stripe provisions the bank details. When the status becomes `active`, you can retrieve the credentials (bank details) and share them to receive funds. You can monitor incoming funds using [received credits](https://docs.stripe.com/treasury/connect/moving-money/fund-a-financial-account.md#monitor-received-credits).

Outbound transfers require a financial address.

Add a payout method to the account that will receive the funds:

#### GB bank account

Create a GB bank account and initiate Confirmation of Payee (CoP) using the [GB Bank Accounts API](https://docs.stripe.com/api/v2/core/vault/gb-bank-accounts.md?api-version=preview).

```curl
curl -X POST https://api.stripe.com/v2/core/vault/gb_bank_accounts \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-07-29.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "sort_code": "108800",
    "account_number": "00012345",
    "currency": "gbp",
    "confirmation_of_payee": {
        "initiate": true
    }
  }'
```

```json
{
  "id": "{{PAYOUT_METHOD_ID}}",
  "object": "v2.core.vault.gb_bank_account",
  "bank_name": "Test Bank",
  "last4": "2345",
  "confirmation_of_payee": { "status": "awaiting_acknowledgement" }
}
```

Check CoP status and acknowledge if needed.

```curl
curl https://api.stripe.com/v2/core/vault/gb_bank_accounts/{{PAYOUT_METHOD_ID}} \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-07-29.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

```curl
curl -X POST https://api.stripe.com/v2/core/vault/gb_bank_accounts/{{PAYOUT_METHOD_ID}}/acknowledge_confirmation_of_payee \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-07-29.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

#### US bank account

Create a US bank account for ACH using the [US Bank Accounts API](https://docs.stripe.com/api/v2/core/vault/us-bank-accounts.md?api-version=preview).

```curl
curl -X POST https://api.stripe.com/v2/core/vault/us_bank_accounts \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-07-29.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "routing_number": "110000000",
    "account_number": "000123456789",
    "bank_account_type": "checking",
    "currency": "usd"
  }'
```

```json
{
  "id": "{{PAYOUT_METHOD_ID}}",
  "object": "v2.core.vault.us_bank_account",
  "bank_name": "Test Bank",
  "last4": "6789",
  "routing_number": "110000000"
}
```

Optionally, you can add a Fedwire routing number if you want to support wires.

```curl
curl -X POST https://api.stripe.com/v2/core/vault/us_bank_accounts/{{BANKACCOUNT_ID}} \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-07-29.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "fedwire_routing_number": "110000000"
  }'
```

#### OSI (50+ countries)

Create a payout method globally with the [OutboundSetupIntents API](https://docs.stripe.com/api/v2/money-management/outbound-setup-intents.md?api-version=preview). In this sample, the response shows required next steps to obtain payee confirmation and that the status requires action, because the country of the bank account requires it.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_setup_intents \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-07-29.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "payout_method_data": {
        "type": "bank_account",
        "bank_account": {
            "country": "GB",
            "routing_number": "108800",
            "account_number": "00012345",
            "currency": "gbp"
        }
    },
    "usage_intent": "payment"
  }'
```

```json
{
  "id": "osi_test_61Uo1MjgIZUEjAHYm16Uo0zj0KE9m04eAZihENE5YR8i",
  "object": "v2.money_management.outbound_setup_intent",
  "created": "2026-06-04T15:42:13.000Z",
  "next_action": {
    "confirmation_of_payee": {
      "object": "core.vault.gb_bank_account",
      "status": "uninitiated"
    },
    "type": "confirmation_of_payee"
  },
  "payout_method": {
    "id": "gbba_test_61Uo1MizBMc75kr8s16Uo0zj0KE9m04eAZihENE5YJA8",
    "object": "v2.money_management.payout_method",
    "available_payout_speeds": [
      "standard"
    ],
    "bank_account": {
      ...
    },
    "created": "2026-06-04T15:42:12.945Z",
    "latest_outbound_setup_intent": "osi_test_61Uo1MjgIZUEjAHYm16Uo0zj0KE9m04eAZihENE5YR8i",
    "type": "bank_account",
    "usage_status": {
      "payments": "requires_action",
      "transfers": "eligible"
    },
    "livemode": false
  },
  "status": "requires_action",
  "usage_intent": "payment",
  "livemode": false
}
```

Make the outbound transfer from the financial account according to the region and currency.

#### General

At this point, you have all the necessary pieces to transfer funds from the connected account’s financial account using the [Create an OutboundTransfer](https://docs.stripe.com/api/v2/money-management/outbound-transfers/create.md?api-version=preview) endpoint.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_transfers \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "to": {
        "payout_method": "{{PAYOUT_METHOD_ID}}",
        "currency": "usd"
    },
    "amount": {
        "value": 30000,
        "currency": "usd"
    },
    "description": "Transfer to a connected account'\''s bank account"
  }'
```

#### Intra-EU [Private preview]
Available in: AT, BE, HR, CY, EE, FI, FR, DE, GR, IE, IT, LV, LT, LU, MT, NL, PT, SK, SI, ES
If the account is in the EU, we need to use [Recipient Verifications](https://docs.stripe.com/api/v2/recipient-verifications.md?api-version=preview) to perform a Verification of Payee. This verification ensures that the account credentials match the bank account beneficiary before making the payment.

```curl
curl -X POST https://api.stripe.com/v2/money_management/recipient_verifications \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "payout_method": "{{PAYOUT_METHOD_ID}}"
  }'
```

The response includes the recipient verification ID, expiration, and verification details.

```json
{
  "id": "{{RECIPIENT_VERIFICATION_ID}}",
  "object": "v2.money_management.recipient_verification",
  "match_result": "match",
  "match_result_details": {
    "matched_name": "…",
    "message": "The provided name matches the name the bank has on file for this account.",
    "provided_name": "…"
  },
  "expires_at": "2025-11-17T16:30:47.256824340Z",
  "status": "verified",
  "status_transitions": null,
  ...
}
```

In case of a partial match or mismatch, you must acknowledge the recipient verification:

```curl
curl -X POST https://api.stripe.com/v2/money_management/recipient_verifications/{{RECIPIENTVERIFICATIONID_ID}}/acknowledge \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

At this point, you have all the necessary pieces to transfer funds from the connected account’s financial account using the [Create an OutboundTransfer](https://docs.stripe.com/api/v2/money-management/outbound-transfers/create.md?api-version=preview) endpoint.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_transfers \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "eur"
    },
    "to": {
        "payout_method": "{{PAYOUT_METHOD_ID}}",
        "currency": "eur"
    },
    "amount": {
        "value": 30000,
        "currency": "eur"
    },
    "recipient_verification": "{{RECIPIENTVERIFICATIONID_ID}}",
    "description": "Transfer to a connected account'\''s bank account"
  }'
```

#### USD [Private preview]
Available in: US
Add the US bank account as a payout method in a [recipient OutboundSetupIntent](https://docs.stripe.com/treasury/connect/account-management/connected-accounts.md#recipient-payout-methods), then create the outbound transfer.

#### ACH

Typically takes 2-3 business days

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_transfers \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "to": {
        "payout_method": "{{PAYOUT_METHOD_ID}}",
        "currency": "usd"
    },
    "amount": {
        "value": 30000,
        "currency": "usd"
    },
    "description": "Transfer to connected account'\''s US bank account"
  }'
```

#### Wire

Typically completes the same business day

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_transfers \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "to": {
        "payout_method": "{{PAYOUT_METHOD_ID}}",
        "currency": "usd"
    },
    "amount": {
        "value": 30000,
        "currency": "usd"
    },
    "delivery_options": {
        "bank_account": "wire"
    },
    "description": "Wire transfer to connected account'\''s US bank account"
  }'
```

Stripe supports both FedWire and CHIPS, and automatically routes to the most cost-effective and efficient network.

## Webhooks

Stripe emits the following `OutboundTransfer` [events](https://docs.stripe.com/api/v2/money-management/outbound-transfers/event-types.md?api-version=preview) to your [webhook](https://docs.stripe.com/webhooks.md) endpoint:

- `v2.money_management.outbound_transfer.created`
- `v2.money_management.outbound_transfer.posted`
- `v2.money_management.outbound_transfer.returned`
- `v2.money_management.outbound_transfer.updated`
- `v2.money_management.outbound_transfer.failed`
- `v2.money_management.outbound_transfer.canceled`

## See also

- [Build an integration](https://docs.stripe.com/treasury/connect/build-an-integration.md)
- [Financial accounts](https://docs.stripe.com/treasury/connect/account-management/financial-accounts.md)
- [Connected accounts](https://docs.stripe.com/treasury/connect/account-management/connected-accounts.md)

