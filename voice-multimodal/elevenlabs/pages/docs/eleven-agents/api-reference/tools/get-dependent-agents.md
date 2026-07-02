---
title: "Get dependent agents"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/tools/get-dependent-agents.md
path: docs/eleven-agents/api-reference/tools/get-dependent-agents
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get dependent agents

GET https://api.elevenlabs.io/v1/convai/tools/{tool_id}/dependent-agents

Get a list of agents depending on this tool

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/tools/get-dependent-agents

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/tools/{tool_id}/dependent-agents:
    get:
      operationId: get_dependent_agents
      summary: Get Dependent Agents List
      description: Get a list of agents depending on this tool
      tags:
        - subpackage_conversationalAi/tools
      parameters:
        - name: tool_id
          in: path
          description: ID of the requested tool.
          required: true
          schema:
            type: string
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
          required: false
          schema:
            type: string
        - name: page_size
          in: query
          description: >-
            How many documents to return at maximum. Can not exceed 100,
            defaults to 30.
          required: false
          schema:
            type: integer
            default: 30
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
                $ref: '#/components/schemas/type_:GetToolDependentAgentsResponseModel'
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
    type_:DependentAvailableAgentIdentifierAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: DependentAvailableAgentIdentifierAccessLevel
    type_:GetToolDependentAgentsResponseModelAgentsItem:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - available
              description: 'Discriminator value: available'
            referenced_resource_ids:
              type: array
              items:
                type: string
              description: >-
                If the agent is a transitive dependent, contains IDs of the
                resources that the agent depends on directly.
            id:
              type: string
            name:
              type: string
            created_at_unix_secs:
              type: integer
            access_level:
              $ref: >-
                #/components/schemas/type_:DependentAvailableAgentIdentifierAccessLevel
          required:
            - type
            - id
            - name
            - created_at_unix_secs
            - access_level
        - type: object
          properties:
            type:
              type: string
              enum:
                - unknown
              description: 'Discriminator value: unknown'
            referenced_resource_ids:
              type: array
              items:
                type: string
              description: >-
                If the agent is a transitive dependent, contains IDs of the
                resources that the agent depends on directly.
            id:
              type: string
          required:
            - type
            - id
      discriminator:
        propertyName: type
      title: GetToolDependentAgentsResponseModelAgentsItem
    type_:DependentBranchInfo:
      type: object
      properties:
        agent_id:
          type: string
        agent_name:
          type: string
        branch_id:
          type: string
        branch_name:
          type: string
        is_main:
          type: boolean
      required:
        - agent_id
        - agent_name
        - branch_id
        - branch_name
        - is_main
      title: DependentBranchInfo
    type_:GetToolDependentAgentsResponseModel:
      type: object
      properties:
        agents:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:GetToolDependentAgentsResponseModelAgentsItem
        branches:
          type: array
          items:
            $ref: '#/components/schemas/type_:DependentBranchInfo'
        next_cursor:
          type: string
        has_more:
          type: boolean
      required:
        - agents
        - has_more
      title: GetToolDependentAgentsResponseModel
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
  "agents": [
    {
      "type": "available",
      "access_level": "admin",
      "created_at_unix_secs": 1,
      "id": "id",
      "name": "name",
      "referenced_resource_ids": [
        "referenced_resource_ids"
      ]
    }
  ],
  "has_more": true,
  "branches": [
    {
      "agent_id": "agent_id",
      "agent_name": "agent_name",
      "branch_id": "branch_id",
      "branch_name": "branch_name",
      "is_main": true
    }
  ],
  "next_cursor": "next_cursor"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tools.getDependentAgents("tool_id", {
        cursor: "cursor",
        pageSize: 1,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tools.get_dependent_agents(
    tool_id="tool_id",
    cursor="cursor",
    page_size=1,
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

	url := "https://api.elevenlabs.io/v1/convai/tools/tool_id/dependent-agents?cursor=cursor&page_size=1"

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

url = URI("https://api.elevenlabs.io/v1/convai/tools/tool_id/dependent-agents?cursor=cursor&page_size=1")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/tools/tool_id/dependent-agents?cursor=cursor&page_size=1")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/tools/tool_id/dependent-agents?cursor=cursor&page_size=1');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/tools/tool_id/dependent-agents?cursor=cursor&page_size=1");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/tools/tool_id/dependent-agents?cursor=cursor&page_size=1")! as URL,
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
