---
title: "List pronunciation dictionaries"
source: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/list.md
path: docs/api-reference/pronunciation-dictionaries/list
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List pronunciation dictionaries

GET https://api.elevenlabs.io/v1/pronunciation-dictionaries

Get a list of the pronunciation dictionaries you have access to and their metadata

Reference: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/list

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `cursor` (string, optional, nullable) — Used for fetching next page. Cursor is returned in the response.
- `page_size` (integer, optional, default: 30) — How many pronunciation dictionaries to return at maximum. Can not exceed 100, defaults to 30.
- `sort` (enum, optional, nullable, default: creation_time_unix) — Which field to sort by, one of 'created_at_unix' or 'name'.
  - Allowed values: `creation_time_unix`, `name`
- `sort_direction` (string, optional, nullable, default: DESCENDING) — Which direction to sort the voices in. 'ascending' or 'descending'.
- `include_archived` (boolean, optional, default: true) — Whether to include archived pronunciation dictionaries in the response.

## Response

### 200

Successful Response

- `pronunciation_dictionaries` (list of object, required) — A list of pronunciation dictionaries and their metadata.
  - `id` (string, required) — The ID of the pronunciation dictionary.
  - `latest_version_id` (string, required) — The ID of the latest version of the pronunciation dictionary.
  - `latest_version_rules_num` (integer, required) — The number of rules in the latest version of the pronunciation dictionary.
  - `name` (string, required) — The name of the pronunciation dictionary.
  - `permission_on_resource` (enum, required, nullable) — The permission on the resource of the pronunciation dictionary.
    - Allowed values: `admin`, `editor`, `commenter`, `viewer`
  - `created_by` (string, required) — The user ID of the creator of the pronunciation dictionary.
  - `creation_time_unix` (integer, required) — The creation time of the pronunciation dictionary in Unix timestamp.
  - `archived_time_unix` (integer, optional, nullable) — The archive time of the pronunciation dictionary in Unix timestamp.
  - `description` (string, optional, nullable) — The description of the pronunciation dictionary.
- `has_more` (boolean, required) — Whether there are more pronunciation dictionaries to fetch.
- `next_cursor` (string, optional, nullable) — The next cursor to use for pagination.

## Examples

**Response**

```json
{
  "pronunciation_dictionaries": [
    {
      "id": "5xM3yVvZQKV0EfqQpLrJ",
      "latest_version_id": "5xM3yVvZQKV0EfqQpLr2",
      "latest_version_rules_num": 2,
      "name": "My Dictionary",
      "permission_on_resource": "admin",
      "created_by": "ar6633Es2kUjFXBdR1iVc9ztsXl1",
      "creation_time_unix": 1714156800,
      "description": "This is a test dictionary"
    }
  ],
  "has_more": false,
  "next_cursor": "5xM3yVvZQKV0EfqQpLr2"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.pronunciationDictionaries.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.pronunciation_dictionaries.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries"

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

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/pronunciation-dictionaries")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries")! as URL,
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
