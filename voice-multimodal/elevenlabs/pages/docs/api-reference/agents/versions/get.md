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
- `parents` (AgentVersionParents, required)
- `access_info` (ResourceAccessInfo, optional, nullable)
- `merged_authors` (list of ResourceAccessInfo, optional, nullable) — For a merge into the main branch, the people who published the merged changes on the source branch (access_info is whoever ran the merge). Null when not recorded.

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### AgentVersionParents

- `in_branch_parent_id` (string, optional, nullable)
- `out_of_branch_parent_id` (string, optional, nullable)
- `merged_into_branch_id` (string, optional, nullable)
- `merged_from_branch_id` (string, optional, nullable)
- `merged_from_version_id` (string, optional, nullable)
- `rebased_from_version_id` (string, optional, nullable)

### ResourceAccessInfo

- `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
- `creator_name` (string, required) — Name of the agent's creator
- `creator_email` (string, required) — Email of the agent's creator
- `role` (enum, required) — The role of the user making the request
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`
- `anonymous_access_level_override` (enum, optional, nullable) — The access level for anonymous users. If None, the resource is not shared publicly.
  - Allowed values: `admin`, `editor`, `commenter`, `viewer`
- `access_source` (enum, optional, nullable) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
  - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

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
  "branch_id": "agtbrnch_main_7f3k9pqr2mxw1yz",
  "version_description": "Updated system prompt to improve customer support responses and added new FAQ knowledge base",
  "seq_no_in_branch": 5,
  "time_committed_secs": 1718035200,
  "parents": {
    "in_branch_parent_id": "agtvrsn_0801k3zzfjxxfxt93gd841r7tv4s",
    "out_of_branch_parent_id": null,
    "merged_into_branch_id": null,
    "merged_from_branch_id": null,
    "merged_from_version_id": null,
    "rebased_from_version_id": null
  },
  "access_info": {
    "is_creator": true,
    "creator_name": "John Doe",
    "creator_email": "john.doe@example.com",
    "role": "admin",
    "access_source": "creator"
  },
  "merged_authors": [
    {
      "is_creator": false,
      "creator_name": "Jane Smith",
      "creator_email": "jane.smith@example.com",
      "role": "editor",
      "anonymous_access_level_override": null,
      "access_source": "explicit"
    }
  ]
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/versions/agtvrsn_0901k4aafjxxfxt93gd841r7tv5t"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/versions/agtvrsn_0901k4aafjxxfxt93gd841r7tv5t';
const options = {method: 'GET', headers: {'Content-Type': 'application/json'}, body: '{}'};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/versions/agtvrsn_0901k4aafjxxfxt93gd841r7tv5t"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/versions/agtvrsn_0901k4aafjxxfxt93gd841r7tv5t")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/versions/agtvrsn_0901k4aafjxxfxt93gd841r7tv5t")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/versions/agtvrsn_0901k4aafjxxfxt93gd841r7tv5t', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/versions/agtvrsn_0901k4aafjxxfxt93gd841r7tv5t");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/versions/agtvrsn_0901k4aafjxxfxt93gd841r7tv5t")! as URL,
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
