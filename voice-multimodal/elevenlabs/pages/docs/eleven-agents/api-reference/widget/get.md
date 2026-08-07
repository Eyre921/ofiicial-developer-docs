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

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Path parameters

- `agent_id` (string, required) — The id of an agent. This is returned on agent creation.

### Query parameters

- `conversation_signature` (string, optional) — An expiring token that enables a websocket conversation to start. These can be generated for an agent using the /v1/convai/conversation/get_signed_url endpoint

## Response

### 200

Successful Response

- `agent_id` (string, required)
- `widget_config` (object, required)
  - `language` (string, required)
  - `variant` (enum, optional, default: full) — The variant of the widget
    - Allowed values: `tiny`, `compact`, `full`, `expandable`
  - `placement` (enum, optional, default: bottom-right) — The placement of the widget on the screen
    - Allowed values: `top-left`, `top`, `top-right`, `bottom-left`, `bottom`, `bottom-right`
  - `expandable` (enum, optional, default: never) — Whether the widget is expandable
    - Allowed values: `never`, `mobile`, `desktop`, `always`
  - `avatar` (object, optional) — The avatar of the widget
    - `type`: `orb`
      - `color_1` (string, optional, default: #2792dc) — The first color of the avatar
      - `color_2` (string, optional, default: #9ce6e6) — The second color of the avatar
    - `type`: `url`
      - `custom_url` (string, optional, default: ) — The custom URL of the avatar
    - `type`: `image`
      - `url` (string, optional, default: ) — The URL of the avatar
  - `feedback_mode` (enum, optional, default: none) — The feedback mode of the widget
    - Allowed values: `none`, `during`, `end`
  - `end_feedback` (object, optional) — Configuration for feedback collected at the end of the conversation
    - `type` ("rating", optional) — The type of feedback to collect at the end of the conversation
  - `bg_color` (string, optional, default: #ffffff) — The background color of the widget
  - `text_color` (string, optional, default: #000000) — The text color of the widget
  - `btn_color` (string, optional, default: #000000) — The button color of the widget
  - `btn_text_color` (string, optional, default: #ffffff) — The button text color of the widget
  - `border_color` (string, optional, default: #e1e1e1) — The border color of the widget
  - `focus_color` (string, optional, default: #000000) — The focus color of the widget
  - `border_radius` (integer, optional) — The border radius of the widget
  - `btn_radius` (integer, optional) — The button radius of the widget
  - `action_text` (string, optional) — The action text of the widget
  - `start_call_text` (string, optional) — The start call text of the widget
  - `end_call_text` (string, optional) — The end call text of the widget
  - `expand_text` (string, optional) — The expand text of the widget
  - `listening_text` (string, optional) — The text to display when the agent is listening
  - `speaking_text` (string, optional) — The text to display when the agent is speaking
  - `shareable_page_text` (string, optional) — The text to display when sharing
  - `shareable_page_show_terms` (boolean, optional, default: true) — Whether to show terms and conditions on the shareable page
  - `terms_text` (string, optional) — The text to display for terms and conditions
  - `terms_html` (string, optional) — The HTML to display for terms and conditions
  - `terms_key` (string, optional) — The key to display for terms and conditions
  - `show_avatar_when_collapsed` (boolean, optional) — Whether to show the avatar when the widget is collapsed
  - `disable_banner` (boolean, optional, default: false) — Whether to disable the banner
  - `override_link` (string, optional) — The override link for the widget
  - `markdown_link_allowed_hosts` (list of object, optional) — List of allowed hostnames for clickable markdown links. Use \{ hostname: '\*' } to allow any domain. Empty means no links are allowed.
    - `hostname` (string, required) — The hostname of the allowed origin
  - `markdown_link_include_www` (boolean, optional, default: true) — Whether to automatically include www. variants of allowed hosts
  - `markdown_link_allow_http` (boolean, optional, default: true) — Whether to allow http:// in addition to https:// for allowed hosts
  - `mic_muting_enabled` (boolean, optional, default: false) — Whether to enable mic muting
  - `transcript_enabled` (boolean, optional, default: false) — Whether the widget should show the conversation transcript as it goes on
  - `text_input_enabled` (boolean, optional, default: true) — Whether the user should be able to send text messages
  - `conversation_mode_toggle_enabled` (boolean, optional, default: false) — Whether to enable the conversation mode toggle in the widget
  - `default_expanded` (boolean, optional, default: false) — Whether the widget should be expanded by default
  - `always_expanded` (boolean, optional, default: false) — Whether the widget should always be expanded
  - `dismissible` (boolean, optional, default: false) — Whether the widget can be dismissed by the user
  - `show_agent_status` (boolean, optional, default: false) — Whether to show agent working/done/error status during tool use
  - `show_conversation_id` (boolean, optional, default: true) — Whether to show the conversation ID after disconnection.
  - `strip_audio_tags` (boolean, optional, default: true) — Whether to strip audio markup from messages.
  - `syntax_highlight_theme` (enum, optional) — Theme for code block syntax highlighting. Defaults to auto-detection by the widget when not set.
    - Allowed values: `light`, `dark`
  - `text_contents` (object, optional) — Text contents of the widget
    - `main_label` (string, optional) — Call to action displayed inside the compact and full variants.
    - `start_call` (string, optional) — Text and ARIA label for the start call button.
    - `start_chat` (string, optional) — Text and ARIA label for the start chat button (text only)
    - `new_call` (string, optional) — Text and ARIA label for the new call button. Displayed when the caller already finished at least one call in order ot start the next one.
    - `end_call` (string, optional) — Text and ARIA label for the end call button.
    - `mute_microphone` (string, optional) — ARIA label for the mute microphone button.
    - `change_language` (string, optional) — ARIA label for the change language dropdown.
    - `collapse` (string, optional) — ARIA label for the collapse button.
    - `expand` (string, optional) — ARIA label for the expand button.
    - `copied` (string, optional) — Text displayed when the user copies a value using the copy button.
    - `accept_terms` (string, optional) — Text and ARIA label for the accept terms button.
    - `dismiss_terms` (string, optional) — Text and ARIA label for the cancel terms button.
    - `listening_status` (string, optional) — Status displayed when the agent is listening.
    - `speaking_status` (string, optional) — Status displayed when the agent is speaking.
    - `connecting_status` (string, optional) — Status displayed when the agent is connecting.
    - `chatting_status` (string, optional) — Status displayed when the agent is chatting (text only)
    - `input_label` (string, optional) — ARIA label for the text message input.
    - `input_placeholder` (string, optional) — Placeholder text for the text message input.
    - `input_placeholder_text_only` (string, optional) — Placeholder text for the text message input (text only)
    - `input_placeholder_new_conversation` (string, optional) — Placeholder text for the text message input when starting a new conversation (text only)
    - `user_ended_conversation` (string, optional) — Information message displayed when the user ends the conversation.
    - `agent_ended_conversation` (string, optional) — Information message displayed when the agent ends the conversation.
    - `conversation_id` (string, optional) — Text label used next to the conversation ID.
    - `error_occurred` (string, optional) — Text label used when an error occurs.
    - `copy_id` (string, optional) — Text and ARIA label used for the copy ID button.
    - `initiate_feedback` (string, optional) — Text displayed to prompt the user for feedback.
    - `request_follow_up_feedback` (string, optional) — Text displayed to request additional feedback details.
    - `thanks_for_feedback` (string, optional) — Text displayed to thank the user for providing feedback.
    - `thanks_for_feedback_details` (string, optional) — Additional text displayed explaining the value of user feedback.
    - `follow_up_feedback_placeholder` (string, optional) — Placeholder text for the follow-up feedback input field.
    - `submit` (string, optional) — Text and ARIA label for the submit button.
    - `go_back` (string, optional) — Text and ARIA label for the go back button.
    - `send_message` (string, optional) — Text and ARIA label for the send message button.
    - `text_mode` (string, optional) — Text and ARIA label for the switch to text mode button.
    - `voice_mode` (string, optional) — Text and ARIA label for the switch to voice mode button.
    - `switched_to_text_mode` (string, optional) — Toast notification displayed when switching to text mode.
    - `switched_to_voice_mode` (string, optional) — Toast notification displayed when switching to voice mode.
    - `copy` (string, optional) — Text and ARIA label for the copy button.
    - `download` (string, optional) — Text and ARIA label for the download button.
    - `wrap` (string, optional) — Text and ARIA label for the wrap toggle button.
    - `agent_working` (string, optional) — Status text displayed when the agent is processing a tool call.
    - `agent_done` (string, optional) — Status text displayed when the agent finishes processing a tool call.
    - `agent_error` (string, optional) — Status text displayed when the agent encounters an error during a tool call.
    - `attach_file` (string, optional) — Text and ARIA label for the attach file button.
    - `remove_file` (string, optional) — ARIA label for the remove file button.
    - `file_upload_error` (string, optional) — Error message displayed when a file fails to upload.
    - `file_type_unsupported` (string, optional) — Error message displayed when an unsupported file type is selected. Followed by the list of accepted types.
    - `file_too_large` (string, optional) — Error message displayed when a file exceeds the maximum size limit.
    - `file_limit_reached` (string, optional) — Error message displayed when the maximum number of files for a conversation is reached.
    - `typing_indicator` (string, optional) — Status text displayed while the agent is typing.
  - `styles` (object, optional) — Styles for the widget
    - `base` (string, optional) — The base background color.
    - `base_hover` (string, optional) — The color of the base background when hovered.
    - `base_active` (string, optional) — The color of the base background when active (clicked).
    - `base_border` (string, optional) — The color of the border against the base background.
    - `base_subtle` (string, optional) — The color of subtle text against the base background.
    - `base_primary` (string, optional) — The color of primary text against the base background.
    - `base_error` (string, optional) — The color of error text against the base background.
    - `accent` (string, optional) — The accent background color.
    - `accent_hover` (string, optional) — The color of the accent background when hovered.
    - `accent_active` (string, optional) — The color of the accent background when active (clicked).
    - `accent_border` (string, optional) — The color of the border against the accent background.
    - `accent_subtle` (string, optional) — The color of subtle text against the accent background.
    - `accent_primary` (string, optional) — The color of primary text against the accent background.
    - `overlay_padding` (double, optional) — The padding around the edges of the viewport.
    - `button_radius` (double, optional) — The radius of the buttons.
    - `input_radius` (double, optional) — The radius of the input fields.
    - `bubble_radius` (double, optional) — The radius of the chat bubbles.
    - `sheet_radius` (double, optional) — The default radius of sheets.
    - `compact_sheet_radius` (double, optional) — The radius of the sheet in compact mode.
    - `dropdown_sheet_radius` (double, optional) — The radius of the dropdown sheet.
  - `show_resize_button` (boolean, optional, default: true) — Whether to show the resize button
  - `supported_language_overrides` (list of string, optional)
  - `language_presets` (map from string to object, optional) — Language presets for the widget
    - `first_message` (string, optional)
    - `text_contents` (object, optional) — The text contents for the selected language
      - `main_label` (string, optional) — Call to action displayed inside the compact and full variants.
      - `start_call` (string, optional) — Text and ARIA label for the start call button.
      - `start_chat` (string, optional) — Text and ARIA label for the start chat button (text only)
      - `new_call` (string, optional) — Text and ARIA label for the new call button. Displayed when the caller already finished at least one call in order ot start the next one.
      - `end_call` (string, optional) — Text and ARIA label for the end call button.
      - `mute_microphone` (string, optional) — ARIA label for the mute microphone button.
      - `change_language` (string, optional) — ARIA label for the change language dropdown.
      - `collapse` (string, optional) — ARIA label for the collapse button.
      - `expand` (string, optional) — ARIA label for the expand button.
      - `copied` (string, optional) — Text displayed when the user copies a value using the copy button.
      - `accept_terms` (string, optional) — Text and ARIA label for the accept terms button.
      - `dismiss_terms` (string, optional) — Text and ARIA label for the cancel terms button.
      - `listening_status` (string, optional) — Status displayed when the agent is listening.
      - `speaking_status` (string, optional) — Status displayed when the agent is speaking.
      - `connecting_status` (string, optional) — Status displayed when the agent is connecting.
      - `chatting_status` (string, optional) — Status displayed when the agent is chatting (text only)
      - `input_label` (string, optional) — ARIA label for the text message input.
      - `input_placeholder` (string, optional) — Placeholder text for the text message input.
      - `input_placeholder_text_only` (string, optional) — Placeholder text for the text message input (text only)
      - `input_placeholder_new_conversation` (string, optional) — Placeholder text for the text message input when starting a new conversation (text only)
      - `user_ended_conversation` (string, optional) — Information message displayed when the user ends the conversation.
      - `agent_ended_conversation` (string, optional) — Information message displayed when the agent ends the conversation.
      - `conversation_id` (string, optional) — Text label used next to the conversation ID.
      - `error_occurred` (string, optional) — Text label used when an error occurs.
      - `copy_id` (string, optional) — Text and ARIA label used for the copy ID button.
      - `initiate_feedback` (string, optional) — Text displayed to prompt the user for feedback.
      - `request_follow_up_feedback` (string, optional) — Text displayed to request additional feedback details.
      - `thanks_for_feedback` (string, optional) — Text displayed to thank the user for providing feedback.
      - `thanks_for_feedback_details` (string, optional) — Additional text displayed explaining the value of user feedback.
      - `follow_up_feedback_placeholder` (string, optional) — Placeholder text for the follow-up feedback input field.
      - `submit` (string, optional) — Text and ARIA label for the submit button.
      - `go_back` (string, optional) — Text and ARIA label for the go back button.
      - `send_message` (string, optional) — Text and ARIA label for the send message button.
      - `text_mode` (string, optional) — Text and ARIA label for the switch to text mode button.
      - `voice_mode` (string, optional) — Text and ARIA label for the switch to voice mode button.
      - `switched_to_text_mode` (string, optional) — Toast notification displayed when switching to text mode.
      - `switched_to_voice_mode` (string, optional) — Toast notification displayed when switching to voice mode.
      - `copy` (string, optional) — Text and ARIA label for the copy button.
      - `download` (string, optional) — Text and ARIA label for the download button.
      - `wrap` (string, optional) — Text and ARIA label for the wrap toggle button.
      - `agent_working` (string, optional) — Status text displayed when the agent is processing a tool call.
      - `agent_done` (string, optional) — Status text displayed when the agent finishes processing a tool call.
      - `agent_error` (string, optional) — Status text displayed when the agent encounters an error during a tool call.
      - `attach_file` (string, optional) — Text and ARIA label for the attach file button.
      - `remove_file` (string, optional) — ARIA label for the remove file button.
      - `file_upload_error` (string, optional) — Error message displayed when a file fails to upload.
      - `file_type_unsupported` (string, optional) — Error message displayed when an unsupported file type is selected. Followed by the list of accepted types.
      - `file_too_large` (string, optional) — Error message displayed when a file exceeds the maximum size limit.
      - `file_limit_reached` (string, optional) — Error message displayed when the maximum number of files for a conversation is reached.
      - `typing_indicator` (string, optional) — Status text displayed while the agent is typing.
    - `terms_text` (string, optional) — The text to display for terms and conditions in this language
    - `terms_html` (string, optional) — The HTML to display for terms and conditions in this language
    - `terms_key` (string, optional) — The key to display for terms and conditions in this language
  - `text_only` (boolean, optional, default: false) — Whether the agent uses text-only mode
  - `supports_text_only` (boolean, optional, default: false) — Whether the agent can be switched to text-only mode
  - `first_message` (string, optional)
  - `use_rtc` (boolean, optional) — Whether to use WebRTC for conversation connections
  - `file_input_config` (object, optional) — Configuration for file upload in the widget
    - `enabled` (boolean, optional, default: true) — When enabled, users may attach images or PDFs in chat when the LLM supports multimodal input.
    - `max_files_in_memory` (integer, optional, default: 10) — Number of most-recent files kept in memory during a conversation. Older files are summarized and their bytes freed.
    - `max_files_per_conversation` (integer, optional, default: 10) — Total files a user can upload in one conversation. Uploads are billed per file. Use -1 for no limit, or a value >= max_files_in_memory.

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
      "agent_error": "agent_error",
      "attach_file": "attach_file",
      "remove_file": "remove_file",
      "file_upload_error": "file_upload_error",
      "file_type_unsupported": "file_type_unsupported",
      "file_too_large": "file_too_large",
      "file_limit_reached": "file_limit_reached",
      "typing_indicator": "typing_indicator"
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
    "show_resize_button": true,
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
      "max_files_in_memory": 10,
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
