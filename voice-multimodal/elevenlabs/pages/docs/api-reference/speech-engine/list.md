---
title: "List Speech Engines"
source: https://elevenlabs.io/docs/api-reference/speech-engine/list.md
path: docs/api-reference/speech-engine/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List Speech Engines

GET https://api.elevenlabs.io/v1/speech-engine

Returns a paginated list of Speech Engine resources.

Reference: https://elevenlabs.io/docs/api-reference/speech-engine/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `page_size` (integer, optional, default: 30) — How many Speech Engines to return at maximum. Can not exceed 100, defaults to 30.
- `search` (string, optional, nullable) — Search term to filter Speech Engines by name
- `sort_direction` (enum, optional) — The direction to sort the results
  - Allowed values: `asc`, `desc`
- `sort_by` (enum, optional, nullable) — The field to sort the results by
  - Allowed values: `name`, `created_at`, `call_count_7d`
- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `speech_engines` (list of object, required) — The speech engines matching the query
  - `speech_engine_id` (string, required) — The speech engine resource ID
  - `name` (string, required) — Human-readable name for the speech engine
  - `created_at_unix_secs` (integer, required) — Creation time in Unix seconds
  - `tags` (list of string, required) — Arbitrary tags for categorization and filtering
  - `access_info` (object, required) — The access information of the speech engine for the user
    - `is_creator` (boolean, required) — Whether the user making the request is the creator of the agent
    - `creator_name` (string, required) — Name of the agent's creator
    - `creator_email` (string, required) — Email of the agent's creator
    - `role` (enum, required) — The role of the user making the request
      - Allowed values: `admin`, `editor`, `commenter`, `viewer`
    - `anonymous_access_level_override` (enum, optional, nullable) — The access level for anonymous users. If None, the resource is not shared publicly.
      - Allowed values: `admin`, `editor`, `commenter`, `viewer`
    - `access_source` (enum, optional, nullable) — Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.
      - Allowed values: `creator`, `explicit`, `workspace_admin`, `workspace_default`
- `has_more` (boolean, required) — Whether there are more results
- `next_cursor` (string, optional, nullable) — Cursor for fetching the next page

## Examples

**Response**

```json
{
  "speech_engines": [
    {
      "speech_engine_id": "seng_3701k3ttaq12ewp8b7qv5rfyszkz",
      "name": "My Speech Engine",
      "created_at_unix_secs": 1714000000,
      "tags": [
        "production",
        "v1"
      ],
      "access_info": {
        "is_creator": true,
        "creator_name": "John Doe",
        "creator_email": "john@example.com",
        "role": "admin"
      }
    }
  ],
  "has_more": false
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.speechEngine.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.speech_engine.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/speech-engine"

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

url = URI("https://api.elevenlabs.io/v1/speech-engine")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/speech-engine")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/speech-engine');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/speech-engine");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/speech-engine")! as URL,
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
