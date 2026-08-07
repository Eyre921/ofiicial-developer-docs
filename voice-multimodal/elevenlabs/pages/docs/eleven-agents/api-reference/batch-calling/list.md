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

- `batch_calls` (list of object, required)
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
  - `telephony_call_config` (object, required)
    - `ringing_timeout_secs` (integer, optional, default: 60) — How long to ring the recipient before giving up, in seconds. Note that this will also be limited by the provider's own constraints.
    - `twilio_call_recording_enabled` (boolean, optional, default: false) — Whether to record the call using Twilio call recording. Ignored for non-Twilio providers. Recordings are stored in your Twilio account.
  - `agent_name` (string, required)
  - `phone_number_id` (string, optional)
  - `phone_provider` (enum, optional)
    - Allowed values: `twilio`, `sip_trunk`, `exotel`
  - `whatsapp_params` (object, optional)
    - `whatsapp_call_permission_request_template_name` (string, required)
    - `whatsapp_call_permission_request_template_language_code` (string, required)
    - `whatsapp_phone_number_id` (string, optional)
  - `branch_id` (string, optional)
  - `environment` (string, optional)
  - `timezone` (string, optional)
  - `target_concurrency_limit` (integer, optional) — Maximum number of simultaneous calls for this batch. When set, dispatch is governed by this limit rather than workspace/agent capacity percentages.
  - `branch_name` (string, optional)
- `next_doc` (string, optional) — The next document, used to paginate through the batch calls
- `has_more` (boolean, optional, default: false) — Whether there are more batch calls to paginate through

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
      "id": "bc_9f8a7c6d-1234-4e56-8b9a-0f1e2d3c4b5a",
      "name": "April Marketing Campaign Batch",
      "agent_id": "agent_42f7e8d9-0abc-4def-9a12-3456789bcdef",
      "created_at_unix": 1712000000,
      "scheduled_time_unix": 1712604800,
      "total_calls_dispatched": 150,
      "total_calls_scheduled": 200,
      "total_calls_finished": 140,
      "last_updated_at_unix": 1712650000,
      "status": "pending",
      "retry_count": 2,
      "telephony_call_config": {
        "ringing_timeout_secs": 45,
        "twilio_call_recording_enabled": true
      },
      "agent_name": "Sales Outreach Bot",
      "phone_number_id": "pn_7d3f2a1b-4567-4c89-9e0f-1a2b3c4d5e6f",
      "phone_provider": "twilio",
      "whatsapp_params": {
        "whatsapp_call_permission_request_template_name": "customer_permission_request",
        "whatsapp_call_permission_request_template_language_code": "en_US",
        "whatsapp_phone_number_id": "wpn_1234567890abcdef"
      },
      "branch_id": "branch_nyc_office",
      "environment": "production",
      "timezone": "America/New_York",
      "target_concurrency_limit": 20,
      "branch_name": "New York City Office"
    }
  ],
  "next_doc": "bc_9f8a7c6d-1234-4e56-8b9a-0f1e2d3c4b5b",
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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1"

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

url = URI("https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1")! as URL,
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
