---
title: "Create Studio Project"
source: https://elevenlabs.io/docs/api-reference/studio/add-project.md
path: docs/api-reference/studio/add-project
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create Studio Project

POST https://api.elevenlabs.io/v1/studio/projects
Content-Type: multipart/form-data

Creates a new Studio project, it can be either initialized as blank, from a document or from a URL.

Reference: https://elevenlabs.io/docs/api-reference/studio/add-project

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Body (multipart/form-data)

- `name` (string, required) — The name of the Studio project, used for identification only.
- `default_title_voice_id` (string, optional) — The voice_id that corresponds to the default voice used for new titles.
- `default_paragraph_voice_id` (string, optional) — The voice_id that corresponds to the default voice used for new paragraphs.
- `default_model_id` (string, optional) — The ID of the model to be used for this Studio project, you can query GET /v1/models to list all available models.
- `from_url` (string, optional) — An optional URL from which we will extract content to initialize the Studio project. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.
- `from_document` (file, optional) — An optional .epub, .pdf, .txt or similar file can be provided. If provided, we will initialize the Studio project with its content. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.
- `from_content_json` (string, optional) — An optional content to initialize the Studio project with. If this is set, 'from\_url' and 'from\_document' must be null. If neither 'from\_url', 'from\_document', 'from\_content' are provided we will initialize the Studio project as blank. Example: \[\{"name": "Chapter A", "blocks": \[\{"sub\_type": "p", "nodes": \[\{"voice\_id": "6lCwbsX1yVjD49QmpkT0", "text": "A", "type": "tts\_node"}, \{"voice\_id": "6lCwbsX1yVjD49QmpkT1", "text": "B", "type": "tts\_node"}]}, \{"sub\_type": "h1", "nodes": \[\{"voice\_id": "6lCwbsX1yVjD49QmpkT0", "text": "C", "type": "tts\_node"}, \{"voice\_id": "6lCwbsX1yVjD49QmpkT1", "text": "D", "type": "tts\_node"}]}]}, \{"name": "Chapter B", "blocks": \[\{"sub\_type": "p", "nodes": \[\{"voice\_id": "6lCwbsX1yVjD49QmpkT0", "text": "E", "type": "tts\_node"}, \{"voice\_id": "6lCwbsX1yVjD49QmpkT1", "text": "F", "type": "tts\_node"}]}, \{"sub\_type": "h2", "nodes": \[\{"voice\_id": "6lCwbsX1yVjD49QmpkT0", "text": "G", "type": "tts\_node"}, \{"voice\_id": "6lCwbsX1yVjD49QmpkT1", "text": "H", "type": "tts\_node"}]}]}]
- `quality_preset` (enum, optional) — Output quality of the generated audio. Must be one of: 'standard' - standard output format, 128kbps with 44.1kHz sample rate. 'high' - high quality output format, 192kbps with 44.1kHz sample rate and major improvements on our side. 'ultra' - ultra quality output format, 192kbps with 44.1kHz sample rate and highest improvements on our side. 'ultra_lossless' - ultra quality output format, 705.6kbps with 44.1kHz sample rate and highest improvements on our side in a fully lossless format. If not provided, defaults to the highest quality preset available on your subscription tier.
- `title` (string, optional) — An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download.
- `author` (string, optional) — An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download.
- `description` (string, optional) — An optional description of the Studio project.
- `genres` (list of string, optional) — An optional list of genres associated with the Studio project.
- `target_audience` (enum, optional) — An optional target audience of the Studio project.
- `language` (string, optional) — An optional language of the Studio project. Two-letter language code (ISO 639-1).
- `content_type` (string, optional) — An optional content type of the Studio project.
- `original_publication_date` (string, optional) — An optional original publication date of the Studio project, in the format YYYY-MM-DD or YYYY.
- `mature_content` (boolean, optional) — An optional specification of whether this Studio project contains mature content.
- `isbn_number` (string, optional) — An optional ISBN number of the Studio project you want to create, this will be added as metadata to the mp3 file on Studio project or chapter download.
- `acx_volume_normalization` (boolean, optional) — [Deprecated] When the Studio project is downloaded, should the returned audio have postprocessing in order to make it compliant with audiobook normalized volume requirements
- `volume_normalization` (boolean, optional) — When the Studio project is downloaded, should the returned audio have postprocessing in order to make it compliant with audiobook normalized volume requirements
- `pronunciation_dictionary_locators` (list of string, optional) — A list of pronunciation dictionary locators (pronunciation\_dictionary\_id, version\_id) encoded as a list of JSON strings for pronunciation dictionaries to be applied to the text. A list of json encoded strings is required as adding projects may occur through formData as opposed to jsonBody. To specify multiple dictionaries use multiple --form lines in your curl, such as --form 'pronunciation\_dictionary\_locators="\{"pronunciation\_dictionary\_id":"Vmd4Zor6fplcA7WrINey","version\_id":"hRPaxjlTdR7wFMhV4w0b"}"' --form 'pronunciation\_dictionary\_locators="\{"pronunciation\_dictionary\_id":"JzWtcGQMJ6bnlWwyMo7e","version\_id":"lbmwxiLu4q6txYxgdZqn"}"'.
- `callback_url` (string, optional) — A url that will be called by our service when the Studio project is converted. Request will contain a json blob containing the status of the conversion Messages: 1. When project was converted successfully: \{ type: "project\_conversion\_status", event\_timestamp: 1234567890, data: \{ request\_id: "1234567890", project\_id: "21m00Tcm4TlvDq8ikWAM", conversion\_status: "success", project\_snapshot\_id: "22m00Tcm4TlvDq8ikMAT", error\_details: None, } } 2. When project conversion failed: \{ type: "project\_conversion\_status", event\_timestamp: 1234567890, data: \{ request\_id: "1234567890", project\_id: "21m00Tcm4TlvDq8ikWAM", conversion\_status: "error", project\_snapshot\_id: None, error\_details: "Error details if conversion failed" } } 3. When chapter was converted successfully: \{ type: "chapter\_conversion\_status", event\_timestamp: 1234567890, data: \{ request\_id: "1234567890", project\_id: "21m00Tcm4TlvDq8ikWAM", chapter\_id: "22m00Tcm4TlvDq8ikMAT", conversion\_status: "success", chapter\_snapshot\_id: "23m00Tcm4TlvDq8ikMAV", error\_details: None, } } 4. When chapter conversion failed: \{ type: "chapter\_conversion\_status", event\_timestamp: 1234567890, data: \{ request\_id: "1234567890", project\_id: "21m00Tcm4TlvDq8ikWAM", chapter\_id: "22m00Tcm4TlvDq8ikMAT", conversion\_status: "error", chapter\_snapshot\_id: None, error\_details: "Error details if conversion failed" } }
- `fiction` (enum, optional) — An optional specification of whether the content of this Studio project is fiction.
- `apply_text_normalization` (enum, optional) — This parameter controls text normalization with four modes: 'auto', 'on', 'apply_english' and 'off'. When set to 'auto', the system will automatically decide whether to apply text normalization (e.g., spelling out numbers). With 'on', text normalization will always be applied, while with 'off', it will be skipped. 'apply_english' is the same as 'on' but will assume that text is in English.
- `auto_convert` (boolean, optional) — Whether to auto convert the Studio project to audio or not.
- `auto_assign_voices` (boolean, optional) — [Alpha Feature] Whether automatically assign voices to phrases in the create Project.
- `source_type` (enum, optional) — The type of Studio project to create.
- `voice_settings` (list of string, optional) — Optional voice settings overrides for the project, encoded as a list of JSON strings. Example: \["\{"voice\_id": "21m00Tcm4TlvDq8ikWAM", "stability": 0.7, "similarity\_boost": 0.8, "style": 0.5, "speed": 1.0, "use\_speaker\_boost": true}"]
- `create_publishing_read` (boolean, optional) — If true, creates a corresponding read for direct publishing in draft state

