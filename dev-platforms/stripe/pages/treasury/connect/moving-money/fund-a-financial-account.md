---
title: "Fund a financial account"
source: https://docs.stripe.com/treasury/connect/moving-money/fund-a-financial-account.md
path: treasury/connect/moving-money/fund-a-financial-account
---

# Fund a financial account

Learn how to move money into a financial account balance.

You have the following options to fund a financial account:

| Funding method | Availability for outbound payments and transfers | Where to initiate |
| --- | --- | --- |
| [Send funds from a Stripe payments balance](https://docs.stripe.com/treasury/connect/moving-money/fund-a-financial-account.md#payments-balance) | Instant | Stripe API |
| [Send funds from your external bank account to a FinancialAddress](https://docs.stripe.com/treasury/connect/moving-money/fund-a-financial-account.md#external-account) | 1 business day (7 days initially for the first 5000 GBP in funding) | From your bank |
| [Use inbound transfers from a linked external bank account](https://docs.stripe.com/treasury/connect/moving-money/fund-a-financial-account.md#inbound-transfer) | Instant | Stripe API |
| [Send funds from an existing financial account](https://docs.stripe.com/treasury/connect/moving-money/fund-a-financial-account.md#existing-financial-account) | Instant | Stripe API |
| [Simulate a received credit](https://docs.stripe.com/treasury/connect/moving-money/fund-a-financial-account.md#testingrc) (Sandbox only) | Instant | Stripe API |
| [Use automatic transfer rules](https://docs.stripe.com/treasury/connect/moving-money/fund-a-financial-account.md#automatic-transfer-rules) | Instant (when rule triggers) | Stripe API |

## Send funds from a Stripe Payments balance 

As the platform, you can move money from your payments [Balance](https://docs.stripe.com/api/balance.md) to your financial accounts or from your connected accounts’ payments balance to their financial accounts.

When testing, you can use [Stripe test cards](https://docs.stripe.com/testing.md?testing-method=tokens#available-balance), as in the following example. Test cards allow you to fund your Stripe payments balance instantly so you can test moving those funds to your financial account without waiting.

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -d amount=10000 \
  -d currency=gbp \
  -d payment_method=pm_card_bypassPending \
  -d confirm=true \
  --data-urlencode "return_url=https://example.com/return"
```

The following example moves funds from a platform’s balance to its financial account:

```curl
curl https://api.stripe.com/v1/payouts \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -d amount=978 \
  -d currency=gbp \
  -d "payout_method={{FINANCIALACCOUNTID_ID}}"
```

To move money from your connected account’s payments balance, pass the `Stripe-Account` to identify the connected account as the target of the request:

```curl
curl https://api.stripe.com/v1/payouts \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}" \
  -d amount=78 \
  -d currency=gbp \
  -d "payout_method={{FINANCIALACCOUNTID_ID}}"
```

## Send funds from an external bank account 

You should only credit financial accounts using external bank accounts that you own.

To get the bank credentials for your financial account, you must create a [FinancialAddress](https://docs.stripe.com/api/v2/money-management/financial-addresses.md?api-version=preview).

To create a financial address for your financial account, use the [Create FinancialAddress](https://docs.stripe.com/api/v2/money-management/financial-addresses/create.md?api-version=preview) API.

Create a [Financial Address](https://docs.stripe.com/api/v2/money-management/financial-addresses.md?api-version=preview) to assign bank details to your financial account you can share with customers or partners so they can send funds directly to the financial account. Specify the `type` corresponding to the country of the financial account to make sure we provision the correct [address credentials](https://docs.stripe.com/api/v2/money-management/financial-addresses/object.md?api-version=preview#v2_financial_address_object-credentials) (such as a US routing number or a British sort code).

After you create a financial address, it starts in a `pending` status while Stripe provisions the bank details. When the status becomes `active`, you can retrieve the credentials (bank details) and share them to receive funds. You can monitor incoming funds using [received credits](https://docs.stripe.com/treasury/connect/moving-money/fund-a-financial-account.md#monitor-received-credits).

```curl
curl -X POST https://api.stripe.com/v2/money_management/financial_addresses \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "financial_account": "{{FINANCIALACCOUNTID_ID}}",
    "type": "gb_bank_account"
  }'
```

If successful, the response provides the ID for the financial address you’re creating:

```json
{
  "id": "{{FINANCIAL_ADDRESS_ID}}",
  "object": "v2.money_management.financial_address",
  "created": "2025-06-19T19:17:54.607Z",
  "credentials": null,
  "currency": "gbp",
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
  "settlement_currency": "gbp",
  "status": "pending",
  "livemode": false
}
```

You can use the [Get FinancialAddress](https://docs.stripe.com/api/v2/money-management/financial-addresses/retrieve.md?api-version=preview) API to fetch details about the financial address:

```curl
curl -G https://api.stripe.com/v2/money_management/financial_addresses/{{FINANCIAL_ADDRESS_ID}} \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  -d "include[0]=credentials.gb_bank_account.account_number"
```

After you retrieve the FinancialAddress, you can view the account credentials, such as a US routing number or British sort code, which you can use to send money from your external bank account.

```json
{
  "id": "{{FINANCIAL_ADDRESS_ID}}",
  "object": "v2.money_management.financial_address",
  "created": "2025-07-21T10:43:17.249Z",
  "credentials": {
    "gb_bank_account": {
      "account_holder_name": "John Smith",
      "account_number": "00000000",
      "last4": "0000",
      "sort_code": "000000"
    },
    "type": "gb_bank_account"
  },
  "currency": "gbp",
  "financial_account": "fa_12345",
  "status": "active",
  "livemode": false
}
```

To list financial addresses associated with your financial account, use the [List Financial Addresses](https://docs.stripe.com/api/v2/money-management/financial-addresses/list.md?api-version=preview) API. You can use different parameters to filter out financial addresses for your financial account.

The following example request lists all financial addresses for the account:

```curl
curl https://api.stripe.com/v2/money_management/financial_addresses \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

In the US, connected accounts can fund USD financial accounts by sending ACH, RTP, or wire transfers to the financial address credentials. RTP funds are typically available within minutes.

| Funding method | Funds available | Where to initiate |
| --- | --- | --- |
| ACH | 0–3 business days | From your bank |
| RTP | Typically within minutes | From your bank |
| Wire | Same day | From your bank |

> RTP funding is available only for financial accounts in the US. If your Stripe account is outside the US, you can fund your USD financial account using ACH or a wire.

## Use inbound transfers from a linked external bank account  (Private preview)

If you’re a platform in the US, you can use inbound transfers to debit your connected account’s linked external bank account to fund their Stripe financial account.

You embed a component in your platform where users link and verify their bank account for instant verification with no microdeposits or waiting period. Stripe:

- Verifies ownership and obtains proof that the account holder authorized the debit.
- Secures a mandate for legal authorization to pull funds on an ongoing basis.
- Generates a tokenized credential representing the account and routing numbers securely vaulted as a reusable `usba_*` payment method.

Your connected account must have the `money_manager` configuration and active [business_storage.inbound.usd](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=preview#v2_create_accounts-configuration-money_manager-capabilities-business_storage-inbound-usd) capability to use inbound transfers to fund their financial accounts from their external bank account.

### Authenticate the external account

Create an [AccountSession](https://docs.stripe.com/api/account_sessions.md) on your server to render either the `account_management` or `account_onboarding` embedded component requesting the `external_account_collection` feature. This allows your connected account to link their external bank account to Stripe through the component UI.

```curl
curl https://api.stripe.com/v1/account_sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-06-24.preview; embedded_connect_beta=v2" \
  --data-urlencode "account=identifier(connectedAccount)" \
  -d "components[account_management][enabled]=true" \
  -d "components[account_management][features][external_account_collection]=true"
```

### Create an inbound transfer

You or your connected account can initiate an inbound transfer to move funds into their financial account from their linked external account.

#### Embedded component

You can render the [financial_accounts](https://docs.stripe.com/treasury/connect/prebuilt-embedded-finance.md#available-components) embedded component to allow your connected account to transfer money from their linked external account to their financial account using the **Move money** user interface.

#### API

1. Look up the credential created from the external account authorization session.
   ```curl
   curl https://api.stripe.com/v2/money_management/payout_methods \
     -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
     -H "Stripe-Version: 2026-06-24.preview" \
     -H "Stripe-Context: {{CONTEXT_ID}}"
   ```
Make sure the `usage_status.transfers` parameter for the credential is `eligible`.
2. Provide the `usba_*` credential ID as the value of the `from` parameter in the InboundTransfer request.
   ```curl
   curl -X POST https://api.stripe.com/v2/money_management/inbound_transfers \
     -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
     -H "Stripe-Version: 2026-06-24.preview" \
     -H "Stripe-Context: {{CONTEXT_ID}}" \
     --json '{
       "from": {
           "payment_method": "usba_123456"
       },
       "to": {
           "financial_account": "{{FINANCIALACCOUNTID_ID}}",
           "currency": "usd"
       },
       "amount": {
           "value": 1,
           "currency": "usd"
       },
       "description": "Transfer from external account"
     }'
   ```

### Transfer lifecycle

After creation, an inbound transfer moves through various states. Listen for and handle the following `v2.money_management.inbound_transfer` webhook events at each stage:

| Event | Description |
| --- | --- |
| `bank_debit_queued` | Transfer created, waiting to send to the bank network. |
| `bank_debit_processing` | Debit submitted to ACH, awaiting settlement. |
| `bank_debit_succeeded` | Bank confirmed the debit. |
| `available` | Funds available in the financial account. |
| `bank_debit_failed` | Debit failed, possibly because of insufficient funds or an invalid account. |
| `bank_debit_returned` | The bank returned the debit after initial success (can occur days later). |

## Send funds from an existing financial account 

You can transfer funds between financial accounts using the [OutboundTransfer](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-transfers.md#move-money-from-one-financial-account-to-another-financial-account) or [OutboundPayment](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-payments.md#move-money-from-a-platform-to-connected-account) APIs.

- Use [OutboundTransfer](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-transfers.md#move-money-from-one-financial-account-to-another-financial-account) to transfer money between financial accounts owned by the same entity (for example, between two financial accounts owned by the same platform, or two financial accounts owned by the same connected account).
- Use [OutboundPayment](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-payments.md#move-money-from-a-platform-to-connected-account) for payments between different connected accounts, and payments to and from the platform and connected account.

## Monitor received credits

Every transaction that adds funds to a financial account generates a [ReceivedCredit](https://docs.stripe.com/api/v2/money-management/received-credits/object.md?api-version=preview) object on the financial account, detailing how funds were sent and from what account, where possible.

For USD financial accounts in the US, funds can arrive through ACH, RTP, or wire transfers.

### List received credits

[List received credits](https://docs.stripe.com/api/v2/money-management/received-credits/retrieve.md?api-version=preview) to review a set of funding transactions for a financial account. Use parameters in the request to filter the results by created date or to limit responses.

```curl
curl https://api.stripe.com/v2/money_management/received_credits \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

### Get a received credit

[Retrieve a received credit](https://docs.stripe.com/api/v2/money-management/received-credits/retrieve.md?api-version=preview) by its ID to review details such as the `amount`, `status`, and `type` of transfer.

```curl
curl https://api.stripe.com/v2/money_management/received_credits/{{RECEIVED_CREDIT_ID}} \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

```json
    {
      "id": "rc_test_123",
      "object": "v2.money_management.received_credit",
      "amount": {
        "value": 1,
        "currency": "gbp"
      },
      "balance_transfer": {
        "payout_v1": "",
        "type": "outbound_payment"
      },
      "created": "2025-06-11T19:25:47.222Z",
      "description": "Received money from an FA",
      "financial_account": "fa_test_321",
      "receipt_url": "https://payments.stripe.com/transaction_receipt/…",
      "status": "succeeded",
      "status_details": null,
      "status_transitions": {
        "failed_at": null,
        "returned_at": null,
        "succeeded_at": "2025-06-11T19:25:47.222Z"
      },
      "type": "balance_transfer",
      "livemode": false
    }
```

### Create a test received credit 

[Credit a financial address](https://docs.stripe.com/api/v2/money-management/financial-addresses/credit.md?api-version=preview) to add virtual funds and increase your financial account balance for testing.

```curl
curl -X POST https://api.stripe.com/v2/test_helpers/financial_addresses/{{FINANCIAL_ADDRESS_ID}}/credit \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "amount": {
        "value": 250,
        "currency": "gbp"
    },
    "network": "fps"
  }'
```

Set `network` to `fps` or `chaps` to simulate the respective payment network:

| Network value | Settlement | Transaction limit |
| --- | --- | --- |
| `fps` | Typically within minutes | 1,000,000 GBP |
| `chaps` | Same day | No upper limit |

The response indicates if the simulation was successful, and you can check the balance of the financial account to confirm the increase.

```curl
curl https://api.stripe.com/v2/money_management/financial_accounts/{{FINANCIALACCOUNTID_ID}} \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

## Set up automatic transfer rules 

Automatic transfer rules enable platforms to automatically split funds from a connected account’s payments balance to a financial account during scheduled payouts. This eliminates the need for manual calculations and transfers.

Before setting up automatic transfer rules, make sure:

- The connected account has at least one active financial account.
- The connected account is on an automatic payout schedule.
- The financial account supports the currency you want to transfer.

### Configure automatic transfer rules

Use the [Balance Settings API](https://docs.stripe.com/api/balance-settings.md?api-version=preview) to configure automatic transfer rules for your connected accounts. You can set one financial account per currency as the automatic transfer destination.

You can also configure automatic transfer rules for users on a manual payout schedule.

### Enable automatic payouts

Automatic payouts is disabled if `payments.payouts.schedule.interval` is set to `manual`. You must enable automatic payouts to activate the rules.

```curl
curl https://api.stripe.com/v1/balance_settings \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}" \
  -d "payments[payouts][schedule][interval]=daily"
```

### Transfer a fixed amount

Transfer up to a specific amount to a financial account, with the remaining balance going to the connected account’s external bank account. When you use `transfer_up_to_amount`, the connected account must have a bank account configured for the currency. If the balance is less than `transfer_up_to_amount`, the entire balance is transferred to the financial account.

```curl
curl https://api.stripe.com/v1/balance_settings \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}" \
  -d "payments[payouts][automatic_transfer_rules_by_currency][gbp][0][payout_method]={{FINANCIALACCOUNTID_ID}}" \
  -d "payments[payouts][automatic_transfer_rules_by_currency][gbp][0][type]=transfer_up_to_amount" \
  -d "payments[payouts][automatic_transfer_rules_by_currency][gbp][0][transfer_up_to_amount]=1500000"
```

### Transfer all funds

Transfer all available funds to a financial account. When you use `transfer_all`, an external bank account isn’t required for the connected account.

```curl
curl https://api.stripe.com/v1/balance_settings \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}" \
  -d "payments[payouts][automatic_transfer_rules_by_currency][gbp][0][payout_method]={{FINANCIALACCOUNTID_ID}}" \
  -d "payments[payouts][automatic_transfer_rules_by_currency][gbp][0][type]=transfer_all"
```

### Update automatic transfer rules

Update a rule by submitting the complete configuration for the currency:

```curl
curl https://api.stripe.com/v1/balance_settings \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}" \
  -d "payments[payouts][automatic_transfer_rules_by_currency][gbp][0][payout_method]={{FINANCIALACCOUNTID_ID}}" \
  -d "payments[payouts][automatic_transfer_rules_by_currency][gbp][0][type]=transfer_up_to_amount" \
  -d "payments[payouts][automatic_transfer_rules_by_currency][gbp][0][transfer_up_to_amount]=2000000"
```

### Remove automatic transfer rules

Remove the automatic transfer rule for a currency:

```curl
curl https://api.stripe.com/v1/balance_settings \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}" \
  -d "payments[payouts][automatic_transfer_rules_by_currency][gbp]="
```

### View the current configuration

Retrieve the current automatic transfer rules:

```curl
curl https://api.stripe.com/v1/balance_settings \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}"
```

