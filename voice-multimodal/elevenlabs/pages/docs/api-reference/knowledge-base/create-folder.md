---
title: "Create folder"
source: https://elevenlabs.io/docs/api-reference/knowledge-base/create-folder.md
path: docs/api-reference/knowledge-base/create-folder
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create folder

POST https://api.elevenlabs.io/v1/convai/knowledge-base/folder
Content-Type: application/json

Create a folder used for grouping documents together.

Reference: https://elevenlabs.io/docs/api-reference/knowledge-base/create-folder

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/knowledge-base/folder:
    post:
      operationId: create_folder
      summary: Create Folder
      description: Create a folder used for grouping documents together.
      tags:
        - documents
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
                $ref: '#/components/schemas/AddKnowledgeBaseResponseModel'
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
                #/components/schemas/Body_Create_folder_v1_convai_knowledge_base_folder_post
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
    Body_Create_folder_v1_convai_knowledge_base_folder_post:
      type: object
      properties:
        name:
          type: string
          description: A custom, human-readable name for the document.
        parent_folder_id:
          type:
            - string
            - 'null'
          description: >-
            If set, the created document or folder will be placed inside the
            given folder.
        enable_auto_sync:
          type: boolean
          default: false
          description: Whether to enable auto-sync for this URL document.
        auto_remove:
          type: boolean
          default: false
          description: >-
            Whether to automatically remove the document if the URL becomes
            unavailable. Only applicable when auto-sync is enabled.
      required:
        - name
      title: Body_Create_folder_v1_convai_knowledge_base_folder_post
    KnowledgeBaseFolderPathSegmentSummaryResponseModel:
      type: object
      properties:
        id:
          type: string
      required:
        - id
      title: KnowledgeBaseFolderPathSegmentSummaryResponseModel
    AddKnowledgeBaseResponseModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        folder_path:
          type: array
          items:
            $ref: >-
              #/components/schemas/KnowledgeBaseFolderPathSegmentSummaryResponseModel
          description: >-
            The folder path segments leading to this entity, from root to parent
            folder.
      required:
        - id
        - name
      title: AddKnowledgeBaseResponseModel
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
  "name": "Project Documentation"
}
```

**Response**

```json
{
  "id": "folder_9f8b7c6d5e4a3b2c1d0e",
  "name": "Project Documentation",
  "folder_path": [
    {
      "id": "root_folder_1234567890abcdef"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.documents.createFolder({
        name: "Project Documentation",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.create_folder(
    name="Project Documentation",
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/folder"

	payload := strings.NewReader("{\n  \"name\": \"Project Documentation\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/folder")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Project Documentation\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/knowledge-base/folder")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"Project Documentation\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/knowledge-base/folder', [
  'body' => '{
  "name": "Project Documentation"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/folder");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"Project Documentation\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["name": "Project Documentation"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/folder")! as URL,
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
