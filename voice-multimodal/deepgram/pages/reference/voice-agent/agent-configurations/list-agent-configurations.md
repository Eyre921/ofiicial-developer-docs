---
title: "List Agent Configurations"
source: https://developers.deepgram.com/reference/voice-agent/agent-configurations/list-agent-configurations.md
path: reference/voice-agent/agent-configurations/list-agent-configurations
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# List Agent Configurations

GET https://api.deepgram.com/v1/projects/{project_id}/agents

Returns all agent configurations for the specified project. Configurations are returned in their uninterpolated form—template variable placeholders appear as-is rather than with their substituted values.

Reference: https://developers.deepgram.com/reference/voice-agent/agent-configurations/list-agent-configurations

## Authentication

- `Authorization` header (required) (prefixed with ` Token  `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Request

### Path parameters

- `project_id` (string, required) — The unique identifier of the project

## Response

### 200

A list of agent configurations

- `agents` (list of AgentConfigurationV1, optional) — A list of agent configurations for the project

## Errors

### 400 Bad Request Error

Invalid Request

- `ErrorResponse`
  - ErrorResponseTextError: string
  - ErrorResponseLegacyError: ErrorResponseLegacyError
  - ErrorResponseModernError: ErrorResponseModernError

## Types

### AgentConfigurationV1

A reusable agent configuration

- `agent_id` (string, required) — The unique identifier of the agent configuration
- `config` (AgentConfigurationV1Config, required) — The agent configuration object
- `metadata` (map from string to string, optional) — A map of arbitrary key-value pairs for labeling or organizing the agent configuration
- `created_at` (string, optional) — Timestamp when the configuration was created
- `updated_at` (string, optional) — Timestamp when the configuration was last updated

### ErrorResponseLegacyError

- `err_code` (string, optional) — The error code
- `err_msg` (string, optional) — The error message
- `request_id` (string, optional) — The request ID

### ErrorResponseModernError

- `category` (string, optional) — The category of the error
- `message` (string, optional) — A message about the error
- `details` (string, optional) — A description of the error
- `request_id` (string, optional) — The unique identifier of the request

### AgentConfigurationV1Config

The agent configuration object

## Examples

**Response**

```json
{
  "agents": [
    {
      "agent_id": "string",
      "config": {},
      "metadata": {},
      "created_at": "2024-01-15T09:30:00Z",
      "updated_at": "2024-01-15T09:30:00Z"
    }
  ]
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents';
const options = {method: 'GET', headers: {Authorization: 'Token <apiKey>'}};

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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Token <apiKey>")

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Token <apiKey>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

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
