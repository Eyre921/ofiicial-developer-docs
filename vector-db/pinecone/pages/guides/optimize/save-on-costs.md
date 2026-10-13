---
title: "Save on Pinecone costs"
source: https://docs.pinecone.io/guides/optimize/save-on-costs
path: guides/optimize/save-on-costs
---

Lower Pinecone costs with prepaid credits and discounts, bulk import, namespaces for multitenancy, and read patterns that use fewer read units.

You can lower your Pinecone bill with discounted rates and by changing how you load and read data. For how usage is measured, see [Understand Pinecone cost](/guides/manage-cost/understanding-cost).

## Credits and discounts

In addition to the workload optimizations below, you can lower your effective rate:

* **Prepaid credits and annual commitments** earn discounted usage rates. See [Prepaid credits](/guides/manage-cost/understanding-cost#prepaid-credits).
* **Dedicated read nodes** can lower cost for sustained, high read throughput when you fully use the provisioned capacity (see [Choose the right index capacity mode](#choose-the-right-index-capacity-mode)).
* **Volume discounts.** Standard and Enterprise customers can [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) to discuss cost optimization and discounts.

## Prefer bulk import over upsert for large loads

When you need to populate a new namespace or load a large dataset (for example, millions of records or hundreds of GB), [importing from object storage](/guides/index-data/import-data) is usually the most efficient and cost-effective path compared to streaming [upserts](/guides/index-data/upsert-data).

* **Import** is optimized for one-time or bulk loads from Parquet in your object store and is priced based on data read during the job. See [Import cost](/guides/manage-cost/understanding-cost#imports).
* **Upsert** is priced in write units based on request size; many small requests can cost more than fewer large ones for the same total data. See [Write unit pricing](/guides/manage-cost/understanding-cost#write-units).

Use upsert (including [batch upsert](/guides/index-data/upsert-data#upsert-in-batches)) for ongoing, incremental ingestion after your initial load. For how import and upsert compare, see the [data ingestion overview](/guides/index-data/data-ingestion-overview).

## Use namespaces for multitenancy

If you need to isolate each customer's or user's data, [partition tenants with namespaces](/guides/index-data/implement-multitenancy) instead of creating separate indexes. This often lowers storage overhead and query cost, because a query's cost depends on the size of the namespace it scans.

## Right-size reads and queries

* Avoid returning vector values from a query when you don't need them (`include_values=false`, the default), especially at high `top_k`. Values are typically the largest part of a response, so leaving them out lowers [egress](/guides/manage-cost/understanding-cost#egress) and helps you stay within your plan's egress allowance.
* Use [metadata filters](/guides/search/filter-by-metadata) so queries scan fewer records where your workload allows.
* To retrieve known records without a query, use a [hierarchical ID schema](/guides/index-data/data-modeling#use-structured-ids), [list record IDs](/guides/manage-data/list-record-ids) by prefix, and then [fetch](/guides/manage-data/fetch-data) the records you need. A [query's read units](/guides/manage-cost/understanding-cost#query) grow with namespace size, while fetch [uses 1 read unit per 10 records](/guides/manage-cost/understanding-cost#fetch).

<Note>
  Omitting values lowers egress, not [read units](/guides/manage-cost/understanding-cost#read-units): query read unit cost depends on the size of the namespace scanned, not on the size of the response.
</Note>

<Note>
  Indexes built on [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes/overview) aren't subject to read unit limits for query, fetch, list, and full-text search operations. For sizing and capacity planning guidance, see the [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes/overview) guide.
</Note>

## Choose the right index capacity mode

For sustained, high read throughput, [dedicated read nodes](/guides/index-data/dedicated-read-nodes/overview) can be more cost-effective than on-demand when you fully use provisioned read capacity. For spiky or low-QPS workloads, on-demand may be cheaper. See [When to use dedicated read nodes](/guides/index-data/dedicated-read-nodes/overview#when-to-use-dedicated-read-nodes) and [Understand Pinecone cost](/guides/manage-cost/understanding-cost).

## See also

* [Decrease latency](/guides/optimize/decrease-latency)
* [Increase throughput](/guides/optimize/increase-throughput)
* [Understand Pinecone cost](/guides/manage-cost/understanding-cost)
* [Monitor usage and costs](/guides/manage-cost/monitor-usage-and-costs)
