---
title: "Custom payment methods"
source: https://docs.stripe.com/payments/payment-methods/custom-payment-methods.md
path: payments/payment-methods/custom-payment-methods
---

# Custom payment methods

Extend your integrations with additional payment methods processed outside of Stripe.

Custom payment methods extend your payment and billing integrations with payment methods that your payment method provider processes outside of Stripe. Display them in your payment form and process the payment in your own code. Or use an adapter that you host to connect Checkout to your provider’s redirect flow. For payment methods that Stripe processes, see the [payment method overview](https://docs.stripe.com/payments/payment-methods/overview.md).

## Choose an integration 

Add a custom payment method in one of two ways. No matter which method you use, your payment method provider processes the payment.

| Integration | Display in your payment form | Redirect-based |
| --- | --- | --- |
| Stripe role | Displays the payment method | Displays the payment method, calls your adapter, and redirects the customer |
| Your role | Process the payment in your client-side code | Build and host an adapter that starts the payment and reports the result |
| Supported APIs | [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) | [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions.md) |
| Payment result in Stripe | Optional. Report it with the [Payment Records API](https://docs.stripe.com/api/payment-record/report.md). | Required. Your adapter reports it. |

If you use the Checkout Sessions API and your provider redirects customers to complete the payment, add a [redirect-based payment method](https://docs.stripe.com/payments/payment-methods/custom-payment-methods/redirect.md). Otherwise, display the custom payment method in your payment form.

Then use the guide that matches your integration:

[Payment Element](https://docs.stripe.com/payments/payment-element/custom-payment-methods.md): Display a custom payment method in the Payment Element or Express Checkout Element, and process the payment in your client-side code.

[Mobile Payment Element](https://docs.stripe.com/payments/mobile/custom-payment-methods.md): Display a custom payment method in your mobile app.

[Redirect-based payment methods (Private preview)](https://docs.stripe.com/payments/payment-methods/custom-payment-methods/redirect.md): Build an adapter that lets Checkout redirect customers to your payment method provider.

[Third-party payment processing](https://docs.stripe.com/billing/subscriptions/third-party-payment-processing.md): Bill subscriptions with payment methods stored with your third-party processor.

## Configure a custom payment method type 

Create custom payment method types in the Dashboard to represent payment methods that you process outside Stripe. For example, if you use `SamplePay` as another processor, you can create a `SamplePayCard` type for cards processed by `SamplePay`.

Go to [Custom payment method types](https://dashboard.stripe.com/settings/custom_payment_methods), then complete these actions:

1. **Create the type**: Create a custom payment method type for each payment method that you want to offer your customers at checkout.
2. **Choose a preset or provide branding**: Choose from the presets for common payment methods processed outside of Stripe, or provide your own display name and logo. Use a preset if you display the payment method in the Payment Element. Provide custom branding if you use a custom front end or interact with the custom payment method through the [Payment Methods API](https://docs.stripe.com/api/payment_methods.md). Make sure the display name and logo comply with the [marks policy](https://docs.stripe.com/payments/payment-methods/custom-payment-methods.md#marks-requirements).
3. **Configure an adapter for redirect-based payments**: If you add a redirect-based payment method, enter the URL of the adapter endpoint that receives requests from Stripe.
4. **Save the type**: Click **Create** to save the type. You can then view its details in the Dashboard and use it to create custom payment methods. You can’t retrieve custom payment method types through the API, so store the type ID in your database for use when creating payment methods.

## Create payment methods with the API 

Create and retrieve custom payment methods with the [Payment Methods API](https://docs.stripe.com/api/payment_methods.md). When creating them, pass the ID of the custom payment method type you configured in the Stripe Dashboard as `custom[type]`.

```curl
curl https://api.stripe.com/v1/payment_methods \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d type=custom \
  -d "custom[type]={{CUSTOM_PAYMENT_METHOD_TYPE_ID}}"
```

```json
{
  "id": "pm_123456789",
  "object": "payment_method",
  "billing_details": {
    "address": {...},
    "email": "jenny@example.com",
    "name": "Jenny Rosen",
    "phone": "+335555555555"
  },
  "custom": {
    "display_name": "SamplePayCard",
    "logo": {
      "content_type": "image/jpeg",
      "url": "https://files.stripe.com/files/..."
    },
    "type": "cpmt_..."
  },
  "type": "custom",
  (...)
}
```

Your platform account can create custom payment methods in its connected accounts using its own custom payment method types, as well as the connected account’s custom payment method types.

```curl
curl https://api.stripe.com/v1/payment_methods \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d type=custom \
  -d "custom[type]={{CUSTOM_PAYMENT_METHOD_TYPE_ID}}"
```

## Product support 

The following table shows which Stripe products support each integration:

| Integration | [Connect](https://docs.stripe.com/connect.md) | [Checkout](https://docs.stripe.com/payments/checkout.md) | [Payment Links](https://docs.stripe.com/payment-links.md) | [Payment Element](https://docs.stripe.com/payments/payment-element.md) | [Express Checkout Element](https://docs.stripe.com/elements/express-checkout-element.md) | [Mobile Payment Element](https://docs.stripe.com/payments/mobile.md) | [Subscriptions](https://docs.stripe.com/subscriptions.md) | [Invoicing](https://docs.stripe.com/invoicing.md) | [Customer Portal](https://docs.stripe.com/customer-management.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Display in your payment form | ✓ Supported | - Unsupported | - Unsupported | ✓ Supported | (Private preview) | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported |
| Redirect-based | - Unsupported | ✓ Supported | - Unsupported | ✓ Supported 1 | - Unsupported | - Unsupported | ✓ Supported | ✓ Supported 2 | ✓ Supported 3 |

1 With the Checkout Sessions API only.2 Collect invoice payments with a saved custom payment method. Customers can’t add a custom payment method on the hosted invoice page.3 Customers can manage existing subscriptions, but can’t change a subscription’s payment method to a custom payment method.

## Compliance 

### Ongoing availability of custom payment methods and PSP integrations 

Stripe might at any time decide to remove or block the availability of any payment method as a custom payment method (for example, if required to do so by a governmental authority). Stripe notifies you of any removal of a custom payment method that you’re using, and you must immediately remove the custom payment method in your code. Failure to do so results in the custom payment method not rendering to your customers.

### Restricted custom payment methods 

The following payment methods or types of payment methods are prohibited from being used with custom payment methods and third-party payment processors:

- In Indonesia and Thailand:
  - The [crypto payment methods](https://market.sec.or.th/public/idisc/th/Viewmore/invalert-head?LicenseType=03&PublicFlag=Y) provided by the operators
  - Any other crypto-related payment methods

### Marks requirements 

The use of name, logo, icon, design element or anything else that can identify a payment method (“Marks”) must adhere to the following guidance:

- Follow any Marks guidelines of that payment method provider (for example, [terms](https://stripe.com/legal/marks) for use of Stripe Marks).
- Don’t alter or modify the payment method Marks, unless you have permission to do so.
- Don’t use the payment method Marks in violation of your obligations to that payment method provider.
- Don’t use Marks of one payment method provider for another payment method provider.
- Don’t use methods, devices or designs to obfuscate or mislead as to the true underlying payment method.
- Don’t use the payment method Marks in violation of any laws or regulations.

### Disclaimer 

By using custom payment methods (CPM) and [third-party payment processors](https://docs.stripe.com/billing/subscriptions/third-party-payment-processing.md), you acknowledge that:

- The third-party payment services provider (PSP) provides operation and support of CPMs and your third-party payment processors integration.
- Your chosen PSP complies with applicable laws, including anti-money laundering (AML) and sanctions laws.
- You’re responsible for maintaining a direct integration with the PSP.
- You must maintain an agreement with the PSP and must comply with your agreements with each PSP.
- You’re responsible for obtaining all necessary [rights to use the PSP’s marks and logos](https://docs.stripe.com/payments/payment-methods/custom-payment-methods.md#marks-requirements) within your checkout.
- Stripe isn’t responsible for the processing of any transactions with any PSP including, for example, any charges, refunds, disputes, settlements, or funds flows.
- You or the PSP are responsible for the completion of the purchase flow after a customer has selected a CPM, including, for example, the order confirmation and reconciliation of orders.
- You’re responsible for properly configuring the CPM and third-party payment processor integration, which might include configuring a redirect URL.
- You must immediately remove any CPM and disable your PSP integration in the event your agreement with any PSP terminates or Stripe, at its sole discretion, gives you notices or documents its [prohibition of use of that type of custom payment method](https://docs.stripe.com/payments/payment-methods/custom-payment-methods.md#restricted-custom-payment-methods).
- You can’t integrate with [restricted PSPs](https://docs.stripe.com/payments/payment-methods/custom-payment-methods.md#restricted-custom-payment-methods).
- You’re solely responsible for correctly presenting customers with their chosen CPM.
- You won’t misrepresent that Stripe processes payments for the CPMs you present to your customers.
- As a third-party payment processor user, you’ve obtained the requisite permission to enable Stripe to collect, use, retain, and disclose the data provided through the integration (“PSP Data”).
- You authorize Stripe to access and use the PSP Data to provide and update the Stripe services, comply with legal and financial partner requirements, and prevent and mitigate fraud, financial loss, and other harm.
- To the extent permitted by law, upon Stripe’s written request, you agree to provide Stripe with information about transactions with PSPs using the services so that Stripe can comply with any investigations, administrative inquiries, legal requirements, audits, and demands or inquiries from consumers, businesses, or PSPs.

> Consult with legal counsel to confirm what additional requirements specific to your business you might need to comply with before using these services.

