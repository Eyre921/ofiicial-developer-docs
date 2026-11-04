---
title: "Search a legacy integrated index with text"
source: https://docs.pinecone.io/guides/legacy/records-api/search-with-text
path: guides/legacy/records-api/search-with-text
---

Search a legacy integrated index with query text through the legacy Records API, with dense or sparse embedding and optional metadata filters.

> [!NOTE]
>
> New projects should use the [Documents API](/guides/indexes/create-an-index#create-a-document-index). To move an existing index, see [Move to the Documents API](/guides/indexes/move-to-the-documents-api).

This page shows you how to search a legacy integrated index created with `create_index_for_model`. The legacy Records API converts the query text to a vector with the embedding model associated with the index. For a document index with [integrated embedding](/guides/search/integrated-embedding), see [Semantic search](/guides/search/semantic-search) and [Sparse-vector search](/guides/search/sparse-vector-search).

## Search with dense embedding

To search a legacy integrated index with query text, use the [Search with text](/reference/api/latest/data-plane/search_records) operation with the following parameters:

* The `namespace` to query. To use the default namespace, set the namespace to `"__default__"`.
* The `query.inputs.text` parameter with the query text. Pinecone uses the embedding model integrated with the index to convert the text to a dense vector automatically.
* The `query.top_k` parameter with the number of similar records to return.
* Optionally, the `fields` to return in the response. If you don't specify any, the response includes all fields.

For example, the following code searches for the 2 records most semantically related to the query text "Disease prevention":

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

results = index.search(
    namespace="example-namespace", 
    query={
        "inputs": {"text": "Disease prevention"}, 
        "top_k": 2
    },
    fields=["category", "chunk_text"]
)

print(results)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index, 
// see https://docs.pinecone.io/guides/indexes/target-an-index
const namespace = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

const response = await namespace.searchRecords({
  query: {
    topK: 2,
    inputs: { text: 'Disease prevention' },
  },
  fields: ['chunk_text', 'category'],
});

console.log(response);
```

```java Java theme={null}
import io.pinecone.clients.Index;
import io.pinecone.configs.PineconeConfig;
import io.pinecone.configs.PineconeConnection;
import org.openapitools.db_data.client.ApiException;
import org.openapitools.db_data.client.model.SearchRecordsResponse;

import java.util.*;

public class SearchText {
    public static void main(String[] args) throws ApiException {
        PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
        // To get the unique host for an index, 
        // see https://docs.pinecone.io/guides/indexes/target-an-index
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);

        Index index = new Index(config, connection, "integrated-dense-java");

        String query = "Disease prevention";
        List<String> fields = new ArrayList<>();
        fields.add("category");
        fields.add("chunk_text");

        // Search the index
        SearchRecordsResponse recordsResponse = index.searchRecordsByText(query,  "example-namespace", fields, 2, null, null);

        // Print the results
        System.out.println(recordsResponse);
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

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
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
    // see https://docs.pinecone.io/guides/indexes/target-an-index
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
    if err != nil {
        log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    } 

    res, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
        Query: pinecone.SearchRecordsQuery{
            TopK: 2,
            Inputs: &map[string]interface{}{
                "text": "Disease prevention",
            },
        },
        Fields: &[]string{"chunk_text", "category"},
    })
    if err != nil {
        log.Fatalf("Failed to search records: %v", err)
    }
    fmt.Println(prettifyStruct(res))
}
```

```bash curl theme={null}
INDEX_HOST="INDEX_HOST"
NAMESPACE="YOUR_NAMESPACE"
PINECONE_API_KEY="YOUR_API_KEY"

curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "query": {
            "inputs": {"text": "Disease prevention"},
            "top_k": 2
        },
        "fields": ["category", "chunk_text"]
     }'
