---
title: "Get widget"
source: https://elevenlabs.io/docs/eleven-agents/api-reference/widget/get.md
path: docs/eleven-agents/api-reference/widget/get
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get widget

GET https://api.elevenlabs.io/v1/convai/agents/{agent_id}/widget

Retrieve the widget configuration for an agent

Reference: https://elevenlabs.io/docs/eleven-agents/api-reference/widget/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/convai/agents/{agent_id}/widget:
    get:
      operationId: get
      summary: Get Agent Widget Config
      description: Retrieve the widget configuration for an agent
      tags:
        - subpackage_conversationalAi/agents/widget
      parameters:
        - name: agent_id
          in: path
          description: The id of an agent. This is returned on agent creation.
          required: true
          schema:
            type: string
        - name: conversation_signature
          in: query
          description: >-
            An expiring token that enables a websocket conversation to start.
            These can be generated for an agent using the
            /v1/convai/conversation/get_signed_url endpoint
          required: false
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
                $ref: '#/components/schemas/type_:GetAgentEmbedResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_:HTTPValidationError'
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
    type_:EmbedVariant:
      type: string
      enum:
        - tiny
        - compact
        - full
        - expandable
      default: full
      title: EmbedVariant
    type_:WidgetPlacement:
      type: string
      enum:
        - top-left
        - top
        - top-right
        - bottom-left
        - bottom
        - bottom-right
      default: bottom-right
      title: WidgetPlacement
    type_:WidgetExpandable:
      type: string
      enum:
        - never
        - mobile
        - desktop
        - always
      default: never
      title: WidgetExpandable
    type_:WidgetConfigResponseAvatar:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - orb
              description: 'Discriminator value: orb'
            color_1:
              type: string
              default: '#2792dc'
              description: The first color of the avatar
            color_2:
              type: string
              default: '#9ce6e6'
              description: The second color of the avatar
          required:
            - type
        - type: object
          properties:
            type:
              type: string
              enum:
                - url
              description: 'Discriminator value: url'
            custom_url:
              type: string
              default: ''
              description: The custom URL of the avatar
          required:
            - type
        - type: object
          properties:
            type:
              type: string
              enum:
                - image
              description: 'Discriminator value: image'
            url:
              type: string
              default: ''
              description: The URL of the avatar
          required:
            - type
      discriminator:
        propertyName: type
      description: The avatar of the widget
      title: WidgetConfigResponseAvatar
    type_:WidgetFeedbackMode:
      type: string
      enum:
        - none
        - during
        - end
      default: none
      title: WidgetFeedbackMode
    type_:WidgetEndFeedbackType:
      type: string
      enum:
        - rating
      title: WidgetEndFeedbackType
    type_:WidgetEndFeedbackConfig:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/type_:WidgetEndFeedbackType'
          description: The type of feedback to collect at the end of the conversation
      title: WidgetEndFeedbackConfig
    type_:AllowlistItem:
      type: object
      properties:
        hostname:
          type: string
          description: The hostname of the allowed origin
      required:
        - hostname
      title: AllowlistItem
    type_:WidgetConfigResponseSyntaxHighlightTheme:
      type: string
      enum:
        - light
        - dark
      title: WidgetConfigResponseSyntaxHighlightTheme
    type_:WidgetTextContents:
      type: object
      properties:
        main_label:
          type: string
          description: Call to action displayed inside the compact and full variants.
        start_call:
          type: string
          description: Text and ARIA label for the start call button.
        start_chat:
          type: string
          description: Text and ARIA label for the start chat button (text only)
        new_call:
          type: string
          description: >-
            Text and ARIA label for the new call button. Displayed when the
            caller already finished at least one call in order ot start the next
            one.
        end_call:
          type: string
          description: Text and ARIA label for the end call button.
        mute_microphone:
          type: string
          description: ARIA label for the mute microphone button.
        change_language:
          type: string
          description: ARIA label for the change language dropdown.
        collapse:
          type: string
          description: ARIA label for the collapse button.
        expand:
          type: string
          description: ARIA label for the expand button.
        copied:
          type: string
          description: Text displayed when the user copies a value using the copy button.
        accept_terms:
          type: string
          description: Text and ARIA label for the accept terms button.
        dismiss_terms:
          type: string
          description: Text and ARIA label for the cancel terms button.
        listening_status:
          type: string
          description: Status displayed when the agent is listening.
        speaking_status:
          type: string
          description: Status displayed when the agent is speaking.
        connecting_status:
          type: string
          description: Status displayed when the agent is connecting.
        chatting_status:
          type: string
          description: Status displayed when the agent is chatting (text only)
        input_label:
          type: string
          description: ARIA label for the text message input.
        input_placeholder:
          type: string
          description: Placeholder text for the text message input.
        input_placeholder_text_only:
          type: string
          description: Placeholder text for the text message input (text only)
        input_placeholder_new_conversation:
          type: string
          description: >-
            Placeholder text for the text message input when starting a new
            conversation (text only)
        user_ended_conversation:
          type: string
          description: Information message displayed when the user ends the conversation.
        agent_ended_conversation:
          type: string
          description: Information message displayed when the agent ends the conversation.
        conversation_id:
          type: string
          description: Text label used next to the conversation ID.
        error_occurred:
          type: string
          description: Text label used when an error occurs.
        copy_id:
          type: string
          description: Text and ARIA label used for the copy ID button.
        initiate_feedback:
          type: string
          description: Text displayed to prompt the user for feedback.
        request_follow_up_feedback:
          type: string
          description: Text displayed to request additional feedback details.
        thanks_for_feedback:
          type: string
          description: Text displayed to thank the user for providing feedback.
        thanks_for_feedback_details:
          type: string
          description: Additional text displayed explaining the value of user feedback.
        follow_up_feedback_placeholder:
          type: string
          description: Placeholder text for the follow-up feedback input field.
        submit:
          type: string
          description: Text and ARIA label for the submit button.
        go_back:
          type: string
          description: Text and ARIA label for the go back button.
        send_message:
          type: string
          description: Text and ARIA label for the send message button.
        text_mode:
          type: string
          description: Text and ARIA label for the switch to text mode button.
        voice_mode:
          type: string
          description: Text and ARIA label for the switch to voice mode button.
        switched_to_text_mode:
          type: string
          description: Toast notification displayed when switching to text mode.
        switched_to_voice_mode:
          type: string
          description: Toast notification displayed when switching to voice mode.
        copy:
          type: string
          description: Text and ARIA label for the copy button.
        download:
          type: string
          description: Text and ARIA label for the download button.
        wrap:
          type: string
          description: Text and ARIA label for the wrap toggle button.
        agent_working:
          type: string
          description: Status text displayed when the agent is processing a tool call.
        agent_done:
          type: string
          description: >-
            Status text displayed when the agent finishes processing a tool
            call.
        agent_error:
          type: string
          description: >-
            Status text displayed when the agent encounters an error during a
            tool call.
      title: WidgetTextContents
    type_:WidgetStyles:
      type: object
      properties:
        base:
          type: string
          description: The base background color.
        base_hover:
          type: string
          description: The color of the base background when hovered.
        base_active:
          type: string
          description: The color of the base background when active (clicked).
        base_border:
          type: string
          description: The color of the border against the base background.
        base_subtle:
          type: string
          description: The color of subtle text against the base background.
        base_primary:
          type: string
          description: The color of primary text against the base background.
        base_error:
          type: string
          description: The color of error text against the base background.
        accent:
          type: string
          description: The accent background color.
        accent_hover:
          type: string
          description: The color of the accent background when hovered.
        accent_active:
          type: string
          description: The color of the accent background when active (clicked).
        accent_border:
          type: string
          description: The color of the border against the accent background.
        accent_subtle:
          type: string
          description: The color of subtle text against the accent background.
        accent_primary:
          type: string
          description: The color of primary text against the accent background.
        overlay_padding:
          type: number
          format: double
          description: The padding around the edges of the viewport.
        button_radius:
          type: number
          format: double
          description: The radius of the buttons.
        input_radius:
          type: number
          format: double
          description: The radius of the input fields.
        bubble_radius:
          type: number
          format: double
          description: The radius of the chat bubbles.
        sheet_radius:
          type: number
          format: double
          description: The default radius of sheets.
        compact_sheet_radius:
          type: number
          format: double
          description: The radius of the sheet in compact mode.
        dropdown_sheet_radius:
          type: number
          format: double
          description: The radius of the dropdown sheet.
      title: WidgetStyles
    type_:WidgetLanguagePresetResponse:
      type: object
      properties:
        first_message:
          type: string
        text_contents:
          $ref: '#/components/schemas/type_:WidgetTextContents'
          description: The text contents for the selected language
        terms_text:
          type: string
          description: The text to display for terms and conditions in this language
        terms_html:
          type: string
          description: The HTML to display for terms and conditions in this language
        terms_key:
          type: string
          description: The key to display for terms and conditions in this language
      title: WidgetLanguagePresetResponse
    type_:FileInputConfig:
      type: object
      properties:
        enabled:
          type: boolean
          default: true
          description: >-
            When enabled, users may attach images or PDFs in chat when the LLM
            supports multimodal input.
        max_files_per_conversation:
          type: integer
          default: 10
          description: Maximum number of files that can be uploaded per conversation.
      title: FileInputConfig
    type_:WidgetConfigResponse:
      type: object
      properties:
        variant:
          $ref: '#/components/schemas/type_:EmbedVariant'
          description: The variant of the widget
        placement:
          $ref: '#/components/schemas/type_:WidgetPlacement'
          description: The placement of the widget on the screen
        expandable:
          $ref: '#/components/schemas/type_:WidgetExpandable'
          description: Whether the widget is expandable
        avatar:
          $ref: '#/components/schemas/type_:WidgetConfigResponseAvatar'
          description: The avatar of the widget
        feedback_mode:
          $ref: '#/components/schemas/type_:WidgetFeedbackMode'
          description: The feedback mode of the widget
        end_feedback:
          $ref: '#/components/schemas/type_:WidgetEndFeedbackConfig'
          description: Configuration for feedback collected at the end of the conversation
        bg_color:
          type: string
          default: '#ffffff'
          description: The background color of the widget
        text_color:
          type: string
          default: '#000000'
          description: The text color of the widget
        btn_color:
          type: string
          default: '#000000'
          description: The button color of the widget
        btn_text_color:
          type: string
          default: '#ffffff'
          description: The button text color of the widget
        border_color:
          type: string
          default: '#e1e1e1'
          description: The border color of the widget
        focus_color:
          type: string
          default: '#000000'
          description: The focus color of the widget
        border_radius:
          type: integer
          description: The border radius of the widget
        btn_radius:
          type: integer
          description: The button radius of the widget
        action_text:
          type: string
          description: The action text of the widget
        start_call_text:
          type: string
          description: The start call text of the widget
        end_call_text:
          type: string
          description: The end call text of the widget
        expand_text:
          type: string
          description: The expand text of the widget
        listening_text:
          type: string
          description: The text to display when the agent is listening
        speaking_text:
          type: string
          description: The text to display when the agent is speaking
        shareable_page_text:
          type: string
          description: The text to display when sharing
        shareable_page_show_terms:
          type: boolean
          default: true
          description: Whether to show terms and conditions on the shareable page
        terms_text:
          type: string
          description: The text to display for terms and conditions
        terms_html:
          type: string
          description: The HTML to display for terms and conditions
        terms_key:
          type: string
          description: The key to display for terms and conditions
        show_avatar_when_collapsed:
          type: boolean
          description: Whether to show the avatar when the widget is collapsed
        disable_banner:
          type: boolean
          default: false
          description: Whether to disable the banner
        override_link:
          type: string
          description: The override link for the widget
        markdown_link_allowed_hosts:
          type: array
          items:
            $ref: '#/components/schemas/type_:AllowlistItem'
          description: >-
            List of allowed hostnames for clickable markdown links. Use {
            hostname: '*' } to allow any domain. Empty means no links are
            allowed.
        markdown_link_include_www:
          type: boolean
          default: true
          description: Whether to automatically include www. variants of allowed hosts
        markdown_link_allow_http:
          type: boolean
          default: true
          description: Whether to allow http:// in addition to https:// for allowed hosts
        mic_muting_enabled:
          type: boolean
          default: false
          description: Whether to enable mic muting
        transcript_enabled:
          type: boolean
          default: false
          description: >-
            Whether the widget should show the conversation transcript as it
            goes on
        text_input_enabled:
          type: boolean
          default: true
          description: Whether the user should be able to send text messages
        conversation_mode_toggle_enabled:
          type: boolean
          default: false
          description: Whether to enable the conversation mode toggle in the widget
        default_expanded:
          type: boolean
          default: false
          description: Whether the widget should be expanded by default
        always_expanded:
          type: boolean
          default: false
          description: Whether the widget should always be expanded
        dismissible:
          type: boolean
          default: false
          description: Whether the widget can be dismissed by the user
        show_agent_status:
          type: boolean
          default: false
          description: Whether to show agent working/done/error status during tool use
        show_conversation_id:
          type: boolean
          default: true
          description: Whether to show the conversation ID after disconnection.
        strip_audio_tags:
          type: boolean
          default: true
          description: Whether to strip audio markup from messages.
        syntax_highlight_theme:
          $ref: '#/components/schemas/type_:WidgetConfigResponseSyntaxHighlightTheme'
          description: >-
            Theme for code block syntax highlighting. Defaults to auto-detection
            by the widget when not set.
        text_contents:
          $ref: '#/components/schemas/type_:WidgetTextContents'
          description: Text contents of the widget
        styles:
          $ref: '#/components/schemas/type_:WidgetStyles'
          description: Styles for the widget
        language:
          type: string
        supported_language_overrides:
          type: array
          items:
            type: string
        language_presets:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/type_:WidgetLanguagePresetResponse'
          description: Language presets for the widget
        text_only:
          type: boolean
          default: false
          description: Whether the agent uses text-only mode
        supports_text_only:
          type: boolean
          default: false
          description: Whether the agent can be switched to text-only mode
        first_message:
          type: string
        use_rtc:
          type: boolean
          description: Whether to use WebRTC for conversation connections
        file_input_config:
          $ref: '#/components/schemas/type_:FileInputConfig'
          description: Configuration for file upload in the widget
      required:
        - language
      title: WidgetConfigResponse
    type_:GetAgentEmbedResponseModel:
      type: object
      properties:
        agent_id:
          type: string
        widget_config:
          $ref: '#/components/schemas/type_:WidgetConfigResponse'
      required:
        - agent_id
        - widget_config
      title: GetAgentEmbedResponseModel
    type_:ValidationErrorLocItem:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItem
    type_:ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationErrorLocItem'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    type_:HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/type_:ValidationError'
      title: HTTPValidationError

