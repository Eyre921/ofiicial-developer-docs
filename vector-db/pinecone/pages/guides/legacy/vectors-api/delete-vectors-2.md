---
title: "Delete vectors from a legacy vector index"
source: https://docs.pinecone.io/guides/legacy/vectors-api/delete-vectors
path: guides/legacy/vectors-api/delete-vectors
---

Delete records from a legacy vector index by ID or metadata filter with the legacy Vectors API, or delete every record in a namespace.

> [!NOTE]
>
> New projects should use the [Documents API](/guides/get-started/documents-api). To move an existing index, see [Move to the Documents API](/guides/indexes/move-to-the-documents-api).

This page shows you how to delete records from a namespace in a legacy vector index with the legacy Vectors API. For a document index, see [Delete data](/guides/data/delete-data).

## Delete records by ID

Since Pinecone records can always be efficiently accessed using their ID, deleting by ID is the most efficient way to remove specific records from a namespace.

> [!NOTE]
>
> To remove records from the default namespace, specify `"__default__"` as the namespace in your request.

```Python Python theme={null}
# pip install pinecone
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST", grpc=True)

index.delete(ids=["id-1", "id-2"], namespace='example-namespace')
```

```JavaScript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index, 
// see https://docs.pinecone.io/guides/indexes/target-an-index
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
        // see https://docs.pinecone.io/guides/indexes/target-an-index
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);
        Index index = new Index(config, connection, "INDEX_NAME");
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

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
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
    // see https://docs.pinecone.io/guides/indexes/target-an-index
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
# see https://docs.pinecone.io/guides/indexes/target-an-index
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

## Delete records by metadata

To delete records from a namespace based on their metadata values, pass a [metadata filter expression](/guides/indexes/index-data-overview#metadata-filter-expressions) to the `delete` operation. This deletes all records in the namespace that match the filter expression.

For example, the following code deletes all records with a `genre` field set to `documentary` from namespace `example-namespace`:

```Python Python theme={null}
# pip install pinecone
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST", grpc=True)

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
// see https://docs.pinecone.io/guides/indexes/target-an-index
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
        // see https://docs.pinecone.io/guides/indexes/target-an-index
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);
        Index index = new Index(config, connection, "INDEX_NAME");
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

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
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
    // see https://docs.pinecone.io/guides/indexes/target-an-index
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
# see https://docs.pinecone.io/guides/indexes/target-an-index
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

## Delete all records in a namespace

To delete all of the records in a namespace but not the namespace itself, provide a `namespace` parameter and specify the appropriate `deleteAll` parameter for your SDK. To target the default namespace, set `namespace` to `"__default__"`.

```Python Python theme={null}
# pip install pinecone
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST", grpc=True)

index.delete(delete_all=True, namespace='example-namespace')
```

```JavaScript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index, 
// see https://docs.pinecone.io/guides/indexes/target-an-index
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
        // see https://docs.pinecone.io/guides/indexes/target-an-index
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);
        Index index = new Index(config, connection, "INDEX_NAME");
        index.deleteAll("example-namespace");
    }
}
```

```go Go theme={null}
package main

import (
    "context"
    "log"

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
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
    // see https://docs.pinecone.io/guides/indexes/target-an-index
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
# see https://docs.pinecone.io/guides/indexes/target-an-index
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

## Delete limits

### Delete by ID limits

| Metric | Limit |
| :- | :- |
| Max IDs per request | 1000 IDs |
| Max request rate | 5000 records per second per index or namespace |

### Delete by metadata limits

| Metric | Limit |
| :- | :- |
| Max request rate | 20 requests per second per namespace 500 requests per second per index |

## Data freshness

Pinecone is eventually consistent, so there can be a slight delay before new or changed records are visible to queries. You can view index stats to [check data freshness](/guides/data/check-data-freshness).
