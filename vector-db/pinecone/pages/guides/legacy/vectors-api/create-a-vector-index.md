---
title: "Create a legacy vector index"
source: https://docs.pinecone.io/guides/legacy/vectors-api/create-a-vector-index
path: guides/legacy/vectors-api/create-a-vector-index
---

Create a legacy vector index that stores dense or sparse vectors you generate with an external embedding model, served by the legacy Vectors API.

> [!NOTE]
>
> New projects should use the [Documents API](/guides/indexes/create-an-index#create-a-document-index). To move an existing index, see [Move to the Documents API](/guides/indexes/move-to-the-documents-api).

A legacy vector index stores dense or sparse vectors that you generate with an external embedding model, and it's read and written through the legacy Vectors API. To store vectors in a document index instead, declare a `dense_vector` or `sparse_vector` field. See [Create a document index](/guides/indexes/create-an-index#create-a-document-index).

## Dense vectors

If you use an external embedding model to convert your data to dense vectors, [create an index](/reference/api/2026-04/control-plane/create_index) as follows:

* Provide a `name` for the index.
* Set the `vector_type` to `dense`.
* Specify the `dimension` and similarity `metric` of the vectors you'll store in the index. This should match the dimension and metric supported by your embedding model.
* Set `spec.cloud` and `spec.region` to the [cloud and region](/guides/indexes/index-configuration#cloud-regions) where the index should be deployed. For Python, you also need to import the `ServerlessSpec` class.

Other parameters are optional. See [Create an index](/reference/api/2026-04/control-plane/create_index) for details.

```python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec

pc = Pinecone(api_key="YOUR_API_KEY")

index_name = "standard-dense-py"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        vector_type="dense",
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ),
        deletion_protection="disabled",
        tags={
            "environment": "development"
        }
    )
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

await pc.createIndex({
  name: 'standard-dense-js',
  vectorType: 'dense',
  dimension: 1536,
  metric: 'cosine',
  spec: {
    serverless: {
      cloud: 'aws',
      region: 'us-east-1'
    }
  },
  deletionProtection: 'disabled',
  tags: { environment: 'development' }, 
});
```

```java Java theme={null}
import io.pinecone.clients.Pinecone;
import java.util.HashMap;
import java.util.Map;

public class CreateServerlessIndexExample {
    public static void main(String[] args) {
        Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
        String indexName = "standard-dense-java";
        String cloud = "aws";
        String region = "us-east-1";
        Map<String, String> tags = new HashMap<>();
        tags.put("environment", "development");
        pc.createServerlessIndex(
            indexName,
            "cosine", 
            1536, 
            cloud,
            region,
            "disabled", 
            tags
        );
    }
}
```

```go Go theme={null}
package main

import (
    "context"
    "fmt"
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

    // Serverless index
  	indexName := "standard-dense-go"
	vectorType := "dense"
    dimension := int32(1536)
    metric := pinecone.IndexMetricCosine
	deletionProtection := pinecone.DeletionProtectionDisabled

    idx, err := pc.CreateServerlessIndex(ctx, &pinecone.CreateServerlessIndexRequest{
        Name:               indexName,
        VectorType:         &vectorType,
        Dimension:          &dimension,
        Metric:             &metric,
        Cloud:              pinecone.CloudAWS,
        Region:             "us-east-1",
        DeletionProtection: &deletionProtection,
        Tags:               &pinecone.IndexTags{ "environment": "development" },
    })
    if err != nil {
        log.Fatalf("Failed to create serverless index: %v", err)
    } else {
        fmt.Printf("Successfully created serverless index: %v", idx.Name)
    }
}
```

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -X POST "https://api.pinecone.io/indexes" \
     -H "Accept: application/json" \
     -H "Content-Type: application/json" \
     -H "Api-Key: $PINECONE_API_KEY" \
     -H "X-Pinecone-Api-Version: 2026-07" \
     -d '{
           "name": "standard-dense-curl",
           "deployment": {
             "deployment_type": "managed",
             "cloud": "aws",
             "region": "us-east-1"
           },
           "schema": {
             "fields": {
               "_values": { "type": "dense_vector", "dimension": 1536, "metric": "cosine" }
             }
           },
           "tags": {
             "environment": "development"
           },
           "deletion_protection": "disabled"
         }'
```

```bash CLI theme={null}
# Target the project where you want to create the index.
pc target -o "example-org" -p "example-project"
# Create the index.
pc index create \
  --name "standard-dense-cli" \
  --vector-type "dense" \
  --dimension 1536 \
  --metric "cosine" \
  --cloud "aws" \
  --region "us-east-1" \
  --tags "environment=development" \
  --deletion-protection "disabled"
```

## Sparse vectors

If you use an external embedding model to convert your data to sparse vectors, [create an index](/reference/api/2026-04/control-plane/create_index) as follows:

* Provide a `name` for the index.
* Set the `vector_type` to `sparse`.
* Set the distance `metric` to `dotproduct`. Indexes that store sparse vectors don't support other [distance metrics](/guides/indexes/index-data-overview#distance-metrics).
* Set `spec.cloud` and `spec.region` to the cloud and region where the index should be deployed.

Other parameters are optional. See [Create an index](/reference/api/2026-04/control-plane/create_index) for details.

```python Python theme={null}
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key="YOUR_API_KEY")

