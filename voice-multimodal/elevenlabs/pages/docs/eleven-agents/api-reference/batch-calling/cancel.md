---
title: "Cancel batch calling job"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/cancel.md
path: docs/eleven-agents/api-reference/batch-calling/cancel
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Cancel batch calling job

POST https://api.elevenlabs.io/v1/convai/batch-calling/{batch_id}/cancel

Cancel a running batch call and set all recipients to cancelled status.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/cancel

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/batch-calling/{batch_id}/cancel:
    post:
      operationId: cancel
      summary: Cancel A Batch Call.
      description: Cancel a running batch call and set all recipients to cancelled status.
      tags:
        - batchCalls
      parameters:
        - name: batch_id
          in: path
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
                $ref: '#/components/schemas/type_:BatchCallResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
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
    type_:TelephonyProvider:
      type: string
      enum:
        - twilio
        - sip_trunk
        - exotel
      title: TelephonyProvider
    type_:BatchCallWhatsAppParams:
      type: object
      properties:
        whatsapp_phone_number_id:
          type: string
        whatsapp_call_permission_request_template_name:
          type: string
        whatsapp_call_permission_request_template_language_code:
          type: string
      required:
        - whatsapp_call_permission_request_template_name
        - whatsapp_call_permission_request_template_language_code
      title: BatchCallWhatsAppParams
    type_:BatchCallStatus:
      type: string
      enum:
        - pending
        - in_progress
        - completed
        - failed
        - cancelled
      title: BatchCallStatus
    type_:TelephonyCallConfig:
      type: object
      properties:
        ringing_timeout_secs:
          type: integer
          default: 60
          description: >-
            How long to ring the recipient before giving up, in seconds. Note
            that this will also be limited by the provider's own constraints.
        twilio_call_recording_enabled:
          type: boolean
          default: false
          description: >-
            Whether to record the call using Twilio call recording. Ignored for
            non-Twilio providers. Recordings are stored in your Twilio account.
      title: TelephonyCallConfig
    type_:BatchCallResponse:
      type: object
      properties:
        id:
          type: string
        phone_number_id:
          type: string
        phone_provider:
          $ref: '#/components/schemas/type_:TelephonyProvider'
        whatsapp_params:
          $ref: '#/components/schemas/type_:BatchCallWhatsAppParams'
        name:
          type: string
        agent_id:
          type: string
        branch_id:
          type: string
        environment:
          type: string
        created_at_unix:
          type: integer
        scheduled_time_unix:
          type: integer
        timezone:
          type: string
        total_calls_dispatched:
          type: integer
          default: 0
        total_calls_scheduled:
          type: integer
          default: 0
        total_calls_finished:
          type: integer
          default: 0
        last_updated_at_unix:
          type: integer
        status:
          $ref: '#/components/schemas/type_:BatchCallStatus'
        retry_count:
          type: integer
          default: 0
        telephony_call_config:
          $ref: '#/components/schemas/type_:TelephonyCallConfig'
        target_concurrency_limit:
          type: integer
          description: >-
            Maximum number of simultaneous calls for this batch. When set,
            dispatch is governed by this limit rather than workspace/agent
            capacity percentages.
        agent_name:
          type: string
        branch_name:
          type: string
      required:
        - id
        - name
        - agent_id
        - created_at_unix
        - scheduled_time_unix
        - total_calls_dispatched
        - total_calls_scheduled
        - total_calls_finished
        - last_updated_at_unix
        - status
        - retry_count
        - telephony_call_config
        - agent_name
      title: BatchCallResponse
    type_:ValidationErrorLocItem:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItem
    type_:ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationErrorLocItem'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    type_:HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationError'
      title: HTTPValidationError

```

## Examples

**Response**

```json
{
  "id": "id",
  "name": "name",
  "agent_id": "agent_id",
  "created_at_unix": 1,
  "scheduled_time_unix": 1,
  "total_calls_dispatched": 1,
  "total_calls_scheduled": 1,
  "total_calls_finished": 1,
  "last_updated_at_unix": 1,
  "status": "pending",
  "retry_count": 1,
  "telephony_call_config": {
    "ringing_timeout_secs": 1,
    "twilio_call_recording_enabled": true
  },
  "agent_name": "agent_name",
  "phone_number_id": "phone_number_id",
  "phone_provider": "twilio",
  "whatsapp_params": {
    "whatsapp_call_permission_request_template_name": "whatsapp_call_permission_request_template_name",
    "whatsapp_call_permission_request_template_language_code": "whatsapp_call_permission_request_template_language_code",
    "whatsapp_phone_number_id": "whatsapp_phone_number_id"
  },
  "branch_id": "branch_id",
  "environment": "environment",
  "timezone": "timezone",
  "target_concurrency_limit": 1,
  "branch_name": "branch_name"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.batchCalls.cancel("batch_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.batch_calls.cancel(
    batch_id="batch_id",
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/cancel"

	req, _ := http.NewRequest("POST", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/cancel")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/cancel")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/cancel');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/cancel");
var request = new RestRequest(Method.POST);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/batch-calling/batch_id/cancel")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"

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
