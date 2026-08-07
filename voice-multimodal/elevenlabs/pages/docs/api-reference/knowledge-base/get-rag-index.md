---
title: "Get RAG index"
source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-rag-index.md
path: docs/api-reference/knowledge-base/get-rag-index
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get RAG index

GET https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}/rag-index

Provides information about all RAG indexes of the specified knowledgebase document.

Reference: https://elevenlabs.io/docs/api-reference/knowledge-base/get-rag-index

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `documentation_id` (string, required) — The id of a document from the knowledge base. This is returned on document addition.

## Response

### 200

Successful Response

- `indexes` (list of object, required)
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
  "indexes": [
    {
      "id": "string",
      "model": "e5_mistral_7b_instruct",
      "status": "new",
      "progress_percentage": 1.1,
      "document_model_index_usage": {
        "used_bytes": 1
      }
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.getDocumentRagIndexes("documentation_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.get_document_rag_indexes(
    documentation_id="documentation_id",
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index"

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index")! as URL,
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
