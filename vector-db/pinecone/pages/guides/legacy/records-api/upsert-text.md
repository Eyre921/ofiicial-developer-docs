---
title: "Upsert text into a legacy integrated index"
source: https://docs.pinecone.io/guides/legacy/records-api/upsert-text
path: guides/legacy/records-api/upsert-text
---

Upsert source text into a legacy integrated index with the legacy Records API, and have Pinecone convert it to dense or sparse vectors.

> [!NOTE]
>
> New projects should use the [Documents API](/guides/indexes/create-an-index#create-a-document-index). To move an existing index, see [Move to the Documents API](/guides/indexes/move-to-the-documents-api).

This page shows you how to upsert source text into a legacy integrated index created with `create_index_for_model`. The legacy Records API converts the text to vectors with the hosted embedding model associated with the index. For a document index with [integrated embedding](/guides/search/integrated-embedding), see [Upsert data](/guides/data/upsert-data).

When you describe a legacy integrated index, its text field has the `semantic_text` type. Document schemas don't use that type.

## Upsert text as dense vectors

To upsert source text into a legacy integrated index, use the [Upsert text](/reference/api/latest/data-plane/upsert_records) operation. Pinecone converts the text to dense vectors automatically using the hosted dense embedding model associated with the index.

* Specify the [`namespace`](/guides/indexes/index-data-overview#namespaces) to upsert into. If the namespace doesn't exist, it's created. To use the default namespace, set the namespace to `"__default__"`.
* Format your input data as records, each with the following:
  * An `_id` field with a unique record identifier for the index namespace. `id` can be used as an alias for `_id`.
  * A field with the source text to convert to a vector. This field must match the `field_map` specified in the index.
  * Additional fields are stored as record [metadata](/guides/indexes/index-data-overview#metadata) and can be returned in search results or used to [filter search results](/guides/search/filter-by-metadata).

For example, the following code converts the sentences in the `chunk_text` fields to dense vectors and then upserts them into `example-namespace` in an example index. The additional `category` field is stored as metadata.

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

# Upsert records into a namespace
# `chunk_text` fields are converted to dense vectors
# `category` fields are stored as metadata
index.upsert_records(
    namespace="example-namespace",
    records=[
        {
            "_id": "rec1",
            "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.",
            "category": "digestive system", 
        },
        {
            "_id": "rec2",
            "chunk_text": "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.",
            "category": "cultivation",
        },
        {
            "_id": "rec3",
            "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.",
            "category": "immune system",
        },
        {
            "_id": "rec4",
            "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.",
            "category": "endocrine system",
        },
    ]
) 
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index, 
// see https://docs.pinecone.io/guides/indexes/target-an-index
const namespace = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

// Upsert records into a namespace
// `chunk_text` fields are converted to dense vectors
// `category` is stored as metadata
await namespace.upsertRecords({ records: [
        {
            "_id": "rec1",
            "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.",
            "category": "digestive system", 
        },
        {
            "_id": "rec2",
            "chunk_text": "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.",
            "category": "cultivation",
        },
        {
            "_id": "rec3",
            "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.",
            "category": "immune system",
        },
        {
            "_id": "rec4",
            "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.",
            "category": "endocrine system",
        }
] });
```

```java Java theme={null}
import io.pinecone.clients.Index;
import io.pinecone.configs.PineconeConfig;
import io.pinecone.configs.PineconeConnection;
import org.openapitools.db_data.client.ApiException;

import java.util.*;

public class UpsertText {
    public static void main(String[] args) throws ApiException {
        PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);

        Index index = new Index(config, connection, "integrated-dense-java");
        ArrayList<Map<String, String>> upsertRecords = new ArrayList<>();

        HashMap<String, String> record1 = new HashMap<>();
        record1.put("_id", "rec1");
        record1.put("category", "digestive system");
        record1.put("chunk_text", "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.");

        HashMap<String, String> record2 = new HashMap<>();
        record2.put("_id", "rec2");
        record2.put("category", "cultivation");
        record2.put("chunk_text", "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.");

        HashMap<String, String> record3 = new HashMap<>();
        record3.put("_id", "rec3");
        record3.put("category", "immune system");
        record3.put("chunk_text", "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.");

        HashMap<String, String> record4 = new HashMap<>();
        record4.put("_id", "rec4");
        record4.put("category", "endocrine system");
        record4.put("chunk_text", "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.");

        upsertRecords.add(record1);
        upsertRecords.add(record2);
        upsertRecords.add(record3);
        upsertRecords.add(record4);

        index.upsertRecords("example-namespace", upsertRecords);
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

    // Upsert records into a namespace
    // `chunk_text` fields are converted to dense vectors
    // `category` is stored as metadata
	records := []*pinecone.IntegratedRecord{
        {
            "_id": "rec1",
            "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.",
            "category": "digestive system", 
        },
        {
            "_id": "rec2",
            "chunk_text": "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.",
            "category": "cultivation",
        },
        {
            "_id": "rec3",
            "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.",
            "category": "immune system",
        },
        {
            "_id": "rec4",
            "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.",
            "category": "endocrine system",
        },
	}

	err = idxConnection.UpsertRecords(ctx, records)
	if err != nil {
		log.Fatalf("Failed to upsert vectors: %v", err)
	}
}
```

```shell curl theme={null}
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
INDEX_HOST="INDEX_HOST"
NAMESPACE="YOUR_NAMESPACE"
PINECONE_API_KEY="YOUR_API_KEY"

# Upsert records into a namespace
# `chunk_text` fields are converted to dense vectors
# `category` is stored as metadata
curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/upsert" \
  -H "Content-Type: application/x-ndjson" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{"_id": "rec1", "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.", "category": "digestive system"}
      {"_id": "rec2", "chunk_text": "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.", "category": "cultivation"}
      {"_id": "rec3", "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.", "category": "immune system"}
      {"_id": "rec4", "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.", "category": "endocrine system"}'
```

## Upsert text as sparse vectors

To upsert source text into a legacy integrated index, use the [Upsert text](/reference/api/latest/data-plane/upsert_records) operation. Pinecone converts the text to sparse vectors automatically using the hosted sparse embedding model associated with the index.

* Specify the [`namespace`](/guides/indexes/index-data-overview#namespaces) to upsert into. If the namespace doesn't exist, it's created. To use the default namespace, set the namespace to `"__default__"`.
* Format your input data as records, each with the following:
  * An `_id` field with a unique record identifier for the index namespace. `id` can be used as an alias for `_id`.
  * A field with the source text to convert to a vector. This field must match the `field_map` specified in the index.
  * Additional fields are stored as record [metadata](/guides/indexes/index-data-overview#metadata) and can be returned in search results or used to [filter search results](/guides/search/filter-by-metadata).

For example, the following code converts the sentences in the `chunk_text` fields to sparse vectors and then upserts them into `example-namespace` in an example index. The additional `category` and `quarter` fields are stored as metadata.

```python Python theme={null}
import time

from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

# Upsert records into a namespace
# `chunk_text` fields are converted to sparse vectors
# `category` and `quarter` fields are stored as metadata
index.upsert_records(
    namespace="example-namespace",
    records=[
        { 
            "_id": "vec1", 
            "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.", 
            "category": "technology",
            "quarter": "Q3"
        },
        { 
            "_id": "vec2", 
            "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.", 
            "category": "technology",
            "quarter": "Q4"
        },
        { 
            "_id": "vec3", 
            "chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
            "category": "technology",
            "quarter": "Q3"
        },
        { 
            "_id": "vec4", 
            "chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.", 
            "category": "technology",
            "quarter": "Q4"
        }
    ]
)

time.sleep(10) # Wait for the upserted vectors to be indexed
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index, 
// see https://docs.pinecone.io/guides/indexes/target-an-index
const namespace = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

// Upsert records into a namespace
// `chunk_text` fields are converted to sparse vectors
// `category` and `quarter` fields are stored as metadata
await namespace.upsertRecords({ records: [
    { 
        "_id": "vec1", 
        "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.", 
        "category": "technology",
        "quarter": "Q3"
    },
    { 
        "_id": "vec2", 
        "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.", 
        "category": "technology",
        "quarter": "Q4"
    },
    { 
        "_id": "vec3", 
        "chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
        "category": "technology",
        "quarter": "Q3"
    },
    { 
        "_id": "vec4", 
        "chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.", 
        "category": "technology",
        "quarter": "Q4"
    }
] });
```

```java Java theme={null}
import io.pinecone.clients.Index;
import io.pinecone.configs.PineconeConfig;
import io.pinecone.configs.PineconeConnection;
import org.openapitools.db_data.client.ApiException;

import java.util.*;

public class UpsertText {
    public static void main(String[] args) throws ApiException {
        PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);

        Index index = new Index(config, connection, "integrated-sparse-java");
        ArrayList<Map<String, String>> upsertRecords = new ArrayList<>();

        HashMap<String, String> record1 = new HashMap<>();
        record1.put("_id", "rec1");
        record1.put("category", "digestive system");
        record1.put("chunk_text", "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.");

        HashMap<String, String> record2 = new HashMap<>();
        record2.put("_id", "rec2");
        record2.put("category", "cultivation");
        record2.put("chunk_text", "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.");

        HashMap<String, String> record3 = new HashMap<>();
        record3.put("_id", "rec3");
        record3.put("category", "immune system");
        record3.put("chunk_text", "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.");

        HashMap<String, String> record4 = new HashMap<>();
        record4.put("_id", "rec4");
        record4.put("category", "endocrine system");
        record4.put("chunk_text", "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.");

        upsertRecords.add(record1);
        upsertRecords.add(record2);
        upsertRecords.add(record3);
        upsertRecords.add(record4);

        index.upsertRecords("example-namespace", upsertRecords);
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

    // Upsert records into a namespace
    // `chunk_text` fields are converted to sparse vectors
    // `category` and `quarter` fields are stored as metadata
	records := []*pinecone.IntegratedRecord{
		{
			"_id":        "vec1",
			"chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
			"category":   "technology",
			"quarter":    "Q3",
		},
		{
			"_id":        "vec2",
			"chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
			"category":   "technology",
			"quarter":    "Q4",
		},
		{
			"_id":        "vec3",
			"chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
			"category":   "technology",
			"quarter":    "Q3",
		},
		{
			"_id":        "vec4",
			"chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.",
			"category":   "technology",
			"quarter":    "Q4",
		},
	}

	err = idxConnection.UpsertRecords(ctx, records)
	if err != nil {
		log.Fatalf("Failed to upsert vectors: %v", err)
	}
}
```

```shell curl theme={null}
INDEX_HOST="INDEX_HOST"
NAMESPACE="YOUR_NAMESPACE"
PINECONE_API_KEY="YOUR_API_KEY"

curl  "https://$INDEX_HOST/records/namespaces/$NAMESPACE/upsert" \
    -H "Content-Type: application/x-ndjson" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{ "_id": "vec1", "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.", "category": "technology", "quarter": "Q3" }
      { "_id": "vec2", "chunk_text": "Analysts suggest that AAPL'\''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.", "category": "technology", "quarter": "Q4" }
      { "_id": "vec3", "chunk_text": "AAPL'\''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.", "category": "technology", "quarter": "Q3" }
      { "_id": "vec4", "chunk_text": "AAPL may consider healthcare integrations in Q4 to compete with tech rivals entering the consumer wellness space.", "category": "technology", "quarter": "Q4" }'
```
