---
title: "Import records"
source: https://docs.pinecone.io/guides/index-data/import-data
path: guides/index-data/import-data
---

Import large datasets efficiently from Amazon S3, Google Cloud Storage, or Azure Blob Storage into Pinecone serverless indexes using object storage.

Importing from object storage is the most efficient and cost-effective way to load large numbers of records into an index.

To run through this guide in your browser, see the [Bulk import colab notebook](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/pinecone-import.ipynb).

<Note>
  This feature is available on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

## Before you import

Before you can import records, ensure you have a serverless index, a storage integration, and data uploaded to an Amazon S3 bucket, Google Cloud Storage bucket, or Azure Blob Storage container.

Your uploaded data must be in the file format required for your index type: Parquet for vector indexes, or [JSON Lines](https://jsonlines.org/) (JSONL) for indexes with a document schema. If your source data isn't already in that format, prepare it in that format before uploading.

## 1. Create an index

[Create a serverless index](/guides/index-data/create-an-index) for your data.

Be sure to create your index on a cloud that supports importing from the object storage you want to use:

|                                       | …to an **AWS** index | …to a **GCP** index | …to an **Azure** index |
| ------------------------------------- | :------------------: | :-----------------: | :--------------------: |
| Import from **AWS S3**…               |           ✅          |          ❌          |            ❌           |
| Import from **Google Cloud Storage**… |           ✅          |          ✅          |            ✅           |
| Import from **Azure Blob Storage**…   |           ✅          |          ✅          |            ✅           |

## 2. Add a storage integration

To import records from a public data source, a storage integration isn't required. However, to import records from a secure data source, you must create an integration to allow Pinecone access to data in your object storage. See the following guides:

* [Integrate with Amazon S3](/guides/operations/integrations/integrate-with-amazon-s3)
* [Integrate with Google Cloud Storage](/guides/operations/integrations/integrate-with-google-cloud-storage)
* [Integrate with Azure Blob Storage](/guides/operations/integrations/integrate-with-azure-blob-storage)

## 3. Prepare your data

<Steps>
  <Step title="Create a directory for each namespace">
    In your Amazon S3 bucket, Google Cloud Storage bucket, or Azure Blob Storage container, create an import directory containing a subdirectory for each namespace you want to import into. The namespaces must not yet exist in your index.

    For example, to import data into the namespaces `example_namespace1` and `example_namespace2`, your directory structure would look like this:

    ```
    <BUCKET_OR_CONTAINER_NAME>/
    --/<IMPORT_DIR>/
    ----/example_namespace1/
    ----/example_namespace2/
    ```

    <Tip>
      To import into the default namespace, use a subdirectory called `__default__`. The default namespace must be empty.
    </Tip>
  </Step>

  <Step title="Create a data file for each namespace">
    For each namespace, create one or more files defining the data to import. The file format and required fields depend on the index type:

    <Tabs>
      <Tab title="Document schema">
        To import into a namespace in an [index with a document schema](/guides/index-data/data-modeling#documents), use JSONL (`.jsonl`, or gzip-compressed `.jsonl.gz`) files instead of Parquet. Each line is one [document](/guides/get-started/concepts#document), identical in shape to a document you would pass to [`documents.upsert`](/guides/search/full-text-search#data-plane-operations):

        | Field             | JSON type                                      | Description                                                                                                                                                                                                                                                                                                  |
        | ----------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
        | `_id`             | `string`                                       | Required. Unique identifier for each document within the namespace.                                                                                                                                                                                                                                          |
        | Each schema field | Depends on the field's type                    | Encode each schema-declared field by its type: a full-text `string` field as a JSON string; a `dense_vector` field as an array of floats matching the schema's `dimension`; a `sparse_vector` field as `{"indices": [...], "values": [...]}`. A declared `dense_vector` field must appear in every document. |
        | Any other field   | `string`, number, boolean, or array of strings | Optional. Stored and auto-indexed as filterable [metadata](/guides/get-started/concepts#metadata). Field names can't start with `_` or `$`.                                                                                                                                                                  |

        <Note>
          Unlike Parquet imports, fields not declared in the schema aren't ignored: they are stored and auto-indexed as filterable metadata.
        </Note>

        For example, for a schema with a full-text `body` field and a `dense_vector` `embedding` field:

        ```jsonl theme={null}
        {"_id": "doc1", "body": "Machine learning models are revolutionizing natural language processing", "embedding": [0.12, 0.34, 0.56], "category": "technology", "year": 2024}
        {"_id": "doc2", "body": "Vector databases enable fast similarity search across embeddings", "embedding": [0.91, 0.05, 0.44], "category": "technology", "year": 2023}
        ```

        For the full file format, per-field encoding, and directory layout, see [Bulk import](/guides/search/full-text-search#bulk-import).
      </Tab>

      <Tab title="Dense vectors">
        To import into a namespace in an [index of dense vectors](/guides/index-data/indexing-overview#indexes-with-dense-vectors), the Parquet file must contain the following columns:

        | Column name | Parquet type  | Description                                                                                                                     |
        | ----------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------- |
        | `id`        | `STRING`      | Required. The unique [identifier for each record](/guides/get-started/concepts#record-id).                                      |
        | `values`    | `LIST<FLOAT>` | Required. A list of floating-point values that make up the [dense vector embedding](/guides/get-started/concepts#dense-vector). |
        | `metadata`  | `STRING`      | Optional. Additional [metadata](/guides/get-started/concepts#metadata) for each record. To omit from specific rows, use `NULL`. |

        <Note>
          Additional columns in the Parquet file are silently ignored during import; only `id`, `values`, and `metadata` are processed.
        </Note>

        For example:

        ```parquet theme={null}
        id | values                   | metadata
        --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        1  | [ 3.82  2.48 -4.15 ... ] | {"year": 1984, "month": 6, "source": "source1", "title": "Example1", "text": "When ..."}
        2  | [ 1.82  3.48 -2.15 ... ] | {"year": 1990, "month": 4, "source": "source2", "title": "Example2", "text": "Who ..."}
        ```
      </Tab>

      <Tab title="Sparse vectors">
        To import into a namespace in an [index of sparse vectors](/guides/index-data/indexing-overview#indexes-with-sparse-vectors), the Parquet file must contain the following columns:

        | Column name     | Parquet type                                          | Description                                                                                                                                                                                     |
        | --------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | `id`            | `STRING`                                              | Required. The unique [identifier for each record](/guides/get-started/concepts#record-id).                                                                                                      |
        | `sparse_values` | `STRUCT<indices: LIST<UINT_32>, values: LIST<FLOAT>>` | Required. A list of floating-point values (sparse values) and a list of integer values (sparse indices) that make up the [sparse vector embedding](/guides/get-started/concepts#sparse-vector). |
        | `metadata`      | `STRING`                                              | Optional. Additional [metadata](/guides/get-started/concepts#metadata) for each record. To omit from specific rows, use `NULL`.                                                                 |

        <Note>
          Additional columns in the Parquet file are silently ignored during import; only `id`, `sparse_values`, and `metadata` are processed.
        </Note>

        For example:

        ```parquet theme={null}
        id | sparse_values                                                                                       | metadata
        --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        1  | {"indices": [ 822745112 1009084850 1221765879 ... ], "values": [1.7958984 0.41577148 2.828125 ...]} | {"year": 1984, "month": 6, "source": "source1", "title": "Example1", "text": "When ..."}
        2  | {"indices": [ 504939989 1293001993 3201939490 ... ], "values": [1.4383747 0.72849722 1.384775 ...]} | {"year": 1990, "month": 4, "source": "source2", "title": "Example2", "text": "Who ..."}
        ```
      </Tab>

      <Tab title="Dense + sparse">
        To import into a namespace in an [index with both dense and sparse vectors](/guides/search/hybrid-search#use-a-single-index-for-dense-and-sparse-vectors), the Parquet file must contain the following columns:

        | Column name     | Parquet type                                          | Description                                                                                                                                                               |
        | --------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | `id`            | `STRING`                                              | Required. The unique [identifier for each record](/guides/get-started/concepts#record-id).                                                                                |
        | `values`        | `LIST<FLOAT>`                                         | Required. A list of floating-point values that make up the [dense vector embedding](/guides/get-started/concepts#dense-vector).                                           |
        | `sparse_values` | `STRUCT<indices: LIST<UINT_32>, values: LIST<FLOAT>>` | Optional. A list of floating-point values that make up the [sparse vector embedding](/guides/get-started/concepts#sparse-vector). To omit from specific rows, use `NULL`. |
        | `metadata`      | `STRING`                                              | Optional. Additional [metadata](/guides/get-started/concepts#metadata) for each record. To omit from specific rows, use `NULL`.                                           |

        <Note>
          Additional columns in the Parquet file are silently ignored during import; only `id`, `values`, `sparse_values`, and `metadata` are processed.
        </Note>

        For example:

        ```parquet theme={null}
        id | values                   | sparse_values                                                                          | metadata
        --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        1  | [ 3.82  2.48 -4.15 ... ] | {"indices": [1082468256, 1009084850, 1221765879, ...], "values": [2.0, 3.0, 4.0, ...]} | {"year": 1984, "month": 6, "source": "source1", "title": "Example1", "text": "When ..."}
        2  | [ 1.82  3.48 -2.15 ... ] | {"indices": [2225824123, 1293001993, 3201939490, ...], "values": [5.0, 2.0, 3.0, ...]} | {"year": 1990, "month": 4, "source": "source2", "title": "Example2", "text": "Who ..."}
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Upload the files">
    Upload the files into the relevant subdirectory.

    For example, if you have subdirectories for the namespaces `example_namespace1` and `example_namespace2` and upload 4 files into each, your directory structure would look as follows after the upload. Files use the `.parquet` extension for vector indexes, or `.jsonl` / `.jsonl.gz` for document-schema indexes:

    ```
    <BUCKET_OR_CONTAINER_NAME>/
    --/<IMPORT_DIR>/
    ----/example_namespace1/
    ------0.<EXT>
    ------1.<EXT>
    ------2.<EXT>
    ------3.<EXT>
    ----/example_namespace2/
    ------4.<EXT>
    ------5.<EXT>
    ------6.<EXT>
    ------7.<EXT>
    ```
  </Step>
</Steps>

## 4. Import records into an index

<Warning>
  Review [import limits](#import-limits) before starting an import.
</Warning>

<Note>
  The examples below use Parquet files, for indexes **without** a schema definition. Indexes with document schemas import [JSONL files](/guides/search/full-text-search#bulk-import) instead. Semantic-text (auto-embedded) fields aren't yet supported in document schemas.
</Note>

Use the [`start_import`](/reference/api/latest/data-plane/start_import) operation to start an asynchronous import of vectors from object storage into an index.

* For `uri`, specify the URI of the bucket and import directory containing the namespaces and Parquet files you want to import. For example:

  * Amazon S3: `s3://BUCKET_NAME/IMPORT_DIR`
  * Google Cloud Storage: `gs://BUCKET_NAME/IMPORT_DIR`
  * Azure Blob Storage: `https://STORAGE_ACCOUNT.blob.core.windows.net/CONTAINER_NAME/IMPORT_DIR`

* For `integration_id`, specify the Integration ID of the Amazon S3, Google Cloud Storage, or Azure Blob Storage integration you created. The ID is found on the [Storage integrations](https://app.pinecone.io/organizations/-/projects/-/storage) page of the Pinecone console.

  <Note>
    An Integration ID isn't needed to import from a public bucket.
  </Note>

* For `error_mode`, use `continue` or `abort`.

  * With `abort`, the operation stops if any records fail to import.
  * With `continue`, the operation continues on error, but there isn't any notification about which records, if any, failed to import. To see how many records were successfully imported, use the [describe an import](#describe-an-import) operation.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone, ImportErrorMode

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")
  root = "s3://example_bucket/import"

  index.start_import(
      uri=root,
      integration_id="a12b3d4c-47d2-492c-a97a-dd98c8dbefde", # Optional for public buckets
      error_mode=ImportErrorMode.CONTINUE # or ImportErrorMode.ABORT
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const storageURI = 's3://example_bucket/import';
  const errorMode = 'continue'; // or 'abort'
  const integrationID = 'a12b3d4c-47d2-492c-a97a-dd98c8dbefde'; // Optional for public buckets

  await index.startImport(storageURI, errorMode, integrationID); 
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import io.pinecone.clients.AsyncIndex;
  import org.openapitools.db_data.client.ApiException;
  import org.openapitools.db_data.client.model.ImportErrorMode;
  import org.openapitools.db_data.client.model.StartImportResponse;

  public class StartImport {
      public static void main(String[] args) throws ApiException {
          // Initialize a Pinecone client with your API key
          Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

          // Get async imports connection object
          AsyncIndex asyncIndex = pinecone.getAsyncIndexConnection("docs-example");

          // s3 uri
          String uri = "s3://example_bucket/import";

          // Integration ID (optional for public buckets)
          String integrationId = "a12b3d4c-47d2-492c-a97a-dd98c8dbefde";

          // Start an import
          StartImportResponse response = asyncIndex.startImport(uri, integrationId, ImportErrorMode.OnErrorEnum.CONTINUE);
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
  	}

      uri := "s3://example_bucket/import"
      errorMode := "continue" // or "abort"
      importRes, err := idxConnection.StartImport(ctx, uri, nil, (*pinecone.ImportErrorMode)(&errorMode))
      if err != nil {
          log.Fatalf("Failed to start import: %v", err)
      }
      fmt.Printf("Import started with ID: %s", importRes.Id)
  }
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/bulk/imports" \
    -H 'Api-Key: $YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    -H 'X-Pinecone-Api-Version: 2025-10' \
    -d '{
          "integrationId": "a12b3d4c-47d2-492c-a97a-dd98c8dbefde",
          "uri": "s3://example_bucket/import",
          "errorMode": {
              "onError": "continue"
              }
          }'
  ```
</CodeGroup>

The response contains an `id` that you can use to [check the status of the import](#list-imports):

```json Response theme={null}
{
   "id": "101"
}
```

Once all the data is loaded, the [index builder](/guides/get-started/database-architecture#index-builder) indexes the records, which usually takes at least 10 minutes. During this indexing process, the expected job status is `InProgress`, but `100.0` percent complete. Once all the imported records are indexed and fully available for querying, the import operation is set to `Completed`. If you cancel the import before it finishes, the status changes to `Cancelled`.

<Tip>
  You can start a new import using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes). Find the index you want to import into, and click the **ellipsis (...) menu > Import data**.
</Tip>

## 5. Track import progress

The amount of time required for an import depends on various factors, including:

* The number of records to import
* The number of namespaces to import, and the number of records in each
* The total size (in bytes) of the import

To track an import's progress, check its status bar in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/import) or use the [`describe_import`](/reference/api/latest/data-plane/describe_import) operation with the import ID:

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.describe_import(id="101")
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });


  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const results = await index.describeImport(id='101');
  console.log(results);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import io.pinecone.clients.AsyncIndex;
  import org.openapitools.db_data.client.ApiException;
  import org.openapitools.db_data.client.model.ImportModel;

  public class DescribeImport {
      public static void main(String[] args) throws ApiException {
          // Initialize a Pinecone client with your API key
          Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

          // Get async imports connection object
          AsyncIndex asyncIndex = pinecone.getAsyncIndexConnection("docs-example");

          // Describe import
          ImportModel importDetails = asyncIndex.describeImport("101");

          System.out.println(importDetails);
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      importID := "101"

      importDesc, err := idxConnection.DescribeImport(ctx, importID)
      if err != nil {
          log.Fatalf("Failed to describe import: %s - %v", importID, err)
      }
      fmt.Printf("Import ID: %s, Status: %s", importDesc.Id, importDesc.Status)
  }
  ```

  ```bash curl theme={null}
  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://{INDEX_HOST}/bulk/imports/101" \
    -H 'Api-Key: $YOUR_API_KEY' \
    -H 'X-Pinecone-Api-Version: 2025-10'
  ```
</CodeGroup>

The response contains the import details, including the import `status`, `percent_complete`, and `records_imported`:

```json Response theme={null}
{
  "id": "101",
  "uri": "s3://example_bucket/import",
  "status": "InProgress",
  "created_at": "2024-08-19T20:49:00.754Z",
  "finished_at": "2024-08-19T20:49:00.754Z",
  "percent_complete": 42.2,
  "records_imported": 1000000
}
```

If the import fails, the response contains an `error` field with the reason for the failure. See the [Troubleshooting](#troubleshooting) section for more information.

```json Response theme={null}
{
  "id": "102",
  "uri": "s3://example_bucket/import",
  "status": "Failed",
  "percent_complete": 0.0,
  "records_imported": 0,
  "created_at": "2025-08-21T11:29:47.886797+00:00",
  "error": "User error: The namespace \"namespace1\" already exists. Imports are only allowed into nonexistent namespaces.",
  "finished_at": "2025-08-21T11:30:05.506423+00:00"
}
```

## Manage imports

### List imports

Use the [`list_imports`](/reference/api/latest/data-plane/list_imports) operation to list all of the recent and ongoing imports. By default, the operation returns up to 100 imports per page. If the `limit` parameter is passed, the operation returns up to that number of imports per page instead. For example, if `limit=3`, up to 3 imports are returned per page. Whenever there are additional imports to return, the response includes a `pagination_token` for fetching the next page of imports.

<Tabs>
  <Tab title="Python SDK">
    When using the Python SDK, `list_import` paginates automatically.

    ```python Python theme={null}
    from pinecone import Pinecone, ImportErrorMode

    pc = Pinecone(api_key="YOUR_API_KEY")

    # To get the unique host for an index, 
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    index = pc.Index(host="INDEX_HOST")

    # List using a generator that handles pagination
    for i in index.list_imports():
        print(f"id: {i.id} status: {i.status}")

    # List using a generator that fetches all results at once
    operations = list(index.list_imports())
    print(operations)
    ```

    ```json Response theme={null}
    {
      "data": [
        {
          "id": "1",
          "uri": "s3://BUCKET_NAME/PATH/TO/DIR",
          "status": "Pending",
          "started_at": "2024-08-19T20:49:00.754Z",
          "finished_at": "2024-08-19T20:49:00.754Z",
          "percent_complete": 42.2,
          "records_imported": 1000000
        }
      ],
      "pagination": {
        "next": "Tm90aGluZyB0byBzZWUgaGVyZQo="
      }
    }
    ```

    <Tip>
      You can view the list of imports for an index in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes/). Select the index and navigate to the **Imports** tab.
    </Tip>
  </Tab>

  <Tab title="Other SDKs">
    When using the Node.js SDK, Java SDK, Go SDK, or REST API to list recent and ongoing imports, you must manually fetch each page of results. To view the next page of results, include the `paginationToken` provided in the response.

    <CodeGroup>
      ```javascript JavaScript theme={null}
      import { Pinecone } from '@pinecone-database/pinecone';

      const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      const index = pc.index("INDEX_NAME", "INDEX_HOST")

      const results = await index.listImports({ limit: 10, paginationToken: 'Tm90aGluZyB0byBzZWUgaGVyZQo' });
      console.log(results);
      ```

      ```java Java theme={null}
      import io.pinecone.clients.Pinecone;
      import io.pinecone.clients.AsyncIndex;
      import org.openapitools.db_data.client.ApiException;
      import org.openapitools.db_data.client.model.ListImportsResponse;

      public class ListImports {
          public static void main(String[] args) throws ApiException {
              // Initialize a Pinecone client with your API key
              Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

              // Get async imports connection object
              AsyncIndex asyncIndex = pinecone.getAsyncIndexConnection("docs-example");

              // List imports
              ListImportsResponse response = asyncIndex.listImports(10, "Tm90aGluZyB0byBzZWUgaGVyZQo");

              System.out.println(response);
          }
      }
      ```

      ```go Go theme={null}
      package main

      import (
          "context"
          "fmt"
          "log"

          "github.com/pinecone-io/go-pinecone/v4/pinecone"
      )

      func main() {
          ctx := context.Background()

          pc, err := pinecone.NewClient(pinecone.NewClientParams{
              ApiKey: "YOUR_API_KEY",
          })
          if err != nil {
              log.Fatalf("Failed to create Client: %v", err)
          }

          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
          if err != nil {
              log.Fatalf("Failed to create IndexConnection for Host: %v", err)
        	}

          limit := int32(10)
          firstImportPage, err := idxConnection.ListImports(ctx, &limit, nil)
          if err != nil {
              log.Fatalf("Failed to list imports: %v", err)
          }
          fmt.Printf("First page of imports: %+v", firstImportPage.Imports)

          paginationToken := firstImportPage.NextPaginationToken
          nextImportPage, err := idxConnection.ListImports(ctx, &limit, paginationToken)
          if err != nil {
              log.Fatalf("Failed to list imports: %v", err)
          }
          fmt.Printf("Second page of imports: %+v", nextImportPage.Imports)
      }
      ```

      ```bash curl theme={null}
      # To get the unique host for an index,
      # see https://docs.pinecone.io/guides/manage-data/target-an-index
      PINECONE_API_KEY="YOUR_API_KEY"
      INDEX_HOST="INDEX_HOST"

      curl -X GET "https://$INDEX_HOST/bulk/imports?paginationToken==Tm90aGluZyB0byBzZWUgaGVyZQo" \
        -H 'Api-Key: $YOUR_API_KEY' \
        -H 'X-Pinecone-Api-Version: 2025-10'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Cancel an import

The [`cancel_import`](/reference/api/latest/data-plane/cancel_import) operation cancels an import if it isn't yet finished. It has no effect if the import is already complete.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.cancel_import(id="101")
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  await index.cancelImport(id='101');
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import io.pinecone.clients.AsyncIndex;
  import org.openapitools.db_data.client.ApiException;

  public class CancelImport {
      public static void main(String[] args) throws ApiException {
          // Initialize a Pinecone client with your API key
          Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

          // Get async imports connection object
          AsyncIndex asyncIndex = pinecone.getAsyncIndexConnection("docs-example");

          // Cancel import
          asyncIndex.cancelImport("2");
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      importID := "101"

      err = idxConnection.CancelImport(ctx, importID)
      if err != nil {
          log.Fatalf("Failed to cancel import: %s", importID)
      }

      importDesc, err := idxConnection.DescribeImport(ctx, importID)
      if err != nil {
          log.Fatalf("Failed to describe import: %s - %v", importID, err)
      }
  }
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X DELETE "https://{INDEX_HOST}/bulk/imports/101" \
    -H 'Api-Key: $YOUR_API_KEY' \
    -H "X-Pinecone-Api-Version: 2025-10"
  ```
</CodeGroup>

```json Response theme={null}
{}
```

<Tip>
  You can cancel your import using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/import). To cancel an ongoing import, select the index you are importing into and navigate to the **Imports** tab. Then, click the **ellipsis (...) menu > Cancel**.
</Tip>

## Import limits

<Note>
  If your import exceeds these limits, you'll get an error specifying the limit exceeded. See [Troubleshooting](/guides/index-data/import-data#troubleshooting) for details.
</Note>

| Metric                                        | Limit     |
| :-------------------------------------------- | :-------- |
| Max namespaces per import                     | 10,000    |
| Max total input data size (on-demand indexes) | 1 TB      |
| Max total input data size (DRN indexes)       | Unlimited |
| Max files per import                          | 100,000   |
| Max size per file                             | 10 GB     |

The total input data size limit does not apply to indexes with [dedicated read nodes](/guides/index-data/dedicated-read-nodes).

Bulk import supports indexes without a schema definition (Parquet files) and indexes with document schemas ([JSONL files](/guides/search/full-text-search#bulk-import)). Semantic-text (auto-embedded) fields are not yet supported in document schemas.

Also:

* You can't import data from an AWS S3 bucket into a Pinecone index hosted on GCP or Azure.
* You can't import data from S3 Express One Zone storage.
* You can't import data into an existing namespace.
* When importing data into the `__default__` namespace of an index, the default namespace must be empty.
* Each import takes at least 10 minutes to complete.
* When importing into an [index with integrated embedding](/guides/index-data/indexing-overview#vector-embedding), records must contain vectors, not text. To add records with text, you must use [upsert](/guides/index-data/upsert-data).

## Troubleshooting

When an import fails, you'll see an error message with the reason for the failure in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/import) or in the response to the [describe an import](/reference/api/latest/data-plane/describe_import) operation.

<AccordionGroup>
  <Accordion title="Namespace already exists">
    You can't import data into an existing namespace. If your import directory structure contains a folder with the name of an existing namespace in your index, the import will fail with the following error:

    ```
    User error: The namespace "example-namespace" already exists. Imports are only allowed into nonexistent namespaces.
    ```

    To fix this, rename the folder to use a namespace name that doesn't yet exist.
  </Accordion>

  <Accordion title="No namespace found">
    In object storage, your directory structure must be as follows:

    ```
    example_bucket/
    --/imports/
    ----/example_namespace1/
    ------0.parquet
    ------1.parquet
    ------2.parquet
    ------3.parquet
    ----/example_namespace2/
    ------4.parquet
    ------5.parquet
    ------6.parquet
    ------7.parquet
    ```

    If a Parquet file isn't nested under a namespace subdirectory, the import will fail with the following error:

    ```
    User error: "test-import/0.parquet": No namespace detected. Each file should be nested under a subdirectory of the URI prefix. This indicates which namespace it should be imported into.
    ```

    To fix this, move the Parquet file to a namespace subdirectory.
  </Accordion>

  <Accordion title="Parquet files not found">
    Each namespace subdirectory must contain Parquet files with data to import. If a namespace subdirectory doesn't include Parquet files, the import will fail with the following error:

    ```
    User error: No Parquet files found under "gs://example_bucket/imports". Files must be stored with the specified bucket prefix.
    ```

    To fix this, add Parquet files to the namespace subdirectory.
  </Accordion>

  <Accordion title="Namespace not created (empty subdirectory)">
    For document-schema (JSONL) imports, an empty namespace subdirectory behaves differently than for Parquet. A namespace subdirectory that contains no `.jsonl` or `.jsonl.gz` files is silently skipped: the import doesn't create that namespace and doesn't raise an error for it. If a namespace is missing after an import that otherwise succeeded, confirm its subdirectory actually contains importable files.

    If no importable files are found anywhere under the dataset prefix, the import fails with the same `No Parquet files found` error shown above, which says "Parquet files" even for JSONL imports.
  </Accordion>

  <Accordion title="Invalid import URI">
    In your [start import](/reference/api/latest/data-plane/start_import) request, the import `uri` must specify only the bucket and import directory containing the namespaces and Parquet files you want to import. If the `uri` also contains a namespaces directory or a Parquet filename, the import will fail with the following error:

    ```
    User error: "test-import/0.parquet": It looks like you specified a complete path to a parquet file as the URI prefix to import from. Note that the URI prefix should give an ancestor directory with subdirectories to specify each namespace to import into. See https://docs.pinecone.io/guides/data/understanding-imports#directory-structure.
    ```

    To fix this, remove the namespaces directory or Parquet filename from the `uri`.
  </Accordion>

  <Accordion title="Invalid Parquet files">
    When a Parquet file isn't formatted correctly, the import will fail with a message like one of the following:

    ```shell File schema errors theme={null}
    Missing required column "{0}"
    Unsupported column "{0}"
    ```

    ```shell File corruption errors theme={null}
    Parquet footer could not be parsed. Are you sure this is valid parquet?
    ```

    ```shell Type errors theme={null}
    The expected data type for column "{column}" is "{expected}", but got "{given}"
    The expected data type for metadata is a JSON encoded string in UTF-8 format, but got "{given}"
    ```

    These errors are returned for both `continue` and `abort` error modes.

    To fix these errors, check the specific error message and follow the instructions in the [Prepare your data](#3-prepare-your-data) section.
  </Accordion>

  <Accordion title="Invalid JSONL files or documents">
    For document-schema indexes, import files are JSONL: each line is one JSON document, validated against the index's [schema](/guides/search/full-text-search#file-format). A line fails if it isn't valid JSON, or if the document doesn't conform to the schema. Each per-document error identifies the file name, row number, and document `_id`:

    ```
    error reading record (file "0.jsonl", row 2, id "doc1"): {reason}
    ```

    Common reasons include:

    ```shell Malformed JSON theme={null}
    invalid JSON document: {details}
    ```

    ```shell Empty _id theme={null}
    Vector ID must not be empty
    ```

    ```shell Dense-vector dimension mismatch theme={null}
    Vector dimension {actual} does not match the dimension of the index {expected}
    ```

    ```shell Reserved field name theme={null}
    Document with id '{id}': Field name '{name}' cannot start with '_' (reserved for internal use)
    ```

    ```shell Wrong field type theme={null}
    Document with id '{id}': full text search field '{field}' must be a string
    ```

    A document that omits `_id` entirely fails JSON parsing and appears as a malformed-JSON error (`missing field _id`).

    With `errorMode.onError` set to `continue` (the default), invalid documents are skipped and the rest import; with `abort`, the import stops on the first invalid document. If every document in a namespace is skipped, the import fails with `No vectors added, all rows were skipped for namespace: {namespace}`.

    To fix these errors, validate your documents against the [file-format rules](/guides/search/full-text-search#file-format) before importing.
  </Accordion>

  <Accordion title="Invalid records">
    When the `error_mode` is `abort` and a file contains invalid records, the import will stop processing on the first invalid record and return an error message identifying the file name and row:

    ```
    User error: error reading record (file "/0.parquet", row 0):
    ```

    This will be followed by an error message identifying the specific issue. For example:

    ```shell Missing values theme={null}
    missing required values in column "{column}"
    ```

    ```shell Invalid metadata  theme={null}
    Failed to parse metadata: {msg}
    ```

    ```shell Invalid vectors theme={null}
    Upserting dense vectors is not supported for indexes that store only sparse vectors
    ```

    When the `error_mode` is `continue`, the import will skip individual invalid records. However, if all records are invalid and skipped (for example, the vector type in the file doesn't match the vector type of the index), the import will fail with a general message:

    ```
    User error: No vectors added, all rows were skipped for namespace: example-namespace
    ```

    To fix these errors, check the specific error message and follow the instructions in the [Prepare your data](#3-prepare-your-data) section.
  </Accordion>

  <Accordion title="Duplicate records">
    When your import contains duplicate vectors (records with identical vector values), the duplicates are marked as skipped and not imported. Only one occurrence of each unique vector is added to the index.

    This applies to both `continue` and `abort` error modes:

    * With `abort`: The import fails when it encounters a duplicate vector within the import.
    * With `continue`: The import proceeds, skipping duplicate records silently.

    **Example scenario:**
    If your Parquet file contains:

    ```parquet theme={null}
    id | values
    ---|---------
    1  | [0.1, 0.2, 0.3]
    2  | [0.1, 0.2, 0.3]  ← Duplicate of record 1, will be skipped
    3  | [0.4, 0.5, 0.6]
    ```

    Only records 1 and 3 will be imported.

    To prevent this from happening, deduplicate your source data before creating Parquet files by removing records with identical vector values.
  </Accordion>

  <Accordion title="Import exceeds maximum data size for on-demand">
    On-demand indexes have a maximum total input data size of 1 TB per import. If your import exceeds this limit, it will fail with the following error:

    ```
    Import ({size} GB) exceeds the maximum input data size of 1000 GB for on-demand. Consider using Dedicated Read Nodes (DRN) for larger index sizes, or contact support for your use-case.
    ```

    To fix this, either reduce the total size of your import to under 1 TB, use an index with [dedicated read nodes](/guides/index-data/dedicated-read-nodes) (which have no total data size limit for imports), or [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket).

    For `.jsonl.gz` files, size is measured as an estimated uncompressed size of 10× the compressed file, so gzip-compressed files count roughly 10× their on-disk size against this limit.
  </Accordion>
</AccordionGroup>

## See also

* [Integrate with Amazon S3](/guides/operations/integrations/integrate-with-amazon-s3)
* [Integrate with Google Cloud Storage](/guides/operations/integrations/integrate-with-google-cloud-storage)
* [Integrate with Azure Blob Storage](/guides/operations/integrations/integrate-with-azure-blob-storage)
* [Pinecone's pricing](https://www.pinecone.io/pricing/)
