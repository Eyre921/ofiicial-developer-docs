---
title: "Get Audio Effects Catalog"
source: https://elevenlabs.io/docs/api-reference/audio-effects/get-catalog.md
path: docs/api-reference/audio-effects/get-catalog
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Audio Effects Catalog

GET https://api.elevenlabs.io/v1/audio-effects/catalog

Lists the filter presets, reverb environments, and background noises that `audio_effects` can reference in Text to Speech, Text to Dialogue, and agent configurations.

Reference: https://elevenlabs.io/docs/api-reference/audio-effects/get-catalog

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Response

### 200

Successful Response

- `filter_presets` (list of AudioEffectsFilterPresetResponseModel, required)
- `environments` (list of AudioEffectsEnvironmentResponseModel, required)
- `background_noises` (list of AudioEffectsBackgroundNoiseResponseModel, required)

## Errors

### 422 Unprocessable Entity Error

Validation Error

- `detail` (list of ValidationError, optional)

## Types

### AudioEffectsFilterPresetResponseModel

- `filter_preset_id` (string, required) — Value for `audio_effects.filter_preset_id`.
- `name` (string, required) — Display name.
- `description` (string, required, nullable) — What the preset sounds like.

### AudioEffectsEnvironmentResponseModel

- `environment_id` (string, required) — Value for `audio_effects.environment_id`.
- `name` (string, required) — Display name.
- `description` (string, required, nullable) — What the space sounds like.

### AudioEffectsBackgroundNoiseResponseModel

- `background_noise_id` (string, required) — Value for `audio_effects.background_noise_id`.
- `name` (string, required) — Display name.
- `description` (string, required, nullable) — What the noise bed sounds like.

### ValidationError

- `loc` (list of ValidationErrorLocItems, required)
- `msg` (string, required)
- `type` (string, required)

### ValidationErrorLocItems

## Examples

**Response**

```json
{
  "filter_presets": [
    {
      "filter_preset_id": "string",
      "name": "string",
      "description": "string"
    }
  ],
  "environments": [
    {
      "environment_id": "string",
      "name": "string",
      "description": "string"
    }
  ],
  "background_noises": [
    {
      "background_noise_id": "string",
      "name": "string",
      "description": "string"
    }
  ]
}
```

**SDK Code**

```python
import requests

url = "https://api.elevenlabs.io/v1/audio-effects/catalog"

response = requests.get(url)

print(response.json())
```

```javascript
const url = 'https://api.elevenlabs.io/v1/audio-effects/catalog';
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

	url := "https://api.elevenlabs.io/v1/audio-effects/catalog"

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

url = URI("https://api.elevenlabs.io/v1/audio-effects/catalog")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/audio-effects/catalog")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/audio-effects/catalog');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/audio-effects/catalog");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/audio-effects/catalog")! as URL,
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
