---
title: "Delete Agent Configuration"
source: https://developers.deepgram.com/reference/voice-agent/agent-configurations/delete-agent-configuration.md
path: reference/voice-agent/agent-configurations/delete-agent-configuration
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Delete Agent Configuration

DELETE https://api.deepgram.com/v1/projects/{project_id}/agents/{agent_id}

Deletes the specified agent configuration. Deleting an agent configuration can cause a production outage if your service references this agent UUID. Migrate all active sessions to a new configuration before deleting.

Reference: https://developers.deepgram.com/reference/voice-agent/agent-configurations/delete-agent-configuration

## Authentication

- `Authorization` header (required) (prefixed with ` Token  `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Request

### Path parameters

- `project_id` (string, required) — The unique identifier of the project
- `agent_id` (string, required) — The unique identifier of the agent configuration

## Response

### 200

Agent configuration deleted

## Errors

### 400 Bad Request Error

Invalid Request

- `ErrorResponse`
  - ErrorResponseTextError: string
  - ErrorResponseLegacyError: ErrorResponseLegacyError
  - ErrorResponseModernError: ErrorResponseModernError

## Types

### ErrorResponseLegacyError

- `err_code` (string, optional) — The error code
- `err_msg` (string, optional) — The error message
- `request_id` (string, optional) — The request ID

### ErrorResponseModernError

- `category` (string, optional) — The category of the error
- `message` (string, optional) — A message about the error
- `details` (string, optional) — A description of the error
- `request_id` (string, optional) — The unique identifier of the request

## Examples

**Response**

```json
{}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents/a1b2c3d4-e5f6-7890-abcd-ef1234567890"

headers = {"Authorization": "Token <apiKey>"}

response = requests.delete(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents/a1b2c3d4-e5f6-7890-abcd-ef1234567890';
const options = {method: 'DELETE', headers: {Authorization: 'Token <apiKey>'}};

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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents/a1b2c3d4-e5f6-7890-abcd-ef1234567890"

	req, _ := http.NewRequest("DELETE", url, nil)

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents/a1b2c3d4-e5f6-7890-abcd-ef1234567890")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Token <apiKey>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents/a1b2c3d4-e5f6-7890-abcd-ef1234567890")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents/a1b2c3d4-e5f6-7890-abcd-ef1234567890', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents/a1b2c3d4-e5f6-7890-abcd-ef1234567890");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agents/a1b2c3d4-e5f6-7890-abcd-ef1234567890")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
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
