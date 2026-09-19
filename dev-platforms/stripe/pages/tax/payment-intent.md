---
title: "Stripe Tax with PaymentIntents"
source: https://docs.stripe.com/tax/payment-intent.md
path: tax/payment-intent
---

# Stripe Tax with PaymentIntents

Calculate and collect tax in custom payment flows using the Stripe Tax API.

Use the Stripe Tax API to calculate and collect tax in your PaymentIntents integration. After calculating tax, attach the calculation to a PaymentIntent and Stripe records the transaction for reporting.

> #### Choose your integration
> 
> Stripe offers two ways to handle tax with PaymentIntents:
> 
> - **[Simplified](https://docs.stripe.com/tax/payment-intent/simplified.md)**: Stripe automatically manages tax transactions and reversals. Refund reversals use flat-amount distribution. Best for most use cases.
> - **[Custom](https://docs.stripe.com/tax/payment-intent/custom.md)**: You manually record tax transactions and control reversals at the line-item level. Use this if you need fine-grained control.
> 
> For [Checkout](https://docs.stripe.com/tax/checkout.md), [Invoicing](https://docs.stripe.com/tax/invoicing.md), or [Subscriptions](https://docs.stripe.com/tax/subscriptions.md), use their built-in Stripe Tax integrations instead.

## Add registrations

Stripe Tax only calculates tax in jurisdictions where you’re registered to collect tax. You must [add your registrations](https://docs.stripe.com/tax/registering.md#add-a-registration) in the Dashboard.

## Optional: Collect customer address [Client-side]

The tax you collect typically depends on your customer’s location. For the most accurate tax calculation, collect your customer’s full address. Before collecting an address, you can show your customer an estimate based on their [IP address](https://docs.stripe.com/tax/payment-intent.md#calculate-tax).

> The examples below use the [Address Element](https://docs.stripe.com/elements/address-element.md) to collect addresses from customers with autocomplete and localization features. If you only need [minimal tax collection](https://docs.stripe.com/tax/customer-locations.md#supported-formats), you can alternatively use a simple custom address form.

The example below mounts a full billing address form with the Address Element:

```html
<form id="address-form">
  <div id="address-element"></div>
</form>
```

You might pass the address to your server endpoint as follows:

```js
const elements = stripe.elements();
const addressElement = elements.create('address', {mode: 'billing'});
addressElement.mount('#address-element');

document.getElementById('address-form').addEventListener('submit', function(event) {
  event.preventDefault();
  addressElement.getValue().then(function(result) {
    if (!result.complete) {
      return;
    }
    var response = fetch('/preview-cart', {
      method: 'POST',
      body: JSON.stringify({address: result.value.address}),
      headers: {'Content-Type': 'application/json'},
    }).then(function(response) {
      return response.json();
    }).then(function(responseJson) {
      // Handle errors, or display calculated tax to your customer.
    });
  });
});
```

The address information that’s required to calculate tax [varies by customer country](https://docs.stripe.com/tax/customer-locations.md#supported-formats):

- **United States**: We require your customer’s postal code at a minimum. We recommend providing a full address for the most accurate tax calculation result.
- **Canada**: We require your customer’s postal code or province.
- **Other countries**: We only require your customer’s country code.

## Calculate tax [Server-side]

You choose when and how often to [calculate tax](https://docs.stripe.com/api/tax/calculations/create.md). For example, you can:

You can also use a [two-step confirmation](https://docs.stripe.com/payments/build-a-two-step-confirmation.md) integration to calculate tax with a Payment Element between the payment collection and confirmation steps.

- Show a tax estimate based on the customer’s IP address when they enter your checkout flow
- Recalculate tax as your customer types their billing or shipping address
- Calculate the final tax amount to collect when your customer finishes typing their address

Stripe [charges a fee](https://stripe.com/tax/pricing) per tax calculation API call. You can throttle tax calculation API calls to manage your costs.

The examples below show how to calculate tax in a variety of scenarios. Stripe Tax only calculates tax in jurisdictions where you’re registered to collect tax. You must [add your registrations](https://docs.stripe.com/tax/registering.md#add-a-registration) in the Dashboard.

#### Example - United States: tax-exclusive item

This example calculates tax for a US shipping address. The line item has a price of 10 USD and uses your account’s [preset tax code](https://docs.stripe.com/tax/set-up.md#preset-tax-code).

```curl
curl https://api.stripe.com/v1/tax/calculations \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d currency=usd \
  -d "line_items[0][amount]=1000" \
  -d "line_items[0][reference]=L1" \
  -d "customer_details[address][line1]=920 5th Ave" \
  -d "customer_details[address][city]=Seattle" \
  -d "customer_details[address][state]=WA" \
  -d "customer_details[address][postal_code]=98104" \
  -d "customer_details[address][country]=US" \
  -d "customer_details[address_source]=shipping"
```

#### Example - United States: multiple items with shipping

This example has multiple tax-exclusive line items, and a 5 USD shipping cost.

```curl
curl https://api.stripe.com/v1/tax/calculations \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d currency=usd \
  -d "line_items[0][amount]=1000" \
  -d "line_items[0][reference]=L1" \
  -d "line_items[0][tax_code]=txcd_99999999" \
  -d "line_items[1][amount]=5000" \
  -d "line_items[1][reference]=L2" \
  -d "line_items[1][tax_code]=txcd_99999999" \
  -d "line_items[2][amount]=9999" \
  -d "line_items[2][reference]=L3" \
  -d "line_items[2][tax_code]=txcd_99999999" \
  -d "shipping_cost[amount]=500" \
  -d "customer_details[address][line1]=920 5th Ave" \
  -d "customer_details[address][city]=Seattle" \
  -d "customer_details[address][state]=WA" \
  -d "customer_details[address][postal_code]=98104" \
  -d "customer_details[address][country]=US" \
  -d "customer_details[address_source]=shipping"
```

#### Example - Europe: tax-inclusive item

This example calculates tax for a billing address in Ireland, where tax is typically included in prices for non-business customers. The line item has a price of 29.99 EUR and uses tax code `txcd_10302000` (ebook).

```curl
curl https://api.stripe.com/v1/tax/calculations \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d currency=eur \
  -d "line_items[0][amount]=2999" \
  -d "line_items[0][reference]=L1" \
  -d "line_items[0][tax_behavior]=inclusive" \
  -d "line_items[0][tax_code]=txcd_10302000" \
  -d "customer_details[address][country]=IE" \
  -d "customer_details[address_source]=billing"
```

#### Example - Europe: multiple items with shipping

This example calculates tax for a shipping address in Ireland, where tax is typically included in prices for non-business customers. The item being shipped has a price of 59.99 EUR, and a shipping cost of 5 EUR. Since both amounts are tax-inclusive, the customer always pays 64.99 EUR.

```curl
curl https://api.stripe.com/v1/tax/calculations \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d currency=eur \
  -d "line_items[0][amount]=5999" \
  -d "line_items[0][reference]=L1" \
  -d "line_items[0][tax_behavior]=inclusive" \
  -d "line_items[0][tax_code]=txcd_99999999" \
  -d "shipping_cost[amount]=500" \
  -d "shipping_cost[tax_behavior]=inclusive" \
  -d "customer_details[address][line1]=123 Some House" \
  -d "customer_details[address][city]=Dublin" \
  -d "customer_details[address][country]=IE" \
  -d "customer_details[address_source]=shipping"
```

The [calculation response](https://docs.stripe.com/api/tax/calculations/object.md) contains amounts you can display to your customer, and use to take payment:

| Attribute | Description |
| --- | --- |
| [amount_total](https://docs.stripe.com/api/tax/calculations/object.md#tax_calculation_object-amount_total) | The grand total after calculating tax. Use this to set the PaymentIntent [amount](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-amount) to charge your customer. |
| [tax_amount_exclusive](https://docs.stripe.com/api/tax/calculations/object.md#tax_calculation_object-tax_amount_exclusive) | The amount of tax added on top of your line item amounts and shipping cost. This tax amount increases the `amount_total`. Use this to show your customer the amount of tax added to the transaction subtotal. |
| [tax_amount_inclusive](https://docs.stripe.com/api/tax/calculations/object.md#tax_calculation_object-tax_amount_inclusive) | The amount of tax that’s included in your line item amounts and shipping cost (if using tax-inclusive pricing). This tax amount doesn’t increase the `amount_total`. Use this to show your customer the tax included in the total they’re paying. |
| [tax_breakdown](https://docs.stripe.com/api/tax/calculations/object.md#tax_calculation_object-tax_breakdown) | A list of tax amounts broken out by country or state tax rate. Use this to show your customer the specific taxes you’re collecting. |

### Handle customer location errors

If your customer’s address is invalid or isn’t precise enough to calculate tax, the calculation returns the `customer_tax_location_invalid` error code:

```json
{
  "error": {
    "doc_url": "https://docs.stripe.com/error-codes#customer-tax-location-invalid",
    "code": "customer_tax_location_invalid",
    "message": "We could not determine the customer's tax location based on the provided customer address.",
    "param": "customer_details[address]",
    "type": "invalid_request_error"
  }
}
```

If you receive this error, prompt your customer to check the address they entered and fix any typos.

## Next steps

Choose how to handle tax transactions and reversals:

- **[Simplified integration](https://docs.stripe.com/tax/payment-intent/simplified.md)**: Attach the calculation to a PaymentIntent and Stripe automatically creates tax transactions on payment success, and records reversals on refunds.
- **[Custom integration](https://docs.stripe.com/tax/payment-intent/custom.md)**: Manually create tax transactions from calculations, with line-item level control over reversals.

## Testing

Use *sandboxes* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) to confirm your integration works correctly before going live. Sandbox responses are identical in structure to responses in live mode.

> In testing environments, calculations aren’t guaranteed to return up-to-date taxation results. You’re limited to 1,000 tax calculations per day. If you need a higher limit, contact [Stripe support](https://support.stripe.com/contact). For guidance on automated testing and strategies to avoid rate limits in testing environments, see [Automated testing](https://docs.stripe.com/automated-testing.md).

## View tax transactions

You can view all tax transactions for your account on the [Tax Transactions](https://dashboard.stripe.com/test/tax/transactions) page in the Dashboard. Click an individual transaction to see a detailed breakdown of calculated tax by jurisdiction, and by the individual products included in the transaction.

> The [Tax Transactions](https://dashboard.stripe.com/tax/transactions) page only includes *transactions* and not *calculations*. If you expect to see a calculation and can’t find it on this page, verify that you successfully created a tax transaction from the calculation.

## See also

- [Simplified Stripe Tax API](https://docs.stripe.com/tax/payment-intent/simplified.md)
- [Custom Stripe Tax API](https://docs.stripe.com/tax/payment-intent/custom.md)
- [Collect tax IDs with Payment Intents](https://docs.stripe.com/tax/payment-intent/tax-ids.md)
- [Off-Stripe payments](https://docs.stripe.com/tax/off-stripe.md)
- [Reporting and filing](https://docs.stripe.com/tax/reports.md)

