---
title: "Create Agent Variable"
source: https://developers.deepgram.com/reference/voice-agent/agent-variables/create-agent-variable.md
path: reference/voice-agent/agent-variables/create-agent-variable
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Create Agent Variable

POST https://api.deepgram.com/v1/projects/{project_id}/agent-variables
Content-Type: application/json

Creates a new template variable. Variables follow the `DG_<VARIABLE_NAME>` naming format and can substitute any JSON value in an agent configuration.

Reference: https://developers.deepgram.com/reference/voice-agent/agent-variables/create-agent-variable

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Request

### Path parameters

- `project_id` (string, required) — The unique identifier of the project

### Body (application/json)

- `key` (string, required) — The variable name, following the DG\_\<VARIABLE\_NAME> format
- `value` (any, required) — The value to substitute. Can be any valid JSON type (string, number, boolean, object, or array)
- `api_version` (integer, optional, default: 1) — API version. Defaults to 1

## Response

### 200

Agent variable created successfully

- `variable_id` (string, required) — The unique identifier of the variable
- `key` (string, required) — The variable name, following the DG\_\<VARIABLE\_NAME> format
- `value` (any, required) — The value to substitute. Can be any valid JSON type
- `created_at` (string, optional) — Timestamp when the variable was created
- `updated_at` (string, optional) — Timestamp when the variable was last updated

## Examples

**Request**

```json
{
  "key": "DG_API_TIMEOUT",
  "value": 30
}
```

**Response**

```json
{
  "variable_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "key": "DG_API_TIMEOUT",
  "value": 30,
  "created_at": "2024-01-15T09:30:00Z",
  "updated_at": "2024-01-15T09:30:00Z"
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables"

payload = {
    "key": "DG_API_TIMEOUT",
    "value": 30
}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables';
const options = {
  method: 'POST',
  headers: {Authorization: 'Token <apiKey>', 'Content-Type': 'application/json'},
  body: '{"key":"DG_API_TIMEOUT","value":30}'
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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables"

	payload := strings.NewReader("{\n  \"key\": \"DG_API_TIMEOUT\",\n  \"value\": 30\n}")

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Token <apiKey>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"key\": \"DG_API_TIMEOUT\",\n  \"value\": 30\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("{\n  \"key\": \"DG_API_TIMEOUT\",\n  \"value\": 30\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables', [
  'body' => '{
  "key": "DG_API_TIMEOUT",
  "value": 30
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

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Token <apiKey>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"key\": \"DG_API_TIMEOUT\",\n  \"value\": 30\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Token <apiKey>",
  "Content-Type": "application/json"
]
let parameters = [
  "key": "DG_API_TIMEOUT",
  "value": 30
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/agent-variables")! as URL,
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
