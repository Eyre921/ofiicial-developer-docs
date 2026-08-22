---
title: "Multiple financial accounts and external funding"
source: https://docs.stripe.com/treasury/connect/examples/multi-financial-accounts.md
path: treasury/connect/examples/multi-financial-accounts
---

# Multiple financial accounts and external funding

Learn how to create two financial accounts and move funds between them.

This example use case shows an integration using a SaaS platform that provides financial services to restaurants using *Connect* (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) and [Treasury for platforms](https://docs.stripe.com/treasury/connect.md). One restaurant wants two financial accounts (operations and tips) so that card revenue flows to the operations account, then evenly distributes tips to employees. The restaurant also wants to set up US bank account credentials to add funds to the operational account for a dining room renovation.

The example integration requires the following steps:

- Create and onboard a [connected account](https://docs.stripe.com/treasury/connect/account-management/connected-accounts.md) for Treasury for platforms.
- Create two [financial accounts](https://docs.stripe.com/treasury/connect/account-management/financial-accounts.md) (operations and tips).
- Create a financial address so the restaurant can bank-transfer funds into a financial account.
- Move funds between the two financial accounts.

> #### Develop in a sandbox
> 
> Begin in a [sandbox](https://docs.stripe.com/sandboxes.md) with access to Treasury for platforms and use that sandbox’s test API keys for all requests.

## Create the connected account

The platform [creates the connected account](https://docs.stripe.com/api/v2/core/accounts/create.md) for the restaurant with the `merchant` and `money_manager` configurations and requests the associated capabilities.

```curl
curl -X POST https://api.stripe.com/v2/core/accounts \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  --json '{
    "include": [
        "configuration.money_manager"
    ],
    "contact_email": "restaurant@example.com",
    "display_name": "Donut Shop",
    "identity": {
        "country": "US",
        "entity_type": "company"
    },
    "configuration": {
        "merchant": {
            "mcc": "5814",
            "support": {
                "phone": "0000000000"
            },
            "capabilities": {
                "card_payments": {
                    "requested": true
                }
            }
        },
        "money_manager": {
            "capabilities": {
                "received_credits": {
                    "bank_accounts": {
                        "requested": true
                    }
                },
                "business_storage": {
                    "inbound": {
                        "usd": {
                            "requested": true
                        }
                    },
                    "outbound": {
                        "usd": {
                            "requested": true
                        }
                    }
                },
                "outbound_transfers": {
                    "bank_accounts": {
                        "requested": true
                    }
                },
                "outbound_payments": {
                    "bank_accounts": {
                        "requested": true
                    }
                }
            }
        }
    },
    "dashboard": "none",
    "defaults": {
        "currency": "usd",
        "responsibilities": {
            "fees_collector": "application",
            "losses_collector": "application"
        }
    }
  }'
```

```json
{
  "id": "{{CONNECTED_ACCOUNT_ID}}",
  "object": "v2.core.account",
  "applied_configurations": ["merchant","money_manager"],
  "configuration": {
    "money_manager": {
      "capabilities": {
        "business_storage": {
          "inbound": {
            "usd": {
              "requested": true,
              "status": "restricted"
            }
          },
          "outbound": {
            "usd": {
              "requested": true
            }
          }
        }
      }
    }
  },
  "display_name": "Donut Shop",
  "dashboard": "none",
  "livemode": false
}
```

## Onboard the restaurant

The platform then [onboards the connected account](https://docs.stripe.com/connect/api-onboarding.md) by:

1. Retrieving the requirements generated for the requested capabilities.
2. Providing a form to collect the information required from your connected account.
3. Updating the `Account` with the collected information, specifying the connected account in the `Stripe-Context` header: `{{CONNECTED_ACCOUNT_ID}}` to identify the connected account as the account to update.

Alternatively, the platform might create an [account link](https://docs.stripe.com/connect/hosted-onboarding.md?accounts-namespace=v2&lang=curl#create-account-link) specifying the `type` as the `merchant` and `money_manager` configurations, then send the returned URL to the connected account before it expires so they can provide the required information in a Stripe-hosted interface.

The platform listens for the `v2.core.account[configuration.money_manager].capability_status_updated` [webhook](https://docs.stripe.com/webhooks.md) to confirm the capabilities are active for its connected account.

## Create the operations financial account

The platform creates a [US storage financial account](https://docs.stripe.com/api/v2/money-management/financial-accounts/create.md?api-version=preview) for day-to-day operations, specifying the restaurant’s account ID in the `Stripe-Context` header to associate the financial account with the restaurant.

```curl
curl -X POST https://api.stripe.com/v2/money_management/financial_accounts \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "type": "storage",
    "storage": {
        "holds_currencies": [
            "usd"
        ]
    },
    "metadata": {
        "name": "operations"
    }
  }'
```

The response includes the operations financial account ID:

```json
{
  "id": "fa_12345",
  "object": "v2.money_management.financial_account",
  "balance": {
    "available": { "usd": { "value": 0, "currency": "usd" } },
    "inbound_pending": { "usd": { "value": 0, "currency": "usd" } },
    "outbound_pending": { "usd": { "value": 0, "currency": "usd" } }
  },
  "country": "US",
  "created": "2025-06-18T11:05:27.930Z",
  "metadata": { "name": "operations" },
  "status": "pending",
  "status_details": null,
  "storage": { "holds_currencies": ["usd"] },
  "type": "storage",
  "livemode": false
}
```

## Create the tips financial account

The platform creates a second US storage financial account dedicated to tips.

```curl
curl -X POST https://api.stripe.com/v2/money_management/financial_accounts \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "type": "storage",
    "storage": {
        "holds_currencies": [
            "usd"
        ]
    },
    "metadata": {
        "name": "tips"
    }
  }'
```

The response includes the tips financial account ID:

```json
{
  "id": "fa_67890",
  "object": "v2.money_management.financial_account",
  "balance": {
    "available": { "usd": { "value": 0, "currency": "usd" } },
    "inbound_pending": { "usd": { "value": 0, "currency": "usd" } },
    "outbound_pending": { "usd": { "value": 0, "currency": "usd" } }
  },
  "country": "US",
  "created": "2025-06-18T11:06:10.000Z",
  "metadata": { "name": "tips" },
  "status": "pending",
  "status_details": null,
  "storage": { "holds_currencies": ["usd"] },
  "type": "storage",
  "livemode": false
}
```

## Create a financial address for the operations account

To allow the restaurant to add funds through bank transfers, the platform [creates a US bank financial address](https://docs.stripe.com/api/v2/money-management/financial-addresses/create.md?api-version=preview) for the operations financial account.

```curl
curl -X POST https://api.stripe.com/v2/money_management/financial_addresses \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "financial_account": "{{OPERATIONSFINANCIALACCOUNTID_ID}}",
    "type": "us_bank_account"
  }'
```

The response includes the ID of the financial address and the US bank credentials:

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
  "financial_account": identifier("financialAccountId"),
  "created": "2023-03-30T17:32:06.665Z",
  "currency": "usd"
}
```

The platform simulates receiving funds through the financial address using the [Credit a FinancialAddress object test helper](https://docs.stripe.com/api/v2/money-management/financial-addresses/credit.md?api-version=preview) in a sandbox instead of [funding in live mode](https://docs.stripe.com/treasury/connect/moving-money/fund-a-financial-account.md#external-account) using an external bank account.

```curl
curl -X POST https://api.stripe.com/v2/test_helpers/financial_addresses/{{FINANCIAL_ADDRESS_ID}}/credit \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "amount": {
        "value": 5000,
        "currency": "usd"
    },
    "network": "ach"
  }'
```

The response indicates the outcome.

```json
{
  "object": "financial_address_credit_simulation",
  "status": "accepted",
  "livemode": false
}
```

## Move funds from operations to tips

The platform [creates an outbound transfer](https://docs.stripe.com/api/v2/money-management/outbound-transfers/create.md?api-version=preview) to move funds between two financial accounts that both belong to the restaurant.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_transfers \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{OPERATIONSFINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "to": {
        "payout_method": "{{TIPSFINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "amount": {
        "value": 1000,
        "currency": "usd"
    },
    "description": "Move tips to tips FA"
  }'
```

```json
{
  "id": "obt_test_65OAfYe4XKyMwZeHlcV16NybHIZ4SQ3LORe4rpuNGDIRZw",
  "object": "v2.money_management.outbound_transfer",
  "from": {
    "financial_account": "fa_12345",
    "debited": { "value": 1000, "currency": "usd" }
  },
  "to": {
    "payout_method": "fa_67890",
    "credited": { "value": 1000, "currency": "usd" }
  },
  "amount": { "value": 1000, "currency": "usd" },
  "cancelable": true,
  "description": "Move tips to tips FA",
  "status": "processing",
  "status_transitions": {
    "canceled_at": null,
    "failed_at": null,
    "posted_at": null,
    "returned_at": null
  },
  "created": "2025-06-19T17:52:34.829Z",
  "expected_arrival_date": "2025-06-19T17:52:34.803Z",
  "receipt_url": "https://payments.stripe.com/transaction_receipt/…",
  "livemode": false
}
```

To verify balances after the transfer, the platform [lists the connected account’s financial accounts](https://docs.stripe.com/api/v2/money-management/financial-accounts/list.md?api-version=preview).

```curl
curl https://api.stripe.com/v2/money_management/financial_accounts \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

```json
{
  "data": [
    {
      "id": "{% identifier type=\"operationsFinancialAccountId\" /%}",
      "object": "v2.money_management.financial_account",
      "balance": {
        "available": { "usd": { "value": 4000, "currency": "usd" } },
        "inbound_pending": { "usd": { "value": 0, "currency": "usd" } },
        "outbound_pending": { "usd": { "value": 0, "currency": "usd" } }
      },
      "country": "US",
      "status": "open",
      "storage": { "holds_currencies": ["usd"] },
      "type": "storage",
      "livemode": false
    },
    {
      "id": "{% identifier type=\"tipsFinancialAccountId\" /%}",
      "object": "v2.money_management.financial_account",
      "balance": {
        "available": { "usd": { "value": 1000, "currency": "usd" } },
        "inbound_pending": { "usd": { "value": 0, "currency": "usd" } },
        "outbound_pending": { "usd": { "value": 0, "currency": "usd" } }
      },
      "country": "US",
      "status": "open",
      "storage": { "holds_currencies": ["usd"] },
      "type": "storage",
      "livemode": false
    }
  ],
  "next_page_url": null,
  "previous_page_url": null
}
```

With two financial accounts in place and a way to move funds between them, the platform can route revenue from card payments to the operations account and use the tips account to fund periodic employee payouts.

