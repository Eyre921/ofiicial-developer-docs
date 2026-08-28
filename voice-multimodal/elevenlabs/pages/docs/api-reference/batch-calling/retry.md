---
title: "Retry batch calling job"
source: https://elevenlabs.io/docs/api-reference/batch-calling/retry.md
path: docs/api-reference/batch-calling/retry
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Retry batch calling job

POST https://api.elevenlabs.io/v1/convai/batch-calling/{batch_id}/retry

Retry a batch call, calling failed and no-response recipients again.

Reference: https://elevenlabs.io/docs/api-reference/batch-calling/retry

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

**Response**

```json
{
  "id": "string",
  "phone_number_id": "string",
  "phone_provider": "twilio",
  "whatsapp_params": {
    "whatsapp_call_permission_request_template_name": "string",
    "whatsapp_call_permission_request_template_language_code": "string",
    "whatsapp_phone_number_id": "string"
  },
  "name": "string",
  "agent_id": "string",
  "branch_id": "string",
  "environment": "string",
  "created_at_unix": 1,
  "scheduled_time_unix": 1,
  "timezone": "string",
  "total_calls_dispatched": 0,
  "total_calls_scheduled": 0,
  "total_calls_finished": 0,
  "last_updated_at_unix": 1,
  "status": "pending",
  "retry_count": 0,
  "telephony_call_config": {
    "ringing_timeout_secs": 60,
    "twilio_call_recording_enabled": false
  },
  "target_concurrency_limit": 1,
  "agent_name": "string",
  "branch_name": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.batchCalls.retry("batch_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.batch_calls.retry(
    batch_id="batch_id",
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

	url := "https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/retry"

	req, _ := http.NewRequest("POST", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/retry")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/retry")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/retry');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/retry");
var request = new RestRequest(Method.POST);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/retry")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"

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
