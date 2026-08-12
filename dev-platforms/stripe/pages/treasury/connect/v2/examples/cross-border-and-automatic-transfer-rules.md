---
title: "Cross-border payouts and automatic transfer rules"
source: https://docs.stripe.com/treasury/connect/v2/examples/cross-border-and-automatic-transfer-rules.md
path: treasury/connect/v2/examples/cross-border-and-automatic-transfer-rules
---

# Cross-border payouts and automatic transfer rules

Create a financial account, automate funding and send a cross-border OutboundPayment.

This example use case shows an integration using a SaaS platform that provides financial services to property managers using *Connect* (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) and [Treasury for platforms](https://docs.stripe.com/treasury/connect/v2.md). One of its UK property managers needs a financial account to hold rental income and pay landlords internationally.

The example integration requires the following steps:

- Create and onboard a [connected account](https://docs.stripe.com/treasury/connect/v2/account-management/connected-accounts.md) for Treasury for platforms.
- Create a [financial account](https://docs.stripe.com/treasury/connect/v2/account-management/financial-accounts.md).
- Configure automatic transfer rules to move funds from the connected account’s payments balance to the financial account during scheduled payouts.
- Send a cross-border `OutboundPayment` to the landowner in Norway.

> #### Develop in a sandbox
> 
> Begin in a [sandbox](https://docs.stripe.com/sandboxes.md) with access to Treasury for platforms and use that sandbox’s test API keys for all requests.

## Create the connected account

The platform [creates the connected account](https://docs.stripe.com/api/v2/core/accounts/create.md) for the property manager with the `merchant` and `money_manager` configurations and requests the associated capabilities.

```curl
curl -X POST https://api.stripe.com/v2/core/accounts \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  --json '{
    "include": [
        "configuration.money_manager"
    ],
    "contact_email": "property.manager@example.com",
    "display_name": "Property Manager Ltd",
    "identity": {
        "country": "gb",
        "entity_type": "company"
    },
    "configuration": {
        "merchant": {
            "mcc": "6513",
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
                        "gbp": {
                            "requested": true
                        }
                    },
                    "outbound": {
                        "gbp": {
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
        "currency": "gbp",
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
        "business_storage": { "inbound": { "gbp": { "requested": true, "status": "restricted" } }, "outbound": { "gbp": { "requested": true, "status": "restricted" } } }
      }
    }
  },
  "display_name": "Property Manager Ltd",
  "dashboard": "none",
  "livemode": false
}
```

## Onboard the connected account

The platform then [onboards the connected account](https://docs.stripe.com/connect/api-onboarding.md) by:

1. Retrieving the requirements generated for the requested capabilities.
2. Providing a form to collect the information required from your connected account.
3. Updating the `Account` with the collected information, specifying the connected account in the `Stripe-Context` header: `{{CONNECTED_ACCOUNT_ID}}` to identify the connected account as the account to update.

Alternatively, the platform might create an [account link](https://docs.stripe.com/connect/hosted-onboarding.md?accounts-namespace=v2&lang=curl#create-account-link) specifying the `type` as the `merchant` and `money_manager` configurations, then send the returned URL to the connected account before it expires so they can provide the required information in a Stripe-hosted interface.

The platform listens for the `v2.core.account[configuration.money_manager].capability_status_updated` [webhook](https://docs.stripe.com/webhooks.md) to confirm the capabilities are active for its connected account.

## Create the financial account

The platform creates a [GBP storage financial account](https://docs.stripe.com/api/v2/money-management/financial-accounts/create.md?api-version=preview), specifying the property manager’s account ID in the `Stripe-Context` header to associate the financial account with the property manager.

```curl
curl -X POST https://api.stripe.com/v2/money_management/financial_accounts \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "type": "storage",
    "storage": {
        "holds_currencies": [
            "gbp"
        ]
    }
  }'
```

The response includes the financial account ID:

```json
{
  "id": "{{FINANCIAL_ACCOUNT_ID}}",
  "object": "v2.money_management.financial_account",
  "balance": {
    "available": { "gbp": { "value": 0, "currency": "gbp" } },
    "inbound_pending": { "gbp": { "value": 0, "currency": "gbp" } },
    "outbound_pending": { "gbp": { "value": 0, "currency": "gbp" } }
  },
  "country": "GB",
  "created": "2025-06-18T11:05:27.930Z",
  "status": "pending",
  "status_details": null,
  "storage": { "holds_currencies": ["gbp"] },
  "type": "storage",
  "livemode": false
}
```

## Simulate rental income

The platform creates and confirms a test PaymentIntent, using the property manager’s account ID in the `Stripe-Context` header, to simulate a rental payment that funds the property manager’s payments balance.

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}" \
  -d amount=25000 \
  -d currency=gbp \
  -d confirm=true \
  -d payment_method=pm_card_visa \
  --data-urlencode "return_url=https://example.com/return"
```

## Configure automatic transfer rules

Automatic transfer rules require scheduled payouts (not `manual`). The platform updates the property manager’s [balance settings](https://docs.stripe.com/api/balance-settings.md?api-version=preview) to:

- Set `payments.payouts.schedule.interval` to `daily` to make sure the automatic transfer rule can run.
- Set automatic_transfer_rules_by_currency to transfer all GBP funds from the payments balance to the financial account during scheduled payouts.

```curl
curl https://api.stripe.com/v1/balance_settings \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}" \
  -d "payments[payouts][schedule][interval]=daily" \
  -d "payments[payouts][automatic_transfer_rules_by_currency][gbp][0][payout_method]={{FINANCIALACCOUNTID_ID}}" \
  -d "payments[payouts][automatic_transfer_rules_by_currency][gbp][0][type]=transfer_all"
```

The platform listens for the `v2.money_management.received_credit.created` [webhook](https://docs.stripe.com/api/events/types.md?api-version=preview&rds=1#event_types-received_credit.created) to learn when the money movement has started, then lists financial accounts to verify balances:

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
      "id": "{{FINANCIAL_ACCOUNT_ID}}",
      "object": "v2.money_management.financial_account",
      "balance": {
        "available": { "gbp": { "value": 25000, "currency": "gbp" } },
        "inbound_pending": { "gbp": { "value": 0, "currency": "gbp" } },
        "outbound_pending": { "gbp": { "value": 0, "currency": "gbp" } }
      },
      "country": "GB",
      "status": "open",
      "storage": { "holds_currencies": ["gbp"] },
      "type": "storage",
      "livemode": false
    }
  ],
  "next_page_url": null,
  "previous_page_url": null
}
```

## Send a cross-border payment to a Norwegian property owner

The platform creates a recipient-configured connected account to represent the landlord in Norway that the property manager pays from the financial account. This set up follows the steps:

- Create a recipient-configured connected account.
- Onboard the recipient.
- Add a payout method using `OutboundSetupIntents`.
- Create an outbound payment quote (required for cross-border OutboundPayments).
- Create an outbound payment to the recipient using the payout method and quote.

### Create the landlord recipient account

The platform [creates a connected account](https://docs.stripe.com/api/v2/core/accounts/create.md) for the landlord in Norway with the `recipient` configurations and requests the associated capabilities. It specifies the property manager’s account ID in the `Stripe-Context` header to identify the landlord as an account of the property manager rather than a direct account of the platform.

```curl
curl -X POST https://api.stripe.com/v2/core/accounts \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "include": [
        "requirements"
    ],
    "contact_email": "owner.no@example.com",
    "display_name": "NO Property Owner",
    "identity": {
        "country": "no",
        "entity_type": "individual"
    },
    "configuration": {
        "recipient": {
            "capabilities": {
                "bank_accounts": {
                    "local": {
                        "requested": true
                    }
                }
            }
        }
    }
  }'
```

The response includes the account ID and any onboarding requirements:

```json
{
  "id": "{{RECIPIENT_ACCOUNT_ID}}",
  "object": "v2.core.account",
  "applied_configurations": ["recipient"],
  "configuration": {
    "recipient": {
      "capabilities": {
        "bank_accounts": {
          "local": {
            "requested": true,
            "status": "restricted",
            "status_details": [
              {
                "code": "requirements_past_due",
                "resolution": "provide_info"
              }
            ]
          }
        }
      }
    }
  },
  "display_name": "NO Property Owner",
  "requirements": {
    "collector": "stripe",
    "entries": [
      { "description": "identity.individual.date_of_birth.day", "impact": { "restricts_capabilities": [ { "capability": "bank_accounts.local", "configuration": "recipient", "deadline": { "status": "past_due" } } ] }, "minimum_deadline": { "status": "past_due" }, "awaiting_action_from": "user", "errors": [], "reference": null, "requested_reasons": [ { "code": "routine_onboarding" } ] },
      { "description": "identity.individual.date_of_birth.month", "impact": { "restricts_capabilities": [ { "capability": "bank_accounts.local", "configuration": "recipient", "deadline": { "status": "past_due" } } ] }, "minimum_deadline": { "status": "past_due" }, "awaiting_action_from": "user", "errors": [], "reference": null, "requested_reasons": [ { "code": "routine_onboarding" } ] },
      { "description": "identity.individual.date_of_birth.year", "impact": { "restricts_capabilities": [ { "capability": "bank_accounts.local", "configuration": "recipient", "deadline": { "status": "past_due" } } ] }, "minimum_deadline": { "status": "past_due" }, "awaiting_action_from": "user", "errors": [], "reference": null, "requested_reasons": [ { "code": "routine_onboarding" } ] },
      { "description": "identity.individual.given_name", "impact": { "restricts_capabilities": [ { "capability": "bank_accounts.local", "configuration": "recipient", "deadline": { "status": "past_due" } } ] }, "minimum_deadline": { "status": "past_due" }, "awaiting_action_from": "user", "errors": [], "reference": null, "requested_reasons": [ { "code": "routine_onboarding" } ] },
      { "description": "identity.individual.surname", "impact": { "restricts_capabilities": [ { "capability": "bank_accounts.local", "configuration": "recipient", "deadline": { "status": "past_due" } } ] }, "minimum_deadline": { "status": "past_due" }, "awaiting_action_from": "user", "errors": [], "reference": null, "requested_reasons": [ { "code": "routine_onboarding" } ] }
    ],
    "summary": { "minimum_deadline": { "status": "past_due", "time": null } }
  },
  "livemode": false
}
```

### Onboard the landlord

The platform then [onboards the recipient-configured connected account](https://docs.stripe.com/connect/api-onboarding.md) by:

1. Retrieving the requirements populated at account creation.
2. Providing a form to collect the information required.
3. Updating the `Account` with the collected information, specifying the connected account and recipient in the `Stripe-Context` header: `{{CONNECTED_ACCOUNT_ID}}/{{RECIPIENT_ACCOUNT_ID}}` to identify that the platform makes a request on behalf of its property manager’s landlord account.

After submitting required information, the platform confirms the recipient’s capabilities are `active` before proceeding.

```curl
curl -G https://api.stripe.com/v2/core/accounts/{{RECIPIENTACCOUNTID_ID}} \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  -d "include[0]=configuration.recipient" \
  -d "include[1]=requirements"
```

```json
{
  "id": "{{RECIPIENT_ACCOUNT_ID}}",
  "object": "v2.core.account",
  "configuration": {
    "recipient": {
      "capabilities": {
        "bank_accounts": {
          "local": {
            "requested": true,
            "status": "active"
          }
        }
      }
    }
  },
  "livemode": false,
  "requirements": {
    "collector": "stripe",
    "entries": [],
    "summary": { "minimum_deadline": { "status": "past_due", "time": null } }
  },
}
```

### Add a payout method

The platform creates a payout method for the landlord in Norway using an [OutboundSetupIntent](https://docs.stripe.com/api/v2/money-management/outbound-setup-intents.md?api-version=preview). The `Stripe-Context` header includes both the connected account and recipient: `{{CONNECTED_ACCOUNT_ID}}/{{RECIPIENT_ACCOUNT_ID}}` to identify the relationship: the platform making a request on behalf of its property manager’s landlord account.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_setup_intents \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "payout_method_data": {
        "type": "bank_account",
        "bank_account": {
            "country": "NO",
            "account_number": "NO9386011117947"
        }
    },
    "usage_intent": "payment"
  }'
```

The response includes the payout method ID:

```json
{
  "id": "osi_test_61SITWK7KhLsQIGAK16QsOpAPpE97EJALhqt1U5mC4kq",
  "object": "v2.money_management.outbound_setup_intent",
  "created": "2025-06-19T17:52:34.829Z",
  "payout_method": {
    "id": "{{RECIPIENT_PAYOUT_METHOD_ID}}",
    "object": "v2.money_management.payout_method"
  },
  "status": "succeeded",
  "usage_intent": "payment",
  "livemode": false
}
```

### Create an outbound payment quote

The platform creates an [OutboundPaymentQuote](https://docs.stripe.com/api/v2/money-management/outbound-payment-quotes/object.md?api-version=preview) that contains an foreign exchange (FX) rate and fees for this cross-border OutboundPayment. Cross-border OutboundPayments require the quote, and it provides estimated fees and exchange rates.

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
        "currency": "nok"
    },
    "amount": {
        "value": 10000,
        "currency": "gbp"
    }
  }'
```

The response includes the quote ID and FX details:

```json
{
  "id": "{{OUTBOUND_PAYMENT_QUOTE_ID}}",
  "object": "v2.money_management.outbound_payment_quote",
  "amount": {
    "value": 10000,
    "currency": "gbp"
  },
  "created": "2025-09-09T09:21:17.201Z",
  "estimated_fees": [
    {
      "amount": { "value": 50, "currency": "gbp" },
      "type": "standard_payout_fee"
    },
    {
      "amount": { "value": 200, "currency": "gbp" },
      "type": "foreign_exchange_fee"
    }
  ],
  "from": {
    "debited": { "value": 10250, "currency": "gbp" },
    "financial_account": "{{FINANCIAL_ACCOUNT_ID}}"
  },
  "fx_quote": {
    "lock_duration": "five_minutes",
    "lock_expires_at": "2025-09-09T09:26:17.000Z",
    "lock_status": "active",
    "rates": {
      "gbp": { "exchange_rate": "13.0000" }
    },
    "to_currency": "nok"
  },
  "to": {
    "credited": { "value": 130000, "currency": "nok" },
    "recipient": "{{RECIPIENT_ACCOUNT_ID}}"
  },
  "livemode": false
}
```

### Create the cross-border outbound payment to Norwegian recipient

The platform sends an [outbound payment](https://docs.stripe.com/treasury/connect/v2/moving-money/out-of/outbound-payments.md) from the property manager’s financial account to the recipient in Norway using the payout method and quote.

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
        "currency": "nok"
    },
    "amount": {
        "value": 10000,
        "currency": "gbp"
    },
    "outbound_payment_quote": "{{OUTBOUNDPAYMENTQUOTEID_ID}}",
    "description": "Monthly rental remittance to owner (NO)"
  }'
```

```json
{
  "id": "obp_test_65TMskH4DujCYIcfvYM16TMrTK0AE95w2xxtzb7EQQiNLM",
  "object": "v2.money_management.outbound_payment",
  "amount": {
    "value": 10000,
    "currency": "gbp"
  },
  "cancelable": true,
  "created": "2025-10-01T18:30:07.260Z",
  "delivery_options": { "bank_account": "automatic" },
  "description": "Streamer earnings",
  "expected_arrival_date": "2025-10-06T23:59:59.999Z",
  "from": {
    "debited": { "value": 10000, "currency": "gbp" },
    "financial_account": "{{FINANCIAL_ACCOUNT_ID}}"
  },
  "metadata": {},
  "outbound_payment_quote": "{% identifier type=\"outboundPaymentQuoteId\" /%}",
  "receipt_url": "https://qa-payments.stripe.com/transaction_receipt/session_test_61TMskHZxzTs1Q4Ls16TMrTK0AE95w2xxtzb7EQQi1AO",
  "recipient_notification": { "setting": "configured" },
  "statement_descriptor": "Property Management Inc.",
  "status": "processing",
  "status_transitions": {
    "canceled_at": null,
    "failed_at": null,
    "posted_at": null,
    "returned_at": null
  },
  "to": {
    "credited": { "value": 131129, "currency": "nok" },
    "payout_method": "{{RECIPIENT_PAYOUT_METHOD_ID}}",
    "recipient": "{{RECIPIENT_ACCOUNT_ID}}"
  },
  "trace_id": { "status": "pending", "value": "" },
  "livemode": false
}
```

