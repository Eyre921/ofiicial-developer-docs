---
title: "Replace campaign config"
source: https://elevenlabs.io/docs/api-reference/campaigns/config/update.md
path: docs/api-reference/campaigns/config/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Replace campaign config

PUT https://api.elevenlabs.io/v1/convai/outbound-campaigns/config
Content-Type: application/json

Create or replace the workspace's outbound campaign configuration. Send the `version` you last read as `expected_version`, or omit it to create the first configuration. A configuration changed since you read it is not replaced. Campaigns keep the policy they started with.

Reference: https://elevenlabs.io/docs/api-reference/campaigns/config/update

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

This endpoint expects a ReplaceWorkspaceConfigRequest.

- `config` (CampaignConfig-Input, required)
- `expected_version` (integer, optional, nullable) — The `version` of the configuration being replaced. Omit it only to create the first configuration.

## Response

### 200

Successful Response

- `version` (integer, required) — Increases with every replacement; send it as `expected_version`.
- `config` (CampaignConfig-Output, required)

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### CampaignConfig-Input

- `policy` (PolicyConfig-Input, optional) — The policy campaigns take unless they set their own.
- `agent_policies` (map from string to AgentPolicyOverride-Input, optional) — Overrides of `policy`, keyed by agent ID.
- `whatsapp_voice_policy` (AgentPolicyOverride-Input, optional, nullable) — Overrides for WhatsApp voice campaigns, layered between the workspace policy and an agent's overrides. Sections left out follow WhatsApp voice's built-in defaults.

### CampaignConfig-Output

- `policy` (PolicyConfig-Output, optional) — The policy campaigns take unless they set their own.
- `agent_policies` (map from string to AgentPolicyOverride-Output, optional) — Overrides of `policy`, keyed by agent ID.
- `whatsapp_voice_policy` (AgentPolicyOverride-Output, optional, nullable) — Overrides for WhatsApp voice campaigns, layered between the workspace policy and an agent's overrides. Sections left out follow WhatsApp voice's built-in defaults.

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### PolicyConfig-Input

- `timezone` (string, optional, default: UTC) — IANA timezone the calling periods are read in.
- `retry` (RetryPolicy, optional)
- `calling_periods` (list of CallingPeriod, optional) — The weekly windows calls may be placed in.
- `data_collection` (DataCollectionConfig, optional) — The agent's data collection items that steer follow-up calls. Each defaults to the built-in item for its purpose; `null` turns it off.
- `followup_context` (FollowupContextPolicy, optional) — Which `campaign__` dynamic variables follow-up calls get.

### AgentPolicyOverride-Input

Each section set here replaces the whole matching section of the policy.

- `timezone` (string, optional, nullable)
- `retry` (RetryPolicy, optional, nullable)
- `calling_periods` (list of CallingPeriod, optional, nullable)
- `data_collection` (DataCollectionConfig, optional, nullable) — The agent's data collection items that steer follow-up calls. Each defaults to the built-in item for its purpose; `null` turns it off.
- `followup_context` (FollowupContextPolicy, optional, nullable) — Which `campaign__` dynamic variables follow-up calls get.

### PolicyConfig-Output

- `timezone` (string, optional, default: UTC) — IANA timezone the calling periods are read in.
- `retry` (RetryPolicy, optional)
- `calling_periods` (list of CallingPeriod, optional) — The weekly windows calls may be placed in.
- `data_collection` (DataCollectionConfig, optional) — The agent's data collection items that steer follow-up calls. Each defaults to the built-in item for its purpose; `null` turns it off.
- `followup_context` (FollowupContextPolicy, optional) — Which `campaign__` dynamic variables follow-up calls get.

### AgentPolicyOverride-Output

Each section set here replaces the whole matching section of the policy.

- `timezone` (string, optional, nullable)
- `retry` (RetryPolicy, optional, nullable)
- `calling_periods` (list of CallingPeriod, optional, nullable)
- `data_collection` (DataCollectionConfig, optional, nullable) — The agent's data collection items that steer follow-up calls. Each defaults to the built-in item for its purpose; `null` turns it off.
- `followup_context` (FollowupContextPolicy, optional, nullable) — Which `campaign__` dynamic variables follow-up calls get.

### ValidationErrorLocItems

- string
- integer

### RetryPolicy

