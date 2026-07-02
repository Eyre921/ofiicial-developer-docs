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

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/knowledge-base/{documentation_id}/chunks:
    get:
      operationId: list
      summary: Get All Rag Chunks For A Document
      description: Get all RAG chunks for a specific knowledge base document.
      tags:
        - subpackage_conversationalAi/knowledgeBase/documents/chunks
      parameters:
        - name: documentation_id
          in: path
          description: >-
            The id of a document from the knowledge base. This is returned on
            document addition.
          required: true
          schema:
            type: string
        - name: embedding_model
          in: query
          description: The embedding model used to retrieve the chunk.
          required: true
          schema:
            $ref: '#/components/schemas/EmbeddingModelEnum'
        - name: page_size
          in: query
          description: >-
            How many documents to return at maximum. Can not exceed 100,
            defaults to 30.
          required: false
          schema:
            type: integer
            default: 30
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/KnowledgeBaseDocumentChunksResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
servers:
  - url: https://api.elevenlabs.io
    description: Production
  - url: https://api.us.elevenlabs.io
    description: Production US
  - url: https://api.eu.residency.elevenlabs.io
    description: Production EU
  - url: https://api.in.residency.elevenlabs.io
    description: Production India
  - url: https://api.sg.residency.elevenlabs.io
    description: Production Singapore
components:
  schemas:
    EmbeddingModelEnum:
      type: string
      enum:
        - e5_mistral_7b_instruct
        - multilingual_e5_large_instruct
      default: e5_mistral_7b_instruct
      title: EmbeddingModelEnum
    KnowledgeBaseDocumentChunkResponseModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        content:
          type: string
      required:
        - id
        - name
        - content
      title: KnowledgeBaseDocumentChunkResponseModel
    KnowledgeBaseDocumentChunksResponseModel:
      type: object
      properties:
        chunks:
          type: array
          items:
            $ref: '#/components/schemas/KnowledgeBaseDocumentChunkResponseModel'
        next_cursor:
          type:
            - string
            - 'null'
      required:
        - chunks
      title: KnowledgeBaseDocumentChunksResponseModel
    ValidationErrorLocItems:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItems
    ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/ValidationErrorLocItems'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
      title: HTTPValidationError

```

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
