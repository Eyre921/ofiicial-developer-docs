---
title: "Save on Pinecone costs"
source: https://docs.pinecone.io/guides/cost/save-on-costs
path: guides/cost/save-on-costs
---

Lower Pinecone costs with prepaid credits and discounts, bulk import, namespaces for multitenancy, and read patterns that use fewer read units.

You can lower your Pinecone bill with discounted rates and by changing how you load and read data. While you're building, the free [Starter plan](https://www.pinecone.io/pricing/) has no monthly minimum. For how usage is measured, see [Understand Pinecone cost](/guides/cost/understand-cost).

## Credits and discounts

Besides changing how you use the database, you can lower the rate you pay.

* Prepaid credits and annual commitments earn discounted usage rates. See [Prepaid credits](/guides/cost/understand-cost#prepaid-credits).
* Dedicated read nodes can lower cost for sustained, high read throughput when you fully use the provisioned capacity. See [Choose the right index capacity mode](#choose-the-right-index-capacity-mode).
* Standard and Enterprise customers can [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) to discuss volume discounts.

## Use bulk import for large loads

To populate a new namespace or load millions of records, [import from object storage](/guides/data/import-data) instead of streaming [upserts](/guides/data/upsert-data).

* Import handles one-time bulk loads from Parquet in your object store, and is priced on the data it reads during the job. See [Import cost](/guides/cost/understand-cost#imports).
* Upsert is priced in write units by request size. Many small requests can cost more than a few large ones carrying the same data. See [Write unit pricing](/guides/cost/understand-cost#write-units).

Use upsert (including [batch upsert](/guides/data/upsert-data#upsert-in-batches)) for ongoing, incremental ingestion after your initial load. For how import and upsert compare, see the [data ingestion overview](/guides/data/data-ingestion-overview).

## Use namespaces for multitenancy

If you need to isolate each customer's or user's data, [partition tenants with namespaces](/guides/data/implement-multitenancy) instead of creating separate indexes. This often lowers storage overhead and query cost, because a query's cost depends on the size of the namespace it scans.

## Read only what you need

* Avoid returning vector values from a query when you don't need them (`include_values=false`, the default), especially at high `top_k`. Values are typically the largest part of a response, so leaving them out lowers [egress](/guides/cost/understand-cost#egress) and helps you stay within your plan's egress allowance.
* Where your workload allows, use [metadata filters](/guides/search/filter-by-metadata) so queries scan fewer records.
* To retrieve known records without a query, use a [hierarchical ID schema](/guides/indexes/data-modeling#use-structured-ids), [list record IDs](/guides/data/list-record-ids) by prefix, and then [fetch](/guides/data/fetch-data) the records you need. A [query's read units](/guides/cost/understand-cost#query) grow with namespace size, while fetch [uses 1 read unit per 10 records](/guides/cost/understand-cost#fetch).

> [!NOTE]
>
> Omitting values lowers egress but not [read units](/guides/cost/understand-cost#read-units). Query read unit cost depends on the size of the namespace scanned, not the size of the response.

> [!NOTE]
>
> Indexes built on [Dedicated Read Nodes](/guides/optimize/dedicated-read-nodes/overview) aren't subject to read unit limits for query, fetch, list, and full-text search operations. For sizing and capacity planning guidance, see the [Dedicated Read Nodes](/guides/optimize/dedicated-read-nodes/overview) guide.

## Choose the right index capacity mode

For sustained, high read throughput, [dedicated read nodes](/guides/optimize/dedicated-read-nodes/overview) can be more cost-effective than on-demand when you fully use provisioned read capacity. For spiky or low-QPS workloads, on-demand may be cheaper. See [When to use dedicated read nodes](/guides/optimize/dedicated-read-nodes/overview#when-to-use-dedicated-read-nodes) and [Understand Pinecone cost](/guides/cost/understand-cost).

## See also

* [Decrease latency](/guides/optimize/decrease-latency)
* [Increase throughput](/guides/optimize/increase-throughput)
* [Understand Pinecone cost](/guides/cost/understand-cost)
* [Check usage per request](/guides/cost/check-usage-per-request)
