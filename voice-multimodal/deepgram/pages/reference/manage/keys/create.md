---
title: "Create a Project Key"
source: https://developers.deepgram.com/reference/manage/keys/create.md
path: reference/manage/keys/create
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Create a Project Key

POST https://api.deepgram.com/v1/projects/{project_id}/keys
Content-Type: application/json

Creates a new API key with specified settings for the project

Reference: https://developers.deepgram.com/reference/manage/keys/create

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Request

### Path parameters

- `project_id` (string, required) — The unique identifier of the project

### Body (application/json)

- `any or any`

## Response

### 200

API key created successfully

- `api_key_id` (string, optional) — The unique identifier of the API key
- `key` (string, optional) — The API key
- `comment` (string, optional) — A comment for the API key
- `scopes` (list of string, optional) — The scopes for the API key
- `tags` (list of string, optional) — The tags for the API key
- `expiration_date` (string, optional) — The expiration date of the API key

## Examples

**Request**

```json
{
  "expiration_date": "2026-01-01T00:00:00Z"
}
```

**Response**

```json
{
  "api_key_id": "1234567890abcdef1234567890abcdef",
  "key": "1234567890abcdef1234567890abcdef",
  "comment": "a comment",
  "scopes": [
    "member"
  ],
  "tags": [
    "tag-1"
  ],
  "expiration_date": "2024-05-01T00:00:00.000000Z"
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/keys"

payload = { "expiration_date": "2026-01-01T00:00:00Z" }
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/keys';
const options = {
  method: 'POST',
  headers: {Authorization: 'Token <apiKey>', 'Content-Type': 'application/json'},
  body: '{"expiration_date":"2026-01-01T00:00:00Z"}'
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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/keys"

	payload := strings.NewReader("{\n  \"expiration_date\": \"2026-01-01T00:00:00Z\"\n}")

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/keys")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Token <apiKey>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"expiration_date\": \"2026-01-01T00:00:00Z\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/keys")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("{\n  \"expiration_date\": \"2026-01-01T00:00:00Z\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/keys', [
  'body' => '{
  "expiration_date": "2026-01-01T00:00:00Z"
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

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/keys");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Token <apiKey>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"expiration_date\": \"2026-01-01T00:00:00Z\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Token <apiKey>",
  "Content-Type": "application/json"
]
let parameters = ["expiration_date": "2026-01-01T00:00:00Z"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/keys")! as URL,
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
