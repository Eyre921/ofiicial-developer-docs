---
title: "Get Audio Native Project Settings"
source: https://elevenlabs.io/docs/api-reference/audio-native/get-settings.md
path: docs/api-reference/audio-native/get-settings
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Audio Native Project Settings

GET https://api.elevenlabs.io/v1/audio-native/{project_id}/settings

Get player settings for the specific project.

Reference: https://elevenlabs.io/docs/api-reference/audio-native/get-settings

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `project_id` (string, required) — The ID of the Studio project.

## Response

### 200

Successful Response

- `enabled` (boolean, required) — Whether the project is enabled.
- `snapshot_id` (string, optional, nullable) — The ID of the latest snapshot of the project.
- `settings` (object, optional, nullable) — The settings of the project.
  - `title` (string, required) — The title of the project.
  - `image` (string, required) — The image of the project.
  - `author` (string, required) — The author of the project.
  - `small` (boolean, required) — Whether the project is small.
  - `text_color` (string, required) — The text color of the project.
  - `background_color` (string, required) — The background color of the project.
  - `sessionization` (integer, required) — The sessionization of the project. Specifies for how many minutes to persist the session across page reloads.
  - `audio_path` (string, optional, nullable) — The path of the audio file.
  - `audio_url` (string, optional, nullable) — The URL of the audio file.
  - `status` (enum, optional, default: ready) — Current state of the project
    - Allowed values: `processing`, `ready`

## Examples

**Response**

```json
{
  "enabled": true,
  "snapshot_id": "JBFqnCBsd6RMkjVDRZzb",
  "settings": {
    "title": "My Project",
    "image": "https://example.com/image.jpg",
    "author": "John Doe",
    "small": false,
    "text_color": "#000000",
    "background_color": "#FFFFFF",
    "sessionization": 1,
    "audio_path": "audio/my_project.mp3",
    "audio_url": "https://example.com/audio/my_project.mp3",
    "status": "ready"
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.audioNative.getSettings("project_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.audio_native.get_settings(
    project_id="project_id",
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/audio-native/project_id/settings"

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

url = URI("https://api.elevenlabs.io/v1/audio-native/project_id/settings")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/audio-native/project_id/settings")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/audio-native/project_id/settings');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/audio-native/project_id/settings");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/audio-native/project_id/settings")! as URL,
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
