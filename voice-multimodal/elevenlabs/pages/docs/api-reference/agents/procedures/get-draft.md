---
title: "Get Procedure Draft"
source: https://elevenlabs.io/docs/api-reference/agents/procedures/get-draft.md
path: docs/api-reference/agents/procedures/get-draft
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Procedure Draft

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}/draft

Get user's draft for a procedure

Reference: https://elevenlabs.io/docs/api-reference/agents/procedures/get-draft

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
    await client.conversationalAi.agents.procedures.drafts.get("agent_id", "branch_id", "procedure_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.procedures.drafts.get(
    agent_id="agent_id",
    branch_id="branch_id",
    procedure_id="procedure_id",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id/procedures/procedure_id/draft"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id/procedures/procedure_id/draft")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id/procedures/procedure_id/draft")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id/procedures/procedure_id/draft');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id/procedures/procedure_id/draft");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id/procedures/procedure_id/draft")! as URL,
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
