---
title: "Get lead"
source: https://elevenlabs.io/docs/api-reference/campaigns/leads/get.md
path: docs/api-reference/campaigns/leads/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get lead

GET https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/{campaign_id}/leads/{lead_id}

Get one lead of an outbound campaign.

Reference: https://elevenlabs.io/docs/api-reference/campaigns/leads/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `campaign_id` (string, required)
- `lead_id` (string, required)

## Response

### 200

Successful Response

- `lead_id` (string, required)
- `recipient_id` (string, required, nullable) — The `id` given to this recipient when the campaign was created.
- `phone_number` (string, required) — The number the lead's next call dials. It changes when the lead moves on to another listed number or the contact asks to be called on a different one.
- `phone_numbers_index` (integer, required) — The position in `phone_numbers` of the number being called.
- `user_id` (string, required) — The contact's identity: the `user_id` submitted in `conversation_initiation_client_data`, else the lead's phone number.
- `attempt_count` (integer, required) — Calls placed, counted against the policy's `max_total_calls`.
- `failure_count` (integer, required) — Failed calls to the current number; resets on a new number.
- `callback_count` (integer, required) — Callbacks the contact asked for.
- `redirect_count` (integer, required) — Times the contact asked to be called on another number.
- `do_not_call` (boolean, required) — Set when the contact asked not to be called, the lead was removed, or the campaign stopped. The lead isn't called again.
- `terminal_disposition` (enum, required, nullable) — Why the lead won't be called again; unset while it may be.
  - Allowed values: `campaign_ended`, `removed`, `do_not_call`, `completed`, `cancelled`, `suppressed`, `attempt_ceiling_reached`, `callback_ceiling_reached`, `redirect_ceiling_reached`, `permission_not_granted`, `permission_declined`, `permission_request_blocked`, `permission_expired`, `callback_time_invalid`, `redirect_number_invalid`, `couldnt_process`
- `created_at_unix` (integer, required, nullable) — When the lead joined the campaign; unset on older leads.
- `updated_at_unix` (integer, required)
- `dynamic_variables` (map from string to any, required) — The dynamic variables submitted for the lead, with secrets redacted.
- `overrides` (FlattenedConfigOverrides, required) — The conversation overrides submitted for the lead.
- `phone_numbers` (list of string, optional) — The lead's listed numbers, in calling order.
- `delivery` (LeadDeliveryView, optional, nullable) — The lead's latest message delivery; set on message campaigns.

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### FlattenedConfigOverrides

- `language` (string, optional, nullable)
- `first_message` (string, optional, nullable)
- `prompt` (string, optional, nullable)
- `voice_id` (string, optional, nullable)

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

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

- string
- integer

## Examples

**Response**

```json
{
  "lead_id": "string",
  "recipient_id": "string",
  "phone_number": "string",
  "phone_numbers_index": 1,
  "user_id": "string",
  "attempt_count": 1,
  "failure_count": 1,
  "callback_count": 1,
  "redirect_count": 1,
  "do_not_call": true,
  "terminal_disposition": "campaign_ended",
  "created_at_unix": 1,
  "updated_at_unix": 1,
  "dynamic_variables": {},
  "overrides": {
    "language": "string",
    "first_message": "string",
    "prompt": "string",
    "voice_id": "string"
  },
  "phone_numbers": [
    "string"
  ],
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
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/leads/lead_id"

response = requests.get(url)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/leads/lead_id';
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

	url := "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/leads/lead_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/leads/lead_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/leads/lead_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/leads/lead_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/leads/lead_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/campaign_id/leads/lead_id")! as URL,
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