```

In the response, each record has a similarity score that represents its distance to the query vector, calculated according to the index's [similarity metric](/guides/indexes/index-configuration#similarity-metrics):

```python Python theme={null}
{'result': {'hits': [{'_id': 'rec3',
                      '_score': 0.8204272389411926,
                      'fields': {'category': 'immune system',
                                 'chunk_text': 'Rich in vitamin C and other '
                                               'antioxidants, apples '
                                               'contribute to immune health '
                                               'and may reduce the risk of '
                                               'chronic diseases.'}},
                     {'_id': 'rec1',
                      '_score': 0.7931625843048096,
                      'fields': {'category': 'digestive system',
                                 'chunk_text': 'Apples are a great source of '
                                               'dietary fiber, which supports '
                                               'digestion and helps maintain a '
                                               'healthy gut.'}}]},
 'usage': {'embed_total_tokens': 8, 'read_units': 6}}
```

```javascript JavaScript theme={null}
{
  result: { 
    hits: [ 
      {
        _id: 'rec3',
        _score: 0.82042724,
        fields: {
          category: 'immune system',
          chunk_text: 'Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.'
        }
      },
      {
        _id: 'rec1',
        _score: 0.7931626,
        fields: {
          category: 'digestive system',
          chunk_text: 'Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.'
        }
      }
    ]
  },
  usage: { 
    readUnits: 6, 
    embedTotalTokens: 8 
  }
}
```

```java Java theme={null}
class SearchRecordsResponse {
    result: class SearchRecordsResponseResult {
        hits: [class Hit {
            id: rec3
            score: 0.8204272389411926
            fields: {category=immune system, chunk_text=Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.}
            additionalProperties: null
        }, class Hit {
            id: rec1
            score: 0.7931625843048096
            fields: {category=endocrine system, chunk_text=Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.}
            additionalProperties: null
        }]
        additionalProperties: null
    }
    usage: class SearchUsage {
        readUnits: 6
        embedTotalTokens: 13
    }
    additionalProperties: null
}
```

```go Go theme={null}
{
  "result": {
    "hits": [
      {
        "_id": "rec3",
        "_score": 0.82042724,
        "fields": {
          "category": "immune system",
          "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
        }
      },
      {
        "_id": "rec1",
        "_score": 0.7931626,
        "fields": {
          "category": "digestive system",
          "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
        }
      }
    ]
  },
  "usage": {
    "read_units": 6,
    "embed_total_tokens": 8
  }
}
```

```json curl theme={null}
 {
    "result": {
        "hits": [
            {
                "_id": "rec3",
                "_score": 0.82042724,
                "fields": {
                    "category": "immune system",
                    "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
                }
            },
            {
                "_id": "rec1",
                "_score": 0.7931626,
                "fields": {
                    "category": "digestive system",
                    "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut."
                }
            }
        ]
    },
    "usage": {
        "embed_total_tokens": 8,
        "read_units": 6
    }
}
```

## Search with sparse embedding

To search a legacy integrated index with query text, use the [Search with text](/reference/api/latest/data-plane/search_records) operation with the following parameters:

* `namespace`: The [namespace](/guides/indexes/indexing-overview#namespaces) to query. To use the default namespace, set to `"__default__"`.
* `query.inputs.text`:  The query text. Pinecone uses the [embedding model](/guides/indexes/index-configuration#embedding-models) integrated with the index to convert the text to a sparse vector automatically.
* `query.top_k`:  The number of records to return.
* `query.match_terms`: (Optional) A list of terms that must be present in each search result. For more details, see [Filter by required terms](#filter-by-required-terms).
* `fields`: (Optional) The fields to return in the response. If not specified, the response includes all fields.

For example, the following code converts the query "What is AAPL's outlook, considering both product launches and market conditions?" to a sparse vector and then searches for the 3 most similar vectors in the `example-namespace` namespace:

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

results = index.search(
    namespace="example-namespace", 
    query={
        "inputs": {"text": "What is AAPL's outlook, considering both product launches and market conditions?"}, 
        "top_k": 3
    },
    fields=["chunk_text", "quarter"]
)

print(results)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index, 
// see https://docs.pinecone.io/guides/indexes/target-an-index
const namespace = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

const response = await namespace.searchRecords({
  query: {
    topK: 3,
    inputs: { text: "What is AAPL's outlook, considering both product launches and market conditions?" },
  },
  fields: ['chunk_text', 'quarter']
});

console.log(response);
```

