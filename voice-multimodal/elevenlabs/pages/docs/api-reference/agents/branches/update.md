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

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required) — The id of an agent. This is returned on agent creation.
- `branch_id` (string, required) — Unique identifier for the branch.

### Body (application/json)

- `name` (string, optional, nullable) — New name for the branch. Must be unique within the agent.
- `is_archived` (boolean, optional, nullable) — Whether the branch should be archived
- `protection_status` (enum, optional, nullable, default: writer_perms_required) — The protection level for the branch
  - Allowed values: `writer_perms_required`, `admin_perms_required`

## Response

### 200

Successful Response

- `id` (string, required)
- `name` (string, required)
- `agent_id` (string, required)
- `description` (string, required)
- `created_at` (integer, required)
- `last_committed_at` (integer, required)
- `is_archived` (boolean, required)
- `protection_status` (enum, optional, default: writer_perms_required)
  - Allowed values: `writer_perms_required`, `admin_perms_required`
- `access_info` (object, optional, nullable) — Access information for the branch
  - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
  - `creator_name` (string, required) — Name of the agent's creator
  - `creator_email` (string, required) — Email of the agent's creator
  - `role` (enum, required) — The role of the user making the request
    - Allowed values: `admin`, `editor`, `commenter`, `viewer`
  - `anonymous_access_level_override` (enum, optional, nullable) — The access level for anonymous users. If None, the resource is not shared publicly.
    - Allowed values: `admin`, `editor`, `commenter`, `viewer`
  - `access_source` (enum, optional, nullable) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
    - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`
- `current_live_percentage` (double, optional, default: 0) — Percentage of traffic live on the branch
- `parent_branch` (object, optional, nullable) — Parent branch of the branch
  - `id` (string, required)
  - `name` (string, required)
- `most_recent_versions` (list of object, optional) — Most recent versions on the branch
  - `id` (string, required)
  - `agent_id` (string, required)
  - `branch_id` (string, required)
  - `version_description` (string, required)
  - `seq_no_in_branch` (integer, required)
  - `time_committed_secs` (integer, required)
  - `parents` (object, required)
    - `in_branch_parent_id` (string, optional, nullable)
    - `out_of_branch_parent_id` (string, optional, nullable)
    - `merged_into_branch_id` (string, optional, nullable)
    - `merged_from_branch_id` (string, optional, nullable)
    - `merged_from_version_id` (string, optional, nullable)
    - `rebased_from_version_id` (string, optional, nullable)
  - `access_info` (object, optional, nullable)
    - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
    - `creator_name` (string, required) — Name of the agent's creator
    - `creator_email` (string, required) — Email of the agent's creator
    - `role` (enum, required) — The role of the user making the request
      - Allowed values: `admin`, `editor`, `commenter`, `viewer`
    - `anonymous_access_level_override` (enum, optional, nullable) — The access level for anonymous users. If None, the resource is not shared publicly.
      - Allowed values: `admin`, `editor`, `commenter`, `viewer`
    - `access_source` (enum, optional, nullable) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
      - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`

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
