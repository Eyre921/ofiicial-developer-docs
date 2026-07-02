---
title: "Fetch records"
source: https://docs.pinecone.io/guides/manage-data/fetch-data
path: guides/manage-data/fetch-data
---

Retrieve complete records by ID or metadata filter.

<Tip>
  You can fetch data using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/indexes/-/browser).
</Tip>

<Tip>
  Fetches consume [read units (RUs)](/guides/manage-cost/understanding-cost#read-units). See [Understanding cost](/guides/manage-cost/understanding-cost#fetch) for how fetch cost is calculated.
</Tip>

## Fetch records by ID

To fetch records from a namespace based on their IDs, use the `fetch` operation with the following parameters:

* `namespace`: The [namespace](/guides/index-data/indexing-overview#namespaces) containing the records to fetch. To use the default namespace, set this to `"__default__"`.
* `ids`: The IDs of the records to fetch. Maximum of 1000.

<Note>
  For on-demand indexes, since vector values are retrieved from object storage, fetch operations may have increased latency. If you only need metadata or IDs, consider using the [`query`](/reference/api/latest/data-plane/query) operation with `include_values` set to `false` instead. See [Decrease latency](/guides/optimize/decrease-latency#avoid-including-vector-values-when-not-needed) for more details.
</Note>

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  index.fetch(ids=["id-1", "id-2"], namespace="example-namespace")
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const fetchResult = await index.namespace('example-namespace').fetch(['id-1', 'id-2']);
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.proto.FetchResponse;

  import java.util.Arrays;
  import java.util.List;

  public class FetchExample {
      public static void main(String[] args) {
          PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          config.setHost("INDEX_HOST");
          PineconeConnection connection = new PineconeConnection(config);
          Index index = new Index(connection, "INDEX_NAME");

          List<String> ids = Arrays.asList("id-1", "id-2");
          FetchResponse fetchResponse = index.fetch(ids, "example-namespace");
          System.out.println(fetchResponse);
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
      idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
      if err != nil {
          log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    	}

      res, err := idxConnection.FetchVectors(ctx, []string{"id-1", "id-2"})
      if err != nil {
          log.Fatalf("Failed to fetch vectors: %v", err)
      } else {
          fmt.Printf(prettifyStruct(res))
      }
  }
  ```

  ```csharp C# theme={null}
  using Pinecone;

  var pinecone = new PineconeClient("YOUR_API_KEY");

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  var index = pinecone.Index(host: "INDEX_HOST");

  var fetchResponse = await index.FetchAsync(new FetchRequest {
      Ids = new List<string> { "id-1", "id-2" },
      Namespace = "example-namespace"
  });
  ```

  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/vectors/fetch?ids=id-1&ids=id-2&namespace=example-namespace" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10"
  ```
</CodeGroup>

The response looks like this:

<CodeGroup>
  ```Python Python theme={null}
  {'namespace': 'example-namespace',
   'usage': {'readUnits': 1},
   'vectors': {'id-1': {'id': 'id-1',
                        'values': [0.568879, 0.632687092, 0.856837332, ...]},
               'id-2': {'id': 'id-2',
                        'values': [0.00891787093, 0.581895, 0.315718859, ...]}}}
  ```

  ```JavaScript JavaScript theme={null}
  {'namespace': 'example-namespace',
   'usage': {'readUnits': 1},
   'records': {'id-1': {'id': 'id-1',
                        'values': [0.568879, 0.632687092, 0.856837332, ...]},
               'id-2': {'id': 'id-2',
                        'values': [0.00891787093, 0.581895, 0.315718859, ...]}}}
  ```

  ```java Java theme={null}
  namespace: "example-namespace"
  vectors {
    key: "id-1"
    value {
      id: "id-1"
      values: 0.568879
      values: 0.632687092
      values: 0.856837332
      ...
    }
  }
  vectors {
    key: "id-2"
    value {
      id: "id-2"
      values: 0.00891787093
      values: 0.581895
      values: 0.315718859
      ...
    }
  }
  usage {
    read_units: 1
  }
  ```

  ```go Go theme={null}
  {
    "vectors": {
      "id-1": {
        "id": "id-1",
        "values": [
          -0.0089730695,
          -0.020010853,
          -0.0042787646,
          ...
        ]
      },
      "id-2": {
        "id": "id-2",
        "values": [
          -0.005380766,
          0.00215196,
          -0.014833462,
          ...
        ]
      }
    },
    "usage": {
      "read_units": 1
    }
  }
  ```

  ```csharp C# theme={null}
  {
    "vectors": {
      "id-1": {
        "id": "id-1",
        "values": [
          -0.0089730695,
          -0.020010853,
          -0.0042787646,
          ...
        ],
        "sparseValues": null,
        "metadata": null
      },
      "vec1": {
        "id": "id-2",
        "values": [
          -0.005380766,
          0.00215196,
          -0.014833462,
          ...
        ],
        "sparseValues": null,
        "metadata": null
      }
    },
    "namespace": "example-namespace",
    "usage": {
      "readUnits": 1
    }
  ```

  ```json curl theme={null}
  {
    "vectors": {
      "id-1": {
        "id": "id-1",
        "values": [0.568879, 0.632687092, 0.856837332, ...]
      },
      "id-2": {
        "id": "id-2",
        "values": [0.00891787093, 0.581895, 0.315718859, ...]
      }
    },
    "namespace": "example-namespace",
    "usage": {"readUnits": 1},
  }
  ```
</CodeGroup>

## Fetch records by metadata

To fetch records from a namespace based on their metadata values, use the `fetch_by_metadata` operation with the following parameters:

| Parameter         | Required | Description                                                                                                                                                                                                                                                                                                                                         |
| :---------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filter`          | Yes      | A [metadata filter expression](/guides/index-data/indexing-overview#metadata-filter-expressions) describing the records to fetch. Must be present and non-empty.                                                                                                                                                                                    |
| `limit`           | No       | The maximum number of matching records to return in a single response. Defaults to 100; maximum 10,000. To retrieve more than 10,000 matching records, paginate using `paginationToken`.                                                                                                                                                            |
| `namespace`       | No       | The [namespace](/guides/index-data/indexing-overview#namespaces) containing the records to fetch. If omitted or set to an empty string, defaults to the default namespace. To explicitly use the default namespace, set this to `"__default__"`.                                                                                                    |
| `paginationToken` | No       | The `next` token value from the `pagination` object found in a previous response. Include this value to fetch the next page of results, or omit it to start from the beginning. Must be used with the same `namespace` and `filter` parameters that generated it — using an existing token with different parameters will return incorrect results. |

For example, the following code fetches 2 records with a `genre` field set to `Action/Adventure` from the default namespace:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  index = pc.Index(host="INDEX_HOST")

  results = index.fetch_by_metadata(
      filter={"genre": {"$eq": "Action/Adventure"}},
      namespace="__default__",
      limit=2
  )

  print(results)
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

  // To get the unique host for an index, 
  // see https://docs.pinecone.io/guides/manage-data/target-an-index
  const index = pc.index("INDEX_NAME", "INDEX_HOST")

  const results = await index.fetchByMetadata({
    filter: { genre: { $eq: 'Action/Adventure' } },
    namespace: '__default__',
    limit: 2
  });

  console.log(results);
  ```

  ```java Java theme={null}
  import com.google.protobuf.Struct;
  import com.google.protobuf.Value;
  import io.pinecone.clients.Index;
  import io.pinecone.configs.PineconeConfig;
  import io.pinecone.configs.PineconeConnection;
  import io.pinecone.proto.FetchByMetadataResponse;

  public class FetchByMetadataExample {
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
                          .setStringValue("Action/Adventure")
                          .build())
                      .build())
                  .build())
              .build();

          FetchByMetadataResponse response = index.fetchByMetadata(
              "__default__", filter, 2, null);

          System.out.println(response);
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
      "google.golang.org/protobuf/types/known/structpb"
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

      filter, err := structpb.NewStruct(map[string]interface{}{
          "genre": map[string]interface{}{
              "$eq": "Action/Adventure",
          },
      })
      if err != nil {
          log.Fatalf("Failed to create filter: %v", err)
      }

      namespace := "__default__"
      limit := uint32(2)

      res, err := idxConnection.FetchVectorsByMetadata(ctx, &pinecone.FetchVectorsByMetadataRequest{
          Filter:    filter,
          Namespace: &namespace,
          Limit:     &limit,
      })
      if err != nil {
          log.Fatalf("Failed to fetch vectors by metadata: %v", err)
      }
      fmt.Printf(prettifyStruct(res))
  }
  ```

  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X POST "https://$INDEX_HOST/vectors/fetch_by_metadata" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
      "namespace": "__default__",
      "filter": {"genre": {"$eq": "Action/Adventure"}},
      "limit": 2
    }'
  ```
</CodeGroup>

The response looks like this:

```json theme={null}
{
  "vectors": {
    "0": {
      "id": "0",
      "values": [
        0.0234527588, 0.0291595459 ...
      ],
      "metadata": {
        "box-office": 2923706026,
        "genre": "Action/Adventure",
        "summary": "On the alien world of Pandora, paraplegic Marine Jake Sully uses an avatar to walk again and becomes torn between his mission and protecting the planet's indigenous Na'vi people. The film stars Sam Worthington, Zoe Saldana, and Sigourney Weaver.",
        "title": "Avatar",
        "year": 2009
      }
    },
    "1": {
      "id": "1",
      "values": [
        0.0397644043, 0.013053894, ...
      ],
      "metadata": {
        "box-office": 2799439100,
        "genre": "Action/Adventure",
        "summary": "In the aftermath of Thanos wiping out half of the universe, the remaining Avengers assemble once more to undo the chaos, leading to a time-traveling adventure. Stars Robert Downey Jr., Chris Evans, and Scarlett Johansson.",
        "title": "Avengers: Endgame",
        "year": 2019
      }
    }
  },
  "namespace": "__default__",
  "usage": {
    "readUnits": 1
  },
  "pagination": {
    "next": "Tm90aGluZyB0byBzZWUgaGVyZQo="
  }
}
```

To fetch the next page of results, pass the pagination token from the previous response. For example:

<CodeGroup>
  ```Python Python theme={null}
  next_results = index.fetch_by_metadata(
      filter={"genre": {"$eq": "Action/Adventure"}},
      namespace="__default__",
      limit=2,
      pagination_token="Tm90aGluZyB0byBzZWUgaGVyZQo="
  )
  ```

  ```JavaScript JavaScript theme={null}
  const nextResults = await index.fetchByMetadata({
    filter: { genre: { $eq: 'Action/Adventure' } },
    namespace: '__default__',
    limit: 2,
    paginationToken: 'Tm90aGluZyB0byBzZWUgaGVyZQo='
  });
  ```

  ```java Java theme={null}
  FetchByMetadataResponse nextPage = index.fetchByMetadata(
      "__default__", filter, 2, "Tm90aGluZyB0byBzZWUgaGVyZQo=");
  ```

  ```go Go theme={null}
  paginationToken := "Tm90aGluZyB0byBzZWUgaGVyZQo="
  nextRes, err := idxConnection.FetchVectorsByMetadata(ctx, &pinecone.FetchVectorsByMetadataRequest{
      Filter:          filter,
      Namespace:       &namespace,
      Limit:           &limit,
      PaginationToken: &paginationToken,
  })
  ```

  ```shell curl theme={null}
  curl -X POST "https://$INDEX_HOST/vectors/fetch_by_metadata" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
      "namespace": "__default__",
      "filter": {"genre": {"$eq": "Action/Adventure"}},
      "limit": 2,
      "paginationToken": "Tm90aGluZyB0byBzZWUgaGVyZQo="
    }'
  ```
</CodeGroup>

When there are more results available, the response includes a `pagination` object with a `next` token. When there are no more results, the response does not include a `pagination` object.

## Fetch limits

**Fetch by ID limits:**

| Metric              | Limit                             |
| :------------------ | :-------------------------------- |
| Max IDs per request | 1000 IDs                          |
| Max request size    | N/A                               |
| Max request rate    | 100 requests per second per index |

**Fetch by metadata limits:**

| Metric                   | Limit                               |
| :----------------------- | :---------------------------------- |
| Max records per response | 10,000 records                      |
| Max response size        | 4 MB                                |
| Max request rate         | 5 requests per second per namespace |

To retrieve more than 10,000 matching records, paginate through results using the `paginationToken` parameter. See [Fetch records by metadata](#fetch-records-by-metadata).

## Data freshness

Pinecone is eventually consistent, so there can be a slight delay before new or changed records are visible to queries. You can view index stats to [check data freshness](/guides/index-data/check-data-freshness).
