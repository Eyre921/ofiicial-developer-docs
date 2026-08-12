---
title: "Manage namespaces"
source: https://docs.pinecone.io/guides/manage-data/manage-namespaces
path: guides/manage-data/manage-namespaces
---

Create, describe, list, and delete namespaces in Pinecone serverless indexes, including defining filterable metadata fields and schemas ahead of upsert.

## Create a namespace

<Note>
  This feature is available only on the `2025-10` version of the API.
</Note>

Namespaces are created automatically as you [upsert](/guides/index-data/upsert-data) records. However, you can also create namespaces ahead of time using the [`create_namespace`](/reference/api/2025-10/data-plane/createnamespace) operation. Specify a name for the namespace and, optionally, the [metadata fields to index](/guides/index-data/create-an-index#metadata-indexing).

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  namespace = index.create_namespace(
      name="example-namespace",
      schema={
          "fields": {
              "document_id": {"filterable": True},
              "document_title": {"filterable": True},
              "chunk_number": {"filterable": True},
              "document_url": {"filterable": True},
              "created_at": {"filterable": True}
          }
      }
  )

  print(namespace)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index('INDEX_NAME', 'INDEX_HOST');

  const namespace = await index.createNamespace({
    name: 'example-namespace',
    schema: {
      fields: {
        document_id: { filterable: true },
        document_title: { filterable: true },
        chunk_number: { filterable: true },
        document_url: { filterable: true },
        created_at: { filterable: true }
      }
    }
  });

  console.log(namespace);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.proto.NamespaceDescription;
  import io.pinecone.proto.MetadataSchema;
  import io.pinecone.proto.MetadataSchemaField;

  public class CreateNamespaceExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);

          Index index = new Index(config, connection, "INDEX_NAME");

          MetadataSchemaField filterable = MetadataSchemaField.newBuilder()
              .setFilterable(true)
              .build();

          MetadataSchema schema = MetadataSchema.newBuilder()
              .putFields("document_id", filterable)
              .putFields("document_title", filterable)
              .putFields("chunk_number", filterable)
              .putFields("document_url", filterable)
              .putFields("created_at", filterable)
              .build();

          NamespaceDescription namespace = index.createNamespace("example-namespace", schema);

          System.out.println(namespace);
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "encoding/json"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
    	bytes, _ := json.MarshalIndent(obj, "", "  ")
      return string(bytes)
  }

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

      namespace, err := idxConnection.CreateNamespace(ctx, &pinecone.CreateNamespaceParams{
          Name: "example-namespace",
          Schema: &pinecone.MetadataSchema{
              Fields: map[string]pinecone.MetadataSchemaField{
                  "document_id":    {Filterable: true},
                  "document_title": {Filterable: true},
                  "chunk_number":   {Filterable: true},
                  "document_url":   {Filterable: true},
                  "created_at":     {Filterable: true},
              },
          },
      })
      if err != nil {
          log.Fatalf("Failed to create namespace: %v", err)
      }
      fmt.Printf(prettifyStruct(namespace))
  }
  ```

  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/namespaces" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
          "name": "example-namespace",
          "schema": {
            "fields": { 
              "document_id": {"filterable": true},
              "document_title": {"filterable": true},
              "chunk_number": {"filterable": true},
              "document_url": {"filterable": true},
              "created_at": {"filterable": true}
            }
          }
        }'
  ```
</CodeGroup>

The response will look like the following:

```json theme={null}
{
    "name": "example-namespace",
    "record_count": "0",
    "schema": {
        "fields": {
            "document_title": {
                "filterable": true
            },
            "document_url": {
                "filterable": true
            },
            "chunk_number": {
                "filterable": true
            },
            "document_id": {
                "filterable": true
            },
            "created_at": {
                "filterable": true
            }
        }
    }
}
```

## List all namespaces in an index

Use the [`list_namespaces`](/reference/api/latest/data-plane/listnamespaces) operation to list all namespaces in a serverless index.

Up to 100 namespaces are returned at a time by default, in sorted order (bitwise “C” collation). If the `limit` parameter is set, up to that number of namespaces are returned instead. Whenever there are additional namespaces to return, the response also includes a `pagination_token` that you can use to get the next batch of namespaces. When the response does not include a `pagination_token`, there are no more namespaces to return.

