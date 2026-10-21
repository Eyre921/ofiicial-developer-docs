---
title: "List Project Members"
source: https://developers.deepgram.com/reference/manage/members/list.md
path: reference/manage/members/list
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# List Project Members

GET https://api.deepgram.com/v1/projects/{project_id}/members

Retrieves a list of members for a given project

Reference: https://developers.deepgram.com/reference/manage/members/list

## Authentication

- `Authorization` header (required) (prefixed with ` Token  `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Request

### Path parameters

- `project_id` (string, required) — The unique identifier of the project

## Response

### 200

A list of members for a given project

- `members` (list of ListProjectMembersV1ResponseMembersItems, optional)

## Errors

### 400 Bad Request Error

Invalid Request

- `ErrorResponse`
  - ErrorResponseTextError: string
  - ErrorResponseLegacyError: ErrorResponseLegacyError
  - ErrorResponseModernError: ErrorResponseModernError

## Types

### ListProjectMembersV1ResponseMembersItems

- `member_id` (string, optional) — The unique identifier of the member
- `scopes` (list of string, optional) — The API scopes of the member
- `email` (string, optional)
- `first_name` (string, optional)
- `last_name` (string, optional)

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
  "members": [
    {
      "member_id": "string",
      "scopes": [
        "string"
      ],
      "email": "string",
      "first_name": "string",
      "last_name": "string"
    }
  ]
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/members"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/members';
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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/members"

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/members")

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

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/members")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/members', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/members");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/members")! as URL,
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
