---
title: "Get Voice Accents"
source: https://elevenlabs.io/docs/api-reference/voices/accents/get.md
path: docs/api-reference/voices/accents/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Voice Accents

GET https://api.elevenlabs.io/v1/voices/accents

Gets the list of available accents in the shared voice library.

Reference: https://elevenlabs.io/docs/api-reference/voices/accents/get

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `language` (string, optional, nullable) — If provided, only accents for this language code are returned.
- `model_id` (string, optional, nullable) — If provided, returns the accents available for this model. Defaults to the most complete accent list when omitted.

## Response

### 200

Successful Response

- `accents` (list of object, required) — A list of available voice accents.
  - `accent` (string, required) — The accent value used for filtering shared voices via the `accent` query parameter on `GET /v1/shared-voices`.
  - `language` (string, required) — The language code this accent belongs to, e.g. `en`.
  - `code` (string, required) — The full accent code, e.g. `en-american`.
  - `name` (string, required) — The human-readable accent name, e.g. `American`.

## Examples

**Response**

```json
{
  "accents": [
    {
      "accent": "american",
      "language": "en",
      "code": "en-american",
      "name": "American"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.accents.get({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.accents.get()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/voices/accents"

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

url = URI("https://api.elevenlabs.io/v1/voices/accents")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/voices/accents")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/voices/accents');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/accents");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/accents")! as URL,
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
