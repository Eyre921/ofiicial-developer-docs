---
title: "Update agent branch"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/branches/update.md
path: docs/eleven-agents/api-reference/agents/branches/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update agent branch

PATCH https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches/{branch_id}
Content-Type: application/json

Update agent branch properties such as archiving status and protection level

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/branches/update

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

- `name` (string, optional) — New name for the branch. Must be unique within the agent.
- `is_archived` (boolean, optional) — Whether the branch should be archived
- `protection_status` (enum, optional, default: writer_perms_required) — The protection level for the branch
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
- `access_info` (object, optional) — Access information for the branch
  - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
  - `creator_name` (string, required) — Name of the agent's creator
  - `creator_email` (string, required) — Email of the agent's creator
  - `role` (enum, required) — The role of the user making the request
    - Allowed values: `admin`, `editor`, `commenter`, `viewer`
  - `anonymous_access_level_override` (enum, optional) — The access level for anonymous users. If None, the resource is not shared publicly.
    - Allowed values: `admin`, `editor`, `commenter`, `viewer`
  - `access_source` (enum, optional) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
    - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`
- `current_live_percentage` (double, optional, default: 0) — Percentage of traffic live on the branch
- `parent_branch` (object, optional) — Parent branch of the branch
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
    - `in_branch_parent_id` (string, optional)
    - `out_of_branch_parent_id` (string, optional)
    - `merged_into_branch_id` (string, optional)
    - `merged_from_branch_id` (string, optional)
    - `merged_from_version_id` (string, optional)
    - `rebased_from_version_id` (string, optional)
  - `access_info` (object, optional)
    - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
    - `creator_name` (string, required) — Name of the agent's creator
    - `creator_email` (string, required) — Email of the agent's creator
    - `role` (enum, required) — The role of the user making the request
      - Allowed values: `admin`, `editor`, `commenter`, `viewer`
    - `anonymous_access_level_override` (enum, optional) — The access level for anonymous users. If None, the resource is not shared publicly.
      - Allowed values: `admin`, `editor`, `commenter`, `viewer`
    - `access_source` (enum, optional) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
      - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`

## Examples

**Request**

```json
{}
```

**Response**

```json
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
    "anonymous_access_level_override": "admin",
    "access_source": "creator"
  },
  "current_live_percentage": 1.1,
  "parent_branch": {
    "id": "id",
    "name": "name"
  },
  "most_recent_versions": [
    {
      "id": "id",
      "agent_id": "agent_id",
      "branch_id": "branch_id",
      "version_description": "version_description",
      "seq_no_in_branch": 1,
      "time_committed_secs": 1,
      "parents": {},
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
    await client.conversationalAi.agents.branches.update("agent_3701k3ttaq12ewp8b7qv5rfyszkz", "agtbranch_0901k4aafjxxfxt93gd841r7tv5t", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.branches.update(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t")

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

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t")! as URL,
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
