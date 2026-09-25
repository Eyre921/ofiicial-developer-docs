---
title: "List Procedures"
source: https://elevenlabs.io/docs/api-reference/agents/procedures/list.md
path: docs/api-reference/agents/procedures/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List Procedures

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches/{branch_id}/procedures

List the procedures attached to this agent branch. By default, unpublished drafts take precedence over the latest committed version. Pass agent_version_id to list a published snapshot instead. has_draft is true when a procedure has unpublished draft changes on this branch. Procedure content is not included; use Get Procedure to read a procedure's body.

Reference: https://elevenlabs.io/docs/api-reference/agents/procedures/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required) — Agent ID to get the procedure draft from
- `branch_id` (string, required) — Branch ID to get the procedure draft from

### Query parameters

- `agent_version_id` (string, optional, nullable) — The agent version ID to retrieve the procedure for.

## Response

### 200

Successful Response

- `procedures` (list of ProcedureListItemResponseModel, required) — Procedures on the branch with their draft-aware metadata.

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### ProcedureListItemResponseModel

- `procedure_id` (string, required) — Procedure ID
- `has_draft` (boolean, required) — True when the procedure has unpublished draft changes on this branch (a newly created or edited procedure not yet published). When true, the name, type, and trigger reflect that draft.
- `version_id` (string, optional, nullable) — Version ID of a version of the procedure. None for a procedure never versioned.
- `name` (string, optional, default: ) — Procedure name
- `type` (enum, optional, default: free_form) — Procedure type
  - Allowed values: `free_form`, `deterministic`, `folder`
- `trigger` (string, optional, default: ) — When the agent should use this procedure. Empty string means this is a sub-procedure that should only start when another procedure references it.
- `referenced_tool_ids` (list of string, optional) — Tool IDs referenced in the procedure content
- `referenced_kb_ids` (list of string, optional) — Knowledge base IDs referenced in the procedure content
- `referenced_procedure_ids` (list of string, optional) — Procedure IDs referenced in the procedure content
- `referenced_dynamic_variables` (list of string, optional) — Dynamic variable names used in the procedure content
- `folder_parent_id` (string, optional, nullable) — Procedure ID of the folder this procedure is placed in. None means root.

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

## Examples

**Response**

```json
{
  "procedures": [
    {
      "procedure_id": "agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
      "has_draft": false,
      "version_id": "agtprcv_7rbqxer9o12cyxi55ckw6sgz1dl4",
      "name": "Customer Support Procedure",
      "type": "free_form",
      "trigger": "When the customer asks for support",
      "referenced_tool_ids": [
        "tool_123"
      ],
      "referenced_kb_ids": [
        "kb_123"
      ],
      "referenced_procedure_ids": [
        "agtprc_other"
      ],
      "referenced_dynamic_variables": [
        "customer_id"
      ]
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.procedures.list("agent_3701k3ttaq12ewp8b7qv5rfyszkz", "agtbranch_0901k4aafjxxfxt93gd841r7tv5t", {
        agentVersionId: "agtvrsn_8901k4t9z5defmb8vh3e9361y7nj",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.procedures.list(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
    agent_version_id="agtvrsn_8901k4t9z5defmb8vh3e9361y7nj",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures?agent_version_id=agtvrsn_8901k4t9z5defmb8vh3e9361y7nj"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures?agent_version_id=agtvrsn_8901k4t9z5defmb8vh3e9361y7nj")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures?agent_version_id=agtvrsn_8901k4t9z5defmb8vh3e9361y7nj")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures?agent_version_id=agtvrsn_8901k4t9z5defmb8vh3e9361y7nj');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures?agent_version_id=agtvrsn_8901k4t9z5defmb8vh3e9361y7nj");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures?agent_version_id=agtvrsn_8901k4t9z5defmb8vh3e9361y7nj")! as URL,
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
