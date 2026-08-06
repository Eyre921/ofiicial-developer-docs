---
title: "Get test summaries"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/summaries.md
path: docs/eleven-agents/api-reference/tests/summaries
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get test summaries

POST https://api.elevenlabs.io/v1/convai/agent-testing/summaries
Content-Type: application/json

Gets agent response test summaries for the requested test IDs.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/summaries

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agent-testing/summaries:
    post:
      operationId: summaries
      summary: Get Agent Response Test Summaries By Ids
      description: Gets agent response test summaries for the requested test IDs.
      tags:
        - tests
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
                $ref: '#/components/schemas/type_:GetTestsSummariesByIdsResponseModel'
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
                test_ids:
                  type: array
                  items:
                    type: string
                  description: >-
                    List of test IDs to fetch. No duplicates allowed. Prefer at
                    most 1000 IDs per request.
              required:
                - test_ids
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
    type_:ResourceAccessInfoRole:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: The role of the user making the request
      title: ResourceAccessInfoRole
    type_:ResourceAccessInfoAnonymousAccessLevelOverride:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: ResourceAccessInfoAnonymousAccessLevelOverride
    type_:ResourceAccessInfoAccessSource:
      type: string
      enum:
        - creator
        - explicit
        - workspace_admin
        - workspace_default
      title: ResourceAccessInfoAccessSource
    type_:ResourceAccessInfo:
      type: object
      properties:
        is_creator:
          type: boolean
          description: Whether the user making the request is the creator of the agent
        creator_name:
          type: string
          description: Name of the agent's creator
        creator_email:
          type: string
          description: Email of the agent's creator
        role:
          $ref: '#/components/schemas/type_:ResourceAccessInfoRole'
          description: The role of the user making the request
        anonymous_access_level_override:
          $ref: >-
            #/components/schemas/type_:ResourceAccessInfoAnonymousAccessLevelOverride
          description: >-
            The access level for anonymous users. If None, the resource is not
            shared publicly.
        access_source:
          $ref: '#/components/schemas/type_:ResourceAccessInfoAccessSource'
          description: >-
            Why the requesting user has access to this resource. 'creator' =
            caller is the owner. 'explicit' = caller (or one of their workspace
            groups) is listed in role_to_group_ids beyond the workspace-wide
            everyone group. 'workspace_default' = the workspace-wide everyone
            group is listed in role_to_group_ids (every non-anon workspace
            member, including admins, sees this resource). 'workspace_admin' =
            caller is a workspace admin and the admin seat is the *only* path to
            access; reserved for docs nobody else can see. Lets the UI disclose
            why an admin-bypass viewer sees a doc that wasn't explicitly shared
            with them.
      required:
        - is_creator
        - creator_name
        - creator_email
        - role
      title: ResourceAccessInfo
    type_:TestType:
      type: string
      enum:
        - llm
        - tool
        - simulation
        - folder
      title: TestType
    type_:AgentTestEntityType:
      type: string
      enum:
        - test
        - folder
      default: test
      title: AgentTestEntityType
    type_:AgentTestFolderPathSegmentResponseModel:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
          default: ''
      required:
        - id
      title: AgentTestFolderPathSegmentResponseModel
    type_:ConversationInitiationSource:
      type: string
      enum:
        - unknown
        - android_sdk
        - node_js_sdk
        - react_native_sdk
        - react_sdk
        - js_sdk
        - python_sdk
        - widget
        - sip_trunk
        - twilio
        - exotel
        - genesys
        - audiocodes
        - swift_sdk
        - whatsapp
        - twilio_sms
        - flutter_sdk
        - zendesk_integration
        - slack_integration
        - telegram_integration
        - intercom_integration
        - freshdesk_integration
        - salesforce_integration
        - template_preview
        - genesys_bot_connector
        - subagent_tool
      default: unknown
      description: Enum representing the possible sources for conversation initiation.
      title: ConversationInitiationSource
    type_:UnitTestSummaryResponseModel:
      type: object
      properties:
        id:
          type: string
          description: The ID of the test
        name:
          type: string
          description: Name of the test
        access_info:
          $ref: '#/components/schemas/type_:ResourceAccessInfo'
          description: The access information of the test
        created_at_unix_secs:
          type: integer
          description: Creation time of the test in unix seconds
        last_updated_at_unix_secs:
          type: integer
          description: Last update time of the test in unix seconds
        type:
          $ref: '#/components/schemas/type_:TestType'
          description: Type of the test or entity
        entity_type:
          $ref: '#/components/schemas/type_:AgentTestEntityType'
          description: The type of entity (test or folder)
        folder_parent_id:
          type: string
          description: The ID of the parent folder
        folder_path:
          type: array
          items:
            $ref: '#/components/schemas/type_:AgentTestFolderPathSegmentResponseModel'
          description: The folder path segments from root to this entity
        children_count:
          type: integer
          description: Number of direct children (tests and subfolders) for folders only
        conversation_initiation_source:
          $ref: '#/components/schemas/type_:ConversationInitiationSource'
          description: >-
            Channel the test simulates the conversation as. Null for folders or
            default behavior.
      required:
        - id
        - name
        - created_at_unix_secs
        - last_updated_at_unix_secs
        - type
      title: UnitTestSummaryResponseModel
    type_:GetTestsSummariesByIdsResponseModel:
      type: object
      properties:
        tests:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:UnitTestSummaryResponseModel'
          description: Dictionary mapping test IDs to their summary information
      required:
        - tests
      title: GetTestsSummariesByIdsResponseModel
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
  "test_ids": [
    "test_id_1",
    "test_id_2"
  ]
}
```

**Response**

```json
{
  "tests": {
    "key": {
      "id": "id",
      "name": "name",
      "created_at_unix_secs": 1,
      "last_updated_at_unix_secs": 1,
      "type": "llm",
      "access_info": {
        "is_creator": true,
        "creator_name": "John Doe",
        "creator_email": "john.doe@example.com",
        "role": "admin",
        "access_source": "creator"
      },
      "entity_type": "test",
      "folder_parent_id": "folder_parent_id",
      "folder_path": [
        {
          "id": "id"
        }
      ],
      "children_count": 1,
      "conversation_initiation_source": "unknown"
    }
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tests.summaries({
        testIds: [
            "test_id_1",
            "test_id_2",
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.summaries(
    test_ids=[
        "test_id_1",
        "test_id_2"
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

	url := "https://api.elevenlabs.io/v1/convai/agent-testing/summaries"

	payload := strings.NewReader("{\n  \"test_ids\": [\n    \"test_id_1\",\n    \"test_id_2\"\n  ]\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agent-testing/summaries")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"test_ids\": [\n    \"test_id_1\",\n    \"test_id_2\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agent-testing/summaries")
  .header("Content-Type", "application/json")
  .body("{\n  \"test_ids\": [\n    \"test_id_1\",\n    \"test_id_2\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agent-testing/summaries', [
  'body' => '{
  "test_ids": [
    "test_id_1",
    "test_id_2"
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

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agent-testing/summaries");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"test_ids\": [\n    \"test_id_1\",\n    \"test_id_2\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["test_ids": ["test_id_1", "test_id_2"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agent-testing/summaries")! as URL,
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
