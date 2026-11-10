---
title: "List calls"
source: https://elevenlabs.io/docs/api-reference/campaigns/calls/list.md
path: docs/api-reference/campaigns/calls/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List calls

GET https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/{campaign_id}/calls

List the calls of an outbound campaign, newest first: first contacts, retries, callbacks and redirects, whether queued, under way or done.

Reference: https://elevenlabs.io/docs/api-reference/campaigns/calls/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `campaign_id` (string, required)

### Query parameters

- `page_size` (integer, optional, default: 100) — How many items to return at most.
- `lead_id` (string, optional, nullable) — Only this lead's calls.
- `status` (enum, optional, nullable) — Only calls in this status.
  - Allowed values: `queued`, `submitted`, `completed`, `cancelled`, `attention`
- `call_result` (list of enum, optional, nullable) — Only calls that ended in one of these results.
  - Allowed values: `answered`, `voicemail`, `busy`, `no_answer`, `failed`
- `stage` (enum, optional, nullable) — Only messages at this delivery stage. Message campaigns only.
  - Allowed values: `queued`, `sent`, `delivered`, `read`, `replied`, `failed`
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `calls` (list of CallView, required)
- `next_cursor` (string, required, nullable)
- `has_more` (boolean, required)

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### CallView

- `intent_id` (string, required)
- `lead_id` (string, required)
- `intent_type` (enum, required) — `initial` for a lead's first call, else a `retry`, `callback` or `redirect`.
  - Allowed values: `initial`, `retry`, `callback`, `redirect`
- `cold_attempt` (integer, required, nullable) — `1` for the first call and `+1` per retry of it; unset for callbacks, redirects and their retries.
- `status` (enum, required) — `submitted` calls have been handed off for dialing; `attention` calls are held back by an attention item.
  - Allowed values: `queued`, `submitted`, `completed`, `cancelled`, `attention`
- `phone_number` (string, required)
- `scheduled_time_unix` (integer, required) — When the call is due to be placed.
- `conversation_id` (string, required, nullable)
- `outcome` (enum, required, nullable) — The call's final dialing status, set once it ends.
  - Allowed values: `pending`, `dispatched`, `initiated`, `in_progress`, `completed`, `failed`, `cancelled`, `voicemail`
- `call_result` (enum, required, nullable) — How the call ended.
  - Allowed values: `answered`, `voicemail`, `busy`, `no_answer`, `failed`
- `outcome_at_unix` (integer, required, nullable) — When the call ended.
- `decision_disposition` (enum, required, nullable) — What the campaign did after the call, such as queue a retry or a callback, or finish the lead.
  - Allowed values: `completed`, `retry_queued`, `callback_queued`, `redirect_queued`, `attention`, `cancelled`, `do_not_call`, `suppressed`, `window_suspended`, `attempt_ceiling_reached`, `callback_ceiling_reached`, `redirect_ceiling_reached`, `callback_time_invalid`, `redirect_number_invalid`, `couldnt_process`, `suppressed_do_not_call`, `suppressed_after_stop`, `permission_not_granted`, `permission_declined`, `permission_request_blocked`, `permission_expired`
- `collected_dynamic_variables` (map from string to any, optional) — Data collection results this call copied into the lead's dynamic variables for later calls, with secrets redacted.
- `delivery` (LeadDeliveryView, optional, nullable) — The message's delivery; set on message campaigns.

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### LeadDeliveryView

- `status` (enum, required)
  - Allowed values: `pending`, `dispatched`, `initiated`, `in_progress`, `completed`, `failed`, `cancelled`, `voicemail`
- `stage` (enum, required) — The furthest the message got, or `failed` if sending it failed.
  - Allowed values: `queued`, `sent`, `delivered`, `read`, `replied`, `failed`
- `sent_at_unix` (integer, required, nullable)
- `delivered_at_unix` (integer, required, nullable)
- `read_at_unix` (integer, required, nullable)
- `replied_at_unix` (integer, required, nullable)
- `failed_at_unix` (integer, required, nullable)
- `error_message` (string, required, nullable) — Why the message failed to reach the contact.

### ValidationErrorLocItems

- string
- integer

## Examples

**Response**

```json
{
  "calls": [
    {
      "intent_id": "string",
      "lead_id": "string",
      "intent_type": "initial",
      "cold_attempt": 1,
      "status": "queued",
      "phone_number": "string",
      "scheduled_time_unix": 1,
      "conversation_id": "string",
      "outcome": "pending",
      "call_result": "answered",
      "outcome_at_unix": 1,
      "decision_disposition": "completed",
      "collected_dynamic_variables": {},
      "delivery": {
        "status": "pending",
        "stage": "queued",
        "sent_at_unix": 1,
        "delivered_at_unix": 1,
        "read_at_unix": 1,
        "replied_at_unix": 1,
        "failed_at_unix": 1,
        "error_message": "string"
      }
    }
  ],
  "next_cursor": "string",
  "has_more": true
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/calls"

response = requests.get(url)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/calls';
const options = {method: 'GET'};

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
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/calls"

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

url = URI("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/calls")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/calls")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/calls');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/calls");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/calls")! as URL,
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
