---
title: "Update Chapter"
source: https://elevenlabs.io/docs/api-reference/studio/update-chapter.md
path: docs/api-reference/studio/update-chapter
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update Chapter

POST https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters/{chapter_id}
Content-Type: application/json

Updates a chapter.

Reference: https://elevenlabs.io/docs/api-reference/studio/update-chapter

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/studio/projects/{project_id}/chapters/{chapter_id}:
    post:
      operationId: update
      summary: Update Chapter
      description: Updates a chapter.
      tags:
        - subpackage_studio/projects/chapters
      parameters:
        - name: project_id
          in: path
          description: >-
            The ID of the project to be used. You can use the [List
            projects](/docs/api-reference/studio/get-projects) endpoint to list
            all the available projects.
          required: true
          schema:
            type: string
        - name: chapter_id
          in: path
          description: >-
            The ID of the chapter to be used. You can use the [List project
            chapters](/docs/api-reference/studio/get-chapters) endpoint to list
            all the available chapters.
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
                $ref: '#/components/schemas/EditChapterResponseModel'
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
                #/components/schemas/Body_Update_chapter_v1_studio_projects__project_id__chapters__chapter_id__post
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
    ChapterContentBlockInputModelSubType:
      type: string
      enum:
        - p
        - h1
        - h2
        - h3
      title: ChapterContentBlockInputModelSubType
    ChapterContentParagraphTtsNodeInputModel:
      type: object
      properties:
        type:
          type: string
          enum:
            - tts_node
        text:
          type: string
        voice_id:
          type: string
      required:
        - type
        - text
        - voice_id
      title: ChapterContentParagraphTtsNodeInputModel
    ChapterContentBlockInputModel:
      type: object
      properties:
        sub_type:
          oneOf:
            - $ref: '#/components/schemas/ChapterContentBlockInputModelSubType'
            - type: 'null'
        nodes:
          type: array
          items:
            $ref: '#/components/schemas/ChapterContentParagraphTtsNodeInputModel'
        block_id:
          type:
            - string
            - 'null'
      required:
        - nodes
      title: ChapterContentBlockInputModel
    ChapterContentInputModel:
      type: object
      properties:
        blocks:
          type: array
          items:
            $ref: '#/components/schemas/ChapterContentBlockInputModel'
      required:
        - blocks
      title: ChapterContentInputModel
    Body_Update_chapter_v1_studio_projects__project_id__chapters__chapter_id__post:
      type: object
      properties:
        name:
          type:
            - string
            - 'null'
          description: The name of the chapter, used for identification only.
        content:
          oneOf:
            - $ref: '#/components/schemas/ChapterContentInputModel'
            - type: 'null'
          description: The chapter content to use.
      title: >-
        Body_Update_chapter_v1_studio_projects__project_id__chapters__chapter_id__post
    ChapterWithContentResponseModelState:
      type: string
      enum:
        - default
        - converting
      description: The state of the chapter.
      title: ChapterWithContentResponseModelState
    VoiceStatisticsResponseModel:
      type: object
      properties:
        project_voice_ref_id:
          type: string
          description: The project voice reference ID.
        characters_unconverted:
          type: integer
          description: The number of unconverted characters for this voice.
        characters_converted:
          type: integer
          description: The number of converted characters for this voice.
        credits_needed_to_convert:
          type:
            - integer
            - 'null'
          description: >-
            The number of credits needed to convert the remaining audio for this
            voice.
        voice_id:
          type: string
          description: The voice ID.
      required:
        - project_voice_ref_id
        - characters_unconverted
        - characters_converted
        - voice_id
      title: VoiceStatisticsResponseModel
    ChapterStatisticsResponseModel:
      type: object
      properties:
        characters_unconverted:
          type: integer
          description: The number of unconverted characters.
        characters_converted:
          type: integer
          description: The number of converted characters.
        paragraphs_converted:
          type: integer
          description: The number of converted paragraphs.
        paragraphs_unconverted:
          type: integer
          description: The number of unconverted paragraphs.
        credits_needed_to_convert:
          type:
            - integer
            - 'null'
          description: The number of credits needed to convert the remaining paragraphs.
        voice_statistics:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/VoiceStatisticsResponseModel'
          description: Per-voice breakdown of character counts.
      required:
        - characters_unconverted
        - characters_converted
        - paragraphs_converted
        - paragraphs_unconverted
      title: ChapterStatisticsResponseModel
    ChapterContentBlockTtsNodeResponseModel:
      type: object
      properties:
        type:
          type: string
          enum:
            - tts_node
        project_voice_ref_id:
          type: string
        text:
          type: string
        voice_id:
          type: string
      required:
        - type
        - project_voice_ref_id
        - text
        - voice_id
      title: ChapterContentBlockTtsNodeResponseModel
    ChapterContentBlockExtendableNodeResponseModel:
      type: object
      properties:
        type:
          type: string
          enum:
            - _other
      required:
        - type
      description: Not used. Make sure you anticipate new types in the future.
      title: ChapterContentBlockExtendableNodeResponseModel
    ChapterContentBlockResponseModelNodesItems:
      oneOf:
        - $ref: '#/components/schemas/ChapterContentBlockTtsNodeResponseModel'
        - $ref: '#/components/schemas/ChapterContentBlockExtendableNodeResponseModel'
      title: ChapterContentBlockResponseModelNodesItems
    ChapterContentBlockResponseModel:
      type: object
      properties:
        block_id:
          type: string
        nodes:
          type: array
          items:
            $ref: '#/components/schemas/ChapterContentBlockResponseModelNodesItems'
      required:
        - block_id
        - nodes
      title: ChapterContentBlockResponseModel
    ChapterContentResponseModel:
      type: object
      properties:
        blocks:
          type: array
          items:
            $ref: '#/components/schemas/ChapterContentBlockResponseModel'
      required:
        - blocks
      title: ChapterContentResponseModel
    ChapterWithContentResponseModel:
      type: object
      properties:
        chapter_id:
          type: string
          description: The ID of the chapter.
        name:
          type: string
          description: The name of the chapter.
        last_conversion_date_unix:
          type:
            - integer
            - 'null'
          description: The last conversion date of the chapter.
        conversion_progress:
          type:
            - number
            - 'null'
          format: double
          description: The conversion progress of the chapter.
        can_be_downloaded:
          type: boolean
          description: Whether the chapter can be downloaded.
        state:
          $ref: '#/components/schemas/ChapterWithContentResponseModelState'
          description: The state of the chapter.
        has_video:
          type:
            - boolean
            - 'null'
          description: Whether the chapter has a video.
        has_visual_content:
          type:
            - boolean
            - 'null'
          description: >-
            Whether the chapter has any visual content (video, image, or text
            clips).
        voice_ids:
          type:
            - array
            - 'null'
          items:
            type: string
          description: List of voice ids used by the chapter
        statistics:
          oneOf:
            - $ref: '#/components/schemas/ChapterStatisticsResponseModel'
            - type: 'null'
          description: The statistics of the chapter.
        last_conversion_error:
          type:
            - string
            - 'null'
          description: The last conversion error of the chapter.
        content:
          $ref: '#/components/schemas/ChapterContentResponseModel'
      required:
        - chapter_id
        - name
        - can_be_downloaded
        - state
        - content
      title: ChapterWithContentResponseModel
    EditChapterResponseModel:
      type: object
      properties:
        chapter:
          $ref: '#/components/schemas/ChapterWithContentResponseModel'
      required:
        - chapter
      title: EditChapterResponseModel
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
{}
```

**Response**

```json
{
  "chapter": {
    "chapter_id": "aw1NgEzBg83R7vgmiJt6",
    "name": "Chapter 1",
    "can_be_downloaded": true,
    "state": "default",
    "content": {
      "blocks": []
    },
    "last_conversion_date_unix": 1714204800,
    "conversion_progress": 0.5,
    "statistics": {
      "characters_unconverted": 100,
      "characters_converted": 200,
      "paragraphs_converted": 5,
      "paragraphs_unconverted": 3
    }
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.chapters.update("chapter_id", "project_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.chapters.update(
    chapter_id="chapter_id",
    project_id="project_id",
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id"

	payload := strings.NewReader("{}")

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id")! as URL,
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
