---
title: "Create an index"
source: https://docs.pinecone.io/guides/index-data/create-an-index
path: guides/index-data/create-an-index
---

Create a Pinecone serverless index for full-text (BM25), semantic (dense vector), sparse-vector, or hybrid search with a document schema.

A Pinecone index can hold any combination of the following:

* **Documents** are the unit of data in an index with a document schema — JSON records whose ranking fields are indexed according to a schema you declare at index creation. An index with a document schema can mix `dense_vector`, `sparse_vector`, and FTS-enabled `string` ranking fields in the same record, alongside any number of metadata fields (auto-indexed at upsert time). Use documents for [full-text search](/guides/search/full-text-search) (BM25 ranking on `string` fields with `full_text_search` enabled), and to combine multiple scoring methods on the same data via `score_by`.

* **Dense vectors** are numerical representations of the meaning and relationships of text, images, or other data. Indexes of dense vectors are used for [semantic search](/guides/search/semantic-search), or together with sparse vectors for [hybrid search](/guides/search/hybrid-search).

* **Sparse vectors** are high-dimensional vectors with mostly zero values, produced by a sparse embedding model such as [`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0). Indexes of sparse vectors are used for [sparse-vector search](/guides/search/lexical-search), or together with dense vectors for [hybrid search](/guides/search/hybrid-search).

<Tip>
  You can create an index using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/create-index/serverless).
</Tip>

For index naming rules, available cloud regions, similarity metrics, and hosted embedding models, see [Index configuration](/guides/index-data/index-configuration).

## Create an index for full-text search

An index with a document schema stores typed JSON documents. The schema declares how each ranking field is indexed: as a `string` field with `full_text_search` enabled for BM25 ranking, a `dense_vector` for ANN similarity, or a `sparse_vector`. A single index can mix all three ranking field types; at query time, pick the ranking signal with `score_by`. Metadata fields (anything else you upsert) aren't declared in the schema — they're auto-indexed for filtering at upsert time.

<Note>
  Full-text search isn't integrated embedding. A `string` field with `full_text_search` is indexed for BM25 ranking and Lucene queries. It doesn't call an embedding model. Integrated embedding remains available for vector indexes.
</Note>

Indexes with document schemas use API version `2026-07`, supported through REST and the Python (v10 or later), Node.js (v9 or later), and Go (v7 or later) SDKs. For other languages, call the REST endpoint directly.

### Minimal: BM25 on a single text field

The example below creates an `articles` index whose `body` field is indexed for BM25 ranking. Other fields included at upsert time are stored on each document and auto-indexed for filtering as metadata.

<CodeGroup>
  ```python Python theme={null}
  import os
  from pinecone import Pinecone, SchemaBuilder

  pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

  schema = (
      SchemaBuilder()
        .add_string_field(name="body", full_text_search={})
        .build()
  )

  pc.indexes.create(name="articles", schema=schema)
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X POST "https://api.pinecone.io/indexes" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "name": "articles",
      "deployment": {
        "deployment_type": "managed",
        "cloud": "aws",
        "region": "us-east-1"
      },
      "schema": {
        "fields": {
          "body": {
            "type": "string",
            "full_text_search": {}
          }
        }
      }
    }'
  ```
</CodeGroup>

### Multi-field schema: BM25 + dense vector

A single index with a document schema can hold FTS-enabled `string` and `dense_vector` ranking fields together (the same schema can also include a `sparse_vector` field). A single search request ranks by one scoring type — multi-field BM25 is supported (multiple `text` clauses on different fields, or one `query_string` clause spanning fields), and any scoring method can be combined with metadata filters, including text-match filters (`$match_phrase`, `$match_all`, `$match_any`) on FTS-enabled `string` fields.

<CodeGroup>
  ```python Python theme={null}
  import os
  from pinecone import Pinecone, SchemaBuilder

  pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

  schema = (
      SchemaBuilder()
        .add_string_field(name="title", full_text_search={})
        .add_string_field(name="body", full_text_search={})
        .add_dense_vector_field(name="embedding", dimension=1536, metric="cosine")
        .build()
  )

  pc.indexes.create(name="articles-multi", schema=schema)
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X POST "https://api.pinecone.io/indexes" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
      "name": "articles-multi",
      "deployment": {
        "deployment_type": "managed",
        "cloud": "aws",
        "region": "us-east-1"
      },
      "schema": {
        "fields": {
          "title":    { "type": "string", "full_text_search": {} },
          "body":     { "type": "string", "full_text_search": {} },
          "embedding":{ "type": "dense_vector", "dimension": 1536, "metric": "cosine" }
        }
      }
    }'
  ```
</CodeGroup>

You can include additional fields (for example, `category` or `year`) at upsert time. All metadata fields are automatically indexed for filtering — they don't need to be declared in the schema. The schema is for ranking fields only; declaring a metadata-only field (`string` without `full_text_search`, `string_list`, `float`, or `boolean`) is rejected at index creation. To index only the metadata fields you filter on, see [Configure metadata indexing](/guides/index-data/configure-metadata-indexing).

For the full schema reference (all field types, language and analyzer options, dedicated read capacity, and Python SDK examples), see [Full-text search](/guides/search/full-text-search).

<Warning>
  Schema migration is not yet supported. Once an index with a document schema is created, you can't add, remove, or modify fields. Plan your schema carefully — if you need to change a schema, [delete the index](/guides/manage-data/manage-indexes#delete-an-index) and create a new one.
</Warning>

## Create an index for dense vectors

You can create an index that stores dense vectors with [integrated vector embedding](/guides/index-data/indexing-overview#integrated-embedding), or one that stores vectors generated with an external embedding model.

### Integrated embedding

<Note>
  Indexes with integrated embedding don't support [updating](/guides/manage-data/update-data) or [importing](/guides/index-data/import-data) with text.
</Note>

If you want to upsert and search with source text and have Pinecone convert it to dense vectors automatically, [create an index with integrated embedding](/reference/api/latest/control-plane/create_for_model) as follows:

* Provide a `name` for the index.
* Set `cloud` and `region` to the [cloud and region](/guides/index-data/index-configuration#cloud-regions) where the index should be deployed.
* Set `embed.model` to one of [Pinecone's hosted embedding models](/guides/index-data/index-configuration#embedding-models).
* Set `embed.field_map` to the name of the field in your source document that contains the data for embedding.

Other parameters are optional. See the [API reference](/reference/api/latest/control-plane/create_for_model) for details.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index_name = "integrated-dense-py"

  if not pc.has_index(index_name):
      pc.create_index_for_model(
          name=index_name,
          cloud="aws",
          region="us-east-1",
          embed={
              "model":"llama-text-embed-v2",
              "field_map":{"text": "chunk_text"}
          }
      )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.createIndexForModel({
    name: 'integrated-dense-js',
    cloud: 'aws',
    region: 'us-east-1',
    embed: {
      model: 'llama-text-embed-v2',
      fieldMap: { text: 'chunk_text' },
    },
    waitUntilReady: true,
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.CreateIndexForModelRequest;
  import org.openapitools.db_control.client.model.CreateIndexForModelRequestEmbed;
  import org.openapitools.db_control.client.model.DeletionProtection;
  import java.util.HashMap;
  import java.util.Map;

  public class CreateIntegratedIndex {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          String indexName = "integrated-dense-java";
          String region = "us-east-1";
          HashMap<String, String> fieldMap = new HashMap<>();
          fieldMap.put("text", "chunk_text");
          CreateIndexForModelRequestEmbed embed = new CreateIndexForModelRequestEmbed()
                  .model("llama-text-embed-v2")
                  .fieldMap(fieldMap);
          Map<String, String> tags = new HashMap<>();
          tags.put("environment", "development");
          pc.createIndexForModel(
                  indexName,
                  CreateIndexForModelRequest.CloudEnum.AWS,
                  region,
                  embed,
                  DeletionProtection.DISABLED,
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

    	indexName := "integrated-dense-go"
     	deletionProtection := pinecone.DeletionProtectionDisabled

      idx, err := pc.CreateIndexForModel(ctx, &pinecone.CreateIndexForModelRequest{
  		Name:   indexName,
  		Cloud:  pinecone.Aws,
  		Region: "us-east-1",
  		Embed: pinecone.CreateIndexForModelEmbed{
  			Model:    "llama-text-embed-v2",
  			FieldMap: map[string]interface{}{"text": "chunk_text"},
  		},
          DeletionProtection: &deletionProtection,
          Tags:   &pinecone.IndexTags{ "environment": "development" },
  	})
      if err != nil {
          log.Fatalf("Failed to create serverless integrated index: %v", idx.Name)
      } else {
          fmt.Printf("Successfully created serverless integrated index: %v", idx.Name)
      }
  }
  ```

  ```json curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X POST "https://api.pinecone.io/indexes/create-for-model" \
       -H "Content-Type: application/json" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-Api-Version: 2026-07" \
       -d '{
             "name": "integrated-dense-curl",
             "cloud": "aws",
             "region": "us-east-1",
             "embed": {
               "model": "llama-text-embed-v2",
               "field_map": {
                 "text": "chunk_text"
               }
             }
           }'
  ```

  ```bash CLI theme={null}
  # Target the project where you want to create the index.
  pc target -o "example-org" -p "example-project"
  # Create the index.
  pc index create \
    --name "integrated-dense-cli" \
    --metric "cosine" \
    --cloud "aws" \
    --region "us-east-1" \
    --model "llama-text-embed-v2" \
    --field_map "text=chunk_text" \
    --tags "environment=development"
  ```
