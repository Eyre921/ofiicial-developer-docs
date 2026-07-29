---
title: "List Procedures"
source: https://elevenlabs.io/docs/api-reference/agents/procedures/list.md
path: docs/api-reference/agents/procedures/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List Procedures

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches/{branch_id}/procedures

List the agent's procedures on a branch with their procedure_id, version_id, name, type, trigger, and has_draft. has_draft is true when a procedure has unpublished draft changes on this branch; its name/type/trigger then reflect that draft. Does not return procedure content -- use Get Procedure to read a procedure's body.

Reference: https://elevenlabs.io/docs/api-reference/agents/procedures/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures:
    get:
      operationId: list
      summary: List Procedures
      description: >-
        List the agent's procedures on a branch with their procedure_id,
        version_id, name, type, trigger, and has_draft. has_draft is true when a
        procedure has unpublished draft changes on this branch; its
        name/type/trigger then reflect that draft. Does not return procedure
        content -- use Get Procedure to read a procedure's body.
      tags:
        - procedures
      parameters:
        - name: agent_id
          in: path
          description: Agent ID to get the procedure draft from
          required: true
          schema:
            type: string
        - name: branch_id
          in: path
          description: Branch ID to get the procedure draft from
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
                $ref: '#/components/schemas/ListProceduresResponseModel'
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
    ProcedureType:
      type: string
      enum:
        - free_form
        - deterministic
      default: free_form
      title: ProcedureType
    ProcedureListItemResponseModel:
      type: object
      properties:
        procedure_id:
          type: string
          description: Procedure ID
        version_id:
          type:
            - string
            - 'null'
          description: >-
            Version ID of a version of the procedure. None for a procedure never
            versioned.
        name:
          type: string
          default: ''
          description: Procedure name
        type:
          $ref: '#/components/schemas/ProcedureType'
          default: free_form
          description: Procedure type
        trigger:
          type: string
          default: ''
          description: >-
            When the agent should use this procedure. Empty string means this is
            a sub-procedure that should only start when another procedure
            references it.
        has_draft:
          type: boolean
          description: >-
            True when the procedure has unpublished draft changes on this branch
            (a newly created or edited procedure not yet published). When true,
            the name, type, and trigger reflect that draft.
      required:
        - procedure_id
        - has_draft
      title: ProcedureListItemResponseModel
    ListProceduresResponseModel:
      type: object
      properties:
        procedures:
          type: array
          items:
            $ref: '#/components/schemas/ProcedureListItemResponseModel'
          description: Procedures on the branch with their draft-aware metadata.
      required:
        - procedures
      title: ListProceduresResponseModel
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
  "procedures": [
    {
      "procedure_id": "agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
      "has_draft": false,
      "version_id": "agtprcv_7rbqxer9o12cyxi55ckw6sgz1dl4",
      "name": "Customer Support Procedure",
      "type": "free_form",
      "trigger": "When the customer asks for support"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.procedures.list("agent_id", "branch_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.procedures.list(
    agent_id="agent_id",
    branch_id="branch_id",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id/procedures"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id/procedures")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id/procedures")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id/procedures');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id/procedures");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id/procedures")! as URL,
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
