---
title: "Pause all campaigns"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/campaigns/pause-all.md
path: docs/eleven-agents/api-reference/campaigns/pause-all
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Pause all campaigns

POST https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/pause-all

Pause every running outbound campaign in the workspace. Paused campaigns place no new calls until resumed.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/campaigns/pause-all

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Response

### 200

Successful Response

- `paused_campaign_ids` (list of string, required)

## Errors

### 422 Outbound Campaigns Pause All Request Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### ValidationError

- `loc` (list of ValidationErrorLocItem, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItem

- string
- integer

## Examples

**Response**

```json
{
  "paused_campaign_ids": [
    "paused_campaign_ids"
  ]
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/pause-all"

response = requests.post(url)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/pause-all';
const options = {method: 'POST'};

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

	url := "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/pause-all"

	req, _ := http.NewRequest("POST", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/pause-all")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/pause-all")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/pause-all');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/pause-all");
var request = new RestRequest(Method.POST);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/outbound-campaigns/campaigns/pause-all")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"

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
