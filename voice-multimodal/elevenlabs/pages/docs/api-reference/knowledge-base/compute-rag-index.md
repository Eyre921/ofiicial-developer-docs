---
title: "Compute RAG index"
source: https://elevenlabs.io/docs/api-reference/knowledge-base/compute-rag-index.md
path: docs/api-reference/knowledge-base/compute-rag-index
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Compute RAG index

POST https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}/rag-index
Content-Type: application/json

In case the document is not RAG indexed, it triggers rag indexing task, otherwise it just returns the current status.

Reference: https://elevenlabs.io/docs/api-reference/knowledge-base/compute-rag-index

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/knowledge-base/{documentation_id}/rag-index:
    post:
      operationId: compute_rag_index
      summary: Compute Rag Index.
      description: >-
        In case the document is not RAG indexed, it triggers rag indexing task,
        otherwise it just returns the current status.
      tags:
        - subpackage_conversationalAi/knowledgeBase/document
      parameters:
        - name: documentation_id
          in: path
          description: >-
            The id of a document from the knowledge base. This is returned on
            document addition.
          required: true
          schema:
            type: string
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
                $ref: '#/components/schemas/RAGDocumentIndexResponseModel'
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
              $ref: '#/components/schemas/RAGIndexRequestModel'
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
    RAGIndexRequestModel:
      type: object
      properties:
        model:
          $ref: '#/components/schemas/EmbeddingModelEnum'
      required:
        - model
      title: RAGIndexRequestModel
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
  "model": "e5_mistral_7b_instruct"
}
```

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
    await client.conversationalAi.knowledgeBase.document.computeRagIndex("documentation_id", {
        model: "e5_mistral_7b_instruct",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.document.compute_rag_index(
    documentation_id="documentation_id",
    model="e5_mistral_7b_instruct",
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index"

	payload := strings.NewReader("{\n  \"model\": \"e5_mistral_7b_instruct\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"model\": \"e5_mistral_7b_instruct\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index")
  .header("Content-Type", "application/json")
  .body("{\n  \"model\": \"e5_mistral_7b_instruct\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index', [
  'body' => '{
  "model": "e5_mistral_7b_instruct"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"model\": \"e5_mistral_7b_instruct\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["model": "e5_mistral_7b_instruct"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index")! as URL,
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
