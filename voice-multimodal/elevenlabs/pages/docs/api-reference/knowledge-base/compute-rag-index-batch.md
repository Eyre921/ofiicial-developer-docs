---
title: "Compute RAG index in batch"
source: https://elevenlabs.io/docs/api-reference/knowledge-base/compute-rag-index-batch.md
path: docs/api-reference/knowledge-base/compute-rag-index-batch
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Compute RAG index in batch

POST https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index
Content-Type: application/json

Retrieves and/or creates RAG indexes for multiple knowledge base documents in a single request. Maximum 100 items per request.

Reference: https://elevenlabs.io/docs/api-reference/knowledge-base/compute-rag-index-batch

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
                    #/components/schemas/V1ConvaiKnowledgeBaseRagIndexPostResponsesContentApplicationJsonSchema
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Compute_RAG_indexes_in_batch_v1_convai_knowledge_base_rag_index_post
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
    GetOrCreateRAGIndexRequestModel:
      type: object
      properties:
        document_id:
          type: string
          description: ID of the knowledgebase document for which to retrieve the index
        create_if_missing:
          type: boolean
          description: Whether to create the RAG index if it does not exist
        model:
          $ref: '#/components/schemas/EmbeddingModelEnum'
          description: Embedding model to use for the RAG index
      required:
        - document_id
        - create_if_missing
        - model
      title: GetOrCreateRAGIndexRequestModel
    Body_Compute_RAG_indexes_in_batch_v1_convai_knowledge_base_rag_index_post:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/GetOrCreateRAGIndexRequestModel'
          description: List of requested RAG indexes. Minimum 1, maximum 100 items.
      required:
        - items
      title: >-
        Body_Compute_RAG_indexes_in_batch_v1_convai_knowledge_base_rag_index_post
    RAGIndexStatus:
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
      title: RAGIndexStatus
    RAGDocumentIndexUsage:
      type: object
      properties:
        used_bytes:
          type: integer
      required:
        - used_bytes
      title: RAGDocumentIndexUsage
    RAGDocumentIndexResponseModel:
      type: object
      properties:
        id:
          type: string
        model:
          $ref: '#/components/schemas/EmbeddingModelEnum'
        status:
          $ref: '#/components/schemas/RAGIndexStatus'
        progress_percentage:
          type: number
          format: double
        document_model_index_usage:
          $ref: '#/components/schemas/RAGDocumentIndexUsage'
      required:
        - id
        - model
        - status
        - progress_percentage
        - document_model_index_usage
      title: RAGDocumentIndexResponseModel
    V1ConvaiKnowledgeBaseRagIndexPostResponsesContentApplicationJsonSchema:
      oneOf:
        - type: object
          properties:
            status:
              type: string
              enum:
                - success
              description: 'Discriminator value: success'
            data:
              $ref: '#/components/schemas/RAGDocumentIndexResponseModel'
          required:
            - status
            - data
          description: RAGIndexBatchSuccessfulResponseModel variant
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
          description: BatchFailureResponseModel variant
      discriminator:
        propertyName: status
      title: V1ConvaiKnowledgeBaseRagIndexPostResponsesContentApplicationJsonSchema
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
{
  "items": [
    {
      "document_id": "string",
      "create_if_missing": true,
      "model": "e5_mistral_7b_instruct"
    }
  ]
}
```

**Response**

```json
{}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.getOrCreateRagIndexes({
        items: [
            {
                documentId: "string",
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
            document_id="string",
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

	payload := strings.NewReader("{\n  \"items\": [\n    {\n      \"document_id\": \"string\",\n      \"create_if_missing\": true,\n      \"model\": \"e5_mistral_7b_instruct\"\n    }\n  ]\n}")

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
request.body = "{\n  \"items\": [\n    {\n      \"document_id\": \"string\",\n      \"create_if_missing\": true,\n      \"model\": \"e5_mistral_7b_instruct\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index")
  .header("Content-Type", "application/json")
  .body("{\n  \"items\": [\n    {\n      \"document_id\": \"string\",\n      \"create_if_missing\": true,\n      \"model\": \"e5_mistral_7b_instruct\"\n    }\n  ]\n}")
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
      "document_id": "string",
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
request.AddParameter("application/json", "{\n  \"items\": [\n    {\n      \"document_id\": \"string\",\n      \"create_if_missing\": true,\n      \"model\": \"e5_mistral_7b_instruct\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["items": [
    [
      "document_id": "string",
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
