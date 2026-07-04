---
title: "List agents"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/list.md
path: docs/eleven-agents/api-reference/agents/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List agents

GET https://api.elevenlabs.io/v1/convai/agents

Returns a list of your agents and their metadata.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agents:
    get:
      operationId: list
      summary: List Agents
      description: Returns a list of your agents and their metadata.
      tags:
        - agents
      parameters:
        - name: page_size
          in: query
          description: >-
            How many Agents to return at maximum. Can not exceed 100, defaults
            to 30.
          required: false
          schema:
            type: integer
            default: 30
        - name: search
          in: query
          description: Search by agents name.
          required: false
          schema:
            type: string
        - name: archived
          in: query
          description: Filter agents by archived status
          required: false
          schema:
            type: boolean
        - name: show_only_owned_agents
          in: query
          description: >-
            If set to true, the endpoint will omit any agents that were shared
            with you by someone else and include only the ones you own.
            Deprecated: use created_by_user_id instead.
          required: false
          schema:
            type: boolean
            default: false
        - name: created_by_user_id
          in: query
          description: >-
            Filter agents by creator user ID. When set, only agents created by
            this user are returned. Takes precedence over
            show_only_owned_agents. Use '@me' to refer to the authenticated
            user.
          required: false
          schema:
            type: string
        - name: sort_direction
          in: query
          description: The direction to sort the results
          required: false
          schema:
            $ref: '#/components/schemas/type_:SortDirection'
        - name: sort_by
          in: query
          description: The field to sort the results by
          required: false
          schema:
            $ref: '#/components/schemas/type_:AgentSortBy'
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
                $ref: '#/components/schemas/type_:GetAgentsPageResponseModel'
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
    type_:SortDirection:
      type: string
      enum:
        - asc
        - desc
      title: SortDirection
    type_:AgentSortBy:
      type: string
      enum:
        - name
        - created_at
        - call_count_7d
      title: AgentSortBy
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
    type_:AgentSummaryResponseModel:
      type: object
      properties:
        agent_id:
          type: string
          description: The ID of the agent
        name:
          type: string
          description: The name of the agent
        tags:
          type: array
          items:
            type: string
          description: Agent tags used to categorize the agent
        created_at_unix_secs:
          type: integer
          description: The creation time of the agent in unix seconds
        access_info:
          $ref: '#/components/schemas/type_:ResourceAccessInfo'
          description: The access information of the agent
        last_call_time_unix_secs:
          type: integer
          description: >-
            The time of the most recent call in unix seconds, null if no calls
            have been made
        archived:
          type: boolean
          default: false
          description: Whether the agent is archived
      required:
        - agent_id
        - name
        - tags
        - created_at_unix_secs
        - access_info
      title: AgentSummaryResponseModel
    type_:GetAgentsPageResponseModel:
      type: object
      properties:
        agents:
          type: array
          items:
            $ref: '#/components/schemas/type_:AgentSummaryResponseModel'
          description: A list of agents and their metadata
        next_cursor:
          type: string
          description: The next cursor to paginate through the agents
        has_more:
          type: boolean
          description: Whether there are more agents to paginate through
      required:
        - agents
        - has_more
      title: GetAgentsPageResponseModel
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
      "agent_id": "J3Pbu5gP6NNKBscdCdwB",
      "name": "My Agent",
      "tags": [
        "Customer Support",
        "Technical Help",
        "Eleven"
      ],
      "created_at_unix_secs": 1716153600,
      "access_info": {
        "is_creator": true,
        "creator_name": "John Doe",
        "creator_email": "john@example.com",
        "role": "admin"
      },
      "last_call_time_unix_secs": 1,
      "archived": false
    }
  ],
  "has_more": false,
  "next_cursor": "123"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.list({
        archived: true,
        createdByUserId: "created_by_user_id",
        cursor: "cursor",
        pageSize: 1,
        search: "search",
        showOnlyOwnedAgents: true,
        sortBy: "name",
        sortDirection: "asc",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.list(
    archived=True,
    created_by_user_id="created_by_user_id",
    cursor="cursor",
    page_size=1,
    search="search",
    show_only_owned_agents=True,
    sort_by="name",
    sort_direction="asc",
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

	url := "https://api.elevenlabs.io/v1/convai/agents?archived=true&created_by_user_id=created_by_user_id&cursor=cursor&page_size=1&search=search&show_only_owned_agents=true&sort_by=name&sort_direction=asc"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents?archived=true&created_by_user_id=created_by_user_id&cursor=cursor&page_size=1&search=search&show_only_owned_agents=true&sort_by=name&sort_direction=asc")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents?archived=true&created_by_user_id=created_by_user_id&cursor=cursor&page_size=1&search=search&show_only_owned_agents=true&sort_by=name&sort_direction=asc")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents?archived=true&created_by_user_id=created_by_user_id&cursor=cursor&page_size=1&search=search&show_only_owned_agents=true&sort_by=name&sort_direction=asc');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents?archived=true&created_by_user_id=created_by_user_id&cursor=cursor&page_size=1&search=search&show_only_owned_agents=true&sort_by=name&sort_direction=asc");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents?archived=true&created_by_user_id=created_by_user_id&cursor=cursor&page_size=1&search=search&show_only_owned_agents=true&sort_by=name&sort_direction=asc")! as URL,
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
