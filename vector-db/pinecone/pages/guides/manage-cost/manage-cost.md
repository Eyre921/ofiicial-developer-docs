---
title: "Manage cost"
source: https://docs.pinecone.io/guides/manage-cost/manage-cost
path: guides/manage-cost/manage-cost
---

Learn strategies for managing cost in Pinecone.

For the latest pricing details, see our [pricing page](https://www.pinecone.io/pricing/).

For help estimating total cost, see [Understanding cost](/guides/manage-cost/understanding-cost). To view or download a detailed report of your current usage and costs, see [Monitor usage and costs](/guides/manage-cost/monitor-usage-and-costs#monitor-organization-level-usage).

To lower your bill, see [Ways to reduce cost](/guides/manage-cost/understanding-cost#ways-to-reduce-cost) and [Save on costs](/guides/optimize/save-on-costs), which cover available credits and discounts plus ways to optimize your workload.

## Set monthly spend alerts

You can set up email alerts to monitor your organization's monthly spending. These alerts notify designated recipients when spending reaches specified thresholds. The alerts automatically reset at the start of each monthly billing cycle.

<Note>
  Spend alerts are available on the [Standard and Enterprise plans](https://www.pinecone.io/pricing/). They are not needed on the Starter or Builder plans, where usage is capped by plan quotas rather than billed per unit.
</Note>

To set a spend alert:

1. Go to [Settings > Spend alerts](https://app.pinecone.io/organizations/-/settings/spend-alerts) in the Pinecone console
2. Click **+ Add Alert**.
3. Enter the dollar amount for the spend alert.
4. Enter the email addresses to send the alert to. [Organization owners](/guides/organizations/understanding-organizations#organization-roles) are listed by default.
5. Click **Create**.

To edit a spend alert:

1. In the row of the spend alert you want to edit, click **ellipsis (...) menu > Edit**.
2. Change the dollar amount and/or email addresses for the spend alert.
3. Click **Update**.

<Note>
  **Auto-spend spike alert**: To protect from unexpected cost increases, Pinecone sends an alert when spending exceeds double your previous month's invoice amount. While the alert threshold is fixed and the alert cannot be deleted, you can modify which email addresses receive the alert and enable or disable the alert notifications.
</Note>

## List by ID prefix

By using a [hierarchical ID schema](/guides/index-data/data-modeling#use-structured-ids), you can retrieve records without performing a query. To do so, you can use [`list`](/reference/api/latest/data-plane/list) to retrieve records by ID prefix, then use `fetch` to retrieve the records you need. This can reduce costs, because [`query` consumes more RUs when scanning a larger namespace](/guides/manage-cost/understanding-cost#query), while [`fetch` consumes a fixed ratio of RUs to records retrieved](/guides/manage-cost/understanding-cost#fetch).

## Use namespaces for multitenancy

If your application requires you to isolate the data of each customer/user, consider [implementing multitenancy with serverless indexes and namespaces](/guides/index-data/implement-multitenancy). With serverless indexes, you pay only for the amount of data stored and operations performed. For queries in particular, the cost is partly based on the total number of records that must be scanned, so using namespaces can significantly reduce query costs.

## Prepaid credits

Pinecone offers an incentive for customers who purchase prepaid credits with an upfront payment. Customers may purchase between \$8,000 and \$25,000 in prepaid credits.

Customers who purchase prepaid credits can unlock additional usage capacity at no extra cost. The available benefits vary based on the selected plan and prepaid amount.

Prepaid credits apply to Pinecone services at List Price. Any usage that exceeds the available prepaid credits will be billed at full List Price.

Customers on Standard and Enterprise pay-as-you-go plans can purchase prepaid credits directly by navigating in the Pinecone console to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).

<Note>
  Purchasing prepaid credits is not available through cloud marketplace billing. To purchase prepaid credits through a cloud marketplace, contact [ar@pinecone.io](mailto:ar@pinecone.io).
</Note>

## Talk to support

Users on Standard and Enterprise plans can [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) for help in optimizing costs.

## See also

* [Understanding cost](/guides/manage-cost/understanding-cost)
* [Monitor usage and costs](/guides/manage-cost/monitor-usage-and-costs)
* [Save on costs](/guides/optimize/save-on-costs)
