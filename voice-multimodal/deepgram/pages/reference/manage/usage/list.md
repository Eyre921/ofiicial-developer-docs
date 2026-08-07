---
title: "List Project Usage Fields"
source: https://developers.deepgram.com/reference/manage/usage/list.md
path: reference/manage/usage/list
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# List Project Usage Fields

GET https://api.deepgram.com/v1/projects/{project_id}/usage/fields

Lists the features, models, tags, languages, and processing method used for requests in the specified project

Reference: https://developers.deepgram.com/reference/manage/usage/list

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Request

### Path parameters

- `project_id` (string, required) — The unique identifier of the project

### Query parameters

- `start` (string, optional) — Start date of the requested date range. Format accepted is YYYY-MM-DD
- `end` (string, optional) — End date of the requested date range. Format accepted is YYYY-MM-DD

## Response

### 200

A list of fields for a specific project

- `tags` (list of string, optional) — List of tags associated with the project
- `models` (list of object, optional) — List of models available for the project.
  - `name` (string, optional) — Name of the model.
  - `language` (string, optional) — The language supported by the model (IETF language tag).
  - `version` (string, optional) — Version identifier of the model, typically with a date and a revision number.
  - `model_id` (string, optional) — Unique identifier for the model.
- `processing_methods` (list of string, optional) — Processing methods supported by the API
- `features` (list of string, optional) — API features available to the project

## Examples

**Response**

```json
{
  "tags": [
    "tag=dev",
    "tag=production"
  ],
  "models": [
    {
      "name": "2-medical-nova",
      "language": "en-MY",
      "version": "2024-05-31.13574",
      "model_id": "1234567890-12345-67890"
    }
  ],
  "processing_methods": [
    "sync",
    "streaming"
  ],
  "features": [
    "alternatives",
    "detect_entities",
    "detect_language"
  ]
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/usage/fields"

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/usage/fields';
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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/usage/fields"

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/usage/fields")

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

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/usage/fields")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/usage/fields', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/usage/fields");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/usage/fields")! as URL,
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
