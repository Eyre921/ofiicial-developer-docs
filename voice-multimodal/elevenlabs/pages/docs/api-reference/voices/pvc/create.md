---
title: "Create PVC voice"
source: https://elevenlabs.io/docs/api-reference/voices/pvc/create.md
path: docs/api-reference/voices/pvc/create
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create PVC voice

POST https://api.elevenlabs.io/v1/voices/pvc
Content-Type: application/json

Creates a new PVC voice with metadata but no samples

Reference: https://elevenlabs.io/docs/api-reference/voices/pvc/create

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (application/json)

- `name` (string, required) — The name that identifies this voice. This will be displayed in the dropdown of the website.
- `language` (string, required) — Language used in the samples.
- `description` (string, optional, nullable) — Description to use for the created voice.
- `labels` (map from string to string, optional, nullable) — Labels for the voice. Keys can be language, accent, gender, or age.

## Response

### 200

Successful Response

- `voice_id` (string, required) — The ID of the voice.

## Examples

**Request**

```json
{
  "name": "John Smith",
  "language": "en"
}
```

**Response**

```json
{
  "voice_id": "b38kUX8pkfYO2kHyqfFy"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.pvc.create({
        name: "John Smith",
        language: "en",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.pvc.create(
    name="John Smith",
    language="en",
)

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

	url := "https://api.elevenlabs.io/v1/voices/pvc"

	payload := strings.NewReader("{\n  \"name\": \"John Smith\",\n  \"language\": \"en\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/voices/pvc")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"John Smith\",\n  \"language\": \"en\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/voices/pvc")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"John Smith\",\n  \"language\": \"en\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/voices/pvc', [
  'body' => '{
  "name": "John Smith",
  "language": "en"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/pvc");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"John Smith\",\n  \"language\": \"en\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "name": "John Smith",
  "language": "en"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/pvc")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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
