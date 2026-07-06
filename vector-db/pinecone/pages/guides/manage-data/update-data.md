---
title: "Update records"
source: https://docs.pinecone.io/guides/manage-data/update-data
path: guides/manage-data/update-data
---

Update vectors and metadata for existing records

You can [update](/reference/api/latest/data-plane/update) a single record using the record ID or multiple records using a metadata filter.

* **Update by ID**: Update a single record's metadata (add or change fields) or vector values.
* **Update by metadata**: Update metadata (add or change fields) across multiple records using a metadata filter. Vector values cannot be updated.

To update entire records, use the [upsert](/guides/index-data/upsert-data) operation instead.

<Tip>
  Updates consume [write units (WUs)](/guides/manage-cost/understanding-cost#write-units). See [Understanding cost](/guides/manage-cost/understanding-cost#update) for how update cost is calculated.
</Tip>

## Update by ID

To update the vector and/or metadata of a single record, use the [`update`](/reference/api/latest/data-plane/update) operation with the following parameters:

* `namespace`: The [namespace](/guides/index-data/indexing-overview#namespaces) containing the record to update. To use the default namespace, set the namespace to `"__default__"`.
* `id`: The ID of the record to update.
* One or both of the following:
  * Updated values for the vector. Specify one of the following:
    * `values`: For dense vectors. Must have the same length as the existing vector.
    * `sparse_values`: For sparse vectors.
  * `setMetadata`: The metadata to add or change. When updating metadata, only the specified metadata fields are modified, and if a specified metadata field does not exist, it is added.

<Warning>
  If a non-existent record ID is specified, no records are affected and a `200 OK` status is returned.
</Warning>

In this example, assume you are updating the dense vector values and one metadata value of the following record in the `example-namespace` namespace:

```
(
    namespace="example-namespace",
    id="id-3", 
    values=[4.0, 2.0], 
    setMetadata={"type": "doc", "genre": "drama"}
)
```

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.update(
  	namespace="example-namespace",
  	id="id-3", 
  	values=[5.0, 3.0], 
  	set_metadata={"genre": "comedy"}
  )
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  await index.namespace('example-namespace').update({
    id: 'id-3',
    values: [5.0, 3.0],
    metadata: {
      genre: "comedy",
    },
  });
  ```

  ```java Java theme={null}
  import com.google.protobuf.Struct;
  import com.google.protobuf.Value;
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.proto.UpdateResponse;

  import java.util.Arrays;
  import java.util.List;

  public class UpdateExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          List<Float> values = Arrays.asList(5.0f, 3.0f);
  		Struct metaData = Struct.newBuilder()
  			.putFields("genre",
  					Value.newBuilder().setStringValue("comedy").build())
  			.build();
          UpdateResponse updateResponse = index.update("id-3", values, metaData, "example-namespace", null, null);
          System.out.println(updateResponse);
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
      "google.golang.org/protobuf/types/known/structpb"
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
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      id := "id-3"

      metadataMap := map[string]interface{}{
          "genre": "comedy",
      }

      metadataFilter, err := structpb.NewStruct(metadataMap)
      if err != nil {
          log.Fatalf("Failed to create metadata map: %v", err)
      }

      err = idxConnection.UpdateVector(ctx, &pinecone.UpdateVectorRequest{
          Id:       id,
          Values: []float32{5.0, 3.0},
          Metadata: metadataFilter,
      })
      if err != nil {
          log.Fatalf("Failed to update vector with ID %v: %v", id, err)
      }
  }
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  # Update both values and metadata
  curl "https://$INDEX_HOST/vectors/update" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
          "id": "id-3",
          "values": [5.0, 3.0],
          "setMetadata": {"genre": "comedy"},
          "namespace": "example-namespace"
        }'
  ```
</CodeGroup>

After the update, the dense vector values and the `genre` metadata value are changed, but the `type` metadata value is unchanged:

```
(
    id="id-3", 
    values=[5.0, 3.0], 
    metadata={"type": "doc", "genre": "comedy"}
)
```

## Update by metadata

To add or change metadata across multiple records in a namespace, use the `update` operation with the following parameters:

* `namespace`: The [namespace](/guides/index-data/indexing-overview#namespaces) containing the records to update. To use the default namespace, set this to `"__default__"`.
* `filter`: A [metadata filter expression](/guides/index-data/indexing-overview#metadata-filter-expressions) to match the records to update.
* `setMetadata`: The metadata to add or change. When updating metadata, only the specified metadata fields are modified. If a specified metadata field does not exist, it is added.
* `dry_run`: Optional. If `true`, the number of records that match the filter expression is returned, but the records are not updated.

  <Note>
    Each request updates a maximum of 100,000 records. Use `"dry_run": true` to check if you need to run the request multiple times. See the example below for details.
  </Note>

For example, let's say you have records that represent chunks of a single document with metadata that keeps track of chunk and document details, and you want to store the author's name with each chunk of the document:

```json theme={null}
{
    "id": "document1#chunk1", 
    "values": [0.0236663818359375, -0.032989501953125, ..., -0.01041412353515625, 0.0086669921875], 
    "metadata": {
        "document_id": "document1",
        "document_title": "Introduction to Vector Databases",
        "chunk_number": 1,
        "chunk_text": "First chunk of the document content...",
        "document_url": "https://example.com/docs/document1"
    }
},
{
    "id": "document1#chunk2", 
    "values": [-0.0412445068359375, 0.028839111328125, ..., 0.01953125, -0.0174560546875],
    "metadata": {
        "document_id": "document1",
        "document_title": "Introduction to Vector Databases", 
        "chunk_number": 2,
        "chunk_text": "Second chunk of the document content...",
        "document_url": "https://example.com/docs/document1"
    }
},
...
```

The following code updates all matching records with the new `author` metadata field:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  # Use dry_run to check how many records match the filter
  dry_run_response = index.update(
      namespace="example-namespace",
      filter={"document_title": {"$eq": "Introduction to Vector Databases"}},
      set_metadata={"author": "Del Klein"},
      dry_run=True
  )
  print(dry_run_response.matched_records)

  # Perform the update
  response = index.update(
      namespace="example-namespace",
      filter={"document_title": {"$eq": "Introduction to Vector Databases"}},
      set_metadata={"author": "Del Klein"}
  )
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  await index.namespace('example-namespace').update({
    filter: { document_title: { $eq: 'Introduction to Vector Databases' } },
    metadata: { author: 'Del Klein' },
  });
  ```

  ```java Java theme={null}
  import com.google.protobuf.Struct;
  import com.google.protobuf.Value;
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.proto.UpdateResponse;

  public class UpdateByMetadataExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");

          Struct filter = Struct.newBuilder()
              .putFields("document_title", Value.newBuilder()
                  .setStructValue(Struct.newBuilder()
                      .putFields("$eq", Value.newBuilder()
                          .setStringValue("Introduction to Vector Databases")
                          .build())
                      .build())
                  .build())
              .build();

          Struct metadata = Struct.newBuilder()
              .putFields("author", Value.newBuilder()
                  .setStringValue("Del Klein")
                  .build())
              .build();

          // Dry run to check how many records match
          UpdateResponse dryRunResponse = index.updateByMetadata(
              filter, metadata, "example-namespace", true);
          System.out.println("Matched records: " + dryRunResponse.getMatchedRecords());

          // Perform the update
          UpdateResponse response = index.updateByMetadata(
              filter, metadata, "example-namespace");
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
      "google.golang.org/protobuf/types/known/structpb"
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
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{
          Host:      "INDEX_HOST",
          Namespace: "example-namespace",
      })
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
      }

      filter, err := structpb.NewStruct(map[string]interface{}{
          "document_title": map[string]interface{}{
              "$eq": "Introduction to Vector Databases",
          },
      })
      if err != nil {
          log.Fatalf("Failed to create filter: %v", err)
      }

      metadata, err := structpb.NewStruct(map[string]interface{}{
          "author": "Del Klein",
      })
      if err != nil {
          log.Fatalf("Failed to create metadata: %v", err)
      }

      // Dry run to check how many records match
      dryRun := true
      dryRunRes, err := idxConnection.UpdateVectorsByMetadata(ctx, &pinecone.UpdateVectorsByMetadataRequest{
          Filter:   filter,
          Metadata: metadata,
          DryRun:   &dryRun,
      })
      if err != nil {
          log.Fatalf("Failed to dry run update: %v", err)
      }
      fmt.Printf("Matched records: %d\n", dryRunRes.MatchedRecords)

      // Perform the update
      res, err := idxConnection.UpdateVectorsByMetadata(ctx, &pinecone.UpdateVectorsByMetadataRequest{
          Filter:   filter,
          Metadata: metadata,
      })
      if err != nil {
          log.Fatalf("Failed to update vectors by metadata: %v", err)
      }
      fmt.Printf("Updated records: %d\n", res.MatchedRecords)
  }
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/vectors/update" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H 'Content-Type: application/json' \
      -H "X-Pinecone-Api-Version: 2025-10" \
      -d '{
              "namespace": "example-namespace",
              "filter": {
                  "document_title": {"$eq": "Introduction to Vector Databases"}
              },
              "setMetadata": {
                  "author": "Del Klein"
              } 
          }'
  ```