```java Java theme={null}
import io.pinecone.clients.Index;
import io.pinecone.configs.PineconeConfig;
import io.pinecone.configs.PineconeConnection;
import org.openapitools.db_data.client.ApiException;
import org.openapitools.db_data.client.model.SearchRecordsResponse;

import java.util.*;

public class SearchText {
    public static void main(String[] args) throws ApiException {
        PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
        // To get the unique host for an index, 
        // see https://docs.pinecone.io/guides/indexes/target-an-index
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);

        Index index = new Index(config, connection, "integrated-sparse-java");

        String query = "What is AAPL's outlook, considering both product launches and market conditions?";
        List<String> fields = new ArrayList<>();
        fields.add("quarter");
        fields.add("chunk_text");

        // Search the index
        SearchRecordsResponse recordsResponse = index.searchRecordsByText(query,  "example-namespace", fields, 3, null, null);

        // Print the results
        System.out.println(recordsResponse);
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

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
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
    // see https://docs.pinecone.io/guides/indexes/target-an-index
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
    if err != nil {
        log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    } 

    res, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
        Query: pinecone.SearchRecordsQuery{
            TopK: 3,
            Inputs: &map[string]interface{}{
                "text": "What is AAPL's outlook, considering both product launches and market conditions?",
            },
        },
        Fields: &[]string{"chunk_text", "quarter"},
    })
    if err != nil {
        log.Fatalf("Failed to search records: %v", err)
    }
    fmt.Println(prettifyStruct(res))
}
```

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/records/namespaces/example-namespace/search" \
  -H "Content-Type: application/json" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "query": {
          "inputs": { "text": "What is AAPL'\''s outlook, considering both product launches and market conditions?" },
          "top_k": 3
        },
        "fields": ["chunk_text", "quarter"]
    }'
```

The results look like this. The most similar records are scored highest.

```python Python theme={null}
{'result': {'hits': [{'_id': 'vec2',
                      '_score': 10.77734375,
                      'fields': {'chunk_text': "Analysts suggest that AAPL'''s "
                                               'upcoming Q4 product launch '
                                               'event might solidify its '
                                               'position in the premium '
                                               'smartphone market.',
                                 'quarter': 'Q4'}},
                     {'_id': 'vec3',
                      '_score': 6.49066162109375,
                      'fields': {'chunk_text': "AAPL'''s strategic Q3 "
                                               'partnerships with '
                                               'semiconductor suppliers could '
                                               'mitigate component risks and '
                                               'stabilize iPhone production.',
                                 'quarter': 'Q3'}},
                     {'_id': 'vec1',
                      '_score': 5.3671875,
                      'fields': {'chunk_text': 'AAPL reported a year-over-year '
                                               'revenue increase, expecting '
                                               'stronger Q3 demand for its '
                                               'flagship phones.',
                                 'quarter': 'Q3'}}]},
 'usage': {'embed_total_tokens': 18, 'read_units': 1}}
