---
title: "Get user subscription"
source: https://elevenlabs.io/docs/api-reference/user/subscription/get.md
path: docs/api-reference/user/subscription/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get user subscription

GET https://api.elevenlabs.io/v1/user/subscription

Gets extended information about the users subscription

Reference: https://elevenlabs.io/docs/api-reference/user/subscription/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Response

### 200

Successful Response

- `tier` (string, required) — The tier of the user's subscription.
- `character_count` (integer, required) — The number of characters used by the user.
- `character_limit` (integer, required) — The maximum number of characters allowed in the current billing period.
- `max_character_limit_extension` (integer, required, nullable) — Deprecated: use `max_credit_limit_extension`. Maximum number of characters that the character limit can be exceeded by. Managed by the workspace admin.
- `max_credit_limit_extension` (integer or "unlimited", required) — Maximum number of credits that the credit limit can be exceeded by. Managed by the workspace admin. `"unlimited"` means no cap, `0` means usage-based billing is disabled.
- `can_extend_character_limit` (boolean, required) — Whether the workspace is entitled to enter overages (usage-based billing).
- `allowed_to_extend_character_limit` (boolean, required) — Deprecated: use `max_credit_limit_extension != 0`. Whether the user is allowed to extend their character limit.
- `voice_slots_used` (integer, required) — The number of voice slots used by the user.
- `professional_voice_slots_used` (integer, required) — The number of professional voice slots used. For consolidated billing this is the group-wide count across all workspaces in the group; see professional_voice_slots_used_in_workspace for the current workspace only.
- `professional_voice_slots_used_in_workspace` (integer, required) — The number of professional voice slots used in the current workspace. For consolidated billing, professional_voice_slots_used counts across all workspaces in the group, while this counts only the current workspace.
- `voice_limit` (integer, required) — The maximum number of voice slots allowed for the user.
- `voice_add_edit_counter` (integer, required) — The number of voice add/edits used by the user.
- `professional_voice_limit` (integer, required) — The maximum number of professional voices allowed for the user.
- `can_extend_voice_limit` (boolean, required) — Whether the user can extend their voice limit.
- `can_use_instant_voice_cloning` (boolean, required) — Whether the user can use instant voice cloning.
- `can_use_professional_voice_cloning` (boolean, required) — Whether the user can use professional voice cloning.
- `current_overage` (object, required) — The current usage-based overage cost.
  - `amount` (string, required)
  - `currency` (enum, required)
    - Allowed values: `usd`, `eur`, `inr`, `pln`
- `status` (enum, required) — The status of the user's subscription.
  - Allowed values: `trialing`, `active`, `incomplete`, `past_due`, `free`, `free_disabled`
- `open_invoices` (list of object, required) — The open invoices for the user.
  - `amount_due_cents` (integer, required) — The amount due in cents.
  - `discounts` (list of object, required) — The discounts applied to the invoice.
    - `discount_percent_off` (double, optional, nullable) — The discount applied to the invoice. E.g. [20.0f] for 20% off.
    - `discount_amount_off` (double, optional, nullable) — The discount applied to the invoice. E.g. [20.0f] for 20 cents off.
  - `next_payment_attempt_unix` (integer, required) — The Unix timestamp of the next payment attempt. -1 when there is no next payment attempt.
  - `payment_intent_status` (enum, required, nullable) — Deprecated. Use [payment_intent_statusses] instead. The status of this invoice's first payment intent. None when there is no payment intent.
    - Allowed values: `canceled`, `processing`, `requires_action`, `requires_capture`, `requires_confirmation`, `requires_payment_method`, `succeeded`
  - `payment_intent_statusses` (list of enum, required) — The statuses of this invoice's payment intents. Empty list when there are no payment intents.
    - Allowed values: `canceled`, `processing`, `requires_action`, `requires_capture`, `requires_confirmation`, `requires_payment_method`, `succeeded`
  - `subtotal_cents` (integer, optional, nullable) — The subtotal amount in cents before tax (exclusive of tax and discounts).
  - `tax_cents` (integer, optional, nullable) — The tax amount in cents.
  - `discount_percent_off` (double, optional, nullable) — Deprecated. Use [discounts] instead. The discount applied to the invoice. E.g. [20.0f] for 20% off.
  - `discount_amount_off` (double, optional, nullable) — Deprecated. Use [discounts] instead. The discount applied to the invoice. E.g. [20.0f] for 20 cents off.
- `has_open_invoices` (boolean, required) — Whether the user has open invoices.
- `next_character_count_reset_unix` (integer, optional, nullable) — The Unix timestamp of the next character count reset.
- `max_voice_add_edits` (integer, optional, nullable) — The maximum number of voice add/edits allowed for the user.
- `currency` (enum, optional, nullable) — The currency of the user's subscription.
  - Allowed values: `usd`, `eur`, `inr`, `pln`
- `billing_period` (enum, optional, nullable) — The billing period of the user's subscription.
  - Allowed values: `monthly_period`, `3_month_period`, `6_month_period`, `annual_period`
- `character_refresh_period` (enum, optional, nullable) — The character refresh period of the user's subscription.
  - Allowed values: `monthly_period`, `3_month_period`, `6_month_period`, `annual_period`
