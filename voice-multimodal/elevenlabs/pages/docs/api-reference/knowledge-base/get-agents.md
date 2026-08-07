---
title: "Get dependent agents"
source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-agents.md
path: docs/api-reference/knowledge-base/get-agents
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get dependent agents

GET https://api.elevenlabs.io/v1/convai/knowledge-base/{documentation_id}/dependent-agents

Get a list of agents depending on this knowledge base document

Reference: https://elevenlabs.io/docs/api-reference/knowledge-base/get-agents

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `documentation_id` (string, required) — The id of a document from the knowledge base. This is returned on document addition.

### Query parameters

- `dependent_type` (enum, optional) — Type of dependent agents to return.
  - Allowed values: `direct`, `transitive`, `all`
- `page_size` (integer, optional, default: 30) — How many documents to return at maximum. Can not exceed 100, defaults to 30.
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `agents` (list of object, required)
  - `type`: `available` (DependentAvailableAgentIdentifier)
    - `access_level` (enum, required)
      - Allowed values: `admin`, `editor`, `commenter`, `viewer`
    - `created_at_unix_secs` (integer, required)
    - `id` (string, required)
    - `name` (string, required)
    - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
  - `type`: `unknown` (DependentUnknownAgentIdentifier)
    - `id` (string, required)
    - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
- `has_more` (boolean, required)
- `branches` (list of object, optional)
  - `agent_id` (string, required)
  - `agent_name` (string, required)
  - `branch_id` (string, required)
  - `branch_name` (string, required)
  - `is_main` (boolean, required)
- `next_cursor` (string, optional, nullable)

## Examples

**Response**

```json
{
  "agents": [
    {
      "type": "available",
      "access_level": "admin",
      "created_at_unix_secs": 1,
      "id": "string",
      "name": "string",
      "referenced_resource_ids": [
        "string"
      ]
    }
  ],
  "has_more": true,
  "branches": [
    {
      "agent_id": "string",
      "agent_name": "string",
      "branch_id": "string",
      "branch_name": "string",
      "is_main": true
    }
  ],
  "next_cursor": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.documents.getAgents("documentation_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.get_agents(
    documentation_id="documentation_id",
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/dependent-agents"

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/dependent-agents")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/dependent-agents")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/dependent-agents');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/dependent-agents");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/dependent-agents")! as URL,
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
