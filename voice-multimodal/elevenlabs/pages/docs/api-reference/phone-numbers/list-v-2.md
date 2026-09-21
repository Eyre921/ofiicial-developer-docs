---
title: "List Phone Numbers Page"
source: https://elevenlabs.io/docs/api-reference/phone-numbers/list-v-2.md
path: docs/api-reference/phone-numbers/list-v-2
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List Phone Numbers Page

GET https://api.elevenlabs.io/v1/convai/v2/phone-numbers

Retrieve a page of Phone Numbers

Reference: https://elevenlabs.io/docs/api-reference/phone-numbers/list-v-2

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `page_size` (integer, optional, default: 100) — Number of phone numbers per page
- `search` (string, optional, nullable) — Filter by phone number ID, label, or phone number. A phone number ID must match exactly; label and phone number matching is a case-insensitive substring.
- `label` (string, optional, nullable) — Filter by label. Matching is a case-insensitive substring.
- `phone_number` (string, optional, nullable) — Filter by phone number
- `provider` (enum, optional, nullable) — Filter by telephony provider
  - Allowed values: `twilio`, `sip_trunk`, `exotel`
- `supports_outbound` (boolean, optional, nullable) — Filter by whether the phone number can place outbound calls
- `agent_id` (string, optional, nullable) — Filter by assigned agent ID
- `branch_id` (string, optional, nullable) — Filter by assigned branch ID
- `sort_by` (enum, optional, nullable) — The field to sort the results by
  - Allowed values: `label`, `phone_number`
