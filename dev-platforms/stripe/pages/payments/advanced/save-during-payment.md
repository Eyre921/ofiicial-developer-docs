---
title: "Save a customer’s payment method when they use it for a payment"
source: https://docs.stripe.com/payments/advanced/save-during-payment.md
path: payments/advanced/save-during-payment
---

# Save a customer's payment method when they use it for a payment

Learn how to save your customer's payment details for future purchases when they make a payment with the Payment Intents API.

Use the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) to save payment details from a purchase. There are several use cases:

- Charge a customer for an e-commerce order and store the details for future purchases.
- Initiate the first payment of a series of recurring payments.
- Charge a deposit and store the details to charge the full amount later.

> #### Card-present transactions
> 
> Card-present transactions, such as payments through Stripe Terminal, use a different process for saving the payment method. For details, see [the Terminal documentation](https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment.md).

## Compliance

You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details for future use, such as displaying a customer’s payment method to them in the checkout flow for a future purchase or charging them when they’re not actively using your website or app. Before saving or charging a customer’s payment method, make sure you:

- Add terms to your website or app that state how you plan to save payment method details, such as:
  - The customer’s agreement allowing you to initiate a payment or a series of payments on their behalf for specified transactions.
  - The anticipated timing and frequency of payments (for example, if the charges are for scheduled installments, subscription payments, or unscheduled top-ups).
  - How you determine the payment amount.
  - Your cancellation policy, if the payment method is for a subscription service.
- Use a saved payment method for only the purpose stated in your terms.
- Collect explicit consent from the customer for this specific use. For example, include a "Save my payment method for future checkbox.
- Keep a record of your customer’s written agreement to your terms.

## Prerequisites

