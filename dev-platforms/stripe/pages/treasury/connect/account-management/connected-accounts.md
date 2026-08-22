---
title: "Connected account financial accounts"
source: https://docs.stripe.com/treasury/connect/account-management/connected-accounts.md
path: treasury/connect/account-management/connected-accounts
---

# Connected account financial accounts

Request money_manager capabilities and collect onboarding requirements for your connected accounts.

To use Treasury for platforms, you must have a Stripe [Connect](https://docs.stripe.com/connect.md) integration where your platform account provides Stripe functionality to its connected accounts. Each connected account exists as an [Account](https://docs.stripe.com/api/v2/core/accounts.md) object in the Accounts v2 API and its access to Stripe functionality is defined by its configuration capabilities, such as `merchant`, `customer`, `recipient`, or `money_manager`.

- The [merchant](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=preview#v2_create_accounts-configuration-merchant) configuration allows the connected account to accept payments from its own customers.
- The [customer](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=preview#v2_create_accounts-configuration-customer) configuration allows the connected account to pay your platform or one of your merchant-configured connected accounts.
- The [recipient](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=preview#v2_create_accounts-configuration-recipient) configuration allows the connected account to receive payouts from you or one of your merchant-configured connected accounts.
- The [money_manager](https://docs.stripe.com/api/v2/core/accounts/create.md?api-version=preview#v2_create_accounts-configuration-money_manager) configuration allows the connected account to use financial accounts to manage their Stripe balance.
- The `card_creator` configuration allows the connected account to create and issue cards to users.

As the platform, you can provision any combination of configuration capabilities to your connected accounts. Different capabilities have different onboarding requirements. Whether you create or update connected accounts to request the capabilities needed for Treasury for platforms, you must collect required information from the connected account before they can use the corresponding functionality.

To enable Treasury for platforms for an existing v1 Account, you can [specify the v1 Account ID in a v2 endpoint](https://docs.stripe.com/connect/accounts-v2/migrate-integration.md#use-v2-endpoints-for-all-your-accounts).

## Eligibility

When you request capabilities associated with the [money_manager](https://docs.stripe.com/treasury/connect/account-management/connected-accounts.md#update-a-connected-account-to-request-a-new-capability) configuration for a connected account, Stripe reviews the account’s provided URL or product description to make sure it complies with our requirements and those of our partners.

Some existing connected accounts might produce an inconclusive review because of insufficient information. For example, connected accounts with multiple owners with ownership stake exceeding 25% might have to provide additional information about each owner.

To reduce the chance of inconclusive reviews, make sure that your connected account onboarding process collects valid URLs and comprehensive product descriptions.

Connected accounts must meet the following requirements to be supported for Treasury for platforms:

- The connected account must be based in a supported region.
- The account must provide either a valid, publicly accessible URL or a product description of at least 10 characters (we recommend more than 30 characters to minimize review delays).
- The account representative must be based in the same country as the account.

## Create a new connected account

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
        "country": "US",
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
        "currency": "usd",
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
            "usd": {
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
            "usd": {
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

## Update a connected account to request a new capability

If you already have an eligible connected account, you can request to add `money_manager` capabilities:

```curl
curl -X POST https://api.stripe.com/v2/core/accounts/{{CONNECTEDACCOUNT_ID}} \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-06-24.preview" \
  --json '{
    "include": [
        "configuration.money_manager"
    ],
    "configuration": {
        "money_manager": {
            "capabilities": {
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
                }
            }
        }
    }
  }'
```

## How capabilities work

To activate a capability, you must first request it by setting its requested property to true. This triggers collection of the capability’s requirements, which is handled by your platform. Requirements can involve identity and compliance documentation, and risk data. When Stripe verifies that a capability’s requirements are fulfilled, it becomes active.

### Available capabilities

| Capability | Description | Configuration |
| --- | --- | --- |
| `card_payments` | Allows the merchant to accept card payments. | `merchant` |
| `received_credits.bank_accounts` | Allows you to create a [Financial Address](https://docs.stripe.com/api/v2/money-management/financial-addresses.md?api-version=preview) for financial accounts to receive inbound credits. | `money_manager` |
| `business_storage.inbound.{currency}` / `business_storage.outbound.{currency}` | List of the currencies which can be held in the financial accounts of the connected account. You must request both inbound and outbound for each currency. | `money_manager` |
| `outbound_payments.bank_accounts` | Send funds from a financial account to a bank account owned by a different entity. | `money_manager` |
| `outbound_payments.financial_accounts` | Send funds from a financial account to a financial account owned by a different entity. | `money_manager` |
| `outbound_transfers.bank_accounts` | Transfer funds from a financial account to a bank account owned by the same entity. | `money_manager` |
| `outbound_transfers.financial_accounts` | Transfer funds from a financial account to another financial account owned by the same entity. | `money_manager` |
| `inbound_transfers.bank_accounts` | Pull funds into a financial account from an external bank account owned by the same entity. | `money_manager` |
| `received_debits.bank_accounts` | Allow a financial account to be debited from an external bank account. | `money_manager` |
| `stripe_balance` | Allows a recipient to manage their Stripe balance. | `recipient` |
| `stripe_transfers` | Allows a recipient to receive transfers into their Stripe balance. | `recipient` |
| `commercial` | Allows creation of issuing cards for commercial purchases. | `card_creator` |
| `consumer` | Allows creation of issuing cards for consumer purchases. | `card_creator` |

### Requirements

Requested capabilities sometimes trigger additional onboarding requirements beyond those needed for accepting payments as a `merchant` or receiving payouts as a `recipient`. Each requirement imposed on a connected account includes the following information:

- The type of information needed to fulfill the requirement.
- Why Stripe needs the information.
- Whether the requirement is overdue (the deadline can be a date or some other type of threshold, such as a certain volume of payments).
- Consequences that Stripe imposes (such as suspending certain functionality or stopping payouts from the Stripe balance for the account) at the deadline if we can’t verify the information.
- Who must take action.

Individuals, sole proprietorships or companies (LLCs, corporations, non-profits, and so on) using Treasury for platforms with `money_manager` capabilities must provide the following information:

**Entity details**

- Business names (customer facing and legal)
- Legal entity type
- Business address
- Business phone number
- Product or service description
- Industry or Merchant category code
- Treasury for platforms terms of service acceptance
- Stripe terms of service acceptance

**Owner details**

- Legal name
- Date of birth
- Residential address
- SSN or TIN (US only)

### Check capability status

Check for one of the following status results in the API or Dashboard:

#### Dashboard

1. Open the [Connected accounts page](https://dashboard.stripe.com/connect/accounts) in the Dashboard.
2. Use the filters to show the accounts that you requested financial account capabilities for.
3. Click an account to view its details page and its capabilities status:
   - **Active**: The connected account has no outstanding requirements and can access Treasury for platforms features.
   - **Pending**: We’re still evaluating the connected account and it can’t access Treasury for platforms features yet.
   - **Inactive**: The connected account has outstanding requirements for financial account capabilities and can’t access Treasury for platforms features yet.
   - **Restricted**: The connected account doesn’t meet the requirements and can’t access Treasury for platforms features.
4. Address outstanding **Actions required** items for inactive capabilities or to appeal a [prohibited or restricted business](https://stripe.com/legal/restricted-businesses) designation. You can do so by providing additional business details about the account or confirming that the account no longer offers the prohibited products or services. If Stripe upholds the determination after your appeal, the capabilities remain `restricted`.

#### API

1. [Retrieve the connected account](https://docs.stripe.com/api/v2/core/accounts/retrieve.md?api-version=preview).

   ```curl
   curl -G https://api.stripe.com/v2/core/accounts/{{CONNECTEDACCOUNT_ID}} \
     -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
     -H "Stripe-Version: 2026-06-24.preview" \
     -d "include[0]=configuration.money_manager" \
     -d "include[1]=requirements"
   ```

2. Inspect the `requirements` and `configuration.money_manager` capabilities for the following status information:

   - `active`: The connected account has no outstanding requirements and can access Treasury for platforms features.
   - `pending`: We’re still evaluating the connected account and it can’t access Treasury for platforms features yet.
   - `restricted`: The connected account doesn’t meet the requirements and can’t access Treasury for platforms features. The status includes the `status_details.code` of `rejected.unsupported_business`.

#### URL errors

If the URL you provide for the connected account returns one of the following errors, resolve the issue before requesting capabilities:

- `invalid_url_format`: Update the URL to a valid format (for example, `.com` or `.org`).
- `invalid_url_denylisted`: The URL is on a denylist. Contact [Treasury support](mailto:treasury-support@stripe.com).
- `invalid_url_website_inaccessible`: The URL might require a password. The connected account’s website must be publicly accessible.
- `invalid_url_website_incomplete`: The URL returns a `404` error.
- `invalid_url_website_other`: Contact [Treasury support](mailto:treasury-support@stripe.com).

If the URL continues to return errors or you can’t resolve the issue, submit a product description instead.

## Onboard the connected account

After you create an account, [onboard its seller or service provider](https://docs.stripe.com/connect/api-onboarding.md) by:

1. Retrieving the requirements populated at account creation.
2. Providing a form to collect the information required from your connected account.
3. Updating the `Account` with the collected information.

Alternatively, you can create an [account link](https://docs.stripe.com/connect/hosted-onboarding.md?accounts-namespace=v2&lang=curl#create-account-link) specifying the `type` as the `merchant` and `money_manager` configurations, then send the returned URL to your connected account so they can provide the required information in a Stripe-hosted interface.

## Specify payout methods for recipient accounts 

For recipient-configured connected accounts, create a `PayoutMethod` to make recurring [outbound payments](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-payments.md) using the recipient’s preferred credentials.

Hosted onboarding collects a recipient’s payout method, but you can add additional payout methods or complete country-specific actions, if needed.

- Use the [OutboundSetupIntents API](https://docs.stripe.com/api/v2/money-management/outbound-setup-intents.md?api-version=preview) to create payout methods globally. OutboundSetupIntent (OSI) supports creating bank account payout methods in more than 50 countries, and returns a `payout_method` that you can use for payments and transfers. OSI can also retrieve `next_action` requirements (for example, Confirmation of Payee in GB).
- Use country-specific endpoints to add features to the payout method that OSI doesn’t capture, such as [GB Bank Accounts](https://docs.stripe.com/api/v2/core/vault/gb-bank-accounts.md?api-version=preview) to initiate or acknowledge GB Confirmation of Payee.

Use the `Stripe-Context` header with `{{CONNECTED_ACCOUNT_ID}}/{{RECIPIENT_ACCOUNT_ID}}` to identify the connected account you’re making the request for.

### Add payout methods with the API

You can add payout methods that collect the credentials required for different countries.

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

### List payout methods

You can list all payout methods for a connected account using the [Payout Methods v2 API](https://docs.stripe.com/api/v2/money-management/payout-methods/list.md?api-version=preview). Review properties such as `available_payout_speeds`, `enabled_delivery_options`, and `usage_status` to help you determine how to use them.

```curl
curl https://api.stripe.com/v2/money_management/payout_methods \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-07-29.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

## Webhooks

When the status of requested capabilities change for a connected account, you receive a `v2.core.account[configuration.money_manager].capability_status_updated` [webhook](https://docs.stripe.com/webhooks.md) confirming the change:

```json
{
  "created": "2025-06-18T02:08:15.025Z",
  "id": "evt_test_321",
  "object": "v2.core.event",
  "type": "v2.core.account[configuration.money_manager].capability_status_updated",
  "data": {
    "updated_capability": "business_storage.outbound.usd"
  },
  "related_object": {
    "id": "{{CONNECTED_ACCOUNT_ID}}",
    "type": "v2.core.account",
    "url": "/v2/core/accounts/{{CONNECTED_ACCOUNT_ID}}?include=configuration.money_manager"
  },
  "changes": ...,
  ...
}
```

## See also

- [Build an integration](https://docs.stripe.com/treasury/connect/build-an-integration.md)
- [Financial accounts](https://docs.stripe.com/treasury/connect/account-management/financial-accounts.md)

