---
title: "Get crawl job"
source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-crawl-job.md
path: docs/api-reference/knowledge-base/get-crawl-job
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get crawl job

GET https://api.elevenlabs.io/v1/convai/knowledge-base/crawl/{crawl_job_id}

Get details about a specific crawl job including status and progress.

Reference: https://elevenlabs.io/docs/api-reference/knowledge-base/get-crawl-job

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
- `pattern` (string, optional, nullable)
- `status` (enum, optional, default: queued)
  - Allowed values: `queued`, `processing`, `succeeded`, `failed`, `skipped`, `cancelled`
- `pages_identified` (integer, optional, default: 0)
- `pages_scraped` (integer, optional, default: 0)
- `pages_skipped` (integer, optional, default: 0)
- `pages_failed` (integer, optional, default: 0)

## Examples

**Response**

```json
{
  "seed_url": "string",
  "max_depth": 1,
  "max_pages": 1,
  "root_folder_id": "string",
  "updated_at": 1,
  "id": "string",
  "created_at": 1,
  "type": "discovery",
  "pattern": "string",
  "status": "queued",
  "pages_identified": 0,
  "pages_scraped": 0,
  "pages_skipped": 0,
  "pages_failed": 0
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
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/crawl/crawl_job_id"

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/crawl/crawl_job_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/crawl/crawl_job_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/crawl/crawl_job_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/crawl/crawl_job_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/crawl/crawl_job_id")! as URL,
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