```

```javascript JavaScript theme={null}
{
  result: { 
    hits: [ 
      {
        _id: "vec2",
        _score: 10.82421875,
        fields: {
          chunk_text: "Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
          quarter: "Q4"
        }
      },
      {
        _id: "vec3",
        _score: 6.49066162109375,
        fields: {
          chunk_text: "AAPL'''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
          quarter: "Q3"
        }
      },
      {
        _id: "vec1",
        _score: 5.3671875,
        fields: {
          chunk_text: "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
          quarter: "Q3"
        }
      }
    ]
  },
  usage: { 
    readUnits: 1, 
    embedTotalTokens: 18 
  }
}
```

```java Java theme={null}
class SearchRecordsResponse {
    result: class SearchRecordsResponseResult {
        hits: [class Hit {
            id: vec2
            score: 10.82421875
            fields: {chunk_text=Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market., quarter=Q4}
            additionalProperties: null
        }, class Hit {
            id: vec3
            score: 6.49066162109375
            fields: {chunk_text=AAPL'''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production., quarter=Q3}
            additionalProperties: null
        }, class Hit {
            id: vec1
            score: 5.3671875
            fields: {chunk_text=AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones., quarter=Q3}
            additionalProperties: null
        }]
        additionalProperties: null
    }
    usage: class SearchUsage {
        readUnits: 1
        embedTotalTokens: 18
    }
    additionalProperties: null
}
```

```go Go theme={null}
{
  "result": {
    "hits": [
      {
        "_id": "vec2",
        "_score": 10.833984,
        "fields": {
          "chunk_text": "Analysts suggest that AAPL's upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
          "quarter": "Q4"
        }
      },
      {
        "_id": "vec3",
        "_score": 6.473572,
        "fields": {
          "chunk_text": "AAPL's strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
          "quarter": "Q3"
        }
      },
      {
        "_id": "vec1",
        "_score": 5.3710938,
        "fields": {
          "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
          "quarter": "Q3"
        }
      }
    ]
  },
  "usage": {
    "read_units": 6,
    "embed_total_tokens": 18
  }
}
```

```json curl theme={null}
{
  "result": {
    "hits": [
      {
        "_id": "vec2",
        "_score": 10.82421875,
        "fields": {
          "chunk_text": "Analysts suggest that AAPL'''s upcoming Q4 product launch event might solidify its position in the premium smartphone market.",
          "quarter": "Q4"
        }
      },
      {
        "_id": "vec3",
        "_score": 6.49066162109375,
        "fields": {
          "chunk_text": "AAPL'''s strategic Q3 partnerships with semiconductor suppliers could mitigate component risks and stabilize iPhone production.",
          "quarter": "Q3"
        }
      },
      {
        "_id": "vec1",
        "_score": 5.3671875,
        "fields": {
          "chunk_text": "AAPL reported a year-over-year revenue increase, expecting stronger Q3 demand for its flagship phones.",
          "quarter": "Q3"
        }
      }
    ]
  },
  "usage": {
    "embed_total_tokens": 18,
    "read_units": 1
  }
}
```

### Filter by required terms

> [!NOTE]
>
> This feature is in [public preview](/release-notes/feature-availability). See [limitations](#limitations) for details.

When searching a legacy integrated index with text, you can specify a list of terms that must be present in each sparse-vector search result. This is especially useful for:

* **Precision filtering**: Ensuring specific entities or concepts appear in results
* **Quality control**: Filtering out results that don't contain essential keywords
* **Domain-specific searches**: Requiring domain-specific terminology in results
* **Entity-based filtering**: Ensuring specific people, places, or things are mentioned

To filter by required terms, add `match_terms` to your query, specifying the `terms` to require and the `strategy` to use. `all` is the only supported strategy: every term must be present.

For example, the following request searches for records about Tesla's stock performance while ensuring both "Tesla" and "stock" appear in each result:

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

curl "https://$INDEX_HOST/records/namespaces/example-namespace/search" \
  -H "Content-Type: application/json" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "query": {
          "inputs": { "text": "What is the current outlook for Tesla stock performance?" },
          "top_k": 3,
          "match_terms": {
            "terms": ["Tesla", "stock"],
            "strategy": "all"
          }
        },
        "fields": ["chunk_text"]
    }'
```

The response includes only records that contain both "Tesla" and "stock":

```json theme={null}
{
  "result": {
    "hits": [
      {
        "_id": "tesla_q4_earnings",
        "_score": 9.82421875,
        "fields": {
          "chunk_text": "Tesla stock surged 8% in after-hours trading following strong Q4 earnings that exceeded analyst expectations. The company reported record vehicle deliveries and improved profit margins."
        }
      },
      {
        "_id": "tesla_competition_analysis",
        "_score": 7.49066162109375,
        "fields": {
          "chunk_text": "Tesla stock faces increasing competition from traditional automakers entering the electric vehicle market. However, analysts maintain that Tesla's technological lead and brand recognition provide significant advantages."
        }
      },
      {
        "_id": "tesla_production_update",
        "_score": 6.3671875,
        "fields": {
          "chunk_text": "Tesla stock performance is closely tied to production capacity at its Gigafactories. Recent expansion announcements suggest the company is positioning for continued growth in global markets."
        }
      }
    ]
  },
  "usage": {
    "embed_total_tokens": 18,
    "read_units": 1
  }
}
```

