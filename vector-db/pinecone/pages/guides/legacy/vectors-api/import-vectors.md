---
title: "Import vectors into a legacy vector index"
source: https://docs.pinecone.io/guides/legacy/vectors-api/import-vectors
path: guides/legacy/vectors-api/import-vectors
---

Prepare Parquet files to bulk import dense, sparse, or hybrid vectors from object storage into a legacy vector index.

> [!NOTE]
>
> New projects should use the [Documents API](/guides/indexes/create-an-index#create-a-document-index). To move an existing index, see [Move to the Documents API](/guides/indexes/move-to-the-documents-api).

> [!NOTE]
>
> This feature is available on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).

A legacy vector index imports Parquet files from object storage. Follow the steps in [Import data](/guides/data/import-data) to create an index, add a storage integration, lay out one directory per namespace, and start the import. This page covers the Parquet file format for each kind of legacy vector index.

You can also import Parquet files into a legacy integrated index, but its records must contain vectors, not text. To add text that Pinecone embeds, use [Upsert text](/guides/legacy/records-api/upsert-text).

## Parquet file format

> [tab] Dense vectors
>
> To import into a namespace in an [index of dense vectors](/guides/indexes/index-data-overview#indexes-with-dense-vectors), the Parquet file must contain the following columns:
>
> | Column name | Parquet type | Description |
> | - | - | - |
> | `id` | `STRING` | Required. The unique [identifier for each record](/guides/get-started/key-terms#record-id). |
> | `values` | `LIST<FLOAT>` | Required. A list of floating-point values that make up the [dense vector embedding](/guides/get-started/key-terms#dense-vector). |
> | `metadata` | `STRING` | Optional. Additional [metadata](/guides/get-started/key-terms#metadata) for each record. To omit from specific rows, use `NULL`. |
>
> > [!NOTE]
> >
> > Additional columns in the Parquet file are silently ignored during import; only `id`, `values`, and `metadata` are processed.
>
> For example:
>
> ```parquet theme={null}
> id | values                   | metadata
> --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
> 1  | [ 3.82  2.48 -4.15 ... ] | {"year": 1984, "month": 6, "source": "source1", "title": "Example1", "text": "When ..."}
> 2  | [ 1.82  3.48 -2.15 ... ] | {"year": 1990, "month": 4, "source": "source2", "title": "Example2", "text": "Who ..."}
> ```

> [tab] Sparse vectors
>
> To import into a namespace in an [index of sparse vectors](/guides/indexes/index-data-overview#indexes-with-sparse-vectors), the Parquet file must contain the following columns:
>
> | Column name | Parquet type | Description |
> | - | - | - |
> | `id` | `STRING` | Required. The unique [identifier for each record](/guides/get-started/key-terms#record-id). |
> | `sparse_values` | `STRUCT<indices: LIST<UINT_32>, values: LIST<FLOAT>>` | Required. A list of floating-point values (sparse values) and a list of integer values (sparse indices) that make up the [sparse vector embedding](/guides/get-started/key-terms#sparse-vector). |
> | `metadata` | `STRING` | Optional. Additional [metadata](/guides/get-started/key-terms#metadata) for each record. To omit from specific rows, use `NULL`. |
>
> > [!NOTE]
> >
> > Additional columns in the Parquet file are silently ignored during import; only `id`, `sparse_values`, and `metadata` are processed.
>
> For example:
>
> ```parquet theme={null}
> id | sparse_values                                                                                       | metadata
> --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
> 1  | {"indices": [ 822745112 1009084850 1221765879 ... ], "values": [1.7958984 0.41577148 2.828125 ...]} | {"year": 1984, "month": 6, "source": "source1", "title": "Example1", "text": "When ..."}
> 2  | {"indices": [ 504939989 1293001993 3201939490 ... ], "values": [1.4383747 0.72849722 1.384775 ...]} | {"year": 1990, "month": 4, "source": "source2", "title": "Example2", "text": "Who ..."}
> ```

> [tab] Dense + sparse
>
> To import into a namespace in an [index with both dense and sparse vectors](/guides/legacy/vectors-api/hybrid-search-single-index), the Parquet file must contain the following columns:
>
> | Column name | Parquet type | Description |
> | - | - | - |
> | `id` | `STRING` | Required. The unique [identifier for each record](/guides/get-started/key-terms#record-id). |
> | `values` | `LIST<FLOAT>` | Required. A list of floating-point values that make up the [dense vector embedding](/guides/get-started/key-terms#dense-vector). |
> | `sparse_values` | `STRUCT<indices: LIST<UINT_32>, values: LIST<FLOAT>>` | Optional. A list of floating-point values that make up the [sparse vector embedding](/guides/get-started/key-terms#sparse-vector). To omit from specific rows, use `NULL`. |
> | `metadata` | `STRING` | Optional. Additional [metadata](/guides/get-started/key-terms#metadata) for each record. To omit from specific rows, use `NULL`. |
>
> > [!NOTE]
> >
> > Additional columns in the Parquet file are silently ignored during import; only `id`, `values`, `sparse_values`, and `metadata` are processed.
>
> For example:
>
> ```parquet theme={null}
> id | values                   | sparse_values                                                                          | metadata
> --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
> 1  | [ 3.82  2.48 -4.15 ... ] | {"indices": [1082468256, 1009084850, 1221765879, ...], "values": [2.0, 3.0, 4.0, ...]} | {"year": 1984, "month": 6, "source": "source1", "title": "Example1", "text": "When ..."}
> 2  | [ 1.82  3.48 -2.15 ... ] | {"indices": [2225824123, 1293001993, 3201939490, ...], "values": [5.0, 2.0, 3.0, ...]} | {"year": 1990, "month": 4, "source": "source2", "title": "Example2", "text": "Who ..."}
> ```
