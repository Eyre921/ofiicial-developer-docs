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

## Multiple financial addresses (Private preview)

> #### Request access
> 
> Enabling Treasury for platforms doesn’t automatically grant access to multiple financial addresses. Contact your Stripe representative to request access.

A financial address allows you to associate virtual bank account credentials (such as account number and US routing number, British sort code, or EU IBAN) with a financial account. Every transfer to a financial account with a financial address identifies the receiving financial address.

You can create multiple financial addresses in the same currency for a single financial account to separate different types of funding while maintaining one underlying balance. Multiple financial addresses allow you to:

- Give different bank account details to different customers or business units.
- Reconcile incoming financial account credits in your own ledger.
- Separate eligible received debits against a financial account.
- Provide bank account details that external parties can use to initiate supported outbound money movement.
- Categorize financial account activity without creating separate financial accounts.

### Choose a reconciliation model

Whether you use dedicated financial addresses or bank transfers to accept payments into your financial account depends on how you reconcile incoming funds against what your customer owes.

- [Create multiple financial addresses](https://docs.stripe.com/treasury/connect/moving-money/fund-a-financial-account.md#external-account) when your platform owns the relationship with the sender and you reconcile in your own system. Your integration maps each financial address to a specific party or ledger entry, monitors incoming funds, and handles differences between the amount received and the amount expected.

  This approach gives your platform direct access to money-movement and transaction data. Your platform is also responsible for payment obligations, overpayments, underpayments, refunds, returns, and other exceptions.

- [Use bank transfers](https://docs.stripe.com/payments/bank-transfers.md) for incoming transfers that pay a specific customer obligation managed by your Stripe integration. Stripe provides financial address details to the customer and reconciles incoming funds to that customer’s open payment or invoice.

  Stripe uses the customer balance to track underpayments, overpayments, and funds that can’t be reconciled automatically. Bank transfers also support refunds and applicable disputes, and you can use them with Checkout, the Payment Element, the Payment Intents API, Invoicing, and Subscriptions.

You can use either or both of these approaches in your integration, applying each where it fits the use case.

| Model | Use case |
| --- | --- |
| Financial addresses | Fund a balance, identify incoming funds, or reconcile transactions in your own ledger. |
| Bank transfers | Match incoming funds to a customer payment or invoice and have Stripe manage the payment lifecycle. |
| Both | Support both managed customer payments and platform-managed money movement. |

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

### Savings (Private preview)
Available in: GB
Connected accounts in the UK can create a [savings financial account](https://docs.stripe.com/treasury/connect/savings-financial-accounts.md) that earns interest.

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
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT}}" \
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
curl -X POST https://api.stripe.com/v2/money_management/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/close \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT}}" \
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

