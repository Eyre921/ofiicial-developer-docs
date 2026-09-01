---
title: "Get RAG chunks for a document"
source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-chunks.md
path: docs/api-reference/knowledge-base/get-chunks
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get RAG chunks for a document

GET https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}/chunks

Get all RAG chunks for a specific knowledge base document.

Reference: https://elevenlabs.io/docs/api-reference/knowledge-base/get-chunks

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `documentation_id` (string, required) — The id of a document from the knowledge base. This is returned on document addition.

### Query parameters

- `embedding_model` (enum, required, default: e5_mistral_7b_instruct) — The embedding model used to retrieve the chunk.
  - Allowed values: `e5_mistral_7b_instruct`, `multilingual_e5_large_instruct`
- `page_size` (integer, optional, default: 30) — How many documents to return at maximum. Can not exceed 100, defaults to 30.
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `chunks` (list of object, required)
  - `id` (string, required)
  - `name` (string, required)
  - `content` (string, required)
- `next_cursor` (string, optional, nullable)

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "chunks": [
    {
      "id": "chunk_001",
      "name": "Introduction to Conversational AI",
      "content": "Conversational AI enables machines to understand, process, and respond to human language in a natural way, using techniques such as natural language processing and machine learning."
    },
    {
      "id": "chunk_002",
      "name": "Knowledge Base Document Structure",
      "content": "Each knowledge base document is divided into multiple chunks to facilitate efficient retrieval and context-aware responses during conversations."
    },
    {
      "id": "chunk_003",
      "name": "Embedding Models Overview",
      "content": "Embedding models convert text into numerical vectors that capture semantic meaning, enabling similarity search and retrieval in large datasets."
    }
  ],
  "next_cursor": "chunk_004"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        apiKey: "sk-1234567890abcdef1234567890abcdef",
    });
    await client.conversationalAi.knowledgeBase.documents.chunks.list("21m00Tcm4TlvDq8ikWAM", {
        embeddingModel: "e5_mistral_7b_instruct",
        pageSize: 30,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    api_key="sk-1234567890abcdef1234567890abcdef",
)

client.conversational_ai.knowledge_base.documents.chunks.list(
    documentation_id="21m00Tcm4TlvDq8ikWAM",
    embedding_model="e5_mistral_7b_instruct",
    page_size=30,
)

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunks?embedding_model=e5_mistral_7b_instruct&page_size=30"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("xi-api-key", "sk-1234567890abcdef1234567890abcdef")
	req.Header.Add("Content-Type", "application/json")

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunks?embedding_model=e5_mistral_7b_instruct&page_size=30")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'sk-1234567890abcdef1234567890abcdef'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunks?embedding_model=e5_mistral_7b_instruct&page_size=30")
  .header("xi-api-key", "sk-1234567890abcdef1234567890abcdef")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunks?embedding_model=e5_mistral_7b_instruct&page_size=30', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => 'sk-1234567890abcdef1234567890abcdef',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunks?embedding_model=e5_mistral_7b_instruct&page_size=30");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "sk-1234567890abcdef1234567890abcdef");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "sk-1234567890abcdef1234567890abcdef",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunks?embedding_model=e5_mistral_7b_instruct&page_size=30")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

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
