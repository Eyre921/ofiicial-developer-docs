---
title: "Import phone number"
source: https://elevenlabs.io/docs/api-reference/phone-numbers/create.md
path: docs/api-reference/phone-numbers/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Import phone number

POST https://api.elevenlabs.io/v1/convai/phone-numbers
Content-Type: application/json

Import Phone Number from provider configuration (Twilio, Exotel, or SIP trunk)

Reference: https://elevenlabs.io/docs/api-reference/phone-numbers/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `object or object or object`
  - CreateTwilioPhoneNumberRequest
    - `phone_number` (string, required) — Phone number
    - `label` (string, required) — Label for the phone number
    - `sid` (string, required) — Twilio Account SID
    - `token` (string, required) — Twilio Auth Token
    - `provider` ("twilio", optional, default: twilio)
    - `agent_id` (string, optional, nullable) — Agent ID to assign the phone number to
    - `region_config` (object, optional, nullable) — Twilio Additional Region Configuration
      - `region_id` (enum, required) — Region ID
        - Allowed values: `us1`, `ie1`, `au1`
      - `token` (string, required) — Auth Token for this region
      - `edge_location` (enum, required) — Edge location for this region
        - Allowed values: `ashburn`, `dublin`, `frankfurt`, `sao-paulo`, `singapore`, `sydney`, `tokyo`, `umatilla`, `roaming`
    - `enable_sms` (boolean, optional, default: true) — Route inbound SMS to ElevenLabs. On by default; set to false to skip SMS configuration for numbers that don't support it.
    - `supports_inbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports inbound calls
    - `supports_outbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports outbound calls
  - CreateExotelPhoneNumberRequest
    - `phone_number` (string, required) — Phone number
    - `label` (string, required) — Label for the phone number
    - `account_sid` (string, required) — Exotel Account SID
    - `api_key` (string, required) — Exotel API Key
    - `api_token` (string, required) — Exotel API Token
    - `api_subdomain` (enum, required) — Exotel region-specific API host
      - Allowed values: `api.in.exotel.com`, `api.exotel.com`
    - `app_id` (string, required) — Exotel applet identifier used in Calls/connect
    - `provider` ("exotel", optional, default: exotel)
    - `agent_id` (string, optional, nullable) — Agent ID to assign the phone number to
    - `applet_url` (string, optional, nullable) — Optional full applet URL override. Defaults to Exotel start_voice URL derived from account SID and app ID.
    - `supports_inbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports inbound calls
    - `supports_outbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports outbound calls
  - CreateSIPTrunkPhoneNumberRequestV2
    - `phone_number` (string, required) — Phone number
    - `label` (string, required) — Label for the phone number
    - `provider` ("sip_trunk", optional, default: sip_trunk)
    - `agent_id` (string, optional, nullable) — Agent ID to assign the phone number to
    - `inbound_trunk_config` (object, optional, nullable)
      - `allowed_addresses` (list of string, optional, nullable) — List of IP addresses that are allowed to use the trunk. Each item in the list can be an individual IP address or a Classless Inter-Domain Routing notation representing a CIDR block.
      - `allowed_numbers` (list of string, optional, nullable) — List of phone numbers that are allowed to use the trunk.
      - `media_encryption` (enum, optional, default: allowed) — Whether or not to encrypt media (data layer).
        - Allowed values: `disabled`, `allowed`, `required`
      - `credentials` (object, optional, nullable) — Optional digest authentication credentials (username/password).
        - `username` (string, required) — SIP trunk username
        - `password` (string, optional, nullable) — SIP trunk password - if not specified, then remain unchanged
      - `remote_domains` (list of string, optional, nullable) — Domains of remote SIP servers used to validate TLS certificates.
      - `attributes_to_headers` (map from string to string, optional) — Map of dynamic variable name to header name for attributes_to_headers
    - `outbound_trunk_config` (object, optional, nullable)
      - `address` (string, required) — Hostname or IP the SIP INVITE is sent to.
      - `transport` (enum, optional, default: auto) — Protocol to use for SIP transport (signalling layer).
        - Allowed values: `auto`, `udp`, `tcp`, `tls`
      - `media_encryption` (enum, optional, default: allowed) — Whether or not to encrypt media (data layer).
        - Allowed values: `disabled`, `allowed`, `required`
      - `headers` (map from string to string, optional) — SIP X-* headers for INVITE request. These headers are sent as-is and may help identify this call.
      - `attributes_to_headers` (map from string to string, optional) — Map of dynamic variable name to header name for attributes_to_headers
      - `credentials` (object, optional, nullable) — Optional digest authentication credentials (username/password). If not provided, ACL authentication is assumed.
        - `username` (string, required) — SIP trunk username
        - `password` (string, optional, nullable) — SIP trunk password - if not specified, then remain unchanged
      - `enabled_codecs` (list of enum, optional) — Media codecs that should be offered in the SDP for outbound calls. If empty, all supported codecs are offered.
        - Allowed values: `G722/8000`, `PCMU/8000`, `PCMA/8000`
    - `supports_inbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports inbound calls
    - `supports_outbound` (boolean, optional, default: true, deprecated) — This field is deprecated and will be removed in the future. Whether this phone number supports outbound calls

## Response

### 200

Successful Response

- `phone_number_id` (string, required) — Phone entity ID

## Examples

**Request**

```json
{
  "account_sid": "your-account-sid",
  "api_key": "your-api-key",
  "api_subdomain": "api.in.exotel.com",
  "api_token": "********",
  "app_id": "12345",
  "label": "Exotel Outbound",
  "phone_number": "+919999999999",
  "provider": "exotel"
}
```

**Response**

```json
{
  "phone_number_id": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.phoneNumbers.create({
        provider: "exotel",
        accountSid: "your-account-sid",
        apiKey: "your-api-key",
        apiSubdomain: "api.in.exotel.com",
        apiToken: "********",
        appId: "12345",
        label: "Exotel Outbound",
        phoneNumber: "+919999999999",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs
from elevenlabs.conversational_ai.phone_numbers import PhoneNumbersCreateRequestBody_Exotel

client = ElevenLabs()

client.conversational_ai.phone_numbers.create(
    request=PhoneNumbersCreateRequestBody_Exotel(
        account_sid="your-account-sid",
        api_key="your-api-key",
        api_subdomain="api.in.exotel.com",
        api_token="********",
        app_id="12345",
        label="Exotel Outbound",
        phone_number="+919999999999",
    ),
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

	url := "https://api.elevenlabs.io/v1/convai/phone-numbers"

	payload := strings.NewReader("{\n  \"account_sid\": \"your-account-sid\",\n  \"api_key\": \"your-api-key\",\n  \"api_subdomain\": \"api.in.exotel.com\",\n  \"api_token\": \"********\",\n  \"app_id\": \"12345\",\n  \"label\": \"Exotel Outbound\",\n  \"phone_number\": \"+919999999999\",\n  \"provider\": \"exotel\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/phone-numbers")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"account_sid\": \"your-account-sid\",\n  \"api_key\": \"your-api-key\",\n  \"api_subdomain\": \"api.in.exotel.com\",\n  \"api_token\": \"********\",\n  \"app_id\": \"12345\",\n  \"label\": \"Exotel Outbound\",\n  \"phone_number\": \"+919999999999\",\n  \"provider\": \"exotel\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/phone-numbers")
  .header("Content-Type", "application/json")
  .body("{\n  \"account_sid\": \"your-account-sid\",\n  \"api_key\": \"your-api-key\",\n  \"api_subdomain\": \"api.in.exotel.com\",\n  \"api_token\": \"********\",\n  \"app_id\": \"12345\",\n  \"label\": \"Exotel Outbound\",\n  \"phone_number\": \"+919999999999\",\n  \"provider\": \"exotel\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/phone-numbers', [
  'body' => '{
  "account_sid": "your-account-sid",
  "api_key": "your-api-key",
  "api_subdomain": "api.in.exotel.com",
  "api_token": "********",
  "app_id": "12345",
  "label": "Exotel Outbound",
  "phone_number": "+919999999999",
  "provider": "exotel"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/phone-numbers");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"account_sid\": \"your-account-sid\",\n  \"api_key\": \"your-api-key\",\n  \"api_subdomain\": \"api.in.exotel.com\",\n  \"api_token\": \"********\",\n  \"app_id\": \"12345\",\n  \"label\": \"Exotel Outbound\",\n  \"phone_number\": \"+919999999999\",\n  \"provider\": \"exotel\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "account_sid": "your-account-sid",
  "api_key": "your-api-key",
  "api_subdomain": "api.in.exotel.com",
  "api_token": "********",
  "app_id": "12345",
  "label": "Exotel Outbound",
  "phone_number": "+919999999999",
  "provider": "exotel"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/phone-numbers")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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
