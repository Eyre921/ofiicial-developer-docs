---
title: "Send money to recipients and financial accounts you don’t own"
source: https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-payments.md
path: treasury/connect/moving-money/out-of/outbound-payments
---

# Send money to recipients and financial accounts you don't own

Move money from platform or connected account financial accounts to third parties.

To move funds between financial accounts and other accounts owned by the same entity, use [OutboundTransfers](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-transfers.md) instead.

Treasury for platform users can send money from their financial account to other recipients using the following types of transactions:

- Payouts from a platform’s or connected account’s financial account to a third-party recipient.
- Payments from a platform’s financial account to a connected account’s financial account.
- Payments between financial accounts owned by different connected accounts under the same platform.
- Payments from a connected account’s financial account to its platform’s financial account.

## Compare integrations 

You can send money from a financial account to a third-party recipient using the Payout Intents API or Outbound Payments API.

| Feature | Payout Intents API (Private preview) | Outbound Payments API |
| --- | --- | --- |
| Process | Provides a staged process, from preparation and review to delivery and handling failures. Supports:
- Fee and exchange rate preview
- Payout scheduling
- Failed and returned payout handling | Creates a single payout attempt that Stripe sends immediately. Use it:
- If your integration already handles payout decisions and failures
- For payments to financial accounts owned by a different connected account or platform |
| Delivery | You can configure manual or automatic confirmation. | Stripe automatically sends the payment upon creation. |
| Fees and currency conversion | Includes estimated fees and the exchange rate quote. | Requires an [OutboundPaymentQuote](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-payments.md#cross-border-outbound-payment) to preview fees, exchange rates, and amounts. |
| Scheduling | You can schedule the payout on a future date. | Not supported. |
| Failed and returned payouts | The PayoutIntent status changes to `requires_action`. You can retry, make changes and then retry, or cancel. If a scheduled payout fails, create a new PayoutIntent instead of retrying it. | The OutboundPayment status changes to `failed` or `returned`. Create a new OutboundPayment to retry. |

## Before you begin

- [Create a recipient](https://docs.stripe.com/treasury/connect/build-an-integration.md#create-a-recipient) with `active` capabilities for relevant networks like `bank_accounts.local` and `bank_accounts.ach`.

- [Look up the recipient’s payout method](https://docs.stripe.com/treasury/connect/account-management/connected-accounts.md#list-payout-methods). For paper checks, first follow the payout method setup instructions for [Payout Intents](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-payments.md?payout-api=payout-intents#check-send-payout-method-payout-intents) or [Outbound Payments](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-payments.md?payout-api=outbound-payment#create-a-check-send-payout-method).

  > #### Check confirmation of payee
  > 
  > For payouts or payments to a UK bank account in GBP, make sure the payout method includes the [Confirmation of Payee](https://docs.stripe.com/treasury/connect/account-management/connected-accounts.md?t4p-geo=uk#recipient-payout-methods).

- [Look up the sending financial account ID](https://docs.stripe.com/api/v2/money-management/financial-accounts.md?api-version=preview).

#### Payout Intents

> #### Request access
> 
> PayoutIntents require separate access in addition to Treasury for platforms. If you already use Treasury for platforms, [request access](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-payments.md#payout_intents_preview) to confirm eligibility for your platform and sending connected accounts.
> 
> ### Get access to PayoutIntents.
> 
> Enter your email to request access.
> 
> ```bash
> curl https://docs.stripe.com/preview/register \
>   -X POST \
>   -H "Content-Type: application/json" \
>   -H "Referer: https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-payments" \
>   -d '{"email": "EMAIL", "preview": "payout_intents_preview"}'
> ```

## Create a PayoutIntent 

When you create a PayoutIntent, you can specify a set of `preferred_networks` to process the payout. Stripe chooses the most appropriate network from your list based on factors like region, currency, and recipient payout method.

Set `confirmation_method` to `manual` to review the payout before Stripe sends it. Set it to `automatic` to send immediately.

Use the `Stripe-Context` header to submit requests on behalf of your connected account. Omit the header to send payouts from your platform’s financial account.

```curl
curl -X POST https://api.stripe.com/v2/money_management/payout_intents \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "to": {
        "recipient": "{{RECIPIENTACCOUNTID_ID}}",
        "payout_method": "{{RECIPIENTPAYOUTMETHODID_ID}}",
        "payout_method_options": {
            "bank_account": {
                "preferred_networks": [
                    "ach"
                ]
            }
        }
    },
    "amount": {
        "value": 1999,
        "currency": "usd"
    },
    "confirmation_method": "manual",
    "description": "Streamer earnings"
  }'
```

### Set additional ACH options 

If you set ACH as a preferred network, you can also set the following ACH options to control how Stripe sends the payout:

- `transaction_purpose`: Set to `payroll` for payroll payouts. NACHA rules require originators to identify payroll payouts to recipients in the US.

```curl
curl -X POST https://api.stripe.com/v2/money_management/payout_intents \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "to": {
        "recipient": "{{RECIPIENTACCOUNTID_ID}}",
        "payout_method": "{{RECIPIENTPAYOUTMETHODID_ID}}",
        "payout_method_options": {
            "bank_account": {
                "preferred_networks": [
                    "ach"
                ],
                "preferred_network_options": {
                    "ach": {
                        "transaction_purpose": "payroll"
                    }
                }
            }
        }
    },
    "amount": {
        "value": 1999,
        "currency": "usd"
    },
    "description": "Payroll"
  }'
```

### Schedule a payout 

To schedule a payout, omit `confirmation_method` and set `schedule_options.execute_on` to a date in `YYYY-MM-DD` format between tomorrow and 180 days from today. You can’t schedule a PayoutIntent that requires confirmation, whether automatic or manual.

The PayoutIntent stays in a `pending` state until Stripe sends the payout on your specified date at 09:00 in the local time zone of the sending account. Funds arrival time depends on the payment network.

You can [update the PayoutIntent](https://docs.stripe.com/api/v2/money-management/payout-intents/update.md?api-version=preview) any time before the scheduled send date.

Stripe doesn’t hold funds for a scheduled payout. If your financial account doesn’t have enough funds on the scheduled date, the PayoutIntent updates to `requires_action` with `next_action.handle_failure.failure_reason` set to `insufficient_funds`. Add funds and create a new PayoutIntent.

### Send a paper check  (Private preview)
Available in: US
> #### Request access
> 
> Check send requires separate access in addition to Treasury for platforms. If you already use Treasury for platforms, contact your Stripe representative to request this feature.

Before sending a paper check, request the following capabilities and confirm that both have an `active` status:

- `configuration.money_manager.capabilities.outbound_payments.paper_checks` on the Account that owns the sending financial account.
- `configuration.recipient.capabilities.paper_checks` on the recipient Account.

#### Create a Check Send payout method 

Create a reusable payout method with an [OutboundSetupIntent](https://docs.stripe.com/api/v2/money-management/outbound-setup-intents/create.md?api-version=preview). Set `payout_method_data.type` to `check_send` and `usage_intent` to `payment`. Provide the name printed on the check in `payout_method_data.check_send.payee_name`, up to 35 characters, and the US mailing address in `payout_method_data.check_send.mailing_address`.

For a recipient of a connected account, set the `Stripe-Context` header to `{{CONNECTED_ACCOUNT_ID}}/{{RECIPIENT_ACCOUNT_ID}}`. For a recipient of your platform, use `{{RECIPIENT_ACCOUNT_ID}}` alone. Store your API key securely. See [best practices for managing secret keys](https://docs.stripe.com/keys-best-practices.md).

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_setup_intents \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "payout_method_data": {
        "type": "check_send",
        "check_send": {
            "payee_name": "Jenny Rosen",
            "mailing_address": {
                "line1": "27 Fredrick Ave",
                "city": "Brothers",
                "state": "OR",
                "postal_code": "97712",
                "country": "US"
            }
        }
    },
    "usage_intent": "payment"
  }'
```

After successful creation, the `OutboundSetupIntent` has status `succeeded`. Save the response’s `payout_method.id` (`chksend_...`) to use as `to.payout_method` for each check sent to that destination. A recipient can have multiple check payout methods.

#### Create the PayoutIntent 

Create a `PayoutIntent` with the recipient Account ID in `to.recipient`.

Set `to.payout_method` to the saved `chksend_...` ID and provide a sender signature, up to 30 characters, in `to.payout_method_options.check_send.signature`. You can also provide a memo, up to 100 characters, in `to.payout_method_options.check_send.memo`. Stripe prints both on the check. Set `to.payout_method_options.check_send.shipping_speed` to `standard` or `priority`. The default is `standard`.

For a connected account’s payment, set `Stripe-Context` to the connected account ID alone. Omit the header to send from your platform’s financial account.

```curl
curl -X POST https://api.stripe.com/v2/money_management/payout_intents \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "to": {
        "recipient": "{{RECIPIENTACCOUNTID_ID}}",
        "payout_method": "chksend_...",
        "payout_method_options": {
            "check_send": {
                "signature": "Jenny Rosen",
                "memo": "Streamer earnings",
                "shipping_speed": "standard"
            }
        }
    },
    "amount": {
        "value": 1999,
        "currency": "usd"
    },
    "description": "Streamer earnings"
  }'
```

To review the payout before Stripe sends it, set `confirmation_method` to `manual` and [confirm the payout](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-payments.md#review-confirm-payout-intent) when you’re ready. After creation, [inspect the payout status](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-payments.md#inspect-payout-intent) and [handle any required action](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-payments.md#handle-required-action).

#### Add attachments to a paper check 

You can include a PDF attachment with a paper check, such as an invoice or receipt. Stripe supports PDF files only. The maximum page count depends on the shipping speed: 5 pages for standard shipping and 50 pages for priority shipping.

Upload the file with the [Files API](https://docs.stripe.com/api/files.md) and set `purpose` to `check_send_attachment`. For a connected account’s payment, include the `Stripe-Account` header with the ID of the connected account that owns the sending financial account. Omit the header for your platform’s payment.

```bash
curl https://files.stripe.com/v1/files \
  -u "{{SECRET_KEY}}:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -F purpose=check_send_attachment \
  -F "file=@/path/to/document.pdf"
```

Pass the returned file ID in `to.payout_method_options.check_send.attachment_file` when you create the `PayoutIntent`.

```curl
curl -X POST https://api.stripe.com/v2/money_management/payout_intents \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "to": {
        "recipient": "{{RECIPIENTACCOUNTID_ID}}",
        "payout_method": "chksend_...",
        "payout_method_options": {
            "check_send": {
                "signature": "Jenny Rosen",
                "memo": "Streamer earnings",
                "shipping_speed": "standard",
                "attachment_file": "{{FILE_ID}}"
            }
        }
    },
    "amount": {
        "value": 1999,
        "currency": "usd"
    },
    "description": "Streamer earnings"
  }'
```

## Review and confirm the PayoutIntent 

A PayoutIntent can require confirmation because you requested it or because a regulatory requirement mandates it. In either case, the PayoutIntent `status` becomes `requires_action` with `next_action.type` set to `confirm`. The confirmation reason is `manually_requested` or `automatically_required`.

Review the following fields on the PayoutIntent:

- `estimated_fees`: The estimated fees for the payout, by fee type.
- `fx_quote`: For payouts that convert currencies, the exchange rate.
- `fx_quote.lock_expires_at`: For locked rates, the lock expiration.
- `fx_quote.lock_status`: For locked rates, whether the rate is `active` or `expired`.
- `from.debited` and `to.credited`: The estimated amounts debited from your financial account and credited to the recipient, with the exchange rate applied.

When you’re ready to send the funds, [confirm the PayoutIntent](https://docs.stripe.com/api/v2/money-management/payout-intents/confirm.md?api-version=preview).

```curl
curl -X POST https://api.stripe.com/v2/money_management/payout_intents/poi_1234/confirm \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

### Handle expired exchange rates 

If the exchange rate lock expires before you confirm, the request fails with `payout_intent_fx_quote_expired`. Get a new rate with [refresh FX quote](https://docs.stripe.com/api/v2/money-management/payout-intents/fx-quote.md?api-version=preview), review the updated `fx_quote`, amounts, and `estimated_fees`, then confirm again.

```curl
curl -X POST https://api.stripe.com/v2/money_management/payout_intents/poi_1234/refresh_fx_quote \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

## Handle payouts that require action 

Listen for the `v2.money_management.payout_intent.requires_action` event so you can respond based on the `next_action.type`:

- `confirm`: You must [review and confirm the payout](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-payments.md#review-confirm-payout-intent).
- `handle_failure`: The payout failed or was returned because of the `next_action.handle_failure.failure_reason`, such as `insufficient_funds` or `payout_method_closed`.

### Update the PayoutIntent 

Stripe doesn’t retry or reroute payouts automatically. You can [update a PayoutIntent](https://docs.stripe.com/api/v2/money-management/payout-intents/update.md?api-version=preview) to handle some failures, for example, by changing to a valid `to.payout_method`.

After you update the PayoutIntent, check its `status` in the response:

- `pending`: Stripe started a new payout attempt. You don’t need to take any further action.
- `requires_action` with `next_action.type` set to `confirm`: You must [review and confirm the payout](https://docs.stripe.com/treasury/connect/moving-money/out-of/outbound-payments.md#review-confirm-payout-intent).

### Reconfirm the PayoutIntent 

You can also [confirm the PayoutIntent](https://docs.stripe.com/api/v2/money-management/payout-intents/confirm.md?api-version=preview) to retry it without making changes, for example, after you add funds to your financial account or refresh the FX quote.

Each retry creates a new payout attempt. If the attempt fails or is returned, the PayoutIntent moves back to `requires_action`.

If a scheduled payout fails, create a new PayoutIntent instead of retrying it.

### Cancel the PayoutIntent 

```curl
curl -X POST https://api.stripe.com/v2/money_management/payout_intents/poi_1234/cancel \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

## Inspect payout status 

[Retrieve a payout](https://docs.stripe.com/api/v2/money-management/payout-intents/retrieve.md?api-version=preview) to inspect its details and status. Specify the PayoutIntent ID in the request.

```curl
curl https://api.stripe.com/v2/money_management/payout_intents/poi_1234 \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

Learn more about [managing payouts](https://docs.stripe.com/global-payouts/manage-payouts.md).

#### Outbound Payments

#### Source currency - GBP

You can create the following types of `OutboundPayment`:

| From a financial account to: | Payout method | Recipient capability | Expected arrival time |
| --- | --- | --- | --- |
| Another financial account under a different account | — | — | Immediate |
| An external UK recipient (third-party payout) | Faster Payments (FPS) | `bank_accounts.local` | Immediate |
| An external FX recipient (third-party payout) | Cross-border | Varies by country | Typically 1-7 days (varies by country) |

#### Source currency - EUR [Private preview]
Available in: AT, BE, BG, HR, CY, EE, FI, FR, DE, GR, IE, IT, LV, LT, LU, MT, NL, PT, SK, SI, ES
You can create the following types of `OutboundPayment`:

| From the connected account’s financial account to: | Payout method | Recipient capability | Expected arrival time |
| --- | --- | --- | --- |
| Another financial account under a different account | — | — | Immediate |
| An external Eurozone recipient (third-party payout) | SEPA | `bank_accounts.local` | Typically 1 business day |
| SEPA-instant | `bank_accounts.local` | Immediate |
| An external FX recipient (third-party payout) | Cross-border | Varies by country | Typically 1-7 days (varies by country) |

#### Source currency - USD [Private preview]
Available in: US
You can create the following types of `OutboundPayment`:

| From a financial account to: | Payout method | Recipient capability | Expected arrival time |
| --- | --- | --- | --- |
| Another financial account under a different account | — | — | Immediate |
| An external US recipient (third-party payout) | Automated Clearing House (ACH) | `bank_accounts.local` | Typically 2-3 business days |
| Wire | `bank_accounts.wire` | Typically 1 business day |
| Push-to-card (Private preview) | `card` | Immediate |
| Real-time payment (RTP) (Private preview) | `bank_accounts.instant` | Within a few seconds to a few minutes |
| Paper check (Check Send) (Private preview) | `paper_checks` | 1-5 business days |

## Move money from a platform to connected account 

To move funds from your platform’s financial account to a connected account’s financial account, create an OutboundPayment without the `Stripe-Context` header:

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_payments \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "to": {
        "payout_method": "{{CONNECTED_ACCOUNT_FINANCIAL_ACCOUNT_ID}}",
        "recipient": "{{CONNECTED_ACCOUNT_ID}}",
        "currency": "usd"
    },
    "amount": {
        "value": 30000,
        "currency": "usd"
    },
    "description": "Funds transfer from platform to connected account"
  }'
```

> When moving funds from your platform’s financial account, don’t include the `Stripe-Context` header. The platform financial account is automatically used as the source of funds.

## Move money between separately owned financial accounts 

Use [Outbound Payments](https://docs.stripe.com/api/v2/money-management/outbound-payments/create.md?api-version=preview) to create an outbound payment:

This example creates an outbound payment between financial accounts belonging to different connected accounts controlled by your platform. Set the `recipient_notification.setting` to `none` so that a Stripe notification isn’t sent to the recipient.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_payments \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "to": {
        "payout_method": "{{RECIPIENT_FINANCIAL_ACCOUNT_ID}}",
        "recipient": "{{RECIPIENT_CONNECTED_ACCOUNT_ID}}",
        "currency": "usd"
    },
    "amount": {
        "value": 30000,
        "currency": "usd"
    },
    "description": "Payout to a financial account of another connected account",
    "recipient_notification": {
        "setting": "none"
    }
  }'
```

Use a similar request to move funds from your connected account’s financial account to your platform’s financial account.

## Create an OutboundPayment to a third-party recipient 

To pay a third-party recipient, first create and onboard a [recipient-configured connected account](https://docs.stripe.com/treasury/connect/build-an-integration.md#create-a-recipient) to generate an account ID and a payout method ID that you need for the transaction.

Then [create an outbound payment](https://docs.stripe.com/api/v2/money-management/outbound-payments/create.md?api-version=preview).

#### General

The following outbound payment example is for a standard payment to a third-party recipient in the same country and currency. The currency automatically uses the corresponding network, such as ACH for USD, FPS for GBP, or SEPA for EUR.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_payments \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "to": {
        "recipient": "{{RECIPIENTACCOUNTID_ID}}",
        "payout_method": "{{RECIPIENTPAYOUTMETHODID_ID}}",
        "currency": "usd"
    },
    "amount": {
        "value": 10000,
        "currency": "usd"
    },
    "description": "Vendor payment"
  }'
```

For payroll payments, set `"purpose": "payroll"` to comply with NACHA requirements.

#### USD — Wire
Available in: US
The following sample sets `delivery_options` to `bank_account.wire` to request a USD wire payment.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_payments \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "to": {
        "recipient": "{{RECIPIENTACCOUNTID_ID}}",
        "payout_method": "{{RECIPIENTPAYOUTMETHODID_ID}}",
        "currency": "usd"
    },
    "amount": {
        "value": 50000,
        "currency": "usd"
    },
    "delivery_options": {
        "bank_account": "wire"
    },
    "description": "Wire transfer"
  }'
```

Stripe supports both FedWire and CHIPS and automatically routes to the most cost-effective and efficient network. Wire payments aren’t reversible.

#### USD — Push-to-card [Private preview]
Available in: US
Push-to-card sends funds to a recipient’s eligible US debit card through Visa Direct or Mastercard Send.

1. Request the `cards` capability on the recipient account:

   ```curl
   curl -X POST https://api.stripe.com/v2/core/accounts/{{RECIPIENTACCOUNTID_ID}} \
     -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
     -H "Stripe-Version: 2026-10-28.preview" \
     --json '{
       "configuration": {
           "recipient": {
               "capabilities": {
                   "cards": {
                       "requested": true
                   }
               }
           }
       }
     }'
   ```

2. Create the payment using the card payout method:

   ```curl
   curl -X POST https://api.stripe.com/v2/money_management/outbound_payments \
     -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
     -H "Stripe-Version: 2026-10-28.preview" \
     -H "Stripe-Context: {{CONTEXT_ID}}" \
     --json '{
       "from": {
           "financial_account": "{{FINANCIALACCOUNTID_ID}}",
           "currency": "usd"
       },
       "to": {
           "recipient": "{{RECIPIENTACCOUNTID_ID}}",
           "payout_method": "{{CARD_PAYOUT_METHOD_ID}}",
           "currency": "usd"
       },
       "amount": {
           "value": 10000,
           "currency": "usd"
       },
       "description": "Instant payout to debit card"
     }'
   ```

Push-to-card payments aren’t reversible. The payout method must be an outbound-eligible US-issued debit card.

#### US RTP [Private preview]
Available in: US
Contact [treasury-support@stripe.com](mailto:treasury-support@stripe.com) to request access.

Real-Time Payments (RTP) sends funds instantly through The Clearing House network and is available for domestic US bank accounts only. Not all banks support RTP. Check eligibility by inspecting the recipient’s payout method for `"instant"` in `available_payout_speeds` before sending.

```curl
curl https://api.stripe.com/v2/money_management/payout_methods/{{RECIPIENTPAYOUTMETHODID_ID}} \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

If `available_payout_speeds` includes `"instant"`, the bank account supports RTP. Create the payment with `delivery_options.speed: "instant"`:

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_payments \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "to": {
        "recipient": "{{RECIPIENTACCOUNTID_ID}}",
        "payout_method": "{{RECIPIENTPAYOUTMETHODID_ID}}",
        "currency": "usd"
    },
    "amount": {
        "value": 10000,
        "currency": "usd"
    },
    "delivery_options": {
        "speed": "instant"
    },
    "description": "Real-time payment via RTP"
  }'
```

RTP payments aren’t reversible.

## Send an OutboundPayment cross-border or to a recipient in a different country or currency 

Stripe supports sending money in local currency to recipients in many different countries. Before making a cross-border outbound payment, review:

- [Payout amounts](https://docs.stripe.com/global-payouts/payout-methods.md#payout-amounts) for country-specific information about currencies and minimum payment amounts
- [Recipient payout methods](https://docs.stripe.com/treasury/connect/account-management/connected-accounts.md#recipient-payout-methods)

> To get access to cross-border Outbound Payments to external bank accounts, contact [treasury-support@stripe.com](mailto:treasury-support@stripe.com). Cross-border transfers between financial accounts are enabled by default.

Create an [OutboundPaymentQuote](https://docs.stripe.com/api/v2/money-management/outbound-payment-quotes/object.md?api-version=preview) to understand applicable FX and fees before making a cross-border outbound payment.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_payment_quotes \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "to": {
        "recipient": "{{RECIPIENTACCOUNTID_ID}}",
        "payout_method": "{{RECIPIENTPAYOUTMETHODID_ID}}",
        "currency": "eur"
    },
    "amount": {
        "value": 30000,
        "currency": "usd"
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
    "currency": "usd"
  },
  "created": "2025-09-09T09:21:17.201Z",
  "delivery_options": null,
  "estimated_fees": [
    {
      "amount": {
        "value": 0,
        "currency": "usd"
      },
      "type": "cross_border_payout_fee"
    },
    {
      "amount": {
        "value": 300,
        "currency": "usd"
      },
      "type": "standard_payout_fee"
    },
    {
      "amount": {
        "value": 100,
        "currency": "usd"
      },
      "type": "foreign_exchange_fee"
    }
  ],
  "from": {
    "debited": {
      "value": 30000,
      "currency": "usd"
    },
    "financial_account": "{{FINANCIAL_ACCOUNT_ID}}"
  },
  "fx_quote": {
    "lock_duration": "five_minutes",
    "lock_expires_at": "2025-09-09T09:26:17.000Z",
    "lock_status": "active",
    "rates": {
      "usd": {
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

Provide the quote in the payout to acknowledge the associated fees.

#### GBP to EUR

Create an [OutboundPayment](https://docs.stripe.com/api/v2/money-management/outbound-payments/create.md?api-version=preview) that sends funds stored in one currency to a recipient in a different currency. The example sends 300 GBP, converted to EUR.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_payments \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
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

#### Intra-EU [Private preview]
Available in: AT, BE, BG, HR, CY, EE, FI, FR, DE, GR, IE, IT, LV, LT, LU, MT, NL, PT, SK, SI, ES
To make an intra-EU payout, you must use [Recipient Verifications](https://docs.stripe.com/api/v2/recipient-verifications.md?api-version=preview) to perform a Verification of Payee of the recipient, even though the currency is the same. This verification ensures that the recipient account credentials match the bank account beneficiary before making the payment.

```curl
curl -X POST https://api.stripe.com/v2/money_management/recipient_verifications \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "recipient": "{{RECIPIENTACCOUNTID_ID}}",
    "payout_method": "{{RECIPIENTPAYOUTMETHODID_ID}}"
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
  "expires_at": "2025-11-03T16:30:47.256824340Z",
  "status": "verified",
  "status_transitions": null,
  ...
}
```

In case of a partial match or mismatch, you must acknowledge the recipient verification:

```curl
curl -X POST https://api.stripe.com/v2/money_management/recipient_verifications/{{RECIPIENTVERIFICATIONID_ID}}/acknowledge \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

At this point, you can [create an OutboundPayment](https://docs.stripe.com/api/v2/money-management/outbound-payments/create.md?api-version=preview).

See [Global payments testing](https://docs.stripe.com/global-payouts/testing.md#test-bank-account-numbers) for test payment accounts you can use to simulate successful and failed payments.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_payments \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "eur"
    },
    "to": {
        "recipient": "{{RECIPIENTACCOUNTID_ID}}",
        "payout_method": "{{RECIPIENTPAYOUTMETHODID_ID}}",
        "currency": "eur"
    },
    "amount": {
        "value": 30000,
        "currency": "eur"
    },
    "recipient_verification": "{{RECIPIENTVERIFICATIONID_ID}}",
    "outbound_payment_quote": "{{OUTBOUNDPAYMENTQUOTEID_ID}}"
  }'
```

## Send a paper check  (Private preview)
Available in: US
> #### Request access
> 
> Check send requires separate access in addition to Treasury for platforms. If you already use Treasury for platforms, contact your Stripe representative to request this feature.

Before sending a paper check, request the following capabilities and confirm that both have an `active` status:

- `configuration.money_manager.capabilities.outbound_payments.paper_checks` on the Account that owns the sending financial account.
- `configuration.recipient.capabilities.paper_checks` on the recipient Account.

### Create a Check Send payout method 

Create a reusable payout method with an [OutboundSetupIntent](https://docs.stripe.com/api/v2/money-management/outbound-setup-intents/create.md?api-version=preview). Set `payout_method_data.type` to `check_send` and `usage_intent` to `payment`. Provide the name printed on the check in `payout_method_data.check_send.payee_name`, up to 35 characters, and the US mailing address in `payout_method_data.check_send.mailing_address`.

For a recipient of a connected account, set the `Stripe-Context` header to `{{CONNECTED_ACCOUNT_ID}}/{{RECIPIENT_ACCOUNT_ID}}`. For a recipient of your platform, use `{{RECIPIENT_ACCOUNT_ID}}` alone. Store your API key securely. See [best practices for managing secret keys](https://docs.stripe.com/keys-best-practices.md).

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_setup_intents \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "payout_method_data": {
        "type": "check_send",
        "check_send": {
            "payee_name": "Jenny Rosen",
            "mailing_address": {
                "line1": "27 Fredrick Ave",
                "city": "Brothers",
                "state": "OR",
                "postal_code": "97712",
                "country": "US"
            }
        }
    },
    "usage_intent": "payment"
  }'
```

After successful creation, the `OutboundSetupIntent` has status `succeeded`. Save the response’s `payout_method.id` (`chksend_...`) to use as `to.payout_method` for each check sent to that destination. A recipient can have multiple check payout methods.

### Create the payment 

Create an `OutboundPayment` with the recipient Account ID in `to.recipient`.

Set `to.payout_method` to the saved `chksend_...` ID and provide a sender signature, up to 30 characters, in `to.payout_method_options.check_send.signature`. You can also provide a memo, up to 100 characters, in `to.payout_method_options.check_send.memo`. Stripe prints both on the check. Set `to.payout_method_options.check_send.shipping_speed` to `standard` or `priority`. The default is `standard`.

For a connected account’s payment, set `Stripe-Context` to the connected account ID alone. Omit the header to send from your platform’s financial account.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_payments \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "to": {
        "recipient": "{{RECIPIENTACCOUNTID_ID}}",
        "payout_method": "chksend_...",
        "payout_method_options": {
            "check_send": {
                "signature": "Jenny Rosen",
                "memo": "Streamer earnings",
                "shipping_speed": "standard"
            }
        }
    },
    "amount": {
        "value": 1999,
        "currency": "usd"
    },
    "description": "Streamer earnings"
  }'
