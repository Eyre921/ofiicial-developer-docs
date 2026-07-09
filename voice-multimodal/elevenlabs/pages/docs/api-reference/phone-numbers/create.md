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

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/phone-numbers:
    post:
      operationId: create
      summary: Import Phone Number
      description: >-
        Import Phone Number from provider configuration (Twilio, Exotel, or SIP
        trunk)
      tags:
        - phoneNumbers
      parameters:
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreatePhoneNumberResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/conversational_ai_phone_numbers_create_Request
servers:
  - url: https://api.elevenlabs.io
    description: Production
  - url: https://api.us.elevenlabs.io
    description: Production US
  - url: https://api.eu.residency.elevenlabs.io
    description: Production EU
  - url: https://api.in.residency.elevenlabs.io
    description: Production India
  - url: https://api.sg.residency.elevenlabs.io
    description: Production Singapore
components:
  schemas:
    TwilioRegionId:
      type: string
      enum:
        - us1
        - ie1
        - au1
      description: Valid Twilio region IDs.
      title: TwilioRegionId
    TwilioEdgeLocation:
      type: string
      enum:
        - ashburn
        - dublin
        - frankfurt
        - sao-paulo
        - singapore
        - sydney
        - tokyo
        - umatilla
        - roaming
      description: Valid Twilio edge locations.
      title: TwilioEdgeLocation
    RegionConfigRequest:
      type: object
      properties:
        region_id:
          $ref: '#/components/schemas/TwilioRegionId'
          description: Region ID
        token:
          type: string
          description: Auth Token for this region
        edge_location:
          $ref: '#/components/schemas/TwilioEdgeLocation'
          description: Edge location for this region
      required:
        - region_id
        - token
        - edge_location
      title: RegionConfigRequest
    CreateTwilioPhoneNumberRequest:
      type: object
      properties:
        phone_number:
          type: string
          description: Phone number
        label:
          type: string
          description: Label for the phone number
        supports_inbound:
          type: boolean
          default: true
          description: >-
            This field is deprecated and will be removed in the future. Whether
            this phone number supports inbound calls
        supports_outbound:
          type: boolean
          default: true
          description: >-
            This field is deprecated and will be removed in the future. Whether
            this phone number supports outbound calls
        provider:
          type: string
          enum:
            - twilio
          default: twilio
        agent_id:
          type:
            - string
            - 'null'
          description: Agent ID to assign the phone number to
        sid:
          type: string
          description: Twilio Account SID
        token:
          type: string
          description: Twilio Auth Token
        region_config:
          oneOf:
            - $ref: '#/components/schemas/RegionConfigRequest'
            - type: 'null'
          description: Twilio Additional Region Configuration
        enable_sms:
          type: boolean
          default: true
          description: >-
            Route inbound SMS to ElevenLabs. On by default; set to false to skip
            SMS configuration for numbers that don't support it.
      required:
        - phone_number
        - label
        - sid
        - token
      title: CreateTwilioPhoneNumberRequest
    ExotelApiSubdomain:
      type: string
      enum:
        - api.in.exotel.com
        - api.exotel.com
      title: ExotelApiSubdomain
    CreateExotelPhoneNumberRequest:
      type: object
      properties:
        phone_number:
          type: string
          description: Phone number
        label:
          type: string
          description: Label for the phone number
        supports_inbound:
          type: boolean
          default: true
          description: >-
            This field is deprecated and will be removed in the future. Whether
            this phone number supports inbound calls
        supports_outbound:
          type: boolean
          default: true
          description: >-
            This field is deprecated and will be removed in the future. Whether
            this phone number supports outbound calls
        provider:
          type: string
          enum:
            - exotel
          default: exotel
        agent_id:
          type:
            - string
            - 'null'
          description: Agent ID to assign the phone number to
        account_sid:
          type: string
          description: Exotel Account SID
        api_key:
          type: string
          description: Exotel API Key
        api_token:
          type: string
          description: Exotel API Token
        api_subdomain:
          $ref: '#/components/schemas/ExotelApiSubdomain'
          description: Exotel region-specific API host
        app_id:
          type: string
          description: Exotel applet identifier used in Calls/connect
        applet_url:
          type:
            - string
            - 'null'
          description: >-
            Optional full applet URL override. Defaults to Exotel start_voice
            URL derived from account SID and app ID.
      required:
        - phone_number
        - label
        - account_sid
        - api_key
        - api_token
        - api_subdomain
        - app_id
      title: CreateExotelPhoneNumberRequest
    SIPMediaEncryptionEnum:
      type: string
      enum:
        - disabled
        - allowed
        - required
      default: allowed
      title: SIPMediaEncryptionEnum
    SIPTrunkCredentialsRequestModel:
      type: object
      properties:
        username:
          type: string
          description: SIP trunk username
        password:
          type:
            - string
            - 'null'
          description: SIP trunk password - if not specified, then remain unchanged
      required:
        - username
      title: SIPTrunkCredentialsRequestModel
    InboundSIPTrunkConfigRequestModel:
      type: object
      properties:
        allowed_addresses:
          type:
            - array
            - 'null'
          items:
            type: string
          description: >-
            List of IP addresses that are allowed to use the trunk. Each item in
            the list can be an individual IP address or a Classless Inter-Domain
            Routing notation representing a CIDR block.
        allowed_numbers:
          type:
            - array
            - 'null'
          items:
            type: string
          description: List of phone numbers that are allowed to use the trunk.
        media_encryption:
          $ref: '#/components/schemas/SIPMediaEncryptionEnum'
          default: allowed
          description: Whether or not to encrypt media (data layer).
        credentials:
          oneOf:
            - $ref: '#/components/schemas/SIPTrunkCredentialsRequestModel'
            - type: 'null'
          description: Optional digest authentication credentials (username/password).
        remote_domains:
          type:
            - array
            - 'null'
          items:
            type: string
          description: Domains of remote SIP servers used to validate TLS certificates.
        attributes_to_headers:
          type: object
          additionalProperties:
            type: string
          description: >-
            Map of dynamic variable name to header name for
            attributes_to_headers
      title: InboundSIPTrunkConfigRequestModel
    SIPTrunkTransportEnum:
      type: string
      enum:
        - auto
        - udp
        - tcp
        - tls
      default: auto
      title: SIPTrunkTransportEnum
    MediaCodec:
      type: string
      enum:
        - G722/8000
        - PCMU/8000
        - PCMA/8000
      title: MediaCodec
    OutboundSIPTrunkConfigRequestModel:
      type: object
      properties:
        address:
          type: string
          description: Hostname or IP the SIP INVITE is sent to.
        transport:
          $ref: '#/components/schemas/SIPTrunkTransportEnum'
          default: auto
          description: Protocol to use for SIP transport (signalling layer).
        media_encryption:
          $ref: '#/components/schemas/SIPMediaEncryptionEnum'
          default: allowed
          description: Whether or not to encrypt media (data layer).
        headers:
          type: object
          additionalProperties:
            type: string
          description: >-
            SIP X-* headers for INVITE request. These headers are sent as-is and
            may help identify this call.
        attributes_to_headers:
          type: object
          additionalProperties:
            type: string
          description: >-
            Map of dynamic variable name to header name for
            attributes_to_headers
        credentials:
          oneOf:
            - $ref: '#/components/schemas/SIPTrunkCredentialsRequestModel'
            - type: 'null'
          description: >-
            Optional digest authentication credentials (username/password). If
            not provided, ACL authentication is assumed.
        enabled_codecs:
          type: array
          items:
            $ref: '#/components/schemas/MediaCodec'
          description: >-
            Media codecs that should be offered in the SDP for outbound calls.
            If empty, all supported codecs are offered.
      required:
        - address
      title: OutboundSIPTrunkConfigRequestModel
    CreateSIPTrunkPhoneNumberRequestV2:
      type: object
      properties:
        phone_number:
          type: string
          description: Phone number
        label:
          type: string
          description: Label for the phone number
        supports_inbound:
          type: boolean
          default: true
          description: >-
            This field is deprecated and will be removed in the future. Whether
            this phone number supports inbound calls
        supports_outbound:
          type: boolean
          default: true
          description: >-
            This field is deprecated and will be removed in the future. Whether
            this phone number supports outbound calls
        provider:
          type: string
          enum:
            - sip_trunk
          default: sip_trunk
        agent_id:
          type:
            - string
            - 'null'
          description: Agent ID to assign the phone number to
        inbound_trunk_config:
          oneOf:
            - $ref: '#/components/schemas/InboundSIPTrunkConfigRequestModel'
            - type: 'null'
        outbound_trunk_config:
          oneOf:
            - $ref: '#/components/schemas/OutboundSIPTrunkConfigRequestModel'
            - type: 'null'
      required:
        - phone_number
        - label
      title: CreateSIPTrunkPhoneNumberRequestV2
    conversational_ai_phone_numbers_create_Request:
      oneOf:
        - $ref: '#/components/schemas/CreateTwilioPhoneNumberRequest'
        - $ref: '#/components/schemas/CreateExotelPhoneNumberRequest'
        - $ref: '#/components/schemas/CreateSIPTrunkPhoneNumberRequestV2'
      description: Create Phone Request Information
      title: conversational_ai_phone_numbers_create_Request
    CreatePhoneNumberResponseModel:
      type: object
      properties:
        phone_number_id:
          type: string
          description: Phone entity ID
      required:
        - phone_number_id
      title: CreatePhoneNumberResponseModel
    ValidationErrorLocItems:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItems
    ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/ValidationErrorLocItems'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
      title: HTTPValidationError

```

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
