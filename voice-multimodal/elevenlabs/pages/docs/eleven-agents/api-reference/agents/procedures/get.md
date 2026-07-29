---
title: "Get Procedure"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/procedures/get.md
path: docs/eleven-agents/api-reference/agents/procedures/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Procedure

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}

Retrieve a procedure at a specific version or the current branch HEAD.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/procedures/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}:
    get:
      operationId: get
      summary: Get Procedure
      description: Retrieve a procedure at a specific version or the current branch HEAD.
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
        - name: procedure_id
          in: path
          description: The procedure ID
          required: true
          schema:
            type: string
        - name: version_id
          in: query
          description: >-
            The version ID to retrieve. If omitted, returns the version at
            branch HEAD.
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
                $ref: '#/components/schemas/type_:ProcedureAtVersionResponseModel'
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
    type_:ProcedureType:
      type: string
      enum:
        - free_form
        - deterministic
      default: free_form
      title: ProcedureType
    type_:ProcedureAtVersionResponseModel:
      type: object
      properties:
        procedure_id:
          type: string
          description: Procedure ID
        version_id:
          type: string
          description: >-
            Version ID of a version of the procedure. None for a procedure never
            versioned.
        name:
          type: string
          description: Procedure name
        content:
          type: string
          description: Procedure content
        type:
          $ref: '#/components/schemas/type_:ProcedureType'
          description: Procedure type
        trigger:
          type: string
          default: ''
          description: >-
            When the agent should use this procedure. Empty string means this is
            a sub-procedure that should only start when another procedure
            references it.
      required:
        - procedure_id
        - name
        - content
      title: ProcedureAtVersionResponseModel
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
  "procedure_id": "agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
  "name": "Customer Support Procedure",
  "content": "# Customer Support Procedure\n\n1. Greet the customer...",
  "version_id": "agtprcv_7rbqxer9o12cyxi55ckw6sgz1dl4",
  "type": "free_form",
  "trigger": "When the customer asks for support"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.procedures.get("agent_3701k3ttaq12ewp8b7qv5rfyszkz", "agtbranch_0901k4aafjxxfxt93gd841r7tv5t", "agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3", {
        versionId: "version_id",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.procedures.get(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
    procedure_id="agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
    version_id="version_id",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures/agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3?version_id=version_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures/agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3?version_id=version_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures/agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3?version_id=version_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures/agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3?version_id=version_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures/agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3?version_id=version_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures/agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3?version_id=version_id")! as URL,
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
