---
title: "List workspace batch calling jobs"
source: https://elevenlabs.io/docs/api-reference/batch-calling/list.md
path: docs/api-reference/batch-calling/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List workspace batch calling jobs

GET https://api.elevenlabs.io/v1/convai/batch-calling/workspace

Get all batch calls for the current workspace.

Reference: https://elevenlabs.io/docs/api-reference/batch-calling/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `limit` (integer, optional, default: 100)
- `last_doc` (string, optional, nullable)
- `agent_id` (string, optional, nullable) — Filter batch calls to a single agent.

## Response

### 200

Successful Response

- `batch_calls` (list of BatchCallResponse, required)
- `next_doc` (string, optional, nullable) — The next document, used to paginate through the batch calls
- `has_more` (boolean, optional, default: false) — Whether there are more batch calls to paginate through

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### BatchCallResponse

- `id` (string, required)
- `phone_number_id` (string, required, nullable)
- `phone_provider` (enum, required, nullable)
  - Allowed values: `twilio`, `sip_trunk`, `exotel`
- `whatsapp_params` (BatchCallWhatsAppParams, required, nullable)
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
- `telephony_call_config` (TelephonyCallConfig-Output, required)
- `target_concurrency_limit` (integer, required, nullable) — Maximum number of simultaneous calls for this batch. When set, dispatch is governed by this limit rather than workspace/agent capacity percentages.
- `agent_name` (string, required)
- `branch_name` (string, required, nullable)

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### BatchCallWhatsAppParams

- `whatsapp_call_permission_request_template_name` (string, required)
- `whatsapp_call_permission_request_template_language_code` (string, required)
- `whatsapp_phone_number_id` (string, optional, nullable)

### TelephonyCallConfig-Output

- `ringing_timeout_secs` (integer, optional, default: 60) — How long to ring the recipient before giving up, in seconds. Note that this will also be limited by the provider's own constraints.
- `twilio_call_recording_enabled` (boolean, optional, default: false) — Whether to record the call using Twilio call recording. Ignored for non-Twilio providers. Recordings are stored in your Twilio account.
- `twilio_machine_detection` (TwilioMachineDetectionConfig, optional, nullable) — Configuration for Twilio's carrier-level answering machine detection (AMD). Omit or set to null to disable it. Ignored for non-Twilio providers and for inbound calls. The resulting verdict is delivered as its own `answering_machine_detection` webhook event, which requires that event to be enabled on the workspace or agent webhook settings; it is not part of the conversation or the post-call webhook. Detection runs asynchronously so it never delays the start of the conversation, and the verdict can arrive at any point during the call -- with `detect_message_end`, even after it has ended. Twilio bills separately for AMD.

### ValidationErrorLocItems

### TwilioMachineDetectionConfig

How to run Twilio's carrier-level answering machine detection (AMD) on a call.

- `mode` (enum, optional, default: enable) — How thorough the detection should be. `enable` returns a verdict as soon as Twilio can tell a human from a machine. `detect_message_end` also waits for the voicemail greeting to finish, which is what produces the `machine_end_*` verdicts, but returns a result later.
  - Allowed values: `enable`, `detect_message_end`

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "batch_calls": [
    {
      "id": "batch_7f3a2c1d9e4b5f8a",
      "phone_number_id": "pn_4d8e2f1a3c7b9d5e",
      "phone_provider": "twilio",
      "whatsapp_params": {
        "whatsapp_call_permission_request_template_name": "call_permission_request_v1",
        "whatsapp_call_permission_request_template_language_code": "en_US",
        "whatsapp_phone_number_id": "wa_9b3c5e7f1a2d4e6f"
      },
      "name": "Q4 Customer Outreach Campaign",
      "agent_id": "agent_3e5f7a9b1c2d4e6f",
      "branch_id": "branch_2a4c6e8f0b1d3e5f",
      "environment": "production",
      "created_at_unix": 1711900800,
      "scheduled_time_unix": 1711987200,
      "timezone": "America/New_York",
      "total_calls_dispatched": 320,
      "total_calls_scheduled": 500,
      "total_calls_finished": 298,
      "last_updated_at_unix": 1711990400,
      "status": "in_progress",
      "retry_count": 2,
      "telephony_call_config": {
        "ringing_timeout_secs": 30,
        "twilio_call_recording_enabled": true,
        "twilio_machine_detection": {
          "mode": "detect_message_end"
        }
      },
      "target_concurrency_limit": 25,
      "agent_name": "Sales Outreach Agent",
      "branch_name": "North America Sales"
    }
  ],
  "next_doc": "batch_1a2b3c4d5e6f7a8b",
  "has_more": true
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/batch-calling/workspace"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/batch-calling/workspace';
const options = {method: 'GET', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "https://api.elevenlabs.io/v1/convai/batch-calling/workspace"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/batch-calling/workspace")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/batch-calling/workspace")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/batch-calling/workspace', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/batch-calling/workspace");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/batch-calling/workspace")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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
