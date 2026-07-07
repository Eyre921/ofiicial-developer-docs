---
title: "Understanding cost"
source: https://docs.pinecone.io/guides/manage-cost/understanding-cost
path: guides/manage-cost/understanding-cost
---

Understand how costs are incurred in Pinecone, including read units (RUs), write units (WUs), storage, egress, and embedding.

For the latest pricing details, see [Pricing](https://www.pinecone.io/pricing/).

Pinecone serverless is usage-based, so you pay only for the data you store and the operations you run. Idle indexes cost nothing. Most early and small workloads fit within the free [Starter plan](https://www.pinecone.io/pricing/), and you can lower costs further as you scale.

## Ways to reduce cost

* **Start free.** The Starter plan has no monthly minimum, so you can build and test before committing to any spend.
* **Prepaid credits and annual commitments.** Committing usage upfront earns discounted rates. See [Prepaid credits](#prepaid-credits).
* **Bulk import credit.** Standard and Enterprise organizations receive a one-time 1 TB import credit for loading data from object storage. See [Imports](#imports).
* **Optimize your workload.** Use namespaces and right-size your reads to cut ongoing query cost. See [Save on costs](/guides/optimize/save-on-costs).
* **Talk to us.** Standard and Enterprise customers can [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) to optimize costs and discuss volume discounts.

## Minimum usage

The Builder, Standard, and Enterprise [pricing plans](https://www.pinecone.io/pricing/) include a monthly minimum usage commitment:

| Plan       | Minimum usage     |
| ---------- | ----------------- |
| Starter    | \$0/month         |
| Builder    | \$20/month (flat) |
| Standard   | \$50/month        |
| Enterprise | \$500/month       |

On the Builder plan, the monthly minimum is a flat fee that covers included usage; additional usage beyond [Builder limits](/reference/api/database-limits) is blocked rather than billed. On the Standard and Enterprise plans, customers are charged for what they use each month beyond the monthly minimum.

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
  Purchasing prepaid credits is not available through cloud marketplace billing. To purchase prepaid credits through a cloud marketplace, contact [ar@pinecone.io](mailto:ar@pinecone.io).
</Note>

## Serverless indexes

With serverless indexes, you pay for the amount of data stored and operations performed, based on four usage metrics: [read units](#read-units), [write units](#write-units), [storage](#storage), and [egress](#egress).

For the latest serverless pricing rates, see [Pricing](https://www.pinecone.io/pricing/).

### Read units

A **read unit (RU)** is the unit Pinecone uses to measure and price the cost of a read request. Read units (RUs) measure the compute, I/O, and network resources consumed by the following read requests:

* [Query](#query)
* [Fetch](#fetch)
* [List](#list)

<Tip>
  Read requests return the number of RUs used. You can use this information to [monitor read costs](/guides/manage-cost/monitor-usage-and-costs#read-units).
</Tip>

<Note>
  Indexes built on [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) are not subject to read unit limits for query, fetch, and list operations. For sizing and capacity planning guidance, see the [Dedicated Read Nodes](/guides/index-data/dedicated-read-nodes) guide.
</Note>

#### Query

The cost of a query scales linearly with the size of the targeted namespace. Specifically, a query uses 1 RU for every 1 GB of namespace size, with a minimum of 0.25 RUs per query.

| Namespace size | Read units per query |
| :------------- | :------------------- |
| \< 0.25 GB     | 0.25 RUs (minimum)   |
| 1 GB           | 1 RU                 |
| 10 GB          | 10 RUs               |
| 50 GB          | 50 RUs               |
| 100 GB         | 100 RUs              |

To learn how to calculate your namespace size, see [Storage](#storage).

<Note>
  Parameters that affect the size of the query response, such as `top_k`, `include_metadata`, and `include_values`, are not relevant for query cost; only the size of the namespace determines the number of RUs used.
</Note>

#### Fetch

A fetch request uses 1 RU for every 10 records fetched, for example:

| Fetched records | RUs |
| --------------- | --- |
| 10              | 1   |
| 50              | 5   |
| 107             | 11  |

Specifying a non-existent ID or adding the same ID more than once does not increase the number of RUs used. However, a fetch request will always use at least 1 RU.

<Note>
  [Fetching records by metadata](/guides/manage-data/fetch-data#fetch-records-by-metadata) uses the same cost model as fetching by ID: 1 RU for every 10 records fetched.
</Note>

#### List

List has a fixed cost of 1 RU per call, with up to 100 records per call.

### Write units

A **write unit (WU)** is the unit Pinecone uses to measure and price the cost of a write request. Write units (WUs) measure the storage and compute resources used by the following write requests:

* [Upsert](#upsert)
* [Update](#update)
* [Delete](#delete)

#### Upsert

An upsert request uses 1 WU for each 1 KB of the request, with a minimum of 5 WUs per request. When an upsert modifies an existing record, the request uses 1 WU for each 1 KB of the existing record as well.

For example, the following table shows the WUs used by upsert requests at different batch sizes and record sizes, assuming all records are new:

| Records per batch | Dimension | Avg. metadata size | Avg. record size | WUs  |
| :---------------- | :-------- | :----------------- | :--------------- | :--- |
| 1                 | 768       | 100 bytes          | 3.2 KB           | 5    |
| 2                 | 768       | 100 bytes          | 3.2 KB           | 7    |
| 10                | 1024      | 15,000 bytes       | 19.10 KB         | 191  |
| 100               | 768       | 500 bytes          | 3.57 KB          | 357  |
| 1000              | 1536      | 1000 bytes         | 7.14 KB          | 7140 |

#### Update

An update request uses 1 WU for each 1 KB of the new and existing record, with a minimum of 5 WUs per request.

For example, the following table shows the WUs used by an update at different record sizes:

| New record size | Previous record size | WUs |
| :-------------- | :------------------- | :-- |
| 6.24 KB         | 6.50 KB              | 13  |
| 19.10 KB        | 15 KB                | 25  |
| 3.57 KB         | 5 KB                 | 9   |
| 7.14 KB         | 10 KB                | 18  |
| 3.17 KB         | 3.17 KB              | 7   |

<Note>
  [Updating records by metadata](/guides/manage-data/update-data#update-by-metadata) uses the same cost model as updating by ID: 1 WU for each 1 KB of the new and existing record.
</Note>

#### Delete

A delete request uses 1 WU for each 1 KB of records deleted, with a minimum of 5 WUs per request.

For example, the following table shows the WUs used by delete requests at different batch sizes and record sizes:

| Records per batch | Dimension | Avg. metadata size | Avg. record size | WUs  |
| :---------------- | :-------- | :----------------- | :--------------- | :--- |
| 1                 | 768       | 100 bytes          | 3.2 KB           | 5    |
| 2                 | 768       | 100 bytes          | 3.2 KB           | 7    |
| 10                | 1024      | 15,000 bytes       | 19.10 KB         | 191  |
| 100               | 768       | 500 bytes          | 3.57 KB          | 357  |
| 1000              | 1536      | 1000 bytes         | 7.14 KB          | 7140 |

Specifying a non-existent ID or adding the same ID more than once does not increase WU use.

[Deleting a namespace](/guides/manage-data/manage-namespaces#delete-a-namespace) or [deleting all records in a namespace using `deleteAll`](/guides/manage-data/delete-data#delete-all-records-in-a-namespace) uses 5 WUs.

<Note>
  [Deleting records by metadata](/guides/manage-data/delete-data#delete-records-by-metadata) uses the same cost model as deleting by ID: 1 WU for each 1 KB of records deleted.
</Note>

### Storage

Storage costs are based on the size of an index on a per-gigabyte (GB) monthly rate. The size of an index is defined as the total size of its records across all namespaces. For the latest storage pricing rates, see [Pricing](https://www.pinecone.io/pricing/).

A record can include a dense vector, a sparse vector, or both. Use the formula that matches your data to calculate total size:

<div>
  <Tabs>
    <Tab title="Index of dense vectors">
      An [index of dense vectors](/guides/index-data/indexing-overview#indexes-with-dense-vectors) contains records with one dense vector each.

      <Note>
        Records can also contain sparse vectors (when the index metric is set to `dotproduct`), which can be useful for [hybrid search](/guides/search/hybrid-search#use-a-single-index-for-dense-and-sparse-vectors). To learn how to calculate size in that case, see [Index with both dense and sparse vectors](#index-with-both-dense-and-sparse-vectors).
      </Note>

      **Calculate size (assuming no sparse vectors)**

      ```
      Index size = Number of records × (
                     ID size + 
                     Metadata size +
                     Dense vector dimensions × 4 bytes
                   )
      ```

      Where:

      * `ID size` and `Metadata size` are measured in bytes, averaged across all records.
      * Each `Dense vector dimension` uses 4 bytes.

      **Example calculations**

      These examples assume 8-byte IDs:

      | Records    | Dense vector dimensions | Avg metadata size | Index size |
      | :--------- | :---------------------- | :---------------- | :--------- |
      | 500,000    | 768                     | 500 bytes         | 1.79 GB    |
      | 1,000,000  | 1536                    | 1,000 bytes       | 7.15 GB    |
      | 5,000,000  | 1024                    | 15,000 bytes      | 95.5 GB    |
      | 10,000,000 | 1536                    | 1,000 bytes       | 71.5 GB    |

      <Note>
        Example: 500,000 records × (8-byte ID + (768 dense vector dimensions × 4 bytes) + 500 bytes of metadata) = 1.79 GB
      </Note>
    </Tab>

    <Tab title="Index of sparse vectors">
      An [index of sparse vectors](/guides/index-data/indexing-overview#indexes-with-sparse-vectors) contains records with one sparse vector each.

      **Calculate size**

      ```
      Index size = Number of records × (
                     ID size + 
                     Metadata size +
                     Number of non-zero sparse values × 8 bytes
                   )
      ```

      Where:

      * `ID size` and `Metadata size` are measured in bytes, averaged across all records.
      * `Number of non-zero sparse values`: Average number across all records. To find the count for a single record, check the length of the sparse vector's `indices` or `values` array. Each non-zero value uses 8 bytes.

      **Example calculations**

      These examples assume 8-byte IDs:

      | Records    | Avg number of non-zero sparse values | Avg metadata size | Index size |
      | :--------- | :----------------------------------- | :---------------- | :--------- |
      | 500,000    | 10                                   | 500 bytes         | 0.29 GB    |
      | 1,000,000  | 50                                   | 1,000 bytes       | 1.41 GB    |
      | 5,000,000  | 100                                  | 15,000 bytes      | 79.0 GB    |
      | 10,000,000 | 50                                   | 1,000 bytes       | 14.1 GB    |

      <Note>
        Example: 500,000 records × (8-byte ID + (10 non-zero sparse values × 8 bytes) + 500 bytes of metadata) = 0.29 GB
      </Note>
    </Tab>

    <Tab title="Index with both dense and sparse vectors">
      An [index with both dense and sparse vectors](/guides/search/hybrid-search#use-a-single-index-for-dense-and-sparse-vectors) contains records that each have one dense vector and an optional sparse vector.

      **Calculate size**

      ```
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

      **Example calculations**

      These examples assume 8-byte IDs:

      | Records    | Dense vector dimensions | Avg number of non-zero sparse values | Avg metadata size | Index size |
      | :--------- | :---------------------- | :----------------------------------- | :---------------- | :--------- |
      | 500,000    | 768                     | 10                                   | 500 bytes         | 1.83 GB    |
      | 1,000,000  | 1536                    | 50                                   | 1,000 bytes       | 7.54 GB    |
      | 5,000,000  | 1024                    | 100                                  | 15,000 bytes      | 99.5 GB    |
      | 10,000,000 | 1536                    | 50                                   | 1,000 bytes       | 75.4 GB    |

      <Note>
        Example: 500,000 records × (8-byte ID + (768 dense vector dimensions × 4 bytes) + (10 non-zero sparse values × 8 bytes) + 500 bytes of metadata) = 1.83 GB
      </Note>
    </Tab>
  </Tabs>
</div>

### Egress

**Egress** measures the data Pinecone returns to you on serverless reads. Egress is measured in GB of total response bytes returned by an in-scope read request, proportional to the record data returned (IDs, scores, values, and metadata).

Egress is metered on read requests that return per-record data:

* [Query](/guides/search/search-overview)
* [Fetch](/guides/manage-data/fetch-data) (by ID and by metadata)
* [List](/guides/manage-data/list-record-ids)
* [Text search](/reference/api/latest/data-plane/search_records) on integrated indexes
* [Full-text search](/guides/search/full-text-search)

Write requests (upsert, update, delete, import), index statistics (such as `describe_index_stats`), and index management requests are not metered for egress.

<Note>
  Egress accrues on all bytes returned by in-scope reads, including IDs, scores, and metadata. Setting `include_values=false` on a [fetch](/guides/manage-data/fetch-data#fetch-records) or query lowers egress but does not exempt the request, because IDs and metadata are still returned.
</Note>

<Tip>
  In-scope read requests return the egress consumed in the response `usage` object. You can use this information to [monitor egress](/guides/manage-cost/monitor-usage-and-costs#egress).
</Tip>

#### Egress allowance

Each plan includes a monthly egress allowance, which resets at the start of each billing period:

| Plan       | Monthly egress allowance |
| :--------- | :----------------------- |
| Free       | 1 GB                     |
| Builder    | 10 GB                    |
| Standard   | 100 GB                   |
| Enterprise | 100 GB                   |

What happens past the allowance depends on your plan:

* **Usage-based plans (Standard, Enterprise):** egress beyond the allowance is billed at the per-GB overage rate and reads keep serving. For the latest egress rate, see [Pricing](https://www.pinecone.io/pricing/).
* **Flat-fee plans (Free, Builder):** in-scope reads are blocked with a `RESOURCE_EXHAUSTED` (429) error and an upgrade prompt once the allowance is reached. Index statistics, index management, and write requests remain available, and the allowance resets at the start of the next billing period.

## Imports

[Importing from object storage](/guides/index-data/import-data) is the most efficient and cost-effective method to load large numbers of records into an index. The cost of an import is based on the size of the records read, whether the records were imported successfully or not.

If the import operation fails (e.g., after encountering a vector of the wrong dimension in an import with `on_error="abort"`), you will still be charged for the records read. However, if the import fails because of an internal system error, you will not incur charges. In this case, the import will return the error message `"We were unable to process your request. If the problem persists, please contact us at https://support.pinecone.io"`.

<Note>
  Standard and Enterprise organizations receive a **one-time 1 TB bulk import credit**, valid through July 31, 2026. Usage beyond the free allotment is billed at the standard import rate. Builder and Free plans are not eligible.
</Note>

For the latest import pricing rates, see [Pricing](https://www.pinecone.io/pricing/).

## Backups and restores

A [backup](/guides/manage-data/backups-overview) is a static copy of a serverless index. Both the cost of storing a backup and [restoring an index](/guides/manage-data/restore-an-index) from a backup is based on the size of the index. For the latest backup and restore pricing rates, see [Pricing](https://www.pinecone.io/pricing/).

## Embedding

Pinecone hosts several [embedding models](/guides/index-data/create-an-index#embedding-models) so it's easy to manage your vector storage and search process on a single platform. You can use a hosted model to embed your data as an integrated part of upserting and querying, or you can use a hosted model to embed your data as a standalone operation.

Embedding costs are determined by how many [tokens](https://www.pinecone.io/learn/tokenization/) are in a request. In general, the more words contained in your passage or query, the more tokens you generate.

For example, if you generate embeddings for the query, "What is the maximum diameter of a red pine?", Pinecone Inference generates 10 tokens, then converts them into an embedding. If the price per token for your billing plan is \$.08 per million tokens, then this API call costs \$.00001.

To learn more about tokenization, see [Choosing an embedding model](https://www.pinecone.io/learn/series/rag/embedding-models-rundown/). For the latest embed pricing rates, see [Pricing](https://www.pinecone.io/pricing/).

<Tip>
  Embedding requests returns the total tokens generated. You can use this information to [monitor and manage embedding costs](/guides/manage-cost/monitor-usage-and-costs#embedding-tokens).
</Tip>

## Reranking

Pinecone hosts several [reranking models](/guides/search/rerank-results#reranking-models) so it's easy to manage two-stage vector retrieval on a single platform. You can use a hosted model to rerank results as an integrated part of a query, or you can use a hosted model to rerank results as a standalone operation.

Reranking costs are determined by the number of requests to the reranking model. For the latest rerank pricing rates, see [Pricing](https://www.pinecone.io/pricing/).

## Assistant

For details on how costs are incurred in Pinecone Assistant, see [Assistant pricing](/guides/assistant/pricing-and-limits).

## HIPAA compliance add-on

Full HIPAA compliance is included with the [Enterprise plan](https://www.pinecone.io/pricing/).

For **Standard plan** customers, HIPAA compliance is available as an optional add-on for **\$190 per month**. The add-on is billed monthly and added to your regular invoice. A 6-month minimum period is required.

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

To enable the HIPAA compliance add-on, [contact sales](mailto:sales@pinecone.io) or [submit a request](https://www.pinecone.io/contact/?contact_form_inquiry_type=Sales). The Pinecone team will review your request and guide you through activation.

## See also

* [Manage cost](/guides/manage-cost/manage-cost)
* [Monitor usage](/guides/manage-cost/monitor-usage-and-costs)
* [Pricing](https://www.pinecone.io/pricing/)
