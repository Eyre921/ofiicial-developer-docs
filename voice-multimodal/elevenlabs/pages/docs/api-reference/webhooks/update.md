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

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `webhook_id` (string, required) — The unique ID for the webhook

### Body (application/json)

- `is_disabled` (boolean, required) — Whether to disable or enable the webhook
- `name` (string, required) — The display name of the webhook (used for display purposes only).
- `retry_enabled` (boolean, optional, nullable) — Whether to enable automatic retries for transient failures (5xx, 429, timeout)
- `request_headers` (map from string to string, optional, nullable) — A list of request headers to include with the webhook delivery (optional)
- `events` (list of enum, optional, nullable) — The complete set of workspace-level events this webhook should be subscribed to. The webhook is added to the events in the list and removed from any not in the list. Omit to leave the current event subscriptions unchanged.
  - Allowed values: `voice_library_removal_notice`, `speech_to_text`, `agent_qa`

## Response

### 200

Successful Response

- `status` (string, required) — The status of the workspace webhook patch request. If the request was successful, the status will be 'ok'. Otherwise an error message with status 500 will be returned.

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
