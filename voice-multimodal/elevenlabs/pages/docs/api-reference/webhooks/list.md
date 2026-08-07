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

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `include_usages` (boolean, optional, default: false) — Whether to include active usages of the webhook, only usable by admins

## Response

### 200

Successful Response

- `webhooks` (list of object, required) — List of webhooks currently configured for the workspace
  - `name` (string, required) — The display name for this webhook.
  - `webhook_id` (string, required) — The unique ID for this webhook.
  - `webhook_url` (string, required) — The HTTPS callback URL that is called when this webhook is triggered in the platform.
  - `is_disabled` (boolean, required) — Whether the webhook has been manually disabled by a user.
  - `is_auto_disabled` (boolean, required) — Whether the webhook has been automatically disabled due to repeated consecutive failures over a long period of time.
  - `created_at_unix` (integer, required) — Original creation time of the webhook.
  - `auth_type` (enum, required) — The authentication mode used to secure the webhook.
    - Allowed values: `hmac`, `oauth2`, `mtls`
  - `usage` (list of object, optional, nullable) — The list of products that are currently configured to trigger this webhook.
    - `usage_type` (enum, required)
      - Allowed values: `ConvAI Agent Settings`, `ConvAI Settings`, `Voice Library Removal Notices`, `Speech to Text`, `Agent QA Evaluations`, `ConvAI Alerting`, `Flows`, `Dubbing`
  - `events` (list of enum, optional, nullable) — The workspace-level events this webhook is currently subscribed to. Only populated when usages are requested.
    - Allowed values: `voice_library_removal_notice`, `speech_to_text`, `agent_qa`
  - `most_recent_failure_error_code` (integer, optional, nullable) — The most recent error code returned from the callback URL.
  - `most_recent_failure_timestamp` (integer, optional, nullable) — The most recent time the webhook failed, failures are any non-200 codes returned by the callback URL.

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
