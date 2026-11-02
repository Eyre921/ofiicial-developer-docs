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
- `used_by` (ConvAIStoredSecretDependencies, required)

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### ConvAIStoredSecretDependencies

- `tools` (list of ConvAiStoredSecretDependenciesToolsItems, required)
- `agents` (list of ConvAiStoredSecretDependenciesAgentsItems, required)
- `others` (list of enum, required)
  - Allowed values: `conversation_initiation_webhook`
- `tools_has_more` (boolean, optional, default: false) — Whether there are more tool dependents beyond the returned preview
- `agents_has_more` (boolean, optional, default: false) — Whether there are more agent dependents beyond the returned preview
- `phone_numbers` (list of DependentPhoneNumberIdentifier, optional)
- `phone_numbers_has_more` (boolean, optional, default: false) — Whether there are more phone number dependents beyond the returned preview
- `mcp_servers` (list of ConvAiStoredSecretDependenciesMcpServersItems, optional)

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ConvAiStoredSecretDependenciesToolsItems

- `type`: `available` (DependentAvailableToolIdentifier)
  - `access_level` (enum, required)
    - Allowed values: `admin`, `editor`, `commenter`, `viewer`
  - `created_at_unix_secs` (integer, required)
  - `id` (string, required)
  - `name` (string, required)
- `type`: `unknown` (DependentUnknownToolIdentifier)
  - `id` (string, required)

### ConvAiStoredSecretDependenciesAgentsItems

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

### DependentPhoneNumberIdentifier

- `phone_number_id` (string, required)
- `phone_number` (string, required)
- `label` (string, required)
- `provider` (enum, required)
  - Allowed values: `twilio`, `sip_trunk`, `exotel`

### ConvAiStoredSecretDependenciesMcpServersItems

- `type`: `available` (DependentAvailableMCPServerIdentifier)
  - `access_level` (enum, required)
    - Allowed values: `admin`, `editor`, `commenter`, `viewer`
  - `created_at_unix_secs` (integer, required)
  - `id` (string, required)
  - `name` (string, required)
- `type`: `unknown` (DependentUnknownMCPServerIdentifier)
  - `id` (string, required)

### ValidationErrorLocItems

- string
- integer

## Examples

**Response**

```json
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
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/secrets/secret_id"

response = requests.get(url)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/secrets/secret_id';
const options = {method: 'GET'};

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
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/secrets/secret_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/secrets/secret_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/secrets/secret_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/secrets/secret_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets/secret_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets/secret_id")! as URL,
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
