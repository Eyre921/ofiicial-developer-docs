---
title: "Update agent branch"
source: https://elevenlabs.io/docs/api-reference/agents/branches/update.md
path: docs/api-reference/agents/branches/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update agent branch

PATCH https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches/{branch_id}
Content-Type: application/json

Update agent branch properties such as archiving status and protection level

Reference: https://elevenlabs.io/docs/api-reference/agents/branches/update

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agents/{agent_id}/branches/{branch_id}:
    patch:
      operationId: update
      summary: Update Agent Branch
      description: >-
        Update agent branch properties such as archiving status and protection
        level
      tags:
        - branches
      parameters:
        - name: agent_id
          in: path
          description: The id of an agent. This is returned on agent creation.
          required: true
          schema:
            type: string
        - name: branch_id
          in: path
          description: Unique identifier for the branch.
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
                $ref: '#/components/schemas/AgentBranchResponse'
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
                #/components/schemas/Body_Update_agent_branch_v1_convai_agents__agent_id__branches__branch_id__patch
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
    BranchProtectionStatus:
      type: string
      enum:
        - writer_perms_required
        - admin_perms_required
      default: writer_perms_required
      title: BranchProtectionStatus
    Body_Update_agent_branch_v1_convai_agents__agent_id__branches__branch_id__patch:
      type: object
      properties:
        name:
          type:
            - string
            - 'null'
          description: New name for the branch. Must be unique within the agent.
        is_archived:
          type:
            - boolean
            - 'null'
          description: Whether the branch should be archived
        protection_status:
          oneOf:
            - $ref: '#/components/schemas/BranchProtectionStatus'
            - type: 'null'
          description: The protection level for the branch
      title: >-
        Body_Update_agent_branch_v1_convai_agents__agent_id__branches__branch_id__patch
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
    AgentBranchBasicInfo:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
      required:
        - id
        - name
      title: AgentBranchBasicInfo
    AgentVersionParents:
      type: object
      properties:
        in_branch_parent_id:
          type:
            - string
            - 'null'
        out_of_branch_parent_id:
          type:
            - string
            - 'null'
        merged_into_branch_id:
          type:
            - string
            - 'null'
        merged_from_branch_id:
          type:
            - string
            - 'null'
        merged_from_version_id:
          type:
            - string
            - 'null'
        rebased_from_version_id:
          type:
            - string
            - 'null'
      title: AgentVersionParents
    AgentVersionMetadata:
      type: object
      properties:
        id:
          type: string
        agent_id:
          type: string
        branch_id:
          type: string
        version_description:
          type: string
        seq_no_in_branch:
          type: integer
        time_committed_secs:
          type: integer
        parents:
          $ref: '#/components/schemas/AgentVersionParents'
        access_info:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfo'
            - type: 'null'
      required:
        - id
        - agent_id
        - branch_id
        - version_description
        - seq_no_in_branch
        - time_committed_secs
        - parents
      title: AgentVersionMetadata
    AgentBranchResponse:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        agent_id:
          type: string
        description:
          type: string
        created_at:
          type: integer
        last_committed_at:
          type: integer
        is_archived:
          type: boolean
        protection_status:
          $ref: '#/components/schemas/BranchProtectionStatus'
          default: writer_perms_required
        access_info:
          oneOf:
            - $ref: '#/components/schemas/ResourceAccessInfo'
            - type: 'null'
          description: Access information for the branch
        current_live_percentage:
          type: number
          format: double
          default: 0
          description: Percentage of traffic live on the branch
        parent_branch:
          oneOf:
            - $ref: '#/components/schemas/AgentBranchBasicInfo'
            - type: 'null'
          description: Parent branch of the branch
        most_recent_versions:
          type: array
          items:
            $ref: '#/components/schemas/AgentVersionMetadata'
          description: Most recent versions on the branch
      required:
        - id
        - name
        - agent_id
        - description
        - created_at
        - last_committed_at
        - is_archived
      title: AgentBranchResponse
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
{}
```

**Response**

```json
{
  "id": "branch_8f7a6d4c2b9e4f1a",
  "name": "Feature Update - Chat Enhancements",
  "agent_id": "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
  "description": "Branch for implementing chat UI improvements and bug fixes",
  "created_at": 1685606400,
  "last_committed_at": 1688294400,
  "is_archived": false,
  "protection_status": "writer_perms_required",
  "access_info": {
    "is_creator": true,
    "creator_name": "John Doe",
    "creator_email": "john.doe@example.com",
    "role": "admin",
    "access_source": "creator"
  },
  "current_live_percentage": 75,
  "parent_branch": {
    "id": "branch_main_001",
    "name": "Main"
  },
  "most_recent_versions": [
    {
      "id": "version_20230630_01",
      "agent_id": "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
      "branch_id": "branch_8f7a6d4c2b9e4f1a",
      "version_description": "Added new chat bubble styles and fixed message ordering bug",
      "seq_no_in_branch": 5,
      "time_committed_secs": 1688294400,
      "parents": {
        "in_branch_parent_id": "version_20230629_04",
        "out_of_branch_parent_id": "version_20230628_03",
        "merged_into_branch_id": "branch_main_001",
        "merged_from_branch_id": "branch_feature_ui_002",
        "merged_from_version_id": "version_20230627_02",
        "rebased_from_version_id": "version_20230626_01"
      },
      "access_info": {
        "is_creator": true,
        "creator_name": "John Doe",
        "creator_email": "john.doe@example.com",
        "role": "admin",
        "access_source": "creator"
      }
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.branches.update("agent_id", "branch_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.branches.update(
    agent_id="agent_id",
    branch_id="branch_id",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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
