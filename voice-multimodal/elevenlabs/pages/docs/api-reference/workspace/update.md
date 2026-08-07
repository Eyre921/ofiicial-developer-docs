---
title: "Update settings"
source: https://elevenlabs.io/docs/api-reference/workspace/update.md
path: docs/api-reference/workspace/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update settings

PATCH https://api.elevenlabs.io/v1/convai/settings
Content-Type: application/json

Update Convai settings for the workspace

Reference: https://elevenlabs.io/docs/api-reference/workspace/update

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `conversation_initiation_client_data_webhook` (object, optional, nullable)
  - `url` (string, required) — The URL to send the webhook to
  - `request_headers` (map from string to string or object, required) — The headers to send with the webhook request
    - ConvAISecretLocator
      - `secret_id` (string, required)
- `webhooks` (object, optional)
  - `post_call_webhook_id` (string, optional, nullable)
  - `events` (list of enum, optional) — List of event types to send via webhook. Options: transcript, audio, call_initiation_failure, unredacted_transcript, unredacted_audio.
    - Allowed values: `transcript`, `audio`, `call_initiation_failure`, `unredacted_transcript`, `unredacted_audio`
  - `transcript_format` (enum, optional, default: json) — Format for transcript webhooks.
    - Allowed values: `json`, `opentelemetry`
  - `send_audio` (boolean, optional, nullable, deprecated) — DEPRECATED: Use 'events' field instead. Whether to send audio data with post-call webhooks for ConvAI conversations
- `can_use_mcp_servers` (boolean, optional, default: false) — Whether the workspace can use MCP servers
- `rag_retention_period_days` (integer, optional, default: 10)
- `conversation_embedding_retention_days` (integer, optional, nullable) — Days to retain conversation embeddings. None means use the system default (30 days).
- `default_livekit_stack` (enum, optional, default: standard)
  - Allowed values: `standard`, `static`

## Response

### 200

Successful Response

- `conversation_initiation_client_data_webhook` (object, optional, nullable)
  - `url` (string, required) — The URL to send the webhook to
  - `request_headers` (map from string to string or object, required) — The headers to send with the webhook request
    - ConvAISecretLocator
      - `secret_id` (string, required)
- `webhooks` (object, optional)
  - `post_call_webhook_id` (string, optional, nullable)
  - `events` (list of enum, optional) — List of event types to send via webhook. Options: transcript, audio, call_initiation_failure, unredacted_transcript, unredacted_audio.
    - Allowed values: `transcript`, `audio`, `call_initiation_failure`, `unredacted_transcript`, `unredacted_audio`
  - `transcript_format` (enum, optional, default: json) — Format for transcript webhooks.
    - Allowed values: `json`, `opentelemetry`
  - `send_audio` (boolean, optional, nullable, deprecated) — DEPRECATED: Use 'events' field instead. Whether to send audio data with post-call webhooks for ConvAI conversations
- `can_use_mcp_servers` (boolean, optional, default: false) — Whether the workspace can use MCP servers
- `rag_retention_period_days` (integer, optional, default: 10)
- `conversation_embedding_retention_days` (integer, optional, nullable) — Days to retain conversation embeddings. None means use the system default (30 days).
- `default_livekit_stack` (enum, optional, default: standard)
  - Allowed values: `standard`, `static`

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "conversation_initiation_client_data_webhook": {
    "url": "https://example.com/webhook",
    "request_headers": {
      "Content-Type": "application/json"
    }
  },
  "webhooks": {
    "post_call_webhook_id": "string",
    "events": [
      "transcript"
    ],
    "transcript_format": "json",
    "send_audio": true
  },
  "can_use_mcp_servers": false,
  "rag_retention_period_days": 10,
  "conversation_embedding_retention_days": 1,
  "default_livekit_stack": "standard"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.settings.update({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.settings.update()

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

	url := "https://api.elevenlabs.io/v1/convai/settings"

	payload := strings.NewReader("{}")

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

url = URI("https://api.elevenlabs.io/v1/convai/settings")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/settings")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/settings', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/settings");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/settings")! as URL,
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
