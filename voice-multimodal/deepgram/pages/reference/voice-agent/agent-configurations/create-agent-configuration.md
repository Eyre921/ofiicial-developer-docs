---
title: "Create Agent Configuration"
source: https://developers.deepgram.com/reference/voice-agent/agent-configurations/create-agent-configuration.md
path: reference/voice-agent/agent-configurations/create-agent-configuration
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Create Agent Configuration

POST https://api.deepgram.com/v1/projects/{project_id}/agents
Content-Type: application/json

Creates a new reusable agent configuration. The `config` field must be a valid JSON string representing the `agent` block of a Settings message. The returned `agent_id` can be passed in place of the full `agent` object in future Settings messages.

Reference: https://developers.deepgram.com/reference/voice-agent/agent-configurations/create-agent-configuration

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Request

### Path parameters

- `project_id` (string, required) — The unique identifier of the project

### Body (application/json)

- `config` (string, required) — A valid JSON string representing the agent block of a Settings message
- `metadata` (map from string to string, optional) — A map of arbitrary key-value pairs for labeling or organizing the agent configuration
- `api_version` (integer, optional, default: 1) — API version. Defaults to 1

## Response

### 200

Agent configuration created successfully

- `agent_id` (string, required) — The unique identifier of the newly created agent configuration
- `config` (object, required) — The parsed agent configuration object
- `metadata` (map from string to string, optional) — Metadata associated with the agent configuration

## Examples

**Request**

```json
{
  "config": "{\"language\":\"en-US\",\"model\":\"general\",\"punctuate\":true,\"profanity_filter\":false}"
}
```

**Response**

```json
{
  "agent_id": "agent_9f8b7c6d5e4a3b2c1d0e",
  "config": {},
  "metadata": {}
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents"

payload = { "config": "{\"language\":\"en-US\",\"model\":\"general\",\"punctuate\":true,\"profanity_filter\":false}" }
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents';
const options = {
  method: 'POST',
  headers: {Authorization: 'Token <apiKey>', 'Content-Type': 'application/json'},
  body: '{"config":"{\"language\":\"en-US\",\"model\":\"general\",\"punctuate\":true,\"profanity_filter\":false}"}'
};

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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents"

	payload := strings.NewReader("{\n  \"config\": \"{\\\"language\\\":\\\"en-US\\\",\\\"model\\\":\\\"general\\\",\\\"punctuate\\\":true,\\\"profanity_filter\\\":false}\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Token <apiKey>")
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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Token <apiKey>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"config\": \"{\\\"language\\\":\\\"en-US\\\",\\\"model\\\":\\\"general\\\",\\\"punctuate\\\":true,\\\"profanity_filter\\\":false}\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("{\n  \"config\": \"{\\\"language\\\":\\\"en-US\\\",\\\"model\\\":\\\"general\\\",\\\"punctuate\\\":true,\\\"profanity_filter\\\":false}\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents', [
  'body' => '{
  "config": "{\\"language\\":\\"en-US\\",\\"model\\":\\"general\\",\\"punctuate\\":true,\\"profanity_filter\\":false}"
}',
  'headers' => [
    'Authorization' => 'Token <apiKey>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Token <apiKey>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"config\": \"{\\\"language\\\":\\\"en-US\\\",\\\"model\\\":\\\"general\\\",\\\"punctuate\\\":true,\\\"profanity_filter\\\":false}\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Token <apiKey>",
  "Content-Type": "application/json"
]
let parameters = ["config": "{\"language\":\"en-US\",\"model\":\"general\",\"punctuate\":true,\"profanity_filter\":false}"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents")! as URL,
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
