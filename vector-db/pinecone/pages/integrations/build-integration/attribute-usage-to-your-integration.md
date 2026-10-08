---
title: "Attribute usage to your integration"
source: https://docs.pinecone.io/integrations/build-integration/attribute-usage-to-your-integration
path: integrations/build-integration/attribute-usage-to-your-integration
---

Learn how to set a source tag in the Pinecone SDKs or the API User-Agent header so that usage from your integration is attributed to it.

After you create your integration, specify a source tag when you create a client with a Pinecone SDK. If you call the API directly, pass the source tag in the `User-Agent` header.

<Note>
  Anyone can create an integration. To apply to become an official Pinecone partner, see [Integration ecosystem](/integrations/build-integration/integration-ecosystem).
</Note>

## Source tag naming conventions

Your source tag must follow these conventions:

* Clearly identify your integration.
* Use only lowercase letters, numbers, underscores, and colons.

For example, for an integration called "New Framework", `"new_framework"` is valid, but `"new framework"` and `"New_framework"` aren't.

## Specify a source tag

Source tags require these minimum SDK versions:

| Pinecone SDK | Required version |
| - | - |
| [Python](/reference/sdks/python/overview) | v3.2.1+ |
| [Node.js](/reference/sdks/node/overview) | v2.2.0+ |
| [Java](/reference/sdks/java/overview) | v1.0.0+ |
| [Go](/reference/sdks/go/overview) | v0.4.1+ |

Pass the source tag when you create the client, or in the `User-Agent` header with curl:

<CodeGroup>
  ```python Python theme={null}
  # REST client
  from pinecone import Pinecone

  pc = Pinecone(
      api_key="YOUR_API_KEY", 
      source_tag="YOUR_SOURCE_TAG"
  )

  # gRPC client
  from pinecone.grpc import PineconeGRPC

  pc = PineconeGRPC(
      api_key="YOUR_API_KEY", 
      source_tag="YOUR_SOURCE_TAG"
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ 
      apiKey: 'YOUR_API_KEY', 
      sourceTag: 'YOUR_SOURCE_TAG' 
  });
  ```

  ```java Java theme={null}
  import io.pinecone.clients.Pinecone;

  public class IntegrationExample {
      public static void main(String[] args) {
          Pinecone pc = new Pinecone.Builder("YOUR_API_KEY")
                  .withSourceTag("YOUR_SOURCE_TAG")
                  .build();
      }
  }
  ```

  ```go Go theme={null}
  import "github.com/pinecone-io/go-pinecone/v4/pinecone"

  client, err := pinecone.NewClient(pinecone.NewClientParams{
  	ApiKey: "YOUR_API_KEY",
  	SourceTag: "YOUR_SOURCE_TAG",
  })
  ```

  ```shell curl theme={null}
  curl -i -X GET "https://api.pinecone.io/indexes" \
    -H "Accept: application/json" \
    -H "Api-Key: YOUR_API_KEY" \
    -H "User-Agent: source_tag=YOUR_SOURCE_TAG" \
    -H "X-Pinecone-Api-Version: 2026-07"
  ```
</CodeGroup>
