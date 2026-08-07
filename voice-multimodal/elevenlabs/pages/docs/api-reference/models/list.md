---
title: "List models"
source: https://elevenlabs.io/docs/api-reference/models/list.md
path: docs/api-reference/models/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List models

GET https://api.elevenlabs.io/v1/models

Gets a list of available models.

Reference: https://elevenlabs.io/docs/api-reference/models/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Response

### 200

Successful Response

- `list of object`
  - `model_id` (string, required) — The unique identifier of the model.
  - `name` (string, optional) — The name of the model.
  - `can_be_finetuned` (boolean, optional) — Whether the model can be finetuned.
  - `can_do_text_to_speech` (boolean, optional) — Whether the model can do text-to-speech.
  - `can_do_voice_conversion` (boolean, optional) — Whether the model can do voice conversion.
  - `can_use_style` (boolean, optional) — Whether the model can use style.
  - `can_use_speaker_boost` (boolean, optional) — Whether the model can use speaker boost.
  - `serves_pro_voices` (boolean, optional) — Whether the model serves pro voices.
  - `token_cost_factor` (double, optional) — The cost factor for the model.
  - `description` (string, optional) — The description of the model.
  - `requires_alpha_access` (boolean, optional) — Whether the model requires alpha access.
  - `max_characters_request_free_user` (integer, optional) — The maximum number of characters that can be requested by a free user.
  - `max_characters_request_subscribed_user` (integer, optional) — The maximum number of characters that can be requested by a subscribed user.
  - `maximum_text_length_per_request` (integer, optional) — The maximum length of text that can be requested for this model.
  - `languages` (list of object, optional) — The languages supported by the model.
    - `language_id` (string, required) — The unique identifier of the language.
    - `name` (string, required) — The name of the language.
  - `model_rates` (object, optional) — The rates for the model.
    - `character_cost_multiplier` (double, required) — The cost multiplier for characters.
    - `cost_discount_multiplier` (double, optional, default: 1) — Discount multiplier applied to cost estimates. Defaults to 1.0 (no discount).
  - `concurrency_group` (string, optional) — The concurrency group for the model.

## Examples

**Response**

```json
[
  {
    "model_id": "string",
    "name": "string",
    "can_be_finetuned": true,
    "can_do_text_to_speech": true,
    "can_do_voice_conversion": true,
    "can_use_style": true,
    "can_use_speaker_boost": true,
    "serves_pro_voices": true,
    "token_cost_factor": 1.1,
    "description": "string",
    "requires_alpha_access": true,
    "max_characters_request_free_user": 1,
    "max_characters_request_subscribed_user": 1,
    "maximum_text_length_per_request": 1,
    "languages": [
      {
        "language_id": "string",
        "name": "string"
      }
    ],
    "model_rates": {
      "character_cost_multiplier": 1,
      "cost_discount_multiplier": 1
    },
    "concurrency_group": "string"
  }
]
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.models.list();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.models.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/models"

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

url = URI("https://api.elevenlabs.io/v1/models")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/models")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/models');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/models");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/models")! as URL,
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