</CodeGroup>

### Handling large updates

Each request updates a maximum of 100,000 records. For larger datasets, use `dry_run` to check the count and repeat the request as needed:

1. To check how many records match the filter expression, send a request with `dry_run` set to `true`:

   ```bash curl {11} theme={null}
   # To get the unique host for an index,
   # see https://docs.pinecone.io/guides/manage-data/target-an-index
   PINECONE_API_KEY="YOUR_API_KEY"
   INDEX_HOST="INDEX_HOST"

   curl "https://$INDEX_HOST/vectors/update" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H 'Content-Type: application/json' \
       -H "X-Pinecone-Api-Version: 2025-10" \
       -d '{
               "dry_run": true,
               "namespace": "example-namespace",
               "filter": {
                   "document_title": {"$eq": "Introduction to Vector Databases"}
               },
               "setMetadata": {
                   "author": "Del Klein"
               } 
           }'
   ```

   The response contains the number of records that match the filter expression:

   ```json theme={null}
   {
       "matchedVectors": 150000
   }
   ```

   Since this number exceeds the 100,000 record limit, you'll need to run the update request multiple times.

2. Initiate the first update by sending the request without the `dry_run` parameter:

   ```bash curl theme={null}
   curl "https://$INDEX_HOST/vectors/update" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H 'Content-Type: application/json' \
       -H "X-Pinecone-Api-Version: 2025-10" \
       -d '{
               "namespace": "example-namespace",
               "filter": {
                   "document_title": {"$eq": "Introduction to Vector Databases"}
               },
               "setMetadata": {
                   "author": "Del Klein"
               } 
           }'
   ```

   Again, the response contains the total number of records that match the filter expression, but only 100,000 will be updated:

   ```json theme={null}
   {
       "matchedVectors": 150000
   }
   ```

