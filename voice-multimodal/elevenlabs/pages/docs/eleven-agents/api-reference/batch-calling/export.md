---
title: "Export batch call results"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/export.md
path: docs/eleven-agents/api-reference/batch-calling/export
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Export batch call results

GET https://api.elevenlabs.io/v1/convai/batch-calling/{batch_id}/export

Download all recipients and conversation results for a terminal batch call as CSV.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/export

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/batch-calling/{batch_id}/export:
    get:
      operationId: export
      summary: Export Batch Call Results
      description: >-
        Download all recipients and conversation results for a terminal batch
        call as CSV.
      tags:
        - batchCalls
      parameters:
        - name: batch_id
          in: path
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
          description: Batch call results CSV.
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
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
{}
```

**Response**

```json
{}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        apiKey: "123e4567-e89b-12d3-a456-426614174000",
    });
    await client.conversationalAi.batchCalls.export("b7f3c9d2-4a1e-4f8a-9c3d-2e5f7a1b8c9d");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    api_key="123e4567-e89b-12d3-a456-426614174000",
)

client.conversational_ai.batch_calls.export(
    batch_id="b7f3c9d2-4a1e-4f8a-9c3d-2e5f7a1b8c9d",
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

	url := "https://api.elevenlabs.io/v1/convai/batch-calling/b7f3c9d2-4a1e-4f8a-9c3d-2e5f7a1b8c9d/export"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("xi-api-key", "123e4567-e89b-12d3-a456-426614174000")
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

url = URI("https://api.elevenlabs.io/v1/convai/batch-calling/b7f3c9d2-4a1e-4f8a-9c3d-2e5f7a1b8c9d/export")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = '123e4567-e89b-12d3-a456-426614174000'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/batch-calling/b7f3c9d2-4a1e-4f8a-9c3d-2e5f7a1b8c9d/export")
  .header("xi-api-key", "123e4567-e89b-12d3-a456-426614174000")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/batch-calling/b7f3c9d2-4a1e-4f8a-9c3d-2e5f7a1b8c9d/export', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
    'xi-api-key' => '123e4567-e89b-12d3-a456-426614174000',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/batch-calling/b7f3c9d2-4a1e-4f8a-9c3d-2e5f7a1b8c9d/export");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "123e4567-e89b-12d3-a456-426614174000");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "xi-api-key": "123e4567-e89b-12d3-a456-426614174000",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/batch-calling/b7f3c9d2-4a1e-4f8a-9c3d-2e5f7a1b8c9d/export")! as URL,
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
