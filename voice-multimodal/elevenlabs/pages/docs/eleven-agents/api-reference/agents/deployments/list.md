---
title: "List Agent Deployments"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/deployments/list.md
path: docs/eleven-agents/api-reference/agents/deployments/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List Agent Deployments

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/deployments

List the traffic split history of an agent, newest first

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/deployments/list

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

- `page` (integer, optional, default: 1) — Page number, starting at 1
- `page_size` (integer, optional, default: 30) — How many results at most should be returned

## Response

### 200

Successful Response

- `results` (list of AgentDeploymentHistoryItem, required)
- `meta` (ListResponseMeta, optional)

## Errors

### 422 Deployments List Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### AgentDeploymentHistoryItem

- `id` (string, required) — ID of the deployment
- `deployed_at_unix_secs` (integer, required) — Unix timestamp of when the traffic split was applied
- `is_active` (boolean, required) — Whether this is the live traffic split
- `traffic_percentage_branch_id_map` (map from string to double, optional) — Map of branch IDs to traffic percentages
- `source` (enum, optional) — What caused this traffic split change. Null for deployments created before this was recorded.
  - Allowed values: `manual`, `branch_merge`
- `access_info` (ResourceAccessInfo, optional) — Access information for the deployment, including who created it

### ListResponseMeta

- `total` (integer, optional)
- `page` (integer, optional)
- `page_size` (integer, optional)

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

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

### ValidationErrorLocItem

## Examples

**Response**

```json
{
  "results": [
    {
      "id": "id",
      "deployed_at_unix_secs": 1,
      "is_active": true,
      "traffic_percentage_branch_id_map": {
        "key": 1.1
      },
      "source": "manual",
      "access_info": {
        "is_creator": true,
        "creator_name": "John Doe",
        "creator_email": "john.doe@example.com",
        "role": "admin",
        "access_source": "creator"
      }
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
    await client.conversationalAi.agents.deployments.list("agent_3701k3ttaq12ewp8b7qv5rfyszkz", {
        page: 1,
        pageSize: 1,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.deployments.list(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    page=1,
    page_size=1,
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/deployments?page=1&page_size=1"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/deployments?page=1&page_size=1")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/deployments?page=1&page_size=1")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/deployments?page=1&page_size=1');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/deployments?page=1&page_size=1");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/deployments?page=1&page_size=1")! as URL,
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
