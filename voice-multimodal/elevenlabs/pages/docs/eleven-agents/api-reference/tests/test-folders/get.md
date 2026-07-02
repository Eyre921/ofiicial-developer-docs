---
title: "Get folder"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/test-folders/get.md
path: docs/eleven-agents/api-reference/tests/test-folders/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get folder

GET https://api.elevenlabs.io/v1/convai/agent-testing/folders/{folder_id}

Gets an agent test folder by ID, including its folder path.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/test-folders/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agent-testing/folders/{folder_id}:
    get:
      operationId: get
      summary: Get Agent Test Folder By Id
      description: Gets an agent test folder by ID, including its folder path.
      tags:
        - subpackage_conversationalAi/tests/folders
      parameters:
        - name: folder_id
          in: path
          description: The folder ID.
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
          description: Folder details retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:GetAgentTestFolderResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
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
    type_:AgentTestFolderPathSegmentResponseModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
          default: ''
      required:
        - id
      title: AgentTestFolderPathSegmentResponseModel
    type_:GetAgentTestFolderResponseModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        folder_path:
          type: array
          items:
            $ref: '#/components/schemas/type_:AgentTestFolderPathSegmentResponseModel'
          description: The path from the root folder to the current folder.
        children_count:
          type: integer
          default: 0
          description: The number of direct children (tests and subfolders) in this folder
      required:
        - id
        - name
      title: GetAgentTestFolderResponseModel
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

**Response**

```json
{
  "id": "id",
  "name": "name",
  "folder_path": [
    {
      "id": "id",
      "name": "name"
    }
  ],
  "children_count": 1
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tests.folders.get("tfld_7301khxdkycse5f88fzjdtrterzm");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.folders.get(
    folder_id="tfld_7301khxdkycse5f88fzjdtrterzm",
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

	url := "https://api.elevenlabs.io/v1/convai/agent-testing/folders/tfld_7301khxdkycse5f88fzjdtrterzm"

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

url = URI("https://api.elevenlabs.io/v1/convai/agent-testing/folders/tfld_7301khxdkycse5f88fzjdtrterzm")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agent-testing/folders/tfld_7301khxdkycse5f88fzjdtrterzm")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agent-testing/folders/tfld_7301khxdkycse5f88fzjdtrterzm');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agent-testing/folders/tfld_7301khxdkycse5f88fzjdtrterzm");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agent-testing/folders/tfld_7301khxdkycse5f88fzjdtrterzm")! as URL,
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
