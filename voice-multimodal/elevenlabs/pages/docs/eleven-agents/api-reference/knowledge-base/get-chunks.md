---
title: "Get RAG chunks for a document"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/get-chunks.md
path: docs/eleven-agents/api-reference/knowledge-base/get-chunks
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get RAG chunks for a document

GET https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}/chunks

Get all RAG chunks for a specific knowledge base document.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/get-chunks

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
- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `chunks` (list of object, required)
  - `id` (string, required)
  - `name` (string, required)
  - `content` (string, required)
- `next_cursor` (string, optional)

## Examples

**Response**

```json
{
  "chunks": [
    {
      "id": "id",
      "name": "name",
      "content": "content"
    }
  ],
  "next_cursor": "next_cursor"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.documents.chunks.list("21m00Tcm4TlvDq8ikWAM", {
        cursor: "cursor",
        embeddingModel: "e5_mistral_7b_instruct",
        pageSize: 1,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.chunks.list(
    documentation_id="21m00Tcm4TlvDq8ikWAM",
    cursor="cursor",
    embedding_model="e5_mistral_7b_instruct",
    page_size=1,
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunks?cursor=cursor&embedding_model=e5_mistral_7b_instruct&page_size=1"

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunks?cursor=cursor&embedding_model=e5_mistral_7b_instruct&page_size=1")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunks?cursor=cursor&embedding_model=e5_mistral_7b_instruct&page_size=1")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunks?cursor=cursor&embedding_model=e5_mistral_7b_instruct&page_size=1');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunks?cursor=cursor&embedding_model=e5_mistral_7b_instruct&page_size=1");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/chunks?cursor=cursor&embedding_model=e5_mistral_7b_instruct&page_size=1")! as URL,
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