Without the `match_terms` filter, you might get results like:

* "Tesla cars are popular in California" (mentions Tesla but not stock)
* "Stock market volatility affects tech companies" (mentions stock but not Tesla)
* "Electric vehicle sales are growing" (neither Tesla nor stock)

#### Limitations

* **Legacy integrated indexes only**: Filtering by required terms is supported only for legacy integrated indexes that use [`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0). In a document index, use a [`$match_all` filter](/guides/search/filter-by-metadata#text-match-filters) instead.
* **Post-processing filter**: The filtering happens after the initial query, so potential matches that weren't included in the initial `top_k` results won't appear in the final results.
* **No phrase matching**: Terms are matched individually in any order and location.
* **No case-sensitivity**: Terms are normalized during processing.

## Search with a metadata filter

The following code searches for the 3 records that are most semantically similar to a query and that have a `category` metadata field with the value `digestive system`. For the supported operators, see [Metadata filter expressions](/guides/search/filter-by-metadata#metadata-filter-expressions).

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index, 
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST")

filtered_results = index.search(
    namespace="example-namespace", 
    query={
        "inputs": {"text": "Disease prevention"}, 
        "top_k": 3,
        "filter": {"category": "digestive system"},
    },
    fields=["category", "chunk_text"]
)

print(filtered_results)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone'

const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

// To get the unique host for an index, 
// see https://docs.pinecone.io/guides/indexes/target-an-index
const namespace = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

const response = await namespace.searchRecords({
  query: {
    topK: 3,
    inputs: { text: "Disease prevention" },
    filter: { category: "digestive system" }
  },
  fields: ['chunk_text', 'category']
});

console.log(response);
```

```java Java theme={null}
import io.pinecone.clients.Index;
import io.pinecone.configs.PineconeConfig;
import io.pinecone.configs.PineconeConnection;
import org.openapitools.db_data.client.ApiException;
import org.openapitools.db_data.client.model.SearchRecordsResponse;

import java.util.*;

public class SearchText {
    public static void main(String[] args) throws ApiException {
        PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
        // To get the unique host for an index, 
        // see https://docs.pinecone.io/guides/indexes/target-an-index
        config.setHost("INDEX_HOST");
        PineconeConnection connection = new PineconeConnection(config);

        Index index = new Index(config, connection, "integrated-dense-java");

        String query = "Disease prevention";
        List<String> fields = new ArrayList<>();
        fields.add("category");
        fields.add("chunk_text");

        Map<String, Object> filter = new HashMap<>();
        filter.put("category", "digestive system");

        // Search the index
        SearchRecordsResponse recordsResponse = index.searchRecordsByText(query,  "example-namespace", fields, 3, filter, null);

        // Print the results
        System.out.println(recordsResponse);
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

    "github.com/pinecone-io/go-pinecone/v7/pinecone"
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
    // see https://docs.pinecone.io/guides/indexes/target-an-index
    idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
    if err != nil {
        log.Fatalf("Failed to create IndexConnection for Host: %v", err)
    } 

    metadataMap := map[string]interface{}{
        "category": map[string]interface{}{
            "$eq": "digestive system",
        },
    }
    res, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
        Query: pinecone.SearchRecordsQuery{
            TopK: 3,
            Inputs: &map[string]interface{}{
                "text": "Disease prevention",
            },
            Filter: &metadataMap,
        },
        Fields: &[]string{"chunk_text", "category"},
    })
    if err != nil {
        log.Fatalf("Failed to search records: %v", err)
    }
    fmt.Printf(prettifyStruct(res))
}
```

```shell curl theme={null}
INDEX_HOST="INDEX_HOST"
NAMESPACE="YOUR_NAMESPACE"
PINECONE_API_KEY="YOUR_API_KEY"

curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2026-07" \
  -d '{
        "query": {
            "inputs": {"text": "Disease prevention"},
            "top_k": 3,
            "filter": {"category": "digestive system"}
        },
        "fields": ["category", "chunk_text"]
     }'
```
