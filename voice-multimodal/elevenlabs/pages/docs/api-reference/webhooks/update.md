---
title: "Update Workspace Webhook"
source: https://elevenlabs.io/docs/api-reference/webhooks/update.md
path: docs/api-reference/webhooks/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update Workspace Webhook

PATCH https://api.elevenlabs.io/v1/workspace/webhooks/{webhook_id}
Content-Type: application/json

Update the specified workspace webhook

Reference: https://elevenlabs.io/docs/api-reference/webhooks/update

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/workspace/webhooks/{webhook_id}:
    patch:
      operationId: update
      summary: Update Workspace Webhook
      description: Update the specified workspace webhook
      tags:
        - webhooks
      parameters:
        - name: webhook_id
          in: path
          description: The unique ID for the webhook
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
                $ref: '#/components/schemas/PatchWorkspaceWebhookResponseModel'
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
                #/components/schemas/Body_Update_workspace_webhook_v1_workspace_webhooks__webhook_id__patch
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
    Body_Update_workspace_webhook_v1_workspace_webhooks__webhook_id__patch:
      type: object
      properties:
        is_disabled:
          type: boolean
          description: Whether to disable or enable the webhook
        name:
          type: string
          description: The display name of the webhook (used for display purposes only).
        retry_enabled:
          type:
            - boolean
            - 'null'
          description: >-
            Whether to enable automatic retries for transient failures (5xx,
            429, timeout)
        request_headers:
          type:
            - object
            - 'null'
          additionalProperties:
            type: string
          description: >-
            A list of request headers to include with the webhook delivery
            (optional)
      required:
        - is_disabled
        - name
      title: Body_Update_workspace_webhook_v1_workspace_webhooks__webhook_id__patch
    PatchWorkspaceWebhookResponseModel:
      type: object
      properties:
        status:
          type: string
          description: >-
            The status of the workspace webhook patch request. If the request
            was successful, the status will be 'ok'. Otherwise an error message
            with status 500 will be returned.
      required:
        - status
      title: PatchWorkspaceWebhookResponseModel
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
  "is_disabled": true,
  "name": "My Callback Webhook"
}
```

**Response**

```json
{
  "status": "ok"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.webhooks.update("webhook_id", {
        isDisabled: true,
        name: "My Callback Webhook",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.webhooks.update(
    webhook_id="webhook_id",
    is_disabled=True,
    name="My Callback Webhook",
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

	url := "https://api.elevenlabs.io/v1/workspace/webhooks/webhook_id"

	payload := strings.NewReader("{\n  \"is_disabled\": true,\n  \"name\": \"My Callback Webhook\"\n}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/workspace/webhooks/webhook_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"is_disabled\": true,\n  \"name\": \"My Callback Webhook\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/workspace/webhooks/webhook_id")
  .header("Content-Type", "application/json")
  .body("{\n  \"is_disabled\": true,\n  \"name\": \"My Callback Webhook\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/workspace/webhooks/webhook_id', [
  'body' => '{
  "is_disabled": true,
  "name": "My Callback Webhook"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/webhooks/webhook_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"is_disabled\": true,\n  \"name\": \"My Callback Webhook\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "is_disabled": true,
  "name": "My Callback Webhook"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/webhooks/webhook_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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