<CodeGroup>
  ```python Python theme={null}
  # Not supported with pinecone["grpc"] extras installed
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index = pc.Index(host="INDEX_HOST")

  # Implicit pagination using a generator function
  for namespace in index.list_namespaces():
      print(namespace.name, ":", namespace.record_count)

  # Manual pagination
  namespaces = index.list_namespaces_paginated(
      limit=2,
      pagination_token="eyJza2lwX3Bhc3QiOiIxMDEwMy0="
  )

  print(namespaces)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  const namespaceList = await index.listNamespaces();

  console.log(namespaceList);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.AsyncIndex;
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.proto.ListNamespacesResponse;
  import org.openapitools.db_data.client.ApiException;

  public class Namespaces {
      public static void main(String[] args) throws ApiException {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);

          Index index = new Index(config, connection, "docs-example");

          // List all namespaces with default pagination limit (100)
          ListNamespacesResponse listNamespacesResponse = index.listNamespaces(null, null);

          // List all namespaces with pagination limit of 2
          ListNamespacesResponse listNamespacesResponseWithLimit = index.listNamespaces(2);

          // List all namespaces with pagination limit and token
          ListNamespacesResponse listNamespacesResponsePaginated = index.listNamespaces(5, "eyJza2lwX3Bhc3QiOiIxMDEwMy0=");

          System.out.println(listNamespacesResponseWithLimit);
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "encoding/json"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
    	bytes, _ := json.MarshalIndent(obj, "", "  ")
      return string(bytes)
  }

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

      limit := uint32(10)
      namespaces, err := idxConnection.ListNamespaces(ctx, &pinecone.ListNamespacesParams{
          Limit: &limit,
      })
      if err != nil {
          log.Fatalf("Failed to list namespaces: %v", err)
      }
      fmt.Printf(prettifyStruct(namespaces))
  }
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/namespaces" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2025-10"
  ```
</CodeGroup>

The response will look like the following:

<CodeGroup>
  ```plaintext Python theme={null}
  # Implicit pagination (print output from: for n in index.list_namespaces(): print(n.name, ":", n.record_count))
  example-namespace : 20000
  example-namespace2 : 10500
  example-namespace3 : 10000
  ...

  # Manual pagination (response from list_namespaces_paginated())
  {
      "namespaces": [
          {"name": "example-namespace", "record_count": "20000"},
          {"name": "example-namespace2", "record_count": "10500"}
      ],
      "pagination": {"next": "Tm90aGluZyB0byBzZWUgaGVyZQo="}
  }
  ```

  ```javascript JavaScript theme={null}
  {
    namespaces: [
      { name: 'example-namespace', recordCount: '20000' },
      { name: 'example-namespace2', recordCount: '10500' },
      ...
    ],
    pagination: "Tm90aGluZyB0byBzZWUgaGVyZQo="
  }
  ```

  ```java Java theme={null}
  namespaces {
    name: "example-namespace"
    record_count: 20000
  }
  namespaces {
    name: "example-namespace2"
    record_count: 10500
  }
  pagination {
    next: "eyJza2lwX3Bhc3QiOiJlZDVhYzFiNi1kMDFiLTQ2NTgtYWVhZS1hYjJkMGI2YzBiZjQiLCJwcmVmaXgiOm51bGx9"
  }
  ```

  ```go Go theme={null}
  {
    "Namespaces": [
      {
        "name": "example-namespace",
        "record_count": 20000
      },
      {
        "name": "example-namespace2",
        "record_count": 10500
      },
      ...
    ],
    "Pagination": {
      "next": "eyJza2lwX3Bhc3QiOiIyNzQ5YTU1YS0zZTQ2LTQ4MDItOGFlNi1hZTJjZGNkMTE5N2IiLCJwcmVmaXgiOm51bGx9"
    }
  }
  ```

  ```json curl theme={null}
  {
    "namespaces": [
      {
        "name": "example-namespace",
        "record_count": 20000
      },
      {
        "name": "example-namespace2",
        "record_count": 10500
      },
      ...
    ],
    "pagination": {
      "next": "Tm90aGluZyB0byBzZWUgaGVyZQo="
    }
  }
  ```
