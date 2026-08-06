---
title: "List tests"
source: https://elevenlabs.io/docs/api-reference/tests/list.md
path: docs/api-reference/tests/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List tests

GET https://api.elevenlabs.io/v1/convai/agent-testing

Lists all agent response tests with pagination support and optional search filtering.

Reference: https://elevenlabs.io/docs/api-reference/tests/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agent-testing:
    get:
      operationId: list
      summary: List Agent Response Tests
      description: >-
        Lists all agent response tests with pagination support and optional
        search filtering.
      tags:
        - tests
      parameters:
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: page_size
          in: query
          description: >-
            How many Tests to return at maximum. Can not exceed 100, defaults to
            30.
          required: false
          schema:
            type: integer
            default: 30
        - name: search
          in: query
          description: Search query to filter tests by name.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: parent_folder_id
          in: query
          description: >-
            Filter by parent folder ID. Use 'root' to get items in the root
            folder.
          required: false
          schema:
            type:
              - string
              - 'null'
        - name: types
          in: query
          description: >-
            If present, the endpoint will return only tests/folders of the given
            types.
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              $ref: '#/components/schemas/TestType'
        - name: include_folders
          in: query
          description: >-
            Deprecated. Use the `types` query param and include `folder`
            instead.
          required: false
          schema:
            type:
              - boolean
              - 'null'
        - name: sort_mode
          in: query
          description: >-
            Sort mode for listing tests. Use 'folders_first' to place folders
            before tests.
          required: false
          schema:
            $ref: '#/components/schemas/V1ConvaiAgentTestingGetParametersSortMode'
            default: default
        - name: sharing_mode
          in: query
          description: >-
            Filter test visibility. Use `shared_with_me` to return only
            tests/folders shared with the current user that they did not create.
          required: false
          schema:
            $ref: '#/components/schemas/TestSharingMode'
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
                $ref: '#/components/schemas/GetTestsPageResponseModel'
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
    TestType:
      type: string
      enum:
        - llm
        - tool
        - simulation
        - folder
      title: TestType
    V1ConvaiAgentTestingGetParametersSortMode:
      type: string
      enum:
        - default
        - folders_first
      default: default
      description: >-
        Sort mode for listing tests. Use 'folders_first' to place folders before
        tests.
      title: V1ConvaiAgentTestingGetParametersSortMode
    TestSharingMode:
      type: string
      enum:
        - all
        - shared_with_me
      title: TestSharingMode
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
    GetTestsPageResponseModel:
      type: object
      properties:
        tests:
          type: array
          items:
            $ref: '#/components/schemas/UnitTestSummaryResponseModel'
        next_cursor:
          type:
            - string
            - 'null'
        has_more:
          type: boolean
      required:
        - tests
        - has_more
      title: GetTestsPageResponseModel
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
  "tests": [
    {
      "id": "string",
      "name": "string",
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
      "folder_parent_id": "string",
      "folder_path": [
        {
          "id": "string",
          "name": ""
        }
      ],
      "children_count": 1,
      "conversation_initiation_source": "unknown"
    }
  ],
  "has_more": true,
  "next_cursor": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tests.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agent-testing"

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

url = URI("https://api.elevenlabs.io/v1/convai/agent-testing")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agent-testing")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agent-testing');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agent-testing");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agent-testing")! as URL,
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
