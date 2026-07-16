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

We recommend planning workloads against the latest limits reported in response headers rather than fixed thresholds.

For the full mechanics of how limits scale, see [Dynamic rate limits](/docs/serverless/rate-limits#dynamic-rate-limits).

### Enterprise and Scale contracts

If you have an active Enterprise or Scale contract, your purchased rate limits stay in place until your contract expires. Nothing changes during your current term.

### Need guaranteed throughput?

If your workload depends on predictable, reserved capacity, [dedicated model inference](/docs/dedicated-endpoints/overview) gives you guaranteed rate limits for inference. You can provision it self-serve or [talk to sales](https://www.together.ai/contact-sales).

### Exceptions

Occasionally, due to the popularity of a specific model, we may apply custom rate limits or access restrictions. These exceptions are called out in the relevant model documentation.

## Cost Analytics

Together AI provides built-in spend analytics so you can track usage and costs across products and models over time.

To access cost analytics, navigate to your [billing settings](https://api.together.ai/settings/organization/~current/billing) and scroll to the **Usage** section. You can also click the **Current Usage** button to see a draft view of your monthly invoice.

<img alt="Cost analytics dashboard showing daily spend by product" />

### Filtering and Grouping

The dashboard supports several ways to slice your data:

* **Group by Product** - See daily costs broken down by product (Endpoints, Storage, Serverless Inference)
* **Group by Line Item** - View a more granular breakdown of individual usage line items
* **Filter by Product** - Focus on a specific product to isolate its spend
* **Filter by Time Range** - Adjust the date range to analyze any period of usage history

The chart updates in real time as you change filters, and the total cost for the selected period is shown in the top right of the chart.
