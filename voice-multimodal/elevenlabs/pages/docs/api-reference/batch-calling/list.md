---
title: "List workspace batch calling jobs"
source: https://elevenlabs.io/docs/api-reference/batch-calling/list.md
path: docs/api-reference/batch-calling/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List workspace batch calling jobs

GET https://api.elevenlabs.io/v1/convai/batch-calling/workspace

Get all batch calls for the current workspace.

Reference: https://elevenlabs.io/docs/api-reference/batch-calling/list

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
        - subpackage_conversationalAi/batchCalls
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
            type:
              - string
              - 'null'
        - name: agent_id
          in: query
          description: Filter batch calls to a single agent.
          required: false
          schema:
            type:
              - string
              - 'null'
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
                $ref: '#/components/schemas/WorkspaceBatchCallsResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
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
    TelephonyProvider:
      type: string
      enum:
        - twilio
        - sip_trunk
        - exotel
      title: TelephonyProvider
    BatchCallWhatsAppParams:
      type: object
      properties:
        whatsapp_phone_number_id:
          type:
            - string
            - 'null'
        whatsapp_call_permission_request_template_name:
          type: string
        whatsapp_call_permission_request_template_language_code:
          type: string
      required:
        - whatsapp_call_permission_request_template_name
        - whatsapp_call_permission_request_template_language_code
      title: BatchCallWhatsAppParams
    BatchCallStatus:
      type: string
      enum:
        - pending
        - in_progress
        - completed
        - failed
        - cancelled
      title: BatchCallStatus
    TelephonyCallConfig:
      type: object
      properties:
        ringing_timeout_secs:
          type: integer
          default: 60
          description: >-
            How long to ring the recipient before giving up, in seconds. Note
            that this will also be limited by the provider's own constraints.
      title: TelephonyCallConfig
    BatchCallResponse:
      type: object
      properties:
        id:
          type: string
        phone_number_id:
          type:
            - string
            - 'null'
        phone_provider:
          oneOf:
            - $ref: '#/components/schemas/TelephonyProvider'
            - type: 'null'
        whatsapp_params:
          oneOf:
            - $ref: '#/components/schemas/BatchCallWhatsAppParams'
            - type: 'null'
        name:
          type: string
        agent_id:
          type: string
        branch_id:
          type:
            - string
            - 'null'
        environment:
          type:
            - string
            - 'null'
        created_at_unix:
          type: integer
        scheduled_time_unix:
          type: integer
        timezone:
          type:
            - string
            - 'null'
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
          $ref: '#/components/schemas/BatchCallStatus'
        retry_count:
          type: integer
          default: 0
        telephony_call_config:
          $ref: '#/components/schemas/TelephonyCallConfig'
        target_concurrency_limit:
          type:
            - integer
            - 'null'
          description: >-
            Maximum number of simultaneous calls for this batch. When set,
            dispatch is governed by this limit rather than workspace/agent
            capacity percentages.
        agent_name:
          type: string
        branch_name:
          type:
            - string
            - 'null'
      required:
        - id
        - phone_number_id
        - phone_provider
        - whatsapp_params
        - name
        - agent_id
        - branch_id
        - environment
        - created_at_unix
        - scheduled_time_unix
        - timezone
        - total_calls_dispatched
        - total_calls_scheduled
        - total_calls_finished
        - last_updated_at_unix
        - status
        - retry_count
        - telephony_call_config
        - target_concurrency_limit
        - agent_name
        - branch_name
      title: BatchCallResponse
    WorkspaceBatchCallsResponse:
      type: object
      properties:
        batch_calls:
          type: array
          items:
            $ref: '#/components/schemas/BatchCallResponse'
        next_doc:
          type:
            - string
            - 'null'
          description: The next document, used to paginate through the batch calls
        has_more:
          type: boolean
          default: false
          description: Whether there are more batch calls to paginate through
      required:
        - batch_calls
      title: WorkspaceBatchCallsResponse
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



**Response**

```json
{
  "batch_calls": [
    {
      "id": "string",
      "phone_number_id": "string",
      "phone_provider": "twilio",
      "whatsapp_params": {
        "whatsapp_call_permission_request_template_name": "string",
        "whatsapp_call_permission_request_template_language_code": "string",
        "whatsapp_phone_number_id": "string"
      },
      "name": "string",
      "agent_id": "string",
      "branch_id": "string",
      "environment": "string",
      "created_at_unix": 1,
      "scheduled_time_unix": 1,
      "timezone": "string",
      "total_calls_dispatched": 0,
      "total_calls_scheduled": 0,
      "total_calls_finished": 0,
      "last_updated_at_unix": 1,
      "status": "pending",
      "retry_count": 0,
      "telephony_call_config": {
        "ringing_timeout_secs": 60
      },
      "target_concurrency_limit": 1,
      "agent_name": "string",
      "branch_name": "string"
    }
  ],
  "next_doc": "string",
  "has_more": false
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.batchCalls.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.batch_calls.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/batch-calling/workspace"

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

url = URI("https://api.elevenlabs.io/v1/convai/batch-calling/workspace")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/batch-calling/workspace")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/batch-calling/workspace');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/batch-calling/workspace");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/batch-calling/workspace")! as URL,
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