```

### Add attachments to a paper check 

You can include a PDF attachment with a paper check, such as an invoice or receipt. Stripe supports PDF files only. The maximum page count depends on the shipping speed: 5 pages for standard shipping and 50 pages for priority shipping.

Upload the file with the [Files API](https://docs.stripe.com/api/files.md) and set `purpose` to `check_send_attachment`. For a connected account’s payment, include the `Stripe-Account` header with the ID of the connected account that owns the sending financial account. Omit the header for your platform’s payment.

```bash
curl https://files.stripe.com/v1/files \
  -u "{{SECRET_KEY}}:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -F purpose=check_send_attachment \
  -F "file=@/path/to/document.pdf"
```

Pass the returned file ID in `to.payout_method_options.check_send.attachment_file` when you create the outbound payment.

```curl
curl -X POST https://api.stripe.com/v2/money_management/outbound_payments \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  -H "Stripe-Context: {{CONTEXT_ID}}" \
  --json '{
    "from": {
        "financial_account": "{{FINANCIALACCOUNTID_ID}}",
        "currency": "usd"
    },
    "to": {
        "recipient": "{{RECIPIENTACCOUNTID_ID}}",
        "payout_method": "chksend_...",
        "payout_method_options": {
            "check_send": {
                "signature": "Jenny Rosen",
                "memo": "Streamer earnings",
                "shipping_speed": "standard",
                "attachment_file": "{{FILE_ID}}"
            }
        }
    },
    "amount": {
        "value": 1999,
        "currency": "usd"
    },
    "description": "Streamer earnings"
  }'
