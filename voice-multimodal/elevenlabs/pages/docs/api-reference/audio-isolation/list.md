---
title: "Get Audio Isolation History"
source: https://elevenlabs.io/docs/api-reference/audio-isolation/list.md
path: docs/api-reference/audio-isolation/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Audio Isolation History

GET https://api.elevenlabs.io/v1/audio-isolation/history

Returns a list of all your audio isolation generations.

Reference: https://elevenlabs.io/docs/api-reference/audio-isolation/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `page_size` (integer, optional, default: 100) — How many history items to return at maximum. Defaults to 100.
- `page` (integer, optional, default: 1) — Page number for search pagination (1-based). Only used when search is provided.
- `search` (string, optional, nullable) — Optional search term used for filtering audio isolation history (title/text).

## Response

### 200

Successful Response

- `items` (list of AudioIsolationHistoryItemResponseModel, required)
- `has_more` (boolean, required)

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### AudioIsolationHistoryItemResponseModel

- `id` (string, required)
- `title` (string, required, nullable)
- `created_at_unix` (integer, required)
- `format` (string, required)
- `duration_seconds` (double, required, nullable)
- `download_url` (string, required, nullable)
- `icon_url` (string, required, nullable)
- `source_video_url` (string, required, nullable)
- `supports_video` (boolean, required)
- `processing` (boolean, required)
- `video_processing_failed` (boolean, required)
- `preview_b64` (string, required, nullable)

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

## Examples

**Response**

```json
{
  "items": [
    {
      "id": "string",
      "title": "string",
      "created_at_unix": 1,
      "format": "string",
      "duration_seconds": 1.1,
      "download_url": "string",
      "icon_url": "string",
      "source_video_url": "string",
      "supports_video": true,
      "processing": true,
      "video_processing_failed": true,
      "preview_b64": "string"
    }
  ],
  "has_more": true
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/audio-isolation/history"

querystring = {"search":"podcast"}

response = requests.get(url, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/audio-isolation/history?search=podcast';
const options = {method: 'GET'};

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

	url := "https://api.elevenlabs.io/v1/audio-isolation/history?search=podcast"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/audio-isolation/history?search=podcast")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/audio-isolation/history?search=podcast")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/audio-isolation/history?search=podcast');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/audio-isolation/history?search=podcast");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/audio-isolation/history?search=podcast")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

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
