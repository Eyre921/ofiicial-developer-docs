---
title: "Get Project Billing Breakdown"
source: https://developers.deepgram.com/reference/manage/billing/breakdown/get.md
path: reference/manage/billing/breakdown/get
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Get Project Billing Breakdown

GET https://api.deepgram.com/v1/projects/{project_id}/billing/breakdown

Retrieves the billing summary for a specific project, with various filter options or by grouping options.

Reference: https://developers.deepgram.com/reference/manage/billing/breakdown/get

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Request

### Path parameters

- `project_id` (string, required) — The unique identifier of the project

### Query parameters

- `start` (string, optional) — Start date of the requested date range. Format accepted is YYYY-MM-DD
- `end` (string, optional) — End date of the requested date range. Format accepted is YYYY-MM-DD
- `accessor` (string, optional) — Filter for requests where a specific accessor was used
- `deployment` (enum, optional) — Filter for requests where a specific deployment was used
  - Allowed values: `hosted`, `beta`, `self-hosted`
- `tag` (string, optional) — Filter for requests where a specific tag was used
- `line_item` (string, optional) — Filter requests by line item (e.g. streaming::nova-3)
- `grouping` (list of enum, optional) — Group billing breakdown by one or more dimensions (accessor, deployment, line_item, tags)
  - Allowed values: `accessor`, `deployment`, `line_item`, `tags`

## Response

### 200

Billing breakdown response

- `start` (string, required) — Start date of the billing summmary period
- `end` (string, required) — End date of the billing summary period
- `resolution` (object, required)
  - `units` (string, required) — Time unit for the resolution
  - `amount` (double, required) — Amount of units
- `results` (list of object, required)
  - `dollars` (float, required) — USD cost of the billing for this grouping
  - `grouping` (object, required)
    - `start` (string, optional) — Start date for this group
    - `end` (string, optional) — End date for this group
    - `accessor` (string, optional, nullable) — Optional accessor identifier, null unless grouped by accessor.
    - `deployment` (string, optional, nullable) — Optional deployment identifier, null unless grouped by deployment.
    - `line_item` (string, optional, nullable) — Optional line item identifier, null unless grouped by line item.
    - `tags` (list of string, optional, nullable) — Optional list of tags, null unless grouped by tags.

## Examples

**Response**

```json
{
  "start": "2025-01-16",
  "end": "2025-01-23",
  "resolution": {
    "units": "day",
    "amount": 1
  },
  "results": [
    {
      "dollars": 0.25,
      "grouping": {
        "start": "2025-01-16",
        "end": "2025-01-16",
        "accessor": "123456789012345678901234",
        "deployment": "hosted",
        "line_item": "streaming::nova-3",
        "tags": [
          "tag1",
          "tag2"
        ]
      }
    }
  ]
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/billing/breakdown"

querystring = {"accessor":"12345678-1234-1234-1234-123456789012","deployment":"hosted","grouping":"[\"deployment\",\"line_item\"]","line_item":"streaming::nova-3","tag":"tag1"}

headers = {"Authorization": "Token <apiKey>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/billing/breakdown?accessor=12345678-1234-1234-1234-123456789012&deployment=hosted&grouping=%5B%22deployment%22%2C%22line_item%22%5D&line_item=streaming%3A%3Anova-3&tag=tag1';
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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/billing/breakdown?accessor=12345678-1234-1234-1234-123456789012&deployment=hosted&grouping=%5B%22deployment%22%2C%22line_item%22%5D&line_item=streaming%3A%3Anova-3&tag=tag1"

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/billing/breakdown?accessor=12345678-1234-1234-1234-123456789012&deployment=hosted&grouping=%5B%22deployment%22%2C%22line_item%22%5D&line_item=streaming%3A%3Anova-3&tag=tag1")

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

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/billing/breakdown?accessor=12345678-1234-1234-1234-123456789012&deployment=hosted&grouping=%5B%22deployment%22%2C%22line_item%22%5D&line_item=streaming%3A%3Anova-3&tag=tag1")
  .header("Authorization", "Token <apiKey>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/billing/breakdown?accessor=12345678-1234-1234-1234-123456789012&deployment=hosted&grouping=%5B%22deployment%22%2C%22line_item%22%5D&line_item=streaming%3A%3Anova-3&tag=tag1', [
  'headers' => [
    'Authorization' => 'Token <apiKey>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/billing/breakdown?accessor=12345678-1234-1234-1234-123456789012&deployment=hosted&grouping=%5B%22deployment%22%2C%22line_item%22%5D&line_item=streaming%3A%3Anova-3&tag=tag1");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Token <apiKey>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Token <apiKey>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/billing/breakdown?accessor=12345678-1234-1234-1234-123456789012&deployment=hosted&grouping=%5B%22deployment%22%2C%22line_item%22%5D&line_item=streaming%3A%3Anova-3&tag=tag1")! as URL,
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
