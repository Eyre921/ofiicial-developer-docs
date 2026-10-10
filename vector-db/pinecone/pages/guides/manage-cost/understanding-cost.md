---
title: "Understand Pinecone cost"
source: https://docs.pinecone.io/guides/manage-cost/understanding-cost
path: guides/manage-cost/understanding-cost
---

Understand how Pinecone bills read units, write units, storage, egress, and embedding for full-text search, semantic search, and hybrid search.

Pinecone serverless is usage-based, so you pay for the data you store and the operations you run. Many small workloads fit within the free [Starter plan](https://www.pinecone.io/pricing/).

<Tip>
  This page explains how usage is measured. For current rates, see [Pricing](https://www.pinecone.io/pricing/).
</Tip>

## Ways to reduce cost

* Build and test on the Starter plan, which is free and has no monthly minimum.
* Buy prepaid credits or commit to annual usage for discounted rates. See [Prepaid credits](#prepaid-credits).
* Split data into namespaces so each query scans less data, and keep read responses small. See [Save on costs](/guides/optimize/save-on-costs).
* On the Standard or Enterprise plan, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) about volume discounts and ways to lower your costs.

## Minimum usage

The Builder, Standard, and Enterprise [pricing plans](https://www.pinecone.io/pricing/) include a monthly minimum usage commitment:

| Plan | Minimum usage |
| - | - |
| Starter | \$0/month |
| Builder | \$20/month (flat) |
| Standard | \$50/month |
| Enterprise | \$500/month |

On the Builder plan, the monthly minimum is a flat fee that covers included usage; additional usage beyond [Builder limits](/reference/api/database-limits/rate-limits#monthly-usage-limits) is blocked rather than billed. On the Standard and Enterprise plans, customers are charged for what they use each month beyond the monthly minimum.

The minimum is a commitment you grow into rather than an extra charge. Once your usage exceeds the minimum, you pay only for what you use.

**Examples**

<AccordionGroup>
  <Accordion title="Usage below monthly minimum">
    * You are on the Standard plan.
    * Your usage for the month of August amounts to \$20.
    * Your usage is below the \$50 monthly minimum, so your total for the month is \$50.

    In this case, the August invoice would include line items for each service you used (totaling \$20), plus a single line item covering the rest of the minimum usage commitment (\$30).
  </Accordion>

  <Accordion title="Usage exceeds monthly minimum">
    * You are on the Standard plan.
    * Your usage for the month of August amounts to \$100.
    * Your usage exceeds the \$50 monthly minimum, so your total for the month is \$100.

    In this case, the August invoice would only show line items for each service you used (totaling \$100). Since your usage exceeds the minimum usage commitment, you are only charged for your actual usage and no additional minimum usage line item appears on your invoice.
  </Accordion>
</AccordionGroup>

## Prepaid credits

Pinecone offers an incentive for customers who purchase prepaid credits with an upfront payment. Customers may purchase between \$8,000 and \$25,000 in prepaid credits.

Customers who purchase prepaid credits can unlock additional usage capacity at no extra cost. The available benefits vary based on the selected plan and prepaid amount.

Prepaid credits apply to Pinecone services at List Price. Any usage that exceeds the available prepaid credits will be billed at full List Price.

Customers on Standard and Enterprise pay-as-you-go plans can purchase prepaid credits directly by navigating in the Pinecone console to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).

<Note>
  Purchasing prepaid credits isn't available through cloud marketplace billing. To purchase prepaid credits through a cloud marketplace, contact [ar@pinecone.io](mailto:ar@pinecone.io).
</Note>

## Serverless indexes

With serverless indexes, you pay for the amount of data stored and operations performed, based on four usage metrics: [read units](#read-units), [write units](#write-units), [storage](#storage), and [egress](#egress).

[Full-text search](/guides/search/full-text-search) on a document index, semantic search on a vector index, and [hybrid search](/guides/search/hybrid-search) that combines the two are all metered by the same four metrics.

For the latest serverless pricing rates, see [Pricing](https://www.pinecone.io/pricing/).

### Read units

A read unit (RU) measures the compute, I/O, and network resources a read request uses. Pinecone bills these read requests in RUs:

* [Query](#query)
* [Fetch](#fetch)
* [List](#list)
* [Full-text search](#full-text-search)

<Tip>
  Read responses include the number of RUs used, which you can use to [monitor read costs](/guides/manage-cost/monitor-usage-and-costs#read-units).
</Tip>

<Note>
  Indexes built on [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes/overview) aren't subject to read unit limits for query, fetch, list, and full-text search operations. For sizing and capacity planning guidance, see the [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes/overview) guide.
</Note>

#### Query

A query uses 1 RU for every 1 GB of namespace size, with a minimum of 0.25 RUs per query.

| Namespace size | Read units per query |
| :- | :- |
| \< 0.25 GB | 0.25 RUs (minimum) |
| 1 GB | 1 RU |
| 10 GB | 10 RUs |
| 50 GB | 50 RUs |
| 100 GB | 100 RUs |

To learn how to calculate your namespace size, see [Storage](#storage).

<Note>
  Parameters that affect the size of the query response, such as `top_k`, `include_metadata`, and `include_values`, don't affect query cost. Only the size of the namespace does.
</Note>

#### Fetch

A fetch request uses 1 RU for every 10 records fetched, for example:

| Fetched records | RUs |
| :- | :- |
| 10 | 1 |
| 50 | 5 |
| 107 | 11 |

Specifying a non-existent ID or adding the same ID more than once doesn't increase the number of RUs used. A fetch request always uses at least 1 RU.

<Note>
  [Fetching records by metadata](/guides/manage-data/fetch-data#fetch-records-by-metadata) uses the same cost model as fetching by ID: 1 RU for every 10 records fetched.
</Note>

#### List

A list request uses 1 RU and returns up to 100 IDs.

#### Full-text search

Searching a [document index](/guides/search/full-text-search) uses 1 RU for every 1 GB of namespace size, with a minimum of 0.25 RUs per search, the same as a [query](#query). This holds whether the request ranks by keyword relevance or by vector similarity.

A document index can declare `string` fields with `full_text_search` enabled and a `dense_vector` field in one schema, and each request ranks by one of them. So a [hybrid search](/guides/search/hybrid-search) that narrows candidates with a [text-match filter](/guides/search/filter-by-metadata#text-match-filters) and then ranks what remains with a `dense_vector` search is billed as one read request. Running a separate keyword search and dense search and merging the results client-side is billed as two.

### Write units

A write unit (WU) measures the storage and compute resources a write request uses. Pinecone bills these write requests in WUs:

* [Upsert](#upsert)
* [Update](#update)
* [Delete](#delete)

<Note>
  Writes to a [document index](/guides/index-data/adopt-the-documents-api) use the same cost models as writes to a vector index. The formulas below apply to both.
</Note>

#### Upsert

An upsert request uses 1 WU for each 1 KB of the request, with a minimum of 5 WUs per request. When an upsert modifies an existing record, the request also uses 1 WU for each 1 KB of the existing record.

The following table shows the WUs used by upsert requests at different batch sizes and record sizes, assuming all records are new:

| Records per batch | Dimension | Avg. metadata size | Avg. record size | WUs |
| :- | :- | :- | :- | :- |
| 1 | 768 | 100 bytes | 3.2 KB | 5 |
| 2 | 768 | 100 bytes | 3.2 KB | 7 |
| 10 | 1024 | 15,000 bytes | 19.10 KB | 191 |
| 100 | 768 | 500 bytes | 3.57 KB | 357 |
| 1,000 | 1536 | 1,000 bytes | 7.14 KB | 7,140 |

#### Update

An update request uses 1 WU for each 1 KB of the new and existing record, with a minimum of 5 WUs per request.

The following table shows the WUs used by an update at different record sizes:

| New record size | Previous record size | WUs |
| :- | :- | :- |
| 6.24 KB | 6.50 KB | 13 |
| 19.10 KB | 15 KB | 25 |
| 3.57 KB | 5 KB | 9 |
| 7.14 KB | 10 KB | 18 |
| 3.17 KB | 3.17 KB | 7 |

<Note>
  [Updating records by metadata](/guides/manage-data/update-data#update-by-metadata) uses the same cost model as updating by ID: 1 WU for each 1 KB of the new and existing record.
</Note>

#### Delete

A delete request uses 1 WU for each 1 KB of records deleted, with a minimum of 5 WUs per request.

The following table shows the WUs used by delete requests at different batch sizes and record sizes:

| Records per batch | Dimension | Avg. metadata size | Avg. record size | WUs |
| :- | :- | :- | :- | :- |
| 1 | 768 | 100 bytes | 3.2 KB | 5 |
| 2 | 768 | 100 bytes | 3.2 KB | 7 |
| 10 | 1024 | 15,000 bytes | 19.10 KB | 191 |
| 100 | 768 | 500 bytes | 3.57 KB | 357 |
| 1,000 | 1536 | 1,000 bytes | 7.14 KB | 7,140 |

Specifying a non-existent ID or adding the same ID more than once doesn't increase WU use.

[Deleting a namespace](/guides/manage-data/manage-namespaces#delete-a-namespace) or [deleting all records in a namespace using `deleteAll`](/guides/manage-data/delete-data#delete-all-records-in-a-namespace) uses 5 WUs.

<Note>
  [Deleting records by metadata](/guides/manage-data/delete-data#delete-records-by-metadata) uses the same cost model as deleting by ID: 1 WU for each 1 KB of records deleted.
</Note>

### Storage

Storage is billed monthly per gigabyte (GB) of index size. An index's size is the total size of its records or documents across all namespaces. For the latest storage pricing rates, see [Pricing](https://www.pinecone.io/pricing/).

A document in a document index can include any combination of `string` fields with `full_text_search` enabled, a dense vector, and a sparse vector. A record in a vector index can include a dense vector, a sparse vector, or both. Use the formula that matches your index to calculate total size:

<div>
  <Tabs>
    <Tab title="Document index">
      A [document index](/guides/index-data/indexing-overview#document-index) contains documents. Each document's size is its ID, its metadata, and the data in every schema field it holds.

      ```text Calculate size theme={null}
      Index size = Number of documents × (
                     ID size +
                     Metadata size +
                     Total full-text-search field size +
                     Dense vector dimensions × 4 bytes +
                     Number of non-zero sparse values × 8 bytes
                   )
      ```

      Where:

      * `ID size` and `Metadata size` are measured in bytes, averaged across all documents. Metadata is every field that isn't declared in the schema.
      * `Total full-text-search field size`: The combined UTF-8 byte length of the text in all `string` fields with `full_text_search` enabled, averaged across all documents. A field with [integrated embedding](/guides/index-data/indexing-overview#integrated-embedding) but no `full_text_search` doesn't store its text, so only its generated vector counts. If a field has both, count its text here and its generated vector below.
      * Each `Dense vector dimension` uses 4 bytes. Sum the dimensions of every dense vector in the document, whether you upsert it or Pinecone generates it for an integrated-embedding field. Omit this term if the schema has no dense vector.
      * `Number of non-zero sparse values`: Average number across all documents, including those without sparse vectors. Count every sparse vector in the document, whether you upsert it or Pinecone generates it. Each non-zero value uses 8 bytes. Omit this term if the schema has no sparse vector.

      These examples assume 8-byte IDs:

      | Documents | Avg total full-text-search field size | Dense vector dimensions | Avg number of non-zero sparse values | Avg metadata size | Index size |
      | :- | :- | :- | :- | :- | :- |
      | 500,000 | 2,000 bytes | None | None | 500 bytes | 1.25 GB |
      | 1,000,000 | 5,000 bytes | 1024 | None | 1,000 bytes | 10.1 GB |
      | 5,000,000 | 2,000 bytes | 768 | 100 | 500 bytes | 31.9 GB |

      <Note>
        Example: 1,000,000 documents × (8-byte ID + 5,000 bytes of full-text-search text + (1024 dense vector dimensions × 4 bytes) + 1,000 bytes of metadata) = 10.1 GB
      </Note>
    </Tab>

    <Tab title="Index of dense vectors">
      An [index of dense vectors](/guides/index-data/indexing-overview#indexes-with-dense-vectors) contains records with one dense vector each.

      <Note>
        Records can also contain sparse vectors (when the index metric is set to `dotproduct`), which can be useful for [hybrid search](/guides/search/hybrid-search/single-index). To learn how to calculate size in that case, see [Index with both dense and sparse vectors](#index-with-both-dense-and-sparse-vectors).
      </Note>

      ```text Calculate size (assuming no sparse vectors) theme={null}
      Index size = Number of records × (
                     ID size + 
                     Metadata size +
                     Dense vector dimensions × 4 bytes
                   )
      ```

      Where:

      * `ID size` and `Metadata size` are measured in bytes, averaged across all records.
      * Each `Dense vector dimension` uses 4 bytes.

      These examples assume 8-byte IDs:

      | Records | Dense vector dimensions | Avg metadata size | Index size |
      | :- | :- | :- | :- |
      | 500,000 | 768 | 500 bytes | 1.79 GB |
      | 1,000,000 | 1536 | 1,000 bytes | 7.15 GB |
      | 5,000,000 | 1024 | 15,000 bytes | 95.5 GB |
      | 10,000,000 | 1536 | 1,000 bytes | 71.5 GB |

      <Note>
        Example: 500,000 records × (8-byte ID + (768 dense vector dimensions × 4 bytes) + 500 bytes of metadata) = 1.79 GB
      </Note>
    </Tab>

    <Tab title="Index of sparse vectors">
      An [index of sparse vectors](/guides/index-data/indexing-overview#indexes-with-sparse-vectors) contains records with one sparse vector each.

      ```text Calculate size theme={null}
      Index size = Number of records × (
                     ID size + 
                     Metadata size +
                     Number of non-zero sparse values × 8 bytes
                   )
      ```

      Where:

      * `ID size` and `Metadata size` are measured in bytes, averaged across all records.
      * `Number of non-zero sparse values`: Average number across all records. To find the count for a single record, check the length of the sparse vector's `indices` or `values` array. Each non-zero value uses 8 bytes.

      These examples assume 8-byte IDs:

      | Records | Avg number of non-zero sparse values | Avg metadata size | Index size |
      | :- | :- | :- | :- |
      | 500,000 | 10 | 500 bytes | 0.29 GB |
      | 1,000,000 | 50 | 1,000 bytes | 1.41 GB |
      | 5,000,000 | 100 | 15,000 bytes | 79.0 GB |
      | 10,000,000 | 50 | 1,000 bytes | 14.1 GB |

      <Note>
        Example: 500,000 records × (8-byte ID + (10 non-zero sparse values × 8 bytes) + 500 bytes of metadata) = 0.29 GB
      </Note>
    </Tab>

    <Tab title="Index with both dense and sparse vectors">
      An [index with both dense and sparse vectors](/guides/search/hybrid-search/single-index) contains records that each have one dense vector and an optional sparse vector.

      ```text Calculate size theme={null}
      Index size = Number of records × (
                     ID size + 
                     Metadata size +
                     Dense vector dimensions × 4 bytes + 
                     Number of non-zero sparse values × 8 bytes
                   )
      ```

      Where:

      * `ID size` and `Metadata size` are measured in bytes, averaged across all records.
      * Each `Dense vector dimension` uses 4 bytes.
      * `Number of non-zero sparse values`: Average number across all records, including those without sparse vectors. To find the count for a single record, check the length of the sparse vector's `indices` or `values` array. Each non-zero value uses 8 bytes.

      These examples assume 8-byte IDs:

      | Records | Dense vector dimensions | Avg number of non-zero sparse values | Avg metadata size | Index size |
      | :- | :- | :- | :- | :- |
      | 500,000 | 768 | 10 | 500 bytes | 1.83 GB |
      | 1,000,000 | 1536 | 50 | 1,000 bytes | 7.54 GB |
      | 5,000,000 | 1024 | 100 | 15,000 bytes | 99.5 GB |
      | 10,000,000 | 1536 | 50 | 1,000 bytes | 75.4 GB |

      <Note>
        Example: 500,000 records × (8-byte ID + (768 dense vector dimensions × 4 bytes) + (10 non-zero sparse values × 8 bytes) + 500 bytes of metadata) = 1.83 GB
      </Note>
    </Tab>
  </Tabs>
</div>

### Egress

Egress measures the data Pinecone returns to you on serverless reads. Egress is measured in GB of total response bytes returned by an in-scope read request, proportional to the record or document data returned (IDs, scores, vector values, text fields, and metadata).

Egress is metered on read requests that return per-record or per-document data:

* [Query](/guides/search/search-overview)
* [Fetch](/guides/manage-data/fetch-data) (records and documents, by ID and by metadata)
* [List](/guides/manage-data/list-record-ids) (record and document IDs)
* [Text search](/reference/api/latest/data-plane/search_records) on integrated indexes
* Search on a document index, whether it ranks by [full-text search](/guides/search/full-text-search) or by vector similarity

Write requests (upsert, update, delete, import), index statistics (such as `describe_index_stats`), and index management requests aren't metered for egress.

Egress applies to indexes that use [dedicated read nodes](/guides/index-data/dedicated-read-nodes/overview) as well as on-demand indexes, because it depends on the data returned to you rather than on the hardware serving the read.

<Note>
  Egress accrues on all bytes returned by in-scope reads, including IDs, scores, and metadata. Leaving vector values out of a [query](/guides/search/search-overview) response (`include_values=false`, the default) lowers egress, but it doesn't exempt the request, because IDs and scores are still returned. `fetch` always returns values, so use `query` when you're searching and only need IDs or metadata.
</Note>

#### Egress allowance

Each plan includes a monthly egress allowance, which resets at the start of each billing period:

| Plan | Monthly egress allowance |
| :- | :- |
| Starter | 1 GB |
| Builder | 10 GB |
| Standard | 100 GB |
| Enterprise | 100 GB |

What happens past the allowance depends on your plan:

* **Usage-based plans (Standard, Enterprise):** Egress beyond the allowance is billed at the per-GB overage rate and reads keep serving. For the latest egress rate, see [Pricing](https://www.pinecone.io/pricing/).
* **Flat-fee plans (Starter, Builder):** In-scope reads are blocked with a `RESOURCE_EXHAUSTED` (429) error and an upgrade prompt once the allowance is reached. Index statistics, index management, and write requests remain available, and the allowance resets at the start of the next billing period.

## Imports

[Importing from object storage](/guides/index-data/import-data) is the most cost-effective way to load large numbers of records into an index. An import is billed by the size of the records it reads, whether or not they import successfully.

If the import fails (e.g., after it reads a vector of the wrong dimension in an import with `on_error="abort"`), you're still charged for the records read. If the import fails because of an internal system error, you aren't charged, and the import returns the error message `"We were unable to process your request. If the problem persists, please contact us at https://support.pinecone.io"`.

For the latest import pricing rates, see [Pricing](https://www.pinecone.io/pricing/).

## Backups and restores

A [backup](/guides/manage-data/backups-overview) is a static copy of a serverless index. Storing a backup and [restoring an index](/guides/manage-data/restore-an-index) from a backup are both billed by the size of the index. For the latest backup and restore pricing rates, see [Pricing](https://www.pinecone.io/pricing/).

## Embedding

Pinecone hosts several [embedding models](/guides/index-data/create-an-index#embedding-models). You can use a hosted model to embed your data as an integrated part of upserting and querying, or you can use a hosted model to embed your data as a standalone operation.

Embedding is billed by the number of [tokens](https://www.pinecone.io/learn/tokenization/) in a request. The more words in your passage or query, the more tokens it generates.

For example, if you generate embeddings for the query, "What is the maximum diameter of a red pine?", Pinecone Inference generates 10 tokens, then converts them into an embedding. If your plan's rate is \$0.08 per million tokens, this call costs \$0.0000008.

To learn more about tokenization, see [Choosing an embedding model](https://www.pinecone.io/learn/series/rag/embedding-models-rundown/). For the latest embed pricing rates, see [Pricing](https://www.pinecone.io/pricing/).

<Tip>
  Embedding requests return the total tokens generated. You can use this information to [monitor and manage embedding costs](/guides/manage-cost/monitor-usage-and-costs#embedding-tokens).
</Tip>

## Reranking

Pinecone hosts several [reranking models](/guides/search/rerank-results#reranking-models). You can use a hosted model to rerank results as an integrated part of a query, or you can use a hosted model to rerank results as a standalone operation.

Reranking is billed by the number of requests to the reranking model. For the latest rerank pricing rates, see [Pricing](https://www.pinecone.io/pricing/).

## Assistant

For details on how costs are incurred in Pinecone Assistant, see [Assistant pricing](/guides/assistant/pricing-and-limits).

## HIPAA compliance add-on

Full HIPAA compliance is included with the [Enterprise plan](https://www.pinecone.io/pricing/). On the Enterprise plan or with the add-on, HIPAA compliance requires you to [configure audit logs](/guides/production/configure-audit-logs).

On the Standard plan, HIPAA compliance is available as an optional add-on for \$190 per month. The add-on is billed monthly and added to your regular invoice. A 6-month minimum period is required.

The HIPAA compliance add-on includes:

* HIPAA-ready infrastructure
* Encrypted data storage
* Audit logging
* Enhanced security controls
* BAA execution and compliance documentation support

<Note>
  If you upgrade to the Enterprise plan, the HIPAA compliance add-on is automatically removed because HIPAA compliance is included with Enterprise.
</Note>

### Enable the HIPAA compliance add-on

To enable the HIPAA compliance add-on, [submit a HIPAA request](https://www.pinecone.io/contact/hipaa/). The Pinecone team reviews your request and guides you through activation.

## See also

* [Manage cost](/guides/manage-cost/manage-cost)
* [Monitor usage](/guides/manage-cost/monitor-usage-and-costs)
* [Full-text search](/guides/search/full-text-search)
* [Hybrid search](/guides/search/hybrid-search)
* [Configure audit logs](/guides/production/configure-audit-logs)
* [Pricing](https://www.pinecone.io/pricing/)
