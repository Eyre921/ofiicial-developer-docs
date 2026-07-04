---
title: "List tests"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/list.md
path: docs/eleven-agents/api-reference/tests/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List tests

GET https://api.elevenlabs.io/v1/convai/agent-testing

Lists all agent response tests with pagination support and optional search filtering.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/list

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
            type: string
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
            type: string
        - name: parent_folder_id
          in: query
          description: >-
            Filter by parent folder ID. Use 'root' to get items in the root
            folder.
          required: false
          schema:
            type: string
        - name: types
          in: query
          description: >-
            If present, the endpoint will return only tests/folders of the given
            types.
          required: false
          schema:
            $ref: '#/components/schemas/type_:TestType'
        - name: include_folders
          in: query
          description: >-
            Deprecated. Use the `types` query param and include `folder`
            instead.
          required: false
          schema:
            type: boolean
        - name: sort_mode
          in: query
          description: >-
            Sort mode for listing tests. Use 'folders_first' to place folders
            before tests.
          required: false
          schema:
            $ref: >-
              #/components/schemas/type_conversationalAi/tests:TestsListRequestSortMode
            default: default
        - name: sharing_mode
          in: query
          description: >-
            Filter test visibility. Use `shared_with_me` to return only
            tests/folders shared with the current user that they did not create.
          required: false
          schema:
            $ref: '#/components/schemas/type_:TestSharingMode'
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
                $ref: '#/components/schemas/type_:GetTestsPageResponseModel'
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
    type_:TestType:
      type: string
      enum:
        - llm
        - tool
        - simulation
        - folder
      title: TestType
    type_conversationalAi/tests:TestsListRequestSortMode:
      type: string
      enum:
        - default
        - folders_first
      default: default
      description: >-
        Sort mode for listing tests. Use 'folders_first' to place folders before
        tests.
      title: TestsListRequestSortMode
    type_:TestSharingMode:
      type: string
      enum:
        - all
        - shared_with_me
      title: TestSharingMode
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
        - swift_sdk
        - whatsapp
        - twilio_sms
        - flutter_sdk
        - zendesk_integration
        - slack_integration
        - telegram_integration
        - intercom_integration
        - freshdesk_integration
        - template_preview
        - genesys_bot_connector
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
    type_:GetTestsPageResponseModel:
      type: object
      properties:
        tests:
          type: array
          items:
            $ref: '#/components/schemas/type_:UnitTestSummaryResponseModel'
        next_cursor:
          type: string
        has_more:
          type: boolean
      required:
        - tests
        - has_more
      title: GetTestsPageResponseModel
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
  "tests": [
    {
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
  ],
  "has_more": true,
  "next_cursor": "next_cursor"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tests.list({
        cursor: "cursor",
        includeFolders: true,
        pageSize: 1,
        parentFolderId: "parent_folder_id",
        search: "search",
        sharingMode: "all",
        sortMode: "default",
        types: [
            "llm",
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.list(
    cursor="cursor",
    include_folders=True,
    page_size=1,
    parent_folder_id="parent_folder_id",
    search="search",
    sharing_mode="all",
    sort_mode="default",
    types=[
        "llm"
    ],
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

	url := "https://api.elevenlabs.io/v1/convai/agent-testing?cursor=cursor&include_folders=true&page_size=1&parent_folder_id=parent_folder_id&search=search&sharing_mode=all&sort_mode=default&types=%5B%22llm%22%5D"

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

url = URI("https://api.elevenlabs.io/v1/convai/agent-testing?cursor=cursor&include_folders=true&page_size=1&parent_folder_id=parent_folder_id&search=search&sharing_mode=all&sort_mode=default&types=%5B%22llm%22%5D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agent-testing?cursor=cursor&include_folders=true&page_size=1&parent_folder_id=parent_folder_id&search=search&sharing_mode=all&sort_mode=default&types=%5B%22llm%22%5D")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agent-testing?cursor=cursor&include_folders=true&page_size=1&parent_folder_id=parent_folder_id&search=search&sharing_mode=all&sort_mode=default&types=%5B%22llm%22%5D');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agent-testing?cursor=cursor&include_folders=true&page_size=1&parent_folder_id=parent_folder_id&search=search&sharing_mode=all&sort_mode=default&types=%5B%22llm%22%5D");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agent-testing?cursor=cursor&include_folders=true&page_size=1&parent_folder_id=parent_folder_id&search=search&sharing_mode=all&sort_mode=default&types=%5B%22llm%22%5D")! as URL,
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
