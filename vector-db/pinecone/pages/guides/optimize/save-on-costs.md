---
title: "Save on costs"
source: https://docs.pinecone.io/guides/optimize/save-on-costs
path: guides/optimize/save-on-costs
---

Learn techniques to reduce spend when ingesting data, querying, and operating indexes.

## Credits and discounts

In addition to the workload optimizations below, you can lower your effective rate:

* **Prepaid credits and annual commitments** earn discounted usage rates. See [Prepaid credits](/guides/manage-cost/understanding-cost#prepaid-credits).
* **One-time bulk import credit.** Standard and Enterprise organizations receive a one-time 1 TB credit for [importing data from object storage](/guides/manage-cost/understanding-cost#imports).
* **Dedicated read nodes** can lower cost for sustained, high read throughput when you fully use the provisioned capacity (see [Choose the right index capacity mode](#choose-the-right-index-capacity-mode)).
* **Volume discounts.** Standard and Enterprise customers can [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) to discuss cost optimization and discounts.

## Prefer bulk import over upsert for large loads

When you need to populate a new namespace or load a large dataset (for example, millions of records or hundreds of GB), [importing from object storage](/guides/index-data/import-data) is usually the most efficient and cost-effective path compared to streaming [upserts](/guides/index-data/upsert-data).

* **Import** is optimized for one-time or bulk loads from Parquet in your object store and is priced based on data read during the job. See [Import cost](/guides/manage-cost/understanding-cost#imports).
* **Upsert** is priced in write units based on request size; many small requests can cost more than fewer large ones for the same total data. See [Write unit pricing](/guides/manage-cost/understanding-cost#write-units).

Use upsert (including [batch upsert](/guides/index-data/upsert-data#upsert-in-batches)) for ongoing, incremental ingestion after your initial load. For how import and upsert compare, see the [data ingestion overview](/guides/index-data/data-ingestion-overview).

Partitioning tenants with [namespaces](/guides/index-data/implement-multitenancy) instead of many separate indexes often lowers storage overhead and query cost, because cost depends in part on how much data each query scans. For patterns and rationale, see [Manage cost](/guides/manage-cost/manage-cost#use-namespaces-for-multitenancy).

## Right-size reads and queries

* Avoid returning vector values in read responses when you do not need them (`include_values=false`), especially at high `top_k`. Values are typically the largest part of a response, so omitting them lowers [egress](/guides/manage-cost/understanding-cost#egress) and helps you stay within your plan's egress allowance.
* Use [metadata filters](/guides/search/filter-by-metadata) so queries scan fewer records where your workload allows.

<Note>
  Omitting values lowers egress, not [read units](/guides/manage-cost/understanding-cost#read-units): query read unit cost depends on the size of the namespace scanned, not on the size of the response.
</Note>

<Note>
  Indexes built on [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) are not subject to read unit limits for query, fetch, and list operations. For sizing and capacity planning guidance, see the [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) guide.
</Note>

## Choose the right index capacity mode

For sustained, high read throughput, [dedicated read nodes](/guides/index-data/dedicated-read-nodes) can be more cost-effective than on-demand when you fully utilize provisioned read capacity. For spiky or low-QPS workloads, on-demand may be cheaper. See [When to use dedicated read nodes](/guides/index-data/dedicated-read-nodes#when-to-use-dedicated-read-nodes) and [Understanding cost](/guides/manage-cost/understanding-cost).

## See also

* [Decrease latency](/guides/optimize/decrease-latency)
* [Increase throughput](/guides/optimize/increase-throughput)
* [Manage cost](/guides/manage-cost/manage-cost)
