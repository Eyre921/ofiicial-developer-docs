---
title: "Update Studio Project Content"
source: https://elevenlabs.io/docs/api-reference/studio/update-content.md
path: docs/api-reference/studio/update-content
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Update Studio Project Content

POST https://api.elevenlabs.io/v1/studio/projects/{project_id}/content
Content-Type: multipart/form-data

Updates Studio project content.

Reference: https://elevenlabs.io/docs/api-reference/studio/update-content

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/studio/projects/{project_id}/content:
    post:
      operationId: update
      summary: Update Studio Project Content
      description: Updates Studio project content.
      tags:
        - content
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
                $ref: '#/components/schemas/EditProjectResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                from_url:
                  type:
                    - string
                    - 'null'
                  description: >-
                    An optional URL from which we will extract content to
                    initialize the Studio project. If this is set, 'from_url'
                    and 'from_content' must be null. If neither 'from_url',
                    'from_document', 'from_content' are provided we will
                    initialize the Studio project as blank.
                from_document:
                  type: string
                  format: binary
                  description: >-
                    An optional .epub, .pdf, .txt or similar file can be
                    provided. If provided, we will initialize the Studio project
                    with its content. If this is set, 'from_url' and
                    'from_content' must be null. If neither 'from_url',
                    'from_document', 'from_content' are provided we will
                    initialize the Studio project as blank.
                from_content_json:
                  type: string
                  description: |2-

                        An optional content to initialize the Studio project with. If this is set, 'from_url' and 'from_document' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.

                        Example:
                        [{"name": "Chapter A", "blocks": [{"sub_type": "p", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "A", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "B", "type": "tts_node"}]}, {"sub_type": "h1", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "C", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "D", "type": "tts_node"}]}]}, {"name": "Chapter B", "blocks": [{"sub_type": "p", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "E", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "F", "type": "tts_node"}]}, {"sub_type": "h2", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "G", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "H", "type": "tts_node"}]}]}]
                        
                auto_convert:
                  type: boolean
                  default: false
                  description: Whether to auto convert the Studio project to audio or not.
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
    ProjectResponseModelTargetAudience:
      type: string
      enum:
        - children
        - young adult
        - adult
        - all ages
      description: The target audience of the project.
      title: ProjectResponseModelTargetAudience
    ProjectState:
      type: string
      enum:
        - creating
        - default
        - converting
        - in_queue
      description: The state of the project.
      title: ProjectState
    ProjectResponseModelAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: The access level of the project.
      title: ProjectResponseModelAccessLevel
    ProjectResponseModelFiction:
      type: string
      enum:
        - fiction
        - non-fiction
      description: Whether the project is fiction.
      title: ProjectResponseModelFiction
    ProjectCreationMetaResponseModelStatus:
      type: string
      enum:
        - draft
        - pending
        - creating
        - finished
        - failed
      description: The status of the project creation action.
      title: ProjectCreationMetaResponseModelStatus
    ProjectCreationMetaType:
      type: string
      enum:
        - blank
        - generate_podcast
        - auto_assign_voices
        - dub_video
        - import_speech
      title: ProjectCreationMetaType
    ProjectCreationMetaResponseModel:
      type: object
      properties:
        creation_progress:
          type: number
          format: double
          description: The progress of the project creation.
        status:
          $ref: '#/components/schemas/ProjectCreationMetaResponseModelStatus'
          description: The status of the project creation action.
        type:
          $ref: '#/components/schemas/ProjectCreationMetaType'
          description: The type of the project creation action.
      required:
        - creation_progress
        - status
        - type
      title: ProjectCreationMetaResponseModel
    ProjectResponseModelSourceType:
      type: string
      enum:
        - blank
        - book
        - article
        - genfm
        - video
        - screenplay
      description: The source type of the project.
      title: ProjectResponseModelSourceType
    CaptionStyleTemplateModel:
      type: object
      properties:
        key:
          type: string
        label:
          type: string
        requires_high_fps:
          type: boolean
          default: false
      required:
        - key
        - label
      title: CaptionStyleTemplateModel
    CaptionStyleModelTextAlign:
      type: string
      enum:
        - start
        - center
        - end
      title: CaptionStyleModelTextAlign
    CaptionStyleModelTextStyle:
      type: string
      enum:
        - normal
        - italic
      title: CaptionStyleModelTextStyle
    CaptionStyleModelTextWeight:
      type: string
      enum:
        - normal
        - bold
        - '900'
      title: CaptionStyleModelTextWeight
    CaptionStyleModelTextTransform:
      type: string
      enum:
        - none
        - uppercase
      title: CaptionStyleModelTextTransform
    CaptionStyleModelTextBlendMode:
      type: string
      enum:
        - normal
        - difference
        - multiply
      title: CaptionStyleModelTextBlendMode
    StudioTextStyleShadowModel:
      type: object
      properties:
        enabled:
          type: boolean
        color:
          type: string
        opacity:
          type: number
          format: double
        blur:
          type: number
          format: double
        offset_x:
          type: number
          format: double
        offset_y:
          type: number
          format: double
      required:
        - enabled
        - color
        - opacity
        - blur
        - offset_x
        - offset_y
      title: StudioTextStyleShadowModel
    StudioTextStyleOutlineModel:
      type: object
      properties:
        enabled:
          type: boolean
        color:
          type: string
        opacity:
          type: number
          format: double
        width:
          type: number
          format: double
      required:
        - enabled
        - color
        - opacity
        - width
      title: StudioTextStyleOutlineModel
    CaptionStyleSectionAnimationModelEnterType:
      type: string
      enum:
        - none
        - fade
        - scale
        - pop
        - slide_up
        - slide_down
        - slam
        - scale_down
        - slide_in
      title: CaptionStyleSectionAnimationModelEnterType
    CaptionStyleSectionAnimationModelExitType:
      type: string
      enum:
        - none
        - fade
        - scale
        - pop
        - slide_up
        - slide_down
        - slam
        - scale_down
        - slide_in
      title: CaptionStyleSectionAnimationModelExitType
    CaptionStyleSectionAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleSectionAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleSectionAnimationModelExitType'
      required:
        - enter_type
        - exit_type
      title: CaptionStyleSectionAnimationModel
    CaptionStyleWordAnimationModelEnterType:
      type: string
      enum:
        - none
        - fade
        - scale
        - pop
        - slide_up
        - slide_down
        - slam
        - scale_down
        - slide_in
      title: CaptionStyleWordAnimationModelEnterType
    CaptionStyleWordAnimationModelExitType:
      type: string
      enum:
        - none
        - fade
        - scale
        - pop
        - slide_up
        - slide_down
        - slam
        - scale_down
        - slide_in
      title: CaptionStyleWordAnimationModelExitType
    CaptionStyleWordAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleWordAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleWordAnimationModelExitType'
      required:
        - enter_type
        - exit_type
      title: CaptionStyleWordAnimationModel
    CaptionStyleCharacterAnimationModelEnterType:
      type: string
      enum:
        - none
        - fade
        - typewriter
      title: CaptionStyleCharacterAnimationModelEnterType
    CaptionStyleCharacterAnimationModelExitType:
      type: string
      enum:
        - none
        - fade
      title: CaptionStyleCharacterAnimationModelExitType
    CaptionStyleCharacterAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleCharacterAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleCharacterAnimationModelExitType'
      required:
        - enter_type
        - exit_type
      title: CaptionStyleCharacterAnimationModel
    CaptionStyleHorizontalPlacementModelAlign:
      type: string
      enum:
        - left
        - center
        - right
      title: CaptionStyleHorizontalPlacementModelAlign
    CaptionStyleHorizontalPlacementModel:
      type: object
      properties:
        align:
          $ref: '#/components/schemas/CaptionStyleHorizontalPlacementModelAlign'
        translate_pct:
          type: number
          format: double
      required:
        - align
        - translate_pct
      title: CaptionStyleHorizontalPlacementModel
    CaptionStyleVerticalPlacementModelAlign:
      type: string
      enum:
        - top
        - center
        - bottom
      title: CaptionStyleVerticalPlacementModelAlign
    CaptionStyleVerticalPlacementModel:
      type: object
      properties:
        align:
          $ref: '#/components/schemas/CaptionStyleVerticalPlacementModelAlign'
        translate_pct:
          type: number
          format: double
      required:
        - align
        - translate_pct
      title: CaptionStyleVerticalPlacementModel
    CaptionStyleModel:
      type: object
      properties:
        template:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleTemplateModel'
            - type: 'null'
        text_font:
          type:
            - string
            - 'null'
        text_scale:
          type:
            - number
            - 'null'
          format: double
        text_color:
          type:
            - string
            - 'null'
        text_align:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextAlign'
            - type: 'null'
        text_style:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextStyle'
            - type: 'null'
        text_weight:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextWeight'
            - type: 'null'
        text_transform:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextTransform'
            - type: 'null'
        text_blend_mode:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextBlendMode'
            - type: 'null'
        text_shadow:
          oneOf:
            - $ref: '#/components/schemas/StudioTextStyleShadowModel'
            - type: 'null'
        text_outline:
          oneOf:
            - $ref: '#/components/schemas/StudioTextStyleOutlineModel'
            - type: 'null'
        background_enabled:
          type:
            - boolean
            - 'null'
        background_color:
          type:
            - string
            - 'null'
        background_opacity:
          type:
            - number
            - 'null'
          format: double
        background_blur:
          type:
            - number
            - 'null'
          format: double
        background_border_radius:
          type:
            - number
            - 'null'
          format: double
        word_highlights_enabled:
          type:
            - boolean
            - 'null'
        word_highlights_color:
          type:
            - string
            - 'null'
        word_highlights_background_color:
          type:
            - string
            - 'null'
        word_highlights_opacity:
          type:
            - number
            - 'null'
          format: double
        word_highlights_border_radius:
          type:
            - number
            - 'null'
          format: double
        word_highlights_blur:
          type:
            - number
            - 'null'
          format: double
        section_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleSectionAnimationModel'
            - type: 'null'
        word_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleWordAnimationModel'
            - type: 'null'
        character_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleCharacterAnimationModel'
            - type: 'null'
        cursor_enabled:
          type:
            - boolean
            - 'null'
        width_pct:
          type:
            - number
            - 'null'
          format: double
        horizontal_placement:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleHorizontalPlacementModel'
            - type: 'null'
        vertical_placement:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleVerticalPlacementModel'
            - type: 'null'
        auto_break_enabled:
          type:
            - boolean
            - 'null'
        max_lines_per_section:
          type:
            - integer
            - 'null'
        max_words_per_line:
          type:
            - integer
            - 'null'
      title: CaptionStyleModel
    ProjectResponseModelAspectRatio:
      type: string
      enum:
        - '16:9'
        - '9:16'
        - '4:5'
        - '1:1'
      description: The aspect ratio of the project.
      title: ProjectResponseModelAspectRatio
    StudioAgentToolSettingsModel:
      type: object
      properties:
        skip_confirmation:
          type: boolean
          default: false
      title: StudioAgentToolSettingsModel
    StudioAgentSettingsModel:
      type: object
      properties:
        tool_settings:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/StudioAgentToolSettingsModel'
      title: StudioAgentSettingsModel
    ProjectResponseModel:
      type: object
      properties:
        project_id:
          type: string
          description: The ID of the project.
        name:
          type: string
          description: The name of the project.
        create_date_unix:
          type: integer
          description: The creation date of the project.
        created_by_user_id:
          type:
            - string
            - 'null'
          description: The user ID who created the project.
        default_title_voice_ref_id:
          type: string
          description: The default title project voice reference ID.
        default_paragraph_voice_ref_id:
          type: string
          description: The default paragraph project voice reference ID.
        default_model_id:
          type: string
          description: The default model ID.
        last_conversion_date_unix:
          type:
            - integer
            - 'null'
          description: The last conversion date of the project.
        can_be_downloaded:
          type: boolean
          description: Whether the project can be downloaded.
        title:
          type:
            - string
            - 'null'
          description: The title of the project.
        author:
          type:
            - string
            - 'null'
          description: The author of the project.
        description:
          type:
            - string
            - 'null'
          description: The description of the project.
        genres:
          type:
            - array
            - 'null'
          items:
            type: string
          description: List of genres of the project.
        cover_image_url:
          type:
            - string
            - 'null'
          description: The cover image URL of the project.
        target_audience:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelTargetAudience'
            - type: 'null'
          description: The target audience of the project.
        language:
          type:
            - string
            - 'null'
          description: Two-letter language code (ISO 639-1) of the language of the project.
        content_type:
          type:
            - string
            - 'null'
          description: The content type of the project, e.g. 'Novel' or 'Short Story'
        original_publication_date:
          type:
            - string
            - 'null'
          description: The original publication date of the project.
        mature_content:
          type:
            - boolean
            - 'null'
          description: Whether the project contains mature content.
        isbn_number:
          type:
            - string
            - 'null'
          description: The ISBN number of the project.
        volume_normalization:
          type: boolean
          description: Whether the project uses volume normalization.
        state:
          $ref: '#/components/schemas/ProjectState'
          description: The state of the project.
        access_level:
          $ref: '#/components/schemas/ProjectResponseModelAccessLevel'
          description: The access level of the project.
        fiction:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelFiction'
            - type: 'null'
          description: Whether the project is fiction.
        quality_check_on:
          type: boolean
          description: Whether quality check is enabled for this project.
        quality_check_on_when_bulk_convert:
          type: boolean
          description: >-
            Whether quality check is enabled on the project when bulk
            converting.
        creation_meta:
          oneOf:
            - $ref: '#/components/schemas/ProjectCreationMetaResponseModel'
            - type: 'null'
          description: The creation meta of the project.
        source_type:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelSourceType'
            - type: 'null'
          description: The source type of the project.
        chapters_enabled:
          type:
            - boolean
            - 'null'
          default: true
          description: Whether chapters are enabled for the project.
        captions_enabled:
          type:
            - boolean
            - 'null'
          default: true
          description: Whether captions are enabled for the project.
        caption_style:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModel'
            - type: 'null'
          description: Global styling to be applied to all captions
        caption_style_template_overrides:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/CaptionStyleModel'
          description: Styling changes that have been made to the provided templates
        public_share_id:
          type:
            - string
            - 'null'
          description: The public share ID of the project.
        aspect_ratio:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelAspectRatio'
            - type: 'null'
          description: The aspect ratio of the project.
        agent_settings:
          oneOf:
            - $ref: '#/components/schemas/StudioAgentSettingsModel'
            - type: 'null'
          description: Agent-related settings for the project
        default_title_voice_id:
          type: string
          description: The default title voice ID.
        default_paragraph_voice_id:
          type: string
          description: The default paragraph voice ID.
      required:
        - project_id
        - name
        - create_date_unix
        - created_by_user_id
        - default_title_voice_ref_id
        - default_paragraph_voice_ref_id
        - default_model_id
        - can_be_downloaded
        - volume_normalization
        - state
        - access_level
        - quality_check_on
        - quality_check_on_when_bulk_convert
        - default_title_voice_id
        - default_paragraph_voice_id
      title: ProjectResponseModel
    EditProjectResponseModel:
      type: object
      properties:
        project:
          $ref: '#/components/schemas/ProjectResponseModel'
      required:
        - project
      title: EditProjectResponseModel
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
  "from_document": "<file: <file1>>"
}
```

**Response**

```json
{
  "project": {
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
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.content.update("project_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.content.update(
    project_id="project_id",
    from_document="example_from_document",
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

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/content"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/content")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects/project_id/content")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects/project_id/content', [
  'multipart' => [
    [
        'name' => 'from_document',
        'filename' => '<file1>',
        'contents' => null
    ]
  ]
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/content");
var request = new RestRequest(Method.POST);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "auto_convert",
    "value": 
  ],
  [
    "name": "from_content_json",
    "value": 
  ],
  [
    "name": "from_document",
    "fileName": "<file1>"
  ],
  [
    "name": "from_url",
    "value": 
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/content")! as URL,
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
