---
title: "List voices"
source: https://elevenlabs.io/docs/api-reference/legacy/voices/get-all.md
path: docs/api-reference/legacy/voices/get-all
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# List voices

GET https://api.elevenlabs.io/v1/voices

Returns a list of all available voices for a user. Stops working once the user's workspace exceeds 500 voices.

Reference: https://elevenlabs.io/docs/api-reference/legacy/voices/get-all

## Servers

- `https://api.elevenlabs.io` (Production, default)
- `https://api.us.elevenlabs.io` (Production US)
- `https://api.eu.residency.elevenlabs.io` (Production EU)
- `https://api.in.residency.elevenlabs.io` (Production India)
- `https://api.sg.residency.elevenlabs.io` (Production Singapore)

## Request

### Query parameters

- `show_legacy` (boolean, optional, nullable, default: false) — If set to true, legacy premade voices will be included in responses from /v1/voices

## Response

### 200

Successful Response

- `voices` (list of object, required) — A list of available voices.
  - `voice_id` (string, required) — The ID of the voice.
  - `name` (string, optional) — The name of the voice.
  - `samples` (list of object, optional, nullable) — List of samples associated with the voice.
    - `sample_id` (string, optional) — The ID of the sample.
    - `file_name` (string, optional) — The name of the sample file.
    - `mime_type` (string, optional) — The MIME type of the sample file.
    - `size_bytes` (integer, optional) — The size of the sample file in bytes.
    - `hash` (string, optional) — The hash of the sample file.
    - `duration_secs` (double, optional, nullable)
    - `remove_background_noise` (boolean, optional, nullable)
    - `has_isolated_audio` (boolean, optional, nullable)
    - `has_isolated_audio_preview` (boolean, optional, nullable)
    - `speaker_separation` (object, optional, nullable)
      - `voice_id` (string, required) — The ID of the voice.
      - `sample_id` (string, required) — The ID of the sample.
      - `status` (enum, required) — The status of the speaker separation.
        - Allowed values: `not_started`, `pending`, `completed`, `failed`
      - `speakers` (map from string to object, optional, nullable) — The speakers of the sample.
        - `speaker_id` (string, required) — The ID of the speaker.
        - `duration_secs` (double, required) — The duration of the speaker segment in seconds.
        - `utterances` (list of object, optional, nullable) — The utterances of the speaker.
          - `start` (double, required) — The start time of the utterance in seconds.
          - `end` (double, required) — The end time of the utterance in seconds.
      - `selected_speaker_ids` (list of string, optional, nullable) — The IDs of the selected speakers.
    - `trim_start` (integer, optional, nullable)
    - `trim_end` (integer, optional, nullable)
  - `category` (enum, optional) — The category of the voice.
    - Allowed values: `generated`, `cloned`, `premade`, `professional`, `famous`, `high_quality`
  - `fine_tuning` (object, optional, nullable) — Fine-tuning information for the voice.
    - `is_allowed_to_fine_tune` (boolean, optional) — Whether the user is allowed to fine-tune the voice.
    - `state` (map from string to enum, optional) — The state of the fine-tuning process for each model.
      - Allowed values: `not_started`, `queued`, `fine_tuning`, `fine_tuned`, `failed`, `delayed`
    - `verification_failures` (list of string, optional) — List of verification failures in the fine-tuning process.
    - `verification_attempts_count` (integer, optional) — The number of verification attempts in the fine-tuning process.
    - `manual_verification_requested` (boolean, optional) — Whether a manual verification was requested for the fine-tuning process.
    - `language` (string, optional, nullable) — The language of the fine-tuning process.
    - `progress` (map from string to double, optional, nullable) — The progress of the fine-tuning process.
    - `message` (map from string to string, optional, nullable) — The message of the fine-tuning process.
    - `dataset_duration_seconds` (double, optional, nullable) — The duration of the dataset in seconds.
    - `verification_attempts` (list of object, optional, nullable) — The number of verification attempts.
      - `text` (string, required) — The text of the verification attempt.
      - `date_unix` (integer, required) — The date of the verification attempt in Unix time.
      - `accepted` (boolean, required) — Whether the verification attempt was accepted.
      - `similarity` (double, required) — The similarity of the verification attempt.
      - `levenshtein_distance` (double, required) — The Levenshtein distance of the verification attempt.
      - `recording` (object, optional, nullable) — The recording of the verification attempt.
        - `recording_id` (string, required) — The ID of the recording.
        - `mime_type` (string, required) — The MIME type of the recording.
        - `size_bytes` (integer, required) — The size of the recording in bytes.
        - `upload_date_unix` (integer, required) — The date of the recording in Unix time.
        - `transcription` (string, required) — The transcription of the recording.
    - `slice_ids` (list of string, optional, nullable) — List of slice IDs.
    - `manual_verification` (object, optional, nullable) — The manual verification of the fine-tuning process.
      - `extra_text` (string, required) — The extra text of the manual verification.
      - `request_time_unix` (integer, required) — The date of the manual verification in Unix time.
      - `files` (list of object, required) — The files of the manual verification.
        - `file_id` (string, required) — The ID of the file.
        - `file_name` (string, required) — The name of the file.
        - `mime_type` (string, required) — The MIME type of the file.
        - `size_bytes` (integer, required) — The size of the file in bytes.
        - `upload_date_unix` (integer, required) — The date of the file in Unix time.
    - `max_verification_attempts` (integer, optional, nullable) — The maximum number of verification attempts.
    - `next_max_verification_attempts_reset_unix_ms` (integer, optional, nullable) — The next maximum verification attempts reset time in Unix milliseconds.
    - `finetuning_state` (any, optional)
  - `labels` (map from string to string, optional) — Labels associated with the voice.
  - `description` (string, optional, nullable) — The description of the voice.
  - `preview_url` (string, optional, nullable) — The preview URL of the voice.
  - `available_for_tiers` (list of string, optional) — The tiers the voice is available for.
  - `settings` (object, optional, nullable) — The settings of the voice.
    - `stability` (double, optional, nullable, default: 0.5) — Determines how stable the voice is and the randomness between each generation. Lower values introduce broader emotional range for the voice. Higher values can result in a monotonous voice with limited emotion.
    - `use_speaker_boost` (boolean, optional, nullable, default: true) — This setting boosts the similarity to the original speaker. Using this setting requires a slightly higher computational load, which in turn increases latency.
    - `similarity_boost` (double, optional, nullable, default: 0.75) — Determines how closely the AI should adhere to the original voice when attempting to replicate it.
    - `style` (double, optional, nullable, default: 0) — Determines the style exaggeration of the voice. This setting attempts to amplify the style of the original speaker. It does consume additional computational resources and might increase latency if set to anything other than 0.
    - `speed` (double, optional, nullable, default: 1) — Adjusts the speed of the voice. A value of 1.0 is the default speed, while values less than 1.0 slow down the speech, and values greater than 1.0 speed it up.
  - `sharing` (object, optional, nullable) — The sharing information of the voice.
    - `status` (enum, optional) — The status of the voice sharing.
      - Allowed values: `enabled`, `disabled`, `copied`, `copied_disabled`
    - `history_item_sample_id` (string, optional, nullable) — The sample ID of the history item.
    - `date_unix` (integer, optional) — The date of the voice sharing in Unix time.
    - `whitelisted_emails` (list of string, optional) — A list of whitelisted emails.
    - `public_owner_id` (string, optional) — The ID of the public owner.
    - `original_voice_id` (string, optional) — The ID of the original voice.
    - `financial_rewards_enabled` (boolean, optional) — Whether financial rewards are enabled.
    - `free_users_allowed` (boolean, optional) — Whether free users are allowed.
    - `live_moderation_enabled` (boolean, optional) — Whether live moderation is enabled.
    - `rate` (double, optional, nullable) — The rate of the voice sharing.
    - `fiat_rate` (double, optional, nullable) — The rate of the voice sharing in USD per 1000 credits.
    - `notice_period` (integer, optional) — The notice period of the voice sharing.
    - `disable_at_unix` (integer, optional, nullable) — The date of the voice sharing in Unix time.
    - `voice_mixing_allowed` (boolean, optional) — Whether voice mixing is allowed.
    - `featured` (boolean, optional) — Whether the voice is featured.
    - `category` (enum, optional) — The category of the voice.
      - Allowed values: `generated`, `cloned`, `premade`, `professional`, `famous`, `high_quality`
    - `reader_app_enabled` (boolean, optional, nullable) — Whether the reader app is enabled.
    - `image_url` (string, optional, nullable) — The image URL of the voice.
    - `ban_reason` (string, optional, nullable) — The ban reason of the voice.
    - `liked_by_count` (integer, optional) — The number of likes on the voice.
    - `cloned_by_count` (integer, optional) — The number of clones on the voice.
    - `name` (string, optional) — The name of the voice.
    - `description` (string, optional, nullable) — The description of the voice.
    - `labels` (map from string to string, optional) — The labels of the voice.
    - `review_status` (enum, optional) — The review status of the voice.
      - Allowed values: `not_requested`, `pending`, `declined`, `allowed`, `allowed_with_changes`
    - `review_message` (string, optional, nullable) — The review message of the voice.
    - `enabled_in_library` (boolean, optional) — Whether the voice is enabled in the library.
    - `instagram_username` (string, optional, nullable) — The Instagram username of the voice.
    - `twitter_username` (string, optional, nullable) — The Twitter/X username of the voice.
    - `youtube_username` (string, optional, nullable) — The YouTube username of the voice.
    - `tiktok_username` (string, optional, nullable) — The TikTok username of the voice.
    - `moderation_check` (object, optional, nullable) — The moderation check of the voice.
      - `date_checked_unix` (integer, optional, nullable) — The date the moderation check was made in Unix time.
      - `name_value` (string, optional, nullable) — The name value of the voice.
      - `name_check` (boolean, optional, nullable) — Whether the name check was successful.
      - `description_value` (string, optional, nullable) — The description value of the voice.
      - `description_check` (boolean, optional, nullable) — Whether the description check was successful.
      - `sample_ids` (list of string, optional, nullable) — A list of sample IDs.
      - `sample_checks` (list of double, optional, nullable) — A list of sample checks.
      - `captcha_ids` (list of string, optional, nullable) — A list of captcha IDs.
      - `captcha_checks` (list of double, optional, nullable) — A list of CAPTCHA check values.
    - `reader_restricted_on` (list of object, optional, nullable) — The reader restricted on of the voice.
      - `resource_type` (enum, required) — The type of resource.
        - Allowed values: `read`, `collection`
      - `resource_id` (string, required) — The ID of the resource.
  - `high_quality_base_model_ids` (list of string, optional) — The base model IDs for high-quality voices.
  - `verified_languages` (list of object, optional, nullable) — The verified languages of the voice.
    - `language` (string, required) — The language of the voice.
    - `model_id` (string, required) — The voice's model ID.
    - `accent` (string, optional, nullable) — The voice's accent, if applicable.
    - `locale` (string, optional, nullable) — The voice's locale, if applicable.
    - `preview_url` (string, optional, nullable) — The voice's preview URL, if applicable.
  - `collection_ids` (list of string, optional, nullable) — The IDs of collections this voice belongs to.
  - `safety_control` (enum, optional, nullable) — The safety controls of the voice.
    - Allowed values: `NONE`, `BAN`, `CAPTCHA`, `ENTERPRISE_BAN`, `ENTERPRISE_CAPTCHA`
  - `voice_verification` (object, optional, nullable) — The voice verification of the voice.
    - `requires_verification` (boolean, required) — Whether the voice requires verification.
    - `is_verified` (boolean, required) — Whether the voice has been verified.
    - `verification_failures` (list of string, required) — List of verification failures.
    - `verification_attempts_count` (integer, required) — The number of verification attempts.
    - `language` (string, optional, nullable) — The language of the voice.
    - `verification_attempts` (list of object, optional, nullable) — Number of times a verification was attempted.
      - `text` (string, required) — The text of the verification attempt.
      - `date_unix` (integer, required) — The date of the verification attempt in Unix time.
      - `accepted` (boolean, required) — Whether the verification attempt was accepted.
      - `similarity` (double, required) — The similarity of the verification attempt.
      - `levenshtein_distance` (double, required) — The Levenshtein distance of the verification attempt.
      - `recording` (object, optional, nullable) — The recording of the verification attempt.
        - `recording_id` (string, required) — The ID of the recording.
        - `mime_type` (string, required) — The MIME type of the recording.
        - `size_bytes` (integer, required) — The size of the recording in bytes.
        - `upload_date_unix` (integer, required) — The date of the recording in Unix time.
        - `transcription` (string, required) — The transcription of the recording.
  - `permission_on_resource` (string, optional, nullable) — The permission on the resource of the voice.
  - `is_owner` (boolean, optional, nullable) — Whether the voice is owned by the user.
  - `is_legacy` (boolean, optional, default: false) — Whether the voice is legacy.
  - `is_mixed` (boolean, optional, default: false) — Whether the voice is mixed.
  - `favorited_at_unix` (integer, optional, nullable) — Timestamp when the voice was marked as favorite in Unix time.
  - `created_at_unix` (integer, optional, nullable) — The creation time of the voice in Unix time.
  - `is_bookmarked` (boolean, optional, nullable) — Whether the voice is bookmarked by the current user. Only relevant for community (library-copied) voices.
  - `recording_quality` (enum, optional, nullable) — The recording quality of the voice as determined by the review pipeline.
    - Allowed values: `studio`, `good`, `ok`, `poor`, `bad`
  - `labelling_status` (enum, optional, nullable) — The review pipeline status of the voice.
    - Allowed values: `in_review`, `review_complete`
  - `recording_quality_reason` (string, optional, nullable) — The reason for the recording quality assessment, as determined by the review pipeline.