- `sort_direction` (enum, optional) — The direction to sort the results
  - Allowed values: `asc`, `desc`
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `phone_numbers` (list of object, required) — The phone numbers on this page
  - `provider`: `exotel` (GetPhoneNumberExotelResponseModel)
    - `label` (string, required) — Label for the phone number
    - `phone_number` (string, required) — Phone number
    - `phone_number_id` (string, required) — The ID of the phone number
    - `assigned_agent` (object, optional, nullable) — The agent that is assigned to the phone number
      - `agent_id` (string, required) — The ID of the agent
      - `agent_name` (string, required) — The name of the agent
      - `environment` (string, optional, nullable) — Environment to use for resolving environment variables on calls to this number.
      - `branch_id` (string, optional, nullable) — Agent branch to use for calls to this number.
    - `supports_inbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports inbound calls
    - `supports_outbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports outbound calls
  - `provider`: `sip_trunk` (GetPhoneNumberSIPTrunkResponseModel)
    - `label` (string, required) — Label for the phone number
    - `livekit_stack` (enum, required, default: standard) — Type of Livekit stack used for this number.
      - Allowed values: `standard`, `static`
    - `phone_number` (string, required) — Phone number
    - `phone_number_id` (string, required) — The ID of the phone number
    - `assigned_agent` (object, optional, nullable) — The agent that is assigned to the phone number
      - `agent_id` (string, required) — The ID of the agent
      - `agent_name` (string, required) — The name of the agent
      - `environment` (string, optional, nullable) — Environment to use for resolving environment variables on calls to this number.
      - `branch_id` (string, optional, nullable) — Agent branch to use for calls to this number.
    - `inbound_trunk` (object, optional, nullable) — Configuration of the Inbound SIP trunk - if configured.
      - `allowed_addresses` (list of string, required) — List of IP addresses that are allowed to use the trunk. Each item in the list can be an individual IP address or a Classless Inter-Domain Routing notation representing a CIDR block.
      - `allowed_numbers` (list of string, required, nullable) — List of phone numbers that are allowed to use the trunk.
      - `media_encryption` (enum, required, default: allowed)
        - Allowed values: `disabled`, `allowed`, `required`
      - `has_auth_credentials` (boolean, required) — Whether authentication credentials are configured
      - `username` (string, optional, nullable) — SIP trunk username (if available)
      - `remote_domains` (list of string, optional, nullable) — Domains of remote SIP servers used to validate TLS certificates.
      - `attributes_to_headers` (map from string to string, optional) — Map of dynamic variable name to header name for attributes_to_headers
    - `outbound_trunk` (object, optional, nullable) — Configuration of the Outbound SIP trunk - if configured.
      - `address` (string, required) — Hostname or IP the SIP INVITE is sent to
      - `transport` (enum, required, default: auto) — Protocol to use for SIP transport
        - Allowed values: `auto`, `udp`, `tcp`, `tls`
      - `media_encryption` (enum, required, default: allowed) — Whether or not to encrypt media (data layer).
        - Allowed values: `disabled`, `allowed`, `required`
      - `has_auth_credentials` (boolean, required) — Whether authentication credentials are configured
      - `headers` (map from string to string, optional) — SIP headers for INVITE request
      - `attributes_to_headers` (map from string to string, optional) — Map of dynamic variable name to header name for attributes_to_headers
      - `username` (string, optional, nullable) — SIP trunk username (if available)
      - `has_outbound_trunk` (boolean, optional, default: false) — Whether a LiveKit SIP outbound trunk is configured
      - `enabled_codecs` (list of enum, optional) — Media codecs that are offered in the SDP for outbound calls. If empty, all supported codecs are offered.
        - Allowed values: `G722/8000`, `PCMU/8000`, `PCMA/8000`
    - `store_sip_messages` (boolean, optional, default: true) — Whether to store SIP messages for this phone number.
    - `provider_config` (object, optional, nullable, deprecated) — SIP Trunk configuration details for a phone number
      - `address` (string, required) — Hostname or IP the SIP INVITE is sent to
      - `transport` (enum, required, default: auto) — Protocol to use for SIP transport
        - Allowed values: `auto`, `udp`, `tcp`, `tls`
      - `media_encryption` (enum, required, default: allowed) — Whether or not to encrypt media (data layer).
        - Allowed values: `disabled`, `allowed`, `required`
      - `has_auth_credentials` (boolean, required) — Whether authentication credentials are configured
      - `headers` (map from string to string, optional) — SIP headers for INVITE request
      - `attributes_to_headers` (map from string to string, optional) — Map of dynamic variable name to header name for attributes_to_headers
      - `username` (string, optional, nullable) — SIP trunk username (if available)
      - `has_outbound_trunk` (boolean, optional, default: false) — Whether a LiveKit SIP outbound trunk is configured
      - `enabled_codecs` (list of enum, optional) — Media codecs that are offered in the SDP for outbound calls. If empty, all supported codecs are offered.
        - Allowed values: `G722/8000`, `PCMU/8000`, `PCMA/8000`
    - `supports_inbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports inbound calls
    - `supports_outbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports outbound calls
  - `provider`: `twilio` (GetPhoneNumberTwilioResponseModel)
    - `label` (string, required) — Label for the phone number
    - `phone_number` (string, required) — Phone number
    - `phone_number_id` (string, required) — The ID of the phone number
    - `assigned_agent` (object, optional, nullable) — The agent that is assigned to the phone number
      - `agent_id` (string, required) — The ID of the agent
      - `agent_name` (string, required) — The name of the agent
      - `environment` (string, optional, nullable) — Environment to use for resolving environment variables on calls to this number.
      - `branch_id` (string, optional, nullable) — Agent branch to use for calls to this number.
    - `supports_inbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports inbound calls
    - `supports_outbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports outbound calls
- `next_cursor` (string, optional, nullable) — Pass this value as `cursor` to fetch the next page. Null when there are no more results.
- `has_more` (boolean, optional, default: false) — Whether there are more results available

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of object, optional)
  - `loc` (list of string or integer, required)
  - `msg` (string, required)
  - `type` (string, required)

## Examples

**Response**

```json
{
  "phone_numbers": [
    {
      "provider": "twilio",
      "label": "Customer Support",
      "phone_number": "+1234567890",
      "phone_number_id": "phone_123"
    }
  ],
  "next_cursor": "string",
  "has_more": false
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.phoneNumbers.listV2({});
}
main();

```

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/v2/phone-numbers"

response = requests.get(url)

print(response.json())
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/v2/phone-numbers"

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

url = URI("https://api.elevenlabs.io/v1/convai/v2/phone-numbers")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/v2/phone-numbers")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/v2/phone-numbers');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/v2/phone-numbers");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/v2/phone-numbers")! as URL,
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
