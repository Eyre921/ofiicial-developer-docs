---
title: "List calls"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/campaigns/calls/list.md
path: docs/eleven-agents/api-reference/campaigns/calls/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List calls

GET https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/{campaign_id}/calls

List the calls of an outbound campaign, newest first: first contacts, retries, callbacks and redirects, whether queued, under way or done.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/campaigns/calls/list

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
- `lead_id` (string, optional) — Only this lead's calls.
- `status` (enum, optional) — Only calls in this status.
  - Allowed values: `queued`, `submitted`, `completed`, `cancelled`, `attention`
- `call_result` (enum, optional) — Only calls that ended in one of these results.
  - Allowed values: `answered`, `voicemail`, `busy`, `no_answer`, `failed`
- `stage` (enum, optional) — Only messages at this delivery stage. Message campaigns only.
  - Allowed values: `queued`, `sent`, `delivered`, `read`, `replied`, `failed`
- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `calls` (list of CallView, required)
- `has_more` (boolean, required)
- `next_cursor` (string, optional)

## Errors

### 422 Calls List Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### CallView

- `intent_id` (string, required)
- `lead_id` (string, required)
- `intent_type` (enum, required) — `initial` for a lead's first call, else a `retry`, `callback` or `redirect`.
  - Allowed values: `initial`, `retry`, `callback`, `redirect`
- `status` (enum, required) — `submitted` calls have been handed off for dialing; `attention` calls are held back by an attention item.
  - Allowed values: `queued`, `submitted`, `completed`, `cancelled`, `attention`
- `phone_number` (string, required)
- `scheduled_time_unix` (integer, required) — When the call is due to be placed.
- `cold_attempt` (integer, optional) — `1` for the first call and `+1` per retry of it; unset for callbacks, redirects and their retries.
- `conversation_id` (string, optional)
- `outcome` (enum, optional) — The call's final dialing status, set once it ends.
  - Allowed values: `pending`, `dispatched`, `initiated`, `in_progress`, `completed`, `failed`, `cancelled`, `voicemail`
- `call_result` (enum, optional) — How the call ended.
  - Allowed values: `answered`, `voicemail`, `busy`, `no_answer`, `failed`
- `outcome_at_unix` (integer, optional) — When the call ended.
- `decision_disposition` (enum, optional) — What the campaign did after the call, such as queue a retry or a callback, or finish the lead.
  - Allowed values: `completed`, `retry_queued`, `callback_queued`, `redirect_queued`, `attention`, `cancelled`, `do_not_call`, `suppressed`, `window_suspended`, `attempt_ceiling_reached`, `callback_ceiling_reached`, `redirect_ceiling_reached`, `callback_time_invalid`, `redirect_number_invalid`, `couldnt_process`, `suppressed_do_not_call`, `suppressed_after_stop`, `permission_not_granted`, `permission_declined`, `permission_request_blocked`, `permission_expired`
- `collected_dynamic_variables` (map from string to any, optional) — Data collection results this call copied into the lead's dynamic variables for later calls, with secrets redacted.
- `delivery` (LeadDeliveryView, optional) — The message's delivery; set on message campaigns.

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

### LeadDeliveryView

- `status` (enum, required)
  - Allowed values: `pending`, `dispatched`, `initiated`, `in_progress`, `completed`, `failed`, `cancelled`, `voicemail`
- `stage` (enum, required) — The furthest the message got, or `failed` if sending it failed.
  - Allowed values: `queued`, `sent`, `delivered`, `read`, `replied`, `failed`
- `sent_at_unix` (integer, optional)
- `delivered_at_unix` (integer, optional)
- `read_at_unix` (integer, optional)
- `replied_at_unix` (integer, optional)
- `failed_at_unix` (integer, optional)
- `error_message` (string, optional) — Why the message failed to reach the contact.

### ValidationErrorLocItem

- string
- integer

## Examples

**Response**

```json
{
  "calls": [
    {
      "intent_id": "intent_id",
      "lead_id": "lead_id",
      "intent_type": "initial",
      "status": "queued",
      "phone_number": "phone_number",
      "scheduled_time_unix": 1,
      "cold_attempt": 1,
      "conversation_id": "conversation_id",
      "outcome": "pending",
      "call_result": "answered",
      "outcome_at_unix": 1,
      "decision_disposition": "completed",
      "collected_dynamic_variables": {
        "key": "value"
      },
      "delivery": {
        "status": "pending",
        "stage": "queued",
        "sent_at_unix": null,
        "delivered_at_unix": null,
        "read_at_unix": null,
        "replied_at_unix": null,
        "failed_at_unix": null,
        "error_message": null
      }
    }
  ],
  "has_more": true,
  "next_cursor": "next_cursor"
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/calls"

querystring = {"call_result":"[\"answered\"]","cursor":"cursor","lead_id":"lead_id","page_size":"1","stage":"queued","status":"queued"}

response = requests.get(url, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/calls?call_result=%5B%22answered%22%5D&cursor=cursor&lead_id=lead_id&page_size=1&stage=queued&status=queued';
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

	url := "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/calls?call_result=%5B%22answered%22%5D&cursor=cursor&lead_id=lead_id&page_size=1&stage=queued&status=queued"

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

url = URI("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/calls?call_result=%5B%22answered%22%5D&cursor=cursor&lead_id=lead_id&page_size=1&stage=queued&status=queued")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/calls?call_result=%5B%22answered%22%5D&cursor=cursor&lead_id=lead_id&page_size=1&stage=queued&status=queued")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/calls?call_result=%5B%22answered%22%5D&cursor=cursor&lead_id=lead_id&page_size=1&stage=queued&status=queued');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/calls?call_result=%5B%22answered%22%5D&cursor=cursor&lead_id=lead_id&page_size=1&stage=queued&status=queued");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/calls?call_result=%5B%22answered%22%5D&cursor=cursor&lead_id=lead_id&page_size=1&stage=queued&status=queued")! as URL,
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
