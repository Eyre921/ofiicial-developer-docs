---
title: "Get secrets"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/workspace/secrets/list.md
path: docs/eleven-agents/api-reference/workspace/secrets/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get secrets

GET https://api.elevenlabs.io/v1/convai/secrets

Get all workspace secrets for the user

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/workspace/secrets/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `page_size` (integer, optional) — How many documents to return at maximum. Can not exceed 100. If not provided, returns all secrets.
- `dependency_limit` (integer, optional) — Maximum number of dependent resources (tools, agents, phone numbers) to return per secret. Can not exceed 100.
- `search` (string, optional) — If specified, returns only secrets whose names start with this string.
- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `secrets` (list of object, required)
  - `type` ("stored", required)
  - `secret_id` (string, required)
  - `name` (string, required)
  - `used_by` (object, required)
    - `tools` (list of object, required)
      - `type`: `available`
        - `access_level` (enum, required)
          - Allowed values: `admin`, `editor`, `commenter`, `viewer`
        - `created_at_unix_secs` (integer, required)
        - `id` (string, required)
        - `name` (string, required)
      - `type`: `unknown`
        - `id` (string, required)
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
    - `others` (list of "conversation_initiation_webhook", required)
    - `tools_has_more` (boolean, optional, default: false) — Whether there are more tool dependents beyond the returned preview
    - `agents_has_more` (boolean, optional, default: false) — Whether there are more agent dependents beyond the returned preview
    - `phone_numbers` (list of object, optional)
      - `phone_number_id` (string, required)
      - `phone_number` (string, required)
      - `label` (string, required)
      - `provider` (enum, required)
        - Allowed values: `twilio`, `sip_trunk`, `exotel`
    - `phone_numbers_has_more` (boolean, optional, default: false) — Whether there are more phone number dependents beyond the returned preview
    - `mcp_servers` (list of object, optional)
      - `type`: `available`
        - `access_level` (enum, required)
          - Allowed values: `admin`, `editor`, `commenter`, `viewer`
        - `created_at_unix_secs` (integer, required)
        - `id` (string, required)
        - `name` (string, required)
      - `type`: `unknown`
        - `id` (string, required)
- `next_cursor` (string, optional) — Cursor for fetching the next page of secrets

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "secrets": [
    {
      "type": "stored",
      "secret_id": "sec_9f8b7c6d5e4a3b2c1d0e",
      "name": "PaymentGatewayAPIKey",
      "used_by": {
        "tools": [
          {
            "type": "available",
            "access_level": "admin",
            "created_at_unix_secs": 1685000000,
            "id": "tool_123abc456def",
            "name": "Stripe Integration"
          }
        ],
        "agents": [
          {
            "type": "available",
            "access_level": "admin",
            "created_at_unix_secs": 1685100000,
            "id": "agent_789xyz012uvw",
            "name": "Billing Agent"
          }
        ],
        "others": [
          "conversation_initiation_webhook"
        ]
      }
    }
  ],
  "next_cursor": "cursor_eyJwYWdlIjoxfQ=="
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.secrets.list({
        cursor: "cursor",
        dependencyLimit: 1,
        pageSize: 1,
        search: "search",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.secrets.list(
    cursor="cursor",
    dependency_limit=1,
    page_size=1,
    search="search",
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

	url := "https://api.elevenlabs.io/v1/convai/secrets?cursor=cursor&dependency_limit=1&page_size=1&search=search"

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

url = URI("https://api.elevenlabs.io/v1/convai/secrets?cursor=cursor&dependency_limit=1&page_size=1&search=search")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/secrets?cursor=cursor&dependency_limit=1&page_size=1&search=search")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/secrets?cursor=cursor&dependency_limit=1&page_size=1&search=search', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets?cursor=cursor&dependency_limit=1&page_size=1&search=search");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets?cursor=cursor&dependency_limit=1&page_size=1&search=search")! as URL,
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
