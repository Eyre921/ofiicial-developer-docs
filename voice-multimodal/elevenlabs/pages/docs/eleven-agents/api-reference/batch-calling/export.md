---
title: "Export batch call results"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/export.md
path: docs/eleven-agents/api-reference/batch-calling/export
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Export batch call results

GET https://api.elevenlabs.io/v1/convai/batch-calling/{batch_id}/export

Download all recipients and conversation results for a terminal batch call as CSV.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/export

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `batch_id` (string, required)

### Query parameters

- `limit` (integer, optional) — Only export the first N recipients; used to preview the columns. Omit to export every recipient.

## Response

### 200

Batch call results CSV.

- File download.

## Errors

### 422 Batch Calls Export Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItem

## Examples

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/batch-calling/%3Abatch_id/export"

querystring = {"limit":"0"}

headers = {"xi-api-key": "string"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/batch-calling/%3Abatch_id/export?limit=0';
const options = {method: 'GET', headers: {'xi-api-key': 'string'}};

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

	url := "https://api.elevenlabs.io/v1/convai/batch-calling/%3Abatch_id/export?limit=0"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("xi-api-key", "string")

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

url = URI("https://api.elevenlabs.io/v1/convai/batch-calling/%3Abatch_id/export?limit=0")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'string'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/batch-calling/%3Abatch_id/export?limit=0")
  .header("xi-api-key", "string")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/batch-calling/%3Abatch_id/export?limit=0', [
  'headers' => [
    'xi-api-key' => 'string',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/batch-calling/%3Abatch_id/export?limit=0");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "string");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["xi-api-key": "string"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/batch-calling/%3Abatch_id/export?limit=0")! as URL,
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
