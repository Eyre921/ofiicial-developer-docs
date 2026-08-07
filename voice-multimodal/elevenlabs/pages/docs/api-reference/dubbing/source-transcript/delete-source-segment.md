---
title: "Delete source segment"
source: https://elevenlabs.io/docs/api-reference/dubbing/source-transcript/delete-source-segment.md
path: docs/api-reference/dubbing/source-transcript/delete-source-segment
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Delete source segment

DELETE https://api.elevenlabs.io/v1/dubbing/project/{project_id}/transcript/segment/{segment_id}

Enterprise only. Remove a source segment from the transcript.

Reference: https://elevenlabs.io/docs/api-reference/dubbing/source-transcript/delete-source-segment

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `project_id` (string, required) — Identifier of the dubbing project.
- `segment_id` (string, required) — Identifier of the segment to remove.

## Response

### 200

Successful Response

- `revision` (integer, required) — The project's source-transcript revision after this edit.

## Examples

**Response**

```json
{
  "revision": 6
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.project.transcript.deleteSegment("proj_1601kwkyxp0hfzvtmyxwqxx6mcy3", "0199a3f0-1c2d-7abc-8def-0123456789ab");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.project.transcript.delete_segment(
    project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
    segment_id="0199a3f0-1c2d-7abc-8def-0123456789ab",
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

	url := "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab"

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

url = URI("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab");
var request = new RestRequest(Method.DELETE);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/project/proj_1601kwkyxp0hfzvtmyxwqxx6mcy3/transcript/segment/0199a3f0-1c2d-7abc-8def-0123456789ab")! as URL,
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
