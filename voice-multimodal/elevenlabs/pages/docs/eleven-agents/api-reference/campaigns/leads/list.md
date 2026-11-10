---
title: "List leads"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/campaigns/leads/list.md
path: docs/eleven-agents/api-reference/campaigns/leads/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List leads

GET https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/{campaign_id}/leads

List the leads of an outbound campaign, one per recipient.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/campaigns/leads/list

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
- `search` (string, optional) — Only leads whose ID, user ID or phone number contains this text.
- `status` (enum, optional) — `in_progress` for leads still being called, `finished` for leads that won't be called again.
  - Allowed values: `in_progress`, `finished`
- `disposition` (enum, optional) — Only leads that finished in one of these ways.
  - Allowed values: `campaign_ended`, `removed`, `do_not_call`, `completed`, `cancelled`, `suppressed`, `attempt_ceiling_reached`, `callback_ceiling_reached`, `redirect_ceiling_reached`, `permission_not_granted`, `permission_declined`, `permission_request_blocked`, `permission_expired`, `callback_time_invalid`, `redirect_number_invalid`, `couldnt_process`
- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `leads` (list of LeadView, required)
- `has_more` (boolean, required)
- `next_cursor` (string, optional)

## Errors

### 422 Leads List Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### LeadView

- `lead_id` (string, required)
- `phone_number` (string, required) — The number the lead's next call dials. It changes when the lead moves on to another listed number or the contact asks to be called on a different one.
- `phone_numbers_index` (integer, required) — The position in `phone_numbers` of the number being called.
- `user_id` (string, required) — The contact's identity: the `user_id` submitted in `conversation_initiation_client_data`, else the lead's phone number.
- `attempt_count` (integer, required) — Calls placed, counted against the policy's `max_total_calls`.
- `failure_count` (integer, required) — Failed calls to the current number; resets on a new number.
- `callback_count` (integer, required) — Callbacks the contact asked for.
- `redirect_count` (integer, required) — Times the contact asked to be called on another number.
- `do_not_call` (boolean, required) — Set when the contact asked not to be called, the lead was removed, or the campaign stopped. The lead isn't called again.
- `updated_at_unix` (integer, required)
- `dynamic_variables` (map from string to any, required) — The dynamic variables submitted for the lead, with secrets redacted.
- `overrides` (FlattenedConfigOverrides, required) — The conversation overrides submitted for the lead.
- `recipient_id` (string, optional) — The `id` given to this recipient when the campaign was created.
- `phone_numbers` (list of string, optional) — The lead's listed numbers, in calling order.
- `terminal_disposition` (enum, optional) — Why the lead won't be called again; unset while it may be.
  - Allowed values: `campaign_ended`, `removed`, `do_not_call`, `completed`, `cancelled`, `suppressed`, `attempt_ceiling_reached`, `callback_ceiling_reached`, `redirect_ceiling_reached`, `permission_not_granted`, `permission_declined`, `permission_request_blocked`, `permission_expired`, `callback_time_invalid`, `redirect_number_invalid`, `couldnt_process`
- `created_at_unix` (integer, optional) — When the lead joined the campaign; unset on older leads.
- `delivery` (LeadDeliveryView, optional) — The lead's latest message delivery; set on message campaigns.

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

### FlattenedConfigOverrides

- `language` (string, optional)
- `first_message` (string, optional)
- `prompt` (string, optional)
- `voice_id` (string, optional)

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
  "leads": [
    {
      "lead_id": "lead_id",
      "phone_number": "phone_number",
      "phone_numbers_index": 1,
      "user_id": "user_id",
      "attempt_count": 1,
      "failure_count": 1,
      "callback_count": 1,
      "redirect_count": 1,
      "do_not_call": true,
      "updated_at_unix": 1,
      "dynamic_variables": {
        "key": "value"
      },
      "overrides": {},
      "recipient_id": "recipient_id",
      "phone_numbers": [
        "phone_numbers"
      ],
      "terminal_disposition": "campaign_ended",
      "created_at_unix": 1,
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

url = "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/leads"

querystring = {"cursor":"cursor","disposition":"[\"campaign_ended\"]","page_size":"1","search":"search","status":"in_progress"}

response = requests.get(url, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/leads?cursor=cursor&disposition=%5B%22campaign_ended%22%5D&page_size=1&search=search&status=in_progress';
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

	url := "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/leads?cursor=cursor&disposition=%5B%22campaign_ended%22%5D&page_size=1&search=search&status=in_progress"

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

url = URI("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/leads?cursor=cursor&disposition=%5B%22campaign_ended%22%5D&page_size=1&search=search&status=in_progress")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/leads?cursor=cursor&disposition=%5B%22campaign_ended%22%5D&page_size=1&search=search&status=in_progress")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/leads?cursor=cursor&disposition=%5B%22campaign_ended%22%5D&page_size=1&search=search&status=in_progress');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/leads?cursor=cursor&disposition=%5B%22campaign_ended%22%5D&page_size=1&search=search&status=in_progress");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/leads?cursor=cursor&disposition=%5B%22campaign_ended%22%5D&page_size=1&search=search&status=in_progress")! as URL,
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
