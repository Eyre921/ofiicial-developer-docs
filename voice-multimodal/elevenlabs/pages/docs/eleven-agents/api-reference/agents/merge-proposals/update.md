---
title: "Update A Merge Proposal"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/merge-proposals/update.md
path: docs/eleven-agents/api-reference/agents/merge-proposals/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update A Merge Proposal

PATCH https://api.elevenlabs.io/v1/convai/agents/{agent_id}/merge-proposals/{merge_proposal_id}
Content-Type: application/json

Edit an open merge_proposal's title or description, or close it. The author closing it is recorded as withdrawn; anyone else as rejected.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/merge-proposals/update

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required) — The id of an agent. This is returned on agent creation.
- `merge_proposal_id` (string, required) — Unique identifier for the merge_proposal.

### Body (application/json)

This endpoint expects an object.

- `title` (string, optional) — New title for the merge_proposal.
- `description` (string, optional) — New description for the merge_proposal.
- `requested_reviewer_user_ids` (list of string, optional) — Replacement list of user IDs to request a review from.
- `close` (boolean, optional, default: false) — When true, close the merge_proposal without merging.

## Response

### 200

Successful Response

- `id` (string, required)
- `agent_id` (string, required)
- `source_branch_id` (string, required)
- `target_branch_id` (string, required)
- `source_tip_version_id_at_creation` (string, required)
- `title` (string, required)
- `created_at` (integer, required)
- `updated_at` (integer, required)
- `description` (string, optional, default: )
- `requested_reviewer_user_ids` (list of string, optional)
- `reviews` (list of MergeProposalReview, optional)
- `comments` (list of MergeProposalComment, optional)
- `outcome` (AgentMergeProposalResponseOutcome, optional)
- `author_user_id` (string, optional) — User ID of the merge_proposal's author.
- `access_info` (ResourceAccessInfo, optional) — Access information for the merge_proposal, including creator.

## Errors

### 422 Merge Proposals Update Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### MergeProposalReview

- `user_id` (string, required)
- `state` (enum, required)
  - Allowed values: `approved`, `changes_requested`
- `submitted_at` (integer, required)
- `comment` (string, optional, default: )
- `reviewer_role` (enum, optional)
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`

### MergeProposalComment

- `id` (string, required)
- `user_id` (string, required)
- `body` (string, required)
- `created_at` (integer, required)

### AgentMergeProposalResponseOutcome

- `status`: `closed`
  - `at` (integer, required)
  - `reason` (enum, required)
    - Allowed values: `withdrawn`, `rejected`, `branch_archived`
  - `by_user_id` (string, optional)
- `status`: `merged`
  - `at` (integer, required)
  - `version_id` (string, required)
  - `by_user_id` (string, optional)
- `status`: `open`

### ResourceAccessInfo

- `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
- `creator_name` (string, required) — Name of the agent's creator
- `creator_email` (string, required) — Email of the agent's creator
- `role` (enum, required) — The role of the user making the request
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`
- `anonymous_access_level_override` (enum, optional) — The access level for anonymous users. If None, the resource is not shared publicly.
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`
- `access_source` (enum, optional) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
  - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItem

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "id": "id",
  "agent_id": "agent_id",
  "source_branch_id": "source_branch_id",
  "target_branch_id": "target_branch_id",
  "source_tip_version_id_at_creation": "source_tip_version_id_at_creation",
  "title": "title",
  "created_at": 1,
  "updated_at": 1,
  "description": "description",
  "requested_reviewer_user_ids": [
    "requested_reviewer_user_ids"
  ],
  "reviews": [
    {
      "user_id": "user_id",
      "state": "approved",
      "submitted_at": 1,
      "comment": "comment",
      "reviewer_role": "admin"
    }
  ],
  "comments": [
    {
      "id": "id",
      "user_id": "user_id",
      "body": "body",
      "created_at": 1
    }
  ],
  "outcome": {
    "status": "closed",
    "at": 1,
    "reason": "withdrawn",
    "by_user_id": "by_user_id"
  },
  "author_user_id": "author_user_id",
  "access_info": {
    "is_creator": true,
    "creator_name": "John Doe",
    "creator_email": "john.doe@example.com",
    "role": "admin",
    "anonymous_access_level_override": "admin",
    "access_source": "creator"
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.mergeProposals.update("agent_3701k3ttaq12ewp8b7qv5rfyszkz", "agtmprop_8901k4t9z5defmb8vh3e9361y7nj", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.merge_proposals.update(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    merge_proposal_id="agtmprop_8901k4t9z5defmb8vh3e9361y7nj",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals/agtmprop_8901k4t9z5defmb8vh3e9361y7nj"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals/agtmprop_8901k4t9z5defmb8vh3e9361y7nj")

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

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals/agtmprop_8901k4t9z5defmb8vh3e9361y7nj")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals/agtmprop_8901k4t9z5defmb8vh3e9361y7nj', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals/agtmprop_8901k4t9z5defmb8vh3e9361y7nj");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/merge-proposals/agtmprop_8901k4t9z5defmb8vh3e9361y7nj")! as URL,
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