## Examples

**Response**

```json
{
  "voices": [
    {
      "voice_id": "21m00Tcm4TlvDq8ikWAM",
      "name": "Rachel",
      "category": "professional",
      "fine_tuning": {
        "is_allowed_to_fine_tune": true,
        "state": {
          "eleven_multilingual_v2": "fine_tuned"
        },
        "verification_failures": [],
        "verification_attempts_count": 2,
        "manual_verification_requested": false
      },
      "labels": {
        "accent": "American",
        "age": "middle-aged",
        "description": "expressive",
        "gender": "female",
        "use_case": "social media"
      },
      "description": "A warm, expressive voice with a touch of humor.",
      "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/9BWtsMINqrJLrRacOk9x/405766b8-1f4e-4d3c-aba1-6f25333823ec.mp3",
      "available_for_tiers": [
        "creator",
        "enterprise"
      ],
      "settings": {
        "stability": 1,
        "use_speaker_boost": true,
        "similarity_boost": 1,
        "style": 0,
        "speed": 1
      },
      "sharing": {
        "status": "enabled",
        "history_item_sample_id": "DCwhRBWXzGAHq8TQ4Fs18",
        "date_unix": 1714204800,
        "whitelisted_emails": [
          "example@example.com"
        ],
        "public_owner_id": "DCwhRBWXzGAHq8TQ4Fs18",
        "original_voice_id": "DCwhRBWXzGAHq8TQ4Fs18",
        "financial_rewards_enabled": true,
        "free_users_allowed": true,
        "live_moderation_enabled": true,
        "rate": 0.05,
        "notice_period": 30,
        "disable_at_unix": 1714204800,
        "voice_mixing_allowed": false,
        "featured": true,
        "category": "professional",
        "reader_app_enabled": true,
        "liked_by_count": 100,
        "cloned_by_count": 50,
        "name": "Rachel",
        "description": "A female voice with a soft and friendly tone.",
        "labels": {
          "accent": "American",
          "gender": "female"
        },
        "review_status": "allowed",
        "enabled_in_library": true,
        "moderation_check": {
          "date_checked_unix": 1714204800,
          "name_value": "Rachel",
          "name_check": true,
          "description_value": "A female voice with a soft and friendly tone.",
          "description_check": true,
          "sample_ids": [
            "sample1",
            "sample2"
          ],
          "sample_checks": [
            0.95,
            0.98
          ],
          "captcha_ids": [
            "captcha1",
            "captcha2"
          ],
          "captcha_checks": [
            0.95,
            0.98
          ]
        },
        "reader_restricted_on": [
          {
            "resource_type": "read",
            "resource_id": "FCwhRBWXzGAHq8TQ4Fs18"
          }
        ]
      },
      "high_quality_base_model_ids": [
        "eleven_v2_flash",
        "eleven_flash_v2",
        "eleven_turbo_v2_5",
        "eleven_multilingual_v2",
        "eleven_v2_5_flash",
        "eleven_flash_v2_5",
        "eleven_turbo_v2"
      ],
      "verified_languages": [
        {
          "language": "en",
          "model_id": "eleven_multilingual_v2",
          "accent": "american",
          "locale": "en-US",
          "preview_url": "https://storage.googleapis.com/eleven-public-prod/premade/voices/9BWtsMINqrJLrRacOk9x/405766b8-1f4e-4d3c-aba1-6f25333823ec.mp3"
        }
      ],
      "voice_verification": {
        "requires_verification": false,
        "is_verified": true,
        "verification_failures": [],
        "verification_attempts_count": 0,
        "language": "en",
        "verification_attempts": [
          {
            "text": "Hello, how are you?",
            "date_unix": 1714204800,
            "accepted": true,
            "similarity": 0.95,
            "levenshtein_distance": 2,
            "recording": {
              "recording_id": "CwhRBWXzGAHq8TQ4Fs17",
              "mime_type": "audio/mpeg",
              "size_bytes": 1000000,
              "upload_date_unix": 1714204800,
              "transcription": "Hello, how are you?"
            }
          }
        ]
      },
      "is_owner": false,
      "is_legacy": false,
      "is_mixed": false
    }
  ]
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.getAll({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.get_all()

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/voices"

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

url = URI("https://api.elevenlabs.io/v1/voices")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/voices")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/voices');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices")! as URL,
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