- `next_invoice` (object, optional, nullable) — The next invoice for the user.
  - `amount_due_cents` (integer, required) — The amount due in cents.
  - `discounts` (list of object, required) — The discounts applied to the invoice.
    - `discount_percent_off` (double, optional, nullable) — The discount applied to the invoice. E.g. [20.0f] for 20% off.
    - `discount_amount_off` (double, optional, nullable) — The discount applied to the invoice. E.g. [20.0f] for 20 cents off.
  - `next_payment_attempt_unix` (integer, required) — The Unix timestamp of the next payment attempt. -1 when there is no next payment attempt.
  - `payment_intent_status` (enum, required, nullable) — Deprecated. Use [payment_intent_statusses] instead. The status of this invoice's first payment intent. None when there is no payment intent.
    - Allowed values: `canceled`, `processing`, `requires_action`, `requires_capture`, `requires_confirmation`, `requires_payment_method`, `succeeded`
  - `payment_intent_statusses` (list of enum, required) — The statuses of this invoice's payment intents. Empty list when there are no payment intents.
    - Allowed values: `canceled`, `processing`, `requires_action`, `requires_capture`, `requires_confirmation`, `requires_payment_method`, `succeeded`
  - `subtotal_cents` (integer, optional, nullable) — The subtotal amount in cents before tax (exclusive of tax and discounts).
  - `tax_cents` (integer, optional, nullable) — The tax amount in cents.
  - `discount_percent_off` (double, optional, nullable) — Deprecated. Use [discounts] instead. The discount applied to the invoice. E.g. [20.0f] for 20% off.
  - `discount_amount_off` (double, optional, nullable) — Deprecated. Use [discounts] instead. The discount applied to the invoice. E.g. [20.0f] for 20 cents off.
- `pending_change` (object or object, optional, nullable) — The pending change for the user.
  - PendingSubscriptionSwitchResponseModel
    - `next_tier` (enum, required) — The tier to change to.
      - Allowed values: `free`, `starter`, `go`, `creator`, `pro`, `growing_business`, `scale_2024_08_10`, `grant_tier_1_2025_07_23`, `grant_tier_2_2025_07_23`, `trial`, `enterprise`
    - `next_billing_period` (enum, required) — The billing period to change to.
      - Allowed values: `monthly_period`, `3_month_period`, `6_month_period`, `annual_period`
    - `timestamp_seconds` (integer, required) — The timestamp of the change.
    - `kind` ("change", optional, default: change)
  - PendingCancellationResponseModel
    - `timestamp_seconds` (integer, required) — The timestamp of the cancellation.
    - `kind` ("cancellation", optional, default: cancellation)
- `has_used_starter_coupon_on_account` (boolean, optional, default: false) — True if any workspace owned by this user's auth account has redeemed the starter first-month discount coupon.
- `has_used_creator_coupon_on_account` (boolean, optional, default: false) — True if any workspace owned by this user's auth account has redeemed the creator first-month discount coupon.

## Examples

**Response**

```json
{
  "tier": "starter",
  "character_count": 1000,
  "character_limit": 10000,
  "max_character_limit_extension": 10000,
  "max_credit_limit_extension": 10000,
  "can_extend_character_limit": true,
  "allowed_to_extend_character_limit": true,
  "voice_slots_used": 1,
  "professional_voice_slots_used": 0,
  "professional_voice_slots_used_in_workspace": 0,
  "voice_limit": 10,
  "voice_add_edit_counter": 0,
  "professional_voice_limit": 1,
  "can_extend_voice_limit": true,
  "can_use_instant_voice_cloning": true,
  "can_use_professional_voice_cloning": true,
  "current_overage": {
    "amount": "0",
    "currency": "usd"
  },
  "status": "active",
  "open_invoices": [
    {
      "amount_due_cents": 1000,
      "discounts": [
        {
          "discount_percent_off": 20
        }
      ],
      "next_payment_attempt_unix": 1738356858,
      "payment_intent_status": "processing",
      "payment_intent_statusses": [
        "processing",
        "succeeded"
      ],
      "subtotal_cents": 900,
      "tax_cents": 100
    }
  ],
  "has_open_invoices": true,
  "next_character_count_reset_unix": 1738356858,
  "currency": "usd",
  "billing_period": "monthly_period",
  "character_refresh_period": "monthly_period",
  "next_invoice": {
    "amount_due_cents": 1000,
    "discounts": [
      {
        "discount_percent_off": 20
      }
    ],
    "next_payment_attempt_unix": 1738356858,
    "payment_intent_status": "processing",
    "payment_intent_statusses": [
      "processing",
      "succeeded"
    ],
    "subtotal_cents": 900,
    "tax_cents": 100
  },
  "has_used_starter_coupon_on_account": false,
  "has_used_creator_coupon_on_account": false
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.user.subscription.get();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.user.subscription.get()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/user/subscription"

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

url = URI("https://api.elevenlabs.io/v1/user/subscription")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/user/subscription")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/user/subscription');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/user/subscription");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/user/subscription")! as URL,
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
