---
title: "Remove Voice From Collection"
source: https://elevenlabs.io/docs/api-reference/voices/collections/remove-voice.md
path: docs/api-reference/voices/collections/remove-voice
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Remove Voice From Collection

DELETE https://api.elevenlabs.io/v1/voices/collections/{collection_id}/voice/{voice_id}

Removes a voice from a voice collection. The voice itself is not deleted. Requires editor access to the collection.

Reference: https://elevenlabs.io/docs/api-reference/voices/collections/remove-voice

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `collection_id` (string, required) — Collection ID.
- `voice_id` (string, required) — Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

## Response

### 200

Successful Response

- `collection_id` (string, required) — The ID of the voice collection.
- `voice_id` (string, required) — The ID of the voice that was removed.

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

## Examples

**Response**

```json
{
  "collection_id": "string",
  "voice_id": "string"
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/voices/collections/collection_id/voice/21m00Tcm4TlvDq8ikWAM"

response = requests.delete(url)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/voices/collections/collection_id/voice/21m00Tcm4TlvDq8ikWAM';
const options = {method: 'DELETE'};

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

	url := "https://api.elevenlabs.io/v1/voices/collections/collection_id/voice/21m00Tcm4TlvDq8ikWAM"

	req, _ := http.NewRequest("DELETE", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/voices/collections/collection_id/voice/21m00Tcm4TlvDq8ikWAM")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/voices/collections/collection_id/voice/21m00Tcm4TlvDq8ikWAM")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/voices/collections/collection_id/voice/21m00Tcm4TlvDq8ikWAM');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/collections/collection_id/voice/21m00Tcm4TlvDq8ikWAM");
var request = new RestRequest(Method.DELETE);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/collections/collection_id/voice/21m00Tcm4TlvDq8ikWAM")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"

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
