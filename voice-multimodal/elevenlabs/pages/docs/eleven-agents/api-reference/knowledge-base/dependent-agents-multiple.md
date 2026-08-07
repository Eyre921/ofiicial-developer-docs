---
title: "Get dependent agents for multiple documents"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/dependent-agents-multiple.md
path: docs/eleven-agents/api-reference/knowledge-base/dependent-agents-multiple
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get dependent agents for multiple documents

POST https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents
Content-Type: application/json

Get a list of agents depending on any of the given knowledge base documents.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/dependent-agents-multiple

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `dependent_type` (enum, optional) — Type of dependent agents to return.
  - Allowed values: `direct`, `transitive`, `all`
- `page_size` (integer, optional, default: 30) — How many documents to return at maximum. Can not exceed 100, defaults to 30.
- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.

### Body (application/json)

- `document_ids` (list of string, required) — The ids of documents or folders from the knowledge base.

## Response

### 200

Successful Response

- `agents` (list of object, required)
  - `type`: `available`
    - `access_level` (enum, required)
      - Allowed values: `admin`, `editor`, `commenter`, `viewer`
    - `created_at_unix_secs` (integer, required)
    - `id` (string, required)
    - `name` (string, required)
    - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
  - `type`: `unknown`
    - `id` (string, required)
    - `referenced_resource_ids` (list of string, optional) — If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
- `has_more` (boolean, required)
- `branches` (list of object, optional)
  - `agent_id` (string, required)
  - `agent_name` (string, required)
  - `branch_id` (string, required)
  - `branch_name` (string, required)
  - `is_main` (boolean, required)
- `next_cursor` (string, optional)

## Examples

**Request**

```json
{
  "document_ids": [
    "21m00Tcm4TlvDq8ikWAM",
    "31m00Tcm4TlvDq8ikWBM"
  ]
}
```

**Response**

```json
{
  "agents": [
    {
      "type": "available",
      "access_level": "admin",
      "created_at_unix_secs": 1,
      "id": "id",
      "name": "name",
      "referenced_resource_ids": [
        "referenced_resource_ids"
      ]
    }
  ],
  "has_more": true,
  "branches": [
    {
      "agent_id": "agent_id",
      "agent_name": "agent_name",
      "branch_id": "branch_id",
      "branch_name": "branch_name",
      "is_main": true
    }
  ],
  "next_cursor": "next_cursor"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.documents.getBulkAgents({
        cursor: "cursor",
        dependentType: "direct",
        pageSize: 1,
        documentIds: [
            "21m00Tcm4TlvDq8ikWAM",
            "31m00Tcm4TlvDq8ikWBM",
        ],
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.get_bulk_agents(
    cursor="cursor",
    dependent_type="direct",
    page_size=1,
    document_ids=[
        "21m00Tcm4TlvDq8ikWAM",
        "31m00Tcm4TlvDq8ikWBM"
    ],
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents?cursor=cursor&dependent_type=direct&page_size=1"

	payload := strings.NewReader("{\n  \"document_ids\": [\n    \"21m00Tcm4TlvDq8ikWAM\",\n    \"31m00Tcm4TlvDq8ikWBM\"\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents?cursor=cursor&dependent_type=direct&page_size=1")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"document_ids\": [\n    \"21m00Tcm4TlvDq8ikWAM\",\n    \"31m00Tcm4TlvDq8ikWBM\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents?cursor=cursor&dependent_type=direct&page_size=1")
  .header("Content-Type", "application/json")
  .body("{\n  \"document_ids\": [\n    \"21m00Tcm4TlvDq8ikWAM\",\n    \"31m00Tcm4TlvDq8ikWBM\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents?cursor=cursor&dependent_type=direct&page_size=1', [
  'body' => '{
  "document_ids": [
    "21m00Tcm4TlvDq8ikWAM",
    "31m00Tcm4TlvDq8ikWBM"
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents?cursor=cursor&dependent_type=direct&page_size=1");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"document_ids\": [\n    \"21m00Tcm4TlvDq8ikWAM\",\n    \"31m00Tcm4TlvDq8ikWBM\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["document_ids": ["21m00Tcm4TlvDq8ikWAM", "31m00Tcm4TlvDq8ikWBM"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/dependent-agents?cursor=cursor&dependent_type=direct&page_size=1")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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
