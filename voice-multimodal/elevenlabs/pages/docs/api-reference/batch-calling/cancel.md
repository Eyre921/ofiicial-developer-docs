---
title: "Cancel batch calling job"
source: https://elevenlabs.io/docs/api-reference/batch-calling/cancel.md
path: docs/api-reference/batch-calling/cancel
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Cancel batch calling job

POST https://api.elevenlabs.io/v1/convai/batch-calling/{batch_id}/cancel

Cancel a running batch call and set all recipients to cancelled status.

Reference: https://elevenlabs.io/docs/api-reference/batch-calling/cancel

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `batch_id` (string, required)

## Response

### 200

Successful Response

- `id` (string, required)
- `phone_number_id` (string, required, nullable)
- `phone_provider` (enum, required, nullable)
  - Allowed values: `twilio`, `sip_trunk`, `exotel`
- `whatsapp_params` (object, required, nullable)
  - `whatsapp_call_permission_request_template_name` (string, required)
  - `whatsapp_call_permission_request_template_language_code` (string, required)
  - `whatsapp_phone_number_id` (string, optional, nullable)
- `name` (string, required)
- `agent_id` (string, required)
- `branch_id` (string, required, nullable)
- `environment` (string, required, nullable)
- `created_at_unix` (integer, required)
- `scheduled_time_unix` (integer, required)
- `timezone` (string, required, nullable)
- `total_calls_dispatched` (integer, required, default: 0)
- `total_calls_scheduled` (integer, required, default: 0)
- `total_calls_finished` (integer, required, default: 0)
- `last_updated_at_unix` (integer, required)
- `status` (enum, required)
  - Allowed values: `pending`, `in_progress`, `completed`, `failed`, `cancelled`
- `retry_count` (integer, required, default: 0)
- `telephony_call_config` (object, required)
  - `ringing_timeout_secs` (integer, optional, default: 60) — How long to ring the recipient before giving up, in seconds. Note that this will also be limited by the provider's own constraints.
  - `twilio_call_recording_enabled` (boolean, optional, default: false) — Whether to record the call using Twilio call recording. Ignored for non-Twilio providers. Recordings are stored in your Twilio account.
- `target_concurrency_limit` (integer, required, nullable) — Maximum number of simultaneous calls for this batch. When set, dispatch is governed by this limit rather than workspace/agent capacity percentages.
- `agent_name` (string, required)
- `branch_name` (string, required, nullable)

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "id": "b7f3c9d2-8a4e-4f3a-9c1e-2d5a7b8e9f01",
  "phone_number_id": "pn_987654321",
  "phone_provider": "twilio",
  "whatsapp_params": {
    "whatsapp_call_permission_request_template_name": "customer_permission_request",
    "whatsapp_call_permission_request_template_language_code": "en_US",
    "whatsapp_phone_number_id": "wa_123456789"
  },
  "name": "April Marketing Campaign",
  "agent_id": "agent_42",
  "branch_id": "branch_nyc_01",
  "environment": "production",
  "created_at_unix": 1712000000,
  "scheduled_time_unix": 1712604800,
  "timezone": "America/New_York",
  "total_calls_dispatched": 150,
  "total_calls_scheduled": 200,
  "total_calls_finished": 120,
  "last_updated_at_unix": 1712650000,
  "status": "cancelled",
  "retry_count": 2,
  "telephony_call_config": {
    "ringing_timeout_secs": 45,
    "twilio_call_recording_enabled": true
  },
  "target_concurrency_limit": 10,
  "agent_name": "Support Agent Alpha",
  "branch_name": "New York Downtown"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.batchCalls.cancel("batch_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.batch_calls.cancel(
    batch_id="batch_id",
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

	url := "https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/cancel"

	payload := strings.NewReader("{}")

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

url = URI("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/cancel")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/cancel")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/cancel', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/cancel");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/cancel")! as URL,
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
