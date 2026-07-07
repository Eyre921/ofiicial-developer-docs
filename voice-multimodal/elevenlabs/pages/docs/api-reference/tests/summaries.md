---
title: "Get test summaries"
source: https://elevenlabs.io/docs/api-reference/tests/summaries.md
path: docs/api-reference/tests/summaries
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get test summaries

POST https://api.elevenlabs.io/v1/convai/agent-testing/summaries
Content-Type: application/json

Gets multiple agent response tests by their IDs. Returns a dictionary mapping test IDs to test summaries.

Reference: https://elevenlabs.io/docs/api-reference/tests/summaries

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
      description: >-
        Gets multiple agent response tests by their IDs. Returns a dictionary
        mapping test IDs to test summaries.
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
                $ref: '#/components/schemas/GetTestsSummariesByIdsResponseModel'
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
              $ref: '#/components/schemas/ListTestsByIdsRequestModel'
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
    ListTestsByIdsRequestModel:
      type: object
      properties:
        test_ids:
          type: array
          items:
            type: string
          description: List of test IDs to fetch. No duplicates allowed.
      required:
        - test_ids
      title: ListTestsByIdsRequestModel
    ResourceAccessInfoRole:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: The role of the user making the request
      title: ResourceAccessInfoRole
    ResourceAccessInfoAnonymousAccessLevelOverride:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: >-
        The access level for anonymous users. If None, the resource is not
        shared publicly.
      title: ResourceAccessInfoAnonymousAccessLevelOverride
    ResourceAccessInfoAccessSource:
      type: string
      enum:
        - creator
        - explicit
        - workspace_admin
        - workspace_default
      description: >-
        Why the requesting user has access to this resource. 'creator' = caller
        is the owner. 'explicit' = caller (or one of their workspace groups) is
        listed in role_to_group_ids beyond the workspace-wide everyone group.
        'workspace_default' = the workspace-wide everyone group is listed in
        role_to_group_ids (every non-anon workspace member, including admins,
        sees this resource). 'workspace_admin' = caller is a workspace admin and
        the admin seat is the *only* path to access; reserved for docs nobody
        else can see. Lets the UI disclose why an admin-bypass viewer sees a doc
        that wasn't explicitly shared with them.
      title: ResourceAccessInfoAccessSource
    ResourceAccessInfo:
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
          $ref: '#/components/schemas/ResourceAccessInfoRole'
          description: The role of the user making the request
        anonymous_access_level_override:
          oneOf:
            - $ref: >-
                #/components/schemas/ResourceAccessInfoAnonymousAccessLevelOverride
            - type: 'null'
          description: >-
            The access level for anonymous users. If None, the resource is not
            shared publicly.
        access_source:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfoAccessSource'
            - type: 'null'
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
    TestType:
      type: string
      enum:
        - llm
        - tool
        - simulation
        - folder
      title: TestType
    AgentTestEntityType:
      type: string
      enum:
        - test
        - folder
      default: test
      title: AgentTestEntityType
    AgentTestFolderPathSegmentResponseModel:
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
    ConversationInitiationSource:
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
    UnitTestSummaryResponseModel:
      type: object
      properties:
        id:
          type: string
          description: The ID of the test
        name:
          type: string
          description: Name of the test
        access_info:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfo'
            - type: 'null'
          description: The access information of the test
        created_at_unix_secs:
          type: integer
          description: Creation time of the test in unix seconds
        last_updated_at_unix_secs:
          type: integer
          description: Last update time of the test in unix seconds
        type:
          $ref: '#/components/schemas/TestType'
          description: Type of the test or entity
        entity_type:
          $ref: '#/components/schemas/AgentTestEntityType'
          default: test
          description: The type of entity (test or folder)
        folder_parent_id:
          type:
            - string
            - 'null'
          description: The ID of the parent folder
        folder_path:
          type: array
          items:
            $ref: '#/components/schemas/AgentTestFolderPathSegmentResponseModel'
          description: The folder path segments from root to this entity
        children_count:
          type:
            - integer
            - 'null'
          description: Number of direct children (tests and subfolders) for folders only
        conversation_initiation_source:
          oneOf:
            - $ref: '#/components/schemas/ConversationInitiationSource'
            - type: 'null'
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
    GetTestsSummariesByIdsResponseModel:
      type: object
      properties:
        tests:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/UnitTestSummaryResponseModel'
          description: Dictionary mapping test IDs to their summary information
      required:
        - tests
      title: GetTestsSummariesByIdsResponseModel
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
  "test_ids": [
    "test_id_1",
    "test_id_2"
  ]
}
```

**Response**

```json
{
  "tests": {}
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
