---
title: "Bulk move documents"
source: https://elevenlabs.io/docs/api-reference/knowledge-base/bulk-move.md
path: docs/api-reference/knowledge-base/bulk-move
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Bulk move documents

POST https://api.elevenlabs.io/v1/convai/knowledge-base/bulk-move
Content-Type: application/json

Moves multiple entities from one folder to another.

Reference: https://elevenlabs.io/docs/api-reference/knowledge-base/bulk-move

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/knowledge-base/bulk-move:
    post:
      operationId: bulk_move
      summary: Bulk Move Entities To Folder
      description: Moves multiple entities from one folder to another.
      tags:
        - subpackage_conversationalAi/knowledgeBase/documents
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
                $ref: >-
                  #/components/schemas/conversational_ai_knowledge_base_documents_bulk_move_Response_200
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
                #/components/schemas/Body_Bulk_move_entities_to_folder_v1_convai_knowledge_base_bulk_move_post
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
    Body_Bulk_move_entities_to_folder_v1_convai_knowledge_base_bulk_move_post:
      type: object
      properties:
        document_ids:
          type: array
          items:
            type: string
          description: The ids of documents or folders from the knowledge base.
        move_to:
          type:
            - string
            - 'null'
          description: >-
            The folder to move the entities to. If not set, the entities will be
            moved to the root folder.
      required:
        - document_ids
      title: >-
        Body_Bulk_move_entities_to_folder_v1_convai_knowledge_base_bulk_move_post
    conversational_ai_knowledge_base_documents_bulk_move_Response_200:
      type: object
      properties: {}
      description: Empty response body
      title: conversational_ai_knowledge_base_documents_bulk_move_Response_200
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
  "document_ids": [
    "21m00Tcm4TlvDq8ikWAM",
    "31m00Tcm4TlvDq8ikWBM"
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
    await client.conversationalAi.knowledgeBase.documents.bulkMove({
        documentIds: [
            "21m00Tcm4TlvDq8ikWAM",
            "31m00Tcm4TlvDq8ikWBM",
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.bulk_move(
    document_ids=[
        "21m00Tcm4TlvDq8ikWAM",
        "31m00Tcm4TlvDq8ikWBM"
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/bulk-move"

	payload := strings.NewReader("{\n  \"document_ids\": [\n    \"21m00Tcm4TlvDq8ikWAM\",\n    \"31m00Tcm4TlvDq8ikWBM\"\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/bulk-move")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"document_ids\": [\n    \"21m00Tcm4TlvDq8ikWAM\",\n    \"31m00Tcm4TlvDq8ikWBM\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/knowledge-base/bulk-move")
  .header("Content-Type", "application/json")
  .body("{\n  \"document_ids\": [\n    \"21m00Tcm4TlvDq8ikWAM\",\n    \"31m00Tcm4TlvDq8ikWBM\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/knowledge-base/bulk-move', [
  'body' => '{
  "document_ids": [
    "21m00Tcm4TlvDq8ikWAM",
    "31m00Tcm4TlvDq8ikWBM"
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

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/bulk-move");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"document_ids\": [\n    \"21m00Tcm4TlvDq8ikWAM\",\n    \"31m00Tcm4TlvDq8ikWBM\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["document_ids": ["21m00Tcm4TlvDq8ikWAM", "31m00Tcm4TlvDq8ikWBM"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/bulk-move")! as URL,
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
