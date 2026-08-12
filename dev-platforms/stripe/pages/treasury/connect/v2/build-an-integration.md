---
title: "Build an integration with Treasury for platforms"
source: https://docs.stripe.com/treasury/connect/v2/build-an-integration.md
path: treasury/connect/v2/build-an-integration
---

# Build an integration with Treasury for platforms

Set up an end-to-end integration with Treasury for platforms and familiarize yourself with its basic concepts.

As a platform using [Connect](https://docs.stripe.com/connect.md), you can use Stripe Treasury for platforms to embed financial services in your product. Use this guide to learn basic concepts and endpoints to implement Treasury for platforms.

## Create a connected account

Begin in a [sandbox](https://docs.stripe.com/sandboxes.md) with access to Treasury for platforms and create a [v2 connected account](https://docs.stripe.com/api/v2/core/accounts.md) that you use to request capabilities to:

- Create financial accounts that can hold funds (`money_manager` configuration)
- Create a financial address to fund the financial account (`money_manager` configuration)
- Receive funds transfers (v1 transfers) from platform accounts (`recipient` configuration)
- Process card payments (`merchant` configuration)

To enable Treasury for platforms for a v1 Account, you can [specify a v1 Account in a v2 endpoint](https://docs.stripe.com/connect/accounts-v2/migrate-integration.md#use-v2-endpoints-for-all-your-accounts).

The account must not use a Stripe-hosted dashboard and you must be responsible for requirements collection.

```curl
curl -X POST https://api.stripe.com/v2/core/accounts \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  --json '{
    "include": [
        "configuration.money_manager"
    ],
    "contact_email": "test@example.com",
    "display_name": "John Smith",
    "identity": {
        "country": "gb",
        "entity_type": "individual"
    },
    "configuration": {
        "merchant": {
            "mcc": "8011",
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
                "outbound_payments": {
                    "bank_accounts": {
                        "requested": true
                    },
                    "financial_accounts": {
                        "requested": true
                    }
                },
                "outbound_transfers": {
                    "bank_accounts": {
                        "requested": true
                    },
                    "financial_accounts": {
                        "requested": true
                    }
                },
                "inbound_transfers": {
                    "bank_accounts": {
                        "requested": true
                    }
                },
                "received_debits": {
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

The response includes the connected account ID.

```json
{
  "id": "acct_123",
  "object": "v2.core.account",
  "applied_configurations": [
    "merchant",
    "money_manager"
  ],
  "configuration": {
    "customer": null,
    "merchant": null,
    "recipient": null,
    "money_manager": {
      "capabilities": {
        "received_credits": {
          "bank_accounts": {
            "requested": true,
            "status": "restricted",
            "status_details": [
              {
                "code": "requirements_past_due",
                "resolution": "provide_info"
              }
            ]
          }
        },
        "business_storage": {
          "inbound": {
            "gbp": {
              "requested": true,
              "status": "restricted",
              "status_details": [
                {
                  "code": "requirements_past_due",
                  "resolution": "provide_info"
                }
              ]
            }
          },
          "outbound": {
            "gbp": {
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
        },
        "outbound_payments": {
          "bank_accounts": {
            "requested": true,
            "status": "restricted",
            "status_details": [
              {
                "code": "requirements_past_due",
                "resolution": "provide_info"
              }
            ]
          },
          "financial_accounts": {
            "requested": true,
            "status": "restricted",
            "status_details": [
              {
                "code": "requirements_past_due",
                "resolution": "provide_info"
              }
            ]
          }
        },
        "outbound_transfers": {
          "bank_accounts": {
            "requested": true,
            "status": "restricted",
            "status_details": [
              {
                "code": "requirements_past_due",
                "resolution": "provide_info"
              }
            ]
          },
          "financial_accounts": {
            "requested": true,
            "status": "restricted",
            "status_details": [
              {
                "code": "requirements_past_due",
                "resolution": "provide_info"
              }
            ]
          }
        },
        "inbound_transfers": {
          "bank_accounts": {
            "requested": true,
            "status": "restricted",
            "status_details": [
              {
                "code": "requirements_past_due",
                "resolution": "provide_info"
              }
            ]
          }
        },
        "received_debits": {
          "bank_accounts": {
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
  "contact_email": "test@example.com",
  "created": "2025-06-18T00:48:16.000Z",
  "dashboard": "none",
  "identity": null,
  "defaults": null,
  "display_name": "John Smith",
  "metadata": {},
  "requirements": null,
  "livemode": false
}
```

## Onboard the connected account

After you create an account, [onboard its seller or service provider](https://docs.stripe.com/connect/api-onboarding.md) by:

1. Retrieving the requirements populated at account creation.
2. Providing a form to collect the information required from your connected account.
3. Updating the `Account` with the collected information.

Alternatively, you can create an [account link](https://docs.stripe.com/connect/hosted-onboarding.md?accounts-namespace=v2&lang=curl#create-account-link) specifying the `type` as the `merchant` and `money_manager` configurations, then send the returned URL to your connected account so they can provide the required information in a Stripe-hosted interface.

## Create a financial account and financial address

Treasury for platforms uses [FinancialAccount](https://docs.stripe.com/api/v2/money-management/financial-accounts/object.md?api-version=preview) objects to store funds, manage your money, and use Stripe services for making payments or receiving money. The `Stripe-Context` header is `{{CONNECTED_ACCOUNT_ID}}`. See [Stripe-Context header](https://docs.stripe.com/context.md) for more information on API request contexts. You can use the FinancialAccount API to create a Financial Account.

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
    },
    "metadata": {
        "purpose": "holds_money_for_payouts"
    }
  }'
```

The response includes the ID of the financial account.

```json
{
  "id": "fa_test_123",
  "object": "v2.money_management.financial_account",
  // The available balance shows money that can be used.
  "balance": {
    "available": {
      "gbp": {
        "value": 78,
        "currency": "gbp"
      }
    },
    "inbound_pending": {
      "gbp": {
        "value": 0,
        "currency": "gbp"
      }
    },
    "outbound_pending": {
      "gbp": {
        "value": 0,
        "currency": "gbp"
      }
    }
  },
  "country": "GB",
  "created": "2025-06-18T11:05:27.930Z",
  "metadata": null,
  "other": null,
  // The status can be `open`, `closed` or `pending`
  "status": "pending",
  "status_details": null,
  "storage": {
    "holds_currencies": [
      "gbp"
    ]
  },
  "metadata": {
    "purpose": "holds_money_for_payouts"
  },
  "type": "storage",
  "livemode": false
}
```

Create a [Financial Address](https://docs.stripe.com/api/v2/money-management/financial-addresses.md?api-version=preview) to assign bank details to your financial account you can share with customers or partners so they can send funds directly to the financial account. Specify the `type` corresponding to the country of the financial account to make sure we provision the correct [address credentials](https://docs.stripe.com/api/v2/money-management/financial-addresses/object.md?api-version=preview#v2_financial_address_object-credentials) (such as a US routing number or a British sort code).

After you create a financial address, it starts in a `pending` status while Stripe provisions the bank details. When the status becomes `active`, you can retrieve the credentials (bank details) and share them to receive funds. You can monitor incoming funds using [received credits](https://docs.stripe.com/treasury/connect/v2/moving-money/fund-a-financial-account.md#monitor-received-credits).

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

## Fund the financial account

Simulate receiving funds through the financial address using the [test helper](https://docs.stripe.com/api/v2/money-management/financial-addresses/credit.md?api-version=preview) in a sandbox instead of [funding in live mode](https://docs.stripe.com/treasury/connect/v2/moving-money/fund-a-financial-account.md#external-account) using an external bank account.

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

The response indicates if the simulation was successful:

```json
{
  "object": "financial_address_credit_simulation",
  "status": "accepted",
  "livemode": false
}
```

This creates a [ReceivedCredit](https://docs.stripe.com/treasury/connect/v2/moving-money/fund-a-financial-account.md#monitor-received-credits) object, which represents incoming money movements into a financial account. Use the [Retrieve Financial Account](https://docs.stripe.com/api/v2/money-management/financial-accounts/retrieve.md?api-version=preview) endpoint to verify that funds have landed in the financial account.

```curl
curl https://api.stripe.com/v2/money_management/financial_accounts/{{FINANCIALACCOUNTID_ID}} \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

The response includes different types of [balances](https://docs.stripe.com/treasury/connect/v2/account-management/financial-accounts.md#balances). The available balance shows the 250 GBP you funded.

```json
{
  "id": "{{FINANCIAL_ACCOUNT_ID}}",
  "object": "v2.money_management.financial_account",
  "balance": {
    "available": {
      "gbp": {
        "value": 250,
        "currency": "gbp"
      }
    },
    "inbound_pending": {
      "gbp": {
        "value": 0,
        "currency": "gbp"
      }
    },
    "outbound_pending": {
      "gbp": {
        "value": 0,
        "currency": "gbp"
      }
    }
  },
  "country": "GB",
  "created": "2025-06-11T13:01:21.289Z",
  "metadata": null,
  "other": null,
  "status": "open",
  "status_details": null,
  "storage": {
    "holds_currencies": [
      "gbp"
    ]
  },
  "type": "storage",
  "livemode": false
}
```

## Create a recipient

To make an outbound payment to a third party from a connected account, create a recipient-configured [v2 Account](https://docs.stripe.com/api/v2/core/accounts/create.md).

```curl
curl -X POST https://api.stripe.com/v2/core/accounts \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "contact_email": "jenny.rosen@stripe.com",
    "display_name": "Jenny Rosen",
    "identity": {
        "country": "GB",
        "entity_type": "individual",
        "individual": {
            "given_name": "Jenny",
            "legal_gender": "female",
            "surname": "Rosen"
        }
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
    },
    "include": [
        "requirements",
        "configuration.recipient",
        "identity"
    ]
  }'
```

The response includes the recipient account ID and requested capabilities.

```json
{
  "id": "acct_6789",
  "object": "v2.core.account",
  "applied_configurations": [
    "recipient"
  ],
  "configuration": {
    "customer": null,
    "merchant": null,
    "recipient": {
      "capabilities": {
        "bank_accounts": {
          "local": {
            "requested": true,
            "status": "active",
            "status_details": []
          },
          "wire": null
        },
        "cards": null,
        "stripe_balance": null
      },
      "default_outbound_destination": null
    },
    ...
```

## Onboard the recipient

Onboard a recipient-configured account in the same way you [onboard connected accounts](https://docs.stripe.com/treasury/connect/v2/build-an-integration.md#onboard-the-connected-account) with other types of configurations.

## Create a payout method

Create a payout method for the recipient using an [OutboundSetupIntent](https://docs.stripe.com/api/v2/money-management/outbound-setup-intents.md?api-version=preview). Include both the connected account and recipient in the `Stripe-Context` header to identify that you’re making a request on behalf of your connected account for its recipient account: `{{CONNECTED_ACCOUNT_ID}}/{{RECIPIENT_ACCOUNT_ID}}`.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_setup_intents \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "payout_method_data": {
        "type": "bank_account",
        "bank_account": {
            "country": "GB",
            "account_number": "NO9386011117947"
        }
    },
    "usage_intent": "payment"
  }'
```

The response includes the payout method ID:

```json
{
  "id": "osi_test_64SITWA7KhLsQIGAK16QsOpAPpE97EJALhqt1U5mC4kq",
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

## Pay the recipient

Onboarding a recipient-configured connected account attaches a [PayoutMethod](https://docs.stripe.com/api/v2/money-management/payout-methods/object.md?api-version=preview) to their account that represents their banking account and allows you to make recurring payouts. [Retrieve the recipient’s payout method](https://docs.stripe.com/api/v2/money-management/payout-methods/list.md?api-version=preview) to use the ID in your payout.

The Stripe-Context header in this request is the path `{{CONNECTED_ACCOUNT_ID}}/{{RECIPIENT_ACCOUNT_ID}}`.

```curl
curl https://api.stripe.com/v2/money_management/payout_methods \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-07-29.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

[Create an Outbound Payment](https://docs.stripe.com/api/v2/money-management/outbound-payments/create.md?api-version=preview) to move the money from your financial account to the recipient’s payout method banking account.

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
        "value": 100,
        "currency": "gbp"
    },
    "description": "Payout from a platform financial account to connected account financial account"
  }'
```

The response includes the outbound payment ID and transaction details.

```json
{
  "id": "obp_test_65SlAavriewxesYj6PN16SiAU68AE9NQclWBzpoRJEmCR6",
  "object": "v2.money_management.outbound_payment",
  "amount": {
    "value": 100,
    "currency": "gbp"
  },
  "cancelable": false,
  "created": "2025-06-19T17:52:34.829Z",
  "delivery_options": null,
  "description": "Payout from a platform financial account to connected account financial account",
  "expected_arrival_date": "2025-06-19T17:52:34.803Z",
  "from": {
    "debited": {
      "value": 100,
      "currency": "gbp"
    },
    "financial_account": "{{FINANCIAL_ACCOUNT_ID}}"
  },
  "metadata": {},
  "receipt_url": "https://payments.stripe.com/transaction_receipt/…",
  "recipient_notification": {
    "setting": "configured"
  },
  "statement_descriptor": "Treasury Sandbox",
  "status": "posted",
  "status_details": null,
  "status_transitions": {
    "canceled_at": null,
    "failed_at": null,
    "posted_at": "2025-06-19T17:52:34.852Z",
    "returned_at": null
  },
  "to": {
    "credited": {
      "value": 78,
      "currency": "gbp"
    },
    "payout_method": "{{RECIPIENT_PAYOUT_METHOD_ID}}",
    "recipient": "{{RECIPIENT_ACCOUNT_ID}}"
  },
  "trace_id": {
    "status": "pending",
    "value": ""
  },
  "livemode": false
}
```

Learn more about [outbound payments](https://docs.stripe.com/treasury/connect/v2/moving-money/out-of/outbound-payments.md).

## Webhooks

Listen for and handle [v2.money_management events](https://docs.stripe.com/treasury/connect/v2/account-management/financial-accounts.md#webhooks) related to financial account activity.

