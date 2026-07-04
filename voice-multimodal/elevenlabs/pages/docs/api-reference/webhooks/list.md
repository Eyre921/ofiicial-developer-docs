---
title: "List Workspace Webhooks"
source: https://elevenlabs.io/docs/api-reference/webhooks/list.md
path: docs/api-reference/webhooks/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List Workspace Webhooks

GET https://api.elevenlabs.io/v1/workspace/webhooks

List all webhooks for a workspace

Reference: https://elevenlabs.io/docs/api-reference/webhooks/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/workspace/webhooks:
    get:
      operationId: list
      summary: List Workspace Webhooks
      description: List all webhooks for a workspace
      tags:
        - webhooks
      parameters:
        - name: include_usages
          in: query
          description: >-
            Whether to include active usages of the webhook, only usable by
            admins
          required: false
          schema:
            type: boolean
            default: false
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
                $ref: '#/components/schemas/WorkspaceWebhookListResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
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
    WebhookAuthMethodType:
      type: string
      enum:
        - hmac
        - oauth2
        - mtls
      title: WebhookAuthMethodType
    WebhookUsageType:
      type: string
      enum:
        - ConvAI Agent Settings
        - ConvAI Settings
        - Voice Library Removal Notices
        - Speech to Text
        - Agent QA Evaluations
      title: WebhookUsageType
    WorkspaceWebhookUsageResponseModel:
      type: object
      properties:
        usage_type:
          $ref: '#/components/schemas/WebhookUsageType'
      required:
        - usage_type
      title: WorkspaceWebhookUsageResponseModel
    WorkspaceWebhookResponseModel:
      type: object
      properties:
        name:
          type: string
          description: The display name for this webhook.
        webhook_id:
          type: string
          description: The unique ID for this webhook.
        webhook_url:
          type: string
          description: >-
            The HTTPS callback URL that is called when this webhook is triggered
            in the platform.
        is_disabled:
          type: boolean
          description: Whether the webhook has been manually disabled by a user.
        is_auto_disabled:
          type: boolean
          description: >-
            Whether the webhook has been automatically disabled due to repeated
            consecutive failures over a long period of time.
        created_at_unix:
          type: integer
          description: Original creation time of the webhook.
        auth_type:
          $ref: '#/components/schemas/WebhookAuthMethodType'
          description: The authentication mode used to secure the webhook.
        usage:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/WorkspaceWebhookUsageResponseModel'
          description: >-
            The list of products that are currently configured to trigger this
            webhook.
        most_recent_failure_error_code:
          type:
            - integer
            - 'null'
          description: The most recent error code returned from the callback URL.
        most_recent_failure_timestamp:
          type:
            - integer
            - 'null'
          description: >-
            The most recent time the webhook failed, failures are any non-200
            codes returned by the callback URL.
      required:
        - name
        - webhook_id
        - webhook_url
        - is_disabled
        - is_auto_disabled
        - created_at_unix
        - auth_type
      title: WorkspaceWebhookResponseModel
    WorkspaceWebhookListResponseModel:
      type: object
      properties:
        webhooks:
          type: array
          items:
            $ref: '#/components/schemas/WorkspaceWebhookResponseModel'
          description: List of webhooks currently configured for the workspace
      required:
        - webhooks
      title: WorkspaceWebhookListResponseModel
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



**Response**

```json
{
  "webhooks": [
    {
      "name": "My Webhook",
      "webhook_id": "123",
      "webhook_url": "https://elevenlabs.io/example-callback-url",
      "is_disabled": false,
      "is_auto_disabled": false,
      "created_at_unix": 123456789,
      "auth_type": "hmac",
      "usage": [
        {
          "usage_type": "ConvAI Settings"
        }
      ],
      "most_recent_failure_error_code": 404,
      "most_recent_failure_timestamp": 123456799
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.webhooks.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.webhooks.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/workspace/webhooks"

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

url = URI("https://api.elevenlabs.io/v1/workspace/webhooks")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/workspace/webhooks")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/workspace/webhooks');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/workspace/webhooks");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/workspace/webhooks")! as URL,
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