3. Pinecone is eventually consistent, so there can be a slight delay before your update request is processed. Repeat the `dry_run` request until the number of matching records shows that the first 100,000 records have been updated:

   ```bash curl {11} theme={null}
   # To get the unique host for an index,
   # see https://docs.pinecone.io/guides/manage-data/target-an-index
   PINECONE_API_KEY="YOUR_API_KEY"
   INDEX_HOST="INDEX_HOST"

   curl "https://$INDEX_HOST/vectors/update" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H 'Content-Type: application/json' \
       -H "X-Pinecone-Api-Version: 2025-10" \
       -d '{
               "dry_run": true,
               "namespace": "example-namespace",
               "filter": {
                   "document_title": {"$eq": "Introduction to Vector Databases"}
               },
               "setMetadata": {
                   "author": "Del Klein"
               } 
           }'
   ```

   ```json theme={null}
   {
       "matchedVectors": 50000
   }
   ```

4. Once the first 100,000 records have been updated, update the remaining records:

   ```bash curl theme={null}
   curl "https://$INDEX_HOST/vectors/update" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H 'Content-Type: application/json' \
       -H "X-Pinecone-Api-Version: 2025-10" \
       -d '{
               "namespace": "example-namespace",
               "filter": {
                   "document_title": {"$eq": "Introduction to Vector Databases"}
               },
               "setMetadata": {
                   "author": "Del Klein"
               } 
           }'
   ```

5. Repeat the `dry_run` request until the number of matching records shows that the remaining records have been updated:

   ```bash curl {11} theme={null}
   # To get the unique host for an index,
   # see https://docs.pinecone.io/guides/manage-data/target-an-index
   PINECONE_API_KEY="YOUR_API_KEY"
   INDEX_HOST="INDEX_HOST"

   curl "https://$INDEX_HOST/vectors/update" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H 'Content-Type: application/json' \
       -H "X-Pinecone-Api-Version: 2025-10" \
       -d '{
               "dry_run": true,
               "namespace": "example-namespace",
               "filter": {
                   "document_title": {"$eq": "Introduction to Vector Databases"}
               },
               "setMetadata": {
                   "author": "Del Klein"
               } 
           }'
   ```

   ```json theme={null}
   {
       "matchedVectors": 0
   }
   ```

   Once the request has completed, all matching records include the author name as metadata:

   ```json {10,22} theme={null}
   {
       "id": "document1#chunk1", 
       "values": [0.0236663818359375, -0.032989501953125, ..., -0.01041412353515625, 0.0086669921875], 
       "metadata": {
           "document_id": "document1",
           "document_title": "Introduction to Vector Databases",
           "chunk_number": 1,
           "chunk_text": "First chunk of the document content...",
           "document_url": "https://example.com/docs/document1",
           "author": "Del Klein"
       }
   },
   {
       "id": "document1#chunk2", 
       "values": [-0.0412445068359375, 0.028839111328125, ..., 0.01953125, -0.0174560546875],
       "metadata": {
           "document_id": "document1",
           "document_title": "Introduction to Vector Databases", 
           "chunk_number": 2,
           "chunk_text": "Second chunk of the document content...",
           "document_url": "https://example.com/docs/document1",
           "author": "Del Klein"
       }
   },
   ...
   ```

### Limitations

* Each request updates a maximum of 100,000 records. Use `"dry_run": true` to check if you need to run the request multiple times. See the example above for details.
* You can add or change metadata across multiple records, but you cannot remove metadata fields.

## Remove a metadata field

To remove a metadata field from a record, use the [upsert](/guides/index-data/upsert-data) operation to replace the record's metadata, providing the record's existing ID and vector values along with only the metadata you want to keep. Because upsert replaces a record's metadata in full, any fields you omit are cleared.

## Data freshness

Pinecone is eventually consistent, so there can be a slight delay before updates are visible to queries. You can [use log sequence numbers](/guides/index-data/check-data-freshness#check-the-log-sequence-number) to check whether an update request has completed.

## See also

* [Update an entire document](/guides/index-data/data-modeling#update-an-entire-document)
