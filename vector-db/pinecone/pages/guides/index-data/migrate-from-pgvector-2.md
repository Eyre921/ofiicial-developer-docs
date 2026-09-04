---
title: "Migrate from pgvector"
source: https://docs.pinecone.io/guides/index-data/migrate-from-pgvector
path: guides/index-data/migrate-from-pgvector
---

Migrate vector data from pgvector to Pinecone Database, validate search results, synchronize incremental changes, and cut over application traffic.

This guide shows you how to migrate a vector-search workload from pgvector to Pinecone Database while keeping PostgreSQL available as the source of truth until cutover. It's based on the [pgvector-migration tool](https://github.com/pinecone-field/pgvector-migration), which provides a step-by-step migration manual, a runnable notebook, and a synchronization script that supports backfills, incremental synchronization, and reconciliation.

## Before you migrate

You need:

* A Pinecone account and [API key](https://app.pinecone.io/organizations/-/projects/-/keys).
* Network access to your PostgreSQL database.
* Python 3.9 or later.
* A PostgreSQL role that can read the tables you want to migrate.
* Write access to PostgreSQL if you use the synchronization script. The script creates bookkeeping tables or an outbox table and triggers, depending on the synchronization strategy.

Clone the migration repository and install its dependencies:

```bash Terminal theme={null}
git clone https://github.com/pinecone-field/pgvector-migration.git
cd pgvector-migration
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

<Note>
  The repository's `requirements.txt` installs the `pinecone`, `psycopg`, `pgvector`, and `pyarrow` packages used throughout this guide.
</Note>

Set the connection string, API key, and Pinecone index name as environment variables:

```bash Terminal theme={null}
export PG_CONN="postgresql://USER:PASSWORD@HOST:5432/DATABASE"
export PINECONE_API_KEY="YOUR_API_KEY"
export PINECONE_INDEX="pgvector-migration"
```

<Warning>
  Complete the workflow first in a test or staging environment using a disposable Pinecone index and representative source data. Delete the disposable index after validation. When you repeat the workflow in production, create a new, empty production index and don't stream pilot records into its target namespaces. Bulk import requires those namespaces not to exist.
</Warning>

<Tip>
  The [`migration_walkthrough.ipynb`](https://github.com/pinecone-field/pgvector-migration/blob/main/migration_walkthrough.ipynb) notebook runs every step in this guide against a local Dockerized pgvector database, so you can test the workflow before running it against your own data.
</Tip>

## 1. Inspect the pgvector data

For every table you want to migrate, identify the primary key, vector column, vector dimension, distance metric, metadata columns, and row count.

Find the vector columns and their dimensions:

```sql PostgreSQL theme={null}
SELECT c.relname AS table_name,
       a.attname AS column_name,
       format_type(a.atttypid, a.atttypmod) AS column_type
FROM pg_attribute a
JOIN pg_class c ON c.oid = a.attrelid
JOIN pg_type t ON t.oid = a.atttypid
WHERE t.typname = 'vector'
  AND a.attnum > 0
  AND NOT a.attisdropped
  AND c.relkind = 'r'
ORDER BY table_name;
```

Inspect each pgvector index to determine the distance metric:

```sql PostgreSQL theme={null}
SELECT indexname, indexdef
FROM pg_indexes
WHERE tablename = 'TABLE_NAME';
```

Map the pgvector operator class to the Pinecone metric:

| pgvector operator class | pgvector operator | Pinecone metric |
| ----------------------- | ----------------- | --------------- |
| `vector_cosine_ops`     | `<=>`             | `cosine`        |
| `vector_ip_ops`         | `<#>`             | `dotproduct`    |
| `vector_l2_ops`         | `<->`             | `euclidean`     |

If the table doesn't have a pgvector index, inspect the distance operator used by your application queries. The Pinecone index dimension and metric must match the source data.

Also record the source count for each table. You'll compare these counts with Pinecone after the backfill:

```sql PostgreSQL theme={null}
SELECT count(*) FROM TABLE_NAME;
```

## 2. Map access controls

If your tables use PostgreSQL row-level security (RLS), review every policy before choosing a Pinecone layout:

```sql PostgreSQL theme={null}
SELECT schemaname, tablename, policyname, cmd, qual
FROM pg_policies
WHERE schemaname = 'public'
ORDER BY tablename, policyname;
```

Pinecone doesn't evaluate PostgreSQL RLS policies. Use a namespace for a hard tenant boundary, or copy access-control attributes into record metadata and apply a server-side metadata filter to every search. Derive the namespace or filter values from the authenticated session, not from client input.

If a policy depends on joins, functions, or data outside the vector row, enforce the access decision in your application. When you denormalize permissions into metadata, synchronize permission changes as well as changes to the vector table.

## 3. Choose the index and namespace layout

By default, `sync.py` uses one Pinecone index and maps each PostgreSQL table to a namespace with the same name. The steps below use this layout. Tables can share an index only when their vectors have the same dimension and use the same distance metric.

| Source data                                         | Pinecone layout                                                                   |
| --------------------------------------------------- | --------------------------------------------------------------------------------- |
| One table, or several tables searched independently | One namespace per table in a shared index                                         |
| Several tables searched together                    | One shared namespace with a `source_table` metadata field                         |
| Tables with different dimensions or metrics         | One index per dimension and metric combination                                    |
| Tenant-isolated data                                | One namespace per tenant, with optional metadata filters for finer access control |

To use a shared namespace, tenant-based namespaces, or multiple indexes, update the namespace and index routing in `sync.py` before you run the migration.

Use a string for every record ID. The migration repository prefixes source IDs with the table name, such as `documents#4021`, to prevent collisions. Each Pinecone record contains the vector in `values` and selected source columns in `metadata`.

Metadata values must be strings, numbers, booleans, or lists of strings. Omit `NULL` values and convert PostgreSQL `numeric` values to floats. Don't name a source metadata field `metadata`; `metadata` is the top-level Parquet column that contains the JSON-encoded metadata object.

## 4. Create the Pinecone index

<Note>
  The examples below use two PostgreSQL tables, `documents` and `products`, with 768-dimensional vectors stored in an `embedding` column and queried using cosine distance. Replace all example table names, column names, dimensions, metrics, metadata fields, and namespaces with values from your workload.
</Note>

Create a new, empty production serverless index with the dimension and metric you identified from pgvector:

```python Python theme={null}
import os

from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(
    api_key=os.environ["PINECONE_API_KEY"],
    source_tag="pinecone_io:docs:pgvector_migration",
)

index_name = "pgvector-migration"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
```

Replace the example dimension, metric, cloud, and region with values appropriate for your workload. If separate source tables have different dimensions or metrics, create separate indexes.

## 5. Configure the source tables

In the cloned migration repository, edit the `TABLES` configuration near the top of [`sync.py`](https://github.com/pinecone-field/pgvector-migration/blob/main/sync.py) to match your PostgreSQL schema. Each entry defines the primary key, vector column, metadata columns, and optional change timestamp:

```python Python theme={null}
TABLES = {
    "documents": {
        "id": "id",
        "vector": "embedding",
        "metadata": ["title", "category"],
        "updated_at": "updated_at",
    },
    "products": {
        "id": "id",
        "vector": "embedding",
        "metadata": ["name", "price"],
        "updated_at": "updated_at",
    },
}
```

By default, `sync.py` maps each configured table to a namespace with the same name.

Run all `sync.py` commands below from the root of the cloned pgvector-migration repository.

## 6. Backfill the records

### Initialize change tracking

The following workflow uses the default change-log strategy. If the source stays writable during the backfill, initialize change tracking before copying records. This captures changes made during the backfill so you can apply them afterward:

```bash Terminal theme={null}
python sync.py init --strategy changelog
```

### Bulk import

For a production backfill, use [bulk import](/guides/index-data/import-data). Create an `export.py` file with the following code from the tool's migration workflow. It writes one import-ready Parquet file per table.

<Note>
  The export script reuses the PostgreSQL connection, `TABLES` configuration, and record-mapping helpers from `sync.py`. Configure `TABLES` in `sync.py` before running the export.
</Note>

```python Python theme={null}
import json
import os

import pyarrow as pa
import pyarrow.parquet as pq

from sync import TABLES, build_record, connect, select_cols


PARQUET_SCHEMA = pa.schema([
    ("id", pa.string()),
    ("values", pa.list_(pa.float32())),
    ("metadata", pa.string()),
])


def export_table_to_parquet(conn, table, config, output_path):
    ids, values, metadata = [], [], []
    with conn.transaction():
        with conn.cursor(name=f"stream_{table}") as cursor:
            cursor.execute(f"SELECT {select_cols(config)} FROM {table}")
            for row in cursor:
                record_id, vector, record_metadata = build_record(
                    table, row, config
                )
                ids.append(record_id)
                values.append(vector)
                metadata.append(json.dumps(record_metadata))

    arrow_table = pa.table(
        {"id": ids, "values": values, "metadata": metadata},
        schema=PARQUET_SCHEMA,
    )
    pq.write_table(arrow_table, output_path)
    print(f"Wrote {len(ids)} records to {output_path}")


conn = connect()
try:
    os.makedirs("export", exist_ok=True)
    for table, config in TABLES.items():
        os.makedirs(f"export/{table}", exist_ok=True)
        export_table_to_parquet(
            conn,
            table,
            config,
            f"export/{table}/0.parquet",
        )
finally:
    conn.close()
```

Run the export:

```bash Terminal theme={null}
python export.py
```

The script creates one directory per namespace and one Parquet file per table:

```console Output theme={null}
export/
├── documents/
│   └── 0.parquet
└── products/
    └── 0.parquet
```

If a table would produce a file larger than the maximum file size, split it into numbered files in the same namespace directory. Review the [import limits](/guides/index-data/import-data#import-limits) before exporting a large dataset.

Upload the generated directory tree to Amazon S3, Google Cloud Storage, or Azure Blob Storage. Then start an import using the import root URI:

```python Python theme={null}
from pinecone import ImportErrorMode

index = pc.Index(host="INDEX_HOST")

operation = index.start_import(
    uri="s3://BUCKET_NAME/IMPORT_ROOT",
    integration_id="STORAGE_INTEGRATION_ID",
    error_mode=ImportErrorMode.CONTINUE,
)

print(operation.id)
```

Use the import ID with the [`describe_import` operation](/guides/index-data/import-data#5-track-import-progress) to monitor progress. Each import takes at least 10 minutes. Wait until the import status is `Completed` before validating record counts in the next step.

The target namespaces must not already exist. A private bucket or container requires a [storage integration](/guides/operations/integrations/manage-storage-integrations).

### Streaming backfill

For a small dataset, you can instead use the streaming backfill in `sync.py`:

```bash Terminal theme={null}
python sync.py backfill
```

Streaming upsert requests are limited by both record count and request size. The script uses batches of 200 records to stay below the 2 MB request limit for its 768-dimensional example. Reduce the batch size for larger vectors or metadata.

### Apply captured changes

If you initialized change tracking, apply the changes captured while the backfill was running:

```bash Terminal theme={null}
python sync.py sync --strategy changelog
```

## 7. Validate the backfill

Compare the source row count for each table with the record count for its target namespace:

```python Python theme={null}
index = pc.Index(host="INDEX_HOST")
stats = index.describe_index_stats()

print(stats.total_vector_count)
for namespace, details in stats.namespaces.items():
    print(namespace, details.vector_count)
```

Index statistics are eventually consistent, so allow time for the counts to update.

Next, run a representative set of query vectors against pgvector and Pinecone. For example, the following code compares the top 10 results for a vector selected from the `documents` table:

```python Python theme={null}
import os

import psycopg
from pgvector.psycopg import register_vector
from pinecone import Pinecone

conn = psycopg.connect(os.environ["PG_CONN"])
register_vector(conn)

pc = Pinecone(
    api_key=os.environ["PINECONE_API_KEY"],
    source_tag="pinecone_io:docs:pgvector_migration",
)
index = pc.Index(host="INDEX_HOST")

query_vector = conn.execute(
    "SELECT embedding FROM documents WHERE embedding IS NOT NULL LIMIT 1"
).fetchone()[0]

pgvector_ids = [
    f"documents#{row[0]}"
    for row in conn.execute(
        "SELECT id FROM documents ORDER BY embedding <=> %s LIMIT %s",
        (query_vector, 10),
    ).fetchall()
]

pinecone_ids = [
    match.id
    for match in index.query(
        vector=query_vector.tolist(),
        top_k=10,
        namespace="documents",
    ).matches
]

print("pgvector:", pgvector_ids)
print("Pinecone:", pinecone_ids)
```

Replace the table, columns, namespace, and pgvector operator with values for your workload. Use `<=>` for cosine distance, `<#>` for inner product, or `<->` for Euclidean distance.

Compare the returned record IDs and ordering. Small ordering differences for near-ties are expected with approximate search. Large differences can indicate a mismatched metric or inconsistent vector normalization.

## 8. Keep Pinecone synchronized

After the initial copy, synchronize inserts, updates, and deletes until cutover. The repository's `sync.py` supports two strategies:

| Strategy   | Use when                                                                 | Behavior                                                                                            |
| ---------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| Change-log | Updates and deletes must be captured reliably.                           | Creates an outbox table and per-table triggers, then applies the latest operation for each record.  |
| Watermark  | The workload is mostly inserts and has a maintained `updated_at` column. | Tracks migrated IDs and the last synchronization timestamp. Deletes are detected with an anti-join. |

The change-log strategy is the default. Run the synchronization command on a schedule until cutover:

```bash Terminal theme={null}
python sync.py sync --strategy changelog
```

The PostgreSQL role used by the script must be able to create the outbox table, functions, and triggers, and update the outbox table.

For workloads that are mostly inserts and have a maintained `updated_at` column, the tool also supports a watermark strategy. This strategy uses its first synchronization run to backfill records. For setup, limitations, and commands, see the [watermark strategy in the pgvector-migration tool](https://github.com/pinecone-field/pgvector-migration#strategy-a--watermark--anti-join-in-postgres-simplest).

Periodically reconcile all record IDs, and run reconciliation immediately before cutover:

```bash Terminal theme={null}
python sync.py reconcile
```

Reconciliation upserts records missing from Pinecone and deletes records that no longer exist in pgvector.

## 9. Cut over application traffic

Keep pgvector serving traffic and continue synchronization while you cut over:

1. Shadow a sample of production searches to Pinecone without returning those results to users. Compare search quality and latency.
2. Route a small percentage of reads to Pinecone and monitor results.
3. Increase the percentage after validation.
4. Immediately before switching the primary read path, run `sync` with your selected strategy, run `python sync.py reconcile`, and then run `sync` again to apply changes captured during reconciliation.
5. Run `sync` once more and confirm that it reports no outstanding changes. Then make Pinecone the primary read path.
6. Keep pgvector available as a rollback target until the new read path is stable. You can point reads back to pgvector as it never stopped serving and is still authoritative.

For implementation details, troubleshooting, and the complete runnable workflow, see the [pgvector-migration tool](https://github.com/pinecone-field/pgvector-migration).
