---
title: "Collect customer locations"
source: https://docs.stripe.com/tax/customer-locations.md
path: tax/customer-locations
---

# Collect customer addresses

Learn about collecting customer address information to calculate tax.

Stripe Tax requires your customer’s location to automatically calculate tax. This requirement applies even if you don’t have an active registration. Without a registration in the customer’s location, the calculation returns zero tax. To learn more, see [Understand zero tax amounts](https://docs.stripe.com/tax/zero-tax.md). This guide helps you understand how to collect addresses from your customers.

## Which customer address we use 

Stripe Tax uses a single address as your customer’s location when calculating tax. How we choose an address doesn’t depend on the type of product you sell.

You can see which location an automatic tax calculated payment used in the **Tax calculation** section of the Transactions details page in your Dashboard.

You can also review the [tax.location.source](https://docs.stripe.com/api/customers/object.md#customer_object-tax-location-source) field on the Customer API object.

### Checkout and Payment Links 

Checkout and Payment Links use the address collected during the session.

### Invoicing, Subscriptions, and custom payment integrations  

#### Customer v1

We use the first viable item in the list below to determine your customer’s location:

1. We use your customer’s [shipping address](https://docs.stripe.com/api/customers/object.md#customer_object-shipping), if present.

- If a shipping address is present but invalid, we raise a `customer_tax_location_invalid` error instead of trying the next address in this list.

1. We use your customer’s [billing address](https://docs.stripe.com/api/customers/object.md#customer_object-address), if present.

- If a billing address is present but invalid, we raise a `customer_tax_location_invalid` error instead of trying the next address in the list.

1. We use the [billing details](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-billing_details) of the most specific payment method, if present: 
   1. [Default payment method](https://docs.stripe.com/api/invoices/object.md#invoice_object-default_payment_method) of the invoice, if present.
   2. [Default payment method](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-default_payment_method) of the subscription, if present.
   3. [Default payment method](https://docs.stripe.com/api/customers/object.md#customer_object-invoice_settings-default_payment_method) of the customer, if present.
2. We use your customer’s [IP address](https://docs.stripe.com/api/customers/object.md#customer_object-tax-ip_address), if present.

Display of the precedence order of customer addresses that Stripe Tax uses. (See full diagram at https://docs.stripe.com/tax/customer-locations)

```text
+-------------------------------------------------+
| Customer object                                 |
+-------------------------------------------------+
| id: cus_1234                                    |
| shipping.address: Address #1                    |
| billing.address: Address #2                     |
| invoice_settings.default_payment_method: pm_qux |
| tax.ip_address: Address #6                      |
+-------------------------------------------------+

+--------------------------------+
| Subscription object            |
+--------------------------------+
| id: sub_1234                   |
| customer: cus_1234             |
| default_payment_method: pm_bar |
+--------------------------------+

+--------------------------------+
| Invoice object                 |
+--------------------------------+
| id: in_1234                    |
| subscription: sub_1234         |
| default_payment_method: pm_foo |
+--------------------------------+

+-------------------------------------+
| PaymentMethod object                |
+-------------------------------------+
| id: pm_foo                          |
| type: card                          |
| billing_details.address: Address #3 |
+-------------------------------------+

+-------------------------------------+
| PaymentMethod object                |
+-------------------------------------+
| id: pm_bar                          |
| type: card                          |
| billing_details.address: Address #4 |
+-------------------------------------+

+-------------------------------------+
| PaymentMethod object                |
+-------------------------------------+
| id: pm_qux                          |
| type: card                          |
| billing_details.address: Address #5 |
+-------------------------------------+

[Subscription object.customer] --> [Customer object]
[Invoice object.subscription] --> [Subscription object]
[Invoice object.default_payment_method] --> [PaymentMethod object]
[Subscription object.default_payment_method] --> [PaymentMethod object]
[Customer object.invoice_settings.default_payment_method] --> [PaymentMethod object]
```

If the billing details associated with a payment method are incomplete or missing, we try assembling a more complete billing address. For example, knowing the country of the card issuer, we combine it with the postal code in the billing details.

### Tax API 

For the Tax API, the address hierarchy follows a simplified approach:

- The address provided in the API request is used directly for tax calculations.
- There is no fallback to other address sources such as shipping address, billing address, payment method, or IP addresses.

> When using the Tax API, you must provide a valid and complete address in your API requests, or they return an error. Include the country and, where applicable, the postal code and state.

## Minimal address collection 

Each billing and shipping address has the fields `line1`, `line2`, `city`, `state`, `postal_code`, and `country`. The `country` must be a [two-letter ISO 3166-1 code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

#### United States

| Example addresses | Explanation | Supported |
| --- | --- | --- |
| - `line1`: 27 Fredrick Ave
- `city`: Brothers
- `state`: OR
- `postal_code`: 97712
- `country`: US | **Full address**

A full address includes at least a line1 (street address or PO Box), city, state, postal code, and country.

The address is matched to the closest address or street in the US Postal Service address database. If a match isn’t found, we use the geographical center (average location of addresses) of the 5-digit postal code as a fallback. | ✓ Supported |
| 9-digit postal code:

- `postal_code`: 97712-4918
- `country`: US

5-digit postal code:

- `postal_code`: 97712
- `country`: US | **Country and postal code**

If you provide a 5-digit or 9-digit postal code, our system only uses the initial 5 digits for tax calculations. The tax is calculated at the geographical center, which reflects the average location of addresses within the 5-digit postal code area. Check that this is [suitable for your business](https://docs.stripe.com/tax/customer-locations.md#us-postal-codes). | ✓ Supported |
| - `state`: OR
- `country`: US | **Country and state**

We can’t calculate tax for US customers with only an ISO [country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) and [state code](https://en.wikipedia.org/wiki/ISO_3166-2). | ✗ Not supported |
| - `country`: US | **Country**

We can’t calculate tax for US customers with only an [ISO country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes). | ✗ Not supported |

#### Canada

| Example addresses | Explanation | Supported |
| --- | --- | --- |
| - `line1`: 1 Rocky Road
- `city`: Vancouver
- `province`: BC
- `postal_code`: V1X 1X1
- `country`: CA | **Full address**

A full address includes at least a line1 (street address), city, province, postal code, and country.

We calculate tax from the [ISO country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) and province. We don’t use the other address fields to calculate tax. | ✓ Supported |
| 6-digit postal code:

- `postal_code`: V1X 1X1
- `country`: CA | **Country and postal code**

We calculate tax from the [ISO country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) and province, which we determine from the postal code. | ✓ Supported |
| - `province`: BC
- `country`: CA | **Country and province**

We calculate tax for Canada customers from the [ISO country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) and province. | ✓ Supported |
| - `country`: CA | **Country**

We can’t calculate tax for Canada customers with only an [ISO country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes). | ✗ Not supported |

#### India

| Example addresses | Explanation | Supported |
| --- | --- | --- |
| - `line1`: Rafi Marg, 118
- `city`: Delhi
- `province`:  National Capital Territory (NCT) of Delhi (Union Territory)
- `postal_code`: 110001
- `country`: IN | **Full address**

A full address includes at least a line1 (street address), city, province, postal code, and country.

We calculate tax from the [ISO country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) and either the postal code or the province name. | ✓ Supported |
| 6-digit postal code:

- `postal_code`: 110001
- `country`: IN | **Country and postal code**

We calculate tax from the [ISO country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) and either the postal code or the province name. | ✓ Supported |
| - `province`: National Capital Territory (NCT) of Delhi (Union Territory)
- `country`: IN | **Country and province**

We calculate tax from the [ISO country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) and either the postal code or the province name. | ✓ Supported |
| - `country`: IN | **Country**

We can’t calculate tax for customers in India with only an [ISO country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes). | ✗ Not supported |

#### Everywhere else

| Example addresses | Explanation | Supported |
| --- | --- | --- |
| - `line1`: 1 Grand Canal St
- `city`: Dublin
- `postal_code`: D02 H210
- `country`: IE | **Full address**

The fields included in a full address differ by country, but typically include the line1 (street address), city, state, postal code, and country.

We calculate tax from the ISO [country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes), and the [state code](https://en.wikipedia.org/wiki/ISO_3166-2) or postal code, if provided. The other address fields aren’t used to calculate tax. | ✓ Supported |
| - `postal_code`: 51001
- `country`: ES | **Country and postal code**

We calculate tax from the ISO [country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes), and use the postal code to determine if your customer is located in an [excluded territory](https://docs.stripe.com/tax/customer-locations.md#europe-excluded-territories). | ✓ Supported |
| - `state`: CE
- `country`: ES | **Country and state**

We calculate tax from the ISO [country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) and [state code](https://en.wikipedia.org/wiki/ISO_3166-2). We use the state code to determine if your customer is located in an [excluded territory](https://docs.stripe.com/tax/customer-locations.md#europe-excluded-territories). | ✓ Supported |
| - `country`: ES | **Country**

We calculate tax from the [ISO country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes). If your customer is located in an [excluded territory](https://docs.stripe.com/tax/customer-locations.md#europe-excluded-territories), they pay the country tax rate. | ✓ Supported |

Use one of the supported address formats above to make sure that we can recognize your customer addresses consistently.

## Regional considerations 

### United States

In the United States, sales tax rules and rates vary by state, with some states having hundreds of districts setting their own rates. We recommend collecting a full address (including [line1](https://docs.stripe.com/api/customers/object.md#customer_object-address-line1), [city](https://docs.stripe.com/api/customers/object.md#customer_object-address-city), and [state](https://docs.stripe.com/api/customers/object.md#customer_object-address-state)) from your customers in the US.

#### IP Address Accuracy

In most cases, we can resolve an IP address to a physical area, but its precision varies and might not reflect the customer’s actual location. Given that the US imposes local taxes, we don’t recommend relying on a customer’s IP address to determine their address.

#### Precise Address Lookup

Stripe Tax supports full rooftop-accurate address lookup for customer addresses in the US, meaning you can attribute your customer’s location to a specific house or building. This provides greater accuracy in the US, where two houses located side-by-side on the same street might be subject to different tax rates, due to complex jurisdiction boundaries.

For addresses outside the US, Stripe uses the country, state, and postal code fields to determine tax obligations without comparing against a comprehensive address database. See “[Special jurisdictions and excluded territories](https://docs.stripe.com/tax/zero-tax.md#excluded-territories)” for more about when the state and postal code are used.

> Stripe Tax uses the 5-digit US postal code if the address lacks sufficient information, has inconsistencies, or otherwise can’t be matched to an address in the US Postal Service address database.

#### US Military and Diplomatic Addresses

Stripe Tax calculates no tax for US military and diplomatic mail going overseas. Overseas military and diplomatic addresses are assigned an APO, FPO, or DPO zip code, and the USPS treats it as domestic mail before transferring it to the military. Because sales to these special zip codes are sent out of the country, their sales taxes don’t apply.

#### ZIP Codes 

In the United States, Stripe Tax supports calculating sales tax with only a basic 5-digit US postal code. We use the point at the geographical center of the 5-digit postal code area as your customer’s location. The tax rate at this point might differ from the tax rate at your customer’s full address. Whether or not a postal code alone is sufficient to identify the correct tax rates to impose varies by state.

We recommend against relying on a postal code alone in the following states:

- Alabama
- Alaska
- Arizona
- Arkansas
- California
- Colorado
- Illinois
- Kansas
- Louisiana
- Missouri
- Nebraska
- New Mexico
- North Dakota
- Oklahoma
- South Dakota
- Texas
- Utah
- Washington
- West Virginia

> Stripe Tax also supports 9-digit ZIP+4 codes, but we don’t use the four additional digits.

### Europe

#### IP Address Reliability

In regions that don’t impose local taxes, such as the EU, an IP address is more likely to resolve to an accurate address.

#### Excluded territories 

In Europe, tax authorities in each country impose tax, not state or local authorities. The tax rate for the country doesn’t apply in a small number of areas, even though they’re physically located in a country that imposes tax. For example, the Italian postal code “00120” identifies Vatican City, where Italian VAT doesn’t apply.

Collect your customer’s postal code or state to enable Stripe Tax to determine when your customer is located in an excluded territory. See the [list of excluded territories](https://docs.stripe.com/tax/zero-tax.md#excluded-territories) supported by Stripe Tax.

## Best practices for collecting customer addresses

> #### Validate addresses before saving
> 
> Use the [Address Resolution API](https://docs.stripe.com/tax/address-resolution.md) to check how precisely Stripe Tax can determine the tax rate for an address and which fields to collect for better accuracy.

### Checkout and Payment Links 

Checkout handles the collection of customer addresses for you, including those created by Payment Links.

### Invoicing, Subscriptions, and custom payment integrations 

If you don’t use Payment Links or Checkout, you’re responsible for the collection of customer addresses.

#### Customer v1

- Collect and set both the [country](https://docs.stripe.com/api/customers/object.md#customer_object-address-country) and the [postal_code](https://docs.stripe.com/api/customers/object.md#customer_object-address-postal_code) fields on your `Customer`.
- When creating or updating a `Customer`, set [tax.validate_location](https://docs.stripe.com/api/customers/create.md#create_customer-tax-validate_location) to `immediately` to prevent [customer_tax_location_invalid](https://docs.stripe.com/error-codes.md#customer-tax-location-invalid) errors later.

- Use two-letter country codes ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
- Listen for [subscription webhook events](https://docs.stripe.com/billing/subscriptions/webhooks.md) as most activity happens asynchronously.

## Handle invoice finalization errors 

Finalizing invoices with Stripe Tax requires a recognized customer location. Location details might be missing or invalid if you update or remove a customer’s default payment method, or if you didn’t provide `tax[validate_location]="immediately"` when creating or updating a `Customer`.

If we don’t have a recognized customer location, invoices for a `Subscription` continue to [finalize automatically](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection.md) but without calculating taxes. This has the following effects:

- The `automatic_tax[enabled]` parameter changes to `false` on the [subscription](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-automatic_tax-enabled) and [invoice](https://docs.stripe.com/api/invoices/object.md#invoice_object-automatic_tax-enabled).
- The `Invoice[automatic_tax][disabled_reason]` parameter changes to `finalization_requires_location_inputs`.
- The `Subscription[automatic_tax][disabled_reason]` parameter changes to `requires_location_inputs`.
- If the `Subscription` has a [schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules.md), we set `automatic_tax[enabled]` to `false` on the current phase and in `default_settings`. We set the `disabled_reason` in both to `requires_location_inputs`.
- We send `invoice.updated` and `customer.subscription.updated` [events](https://docs.stripe.com/billing/subscriptions/webhooks.md#events) to inform your integration of these changes.
  - If there’s a schedule, we also send a `subscription_schedule.updated` webhook.
- The `Invoice` finalizes without calculating or collecting taxes. It won’t contain any tax amounts.
- We collect payment as usual according to the [collection method](https://docs.stripe.com/billing/collection-method.md) for the `Invoice`.

To review subscriptions without automatic tax calculations in your Stripe Dashboard, visit your Subscriptions page and filter the view by the **Automatic tax not enabled** option. To reactivate automatic tax for these subscriptions in the future, make sure you have at least one valid customer location, and activate automatic tax through the [Stripe Tax Dashboard](https://dashboard.stripe.com/tax/migrations).

### Exceptions to automatically disabling tax

Stripe returns an error and leaves the `Invoice` in a `draft` status when finalizing with the [API](https://docs.stripe.com/api/invoices/finalize.md) or Dashboard without a valid customer location. In the API, this returns an HTTP 400 error with a `code` of `customer_tax_location_invalid`.

Similarly, for automatic finalization of standalone invoices without a `Subscription`, the `Invoice` remains a draft if the customer location isn’t valid. We send an [invoice.finalization_failed](https://docs.stripe.com/api/events/types.md#event_types-invoice.finalization_failed) event with the `Invoice` [last_finalization_error[code]](https://docs.stripe.com/api/invoices/object.md#invoice_object-last_finalization_error-code) being `customer_tax_location_invalid`.

How you recover from a `customer_tax_location_invalid` error depends on whether you have or can collect a `Customer` address.

If you have a `Customer` address, or can collect one, update the `Customer` and finalize the `Invoice` manually.

#### Customer v1

1. Update [tax.validate_location](https://docs.stripe.com/api/customers/create.md#create_customer-tax-validate_location) to `immediately` to make sure that the new address is valid.
2. [Finalize](https://docs.stripe.com/api/invoices/finalize.md) the `Invoice`.

If you don’t have a customer’s address or can’t collect it, disable Stripe Tax for the `Invoice` and its `Subscription`, and finalize the `Invoice` manually.

1. Update the affected [Invoice](https://docs.stripe.com/api/invoices/update.md#update_invoice-automatic_tax) with `automatic_tax[enabled]=false`.
2. Update the affected [Subscription](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-automatic_tax-enabled) with `automatic_tax[enabled]=false`.
3. Finalize the [Invoice](https://docs.stripe.com/api/invoices/finalize.md).

## See also

- [Understanding zero tax](https://docs.stripe.com/tax/zero-tax.md)
- [Available tax codes](https://docs.stripe.com/tax/tax-codes.md)
- [How tax is calculated](https://docs.stripe.com/tax/calculating.md)

