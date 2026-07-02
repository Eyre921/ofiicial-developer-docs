---
title: "How do credits work?"
source: https://docs.fireworks.ai/faq-new/billing-pricing/what-happens-when-i-finish-my-1-dollar-credit
path: faq-new/billing-pricing/what-happens-when-i-finish-my-1-dollar-credit
---

<Note>
  Contracted customers may have the option to move to post-paid billing. [Contact our sales team](https://fireworks.ai/company/contact-us) to discuss your options.
</Note>

## How credits are applied

Fireworks operates on a **pre-paid credits** billing system. You purchase credits to use the platform:

* Credits are used first for all usage.
* If credits are exhausted and auto top-up is disabled, usage pauses until you add credits.
* If auto top-up is enabled, credits are purchased automatically when your balance reaches your configured minimum.
* You can set a monthly budget cap to limit total spend.

## Missing credits after purchase?

If you don't see your credits reflected immediately:

1. Visit your **billing dashboard**
2. Review the **"Credits"** section
3. Check your **credit balance** and **auto top-up settings**

**Important**: Usage consumes available credits. If your balance is low, enable auto top-up to avoid interruptions.

## Why did I receive an invoice after depositing credits?

Most accounts on pre-paid billing should not see month-end overage invoices. If you received an invoice, your account may be on a post-paid contract. Contact [community\_billing@fireworks.ai](mailto:community_billing@fireworks.ai) so we can confirm your billing configuration.

## What happens when I finish my \$1 credit?

When you finish your \$1 credit, the following occurs:

## Account Status

* **Without payment method**: Your account will be **suspended** until you add a payment method. For request-rate behavior, see [Account quotas](/guides/quotas_usage/account-quotas#account-wide-request-limits); for serverless TPM upper bounds, see [Serverless rate limits](/serverless/rate-limits).
* **With payment method**: Add credits to continue usage. [Account-wide request limits](/guides/quotas_usage/account-quotas#account-wide-request-limits) increase, and [serverless TPM upper bounds](/serverless/rate-limits) grow as your account spend tier rises.

**Payment Method Requirements:**

* Adding a payment method is required to continue service after credit depletion
* Add credits (or enable auto top-up) to continue service after credit depletion
* As you spend more with Fireworks, your adaptive usage limits and serverless TPM upper bounds can increase

## Where's my receipt for purchased credits?

Receipts for purchased credits are sent via Stripe upon purchase. Check your email for receipts from Stripe (not Fireworks). If you can't find your receipt, contact [community\_billing@fireworks.ai](mailto:community_billing@fireworks.ai).

<Note>
  For spend limits, tiers, and account-wide request limits, see [Account quotas](/guides/quotas_usage/account-quotas). For adaptive serverless TPM upper bounds, see [Serverless rate limits](/serverless/rate-limits).
</Note>
