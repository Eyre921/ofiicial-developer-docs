---
title: "Compute RAG index"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/compute-rag-index.md
path: docs/eleven-agents/api-reference/knowledge-base/compute-rag-index
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Compute RAG index

POST https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}/rag-index
Content-Type: application/json

In case the document is not RAG indexed, it triggers rag indexing task, otherwise it just returns the current status.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/compute-rag-index

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
                $ref: '#/components/schemas/type_:RagDocumentIndexResponseModel'
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
                model:
                  $ref: '#/components/schemas/type_:EmbeddingModelEnum'
              required:
                - model
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
  "model": "e5_mistral_7b_instruct"
}
```

**Response**

```json
{
  "id": "21m00Tcm4TlvDq8ikWAM",
  "model": "e5_mistral_7b_instruct",
  "status": "processing",
  "progress_percentage": 45.7,
  "document_model_index_usage": {
    "used_bytes": 1048576
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.document.computeRagIndex("21m00Tcm4TlvDq8ikWAM", {
        model: "e5_mistral_7b_instruct",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.document.compute_rag_index(
    documentation_id="21m00Tcm4TlvDq8ikWAM",
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/rag-index"

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/rag-index")

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

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/rag-index")
  .header("Content-Type", "application/json")
  .body("{\n  \"model\": \"e5_mistral_7b_instruct\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/rag-index', [
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

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/rag-index");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/21m00Tcm4TlvDq8ikWAM/rag-index")! as URL,
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
