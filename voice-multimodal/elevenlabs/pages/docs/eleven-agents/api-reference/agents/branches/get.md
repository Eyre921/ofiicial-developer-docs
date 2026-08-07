---
title: "Get agent branch"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/branches/get.md
path: docs/eleven-agents/api-reference/agents/branches/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get agent branch

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches/{branch_id}

Get information about a single agent branch

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/branches/get

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
    await client.conversationalAi.agents.branches.get("agent_3701k3ttaq12ewp8b7qv5rfyszkz", "agtbranch_0901k4aafjxxfxt93gd841r7tv5t");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.branches.get(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t")! as URL,
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
