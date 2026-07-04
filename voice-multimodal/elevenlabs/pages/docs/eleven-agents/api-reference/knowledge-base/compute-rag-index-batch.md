---
title: "Compute RAG index in batch"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/compute-rag-index-batch.md
path: docs/eleven-agents/api-reference/knowledge-base/compute-rag-index-batch
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Compute RAG index in batch

POST https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index
Content-Type: application/json

Retrieves and/or creates RAG indexes for multiple knowledge base documents in a single request. Maximum 100 items per request.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/compute-rag-index-batch

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/knowledge-base/rag-index:
    post:
      operationId: get_or_create_rag_indexes
      summary: Compute Rag Indexes In Batch
      description: >-
        Retrieves and/or creates RAG indexes for multiple knowledge base
        documents in a single request. Maximum 100 items per request.
      tags:
        - knowledgeBase
      parameters:
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
                type: object
                additionalProperties:
                  $ref: >-
                    #/components/schemas/type_conversationalAi/knowledgeBase:KnowledgeBaseGetOrCreateRagIndexesResponseValue
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                items:
                  type: array
                  items:
                    $ref: '#/components/schemas/type_:GetOrCreateRagIndexRequestModel'
                  description: List of requested RAG indexes. Minimum 1, maximum 100 items.
              required:
                - items
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
    type_:EmbeddingModelEnum:
      type: string
      enum:
        - e5_mistral_7b_instruct
        - multilingual_e5_large_instruct
      default: e5_mistral_7b_instruct
      title: EmbeddingModelEnum
    type_:GetOrCreateRagIndexRequestModel:
      type: object
      properties:
        document_id:
          type: string
          description: ID of the knowledgebase document for which to retrieve the index
        create_if_missing:
          type: boolean
          description: Whether to create the RAG index if it does not exist
        model:
          $ref: '#/components/schemas/type_:EmbeddingModelEnum'
          description: Embedding model to use for the RAG index
      required:
        - document_id
        - create_if_missing
        - model
      title: GetOrCreateRagIndexRequestModel
    type_:RagIndexStatus:
      type: string
      enum:
        - new
        - created
        - processing
        - failed
        - succeeded
        - rag_limit_exceeded
        - document_too_small
        - cannot_index_folder
      title: RagIndexStatus
    type_:RagDocumentIndexUsage:
      type: object
      properties:
        used_bytes:
          type: integer
      required:
        - used_bytes
      title: RagDocumentIndexUsage
    type_:RagDocumentIndexResponseModel:
      type: object
      properties:
        id:
          type: string
        model:
          $ref: '#/components/schemas/type_:EmbeddingModelEnum'
        status:
          $ref: '#/components/schemas/type_:RagIndexStatus'
        progress_percentage:
          type: number
          format: double
        document_model_index_usage:
          $ref: '#/components/schemas/type_:RagDocumentIndexUsage'
      required:
        - id
        - model
        - status
        - progress_percentage
        - document_model_index_usage
      title: RagDocumentIndexResponseModel
    type_conversationalAi/knowledgeBase:KnowledgeBaseGetOrCreateRagIndexesResponseValue:
      oneOf:
        - type: object
          properties:
            status:
              type: string
              enum:
                - success
              description: 'Discriminator value: success'
            data:
              $ref: '#/components/schemas/type_:RagDocumentIndexResponseModel'
          required:
            - status
            - data
        - type: object
          properties:
            status:
              type: string
              enum:
                - failure
              description: 'Discriminator value: failure'
            error_code:
              type: integer
            error_status:
              type: string
            error_message:
              type: string
          required:
            - status
            - error_code
            - error_status
            - error_message
      discriminator:
        propertyName: status
      title: KnowledgeBaseGetOrCreateRagIndexesResponseValue
    type_:ValidationErrorLocItem:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItem
    type_:ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationErrorLocItem'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    type_:HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationError'
      title: HTTPValidationError

```

## Examples

**Request**

```json
{
  "items": [
    {
      "document_id": "document_id",
      "create_if_missing": true,
      "model": "e5_mistral_7b_instruct"
    }
  ]
}
```

**Response**

```json
{
  "key": {
    "status": "success",
    "data": {
      "id": "id",
      "model": "e5_mistral_7b_instruct",
      "status": "new",
      "progress_percentage": 1.1,
      "document_model_index_usage": {
        "used_bytes": 1
      }
    }
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.getOrCreateRagIndexes({
        items: [
            {
                documentId: "document_id",
                createIfMissing: true,
                model: "e5_mistral_7b_instruct",
            },
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, GetOrCreateRagIndexRequestModel

client = ElevenLabs()

client.conversational_ai.knowledge_base.get_or_create_rag_indexes(
    items=[
        GetOrCreateRagIndexRequestModel(
            document_id="document_id",
            create_if_missing=True,
            model="e5_mistral_7b_instruct",
        )
    ],
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index"

	payload := strings.NewReader("{\n  \"items\": [\n    {\n      \"document_id\": \"document_id\",\n      \"create_if_missing\": true,\n      \"model\": \"e5_mistral_7b_instruct\"\n    }\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"items\": [\n    {\n      \"document_id\": \"document_id\",\n      \"create_if_missing\": true,\n      \"model\": \"e5_mistral_7b_instruct\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index")
  .header("Content-Type", "application/json")
  .body("{\n  \"items\": [\n    {\n      \"document_id\": \"document_id\",\n      \"create_if_missing\": true,\n      \"model\": \"e5_mistral_7b_instruct\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index', [
  'body' => '{
  "items": [
    {
      "document_id": "document_id",
      "create_if_missing": true,
      "model": "e5_mistral_7b_instruct"
    }
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"items\": [\n    {\n      \"document_id\": \"document_id\",\n      \"create_if_missing\": true,\n      \"model\": \"e5_mistral_7b_instruct\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["items": [
    [
      "document_id": "document_id",
      "create_if_missing": true,
      "model": "e5_mistral_7b_instruct"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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
