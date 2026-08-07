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

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `settings` (object, required) — Webhook settings object containing auth_type and corresponding configuration
  - `auth_type` ("hmac", required) — The authentication type for this webhook
  - `name` (string, required) — The display name for this webhook
  - `webhook_url` (string, required) — The HTTPS callback URL that will be called when this webhook is triggered
  - `request_headers` (map from string to string, optional, nullable) — Optional custom request headers to include with each webhook delivery

## Response

### 200

Successful Response

- `webhook_id` (string, required)
- `webhook_secret` (string, optional, nullable)

## Examples

**Request**

```json
{
  "settings": {
    "auth_type": "string",
    "name": "string",
    "webhook_url": "string"
  }
}
```

**Response**

```json
{
  "webhook_id": "string",
  "webhook_secret": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.webhooks.create({
        settings: {
            authType: "string",
            name: "string",
            webhookUrl: "string",
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
        auth_type="string",
        name="string",
        webhook_url="string",
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

	payload := strings.NewReader("{\n  \"settings\": {\n    \"auth_type\": \"string\",\n    \"name\": \"string\",\n    \"webhook_url\": \"string\"\n  }\n}")

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
request.body = "{\n  \"settings\": {\n    \"auth_type\": \"string\",\n    \"name\": \"string\",\n    \"webhook_url\": \"string\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/workspace/webhooks")
  .header("Content-Type", "application/json")
  .body("{\n  \"settings\": {\n    \"auth_type\": \"string\",\n    \"name\": \"string\",\n    \"webhook_url\": \"string\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/workspace/webhooks', [
  'body' => '{
  "settings": {
    "auth_type": "string",
    "name": "string",
    "webhook_url": "string"
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
request.AddParameter("application/json", "{\n  \"settings\": {\n    \"auth_type\": \"string\",\n    \"name\": \"string\",\n    \"webhook_url\": \"string\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["settings": [
    "auth_type": "string",
    "name": "string",
    "webhook_url": "string"
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
