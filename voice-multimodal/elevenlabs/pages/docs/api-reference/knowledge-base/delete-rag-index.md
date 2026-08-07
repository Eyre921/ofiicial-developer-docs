---
title: "Delete RAG index"
source: https://elevenlabs.io/docs/api-reference/knowledge-base/delete-rag-index.md
path: docs/api-reference/knowledge-base/delete-rag-index
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Delete RAG index

DELETE https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}/rag-index/{rag_index_id}

Delete RAG index for the knowledgebase document.

Reference: https://elevenlabs.io/docs/api-reference/knowledge-base/delete-rag-index

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `documentation_id` (string, required) — The id of a document from the knowledge base. This is returned on document addition.
- `rag_index_id` (string, required) — The id of RAG index of document from the knowledge base.

## Response

### 200

Successful Response

- `id` (string, required)
- `model` (enum, required, default: e5_mistral_7b_instruct)
  - Allowed values: `e5_mistral_7b_instruct`, `multilingual_e5_large_instruct`
- `status` (enum, required)
  - Allowed values: `new`, `created`, `processing`, `failed`, `succeeded`, `rag_limit_exceeded`, `document_too_small`, `cannot_index_folder`
- `progress_percentage` (double, required)
- `document_model_index_usage` (object, required)
  - `used_bytes` (integer, required)

## Examples

**Response**

```json
{
  "id": "string",
  "model": "e5_mistral_7b_instruct",
  "status": "new",
  "progress_percentage": 1.1,
  "document_model_index_usage": {
    "used_bytes": 1
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.deleteDocumentRagIndex("documentation_id", "rag_index_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.delete_document_rag_index(
    documentation_id="documentation_id",
    rag_index_id="rag_index_id",
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index/rag_index_id"

	req, _ := http.NewRequest("DELETE", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index/rag_index_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index/rag_index_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index/rag_index_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index/rag_index_id");
var request = new RestRequest(Method.DELETE);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index/rag_index_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"

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
