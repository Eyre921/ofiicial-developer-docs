---
title: "Update Procedure Draft"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/procedures/update.md
path: docs/eleven-agents/api-reference/agents/procedures/update
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update Procedure Draft

PATCH https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}/draft
Content-Type: application/json

Create or update user's draft for a procedure

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/procedures/update

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
- `procedure_id` (string, required) — The procedure ID

### Body (application/json)

- `name` (string, required) — Procedure name
- `content` (string, required) — Procedure content
- `type` (enum, required, default: free_form) — Procedure type
  - Allowed values: `free_form`, `deterministic`
- `trigger` (string, optional) — When the agent should use this procedure. Empty string means this is a sub-procedure that should only start when another procedure references it. If omitted or null, the trigger is derived from the content instead. Also accepts `description` as an alias.

## Response

### 200

Successful Response

- `procedure_id` (string, required) — Procedure ID
- `name` (string, required) — Procedure name
- `content` (string, required) — Procedure content
- `type` (enum, optional, default: free_form) — Procedure type
  - Allowed values: `free_form`, `deterministic`
- `trigger` (string, optional, default: ) — When the agent should use this procedure. Empty string means this is a sub-procedure that should only start when another procedure references it.

## Examples

**Request**

```json
{
  "name": "name",
  "content": "content",
  "type": "free_form"
}
```

**Response**

```json
{
  "procedure_id": "agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
  "name": "Customer Support Procedure",
  "content": "# Customer Support Procedure\n\n1. Greet the customer...",
  "type": "free_form",
  "trigger": "When the customer asks for support"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.procedures.drafts.update("agent_3701k3ttaq12ewp8b7qv5rfyszkz", "agtbranch_0901k4aafjxxfxt93gd841r7tv5t", "agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3", {
        name: "name",
        content: "content",
        type: "free_form",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.procedures.drafts.update(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
    procedure_id="agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
    name="name",
    content="content",
    type="free_form",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures/agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3/draft"

	payload := strings.NewReader("{\n  \"name\": \"name\",\n  \"content\": \"content\",\n  \"type\": \"free_form\"\n}")

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures/agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3/draft")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"name\",\n  \"content\": \"content\",\n  \"type\": \"free_form\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures/agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3/draft")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"name\",\n  \"content\": \"content\",\n  \"type\": \"free_form\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures/agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3/draft', [
  'body' => '{
  "name": "name",
  "content": "content",
  "type": "free_form"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures/agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3/draft");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"name\",\n  \"content\": \"content\",\n  \"type\": \"free_form\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "name": "name",
  "content": "content",
  "type": "free_form"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/branches/agtbranch_0901k4aafjxxfxt93gd841r7tv5t/procedures/agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3/draft")! as URL,
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
