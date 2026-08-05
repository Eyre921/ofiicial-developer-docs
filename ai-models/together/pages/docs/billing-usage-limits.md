---
title: "Usage limits & analytics"
source: https://docs.together.ai/docs/billing-usage-limits
path: docs/billing-usage-limits
---

Understanding rate limits, model access, and cost analytics on Together AI.

## Rate limits

Together AI uses **dynamic rate limits**. Your limits scale with your actual usage. The more you use the platform reliably, the higher your limits grow. Limits are applied per model, not per account tier.

Build Tiers (Build Tier 1–5), Scale, and Enterprise tier labels have been retired. They no longer appear in your account or API responses.

### Checking your current rate limits

Every serverless inference API request returns response headers with the latest rate limits for the model you called, along with current usage and reset timing. See [Fetching latest serverless rate limits](/docs/serverless/rate-limits#fetching-latest-serverless-rate-limits) for details.

Plan workloads against the latest limits reported in response headers rather than fixed thresholds.

For the full mechanics of how limits scale, see [Dynamic rate limits](/docs/serverless/rate-limits#dynamic-rate-limits).

### Enterprise and Scale contracts

If you have an active Enterprise or Scale contract, your purchased rate limits stay in place until your contract expires. Nothing changes during your current term.

### Need guaranteed throughput?

If your workload depends on predictable, reserved capacity, [dedicated model inference](/docs/dedicated-endpoints/overview) gives you guaranteed rate limits for inference. You can provision it self-serve or [talk to sales](https://www.together.ai/contact-sales).

### Exceptions

Occasionally, due to the popularity of a specific model, Together may apply custom rate limits or access restrictions. These exceptions are called out in the relevant model documentation.

## Cost analytics

Together AI provides built-in spend analytics so you can track usage and costs across products and models over time.

To access organization-level cost analytics, open your [billing settings](https://api.together.ai/settings/organization/~current/billing) and scroll to the **Usage** section. You can also select **See detailed cost analytics** on the monthly spend card, or open your [project's cost analytics page](https://api.together.ai/settings/projects/~current/cost-analytics) to scope the view to a single project. Select **Current Usage** on the billing page to see a draft view of your monthly invoice.

<img alt="Cost analytics dashboard showing daily spend by product" />

### Measure and grouping

The chart toolbar lets you choose how to measure and group usage:

* **Measure: Cost (\$)** - Chart daily spend in US dollars for the selected period. This is the default view.
* **Measure: Units** - Chart daily billable units (for example, tokens) instead of dollar amounts. Totals and tooltips show unit counts. The chart subtitle updates to **Daily Units by …**.
* **Group by Product** - Break down by product (Endpoints, Storage, Serverless Inference).
* **Group by Line items** - Show individual usage line items.
* **Group by Project** (beta) - Attribute spend or units to projects in your organization.
* **Group by API key** (beta) - Attribute spend or units to API keys.

When **Measure** is **Units**, grouping by product, project, or API key aggregates line-item quantities for that dimension. Group by **Line items** shows each billable line item's unit count directly.

### Filtering and time range

* **Filter** - Include or exclude specific series from the current group-by dimension with a multi-select filter (type to search options). The control shows **All usage** until you apply a filter, and filtering is not available when you group by line items.
* **Time range** - Adjust the start and end dates to analyze any period of usage history. All dates are in UTC.

The chart updates as you change controls. The summary in the top right shows the total cost or total units for the selected period, depending on the measure.
