---
title: "List Studio Projects"
source: https://elevenlabs.io/docs/api-reference/studio/get-projects.md
path: docs/api-reference/studio/get-projects
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List Studio Projects

GET https://api.elevenlabs.io/v1/studio/projects

Returns a list of your Studio projects with metadata.

Reference: https://elevenlabs.io/docs/api-reference/studio/get-projects

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Response

### 200

Successful Response

- `projects` (list of object, required) — A list of projects with their metadata.
  - `project_id` (string, required) — The ID of the project.
  - `name` (string, required) — The name of the project.
  - `create_date_unix` (integer, required) — The creation date of the project.
  - `created_by_user_id` (string, required, nullable) — The user ID who created the project.
  - `default_title_voice_ref_id` (string, required) — The default title project voice reference ID.
  - `default_paragraph_voice_ref_id` (string, required) — The default paragraph project voice reference ID.
  - `default_model_id` (string, required) — The default model ID.
  - `can_be_downloaded` (boolean, required) — Whether the project can be downloaded.
  - `volume_normalization` (boolean, required) — Whether the project uses volume normalization.
  - `state` (enum, required) — The state of the project.
    - Allowed values: `creating`, `default`, `converting`, `in_queue`
  - `access_level` (enum, required) — The access level of the project.
    - Allowed values: `admin`, `editor`, `commenter`, `viewer`
  - `quality_check_on` (boolean, required, deprecated) — Whether quality check is enabled for this project.
  - `quality_check_on_when_bulk_convert` (boolean, required, deprecated) — Whether quality check is enabled on the project when bulk converting.
  - `default_title_voice_id` (string, required, deprecated) — The default title voice ID.
  - `default_paragraph_voice_id` (string, required, deprecated) — The default paragraph voice ID.
  - `last_conversion_date_unix` (integer, optional, nullable) — The last conversion date of the project.
  - `title` (string, optional, nullable) — The title of the project.
  - `author` (string, optional, nullable) — The author of the project.
  - `description` (string, optional, nullable) — The description of the project.
  - `genres` (list of string, optional, nullable) — List of genres of the project.
  - `cover_image_url` (string, optional, nullable) — The cover image URL of the project.
  - `target_audience` (enum, optional, nullable) — The target audience of the project.
    - Allowed values: `children`, `young adult`, `adult`, `all ages`
  - `language` (string, optional, nullable) — Two-letter language code (ISO 639-1) of the language of the project.
  - `content_type` (string, optional, nullable) — The content type of the project, e.g. 'Novel' or 'Short Story'
  - `original_publication_date` (string, optional, nullable) — The original publication date of the project.
  - `mature_content` (boolean, optional, nullable) — Whether the project contains mature content.
  - `isbn_number` (string, optional, nullable) — The ISBN number of the project.
  - `fiction` (enum, optional, nullable) — Whether the project is fiction.
    - Allowed values: `fiction`, `non-fiction`
  - `creation_meta` (object, optional, nullable) — The creation meta of the project.
    - `creation_progress` (double, required) — The progress of the project creation.
    - `status` (enum, required) — The status of the project creation action.
      - Allowed values: `draft`, `pending`, `creating`, `finished`, `failed`
    - `type` (enum, required) — The type of the project creation action.
      - Allowed values: `blank`, `generate_podcast`, `auto_assign_voices`, `dub_video`, `import_speech`
  - `source_type` (enum, optional, nullable) — The source type of the project.
    - Allowed values: `blank`, `book`, `article`, `genfm`, `video`, `screenplay`
  - `chapters_enabled` (boolean, optional, nullable, default: true) — Whether chapters are enabled for the project.
  - `captions_enabled` (boolean, optional, nullable, default: true) — Whether captions are enabled for the project.
  - `caption_style` (object, optional, nullable) — Global styling to be applied to all captions
    - `template` (object, optional, nullable)
      - `key` (string, required)
      - `label` (string, required)
      - `requires_high_fps` (boolean, optional, default: false)
    - `text_font` (string, optional, nullable)
    - `text_scale` (double, optional, nullable)
    - `text_color` (string, optional, nullable)
    - `text_align` (enum, optional, nullable)
      - Allowed values: `start`, `center`, `end`
    - `text_style` (enum, optional, nullable)
      - Allowed values: `normal`, `italic`
    - `text_weight` (enum, optional, nullable)
      - Allowed values: `normal`, `bold`, `900`
    - `text_transform` (enum, optional, nullable)
      - Allowed values: `none`, `uppercase`
    - `text_blend_mode` (enum, optional, nullable)
      - Allowed values: `normal`, `difference`, `multiply`
    - `text_shadow` (object, optional, nullable)
      - `enabled` (boolean, required)
      - `color` (string, required)
      - `opacity` (double, required)
      - `blur` (double, required)
      - `offset_x` (double, required)
      - `offset_y` (double, required)
    - `text_outline` (object, optional, nullable)
      - `enabled` (boolean, required)
      - `color` (string, required)
      - `opacity` (double, required)
      - `width` (double, required)
    - `background_enabled` (boolean, optional, nullable)
    - `background_color` (string, optional, nullable)
    - `background_opacity` (double, optional, nullable)
    - `background_blur` (double, optional, nullable)
    - `background_border_radius` (double, optional, nullable)
    - `word_highlights_enabled` (boolean, optional, nullable)
    - `word_highlights_color` (string, optional, nullable)
    - `word_highlights_background_color` (string, optional, nullable)
    - `word_highlights_opacity` (double, optional, nullable)
    - `word_highlights_border_radius` (double, optional, nullable)
    - `word_highlights_blur` (double, optional, nullable)
    - `section_animation` (object, optional, nullable)
      - `enter_type` (enum, required)
        - Allowed values: `none`, `fade`, `scale`, `pop`, `slide_up`, `slide_down`, `slam`, `scale_down`, `slide_in`
      - `exit_type` (enum, required)
        - Allowed values: `none`, `fade`, `scale`, `pop`, `slide_up`, `slide_down`, `slam`, `scale_down`, `slide_in`
    - `word_animation` (object, optional, nullable)
      - `enter_type` (enum, required)
        - Allowed values: `none`, `fade`, `scale`, `pop`, `slide_up`, `slide_down`, `slam`, `scale_down`, `slide_in`
      - `exit_type` (enum, required)
        - Allowed values: `none`, `fade`, `scale`, `pop`, `slide_up`, `slide_down`, `slam`, `scale_down`, `slide_in`
    - `character_animation` (object, optional, nullable)
      - `enter_type` (enum, required)
        - Allowed values: `none`, `fade`, `typewriter`
      - `exit_type` (enum, required)
        - Allowed values: `none`, `fade`
    - `cursor_enabled` (boolean, optional, nullable)
    - `width_pct` (double, optional, nullable)
    - `horizontal_placement` (object, optional, nullable)
      - `align` (enum, required)
        - Allowed values: `left`, `center`, `right`
      - `translate_pct` (double, required)
    - `vertical_placement` (object, optional, nullable)
      - `align` (enum, required)
        - Allowed values: `top`, `center`, `bottom`
      - `translate_pct` (double, required)
    - `auto_break_enabled` (boolean, optional, nullable)
    - `max_lines_per_section` (integer, optional, nullable)
    - `max_words_per_line` (integer, optional, nullable)
  - `caption_style_template_overrides` (map from string to object, optional, nullable) — Styling changes that have been made to the provided templates
    - `template` (object, optional, nullable)
      - `key` (string, required)
      - `label` (string, required)
      - `requires_high_fps` (boolean, optional, default: false)
    - `text_font` (string, optional, nullable)
    - `text_scale` (double, optional, nullable)
    - `text_color` (string, optional, nullable)
    - `text_align` (enum, optional, nullable)
      - Allowed values: `start`, `center`, `end`
    - `text_style` (enum, optional, nullable)
      - Allowed values: `normal`, `italic`
    - `text_weight` (enum, optional, nullable)
      - Allowed values: `normal`, `bold`, `900`
    - `text_transform` (enum, optional, nullable)
      - Allowed values: `none`, `uppercase`
    - `text_blend_mode` (enum, optional, nullable)
      - Allowed values: `normal`, `difference`, `multiply`
    - `text_shadow` (object, optional, nullable)
      - `enabled` (boolean, required)
      - `color` (string, required)
      - `opacity` (double, required)
      - `blur` (double, required)
      - `offset_x` (double, required)
      - `offset_y` (double, required)
    - `text_outline` (object, optional, nullable)
      - `enabled` (boolean, required)
      - `color` (string, required)
      - `opacity` (double, required)
      - `width` (double, required)
    - `background_enabled` (boolean, optional, nullable)
    - `background_color` (string, optional, nullable)
    - `background_opacity` (double, optional, nullable)
    - `background_blur` (double, optional, nullable)
    - `background_border_radius` (double, optional, nullable)
    - `word_highlights_enabled` (boolean, optional, nullable)
    - `word_highlights_color` (string, optional, nullable)
    - `word_highlights_background_color` (string, optional, nullable)
    - `word_highlights_opacity` (double, optional, nullable)
    - `word_highlights_border_radius` (double, optional, nullable)
    - `word_highlights_blur` (double, optional, nullable)
    - `section_animation` (object, optional, nullable)
      - `enter_type` (enum, required)
        - Allowed values: `none`, `fade`, `scale`, `pop`, `slide_up`, `slide_down`, `slam`, `scale_down`, `slide_in`
      - `exit_type` (enum, required)
        - Allowed values: `none`, `fade`, `scale`, `pop`, `slide_up`, `slide_down`, `slam`, `scale_down`, `slide_in`
    - `word_animation` (object, optional, nullable)
      - `enter_type` (enum, required)
        - Allowed values: `none`, `fade`, `scale`, `pop`, `slide_up`, `slide_down`, `slam`, `scale_down`, `slide_in`
      - `exit_type` (enum, required)
        - Allowed values: `none`, `fade`, `scale`, `pop`, `slide_up`, `slide_down`, `slam`, `scale_down`, `slide_in`
    - `character_animation` (object, optional, nullable)
      - `enter_type` (enum, required)
        - Allowed values: `none`, `fade`, `typewriter`
      - `exit_type` (enum, required)
        - Allowed values: `none`, `fade`
    - `cursor_enabled` (boolean, optional, nullable)
    - `width_pct` (double, optional, nullable)
    - `horizontal_placement` (object, optional, nullable)
      - `align` (enum, required)
        - Allowed values: `left`, `center`, `right`
      - `translate_pct` (double, required)
    - `vertical_placement` (object, optional, nullable)
      - `align` (enum, required)
        - Allowed values: `top`, `center`, `bottom`
      - `translate_pct` (double, required)
    - `auto_break_enabled` (boolean, optional, nullable)
    - `max_lines_per_section` (integer, optional, nullable)
    - `max_words_per_line` (integer, optional, nullable)
  - `public_share_id` (string, optional, nullable) — The public share ID of the project.
  - `aspect_ratio` (enum, optional, nullable) — The aspect ratio of the project.
    - Allowed values: `16:9`, `9:16`, `4:5`, `1:1`
  - `agent_settings` (object, optional, nullable) — Agent-related settings for the project
    - `tool_settings` (map from string to object, optional)
      - `skip_confirmation` (boolean, optional, default: false)

