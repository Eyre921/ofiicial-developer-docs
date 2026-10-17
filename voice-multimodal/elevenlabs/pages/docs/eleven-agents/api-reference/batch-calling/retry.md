---
title: "Retry batch calling job"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/retry.md
path: docs/eleven-agents/api-reference/batch-calling/retry
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Retry batch calling job

POST https://api.elevenlabs.io/v1/convai/batch-calling/{batch_id}/retry

Retry a batch call, calling failed and no-response recipients again.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/retry

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
- `name` (string, required)
- `agent_id` (string, required)
- `created_at_unix` (integer, required)
- `scheduled_time_unix` (integer, required)
- `total_calls_dispatched` (integer, required, default: 0)
- `total_calls_scheduled` (integer, required, default: 0)
- `total_calls_finished` (integer, required, default: 0)
- `last_updated_at_unix` (integer, required)
- `status` (enum, required)
  - Allowed values: `pending`, `in_progress`, `completed`, `failed`, `cancelled`
- `retry_count` (integer, required, default: 0)
- `telephony_call_config` (TelephonyCallConfigOutput, required)
- `agent_name` (string, required)
- `phone_number_id` (string, optional)
- `phone_provider` (enum, optional)
  - Allowed values: `twilio`, `sip_trunk`, `exotel`
- `whatsapp_params` (BatchCallWhatsAppParams, optional)
- `branch_id` (string, optional)
- `environment` (string, optional)
- `timezone` (string, optional)
- `target_concurrency_limit` (integer, optional) — Maximum number of simultaneous calls for this batch. When set, dispatch is governed by this limit rather than workspace/agent capacity percentages.
- `branch_name` (string, optional)

## Errors

### 422 Batch Calls Retry Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### TelephonyCallConfigOutput

- `ringing_timeout_secs` (integer, optional, default: 60) — How long to ring the recipient before giving up, in seconds. Note that this will also be limited by the provider's own constraints.
- `twilio_call_recording_enabled` (boolean, optional, default: false) — Whether to record the call using Twilio call recording. Ignored for non-Twilio providers. Recordings are stored in your Twilio account.
- `twilio_machine_detection` (TwilioMachineDetectionConfig, optional) — Configuration for Twilio's carrier-level answering machine detection (AMD). Omit or set to null to disable it. Ignored for non-Twilio providers and for inbound calls. The resulting verdict is delivered as its own `answering_machine_detection` webhook event, which requires that event to be enabled on the workspace or agent webhook settings; it is not part of the conversation or the post-call webhook. Detection runs asynchronously so it never delays the start of the conversation, and the verdict can arrive at any point during the call -- with `detect_message_end`, even after it has ended. Twilio bills separately for AMD.

### BatchCallWhatsAppParams

- `whatsapp_call_permission_request_template_name` (string, required)
- `whatsapp_call_permission_request_template_language_code` (string, required)
- `whatsapp_phone_number_id` (string, optional)

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

### TwilioMachineDetectionConfig

How to run Twilio's carrier-level answering machine detection (AMD) on a call.

- `mode` (enum, optional, default: enable) — How thorough the detection should be. `enable` returns a verdict as soon as Twilio can tell a human from a machine. `detect_message_end` also waits for the voicemail greeting to finish, which is what produces the `machine_end_*` verdicts, but returns a result later.
  - Allowed values: `enable`, `detect_message_end`

### ValidationErrorLocItem

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "id": "batch_3f8a2c1d9e4b7a6f",
  "name": "Q4 Customer Outreach Campaign - Retry",
  "agent_id": "agent_7c3d2e1f4b8a9d6c",
  "created_at_unix": 1718035200,
  "scheduled_time_unix": 1718121600,
  "total_calls_dispatched": 48,
  "total_calls_scheduled": 60,
  "total_calls_finished": 42,
  "last_updated_at_unix": 1718125800,
  "status": "in_progress",
  "retry_count": 1,
  "telephony_call_config": {
    "ringing_timeout_secs": 30,
    "twilio_call_recording_enabled": true,
    "twilio_machine_detection": {
      "mode": "detect_message_end"
    }
  },
  "agent_name": "Customer Support Agent",
  "phone_number_id": "PN4e2a1b8c7d3f9e5a",
  "phone_provider": "twilio",
  "whatsapp_params": {
    "whatsapp_call_permission_request_template_name": "call_permission_request_v1",
    "whatsapp_call_permission_request_template_language_code": "en_US",
    "whatsapp_phone_number_id": "WA1234567890abcdef"
  },
  "branch_id": "branch_a1b2c3d4e5f6",
  "environment": "production",
  "timezone": "America/New_York",
  "target_concurrency_limit": 10,
  "branch_name": "North America Sales"
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/retry"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/retry';
const options = {method: 'POST', headers: {'Content-Type': 'application/json'}, body: '{}'};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
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

	url := "https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/retry"

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

url = URI("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/retry")

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

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/retry")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/retry', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/retry");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/retry")! as URL,
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