```

## Examples

**Response**

```json
{
  "agent_id": "agent_id",
  "widget_config": {
    "language": "en",
    "variant": "tiny",
    "placement": "top-left",
    "expandable": "never",
    "avatar": {
      "type": "orb",
      "color_1": "#2792dc",
      "color_2": "#9ce6e6"
    },
    "feedback_mode": "none",
    "end_feedback": {
      "type": "rating"
    },
    "bg_color": "bg_color",
    "text_color": "text_color",
    "btn_color": "btn_color",
    "btn_text_color": "btn_text_color",
    "border_color": "border_color",
    "focus_color": "focus_color",
    "border_radius": 1,
    "btn_radius": 1,
    "action_text": "action_text",
    "start_call_text": "start_call_text",
    "end_call_text": "end_call_text",
    "expand_text": "expand_text",
    "listening_text": "listening_text",
    "speaking_text": "speaking_text",
    "shareable_page_text": "shareable_page_text",
    "shareable_page_show_terms": true,
    "terms_text": "terms_text",
    "terms_html": "terms_html",
    "terms_key": "terms_key",
    "show_avatar_when_collapsed": true,
    "disable_banner": true,
    "override_link": "override_link",
    "markdown_link_allowed_hosts": [
      {
        "hostname": "hostname"
      }
    ],
    "markdown_link_include_www": true,
    "markdown_link_allow_http": true,
    "mic_muting_enabled": true,
    "transcript_enabled": true,
    "text_input_enabled": true,
    "conversation_mode_toggle_enabled": true,
    "default_expanded": true,
    "always_expanded": true,
    "dismissible": true,
    "show_agent_status": true,
    "show_conversation_id": true,
    "strip_audio_tags": true,
    "syntax_highlight_theme": "light",
    "text_contents": {
      "main_label": "main_label",
      "start_call": "start_call",
      "start_chat": "start_chat",
      "new_call": "new_call",
      "end_call": "end_call",
      "mute_microphone": "mute_microphone",
      "change_language": "change_language",
      "collapse": "collapse",
      "expand": "expand",
      "copied": "copied",
      "accept_terms": "accept_terms",
      "dismiss_terms": "dismiss_terms",
      "listening_status": "listening_status",
      "speaking_status": "speaking_status",
      "connecting_status": "connecting_status",
      "chatting_status": "chatting_status",
      "input_label": "input_label",
      "input_placeholder": "input_placeholder",
      "input_placeholder_text_only": "input_placeholder_text_only",
      "input_placeholder_new_conversation": "input_placeholder_new_conversation",
      "user_ended_conversation": "user_ended_conversation",
      "agent_ended_conversation": "agent_ended_conversation",
      "conversation_id": "conversation_id",
      "error_occurred": "error_occurred",
      "copy_id": "copy_id",
      "initiate_feedback": "initiate_feedback",
      "request_follow_up_feedback": "request_follow_up_feedback",
      "thanks_for_feedback": "thanks_for_feedback",
      "thanks_for_feedback_details": "thanks_for_feedback_details",
      "follow_up_feedback_placeholder": "follow_up_feedback_placeholder",
      "submit": "submit",
      "go_back": "go_back",
      "send_message": "send_message",
      "text_mode": "text_mode",
      "voice_mode": "voice_mode",
      "switched_to_text_mode": "switched_to_text_mode",
      "switched_to_voice_mode": "switched_to_voice_mode",
      "copy": "copy",
      "download": "download",
      "wrap": "wrap",
      "agent_working": "agent_working",
      "agent_done": "agent_done",
      "agent_error": "agent_error"
    },
    "styles": {
      "base": "base",
      "base_hover": "base_hover",
      "base_active": "base_active",
      "base_border": "base_border",
      "base_subtle": "base_subtle",
      "base_primary": "base_primary",
      "base_error": "base_error",
      "accent": "accent",
      "accent_hover": "accent_hover",
      "accent_active": "accent_active",
      "accent_border": "accent_border",
      "accent_subtle": "accent_subtle",
      "accent_primary": "accent_primary",
      "overlay_padding": 1.1,
      "button_radius": 1.1,
      "input_radius": 1.1,
      "bubble_radius": 1.1,
      "sheet_radius": 1.1,
      "compact_sheet_radius": 1.1,
      "dropdown_sheet_radius": 1.1
    },
    "supported_language_overrides": [
      "es",
      "fr"
    ],
    "language_presets": {
      "key": {}
    },
    "text_only": false,
    "supports_text_only": true,
    "first_message": "Hello! How can I help you today?",
    "use_rtc": false,
    "file_input_config": {
      "enabled": false,
      "max_files_per_conversation": 10
    }
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.widget.get("agent_3701k3ttaq12ewp8b7qv5rfyszkz", {
        conversationSignature: "conversation_signature",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.widget.get(
    agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
    conversation_signature="conversation_signature",
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

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/widget?conversation_signature=conversation_signature"

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

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/widget?conversation_signature=conversation_signature")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/widget?conversation_signature=conversation_signature")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/widget?conversation_signature=conversation_signature');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/widget?conversation_signature=conversation_signature");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_3701k3ttaq12ewp8b7qv5rfyszkz/widget?conversation_signature=conversation_signature")! as URL,
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