```

### Delivery options 

Choose a `to.payout_method_options.check_send.shipping_speed` of `standard` or `priority` to control how Stripe prints and mails the check. The default is `standard`.

| Delivery option | Printing and mailing deadline |
| --- | --- |
| Standard (USPS First Class) | 10:59pm ET for shipment by the end of the next business day. Arrives in 3-5 business days. |
| Priority (FedEx Overnight) 1 | 1pm ET for same-day shipment. Arrives the next business morning. |

1 FedEx Overnight doesn’t deliver to P.O. boxes.

### Returned checks 

If a check is undeliverable, Stripe updates the `OutboundPayment.status` to `failed` and sets `status_details.failed.reason` to `check_undeliverable` after the return mail address receives the check.

### Expired checks 

Checks expire after 90 days. An expired check transitions to `failed`, with reason `check_expired`.

### Void a check 

Unlike bank payments, you can cancel paper checks after mailing and before deposit. To issue a stop payment, [cancel the check’s OutboundPayment](https://docs.stripe.com/api/v2/money-management/outbound-payments/cancel.md?api-version=preview) if its `status` is `processing` and `cancelable` is `true`. For a connected account’s payment, include the `Stripe-Context` header with that account’s ID.

Successful cancellation returns status `canceled`, and Stripe sends the `v2.money_management.outbound_payment.canceled` event. Stripe doesn’t automatically reissue the check. Confirm cancellation succeeded before creating a replacement `OutboundPayment`.

### Retrieve a file attachment 

You can [download a file attached to a check](https://docs.stripe.com/file-upload.md#download-file-contents) in the command line, specifying the file ID from the `to.payout_method_options.check_send.attachment_file` parameter.

### Sample paper check 

Set the check amount with `amount.value` and `amount.currency`, the signature with `to.payout_method_options.check_send.signature`, and an optional memo with `to.payout_method_options.check_send.memo`. Stripe uses `check_send.payee_name` and `check_send.mailing_address` from the payout method for the recipient details.
![Sample paper check with annotations identifying the payer, recipient name and address, amount, signature, and memo.](https://b.stripecdn.com/docs-statics-srv/assets/sample-paper-check.b318a7e4cca8bf5d145bef1ef8b8a199.png)

## See also

- [Build an integration](https://docs.stripe.com/treasury/connect/build-an-integration.md)
- [Financial accounts](https://docs.stripe.com/treasury/connect/account-management/financial-accounts.md)
- [Connected accounts](https://docs.stripe.com/treasury/connect/account-management/connected-accounts.md)

