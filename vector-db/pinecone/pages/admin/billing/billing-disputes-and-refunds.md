---
title: "Billing disputes and refunds"
source: https://docs.pinecone.io/admin/billing/billing-disputes-and-refunds
path: admin/billing/billing-disputes-and-refunds
---

Understand Pinecone's policy of not refunding unused indexes, and why migrating a pod-based index to serverless can lower a bill you'd otherwise dispute.

As a rule, Pinecone doesn't offer refunds for unused indexes. If you use a pod-based index, Pinecone charges only for the pods you use to create it, not per API call or query. Whether or not you've used your index doesn't affect billing.

Serverless indexes are a better fit if you don't plan to use your index on a regular basis. Serverless indexes are billed by the number of reads and writes you run and how much storage your index consumes. If your bill for your pod-based index is too high, we recommend [migrating to a serverless index](/guides/indexes/pods/migrate-a-pod-based-index-to-serverless) instead.

Pinecone's billing policies are detailed in the [user agreement](https://www.pinecone.io/user-agreement/) and [pricing page](https://pinecone.io/pricing).

These pages can help you manage your bill:

* [Account deactivation for non-payment](/admin/billing/non-payment-account-deactivation)
* [Change your billing plan](/admin/billing/upgrade-billing-plan)
* [Download a usage report](/admin/billing/download-usage-report)
* [Understand cost](/guides/manage-cost/understanding-cost)
* [Save on Pinecone costs](/guides/manage-cost/save-on-costs)