index_name = "standard-sparse-py"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        vector_type="sparse",
        metric="dotproduct",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

await pc.createIndex({
  name: 'standard-sparse-js',
  vectorType: 'sparse',
  metric: 'dotproduct',
  spec: {
    serverless: {
      cloud: 'aws',
      region: 'us-east-1'
    },
  },
});
```

```java Java theme={null}
import io.pinecone.clients.Pinecone;

import java.util.*;

public class SparseIndex {
    public static void main(String[] args) throws InterruptedException {
        // Instantiate Pinecone class
        Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();

        // Create the index
        String indexName = "standard-sparse-java";
        String cloud = "aws";
        String region = "us-east-1";
        String vectorType = "sparse";
        Map<String, String> tags = new HashMap<>();
        tags.put("env", "test");
        pinecone.createSparseServelessIndex(indexName,
                cloud,
                region,
                "disabled",
                tags,
                vectorType);
    }
}
```

```go Go theme={null}
package main

import (
	"context"
	"fmt"
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

	indexName := "standard-sparse-go"
	vectorType := "sparse"
	metric := pinecone.IndexMetricDotproduct
	deletionProtection := pinecone.DeletionProtectionDisabled

	idx, err := pc.CreateServerlessIndex(ctx, &pinecone.CreateServerlessIndexRequest{
		Name:               indexName,
		Metric:             &metric,
		VectorType:         &vectorType,
		Cloud:              pinecone.CloudAWS,
		Region:             "us-east-1",
		DeletionProtection: &deletionProtection,
	})
	if err != nil {
		log.Fatalf("Failed to create serverless index: %v", err)
	} else {
		fmt.Printf("Successfully created serverless index: %v", idx.Name)
	}
}
```

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -X POST "https://api.pinecone.io/indexes" \
     -H "Accept: application/json" \
     -H "Content-Type: application/json" \
     -H "Api-Key: $PINECONE_API_KEY" \
     -H "X-Pinecone-Api-Version: 2026-07" \
     -d '{
            "name": "standard-sparse-curl",
            "deployment": {
               "deployment_type": "managed",
               "cloud": "aws",
               "region": "us-east-1"
            },
            "schema": {
               "fields": {
                  "_sparse_values": { "type": "sparse_vector" }
               }
            }
         }'
```

```bash CLI theme={null}
# Target the project where you want to create the index.
pc target -o "example-org" -p "example-project"
# Create the index.
pc index create \
  --name "standard-sparse-cli" \
  --vector-type "sparse" \
  --metric "dotproduct" \
  --cloud "aws" \
  --region "us-east-1" \
  --tags "environment=development"
```

## Wait for the index to be ready

A new index can't accept data until its `status.ready` field is `true`. See [Wait for the index to be ready](/guides/indexes/create-an-index#wait-for-the-index-to-be-ready).
