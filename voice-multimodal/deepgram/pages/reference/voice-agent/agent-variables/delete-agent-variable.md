---
title: "Delete Agent Variable"
source: https://developers.deepgram.com/reference/voice-agent/agent-variables/delete-agent-variable.md
path: reference/voice-agent/agent-variables/delete-agent-variable
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Delete Agent Variable

DELETE https://api.deepgram.com/v1/projects/{project_id}/agent-variables/{variable_id}

Deletes the specified template variable

Reference: https://developers.deepgram.com/reference/voice-agent/agent-variables/delete-agent-variable

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Request

### Path parameters

- `project_id` (string, required) — The unique identifier of the project
- `variable_id` (string, required) — The unique identifier of the agent variable

## Response

### 200

Agent variable deleted

## Examples

**Request**

```json
{}
```

**Response**

```json
{}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890"

payload = {}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.delete(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890';
const options = {
  method: 'DELETE',
  headers: {Authorization: 'Token <apiKey>', 'Content-Type': 'application/json'},
  body: '{}'
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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("DELETE", url, payload)

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Token <apiKey>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Token <apiKey>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Authorization", "Token <apiKey>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Token <apiKey>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables/v1a2b3c4-d5e6-7890-abcd-ef1234567890")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
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
