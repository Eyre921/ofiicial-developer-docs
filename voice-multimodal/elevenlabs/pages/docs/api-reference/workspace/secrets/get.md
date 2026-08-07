---
title: "Get secret"
source: https://elevenlabs.io/docs/api-reference/workspace/secrets/get.md
path: docs/api-reference/workspace/secrets/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get secret

GET https://api.elevenlabs.io/v1/convai/secrets/{secret_id}

Get a workspace secret by ID

Reference: https://elevenlabs.io/docs/api-reference/workspace/secrets/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `secret_id` (string, required)

## Response

### 200

Successful Response

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

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "type": "stored",
  "secret_id": "sec_9f8b7c6d5e4a3b2c1d0e",
  "name": "DatabaseCredentials",
  "used_by": {
    "tools": [
      {
        "type": "available",
        "access_level": "admin",
        "created_at_unix_secs": 1685000000,
        "id": "tool_123abc456def",
        "name": "DataSyncTool"
      }
    ],
    "agents": [
      {
        "type": "available",
        "access_level": "admin",
        "created_at_unix_secs": 1685100000,
        "id": "agent_987zyx654wvu",
        "name": "CustomerSupportAgent",
        "referenced_resource_ids": [
          "res_789xyz123uvw"
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
        "phone_number_id": "pn_5551234567",
        "phone_number": "+15551234567",
        "label": "Support Line",
        "provider": "twilio"
      }
    ],
    "phone_numbers_has_more": false,
    "mcp_servers": [
      {
        "type": "available",
        "access_level": "admin",
        "created_at_unix_secs": 1685200000,
        "id": "mcp_321fed654cba",
        "name": "PrimaryMCPServer"
      }
    ]
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.secrets.get("secret_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.secrets.get(
    secret_id="secret_id",
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

	url := "https://api.elevenlabs.io/v1/convai/secrets/secret_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/secrets/secret_id")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/secrets/secret_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/secrets/secret_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets/secret_id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets/secret_id")! as URL,
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
