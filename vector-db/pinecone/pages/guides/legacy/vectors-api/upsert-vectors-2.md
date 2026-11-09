---
title: "Upsert vectors into a legacy vector index"
source: https://docs.pinecone.io/guides/legacy/vectors-api/upsert-vectors
path: guides/legacy/vectors-api/upsert-vectors
---

Upsert dense and sparse vectors into a legacy vector index with the legacy Vectors API, in batches or in parallel.

> [!NOTE]
>
> New projects should use the [Documents API](/guides/indexes/create-an-index#create-a-document-index). To move an existing index, see [Move to the Documents API](/guides/indexes/move-to-the-documents-api).

This page shows you how to upsert records into a namespace in a legacy vector index with the legacy Vectors API. For a document index, see [Upsert data](/guides/data/upsert-data).

If a record ID already exists, upserting overwrites the entire record. To change only part of a record, [update](/guides/legacy/vectors-api/update-vectors) it.

## Upsert dense vectors

To upsert dense vectors into an [index of dense vectors](/guides/legacy/vectors-api/create-a-vector-index#dense-vectors), use the [Upsert records](/reference/api/latest/data-plane/upsert) operation:

* Specify the [`namespace`](/guides/indexes/index-data-overview#namespaces) to upsert into. If the namespace doesn't exist, it's created. To use the default namespace, set the namespace to `"__default__"`.
* Format your input data as records, each with the following:
  * An `id` field with a unique record identifier for the index namespace.
  * A `values` field with the dense vector values.
  * Optionally, a `metadata` field with [key-value pairs](/guides/indexes/index-data-overview#metadata) to store additional information or context. When you query the index, you can use metadata to [filter search results](/guides/search/filter-by-metadata).

```Python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST", grpc=True)

index.upsert(
  vectors=[
    {
      "id": "A", 
      "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
      "metadata": {"genre": "comedy", "year": 2020}
    },
    {
      "id": "B", 
      "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
      "metadata": {"genre": "documentary", "year": 2019}
    },
    {
      "id": "C", 
      "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
      "metadata": {"genre": "comedy", "year": 2019}
    },
    {
      "id": "D", 
      "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
      "metadata": {"genre": "drama"}
    }
  ],
  namespace="example-namespace"
)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index, 
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index("INDEX_NAME", "INDEX_HOST")

const records = [
    {
      id: 'A',
      values: [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
      metadata: { genre: "comedy", year: 2020 },
    },
    {
      id: 'B',
      values: [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
      metadata: { genre: "documentary", year: 2019 },
    },
    {
      id: 'C',
      values: [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
      metadata: { genre: "comedy", year: 2019 },
    },
    {
      id: 'D',
      values: [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
      metadata: { genre: "drama" },
    }
]

await index.namespace('example-namespace').upsert({ records: records });
```

```java Java theme={null}
import com.google.protobuf.Struct;
import com.google.protobuf.Value;
import io.pinecone.clients.Index;
import io.pinecone.configs.PineconeConfig;
import io.pinecone.configs.PineconeConnection;

import java.util.Arrays;
import java.util.List;

public class UpsertExample {
    public static void main(String[] args) {
        PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
        // To get the unique host for an index, 
        // see https://docs.pinecone.io/guides/indexes/target-an-index
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);
        Index index = new Index(config, connection, "INDEX_NAME");
        List<Float> values1 = Arrays.asList(0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f, 0.1f);
        List<Float> values2 = Arrays.asList(0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f, 0.2f);
        List<Float> values3 = Arrays.asList(0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f, 0.3f);
        List<Float> values4 = Arrays.asList(0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f);
        Struct metaData1 = Struct.newBuilder()
                .putFields("genre", Value.newBuilder().setStringValue("comedy").build())
                .putFields("year", Value.newBuilder().setNumberValue(2020).build())
                .build();
        Struct metaData2 = Struct.newBuilder()
                .putFields("genre", Value.newBuilder().setStringValue("documentary").build())
                .putFields("year", Value.newBuilder().setNumberValue(2019).build())
                .build();
        Struct metaData3 = Struct.newBuilder()
                .putFields("genre", Value.newBuilder().setStringValue("comedy").build())
                .putFields("year", Value.newBuilder().setNumberValue(2019).build())
                .build();
        Struct metaData4 = Struct.newBuilder()
                .putFields("genre", Value.newBuilder().setStringValue("drama").build())
                .build();

        index.upsert("A", values1, null, null, metaData1, "example-namespace");
        index.upsert("B", values2, null, null, metaData2, "example-namespace");
        index.upsert("C", values3, null, null, metaData3, "example-namespace");
        index.upsert("D", values4, null, null, metaData4, "example-namespace");
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
    // see https://docs.pinecone.io/guides/indexes/target-an-index
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
    if err != nil {
        log.Fatalf("Failed to create IndexConnection for Host: %v", err)
	  }

    metadataMap1 := map[string]interface{}{
        "genre": "comedy",
        "year": 2020,
    }

    metadata1, err := structpb.NewStruct(metadataMap1)
    if err != nil {
        log.Fatalf("Failed to create metadata map: %v", err)
    }

    metadataMap2 := map[string]interface{}{
        "genre": "documentary",
        "year": 2019,
    }

    metadata2, err := structpb.NewStruct(metadataMap2)
    if err != nil {
        log.Fatalf("Failed to create metadata map: %v", err)
    }

    metadataMap3 := map[string]interface{}{
        "genre": "comedy",
        "year": 2019,
    }

    metadata3, err := structpb.NewStruct(metadataMap3)
    if err != nil {
        log.Fatalf("Failed to create metadata map: %v", err)
    }

    metadataMap4 := map[string]interface{}{
        "genre": "drama",
    }

    metadata4, err := structpb.NewStruct(metadataMap4)
    if err != nil {
        log.Fatalf("Failed to create metadata map: %v", err)
    }

    vectors := []*pinecone.Vector{
        {
            Id:     "A",
            Values: &[]float32{0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1},
            Metadata: metadata1,
        },
        {
            Id:     "B",
            Values: &[]float32{0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2},
            Metadata: metadata2,
        },
        {
            Id:     "C",
            Values: &[]float32{0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3},
            Metadata: metadata3,
        },   
        {
            Id:     "D",
            Values: &[]float32{0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4},
            Metadata: metadata4,
        },   
    }

    count, err := idxConnection.UpsertVectors(ctx, vectors)
    if err != nil {
        log.Fatalf("Failed to upsert vectors: %v", err)
    } else {
        fmt.Printf("Successfully upserted %d vector(s)!\n", count)
    }
}
```

```bash curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/vectors/upsert" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
    "vectors": [
      {
        "id": "A",
        "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
        "metadata": {"genre": "comedy", "year": 2020}
      },
      {
        "id": "B",
        "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
        "metadata": {"genre": "documentary", "year": 2019}
      },
      {
        "id": "C",
        "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
        "metadata": {"genre": "comedy", "year": 2019}
      },
      {
        "id": "D",
        "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
        "metadata": {"genre": "drama"}
      }
    ],
    "namespace": "example-namespace"
  }'
```

## Upsert sparse vectors

To upsert sparse vectors into an [index of sparse vectors](/guides/legacy/vectors-api/create-a-vector-index#sparse-vectors), use the [Upsert records](/reference/api/latest/data-plane/upsert) operation:

* Specify the [`namespace`](/guides/indexes/index-data-overview#namespaces) to upsert into. If the namespace doesn't exist, it's created. To use the default namespace, set the namespace to `"__default__"`.
* Format your input data as records, each with the following:
  * An `id` field with a unique record identifier for the index namespace.
  * A `sparse_values` field with the sparse vector values and indices.
  * Optionally, a `metadata` field with [key-value pairs](/guides/indexes/index-data-overview#metadata) to store additional information or context. When you query the index, you can use metadata to [filter search results](/guides/search/filter-by-metadata).

For example, the following code upserts sparse vector representations of sentences related to the term "apple", with the source text and additional fields stored as metadata:

```python Python theme={null}
from pinecone import Pinecone, SparseValues, Vector

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

index.upsert(
    namespace="example-namespace",
    vectors=[
        {
            "id": "vec1",
            "sparse_values": {
                "values": [1.7958984, 0.41577148, 2.828125, 2.8027344, 2.8691406, 1.6533203, 5.3671875, 1.3046875, 0.49780273, 0.5722656, 2.71875, 3.0820312, 2.5019531, 4.4414062, 3.3554688],
                "indices": [822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191]
            },
            "metadata": {
                "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
                "category": "technology",
                "quarter": "Q3"
            }
        },
        {
            "id": "vec2",
            "sparse_values": {
                "values": [0.4362793, 3.3457031, 2.7714844, 3.0273438, 3.3164062, 5.6015625, 2.4863281, 0.38134766, 1.25, 2.9609375, 0.34179688, 1.4306641, 0.34375, 3.3613281, 1.4404297, 2.2558594, 2.2597656, 4.8710938, 0.5605469],
                "indices": [131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697]
            },
            "metadata": {
                "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
                "category": "technology",
                "quarter": "Q4"
            }
        },
        {
            "id": "vec3",
            "sparse_values": {
                "values": [2.6875, 4.2929688, 3.609375, 3.0722656, 2.1152344, 5.78125, 3.7460938, 3.7363281, 1.2695312, 3.4824219, 0.7207031, 0.0826416, 4.671875, 3.7011719, 2.796875, 0.61621094],
                "indices": [8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697]
            },
            "metadata": {
                "chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production",
                "category": "technology",
                "quarter": "Q3"
            }
        },
        {
            "id": "vec4",
            "sparse_values": {
                "values": [0.73046875, 0.46972656, 2.84375, 5.2265625, 3.3242188, 1.9863281, 0.9511719, 0.5019531, 4.4257812, 3.4277344, 0.41308594, 4.3242188, 2.4179688, 3.1757812, 1.0224609, 2.0585938, 2.5859375],
                "indices": [131900689, 152217691, 441495248, 1640781426, 1851149807, 2263326288, 2502307765, 2641553256, 2684780967, 2966813704, 3162218338, 3283104238, 3488055477, 3530642888, 3888762515, 4152503047, 4177290673]
            },
            "metadata": {
                "chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.",
                "category": "technology",
                "quarter": "Q4"
            }
        }
    ]
)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

// To get the unique host for an index, 
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index("INDEX_NAME", "INDEX_HOST")

await index.namespace('example-namespace').upsert({ records: [
  {
    id: 'vec1',
    sparseValues: {
      indices: [822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191],
      values: [1.7958984, 0.41577148, 2.828125, 2.8027344, 2.8691406, 1.6533203, 5.3671875, 1.3046875, 0.49780273, 0.5722656, 2.71875, 3.0820312, 2.5019531, 4.4414062, 3.3554688]
    },
    metadata: { 
      chunk_text: 'AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.', 
      category: 'technology',
      quarter: 'Q3' 
    }
  },
  {
    id: 'vec2',
    sparseValues: {
      indices: [131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697],
      values: [0.4362793, 3.3457031, 2.7714844, 3.0273438, 3.3164062, 5.6015625, 2.4863281, 0.38134766, 1.25, 2.9609375, 0.34179688, 1.4306641, 0.34375, 3.3613281, 1.4404297, 2.2558594, 2.2597656, 4.8710938, 0.5605469]
    },
    metadata: { 
      chunk_text: "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.", 
      category: 'technology',
      quarter: 'Q4' 
    }
  },
  {
    id: 'vec3',
    sparseValues: {
      indices: [8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697],
      values: [2.6875, 4.2929688, 3.609375, 3.0722656, 2.1152344, 5.78125, 3.7460938, 3.7363281, 1.2695312, 3.4824219, 0.7207031, 0.0826416, 4.671875, 3.7011719, 2.796875, 0.61621094]
    },
    metadata: { 
      chunk_text: "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production", 
      category: 'technology',
      quarter: 'Q3' 
    }
  },
  {
    id: 'vec4',
    sparseValues: {
      indices: [131900689, 152217691, 441495248, 1640781426, 1851149807, 2263326288, 2502307765, 2641553256, 2684780967, 2966813704, 3162218338, 3283104238, 3488055477, 3530642888, 3888762515, 4152503047, 4177290673],
      values: [0.73046875, 0.46972656, 2.84375, 5.2265625, 3.3242188, 1.9863281, 0.9511719, 0.5019531, 4.4257812, 3.4277344, 0.41308594, 4.3242188, 2.4179688, 3.1757812, 1.0224609, 2.0585938, 2.5859375]
    },
    metadata: { 
      chunk_text: 'AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.', 
      category: 'technology',
      quarter: 'Q4' 
    }
  }
] });
```

```java Java theme={null}
import io.pinecone.clients.Pinecone;
import io.pinecone.clients.Index;
import com.google.protobuf.Struct;
import com.google.protobuf.Value;

import java.util.*;

public class UpsertSparseVectors {
    public static void main(String[] args) throws InterruptedException {
        // Instantiate Pinecone class
        Pinecone pinecone = new Pinecone.Builder("YOUR_API_KEY").build();
        
        Index index = pinecone.getIndexConnection("INDEX_NAME");

        // Record 1
        ArrayList<Long> indices1 = new ArrayList<>(Arrays.asList(
                822745112L, 1009084850L, 1221765879L, 1408993854L, 1504846510L,
                1596856843L, 1640781426L, 1656251611L, 1807131503L, 2543655733L,
                2902766088L, 2909307736L, 3246437992L, 3517203014L, 3590924191L
        ));

        ArrayList<Float> values1 = new ArrayList<>(Arrays.asList(
                1.7958984f, 0.41577148f, 2.828125f, 2.8027344f, 2.8691406f,
                1.6533203f, 5.3671875f, 1.3046875f, 0.49780273f, 0.5722656f,
                2.71875f, 3.0820312f, 2.5019531f, 4.4414062f, 3.3554688f
        ));

        Struct metaData1 = Struct.newBuilder()
                .putFields("chunk_text", Value.newBuilder().setStringValue("AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.").build())
                .putFields("category", Value.newBuilder().setStringValue("technology").build())
                .putFields("quarter", Value.newBuilder().setStringValue("Q3").build())
                .build();

        // Record 2
        ArrayList<Long> indices2 = new ArrayList<>(Arrays.asList(
                131900689L, 592326839L, 710158994L, 838729363L, 1304885087L,
                1640781426L, 1690623792L, 1807131503L, 2066971792L, 2428553208L,
                2548600401L, 2577534050L, 3162218338L, 3319279674L, 3343062801L,
                3476647774L, 3485013322L, 3517203014L, 4283091697L
        ));

        ArrayList<Float> values2 = new ArrayList<>(Arrays.asList(
                0.4362793f, 3.3457031f, 2.7714844f, 3.0273438f, 3.3164062f,
                5.6015625f, 2.4863281f, 0.38134766f, 1.25f, 2.9609375f,
                0.34179688f, 1.4306641f, 0.34375f, 3.3613281f, 1.4404297f,
                2.2558594f, 2.2597656f, 4.8710938f, 0.5605469f
        ));

        Struct metaData2 = Struct.newBuilder()
                .putFields("chunk_text", Value.newBuilder().setStringValue("Analysts suggest that AAPL'\\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.").build())
                .putFields("category", Value.newBuilder().setStringValue("technology").build())
                .putFields("quarter", Value.newBuilder().setStringValue("Q4").build())
                .build();

        // Record 3
        ArrayList<Long> indices3 = new ArrayList<>(Arrays.asList(
                8661920L, 350356213L, 391213188L, 554637446L, 1024951234L,
                1640781426L, 1780689102L, 1799010313L, 2194093370L, 2632344667L,
                2641553256L, 2779594451L, 3517203014L, 3543799498L,
                3837503950L, 4283091697L
        ));

        ArrayList<Float> values3 = new ArrayList<>(Arrays.asList(
                2.6875f, 4.2929688f, 3.609375f, 3.0722656f, 2.1152344f,
                5.78125f, 3.7460938f, 3.7363281f, 1.2695312f, 3.4824219f,
                0.7207031f, 0.0826416f, 4.671875f, 3.7011719f, 2.796875f,
                0.61621094f
        ));

        Struct metaData3 = Struct.newBuilder()
                .putFields("chunk_text", Value.newBuilder().setStringValue("AAPL'\\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production").build())
                .putFields("category", Value.newBuilder().setStringValue("technology").build())
                .putFields("quarter", Value.newBuilder().setStringValue("Q3").build())
                .build();

        // Record 4
        ArrayList<Long> indices4 = new ArrayList<>(Arrays.asList(
                131900689L, 152217691L, 441495248L, 1640781426L, 1851149807L,
                2263326288L, 2502307765L, 2641553256L, 2684780967L, 2966813704L,
                3162218338L, 3283104238L, 3488055477L, 3530642888L, 3888762515L,
                4152503047L, 4177290673L
        ));

        ArrayList<Float> values4 = new ArrayList<>(Arrays.asList(
                0.73046875f, 0.46972656f, 2.84375f, 5.2265625f, 3.3242188f,
                1.9863281f, 0.9511719f, 0.5019531f, 4.4257812f, 3.4277344f,
                0.41308594f, 4.3242188f, 2.4179688f, 3.1757812f, 1.0224609f,
                2.0585938f, 2.5859375f
        ));

        Struct metaData4 = Struct.newBuilder()
                .putFields("chunk_text", Value.newBuilder().setStringValue("AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space").build())
                .putFields("category", Value.newBuilder().setStringValue("technology").build())
                .putFields("quarter", Value.newBuilder().setStringValue("Q4").build())
                .build();

        index.upsert("vec1", Collections.emptyList(), indices1, values1, metaData1, "example-namespace");
        index.upsert("vec2", Collections.emptyList(), indices2, values2, metaData2, "example-namespace");
        index.upsert("vec3", Collections.emptyList(), indices3, values3, metaData3, "example-namespace");
        index.upsert("vec4", Collections.emptyList(), indices4, values4, metaData4, "example-namespace");
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
	// see https://docs.pinecone.io/guides/indexes/target-an-index
	idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
	if err != nil {
		log.Fatalf("Failed to create IndexConnection for Host: %v", err)
	}

	sparseValues1 := pinecone.SparseValues{
		Indices: []uint32{822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191},
		Values:  []float32{1.7958984, 0.41577148, 2.828125, 2.8027344, 2.8691406, 1.6533203, 5.3671875, 1.3046875, 0.49780273, 0.5722656, 2.71875, 3.0820312, 2.5019531, 4.4414062, 3.3554688},
	}

	metadataMap1 := map[string]interface{}{
		"chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones",
		"category":    "technology",
		"quarter":     "Q3",
	}

	metadata1, err := structpb.NewStruct(metadataMap1)
	if err != nil {
		log.Fatalf("Failed to create metadata map: %v", err)
	}

	sparseValues2 := pinecone.SparseValues{
		Indices: []uint32{131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697},
		Values:  []float32{0.4362793, 3.3457031, 2.7714844, 3.0273438, 3.3164062, 5.6015625, 2.4863281, 0.38134766, 1.25, 2.9609375, 0.34179688, 1.4306641, 0.34375, 3.3613281, 1.4404297, 2.2558594, 2.2597656, 4.8710938, 0.560546},
	}

	metadataMap2 := map[string]interface{}{
		"chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
		"category":    "technology",
		"quarter":     "Q4",
	}

	metadata2, err := structpb.NewStruct(metadataMap2)
	if err != nil {
		log.Fatalf("Failed to create metadata map: %v", err)
	}

	sparseValues3 := pinecone.SparseValues{
		Indices: []uint32{8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697},
		Values:  []float32{2.6875, 4.2929688, 3.609375, 3.0722656, 2.1152344, 5.78125, 3.7460938, 3.7363281, 1.2695312, 3.4824219, 0.7207031, 0.0826416, 4.671875, 3.7011719, 2.796875, 0.61621094},
	}

	metadataMap3 := map[string]interface{}{
		"chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production",
		"category":    "technology",
		"quarter":     "Q3",
	}

	metadata3, err := structpb.NewStruct(metadataMap3)
	if err != nil {
		log.Fatalf("Failed to create metadata map: %v", err)
	}

	sparseValues4 := pinecone.SparseValues{
		Indices: []uint32{131900689, 152217691, 441495248, 1640781426, 1851149807, 2263326288, 2502307765, 2641553256, 2684780967, 2966813704, 3162218338, 3283104238, 3488055477, 3530642888, 3888762515, 4152503047, 4177290673},
		Values:  []float32{0.73046875, 0.46972656, 2.84375, 5.2265625, 3.3242188, 1.9863281, 0.9511719, 0.5019531, 4.4257812, 3.4277344, 0.41308594, 4.3242188, 2.4179688, 3.1757812, 1.0224609, 2.0585938, 2.5859375},
	}

	metadataMap4 := map[string]interface{}{
		"chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.",
		"category":    "technology",
		"quarter":     "Q4",
	}

	metadata4, err := structpb.NewStruct(metadataMap4)
	if err != nil {
		log.Fatalf("Failed to create metadata map: %v", err)
	}

	vectors := []*pinecone.Vector{
		{
			Id:           "vec1",
			SparseValues: &sparseValues1,
			Metadata:     metadata1,
		},
		{
			Id:           "vec2",
			SparseValues: &sparseValues2,
			Metadata:     metadata2,
		},
		{
			Id:           "vec3",
			SparseValues: &sparseValues3,
			Metadata:     metadata3,
		},
		{
			Id:           "vec4",
			SparseValues: &sparseValues4,
			Metadata:     metadata4,
		},
	}

	count, err := idxConnection.UpsertVectors(ctx, vectors)
	if err != nil {
		log.Fatalf("Failed to upsert vectors: %v", err)
	} else {
		fmt.Printf("Successfully upserted %d vector(s)!\n", count)
	}
}
```

```shell curl theme={null}
INDEX_HOST="INDEX_HOST"
PINECONE_API_KEY="YOUR_API_KEY"

curl "https://$INDEX_HOST/vectors/upsert" \
  -H "Content-Type: application/json" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "namespace": "example-namespace",
        "vectors": [
            {
                "id": "vec1",
                "sparseValues": {
                    "values": [1.7958984, 0.41577148, 2.828125, 2.8027344, 2.8691406, 1.6533203, 5.3671875, 1.3046875, 0.49780273, 0.5722656, 2.71875, 3.0820312, 2.5019531, 4.4414062, 3.3554688],
                    "indices": [822745112, 1009084850, 1221765879, 1408993854, 1504846510, 1596856843, 1640781426, 1656251611, 1807131503, 2543655733, 2902766088, 2909307736, 3246437992, 3517203014, 3590924191]
                },
                "metadata": {
                    "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
                    "category": "technology",
                    "quarter": "Q3"
                }
            },
            {
                "id": "vec2",
                "sparseValues": {
                    "values": [0.4362793, 3.3457031, 2.7714844, 3.0273438, 3.3164062, 5.6015625, 2.4863281, 0.38134766, 1.25, 2.9609375, 0.34179688, 1.4306641, 0.34375, 3.3613281, 1.4404297, 2.2558594, 2.2597656, 4.8710938, 0.5605469],
                    "indices": [131900689, 592326839, 710158994, 838729363, 1304885087, 1640781426, 1690623792, 1807131503, 2066971792, 2428553208, 2548600401, 2577534050, 3162218338, 3319279674, 3343062801, 3476647774, 3485013322, 3517203014, 4283091697]
                },
                "metadata": {
                    "chunk_text": "Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
                    "category": "technology",
                    "quarter": "Q4"
                }
            },
            {
                "id": "vec3",
                "sparseValues": {
                    "values": [2.6875, 4.2929688, 3.609375, 3.0722656, 2.1152344, 5.78125, 3.7460938, 3.7363281, 1.2695312, 3.4824219, 0.7207031, 0.0826416, 4.671875, 3.7011719, 2.796875, 0.61621094],
                    "indices": [8661920, 350356213, 391213188, 554637446, 1024951234, 1640781426, 1780689102, 1799010313, 2194093370, 2632344667, 2641553256, 2779594451, 3517203014, 3543799498, 3837503950, 4283091697]
                },
                "metadata": {
                    "chunk_text": "AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production",
                    "category": "technology",
                    "quarter": "Q3"
                }
            },
            {
                "id": "vec4",
                "sparseValues": {
                    "values": [0.73046875, 0.46972656, 2.84375, 5.2265625, 3.3242188, 1.9863281, 0.9511719, 0.5019531, 4.4257812, 3.4277344, 0.41308594, 4.3242188, 2.4179688, 3.1757812, 1.0224609, 2.0585938, 2.5859375],
                    "indices": [131900689, 152217691, 441495248, 1640781426, 1851149807, 2263326288, 2502307765, 2641553256, 2684780967, 2966813704, 3162218338, 3283104238, 3488055477, 3530642888, 3888762515, 4152503047, 4177290673]
                },
                "metadata": {
                    "chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.",
                    "category": "technology",
                    "quarter": "Q4"
                }
            },
        ]
    }'
```

## Upsert in batches

> [!TIP]
>
> To control costs when ingesting large datasets (10,000,000+ records), use [import](/guides/data/import-data) instead of upsert.

Send upserts in batches to help increase throughput. A batch should be as large as possible (up to 1,000 records) without exceeding the [max request size of 2 MB](#upsert-limits).

The number of records that fit in one batch depends on the vector dimension and metadata size:

| Dimension | Metadata (bytes) | Max batch size |
| :- | :- | :- |
| 386 | 0 | 1,000 |
| 768 | 500 | 559 |
| 1536 | 2000 | 245 |

```Python Python theme={null}
import random
import itertools
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST", grpc=True)

def chunks(iterable, batch_size=200):
    """A helper function to break an iterable into chunks of size batch_size."""
    it = iter(iterable)
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))

vector_dim = 128
vector_count = 10000

# Example generator that generates many (id, vector) pairs
example_data_generator = map(lambda i: (f'id-{i}', [random.random() for _ in range(vector_dim)]), range(vector_count))

# Upsert data with 200 vectors per upsert request
for ids_vectors_chunk in chunks(example_data_generator, batch_size=200):
    index.upsert(vectors=ids_vectors_chunk) 
```

```JavaScript JavaScript theme={null}
import { Pinecone } from "@pinecone-database/pinecone";

const RECORD_COUNT = 10000;
const RECORD_DIMENSION = 128;

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" });

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index({ host: "INDEX_HOST" });

// A helper function that breaks an array into chunks of size batchSize
const chunks = (array, batchSize = 200) => {
  const chunks = [];

  for (let i = 0; i < array.length; i += batchSize) {
    chunks.push(array.slice(i, i + batchSize));
  }

  return chunks;
};

// Example data generation function, creates many (id, vector) pairs
const generateExampleData = () =>
  Array.from({ length: RECORD_COUNT }, (_, i) => {
    return {
      id: `id-${i}`,
      values: Array.from({ length: RECORD_DIMENSION }, (_, i) => Math.random()),
    };
  });

const exampleRecordData = generateExampleData();
const recordChunks = chunks(exampleRecordData);

// Upsert data with 200 records per upsert request
for (const chunk of recordChunks) {
  await index.upsert({ records: chunk })
}
```

```java Java theme={null}
import io.pinecone.clients.Index;
import io.pinecone.configs.PineconeConfig;
import io.pinecone.configs.PineconeConnection;
import io.pinecone.unsigned_indices_model.VectorWithUnsignedIndices;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class UpsertBatchExample {
    private static final int RECORD_COUNT = 10000;
    private static final int RECORD_DIMENSION = 128;
    private static final int BATCH_SIZE = 200;

    public static void main(String[] args) {
        PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
        // To get the unique host for an index,
        // see https://docs.pinecone.io/guides/indexes/target-an-index
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);
        Index index = new Index(config, connection, "INDEX_NAME");

        List<VectorWithUnsignedIndices> vectors = generateVectors();

        // Upsert data with 200 vectors per upsert request
        for (int i = 0; i < vectors.size(); i += BATCH_SIZE) {
            index.upsert(vectors.subList(i, Math.min(i + BATCH_SIZE, vectors.size())), "example-namespace");
        }
    }

    // Example data generation function, creates many (id, vector) pairs
    private static List<VectorWithUnsignedIndices> generateVectors() {
        Random random = new Random();
        List<VectorWithUnsignedIndices> vectors = new ArrayList<>();

        for (int i = 0; i < RECORD_COUNT; i++) {
            List<Float> values = new ArrayList<>();
            for (int j = 0; j < RECORD_DIMENSION; j++) {
                values.add(random.nextFloat());
            }
            vectors.add(new VectorWithUnsignedIndices("id-" + i, values));
        }

        return vectors;
    }
}
```

```go Go theme={null}
package main

import (
	"context"
	"fmt"
	"log"
	"math/rand"

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

	// Example data: 10,000 vectors with 128 dimensions
	vectors := make([]*pinecone.Vector, 10000)
	for i := range vectors {
		values := make([]float32, 128)
		for j := range values {
			values[j] = rand.Float32()
		}
		vectors[i] = &pinecone.Vector{Id: fmt.Sprintf("id-%d", i), Values: &values}
	}

	// Upsert 200 vectors per request
	batchSize := 200
	for start := 0; start < len(vectors); start += batchSize {
		end := min(start+batchSize, len(vectors))
		if _, err := idxConnection.UpsertVectors(ctx, vectors[start:end]); err != nil {
			log.Fatalf("Failed to upsert batch starting at %d: %v", start, err)
		}
	}
}
```

## Upsert in parallel

> [!TIP]
>
> Python SDK v6.0.0 and later provide `async` methods for use with [asyncio](https://docs.python.org/3/library/asyncio.html). Asyncio support lets you use Pinecone with async web frameworks such as FastAPI, Quart, and Sanic. For details, see [Async requests](/reference/sdks/python/overview#async-requests).

Send multiple upserts in parallel to help increase throughput. Each upsert call blocks until the response arrives, so send several at once.

Upserts can be made asynchronously:

```Python Python theme={null}
# This example uses `async_req=True` and multiple threads.
# For a single-threaded approach compatible with modern async web frameworks, 
# see https://docs.pinecone.io/reference/sdks/python/overview#async-requests
import random
import itertools
from pinecone import Pinecone

# Initialize the client with pool_threads=30. This limits simultaneous requests to 30.
pc = Pinecone(api_key="YOUR_API_KEY", pool_threads=30)

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

def chunks(iterable, batch_size=200):
    """A helper function to break an iterable into chunks of size batch_size."""
    it = iter(iterable)
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))

vector_dim = 128
vector_count = 10000

example_data_generator = map(lambda i: (f'id-{i}', [random.random() for _ in range(vector_dim)]), range(vector_count))

# Upsert data with 200 vectors per upsert request asynchronously
# - Pass async_req=True to index.upsert()
with pc.index(host="INDEX_HOST", pool_threads=30) as index:
    # Send requests in parallel
    async_results = [
        index.upsert(vectors=ids_vectors_chunk, async_req=True)
        for ids_vectors_chunk in chunks(example_data_generator, batch_size=200)
    ]
    # Wait for and retrieve responses (this raises in case of error)
    [async_result.get() for async_result in async_results]
```

```JavaScript JavaScript theme={null}
import { Pinecone } from "@pinecone-database/pinecone";

const RECORD_COUNT = 10000;
const RECORD_DIMENSION = 128;

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" });

// To get the unique host for an index,
// see https://docs.pinecone.io/guides/indexes/target-an-index
const index = pc.index({ host: "INDEX_HOST" });

// A helper function that breaks an array into chunks of size batchSize
const chunks = (array, batchSize = 200) => {
  const chunks = [];

  for (let i = 0; i < array.length; i += batchSize) {
    chunks.push(array.slice(i, i + batchSize));
  }

  return chunks;
};

// Example data generation function, creates many (id, vector) pairs
const generateExampleData = () =>
  Array.from({ length: RECORD_COUNT }, (_, i) => {
    return {
      id: `id-${i}`,
      values: Array.from({ length: RECORD_DIMENSION }, (_, i) => Math.random()),
    };
  });

const exampleRecordData = generateExampleData();
const recordChunks = chunks(exampleRecordData);

// Upsert data with 200 records per request asynchronously using Promise.all()
await Promise.all(recordChunks.map((chunk) => index.upsert({ records: chunk })));
```

```java Java theme={null}
import io.pinecone.clients.Index;
import io.pinecone.configs.PineconeConfig;
import io.pinecone.configs.PineconeConnection;
import io.pinecone.unsigned_indices_model.VectorWithUnsignedIndices;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class UpsertParallelExample {
    private static final int RECORD_COUNT = 10000;
    private static final int RECORD_DIMENSION = 128;
    private static final int BATCH_SIZE = 200;

    public static void main(String[] args) throws InterruptedException {
        PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
        // To get the unique host for an index,
        // see https://docs.pinecone.io/guides/indexes/target-an-index
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);
        Index index = new Index(config, connection, "INDEX_NAME");

        List<VectorWithUnsignedIndices> vectors = generateVectors();

        // Send up to 10 requests of 200 vectors at a time
        ExecutorService executor = Executors.newFixedThreadPool(10);
        for (int i = 0; i < vectors.size(); i += BATCH_SIZE) {
            List<VectorWithUnsignedIndices> batch = vectors.subList(i, Math.min(i + BATCH_SIZE, vectors.size()));
            executor.submit(() -> index.upsert(batch, "example-namespace"));
        }

        // Wait for all requests to finish
        executor.shutdown();
        executor.awaitTermination(5, TimeUnit.MINUTES);
    }

    // Example data generation function, creates many (id, vector) pairs
    private static List<VectorWithUnsignedIndices> generateVectors() {
        Random random = new Random();
        List<VectorWithUnsignedIndices> vectors = new ArrayList<>();

        for (int i = 0; i < RECORD_COUNT; i++) {
            List<Float> values = new ArrayList<>();
            for (int j = 0; j < RECORD_DIMENSION; j++) {
                values.add(random.nextFloat());
            }
            vectors.add(new VectorWithUnsignedIndices("id-" + i, values));
        }

        return vectors;
    }
}
```

```go Go theme={null}
package main

import (
	"context"
	"fmt"
	"log"
	"math/rand"
	"sync"

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

	// Example data: 10,000 vectors with 128 dimensions
	vectors := make([]*pinecone.Vector, 10000)
	for i := range vectors {
		values := make([]float32, 128)
		for j := range values {
			values[j] = rand.Float32()
		}
		vectors[i] = &pinecone.Vector{Id: fmt.Sprintf("id-%d", i), Values: &values}
	}

	// Send up to 10 requests of 200 vectors at a time
	batchSize := 200
	semaphore := make(chan struct{}, 10)
	errs := make(chan error, len(vectors)/batchSize+1)
	var wg sync.WaitGroup

	for start := 0; start < len(vectors); start += batchSize {
		batch := vectors[start:min(start+batchSize, len(vectors))]
		wg.Add(1)
		semaphore <- struct{}{}
		go func(start int, batch []*pinecone.Vector) {
			defer wg.Done()
			defer func() { <-semaphore }()
			if _, err := idxConnection.UpsertVectors(ctx, batch); err != nil {
				errs <- fmt.Errorf("batch starting at %d: %w", start, err)
			}
		}(start, batch)
	}

	wg.Wait()
	close(errs)
	for err := range errs {
		log.Printf("Failed to upsert %v", err)
	}
}
```

### Python SDK with gRPC

The Python SDK with gRPC can upsert faster. Unlike REST, gRPC multiplexes requests, so it handles many requests in parallel without head-of-line blocking. You can also pass retry strategies to the gRPC SDK, including [exponential backoff](/guides/production/error-handling#implement-retry-logic). The gRPC client supports legacy vector indexes only.

gRPC support is included in the base `pinecone` package, and upsert, query, fetch, and delete use the same syntax as the standard SDK. To use it, import the `pinecone.grpc` subpackage and target an index as usual:

```Python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

# This is gRPC client aliased as "Pinecone"
pc = Pinecone(api_key='YOUR_API_KEY')  

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST", grpc=True)
```

To send multiple upserts in parallel, use `upsert_async`, which returns a future for each request:

```Python Python theme={null}
def chunker(seq, batch_size):
  return (seq[pos:pos + batch_size] for pos in range(0, len(seq), batch_size))

futures = [
  index.upsert_async(vectors=chunk)
  for chunk in chunker(data, batch_size=200)
]

# Wait for and retrieve responses (this raises in case of error)
[future.result() for future in futures]
```

> [!NOTE]
>
> Upserts through the gRPC SDK can hit write throttling sooner. If this happens often, [implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic).

## Upsert limits

| Metric | Limit |
| :- | :- |
| Max [batch size](/guides/legacy/vectors-api/upsert-vectors#upsert-in-batches) for records with vectors | 1,000 records, up to 2 MB total |
| Max batch size for records with text | 96 records |
| Max documents per upsert request | 1,000, or 96 when the schema declares `embed` or `sparse_embed` |
| Max document upsert request size | 2 MB |
| Max document size | 2 MB |
| Max `full_text_search` string fields per schema | 100 |
| Max size per `full_text_search` string field | 100 KB |
| Max tokens per `full_text_search` string field | 10,000 |
| Max [bytes per token](/guides/search/full-text-search/text-processing#tokens-and-analyzers) | 1,024 bytes |
| Max filterable metadata size per document | 40 KB |
| Max length for a record ID | 512 characters |
| Max dimensionality for dense vectors | 20,000 |
| Max non-zero values for sparse vectors | 2048 |
| Max dimensionality for sparse vectors | 4.2 billion |

The limit for text is lower because Pinecone converts that text to vectors at upsert time with [integrated embedding](/guides/indexes/index-data-overview#integrated-embedding), and 96 is the max batch size of the [hosted embedding models](/guides/indexes/index-configuration#embedding-models) doing the conversion.

The 40 KB filterable metadata limit doesn't apply to `full_text_search` text fields.
