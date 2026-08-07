---
title: "Get agent version metadata"
source: https://elevenlabs.io/docs/api-reference/agents/versions/get.md
path: docs/api-reference/agents/versions/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get agent version metadata

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/versions/{version_id}

Get metadata for a specific agent version

Reference: https://elevenlabs.io/docs/api-reference/agents/versions/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required) — The id of an agent. This is returned on agent creation.
- `version_id` (string, required) — Unique identifier for the version.

## Response

### 200

Successful Response

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
  "id": "agtvrsn_0901k4aafjxxfxt93gd841r7tv5t",
  "agent_id": "agent_3701k3ttaq12ewp8b7qv5rfyszkz",
  "branch_id": "branch_5f8d7a9c2b1e4d3f9a7c1234",
  "version_description": "Initial release of the customer support agent with basic FAQ capabilities.",
  "seq_no_in_branch": 3,
  "time_committed_secs": 1682544000,
  "parents": {
    "in_branch_parent_id": "agtvrsn_0801j3aafjxxfxt93gd841r7tv5s",
    "out_of_branch_parent_id": null,
    "merged_into_branch_id": null,
    "merged_from_branch_id": null,
    "merged_from_version_id": null,
    "rebased_from_version_id": null
  },
  "access_info": {
    "is_creator": true,
    "creator_name": "Alice Johnson",
    "creator_email": "alice.johnson@elevenlabs.io",
    "role": "admin",
    "access_source": "creator"
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.versions.get("agent_id", "version_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.versions.get(
    agent_id="agent_id",
    version_id="version_id",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/versions/version_id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/versions/version_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_id/versions/version_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/versions/version_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/versions/version_id");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/versions/version_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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
