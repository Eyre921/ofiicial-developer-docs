---
title: "List agent branches"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/branches/list.md
path: docs/eleven-agents/api-reference/agents/branches/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List agent branches

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches

Returns a list of branches an agent has

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/branches/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agents/{agent_id}/branches:
    get:
      operationId: list
      summary: List Agent Branches
      description: Returns a list of branches an agent has
      tags:
        - branches
      parameters:
        - name: agent_id
          in: path
          description: The id of an agent. This is returned on agent creation.
          required: true
          schema:
            type: string
        - name: include_archived
          in: query
          description: Whether archived branches should be included
          required: false
          schema:
            type: boolean
            default: false
        - name: limit
          in: query
          description: How many results at most should be returned
          required: false
          schema:
            type: integer
            default: 100
        - name: include_commit_status
          in: query
          description: >-
            Whether to compute how far each branch has diverged from main
            (commits_ahead/commits_behind). This walks the version DAG of every
            branch, so it is slow on agents with long histories and is off by
            default, leaving those fields null.
          required: false
          schema:
            type: boolean
            default: false
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
                $ref: '#/components/schemas/type_:ListResponseAgentBranchSummary'
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
    type_:ListResponseMeta:
      type: object
      properties:
        total:
          type: integer
        page:
          type: integer
        page_size:
          type: integer
      title: ListResponseMeta
    type_:BranchProtectionStatus:
      type: string
      enum:
        - writer_perms_required
        - admin_perms_required
      default: writer_perms_required
      title: BranchProtectionStatus
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
    type_:AgentBranchSummary:
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
          $ref: '#/components/schemas/type_:BranchProtectionStatus'
        access_info:
          $ref: '#/components/schemas/type_:ResourceAccessInfo'
          description: Access information for the branch
        current_live_percentage:
          type: number
          format: double
          default: 0
          description: Percentage of traffic live on the branch
        parent_branch_id:
          type: string
          description: ID of the parent branch
        draft_exists:
          type: boolean
          default: false
          description: Whether a draft exists for the branch
        calls_7d:
          type: integer
          default: 0
          description: Number of calls in the last 7 days
        commits_ahead:
          type: integer
          description: >-
            Number of commits on this branch not yet on main, relative to their
            common ancestor. Null if it could not be computed (e.g. no common
            ancestor, or the branch history exceeds the comparison budget).
        commits_behind:
          type: integer
          description: >-
            Number of commits on main not yet incorporated into this branch,
            relative to their common ancestor. Null if it could not be computed
            (e.g. no common ancestor, or the branch history exceeds the
            comparison budget).
        merged_into_branch_id:
          type: string
          description: ID of the branch this branch's tip version was merged into, if any
      required:
        - id
        - name
        - agent_id
        - description
        - created_at
        - last_committed_at
        - is_archived
      title: AgentBranchSummary
    type_:ListResponseAgentBranchSummary:
      type: object
      properties:
        meta:
          $ref: '#/components/schemas/type_:ListResponseMeta'
        results:
          type: array
          items:
            $ref: '#/components/schemas/type_:AgentBranchSummary'
      required:
        - results
      title: ListResponseAgentBranchSummary
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
  "results": [
    {
      "id": "id",
      "name": "name",
      "agent_id": "agent_id",
      "description": "description",
      "created_at": 1,
      "last_committed_at": 1,
      "is_archived": true,
      "protection_status": "writer_perms_required",
      "access_info": {
        "is_creator": true,
        "creator_name": "John Doe",
        "creator_email": "john.doe@example.com",
        "role": "admin",
        "access_source": "creator"
      },
      "current_live_percentage": 1.1,
      "parent_branch_id": "parent_branch_id",
      "draft_exists": true,
      "calls_7d": 1,
      "commits_ahead": 1,
      "commits_behind": 1,
      "merged_into_branch_id": "merged_into_branch_id"
    }
  ],
  "meta": {
    "total": 1,
    "page": 1,
    "page_size": 1
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.branches.list("agent_3701k3ttaq12ewp8b7qv5rfyszkz", {
        includeArchived: true,
        includeCommitStatus: true,
        limit: 1,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.branches.list(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    include_archived=True,
    include_commit_status=True,
    limit=1,
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches?include_archived=true&include_commit_status=true&limit=1"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches?include_archived=true&include_commit_status=true&limit=1")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches?include_archived=true&include_commit_status=true&limit=1")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches?include_archived=true&include_commit_status=true&limit=1');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches?include_archived=true&include_commit_status=true&limit=1");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches?include_archived=true&include_commit_status=true&limit=1")! as URL,
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
