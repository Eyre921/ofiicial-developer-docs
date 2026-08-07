---
title: "Get secrets"
source: https://elevenlabs.io/docs/api-reference/workspace/secrets/list.md
path: docs/api-reference/workspace/secrets/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get secrets

GET https://api.elevenlabs.io/v1/convai/secrets

Get all workspace secrets for the user

Reference: https://elevenlabs.io/docs/api-reference/workspace/secrets/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `page_size` (integer, optional, nullable) — How many documents to return at maximum. Can not exceed 100. If not provided, returns all secrets.
- `dependency_limit` (integer, optional, nullable) — Maximum number of dependent resources (tools, agents, phone numbers) to return per secret. Can not exceed 100.
- `search` (string, optional, nullable) — If specified, returns only secrets whose names start with this string.
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `secrets` (list of object, required)
  - `type` ("stored", required)
  - `secret_id` (string, required)
  - `name` (string, required)
  - `used_by` (object, required)
    - `tools` (list of object, required)
      - `type`: `available` (DependentAvailableToolIdentifier)
        - `access_level` (enum, required)
          - Allowed values: `admin`, `editor`, `commenter`, `viewer`
        - `created_at_unix_secs` (integer, required)
        - `id` (string, required)
        - `name` (string, required)
      - `type`: `unknown` (DependentUnknownToolIdentifier)
        - `id` (string, required)
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
    - `others` (list of enum, required)
      - Allowed values: `conversation_initiation_webhook`
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
      - `type`: `available` (DependentAvailableMCPServerIdentifier)
        - `access_level` (enum, required)
          - Allowed values: `admin`, `editor`, `commenter`, `viewer`
        - `created_at_unix_secs` (integer, required)
        - `id` (string, required)
        - `name` (string, required)
      - `type`: `unknown` (DependentUnknownMCPServerIdentifier)
        - `id` (string, required)
- `next_cursor` (string, optional, nullable) — Cursor for fetching the next page of secrets

## Examples

**Response**

```json
{
  "secrets": [
    {
      "type": "string",
      "secret_id": "string",
      "name": "string",
      "used_by": {
        "tools": [
          {
            "type": "available",
            "access_level": "admin",
            "created_at_unix_secs": 1,
            "id": "string",
            "name": "string"
          }
        ],
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
        "others": [
          "conversation_initiation_webhook"
        ],
        "tools_has_more": false,
        "agents_has_more": false,
        "phone_numbers": [
          {
            "phone_number_id": "string",
            "phone_number": "string",
            "label": "string",
            "provider": "twilio"
          }
        ],
        "phone_numbers_has_more": false,
        "mcp_servers": [
          {
            "type": "available",
            "access_level": "admin",
            "created_at_unix_secs": 1,
            "id": "string",
            "name": "string"
          }
        ]
      }
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
    await client.conversationalAi.secrets.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.secrets.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/secrets"

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

url = URI("https://api.elevenlabs.io/v1/convai/secrets")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/secrets")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/secrets');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets")! as URL,
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
