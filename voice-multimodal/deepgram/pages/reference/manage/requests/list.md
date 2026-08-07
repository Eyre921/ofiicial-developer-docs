---
title: "List Project Requests"
source: https://developers.deepgram.com/reference/manage/requests/list.md
path: reference/manage/requests/list
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# List Project Requests

GET https://api.deepgram.com/v1/projects/{project_id}/requests

Generates a list of requests for a specific project

Reference: https://developers.deepgram.com/reference/manage/requests/list

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Request

### Path parameters

- `project_id` (string, required) — The unique identifier of the project

### Query parameters

- `start` (string, optional) — Start date of the requested date range. Formats accepted are YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or YYYY-MM-DDTHH:MM:SS+HH:MM
- `end` (string, optional) — End date of the requested date range. Formats accepted are YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or YYYY-MM-DDTHH:MM:SS+HH:MM
- `limit` (double, optional, default: 10) — Number of results to return per page. Default 10. Range [1,1000]
- `page` (double, optional) — Navigate and return the results to retrieve specific portions of information of the response
- `accessor` (string, optional) — Filter for requests where a specific accessor was used
- `request_id` (string, optional) — Filter for a specific request id
- `deployment` (enum, optional) — Filter for requests where a specific deployment was used
  - Allowed values: `hosted`, `beta`, `self-hosted`
- `endpoint` (enum, optional) — Filter for requests where a specific endpoint was used
  - Allowed values: `listen`, `read`, `speak`, `agent`
- `method` (enum, optional) — Filter for requests where a specific method was used
  - Allowed values: `sync`, `async`, `streaming`
- `status` (enum, optional) — Filter for requests that succeeded (status code \< 300) or failed (status code >=400)
  - Allowed values: `succeeded`, `failed`

## Response

### 200

A list of requests for a specific project

- `page` (double, optional) — The page number of the paginated response
- `limit` (double, optional) — The number of results per page
- `requests` (list of object, optional)
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
  "page": 0,
  "limit": 10,
  "requests": [
    {
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
  ]
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests';
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

	url := "https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests"

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

url = URI("https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests")

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

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/12345678-90ab-cdef-1234-567890abcdef/requests")! as URL,
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
