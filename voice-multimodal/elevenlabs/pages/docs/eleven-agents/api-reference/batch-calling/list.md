---
title: "List workspace batch calling jobs"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/list.md
path: docs/eleven-agents/api-reference/batch-calling/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List workspace batch calling jobs

GET https://api.elevenlabs.io/v1/convai/batch-calling/workspace

Get all batch calls for the current workspace.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/batch-calling/workspace:
    get:
      operationId: list
      summary: Get All Batch Calls For A Workspace.
      description: Get all batch calls for the current workspace.
      tags:
        - batchCalls
      parameters:
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            default: 100
        - name: last_doc
          in: query
          required: false
          schema:
            type: string
        - name: agent_id
          in: query
          description: Filter batch calls to a single agent.
          required: false
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
                $ref: '#/components/schemas/type_:WorkspaceBatchCallsResponse'
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
    type_:WorkspaceBatchCallsResponse:
      type: object
      properties:
        batch_calls:
          type: array
          items:
            $ref: '#/components/schemas/type_:BatchCallResponse'
        next_doc:
          type: string
          description: The next document, used to paginate through the batch calls
        has_more:
          type: boolean
          default: false
          description: Whether there are more batch calls to paginate through
      required:
        - batch_calls
      title: WorkspaceBatchCallsResponse
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

**Request**

```json
{}
```

**Response**

```json
{
  "batch_calls": [
    {
      "id": "bc_9f8a7c6d-1234-4e56-8b9a-0f1e2d3c4b5a",
      "name": "April Marketing Campaign Batch",
      "agent_id": "agent_42f7e8d9-0abc-4def-9a12-3456789bcdef",
      "created_at_unix": 1712000000,
      "scheduled_time_unix": 1712604800,
      "total_calls_dispatched": 150,
      "total_calls_scheduled": 200,
      "total_calls_finished": 140,
      "last_updated_at_unix": 1712650000,
      "status": "pending",
      "retry_count": 2,
      "telephony_call_config": {
        "ringing_timeout_secs": 45,
        "twilio_call_recording_enabled": true
      },
      "agent_name": "Sales Outreach Bot",
      "phone_number_id": "pn_7d3f2a1b-4567-4c89-9e0f-1a2b3c4d5e6f",
      "phone_provider": "twilio",
      "whatsapp_params": {
        "whatsapp_call_permission_request_template_name": "customer_permission_request",
        "whatsapp_call_permission_request_template_language_code": "en_US",
        "whatsapp_phone_number_id": "wpn_1234567890abcdef"
      },
      "branch_id": "branch_nyc_office",
      "environment": "production",
      "timezone": "America/New_York",
      "target_concurrency_limit": 20,
      "branch_name": "New York City Office"
    }
  ],
  "next_doc": "bc_9f8a7c6d-1234-4e56-8b9a-0f1e2d3c4b5b",
  "has_more": true
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.batchCalls.list({
        agentId: "agent_id",
        lastDoc: "last_doc",
        limit: 1,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.batch_calls.list(
    agent_id="agent_id",
    last_doc="last_doc",
    limit=1,
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

	url := "https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/batch-calling/workspace?agent_id=agent_id&last_doc=last_doc&limit=1")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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
