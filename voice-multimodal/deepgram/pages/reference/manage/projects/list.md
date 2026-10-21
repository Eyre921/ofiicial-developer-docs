---
title: "List Projects"
source: https://developers.deepgram.com/reference/manage/projects/list.md
path: reference/manage/projects/list
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# List Projects

GET https://api.deepgram.com/v1/projects

Retrieves basic information about the projects associated with the API key

Reference: https://developers.deepgram.com/reference/manage/projects/list

## Authentication

- `Authorization` header (required) (prefixed with ` Token  `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Response

### 200

A list of projects

- `projects` (list of ListProjectsV1ResponseProjectsItems, optional)

## Errors

### 400 Bad Request Error

Invalid Request

- `ErrorResponse`
  - ErrorResponseTextError: string
  - ErrorResponseLegacyError: ErrorResponseLegacyError
  - ErrorResponseModernError: ErrorResponseModernError

## Types

### ListProjectsV1ResponseProjectsItems

- `project_id` (string, optional) — The unique identifier of the project
- `name` (string, optional) — The name of the project

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
{
  "projects": [
    {
      "project_id": "string",
      "name": "string"
    }
  ]
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects';
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

	url := "https://api.deepgram.com/v1/projects"

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

url = URI("https://api.deepgram.com/v1/projects")

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

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects")! as URL,
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
