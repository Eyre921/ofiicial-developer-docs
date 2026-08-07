---
title: "List crawl jobs"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/list-crawl-jobs.md
path: docs/eleven-agents/api-reference/knowledge-base/list-crawl-jobs
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List crawl jobs

GET https://api.elevenlabs.io/v1/convai/knowledge-base/crawl

Get a list of ongoing and recent crawl jobs for the user.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/list-crawl-jobs

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `include_job_ids` (string, optional) — Ids of additional crawl jobs to retrieve
- `page_size` (integer, optional, default: 30) — How many documents to return at maximum. Can not exceed 100, defaults to 30.
- `cursor` (string, optional) — Used for fetching next page. Cursor is returned in the response.

## Response

### 200

Successful Response

- `crawl_jobs` (list of object, required)
  - `seed_url` (string, required)
  - `max_depth` (integer, required)
  - `max_pages` (integer, required)
  - `root_folder_id` (string, required)
  - `updated_at` (integer, required)
  - `id` (string, required)
  - `created_at` (integer, required)
  - `type` (enum, optional, default: discovery)
    - Allowed values: `discovery`, `sitemap`
  - `pattern` (string, optional)
  - `status` (enum, optional, default: queued)
    - Allowed values: `queued`, `processing`, `succeeded`, `failed`, `skipped`, `cancelled`
  - `pages_identified` (integer, optional, default: 0)
  - `pages_scraped` (integer, optional, default: 0)
  - `pages_skipped` (integer, optional, default: 0)
  - `pages_failed` (integer, optional, default: 0)
- `next_cursor` (string, optional)

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "crawl_jobs": [
    {
      "seed_url": "https://example.com/docs",
      "max_depth": 3,
      "max_pages": 150,
      "root_folder_id": "folder_9a8b7c6d5e4f3g2h1i0j",
      "updated_at": 1685606400,
      "id": "crawljob_1234567890abcdef",
      "created_at": 1685520000,
      "type": "discovery",
      "pattern": "/docs/*",
      "status": "processing",
      "pages_identified": 120,
      "pages_scraped": 100,
      "pages_skipped": 10,
      "pages_failed": 5
    }
  ],
  "next_cursor": "cursor_abcdef1234567890"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.crawlJobs.list({
        cursor: "cursor",
        includeJobIds: [
            "include_job_ids",
        ],
        pageSize: 1,
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.crawl_jobs.list(
    cursor="cursor",
    include_job_ids=[
        "include_job_ids"
    ],
    page_size=1,
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/crawl?cursor=cursor&include_job_ids=%5B%22include_job_ids%22%5D&page_size=1"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/crawl?cursor=cursor&include_job_ids=%5B%22include_job_ids%22%5D&page_size=1")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/crawl?cursor=cursor&include_job_ids=%5B%22include_job_ids%22%5D&page_size=1")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/crawl?cursor=cursor&include_job_ids=%5B%22include_job_ids%22%5D&page_size=1', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/crawl?cursor=cursor&include_job_ids=%5B%22include_job_ids%22%5D&page_size=1");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/crawl?cursor=cursor&include_job_ids=%5B%22include_job_ids%22%5D&page_size=1")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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
