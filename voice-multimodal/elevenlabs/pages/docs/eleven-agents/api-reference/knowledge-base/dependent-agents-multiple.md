---
title: "Get dependent agents for multiple documents"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/dependent-agents-multiple.md
path: docs/eleven-agents/api-reference/knowledge-base/dependent-agents-multiple
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get dependent agents for multiple documents

POST https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents
Content-Type: application/json

Get a list of agents depending on any of the given knowledge base documents.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/dependent-agents-multiple

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/knowledge-base/dependent-agents:
    post:
      operationId: get_bulk_agents
      summary: Get Dependent Agents For Multiple Documents
      description: >-
        Get a list of agents depending on any of the given knowledge base
        documents.
      tags:
        - documents
      parameters:
        - name: dependent_type
          in: query
          description: Type of dependent agents to return.
          required: false
          schema:
            $ref: '#/components/schemas/type_:KnowledgeBaseDependentType'
        - name: page_size
          in: query
          description: >-
            How many documents to return at maximum. Can not exceed 100,
            defaults to 30.
          required: false
          schema:
            type: integer
            default: 30
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
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
                $ref: >-
                  #/components/schemas/type_:GetKnowledgeBaseDependentAgentsResponseModel
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                document_ids:
                  type: array
                  items:
                    type: string
                  description: The ids of documents or folders from the knowledge base.
              required:
                - document_ids
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
    type_:KnowledgeBaseDependentType:
      type: string
      enum:
        - direct
        - transitive
        - all
      title: KnowledgeBaseDependentType
    type_:DependentAvailableAgentIdentifierAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: DependentAvailableAgentIdentifierAccessLevel
    type_:GetKnowledgeBaseDependentAgentsResponseModelAgentsItem:
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
      title: GetKnowledgeBaseDependentAgentsResponseModelAgentsItem
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
    type_:GetKnowledgeBaseDependentAgentsResponseModel:
      type: object
      properties:
        agents:
          type: array
          items:
            $ref: >-
              #/components/schemas/type_:GetKnowledgeBaseDependentAgentsResponseModelAgentsItem
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
      title: GetKnowledgeBaseDependentAgentsResponseModel
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
{
  "document_ids": [
    "21m00Tcm4TlvDq8ikWAM",
    "31m00Tcm4TlvDq8ikWBM"
  ]
}
```

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
    await client.conversationalAi.knowledgeBase.documents.getBulkAgents({
        cursor: "cursor",
        dependentType: "direct",
        pageSize: 1,
        documentIds: [
            "21m00Tcm4TlvDq8ikWAM",
            "31m00Tcm4TlvDq8ikWBM",
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.get_bulk_agents(
    cursor="cursor",
    dependent_type="direct",
    page_size=1,
    document_ids=[
        "21m00Tcm4TlvDq8ikWAM",
        "31m00Tcm4TlvDq8ikWBM"
    ],
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents?cursor=cursor&dependent_type=direct&page_size=1"

	payload := strings.NewReader("{\n  \"document_ids\": [\n    \"21m00Tcm4TlvDq8ikWAM\",\n    \"31m00Tcm4TlvDq8ikWBM\"\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents?cursor=cursor&dependent_type=direct&page_size=1")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"document_ids\": [\n    \"21m00Tcm4TlvDq8ikWAM\",\n    \"31m00Tcm4TlvDq8ikWBM\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents?cursor=cursor&dependent_type=direct&page_size=1")
  .header("Content-Type", "application/json")
  .body("{\n  \"document_ids\": [\n    \"21m00Tcm4TlvDq8ikWAM\",\n    \"31m00Tcm4TlvDq8ikWBM\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents?cursor=cursor&dependent_type=direct&page_size=1', [
  'body' => '{
  "document_ids": [
    "21m00Tcm4TlvDq8ikWAM",
    "31m00Tcm4TlvDq8ikWBM"
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents?cursor=cursor&dependent_type=direct&page_size=1");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"document_ids\": [\n    \"21m00Tcm4TlvDq8ikWAM\",\n    \"31m00Tcm4TlvDq8ikWBM\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["document_ids": ["21m00Tcm4TlvDq8ikWAM", "31m00Tcm4TlvDq8ikWBM"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents?cursor=cursor&dependent_type=direct&page_size=1")! as URL,
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