</CodeGroup>

## Describe a namespace

Use the [`describe_namespace`](/reference/api/latest/data-plane/describenamespace) operation to get details about a namespace in a serverless index, including the total number of vectors in the namespace.

<CodeGroup>
  ```python Python theme={null}
  # Not supported with pinecone["grpc"] extras installed
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index = pc.Index(host="INDEX_HOST")

  namespace = index.describe_namespace(namespace="example-namespace")

  print(namespace)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const index = pc.index('docs-example');

  const namespace = await index.describeNamespace('example-namespace');

  console.log(namespace);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.proto.NamespaceDescription;

  import org.openapitools.db_data.client.ApiException;

  public class Namespaces {
      public static void main(String[] args) throws ApiException {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);

          Index index = new Index(config, connection, "docs-example");

          NamespaceDescription namespaceDescription = index.describeNamespace("example-namespace");

          System.out.println(namespaceDescription);
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "encoding/json"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
    	bytes, _ := json.MarshalIndent(obj, "", "  ")
      return string(bytes)
  }

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

      namespace, err := idxConnection.DescribeNamespace(ctx, "example-namespace")
      if err != nil {
          log.Fatalf("Failed to describe namespace: %v", err)
      }
      fmt.Printf(prettifyStruct(namespace))
  }
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"
  NAMESPACE="NAMESPACE_NAME"  # To target the default namespace, use "__default__".

  curl -X GET "https://$INDEX_HOST/namespaces/$NAMESPACE" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2025-10"
  ```
</CodeGroup>

The response will look like the following:

<CodeGroup>
  ```python Python theme={null}
  {
      "name": "example-namespace",
      "record_count": "20000"
  }
  ```

  ```javascript JavaScript theme={null}
  { name: 'example-namespace', recordCount: '20000' }
  ```

  ```java Java theme={null}
  name: "example-namespace"
  record_count: 20000
  ```

  ```go Go theme={null}
  {
    "name": "example-namespace",
    "record_count": 20000
  }
  ```

  ```json curl theme={null}
  {
    "name": "example-namespace",
    "record_count": 20000
  }
  ```
</CodeGroup>

## Delete a namespace

Use the [`delete_namespace`](/reference/api/latest/data-plane/deletenamespace) operation to delete a namespace in a serverless index.

<Warning>
  Deleting a namespace is irreversible. All data in the namespace is permanently deleted.
</Warning>

<CodeGroup>
  ```python Python theme={null}
  # Not supported with pinecone["grpc"] extras installed
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index = pc.Index(host="INDEX_HOST")

  index.delete_namespace(namespace="example-namespace")
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' })

  const index = pc.index('INDEX_NAME', 'INDEX_HOST');

  const namespace = await index.deleteNamespace('example-namespace');

  console.log(namespace);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;

  import java.util.concurrent.ExecutionException;

  public class DeleteNamespace {
      public static void main(String[] args) throws ExecutionException, InterruptedException {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
        // To get the unique host for an index, 
        // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);

          Index index = new Index(config, connection, "docs-example");

          index.deleteNamespace("example-namespace");
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "encoding/json"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v4/pinecone"
  )

  func prettifyStruct(obj interface{}) string {
    	bytes, _ := json.MarshalIndent(obj, "", "  ")
      return string(bytes)
  }

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

      err := idxConnection.DeleteNamespace(ctx, "example-namespace")
      if err != nil {
          log.Fatalf("Failed to delete namespace: %v", err)
      }
  }
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"
  NAMESPACE="NAMESPACE_NAME" # To target the default namespace, use "__default__".

  curl -X DELETE "https://$INDEX_HOST/namespaces/$NAMESPACE" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2025-10"
  ```
</CodeGroup>

## Rename a namespace

Pinecone does not support renaming namespaces directly. Instead, you must [delete the records](/guides/manage-data/delete-data) in the namespace and [upsert the records](/guides/index-data/upsert-data) to a new namespace.

## Move records to a new namespace

Pinecone does not support moving records between namespaces directly. Instead, you must [delete the records](/guides/manage-data/delete-data) in the old namespace and [upsert the records](/guides/index-data/upsert-data) to the new namespace.
