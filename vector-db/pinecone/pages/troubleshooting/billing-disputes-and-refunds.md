---
title: "Billing disputes and refunds"
source: https://docs.pinecone.io/troubleshooting/billing-disputes-and-refunds
path: troubleshooting/billing-disputes-and-refunds
---

Understand Pinecone's policy of not refunding unused indexes, and why migrating a pod-based index to serverless can lower a bill you'd otherwise dispute.

As a rule, Pinecone does not offer refunds for unused indexes. If you use a pod-based index, we charge only for the pods you use to create it, not per API call or query. Whether you have used your index or not does not factor into our billing.

Our serverless indexes are a better fit if you don't plan to use your index on a regular basis. Serverless indexes are billed by the number of reads and writes you run and how much storage your index consumes. If your bill for your pod-based index is too high, we recommend [migrating to a serverless index](/guides/indexes/pods/migrate-a-pod-based-index-to-serverless) instead.

Our billing policies are detailed in our [user agreement](https://www.pinecone.io/user-agreement/) and [pricing page](https://pinecone.io/pricing).

We have several resources available to help you manage your bill:

* [Account deactivation for non-payment](/guides/organizations/manage-billing/non-payment-account-deactivation)
* [Change your billing plan](/guides/organizations/manage-billing/upgrade-billing-plan)
* [Monitor your usage and costs](/guides/manage-cost/monitor-usage-and-costs)
* [Understand cost](/guides/manage-cost/understanding-cost)
* [Manage cost](/guides/manage-cost/manage-cost)
