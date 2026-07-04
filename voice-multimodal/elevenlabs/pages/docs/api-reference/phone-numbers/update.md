---
title: "Update phone number"
source: https://elevenlabs.io/docs/api-reference/phone-numbers/update.md
path: docs/api-reference/phone-numbers/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update phone number

PATCH https://api.elevenlabs.io/v1/convai/phone-numbers/{phone_number_id}
Content-Type: application/json

Update assigned agent of a phone number

Reference: https://elevenlabs.io/docs/api-reference/phone-numbers/update

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/phone-numbers/{phone_number_id}:
    patch:
      operationId: update
      summary: Update Phone Number
      description: Update assigned agent of a phone number
      tags:
        - phoneNumbers
      parameters:
        - name: phone_number_id
          in: path
          description: >-
            The phone number ID. This is returned when a phone number is
            imported.
          required: true
          schema:
            type: string
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
                $ref: >-
                  #/components/schemas/conversational_ai_phone_numbers_update_Response_200
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
              $ref: '#/components/schemas/UpdatePhoneNumberRequest'
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
    LivekitStackType:
      type: string
      enum:
        - standard
        - static
      default: standard
      title: LivekitStackType
    UpdatePhoneNumberRequest:
      type: object
      properties:
        agent_id:
          type:
            - string
            - 'null'
        label:
          type:
            - string
            - 'null'
        inbound_trunk_config:
          oneOf:
            - $ref: '#/components/schemas/InboundSIPTrunkConfigRequestModel'
            - type: 'null'
        outbound_trunk_config:
          oneOf:
            - $ref: '#/components/schemas/OutboundSIPTrunkConfigRequestModel'
            - type: 'null'
        livekit_stack:
          oneOf:
            - $ref: '#/components/schemas/LivekitStackType'
            - type: 'null'
        store_sip_messages:
          type:
            - boolean
            - 'null'
        environment:
          type:
            - string
            - 'null'
          description: >-
            Environment to use for resolving environment variables on calls to
            this number.
        branch_id:
          type:
            - string
            - 'null'
          description: Agent branch to use for calls to this number.
      title: UpdatePhoneNumberRequest
    PhoneNumberAgentInfo:
      type: object
      properties:
        agent_id:
          type: string
          description: The ID of the agent
        agent_name:
          type: string
          description: The name of the agent
        environment:
          type:
            - string
            - 'null'
          description: >-
            Environment to use for resolving environment variables on calls to
            this number.
        branch_id:
          type:
            - string
            - 'null'
          description: Agent branch to use for calls to this number.
      required:
        - agent_id
        - agent_name
      title: PhoneNumberAgentInfo
    GetPhoneNumberOutboundSIPTrunkConfigResponseModel:
      type: object
      properties:
        address:
          type: string
          description: Hostname or IP the SIP INVITE is sent to
        transport:
          $ref: '#/components/schemas/SIPTrunkTransportEnum'
          description: Protocol to use for SIP transport
        media_encryption:
          $ref: '#/components/schemas/SIPMediaEncryptionEnum'
          description: Whether or not to encrypt media (data layer).
        headers:
          type: object
          additionalProperties:
            type: string
          description: SIP headers for INVITE request
        attributes_to_headers:
          type: object
          additionalProperties:
            type: string
          description: >-
            Map of dynamic variable name to header name for
            attributes_to_headers
        has_auth_credentials:
          type: boolean
          description: Whether authentication credentials are configured
        username:
          type:
            - string
            - 'null'
          description: SIP trunk username (if available)
        has_outbound_trunk:
          type: boolean
          default: false
          description: Whether a LiveKit SIP outbound trunk is configured
        enabled_codecs:
          type: array
          items:
            $ref: '#/components/schemas/MediaCodec'
          description: >-
            Media codecs that are offered in the SDP for outbound calls. If
            empty, all supported codecs are offered.
      required:
        - address
        - transport
        - media_encryption
        - has_auth_credentials
      description: SIP Trunk configuration details for a phone number
      title: GetPhoneNumberOutboundSIPTrunkConfigResponseModel
    GetPhoneNumberInboundSIPTrunkConfigResponseModel:
      type: object
      properties:
        allowed_addresses:
          type: array
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
        has_auth_credentials:
          type: boolean
          description: Whether authentication credentials are configured
        username:
          type:
            - string
            - 'null'
          description: SIP trunk username (if available)
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
      required:
        - allowed_addresses
        - allowed_numbers
        - media_encryption
        - has_auth_credentials
      title: GetPhoneNumberInboundSIPTrunkConfigResponseModel
    conversational_ai_phone_numbers_update_Response_200:
      oneOf:
        - type: object
          properties:
            provider:
              type: string
              enum:
                - twilio
              description: 'Discriminator value: twilio'
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
                This field is deprecated and will be removed in the future.
                Whether this phone number supports inbound calls
            supports_outbound:
              type: boolean
              default: true
              description: >-
                This field is deprecated and will be removed in the future.
                Whether this phone number supports outbound calls
            phone_number_id:
              type: string
              description: The ID of the phone number
            assigned_agent:
              oneOf:
                - $ref: '#/components/schemas/PhoneNumberAgentInfo'
                - type: 'null'
              description: The agent that is assigned to the phone number
          required:
            - provider
            - phone_number
            - label
            - phone_number_id
          description: GetPhoneNumberTwilioResponseModel variant
        - type: object
          properties:
            provider:
              type: string
              enum:
                - exotel
              description: 'Discriminator value: exotel'
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
                This field is deprecated and will be removed in the future.
                Whether this phone number supports inbound calls
            supports_outbound:
              type: boolean
              default: true
              description: >-
                This field is deprecated and will be removed in the future.
                Whether this phone number supports outbound calls
            phone_number_id:
              type: string
              description: The ID of the phone number
            assigned_agent:
              oneOf:
                - $ref: '#/components/schemas/PhoneNumberAgentInfo'
                - type: 'null'
              description: The agent that is assigned to the phone number
          required:
            - provider
            - phone_number
            - label
            - phone_number_id
          description: GetPhoneNumberExotelResponseModel variant
        - type: object
          properties:
            provider:
              type: string
              enum:
                - sip_trunk
              description: 'Discriminator value: sip_trunk'
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
                This field is deprecated and will be removed in the future.
                Whether this phone number supports inbound calls
            supports_outbound:
              type: boolean
              default: true
              description: >-
                This field is deprecated and will be removed in the future.
                Whether this phone number supports outbound calls
            phone_number_id:
              type: string
              description: The ID of the phone number
            assigned_agent:
              oneOf:
                - $ref: '#/components/schemas/PhoneNumberAgentInfo'
                - type: 'null'
              description: The agent that is assigned to the phone number
            provider_config:
              oneOf:
                - $ref: >-
                    #/components/schemas/GetPhoneNumberOutboundSIPTrunkConfigResponseModel
                - type: 'null'
            outbound_trunk:
              oneOf:
                - $ref: >-
                    #/components/schemas/GetPhoneNumberOutboundSIPTrunkConfigResponseModel
                - type: 'null'
              description: Configuration of the Outbound SIP trunk - if configured.
            inbound_trunk:
              oneOf:
                - $ref: >-
                    #/components/schemas/GetPhoneNumberInboundSIPTrunkConfigResponseModel
                - type: 'null'
              description: Configuration of the Inbound SIP trunk - if configured.
            livekit_stack:
              $ref: '#/components/schemas/LivekitStackType'
              description: Type of Livekit stack used for this number.
            store_sip_messages:
              type: boolean
              default: true
              description: Whether to store SIP messages for this phone number.
          required:
            - provider
            - phone_number
            - label
            - phone_number_id
            - livekit_stack
          description: GetPhoneNumberSIPTrunkResponseModel variant
      discriminator:
        propertyName: provider
      title: conversational_ai_phone_numbers_update_Response_200
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
{}
```

**Response**

```json
{
  "provider": "twilio",
  "label": "Customer Support",
  "phone_number": "+1234567890",
  "phone_number_id": "phone_123"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.phoneNumbers.update("phone_number_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.phone_numbers.update(
    phone_number_id="phone_number_id",
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

	url := "https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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
