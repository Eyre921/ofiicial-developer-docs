---
title: "Get dependent agents for multiple documents"
source: https://elevenlabs.io/docs/api-reference/knowledge-base/dependent-agents-multiple.md
path: docs/api-reference/knowledge-base/dependent-agents-multiple
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get dependent agents for multiple documents

POST https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents
Content-Type: application/json

Get a list of agents depending on any of the given knowledge base documents.

Reference: https://elevenlabs.io/docs/api-reference/knowledge-base/dependent-agents-multiple

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
            $ref: '#/components/schemas/KnowledgeBaseDependentType'
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
                $ref: >-
                  #/components/schemas/GetKnowledgeBaseDependentAgentsResponseModel
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
                #/components/schemas/Body_Get_dependent_agents_for_multiple_documents_v1_convai_knowledge_base_dependent_agents_post
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
    KnowledgeBaseDependentType:
      type: string
      enum:
        - direct
        - transitive
        - all
      title: KnowledgeBaseDependentType
    Body_Get_dependent_agents_for_multiple_documents_v1_convai_knowledge_base_dependent_agents_post:
      type: object
      properties:
        document_ids:
          type: array
          items:
            type: string
          description: The ids of documents or folders from the knowledge base.
      required:
        - document_ids
      title: >-
        Body_Get_dependent_agents_for_multiple_documents_v1_convai_knowledge_base_dependent_agents_post
    V1ConvaiKnowledgeBaseSummariesGetResponsesContentApplicationJsonSchemaDiscriminatorMappingSuccessDataDiscriminatorMappingUrlDependentAgentsItemsDiscriminatorMappingAvailableAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: >-
        V1ConvaiKnowledgeBaseSummariesGetResponsesContentApplicationJsonSchemaDiscriminatorMappingSuccessDataDiscriminatorMappingUrlDependentAgentsItemsDiscriminatorMappingAvailableAccessLevel
    GetKnowledgeBaseDependentAgentsResponseModelAgentsItems:
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
                #/components/schemas/V1ConvaiKnowledgeBaseSummariesGetResponsesContentApplicationJsonSchemaDiscriminatorMappingSuccessDataDiscriminatorMappingUrlDependentAgentsItemsDiscriminatorMappingAvailableAccessLevel
          required:
            - type
            - id
            - name
            - created_at_unix_secs
            - access_level
          description: DependentAvailableAgentIdentifier variant
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
          description: |-
            A model that represents an agent dependent on a knowledge base/tools
            to which the user has no direct access.
      discriminator:
        propertyName: type
      title: GetKnowledgeBaseDependentAgentsResponseModelAgentsItems
    DependentBranchInfo:
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
    GetKnowledgeBaseDependentAgentsResponseModel:
      type: object
      properties:
        agents:
          type: array
          items:
            $ref: >-
              #/components/schemas/GetKnowledgeBaseDependentAgentsResponseModelAgentsItems
        branches:
          type: array
          items:
            $ref: '#/components/schemas/DependentBranchInfo'
        next_cursor:
          type:
            - string
            - 'null'
        has_more:
          type: boolean
      required:
        - agents
        - has_more
      title: GetKnowledgeBaseDependentAgentsResponseModel
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
      "created_at_unix_secs": 1685600000,
      "id": "agent_9f8b7c6d5e4a3b2c1d0e",
      "name": "Customer Support Bot",
      "referenced_resource_ids": [
        "41m00Tcm4TlvDq8ikWCM"
      ]
    }
  ],
  "has_more": true,
  "branches": [
    {
      "agent_id": "agent_9f8b7c6d5e4a3b2c1d0e",
      "agent_name": "Customer Support Bot",
      "branch_id": "branch_123abc456def",
      "branch_name": "Main Production",
      "is_main": true
    }
  ],
  "next_cursor": "cursor_eyJwYWdlIjoxfQ=="
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.documents.getBulkAgents({
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents"

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents")

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

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents")
  .header("Content-Type", "application/json")
  .body("{\n  \"document_ids\": [\n    \"21m00Tcm4TlvDq8ikWAM\",\n    \"31m00Tcm4TlvDq8ikWBM\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents', [
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

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents")! as URL,
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