</CodeGroup>

### Bring your own vectors

If you use an external embedding model to convert your data to dense vectors, [create an index](/reference/api/2026-04/control-plane/create_index) as follows:

* Provide a `name` for the index.
* Set the `vector_type` to `dense`.
* Specify the `dimension` and similarity `metric` of the vectors you'll store in the index. This should match the dimension and metric supported by your embedding model.
* Set `spec.cloud` and `spec.region` to the [cloud and region](/guides/index-data/index-configuration#cloud-regions) where the index should be deployed. For Python, you also need to import the `ServerlessSpec` class.

Other parameters are optional. See the [API reference](/reference/api/2026-04/control-plane/create_index) for details.

<CodeGroup>
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
  import org.openapitools.db_control.client.model.IndexModel;
  import org.openapitools.db_control.client.model.DeletionProtection;
  import java.util.HashMap;

  public class CreateServerlessIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          String indexName = "standard-dense-java";
          String cloud = "aws";
          String region = "us-east-1";
          String vectorType = "dense";
          Map<String, String> tags = new HashMap<>();
          tags.put("environment", "development");
          pc.createServerlessIndex(
              indexName,
              "cosine", 
              1536, 
              cloud,
              region,
              DeletionProtection.DISABLED, 
              tags, 
              vectorType
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

      // Serverless index
    	indexName := "standard-dense-go"
  	vectorType := "dense"
      dimension := int32(1536)
      metric := pinecone.Cosine
  	deletionProtection := pinecone.DeletionProtectionDisabled

      idx, err := pc.CreateServerlessIndex(ctx, &pinecone.CreateServerlessIndexRequest{
          Name:               indexName,
          VectorType:         &vectorType,
          Dimension:          &dimension,
          Metric:             &metric,
          Cloud:              pinecone.Aws,
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
    --vector_type "dense" \
    --dimension 1536 \
    --metric "cosine" \
    --cloud "aws" \
    --region "us-east-1" \
    --tags "environment=development" \
    --deletion_protection "disabled"
  ```
</CodeGroup>

## Create an index for sparse vectors

You can create an index that stores sparse vectors with [integrated vector embedding](/guides/index-data/indexing-overview#integrated-embedding), or one that stores vectors generated with an external embedding model.

### Integrated embedding

If you want to upsert and search with source text and have Pinecone convert it to sparse vectors automatically, [create an index with integrated embedding](/reference/api/latest/control-plane/create_for_model) as follows:

* Provide a `name` for the index.
* Set `cloud` and `region` to the [cloud and region](/guides/index-data/index-configuration#cloud-regions) where the index should be deployed.
* Set `embed.model` to one of [Pinecone's hosted sparse embedding models](/guides/index-data/index-configuration#embedding-models).
* Set `embed.field_map` to the name of the field in your source document that contains the text for embedding.
* If needed, `embed.read_parameters` and `embed.write_parameters` can be used to override the default model embedding behavior.

Other parameters are optional. See the [API reference](/reference/api/latest/control-plane/create_for_model) for details.

<CodeGroup>
  ```python Python theme={null}
  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  index_name = "integrated-sparse-py"

  if not pc.has_index(index_name):
      pc.create_index_for_model(
          name=index_name,
          cloud="aws",
          region="us-east-1",
          embed={
              "model":"pinecone-sparse-english-v0",
              "field_map":{"text": "chunk_text"}
          }
      )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.createIndexForModel({
    name: 'integrated-sparse-js',
    cloud: 'aws',
    region: 'us-east-1',
    embed: {
      model: 'pinecone-sparse-english-v0',
      fieldMap: { text: 'chunk_text' },
    },
    waitUntilReady: true,
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.ApiException;
  import org.openapitools.db_control.client.model.CreateIndexForModelRequest;
  import org.openapitools.db_control.client.model.CreateIndexForModelRequestEmbed;
  import org.openapitools.db_control.client.model.DeletionProtection;
  import java.util.HashMap;
  import java.util.Map;

  public class CreateIntegratedIndex {
      public static void main(String[] args) throws ApiException {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
          String indexName = "integrated-sparse-java";
          String region = "us-east-1";
          HashMap<String, String> fieldMap = new HashMap<>();
          fieldMap.put("text", "chunk_text");
          CreateIndexForModelRequestEmbed embed = new CreateIndexForModelRequestEmbed()
                  .model("pinecone-sparse-english-v0")
                  .fieldMap(fieldMap);
          Map<String, String> tags = new HashMap<>();
          tags.put("environment", "development");
          pc.createIndexForModel(
                  indexName,
                  CreateIndexForModelRequest.CloudEnum.AWS,
                  region,
                  embed,
                  DeletionProtection.DISABLED,
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

    	indexName := "integrated-sparse-go"
  	deletionProtection := pinecone.DeletionProtectionDisabled

      idx, err := pc.CreateIndexForModel(ctx, &pinecone.CreateIndexForModelRequest{
  		Name:   indexName,
  		Cloud:  pinecone.Aws,
  		Region: "us-east-1",
  		Embed: pinecone.CreateIndexForModelEmbed{
  			Model:    "pinecone-sparse-english-v0",
  			FieldMap: map[string]interface{}{"text": "chunk_text"},
  		},
          DeletionProtection: &deletionProtection,
          Tags:   &pinecone.IndexTags{ "environment": "development" },

  	})
      if err != nil {
          log.Fatalf("Failed to create serverless integrated index: %v", idx.Name)
      } else {
          fmt.Printf("Successfully created serverless integrated index: %v", idx.Name)
      }
  }
  ```

  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X POST "https://api.pinecone.io/indexes/create-for-model" \
       -H "Content-Type: application/json" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-Api-Version: 2026-07" \
       -d '{
             "name": "integrated-sparse-curl",
             "cloud": "aws",
             "region": "us-east-1",
             "embed": {
               "model": "pinecone-sparse-english-v0",
               "field_map": {
                 "text": "chunk_text"
               }
             }
           }'
  ```

  ```bash CLI theme={null}
  # Target the project where you want to create the index.
  pc target -o "example-org" -p "example-project"
  # Create the index.
  pc index create \
    --name "integrated-sparse-cli" \
    --cloud "aws" \
    --region "us-east-1" \
    --model "pinecone-sparse-english-v0" \
    --field_map "text=chunk_text" \
    --tags "environment=development"
  ```
</CodeGroup>

### Bring your own vectors

If you use an external embedding model to convert your data to sparse vectors, [create an index](/reference/api/2026-04/control-plane/create_index) as follows:

* Provide a `name` for the index.
* Set the `vector_type` to `sparse`.
* Set the distance `metric` to `dotproduct`. Indexes that store sparse vectors don't support other [distance metrics](/guides/index-data/indexing-overview#distance-metrics).
* Set `spec.cloud` and `spec.region` to the cloud and region where the index should be deployed.

Other parameters are optional. See the [API reference](/reference/api/2026-04/control-plane/create_index) for details.

<CodeGroup>
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
  import org.openapitools.db_control.client.model.DeletionProtection;

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
                  DeletionProtection.DISABLED,
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

  	indexName := "standard-sparse-go"
  	vectorType := "sparse"
  	metric := pinecone.Dotproduct
  	deletionProtection := pinecone.DeletionProtectionDisabled

  	idx, err := pc.CreateServerlessIndex(ctx, &pinecone.CreateServerlessIndexRequest{
  		Name:               indexName,
  		Metric:             &metric,
  		VectorType:         &vectorType,
  		Cloud:              pinecone.Aws,
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
    --vector_type "sparse" \
    --metric "dotproduct" \
    --cloud "aws" \
    --region "us-east-1" \
    --tags "environment=development"
  ```
</CodeGroup>

## Wait for the index to be ready

A new index of any type can't accept data until its `status.ready` field is `true`. The Python SDK waits for this by default, and the Node.js SDK waits when you pass `waitUntilReady: true`. If you call the API directly, [describe the index](/guides/manage-data/manage-indexes#describe-an-index) repeatedly until `status.ready` is `true`, then upsert.

## Create an index from a backup

You can restore an index from a backup, regardless of whether it stores dense or sparse vectors. For more details, see [Restore an index](/guides/manage-data/restore-an-index).
