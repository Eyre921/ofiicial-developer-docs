---
title: "Get a Project Request"
source: https://developers.deepgram.com/reference/manage/requests/get.md
path: reference/manage/requests/get
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Get a Project Request

GET https://api.deepgram.com/v1/projects/{project_id}/requests/{request_id}

Retrieves a specific request for a specific project

Reference: https://developers.deepgram.com/reference/manage/requests/get

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Request

### Path parameters

- `project_id` (string, required) — The unique identifier of the project
- `request_id` (string, required) — The unique identifier of the request

## Response

### 200

A specific request for a specific project

- `request` (object, optional) — A single request
  - `request_id` (string, optional) — The unique identifier of the request
  - `project_uuid` (string, optional) — The unique identifier of the project
  - `created` (string, optional) — The date and time the request was created
  - `path` (string, optional) — The API path of the request
  - `api_key_id` (string, optional) — The unique identifier of the API key
  - `response` (object, optional) — The response of the request
  - `code` (double, optional) — The response code of the request
  - `deployment` (string, optional) — The deployment type
  - `callback` (string, optional) — The callback URL for the request

## Examples

**Response**

```json
{
  "request": {
    "request_id": "a3f1c9d2-4b7e-4f9a-8c3d-2e5f7b9a1c0d",
    "project_uuid": "12345678-90ab-cdef-1234-567890abcdef",
    "created": "2024-01-15T09:48:20.000Z",
    "path": "/v1/listen?",
    "api_key_id": "b1e2c3d4-5678-90ab-cdef-1234567890ab",
    "response": {
      "details": {
        "usd": 0.0075,
        "duration": 30,
        "total_audio": 30,
        "channels": 1,
        "streams": 1,
        "tier": "base",
        "metadata": {},
        "models": [
          "1a2b3c4d-5e6f-4a8b-9c0d-1e2f3a4b5c6d"
        ],
        "method": "sync",
        "tags": [],
        "features": [],
        "config": {}
      },
      "token_details": [],
      "code": 200,
      "completed": "2024-01-15T09:48:21.000Z",
      "deployment": "hosted:us"
    },
    "callback": null
  }
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests/a3f1c9d2-4b7e-4f9a-8c3d-2e5f7b9a1c0d"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests/a3f1c9d2-4b7e-4f9a-8c3d-2e5f7b9a1c0d';
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

	url := "https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests/a3f1c9d2-4b7e-4f9a-8c3d-2e5f7b9a1c0d"

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

url = URI("https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests/a3f1c9d2-4b7e-4f9a-8c3d-2e5f7b9a1c0d")

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

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests/a3f1c9d2-4b7e-4f9a-8c3d-2e5f7b9a1c0d")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests/a3f1c9d2-4b7e-4f9a-8c3d-2e5f7b9a1c0d', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests/a3f1c9d2-4b7e-4f9a-8c3d-2e5f7b9a1c0d");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests/a3f1c9d2-4b7e-4f9a-8c3d-2e5f7b9a1c0d")! as URL,
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
