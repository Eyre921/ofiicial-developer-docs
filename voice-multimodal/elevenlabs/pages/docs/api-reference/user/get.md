---
title: "Get user"
source: https://elevenlabs.io/docs/api-reference/user/get.md
path: docs/api-reference/user/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get user

GET https://api.elevenlabs.io/v1/user

Gets information about the user

Reference: https://elevenlabs.io/docs/api-reference/user/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Response

### 200

Successful Response

- `user_id` (string, required) — The unique identifier of the user.
- `subscription` (object, required) — Details of the user's subscription.
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
  - `next_character_count_reset_unix` (integer, optional, nullable) — The Unix timestamp of the next character count reset.
  - `max_voice_add_edits` (integer, optional, nullable) — The maximum number of voice add/edits allowed for the user.
  - `currency` (enum, optional, nullable) — The currency of the user's subscription.
    - Allowed values: `usd`, `eur`, `inr`, `pln`
  - `billing_period` (enum, optional, nullable) — The billing period of the user's subscription.
    - Allowed values: `monthly_period`, `3_month_period`, `6_month_period`, `annual_period`
  - `character_refresh_period` (enum, optional, nullable) — The character refresh period of the user's subscription.
    - Allowed values: `monthly_period`, `3_month_period`, `6_month_period`, `annual_period`
- `is_onboarding_completed` (boolean, required) — Whether the user's onboarding is completed.
- `is_onboarding_checklist_completed` (boolean, required) — Whether the user's onboarding checklist is completed.
- `created_at` (integer, required) — The unix timestamp of the user's creation. 0 if the user was created before the unix timestamp was added.
- `seat_type` (enum, required) — The seat type of the user.
  - Allowed values: `workspace_admin`, `workspace_member`, `workspace_lite_member`
- `is_new_user` (boolean, required, deprecated) — Whether the user is new. This field is deprecated and will be removed in the future. Use 'created_at' instead.
- `can_use_delayed_payment_methods` (boolean, required, deprecated) — This field is deprecated and will be removed in a future major version. Instead use subscription.trust_on_invoice_creation.
- `show_compliance_terms` (boolean, optional, default: false) — Whether to show compliance terms (ToS, Privacy Policy, biometric consent) during onboarding. Set for users signing up from the marketing site.
- `first_name` (string, optional, nullable) — First name of the user.
- `is_api_key_hashed` (boolean, optional, default: false) — Whether the user's API key is hashed.
- `xi_api_key_preview` (string, optional, nullable) — The preview of the user's API key.
- `referral_link_code` (string, optional, nullable) — The referral link code of the user.
- `partnerstack_partner_default_link` (string, optional, nullable) — The Partnerstack partner default link of the user.

## Examples

**Response**

```json
{
  "user_id": "1234567890",
  "subscription": {
    "tier": "trial",
    "character_count": 17231,
    "character_limit": 100000,
    "max_character_limit_extension": 10000,
    "max_credit_limit_extension": 10000,
    "can_extend_character_limit": false,
    "allowed_to_extend_character_limit": false,
    "voice_slots_used": 1,
    "professional_voice_slots_used": 0,
    "professional_voice_slots_used_in_workspace": 0,
    "voice_limit": 120,
    "voice_add_edit_counter": 212,
    "professional_voice_limit": 1,
    "can_extend_voice_limit": false,
    "can_use_instant_voice_cloning": true,
    "can_use_professional_voice_cloning": true,
    "current_overage": {
      "amount": "0",
      "currency": "usd"
    },
    "status": "free",
    "next_character_count_reset_unix": 1738356858,
    "max_voice_add_edits": 230,
    "currency": "usd",
    "billing_period": "monthly_period",
    "character_refresh_period": "monthly_period"
  },
  "is_onboarding_completed": true,
  "is_onboarding_checklist_completed": true,
  "created_at": 1753999199,
  "seat_type": "workspace_member",
  "is_new_user": false,
  "can_use_delayed_payment_methods": false,
  "show_compliance_terms": false,
  "first_name": "John",
  "is_api_key_hashed": false
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.user.get();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.user.get()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/user"

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

url = URI("https://api.elevenlabs.io/v1/user")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/user")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/user');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/user");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/user")! as URL,
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