1. Follow the Payment Intents API guide to [accept a payment](https://docs.stripe.com/payments/accept-a-payment-intent-first.md).
2. Follow this guide to save the payment method used during a payment so you can retrieve it for use in future payments by the same customer.

## Save payment methods during payment [Server-side]

You can configure the Payment Element to save your customer’s payment methods for future use. This section shows you how to integrate the [saved payment methods feature](https://docs.stripe.com/payments/save-customer-payment-methods.md), which enables the Payment Element to:

- Prompt customers for consent to save a payment method
- Save payment methods when customers provide consent
- Display saved payment methods to customers for future purchases
- [Automatically update lost or expired cards](https://docs.stripe.com/payments/cards/overview.md#automatic-card-updates) when customers replace them
![The Payment Element and a saved payment method checkbox](https://b.stripecdn.com/docs-statics-srv/assets/spm-save.fe0b24afd0f0a06e0cf4eecb0ce2403a.png)

Save payment methods.
![The Payment Element with a Saved payment method selected](https://b.stripecdn.com/docs-statics-srv/assets/spm-saved.5dba5a8a190a9a0e9f1a99271bed3f4b.png)

Reuse a previously saved payment method.

### Enable saving the payment method in the Payment Element

When creating a [PaymentIntent](https://docs.stripe.com/api/payment_intents/.md) on your server, also create a [CustomerSession](https://docs.stripe.com/api/customer_sessions/.md) providing the customer’s ID (using either `customer` for a `Customer` object or `customer_account` for a customer-configured `Account` object) and enabling the [payment_element](https://docs.stripe.com/api/customer_sessions/object.md#customer_session_object-components-payment_element) component for your session. Configure which saved payment method [features](https://docs.stripe.com/api/customer_sessions/create.md#create_customer_session-components-payment_element-features) you want to enable. For instance, enabling [payment_method_save](https://docs.stripe.com/api/customer_sessions/create.md#create_customer_session-components-payment_element-features-payment_method_save) displays a checkbox offering customers to save their payment details for future use.

You can specify `setup_future_usage` on a PaymentIntent or Checkout Session to override the default behavior for saving payment methods. This ensures that you automatically save the payment method for future use, even if the customer doesn’t explicitly choose to save it. If you intend to specify `setup_future_usage`, don’t set `payment_method_save_usage` in the same payment transaction because `setup_future_usage` controls the save behavior.

> #### Use the Accounts v2 API to represent customers
> 
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
> 
> To join the Accounts v2 preview, go to [Account previews and features](https://dashboard.stripe.com/settings/previews) in your Dashboard and enable **Reusable payment methods for Global Payouts**.
> 
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

#### Accounts v2

#### Ruby

```ruby

# Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
# Find your keys at https://dashboard.stripe.com/apikeys.
client = Stripe::StripeClient.new('<<YOUR_SECRET_KEY>>')

post '/create-intent-and-customer-session' do
  intent = client.v1.payment_intents.create({
    amount: 1099,
    currency: 'usd',
    automatic_payment_methods: {enabled: true},
    customer_account: {{CUSTOMER_ACCOUNT_ID}},
  })
  customer_session = client.v1.customer_sessions.create({
    customer_account: {{CUSTOMER_ACCOUNT_ID}},
    components: {
      payment_element: {
          enabled: true,
          features: {
            payment_method_redisplay: 'enabled',
            payment_method_save: 'enabled',
            payment_method_save_usage: 'off_session',
            payment_method_remove: 'enabled',
          },
        },
    },
  })
  {
    client_secret: intent.client_secret,
    customer_session_client_secret: customer_session.client_secret
  }.to_json
end
```

#### Customers v1

#### Ruby

```ruby

# Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
# Find your keys at https://dashboard.stripe.com/apikeys.
client = Stripe::StripeClient.new('<<YOUR_SECRET_KEY>>')

post '/create-intent-and-customer-session' do
  intent = client.v1.payment_intents.create({
    amount: 1099,
    currency: 'usd',
    # In the latest version of the API, specifying the `automatic_payment_methods` parameter
    # is optional because Stripe enables its functionality by default.
    automatic_payment_methods: {enabled: true},
    customer: {{CUSTOMER_ID}},
  })
  customer_session = client.v1.customer_sessions.create({
    customer: {{CUSTOMER_ID}},
    components: {
      payment_element: {
          enabled: true,
          features: {
            payment_method_redisplay: 'enabled',
            payment_method_save: 'enabled',
            payment_method_save_usage: 'off_session',
            payment_method_remove: 'enabled',
          },
        },
    },
  })
  {
    client_secret: intent.client_secret,
    customer_session_client_secret: customer_session.client_secret
  }.to_json
end
```

Your Elements instance uses the CustomerSession’s *client secret* (A client secret is used with your publishable key to authenticate a request for a single object. Each client secret is unique to the object it's associated with) to access that customer’s saved payment methods. [Handle errors](https://docs.stripe.com/error-handling.md) properly when you create the CustomerSession. If an error occurs, you don’t need to provide the CustomerSession client secret to the Elements instance, as it’s optional.

Create the Elements instance using the client secrets for both the PaymentIntent and the CustomerSession. Then, use this Elements instance to create a Payment Element.

```javascript
// Create the CustomerSession and obtain its clientSecret
const res = await fetch("/create-intent-and-customer-session", {
  method: "POST"
});

const {
  customer_session_client_secret: customerSessionClientSecret
} = await res.json();

const elementsOptions = {
  clientSecret: '{{CLIENT_SECRET}}',
  customerSessionClientSecret,
  // Fully customizable with appearance API.
  appearance: {/*...*/},
};

// Set up Stripe.js and Elements to use in checkout form, passing the client secret
// and CustomerSession's client secret obtained in a previous step
const elements = stripe.elements(elementsOptions);

// Create and mount the Payment Element
const paymentElementOptions = { layout: 'accordion'};
const paymentElement = elements.create('payment', paymentElementOptions);
paymentElement.mount('#payment-element');
```

When confirming the PaymentIntent, Stripe.js automatically controls setting [setup_future_usage](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-setup_future_usage) on the PaymentIntent and [allow_redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) on the PaymentMethod, depending on whether the customer checked the box to save their payment details.

### Enforce CVC recollection

Optionally, specify `require_cvc_recollection` [when creating the PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card-require_cvc_recollection) to enforce CVC recollection when a customer is paying with a card.

### Detect the selection of a saved payment method

To control dynamic content when a saved payment method is selected, listen to the Payment Element `change` event, which is populated with the selected payment method.

```javascript
paymentElement.on('change', function(event) {
  if (event.value.payment_method) {
    // Control dynamic content if a saved payment method is selected
  }
})
```

## Save only payment methods that support reuse [Server-side]

You can’t make all payment methods [reusable](https://docs.stripe.com/payments/accept-a-payment.md#save-payment-method-details) by enabling `setup_future_usage` in the Payment Intent. See [Payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md#additional-api-supportability) to learn more about which payment methods are compatible with `setup_future_usage`.

Instead, you can save payment method details only when a customer selects a payment method that supports it. For example, if you accept both card payments and Giropay (which you can’t reuse), configure `setup_future_usage=off_session` on the `payment_method_options[card]` object.

If the customer declines to have their payment details saved, disable `setup_future_usage` in the PaymentIntent on the server-side. We don’t support making this adjustment on the client-side.

#### Manage payment methods from the Dashboard

You can manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

#### curl

```bash
curl https://api.stripe.com/v1/payment_intents \
  -u <<YOUR_SECRET_KEY>>: \
  -d "amount"=1099 \
  -d "currency"="usd" \
  -d "automatic_payment_methods[enabled]"="true" \
  -d "payment_method_options[card][setup_future_usage]"="off_session"
```

#### Listing payment methods manually

Alternatively, you can list `card` and `giropay` using [allowed_payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-allowed_payment_method_types), as in the following example.

#### curl

```bash
curl https://api.stripe.com/v1/payment_intents \
  -u <<YOUR_SECRET_KEY>>: \
  -d "amount"=1099 \
  -d "currency"="usd" \
  -d "allowed_payment_method_types[]"="card" \
  -d "allowed_payment_method_types[]"="giropay" \
  -d "payment_method_options[card][setup_future_usage]"="off_session"
```

## Charge the saved payment method later [Server-side]

> `bancontact`, `ideal`, and `sofort` are one-time payment methods by default. When set up for future usage, they generate a `sepa_debit` reusable payment method type so you need to use `sepa_debit` to query for saved payment methods.

To find a payment method to charge, list the payment methods associated with your customer. This example lists cards, but you can list any supported [type](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-type).

> #### Use the Accounts v2 API to represent customers
> 
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
> 
> To join the Accounts v2 preview, go to [Account previews and features](https://dashboard.stripe.com/settings/previews) in your Dashboard and enable **Reusable payment methods for Global Payouts**.
> 
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

#### Accounts v2

```curl
curl -G https://api.stripe.com/v1/payment_methods \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer_account={{CUSTOMERACCOUNT_ID}}" \
  -d type=card
```

#### Customers v1

```curl
curl -G https://api.stripe.com/v1/payment_methods \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d type=card
```

When you’re ready to charge your customer *off-session* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information), use the ID of the `Customer` or customer-configured `Account` and the `PaymentMethod` ID to create a `PaymentIntent` with the amount and currency of the payment. Set a few other parameters to make the off-session payment:

- Set [off_session](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-off_session) to true to indicate that the customer isn’t in your checkout flow to respond to any authentication requests. If, during your checkout flow, a partner (such as a card issuer or bank) requests authentication, Stripe requests exemptions using customer information from a previous *on-session* (A payment is described as on-session if it occurs while the customer is actively in your checkout flow and able to authenticate the payment method) transaction. If the conditions for exemption aren’t met, the `PaymentIntent` might throw an error.
- Set [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) to true to trigger confirmation immediately when the `PaymentIntent` is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the `PaymentMethod`’s ID.
- Depending on how you represent customers in your integration, set either [customer_account](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer_account) to the ID of the customer-configured `Account` or [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the `Customer`.

#### Accounts v2

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1099 \
  -d currency=usd \
  -d "automatic_payment_methods[enabled]=true" \
  -d "customer_account={{CUSTOMERACCOUNT_ID}}" \
  -d payment_method={{PAYMENT_METHOD_ID}} \
  --data-urlencode "return_url=https://example.com/order/123/complete" \
  -d off_session=true \
  -d confirm=true
```

#### Customers v1

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1099 \
  -d currency=usd \
  -d "automatic_payment_methods[enabled]=true" \
  -d "customer={{CUSTOMER_ID}}" \
  -d payment_method={{PAYMENT_METHOD_ID}} \
  --data-urlencode "return_url=https://example.com/order/123/complete" \
  -d off_session=true \
  -d confirm=true
```

## Test the integration

Use test payment details and the test redirect page to verify your integration. Click the tabs below to view details for each payment method.

#### Cards

| Payment method | Scenario | How to test |
| --- | --- | --- |
| Credit card | The card setup succeeds and doesn’t require *authentication* (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase). | Fill out the credit card form using the credit card number `4242 4242 4242 4242` with any expiration, CVC, and postal code. |
| Credit card | The card requires authentication for the initial setup, then succeeds for subsequent payments. | Fill out the credit card form using the credit card number `4000 0025 0000 3155` with any expiration, CVC, and postal code. |
| Credit card | The card requires authentication for the initial setup and also requires authentication for subsequent payments. | Fill out the credit card form using the credit card number `4000 0027 6000 3184` with any expiration, CVC, and postal code. |
| Credit card | The card is declined during setup. | Fill out the credit card form using the credit card number `4000 0000 0000 9995` with any expiration, CVC, and postal code. |

#### Bank redirects

| Payment method | Scenario | How to test |
| --- | --- | --- |
| Bancontact | Your customer successfully sets up a SEPA Direct Debit payment method for future usage by using Bancontact. | Use any name in the Bancontact form, then click **Authorize test setup** on the redirect page. |
| Bancontact | Your customer fails to authenticate on the Bancontact redirect page. | Use any name in the Bancontact form, then click **Fail test setup** on the redirect page. |
| BECS Direct Debit | Your customer successfully pays with BECS Direct Debit. | Fill out the form using the account number `900123456`. The confirmed `PaymentIntent` status initially transitions to `processing`, then to `succeeded` 3 minutes later. |
| BECS Direct Debit | Your customer’s payment fails with an `account_closed` error code. | Fill out the form using the account number `111111113`. |
| iDEAL | Your customer successfully sets up a [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit.md) payment method for future usage by using iDEAL. | Use any name and bank in the iDEAL form, then click **Authorize test setup** on the redirect page. |
| iDEAL | Your customer fails to authenticate on the iDEAL redirect page. | Select any bank and use any name in the iDEAL form, then click **Fail test setup** on the redirect page. |

#### Bank debits

| Payment method | Scenario | How to test |
| --- | --- | --- |
| SEPA Direct Debit | Your customer successfully pays with SEPA Direct Debit. | Fill out the form using the account number `AT321904300235473204`. The confirmed `PaymentIntent` status initially transitions to `processing`, then to  `succeeded` 3 minutes later. |
| SEPA Direct Debit | Your customer’s `PaymentIntent` status transitions from `processing` to `requires_payment_method`. | Fill out the form using the account number `AT861904300235473202`. |

### Test charging a saved SEPA Debit PaymentMethod

Confirming the `PaymentIntent` using iDEAL, Bancontact, or Sofort generates a [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit.md) *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs). SEPA Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method that transitions to an intermediate `processing` state before transitioning several days later to a `succeeded` or `requires_payment_method` state.

#### Email

Set `payment_method.billing_details.email` to one of the following values to test the `PaymentIntent` status transitions. You can include your own custom text at the beginning of the email address followed by an underscore. For example, `test_1_generatedSepaDebitIntentsFail@example.com` results in a SEPA Direct Debit PaymentMethod that always fails when used with a `PaymentIntent`.

| Email Address | Description |
| --- | --- |
| `generatedSepaDebitIntentsSucceed@example.com` | The `PaymentIntent` status transitions from `processing` to `succeeded`. |
| `generatedSepaDebitIntentsSucceedDelayed@example.com` | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes. |
| `generatedSepaDebitIntentsFail@example.com` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`. |
| `generatedSepaDebitIntentsFailDelayed@example.com` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes. |
| `generatedSepaDebitIntentsSucceedDisputed@example.com` | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately. |
| `generatedSepaDebitIntentsFailsDueToInsufficientFunds@example.com` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

#### PaymentMethod

Use these PaymentMethods to test that the `PaymentIntent` status transitions. These tokens are useful for automated testing to immediately attach the PaymentMethod to the SetupIntent on the server.

| Payment Method | Description |
| --- | --- |
| `pm_bancontact_generatedSepaDebitIntentsSucceed` | The `PaymentIntent` status transitions from `processing` to `succeeded`. |
| `pm_bancontact_generatedSepaDebitIntentsSucceedDelayed` | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes. |
| `pm_bancontact_generatedSepaDebitIntentsFail` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`. |
| `pm_bancontact_generatedSepaDebitIntentsFailDelayed` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes. |
| `pm_bancontact_generatedSepaDebitIntentsSucceedDisputed` | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately. |
| `pm_bancontact_generatedSepaDebitIntentsFailsDueToInsufficientFunds` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

## See also

- [Save payment details during in-app payments](https://docs.stripe.com/payments/mobile/save-during-payment.md)
- [Save payment details during payment with Checkout](https://docs.stripe.com/payments/checkout/save-during-payment.md)
- [Set up future payments](https://docs.stripe.com/payments/save-and-reuse.md)
- [Handle post-payment events](https://docs.stripe.com/events/set-up-events.md)

