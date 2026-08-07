---
title: "List Project Models"
source: https://developers.deepgram.com/reference/manage/projects/models/list.md
path: reference/manage/projects/models/list
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# List Project Models

GET https://api.deepgram.com/v1/projects/{project_id}/models

Returns metadata on all the latest models that a specific project has access to, including non-public models

Reference: https://developers.deepgram.com/reference/manage/projects/models/list

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Request

### Path parameters

- `project_id` (string, required) — The unique identifier of the project

### Query parameters

- `include_outdated` (boolean, optional) — returns non-latest versions of models

## Response

### 200

A list of models

- `stt` (list of object, optional)
  - `name` (string, optional)
  - `canonical_name` (string, optional)
  - `architecture` (string, optional)
  - `languages` (list of string, optional)
  - `version` (string, optional)
  - `uuid` (string, optional)
  - `batch` (boolean, optional)
  - `streaming` (boolean, optional)
  - `formatted_output` (boolean, optional)
- `tts` (list of object, optional)
  - `name` (string, optional)
  - `canonical_name` (string, optional)
  - `architecture` (string, optional)
  - `languages` (list of string, optional)
  - `version` (string, optional)
  - `uuid` (string, optional)
  - `metadata` (object, optional)
    - `accent` (string, optional)
    - `age` (string, optional)
    - `color` (string, optional)
    - `image` (string, optional)
    - `sample` (string, optional)
    - `tags` (list of string, optional)
    - `use_cases` (list of string, optional)

## Examples

**Response**

```json
{
  "stt": [
    {
      "name": "nova-3",
      "canonical_name": "nova-3",
      "architecture": "base",
      "languages": [
        "en",
        "en-us"
      ],
      "version": "2021-11-10.1",
      "uuid": "6b28e919-8427-4f32-9847-492e2efd7daf",
      "batch": true,
      "streaming": true,
      "formatted_output": true
    }
  ],
  "tts": [
    {
      "name": "zeus",
      "canonical_name": "aura-2-zeus-en",
      "architecture": "aura-2",
      "languages": [
        "en",
        "en-US"
      ],
      "version": "2025-04-07.0",
      "uuid": "2baf189d-91ac-481d-b6d1-750888667b31",
      "metadata": {
        "accent": "American",
        "age": "Adult",
        "color": "#C58DFF",
        "image": "https://static.deepgram.com/examples/avatars/zeus.jpg",
        "sample": "https://static.deepgram.com/examples/Aura-2-zeus.wav",
        "tags": [
          "masculine",
          "deep",
          "trustworthy",
          "smooth"
        ],
        "use_cases": [
          "IVR"
        ]
      }
    }
  ]
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models';
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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models"

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models")

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

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models")! as URL,
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
