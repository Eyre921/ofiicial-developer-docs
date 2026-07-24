---
title: "Create crawl job"
source: https://elevenlabs.io/docs/api-reference/knowledge-base/create-crawl-job.md
path: docs/api-reference/knowledge-base/create-crawl-job
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create crawl job

POST https://api.elevenlabs.io/v1/convai/knowledge-base/crawl
Content-Type: application/json

Create a crawl job to crawl the given URL with specified depth and page limits.

Reference: https://elevenlabs.io/docs/api-reference/knowledge-base/create-crawl-job

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/knowledge-base/crawl:
    post:
      operationId: create
      summary: Create Crawl Job
      description: >-
        Create a crawl job to crawl the given URL with specified depth and page
        limits.
      tags:
        - crawlJobs
      parameters:
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
                $ref: '#/components/schemas/CreateCrawlJobResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_Create_crawl_job_v1_convai_knowledge_base_crawl_post
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
    Body_Create_crawl_job_v1_convai_knowledge_base_crawl_post:
      type: object
      properties:
        url:
          type: string
          description: >-
            URL to a page of documentation that the agent will have access to in
            order to interact with users.
        max_depth:
          type: integer
          default: 3
          description: Maximum depth for crawling (1-5), defaults to 3.
        max_pages:
          type: integer
          default: 1000
          description: Maximum number of pages to crawl (1-10,000), defaults to 1000.
        pattern:
          type:
            - string
            - 'null'
          description: If set, only URLs that match this pattern are included.
        sitemap_urls:
          type:
            - array
            - 'null'
          items:
            type: string
          description: >-
            List of URLs to crawl from sitemap (optional, overrides automatic
            URL discovery).
        parent_folder_id:
          type:
            - string
            - 'null'
          description: >-
            If set, the created document or folder will be placed inside the
            given folder.
        enable_auto_sync:
          type: boolean
          default: false
          description: Whether to enable auto-sync for this URL document.
        auto_remove:
          type: boolean
          default: false
          description: >-
            Whether to automatically remove the document if the URL becomes
            unavailable. Only applicable when auto-sync is enabled.
      required:
        - url
      title: Body_Create_crawl_job_v1_convai_knowledge_base_crawl_post
    CrawlType:
      type: string
      enum:
        - discovery
        - sitemap
      default: discovery
      title: CrawlType
    KnowledgeBaseFolderPathSegmentSummaryResponseModel:
      type: object
      properties:
        id:
          type: string
      required:
        - id
      title: KnowledgeBaseFolderPathSegmentSummaryResponseModel
    CreateCrawlJobResponseModel:
      type: object
      properties:
        id:
          type: string
        type:
          $ref: '#/components/schemas/CrawlType'
        root_folder_id:
          type: string
        status:
          type: string
        created_at:
          type: integer
        folder_path:
          type: array
          items:
            $ref: >-
              #/components/schemas/KnowledgeBaseFolderPathSegmentSummaryResponseModel
          description: >-
            The folder path segments leading to the root folder, from root to
            parent folder.
      required:
        - id
        - type
        - root_folder_id
        - status
        - created_at
      title: CreateCrawlJobResponseModel
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



**Request**

```json
{
  "url": "https://docs.elevenlabs.io/api/knowledge-base"
}
```

**Response**

```json
{
  "id": "crawljob-9f8b7a6d-1234-4e56-8abc-1234567890ab",
  "type": "discovery",
  "root_folder_id": "folder-4d3c2b1a-5678-4e90-b123-abcdef123456",
  "status": "pending",
  "created_at": 1712000000,
  "folder_path": [
    {
      "id": "folder-root-0001"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.crawlJobs.create({
        url: "https://docs.elevenlabs.io/api/knowledge-base",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.crawl_jobs.create(
    url="https://docs.elevenlabs.io/api/knowledge-base",
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

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/crawl"

	payload := strings.NewReader("{\n  \"url\": \"https://docs.elevenlabs.io/api/knowledge-base\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/crawl")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"url\": \"https://docs.elevenlabs.io/api/knowledge-base\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/knowledge-base/crawl")
  .header("Content-Type", "application/json")
  .body("{\n  \"url\": \"https://docs.elevenlabs.io/api/knowledge-base\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/knowledge-base/crawl', [
  'body' => '{
  "url": "https://docs.elevenlabs.io/api/knowledge-base"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/crawl");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"url\": \"https://docs.elevenlabs.io/api/knowledge-base\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["url": "https://docs.elevenlabs.io/api/knowledge-base"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/crawl")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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
