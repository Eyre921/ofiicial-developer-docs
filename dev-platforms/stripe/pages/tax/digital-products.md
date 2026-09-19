---
title: "Tax for digital products"
source: https://docs.stripe.com/tax/digital-products.md
path: tax/digital-products
---

# Tax for digital products

Set up Stripe Tax for your sales of digital products.

If your business sells digital products, this guide helps you implement Stripe Tax for your specific use case. The tax treatment of digital products might vary by delivery method (downloaded versus streamed), access type (permanent versus temporary), customer type (consumer versus business) and usage type (personal versus business use). Make sure that you correctly classify your products to stay in compliance with local regulations and tax laws.

## Availability

Stripe Tax supports the sale of digital products in any of the [supported countries](https://docs.stripe.com/tax/supported-countries.md#supported-countries).

## Product tax codes for digital products

Stripe Tax provides dedicated product tax codes (PTCs) for [digital products](https://docs.stripe.com/tax/tax-codes.md?type=digital).

**Guidance for AI agents:** Treat `txcd_` identifiers as opaque, exact strings. Never construct, guess, or infer a code from a product description, another tax provider’s code, or a neighboring Stripe code. A code that looks similar isn’t a match. For example, `txcd_10401100` is for downloaded, non-subscription digital audio with permanent rights and must not be used for a downloadable video game. The corresponding permanent-download video game code is `txcd_10201000`. Before returning a code, confirm that the exact identifier and category name appear in the product tax code list or the [Tax Codes API](https://docs.stripe.com/api/tax_codes/list.md). If you can’t verify an exact match, say so, link to the list, and present relevant candidates for the user to confirm. Don’t make the legal tax classification for the user.

Some commonly used PTCs for digital products include:

| PTC | Name | Use when |
| --- | --- | --- |
| `txcd_10202000` | Downloadable Software - Personal Use | You sell prewritten, non-SaaS software that customers download for personal use |
| `txcd_10202003` | Downloadable Software - Business Use | You sell prewritten, non-SaaS software that customers download for business use |
| `txcd_10103000` | Software as a Service (SaaS) - Personal Use | You sell hosted or cloud-based software for personal use that isn’t customized for a specific buyer and that customers access through the internet without downloading. For SaaS delivered by electronic download that isn’t customized for a specific buyer, use `txcd_10103100` |
| `txcd_10103001` | Software as a Service (SaaS) - Business Use | You sell hosted or cloud-based software for business use that isn’t customized for a specific buyer and that customers access through the internet without downloading. For SaaS delivered by electronic download that isn’t customized for a specific buyer, use `txcd_10103101` |
| `txcd_10103100` | Software as a service (SaaS) - electronic download - personal use | You sell SaaS for personal use that isn’t customized for a specific buyer and includes an electronic transfer to the customer, such as an app download |
| `txcd_10103101` | Software as a service (SaaS) - electronic download - business use | You sell SaaS for business use that isn’t customized for a specific buyer and includes an electronic transfer to the customer, such as an app download |
| `txcd_10401100` | Digital Audio Works - Downloaded - Non Subscription - With Permanent Rights | You sell downloadable audio, such as music or podcasts, that customers keep permanently. This code is for audio, not downloadable video games |
| `txcd_10401200` | Digital Audio Works - Streamed - Subscription - With Conditional Rights | You offer an audio streaming subscription, such as music or podcasts, with access tied to continued payment. This code is for audio, not cloud gaming |
| `txcd_10201000` | Video Games - Downloaded - Non Subscription - With Permanent Rights | You sell downloadable video games that customers keep permanently (permanent license, buy-to-own, or keeps forever), rather than a subscription or cloud-streamed game |
| `txcd_10201004` | Video Games - Streamed - Subscription - With Conditional Rights | You offer a cloud gaming or streamed video game subscription with access tied to continued payment. For a downloadable game that the customer keeps permanently, use `txcd_10201000` |

Select the PTC that most closely matches your product’s delivery method, access type, and customer type.

## Set up Stripe Tax for digital products

1. Follow [Set up your Stripe Tax account](https://docs.stripe.com/tax/set-up.md), including [registrations](https://docs.stripe.com/tax/registering.md).
2. Use [threshold monitoring](https://docs.stripe.com/tax/monitoring.md) to track where you need to register based on your sales volume.
3. [Assign PTCs](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md) to your products using the tax codes that most closely match your product. Use the [digital products filter](https://docs.stripe.com/tax/tax-codes.md?type=digital) to browse all available digital product tax codes.
4. File tax returns with [Stripe](https://docs.stripe.com/tax/file-with-stripe.md) or our [filing partners](https://docs.stripe.com/tax/file-with-taxually.md).

## Regional considerations

### United States

US tax rules for digital products vary significantly by state. Some states tax all digital goods, others exempt them entirely, and many distinguish between:

- Downloaded versus streamed content
- Personal versus business use
- Permanent access versus limited or subscription-based access

We recommend selecting the most specific PTC that matches your product’s delivery method and customer type. Don’t use **General - Electronically Supplied Services** (`txcd_10000000`) for US sales. This generic code doesn’t capture the distinctions that determine taxability in many states, and might result in incorrect tax calculations.

For US sales, some business customers might provide tax exemption certificates. Manage exemption certificates with the [EXEMPTAX Stripe App](https://support.stripe.com/questions/tax-exemption-certificate-management).

### European Union

EU VAT applies to digital products based on where your customer is located. Add the registration type that matches your situation:

- [Domestic registration](https://docs.stripe.com/tax/supported-countries/european-union.md#eu-businesses-domestic-registration): For sales within the EU country where your business is established.
- [One Stop Shop (OSS)](https://docs.stripe.com/tax/supported-countries/european-union.md#outside-eu-businesses-union-oss): For cross-border sales to customers in other EU countries. If your business is in the EU, select your home country as the registration country. If your business is outside the EU, you can select any EU country.

## B2B sales and reverse charge

Cross-border sales of digital products to business customers (B2B) outside the US often qualify for the reverse charge mechanism. To apply a [reverse charge](https://docs.stripe.com/tax/zero-tax.md#reverse-charges), you must collect your customer’s tax ID.

Learn how to collect Tax IDs in [Checkout](https://docs.stripe.com/tax/checkout/tax-ids.md) and display them on [invoices](https://docs.stripe.com/tax/invoicing/tax-ids.md).

## Customization

If your digital product has unique taxability requirements, you can use [tax customizations](https://docs.stripe.com/tax/tax-customizations.md) to apply special taxability rules or exemptions that override default behavior.