## Response

### 200

Successful Response

- `project` (object, required)
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

**Request**

```json
{
  "from_document": "<file: <file1>>",
  "name": "Project 1"
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
    await client.studio.projects.create({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.create(
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

	url := "https://api.elevenlabs.io/v1/studio/projects"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"acx_volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_assign_voices\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"callback_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"create_publishing_read\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_paragraph_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_title_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fiction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"genres\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"isbn_number\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mature_content\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nProject 1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_publication_date\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"quality_preset\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_audience\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_settings\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

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

url = URI("https://api.elevenlabs.io/v1/studio/projects")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"acx_volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_assign_voices\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"callback_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"create_publishing_read\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_paragraph_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_title_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fiction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"genres\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"isbn_number\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mature_content\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nProject 1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_publication_date\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"quality_preset\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_audience\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_settings\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"acx_volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_assign_voices\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"callback_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"create_publishing_read\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_paragraph_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_title_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fiction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"genres\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"isbn_number\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mature_content\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nProject 1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_publication_date\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"quality_preset\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_audience\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_settings\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects', [
  'multipart' => [
    [
        'name' => 'from_document',
        'filename' => '<file1>',
        'contents' => null
    ],
    [
        'name' => 'name',
        'contents' => 'Project 1'
    ]
  ]
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects");
var request = new RestRequest(Method.POST);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"acx_volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_assign_voices\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"callback_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"create_publishing_read\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_paragraph_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_title_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fiction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"genres\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"isbn_number\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mature_content\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nProject 1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_publication_date\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"quality_preset\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_audience\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_settings\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "acx_volume_normalization",
    "value": 
  ],
  [
    "name": "apply_text_normalization",
    "value": 
  ],
  [
    "name": "author",
    "value": 
  ],
  [
    "name": "auto_assign_voices",
    "value": 
  ],
  [
    "name": "auto_convert",
    "value": 
  ],
  [
    "name": "callback_url",
    "value": 
  ],
  [
    "name": "content_type",
    "value": 
  ],
  [
    "name": "create_publishing_read",
    "value": 
  ],
  [
    "name": "default_model_id",
    "value": 
  ],
  [
    "name": "default_paragraph_voice_id",
    "value": 
  ],
  [
    "name": "default_title_voice_id",
    "value": 
  ],
  [
    "name": "description",
    "value": 
  ],
  [
    "name": "fiction",
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
  ],
  [
    "name": "genres",
    "value": 
  ],
  [
    "name": "isbn_number",
    "value": 
  ],
  [
    "name": "language",
    "value": 
  ],
  [
    "name": "mature_content",
    "value": 
  ],
  [
    "name": "name",
    "value": "Project 1"
  ],
  [
    "name": "original_publication_date",
    "value": 
  ],
  [
    "name": "pronunciation_dictionary_locators",
    "value": 
  ],
  [
    "name": "quality_preset",
    "value": 
  ],
  [
    "name": "source_type",
    "value": 
  ],
  [
    "name": "target_audience",
    "value": 
  ],
  [
    "name": "title",
    "value": 
  ],
  [
    "name": "voice_settings",
    "value": 
  ],
  [
    "name": "volume_normalization",
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects")! as URL,
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
