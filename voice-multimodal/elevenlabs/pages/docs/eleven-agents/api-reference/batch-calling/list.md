---
title: "List workspace batch calling jobs"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/list.md
path: docs/eleven-agents/api-reference/batch-calling/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List workspace batch calling jobs

GET https://api.elevenlabs.io/v1/convai/batch-calling/workspace

Get all batch calls for the current workspace.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `limit` (integer, optional, default: 100)
- `last_doc` (string, optional)
- `agent_id` (string, optional) — Filter batch calls to a single agent.

## Response

### 200

Successful Response

- `batch_calls` (list of BatchCallResponse, required)
- `next_doc` (string, optional) — The next document, used to paginate through the batch calls
- `has_more` (boolean, optional, default: false) — Whether there are more batch calls to paginate through

## Errors

### 422 Batch Calls List Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### BatchCallResponse

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

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

### TelephonyCallConfigOutput

- `ringing_timeout_secs` (integer, optional, default: 60) — How long to ring the recipient before giving up, in seconds. Note that this will also be limited by the provider's own constraints.
- `twilio_call_recording_enabled` (boolean, optional, default: false) — Whether to record the call using Twilio call recording. Ignored for non-Twilio providers. Recordings are stored in your Twilio account.
- `twilio_machine_detection` (TwilioMachineDetectionConfig, optional) — Configuration for Twilio's carrier-level answering machine detection (AMD). Omit or set to null to disable it. Ignored for non-Twilio providers and for inbound calls. The resulting verdict is delivered as its own `answering_machine_detection` webhook event, which requires that event to be enabled on the workspace or agent webhook settings; it is not part of the conversation or the post-call webhook. Detection runs asynchronously so it never delays the start of the conversation, and the verdict can arrive at any point during the call -- with `detect_message_end`, even after it has ended. Twilio bills separately for AMD.

### BatchCallWhatsAppParams

- `whatsapp_call_permission_request_template_name` (string, required)
- `whatsapp_call_permission_request_template_language_code` (string, required)
- `whatsapp_phone_number_id` (string, optional)

### ValidationErrorLocItem

### TwilioMachineDetectionConfig

How to run Twilio's carrier-level answering machine detection (AMD) on a call.

- `mode` (enum, optional, default: enable) — How thorough the detection should be. `enable` returns a verdict as soon as Twilio can tell a human from a machine. `detect_message_end` also waits for the voicemail greeting to finish, which is what produces the `machine_end_*` verdicts, but returns a result later.
  - Allowed values: `enable`, `detect_message_end`

## Examples

**Response**

```json
{
  "batch_calls": [
    {
      "id": "id",
      "name": "name",
      "agent_id": "agent_id",
      "created_at_unix": 1,
      "scheduled_time_unix": 1,
      "total_calls_dispatched": 1,
      "total_calls_scheduled": 1,
      "total_calls_finished": 1,
      "last_updated_at_unix": 1,
      "status": "pending",
      "retry_count": 1,
      "telephony_call_config": {},
      "agent_name": "agent_name",
      "phone_number_id": "phone_number_id",
      "phone_provider": "twilio",
      "whatsapp_params": {
        "whatsapp_call_permission_request_template_name": "whatsapp_call_permission_request_template_name",
        "whatsapp_call_permission_request_template_language_code": "whatsapp_call_permission_request_template_language_code"
      },
      "branch_id": "branch_id",
      "environment": "environment",
      "timezone": "timezone",
      "target_concurrency_limit": 1,
      "branch_name": "branch_name"
    }
  ],
  "next_doc": "next_doc",
  "has_more": true
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.batchCalls.list({
        agentId: "agent_id",
        lastDoc: "last_doc",
        limit: 1,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.batch_calls.list(
    agent_id="agent_id",
    last_doc="last_doc",
    limit=1,
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

	url := "https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1"

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

url = URI("https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1")! as URL,
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
