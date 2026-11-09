---
title: "Create a legacy integrated index"
source: https://docs.pinecone.io/guides/legacy/records-api/create-an-integrated-index
path: guides/legacy/records-api/create-an-integrated-index
---

Create a legacy integrated index with create_index_for_model, so Pinecone embeds source text with a hosted model through the legacy Records API.

> [!NOTE]
>
> New projects should use the [Documents API](/guides/indexes/create-an-index#create-a-document-index). To move an existing index, see [Move to the Documents API](/guides/indexes/move-to-the-documents-api).

A legacy integrated index is created with `create_index_for_model` and served by the legacy Records API. Pinecone converts the source text you upsert and search with to vectors, using one hosted embedding model per index. To have Pinecone embed text in a document index instead, declare `embed` or `sparse_embed` on a `string` field. See [Integrated embedding](/guides/search/integrated-embedding).

> [!NOTE]
>
> Legacy integrated indexes (created with `create_index_for_model` and served by the legacy Records API) don't support [updating](/guides/data/update-data) or [importing](/guides/data/import-data) with text.

## Dense embedding

If you want to upsert and search with source text and have Pinecone convert it to dense vectors automatically, [create an index with integrated embedding](/reference/api/latest/control-plane/create_for_model) as follows:

* Provide a `name` for the index.
* Set `cloud` and `region` to the [cloud and region](/guides/indexes/index-configuration#cloud-regions) where the index should be deployed.
* Set `embed.model` to one of [Pinecone's hosted embedding models](/guides/indexes/index-configuration#embedding-models).
* Set `embed.field_map` to the name of the field in your source document that contains the data for embedding.

Other parameters are optional. See [Create an index with integrated embedding](/reference/api/latest/control-plane/create_for_model) for details.

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
import org.openapitools.db_control.client.model.CreateIndexForModelRequestEmbed;
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
                "aws",
                region,
                embed,
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

  	indexName := "integrated-dense-go"
   	deletionProtection := pinecone.DeletionProtectionDisabled

    idx, err := pc.CreateIndexForModel(ctx, &pinecone.CreateIndexForModelRequest{
		Name:   indexName,
		Cloud:  pinecone.CloudAWS,
		Region: "us-east-1",
		Embed: pinecone.CreateIndexForModelEmbed{
			Model:    "llama-text-embed-v2",
			FieldMap: map[string]interface{}{"text": "chunk_text"},
		},
        DeletionProtection: &deletionProtection,
        Tags:   &pinecone.IndexTags{ "environment": "development" },
	})
    if err != nil {
        log.Fatalf("Failed to create serverless integrated index: %v", err)
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
  --field-map "text=chunk_text" \
  --tags "environment=development"
```

## Sparse embedding

If you want to upsert and search with source text and have Pinecone convert it to sparse vectors automatically, [create an index with integrated embedding](/reference/api/latest/control-plane/create_for_model) as follows:

* Provide a `name` for the index.
* Set `cloud` and `region` to the [cloud and region](/guides/indexes/index-configuration#cloud-regions) where the index should be deployed.
* Set `embed.model` to one of [Pinecone's hosted sparse embedding models](/guides/indexes/index-configuration#embedding-models).
* Set `embed.field_map` to the name of the field in your source document that contains the text for embedding.
* If needed, `embed.read_parameters` and `embed.write_parameters` can be used to override the default model embedding behavior.

Other parameters are optional. See [Create an index with integrated embedding](/reference/api/latest/control-plane/create_for_model) for details.

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
import org.openapitools.db_control.client.model.CreateIndexForModelRequestEmbed;
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
                "aws",
                region,
                embed,
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

  	indexName := "integrated-sparse-go"
	deletionProtection := pinecone.DeletionProtectionDisabled

    idx, err := pc.CreateIndexForModel(ctx, &pinecone.CreateIndexForModelRequest{
		Name:   indexName,
		Cloud:  pinecone.CloudAWS,
		Region: "us-east-1",
		Embed: pinecone.CreateIndexForModelEmbed{
			Model:    "pinecone-sparse-english-v0",
			FieldMap: map[string]interface{}{"text": "chunk_text"},
		},
        DeletionProtection: &deletionProtection,
        Tags:   &pinecone.IndexTags{ "environment": "development" },

	})
    if err != nil {
        log.Fatalf("Failed to create serverless integrated index: %v", err)
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
  --field-map "text=chunk_text" \
  --tags "environment=development"
```

## Wait for the index to be ready

A new index can't accept data until its `status.ready` field is `true`. See [Wait for the index to be ready](/guides/indexes/create-an-index#wait-for-the-index-to-be-ready).
