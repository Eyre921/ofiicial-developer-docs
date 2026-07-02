---
title: "Authentication"
source: https://docs.pinecone.io/reference/api/authentication
path: reference/api/authentication
---

Pinecone REST API: All requests to Pinecone APIs must contain a valid API key for the target project.

All requests to [Pinecone APIs](/reference/api/introduction) must contain a valid [API key](/guides/production/security-overview#api-keys) for the target project.

## Get an API key

[Create a new API key](https://app.pinecone.io/organizations/-/projects/-/keys) in the Pinecone console, or use the connect widget below to generate a key.

<div>
  <div>
    <div>
      <div />
    </div>
  </div>
</div>

Copy your generated key:

```
PINECONE_API_KEY="{{YOUR_API_KEY}}"

# This API key has ReadWrite access to all indexes in your project.
```

## Initialize a client

When using a [Pinecone SDK](/reference/pinecone-sdks), initialize a client object with your API key and then reuse the authenicated client in subsquent function calls. For example:

<CodeGroup>
  ```Python Python theme={null}
  from pinecone.grpc import PineconeGRPC as Pinecone
  from pinecone import ServerlessSpec

  pc = Pinecone(api_key='YOUR_API_KEY')

  # Creates an index using the API key stored in the client 'pc'.
  pc.create_index(
      name="docs-example",
      dimension=1536,
      metric="cosine",
      spec=ServerlessSpec(
          cloud='aws', 
          region='us-east-1'
      ) 
  ) 
  ```

  ```JavaScript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({
      apiKey: 'YOUR_API_KEY' 
  });

  // Creates an index using the API key stored in the client 'pc'.
  await pc.createIndex({
      name: 'docs-example',
      dimension: 1536,
      metric: 'cosine',
      spec: { 
          serverless: { 
              cloud: 'aws', 
              region: 'us-east-1' 
          }
      } 
  }) 
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;
  import org.openapitools.db_control.client.model.IndexModel;
  import org.openapitools.db_control.client.model.DeletionProtection;

  public class CreateServerlessIndexExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();

          // Creates an index using the API key stored in the client 'pc'.
          pc.createServerlessIndex("docs-example", "cosine", 1536, "aws", "us-east-1");
      }
  }
  ```

  ```go Go theme={null}
  package main

  import (
      "context"
      "fmt"
      "log"

      "github.com/pinecone-io/go-pinecone/v3/pinecone"
  )

  func main() {
      ctx := context.Background()

      pc, err := pinecone.NewClient(pinecone.NewClientParams{
          ApiKey: "YOUR_API_KEY",
      })
      if err != nil {
          log.Fatalf("Failed to create Client: %v", err)
      }

  	indexName := "docs-example"
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
      })
      if err != nil {
          log.Fatalf("Failed to create serverless index: %v", err)
      } else {
          fmt.Printf("Successfully created serverless index: %v", idx.Name)
      }
  }
  ```

  ```shell curl theme={null}
  curl -s "https://api.pinecone.io/indexes" \
      -H "Api-Key: YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -H "X-Pinecone-Api-Version: 2025-10" \
      -d '{
          "name":  "docs-example",
          "dimension": 1536,
          "metric": "cosine",
          "spec": {
              "serverless": {
                 "cloud":"aws",
                 "region": "us-east-1"
              }
          }
      }'
  ```
</CodeGroup>

## Add headers to an HTTP request

All HTTP requests to Pinecone APIs must contain an `Api-Key` header that specifies a valid [API key](/guides/production/security-overview#api-keys) and must be encoded as JSON with the `Content-Type: application/json` header. For example:

```shell curl theme={null}
curl https://api.pinecone.io/indexes \
   -H "Content-Type: application/json" \
   -H "Api-Key: $PINECONE_API_KEY" \
  -H "X-Pinecone-Api-Version: 2025-10" \
   -d '{
         "name":  "docs-example",
         "dimension": 1536,
         "metric": "cosine",
         "spec": {
            "serverless": {
               "cloud":"aws",
               "region": "us-east-1"
            }
         }
      }'
```

## Troubleshooting

<AccordionGroup>
  <Accordion title="Initialization errors due to outdated SDKs">
    Older versions of Pinecone required you to initialize a client with an `init` method that takes both `api_key` and `environment` parameters, for example:

    <CodeGroup>
      ```python Python theme={null}
      # Legacy initialization
      import pinecone

      pc = pinecone.init(
          api_key="PINECONE_API_KEY",
          environment="PINECONE_ENVIRONMENT"
      )
      ```

      ```javascript JavaScript theme={null}
      // Legacy initialization
      import { Pinecone } from '@pinecone-database/pinecone';

      const pineconeClient = new PineconeClient();
      await pineconeClient.init({
          apiKey: 'PINECONE_API_KEY',
          environment: 'PINECONE_ENVIRONMENT',
      });
      ```
    </CodeGroup>

    In more recent versions of Pinecone, this has changed. Initialization no longer requires an `init` step, and cloud environment is defined for each index rather than an entire project. Client initialization now only requires an `api_key` parameter, for example:

    <CodeGroup>
      ```python Python theme={null}
      # New initialization
      from pinecone import Pinecone

      pc = Pinecone(api_key="YOUR_API_KEY")
      ```

      ```javascript JavaScript theme={null}
      // New initialization
      import { Pinecone } from '@pinecone-database/pinecone';

      const pc = new Pinecone({
          apiKey: 'YOUR_API_KEY' 
      });
      ```
    </CodeGroup>

    If you are receiving errors about initialization, upgrade your [Pinecone SDK](/reference/pinecone-sdks) to the latest version, for example:

    <CodeGroup>
      ```shell Python theme={null}
      # Upgrade Pinecone SDK
      pip install pinecone --upgrade
      ```

      ```shell JavaScript theme={null}
      # Upgrade Pinecone SDK
      npm install @pinecone-database/pinecone@latest
      ```
    </CodeGroup>

    Also, note that some third-party tutorials and examples still reference the older initialization method. In such cases, follow the example above and the examples throughout the Pinecone documentation instead.
  </Accordion>
</AccordionGroup>
