---
title: "Get document chunk"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/get-chunk.md
path: docs/eleven-agents/api-reference/knowledge-base/get-chunk
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get document chunk

GET https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}/chunk/{chunk_id}

Get details about a specific documentation part used by RAG.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/get-chunk

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `documentation_id` (string, required) — The id of a document from the knowledge base. This is returned on document addition.
- `chunk_id` (string, required) — The id of a document RAG chunk from the knowledge base.

### Query parameters

- `embedding_model` (enum, optional, default: e5_mistral_7b_instruct) — The embedding model used to retrieve the chunk.
  - Allowed values: `e5_mistral_7b_instruct`, `multilingual_e5_large_instruct`

## Response

### 200

Successful Response

- `id` (string, required)
- `name` (string, required)
- `content` (string, required)

## Examples

**Response**

```json
{
  "id": "id",
  "name": "name",
  "content": "content"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.documents.chunk.get("21m00Tcm4TlvDq8ikWAM", "chunk_id", {
        embeddingModel: "e5_mistral_7b_instruct",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.chunk.get(
    documentation_id="21m00Tcm4TlvDq8ikWAM",
    chunk_id="chunk_id",
    embedding_model="e5_mistral_7b_instruct",
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/chunk_id?embedding_model=e5_mistral_7b_instruct"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/chunk_id?embedding_model=e5_mistral_7b_instruct")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/chunk_id?embedding_model=e5_mistral_7b_instruct")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/chunk_id?embedding_model=e5_mistral_7b_instruct');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/chunk_id?embedding_model=e5_mistral_7b_instruct");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunk/chunk_id?embedding_model=e5_mistral_7b_instruct")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```
