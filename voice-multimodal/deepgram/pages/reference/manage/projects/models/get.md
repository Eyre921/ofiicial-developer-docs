---
title: "Get a Project Model"
source: https://developers.deepgram.com/reference/manage/projects/models/get.md
path: reference/manage/projects/models/get
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Get a Project Model

GET https://api.deepgram.com/v1/projects/{project_id}/models/{model_id}

Returns metadata for a specific model

Reference: https://developers.deepgram.com/reference/manage/projects/models/get

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Request

### Path parameters

- `project_id` (string, required) — The unique identifier of the project
- `model_id` (string, required) — The specific UUID of the model

## Response

### 200

A model object that can be either STT or TTS

- `object or object`
  - object
    - `name` (string, optional)
    - `canonical_name` (string, optional)
    - `architecture` (string, optional)
    - `languages` (list of string, optional)
    - `version` (string, optional)
    - `uuid` (string, optional)
    - `batch` (boolean, optional)
    - `streaming` (boolean, optional)
    - `formatted_output` (boolean, optional)
  - object
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
  "name": "general",
  "canonical_name": "enhanced-general",
  "architecture": "polaris",
  "languages": [
    "en",
    "en-us"
  ],
  "version": "2022-05-18.1",
  "uuid": "c7226e9e-ae1c-4057-ae2a-a71a6b0dc588",
  "batch": true,
  "streaming": true,
  "formatted_output": false
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models/af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models/af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291';
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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models/af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291"

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models/af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291")

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

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models/af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models/af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models/af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/models/af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291")! as URL,
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
