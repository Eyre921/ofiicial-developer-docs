---
title: "Pricing"
source: https://docs.sentry.io/pricing.md
path: pricing
---

---
title: "Pricing & Billing"
description: "Learn about pricing, managing volume, and the different Sentry plans."
url: https://docs.sentry.io/pricing/
---

# Pricing & Billing | Sentry Docs

This pricing applies to organizations on Sentry’s **latest** pricing plan. For information on older plans that include transactions or performance units based billing, go to your [**Settings > Subscription**](https://sentry.io/orgredirect/organizations/:orgslug/settings/billing/overview/) page.

This page gives you an in-depth understanding of our pricing and billing structure, including:

* [How our pricing works](https://docs.sentry.io/pricing.md#pricing-how-it-works) and [per-category pricing](https://docs.sentry.io/pricing.md#pricing-by-product-and-data-category)
* [Billing cycles](https://docs.sentry.io/pricing.md#billing-cycles)
* [Taxes](https://docs.sentry.io/pricing.md#taxes) and [exemptions](https://docs.sentry.io/pricing.md#tax-exemptions)

## [Terminology](https://docs.sentry.io/pricing.md#terminology)

* **Volume:** Volume refers to the total number of events and attachments — or the total amount of data sent by your organization.

* **Reserved volume:** A predetermined amount of data you pay for in advance at a discount, on a monthly or annual basis. Your base plan includes a set amount of volume for each data category.

* **Pay-as-you-go (PAYG) budget:** A PAYG budget is shared among all categories on a first-come, first-served basis and covers any overages above your reserved volume. You will only be charged for what you use up to your PAYG budget.

## [Pricing: How It Works](https://docs.sentry.io/pricing.md#pricing-how-it-works)

We bill based on the amount of data processed. Each [paid plan](https://sentry.io/pricing/) comes with the below pre-set monthly event volume, which is included in the price:

* 50k errors
* 5GB logs
* 5GB application metrics
* 5M spans
* 50 replays
* 1 uptime monitor
* 1 cron monitor
* 100 size analysis builds
* 1GB of attachments
* Continuous profiling (available only through PAYG)
* UI Profiling (available only through PAYG)
* Seer (available only through purchase of Seer)

On top of that, you can set aside a PAYG budget that can be used to send additional data in applicable categories. Alternatively, you can choose to pay ahead of time to reserve additional volume at a discounted price. Any unused reserved volume will expire at the end of each billing month.

Any data sent after you've run through your reserved volume and PAYG budget will be dropped and you won't be charged for it. This means that you'll lose monitoring for the remainder of the billing cycle, so make sure your budget matches your usage.

For more information on how to manage your monthly spending, check out our [Quota Management documentation](https://docs.sentry.io/pricing/quotas.md).

### [Pricing by Product and Data Category](https://docs.sentry.io/pricing.md#pricing-by-product-and-data-category)

Sentry offers several products, each of which have their own pricing structure as listed in the tables below. Paid pricing plans include a standard volume of events for each product or data category and you can buy more either by prepaying for reserved volume and/or setting up a PAYG budget.

Please note that all per-category prices listed below have been rounded.

#### [Errors Pricing](https://docs.sentry.io/pricing.md#errors-pricing)

| Error Volume | Team Reserved | Team PAYG  | Business Reserved | Business PAYG |
| ------------ | ------------- | ---------- | ----------------- | ------------- |
| >50k-100k    | $0.0002900    | $0.0003625 | $0.0008900        | $0.0011125    |
| >100k-500k   | $0.0001750    | $0.0002188 | $0.0005000        | $0.0006250    |
| >500k-10M    | $0.0001500    | $0.0001875 | $0.0003000        | $0.0003750    |
| >10M-20M     | $0.0001300    | $0.0001625 | $0.0002600        | $0.0003250    |
| >20M         | $0.0001200    | $0.0001500 | $0.0002400        | $0.0003000    |

#### [Logs Pricing](https://docs.sentry.io/pricing.md#logs-pricing)

All Sentry plans include 5GB of logs. Additional usage can only be purchased with your PAYG budget.

| Team PAYG | Business PAYG |
| --------- | ------------- |
| $0.50/GB  | $0.50/GB      |

#### [Application Metrics Pricing](https://docs.sentry.io/pricing.md#application-metrics-pricing)

All Sentry plans include 5GB of application metrics. Additional usage can only be purchased with your PAYG budget.

| Team PAYG | Business PAYG |
| --------- | ------------- |
| $0.50/GB  | $0.50/GB      |

#### [Tracing Pricing](https://docs.sentry.io/pricing.md#tracing-pricing)

Tracing is enabled by and will be billed for in spans.

| Span Volume | Team Reserved | Team PAYG  | Business Reserved | Business PAYG |
| ----------- | ------------- | ---------- | ----------------- | ------------- |
| >5M-100M    | $0.0000016    | $0.0000020 | $0.0000032        | $0.0000040    |
| >100M       | $0.0000014    | $0.0000018 | $0.0000029        | $0.0000036    |

#### [Replays Pricing](https://docs.sentry.io/pricing.md#replays-pricing)

| Replay Volume | Team Reserved | Team PAYG  | Business Reserved | Business PAYG |
| ------------- | ------------- | ---------- | ----------------- | ------------- |
| >50-5k        | $0.0030000    | $0.0037500 | $0.0030000        | $0.0037500    |
| >5k-100k      | $0.0028500    | $0.0035630 | $0.0028500        | $0.0035630    |
| >100k-900k    | $0.0025650    | $0.0032060 | $0.0025650        | $0.0032060    |
| >900k-4.5M    | $0.0023090    | $0.0028860 | $0.0023090        | $0.0028860    |
| >4.5M         | $0.0019620    | $0.0024530 | $0.0019620        | $0.0024530    |

#### [Profiling Pricing](https://docs.sentry.io/pricing.md#profiling-pricing)

Profile Hours are determined by the length of the profile in milliseconds and are billed in hours. Partial hours are prorated and rounded down to the nearest cent. Profile Hours can only be purchased with your PAYG budget.

[Transaction-Based profiling](https://docs.sentry.io/product/profiling/transaction-vs-continuous-profiling.md) is billed under either UI or Continuous Profile Hours, by extracting the duration from the samples that make up the profile.

**Continuous Profile Hours**

| Team PAYG    | Business PAYG |
| ------------ | ------------- |
| $0.0315/hour | $0.0315/hour  |

**UI Profile Hours**

| Team PAYG  | Business PAYG |
| ---------- | ------------- |
| $0.25/hour | $0.25/hour    |

#### [Monitors Pricing](https://docs.sentry.io/pricing.md#monitors-pricing)

All Sentry plans include one cron monitor and one uptime monitor. Additional monitors can only be purchased with your PAYG budget.

More details on how to activate, deactivate, and manage your monitors quota is available under:

* [Billing Quota Management: Manage Your Cron and Uptime Monitors](https://docs.sentry.io/pricing/quotas/manage-cron-monitors.md)

**Cron Monitors**

| Team PAYG     | Business PAYG |
| ------------- | ------------- |
| $0.78/monitor | $0.78/monitor |

**Uptime Monitors**

| Team PAYG     | Business PAYG |
| ------------- | ------------- |
| $1.00/monitor | $1.00/monitor |

#### [Attachments Pricing (per GB)](https://docs.sentry.io/pricing.md#attachments-pricing-per-gb)

| Attachment Size | Team Reserved | Team PAYG | Business Reserved | Business PAYG |
| --------------- | ------------- | --------- | ----------------- | ------------- |
| >1GB            | $0.2500       | $0.3125   | $0.2500           | $0.3125       |

#### [Size Analysis](https://docs.sentry.io/pricing.md#size-analysis)

[Size Analysis](https://docs.sentry.io/product/size-analysis.md) helps mobile development teams monitor and reduce mobile app size, which can help improve install and uninstall rates. It breaks down your mobile apps so you can see exactly where size is coming from, and surfaces insights that recommend specific fixes. Every organization has 100 size analysis builds that can be uploaded per billing period. Additional builds are only available through an Enterprise Plan. If you’d like to explore Enterprise plan options, email <sales@sentry.io> to discuss pricing for additional builds.

#### [Seer Pricing](https://docs.sentry.io/pricing.md#seer-pricing)

Seer is Sentry's AI debugging agent. It catches breaking changes before deploy and debugs and fixes issues in production. Access Seer by enabling it on your existing subscription in [settings](https://sentry.io/orgredirect/organizations/:orgslug/settings/billing/overview/?product=seer). Seer usage is billed separately as its own monthly charge and does not count against your PAYG budget.

Access Seer by adding it to your existing subscription for $40 per active contributor per month, where an active contributor is defined as any user who makes 2 or more PRs to a [Seer-Enabled repository](https://docs.sentry.io/product/ai-in-sentry/seer.md#getting-started-with-seer). A repo is considered Seer-Enabled when it is connected to Sentry and has one or more Seer features enabled. At the end of the month, contributor counts reset.

| Team                   | Business               |
| ---------------------- | ---------------------- |
| $40/active contributor | $40/active contributor |

For Github, all members of your repositories, *except* GitHub bots marked as `[bot]`, are counted as active contributors.

For Gitlab, all accounts (group members) are counted as active contributors, even when using Autofix or bots for fixes.

#### [Legacy Seer Pricing](https://docs.sentry.io/pricing.md#legacy-seer-pricing)

As of January 2026, Legacy Seer pricing will no longer be offered as an add-on to your Sentry subscription.

If you were subscribed to Seer before January 2026, you are likely on legacy Seer pricing, which is $20/month per Sentry subscription, plus $25 worth of Seer event credits. This can be used for any combination of **Issue Scans** or **Issue Fixes** (see pricing tables below). Any usage beyond this $25 credit will draw from your PAYG budget. Any usage beyond the $25 credit will draw from your [PAYG budget](https://docs.sentry.io/pricing.md#terminology).

You can see how you're using Seer and manage your usage by going to the [stats page](https://sentry.io/orgredirect/organizations/:orgslug/stats/) and selecting the **Issue Fixes** or **Issue Scans** categories, and updating the automation settings for when to run Seer in [project settings](https://sentry.io/orgredirect/organizations/:orgslug/settings/projects/:projectId/seer/).

##### [Issue Scans](https://docs.sentry.io/pricing.md#issue-scans)

Issue Scan automatically classifies and triages issues to determine which are the most likely to be fixable with a code change. Issue Scans are billed per run.

| Issue Scan Volume | Team PAYG  | Business PAYG |
| ----------------- | ---------- | ------------- |
| >0-10k            | $0.0030000 | $0.0030000    |
| >10k-100k         | $0.0027000 | $0.0027000    |
| >100k-500k        | $0.0024300 | $0.0024300    |
| >500k             | $0.0021870 | $0.0021870    |

##### [Issue Fixes](https://docs.sentry.io/pricing.md#issue-fixes)

Issue Fix performs a deep root cause analysis of an issue, using all of the context that is available to Sentry, generating a code fix, and opening a Pull Request in Github.

Issue Fixes are billed per run. Interactions with the same run will only be billed once; restarting a run with the "Start Over" button will be billed as a separate run.

| Team PAYG | Business PAYG |
| --------- | ------------- |
| $1.00/run | $1.00/run     |

## [Billing Cycles](https://docs.sentry.io/pricing.md#billing-cycles)

Billing or Owner-level users have the permissions to make changes to information on the Subscription page and access receipts. If you need a receipt, but don't have the right permissions, reach out to your administrator.

Your billing cycle will be either monthly or annually, depending on the contract term of your subscription, and whether or not you are using pay-as-you-go (PAYG):

* **Annual Subscriptions:** You will be billed annually at the beginning of your billing cycle for your paid plan and reserved volume. If you use PAYG, you will receive a monthly bill for this usage.

* **Monthly Subscriptions:** You will be billed monthly at the beginning of your billing cycle for your paid plan and reserved volume. If you use PAYG, the bill you receive will also include any PAYG usage from the previous billing cycle.

Users with [Billing or Owner-level](https://docs.sentry.io/organization/membership.md) permissions can find their receipts in [**Settings > Subscription > Receipts**](https://sentry.io/orgredirect/organizations/:orgslug/settings/billing/receipts/).

### [Changing Plans Mid-cycle](https://docs.sentry.io/pricing.md#changing-plans-mid-cycle)

If you decide to increase your PAYG budget in the middle of your billing cycle, Sentry will start processing additional data as soon as the increase becomes effective.\*

If you want to decrease your PAYG budget in the middle of your billing cycle, but have already consumed more data than the new desired amount allows, your budget will be lowered to match what you've already used. Any new data will be rejected. Your PAYG budget will be decreased to the desired amount on your next billing date.

If you upgrade from a Team to a Business plan mid-cycle, any existing PAYG budget will be recalculated based on Business tier pricing. This may mean that your PAYG budget will be consumed faster than it was before.

\*In most cases, new budgets will take effect within minutes. Otherwise, we guarantee a maximum turnaround time of 24 hours.

## [Plans and Free Trials](https://docs.sentry.io/pricing.md#plans-and-free-trials)

Sentry has one free Developer plan and three paid plans: Team, Business, and Enterprise. You can find more information about each by going to our [pricing page](https://sentry.io/pricing/).

Plan upgrades take effect immediately. Plan downgrades and cancellations are processed at the end of the current contract cycle and cannot be refunded. If you no longer want to be on a paid plan, you'll revert to the base Developer plan at the end of your current contract.

All new Sentry accounts come with a 14-day free trial period. You'll have the option to upgrade and continue to use Sentry's paid features at any time before your trial ends. Upgrades will be effective immediately. Users who haven't upgraded by the end of their free trial will remain on the free Developer plan with limited features.

## [Product Trials](https://docs.sentry.io/pricing.md#product-trials)

In addition to the free Business trial available to new accounts, Sentry offers a one-time, 14-day product trial as a way to let your organization try out products that aren't part of your billing plan (such as Tracing and Session Replays). Product trials are specific to each product, so you can try one product at a time or multiple products at the same time.

Anyone who's on a Free, Team, or Business plan can initiate a product trial directly from the Sentry UI. Keep in mind that each org can only trial each product once.

During your 14-day product trial, you'll be able to send us an unlimited number of events. If you continue to use the product after your trial period is up, any additional usage will be billed using your available reserved volume or your pay-as-you-go budget. You won't be billed for any data you've used during the 14-day trial period.

### [Seer Trial](https://docs.sentry.io/pricing.md#seer-trial)

[Seer](https://docs.sentry.io/product/ai-in-sentry/seer.md) is Sentry's AI debugging agent, available as an add-on subscription for Team and Business plans. For pricing details, see [Seer Pricing](https://docs.sentry.io/pricing.md#seer-pricing).

Seer does not use your application data, error information, or source code to train AI models. All generated output is shown only to members of your organization.

Go to [**Organization Settings > Subscription**](https://sentry.io/orgredirect/organizations/:orgslug/settings/billing/overview/), then click "Start Trial" for Seer. Alternatively, you can find a similar flow on the **Issue** details page from the Seer panel or on the [**Seer settings**](https://sentry.io/orgredirect/organizations/:orgslug/settings/seer/) page.

After starting your Seer trial, you'll need to configure the GitHub integration to connect your repositories. For setup instructions, see [Getting Started with Seer](https://docs.sentry.io/product/ai-in-sentry/seer.md#getting-started-with-seer).

### [Who's Eligible for a Product Trial and When?](https://docs.sentry.io/pricing.md#whos-eligible-for-a-product-trial-and-when)

**New accounts**

New accounts will be able to request a one-time product trial on day 15, after the initial 14-day Business trial has ended, or immediately after a plan has been upgraded to a paid plan.

**Free accounts**

Free accounts will be able to request a one-time product trial at any time.

**Existing Team or Business accounts**

* Existing Team or Business accounts will be able to request a one-time product trial for products that aren't already part of their billing plan at any time.

* Existing Team accounts that haven't opted in to a Business trial will have the option to request a Business trial and product trials for products that aren't already part of their billing plan at any time.

## [Taxes](https://docs.sentry.io/pricing.md#taxes)

The following sections cover taxation for various jurisdictions, business-to-business and business-to-customer taxation differences, and exemptions.

Currently, prices displayed on our [pricing page](http://sentry.io/pricing) don't include sales tax since tax rates and applicability varies across country, state/province, and locality.

### [US Taxes](https://docs.sentry.io/pricing.md#us-taxes)

Customers with a US-based billing address may be subject to state and local sales tax. Sales tax will apply to billing addresses located in the following states/localities:

* Arizona
* California
* Colorado
* Connecticut
* District of Columbia
* Florida
* Hawaii
* Illinois
* Iowa
* Kentucky
* Louisiana
* Maryland
* Massachusetts
* Michigan
* New Jersey
* New Mexico
* New York
* Ohio
* Pennsylvania
* Rhode Island
* South Carolina
* Texas
* Tennessee
* Utah
* Vermont
* Washington

### [Canadian Taxes](https://docs.sentry.io/pricing.md#canadian-taxes)

As of October 1, 2022, customers with a Canadian-based billing address may be subject to provincial and local sales tax, varying according to province. Canadian customers may be subject to one or more of the following taxes depending on their location:

| Province(s)                                                    | Tax Type(s)                                        | Total Tax Rate |
| -------------------------------------------------------------- | -------------------------------------------------- | -------------- |
| Alberta, Northwest Territories, Nunavut, Yukon                 | Goods & Service Tax (5%)                           | 5%             |
| British Columbia, Manitoba                                     | Goods & Service Tax (5%) Provincial Sales Tax (7%) | 12%            |
| New Brunswick, Newfoundland and Labrador, Prince Edward Island | Harmonized Sales Tax                               | 15%            |
| Nova Scotia                                                    | Harmonized Sales Tax                               | 14%            |
| Ontario                                                        | Harmonized Sales Tax                               | 13%            |
| Quebec                                                         | Goods & Service Tax (5%) Quebec Sales Tax (9.975%) | 14.975%        |
| Saskatchewan                                                   | Goods & Service Tax (5%) Provincial Sales Tax (6%) | 11%            |

All Canadian federal and provincial taxes will be calculated based on billing address.

### [VAT](https://docs.sentry.io/pricing.md#vat)

In the European Union (EU) and United Kingdom (UK), in accordance with EU VAT and UK VAT legislation respectively, VAT will be applied only to orders where exemption documentation or a valid VAT ID has not been supplied prior to or at the time of payment.

### [B2B and B2C Taxation - Differences](https://docs.sentry.io/pricing.md#b2b-and-b2c-taxation---differences)

Internationally, sales tax rules differ based on whether the customer is business-to-business (B2B) or business-to-consumer (B2C). In most countries, B2C sales are taxable, while B2B customers are not charged sales tax at the point of sale, but self-assess when they file their returns.

However, in some countries, both B2C and B2B customers need to be charged sales tax at the point of sale. Sentry will levy tax on your purchase based on your local tax legislation and rate according to your billing address.

### [Tax Exemptions](https://docs.sentry.io/pricing.md#tax-exemptions)

If your company or non-profit organization qualifies for a sales tax exemption, you can reach out to <tax@sentry.io> with the following information to have sales tax removed from any future bills:

* Organization name
* Copy of a signed tax exempt certificate

If you've submitted an exemption form, and you're still being charged sales taxes, that's because either:

* The exemption certificate was still in review after the billing period was closed.
* The exemption certificate covers a state that is different from your billing address.

Updating your address or submitting a tax exemption certificate doesn't impact the taxes charged on older bills. We do not adjust the billing of a closed billing period.

## Pages in this section

- [Pricing & Billing (before June 11, 2024)](https://docs.sentry.io/pricing/legacy-pricing.md)
- [Billing Quota Management](https://docs.sentry.io/pricing/quotas.md)