## Examples

**Response**

```json
{
  "projects": [
    {
      "project_id": "aw1NgEzBg83R7vgmiJt6",
      "name": "My Project",
      "create_date_unix": 1714204800,
      "created_by_user_id": "Vbtgl3bRdj6lk79rYAgx",
      "default_title_voice_ref_id": "JBFqnCBsd6RMkjVDRZzb",
      "default_paragraph_voice_ref_id": "JBFqnCBsd6RMkjVDRZzb",
      "default_model_id": "eleven_multilingual_v2",
      "can_be_downloaded": true,
      "volume_normalization": true,
      "state": "default",
      "access_level": "viewer",
      "quality_check_on": false,
      "quality_check_on_when_bulk_convert": false,
      "default_title_voice_id": "JBFqnCBsd6RMkjVDRZzb",
      "default_paragraph_voice_id": "JBFqnCBsd6RMkjVDRZzb",
      "last_conversion_date_unix": 1714204800,
      "title": "My Project",
      "author": "John Doe",
      "description": "This is a description of my project.",
      "genres": [
        "Novel",
        "Short Story"
      ],
      "cover_image_url": "https://example.com/cover.jpg",
      "target_audience": "young adult",
      "language": "en",
      "content_type": "Novel",
      "original_publication_date": "2025-01-01",
      "mature_content": false,
      "isbn_number": "978-90-274-3964-2",
      "fiction": "fiction",
      "creation_meta": {
        "creation_progress": 0.5,
        "status": "pending",
        "type": "blank"
      },
      "public_share_id": "abc123def456789"
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.list();
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.list()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects"

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

url = URI("https://api.elevenlabs.io/v1/studio/projects")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects")! as URL,
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
