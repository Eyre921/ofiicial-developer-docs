---
title: "Get crawl job"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/get-crawl-job.md
path: docs/eleven-agents/api-reference/knowledge-base/get-crawl-job
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get crawl job

GET https://api.elevenlabs.io/v1/convai/knowledge-base/crawl/{crawl_job_id}

Get details about a specific crawl job including status and progress.

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/get-crawl-job

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `crawl_job_id` (string, required) — The id of the crawl job to retrieve

## Response

### 200

Successful Response

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

## Examples

**Request**

```json
{}
```

**Response**

```json
{
  "seed_url": "https://www.example.com",
  "max_depth": 3,
  "max_pages": 100,
  "root_folder_id": "folder_9a8b7c6d5e4f3g2h1i0j",
  "updated_at": 1687804800,
  "id": "crawljob_1234567890abcdef",
  "created_at": 1687718400,
  "type": "discovery",
  "pattern": "/blog/*",
  "status": "processing",
  "pages_identified": 75,
  "pages_scraped": 50,
  "pages_skipped": 10,
  "pages_failed": 5
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.crawlJobs.get("crawl_job_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.crawl_jobs.get(
    crawl_job_id="crawl_job_id",
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/crawl/crawl_job_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/crawl/crawl_job_id")

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

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/crawl/crawl_job_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/crawl/crawl_job_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/crawl/crawl_job_id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/crawl/crawl_job_id")! as URL,
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
