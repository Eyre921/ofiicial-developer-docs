---
title: "List crawl jobs"
source: https://elevenlabs.io/docs/api-reference/knowledge-base/list-crawl-jobs.md
path: docs/api-reference/knowledge-base/list-crawl-jobs
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List crawl jobs

GET https://api.elevenlabs.io/v1/convai/knowledge-base/crawl

Get a list of ongoing and recent crawl jobs for the user.

Reference: https://elevenlabs.io/docs/api-reference/knowledge-base/list-crawl-jobs

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/knowledge-base/crawl:
    get:
      operationId: list
      summary: List Ongoing And Recent Crawl Jobs Created By A User
      description: Get a list of ongoing and recent crawl jobs for the user.
      tags:
        - crawlJobs
      parameters:
        - name: include_job_ids
          in: query
          description: Ids of additional crawl jobs to retrieve
          required: false
          schema:
            type:
              - array
              - 'null'
            items:
              type: string
        - name: page_size
          in: query
          description: >-
            How many documents to return at maximum. Can not exceed 100,
            defaults to 30.
          required: false
          schema:
            type: integer
            default: 30
        - name: cursor
          in: query
          description: Used for fetching next page. Cursor is returned in the response.
          required: false
          schema:
            type:
              - string
              - 'null'
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
                $ref: '#/components/schemas/ListCrawlJobsResponseModel'
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
    ListCrawlJobsResponseModel:
      type: object
      properties:
        crawl_jobs:
          type: array
          items:
            $ref: '#/components/schemas/GetCrawlJobResponseModel'
        next_cursor:
          type:
            - string
            - 'null'
      required:
        - crawl_jobs
      title: ListCrawlJobsResponseModel
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
  "crawl_jobs": [
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
  ],
  "next_cursor": "string"
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.crawlJobs.list({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.crawl_jobs.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/crawl"

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/crawl")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/crawl")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/crawl');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/crawl");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/crawl")! as URL,
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
