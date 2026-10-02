---
title: "Download a usage report"
source: https://docs.pinecone.io/guides/assistant/admin/download-usage-report
path: guides/assistant/admin/download-usage-report
---

Export a detailed Pinecone usage and cost report for your organization to analyze index consumption, credits, and monthly billing charges.

<Note>
  To view usage and costs across your Pinecone organization, you must be an [organization owner or billing admin](/guides/organizations/understanding-organizations#organization-roles). Also, this feature is available only to organizations on the Standard or Enterprise plans.
</Note>

The **Usage** dashboard in the Pinecone console gives you a detailed report of usage and costs across your organization, broken down by each billable SKU or aggregated by project or service. You can view the report in the console or download it as a CSV file for more detailed analysis.

1. Go to [**Settings > Usage**](https://app.pinecone.io/organizations/-/settings/usage) in the Pinecone console.
2. Select the time range to report on. This defaults to the last 30 days.
3. Select the scope for your report:
   * **SKU:** The usage and cost for each billable SKU, for example, read units per cloud region, storage size per cloud region, or tokens per embedding model.
   * **Project:** The aggregated cost for each project in your organization.
   * **Service:** The aggregated cost for each service your organization uses, for example, database (includes serverless back up and restore), assistants, inference (embedding and reranking), and collections.
4. Choose the specific SKUs, projects, or services you want to report on. This defaults to all.
5. To download the report as a CSV file, click **Download**.

   <Tip>
     The CSV download provides more granular detail than the console view, including breakdowns by individual index as well as project and index tags.
   </Tip>

Dates are shown in UTC to match billing invoices. Cost data is delayed up to three days from the actual usage date.