- `retry_delay_seconds` (integer, optional, default: 600) — How long to wait before a short retry.
- `max_short_retries` (integer, optional, default: 1) — Retries a calling window allows after a failed call. Once used up, the next retry waits for the following window, which starts afresh.
- `max_total_calls` (integer, optional, default: 6) — The most calls a lead gets, counting the first.
- `max_callbacks` (integer, optional, default: 2) — The most callbacks to honor for one number.
- `max_redirects` (integer, optional, default: 2) — The most times a lead follows a request to call another number.
- `interval_placement` (enum, optional, default: start) — Where in a later calling window a pushed-back call lands: at its `start`, at a `random` time, or `rotate`d `rotate_step_seconds` past where the last call in that window failed.
  - Allowed values: `start`, `random`, `rotate`
- `rotate_step_seconds` (integer, optional, default: 900) — How far `rotate` placement moves each call. Only used by `rotate`.
- `max_consecutive_failures_per_number` (integer, optional, nullable) — Calls to one number that may fail in a row before the lead moves on to its next listed number, or ends when there is none. An answered call, or a redirect to a new number, restarts the count. Unset leaves only `max_total_calls`.

### CallingPeriod

- `weekdays` (list of integer, required) — Days the intervals apply on, from `0` (Monday) to `6` (Sunday).
- `intervals` (list of CallingIntervalPolicy, required) — Windows on each of those days. They may not overlap on any day.

### DataCollectionConfig

The agent's data collection items that steer follow-up calls. Each defaults to the built-in item for its purpose; `null` turns it off.

- `callback_time` (string, optional, nullable, default: __system_data_collection_callback_time) — The item holding when the contact asked to be called back.
- `redirect_phone_number` (string, optional, nullable, default: __system_data_collection_redirect_phone_number) — The item holding another number the contact asked to be called on.
- `stop` (string, optional, nullable, default: __system_data_collection_do_not_call) — The item that is true when the contact asked not to be called again.
- `mappings` (map from string to string, optional) — Copies data collection results into dynamic variables for later calls: each key is a data collection item ID and its value the variable's name.

### FollowupContextPolicy

Which `campaign__` dynamic variables follow-up calls get.

- `call_type` (boolean, optional, default: true) — Pass the call type as `campaign__call_type`.
- `previous_conversation_id` (boolean, optional, default: true) — Pass the last conversation's ID as `campaign__previous_conversation_id`.
- `previous_summary` (boolean, optional, default: true) — Pass the last conversation's summary as `campaign__previous_summary`.
- `previous_transcript` (boolean, optional, default: true) — Pass the last conversation's transcript as `campaign__previous_transcript`.

### CallingIntervalPolicy

- `start` (string, required) — Local start time, as `HH:MM`.
- `end` (string, required) — Local end time, as `HH:MM`; `24:00` ends at midnight.

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "version": 1,
  "config": {
    "policy": {
      "timezone": "UTC",
      "retry": {
        "retry_delay_seconds": 600,
        "max_short_retries": 1,
        "max_total_calls": 6,
        "max_callbacks": 2,
        "max_redirects": 2,
        "interval_placement": "start",
        "rotate_step_seconds": 900,
        "max_consecutive_failures_per_number": 1
      },
      "calling_periods": [
        {
          "weekdays": [
            1
          ],
          "intervals": [
            {
              "start": "string",
              "end": "string"
            }
          ]
        }
      ],
      "data_collection": {
        "callback_time": "string",
        "redirect_phone_number": "string",
        "stop": "string",
        "mappings": {}
      },
      "followup_context": {
        "call_type": true,
        "previous_conversation_id": true,
        "previous_summary": true,
        "previous_transcript": true
      }
    },
    "agent_policies": {},
    "whatsapp_voice_policy": {
      "timezone": "string",
      "retry": {
        "retry_delay_seconds": 600,
        "max_short_retries": 1,
        "max_total_calls": 6,
        "max_callbacks": 2,
        "max_redirects": 2,
        "interval_placement": "start",
        "rotate_step_seconds": 900,
        "max_consecutive_failures_per_number": 1
      },
      "calling_periods": [
        {
          "weekdays": [
            1
          ],
          "intervals": [
            {
              "start": "string",
              "end": "string"
            }
          ]
        }
      ],
      "data_collection": {
        "callback_time": "string",
        "redirect_phone_number": "string",
        "stop": "string",
        "mappings": {}
      },
      "followup_context": {
        "call_type": true,
        "previous_conversation_id": true,
        "previous_summary": true,
        "previous_transcript": true
      }
    }
  }
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/outbound-campaigns/config"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/config';
const options = {method: 'PUT', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "https://api.elevenlabs.io/v1/convai/outbound-campaigns/config"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PUT", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/outbound-campaigns/config")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("https://api.elevenlabs.io/v1/convai/outbound-campaigns/config")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/config', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/outbound-campaigns/config");
var request = new RestRequest(Method.PUT);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/outbound-campaigns/config")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
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
