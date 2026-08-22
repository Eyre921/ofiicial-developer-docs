---
title: "Financial accounts"
source: https://docs.stripe.com/treasury/connect/account-management/financial-accounts.md
path: treasury/connect/account-management/financial-accounts
---

# Financial accounts

Use financial accounts to store, send, and receive funds.

Financial accounts serve as the source or destination of funds storage and movement across all Stripe products. You can provision different financial accounts with their own distinct balances for your platform and your connected accounts.

For example, a connected account on your platform might have a 100 USD payment balance and a 200 USD storage financial account balance, representing a total balance of 300 USD. These two balances remain separate, but you can move money in and out of these accounts for different purposes depending on which [capabilities you enable for the connected accounts](https://docs.stripe.com/treasury/connect/account-management/connected-accounts.md#how-capabilities-work).

## Balances

A financial account balance includes both settled and pending transactions, so the total might not reflect the funds a connected account can spend. [Retrieve a financial account](https://docs.stripe.com/api/v2/money-management/financial-accounts/retrieve.md?api-version=preview) to view the following balance subtotals and their currency:

- `available`: Funds the connected account can spend now.
- `inbound_pending`: Funds that aren’t spendable yet, but that become available later.
- `outbound_pending`: Funds that are in the account, but aren’t spendable because they’re held for pending outbound flows.

### Negative balances 

If your connected account has a negative balance in one of their financial accounts, Stripe holds an equivalent reserve on your platform’s [connected reserve balance](https://docs.stripe.com/connect/account-balances.md#understanding-connected-reserve-balances), funded from your platform’s [payments balance](https://docs.stripe.com/payments/balances.md#payments-balance). This reserve automatically releases after the negative balance resolves.

After 180 days, Stripe remediates a negative balance by moving funds from your platform reserve to bring the financial account back to zero.

Monitor your connected accounts to identify and address negative financial account balances to avoid Stripe interventions. Contact your connected account representative and, if necessary, you can [add funds to a financial account](https://docs.stripe.com/treasury/connect/moving-money/fund-a-financial-account.md).

Stripe contacts you if individual or aggregate balances exceed our risk limits.

## Financial account types

The `FinancialAccount` object has a [type](https://docs.stripe.com/api/v2/money-management/financial-accounts/object.md?api-version=preview#v2_financial_account_object-type) that determines:

- **What the balance represents:** A balance might represent incoming payments or fees.
- **What you can do with it:** Each type supports a specific set of money management APIs, such as outbound payments or multiprocessor settlement.
- **How Stripe displays it:** The type determines the display name and context shown to users.

### Storage

You can create `storage` financial accounts to separate funds for different purposes and different currencies, such as:

- Holding funds transferred from the payments balance, received from a FinancialAddress, or pulled by InboundTransfer.
- Supporting OutboundPayments, OutboundTransfers, card spend, and other money management APIs.
- Specifying `funds_usage_type` values of `consumer` or `business`.

Your [connected account](https://docs.stripe.com/treasury/connect/account-management/connected-accounts.md) must have active `business_storage` capabilities for each currency its storage financial accounts support.

- `money_manager.business_storage.inbound.{currency}`: Enables creating storage FAs and receiving funds into them
- `money_manager.business_storage.outbound.{currency}`: Enables sending funds out of storage FAs

> #### FDIC eligibility
> 
> Storage financial accounts for US businesses are FDIC-eligible.

### Payments (Private preview)
Available in: US
If you’re a platform in the US using [Prebuilt embedded finance](https://docs.stripe.com/treasury/connect/prebuilt-embedded-finance.md), Stripe automatically creates a `payments` financial account representing the Stripe payments balance you see in your Dashboard. The funds in this financial account aren’t FDIC-eligible.

- Every Stripe user has only one `payments` financial account, which Stripe creates automatically.
- You can’t create additional financial accounts with the `payments` type.
- The `payments` balance reflects funds from card payments, bank transfers, and other payment methods.
- This financial account shares the same balance with an existing v1 Account payments account. You can continue to use the v1 payments balance in your integrations, but must use the financial account ID for money management operations.
- You can make [money management API requests](https://docs.stripe.com/treasury/connect/account-management/financial-accounts.md#money-management-behavior) from the `payments` financial account when the applicable `money_manager` capabilities are active.
- You can fund Issuing card spend from the `payments` financial account.

#### Retrieve the payments financial account

You can retrieve a connected account’s financial accounts using the `type: "payments"` filter to get the payments financial account ID for use in other API requests, such as outbound payments and outbound transfers.

```curl
curl -G https://api.stripe.com/v2/money_management/financial_accounts \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  -d type=payments
```

The response includes the payments `FinancialAccount` with its ID:

```json
{
  "data": [
    {
      "id": "fa_payments_abc123",
      "type": "payments",
      "balances": {
        "available": { "value": 50000, "currency": "usd" }
      }
    }
  ]
}
```

#### Money management behavior

When a connected account has `money_manager` capabilities, they can take additional actions on the payments financial account.

| Operation | Description |
| --- | --- |
| OutboundPayments | Send funds to a recipient’s bank account, card, or financial account |
| OutboundTransfers | Send funds to the account’s own external bank account |
| InboundTransfers | Pull funds from the account’s own external bank account |
| ReceivedCredits | Receive funds from external bank accounts using a financial address |
| OutboundTransfers (between FAs) | Move funds between the Payments FA and Storage FAs |
| Issuing | Fund prepaid or credit cards backed by the financial account balance |

## Financial account actions

You can perform any of the following requests on the [FinancialAccount](https://docs.stripe.com/api/v2/money-management/financial-accounts.md?api-version=preview) object:

- Create a financial account
- Update a financial account
- Retrieve a financial account
- List financial accounts
- List financial account statements
- Retrieve a financial account statement
- List transactions
- Retrieve a transaction
- Close a financial account

### Webhooks

The following `v2.money_management` events trigger in response to financial account activity. Listen for them so you can incorporate handling in your integration.

| Event | Triggered |
| --- | --- |
| `financial_account.created` | A new financial account was created. |
| `financial_account.updated` | A financial account was updated. |
| `financial_address.activated` | A financial address activated and can receive funds. |
| `financial_address.failed` | A financial address failed to activate and can’t receive funds. |
| `outbound_payment.canceled` | An outbound payment was canceled before completing. |
| `outbound_payment.created` | An outbound payment was created. |
| `outbound_payment.failed` | An outbound payment failed to post. |
| `outbound_payment.posted` | An outbound payment posted. |
| `outbound_payment.returned` | An outbound payment returned. |
| `outbound_payment.updated` | An outbound payment was updated. |
| `outbound_transfer.canceled` | An outbound transfer was canceled before completing. |
| `outbound_transfer.created` | An outbound transfer was created. |
| `outbound_transfer.failed` | An outbound transfer failed to post. |
| `outbound_transfer.posted` | An outbound transfer posted. |
| `outbound_transfer.returned` | An outbound transfer returned. |
| `outbound_transfer.updated` | An outbound transfer was updated. |
| `payout_method.created` | A payout method was created. |
| `payout_method.updated` | A payout method was updated. |
| `received_credit.available` | Funds from a received credit settled and you can use them. |
| `received_credit.failed` | A payment into the financial account failed. Inspect the [ReceivedCredit status_details](https://docs.stripe.com/api/v2/money-management/received-credits/object.md?api-version=preview#v2_received_credit_object-status_details) for more information. |
| `received_credit.returned` | A payment into the financial account was reversed, returned to the originator, and deducted from the balance. |
| `received_credit.succeeded` | A payment into the financial account succeeded. |
| `transaction.created` | A transaction recording funds movement into or out of the financial account was created. |
| `transaction.updated` | A transaction recording funds movement into or out of the financial account was updated. |

### Close a financial account

You can permanently [close a financial account](https://docs.stripe.com/api/v2/money-management/financial-accounts/close.md?api-version=preview) if:

- Its [status](https://docs.stripe.com/api/v2/money-management/financial-accounts/retrieve.md?api-version=preview#v2_retrieve_financial_accounts-response-status) is `open`.
- Its balance is zero, or you specify [forwarding settings](https://docs.stripe.com/api/v2/money-management/financial-accounts/close.md?api-version=preview#v2_close_financial_accounts-forwarding_settings) to redirect any incoming transactions after closing.

```curl
curl -X POST https://api.stripe.com/v2/money_management/financial_accounts/{{FINANCIALACCOUNTID_ID}}/close \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "forwarding_settings": {
        "payout_method": "{{ALTERNATIVE_FINANCIAL_ACCOUNT_ID}}",
        "payment_method": "{{ALTERNATIVE_FINANCIAL_ACCOUNT_ID}}"
    }
  }'
```

### Required capabilities

Your ability to perform financial account actions depends on enabling the [corresponding capabilities](https://docs.stripe.com/treasury/connect/account-management/connected-accounts.md#how-capabilities-work) for your connected accounts.

## See also

- [Build an integration](https://docs.stripe.com/treasury/connect/build-an-integration.md)
- [Working with connected accounts](https://docs.stripe.com/treasury/connect/account-management/connected-accounts.md)

