---
title: "Create Workspace Webhook"
source: https://elevenlabs.io/docs/api-reference/webhooks/create.md
path: docs/api-reference/webhooks/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create Workspace Webhook

POST https://api.elevenlabs.io/v1/workspace/webhooks
Content-Type: application/json

Create a new webhook for the workspace with the specified authentication type.

Reference: https://elevenlabs.io/docs/api-reference/webhooks/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/workspace/webhooks:
    post:
      operationId: create
      summary: Create Workspace Webhook
      description: >-
        Create a new webhook for the workspace with the specified authentication
        type.
      tags:
        - webhooks
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
                $ref: '#/components/schemas/WorkspaceCreateWebhookResponseModel'
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
                #/components/schemas/Body_Create_workspace_webhook_v1_workspace_webhooks_post
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
    WebhookHMACSettings:
      type: object
      properties:
        auth_type:
          type: string
          enum:
            - hmac
          description: The authentication type for this webhook
        name:
          type: string
          description: The display name for this webhook
        webhook_url:
          type: string
          description: >-
            The HTTPS callback URL that will be called when this webhook is
            triggered
        request_headers:
          type:
            - object
            - 'null'
          additionalProperties:
            type: string
          description: >-
            Optional custom request headers to include with each webhook
            delivery
      required:
        - auth_type
        - name
        - webhook_url
      description: Settings for creating an HMAC-authenticated webhook
      title: WebhookHMACSettings
    Body_Create_workspace_webhook_v1_workspace_webhooks_post:
      type: object
      properties:
        settings:
          $ref: '#/components/schemas/WebhookHMACSettings'
          description: >-
            Webhook settings object containing auth_type and corresponding
            configuration
      required:
        - settings
      title: Body_Create_workspace_webhook_v1_workspace_webhooks_post
    WorkspaceCreateWebhookResponseModel:
      type: object
      properties:
        webhook_id:
          type: string
        webhook_secret:
          type:
            - string
            - 'null'
      required:
        - webhook_id
      title: WorkspaceCreateWebhookResponseModel
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
  "settings": {
    "auth_type": "hmac",
    "name": "Order Processing Webhook",
    "webhook_url": "https://webhooks.example.com/order-processing"
  }
}
```

**Response**

```json
{
  "webhook_id": "a1b2c3d4-e5f6-7890-ab12-cd34ef567890",
  "webhook_secret": "9f8e7d6c5b4a3210fedcba9876543210"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.webhooks.create({
        settings: {
            authType: "hmac",
            name: "Order Processing Webhook",
            webhookUrl: "https://webhooks.example.com/order-processing",
        },
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, WebhookHmacSettings

client = ElevenLabs()

client.webhooks.create(
    settings=WebhookHmacSettings(
        auth_type="hmac",
        name="Order Processing Webhook",
        webhook_url="https://webhooks.example.com/order-processing",
    ),
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

	url := "https://api.elevenlabs.io/v1/workspace/webhooks"

	payload := strings.NewReader("{\n  \"settings\": {\n    \"auth_type\": \"hmac\",\n    \"name\": \"Order Processing Webhook\",\n    \"webhook_url\": \"https://webhooks.example.com/order-processing\"\n  }\n}")

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

url = URI("https://api.elevenlabs.io/v1/workspace/webhooks")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"settings\": {\n    \"auth_type\": \"hmac\",\n    \"name\": \"Order Processing Webhook\",\n    \"webhook_url\": \"https://webhooks.example.com/order-processing\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/workspace/webhooks")
  .header("Content-Type", "application/json")
  .body("{\n  \"settings\": {\n    \"auth_type\": \"hmac\",\n    \"name\": \"Order Processing Webhook\",\n    \"webhook_url\": \"https://webhooks.example.com/order-processing\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/workspace/webhooks', [
  'body' => '{
  "settings": {
    "auth_type": "hmac",
    "name": "Order Processing Webhook",
    "webhook_url": "https://webhooks.example.com/order-processing"
  }
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/webhooks");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"settings\": {\n    \"auth_type\": \"hmac\",\n    \"name\": \"Order Processing Webhook\",\n    \"webhook_url\": \"https://webhooks.example.com/order-processing\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["settings": [
    "auth_type": "hmac",
    "name": "Order Processing Webhook",
    "webhook_url": "https://webhooks.example.com/order-processing"
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/webhooks")! as URL,
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
