---
title: "Prebuilt embedded finance"
source: https://docs.stripe.com/treasury/connect/v2/prebuilt-embedded-finance.md
path: treasury/connect/v2/prebuilt-embedded-finance
---

# Prebuilt embedded finance

Add financial accounts, money movement, and card issuing to your platform without a custom integration.
Available in: US
Launch Stripe Treasury and Issuing for platforms as a prebuilt set of embeddable components. Render Stripe financial account features such as bill pay, issuing, and cash rewards as a branded UI in your platform application while avoiding custom coding and compliance reviews. Stripe provides features such as pre-configured fees, pre-configured Radar rules, and extending [managed risk](https://docs.stripe.com/connect/risk-management/managed-risk.md) coverage to both payments and financial accounts.

### Request to join the preview for prebuilt embedded finance.

Enter your email to request access.

```bash
curl https://docs.stripe.com/preview/register \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Referer: https://docs.stripe.com/treasury/connect/v2/prebuilt-embedded-finance" \
  -d '{"email": "EMAIL", "preview": "efs_waitlist_preview"}'
```

## Before you begin

- You must be a Connect platform using [Accounts v2](https://docs.stripe.com/connect/accounts-v2.md).
  - To enable Treasury for platforms for a v1 Account, you can [specify a v1 Account in a v2 endpoint](https://docs.stripe.com/connect/accounts-v2/migrate-integration.md#use-v2-endpoints-for-all-your-accounts).
- You must use API version `2026-06-24.preview` or later.
- You must use a [restricted API key](https://docs.stripe.com/keys/restricted-api-keys.md) with Money Management permissions for live requests for both your platform and your connected accounts. [Create one in the Dashboard](https://dashboard.stripe.com/apikeys/create?permissions%5B0%5D=rak_money_management_financial_account_read&permissions%5B1%5D=rak_money_management_outbound_payment_write&connectPermissions%5B0%5D=rak_money_management_financial_account_read&connectPermissions%5B1%5D=rak_money_management_payout_method_read).

## Available components

You can render the following components in your user interface to expose the associated information and interaction. You can choose which features of the component to enable.

> #### Align features
> 
> Some features are available through multiple components. You must set a feature to the same setting across all components rendered in an account session. For example, if you render the `financial_accounts` and `recipients_list` components, they must both set the `send_money` feature to the same value.

| Component | Description | Supported features | Requires |
| --- | --- | --- | --- |
| `financial_accounts` | Displays financial account balances and account numbers. | - `bill_management`
- `card_management`
- `disable_stripe_user_authentication`
- `send_money`
- 
- `edit_payout_schedule` | `money_manager` capabilities |
| `financial_accounts_transactions` | Unified transaction history including payments and money management activity. | - `capture_payments`
- `card_management`
- `card_spend_dispute_management`
- `destination_on_behalf_of_charge_management`
- `dispute_management`
- `refund_management` | `payments` financial account |
| `issuing_cards_list` | Lists and manages Issuing cards attached to a financial account. | - `card_management`
- `card_spend_dispute_management`
- `cardholder_management`
- `disable_stripe_user_authentication`
- `spend_control_management` | - `money_manager` capabilities (must be active before requesting `card_creator` capabilities)
- `card_creator` capabilities |
| `bills` | Enables connected accounts to pay bills from their financial account. | - `send_money`
- `bill_management`
- `disable_stripe_user_authentication` | - `storage` financial account
- `money_manager` capabilities |
| `recipients_list` | Enables connected accounts to list all their recipient-configured connected accounts. | - `disable_stripe_user_authentication`
- `send_money` | - `payments` financial account
- `money_manager` capabilities |

### Financial accounts

Note: The following is a preview/demo component that behaves differently than live mode usage with real connected accounts. The actual component has more functionality than what might appear in this demo component. For example, for connected accounts without Stripe dashboard access (custom accounts), no user authentication is required in production.

### Financial account transactions

Note: The following is a preview/demo component that behaves differently than live mode usage with real connected accounts. The actual component has more functionality than what might appear in this demo component. For example, for connected accounts without Stripe dashboard access (custom accounts), no user authentication is required in production.

### Bills

Note: The following is a preview/demo component that behaves differently than live mode usage with real connected accounts. The actual component has more functionality than what might appear in this demo component. For example, for connected accounts without Stripe dashboard access (custom accounts), no user authentication is required in production.

### Recipients

Note: The following is a preview/demo component that behaves differently than live mode usage with real connected accounts. The actual component has more functionality than what might appear in this demo component. For example, for connected accounts without Stripe dashboard access (custom accounts), no user authentication is required in production.

## Enable capabilities

Your [connected accounts](https://docs.stripe.com/treasury/connect/v2/account-management/connected-accounts.md) must have the `money_manager` and `card_creator` configurations and active capabilities before they can interact with embedded components for financial accounts and Issuing.

After you request the capabilities for each account configuration, Stripe returns a set of requirements for additional information and business verification, which might include:

- Beneficial owner date of birth, address, and SSN or ITIN
- KYC/KYB reconfirmation and Issuing ToS acceptance verification
- EIN verification
- Physical address

You must collect the requirements from your connected accounts to enable the requested capabilities. You can use the [Connect embedded onboarding](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding.md) component to collect onboarding requirements from your connected accounts.

1. Create or update the connected account, requesting `money_manager` and `card_creator` capabilities.

   ```curl
   curl -X POST https://api.stripe.com/v2/core/accounts \
     -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
     -H "Stripe-Version: 2026-06-24.preview" \
     --json '{
       "include": [
           "configuration.money_manager",
           "configuration.card_creator"
       ],
       "configuration": {
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
           },
           "card_creator": {
               "capabilities": {
                   "commercial": {
                       "celtic": {
                           "spend_card": {
                               "requested": true
                           }
                       }
                   }
               }
           }
       }
     }'
   ```

2. Initiate an Account Session to render the onboarding component with the features that extract and collect the requirements needed to activate the requested capabilities.

   ```curl
   curl https://api.stripe.com/v1/account_sessions \
     -u "<<YOUR_SECRET_KEY>>:" \
     --data-urlencode "account=identifier(connectedAccount)" \
     -d "components[account_onboarding][enabled]=true" \
     -d "components[account_onboarding][features][disable_stripe_user_authentication]=true" \
     -d "components[account_onboarding][features][external_account_collection]=false"
   ```

   Use `collectionOptions.only` to specify collecting only the requirements you extracted from the capabilities request. You can use wildcard matching, such as `"beneficial_owner.*"`.

   ```javascript
   const onboarding = connectInstance.create('account-onboarding', {
     collectionOptions: { only: ["beneficial_owner.dob", "beneficial_owner.address", "beneficial_owner.id"] }
   });
   
   onboarding.setOnExit(() => {
   // Reload dashboard or check capability status
   });
   ```

3. After all capabilities are active, you can embed the prebuilt finance components to give your connected accounts access to related features through your platform site.

## Set up an AccountSession

Create an [AccountSession](https://docs.stripe.com/api/account_sessions.md) on your server to render each of the components you want to embed. Specify the `features` to provide each component’s available actions.

```curl
curl https://api.stripe.com/v1/account_sessions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-06-24.preview; embedded_connect_beta=v2" \
  --data-urlencode "account=identifier(connectedAccount)" \
  -d "components[notification_banner][enabled]=true" \
  -d "components[financial_accounts][enabled]=true" \
  -d "components[financial_accounts][features][send_money]=true" \
  -d "components[financial_accounts][features][edit_payout_schedule]=true" \
  -d "components[financial_accounts_transactions][enabled]=true" \
  -d "components[financial_accounts_transactions][features][capture_payments]=true" \
  -d "components[financial_accounts_transactions][features][dispute_management]=true" \
  -d "components[financial_accounts_transactions][features][refund_management]=true" \
  -d "components[financial_accounts_transactions][features][destination_on_behalf_of_charge_management]=true" \
  -d "components[issuing_cards_list][enabled]=true" \
  -d "components[issuing_cards_list][features][card_management]=true" \
  -d "components[issuing_cards_list][features][cardholder_management]=true" \
  -d "components[issuing_cards_list][features][card_spend_dispute_management]=true" \
  -d "components[issuing_cards_list][features][spend_control_management]=true" \
  -d "components[issuing_cards_list][features][disable_stripe_user_authentication]=true" \
  -d "components[bills][enabled]=true" \
  -d "components[bills][features][send_money]=true" \
  -d "components[bills][features][bill_management]=true" \
  -d "components[recipients_list][enabled]=true" \
  -d "components[recipients_list][features][send_money]=true" \
  -d "components[balances][enabled]=true"
```

### Error handling

If the connected account doesn’t meet the requirements for an enabled component, Account Session creation returns a `400` error with a descriptive code. Handle these errors server-side before returning the client secret to your front end.

| Error code | Cause | Resolution |
| --- | --- | --- |
| `account_sessions_missing_account_configuration` | The connected account is missing a required configuration (for example, `money_manager`). | Update the connected account to add the configuration and request its capabilities. |
| `account_sessions_missing_financial_account_capabilities` | The connected account is missing required `money_manager` capabilities. | Request the missing capabilities: `inbound_transfers.bank_accounts`, `outbound_transfers.bank_accounts`, `outbound_transfers.financial_accounts`, `received_credits.bank_accounts`. |
| `account_sessions_missing_send_money_capabilities` | The connected account is missing required `send_money` capabilities. | Request either or both missing capabilities: `outbound_payments.bank_accounts` `outbound_payments.cards`. |
| `account_sessions_missing_card_issuing_capability` | The connected account is missing required capabilities for the `issuing_cards_list` component. | Update the connected account to add the `card_creator` configuration and request its capabilities. |
| `account_sessions_missing_v2_payments_financial_account` | The connected account is missing a v2 `payments` financial account | [Contact support](https://support.stripe.com/contact) — this indicates a provisioning issue. |

## Customize component appearance

You can match the [appearance of embedded finance components](https://docs.stripe.com/connect/get-started-connect-embedded-components.md?platform=web#customize-the-look-of-connect-embedded-components) with your brand using the following appearance variables when you render the components.

| Variable | Description |
| --- | --- |
| `colorPrimary` | Button and accent color |
| `colorBackground` | Component background |
| `fontFamily` | Font applied to all text |
| `borderRadius` | Corner radius for cards and inputs |
| `spacingUnit` | Base spacing multiplier |

## Initialize ConnectJS

Initialize ConnectJS with your publishable key, the client secret from the Account Session, and your appearance settings.

```javascript
import { loadConnectAndInitialize } from "@stripe/connect-js";

// Fetch AccountSession and capability status from your server
const { client_secret, money_manager_active, issuing_active } = await getAccountSession(accountId);

const stripeConnectInstance = loadConnectAndInitialize({
  publishableKey: "{{PUBLISHABLE_KEY}}",
  fetchClientSecret: async () => client_secret,
  appearance: {
    overlays: "dialog",
    variables: {
      // Branding
      colorPrimary: "#635BFF",
      colorBackground: "#FFFFFF",
      colorText: "#1A1A1A",
      colorBorder: "#E5E7EB",
      // Typography
      fontFamily: "Inter, system-ui, sans-serif",
      fontSizeBase: "14px",
      // Shape
      borderRadius: "8px",
      spacingUnit: "12px"
    }
  }
});
```

## Render components

You can only render embedded components when the connected account has the active required configuration capabilities. You can show the standard [balances](https://docs.stripe.com/connect/supported-embedded-components/balances.md) embedded component for connected accounts without (or still onboarding) financial account and issuing related capabilities.

```javascript
const stripeConnectInstance = loadConnectAndInitialize({
  publishableKey: "pk_live_...",
  fetchClientSecret: async () => {
    const response = await fetch('/api/account-session', {
      method: 'POST',
      body: JSON.stringify({ account_id: connectedAccountId })
    });
    const { client_secret } = await response.json();
    return client_secret;
  }
});

// Financial accounts components — render when money_manager capabilities are active
const fa = stripeConnectInstance.create("financial-accounts");
document.getElementById("fa-container").appendChild(fa);

const txns = stripeConnectInstance.create("financial-accounts-transactions");
document.getElementById("txns-container").appendChild(txns);

const recipients = stripeConnectInstance.create("recipients-list");
document.getElementById("recipients-container").appendChild(recipients);

// Issuing — render when card_creator capabilities are active
const cards = stripeConnectInstance.create("issuing-cards-list");
document.getElementById("cards-container").appendChild(cards);
```

## Handle events

Register event handlers on components to respond to user actions. Common use cases include:

- Refreshing your dashboard after a user sends money.
- Updating account state after a transfer completes.
- Checking capability status after onboarding exits.

```javascript
const fa = stripeConnectInstance.create("financial-accounts");

// Called when the user completes or exits a modal flow (send money, transfer, add recipient)
fa.setOnExit(() => {
  // Refresh your UI, re-fetch account balances, or update transaction lists
  refreshDashboard();
});
```

For the onboarding component, use `setOnExit` to detect when a user completes step-up compliance and check whether capabilities have activated:

```javascript
const onboarding = stripeConnectInstance.create("account-onboarding", {
  collectionOptions: { only: requiredFields }
});

onboarding.setOnExit(() => {
  // Check if capabilities are now active and update which components to render
  checkCapabilityStatus(connectedAccountId);
});
```

## See also

- [Financial accounts](https://docs.stripe.com/treasury/connect/v2/account-management/financial-accounts.md)
- [Connected accounts](https://docs.stripe.com/treasury/connect/v2/account-management/connected-accounts.md)

