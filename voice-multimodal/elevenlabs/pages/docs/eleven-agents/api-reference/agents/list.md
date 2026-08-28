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

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `page_size` (integer, optional, default: 30) — How many Agents to return at maximum. Can not exceed 100, defaults to 30.
- `search` (string, optional) — Search by agents name.
- `archived` (boolean, optional) — Filter agents by archived status
- `show_only_owned_agents` (boolean, optional, default: false, deprecated) — If set to true, the endpoint will omit any agents that were shared with you by someone else and include only the ones you own. Deprecated: use created_by_user_id instead.
- `created_by_user_id` (string, optional) — Filter agents by creator user ID. When set, only agents created by this user are returned. Takes precedence over show_only_owned_agents. Use '@me' to refer to the authenticated user.
- `tags` (string, optional) — Filter agents by tag. Repeat the parameter to match any of several tags.
- `sort_direction` (enum, optional) — The direction to sort the results
  - Allowed values: `asc`, `desc`
- `sort_by` (enum, optional) — The field to sort the results by
  - Allowed values: `name`, `created_at`, `call_count_7d`
- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `agents` (list of object, required) — A list of agents and their metadata
  - `agent_id` (string, required) — The ID of the agent
  - `name` (string, required) — The name of the agent
  - `tags` (list of string, required) — Agent tags used to categorize the agent
  - `created_at_unix_secs` (integer, required) — The creation time of the agent in unix seconds
  - `access_info` (object, required) — The access information of the agent
    - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
    - `creator_name` (string, required) — Name of the agent's creator
    - `creator_email` (string, required) — Email of the agent's creator
    - `role` (enum, required) — The role of the user making the request
      - Allowed values: `admin`, `editor`, `commenter`, `viewer`
    - `anonymous_access_level_override` (enum, optional) — The access level for anonymous users. If None, the resource is not shared publicly.
      - Allowed values: `admin`, `editor`, `commenter`, `viewer`
    - `access_source` (enum, optional) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
      - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`
  - `last_call_time_unix_secs` (integer, optional) — The time of the most recent call in unix seconds, null if no calls have been made
  - `archived` (boolean, optional, default: false) — Whether the agent is archived
- `has_more` (boolean, required) — Whether there are more agents to paginate through
- `next_cursor` (string, optional) — The next cursor to paginate through the agents

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
        tags: [
            "tags",
        ],
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
    tags=[
        "tags"
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

	url := "https://api.elevenlabs.io/v1/convai/agents?archived=true&created_by_user_id=created_by_user_id&cursor=cursor&page_size=1&search=search&show_only_owned_agents=true&sort_by=name&sort_direction=asc&tags=%5B%22tags%22%5D"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents?archived=true&created_by_user_id=created_by_user_id&cursor=cursor&page_size=1&search=search&show_only_owned_agents=true&sort_by=name&sort_direction=asc&tags=%5B%22tags%22%5D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents?archived=true&created_by_user_id=created_by_user_id&cursor=cursor&page_size=1&search=search&show_only_owned_agents=true&sort_by=name&sort_direction=asc&tags=%5B%22tags%22%5D")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents?archived=true&created_by_user_id=created_by_user_id&cursor=cursor&page_size=1&search=search&show_only_owned_agents=true&sort_by=name&sort_direction=asc&tags=%5B%22tags%22%5D');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents?archived=true&created_by_user_id=created_by_user_id&cursor=cursor&page_size=1&search=search&show_only_owned_agents=true&sort_by=name&sort_direction=asc&tags=%5B%22tags%22%5D");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents?archived=true&created_by_user_id=created_by_user_id&cursor=cursor&page_size=1&search=search&show_only_owned_agents=true&sort_by=name&sort_direction=asc&tags=%5B%22tags%22%5D")! as URL,
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
