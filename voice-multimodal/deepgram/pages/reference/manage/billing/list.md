---
title: "Get Project Balances"
source: https://developers.deepgram.com/reference/manage/billing/list.md
path: reference/manage/billing/list
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Get Project Balances

GET https://api.deepgram.com/v1/projects/{project_id}/balances

Generates a list of outstanding balances for the specified project

Reference: https://developers.deepgram.com/reference/manage/billing/list

## Authentication

- `Authorization` header (required) (prefixed with `Token `) — Use `Authorization: Token <API_KEY>` Example: `Authorization: Token 12345abcdef`

## Request

### Path parameters

- `project_id` (string, required) — The unique identifier of the project

## Response

### 200

A list of outstanding balances

- `balances` (list of object, optional)
  - `balance_id` (string, optional) — The unique identifier of the balance
  - `amount` (double, optional, default: 0) — The amount of the balance
  - `units` (string, optional) — The units of the balance, such as "USD"
  - `purchase_order_id` (string, optional) — Description or reference of the purchase

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "balances": [
    {
      "balance_id": "b7f3c9d2-4a1e-4f8b-9c3d-2e5a7f8b9c1d",
      "amount": 1250.75,
      "units": "USD",
      "purchase_order_id": "PO-2024-04567"
    }
  ]
}
```

**SDK Code**

```python
import requests

url = "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/balances"

payload = {}
headers = {
    "Authorization": "Token <apiKey>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/balances';
const options = {
  method: 'GET',
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

	url := "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/balances"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

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

url = URI("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/balances")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Token <apiKey>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/balances")
  .header("Authorization", "Token <apiKey>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/balances', [
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

var client = new RestClient("https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/balances");
var request = new RestRequest(Method.GET);
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.deepgram.com/v1/projects/123456-7890-1234-5678-901234/balances")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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
