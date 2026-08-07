---
title: "Create a Project Self-Hosted Distribution Credential"
source: https://developers.deepgram.com/reference/self-hosted/distribution-credentials/create.md
path: reference/self-hosted/distribution-credentials/create
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Create a Project Self-Hosted Distribution Credential

POST https://api.deepgram.com/v1/projects/{project_id}/self-hosted/distribution/credentials
Content-Type: application/json

Creates a set of distribution credentials for the specified project

Reference: https://developers.deepgram.com/reference/self-hosted/distribution-credentials/create

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Request

### Path parameters

- `project_id` (string, required) — The unique identifier of the project

### Query parameters

- `scopes` (list of enum, optional, default: ["self-hosted:products"]) — List of permission scopes for the credentials
  - Allowed values: `self-hosted:products`, `self-hosted:product:api`, `self-hosted:product:engine`, `self-hosted:product:license-proxy`, `self-hosted:product:dgtools`, `self-hosted:product:billing`, `self-hosted:product:hotpepper`, `self-hosted:product:metrics-server`
- `provider` (enum, optional, default: quay) — The provider of the distribution service
  - Allowed values: `quay`

### Body (application/json)

- `comment` (string, optional) — Optional comment about the credentials

## Response

### 200

Single distribution credential

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

**Request**

```json
{}
```

**Response**

```json
{
  "member": {
    "member_id": "c7b9b131-73f3-11d9-8665-0b00d2e44b83",
    "email": "email@example.com"
  },
  "distribution_credentials": {
    "distribution_credentials_id": "82c32c10-53b2-4d23-993f-864b3d44502a",
    "provider": "quay",
    "scopes": [
      "self-hosted:product:api",
      "self-hosted:product:engine"
    ],
    "created": "2023-06-28T15:36:59.609841Z",
    "comment": "My Self-Hosted Distribution Credentials"
  }
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials"

payload = {}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials';
const options = {
  method: 'POST',
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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials"

	payload := strings.NewReader("{}")

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Token <apiKey>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials', [
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

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials");
var request = new RestRequest(Method.POST);
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/self-hosted/distribution/credentials")! as URL,
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
