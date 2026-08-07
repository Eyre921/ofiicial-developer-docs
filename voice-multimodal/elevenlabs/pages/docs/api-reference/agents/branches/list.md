---
title: "List agent branches"
source: https://elevenlabs.io/docs/api-reference/agents/branches/list.md
path: docs/api-reference/agents/branches/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List agent branches

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches

Returns a list of branches an agent has

Reference: https://elevenlabs.io/docs/api-reference/agents/branches/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required) — The id of an agent. This is returned on agent creation.

### Query parameters

- `include_archived` (boolean, optional, default: false) — Whether archived branches should be included
- `limit` (integer, optional, default: 100) — How many results at most should be returned
- `include_commit_status` (boolean, optional, default: false) — Whether to compute how far each branch has diverged from main (commits_ahead/commits_behind). This walks the version DAG of every branch, so it is slow on agents with long histories and is off by default, leaving those fields null.

## Response

### 200

Successful Response

- `results` (list of object, required)
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
  - `parent_branch_id` (string, optional, nullable) — ID of the parent branch
  - `draft_exists` (boolean, optional, default: false) — Whether a draft exists for the branch
  - `calls_7d` (integer, optional, default: 0) — Number of calls in the last 7 days
  - `commits_ahead` (integer, optional, nullable) — Number of commits on this branch not yet on main, relative to their common ancestor. Null if it could not be computed (e.g. no common ancestor, or the branch history exceeds the comparison budget).
  - `commits_behind` (integer, optional, nullable) — Number of commits on main not yet incorporated into this branch, relative to their common ancestor. Null if it could not be computed (e.g. no common ancestor, or the branch history exceeds the comparison budget).
  - `merged_into_branch_id` (string, optional, nullable) — ID of the branch this branch's tip version was merged into, if any
- `meta` (object, optional)
  - `total` (integer, optional, nullable)
  - `page` (integer, optional, nullable)
  - `page_size` (integer, optional, nullable)

## Examples

**Response**

```json
{
  "results": [
    {
      "id": "string",
      "name": "string",
      "agent_id": "string",
      "description": "string",
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
      "current_live_percentage": 0,
      "parent_branch_id": "string",
      "draft_exists": false,
      "calls_7d": 0,
      "commits_ahead": 1,
      "commits_behind": 1,
      "merged_into_branch_id": "string"
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
    await client.conversationalAi.agents.branches.list("agent_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.branches.list(
    agent_id="agent_id",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/branches"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/branches');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/branches")! as URL,
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
