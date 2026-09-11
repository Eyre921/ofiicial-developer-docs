---
title: "Delete data"
source: https://docs.pinecone.io/guides/manage-data/delete-data
path: guides/manage-data/delete-data
---

Delete Pinecone documents or records from a namespace by ID or metadata filter, or delete every document or record the namespace holds.

This page shows you how to delete the data in an index [namespace](/guides/index-data/indexing-overview#namespaces). The kind of index determines which operation you use. An index with a [document schema](/guides/search/full-text-search#schema-definition) uses the Documents API, and a vector index uses the [Vectors API](/reference/api/latest/data-plane/delete). If you aren't sure which kind of index you have, see [Adopt the Documents API](/guides/index-data/adopt-the-documents-api).

* **[Delete documents](#delete-documents)**: Delete documents by ID, by metadata filter, or delete every document in the namespace.
* **[Delete records](#delete-records-by-id)**: The same three options for a vector index.

<Tip>
  Deletes consume [write units (WUs)](/guides/manage-cost/understanding-cost#write-units). See [Understanding cost](/guides/manage-cost/understanding-cost#delete) for how delete cost is calculated.
</Tip>

## Delete documents

In an index with a document schema, delete documents by ID, by metadata filter, or delete the whole namespace's contents. A request specifies exactly one of `ids`, `filter`, or `delete_all`, and can name up to 1,000 IDs.

### Delete documents by ID

To delete specific documents, pass their IDs:

<CodeGroup>
  ```Python Python theme={null}
  # pip install --upgrade pinecone
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.documents.delete(namespace="articles", ids=["doc-1", "doc-2"])
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/namespaces/articles/documents/delete" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-07" \
      -d '{
              "ids": ["doc-1", "doc-2"]
          }'
  ```
</CodeGroup>

### Delete documents by metadata

To delete every document matching a [metadata filter expression](/guides/index-data/indexing-overview#metadata-filter-expressions), pass a `filter`. The response reports how many documents matched:

<CodeGroup>
  ```Python Python theme={null}
  # Connect to an index as shown above.
  response = index.documents.delete(
      namespace="articles",
      filter={"category": {"$eq": "news"}},
  )
  print(response.matched_records)
  ```

  ```bash curl theme={null}
  curl "https://$INDEX_HOST/namespaces/articles/documents/delete" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-07" \
      -d '{
              "filter": { "category": { "$eq": "news" } }
          }'
  ```
</CodeGroup>

```json theme={null}
{
    "matched_records": 6
}
```

### Delete all documents in a namespace

To empty a namespace without deleting the namespace itself, pass `delete_all`:

<CodeGroup>
  ```Python Python theme={null}
  # Connect to an index as shown above.
  index.documents.delete(namespace="articles", delete_all=True)
  ```

  ```bash curl theme={null}
  curl "https://$INDEX_HOST/namespaces/articles/documents/delete" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2026-07" \
      -d '{
              "delete_all": true
          }'
  ```
</CodeGroup>

A delete by ID and a `delete_all` return an empty response body. Only a filtered delete reports `matched_records`.

<Note>
  [Text-match operators](/guides/search/filter-by-metadata#text-match-filters) (`$match_phrase`, `$match_all`, `$match_any`) aren't supported in a filtered delete, and a request carrying one is rejected with a `400`. To delete documents by text match, [search](/guides/search/full-text-search) for them first and delete the IDs the search returns.
</Note>

For the full request and response schema, see [Delete documents](/reference/api/latest/data-plane/delete_documents).

## Delete records

In a vector index, delete records by ID, by metadata filter, or delete every record in the namespace.

### Delete records by ID

Since Pinecone records can always be efficiently accessed using their ID, deleting by ID is the most efficient way to remove specific records from a namespace.

<Note>
  To remove records from the default namespace, specify `"__default__"` as the namespace in your request.
</Note>

<CodeGroup>
  ```Python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.delete(ids=["id-1", "id-2"], namespace='example-namespace')
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const ns = index.namespace('example-namespace')
  // Delete one record by ID.
  await ns.deleteOne('id-1');
  // Delete more than one record by ID.
  await ns.deleteMany(['id-2', 'id-3']);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;

  import java.util.Arrays;
  import java.util.List;

  public class DeleteExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          List<String> ids = Arrays.asList("id-1", "id-2");
          index.deleteByIds(ids, "example-namespace");
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
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
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      id1 := "id-1"
      id2 := "id-2"

      err = idxConnection.DeleteVectorsById(ctx, []string{id1, id2})
      if err != nil {
          log.Fatalf("Failed to delete vector with ID %v: %v", id, err)
      }
  }
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/vectors/delete" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "ids": [
        "id-1", 
        "id-2"
      ],
      "namespace": "example-namespace"
    }
  '
  ```
</CodeGroup>

### Delete records by metadata

To delete records from a namespace based on their metadata values, pass a [metadata filter expression](/guides/index-data/indexing-overview#metadata-filter-expressions) to the `delete` operation. This deletes all records in the namespace that match the filter expression.

For example, the following code deletes all records with a `genre` field set to `documentary` from namespace `example-namespace`:

<CodeGroup>
  ```Python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.delete(
      filter={
          "genre": {"$eq": "documentary"}
      },
      namespace="example-namespace" 
  )
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const ns = index.namespace('example-namespace')

  await ns.deleteMany({
    genre: { $eq: "documentary" },
  });
  ```

  ```java Java theme={null}
  import com.google.protobuf.Struct;
  import com.google.protobuf.Value;
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;

  import java.util.Arrays;
  import java.util.List;

  public class DeleteExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          Struct filter = Struct.newBuilder()
                  .putFields("genre", Value.newBuilder()
                          .setStructValue(Struct.newBuilder()
                                  .putFields("$eq", Value.newBuilder()
                                          .setStringValue("documentary")
                                          .build()))
                          .build())
                  .build();
          index.deleteByFilter(filter, "example-namespace");
          
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
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
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      metadataFilter := map[string]interface{}{
  		"genre": map[string]interface{}{
  			"$eq": "documentary",
  		},
      }

      filter, err := structpb.NewStruct(metadataFilter)
      if err != nil {
          log.Fatalf("Failed to create metadata filter: %v", err)
      }

      err = idxConnection.DeleteVectorsByFilter(ctx, filter)
      if err != nil {
          log.Fatalf("Failed to delete vector(s) with filter %+v: %v", filter, err)
      }
  }
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -i "https://$INDEX_HOST/vectors/delete" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "filter": {"genre": {"$eq": "documentary"}},
      "namespace": "example-namespace"
    }'
  ```
</CodeGroup>

### Delete all records in a namespace

To delete all of the records in a namespace but not the namespace itself, provide a `namespace` parameter and specify the appropriate `deleteAll` parameter for your SDK. To target the default namespace, set `namespace` to `"__default__"`.

<CodeGroup>
  ```Python Python theme={null}
  # pip install "pinecone[grpc]"
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.delete(delete_all=True, namespace='example-namespace')
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  await index.namespace('example-namespace').deleteAll();
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;

  import java.util.Arrays;
  import java.util.List;

  public class DeleteExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");
          index.deleteAll("example-namespace");
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
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
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      err = idxConnection.DeleteAllVectorsInNamespace(ctx)
      if err != nil {
          log.Fatalf("Failed to delete all vectors in namespace %v: %v", namespace, err)
      }
  }
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/vectors/delete" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "deleteAll": true,
      "namespace": "example-namespace"
    }
  '
  ```
</CodeGroup>

## Delete an entire namespace

To delete an entire namespace and all of its records, see [Delete a namespace](/guides/manage-data/manage-namespaces#delete-a-namespace).

## Delete an entire index

To remove all records from an index, [delete the index](/guides/manage-data/manage-indexes#delete-an-index) and [recreate it](/guides/index-data/create-an-index).

## Vector delete limits

These limits apply to the Vectors API. For an index with a document schema, see [Delete documents](#delete-documents).

### Delete by ID limits

| Metric              | Limit                                          |
| :------------------ | :--------------------------------------------- |
| Max IDs per request | 1000 IDs                                       |
| Max request rate    | 5000 records per second per index or namespace |

### Delete by metadata limits

| Metric           | Limit                                                                      |
| :--------------- | :------------------------------------------------------------------------- |
| Max request rate | 5 requests per second per namespace<br />500 requests per second per index |

## Data freshness

Pinecone is eventually consistent, so there can be a slight delay before new or changed records are visible to queries. You can view index stats to [check data freshness](/guides/index-data/check-data-freshness).
