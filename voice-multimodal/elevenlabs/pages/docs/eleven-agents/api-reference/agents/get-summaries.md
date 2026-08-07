---
title: "Get agent summaries"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/get-summaries.md
path: docs/eleven-agents/api-reference/agents/get-summaries
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get agent summaries

GET https://api.elevenlabs.io/v1/convai/agents/summaries

Returns summaries for the specified agents.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/get-summaries

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `agent_ids` (string, optional) — List of agent IDs to fetch summaries for

## Response

### 200

Successful Response

- `map from string to object`
  - `status`: `success`
    - `data` (object, required)
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
  - `status`: `failure`
    - `error_code` (integer, required)
    - `error_message` (string, required)
    - `error_status` (string, required)

## Examples

**Response**

```json
{
  "key": {
    "status": "success",
    "data": {
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
      "last_call_time_unix_secs": 1716240000,
      "archived": false
    }
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.summaries.get({
        agentIds: [
            "agent_ids",
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.summaries.get(
    agent_ids=[
        "agent_ids"
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

	url := "https://api.elevenlabs.io/v1/convai/agents/summaries?agent_ids=%5B%22agent_ids%22%5D"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/summaries?agent_ids=%5B%22agent_ids%22%5D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/summaries?agent_ids=%5B%22agent_ids%22%5D")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/summaries?agent_ids=%5B%22agent_ids%22%5D');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/summaries?agent_ids=%5B%22agent_ids%22%5D");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/summaries?agent_ids=%5B%22agent_ids%22%5D")! as URL,
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
