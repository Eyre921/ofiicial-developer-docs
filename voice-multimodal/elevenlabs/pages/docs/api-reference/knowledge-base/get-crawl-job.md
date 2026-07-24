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

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/knowledge-base/crawl/{crawl_job_id}:
    get:
      operationId: get
      summary: Get Crawl Job Details
      description: Get details about a specific crawl job including status and progress.
      tags:
        - crawlJobs
      parameters:
        - name: crawl_job_id
          in: path
          description: The id of the crawl job to retrieve
          required: true
          schema:
            type: string
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetCrawlJobResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
servers:
  - url: https://api.elevenlabs.io
    description: Production
  - url: https://api.us.elevenlabs.io
    description: Production US
  - url: https://api.eu.residency.elevenlabs.io
    description: Production EU
  - url: https://api.in.residency.elevenlabs.io
    description: Production India
  - url: https://api.sg.residency.elevenlabs.io
    description: Production Singapore
components:
  schemas:
    CrawlType:
      type: string
      enum:
        - discovery
        - sitemap
      default: discovery
      title: CrawlType
    CrawlStatus:
      type: string
      enum:
        - queued
        - processing
        - succeeded
        - failed
        - skipped
        - cancelled
      default: queued
      title: CrawlStatus
    GetCrawlJobResponseModel:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/CrawlType'
          default: discovery
        seed_url:
          type: string
        pattern:
          type:
            - string
            - 'null'
        max_depth:
          type: integer
        max_pages:
          type: integer
        status:
          $ref: '#/components/schemas/CrawlStatus'
          default: queued
        pages_identified:
          type: integer
          default: 0
        pages_scraped:
          type: integer
          default: 0
        pages_skipped:
          type: integer
          default: 0
        pages_failed:
          type: integer
          default: 0
        root_folder_id:
          type: string
        updated_at:
          type: integer
        id:
          type: string
        created_at:
          type: integer
      required:
        - seed_url
        - max_depth
        - max_pages
        - root_folder_id
        - updated_at
        - id
        - created_at
      title: GetCrawlJobResponseModel
    ValidationErrorLocItems:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItems
    ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/ValidationErrorLocItems'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
      title: HTTPValidationError

```

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
