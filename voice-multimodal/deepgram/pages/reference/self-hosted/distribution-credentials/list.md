---
title: "List Project Self-Hosted Distribution Credentials"
source: https://developers.deepgram.com/reference/self-hosted/distribution-credentials/list.md
path: reference/self-hosted/distribution-credentials/list
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# List Project Self-Hosted Distribution Credentials

GET https://api.deepgram.com/v1/projects/{project_id}/self-hosted/distribution/credentials

Lists sets of distribution credentials for the specified project

Reference: https://developers.deepgram.com/reference/self-hosted/distribution-credentials/list

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Request

### Path parameters

- `project_id` (string, required) — The unique identifier of the project

## Response

### 200

A list of distribution credentials for a specific project

- `distribution_credentials` (list of object, optional) — Array of distribution credentials with associated member information
  - `member` (object, required)
    - `member_id` (string, required) — Unique identifier for the member
    - `email` (string, required) — Email address of the member
  - `distribution_credentials` (object, required)
    - `distribution_credentials_id` (string, required) — Unique identifier for the distribution credentials
    - `provider` (string, required) — The provider of the distribution service
    - `scopes` (list of string, required) — List of permission scopes for the credentials
    - `created` (string, required) — Timestamp when the credentials were created
    - `comment` (string, optional) — Optional comment about the credentials

## Examples

**Response**

```json
{
  "distribution_credentials": [
    {
      "member": {
        "member_id": "3376abcd-8e5e-49d3-92d4-876d3a4f0363",
        "email": "email@example.com"
      },
      "distribution_credentials": {
        "distribution_credentials_id": "8b36cfd0-472f-4a21-833f-2d6343c3a2f3",
        "provider": "quay",
        "scopes": [
          "self-hosted:product:api",
          "self-hosted:product:engine"
        ],
        "created": "2023-06-28T15:36:59.609841Z",
        "comment": "My Self-Hosted Distribution Credentials"
      }
    }
  ]
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials';
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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials"

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials")

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

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials")! as URL,
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
